#!/usr/bin/env python
""" generated source for module RoundTripTests """
# package: org.lflang.tests.compiler
# import java.io.IOException
# import java.io.PrintWriter
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.StandardCopyOption
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.resource.XtextResource
# import org.eclipse.xtext.resource.XtextResourceSet
# import org.eclipse.xtext.testing.InjectWith
# import org.eclipse.xtext.testing.extensions.InjectionExtension

#import org.junit.jupiter.api.Assertions

#import org.junit.jupiter.api.Test

#import org.junit.jupiter.api.extension.ExtendWith

#import org.opentest4j.AssertionFailedError

from org.lflang import LFStandaloneSetup

from org.lflang import Target

from org.lflang.LFast import FormattingUtils

from org.lflang.LFast import IsEqual

from org.lflang.lf import Model

from org.lflang.tests import LFInjectorProvider

from org.lflang.tests import LFTest

from org.lflang.tests import TestRegistry

TestCategory = TestRegistry.Te
from org.lflang.tests.TestRegistry import TestRegistry.TestCategory
# import com.google.inject.Injector

@ExtendWith(InjectionExtension.__class__)
@InjectWith(LFInjectorProvider.__class__)
class RoundTripTests:
    """ generated source for class RoundTripTests """
    def roundTripTest(self):
        """ generated source for method roundTripTest """
        for target in Target.values():
            for category in TestCategory.values():
                for test in TestRegistry.getRegisteredTests(target, category, False):
                    run(test.srcFile)

    def run(self, file):
        """ generated source for method run """
        originalModel = parse(file)
        Assertions.assertTrue(originalModel.eResource().getErrors().isEmpty())
        smallLineLength = 20
        squishedTestCase = FormattingUtils.render(originalModel, smallLineLength)
        resultingModel = getResultingModel(file, squishedTestCase)
        Assertions.assertNotNull(resultingModel)
        if not resultingModel.eResource().getErrors().isEmpty():
            resultingModel.eResource().getErrors().forEach(System.err.println)
            Assertions.assertTrue(resultingModel.eResource().getErrors().isEmpty())
        if not IsEqual(originalModel).doSwitch(resultingModel):
            System.out.printf("The following is what %s looks like after applying formatting with the preferred line " + "length set to %d columns:%n%s%n%n", file, smallLineLength, squishedTestCase)
            raise AssertionError("The reformatted version of {:s} was not equivalent to the original file.".format(file.getFileName()))
        normalTestCase = FormattingUtils.render(originalModel)
        try:
            Assertions.assertEquals(Files.readString(file).replaceAll("\\r\\n?", "\n"), normalTestCase)
        except AssertionFailedError as e:
            System.err.printf("An assertion failed while checking that the content of %s is the same before and " + "after formatting. Check that %s is formatted according to lff and the " + "formatter provided with the VS Code extension.%n", file, file.getFileName())
            System.out.printf("The following is what %s looks like after applying formatting normally:%n%s%n%n", file.getFileName(), normalTestCase)
            raise e

    def getResultingModel(self, file, reformattedTestCase):
        """ generated source for method getResultingModel """
        swap = file.getParent().resolve(file.getFileName().__str__() + ".swp")
        Files.move(file, swap, StandardCopyOption.REPLACE_EXISTING)
        out.println(reformattedTestCase)
        resultingModel = parse(file)
        Files.move(swap, file, StandardCopyOption.REPLACE_EXISTING)
        return resultingModel

    def parse(self, file):
        """ generated source for method parse """
        injector = LFStandaloneSetup().createInjectorAndDoEMFRegistration()
        resourceSet = injector.getInstance(XtextResourceSet.__class__)
        resourceSet.addLoadOption(XtextResource.OPTION_RESOLVE_ALL, Boolean.TRUE)
        resource = resourceSet.getResource(URI.createFileURI(file.toFile().getAbsolutePath()), True)
        return resource.getContents().get(0)
