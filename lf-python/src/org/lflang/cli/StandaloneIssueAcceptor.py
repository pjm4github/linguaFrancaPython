#!/usr/bin/env python
""" generated source for module StandaloneIssueAcceptor """
# package: org.lflang.cli
# 
#  *
#
from include.overloading import overloaded

class StandaloneIssueAcceptor(ValidationMessageAcceptor):
    """ generated source for class StandaloneIssueAcceptor """
    collector = None

    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return self.collector.getErrorsOccurred()

    @overloaded
    def accept(self, lfIssue):
        """ generated source for method accept """
        self.collector.accept(lfIssue)

    @accept.register(object, Severity, str, EObject, EStructuralFeature, int, str, A)
    def accept_0(self, severity, message, object, feature, index, code_, *issueData):
        """ generated source for method accept_0 """
        diagnostic = EObjectDiagnosticImpl(severity, code_, message, object, feature, index, issueData)
        lfIssue = LfIssue(message, severity, diagnostic.getLine(), diagnostic.getColumn(), diagnostic.getLineEnd(), diagnostic.getColumnEnd(), diagnostic.getLength(), getPath(diagnostic))
        self.accept(lfIssue)

    #      * Best effort to get a fileName. May return null.
    #      
    def getPath(self, diagnostic):
        """ generated source for method getPath """
        file = None
        try:
            file = FileUtil.toPath(diagnostic.getUriToProblem())
        except IOError as e:
            pass
            #  just continue with null
        return file

    @accept.register(object, Severity, str, EObject, int, int, str, A)
    def accept_1(self, severity, message, object, offset, length, code_, *issueData):
        """ generated source for method accept_1 """
        raise TypeError("not implemented: range based diagnostics")

    @overloaded
    def acceptError(self, message, object, feature, index, code_, *issueData):
        """ generated source for method acceptError """
        self.accept(logging.ERROR, message, object, feature, index, code_, issueData)

    @acceptError.register(object, str, EObject, int, int, str, A)
    def acceptError_0(self, message, object, offset, length, code_, *issueData):
        """ generated source for method acceptError_0 """
        self.accept(logging.ERROR, message, object, offset, length, code_, issueData)

    @overloaded
    def acceptWarning(self, message, object, feature, index, code_, *issueData):
        """ generated source for method acceptWarning """
        self.accept(logging.WARNING, message, object, feature, index, code_, issueData)

    @acceptWarning.register(object, str, EObject, int, int, str, A)
    def acceptWarning_0(self, message, object, offset, length, code_, *issueData):
        """ generated source for method acceptWarning_0 """
        self.accept(logging.WARNING, message, object, offset, length, code_, issueData)

    @overloaded
    def acceptInfo(self, message, object, feature, index, code_, *issueData):
        """ generated source for method acceptInfo """
        self.accept(logging.INFO, message, object, feature, index, code_, issueData)

    @acceptInfo.register(object, str, EObject, int, int, str, A)
    def acceptInfo_0(self, message, object, offset, length, code_, *issueData):
        """ generated source for method acceptInfo_0 """
        self.accept(logging.INFO, message, object, offset, length, code_, issueData)
