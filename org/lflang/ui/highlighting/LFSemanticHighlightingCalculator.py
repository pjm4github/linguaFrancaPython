#!/usr/bin/env python
""" generated source for module LFSemanticHighlightingCalculator """
# 
# Copyright (c) 2021, Kiel University.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.ui.highlighting
# import org.eclipse.xtext.ide.editor.syntaxcoloring.IHighlightedPositionAcceptor
# import org.eclipse.xtext.ide.editor.syntaxcoloring.ISemanticHighlightingCalculator
# import org.eclipse.xtext.parser.IParseResult
# import org.eclipse.xtext.resource.ILocationInFileProvider
# import org.eclipse.xtext.resource.XtextResource
# import org.eclipse.xtext.util.CancelIndicator

from org.lflang.lf import Model
# import com.google.inject.Inject

# 
#  * Syntax highlighting adjustments for LF.
#  *  
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class LFSemanticHighlightingCalculator(ISemanticHighlightingCalculator):
    """ generated source for class LFSemanticHighlightingCalculator """
    locator = None

    #      * {@inheritDoc}
    #      
    def provideHighlightingFor(self, resource, acceptor, cancelIndicator):
        """ generated source for method provideHighlightingFor """
        if resource == None or self.locator == None:
            return
        parseResult = resource.getParseResult()
        if parseResult == None or parseResult.getRootASTElement() == None:
            return
        model = parseResult.getRootASTElement()
