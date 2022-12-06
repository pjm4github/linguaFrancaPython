#!/usr/bin/env python
""" generated source for module CppRos2Test """
# package: org.lflang.tests.runtime
import org.junit.jupiter.api.Assumptions

import org.junit.jupiter.api.Test

from org.lflang.ASTUtils

from org.lflang.Target

from org.lflang.lf import Element

from org.lflang.lf import LfFactory

from org.lflang.tests.TestBase

from org.lflang.tests.TestRegistry.TestCategory

# 
#  * Run C++ tests using the ROS2 platform.
#  *
#  * NOTE: This test does not inherit any tests because it directly extends TestBase.
#  *
#  * @author Christian Menard <christian.menard@tu-dresden.de>
#  
class CppRos2Test(TestBase):
    """ generated source for class CppRos2Test """
    def __init__(self):
        """ generated source for method __init__ """
        super(CppRos2Test, self).__init__(Target.CPP)

    #      * Run C++ tests with the ros2 target property set
    #      
    def runWithRos2(self):
        """ generated source for method runWithRos2 """
        Assumptions.assumeTrue(isLinux(), "Only supported on Linux")
        trueLiteral = LfFactory.eINSTANCE.createElement()
        trueLiteral.setLiteral("true")
        runTestsForTargets(Message.DESC_ROS2, True, ASTUtils.addTargetProperty(it.fileConfig.resource, "ros2", trueLiteral), True)
