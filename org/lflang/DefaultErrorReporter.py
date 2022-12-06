#!/usr/bin/env python
""" generated source for module DefaultErrorReporter """
# package: org.lflang
# import org.eclipse.emf.ecore.EObject
# import java.nio.file.Path

# 
#  * Simple implementation of the ErrorReport interface that simply prints to
#  * standard out.
#
from include.overloading import overloaded
from lflang.ErrorReporter import ErrorReporter
from lflang.cli.StandaloneErrorReporter import Path
from lflang.diagram.synthesis.util.LayoutPostProcessing import EObject


class DefaultErrorReporter(ErrorReporter):
    """ generated source for class DefaultErrorReporter """
    errorsOccurred = False

    def println(self, s):
        """ generated source for method println """
        print(s)
        return s

    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """
        self.errorsOccurred = True
        return self.println("ERROR: " + message)

    @reportError.register(object, EObject, str)
    def reportError_0(self, object, message):
        """ generated source for method reportError_0 """
        self.errorsOccurred = True
        return self.println("ERROR: " + message)

    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """
        self.errorsOccurred = True
        return self.println("ERROR: " + message)

    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """
        return self.println("WARNING: " + message)

    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """
        return self.println("INFO: " + message)

    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, object, message):
        """ generated source for method reportWarning_0 """
        return self.println("WARNING: " + message)

    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, object, message):
        """ generated source for method reportInfo_0 """
        return self.println("INFO: " + message)

    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """
        return self.println("WARNING: " + message)

    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """
        return self.println("INFO: " + message)

    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return self.errorsOccurred
