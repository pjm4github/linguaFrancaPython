#!/usr/bin/env python
""" generated source for module StandaloneErrorReporter """
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
# package: org.lflang.cli
# import java.nio.file.Path
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.diagnostics.Severity
from include.MiscClasses import LfIssue
from include.overloading import overloaded
from lflang.diagram.synthesis.util.LayoutPostProcessing import EObject
from org.lflang import ErrorReporter
# import com.google.inject.Inject
import logging
# 
#  * An error reporter that forwards all messages to an {@link IssueCollector}.
#  * They'll be sorted out later.
#  
class Path:
    pass


class StandaloneErrorReporter(ErrorReporter):
    """ generated source for class StandaloneErrorReporter """
    issueAcceptor = None

    def reportWithNode(self, message, severity, obj):
        """ generated source for method reportWithNode """
        self.issueAcceptor.accept(severity, message, obj, None, 0, None)
        return message

    def reportSimpleFileCtx(self, message, severity, line, path):
        """ generated source for method reportSimpleFileCtx """
        issue = LfIssue(message, severity, line, 1, line, 1, 0, path)
        self.issueAcceptor.accept(issue)
        #  Return a string that can be inserted into the generated code.
        return message

    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """
        return self.reportSimpleFileCtx(message, logging.ERROR, None, None)

    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """
        return self.reportSimpleFileCtx(message, logging.WARNING, None, None)

    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """
        return self.reportSimpleFileCtx(message, logging.INFO, None, None)

    @reportError.register(object, EObject, str)
    def reportError_0(self, obj, message):
        """ generated source for method reportError_0 """
        return self.reportWithNode(message, logging.ERROR, obj)

    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, obj, message):
        """ generated source for method reportWarning_0 """
        return self.reportWithNode(message, logging.WARNING, obj)

    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, obj, message):
        """ generated source for method reportInfo_0 """
        return self.reportWithNode(message, logging.INFO, obj)

    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """
        return self.reportSimpleFileCtx(message, logging.ERROR, line, file)

    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """
        return self.reportSimpleFileCtx(message, logging.WARNING, line, file)

    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """
        return self.reportSimpleFileCtx(message, logging.INFO, line, file)

    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return self.issueAcceptor.getErrorsOccurred()
