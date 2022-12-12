#!/usr/bin/env python
""" generated source for module EclipseErrorReporter """
# 
#  * Copyright (c) 2019, The University of California at Berkeley. Copyright (c)
#  * 2019, TU Dresden
#  * 
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  * 
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  * 
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
#  * 
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  * POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.generator
# import java.io.IOException
# import java.nio.file.Path
# import org.eclipse.core.resources.IMarker
# import org.eclipse.core.resources.IResource
# import org.eclipse.core.runtime.CoreException
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.diagnostics.Severity
# import org.eclipse.xtext.validation.EObjectDiagnosticImpl
import logging
import sys

from include.overloading import overloaded
from lflang.cli.StandaloneErrorReporter import Path
from lflang.cli.StandaloneIssueAcceptor import EObjectDiagnosticImpl
from lflang.diagram.synthesis.util.LayoutPostProcessing import EObject
from lflang.generator.GeneratorBase import IMarker
from org.lflang import ErrorReporter

from org.lflang import FileConfig

from org.lflang.util import FileUtil

# 
#  * An error reporter that prints messages to the command line output and also
#  * sets markers in the Epoch IDE.
#  *
#  * This class should only be used in EPOCH Mode.
#  
class Severity:
    pass


class CoreException:
    pass


class IResource:
    pass


class EclipseErrorReporter(ErrorReporter):
    """ generated source for class EclipseErrorReporter """
    fileConfig = None
    errorsOccurred = False

    def __init__(self, fc):
        """ generated source for method __init__ """
        super().__init__()
        self.fileConfig = fc

    #  private val EObject.node get() = NodeModelUtils.getNode(this)
    #      * Report a warning or error on the specified object
    #      *
    #      * The caller should not throw an exception so execution can continue. This
    #      * will print the error message to stderr. If running in EPOCH mode
    #      * (within the Eclipse IDE), then this also adds a marker to the editor.
    #      * 
    #      * @param message  The error message.
    #      * @param severity One of IMarker.SEVERITY_ERROR or IMarker.SEVERITY_WARNING
    #      * @param obj      The Ecore object, or null if it is not known.
    #      
    @overloaded
    def report(self, message, severity, obj):
        """ generated source for method report """
        if obj != None:
            diagnostic = EObjectDiagnosticImpl(severity, None, message, obj, None, -1, None)
            line = diagnostic.getLine()
            file = None
            try:
                file = FileUtil.toPath(diagnostic.getUriToProblem())
            except IOError as e:
                pass
                #  just continue with null
            return self.report(message, severity, line, file)
        return self.report(message, severity, None, None)

    #      * Report a warning or error on the specified line of the specified file.
    #      *
    #      * The caller should not throw an exception so execution can continue. This
    #      * will print the error message to stderr. If running in EPOCH mode
    #      * (within the Eclipse IDE), then this also adds a marker to the editor.
    #      * 
    #      * @param message  The error message.
    #      * @param severity One of IMarker.SEVERITY_ERROR or IMarker.SEVERITY_WARNING or IMarker.SEVERITY_INFO
    #      * @param line     The line number or null if it is not known.
    #      * @param file     The file, or null if it is not known.
    #      
    @report.register(object, str, Severity, int, Path)
    def report_0(self, message, severity, line, file):
        """ generated source for method report_0 """
        isError = severity == logging.ERROR
        isInfo = severity == logging.INFO
        if isError:
            self.errorsOccurred = True
        header = "ERROR" if isError else ("INFO" if isInfo else "WARNING")
        if line == None or file == None:
            sys.stderr(header + ": " + message)
        else:
            sys.stderr(header + ": " + file + " line " + line + "\n" + message)
        #  Determine the iResource to report on
        iResource = FileUtil.getIResource(file) if file != None else None
        #  if we couldn't find an iResource (for whatever reason), then use the
        #  iResource of the main file
        if iResource == None:
            iResource = self.fileConfig.iResource
        #  Create a marker in the IDE for the error.
        #  See: https://help.eclipse.org/2020-03/index.jsp?topic=%2Forg.eclipse.platform.doc.isv%2Fguide%2FresAdv_markers.html
        try:
            marker = iResource.createMarker(IMarker.PROBLEM)
            #  Mark as LF compilation marker to be able to remove marker at next compile run
            marker.setAttribute(self.__class__.__name__, True)
            marker.setAttribute(IMarker.MESSAGE, message)
            marker.setAttribute(IMarker.LINE_NUMBER, 1 if line == None else line)
            marker.setAttribute(IMarker.LOCATION, "1" if line == None else str(line)())
            marker.setAttribute(IMarker.SEVERITY,
                                IMarker.SEVERITY_ERROR if isError else
                                    (IMarker.SEVERITY_INFO if isInfo else IMarker.SEVERITY_WARNING)
                                )
            marker.setAttribute(IMarker.PRIORITY, IMarker.PRIORITY_HIGH)
            marker.setAttribute(IMarker.USER_EDITABLE, False)
        except CoreException as e:
            sys.stderr("WARNING: Setting markers in the IDE failed:\n" + str(e)())
        return header + ": " + message

    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """
        return self.report(message, logging.ERROR, None, None)

    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """
        return self.report(message, logging.WARNING, None, None)

    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """
        return self.report(message, logging.INFO, None, None)

    @reportError.register(object, EObject, str)
    def reportError_0(self, obj, message):
        """ generated source for method reportError_0 """
        return self.report(message, logging.ERROR, obj)

    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, obj, message):
        """ generated source for method reportWarning_0 """
        return self.report(message, logging.WARNING, obj)

    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, obj, message):
        """ generated source for method reportInfo_0 """
        return self.report(message, logging.INFO, obj)

    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """
        return self.report(message, logging.ERROR, line, file)

    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """
        return self.report(message, logging.WARNING, line, file)

    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """
        return self.report(message, logging.INFO, line, file)

    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return self.errorsOccurred

    def clearMarkers(self):
        """ generated source for method clearMarkers """
        try:
            resource = FileUtil.getIResource(self.fileConfig.srcFile)
            markers = resource.findMarkers(None, True, IResource.DEPTH_INFINITE)
            for marker in markers:
                if marker.getAttribute(self.__class__.__name__, False):
                    marker.delete()
        except Exception as e:
            self.reportWarning("Deleting markers in the IDE failed: $e")
