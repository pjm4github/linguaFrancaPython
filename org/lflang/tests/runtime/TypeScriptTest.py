#!/usr/bin/env python
""" generated source for module TypeScriptTest """
# package: org.lflang.tests.runtime
import org.junit.jupiter.api.Assumptions

import org.junit.jupiter.api.Test

from org.lflang.Target

from org.lflang.tests.RuntimeTest

# 
#  * Collection of tests for the TypeScript target.
#  *
#  * Even though all tests are implemented in the base class, we override them
#  * here so that each test can be easily invoked individually from IDEs with
#  * JUnit support like Eclipse and IntelliJ.
#  * This is typically done by right-clicking on the name of the test method and
#  * then clicking "Run".
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class TypeScriptTest(RuntimeTest):
    """ generated source for class TypeScriptTest """
    def __init__(self):
        """ generated source for method __init__ """
        super().__init__(Target.TS)

    def supportsDockerOption(self):
        """ generated source for method supportsDockerOption """
        return True

    def supportsFederatedExecution(self):
        """ generated source for method supportsFederatedExecution """
        return True

    def runGenericTests(self):
        """ generated source for method runGenericTests """
        super().runGenericTests()

    def runTargetSpecificTests(self):
        """ generated source for method runTargetSpecificTests """
        super().runTargetSpecificTests()

    def runMultiportTests(self):
        """ generated source for method runMultiportTests """
        super().runMultiportTests()

    def runConcurrentTests(self):
        """ generated source for method runConcurrentTests """
        super().runConcurrentTests()

    def runFederatedTests(self):
        """ generated source for method runFederatedTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super().runFederatedTests()

    def runDockerTests(self):
        """ generated source for method runDockerTests """
        super().runDockerTests()

    def runDockerFederatedTests(self):
        """ generated source for method runDockerFederatedTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        super().runDockerFederatedTests()

    def runAsFederated(self):
        """ generated source for method runAsFederated """
