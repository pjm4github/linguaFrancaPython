#!/usr/bin/env python
""" generated source for module SynthesisErrorReporter """
# 
# Copyright (c) 2020, Kiel University.
# *
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# *
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# *
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# *
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.diagram.synthesis.util
# import java.nio.file.Path
# import org.eclipse.emf.ecore.EObject
from include.overloading import overloaded
from lflang.cli.StandaloneErrorReporter import Path
from lflang.diagram.synthesis.util.LayoutPostProcessing import EObject
from org.lflang import ErrorReporter

# 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class SynthesisErrorReporter(ErrorReporter):
    """ generated source for class SynthesisErrorReporter """
    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """
        return None

    @reportError.register(object, EObject, str)
    def reportError_0(self, object, message):
        """ generated source for method reportError_0 """
        return None

    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """
        return None

    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """
        return None

    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, object, message):
        """ generated source for method reportWarning_0 """
        return None

    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """
        return None

    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """
        return None

    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, object, message):
        """ generated source for method reportInfo_0 """
        return None

    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """
        return None

    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return False
