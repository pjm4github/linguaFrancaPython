#!/usr/bin/env python
""" generated source for module AbstractSynthesisExtensions """
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
# package: org.lflang.diagram.synthesis
# import de.cau.cs.kieler.klighd.SynthesisOption
# import de.cau.cs.kieler.klighd.syntheses.AbstractDiagramSynthesis
# import javax.inject.Inject
# import org.eclipse.emf.ecore.EObject

# 
#  * Abstract super class for extension classes used in for the diagram synthesis that provides some convince methods.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class AbstractSynthesisExtensions(object):
    """ generated source for class AbstractSynthesisExtensions """
    delegate = None

    def getBooleanValue(self, option):
        """ generated source for method getBooleanValue """
        return self.delegate.getBooleanValue(option)

    def getFloatValue(self, option):
        """ generated source for method getFloatValue """
        return self.delegate.getFloatValue(option)

    def getObjectValue(self, option):
        """ generated source for method getObjectValue """
        return self.delegate.getObjectValue(option)

    def associateWith(self, derived, source):
        """ generated source for method associateWith """
        return self.delegate.associateWith(derived, source)

    # @SuppressWarnings("unchecked")
    def getRootSynthesis(self):
        """ generated source for method getRootSynthesis """
        return self.delegate
