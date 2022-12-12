#!/usr/bin/env python
""" generated source for module TargetConfig """
# 
# Copyright (c) 2019, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.HashSet
# import java.util.List
# import java.util.Map
# import java.util.Set

from org.lflang.TargetProperty import BuildType

from org.lflang.TargetProperty import ClockSyncMode

from org.lflang.TargetProperty import CoordinationType

from org.lflang.TargetProperty import LogLevel

from org.lflang.TargetProperty import Platform

from org.lflang.TargetProperty import SchedulerOption

from org.lflang.generator.rust import RustTargetConfig

#  
#  * A class for keeping the current target configuration.
#  * 
#  * Class members of type String are initialized as empty strings, 
#  * unless otherwise stated.
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  

class ClockSyncOptions(object):
    """ generated source for class ClockSyncOptions """
    #          * Dampen the adjustments to the clock synchronization offset by this rate.
    #          * The default is 10.
    #
    attenuation = 10

    #          * Whether or not to collect statistics while performing clock synchronization.
    #          * This setting is only considered when clock synchronization has been activated.
    #          * The default is true.
    #
    collectStats = True

    #          * Enable clock synchronization for federates on the same machine.
    #          * Default is false.
    #
    localFederatesOn = False

    #          * Interval at which clock synchronization is initiated by the RTI (will be passed
    #          * to it as an argument on the command-line).
    #          * The default is 5 milliseconds.
    #
    period = TimeValue(5, TimeUnit.MILLI)

    #          * Indicate the number of exchanges to be had per each clock synchronization round.
    #          * See /lib/core/federated/clock-sync.h for more details.
    #          * The default is 10.
    #
    trials = 10

    #          * Used to create an artificial clock synchronization error for the purpose of testing.
    #          * The default is null.
    #
    testOffset = None


#      * Settings related to coordination of federated execution.
#
class CoordinationOptions(object):
    """ generated source for class CoordinationOptions """
    #          * For centralized coordination, if a federate has a physical action that can trigger
    #          * an output, directly or indirectly, then it will send NET (next event tag) messages
    #          * to the RTI periodically as its physical clock advances. This option sets the amount
    #          * of time to wait between sending such messages. Increasing this value results in
    #          * downstream federates that lag further behind physical time (if the "after" delays
    #          * are insufficient).
    #          * The default is null, which means it is up the implementation to choose an interval.
    #
    advance_message_interval = None


#      * Settings related to Docker options.
#
class DockerOptions(object):
    """ generated source for class DockerOptions """
    #          * The base image and tag from which to build the Docker image. The default is "alpine:latest".
    #
    from_ = "alpine:latest"


#      * Settings related to tracing options.
#
class TracingOptions(object):
    """ generated source for class TracingOptions """
    #          * The name to use as the root of the trace file produced.
    #          * This defaults to the name of the .lf file.
    #
    traceFileName = None


class TargetConfig(object):
    """ generated source for class TargetConfig """
    #      * Keep track of every target property that is explicitly set by the user.
    #      
    setByUser = set()

    #      * Specify Baud Rate for Embedded Devices, including Arduino.
    #      
    baudRate = 9600

    #      * A list of custom build commands that replace the default build process of
    #      * directly invoking a designated compiler. A common usage of this target
    #      * property is to set the command to build on the basis of a Makefile.
    #      
    buildCommands = []

    #      * The mode of clock synchronization to be used in federated programs.
    #      * The default is 'initial'.
    #      
    clockSync = ClockSyncMode.INIT

    #      * Clock sync options.
    #      
    clockSyncOptions = ClockSyncOptions()

    #      * Parameter passed to cmake. The default is 'Release'.
    #      
    cmakeBuildType = BuildType.RELEASE

    #      * Enable or disable the use of CMake to build.
    #      * 
    #      * The default is enabled.
    #      
    useCmake = True

    #      * Optional additional extensions to include in the generated CMakeLists.txt.
    #      
    cmakeIncludes = []

    #      * List of cmake-includes from the cmake-include target property with no path info.
    #      * Useful for copying them to remote machines. This is needed because
    #      * target cmake-includes can be resources with resource paths.
    #      
    cmakeIncludesWithoutPath = []

    #      * The compiler to invoke, unless a build command has been specified.
    #      
    compiler = ""

    #      * Additional sources to add to the compile command if appropriate.
    #      
    compileAdditionalSources = []

    #      * Additional (preprocessor) definitions to add to the compile command if appropriate.
    #      * 
    #      * The first string is the definition itself, and the second string is the value to attribute to that definition, if any.
    #      * The second value could be left empty.
    #      
    compileDefinitions = dict()

    #      * Additional libraries to add to the compile command using the "-l" command-line option.
    #      
    compileLibraries = []

    #      * Flags to pass to the compiler, unless a build command has been specified.
    #      
    compilerFlags = []

    #      * The type of coordination used during the execution of a federated program.
    #      * The default is 'centralized'.
    #      
    coordination = CoordinationType.CENTRALIZED

    #      * Docker options.
    #      
    dockerOptions = None

    #      * Coordination options.
    #      
    coordinationOptions = CoordinationOptions()

    #      * Link to an external runtime library instead of the default one.
    #      
    externalRuntimePath = None

    #      * If true, configure the execution environment such that it does not
    #      * wait for physical time to match logical time. The default is false.
    #      
    fastMode = False

    #      * List of files to be copied to src-gen.
    #      
    fileNames = []

    #      * List of file names from the files target property with no path info.
    #      * Useful for copying them to remote machines. This is needed because
    #      * target files can be resources with resource paths.
    #      
    filesNamesWithoutPath = []

    #      * If true, configure the execution environment to keep executing if there
    #      * are no more events on the event queue. The default is false.
    #      
    keepalive = False

    #      * The level of logging during execution. The default is INFO.
    #      
    logLevel = LogLevel.INFO

    #      * Flags to pass to the linker, unless a build command has been specified.
    #      
    linkerFlags = ""

    #      * If true, do not invoke the target compiler or build command.
    #      * The default is false.
    #      
    noCompile = False

    #      * If true, do not perform runtime validation. The default is false.
    #      
    noRuntimeValidation = False

    #      * Set the target platform.
    #      * This tells the build system what platform-specific support
    #      * files it needs to incorporate at compile time.
    #      *
    #      * @author Samuel Berkun (sberkun@berkeley.edu)
    #      
    platform = Platform.AUTO

    #      * List of proto files to be processed by the code generator.
    #      
    protoFiles = []

    #      * If true, generate ROS2 specific code.
    #      
    ros2 = False

    #      * Additional ROS2 packages that the LF program depends on.
    #      
    ros2Dependencies = None

    #      * The version of the runtime library to be used in the generated target.
    #      
    runtimeVersion = None

    #  Whether all reactors are to be generated into a single target language file. 
    singleFileProject = False

    #  What runtime scheduler to use. 
    schedulerType = SchedulerOption.getDefault()

    #      * The number of worker threads to deploy. The default is zero, which indicates that
    #      * the runtime is allowed to freely choose the number of workers.
    #      
    workers = 0

    #      * Indicate whether the runtime should use multithreaded execution.
    #      
    threading = True

    #      * The timeout to be observed during execution of the program.
    #      
    timeout = None

    #      * If non-null, configure the runtime environment to perform tracing.
    #      * The default is null.
    #      
    tracing = None

    #      * If true, the resulting binary will output a graph visualizing all reaction dependencies.
    #      *
    #      * This option is currently only used for C++ and Rust. This export function is a valuable tool
    #      * for debugging LF programs and helps to understand the dependencies inferred by the runtime.
    #      
    exportDependencyGraph = False

    #      * If true, the resulting binary will output a yaml file describing the whole reactor structure
    #      * of the program.
    #      *
    #      * This option is currently only used for C++. This export function is a valuable tool for debugging
    #      * LF programs and performing external analysis.
    #      
    exportToYaml = False

    #  Rust-specific configuration. 
    rust = RustTargetConfig()

    #      * Settings related to clock synchronization.
    #      
