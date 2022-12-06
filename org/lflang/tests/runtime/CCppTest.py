#!/usr/bin/env python
""" generated source for module CCppTest """
# package: org.lflang.tests.runtime
import org.junit.jupiter.api.Assumptions

import org.junit.jupiter.api.Test

from org.lflang.ASTUtils

from org.lflang.Target

from org.lflang.tests.TestBase

from org.lflang.tests.TestRegistry.TestCategory

# 
#  * Collection of tests for the CCpp target.
#  *
#  * NOTE: This test does not inherit any tests because it directly extends TestBase.
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class CCppTest(TestBase):
    """ generated source for class CCppTest """
    #      * This target selects the C target it has no tests defined for it.
    #      * Instead, it reconfigures existing C tests to adopt the CCpp target.
    #      
    def __init__(self):
        """ generated source for method __init__ """
        super(CCppTest, self).__init__(Target.C)

    #      * Run C tests with the target CCpp.
    #      
    def runAsCCpp(self):
        """ generated source for method runAsCCpp """
        Assumptions.assumeFalse(isWindows(), Message.NO_WINDOWS_SUPPORT)
        runTestsForTargets(Message.DESC_AS_CCPP, CCppTest.isExcludedFromCCpp, ASTUtils.changeTargetName(it.fileConfig.resource, Target.CCPP.getDisplayName()), True)

    #      * Exclusion function for runAsCCpp test
    #      
    @classmethod
    def isExcludedFromCCpp(cls, category):
        """ generated source for method isExcludedFromCCpp """
        excluded = category == TestCategory.SERIALIZATION
        excluded |= isWindows() and (category == TestCategory.DOCKER_FEDERATED or category == TestCategory.ARDUINO)
        excluded |= isMac() and (category == TestCategory.DOCKER_FEDERATED or category == TestCategory.DOCKER)
        return not excluded
