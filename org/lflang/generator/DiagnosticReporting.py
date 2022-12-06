#!/usr/bin/env python
""" generated source for module DiagnosticReporting """
from abc import ABCMeta, abstractmethod
# package: org.lflang.generator
# import java.nio.file.Path
# import java.util.Map
# import org.eclipse.lsp4j.DiagnosticSeverity

from org.lflang.ErrorReporter import ErrorReporter

# 
#  * {@code DiagnosticReporting} provides utilities for
#  * reporting validation output.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class DiagnosticSeverity:
    pass


class DiagnosticReporting(object):
    """ generated source for class DiagnosticReporting """
    def __init__(self):
        """ generated source for method __init__ """
        #  utility class

    #      * A means of parsing the output of a validator.
    #      
    class Strategy(object):
        """ generated source for interface Strategy """
        __metaclass__ = ABCMeta
            #          * Parse the validation output and report any errors
        #          * that it contains.
        #          * @param validationOutput any validation output
        #          * @param errorReporter any error reporter
        #          * @param map the map from generated files to CodeMaps
        #          
        @abstractmethod
        def report(self, validationOutput, errorReporter, map):
            """ generated source for method report """

    #      * Format the given data as a human-readable message.
    #      * @param message An error message.
    #      * @param path The path of the source of the message.
    #      * @param position The position where the message originates.
    #      * @return The given data as a human-readable message.
    #      
    @classmethod
    def messageOf(cls, message, path, position):
        """ generated source for method messageOf """
        return "{:s} [{:s}:{:s}:{:s}]".format(message,
                                              path.getFileName().__str__(),
                                              position.getOneBasedLine(),
                                              position.getOneBasedColumn())

    #      * Convert {@code severity} into a {@code DiagnosticSeverity} using a heuristic that should be
    #      * compatible with many tools.
    #      * @param severity The string representation of a diagnostic severity.
    #      * @return The {@code DiagnosticSeverity} representation of {@code severity}.
    #      
    @classmethod
    def severityOf(cls, severity):
        """ generated source for method severityOf """
        severity = severity.lower()
        if severity.contains("error"):
            return DiagnosticSeverity.Error
        elif severity.contains("warning"):
            return DiagnosticSeverity.Warning
        elif severity.contains("hint") or severity.contains("help"):
            return DiagnosticSeverity.Hint
        else:
            return DiagnosticSeverity.Information
