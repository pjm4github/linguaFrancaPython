#!/usr/bin/env python
""" generated source for module RuntimeTest """
# package: org.lflang.tests
# import java.util.EnumSet
# import java.util.List
from include.overloading import overloaded
#import org.junit.jupiter.api.Assumptions
#import org.junit.jupiter.api.Test

from org.lflang import ASTUtils

from org.lflang import Target

# from org.lflang.tests import TestCategory

# 
#  * A collection of JUnit tests to perform on a given set of targets.
#  * 
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  *
#  
class RuntimeTest(TestBase):
    """ generated source for class RuntimeTest """
    #      * Construct a test instance that runs tests for a single target.
    #      *
    #      * @param target The target to run tests for.
    #      
    @overloaded
    def __init__(self, target):
        """ generated source for method __init__ """
        super(RuntimeTest, self).__init__(target)

    #      * Construct a test instance that runs tests for a list of targets.
    #      * @param targets The targets to run tests for.
    #      
    @__init__.register(object, List)
    def __init___0(self, targets):
        """ generated source for method __init___0 """
        super(RuntimeTest, self).__init__(targets)

    #      * Whether to enable {@link #runFederatedTests()}.
    #      
    def supportsFederatedExecution(self):
        """ generated source for method supportsFederatedExecution """
        return False

    #      * Whether to enable {@link #runTypeParameterTests()}.
    #      
    def supportsGenericTypes(self):
        """ generated source for method supportsGenericTypes """
        return False

    #      * Whether to enable {@link #runDockerTests()} and {@link #runDockerFederatedTests()}.
    #      
    def supportsDockerOption(self):
        """ generated source for method supportsDockerOption """
        return False

    def runGenericTests(self):
        """ generated source for method runGenericTests """
        runTestsForTargets(Message.DESC_GENERIC, TestCategory.GENERIC.equals, Configurators.noChanges, False)

    def runTargetSpecificTests(self):
        """ generated source for method runTargetSpecificTests """
        runTestsForTargets(Message.DESC_TARGET_SPECIFIC, TestCategory.TARGET.equals, Configurators.noChanges, False)

    def runMultiportTests(self):
        """ generated source for method runMultiportTests """
        runTestsForTargets(Message.DESC_MULTIPORT, TestCategory.MULTIPORT.equals, Configurators.noChanges, False)

    def runTypeParameterTests(self):
        """ generated source for method runTypeParameterTests """
        Assumptions.assumeTrue(self.supportsGenericTypes(), Message.NO_GENERICS_SUPPORT)
        runTestsForTargets(Message.DESC_TYPE_PARMS, TestCategory.GENERICS.equals, Configurators.noChanges, False)

    def runAsFederated(self):
        """ generated source for method runAsFederated """
        Assumptions.assumeTrue(self.supportsFederatedExecution(), Message.NO_FEDERATION_SUPPORT)
        categories = EnumSet.allOf(TestCategory.__class__)
        categories.removeAll(EnumSet.of(TestCategory.CONCURRENT, TestCategory.FEDERATED, TestCategory.MULTIPORT))
        runTestsFor(list(Target.C), Message.DESC_AS_FEDERATED, categories.contains, True)

    def runConcurrentTests(self):
        """ generated source for method runConcurrentTests """
        runTestsForTargets(Message.DESC_CONCURRENT, TestCategory.CONCURRENT.equals, Configurators.noChanges, False)

    def runFederatedTests(self):
        """ generated source for method runFederatedTests """
        Assumptions.assumeTrue(self.supportsFederatedExecution(), Message.NO_FEDERATION_SUPPORT)
        runTestsForTargets(Message.DESC_FEDERATED, TestCategory.FEDERATED.equals, Configurators.noChanges, False)

    #      * Run the tests for modal reactors.
    #      
    def runModalTests(self):
        """ generated source for method runModalTests """
        runTestsForTargets(Message.DESC_MODAL, TestCategory.MODAL_MODELS.equals, Configurators.noChanges, False)

    #  
    # Run docker tests, provided that the platform is Linux and the target supports Docker.
    # Skip if platform is not Linux or target does not support Docker.
    #       
    def runDockerTests(self):
        """ generated source for method runDockerTests """
        Assumptions.assumeTrue(isLinux(), Message.NO_DOCKER_TEST_SUPPORT)
        Assumptions.assumeTrue(self.supportsDockerOption(), Message.NO_DOCKER_SUPPORT)
        runTestsForTargets(Message.DESC_DOCKER, TestCategory.DOCKER.equals, Configurators.noChanges, False)

    #  
    # Run federated docker tests, provided that the platform is Linux, the target supports Docker,
    # and the target supports federated execution. If any of these requirements are not met, skip
    # the tests.
    #       
    def runDockerFederatedTests(self):
        """ generated source for method runDockerFederatedTests """
        Assumptions.assumeTrue(isLinux(), Message.NO_DOCKER_TEST_SUPPORT)
        Assumptions.assumeTrue(self.supportsDockerOption(), Message.NO_DOCKER_SUPPORT)
        Assumptions.assumeTrue(self.supportsFederatedExecution(), Message.NO_FEDERATION_SUPPORT)
        runTestsForTargets(Message.DESC_DOCKER_FEDERATED, TestCategory.DOCKER_FEDERATED.equals, Configurators.noChanges, False)

    def runWithThreadingOff(self):
        """ generated source for method runWithThreadingOff """
        Assumptions.assumeTrue(supportsSingleThreadedExecution(), Message.NO_SINGLE_THREADED_SUPPORT)
        self.runTestsForTargets(Message.DESC_SINGLE_THREADED, Configurators.compatibleWithThreadingOff, Configurators.disableThreading, True)
