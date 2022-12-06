#!/usr/bin/env python
""" generated source for module SerializationTest """
# package: org.lflang.tests.serialization
import org.junit.jupiter.api.Assumptions

import org.junit.jupiter.api.Test

from org.lflang.Target

from org.lflang.tests.Configurators

from org.lflang.tests.TestBase

from org.lflang.tests.TestRegistry.TestCategory

class SerializationTest(TestBase):
    """ generated source for class SerializationTest """
    def __init__(self):
        """ generated source for method __init__ """
        super(SerializationTest, self).__init__(Target.ALL)

    def runSerializationTestsWithThreadingOff(self):
        """ generated source for method runSerializationTestsWithThreadingOff """
        Assumptions.assumeTrue(supportsSingleThreadedExecution(), Message.NO_SINGLE_THREADED_SUPPORT)
        runTestsForTargets(Message.DESC_SERIALIZATION, TestCategory.SERIALIZATION.equals, Configurators.disableThreading, False)

    def runSerializationTests(self):
        """ generated source for method runSerializationTests """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        runTestsForTargets(Message.DESC_SERIALIZATION, TestCategory.SERIALIZATION.equals, Configurators.noChanges, False)
