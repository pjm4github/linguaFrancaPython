#!/usr/bin/env python
""" generated source for module LinguaFrancaParsingTest """
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
# import com.google.inject.Inject
# import org.eclipse.xtext.testing.InjectWith
# import org.eclipse.xtext.testing.extensions.InjectionExtension
# import org.eclipse.xtext.testing.util.ParseHelper

from org.lflang.lf import LfPackage

from org.lflang.lf import Model

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions

import org.junit.jupiter.api.extension.ExtendWith

from org.lflang.tests.LFInjectorProvider

# 
#  * Test harness for ensuring that grammar captures
#  * all corner cases.
#  
@ExtendWith(InjectionExtension.__class__)
@InjectWith(LFInjectorProvider.__class__)
class LinguaFrancaParsingTest:
    """ generated source for class LinguaFrancaParsingTest """
    parser = None

    def checkForTarget(self):
        """ generated source for method checkForTarget """
        testCase = "\n            targett C;\n            reactor Foo {\n            }        "
        result = self.parser.parse(testCase)
        Assertions.assertNotNull(result)
        Assertions.assertFalse(result.eResource().getErrors().isEmpty(), "Failed to catch misspelled target keyword.")

    def testAttributes(self):
        """ generated source for method testAttributes """
        testCase = "\n                target C;\n                @label(\"somethign\", \"else\")\n                @ohio()\n                @a\n                @bdebd(a=\"b\")\n                @bd(\"abc\")\n                @bd(\"abc\")\n                @a(a=\"a\", b=\"b\")\n                @a(a=\"a\", b=\"b\")\n                main reactor {\n\n                }            "
        parseWithoutError(testCase)

    def testAttributeContexts(self):
        """ generated source for method testAttributeContexts """
        testCase = "\n                target C;\n                @a\n                main reactor(@b parm: int) {\n\n                                    @ohio reaction() {==}\n                    @ohio logical action f;\n                    @ohio timer t;\n                    @ohio input q: int;\n                    @ohio output q2: int;\n                }\n            "
        parseWithoutError(testCase)

    def parseWithoutError(self, s):
        """ generated source for method parseWithoutError """
        model = self.parser.parse(s)
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model.eResource().getErrors())
        return model
