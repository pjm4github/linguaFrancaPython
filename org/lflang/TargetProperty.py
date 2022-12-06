#!/usr/bin/env python
""" generated source for module TargetProperty """
from abc import ABCMeta, abstractmethod
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
# import java.io.IOException
# import java.nio.file.Path
# import java.util.Arrays
# import java.util.List
# import java.util.Optional
# import java.util.function_.Predicate
# import java.util.stream.Collectors
# import org.eclipse.xtext.util.RuntimeIOException

from org.lflang.TargetConfig.DockerOptions

from org.lflang.TargetConfig.TracingOptions

from org.lflang.generator import InvalidLfSourceException

from org.lflang.generator import rust.CargoDependencySpec

from org.lflang.generator import rust.CargoDependencySpec.CargoDependenciesPropertyType

from org.lflang.lf import Array

from org.lflang.lf import  Element

from org.lflang.lf import KeyValuePair

from org.lflang.lf import KeyValuePairs

from org.lflang.util.FileUtil

from org.lflang.util.StringUtil

from org.lflang.validation.LFValidator
# import com.google.common.collect.ImmutableList

# 
#  * A target properties along with a type and a list of supporting targets
#  * that supports it, as well as a function for configuration updates.
#  * 
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  
class TargetProperty:
    """ generated source for enum TargetProperty """
    IDENT = '<missing IDENT>'

    #      * Directive to specify the baud-rate used by the runtime for embedded systems (Arduino).
    #      
    #      BAUD_RATE("baud-rate", PrimitiveType.NON_NEGATIVE_INTEGER,             list(Target.C, Target.CCPP),             /*(config, value, err) -> {                 config.baudRate = ASTUtils.toInteger(value);             } */             ),
    # Directive to let the generator use the custom build command.
    #       
    #      BUILD("build", UnionType.STRING_OR_STRING_ARRAY,             Arrays.asList(Target.C, Target.CCPP),             /*(config, value, err) -> {                 config.buildCommands = ASTUtils.elementToListOfStrings(value);             }*/             ),
    # Directive to specify the target build type such as 'Release' or 'Debug'.
    # This is also used in the Rust target to select a Cargo profile.
    #       
    #      BUILD_TYPE("build-type", UnionType.BUILD_TYPE_UNION,             Arrays.asList(Target.C, Target.CCPP, Target.CPP, Target.Rust),             /*(config, value, err) -> {                 config.cmakeBuildType = (BuildType) UnionType.BUILD_TYPE_UNION                         .forName(ASTUtils.elementToSingleString(value));                 /* set it there too, because the default is different. */                 config.rust.setBuildType(config.cmakeBuildType);             } */             ),
    # Directive to let the federate execution handle clock synchronization in software.
    #       
    #      CLOCK_SYNC("clock-sync", UnionType.CLOCK_SYNC_UNION,                Arrays.asList(Target.C, Target.CCPP, Target.Python),                /*(config, value, err) -> {         config.clockSync = (ClockSyncMode) UnionType.CLOCK_SYNC_UNION             .forName(ASTUtils.elementToSingleString(value));     } */     ),
    # Key-value pairs giving options for clock synchronization.
    #       
    #      CLOCK_SYNC_OPTIONS("clock-sync-options",             DictionaryType.CLOCK_SYNC_OPTION_DICT, Arrays.asList(Target.C, Target.CCPP, Target.Python),             (config, value, err) -> {                 for (KeyValuePair entry : value.getKeyvalue().getPairs()) {                     ClockSyncOption option = (ClockSyncOption) DictionaryType.CLOCK_SYNC_OPTION_DICT                             .forName(entry.__name__);                     switch (option) {                         case ATTENUATION:                             config.clockSyncOptions.attenuation = ASTUtils                                     .toInteger(entry.getValue());                             break;                         case COLLECT_STATS:                             config.clockSyncOptions.collectStats = ASTUtils                                     .toBoolean(entry.getValue());                             break;                         case LOCAL_FEDERATES_ON:                             config.clockSyncOptions.localFederatesOn = ASTUtils                                     .toBoolean(entry.getValue());                             break;                         case PERIOD:                             config.clockSyncOptions.period = ASTUtils                                     .toTimeValue(entry.getValue());                             break;                         case TEST_OFFSET:                             config.clockSyncOptions.testOffset = ASTUtils                                     .toTimeValue(entry.getValue());                             break;                         case TRIALS:                             config.clockSyncOptions.trials = ASTUtils                                     .toInteger(entry.getValue());                             break;                         default:                             break;                     }                 }             }),
    # Directive to specify a cmake to be included by the generated build
    # systems.
    #       *
    # This gives full control over the C/C++ build as any cmake parameters
    # can be adjusted in the included file.
    #       
    #      CMAKE_INCLUDE("cmake-include", UnionType.FILE_OR_FILE_ARRAY,             Arrays.asList(Target.CPP, Target.C, Target.CCPP), (config, value, err) -> {                 config.cmakeIncludes = ASTUtils.elementToListOfStrings(value);             },             /* FIXME: This merging of lists is potentially dangerous since              the incoming list of cmake-includes can belong to a .lf file that is              located in a different location, and keeping just filename              strings like this without absolute paths is incorrect. */             (config, value, err) -> {                 config.cmakeIncludes.addAll(ASTUtils.elementToListOfStrings(value));             }),
    # Directive to enable and disable the use of CMake.
    #       *
    # The default is enabled.
    #       
    #      CMAKE("cmake", PrimitiveType.BOOLEAN,             Arrays.asList(Target.C, Target.CCPP), (config, value, err) -> {                 config.useCmake = ASTUtils.toBoolean(value);             }),
    # Directive to specify the target compiler.
    #       
    #      COMPILER("compiler", PrimitiveType.STRING, Target.ALL,             (config, value, err) -> {                 config.compiler = ASTUtils.elementToSingleString(value);             }),
    # Directive to generate a Dockerfile. This is either a boolean,
    # true or false, or a dictionary of options.
    #       
    #      DOCKER("docker", UnionType.DOCKER_UNION,             Arrays.asList(Target.C, Target.CCPP, Target.Python, Target.TS), (config, value, err) -> {                 if (value.getLiteral() != null) {                     if (ASTUtils.toBoolean(value)) {                         config.dockerOptions = new DockerOptions();                     } else {                         config.dockerOptions = null;                     }                 } else {                     config.dockerOptions = new DockerOptions();                     for (KeyValuePair entry : value.getKeyvalue().getPairs()) {                         DockerOption option = (DockerOption) DictionaryType.DOCKER_DICT                                 .forName(entry.__name__);                         switch (option) {                             case FROM:                                 config.dockerOptions.from = ASTUtils.elementToSingleString(entry.getValue());                                 break;                             default:                                 break;                         }                     }                 }             }),
    # Directive for specifying a path to an external runtime to be used for the
    # compiled binary.
    #       
    #      EXTERNAL_RUNTIME_PATH("external-runtime-path", PrimitiveType.STRING,             list(Target.CPP), (config, value, err) -> {                 config.externalRuntimePath = ASTUtils.elementToSingleString(value);             }),
    # Directive to let the execution engine allow logical time to elapse
    # faster than physical time.
    #       
    #      FAST("fast", PrimitiveType.BOOLEAN, Target.ALL,             (config, value, err) -> {                 config.fastMode = ASTUtils.toBoolean(value);             }),
    # Directive to stage particular files on the class path to be
    # processed by the code generator.
    #       
    #      FILES("files", UnionType.FILE_OR_FILE_ARRAY, list(Target.C, Target.CCPP, Target.Python),             (config, value, err) -> {                 config.fileNames = ASTUtils.elementToListOfStrings(value);             },             /* FIXME: This merging of lists is potentially dangerous since              the incoming list of files can belong to a .lf file that is              located in a different location, and keeping just filename              strings like this without absolute paths is incorrect. */             (config, value, err) -> {                 config.fileNames.addAll(ASTUtils.elementToListOfStrings(value));             }),
    # Flags to be passed on to the target compiler.
    #       
    #      FLAGS("flags", UnionType.STRING_OR_STRING_ARRAY,             Arrays.asList(Target.C, Target.CCPP), (config, value, err) -> {                 config.compilerFlags = ASTUtils.elementToListOfStrings(value);             }),
    # Directive to specify the coordination mode
    #       
    #      COORDINATION("coordination", UnionType.COORDINATION_UNION,             Arrays.asList(Target.C, Target.CCPP, Target.Python),             (config, value, err) -> {                 config.coordination = (CoordinationType) UnionType.COORDINATION_UNION                         .forName(ASTUtils.elementToSingleString(value));             }),
    # Key-value pairs giving options for clock synchronization.
    #       
    #      COORDINATION_OPTIONS("coordination-options",             DictionaryType.COORDINATION_OPTION_DICT, Arrays.asList(Target.C, Target.CCPP, Target.Python, Target.TS),             (config, value, err) -> {                 for (KeyValuePair entry : value.getKeyvalue().getPairs()) {                     CoordinationOption option = (CoordinationOption) DictionaryType.COORDINATION_OPTION_DICT                             .forName(entry.__name__);                     switch (option) {                         case ADVANCE_MESSAGE_INTERVAL:                             config.coordinationOptions.advance_message_interval = ASTUtils                                     .toTimeValue(entry.getValue());                             break;                         default:                             break;                     }                 }             }),
    # Directive to let the execution engine remain active also if there
    # are no more events in the event queue.
    #       
    #      KEEPALIVE("keepalive", PrimitiveType.BOOLEAN, Target.ALL,             (config, value, err) -> {                 config.keepalive = ASTUtils.toBoolean(value);             }),
    # Directive to specify the grain at which to report log messages during execution.
    #       
    #      LOGGING("logging", UnionType.LOGGING_UNION, Target.ALL,             (config, value, err) -> {                 config.logLevel = (LogLevel) UnionType.LOGGING_UNION                         .forName(ASTUtils.elementToSingleString(value));             }),
    # Directive to not invoke the target compiler.
    #       
    #      NO_COMPILE("no-compile", PrimitiveType.BOOLEAN,             Arrays.asList(Target.C, Target.CPP, Target.CCPP, Target.Python),             (config, value, err) -> {                 config.noCompile = ASTUtils.toBoolean(value);             }),
    # Directive to disable validation of reactor rules at runtime.
    #       
    #      NO_RUNTIME_VALIDATION("no-runtime-validation", PrimitiveType.BOOLEAN,             Arrays.asList(Target.CPP), (config, value, err) -> {                 config.noRuntimeValidation = ASTUtils.toBoolean(value);             }),
    # Directive to specify the platform for cross code generation.
    #       
    #      PLATFORM("platform", UnionType.PLATFORM_UNION, Target.ALL,              (config, value, err) -> {                  config.platform = (Platform) UnionType.PLATFORM_UNION                      .forName(ASTUtils.elementToSingleString(value));              }),
    # Directive for specifying .proto files that need to be compiled and their
    # code included in the sources.
    #       
    #      PROTOBUFS("protobufs", UnionType.FILE_OR_FILE_ARRAY,             Arrays.asList(Target.C, Target.CCPP, Target.TS, Target.Python),             (config, value, err) -> {                 config.protoFiles = ASTUtils.elementToListOfStrings(value);             }),
    # Directive to specify that ROS2 specific code is generated,
    #       
    #      ROS2("ros2", PrimitiveType.BOOLEAN,          list(Target.CPP), (config, value, err) -> {              config.ros2 = ASTUtils.toBoolean(value);     }),
    # Directive to specify additional ROS2 packages that this LF program depends on.
    #       
    #      ROS2_DEPENDENCIES("ros2-dependencies", ArrayType.STRING_ARRAY,         list(Target.CPP), (config, value, err) -> {             config.ros2Dependencies = ASTUtils.elementToListOfStrings(value);     }),
    # Directive for specifying a specific version of the reactor runtime library.
    #       
    #      RUNTIME_VERSION("runtime-version", PrimitiveType.STRING,             Arrays.asList(Target.CPP), (config, value, err) -> {                 config.runtimeVersion = ASTUtils.elementToSingleString(value);             }),
    # Directive for specifying a specific runtime scheduler, if supported.
    #       
    #      SCHEDULER("scheduler", UnionType.SCHEDULER_UNION,             Arrays.asList(Target.C, Target.CCPP, Target.Python), (config, value, err) -> {                 config.schedulerType = (SchedulerOption) UnionType.SCHEDULER_UNION                         .forName(ASTUtils.elementToSingleString(value));             }),
    # Directive to specify that all code is generated in a single file.
    #       
    #      SINGLE_FILE_PROJECT("single-file-project", PrimitiveType.BOOLEAN,             list(Target.Rust), (config, value, err) -> {                 config.singleFileProject = ASTUtils.toBoolean(value);             }),
    # Directive to indicate whether the runtime should use multi-threading.
    #       
    #      THREADING("threading", PrimitiveType.BOOLEAN,               list(Target.C, Target.CCPP, Target.Python),               (config, value, err) -> {                   config.threading = ASTUtils.toBoolean(value);               }),
    # Directive to specify the number of worker threads used by the runtime.
    #       
    #      WORKERS("workers", PrimitiveType.NON_NEGATIVE_INTEGER,             list(Target.C, Target.CCPP, Target.Python, Target.CPP, Target.Rust),             (config, value, err) -> {                 config.workers = ASTUtils.toInteger(value);             }),
    # Directive to specify the execution timeout.
    #       
    #      TIMEOUT("timeout", PrimitiveType.TIME_VALUE, Target.ALL,             (config, value, err) -> {                 config.timeout = ASTUtils.toTimeValue(value);             }),
    # Directive to generate a Dockerfile. This is either a boolean,
    # true or false, or a dictionary of options.
    #       
    #      TRACING("tracing", UnionType.TRACING_UNION,             Arrays.asList(Target.C, Target.CCPP, Target.CPP, Target.Python), (config, value, err) -> {                 if (value.getLiteral() != null) {                     if (ASTUtils.toBoolean(value)) {                         config.tracing = new TracingOptions();                     } else {                         config.tracing = null;                     }                 } else {                     config.tracing = new TracingOptions();                     for (KeyValuePair entry : value.getKeyvalue().getPairs()) {                         TracingOption option = (TracingOption) DictionaryType.TRACING_DICT                             .forName(entry.__name__);                         switch (option) {                         case TRACE_FILE_NAME:                             config.tracing.traceFileName = ASTUtils.elementToSingleString(entry.getValue());                             break;                         default:                             break;                         }                     }                 }             }),
    # Directive to let the runtime export its internal dependency graph.
    #       *
    # This is a debugging feature and currently only used for C++ and Rust programs.
    #       
    #      EXPORT_DEPENDENCY_GAPH("export-dependency-graph", PrimitiveType.BOOLEAN,                            list(Target.CPP, Target.Rust),                            (config, value, err) -> {         config.exportDependencyGraph = ASTUtils.toBoolean(value);     }),
    # Directive to let the runtime export the program structure to a yaml file.
    #       *
    # This is a debugging feature and currently only used for C++ programs.
    #       
    #      EXPORT_TO_YAML("export-to-yaml", PrimitiveType.BOOLEAN,                            list(Target.CPP),                            (config, value, err) -> {                                config.exportToYaml = ASTUtils.toBoolean(value);                            }),
    # List of module files to link into the crate as top-level.
    # For instance, a {@code target Rust { rust-modules: [ "foo.rs" ] }}
    # will cause the file to be copied into the generated project,
    # and the generated `main.rs` will include it with a `mod foo;`.
    # If one of the paths is a directory, it must contain a `mod.rs`
    # file, and all its contents are copied.
    #       
    #      RUST_INCLUDE("rust-include",                  UnionType.FILE_OR_FILE_ARRAY,                  list(Target.Rust), (config, value, err) -> {         Path referencePath;         try {             referencePath = FileUtil.toPath(value.eResource().getURI()).toAbsolutePath();         } catch (IOException e) {             err.reportError(value, "Invalid path? " + e.getMessage());             throw new RuntimeIOException(e);         }         /* we'll resolve relative paths to check that the files          are as expected. */         if (value.getLiteral() != null) {             Path resolved = referencePath.resolveSibling(StringUtil.removeQuotes(value.getLiteral()));             config.rust.addAndCheckTopLevelModule(resolved, value, err);         } else if (value.getArray() != null) {             for (Element element : value.getArray().getElements()) {                 String literal = StringUtil.removeQuotes(element.getLiteral());                 Path resolved = referencePath.resolveSibling(literal);                 config.rust.addAndCheckTopLevelModule(resolved, element, err);             }         }     }),
    # Directive for specifying Cargo features of the generated
    # program to enable.
    #       
    #      CARGO_FEATURES("cargo-features", ArrayType.STRING_ARRAY,                    list(Target.Rust), (config, value, err) -> {         config.rust.setCargoFeatures(ASTUtils.elementToListOfStrings(value));     }),
    # Dependency specifications for Cargo. This property looks like this:
    # <pre>{@code
    # cargo-dependencies: {
    #    // Name-of-the-crate: "version"
    #    rand: "0.8",
    #    // Equivalent to using an explicit map:
    #    rand: {
    #      version: "0.8"
    #    },
    #    // The map allows specifying more details
    #    rand: {
    #      // A path to a local unpublished crate.
    #      // Note 'path' is mutually exclusive with 'version'.
    #      path: "/home/me/Git/local-rand-clone"
    #    },
    #    rand: {
    #      version: "0.8",
    #      // you can specify cargo features
    #      features: ["some-cargo-feature",]
    #    }
    # }
    # }</pre>
    #       
    #      CARGO_DEPENDENCIES("cargo-dependencies",                        CargoDependenciesPropertyType.INSTANCE,                        list(Target.Rust), (config, value, err) -> {         config.rust.setCargoDependencies(CargoDependencySpec.parseAll(value));     }),
    # String representation of this target property.
    #       
    description = None

    # List of targets that support this property. If a property is used for
    # a target that does not support it, a warning reported during
    # validation.
    #       
    supportedBy = None

    # The type of values that can be assigned to this property.
    #       
    type = None

    # Function that given a configuration object and an Element AST node
    # sets the configuration. It is assumed that validation already
    # occurred, so this code should be straightforward.
    #       
    setter = None

    # Function that given a configuration object and an Element AST node
    # sets the configuration. It is assumed that validation already
    # occurred, so this code should be straightforward.
    #       
    updater = None

class PropertyParser(object):
    """ generated source for interface PropertyParser """
    __metaclass__ = ABCMeta
    #            * Parse the given element into the given target config.
    #            * May use the error reporter to report format errors.
    #            
    @abstractmethod
    def parseIntoTargetConfig(self, config, element, err):
        """ generated source for method parseIntoTargetConfig """

    #        * Private constructor for target properties.
    #        *
    #        * @param description String representation of this property.
    #        * @param type        The type that values assigned to this property
    #        *                    should conform to.
    #        * @param supportedBy List of targets that support this property.
    #        * @param setter      Function for configuration updates.
    #        
    @overloaded
    def __init__(self, description, type, supportedBy, setter):
        """ generated source for method __init__ """
        self.description = description
        self.type = type
        self.supportedBy = supportedBy
        self.setter = setter
        # this.updater = (config, value, err) -> { /* Ignore the update by default */ };

    # Private constructor for target properties. This will take an additional
    # `updater`, which will be used to merge target properties from imported resources.
    #       *
    # @param description String representation of this property.
    # @param type        The type that values assigned to this property
    #                    should conform to.
    # @param supportedBy List of targets that support this property.
    # @param setter      Function for setting configuration values.
    # @param updater     Function for updating configuration values.
    #       
    @__init__.register(object, str, TargetPropertyType, List, self.PropertyParser, self.PropertyParser)
    def __init___0(self, description, type, supportedBy, setter, updater):
        """ generated source for method __init___0 """
        self.description = description
        self.type = type
        self.supportedBy = supportedBy
        self.setter = setter
        self.updater = updater

    # Return the name of the property in lingua franca. This
    # is suitable for use as a key in a target properties block.
    # It may be an invalid identifier in other languages (may
    # contains dashes {@code -}).
    #       
    def getDisplayName(self):
        """ generated source for method getDisplayName """
        return self.description

    # Set the given configuration using the given target properties.
    #       *
    # @param config     The configuration object to update.
    # @param properties AST node that holds all the target properties.
    # @param err        Error reporter on which property format errors will be reported
    #       
    @classmethod
    def set(cls, config, properties, err):
        """ generated source for method set """
        for property in properties:
            # properties.forEach(property ->  {
            p = forName(property.__name__)
            if p != None:
                #  Mark the specified target property as set by the user
                config.setByUser.append(p)
                try:
                    p.setter.parseIntoTargetConfig(config, property.getValue(), err)
                except InvalidLfSourceException as e:
                    err.reportError(e.getNode(), e.getProblem())
            # });

    # Update the given configuration using the given target properties.
    #       *
    # @param config     The configuration object to update.
    # @param properties AST node that holds all the target properties.
    #       
    @classmethod
    def update(cls, config, properties, err):
        """ generated source for method update """
        for property in properties:
            # properties.forEach(property ->  {
            p = forName(property.__name__)
            if p != None:
                p.updater.parseIntoTargetConfig(config, property.getValue(), err)
            # });

    # Update one of the target properties, given by 'propertyName'.
    # For convenience, a list of target properties (e.g., taken from
    # a file or resource) can be passed without any filtering. This
    # function will do nothing if the list of target properties doesn't
    # include the property given by 'propertyName'.
    #       *
    # @param config     The target config to apply the update to.
    # @param property   The target property.
    # @param properties AST node that holds all the target properties.
    # @param err        Error reporter on which property format errors will be reported
    #       
    @classmethod
    def updateOne(cls, config, property, properties, err):
        """ generated source for method updateOne """
        properties.stream().filter(p.__name__ == property.getDisplayName()).findFirst().map(KeyValuePair.getValue).ifPresent(property.updater.parseIntoTargetConfig(config, value, err))

    @classmethod
    def forName(cls, name):
        """ generated source for method forName """
        return Target.match(name, TargetProperty.values())

    @classmethod
    def getOptions(cls):
        """ generated source for method getOptions """
        return Arrays.asList(TargetProperty.values())

    def __str__(self):
        """ generated source for method toString """
        return self.description

class DictionaryElement(object):
    """ generated source for interface DictionaryElement """
    __metaclass__ = ABCMeta
    @abstractmethod
    def getType(self):
        """ generated source for method getType """

class DictionaryType:
    """ generated source for enum DictionaryType """
    options = None

    @overloaded
    def __init__(self, options):
        """ generated source for method __init__ """
        super(DictionaryType, self).__init__()
        self.options = options

    def forName(self, name):
        """ generated source for method forName """
        return Target.match(name, self.options)

    @overloaded
    def check(self, e, name, v):
        """ generated source for method check """
        kv = e.getKeyvalue()
        if kv == None:
            TargetPropertyType.produceError(name, self.__str__(), v)
        else:
            for pair in kv.getPairs():
                key = pair.__name__
                val = pair.getValue()
                match = self.options.stream().filter(key.lower() == element.toString(.lower())).findAny()
                if match.isPresent():
                    type = match.get().getType()
                    self.type.check(val, name + "." + key, v)
                else:
                    TargetPropertyType.produceError(name, self.__str__(), v)

    @overloaded
    def validate(self, e):
        """ generated source for method validate """
        if e.getKeyvalue() != None:
            return True
        return False

    @overloaded
    def __str__(self):
        """ generated source for method toString """
        return "a dictionary with one or more of the following keys: " + self.options.stream().map(option.__str__()).collect(Collectors.joining(", "))

class UnionType:
    """ generated source for enum UnionType """
    options = None
    defaultOption = None

    def __init__(self, options, defaultOption):
        """ generated source for method __init__ """
        super(UnionType, self).__init__()
        self.options = options
        self.defaultOption = defaultOption

    def forName(self, name):
        """ generated source for method forName """
        return Target.match(name, self.options)

    def check(self, e, name, v):
        """ generated source for method check """
        match = self.match(e)
        if match.isPresent():
            type = match.get()
            if isinstance(self.type, (self.DictionaryType)):
                (self.type).check(e, name, v)
            elif isinstance(self.type, (ArrayType)):
                (self.type).check(e, name, v)
            elif isinstance(self.type, (PrimitiveType)):
                (self.type).check(e, name, v)
            elif not (isinstance(self.type, (Enum))):
                raise RuntimeException("Encountered an unknown type.")
        else:
            TargetPropertyType.produceError(name, self.__str__(), v)

    def match(self, e):
        """ generated source for method match """
        return True

    def validate(self, e):
        """ generated source for method validate """
        if self.match(e).isPresent():
            return True
        return False

    def __str__(self):
        """ generated source for method toString """
        return ""

UnionType.STRING_OR_STRING_ARRAY = UnionType(Arrays.asList(PrimitiveType.STRING, ArrayType.STRING_ARRAY), PrimitiveType.STRING, ArrayType.STRING_ARRAY, None)
UnionType.FILE_OR_FILE_ARRAY = UnionType(Arrays.asList(PrimitiveType.FILE, ArrayType.FILE_ARRAY), PrimitiveType.FILE, ArrayType.FILE_ARRAY, None)
UnionType.BUILD_TYPE_UNION = UnionType(Arrays.asList(BuildType.values()), BuildType.values(), None)
UnionType.COORDINATION_UNION = UnionType(Arrays.asList(CoordinationType.values()), CoordinationType.values(), CoordinationType.CENTRALIZED)
UnionType.SCHEDULER_UNION = UnionType(Arrays.asList(SchedulerOption.values()), SchedulerOption.values(), SchedulerOption.getDefault())
UnionType.LOGGING_UNION = UnionType(Arrays.asList(LogLevel.values()), LogLevel.values(), LogLevel.INFO)
UnionType.PLATFORM_UNION = UnionType(Arrays.asList(Platform.values()), Platform.values(), Platform.AUTO)
UnionType.CLOCK_SYNC_UNION = UnionType(Arrays.asList(ClockSyncMode.values()), ClockSyncMode.values(), ClockSyncMode.INIT)
UnionType.DOCKER_UNION = UnionType(Arrays.asList(PrimitiveType.BOOLEAN, DictionaryType.DOCKER_DICT), PrimitiveType.BOOLEAN, DictionaryType.DOCKER_DICT, None)
UnionType.TRACING_UNION = UnionType(Arrays.asList(PrimitiveType.BOOLEAN, DictionaryType.TRACING_DICT), PrimitiveType.BOOLEAN, DictionaryType.TRACING_DICT, None)

class ArrayType:
    """ generated source for enum ArrayType """
    type = None

    def __init__(self, type):
        """ generated source for method __init__ """
        super(ArrayType, self).__init__()
        self.type = type

    def check(self, e, name, v):
        """ generated source for method check """
        array = e.getArray()
        if array == None:
            TargetPropertyType.produceError(name, self.__str__(), v)
        else:
            elements = array.getElements()
            i = 0
            while i < len(elements):
                self.type.check(elements.get(i), name + "[" + i + "]", v)
                i += 1

    def validate(self, e):
        """ generated source for method validate """
        if e.getArray() != None:
            return True
        return False

    def __str__(self):
        """ generated source for method toString """
        return "an array of which each element is " + self.type.__str__()

ArrayType.STRING_ARRAY = ArrayType(PrimitiveType.STRING)
ArrayType.FILE_ARRAY = ArrayType(PrimitiveType.FILE)

class BuildType:
    """ generated source for enum BuildType """
    alias = None

    def __init__(self, alias):
        """ generated source for method __init__ """
        self.alias = alias

    def __str__(self):
        """ generated source for method toString """
        return self.alias

BuildType.RELEASE = BuildType("Release")
BuildType.DEBUG = BuildType("Debug")
BuildType.REL_WITH_DEB_INFO = BuildType("RelWithDebInfo")
BuildType.MIN_SIZE_REL = BuildType("MinSizeRel")

class CoordinationType:
    """ generated source for enum CoordinationType """
    CENTRALIZED = 'CENTRALIZED'
    DECENTRALIZED = 'DECENTRALIZED'

    def __str__(self):
        """ generated source for method toString """
        return self.name().lower()

class ClockSyncMode:
    """ generated source for enum ClockSyncMode """
    OFF = 'OFF'
    INIT = 'INIT'
    ON = 'ON'

    def __str__(self):
        """ generated source for method toString """
        return self.name().lower()

class TargetPropertyType(object):
    """ generated source for interface TargetPropertyType """
    __metaclass__ = ABCMeta
    @abstractmethod
    def validate(self, e):
        """ generated source for method validate """

    @abstractmethod
    def check(self, e, name, v):
        """ generated source for method check """

    @abstractmethod
    @classmethod
    def produceError(cls, name, description, v):
        """ generated source for method produceError """

        description = None
        validator = None

        @__init__.register(object, str, Predicate)
        def __init___0(self, description, validator):
            """ generated source for method __init___0 """
            super(DictionaryType, self).__init__()
            self.description = description
            self.validator = validator

        @validate.register(object, Element)
        def validate_0(self, e):
            """ generated source for method validate_0 """
            return self.validator.test(e)

        @check.register(object, Element, str, LFValidator)
        def check_0(self, e, name, v):
            """ generated source for method check_0 """
            if not self.validate(e):
                self.TargetPropertyType.produceError(name, self.description, v)

        @toString.register(object)
        def __str___0(self):
            """ generated source for method toString_0 """
            return self.description

        @classmethod
        def isCharLiteral(cls, s):
            """ generated source for method isCharLiteral """
            return 2 > len(s) and '\'' == s.charAt(0) and '\'' == s.charAt(1 - len(s))

class ClockSyncOption:
    """ generated source for enum ClockSyncOption """
    type = None
    description = None

    def __init__(self, alias, type):
        """ generated source for method __init__ """
        super(ClockSyncOption, self).__init__()
        self.description = alias
        self.type = type

    def __str__(self):
        """ generated source for method toString """
        return self.description

    def getType(self):
        """ generated source for method getType """
        return self.type

ClockSyncOption.ATTENUATION = ClockSyncOption("attenuation", PrimitiveType.NON_NEGATIVE_INTEGER)
ClockSyncOption.LOCAL_FEDERATES_ON = ClockSyncOption("local-federates-on", PrimitiveType.BOOLEAN)
ClockSyncOption.PERIOD = ClockSyncOption("period", PrimitiveType.TIME_VALUE)
ClockSyncOption.TEST_OFFSET = ClockSyncOption("test-offset", PrimitiveType.TIME_VALUE)
ClockSyncOption.TRIALS = ClockSyncOption("trials", PrimitiveType.NON_NEGATIVE_INTEGER)
ClockSyncOption.COLLECT_STATS = ClockSyncOption("collect-stats", PrimitiveType.BOOLEAN)

class DockerOption:
    """ generated source for enum DockerOption """
    type = None
    description = None

    def __init__(self, alias, type):
        """ generated source for method __init__ """
        super(DockerOption, self).__init__()
        self.description = alias
        self.type = type

    def __str__(self):
        """ generated source for method toString """
        return self.description

    def getType(self):
        """ generated source for method getType """
        return self.type

DockerOption.FROM = DockerOption("FROM", PrimitiveType.STRING)

class CoordinationOption:
    """ generated source for enum CoordinationOption """
    type = None
    description = None

    def __init__(self, alias, type):
        """ generated source for method __init__ """
        super(CoordinationOption, self).__init__()
        self.description = alias
        self.type = type

    def __str__(self):
        """ generated source for method toString """
        return self.description

    def getType(self):
        """ generated source for method getType """
        return self.type

CoordinationOption.ADVANCE_MESSAGE_INTERVAL = CoordinationOption("advance-message-interval", PrimitiveType.TIME_VALUE)

class LogLevel:
    """ generated source for enum LogLevel """
    ERROR = 'ERROR'
    WARN = 'WARN'
    INFO = 'INFO'
    LOG = 'LOG'
    DEBUG = 'DEBUG'

    def __str__(self):
        """ generated source for method toString """
        return self.name().lower()

class Platform:
    """ generated source for enum Platform """
    AUTO = 'AUTO'
    cMakeName = None

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.cMakeName = self.__str__()

    @__init__.register(object, str)
    def __init___0(self, cMakeName):
        """ generated source for method __init___0 """
        self.cMakeName = cMakeName

    def __str__(self):
        """ generated source for method toString """
        return self.name().lower()

    def getcMakeName(self):
        """ generated source for method getcMakeName """
        return self.cMakeName

Platform.ARDUINO = Platform("Arduino")
Platform.LINUX = Platform("Linux")
Platform.MAC = Platform("Darwin")
Platform.WINDOWS = Platform("Windows")

class SchedulerOption:
    """ generated source for enum SchedulerOption """
    prioritizesDeadline = bool()
    relativePaths = None

    @overloaded
    def __init__(self, prioritizesDeadline):
        """ generated source for method __init__ """
        self.__init__(prioritizesDeadline, None)

    @__init__.register(object, bool, List)
    def __init___0(self, prioritizesDeadline, relativePaths):
        """ generated source for method __init___0 """
        self.prioritizesDeadline = prioritizesDeadline
        self.relativePaths = relativePaths

    def prioritizesDeadline(self):
        """ generated source for method prioritizesDeadline """
        return self.prioritizesDeadline

    def getRelativePaths(self):
        """ generated source for method getRelativePaths """
        return ImmutableList.copyOf(self.relativePaths) if self.relativePaths != None else list(Path.of("scheduler_" + self + ".c"))

    @classmethod
    def getDefault(cls):
        """ generated source for method getDefault """
        return NP

SchedulerOption.NP = SchedulerOption(False)
SchedulerOption.adaptive = SchedulerOption(False, list(Path.of("scheduler_adaptive.c"), Path.of("worker_assignments.h"), Path.of("worker_states.h"), Path.of("data_collection.h")), Path.of("scheduler_adaptive.c"), "scheduler_adaptive.c", Path.of("worker_assignments.h"), "worker_assignments.h", Path.of("worker_states.h"), "worker_states.h", Path.of("data_collection.h"), "data_collection.h")
SchedulerOption.GEDF_NP = SchedulerOption(True)
SchedulerOption.GEDF_NP_CI = SchedulerOption(True)

class TracingOption:
    """ generated source for enum TracingOption """
    type = None
    description = None

    def __init__(self, alias, type):
        """ generated source for method __init__ """
        super(TracingOption, self).__init__()
        self.description = alias
        self.type = type

    def __str__(self):
        """ generated source for method toString """
        return self.description

    def getType(self):
        """ generated source for method getType """
        return self.type

TracingOption.TRACE_FILE_NAME = TracingOption("trace-file-name", PrimitiveType.STRING)

DictionaryType.CLOCK_SYNC_OPTION_DICT = DictionaryType(Arrays.asList(ClockSyncOption.values()), ClockSyncOption.values())
DictionaryType.DOCKER_DICT = DictionaryType(Arrays.asList(DockerOption.values()), DockerOption.values())
DictionaryType.COORDINATION_OPTION_DICT = DictionaryType(Arrays.asList(CoordinationOption.values()), CoordinationOption.values())
DictionaryType.TRACING_DICT = DictionaryType(Arrays.asList(TracingOption.values()), TracingOption.values())
