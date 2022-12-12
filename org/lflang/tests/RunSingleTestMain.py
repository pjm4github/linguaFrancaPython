#!/usr/bin/env python
""" generated source for module RunSingleTestMain """
# 
#  * Copyright (c) 2021, TU Dresden.
#  *
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  *
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  *
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  *
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
# package: org.lflang.tests
# import java.io.FileNotFoundException
# import java.nio.file.Files
# import java.nio.file.Paths
# import java.util.regex.Matcher
# import java.util.regex.Pattern

from org.lflang import Target

from org.lflang.tests.TestBase import TestLevel

from org.lflang.tests.runtime import CCppTest

from org.lflang.tests.runtime import CTest

from org.lflang.tests.runtime import CppTest

from org.lflang.tests.runtime import PythonTest

from org.lflang.tests.runtime import RustTest

from org.lflang.tests.runtime import TypeScriptTest

# 
#  * Execute a single test case. Use it with the gradle task
#  * {@code gradle runSingleTest --args test/Python/src/Minimal.lf}
#  *
#  * @author Clément Fournier
#  
class RunSingleTestMain:
    """ generated source for class RunSingleTestMain """
    TEST_FILE_PATTERN = re.compile("(test/(\\w+))/src/([^/]++/)*(\\w+.lf)")

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        if len(args):
            raise IllegalArgumentException("Expected 1 path to an LF file")
        path = Paths.get(args[0])
        if not Files.exists(path):
            raise FileNotFoundException("No such test file: " + path)
        matcher = cls.TEST_FILE_PATTERN.matcher(args[0])
        if not matcher.matches():
            raise FileNotFoundException("Not a test: " + path)
        target = Target.forName(matcher.group(2)).get()
        testClass = getTestInstance(target)
        testCase = LFTest(target, path.toAbsolutePath())
        TestBase.runSingleTestAndPrintResults(testCase, testClass, TestBase.pathToLevel(path))

    @classmethod
    def getTestInstance(cls, target):
        """ generated source for method getTestInstance """
        if target == C:
            return CTest.__class__
        elif target == CCPP:
            return CCppTest.__class__
        elif target == CPP:
            return CppTest.__class__
        elif target == TS:
            return TypeScriptTest.__class__
        elif target == Python:
            return PythonTest.__class__
        elif target == Rust:
            return RustTest.__class__
        else:
            raise IllegalArgumentException()


if __name__ == '__main__':
    import sys
    RunSingleTestMain.main(sys.argv)
