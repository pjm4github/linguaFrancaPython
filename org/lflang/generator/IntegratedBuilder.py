#!/usr/bin/env python
""" generated source for module IntegratedBuilder """
import logging
from abc import ABCMeta, abstractmethod
# package: org.lflang.generator
# import java.nio.file.Path
# import java.util.List
# import java.util.Properties
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.emf.ecore.resource.ResourceSet
# import org.eclipse.xtext.diagnostics.Severity
# import org.eclipse.xtext.generator.GeneratorDelegate
# import org.eclipse.xtext.generator.JavaIoFileSystemAccess
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.validation.CheckMode
# import org.eclipse.xtext.validation.IResourceValidator
# import org.eclipse.xtext.validation.Issue
from include.MiscClasses import CheckMode, CancelIndicator
from lflang.generator.GeneratorResult import GeneratorResult
from lflang.generator.LanguageServerErrorReporter import LanguageServerErrorReporter
from lflang.generator.MainContext import MainContext
from lflang.lf.Mode import Mode
from lflang.util.Properties import Properties
from org.lflang import ErrorReporter

from org.lflang import FileConfig

from org.lflang.generator import LFGeneratorContext

# import com.google.inject.Inject
# import com.google.inject.Provider

# 
#  * Manages Lingua Franca build processes that are requested
#  * from the language server.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#
#      * A {@code ProgressReporter} reports the progress of a build.
#
class ReportProgress:
    """ generated source for interface ReportProgress """
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply(self, message, percentage):
        """ generated source for method apply """


#  Note: This class is not currently used in response to
#   document edits, even though the validator and code
#   generator are invoked by Xtext in response to
#   document edits.
#      * A {@code ReportMethod} is a way of reporting issues.
#
class ReportMethod:
    """ generated source for interface ReportMethod """
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply(self, file, line, message):
        """ generated source for method apply """



class IntegratedBuilder:
    """ generated source for class IntegratedBuilder """
    START_PERCENT_PROGRESS = 0
    VALIDATED_PERCENT_PROGRESS = 33
    GENERATED_PERCENT_PROGRESS = 67
    COMPILED_PERCENT_PROGRESS = 100

    def __init__(self):
        #  ---------------------- INJECTED DEPENDENCIES ----------------------
        self.validator = None
        self.generator = None
        self.fileAccess = None
        self.resourceSetProvider = None

    #  ------------------------- PUBLIC METHODS --------------------------
    #      * Generates code from the Lingua Franca file {@code f}.
    #      * @param uri The URI of a Lingua Franca file.
    #      * @param mustComplete Whether the build must be taken to completion.
    #      * @return The result of the build.
    #      
    def run(self, uri, mustComplete, reportProgress, cancelIndicator):
        """ generated source for method run """
        #  FIXME: A refactoring of the following line is needed. This refactor will affect FileConfig and
        #   org.lflang.cli.Lfc. The issue is that there is duplicated code.
        #          fileAccess.setOutputPath(
        #              FileConfig.findPackageRoot(Path.of(uri.path()), s -> {}).resolve(FileConfig.DEFAULT_SRC_GEN_DIR).__str__()
        #          );
        parseRoots = self.getResource(uri).getContents()
        if parseRoots.isEmpty():
            return GeneratorResult.NOTHING
        errorReporter = LanguageServerErrorReporter(parseRoots.get(0))
        reportProgress.apply("Validating...", self.START_PERCENT_PROGRESS)
        self.validate(uri, errorReporter)
        reportProgress.apply("Code validation complete.", self.VALIDATED_PERCENT_PROGRESS)
        if cancelIndicator.isCanceled():
            return GeneratorResult.CANCELLED
        if errorReporter.getErrorsOccurred():
            return GeneratorResult.FAILED
        reportProgress.apply("Generating code...", self.VALIDATED_PERCENT_PROGRESS)
        return self.doGenerate(uri, mustComplete, reportProgress, cancelIndicator)

    #  ------------------------- PRIVATE METHODS ------------------------- 
    #      * Validates the Lingua Franca file {@code f}.
    #      * @param uri The URI of a Lingua Franca file.
    #      * @param errorReporter The error reporter.
    #      
    def validate(self, uri, errorReporter):
        """ generated source for method validate """
        for issue in self.validator.validate(self.getResource(uri), CheckMode.ALL, CancelIndicator.NullImpl):
            self.getReportMethod(errorReporter, issue.getSeverity()).apply(uri.path(), issue.getLineNumber(), issue.getMessage())

    #      * Generates code from the contents of {@code f}.
    #      * @param uri The URI of a Lingua Franca file.
    #      * @param mustComplete Whether the build must be taken to completion.
    #      * @param cancelIndicator An indicator that returns true when the build is
    #      *                        cancelled.
    #      * @return The result of the build.
    #      
    def doGenerate(self, uri, mustComplete, reportProgress, cancelIndicator):
        """ generated source for method doGenerate """

        def getFG(fileConfig):
            return fileConfig.resource.getContents().get(0)

        context: LFGeneratorContext = MainContext(
            Mode.LSP_SLOW if mustComplete else LFGeneratorContext.Mode.LSP_MEDIUM,
            cancelIndicator,
            reportProgress,
            Properties(),
            False,
            LanguageServerErrorReporter(getFG)
        )
        self.generator.generate(self.getResource(uri), self.fileAccess, context)
        return context.getResult()

    #      * Returns the resource corresponding to {@code uri}.
    #      * @param uri The URI of a Lingua Franca file.
    #      * @return The resource corresponding to {@code uri}.
    #      
    def getResource(self, uri):
        """ generated source for method getResource """
        return self.resourceSetProvider.get().getResource(uri, True)

    #      * Returns the appropriate reporting method for the
    #      * given {@code Severity}.
    #      * @param severity An arbitrary {@code Severity}.
    #      * @return The appropriate reporting method for
    #      * {@code severity}.
    #      
    def getReportMethod(self, errorReporter, severity):
        """ generated source for method getReportMethod """
        if severity == logging.ERROR:
            return errorReporter.reportError
        return errorReporter.reportWarning
