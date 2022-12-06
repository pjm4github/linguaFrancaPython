#!/usr/bin/env python
""" generated source for module AbstractAction """
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
# package: org.lflang.diagram.synthesis.action
# import de.cau.cs.kieler.klighd.IAction
# import de.cau.cs.kieler.klighd.internal.util.KlighdInternalProperties
# import de.cau.cs.kieler.klighd.kgraph.KGraphElement
# import de.cau.cs.kieler.klighd.kgraph.KNode

from org.lflang.lf import Reactor

# 
#  * Abstract super class for diagram actions that provides some convince methods.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class IAction:
    pass


class KlighdInternalProperties:
    pass


class AbstractAction(IAction):
    """ generated source for class AbstractAction """
    def sourceElement(self, elem):
        """ generated source for method sourceElement """
        return elem.getProperty(KlighdInternalProperties.MODEL_ELEMEMT)

    def sourceIs(self, node, clazz):
        """ generated source for method sourceIs """
        return clazz.isInstance(self.sourceElement(node))

    def sourceIsReactor(self, node):
        """ generated source for method sourceIsReactor """
        return isinstance(node, Reactor)

    def sourceAsReactor(self, node):
        """ generated source for method sourceAsReactor """
        return self.sourceElement(node) if self.sourceIsReactor(node) else None
