#!/usr/bin/env python
""" generated source for module PythonGenerator """
#  Generator for the Python target. 
# 
#  * Copyright (c) 2022, The University of California at Berkeley.
#  * Copyright (c) 2022, The University of Texas at Dallas.
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  * THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  * THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.generator.python
# import java.io.File
# import java.io.IOException
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.HashSet
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Map
# import java.util.Set
# import java.util.stream.Collectors
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.xbase.lib.Exceptions
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import com.google.common.base.Objects
from include.overloading import overloaded

# 
#  * Generator for Python target. This class generates Python code defining each reactor
#  * class given in the input .lf file and imported .lf files.
#  *
#  * Each class will contain all the reaction functions defined by the user in order, with the necessary ports/actions given as parameters.
#  * Moreover, each class will contain all state variables in native Python format.
#  *
#  * A backend is also generated using the CGenerator that interacts with the C code library (see CGenerator.xtend).
#  * The backend is responsible for passing arguments to the Python reactor functions.
#  *
#  * @author{Soroush Bateni <soroush@utdallas.edu>}
#
from lflang import FileConfig, ErrorReporter, Target, ASTUtils, TargetProperty
from lflang.federated.FedFileConfig import FedFileConfig
from lflang.federated.launcher.FedPyLauncher import FedPyLauncher
from lflang.federated.serialization import SupportedSerializers
from lflang.federated.serialization.FedNativePythonSerialization import FedNativePythonSerialization
from lflang.generator import CodeMap, GeneratorUtils, IntegratedBuilder, LFGeneratorContext, GeneratorResult
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.SubContext import SubContext
from lflang.generator.c import CUtil
from lflang.generator.python import PythonPreambleGenerator, PythonNetworkGenerator, PythonPortGenerator, \
    PythonActionGenerator, PythonInfoGenerator, PythonReactionGenerator, PythonModeGenerator, PythonReactorGenerator
from lflang.generator.python.PythonDockerGenerator import PythonDockerGenerator
from lflang.generator.python.PythonTypes import PythonTypes
from lflang.generator.python.PythonValidator import PythonValidator
from lflang.util import FileUtil, StringUtil, LFCommand
from org.lflang.generator.c import CGenerator


class PythonGenerator(CGenerator):
    """ generated source for class PythonGenerator """
    #  Used to add statements that come before reactor classes and user code
    pythonPreamble = CodeBuilder()

    #  Used to add module requirements to setup.py (delimited with )
    pythonRequiredModules = []
    types = None

    @overloaded
    def __init__(self, fileConfig, errorReporter):
        """ generated source for method __init__ """
        super(PythonGenerator, self).__init__()
        self.__init__(fileConfig, errorReporter, PythonTypes(errorReporter))

    @__init__.register(object, FileConfig, ErrorReporter, PythonTypes)
    def __init___0(self, fileConfig, errorReporter, types):
        """ generated source for method __init___0 """
        super(PythonGenerator, self).__init__(types)
        self.targetConfig.compiler = "gcc"
        self.targetConfig.compilerFlags = []
        self.targetConfig.linkerFlags = ""
        self.types = types

    # Generic struct for ports with primitive types and
    # statically allocated arrays in Lingua Franca.
    # This template is defined as
    #   typedef struct {
    #       bool is_present;
    #       lf_sparse_io_record_t* sparse_record; // NULL if there is no sparse record.
    #       int destination_channel;              // -1 if there is no destination.
    #       PyObject* value;
    #       int num_destinations;
    #       lf_token_t* token;
    #       int length;
    #       void (*destructor) (void* value);
    #       void* (*copy_constructor) (void* value);
    #       FEDERATED_GENERIC_EXTENSION
    #   } generic_port_instance_struct;
    #       *
    # @see reactor-c-py/lib/pythontarget.h
    #       
    genericPortType = "generic_port_instance_struct"

    # Generic struct for actions.
    # This template is defined as
    #   typedef struct {
    #      trigger_t* trigger;
    #      PyObject* value;
    #      bool is_present;
    #      bool has_value;
    #      lf_token_t* token;
    #      FEDERATED_CAPSULE_EXTENSION
    #   } generic_action_instance_struct;
    #       *
    # @see reactor-c-py/lib/pythontarget.h
    #       
    genericActionType = "generic_action_instance_struct"

    #  Returns the Target enum for this generator 
    def getTarget(self):
        """ generated source for method getTarget """
        return Target.Python

    protoNames = set()

    #  //////////////////////////////////////////
    #  // Public methods
    def getTargetTypes(self):
        """ generated source for method getTargetTypes """
        return self.types

    #  //////////////////////////////////////////
    #  // Protected methods
    # Generate all Python classes if they have a reaction
    # @param federate The federate instance used to generate classes
    #       
    def generatePythonReactorClasses(self, federate):
        """ generated source for method generatePythonReactorClasses """
        pythonClasses = CodeBuilder()
        pythonClassesInstantiation = CodeBuilder()
        #  Generate reactor classes in Python
        pythonClasses.pr(PythonReactorGenerator.generatePythonClass(main, federate, main, self.types))
        #  Create empty lists to hold reactor instances
        pythonClassesInstantiation.pr(PythonReactorGenerator.generateListsToHoldClassInstances(main, federate))
        #  Instantiate generated classes
        pythonClassesInstantiation.pr(PythonReactorGenerator.generatePythonClassInstantiations(main, federate, main))
        return "\n".join([ pythonClasses.__str__(), "", "# Instantiate classes", pythonClassesInstantiation.__str__()])

    # Generate the Python code constructed from reactor classes and user-written classes.
    # @return the code body
    #       
    def generatePythonCode(self, federate, pyModuleName):
        """ generated source for method generatePythonCode """
        return "\n".join([ "import os", "import sys", "sys.path.append(os.path.dirname(__file__))", "# List imported names, but do not use pylint's --extension-pkg-allow-list option", "# so that these names will be assumed present without having to compile and install.", "# pylint: disable=no-name-in-module, import-error", "from " + pyModuleName + " import (", "    Tag, action_capsule_t, compare_tags, get_current_tag, get_elapsed_logical_time,", "    get_elapsed_physical_time, get_logical_time, get_microstep, get_physical_time,", "    get_start_time, port_capsule, request_stop, schedule_copy,", "    start", ")", "# pylint: disable=c-extension-no-member", "import " + pyModuleName + " as lf", "try:", "    from LinguaFrancaBase.constants import BILLION, FOREVER, NEVER, instant_t, interval_t", "    from LinguaFrancaBase.functions import (", "        DAY, DAYS, HOUR, HOURS, MINUTE, MINUTES, MSEC, MSECS, NSEC, NSECS, SEC, SECS, USEC,", "        USECS, WEEK, WEEKS", "    )", "    from LinguaFrancaBase.classes import Make", "except ModuleNotFoundError:", "    print(\"No module named \'LinguaFrancaBase\'. \"", "          \"Install using \\\"pip3 install LinguaFrancaBase\\\".\")", "    sys.exit(1)", "import copy", "", self.pythonPreamble.__str__(), "", self.generatePythonReactorClasses(federate), "", PythonMainGenerator.generateCode()])

    # Generate the setup.py required to compile and install the module.
    # Currently, the package name is based on filename which does not support sharing the setup.py for multiple .lf files.
    # TODO: use an alternative package name (possibly based on folder name)
    #       *
    # If the LF program itself is threaded or if tracing is enabled, NUMBER_OF_WORKERS is added as a macro
    # so that platform-specific C files will contain the appropriate functions.
    #       
    def generatePythonSetupFile(self, lfModuleName, pyModuleName):
        """ generated source for method generatePythonSetupFile """
        sources = [self.targetConfig.compileAdditionalSources]
        sources.append(lfModuleName + ".c")
        sources = sources.stream().map(Paths.get).map(FileUtil.toUnixString).map(StringUtil.addDoubleQuotes).collect(Collectors.toList())
        macros = []
        macros.append(self.generateMacroEntry("MODULE_NAME", pyModuleName))
        for entry in self.targetConfig.compileDefinitions.entrySet():
            macros.append(self.generateMacroEntry(entry.getKey(), entry.getValue()))
        if self.targetConfig.threading or self.targetConfig.tracing != None:
            macros.append(self.generateMacroEntry("NUMBER_OF_WORKERS", str(self.targetConfig.workers)))
        installRequires = [self.pythonRequiredModules]
        installRequires.append("LinguaFrancaBase")
        installRequires.replaceAll(StringUtil.addDoubleQuotes)
        return "\n".join([ "import sys",
                           "assert (sys.version_info.major >= 3 and sys.version_info.minor >= 6), 'The Python target requires Python version >= 3.6.'",
                           "from setuptools import setup, Extension",
                           "linguafranca" + lfModuleName + "module = Extension(" + StringUtil.addDoubleQuotes(pyModuleName) + ",",
                           "                                            sources = [" + ", ".join(sources) + "],",
                           "                                            define_macros=[" + ", ".join(macros) + "])",
                           "",
                           "setup(name=" + StringUtil.addDoubleQuotes(pyModuleName) + ", version=\"1.0\",",
                           "        ext_modules = [linguafranca" + lfModuleName + "module],",
                           "        install_requires=[" + ", ".join(installRequires) + "])"
                           ])

    def generatePythonFiles(self, federate, lfModuleName, pyModuleName, pyFileName):
        """ generated source for method generatePythonFiles """
        filePath = self.fileConfig.getSrcGenPath().resolve(pyFileName)
        file = filePath.toFile()
        Files.deleteIfExists(filePath)
        if not file.getParentFile().exists():
            file.getParentFile().mkdirs()
        codeMaps = dict()
        codeMaps.put(filePath, CodeMap.fromGeneratedCode(self.generatePythonCode(federate, pyModuleName).__str__()))
        FileUtil.writeToFile(codeMaps.get(filePath).getGeneratedCode(), filePath)
        setupPath = self.fileConfig.getSrcGenPath().resolve("setup.py")
        print("Generating setup file to " + setupPath)
        Files.deleteIfExists(setupPath)
        FileUtil.writeToFile(self.generatePythonSetupFile(lfModuleName, pyModuleName), setupPath)
        return codeMaps

    def pythonCompileCode(self, context):
        """ generated source for method pythonCompileCode """
        pythonCommand = "python3"
        if LFCommand.get("python3", ["--version"], True, self.fileConfig.getSrcGenPath()) == None:
            if LFCommand.get("python", ["--version"], True, self.fileConfig.getSrcGenPath()) != None:
                pythonCommand = "python"
            else:
                errorReporter.reportError("                    Could not find 'python3' or 'python'.\n                    The Python target requires Python >= 3.6 and setuptools >= 45.2.0-1 to build the generated extension.\n                    See https://www.lf-lang.org/docs/handbook/target-language-details.\n                    Auto-compiling can be disabled using the 'no-compile: true' target property.\n")
                return
        buildCmd = commandFactory.createCommand(pythonCommand, ["setup.py", "--quiet", "build_ext", "--inplace"], self.fileConfig.getSrcGenPath())
        buildCmd.setQuiet()
        buildCmd.setEnvironmentVariable("CC", self.targetConfig.compiler)
        buildCmd.setEnvironmentVariable("LDFLAGS", self.targetConfig.linkerFlags)
        if buildCmd.run(context.getCancelIndicator()) == 0:
            print("Successfully built Python extension.")
        else:
            errorReporter.reportError("Failed to build Python extension due to the following error(s):\n" + buildCmd.getErrors())

    def generateDirectives(self):
        """ generated source for method generateDirectives """
        code_ = CodeBuilder()
        code_.prComment("Code generated by the Lingua Franca compiler from:")
        code_.prComment("file:/" + FileUtil.toUnixString(fileConfig.srcFile))
        code_.pr(PythonPreambleGenerator.generateCDefineDirectives(targetConfig, len(federates), isFederated, self.fileConfig.getSrcGenPath(), clockSyncIsOn(), hasModalReactors))
        code_.pr(PythonPreambleGenerator.generateCIncludeStatements(targetConfig, isFederated, hasModalReactors))
        return code_.__str__()

    def generateTopLevelPreambles(self):
        """ generated source for method generateTopLevelPreambles """
        models = set()
        for r in ASTUtils.convertToEmptyListIfNull(self.reactors):
            models.append(ASTUtils.toDefinition(r).eContainer())
        if self.mainDef != None:
            models.append(ASTUtils.toDefinition(self.mainDef.getReactorClass()).eContainer())
        for m in models:
            self.pythonPreamble.pr(PythonPreambleGenerator.generatePythonPreambles(m.getPreambles()))
        return ""

    def enableSupportForSerializationIfApplicable(self, cancelIndicator):
        """ generated source for method enableSupportForSerializationIfApplicable """
        if not IterableExtensions.isNullOrEmpty(targetConfig.protoFiles):
            self.enabledSerializers.append(SupportedSerializers.PROTO)
        for serialization in self.enabledSerializers:
            if serialization == NATIVE:
                pickler = FedNativePythonSerialization()
                self.code_.pr(pickler.generatePreambleForSupport().__str__())
            elif serialization == PROTO:
                for name in self.targetConfig.protoFiles:
                    self.processProtoFile(name, cancelIndicator)
                    dotIndex = name.lastIndexOf(".")
                    rootFilename = name.substring(0, dotIndex) if dotIndex > 0 else name
                    self.pythonPreamble.pr("import " + rootFilename + "_pb2 as " + rootFilename)
                    self.protoNames.append(rootFilename)
            elif serialization == ROS2:
                pass

    def processProtoFile(self, filename, cancelIndicator):
        """ generated source for method processProtoFile """
        protoc = commandFactory.createCommand("protoc", list("--python_out=" + self.fileConfig.getSrcGenPath(), filename), self.fileConfig.srcPath)
        if protoc == None:
            errorReporter.reportError("Processing .proto files requires libprotoc >= 3.6.1")
            return
        returnCode = protoc.run(cancelIndicator)
        if returnCode == 0:
            self.pythonRequiredModules.append("google-api-python-client")
        else:
            errorReporter.reportError("protoc returns error code " + returnCode)

    def generateNetworkReceiverBody(self, action, sendingPort, receivingPort, receivingPortID, sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, type, isPhysical, serializer):
        """ generated source for method generateNetworkReceiverBody """
        return PythonNetworkGenerator.generateNetworkReceiverBody(action, sendingPort, receivingPort, receivingPortID, sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, type, isPhysical, serializer, self.targetConfig.coordination)

    def generateNetworkSenderBody(self, sendingPort, receivingPort, receivingPortID, sendingFed, sendingBankIndex, sendingChannelIndex, receivingFed, type, isPhysical, delay, serializer):
        """ generated source for method generateNetworkSenderBody """
        return PythonNetworkGenerator.generateNetworkSenderBody(sendingPort, receivingPort, receivingPortID, sendingFed, sendingBankIndex, sendingChannelIndex, receivingFed, type, isPhysical, delay, serializer, self.targetConfig.coordination)

    def createFederatedLauncher(self):
        """ generated source for method createFederatedLauncher """
        launcher = FedPyLauncher(targetConfig, self.fileConfig, errorReporter)
        try:
            launcher.createLauncher(federates, federationRTIProperties)
        except IOError as e:
            pass

    def generateAuxiliaryStructs(self, decl):
        """ generated source for method generateAuxiliaryStructs """
        reactor = ASTUtils.toDefinition(decl)
        for input in ASTUtils.allInputs(reactor):
            generateAuxiliaryStructsForPort(decl, input)
        for output in ASTUtils.allOutputs(reactor):
            generateAuxiliaryStructsForPort(decl, output)
        for action in ASTUtils.allActions(reactor):
            generateAuxiliaryStructsForAction(decl, currentFederate, action)

    def generateAuxiliaryStructsForPort(self, decl, port):
        """ generated source for method generateAuxiliaryStructsForPort """
        isTokenType = CUtil.isTokenType(ASTUtils.getInferredType(port), self.types)
        code_.pr(port, PythonPortGenerator.generateAliasTypeDef(decl, port, isTokenType, self.genericPortType))

    def generateAuxiliaryStructsForAction(self, decl, federate, action):
        """ generated source for method generateAuxiliaryStructsForAction """
        if federate != None and not federate.contains(action):
            return
        code_.pr(action, PythonActionGenerator.generateAliasTypeDef(decl, action, self.genericActionType))

    def isOSCompatible(self):
        """ generated source for method isOSCompatible """
        if GeneratorUtils.isHostWindows() and isFederated:
            errorReporter.reportError("Federated LF programs with a Python target are currently not supported on Windows. Exiting code generation.")
            return False
        return True

    def doGenerate(self, resource, context):
        """ generated source for method doGenerate """
        if not self.targetConfig.setByUser.contains(TargetProperty.THREADING):
            self.targetConfig.threading = False
        compileStatus = self.targetConfig.noCompile
        self.targetConfig.noCompile = True
        self.targetConfig.useCmake = False
        cGeneratedPercentProgress = (IntegratedBuilder.VALIDATED_PERCENT_PROGRESS + 100) / 2
        super(PythonGenerator, self).doGenerate(resource, SubContext(context, IntegratedBuilder.VALIDATED_PERCENT_PROGRESS, cGeneratedPercentProgress))
        compilingFederatesContext = SubContext(context, cGeneratedPercentProgress, 100)
        self.targetConfig.noCompile = compileStatus
        if errorsOccurred():
            context.unsuccessfulFinish()
            return
        oldFileConfig = self.fileConfig
        federateCount = 0
        codeMaps = dict()
        for federate in federates:
            federateCount += 1
            lfModuleName = self.fileConfig.name + "_" + federate.name if isFederated else self.fileConfig.name
            if isFederated:
                try:
                    self.fileConfig = FedFileConfig(fileConfig, federate.name)
                except IOError as e:
                    raise Exceptions.sneakyThrow(e)
            if self.main != None:
                try:
                    codeMapsForFederate = self.generatePythonFiles(federate, lfModuleName, generatePythonModuleName(lfModuleName), generatePythonFileName(lfModuleName))
                    codeMaps.putAll(codeMapsForFederate)
                    copyTargetFiles()
                    if not self.targetConfig.noCompile:
                        compilingFederatesContext.reportProgress("Validating {:d}/{:d} sets of generated files...".format(federateCount, len(federates)), 100 * federateCount / len(federates))
                        PythonValidator(fileConfig, errorReporter, codeMaps, self.protoNames).doValidate(context)
                        if not errorsOccurred() and not Objects.equal(context.getMode(), LFGeneratorContext.Mode.LSP_MEDIUM):
                            compilingFederatesContext.reportProgress("Validation complete. Compiling and installing {:d}/{:d} Python modules...".format(federateCount, len(federates)), 100 * federateCount / len(federates))
                            self.pythonCompileCode(context)
                    else:
                        print(PythonInfoGenerator.generateSetupInfo(fileConfig))
                except Exception as e:
                    raise Exceptions.sneakyThrow(e)
                if not isFederated:
                    print(PythonInfoGenerator.generateRunInfo(fileConfig, lfModuleName))
            self.fileConfig = oldFileConfig
        if isFederated:
            print(PythonInfoGenerator.generateFedRunInfo(fileConfig))
        if errorReporter.getErrorsOccurred():
            context.unsuccessfulFinish()
        elif not isFederated:
            context.finish(GeneratorResult.Status.COMPILED, self.fileConfig.name + ".py", self.fileConfig.getSrcGenPath(), self.fileConfig, codeMaps, "python3")
        else:
            context.finish(GeneratorResult.Status.COMPILED, self.fileConfig.name, self.fileConfig.binPath, self.fileConfig, codeMaps, "bash")

    def getDockerGenerator(self):
        """ generated source for method getDockerGenerator """
        return PythonDockerGenerator(isFederated, self.targetConfig)

    def generateDelayBody(self, action, port):
        """ generated source for method generateDelayBody """
        return PythonReactionGenerator.generateCDelayBody(action, port, CUtil.isTokenType(ASTUtils.getInferredType(action), self.types))

    def generateForwardBody(self, action, port):
        """ generated source for method generateForwardBody """
        outputName = ASTUtils.generateVarRef(port)
        if CUtil.isTokenType(ASTUtils.getInferredType(action), self.types):
            return super(PythonGenerator, self).generateForwardBody(action, port)
        else:
            return "lf_set(" + outputName + ", " + action.__name__ + "->token->value);"

    def generateReaction(self, reaction, decl, reactionIndex):
        """ generated source for method generateReaction """
        reactor = ASTUtils.toDefinition(decl)
        if reactor.__name__.contains(GEN_DELAY_CLASS_NAME) or ((mainDef != None and decl == mainDef.getReactorClass() or mainDef == decl) and reactor.isFederated()):
            super(PythonGenerator, self).generateReaction(reaction, decl, reactionIndex)
            return
        code_.pr(PythonReactionGenerator.generateCReaction(reaction, decl, reactionIndex, mainDef, errorReporter, self.types, isFederatedAndDecentralized()))

    def generateStateVariableInitializations(self, instance):
        """ generated source for method generateStateVariableInitializations """

    def generateParameterInitialization(self, instance):
        """ generated source for method generateParameterInitialization """

    def generateMethods(self, reactor):
        """ generated source for method generateMethods """

    def generateUserPreamblesForReactor(self, reactor):
        """ generated source for method generateUserPreamblesForReactor """

    def generateReactorInstanceExtension(self, instance):
        """ generated source for method generateReactorInstanceExtension """
        initializeTriggerObjects.pr(PythonReactionGenerator.generateCPythonReactionLinkers(instance, mainDef))

    def generateSelfStructExtension(self, selfStructBody, decl, constructorCode):
        """ generated source for method generateSelfStructExtension """
        reactor = ASTUtils.toDefinition(decl)
        selfStructBody.pr("char *_lf_name;")
        reactionIndex = 0
        for reaction in ASTUtils.allReactions(reactor):
            selfStructBody.pr("PyObject* " + PythonReactionGenerator.generateCPythonReactionFunctionName(reactionIndex) + ";")
            if reaction.getStp() != None:
                selfStructBody.pr("PyObject* " + PythonReactionGenerator.generateCPythonSTPFunctionName(reactionIndex) + ";")
            if reaction.getDeadline() != None:
                selfStructBody.pr("PyObject* " + PythonReactionGenerator.generateCPythonDeadlineFunctionName(reactionIndex) + ";")
            reactionIndex += 1

    def getConflictingConnectionsInModalReactorsBody(self, source, dest):
        """ generated source for method getConflictingConnectionsInModalReactorsBody """
        return "\n".join([ "\n# Generated forwarding reaction for connections with the same destination", "# but located in mutually exclusive modes.", dest + ".set(" + source + ".value)\n"])

    def setUpGeneralParameters(self):
        """ generated source for method setUpGeneralParameters """
        super(PythonGenerator, self).setUpGeneralParameters()
        if hasModalReactors:
            self.targetConfig.compileAdditionalSources.append("modal_models/impl.c")

    def additionalPostProcessingForModes(self):
        """ generated source for method additionalPostProcessingForModes """
        if not hasModalReactors:
            return
        PythonModeGenerator.generateResetReactionsIfNeeded(reactors)

    @classmethod
    def generateMacroEntry(cls, key, val):
        """ generated source for method generateMacroEntry """
        return "(" + StringUtil.addDoubleQuotes(key) + ", " + StringUtil.addDoubleQuotes(val) + ")"

    @classmethod
    def generatePythonModuleName(cls, lfModuleName):
        """ generated source for method generatePythonModuleName """
        return "LinguaFranca" + lfModuleName

    @classmethod
    def generatePythonFileName(cls, lfModuleName):
        """ generated source for method generatePythonFileName """
        return lfModuleName + ".py"

    def copyTargetFiles(self):
        """ generated source for method copyTargetFiles """
        FileUtil.copyDirectoryFromClassPath("/lib/py/reactor-c-py/include", self.fileConfig.getSrcGenPath(), False)
        FileUtil.copyDirectoryFromClassPath("/lib/py/reactor-c-py/lib", self.fileConfig.getSrcGenPath(), False)
