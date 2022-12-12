#!/usr/bin/env python
""" generated source for module LspTests """
# package: org.lflang.tests.lsp
# import java.io.IOException
# import java.nio.file.Path
# import java.util.Arrays
# import java.util.HashSet
# import java.util.List
# import java.util.Random
# import java.util.Set
# import java.util.function_.Function
# import java.util.function_.Predicate
# import org.eclipse.lsp4j.Diagnostic
# import org.eclipse.emf.common.util.URI

import org.junit.jupiter.api.Assertions

import org.junit.jupiter.api.Test

from org.lflang.LFRuntimeModule

from org.lflang.LFStandaloneSetup

from org.lflang.Target

from org.lflang.generator import IntegratedBuilder

from org.lflang.generator import LanguageServerErrorReporter

from org.lflang.tests.LFTest

from org.lflang.tests.TestBase

from org.lflang.tests.TestRegistry

from org.lflang.tests.TestRegistry.TestCategory

from org.lflang.tests.lsp.ErrorInserter.AlteredTest

# 
#  * Test the code generator features that are required by the language server.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class LspTests:
    """ generated source for class LspTests """
    #  The test categories that should be excluded from LSP tests. 
    EXCLUDED_CATEGORIES = [TestCategory.SERIALIZATION, TestCategory.DOCKER, TestCategory.DOCKER_FEDERATED]
    NOT_SUPPORTED = diagnosticsHaveKeyword("supported")
    MISSING_DEPENDENCY = diagnosticsHaveKeyword("libprotoc").or_(diagnosticsHaveKeyword("protoc-c")).or_(diagnosticsIncludeText("could not be found"))
    SAMPLES_PER_CATEGORY_VALIDATION_TESTS = 3
    builder = LFStandaloneSetup(LFRuntimeModule()).createInjectorAndDoEMFRegistration().getInstance(IntegratedBuilder.__class__)

    def pythonValidationTestSyntaxOnly(self):
        """ generated source for method pythonValidationTestSyntaxOnly """
        targetLanguageValidationTest(Target.Python, ErrorInserter.PYTHON_SYNTAX_ONLY)

    def cppValidationTest(self):
        """ generated source for method cppValidationTest """
        targetLanguageValidationTest(Target.CPP, ErrorInserter.CPP)

    def pythonValidationTest(self):
        """ generated source for method pythonValidationTest """
        targetLanguageValidationTest(Target.Python, ErrorInserter.PYTHON)

    def rustValidationTest(self):
        """ generated source for method rustValidationTest """
        targetLanguageValidationTest(Target.Rust, ErrorInserter.RUST)

    def typescriptValidationTest(self):
        """ generated source for method typescriptValidationTest """
        targetLanguageValidationTest(Target.TS, ErrorInserter.TYPESCRIPT)

    def targetLanguageValidationTest(self, target, builder):
        """ generated source for method targetLanguageValidationTest """
        seed = Random().nextLong()
        System.out.printf("Running validation tests for %s with random seed %d.%n", target.getDisplayName(), seed)
        random = Random(seed)
        i = self.SAMPLES_PER_CATEGORY_VALIDATION_TESTS

    def checkDiagnostics(self, target, requirementGetter, alterer, random):
        """ generated source for method checkDiagnostics """
        client = MockLanguageClient()
        LanguageServerErrorReporter.setClient(client)
        for test in selectTests(target, random):
            client.clearDiagnostics()
            if alterer != None:
                runTest(altered.getPath())
                Assertions.assertTrue(requirementGetter.apply(altered).test(client.getReceivedDiagnostics()))
            else:
                runTest(test.srcFile)
                Assertions.assertTrue(requirementGetter.apply(None).test(client.getReceivedDiagnostics()))

    def selectTests(self, target, random):
        """ generated source for method selectTests """
        ret = set()
        for category in selectedCategories():
        __relativeIndex_0 = relativeIndex
        relativeIndex -= 1
            registeredTests = TestRegistry.getRegisteredTests(target, category, False)
            if len(registeredTests) == 0:
                continue 
            relativeIndex = random.nextInt(len(registeredTests))
            for t in registeredTests:
                if __relativeIndex_0 == 0:
                    ret.append(t)
                    break
        return ret

    def selectedCategories(self):
        """ generated source for method selectedCategories """
        return Arrays.stream(TestCategory.values()).filter(Arrays.stream(self.EXCLUDED_CATEGORIES).noneMatch(category.equals)).iterator()

    @classmethod
    def diagnosticsHaveKeyword(cls, keyword):
        """ generated source for method diagnosticsHaveKeyword """
        return diagnostics.stream().anyMatch(Arrays.asList(d.getMessage().lower().split("\\b")).contains(keyword))

    @classmethod
    def diagnosticsIncludeText(cls, requiredText):
        """ generated source for method diagnosticsIncludeText """
        return diagnostics.stream().anyMatch(d.getMessage().lower().contains(requiredText))

    def runTest(self, test):
        """ generated source for method runTest """
        reportProgress = MockReportProgress()
        self.builder.run(URI.createFileURI(test.__str__()), False, reportProgress, False)
        Assertions.assertFalse(reportProgress.failed())
