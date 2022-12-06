#!/usr/bin/env python
""" generated source for module CliBase """
from packaging.requirements import URI
from pyjavaproperties import Properties
# package: org.lflang.cli
# import java.io.IOException
# import java.nio.file.Path
# import java.util.List
# import java.util.Properties
# import org.apache.commons.cli.CommandLine
# import org.apache.commons.cli.Option
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.emf.ecore.resource.ResourceSet
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.validation.CheckMode
# import org.eclipse.xtext.validation.IResourceValidator
# import org.eclipse.xtext.validation.Issue
from include.MiscClasses import CheckMode, CancelIndicator, LfIssue
from org.lflang.util import FileUtil
# import com.google.inject.Inject
# import com.google.inject.Provider

# 
#  * Base class for standalone CLI applications.
#  *
#  * @author {Marten Lohstroh <marten@berkeley.edu>}
#  * @author {Christian Menard <christian.menard@tu-dresden.de>}
#  * @author {Billy Bao <billybao@berkeley.edu>}
#  


class CliBase(object):
    def __init__(self):
        """ generated source for class CliBase """
        # Object for interpreting command line arguments.
        self.cmd = None

        # Used to collect all errors that happen during validation/generation.
        self.issueCollector = None

        # Used to report error messages at the end.
        self.reporter = None

        # Injected resource provider.
        self.resourceSetProvider = None

        # Injected resource validator.
        self.validator = None

    # Store command-line arguments as properties, to be passed on to the runtime.
    # @param passOptions Which options should be passed to the runtime.
    # @return Provided arguments in cmd as properties, which should be passed to the runtime.
    #       
    def filterProps(self, passOptions):
        """ generated source for method filterProps """
        props = Properties()
        for o in self.cmd.getOptions():
            if passOptions.contains(o):
                value = ""
                if o.hasArg():
                    value = o.getValue()
                props.setProperty(o.getLongOpt(), value)
        return props

    # If some errors were collected, print them and abort execution. Otherwise, return.
    #       
    def exitIfCollectedErrors(self):
        """ generated source for method exitIfCollectedErrors """
        if self.issueCollector.getErrorsOccurred():
            #  if there are errors, don't print warnings.
            errors = self.printErrorsIfAny()
            cause = "previous error" if len(errors) == 1 else f"{len(errors)} previous errors"
            self.reporter.printFatalErrorAndExit("Aborting due to " + cause)

    # If any errors were collected, print them, then return them.
    # @return A list of collected errors.
    #       
    def printErrorsIfAny(self):
        """ generated source for method printErrorsIfAny """
        errors = self.issueCollector.getErrors()
        errors.forEach(self.reporter.printIssue)
        return errors

    # Validates a given resource. If issues arise during validation,
    # these are recorded using the issue collector.
    #
    # @param resource The resource to validate.
    #       
    def validateResource(self, resource):
        """ generated source for method validateResource """
        assert resource != None
        issues = self.validator.validate(resource, CheckMode.ALL, CancelIndicator.NullImpl)
        for issue in issues:
            uri = issue.getUriToProblem()
            #  Issues may also relate to imported resources.
            try:
                self.issueCollector.accept(LfIssue(issue.getMessage(),
                                                   issue.getSeverity(),
                                                   issue.getLineNumber(),
                                                   issue.getColumn(),
                                                   issue.getLineNumberEnd(),
                                                   issue.getColumnEnd(),
                                                   issue.getLength(),
                                                   FileUtil.toPath(uri)))
            except IOError as e:
                self.reporter.printError("Unable to convert '" + uri + "' to path." + e)

    # Obtains a resource from a path. Returns null if path is not an LF file.
    # @param path The path to obtain the resource from.
    # @return The obtained resource. Set to null if path is not an LF file.
    #       
    def getResource(self, path):
        """ generated source for method getResource """
        set = self.resourceSetProvider.get()
        try:
            return set.getResource(URI.createFileURI(path.__str__()), True)
        except BaseException as e:
            return None
