#!/usr/bin/env python
""" generated source for module LinguaFrancaScopingTest """
#  Scoping unit tests. 
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

from org.lflang.lf import Model

import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions
# import org.eclipse.xtext.testing.validation.ValidationTestHelper

from org.lflang.lf import LfPackage
# import org.eclipse.xtext.linking.impl.XtextLinkingDiagnostic

from org.lflang.tests.LFInjectorProvider
# import org.eclipse.emf.ecore.resource.ResourceSet
# import org.eclipse.xtext.generator.JavaIoFileSystemAccess

import org.junit.jupiter.api.extension.ExtendWith

from org.lflang.generator import LFGenerator
# import com.google.inject.Provider

@ExtendWith(InjectionExtension.__class__)
@InjectWith(LFInjectorProvider.__class__)
class LinguaFrancaScopingTest(object):
    """ generated source for class LinguaFrancaScopingTest """
    #  * Test harness for ensuring that cross-references are 
    #  * established correctly and reported when faulty.
    #  
    parser = None
    generator = None
    fileAccess = None
    resourceSetProvider = None
    validator = None

    #      * Ensure that invalid references to contained reactors are reported.
    #      
    def unresolvedReactorReference(self):
        """ generated source for method unresolvedReactorReference """
        #  Java 17:
        #         Model model = """
        #             target C;
        #             reactor From {
        #                 output y:int;
        #             }
        #             reactor To {
        #                 input x:int;
        #             }
        #             
        #             main reactor {
        #                 a = new From();
        #                 d = new To();
        #                 s.y -> d.x;
        #             }
        #         """;
        #  Java 11:
        model = self.parser.parse(String.join(System.getProperty("line.separator"), "target C;", "reactor From {", "    output y:int;", "}", "reactor To {", "    input x:int;", "}", "", "main reactor {", "    a = new From();", "    d = new To();", "    s.y -> d.x;", "}"))
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Instantiation 's'")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Variable 'y'")

    def unresolvedHierarchicalPortReference(self):
        """ generated source for method unresolvedHierarchicalPortReference """
        model = self.parser.parse("\n\n            target C;\n            reactor From {\n                output y:int;\n            }\n            reactor To {\n                input x:int;\n            }\n\n            main reactor {\n                a = new From();\n                d = new To();\n                a.x -> d.y;\n            }\n        ")
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Variable 'x'")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Variable 'y'")

    def unresolvedReferenceInTriggerClause(self):
        """ generated source for method unresolvedReferenceInTriggerClause """
        model = self.parser.parse("\n            target C;\n            main reactor {\n                reaction(unknown) {==}\n            }\n        ")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Variable 'unknown'.")

    def unresolvedReferenceInUseClause(self):
        """ generated source for method unresolvedReferenceInUseClause """
        model = self.parser.parse("\n            target C;\n            main reactor {\n                reaction() unknown {==}\n            }\n        ")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Variable 'unknown'.")

    def unresolvedReferenceInEffectsClause(self):
        """ generated source for method unresolvedReferenceInEffectsClause """
        model = self.parser.parse("\n            target C;\n            main reactor {\n                reaction() -> unknown {==}\n            }\n        ")
        self.validator.assertError(model, LfPackage.eINSTANCE.getVarRef(), XtextLinkingDiagnostic.LINKING_DIAGNOSTIC, "Couldn't resolve reference to Variable 'unknown'.")
