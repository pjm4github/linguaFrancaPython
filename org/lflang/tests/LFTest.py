#!/usr/bin/env python
""" generated source for module LFTest """
# package: org.lflang.tests
# import java.io.ByteArrayOutputStream
# import java.io.IOException
# import java.io.InputStream
# import java.io.InputStreamReader
# import java.io.OutputStream
# import java.io.Reader
# import java.nio.file.Path
# import java.nio.file.Paths
# import org.eclipse.xtext.util.RuntimeIOException
from subprocess import Popen

from include.overloading import overloaded
from org.lflang import FileConfig
from enum import Enum
from io import BytesIO
from org.lflang import Target
import os
from org.lflang.generator import LFGeneratorContext
from include.SpecialExceptions import *

# Information about an indexed Lingua Franca test program.
# @author Marten Lohstroh <marten@berkeley.edu>


class LFTest:
    def __init__(self, target, srcFile):
        """ generated source for class LFTest
        Create a new test.
        :param target The target of the test program.
        :param srcFile The path to the file of the test program.
        """
        super().__init__()
        #  The target of the test program. 
        self.target = target
        #  The path to the test. 
        self.srcFile = srcFile
        #  The name of the test.
        path, filename = os.path.split(srcFile)
        self.name = filename
        # FileConfig.findPackageRoot(srcFile, s).relativize(srcFile).__str__()
        self.relativePath = os.path.dirname(os.path.realpath(self.name))
        #  The result of the test. 
        self.result = Result.UNKNOWN
        #  The exit code of the test. 
        self.exitValue = "?"
        #  Object used to determine where the code generator puts files. 
        self.fileConfig = None
        #  Context provided to the code generators 
        self.context = None
        #  Path of the test program relative to the package root. 
        self.relativePath = None
        #  Records compilation stdout/stderr. 
        self.compilationLog = BytesIO()
        #  Specialized object for capturing output streams while executing the test. 
        self.execLog = ExecutionLogger()
        self.issues = ExecutionLogger()
        #  String builder for collecting issues encountered during test execution.
        self.buffer = ""

    def getOutputStream(self):
        """
        /** Stream object for capturing standard and error output. */
        :return:
        """
        """ generated source for method getOutputStream """
        return self.compilationLog

    def compareTo(self, t):
        """
        /**
        * Comparison implementation to allow for tests to be sorted (e.g., when added to a
        * tree set) based on their path (relative to the root of the test directory).
        */
        :param t:
        :return:
        """
        return self.relativePath.compareTo(t.relativePath)

    def equals(self, o):
        """
        /**
        * Return true if the given object is an LFTest instance with a name identical to this test.
        * @param o The object to test for equality with respect to this one.
        * @return True if the given object is equal to this one, false otherwise.
        */
        :param o:
        :return:
        """
        return isinstance(o, LFTest) and o.name == self.name

    @overloaded
    def __str__(self):
        """
        /**
        * Return a string representing the name of this test.
        * @return The name of this test.
        */
        :return:
        """
        return self.name

    def hashCode(self):
        """
        /**
        * Identify tests uniquely on the basis of their name.
        *
        * @return The hash code of the name of this test.
        */
        :return:
        """
        return self.name.hashCode()

    def hasFailed(self):
        """
        /**
        * Report whether this test has failed.
        * @return True if the test has failed, false otherwise.
        */
        :return:
        """
        return self.result != Result.TEST_PASS

    def reportErrors(self):
        """
        /**
        * Compile a string that contains all collected errors and return it.
        * @return A string that contains all collected errors.
        */
        :return:
        """
        if self.hasFailed():
            print("+---------------------------------------------------------------------------+")
            print("Failed: " + self.__class__.__name__)
            print("-----------------------------------------------------------------------------")
            print("Reason: " + self.result.message + " Exit code: " + self.exitValue)
            if self.exitValue == "139":
                print("This exit code typically indicates a segfault. In this case, the execution output is likely missing or incomplete.")
            self.printIfNotEmpty("Reported issues", str(self.issues))
            self.printIfNotEmpty("Compilation output", str(self.compilationLog))
            self.printIfNotEmpty("Execution output", str(self.execLog))
            print("+---------------------------------------------------------------------------+")

    @classmethod
    def printIfNotEmpty(cls, header, message):
        """
        /**
        * Print the message to the system output, but only if the message is not empty.
        *
        * @param header Header for the message to be printed.
        * @param message The log message to print.
        */
        :param header:
        :param message:
        :return:
        """
        if not message.isEmpty():
            print(header + ":")
            print(message)


class Result(Enum):
    """ generated source for enum Result """
    UNKNOWN = "No information available."
    CONFIG_FAIL = "Could not apply configuration."
    PARSE_FAIL = "Unable to parse test."
    VALIDATE_FAIL = "Unable to validate test."
    CODE_GEN_FAIL = "Error while generating code for test."
    NO_EXEC_FAIL = "Did not execute test."
    TEST_FAIL = "Test did not pass."
    TEST_EXCEPTION = "Test exited with an exception."
    TEST_TIMEOUT = "Test timed out."
    TEST_PASS = "Test passed."

    def __init__(self, message):
        """ generated source for method __init__ """
        self.message = message


class ExecutionLogger:
    """ generated source for class ExecutionLogger """
    def __init__(self):
        self.buffer = ""

    def recordStdOut(self, process):
        """ generated source for method recordStdOut """
        return self.recordStream(self.buffer, process.getInputStream())

    def recordStdErr(self, process):
        """ generated source for method recordStdErr """
        return self.recordStream(self.buffer, process.getErrorStream())

    def recordStream(self, builder, inputStream):
        """
        * Return a thread responsible for recording the given stream.
        *
        * @param builder     The builder to append to.
        * @param inputStream The stream to read from.
        :param builder:
        :param inputStream:
        :return:
        """
        try:
            reader = Popen(builder, inputStream)
            buf = BytesIO()
            ll = reader.read(buf)
            while ll > 0:
                builder.append(buf, 0, ll)
                ll = reader.read(buf)
        except IOException as e:
            raise RuntimeIOException(e)




        #        Thread t = new Thread(() -> {
        #            try (Reader reader = new InputStreamReader(inputStream)) {
        #                int len;
        #                char[] buf = new char[1024];
        #                while ((len = reader.read(buf)) > 0) {
        #                    builder.append(buf, 0, len);
        #                }
        #            } catch (IOException e) {
        #                throw new RuntimeIOException(e);
        #            }
        #        });
        #        t.start();
        #        return t;

    def __str__(self):
        """ generated source for method toString_0 """
        return self.buffer

    def clear(self):
        """ generated source for method clear """
        self.buffer = None
