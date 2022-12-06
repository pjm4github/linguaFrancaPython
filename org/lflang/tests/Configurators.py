#!/usr/bin/env python
""" generated source for module Configurators """
from abc import ABCMeta, abstractmethod
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
from org.lflang.tests.TestRegistry import TestCategory

# 
#  * Configuration procedures for {@link TestBase} methods.
#  *
#  * @author Clément Fournier
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class Configurator(object):
    #      * Configure the given test to use single-threaded execution.
    #      *
    #      * For targets that provide a threaded and an unthreaded runtime,
    #      * this configures using the unthreaded runtime. For targets that
    #      * do not distinguish threaded and unthreaded runtime, the number
    #      * of workers is set to 1.
    #      *
    #      * @param test The test to configure.
    #      * @return True if successful, false otherwise.
    #

    """ generated source for interface Configurator """
    __metaclass__ = ABCMeta

    #          * Apply a side effect to the given test case to change its default configuration.
    #          * Return true if configuration succeeded, false otherwise.
    #
    @abstractmethod
    def configure(self, test):
        """ generated source for method configure """
class Configurators(object):
    """ generated source for class Configurators """
    #  Test configuration function. 


    @classmethod
    def disableThreading(cls, test):
        """ generated source for method disableThreading """
        test.context.getArgs().setProperty("threading", "false")
        test.context.getArgs().setProperty("workers", "1")
        return True

    #      * Make no changes to the configuration.
    #      *
    #      * @param ignoredTest The test to configure.
    #      * @return True
    #      
    @classmethod
    def noChanges(cls, ignoredTest):
        """ generated source for method noChanges """
        return True

    #      * Given a test category, return true if it is compatible with single-threaded execution.
    #      
    @classmethod
    def compatibleWithThreadingOff(cls, category):
        """ generated source for method compatibleWithThreadingOff """
        #  CONCURRENT, FEDERATED, DOCKER_FEDERATED, DOCKER
        #  are not compatible with single-threaded execution.
        excluded = category == TestCategory.CONCURRENT or category == TestCategory.SERIALIZATION or category == TestCategory.FEDERATED or category == TestCategory.DOCKER_FEDERATED or category == TestCategory.DOCKER
        #  SERIALIZATION, TARGET, and ARDUINO tests are excluded on Windows.
        excluded |= TestBase.isWindows() and (category == TestCategory.TARGET or category == TestCategory.ARDUINO)
        return not excluded
