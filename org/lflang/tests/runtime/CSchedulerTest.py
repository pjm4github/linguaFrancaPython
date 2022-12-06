#!/usr/bin/env python
""" generated source for module CSchedulerTest """
# package: org.lflang.tests.runtime
# import java.util.EnumSet

import org.junit.jupiter.api.Test

from org.lflang.Target

from org.lflang.TargetProperty.SchedulerOption

from org.lflang.tests.Configurators

from org.lflang.tests.TestBase

from org.lflang.tests.TestRegistry.TestCategory

# 
#  
class CSchedulerTest(TestBase):
    """ generated source for class CSchedulerTest """
    def __init__(self):
        """ generated source for method __init__ """
        super(CSchedulerTest, self).__init__(Target.C)

    #      * Swap the default runtime scheduler with other supported versions and
    #      * run all the supported tests. Only run tests for a specific non-default
    #      * scheduler if specified using a system property (e.g., -Dscheduler=GEDF_NP).
    #      
    def runWithNonDefaultSchedulers(self):
        """ generated source for method runWithNonDefaultSchedulers """
        categories = EnumSet.of(TestCategory.CONCURRENT, TestCategory.MULTIPORT)
        #  Add federated and docker tests if supported
        if not isWindows():
            categories.append(TestCategory.FEDERATED)
            if isLinux():
                categories.append(TestCategory.DOCKER_FEDERATED)
        name = System.getProperty("scheduler")
        if name != None:
            option = EnumSet.allOf(SchedulerOption.__class__).stream().filter(it.name() == name).findFirst()
            if option.isPresent():
                self.runTest(option.get(), categories)
            else:
                raise RuntimeException("Cannot find runtime scheduler called " + name)
        else:
            for scheduler in EnumSet.allOf(SchedulerOption.__class__):
                if scheduler == SchedulerOption.getDefault():
                    continue 
                self.runTest(scheduler, categories)

    def runTest(self, scheduler, categories):
        """ generated source for method runTest """
        self.runTestsForTargets(Message.DESC_SCHED_SWAPPING + scheduler.__str__() + ".", categories.contains, True)
