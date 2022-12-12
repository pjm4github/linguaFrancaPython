#!/usr/bin/env python
""" generated source for module CGenerator """
#  Generator for C target. 
# 
# Copyright (c) 2019-2021, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.generator.c

# import java.io.File
# import java.io.IOException
# import java.nio.file.Files
# import java.nio.file.Paths
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.concurrent.Executors
# import java.util.concurrent.TimeUnit
# import java.util.regex.Pattern
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.xbase.lib.Exceptions
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.IteratorExtensions
# import org.eclipse.xtext.xbase.lib.StringExtensions



# import com.google.common.base.Objects
# import com.google.common.collect.Iterables

# 
# Generator for C target. This class generates C code defining each reactor
# class given in the input .lf file and imported .lf files. The generated code
# has the following components:
# 
# A typedef for inputs, outputs, and actions of each reactor class. These
#   define the types of the variables that reactions use to access inputs and
#   action values and to set output values.
# 
# A typedef for a "self" struct for each reactor class. One instance of this
#   struct will be created for each reactor instance. See below for details.
# 
# A function definition for each reaction in each reactor class. These
#   functions take an instance of the self struct as an argument.
# 
# A constructor function for each reactor class. This is used to create
#   a new instance of the reactor.
# 
# After these, the main generated function is `_lf_initialize_trigger_objects()`.
# This function creates the instances of reactors (using their constructors)
# and makes connections between them.
# 
# A few other smaller functions are also generated.
# 
# ## Self Struct
# 
# The "self" struct has fields for each of the following:
# 
# parameter: the field name and type match the parameter.
# state: the field name and type match the state.
# action: the field name prepends the action name with "_lf_".
#   A second field for the action is also created to house the trigger_t object.
#   That second field prepends the action name with "_lf__".
# output: the field name prepends the output name with "_lf_".
# input:  the field name prepends the output name with "_lf_".
#   A second field for the input is also created to house the trigger_t object.
#   That second field prepends the input name with "_lf__".
# 
# If, in addition, the reactor contains other reactors and reacts to their outputs,
# then there will be a struct within the self struct for each such contained reactor.
# The name of that self struct will be the name of the contained reactor prepended with "_lf_".
# That inside struct will contain pointers the outputs of the contained reactors
# that are read together with pointers to booleans indicating whether those outputs are present.
# 
# If, in addition, the reactor has a reaction to shutdown, then there will be a pointer to
# trigger_t object (see reactor.h) for the shutdown event and an action struct named
# _lf_shutdown on the self struct.
# 
# ## Reaction Functions
# 
# For each reaction in a reactor class, this generator will produce a C function
# that expects a pointer to an instance of the "self" struct as an argument.
# This function will contain verbatim the C code specified in the reaction, but
# before that C code, the generator inserts a few lines of code that extract from the
# self struct the variables that that code has declared it will use. For example, if
# the reaction declares that it is triggered by or uses an input named "x" of type
# int, the function will contain a line like this:
# ```
#     r_x_t* x = self->_lf_x;
# ```
# where `r` is the full name of the reactor class and the struct type `r_x_t`
# will be defined like this:
# ```
#     typedef struct {
#         int value;
#         bool is_present;
#         int num_destinations;
#     } r_x_t;
# ```
# The above assumes the type of `x` is `int`.
# If the programmer fails to declare that it uses x, then the absence of the
# above code will trigger a compile error when the verbatim code attempts to read `x`.
# 
# ## Constructor
# 
# For each reactor class, this generator will create a constructor function named
# `new_r`, where `r` is the reactor class name. This function will malloc and return
# a pointer to an instance of the "self" struct.  This struct initially represents
# an unconnected reactor. To establish connections between reactors, additional
# information needs to be inserted (see below). The self struct is made visible
# to the body of a reaction as a variable named "self".  The self struct contains the
# following:
# 
# Parameters: For each parameter `p` of the reactor, there will be a field `p`
#   with the type and value of the parameter. So C code in the body of a reaction
#   can access parameter values as `self->p`.
# 
# State variables: For each state variable `s` of the reactor, there will be a field `s`
#   with the type and value of the state variable. So C code in the body of a reaction
#   can access state variables as as `self->s`.
# 
# The self struct also contains various fields that the user is not intended to
# use. The names of these fields begin with at least two underscores. They are:
# 
# Outputs: For each output named `out`, there will be a field `_lf_out` that is
#   a struct containing a value field whose type matches that of the output.
#   The output value is stored here. That struct also has a field `is_present`
#   that is a boolean indicating whether the output has been set.
#   This field is reset to false at the start of every time
#   step. There is also a field `num_destinations` whose value matches the
#   number of downstream reactors that use this variable. This field must be
#   set when connections are made or changed. It is used to initialize
#   reference counts for dynamically allocated message payloads.
#   The reference count is decremented in each destination reactor at the
#   conclusion of each time step, and when it drops to zero, the memory
#   is freed.
# 
# Inputs: For each input named `in` of type T, there is a field named `_lf_in`
#   that is a pointer struct with a value field of type T. The struct pointed
#   to also has an `is_present` field of type bool that indicates whether the
#   input is present.
# 
# Outputs of contained reactors: If a reactor reacts to outputs of a
#   contained reactor `r`, then the self struct will contain a nested struct
#   named `_lf_r` that has fields pointing to those outputs. For example,
#   if `r` has an output `out` of type T, then there will be field in `_lf_r`
#   named `out` that points to a struct containing a value field
#   of type T and a field named `is_present` of type bool.
# 
# Inputs of contained reactors: If a reactor sends to inputs of a
#   contained reactor `r`, then the self struct will contain a nested struct
#   named `_lf_r` that has fields for storing the values provided to those
#   inputs. For example, if R has an input `in` of type T, then there will
#   be field in _lf_R named `in` that is a struct with a value field
#   of type T and a field named `is_present` of type bool.
# 
# Actions: If the reactor has an action a (logical or physical), then there
#   will be a field in the self struct named `_lf_a` and another named `_lf__a`.
#   The type of the first is specific to the action and contains a `value`
#   field with the type and value of the action (if it has a value). That
#   struct also has a `has_value` field, an `is_present` field, and a
#   `token` field (which is NULL if the action carries no value).
#   The `_lf__a` field is of type trigger_t.
#   That struct contains various things, including an array of reactions
#   sensitive to this trigger and a lf_token_t struct containing the value of
#   the action, if it has a value.  See reactor.h in the C library for
#   details.
# 
# Reactions: Each reaction will have several fields in the self struct.
#   Each of these has a name that begins with `_lf__reaction_i`, where i is
#   the number of the reaction, starting with 0. The fields are:
#   * _lf__reaction_i: The struct that is put onto the reaction queue to
#     execute the reaction (see reactor.h in the C library).
# 
# Timers: For each timer t, there is are two fields in the self struct:
#    * _lf__t: The trigger_t struct for this timer (see reactor.h).
#    * _lf__t_reactions: An array of reactions (pointers to the
#      reaction_t structs on this self struct) sensitive to this timer.
# 
# Triggers: For each Timer, Action, Input, and Output of a contained
#   reactor that triggers reactions, there will be a trigger_t struct
#   on the self struct with name `_lf__t`, where t is the name of the trigger.
# 
# ## Connections Between Reactors
# 
# Establishing connections between reactors involves two steps.
# First, each destination (e.g. an input port) must have pointers to
# the source (the output port). As explained above, for an input named
# `in`, the field `_lf_in->value` is a pointer to the output data being read.
# In addition, `_lf_in->is_present` is a pointer to the corresponding
# `out->is_present` field of the output reactor's self struct.
# 
# In addition, the `reaction_i` struct on the self struct has a `triggers`
# field that records all the trigger_t structs for ports and actions
# that are triggered by the i-th reaction. The triggers field is
# an array of arrays of pointers to trigger_t structs.
# The length of the outer array is the number of output channels
# (single ports plus multiport widths) that the reaction effects
# plus the number of input port channels of contained
# reactors that it effects. Each inner array has a length equal to the
# number of final destinations of that output channel or input channel.
# The reaction_i struct has an array triggered_sizes that indicates
# the sizes of these inner arrays. The num_outputs field of the
# reaction_i struct gives the length of the triggered_sizes and
# (outer) triggers arrays. The num_outputs field is equal to the
# total number of single ports and multiport channels that the reaction
# writes to.
# 
# ## Runtime Tables
# 
# This generator creates an populates the following tables used at run time.
# These tables may have to be resized and adjusted when mutations occur.
# 
# _lf_is_present_fields: An array of pointers to booleans indicating whether an
#   event is present. The _lf_start_time_step() function in reactor_common.c uses
#   this to mark every event absent at the start of a time step. The size of this
#   table is contained in the variable _lf_is_present_fields_size.
#    * This table is accompanied by another list, _lf_is_present_fields_abbreviated,
#      which only contains the is_present fields that have been set to true in the
#      current tag. This list can allow a performance improvement if most ports are
#      seldom present because only fields that have been set to true need to be
#      reset to false.
# 
# _lf_tokens_with_ref_count: An array of pointers to structs that point to lf_token_t
#   objects, which carry non-primitive data types between reactors. This is used
#   by the _lf_start_time_step() function to decrement reference counts, if necessary,
#   at the conclusion of a time step. Then the reference count reaches zero, the
#   memory allocated for the lf_token_t object will be freed.  The size of this
#   array is stored in the _lf_tokens_with_ref_count_size variable.
# 
# _lf_shutdown_triggers: An array of pointers to trigger_t structs for shutdown
#   reactions. The length of this table is in the _lf_shutdown_triggers_size
#   variable.
# 
# _lf_timer_triggers: An array of pointers to trigger_t structs for timers that
#   need to be started when the program runs. The length of this table is in the
#   _lf_timer_triggers_size variable.
# 
# _lf_action_table: For a federated execution, each federate will have this table
#   that maps port IDs to the corresponding trigger_t struct.
# 
# @author {Edward A. Lee <eal@berkeley.edu>}
# @author {Marten Lohstroh <marten@berkeley.edu>}
# @author {Mehrdad Niknami <mniknami@berkeley.edu>}
# @author {Christian Menard <christian.menard@tu-dresden.de>}
# @author {Matt Weber <matt.weber@berkeley.edu>}
# @author {Soroush Bateni <soroush@utdallas.edu>}
# @author {Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
# @author {Hou Seng Wong <housengw@berkeley.edu>}
#
import os

from include.SpecialExceptions import RuntimeException
from include.overloading import overloaded
from lflang import FileConfig, ErrorReporter, ASTUtils, TargetProperty, Target
from lflang.TargetProperty import Platform, ClockSyncMode, CoordinationType
from lflang.TimeUnit import TimeUnit
from lflang.federated.FedFileConfig import FedFileConfig
from lflang.federated.launcher.FedCLauncher import FedCLauncher
from lflang.federated.serialization.FedROS2CPPSerialization import FedROS2CPPSerialization
from lflang.generator.GeneratorUtils import GeneratorUtils
from lflang.generator.IntegratedBuilder import IntegratedBuilder
from lflang.generator.GeneratorResult import GeneratorResult
import re
from lflang.generator.GeneratorBase import GeneratorBase

from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.PortInstance import PortInstance
from lflang.generator.ReactionInstance import Runtime
from lflang.generator.ReactorInstance import ReactorInstance
from lflang.generator.SubContext import SubContext
from lflang.generator.TriggerInstance import TriggerInstance
from lflang.generator.c import CUtil, CModesGenerator, CTimerGenerator, CReactionGenerator, CTriggerObjectsGenerator, \
    CFederateGenerator, CMethodGenerator, CConstructorGenerator, CPortGenerator, CActionGenerator, CParameterGenerator, \
    CStateGenerator, CNetworkGenerator, CPreambleGenerator, CCmakeCompiler, CCompiler, CDockerGenerator, \
    CMainGenerator, InteractingContainedReactors
from lflang.generator.c.CCmakeGenerator import CCmakeGenerator
from lflang.generator.c.CTypes import CTypes
from lflang.lf.ActionOrigin import ActionOrigin
from lflang.lf.Action import Action
from lflang.lf.Input import Input
from lflang.lf.Reactor import Reactor
from lflang.util.FileUtil import FileUtil


class StringExtensions:
    pass


class IteratorExtensions:
    pass


class Iterables:
    pass


class Executors:
    pass


class Exceptions:
    pass


class CGenerator(GeneratorBase):
    """ generated source for class CGenerator """
    @overloaded
    def __init__(self, fileConfig, errorReporter, CCppMode, types):
        """ generated source for method __init__ """
        super().__init__(fileConfig, errorReporter)
        self.CCppMode = CCppMode
        self.types = types
        self.fileConfig = fileConfig
        self.targetConfig = None
        #  Regular expression pattern for compiler error messages with resource
        #  and line number information. The first match will a resource URI in the
        #  form of "file:/path/file.lf". The second match will be a line number.
        #  The third match is a character position within the line.
        #  The fourth match will be the error message.
        self.compileErrorPattern = re.compile("^(file:(?P<path>.*)):(?P<line>[0-9]+):(?P<column>[0-9]+):(?P<message>.*)$")
        self.UNDEFINED_MIN_SPACING = -1

        # //////////////////////////////////////////
        # // Protected fields
        #  The main place to put generated code.
        self.code_ = CodeBuilder()

        #  The current federate for which we are generating code.
        self.currentFederate = None

        #  Place to collect code to initialize the trigger objects for all reactor instances.
        self.initializeTriggerObjects = CodeBuilder()

        # Count of the number of is_present fields of the self struct that
        # need to be reinitialized in _lf_start_time_step().
        #
        self.startTimeStepIsPresentCount = 0

        # //////////////////////////////////////////
        # // Private fields
        # Extra lines that need to go into the generated CMakeLists.txt.
        #
        self.cMakeExtras = ""

        #  Place to collect code to execute at the start of a time step.
        self.startTimeStep = CodeBuilder()

        #  Count of the number of token pointers that need to have their
        #  reference count decremented in _lf_start_time_step().
        #
        self.startTimeStepTokens = 0
        self.timerCount = 0
        self.startupReactionCount = 0
        self.shutdownReactionCount = 0
        self.resetReactionCount = 0
        self.modalReactorCount = 0
        self.modalStateResetCount = 0

    @__init__.register(object, FileConfig, ErrorReporter, bool)
    def __init___0(self, fileConfig, errorReporter, CCppMode):
        """ generated source for method __init___0 """
        super().__init__(fileConfig, errorReporter)
        self.__init__(fileConfig, errorReporter, CCppMode, CTypes(errorReporter))

    @__init__.register(object, FileConfig, ErrorReporter)
    def __init___1(self, fileConfig, errorReporter):
        """ generated source for method __init___1 """
        super().__init__(fileConfig, errorReporter)
        self.__init__(fileConfig, errorReporter, False)

    # //////////////////////////////////////////
    # // Public methods
    # Set C-specific default target configurations if needed.
    #       
    def setCSpecificDefaults(self):
        """ generated source for method setCSpecificDefaults """
        if not self.self.targetConfig.useCmake and self.targetConfig.compiler=="":
            if self.CCppMode:
                self.targetConfig.compiler = "g++"
                self.targetConfig.compilerFlags.extend(["-O2", "-Wno-write-strings"])
            else:
                self.targetConfig.compiler = "gcc"
                self.targetConfig.compilerFlags.append("-O2")
                #  "-Wall -Wconversion"
        if self.isFederated:
            #  Add compile definitions for federated execution
            self.targetConfig.compileDefinitions.put("FEDERATED", "")
            if self.targetConfig.coordination == CoordinationType.CENTRALIZED:
                #  The coordination is centralized.
                self.targetConfig.compileDefinitions.put("FEDERATED_CENTRALIZED", "")
            elif self.targetConfig.coordination == CoordinationType.DECENTRALIZED:
                #  The coordination is decentralized
                self.targetConfig.compileDefinitions.put("FEDERATED_DECENTRALIZED", "")

    # Look for physical actions in all resources.
    # If found, set threads to be at least one to allow asynchronous schedule calls.
    #       
    def accommodatePhysicalActionsIfPresent(self):
        """ generated source for method accommodatePhysicalActionsIfPresent """
        #  If there are any physical actions, ensure the threaded engine is used and that
        #  keepalive is set to true, unless the user has explicitly set it to false.
        for resource in GeneratorUtils.getResources(self.reactors):
            actions = [a for a in resource.getAllContents() if isinstance(a, Action.__class__)]
            for action in actions:
                if action.getOrigin() == ActionOrigin.PHYSICAL:
                    #  If the unthreaded runtime is not requested by the user, use the threaded runtime instead
                    #  because it is the only one currently capable of handling asynchronous events.
                    if not self.targetConfig.threading and not self.targetConfig.setByUser.contains(TargetProperty.THREADING):
                        self.targetConfig.threading = True
                        self.errorReporter.reportWarning(action, "Using the threaded C runtime to allow for asynchronous handling of physical action " + action.__name__)
                        return

    # Return true if the host operating system is compatible and
    # otherwise report an error and return false.
    #       
    def isOSCompatible(self):
        """ generated source for method isOSCompatible """
        if GeneratorUtils.isHostWindows():
            if self.isFederated:
                self.errorReporter.reportError("Federated LF programs with a C target are currently not supported on Windows. " + "Exiting code generation.")
                #  Return to avoid compiler errors
                return False
            if self.CCppMode:
                self.errorReporter.reportError("LF programs with a CCpp target are currently not supported on Windows. " + "Exiting code generation.")
                #  FIXME: The incompatibility between our C runtime code and the
                #   Visual Studio compiler is extensive.
                return False
            if not self.targetConfig.useCmake:
                self.errorReporter.reportError("Only CMake is supported as the build system on Windows. " + "Use `cmake: true` in the target properties. Exiting code generation.")
                return False
        return True

    # Generate C code from the Lingua Franca model contained by the
    # specified resource. This is the main entry point for code
    # generation.
    # @param resource The resource containing the source code.
    # @param context The context in which the generator is
    #     invoked, including whether it is cancelled and
    #     whether it is a standalone context
    #       
    def doGenerate(self, resource, context):
        """ generated source for method doGenerate """
        super().doGenerate(resource, context)
        if not GeneratorUtils.canGenerate(self.errorsOccurred(), self.mainDef, self.errorReporter, context):
            return
        if not self.isOSCompatible():
            return
        #  Incompatible OS and configuration
        #  Perform set up that does not generate code
        setUpGeneralParameters()
        commonCode = CodeBuilder(self.code_)
        #  Create the output directories if they don't yet exist.
        dir = self.fileConfig.getSrcGenPath().toFile()
        if not dir.exists():
            dir.mkdirs()
        dir = self.fileConfig.binPath.toFile()
        if not dir.exists():
            dir.mkdirs()
        #  Docker related paths
        dockerGenerator = self.getDockerGenerator()
        #  Keep a separate file config for each federate
        oldFileConfig = self.fileConfig
        numOfCompileThreads = min(6, min(max(len(self.federates), 1), Runtime.getRuntime().availableProcessors()))
        compileThreadPool = Executors.newFixedThreadPool(numOfCompileThreads)
        print("******** Using " + numOfCompileThreads + " threads to compile the program.")
        generatingContext = SubContext(context, IntegratedBuilder.VALIDATED_PERCENT_PROGRESS, IntegratedBuilder.GENERATED_PERCENT_PROGRESS)
        federateCount = 0
        for federate in self.federates:
            lfModuleName = self.fileConfig.name + "_" + federate.name if self.isFederated else self.fileConfig.name
            setUpFederateSpecificParameters(federate, commonCode)
            if self.isFederated:
                #  If federated, append the federate name to the file name.
                #  Only generate one output if there is no federation.
                try:
                    self.fileConfig = FedFileConfig(self.fileConfig, federate.name)
                except IOError as e:
                    Exceptions.sneakyThrow(e)
            generateCodeForCurrentFederate(lfModuleName)
            #  Derive target filename from the .lf filename.
            cFilename = CCompiler.getTargetFileName(lfModuleName, self.CCppMode)
            targetFile = self.fileConfig.getSrcGenPath() + File.separator + cFilename
            try:
                if self.isFederated:
                    #  Need to copy user files again since the source structure changes
                    #  for federated programs.
                    self.copyUserFiles(self.self.targetConfig, self.fileConfig)
                #  If we are running an Arduino Target, need to copy over the BoardOptions file.
                if self.targetConfig.platform == Platform.ARDUINO:
                    FileUtil.copyFile(FileUtil.globFilesEndsWith(self.fileConfig.srcPath, "BoardOptions.cmake").get(0), Paths.get(self.fileConfig.getSrcGenPath().__str__(), File.separator, "BoardOptions.cmake"))
                #  Copy the core lib
                FileUtil.copyFilesFromClassPath("/lib/c/reactor-c/core", self.fileConfig.getSrcGenPath().resolve("core"), CCoreFilesUtils.getCoreFiles(self.isFederated, self.targetConfig.threading, self.targetConfig.schedulerType))
                #  Copy the C target files
                self.copyTargetFiles()
                #  Write the generated code
                self.code_.writeToFile(targetFile)
            except IOError as e:
                Exceptions.sneakyThrow(e)
            #  Create docker file.
            if self.targetConfig.dockerOptions != None and self.mainDef != None:
                dockerGenerator.addFile(dockerGenerator.fromData(lfModuleName, federate.name, self.fileConfig))
            if self.targetConfig.useCmake:
                #  If cmake is requested, generated the CMakeLists.txt
                cmakeGenerator = CCmakeGenerator(self.targetConfig, self.fileConfig)
                cmakeFile = self.fileConfig.getSrcGenPath() + File.separator + "CMakeLists.txt"
                cmakeCode = cmakeGenerator.generateCMakeCode(list(cFilename), lfModuleName, self.errorReporter, self.CCppMode, self.mainDef != None, self.cMakeExtras)
                try:
                    cmakeCode.writeToFile(cmakeFile)
                except IOError as e:
                    Exceptions.sneakyThrow(e)
            #  If this code generator is directly compiling the code, compile it now so that we
            #  clean it up after, removing the #line directives after errors have been reported.
            if not self.targetConfig.noCompile and IterableExtensions.isNullOrEmpty(self.targetConfig.buildCommands) and not federate.isRemote and context.getMode() != LFGeneratorContext.Mode.LSP_MEDIUM:
                #  FIXME: Currently, a lack of main is treated as a request to not produce
                #  a binary and produce a .o file instead. There should be a way to control
                #  this.
                #  Create an anonymous Runnable class and add it to the compileThreadPool
                #  so that compilation can happen in parallel.
                cleanCode = self.code_.removeLines("#line")
                execName = lfModuleName
                threadFileConfig = self.fileConfig
                generator = self
                #  FIXME: currently only passed to report errors with line numbers in the Eclipse IDE
                CppMode = self.CCppMode
                federateCount += 1
                generatingContext.reportProgress("Generated code for {:d}/{:d} executables. Compiling...".format(federateCount, len(self.federates)), 100 * federateCount / len(self.federates))
                #                  compileThreadPool.execute(new Runnable() {
                #                      @Override
                #                      public void run() {
                #  Create the compiler to be used later
                cCompiler = CCompiler(self.targetConfig, threadFileConfig, self.errorReporter, CppMode)
                if self.targetConfig.useCmake:
                    #  Use CMake if requested.
                    cCompiler = CCmakeCompiler(self.targetConfig, threadFileConfig, self.errorReporter, CppMode)
                try:
                    if not cCompiler.runCCompiler(execName, self.main == None, generator, context):
                        #  If compilation failed, remove any bin files that may have been created.
                        CUtil.deleteBinFiles(threadFileConfig)
                        #  If finish has already been called, it is illegal and makes no sense. However,
                        #   if finish has already been called, then this must be a federated execution.
                        if not self.isFederated:
                            context.unsuccessfulFinish()
                    elif not self.isFederated:
                        context.finish(GeneratorResult.Status.COMPILED, execName, self.fileConfig, None)
                    cleanCode.writeToFile(targetFile)
                except IOError as e:
                    Exceptions.sneakyThrow(e)
                #                      }
                #                  });
            self.fileConfig = oldFileConfig
        #  Initiate an orderly shutdown in which previously submitted tasks are
        #  executed, but no new tasks will be accepted.
        compileThreadPool.shutdown()
        #  Wait for all compile threads to finish (NOTE: Can block forever)
        try:
            compileThreadPool.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS)
        except Exception as e:
            Exceptions.sneakyThrow(e)
        if self.isFederated:
            try:
                self.createFederatedLauncher()
            except IOError as e:
                Exceptions.sneakyThrow(e)
        if self.targetConfig.dockerOptions != None and self.mainDef != None:
            dockerGenerator.setHost(self.federationRTIProperties.get("host"))
            try:
                dockerGenerator.writeDockerFiles(self.fileConfig.getSrcGenPath().resolve("docker-compose.yml"))
            except IOError as e:
                raise RuntimeException(e)
        #  If a build directive has been given, invoke it now.
        #  Note that the code does not get cleaned in this case.
        if not self.targetConfig.noCompile:
            if not (self.targetConfig.buildCommands == None):
                CUtil.runBuildCommand(
                    self.fileConfig,
                    self.targetConfig,
                    self.commandFactory,
                    self.errorReporter,
                    self.reportCommandErrors(self),
                    context.getMode()
                )
                context.finish(
                    GeneratorResult.Status.COMPILED, self.fileConfig.name, self.fileConfig, None
                )
            elif self.isFederated:
                context.finish(GeneratorResult.Status.COMPILED, self.fileConfig.name, self.fileConfig, None)
            print("Compiled binary is in " + self.fileConfig.binPath)
        else:
            context.finish(GeneratorResult.GENERATED_NO_EXECUTABLE.apply(None))
        #  In case we are in Eclipse, make sure the generated code is visible.
        GeneratorUtils.refreshProject(resource, context.getMode())

    def generateCodeForCurrentFederate(self, lfModuleName):
        """ generated source for method generateCodeForCurrentFederate """
        self.startTimeStepIsPresentCount = 0
        self.startTimeStepTokens = 0
        self.code_.pr(generateDirectives())
        self.code_.pr(generateTopLevelPreambles())
        self.code_.pr(CMainGenerator(self.targetConfig).generateCode())
        #  Generate code for each reactor.
        self.generateReactorDefinitions()
        #  Generate main instance, if there is one.
        #  Note that any main reactors in imported files are ignored.
        #  Skip generation if there are cycles.
        if self.main != None:
            __actionTableCount_0 = self.actionTableCount
            self.actionTableCount += 1
            self.initializeTriggerObjects.pr("\n".join(["int _lf_startup_reactions_count = 0;", 
                                                        "SUPPRESS_UNUSED_WARNING(_lf_startup_reactions_count);", 
                                                        "int _lf_shutdown_reactions_count = 0;", 
                                                        "SUPPRESS_UNUSED_WARNING(_lf_shutdown_reactions_count);", 
                                                        "int _lf_reset_reactions_count = 0;", 
                                                        "SUPPRESS_UNUSED_WARNING(_lf_reset_reactions_count);", 
                                                        "int _lf_timer_triggers_count = 0;", 
                                                        "SUPPRESS_UNUSED_WARNING(_lf_timer_triggers_count);", 
                                                        "int _lf_tokens_with_ref_count_count = 0;", 
                                                        "SUPPRESS_UNUSED_WARNING(_lf_tokens_with_ref_count_count);", 
                                                        "int bank_index;", "SUPPRESS_UNUSED_WARNING(bank_index);"]))
            #  Add counters for modal initialization
            self.initializeTriggerObjects.pr(CModesGenerator.generateModalInitalizationCounters(self.hasModalReactors))
            #  Create an array of arrays to store all self structs.
            #  This is needed because connections cannot be established until
            #  all reactor instances have self structs because ports that
            #  receive data reference the self structs of the originating
            #  reactors, which are arbitarily far away in the program graph.
            generateSelfStructs(self.main)
            generateReactorInstance(self.main)
            #  If there are timers, create a table of timers to be initialized.
            self.code_.pr(CTimerGenerator.generateDeclarations(self.timerCount))
            #  If there are startup reactions, create a table of triggers.
            self.code_.pr(CReactionGenerator.generateBuiltinTriggersTable(self.startupReactionCount, "startup"))
            #  If there are shutdown reactions, create a table of triggers.
            self.code_.pr(CReactionGenerator.generateBuiltinTriggersTable(self.shutdownReactionCount, "shutdown"))
            #  If there are reset reactions, create a table of triggers.
            self.code_.pr(CReactionGenerator.generateBuiltinTriggersTable(self.resetReactionCount, "reset"))
            #  If there are modes, create a table of mode state to be checked for transitions.
            self.code_.pr(CModesGenerator.generateModeStatesTable(self.hasModalReactors, self.modalReactorCount, self.modalStateResetCount))
            #  Generate function to return a pointer to the action trigger_t
            #  that handles incoming network messages destined to the specified
            #  port. This will only be used if there are federates.
            if len(self.currentFederate.networkMessageActions) > 0:
                #  Create a static array of trigger_t pointers.
                #  networkMessageActions is a list of Actions, but we
                #  need a list of trigger struct names for ActionInstances.
                #  There should be exactly one ActionInstance in the
                #  main reactor for each Action.
                triggers = []
                for action in self.currentFederate.networkMessageActions:
                    #  Find the corresponding ActionInstance.
                    actionInstance = self.main.lookupActionInstance(action)
                    triggers.append(CUtil.triggerRef(actionInstance, None))
                actionTableCount = 0
                for trigger in triggers:
                    self.initializeTriggerObjects.pr("_lf_action_table[" + (__actionTableCount_0) + "] = &" + trigger + ";")
                self.code_.pr("\n".join(["trigger_t* _lf_action_table[" + len(self.currentFederate.networkMessageActions) + "];", 
                                         "trigger_t* _lf_action_for_port(int port_id) {", 
                                         "        if (port_id < " + len(self.currentFederate.networkMessageActions) + ") {", 
                                         "        return _lf_action_table[port_id];", 
                                         "        } else {", 
                                         "        return NULL;", 
                                         "        }", 
                                         "}"]))
            else:
                self.code_.pr("\n".join(["trigger_t* _lf_action_for_port(int port_id) {", 
                                         "        return NULL;", 
                                         "}"]))
            #  Generate function to initialize the trigger objects for all reactors.
            self.code_.pr(CTriggerObjectsGenerator.generateInitializeTriggerObjects(self.currentFederate, self.main, self.targetConfig, self.initializeTriggerObjects, self.startTimeStep, self.types, lfModuleName, federationRTIProperties, self.startTimeStepTokens, self.startTimeStepIsPresentCount, self.isFederated, self.isFederatedAndDecentralized(), clockSyncIsOn()))
            #  Generate function to trigger startup reactions for all reactors.
            self.code_.pr(CReactionGenerator.generateLfTriggerStartupReactions(self.startupReactionCount, self.hasModalReactors))
            #  Generate function to schedule timers for all reactors.
            self.code_.pr(CTimerGenerator.generateLfInitializeTimer(self.timerCount))
            #  Generate a function that will either do nothing
            #  (if there is only one federate or the coordination
            #  is set to decentralized) or, if there are
            #  downstream federates, will notify the RTI
            #  that the specified logical time is complete.
            self.code_.pr("\n".join(["void logical_tag_complete(tag_t tag_to_send) {", 
                                     ("        _lf_logical_tag_complete(tag_to_send);" if self.isFederatedAndCentralized() else ""), 
                                     "}"]))
            if self.isFederated:
                self.code_.pr(CFederateGenerator.generateFederateNeighborStructure(self.currentFederate))
            #  Generate function to schedule shutdown reactions if any
            #  reactors have reactions to shutdown.
            self.code_.pr(CReactionGenerator.generateLfTriggerShutdownReactions(self.shutdownReactionCount, self.hasModalReactors))
            #  Generate an empty termination function for non-federated
            #  execution. For federated execution, an implementation is
            #  provided in federate.c.  That implementation will resign
            #  from the federation and close any open sockets.
            if not self.isFederated:
                self.code_.pr("void terminate_execution() {}")
            #  Generate functions for modes
            self.code_.pr(CModesGenerator.generateLfInitializeModes(self.hasModalReactors))
            self.code_.pr(CModesGenerator.generateLfHandleModeChanges(self.hasModalReactors, self.modalStateResetCount))
            self.code_.pr(CReactionGenerator.generateLfModeTriggeredReactions(self.startupReactionCount, self.resetReactionCount, self.hasModalReactors))

    def getDockerGenerator(self):
        """ generated source for method getDockerGenerator """
        return CDockerGenerator(self.isFederated, self.CCppMode, self.targetConfig)

    def checkModalReactorSupport(self, __):
        """ generated source for method checkModalReactorSupport """
        #  Modal reactors are currently only supported for non federated applications
        super().checkModalReactorSupport(not self.isFederated)

    def getConflictingConnectionsInModalReactorsBody(self, source, dest):
        """ generated source for method getConflictingConnectionsInModalReactorsBody """
        return "\n".join(["// Generated forwarding reaction for connections with the same destination", 
                          "// but located in mutually exclusive modes.", 
                          "lf_set(" + dest + ", " + source + "->value);"])

    # Add files needed for the proper function of the runtime scheduler to
    # {@code coreFiles} and {@link TargetConfig#compileAdditionalSources}.
    #       
    def pickScheduler(self):
        """ generated source for method pickScheduler """
        #  Don't use a scheduler that does not prioritize reactions based on deadlines
        #  if the program contains a deadline (handler). Use the GEDF_NP scheduler instead.
        if not self.targetConfig.schedulerType.prioritizesDeadline():
            #  Check if a deadline is assigned to any reaction
            if self.hasDeadlines(reactors):
                if not self.targetConfig.setByUser.contains(TargetProperty.SCHEDULER):
                    self.targetConfig.schedulerType = TargetProperty.SchedulerOption.GEDF_NP
        self.targetConfig.compileAdditionalSources.append("core" + os.sep + "threaded" + os.sep + "scheduler_" + str(self.targetConfig.schedulerType) + ".c")
        print("******** Using the " + str(self.targetConfig.schedulerType) + " runtime scheduler.")
        self.targetConfig.compileAdditionalSources.append("core" + os.sep + "utils" + os.sep + "semaphore.c")

    def hasDeadlines(self, reactors):
        """ generated source for method hasDeadlines """
        for reactor in reactors:
            for reaction in self.allReactions(reactor):
                if reaction.getDeadline() != None:
                    return True
        return False

    # Look at the 'reactor' eResource.
    # If it is an imported .lf file, incorporate it into the current
    # program in the following manner:
    # - Merge its target property with `targetConfig`
    # - If there are any preambles, add them to the preambles of the reactor.
    #       
    def inspectReactorEResource(self, reactor):
        """ generated source for method inspectReactorEResource """
        #  If the reactor is imported, look at the
        #  target definition of the .lf file in which the reactor is imported from and
        #  append any cmake-include.
        #  Check if the reactor definition is imported
        if reactor.eResource() != self.mainDef.getReactorClass().eResource():
            #  Find the LFResource corresponding to this eResource
            lfResource = None
            for resource in self.resources:
                if resource.getEResource() == reactor.eResource():
                    lfResource = resource
                    break
            #  Copy the user files and cmake-includes to the src-gen path of the main .lf file
            if lfResource != None:
                self.copyUserFiles(lfResource.getTargetConfig(), lfResource.getFileConfig())
            #  Extract the contents of the imported file for the preambles
            contents = self.toDefinition(reactor).eResource().getContents()
            model = contents.get(0)
            self.toDefinition(reactor).getPreambles().addAll(model.getPreambles())

    def copyUserFiles(self, targetConfig, fileConfig):
        """ generated source for method copyUserFiles """
        super().copyUserFiles(targetConfig, fileConfig)
        targetDir = self.fileConfig.getSrcGenPath()
        try:
            Files.createDirectories(targetDir)
        except IOError as e:
            Exceptions.sneakyThrow(e)
        for filename in self.targetConfig.fileNames:
            relativeFileName = CUtil.copyFileOrResource(filename, self.fileConfig.srcFile.getParent(), targetDir)
            if StringExtensions.isNullOrEmpty(relativeFileName):
                self.errorReporter.reportError("Failed to find file " + filename + " specified in the" + " files target property.")
            else:
                self.targetConfig.filesNamesWithoutPath.append(relativeFileName)
        for filename in self.targetConfig.cmakeIncludes:
            relativeCMakeIncludeFileName = CUtil.copyFileOrResource(filename, self.fileConfig.srcFile.getParent(), targetDir)
            if StringExtensions.isNullOrEmpty(relativeCMakeIncludeFileName):
                self.errorReporter.reportError("Failed to find cmake-include file " + filename)
            else:
                self.self.targetConfig.cmakeIncludesWithoutPath.append(relativeCMakeIncludeFileName)

    def generateReactorDefinitions(self):
        """ generated source for method generateReactorDefinitions """
        generatedReactorDecls = {}
        if self.main != None:
            self.generateReactorChildren(self.main, generatedReactorDecls)
        if self.mainDef != None:
            self.generateReactorClass(self.mainDef.getReactorClass())
        if self.mainDef == None:
            for r in self.reactors:
                declarations = self.instantiationGraph.getDeclarations(r)
                if declarations.isEmpty():
                    self.generateReactorClass(r)

    def generateReactorChildren(self, reactor, generatedReactorDecls):
        """ generated source for method generateReactorChildren """
        for r in reactor.children:
            if self.currentFederate.contains(r) and r.reactorDeclaration != None and not generatedReactorDecls.contains(r.reactorDeclaration):
                generatedReactorDecls.append(r.reactorDeclaration)
                self.generateReactorChildren(r, generatedReactorDecls)
                self.inspectReactorEResource(r.reactorDeclaration)
                self.generateReactorClass(r.reactorDeclaration)

    def pickCompilePlatform(self):
        """ generated source for method pickCompilePlatform """
        osName = System.getProperty("os.name").lower()
        if self.targetConfig.platform != Platform.AUTO:
            osName = str(self.targetConfig.platform)
        if osName.contains("arduino"):
            return
        elif osName.contains("mac") or osName.contains("darwin"):
            if self.mainDef != None and not self.targetConfig.useCmake:
                self.targetConfig.compileAdditionalSources.append("core" + os.sep + "platform" + os.sep + "lf_macos_support.c")
        elif osName.contains("win"):
            if self.mainDef != None and not self.targetConfig.useCmake:
                self.targetConfig.compileAdditionalSources.append("core" + os.sep + "platform" + os.sep + "lf_windows_support.c")
        elif osName.contains("nux"):
            if self.mainDef != None and not self.targetConfig.useCmake:
                self.targetConfig.compileAdditionalSources.append("core" + os.sep + "platform" + os.sep + "lf_linux_support.c")
        else:
            self.errorReporter.reportError("Platform " + osName + " is not supported")

    def createFederatedLauncher(self):
        """ generated source for method createFederatedLauncher """
        launcher = FedCLauncher(self.targetConfig, self.fileConfig, self.errorReporter)
        launcher.createLauncher(self.federates, self.federationRTIProperties)

    def clockSyncIsOn(self):
        """ generated source for method clockSyncIsOn """
        return self.targetConfig.clockSync != ClockSyncMode.OFF and (not self.federationRTIProperties.get("host").__str__() == self.currentFederate.host or self.targetConfig.clockSyncOptions.localFederatesOn)

    def initializeClockSynchronization(self):
        """ generated source for method initializeClockSynchronization """
        if self.clockSyncIsOn():
            print("Initial clock synchronization is enabled for federate " + self.currentFederate.id)
            if self.targetConfig.clockSync == ClockSyncMode.ON:
                if self.targetConfig.clockSyncOptions.collectStats:
                    print("Will collect clock sync statistics for federate " + self.currentFederate.id)
                    self.targetConfig.compilerFlags.append("-lm")
                print("Runtime clock synchronization is enabled for federate " + self.currentFederate.id)

    def copyTargetFiles(self):
        """ generated source for method copyTargetFiles """
        FileUtil.copyDirectoryFromClassPath("/lib/c/reactor-c/include", self.fileConfig.getSrcGenPath().resolve("include"), False)
        FileUtil.copyDirectoryFromClassPath("/lib/c/reactor-c/lib", self.fileConfig.getSrcGenPath().resolve("lib"), False)

    def generateReactorClass(self, reactor):
        """ generated source for method generateReactorClass """
        defn = ASTUtils.toDefinition(reactor)
        if isinstance(reactor, Reactor):
            self.code_.pr("// =============== START reactor class " + reactor.__name__)
        else:
            self.code_.pr("// =============== START reactor class " + defn.__name__ + " as " + reactor.__name__)
        self.generateUserPreamblesForReactor(defn)
        constructorCode = CodeBuilder()
        self.generateAuxiliaryStructs(reactor)
        self.generateSelfStruct(reactor, constructorCode)
        self.generateMethods(reactor)
        generateReactions(reactor, self.currentFederate)
        self.generateConstructor(reactor, self.currentFederate, constructorCode)
        self.code_.pr("// =============== END reactor class " + reactor.__name__)
        self.code_.pr("")

    def generateMethods(self, reactor):
        """ generated source for method generateMethods """
        CMethodGenerator.generateMethods(reactor, self.code_, self.types)

    def generateUserPreamblesForReactor(self, reactor):
        """ generated source for method generateUserPreamblesForReactor """
        for p in convertToEmptyListIfNull(reactor.getPreambles()):
            self.code_.pr("// *********** From the preamble, verbatim:")
            self.code_.prSourceLineNumber(p.getCode())
            self.code_.pr(toText(p.getCode()))
            self.code_.pr("\n// *********** End of preamble.")

    def generateConstructor(self, reactor, federate, constructorCode):
        """ generated source for method generateConstructor """
        self.code_.pr(CConstructorGenerator.generateConstructor(reactor, federate, str(constructorCode)))

    def generateAuxiliaryStructs(self, decl):
        """ generated source for method generateAuxiliaryStructs """
        reactor = ASTUtils.toDefinition(decl)
        federatedExtension = CodeBuilder()
        if self.isFederatedAndDecentralized():
            federatedExtension.pr(self.types.getTargetTagType() + " intended_tag;")
        if self.isFederated:
            federatedExtension.pr(self.types.getTargetTimeType() + " physical_time_of_arrival;")
        for input in allInputs(reactor):
            self.code_.pr(CPortGenerator.generateAuxiliaryStruct(decl, input, getTarget(), self.errorReporter, self.types, federatedExtension))
        for output in allOutputs(reactor):
            self.code_.pr(CPortGenerator.generateAuxiliaryStruct(decl, output, getTarget(), self.errorReporter, self.types, federatedExtension))
        for action in allActions(reactor):
            if self.currentFederate.contains(action):
                self.code_.pr(CActionGenerator.generateAuxiliaryStruct(decl, action, getTarget(), self.types, federatedExtension))

    def generateSelfStruct(self, decl, constructorCode):
        """ generated source for method generateSelfStruct """
        reactor = self.toDefinition(decl)
        selfType = CUtil.selfType(decl)
        body = CodeBuilder()
        generateSelfStructExtension(body, decl, constructorCode)
        body.pr(CParameterGenerator.generateDeclarations(reactor, self.types))
        body.pr(CStateGenerator.generateDeclarations(reactor, self.types))
        CActionGenerator.generateDeclarations(reactor, decl, self.currentFederate, body, constructorCode)
        CPortGenerator.generateDeclarations(reactor, decl, body, constructorCode)
        self.generateInteractingContainedReactors(reactor, body, constructorCode)
        CReactionGenerator.generateReactionAndTriggerStructs(self.currentFederate, body, decl, constructorCode, self.types, self.isFederated, self.isFederatedAndDecentralized())
        CModesGenerator.generateDeclarations(reactor, body, constructorCode)
        self.code_.pr("typedef struct {")
        self.code_.indent()
        self.code_.pr("struct self_base_t base;")
        self.code_.pr(body.__str__())
        self.code_.unindent()
        self.code_.pr("} " + selfType + ";")

    def generateInteractingContainedReactors(self, reactor, body, constructorCode):
        """ generated source for method generateInteractingContainedReactors """
        contained = InteractingContainedReactors(reactor, self.currentFederate)
        for containedReactor in contained.containedReactors():
        __triggeredCount_1 = triggeredCount
        triggeredCount += 1
            array = ""
            width = -2
            if containedReactor.getWidthSpec() != None:
                width = CReactionGenerator.maxContainedReactorBankWidth(containedReactor, None, 0, self.mainDef)
                array = "[" + width + "]"
            constructorCode.pr("\n".join(["// Set the _width variable for all cases. This will be -2", 
                                          "// if the reactor is not a bank of reactors.", 
                                          "self->_lf_" + containedReactor.__name__ + "_width = " + width + ";"]))
            body.pr("struct {")
            body.indent()
            for port in contained.portsOfInstance(containedReactor):
                if isinstance(port, (Input)):
                    if not ASTUtils.isMultiport(port):
                        body.pr(port, variableStructType(port, containedReactor.getReactorClass()) + " " + port.__name__ + ";")
                    else:
                        body.pr(port, "\n".join([variableStructType(port, containedReactor.getReactorClass()) + "** " + port.__name__ + ";", 
                                                 "int " + port.__name__ + "_width;"]))
                else:
                    if not ASTUtils.isMultiport(port):
                        body.pr(port, variableStructType(port, containedReactor.getReactorClass()) + "* " + port.__name__ + ";")
                    else:
                        body.pr(port, "\n".join([variableStructType(port, containedReactor.getReactorClass()) + "** " + port.__name__ + ";",
                                                 "int " + port.__name__ + "_width;"]))
                    body.pr(port, "trigger_t " + port.__name__ + "_trigger;")
                    reactorIndex = ""
                    if containedReactor.getWidthSpec() != None:
                        reactorIndex = "[reactor_index]"
                        constructorCode.pr("for (int reactor_index = 0; reactor_index < self->_lf_" + containedReactor.__name__ + "_width; reactor_index++) {")
                        constructorCode.indent()
                    portOnSelf = "self->_lf_" + containedReactor.__name__ + reactorIndex + "." + port.__name__
                    if self.isFederatedAndDecentralized():
                        constructorCode.pr(port, portOnSelf + "_trigger.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};")
                    triggered = contained.reactionsTriggered(containedReactor, port)
                    if len(triggered) > 0:
                        body.pr(port, "reaction_t* " + port.__name__ + "_reactions[" + len(triggered) + "];")
                        triggeredCount = 0
                        for index in triggered:
                            constructorCode.pr(port, portOnSelf + "_reactions[" + __triggeredCount_1 + "] = &self->_lf__reaction_" + index + ";")
                        constructorCode.pr(port, portOnSelf + "_trigger.reactions = " + portOnSelf + "_reactions;")
                    else:
                        pass
                    constructorCode.pr(port, "\n".join([portOnSelf + "_trigger.last = NULL;", 
                                                        portOnSelf + "_trigger.number_of_reactions = " + len(triggered) + ";"]))
                    if self.isFederated:
                        constructorCode.pr(port, portOnSelf + "_trigger.physical_time_of_arrival = NEVER;")
                    if containedReactor.getWidthSpec() != None:
                        constructorCode.unindent()
                        constructorCode.pr("}")
            body.unindent()
            body.pr("\n".join(["} _lf_" + containedReactor.__name__ + array + ";", 
                               "int _lf_" + containedReactor.__name__ + "_width;"]))

    def generateSelfStructExtension(self, body, decl, constructorCode):
        """ generated source for method generateSelfStructExtension """

    def generateReactions(self, decl, federate):
        """ generated source for method generateReactions """
        reactionIndex = 0
        reactor = ASTUtils.toDefinition(decl)
        for reaction in self.allReactions(reactor):
            if federate == None or federate.contains(reaction):
                generateReaction(reaction, decl, reactionIndex)
            reactionIndex += 1

    def generateReaction(self, reaction, decl, reactionIndex):
        """ generated source for method generateReaction """
        self.code_.pr(CReactionGenerator.generateReaction(reaction, decl, reactionIndex, 
                                                          self.mainDef, self.errorReporter, self.types,
                                                          self.isFederatedAndDecentralized(),
                                                          getTarget().requiresTypes))

    def recordBuiltinTriggers(self, instance):
        """ generated source for method recordBuiltinTriggers """
        for reaction in instance.reactions:
            if self.currentFederate.contains(reaction.getDefinition()):
                reactor = reaction.getParent()
                temp = CodeBuilder()
                foundOne = False
                reactionRef = CUtil.reactionRef(reaction)
                for trigger in reaction.triggers:
                    if trigger.isStartup():
                        temp.pr("_lf_startup_reactions[_lf_startup_reactions_count++] = &" + reactionRef + ";")
                        self.startupReactionCount += self.currentFederate.numRuntimeInstances(reactor)
                        foundOne = True
                    elif trigger.isShutdown():
                        temp.pr("_lf_shutdown_reactions[_lf_shutdown_reactions_count++] = &" + reactionRef + ";")
                        foundOne = True
                        self.shutdownReactionCount += self.currentFederate.numRuntimeInstances(reactor)
                        if self.targetConfig.tracing != None:
                            description = CUtil.getShortenedName(reactor)
                            reactorRef = CUtil.reactorRef(reactor)
                            temp.pr("\n".join(["_lf_register_trace_event(" + reactorRef + ", &(" + reactorRef + "->_lf__shutdown),", 
                                               "trace_trigger, " + addDoubleQuotes(description + ".shutdown") + ");"]))
                    elif trigger.isReset():
                        temp.pr("_lf_reset_reactions[_lf_reset_reactions_count++] = &" + reactionRef + ";")
                        self.resetReactionCount += self.currentFederate.numRuntimeInstances(reactor)
                        foundOne = True
                if foundOne:
                    self.initializeTriggerObjects.pr(temp.__str__())

    def generateStartTimeStep(self, instance):
        """ generated source for method generateStartTimeStep """
        for child in instance.children:
            if self.currentFederate.contains(child) and len(child.inputs) > 0:
                foundOne = False
                temp = CodeBuilder()
                temp.startScopedBlock(child, self.currentFederate, self.isFederated, True)
                for input in child.inputs:
                    if CUtil.isTokenType(getInferredType((input.getDefinition())), self.types):
                        foundOne = True
                        temp.pr(CPortGenerator.initializeStartTimeStepTableForInput(input))
                        self.startTimeStepTokens += self.currentFederate.numRuntimeInstances(input.getParent()) * input.getWidth()
                temp.endScopedBlock()
                if foundOne:
                    self.startTimeStep.pr(temp.__str__())
        foundOne = False
        temp = CodeBuilder()
        containerSelfStructName = CUtil.reactorRef(instance)
        portsSeen = {}
        for reaction in instance.reactions:
            if self.currentFederate.contains(reaction.getDefinition()):
                for port in Iterables.filter(reaction.effects, PortInstance.__class__):
                    if isinstance(port, Input) and not portsSeen.contains(port):
                        portsSeen.append(port)
                        if self.currentFederate.contains(port.getParent()):
                            foundOne = True
                            temp.pr("// Add port " + port.getFullName() + " to array of is_present fields.")
                            if not Objects.equal(port.getParent(), instance):
                                temp.startScopedBlock()
                                temp.pr("int count = 0; SUPPRESS_UNUSED_WARNING(count);")
                                temp.startScopedBlock(instance, self.currentFederate, self.isFederated, True)
                                temp.startScopedBankChannelIteration(port, self.currentFederate, None, self.isFederated)
                            else:
                                temp.startScopedBankChannelIteration(port, self.currentFederate, "count", self.isFederated)
                            portRef = CUtil.portRefNested(port)
                            con = "->" if (port.isMultiport()) else "."
                            temp.pr("_lf_is_present_fields[" + self.startTimeStepIsPresentCount + " + count] = &" + portRef + con + "is_present;")
                            if self.isFederatedAndDecentralized():
                                temp.pr("_lf_intended_tag_fields[" + self.startTimeStepIsPresentCount + " + count] = &" + portRef + con + "intended_tag;")
                            self.startTimeStepIsPresentCount += port.getWidth() * self.currentFederate.numRuntimeInstances(port.getParent())
                            if not Objects.equal(port.getParent(), instance):
                                temp.pr("count++;")
                                temp.endScopedBlock()
                                temp.endScopedBlock()
                                temp.endScopedBankChannelIteration(port, None)
                            else:
                                temp.endScopedBankChannelIteration(port, "count")
                for port in Iterables.filter(reaction.sources, PortInstance.__class__):
                    if port.isOutput() and not portsSeen.contains(port):
                        portsSeen.append(port)
                        if CUtil.isTokenType(ASTUtils.getInferredType((port.getDefinition())), self.types):
                            foundOne = True
                            temp.pr("// Add port " + port.getFullName() + " to array _lf_tokens_with_ref_count.")
                            temp.startScopedBlock(instance, self.currentFederate, self.isFederated, True)
                            temp.startScopedBankChannelIteration(port, self.currentFederate, "count", self.isFederated)
                            portRef = CUtil.portRef(port, True, True, None, None, None)
                            temp.pr(CPortGenerator.initializeStartTimeStepTableForPort(portRef))
                            self.startTimeStepTokens += port.getWidth() * self.currentFederate.numRuntimeInstances(port.getParent())
                            temp.endScopedBankChannelIteration(port, "count")
                            temp.endScopedBlock()
        if foundOne:
            self.startTimeStep.pr(temp.__str__())
        temp = CodeBuilder()
        foundOne = False
        for action in instance.actions:
            if self.currentFederate == None or self.currentFederate.contains(action.getDefinition()):
                foundOne = True
                temp.startScopedBlock(instance, self.currentFederate, self.isFederated, True)
                temp.pr("\n".join(["// Add action " + action.getFullName() + " to array of is_present fields.", 
                                   "_lf_is_present_fields[" + self.startTimeStepIsPresentCount + "] ",                                    
                                   "        = &" + containerSelfStructName + "->_lf_" + action.__name__ + ".is_present;"]))
                if self.isFederatedAndDecentralized():
                    temp.pr("\n".join(["// Add action " + action.getFullName() + " to array of intended_tag fields.", 
                                       "_lf_intended_tag_fields[" + self.startTimeStepIsPresentCount + "] ", 
                                       "        = &" + containerSelfStructName + "->_lf_" + action.__name__ + ".intended_tag;"]))
                self.startTimeStepIsPresentCount += self.currentFederate.numRuntimeInstances(action.getParent())
                temp.endScopedBlock()
        if foundOne:
            self.startTimeStep.pr(temp.__str__())
        temp = CodeBuilder()
        foundOne = False
        for child in instance.children:
            if self.currentFederate.contains(child) and len(child.outputs) > 0:
                temp.startScopedBlock()
                temp.pr("int count = 0; SUPPRESS_UNUSED_WARNING(count);")
                temp.startScopedBlock(child, self.currentFederate, self.isFederated, True)
                channelCount = 0
                for output in child.outputs:
                    if not output.getDependsOnReactions().isEmpty():
                        foundOne = True
                        temp.pr("// Add port " + output.getFullName() + " to array of is_present fields.")
                        temp.startChannelIteration(output)
                        temp.pr("_lf_is_present_fields[" + self.startTimeStepIsPresentCount + " + count] = &" + CUtil.portRef(output) + ".is_present;")
                        if self.isFederatedAndDecentralized():
                            temp.pr("\n".join(["// Add port " + output.getFullName() + " to array of intended_tag fields.", 
                                               "_lf_intended_tag_fields[" + self.startTimeStepIsPresentCount + " + count] = &" + CUtil.portRef(output) + ".intended_tag;"]))
                        temp.pr("count++;")
                        channelCount += output.getWidth()
                        temp.endChannelIteration(output)
                self.startTimeStepIsPresentCount += channelCount * self.currentFederate.numRuntimeInstances(child)
                temp.endScopedBlock()
                temp.endScopedBlock()
        if foundOne:
            self.startTimeStep.pr(temp.__str__())

    def generateTimerInitializations(self, instance):
        """ generated source for method generateTimerInitializations """
        for timer in instance.timers:
            if self.currentFederate.contains(timer.getDefinition()):
                if not timer.isStartup():
                    self.initializeTriggerObjects.pr(CTimerGenerator.generateInitializer(timer))
                    self.timerCount += self.currentFederate.numRuntimeInstances(timer.getParent())

    def processProtoFile(self, filename, cancelIndicator):
        """ generated source for method processProtoFile """
        protoc = self.commandFactory.createCommand("protoc-c", list("--c_out=" + self.fileConfig.getSrcGenPath(), filename), self.fileConfig.srcPath)
        if protoc == None:
            self.errorReporter.reportError("Processing .proto files requires proto-c >= 1.3.3.")
            return
        returnCode = protoc.run(cancelIndicator)
        if returnCode == 0:
            nameSansProto = filename.substring(0, 6 - len(filename))
            self.targetConfig.compileAdditionalSources.append(self.fileConfig.getSrcGenPath().resolve(nameSansProto + ".pb-c.c").__str__())
            self.targetConfig.compileLibraries.append("-l")
            self.targetConfig.compileLibraries.append("protobuf-c")
            self.targetConfig.compilerFlags.append("-lprotobuf-c")
        else:
            self.errorReporter.reportError("protoc-c returns error code " + returnCode)

    @classmethod
    @overloaded
    def variableStructType(cls, variable, reactor):
        """ generated source for method variableStructType """
        return reactor.__name__.lower() + "_" + variable.__name__ + "_t"

    @classmethod
    @variableStructType.register(object, TriggerInstance)
    def variableStructType_0(cls, portOrAction):
        """ generated source for method variableStructType_0 """
        return portOrAction.getParent().reactorDeclaration.__name__.lower() + "_" + portOrAction.__name__ + "_t"

    @classmethod
    def getHeapPortMember(cls, portName, member):
        """ generated source for method getHeapPortMember """
        return portName + "->" + member

    @classmethod
    def getStackStructOperator(cls):
        """ generated source for method getStackStructOperator """
        return "."

    def generateTraceTableEntries(self, instance):
        """ generated source for method generateTraceTableEntries """
        if self.targetConfig.tracing != None:
            self.initializeTriggerObjects.pr(CTracingGenerator.generateTraceTableEntries(instance, self.currentFederate))

    def generateReactorInstance(self, instance):
        """ generated source for method generateReactorInstance """
        reactorClass = instance.getDefinition().getReactorClass()
        fullName = instance.getFullName()
        self.initializeTriggerObjects.pr("// ***** Start initializing " + fullName + " of class " + reactorClass.__name__)
        self.initializeTriggerObjects.pr(CUtil.reactorRefName(instance) + "[" + CUtil.runtimeIndex(instance) + "] = new_" + reactorClass.__name__ + "();")
        self.generateTraceTableEntries(instance)
        generateReactorInstanceExtension(instance)
        generateParameterInitialization(instance)
        initializeOutputMultiports(instance)
        initializeInputMultiports(instance)
        self.recordBuiltinTriggers(instance)
        generateStateVariableInitializations(instance)
        self.generateTimerInitializations(instance)
        generateActionInitializations(instance)
        generateInitializeActionToken(instance)
        generateSetDeadline(instance)
        generateModeStructure(instance)
        for child in instance.children:
            if self.currentFederate.contains(child):
                self.startTimeStep.startScopedBlock(child, self.currentFederate, self.isFederated, True)
                self.initializeTriggerObjects.startScopedBlock(child, self.currentFederate, self.isFederated, True)
                self.generateReactorInstance(child)
                self.initializeTriggerObjects.endScopedBlock()
                self.startTimeStep.endScopedBlock()
        if self.isFederatedAndCentralized() and instance.getParent() == self.main:
            outputDelayMap = self.currentFederate.findOutputsConnectedToPhysicalActions(instance)
            minDelay = TimeValue.MAX_VALUE
            outputFound = None
            for output in outputDelayMap.keySet():
                outputDelay = outputDelayMap.get(output)
                if outputDelay.isEarlierThan(minDelay):
                    minDelay = outputDelay
                    outputFound = output
            if minDelay != TimeValue.MAX_VALUE:
                if self.targetConfig.coordinationOptions.advance_message_interval == None:
                    self.errorReporter.reportWarning(outputFound, "\n".join(
                        ["Found a path from a physical action to output for reactor " + addDoubleQuotes(instance.__name__) + ". ", 
                         "The amount of delay is " + minDelay + ".", 
                         "With centralized coordination, this can result in a large number of messages to the RTI.", 
                         "Consider refactoring the code so that the output does not depend on the physical action,", 
                         "or consider using decentralized coordination. To silence this warning, set the target", 
                         "parameter coordination-options with a value like {advance-message-interval: 10 msec}"]))
                self.initializeTriggerObjects.pr("_fed.min_delay_from_physical_action_to_federate_output = " + GeneratorBase.timeInTargetLanguage(minDelay) + ";")
        self.generateStartTimeStep(instance)
        self.initializeTriggerObjects.pr("//***** End initializing " + fullName)

    def generateActionInitializations(self, instance):
        """ generated source for method generateActionInitializations """
        self.initializeTriggerObjects.pr(CActionGenerator.generateInitializers(instance, self.currentFederate))

    def generateInitializeActionToken(self, reactor):
        """ generated source for method generateInitializeActionToken """
        for action in reactor.actions:
            if action.getParent().getTriggers().contains(action) and self.currentFederate.contains(action.getDefinition()):
                type = getInferredType(action.getDefinition())
                payloadSize = "0"
                if not type.isUndefined():
                    typeStr = self.types.getTargetType(type)
                    if CUtil.isTokenType(type, self.types):
                        typeStr = CUtil.rootType(typeStr)
                    if typeStr != None and not typeStr == "" and not typeStr == "void":
                        payloadSize = "sizeof(" + typeStr + ")"
                selfStruct = CUtil.reactorRef(action.getParent())
                self.initializeTriggerObjects.pr(CActionGenerator.generateTokenInitializer(selfStruct, action.__name__, payloadSize))
                self.startTimeStepTokens += self.currentFederate.numRuntimeInstances(action.getParent())

    def generateReactorInstanceExtension(self, instance):
        """ generated source for method generateReactorInstanceExtension """

    def generateStateVariableInitializations(self, instance):
        """ generated source for method generateStateVariableInitializations """
        reactorClass = instance.getDefinition().getReactorClass()
        selfRef = CUtil.reactorRef(instance)
        for stateVar in allStateVars(self.toDefinition(reactorClass)):
            if isInitialized(stateVar):
                mode = instance.lookupModeInstance(stateVar.eContainer()) if isinstance(, (Mode)) else instance.getMode(False)
                self.initializeTriggerObjects.pr(CStateGenerator.generateInitializer(instance, selfRef, stateVar, mode, self.types))
                if mode != None and stateVar.isReset():
                    self.modalStateResetCount += self.currentFederate.numRuntimeInstances(instance)

    def generateSetDeadline(self, instance):
        """ generated source for method generateSetDeadline """
        for reaction in instance.reactions:
            if self.currentFederate.contains(reaction.getDefinition()):
                selfRef = CUtil.reactorRef(reaction.getParent()) + "->_lf__reaction_" + reaction.index
                if reaction.declaredDeadline != None:
                    deadline = reaction.declaredDeadline.maxDelay
                    self.initializeTriggerObjects.pr(selfRef + ".deadline = " + GeneratorBase.timeInTargetLanguage(deadline) + ";")
                else:
                    self.initializeTriggerObjects.pr(selfRef + ".deadline = NEVER;")

    def generateModeStructure(self, instance):
        """ generated source for method generateModeStructure """
        CModesGenerator.generateModeStructure(instance, self.initializeTriggerObjects)
        if not instance.modes.isEmpty():
            self.modalReactorCount += self.currentFederate.numRuntimeInstances(instance)

    def generateParameterInitialization(self, instance):
        """ generated source for method generateParameterInitialization """
        selfRef = CUtil.reactorRef(instance)
        self.initializeTriggerObjects.pr("bank_index = " + CUtil.bankIndex(instance) + ";" + " SUPPRESS_UNUSED_WARNING(bank_index);")
        for parameter in instance.parameters:
            initializer = CParameterGenerator.getInitializer(parameter)
            if initializer.startsWith("{"):
                temporaryVariableName = parameter.uniqueID()
                self.initializeTriggerObjects.pr("\n".join([
                    "static " + self.types.getVariableDeclaration(parameter.type, temporaryVariableName, True) + " = " + initializer + ";", 
                    selfRef + "->" + parameter.__name__ + " = " + temporaryVariableName + ";"]))
            else:
                self.initializeTriggerObjects.pr(selfRef + "->" + parameter.__name__ + " = " + initializer + ";")

    def initializeOutputMultiports(self, reactor):
        """ generated source for method initializeOutputMultiports """
        reactorSelfStruct = CUtil.reactorRef(reactor)
        for output in reactor.outputs:
            self.initializeTriggerObjects.pr(CPortGenerator.initializeOutputMultiport(output, reactorSelfStruct))

    def initializeInputMultiports(self, reactor):
        """ generated source for method initializeInputMultiports """
        reactorSelfStruct = CUtil.reactorRef(reactor)
        for input in reactor.inputs:
            self.initializeTriggerObjects.pr(CPortGenerator.initializeInputMultiport(input, reactorSelfStruct))

    def multiportWidthSpecInC(self, port, contained, reactorInstance):
        """ generated source for method multiportWidthSpecInC """
        result = ""
        count = 0
        selfRef = "self"
        if reactorInstance != None:
            if contained != None:
                selfRef = CUtil.reactorRef(reactorInstance.getChildReactorInstance(contained))
            else:
                selfRef = CUtil.reactorRef(reactorInstance)
        if port.getWidthSpec() != None:
            if not port.getWidthSpec().isOfVariableLength():
                for term in port.getWidthSpec().getTerms():
                    if term.getParameter() != None:
                        result.append(selfRef)
                        result.append("->")
                        result.append(term.getParameter().__name__)
                    else:
                        count += term.getWidth()
        if count > 0:
            if 0 > len(result):
                result.append(" + ")
            result.append(count)
        return result.__str__()

    def getTargetTypes(self):
        """ generated source for method getTargetTypes """
        return self.types

    def setUpGeneralParameters(self):
        """ generated source for method setUpGeneralParameters """
        self.accommodatePhysicalActionsIfPresent()
        self.targetConfig.compileDefinitions.put("LOG_LEVEL", self.targetConfig.logLevel.ordinal() + "")
        self.targetConfig.compileAdditionalSources.addAll(CCoreFilesUtils.getCTargetSrc())
        self.targetConfig.compileAdditionalSources.append("core" + os.sep + "mixed_radix.c")
        self.setCSpecificDefaults()
        createMainReactorInstance()
        if self.isFederated:
            self.targetConfig.threading = True
            self.targetConfig.compileDefinitions.put("WORKERS_NEEDED_FOR_FEDERATE", CUtil.minThreadsToHandleInputPorts(self.federates) + "")
        if self.hasModalReactors:
            self.targetConfig.compileDefinitions.put("MODAL_REACTORS", "")
        if self.targetConfig.threading and self.targetConfig.platform == Platform.ARDUINO:
            if self.targetConfig.setByUser.contains(TargetProperty.THREADING):
                self.errorReporter.reportWarning("Threading is incompatible on Arduino. Setting threading to false.")
            self.targetConfig.threading = False
        if self.targetConfig.threading:
            self.pickScheduler()
        self.pickCompilePlatform()

    def setUpFederateSpecificParameters(self, federate, commonCode):
        """ generated source for method setUpFederateSpecificParameters """
        self.currentFederate = federate
        if self.isFederated:
            self.targetConfig.cmakeIncludes.clear()
            self.targetConfig.cmakeIncludesWithoutPath.clear()
            self.targetConfig.fileNames.clear()
            self.targetConfig.filesNamesWithoutPath.clear()
            target = GeneratorUtils.findTarget(mainDef.getReactorClass().eResource())
            if target.getConfig() != None:
                TargetProperty.updateOne(self.self.targetConfig, 
                                         TargetProperty.CMAKE_INCLUDE, 
                                         convertToEmptyListIfNull(target.getConfig().getPairs()), 
                                         self.errorReporter)
                TargetProperty.updateOne(self.self.targetConfig, 
                                         TargetProperty.FILES, 
                                         convertToEmptyListIfNull(target.getConfig().getPairs()), 
                                         self.errorReporter)
            self.code_ = CodeBuilder(commonCode)
            self.initializeTriggerObjects = CodeBuilder()
            self.initializeClockSynchronization()
            self.startTimeStep = CodeBuilder()

    def generateDelayBody(self, action, port):
        """ generated source for method generateDelayBody """
        ref = ASTUtils.generateVarRef(port)
        return CReactionGenerator.generateDelayBody(ref, 
                                                    action.__name__, 
                                                    CUtil.isTokenType(getInferredType(action), self.types)
                                                    )

    def generateForwardBody(self, action, port):
        """ generated source for method generateForwardBody """
        outputName = ASTUtils.generateVarRef(port)
        return CReactionGenerator.generateForwardBody(outputName, 
                                                      self.types.getTargetType(action), 
                                                      action.__name__, 
                                                      CUtil.isTokenType(getInferredType(action), self.types)
                                                      )

    def generateNetworkReceiverBody(self, action, sendingPort, receivingPort, receivingPortID, 
                                    sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, 
                                    type, isPhysical, serializer):
        """ generated source for method generateNetworkReceiverBody """
        return CNetworkGenerator.generateNetworkReceiverBody(action, sendingPort, receivingPort, receivingPortID,
                                                             sendingFed, receivingFed, receivingBankIndex, 
                                                             receivingChannelIndex, type, isPhysical, serializer, 
                                                             self.types, self.targetConfig.coordination)

    def generateNetworkSenderBody(self, sendingPort, receivingPort, receivingPortID, sendingFed, 
                                  sendingBankIndex, sendingChannelIndex, receivingFed, 
                                  type, isPhysical, delay, serializer):
        """ generated source for method generateNetworkSenderBody """
        return CNetworkGenerator.generateNetworkSenderBody(sendingPort, receivingPort, receivingPortID, 
                                                           sendingFed, sendingBankIndex, sendingChannelIndex, 
                                                           receivingFed, type, isPhysical, delay, serializer, 
                                                           self.types, self.targetConfig.coordination)

    def generateNetworkInputControlReactionBody(self, receivingPortID, maxSTP):
        """ generated source for method generateNetworkInputControlReactionBody """
        return CNetworkGenerator.generateNetworkInputControlReactionBody(receivingPortID, maxSTP, 
                                                                         self.isFederatedAndDecentralized())

    def generateNetworkOutputControlReactionBody(self, port, portID, receivingFederateID, sendingBankIndex, 
                                                 sendingChannelIndex, delay):
        """ generated source for method generateNetworkOutputControlReactionBody """
        return CNetworkGenerator.generateNetworkOutputControlReactionBody(port, portID, receivingFederateID, 
                                                                          sendingBankIndex, sendingChannelIndex, delay)

    def enableSupportForSerializationIfApplicable(self, cancelIndicator):
        """ generated source for method enableSupportForSerializationIfApplicable """
        if not IterableExtensions.isNullOrEmpty(self.targetConfig.protoFiles):
            enabledSerializers.append(SupportedSerializers.PROTO)
        for serializer in enabledSerializers:
            if serializer == NATIVE:
            elif serializer == PROTO:
                for file in self.targetConfig.protoFiles:
                    self.processProtoFile(file, cancelIndicator)
                    dotIndex = file.lastIndexOf(".")
                    rootFilename = file
                    if dotIndex > 0:
                        rootFilename = file.substring(0, dotIndex)
                    self.code_.pr("#include " + addDoubleQuotes(rootFilename + ".pb-c.h"))
            elif serializer == ROS2:
                if not self.CCppMode:
                    raise TypeError("To use the ROS 2 serializer, please use the CCpp target.")
                if not self.targetConfig.useCmake:
                    raise TypeError("Invalid target property \"cmake: false\"" + "To use the ROS 2 serializer, please use the CMake build system (default)")
                ROSSerializer = FedROS2CPPSerialization()
                self.code_.pr(ROSSerializer.generatePreambleForSupport().__str__())
                self.cMakeExtras = "\n".join([self.cMakeExtras, ROSSerializer.generateCompilerExtensionForSupport()])

    def generateDirectives(self):
        """ generated source for method generateDirectives """
        code_ = CodeBuilder()
        code_.prComment("Code generated by the Lingua Franca compiler from:")
        code_.prComment("file:/" + FileUtil.toUnixString(self.fileConfig.srcFile))
        code_.pr(CPreambleGenerator.generateDefineDirectives(self.targetConfig, len(self.federates), self.isFederated, self.fileConfig.getSrcGenPath(), self.clockSyncIsOn(), self.hasModalReactors))
        code_.pr(CPreambleGenerator.generateIncludeStatements(self.targetConfig, self.isFederated))
        return code_.__str__()

    def generateTopLevelPreambles(self):
        """ generated source for method generateTopLevelPreambles """
        code_ = CodeBuilder()
        if self.mainDef != None:
            mainModel = self.toDefinition(mainDef.getReactorClass()).eContainer()
            for p in mainModel.getPreambles():
                code_.pr(toText(p.getCode()))
        return code_.__str__()

    def parseCommandOutput(self, line):
        """ generated source for method parseCommandOutput """
        matcher = self.compileErrorPattern.matcher(line)
        if matcher.find():
            result = ErrorFileAndLine()
            result.filepath = matcher.group("path")
            result.line = matcher.group("line")
            result.character = matcher.group("column")
            result.message = matcher.group("message")
            if not result.message.lower().contains("error:"):
                result.isError = False
            return result
        return None

    def getTarget(self):
        """ generated source for method getTarget """
        return Target.C

    def getNetworkBufferType(self):
        """ generated source for method getNetworkBufferType """
        return "uint8_t*"

    def generateDelayGeneric(self):
        """ generated source for method generateDelayGeneric """
        raise TypeError("TODO: auto-generated method stub")

    def createMainReactorInstance(self):
        """ generated source for method createMainReactorInstance """
        if self.mainDef != None:
            if self.main == None:
                self.main = ReactorInstance(self.toDefinition(self.mainDef.getReactorClass()), self.errorReporter, self.unorderedReactions)
                reactionInstanceGraph = self.main.assignLevels()
                if reactionInstanceGraph.nodeCount() > 0:
                    self.errorReporter.reportError("Main reactor has causality cycles. Skipping code generation.")
                    return
                breadth = reactionInstanceGraph.getBreadth()
                if breadth == 0:
                    self.errorReporter.reportWarning("The program has no reactions")
                else:
                    self.targetConfig.compileDefinitions.put("LF_REACTION_GRAPH_BREADTH", str(reactionInstanceGraph.getBreadth()))
            if self.isFederated:
                self.removeRemoteFederateConnectionPorts(main)
                self.main.clearCaches(False)

    def generateSelfStructs(self, r):
        """ generated source for method generateSelfStructs """
        if not self.currentFederate.contains(r):
            return
        self.initializeTriggerObjects.pr(CUtil.selfType(r) + "* " + CUtil.reactorRefName(r) + "[" + r.getTotalWidth() + "];")
        self.initializeTriggerObjects.pr("SUPPRESS_UNUSED_WARNING(" + CUtil.reactorRefName(r) + ");")
        for child in r.children:
            self.generateSelfStructs(child)
