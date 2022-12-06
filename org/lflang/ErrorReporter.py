#!/usr/bin/env python
""" generated source for module ErrorReporter """
from abc import ABCMeta, abstractmethod
# package: org.lflang
# import java.nio.file.Path
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.lsp4j.DiagnosticSeverity

from org.lflang.generator import Position

# 
#  * Interface for reporting errors.
#  *
#  * @author Edward A. Lee <eal@berkeley.edu>
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  * @author Christian Menard <christian.menard@tu-dresden.de>
#  
class ErrorReporter(object):
    """ generated source for interface ErrorReporter """
    __metaclass__ = ABCMeta
    #      * Report an error.
    #      *
    #      * @param message The error message.
    #      * @return a string that describes the error.
    #      
    @abstractmethod
    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """

    #      * Report a warning.
    #      *
    #      * @param message The warning message.
    #      * @return a string that describes the warning.
    #      
    @abstractmethod
    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """

    #      * Report an informational message.
    #      *
    #      * @param message The message to report
    #      * @return a string that describes the error
    #      
    @abstractmethod
    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """

    #      * Report an error on the specified parse tree object.
    #      *
    #      * @param object  The parse tree object.
    #      * @param message The error message.
    #      * @return a string that describes the error.
    #      
    @abstractmethod
    @reportError.register(object, EObject, str)
    def reportError_0(self, object, message):
        """ generated source for method reportError_0 """

    #      * Report a warning on the specified parse tree object.
    #      *
    #      * @param object  The parse tree object.
    #      * @param message The error message.
    #      * @return a string that describes the warning.
    #      
    @abstractmethod
    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, object, message):
        """ generated source for method reportWarning_0 """

    #      * Report an informational message on the specified parse tree object.
    #      *
    #      * @param object The parse tree object.
    #      * @param message The informational message
    #      * @return a string that describes the info
    #      
    @abstractmethod
    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, object, message):
        """ generated source for method reportInfo_0 """

    #      * Report an error at the specified line within a file.
    #      *
    #      * @param message The error message.
    #      * @param line    The one-based line number to report at.
    #      * @param file    The file to report at.
    #      * @return a string that describes the error.
    #      
    @abstractmethod
    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """

    #      * Report a warning at the specified line within a file.
    #      *
    #      * @param message The error message.
    #      * @param line    The one-based line number to report at.
    #      * @param file    The file to report at.
    #      * @return a string that describes the warning.
    #      
    @abstractmethod
    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """

    #      * Report an informational message at the specified line within a file.
    #      *
    #      * @param file The file to report at.
    #      * @param line The one-based line number to report at.
    #      * @param message The error message.
    #      * @return
    #      
    @abstractmethod
    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """

    #      * Report a message of severity {@code severity}.
    #      * @param file The file to which the message pertains, or {@code null} if the file is unknown.
    #      * @param severity the severity of the message
    #      * @param message the message to send to the IDE
    #      * @return a string that describes the diagnostic
    #      
    #      default String report(Path file, DiagnosticSeverity severity, String message) {
    #          switch (severity) {
    #          case Error:
    #              return reportError(message);
    #           case Warning:
    #           case Hint:
    #          case Information:
    #              return reportInfo(message);
    #           default:
    #               return reportWarning(message);
    #          }
    #      }
    #      * Report a message of severity {@code severity} that
    #      * pertains to line {@code line} of an LF source file.
    #      * @param file The file to which the message pertains, or {@code null} if the file is unknown.
    #      * @param severity the severity of the message
    #      * @param message the message to send to the IDE
    #      * @param line the one-based line number associated
    #      *             with the message
    #      * @return a string that describes the diagnostic
    #      
    #      default String report(Path file, DiagnosticSeverity severity, String message, int line) {
    #          switch (severity) {
    #          case Error:
    #              return reportError(file, line, message);
    #          case Warning:
    #          case Hint:
    #          case Information:
    #              return reportInfo(file, line, message);
    #          default:
    #              return reportWarning(file, line, message);
    #          }
    #      }
    #      * Report a message of severity {@code severity} that
    #      * pertains to the range [{@code startPos}, {@code endPos})
    #      * of an LF source file.
    #      * @param file The file to which the message pertains, or {@code null} if the file is unknown.
    #      * @param severity the severity of the message
    #      * @param message the message to send to the IDE
    #      * @param startPos the position of the first character
    #      *                 of the range of interest
    #      * @param endPos the position immediately AFTER the
    #      *               final character of the range of
    #      *               interest
    #      * @return a string that describes the diagnostic
    #      
    #       default String report(Path file, DiagnosticSeverity severity, String message, Position startPos, Position endPos) {
    #           return report(file, severity, message, startPos.getOneBasedLine());
    #       }
    #      * Check if errors where reported.
    #      *
    #      * @return true if errors where reported
    #      
    @abstractmethod
    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
