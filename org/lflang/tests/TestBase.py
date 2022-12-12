#!/usr/bin/env python
""" generated source for module TestBase """
# package: org.lflang.tests
import urllib
from io import BytesIO

from include.overloading import overloaded
import sys
import unittest
import math
from include.SpecialExceptions import *
import logging
from enum import Enum
from subprocess import Popen
import filewriter as FileWriter
# import java.io.IOException
# import java.io.PrintStream
# import java.io.PrintWriter
# import java.io.StringWriter
# import java.lang.Thread.UncaughtExceptionHandler
# import java.lang.reflect.Constructor
# import java.lang.reflect.InvocationTargetException
# import java.nio.file.Path
# import java.io.File
# import java.io.FileWriter
# import java.io.BufferedWriter
# import java.util.Arrays
# import java.util.Collections
# import java.util.List
# import java.util.Objects
# import java.util.Properties
# import java.util.Set
# import java.util.concurrent.TimeUnit
# import java.util.concurrent.atomic.AtomicReference
# import java.util.function_.Predicate
# import java.util.stream.Collectors
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.resource.ResourceSet
# import org.eclipse.xtext.diagnostics.Severity
# import org.eclipse.xtext.generator.IGeneratorContext
# import org.eclipse.xtext.generator.JavaIoFileSystemAccess
# import org.eclipse.xtext.testing.InjectWith
# import org.eclipse.xtext.testing.extensions.InjectionExtension
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.util.RuntimeIOException
# import org.eclipse.xtext.validation.CheckMode
# import org.eclipse.xtext.validation.IResourceValidator

#import org.junit.jupiter.api.extension.ExtendWith

from org.lflang import DefaultErrorReporter
from org.lflang import FileConfig
from org.lflang import LFRuntimeModule
from org.lflang import LFStandaloneSetup
from org.lflang import Target
from org.lflang.generator import GeneratorResult
from org.lflang.generator import DockerGeneratorBase
from org.lflang.generator import LFGenerator
from org.lflang.generator import LFGeneratorContext
from org.lflang.generator import MainContext
from org.lflang.tests.Configurators import Configurator
from org.lflang.tests.LFTest import Result
from org.lflang.tests.LFTest import LFTest
from org.lflang.tests.TestRegistry import TestCategory

from org.lflang.tests import TestRegistry
from org.lflang.util import FileUtil
from org.lflang.util import LFCommand
from org.lflang import TimeUnit
# import com.google.inject.Inject
# import com.google.inject.Injector
# import com.google.inject.Provider

# 
#  * Base class for test classes that define JUnit tests.
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
#@ExtendWith(InjectionExtension.__class__)
#@InjectWith(LFInjectorProvider.__class__)
class AtomicReference:
    pass


class TestBase:
    """ generated source for class TestBase """
    validator = None
    generator = None
    fileAccess = None
    resourceSetProvider = None

    #  Reference to System.out. 
    out = sys.out

    #  Reference to System.err. 
    err = sys.err

    #  Execution timeout enforced for all tests. 
    MAX_EXECUTION_TIME_SECONDS = 60

    #  Content separator used in test output, 78 characters wide. 
    THIN_LINE = "------------------------------------------------------------------------------" + sys.lineSeparator()

    #  Content separator used in test output, 78 characters wide. 
    THICK_LINE = "==============================================================================" + sys.lineSeparator()

    #  The targets for which to run the tests. 
    targets = None


    # Static function for converting a path to its associated test level.
    # @author Anirudh Rengarajan <arengarajan@berkeley.edu>
    #       
    @classmethod
    def pathToLevel(cls, path):
        """ generated source for method pathToLevel """
        while path.getParent() != None:
            name = path.getFileName().__str__()
            for category in TestCategory.values():
                if category.name().lower() == name.lower():
                    return category.level
            path = path.getParent()
        return cls.TestLevel.EXECUTION

    # A collection messages often used throughout the test package.
    #       *
    # @author Marten Lohstroh <marten@berkeley.edu>
    #       *

    #  Constructor for test classes that test a single target. 
    @overloaded
    def __init__(self, first):
        """ generated source for method __init__ """
        self.__init__([first])

    #  Special ctor for the code coverage test 
    @__init__.register(object, list)
    def __init___0(self, targets:list):
        """ generated source for method __init___0 """
        unittest.TestCase.assertFalse(targets, "empty target list")
        self.targets = targets
        TestRegistry.initialize()


    def runTestsAndPrintResults(self, target, selected, configurator, copy):
        """
        Run selected tests for a given target and configurator up to the specified level.
        #
        :param target The target to run tests for.
        :param selected A predicate that given a test category returns whether
        it should be included in this test run or not.
        :param configurator  A procedure for configuring the tests.
        :param level The level of testing to be performed during this run.
        :param copy Whether or not to work on copies of tests in the test.
        registry.
        :return:
        """
        categories = TestCategory.values()
        for category in categories:
            if category != selected:
                continue
            print(category.getHeader())
            tests = TestRegistry.getRegisteredTests(target, category, copy)
            try:
                self.validateAndRun(tests, configurator, category.level)
            except IOError as e:
                raise RuntimeIOException(e)
            print(TestRegistry.getCoverageReport(target, category))
            self.checkAndReportFailures(tests)

    def runTestsForTargets(self, description, selected, configurator, copy):
        """
        Run tests in the given selection for all targets enabled in this class.
        :param description A string that describes the collection of tests.
        :param selected A predicate that given a test category returns whether
        it should be included in this test run or not.
        :param configurator A procedure for configuring the tests.
        :param level The level of testing to be performed during this run.
        :param copy Whether or not to work on copies of tests in the test.
        registry.
        :return:
        """
        for target in self.targets:
            self.runTestsFor([target], description, selected, configurator, copy)

    def runTestsFor(self, subset, description, selected, configurator, copy):
        """
        Run tests in the given selection for a subset of given targets.
        :param subset The subset of targets to run the selected tests for.
        :param description A string that describes the collection of tests.
        :param selected A predicate that given a test category returns whether
        it should be included in this test run or not.
        :param configurator A procedure for configuring the tests.
        :param level The level of testing to be performed during this run.
        :param copy Whether to work on copies of tests in the test.
        registry.
        :return:
        """
        for target in subset:
            self.printTestHeader(target, description)
            self.runTestsAndPrintResults(target, selected, configurator, copy)

    def supportsSingleThreadedExecution(self):
        """
        Whether to enable {@link #runWithThreadingOff()}.
        :return:
        """
        return False

    @classmethod
    def isWindows(cls):
        """
        Determine whether the current platform is Windows.
        @return true if the current platform is Windwos, false otherwise.
        :return:
        """
        OS = sys.getProperty("os.name").lower()
        return OS.contains("win")

    @classmethod
    def isMac(cls):
        OS = sys.getProperty("os.name").lower()
        return OS.contains("mac")

    @classmethod
    def isLinux(cls):
        OS = sys.getProperty("os.name").lower()
        return OS.contains("linux")

    @classmethod
    def restoreOutputs(cls):
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = cls.out
        sys.stderr = cls.err

    @classmethod
    def redirectOutputs(cls, test):
        """
        Redirect outputs to the given tests for recording.
        :param test The test to redirect outputs to.
        :return:
        """
        sys.stdout = test.getOutputStream()
        sys.stderr = test.getOutputStream()

    @classmethod
    def runSingleTestAndPrintResults(cls, test, testClass, level):
        """
        Run a test, print results on stderr.
        :param test      Test case.
        :param testClass The test class that will execute the test. This is target-specific,
                         it may provide some target-specific configuration. We pass a class
                         and not a new instance because this method needs to ensure the object
                         is properly injected, and so, it needs to control its entire lifecycle.
        :param level     Level to which to run the test.
        :return:
        """
        injector = LFStandaloneSetup(LFRuntimeModule()).createInjectorAndDoEMFRegistration()
        runner = None
        try:
            constructor = testClass.getConstructors()[0]
            runner = constructor.newInstance()
        except InstantiationException as e:
            raise IllegalStateException(e)
        injector.injectMembers(runner)
        tests = set(test)
        try:
            runner.validateAndRun(tests, True, level)
        except IOError as e:
            raise RuntimeIOException(e)
        cls.checkAndReportFailures(tests)

    @classmethod
    def printTestHeader(cls, target, description):
        """
        Print a header that describes a collection of tests.
        :param target The target for which the tests are being performed.
        :param description A string the describes the collection of tests.
        :return:
        """

        sys.stdout.write(TestBase.THICK_LINE)
        print("Target: " + target)
        if description.startsWith("Description: "):
            print(description)
        else:
            print("Description: " + description)
        print(TestBase.THICK_LINE)

    @classmethod
    def checkAndReportFailures(cls, tests):
        """
        Iterate over given tests and evaluate their outcome, report errors if
        there are any.
        :param tests The tests to inspect the results of.
        :return:
        """
        passed = tests.stream().filter().count()
        sys.stdout.write(cls.THIN_LINE)
        print("Passing: " + passed + "/" + len(tests))
        sys.stdout.write(cls.THIN_LINE)
        for test in tests:
            test.reportErrors()
        for lfTest in tests:
            unittest.TestCase.assertEqual(Result.TEST_PASS, lfTest.result)

    def configure(self, test, configurator, level):
        """
        Configure a test by applying the given configurator and return a
        generator context. Also, if the given level is less than
        `TestLevel.BUILD`, add a `no-compile` flag to the generator context. If
        the configurator was not applied successfully, throw an AssertionError.
        :param test the test to configure.
        :param configurator The configurator to apply to the test.
        :param level The level of testing in which the generator context will be
        used.
        :return a generator context with a fresh resource, unaffected by any AST
        transformation that may have occured in other tests.
        @throws IOException if there is any file access problem
        """
        #        var context = new MainContext(
        #            LFGeneratorContext.Mode.STANDALONE, CancelIndicator.NullImpl,{}, {}, new Properties(), true,
        #            new DefaultErrorReporter()
        #

        context = MainContext(LFGeneratorContext.Mode.STANDALONE, None,{}, {}, {}, True, DefaultErrorReporter())
        URI = urllib.request.urlopen()
        r = self.resourceSetProvider.get().getResource(URI.createFileURI(test.srcFile.toFile().getAbsolutePath()), True)
        if r.getErrors().size() > 0:
            test.result = Result.PARSE_FAIL
            raise AssertionError("Test did not parse correctly.")
        # fileAccess.setOutputPath(FileConfig.findPackageRoot(test.srcFile, /*s ->*/ {}).resolve(FileConfig.DEFAULT_SRC_GEN_DIR).toString());
        test.context = context
        test.fileConfig = FileConfig(r, FileConfig.getSrcGenRoot(self.fileAccess), context.useHierarchicalBin())
        # Set the no-compile flag the test is not supposed to reach the build stage.
        if level.compareTo(self.TestLevel.BUILD) < 0:
            context.getArgs().setProperty("no-compile", "")
        self.addExtraLfcArgs(context.getArgs())
        #  Update the test by applying the configuration. E.g., to carry out an AST transformation.
        if configurator != None and not configurator.configure(test):
            test.result = Result.CONFIG_FAIL
            raise AssertionError("Test configuration unsuccessful.")
        return context

    def validate(self, test: LFTest, context):
        """
        Validate the given test. Throw an AssertionError if validation failed.
        :param test: LFTest
        :param context: IGeneratorContext
        :return:
        """
        try:
            # CheckMode.ALL = 3
            issues = self.validator.validate(test.fileConfig.resource, 3, context.getCancelIndicator())
            if issues != None and not issues.isEmpty():
                issuesToString = '\n'.join(issues)
                test.issues += issuesToString
                for it in issues:
                    if it.getSeverity() == logging.ERROR:
                        test.result = Result.VALIDATE_FAIL
        except Exception as e:
            test.result = Result.VALIDATE_FAIL
        if test.result == Result.VALIDATE_FAIL:
            raise AssertionError("Validation unsuccessful.")

    def addExtraLfcArgs(self, args):
        """
        Override to add some LFC arguments to all runs of this test class.
        :param args:
        :return:
        """
        args.setProperty("logging", "Debug")

    def generateCode(self, test):
        """
        Invoke the code generator for the given test.
        :param test The test to generate code for.
        :param test:
        :return:
        """
        result = GeneratorResult.NOTHING
        if test.fileConfig.resource != None:
            self.generator.doGenerate(test.fileConfig.resource, self.fileAccess, test.context)
            result = test.context.getResult()
            if self.generator.errorsOccurred():
                test.result = Result.CODE_GEN_FAIL
                raise AssertionError("Code generation unsuccessful.")
        return result

    def execute(self, test, generatorResult):
        """
        Given an indexed test, execute it and label the test as failing if it
        did not execute, took too long to execute, or executed but exited with
        an error code.

        :param test:
        :param generatorResult:
        :return:
        """
        pbList = self.getExecCommand(test, generatorResult)
        if pbList.isEmpty():
            return
        try:
            for pb in pbList:
                p = pb.start()
                stdout = test.execLog.recordStdOut(p)
                stderr = test.execLog.recordStdErr(p)
                stdoutException = AtomicReference(None)
                stderrException = AtomicReference(None)
                stdout.setUncaughtExceptionHandler()
                stderr.setUncaughtExceptionHandler()
                if not p.waitFor(self.MAX_EXECUTION_TIME_SECONDS, TimeUnit.SECONDS):
                    stdout.interrupt()
                    stderr.interrupt()
                    p.destroyForcibly()
                    test.result = Result.TEST_TIMEOUT
                    return
                else:
                    if stdoutException.get() != None or stderrException.get() != None:
                        test.result = Result.TEST_EXCEPTION
                        test.execLog.buffer.setLength(0)
                        if stdoutException.get() != None:
                            test.execLog.buffer.append("Error during stdout handling:\n")
                            self.appendStackTrace(stdoutException.get(), test.execLog.buffer)
                        if stderrException.get() != None:
                            test.execLog.buffer.append("Error during stderr handling:\n")
                            self.appendStackTrace(stderrException.get(), test.execLog.buffer)
                        return
                    if p.exitValue() != 0:
                        test.result = Result.TEST_FAIL
                        test.exitValue = f"{p.exitValue()}"
                        return
        except Exception as e:
            test.result = Result.TEST_EXCEPTION
            # // Add the stack trace to the test output
            self.appendStackTrace(e, test.execLog.buffer)
            return
        test.result = Result.TEST_PASS
        #          // clear the log if the test succeeded to free memory
        test.execLog = []

    @classmethod
    def appendStackTrace(cls, t, buffer):
        """ generated source for method appendStackTrace """
        sw = ""
        pw = BytesIO(sw)
        t.printStackTrace(pw)
        buffer.append(sw)

    def getDockerRunScript(self, dockerFiles, dockerComposeFilePath):
        """
        Return the content of the bash script used for testing docker option in federated execution.
        :param dockerFiles A list of paths to docker files.
        :param dockerComposeFilePath The path to the docker compose file.
        :return:
        """
        dockerComposeCommand = DockerGeneratorBase.getDockerComposeCommand()
        shCode = ""
        shCode += f"#!/bin/bash\n"
        shCode += f'pids=\"\"\n'
        shCode += f"{dockerComposeCommand} run -f {dockerComposeFilePath} --rm -T rti &\n"
        shCode += f"pids+=\"$!\"\nsleep 3\n"
        for dockerFile in dockerFiles:
            composeServiceName = dockerFile.replace(".Dockerfile", "")
            shCode += f"{dockerComposeCommand} run -f {dockerComposeFilePath} --rm -T {composeServiceName} &\n"
            shCode += f"pids+=\" $!\"\n"
        shCode += f"for p in $pids; do\n"
        shCode += f"    if wait $p; then\n"
        shCode += f"        :\n"
        shCode += f"    else\n"
        shCode += f"        exit 1\n"
        shCode += f"    fi\n"
        shCode += f"done\n"
        return shCode

    def checkDockerExists(self):
        """
        Returns true if docker exists, false otherwise.
        :return:
        """
        checkCommand = LFCommand.get("docker", ["info"])
        return checkCommand.run() == 0

    def getNonfederatedDockerExecCommand(self, test):
        """
        Return a list of Popens used to test the docker option under non-federated execution.
        See the following for references on the instructions called:
        docker build: https://docs.docker.com/engine/reference/commandline/build/
        docker run: https://docs.docker.com/engine/reference/run/
        docker image: https://docs.docker.com/engine/reference/commandline/image/
        :param test The test to get the execution command for.
        :param test:
        :return:
        """
        if not self.checkDockerExists():
            print(self.Message.MISSING_DOCKER)
            return [Popen("exit", "1")]
        srcGenPath = test.fileConfig.getSrcGenPath()
        dockerComposeFile = FileUtil.globFilesEndsWith(srcGenPath, "docker-compose.yml").get(0)
        dockerComposeCommand = DockerGeneratorBase.getDockerComposeCommand()
        return [Popen(dockerComposeCommand, "-f", dockerComposeFile.__str__(), "rm", "-f"), Popen(dockerComposeCommand, "-f", dockerComposeFile.__str__(), "up", "--build"), Popen(dockerComposeCommand, "-f", dockerComposeFile.__str__(), "down", "--rmi", "local")]

    def getFederatedDockerExecCommand(self, test):
        """
        Return a list of Popens used to test the docker option under federated execution.
        :param test The test to get the execution command for.
        :return:
        """
        if not self.checkDockerExists():
            print(self.Message.MISSING_DOCKER)
            return [Popen("exit", "1")]
        srcGenPath = test.fileConfig.getSrcGenPath()
        dockerFiles = FileUtil.globFilesEndsWith(srcGenPath, ".Dockerfile")
        try:
            testScript = open("dockertest", 'w')
            testScript.deleteOnExit()
            if not testScript.setExecutable(True):
                raise IOError("Failed to make test script executable")
            fileWriter = FileWriter(testScript.getAbsoluteFile(), True)
            bufferedWriter = BytesIO(fileWriter)
            dockerComposeFile = FileUtil.globFilesEndsWith(srcGenPath, "docker-compose.yml").get(0)
            bufferedWriter.write(self.getDockerRunScript(dockerFiles, dockerComposeFile))
            bufferedWriter.close()
            return [Popen(testScript.getAbsolutePath())]
        except IOError as e:
            return [Popen("exit", "1")]

    def getExecCommand(self, test, generatorResult):
        """
        Return a list of preconfigured Popen(s) for the command(s)
        that should be used to execute the test program.
        :param test The test to get the execution command for.
        :param generatorResult:
        :return:
        """
        srcBasePath = test.fileConfig.srcPkgPath.resolve("src")
        relativePathName = srcBasePath.relativize(test.fileConfig.srcPath).__str__()
        if relativePathName.lower() == TestCategory.DOCKER.getPath.lower():
            return self.getNonfederatedDockerExecCommand(test)
        elif relativePathName.lower() == TestCategory.DOCKER_FEDERATED.getPath.lower():
            return self.getFederatedDockerExecCommand(test)
        else:
            command = generatorResult.getCommand()
            if command == None:
                test.result = Result.NO_EXEC_FAIL
                test.issues.append("File: ").append(generatorResult.getExecutable()).append(sys.lineSeparator())
            return [] if command == None else [Popen(command.command()).directory(command.directory())]

    def validateAndRun(self, tests, configurator, level):
        """
        Validate and run the given tests, using the specified configuratator and level.
        While performing tests, this method prints a header that reaches completion
        once all tests have been run.
        :param tests A set of tests to run.
        :param configurator A procedure for configuring the tests.
        :param level The level of testing.
        @throws IOException If initial file configuration fails
        :return:
        """
        """ generated source for method validateAndRun """
        x = 78 / len(tests)
        marks = 0
        done = 0
        for test in tests:
            try:
                self.redirectOutputs(test)
                context = self.configure(test, configurator, level)
                self.validate(test, context)
                result = GeneratorResult.NOTHING
                if level.compareTo(self.TestLevel.CODE_GEN) >= 0:
                    result = self.generateCode(test)
                if level == self.TestLevel.EXECUTION:
                    self.execute(test, result)
                elif test.result == Result.UNKNOWN:
                    test.result = Result.TEST_PASS
            except AssertionError as e:
                pass
            except Exception as e:
                test.issues.append(e.getMessage())
            finally:
                self.restoreOutputs()
            done += 1
            while math.floor(done * x) >= marks and marks < 78:
                sys.stdout.write("=")
                marks += 1
        while marks < 78:
            sys.stdout.write("=")
            marks += 1
        sys.stdout.write(sys.lineSeparator())

#
# An enumeration of test levels.
# @author Marten Lohstroh <marten@berkeley.edu>
#       *
#
class TestLevel(Enum):
    """ generated source for enum TestLevel """
    VALIDATION = 'VALIDATION'
    CODE_GEN = 'CODE_GEN'
    BUILD = 'BUILD'
    EXECUTION = 'EXECUTION'

class Message:
    """ generated source for class Message """
    #  Reasons for not running tests.
    NO_WINDOWS_SUPPORT = "Not (yet) supported on Windows."
    NO_SINGLE_THREADED_SUPPORT = "Target does not support single-threaded execution."
    NO_FEDERATION_SUPPORT = "Target does not support federated execution."
    NO_DOCKER_SUPPORT = "Target does not support the 'docker' property."
    NO_DOCKER_TEST_SUPPORT = "Docker tests are only supported on Linux."
    NO_GENERICS_SUPPORT = "Target does not support generic types."

    #  Descriptions of collections of tests.
    DESC_SERIALIZATION = "Run serialization tests."
    DESC_GENERIC = "Run generic tests."
    DESC_TYPE_PARMS = "Run tests for reactors with type parameters."
    DESC_MULTIPORT = "Run multiport tests."
    DESC_AS_FEDERATED = "Run non-federated tests in federated mode."
    DESC_FEDERATED = "Run federated tests."
    DESC_DOCKER = "Run docker tests."
    DESC_DOCKER_FEDERATED = "Run docker federated tests."
    DESC_CONCURRENT = "Run concurrent tests."
    DESC_TARGET_SPECIFIC = "Run target-specific tests"
    DESC_ARDUINO = "Running Arduino tests."
    DESC_AS_CCPP = "Running C tests as CCpp."
    DESC_SINGLE_THREADED = "Run non-concurrent and non-federated tests with threading = off."
    DESC_SCHED_SWAPPING = "Running with non-default runtime scheduler "
    DESC_ROS2 = "Running tests using ROS2."
    DESC_MODAL = "Run modal reactor tests."

    #  Missing dependency messages
    MISSING_DOCKER = "Executable 'docker' not found or 'docker' daemon thread not running"
