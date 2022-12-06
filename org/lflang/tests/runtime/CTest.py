#!/usr/bin/env python
""" generated source for module CTest """
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
# package: org.lflang.tests.runtime
# import java.util.List

import org.junit.jupiter.api.Assumptions

import org.junit.jupiter.api.Disabled

import org.junit.jupiter.api.Test

from org.lflang.Target

from org.lflang.tests.Configurators

from org.lflang.tests.RuntimeTest

from org.lflang.tests.TestRegistry.TestCategory

# 
#  * Collection of tests for the C target.
#  *
#  * Tests that are implemented in the base class are still overridden so that
#  * each test can be easily invoked individually from IDEs with JUnit support
#  * like Eclipse and IntelliJ.
#  * This is typically done by right-clicking on the name of the test method and
#  * then clicking "Run".*
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class CTest(RuntimeTest):
    """ generated source for class CTest """
    def __init__(self):
        """ generated source for method __init__ """
        super(CTest, self).__init__(Target.C)

    def supportsSingleThreadedExecution(self):
        """ generated source for method supportsSingleThreadedExecution """
        return True

    def supportsFederatedExecution(self):
        """ generated source for method supportsFederatedExecution """
        return True

    def supportsDockerOption(self):
        """ generated source for method supportsDockerOption """
        return True

    def runGenericTests(self):
        """ generated source for method runGenericTests """
        super(CTest, self).runGenericTests()

    def runTargetSpecificTests(self):
        """ generated source for method runTargetSpecificTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super(CTest, self).runTargetSpecificTests()

    def runMultiportTests(self):
        """ generated source for method runMultiportTests """
        super(CTest, self).runMultiportTests()

    def runArduinoTests(self):
        """ generated source for method runArduinoTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super(CTest, self).runTestsFor(list(Target.C), Message.DESC_ARDUINO, TestCategory.ARDUINO.equals, Configurators.noChanges, False)

    def runWithThreadingOff(self):
        """ generated source for method runWithThreadingOff """
        super(CTest, self).runWithThreadingOff()

    @Disabled("TODO only 27/96 tests pass")
    def runAsFederated(self):
        """ generated source for method runAsFederated """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super(CTest, self).runAsFederated()

    def runConcurrentTests(self):
        """ generated source for method runConcurrentTests """
        super(CTest, self).runConcurrentTests()

    def runFederatedTests(self):
        """ generated source for method runFederatedTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super(CTest, self).runFederatedTests()

    def runDockerTests(self):
        """ generated source for method runDockerTests """
        super(CTest, self).runDockerTests()

    def runDockerFederatedTests(self):
        """ generated source for method runDockerFederatedTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super(CTest, self).runDockerFederatedTests()
