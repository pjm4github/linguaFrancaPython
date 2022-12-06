#!/usr/bin/env python
""" generated source for module LinguaFrancaASTUtilsTest """
#  ASTUtils Unit Tests. 
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
# package: org.lflang.tests.compiler
import 

import 
# import java.util.List
# import java.util.Map
# import java.util.stream.Collectors

import javax.inject.Inject
# import org.eclipse.xtext.testing.InjectWith
# import org.eclipse.xtext.testing.extensions.InjectionExtension
# import org.eclipse.xtext.testing.util.ParseHelper

import org.junit.jupiter.api.Assertions

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.extension.ExtendWith

from org.lflang.ASTUtils

from org.lflang.lf import Instantiation

from org.lflang.lf import Literal

from org.lflang.lf import Model

from org.lflang.lf import Parameter

from org.lflang.lf import StateVar

from org.lflang.tests.LFInjectorProvider

# 
#  * Collection of unit tests on the ASTutils.
#  * 
#  * @author{Christian Menard <christian.menard@tu-dresden.de>}
#  
@ExtendWith(InjectionExtension.__class__)
@InjectWith(LFInjectorProvider.__class__)
class LinguaFrancaASTUtilsTest(object):
    """ generated source for class LinguaFrancaASTUtilsTest """
    parser = None

    #      * Test that isInititialized returns true for inititialized state variables
    #      
    def initializedState(self):
        """ generated source for method initializedState """
        #  Java 17:
        #         Model model = parser.parse("""
        #             target Cpp;
        #             main reactor Foo {
        #                 state a();
        #                 state b:int(3);
        #                 state c:int[](1,2,3);
        #                 state d(1 sec);
        #                 state e(1 sec, 2 sec, 3 sec);
        #             }
        #         """);
        #  Java 11:
        model = self.parser.parse(String.join(System.getProperty("line.separator"), "target Cpp;", "main reactor {", "    state a();", "    state b:int(3);", "    state c:int[](1,2,3);", "    state d(1 sec);", "    state e(1 sec, 2 sec, 3 sec);", "}"))
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model.eResource().getErrors())
        for obj in model.eAllContents():
            if isinstance(obj, (StateVar)):
                Assertions.assertTrue(isInitialized(obj))

    def uninitializedState(self):
        """ generated source for method uninitializedState """
        model = self.parser.parse(String.join(System.getProperty("line.separator"), "target Cpp;", "main reactor {", "    state a;", "    state b:int;", "    state c:int[];", "    state d:time;", "    state e:time;", "}"))
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model.eResource().getErrors())
        for obj in model.eAllContents():
            if isinstance(obj, (StateVar)):
                Assertions.assertFalse(isInitialized(obj))

    def getInsts(self, model):
        """ generated source for method getInsts """
        return asStream(model.eAllContents())

    def initialValue(self):
        """ generated source for method initialValue """
        model = self.parser.parse(String.join(System.getProperty("line.separator"), "target C;", "reactor A(x:int(1)) {}", "reactor B(y:int(2)) {", "    a1 = new A(x = y);", "    a2 = new A(x = -1);", "}", "reactor C(z:int(3)) {", "    b1 = new B(y = z);", "    b2 = new B(y = -2);", "}"))
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model.eResource().getErrors())
        map = self.getInsts(model)
        for obj in model.eAllContents():
            if isinstance(obj, (Parameter)):
                parameter = obj
                if parameter.__name__ == "x":
                    values = ASTUtils.initialValue(parameter, None)
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "1")
                    values = ASTUtils.initialValue(parameter, list(map.get("a1")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "2")
                    values = ASTUtils.initialValue(parameter, list(map.get("a2")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "-1")
                    values = ASTUtils.initialValue(parameter, list(map.get("a1"), map.get("b1")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "3")
                    values = ASTUtils.initialValue(parameter, list(map.get("a2"), map.get("b1")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "-1")
                    values = ASTUtils.initialValue(parameter, list(map.get("a1"), map.get("b2")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "-2")
                    values = ASTUtils.initialValue(parameter, list(map.get("a2"), map.get("b2")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "-1")
                elif parameter.__name__ == "y":
                    values = ASTUtils.initialValue(parameter, None)
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "2")
                    Assertions.assertThrows(IllegalArgumentException.__class__, ASTUtils.initialValue(parameter, list(map.get("a1"))))
                    values = ASTUtils.initialValue(parameter, list(map.get("b1")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "3")
                    values = ASTUtils.initialValue(parameter, list(map.get("b2")))
                    Assertions.assertInstanceOf(Literal.__class__, values.get(0))
                    Assertions.assertEquals((values.get(0)).getLiteral(), "-2")
