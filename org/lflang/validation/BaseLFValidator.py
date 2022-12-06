#!/usr/bin/env python
""" generated source for module BaseLFValidator """
# 
#  * Copyright (c) 2021, TU Dresden.
#  * 
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  * 
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  * 
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
#  * 
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  * POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.validation
# import java.lang.reflect.Method
# import java.util.Map
# import org.eclipse.emf.common.util.DiagnosticChain
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.validation.Check
# import org.eclipse.xtext.validation.CheckMode
# import org.eclipse.xtext.validation.CheckType
from lflang.validation.AbstractLFValidator import AbstractLFValidator
from org.lflang import ASTUtils

from org.lflang import TimeUnit

#from org.lflang.lf.LfPackage import Literals

from org.lflang.lf import Time

class BaseLFValidator(AbstractLFValidator):
    """ generated source for class BaseLFValidator """
    # @Check(CheckType.FAST)
    def checkTime(self, time):
        """ generated source for method checkTime """
        if not ASTUtils.isValidTime(time):
            raise Exception("Invalid time unit. " + "Should be one of " + TimeUnit.list() + ".", Literals.TIME__UNIT)

    # Provides convenient access to the inner state of the validator.
    # <p>
    # The validator only gives protected access to its own state. With
    # this class, we can grant access to the inner state to other objects.
    #
    # @author Christian Menard <christian.menard@tu-dresden.de>
    #
    class ValidatorStateAccess(object):
        """ generated source for class ValidatorStateAccess """
        def getCurrentObject(self):
            """ generated source for method getCurrentObject """
            return BaseLFValidator.self.getCurrentObject()

        def getCurrentMethod(self):
            """ generated source for method getCurrentMethod """
            return BaseLFValidator.self.getCurrentMethod()

        def getChain(self):
            """ generated source for method getChain """
            return BaseLFValidator.self.getChain()

        def getCheckMode(self):
            """ generated source for method getCheckMode """
            return BaseLFValidator.self.getCheckMode()

        def getContext(self):
            """ generated source for method getContext """
            return BaseLFValidator.self.getContext()
