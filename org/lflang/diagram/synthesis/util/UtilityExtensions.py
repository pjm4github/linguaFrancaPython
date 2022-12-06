#!/usr/bin/env python
""" generated source for module UtilityExtensions """
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
# import java.util.ArrayList
# import java.util.Arrays
# import java.util.List
# import org.eclipse.elk.core.math.ElkMargin
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.elk.core.util.IndividualSpacings
# import org.eclipse.xtext.nodemodel.ICompositeNode
# import org.eclipse.xtext.nodemodel.util.NodeModelUtils
# import org.eclipse.xtext.xbase.lib.Extension
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.StringExtensions

# import de.cau.cs.kieler.klighd.internal.util.KlighdInternalProperties
# import de.cau.cs.kieler.klighd.kgraph.KGraphElement
# import de.cau.cs.kieler.klighd.kgraph.KGraphFactory
# import de.cau.cs.kieler.klighd.kgraph.KIdentifier
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared

# 
#  * Extension class that provides various utility methods for the synthesis.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#

from lflang.LFast.Nodemodels import NodeModelUtils
from lflang.diagram.synthesis.AbstractSynthesisExtensions import AbstractSynthesisExtensions
from lflang.diagram.synthesis.LinguaFrancaSynthesis import IterableExtensions
from lflang.diagram.synthesis.action.AbstractAction import KlighdInternalProperties
from lflang.diagram.synthesis.postprocessor.ReactionPortAdjustment import KGraphFactory
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import CoreOptions, ElkMargin
from lflang.lf import Reactor


class IndividualSpacings:
    pass


class UtilityExtensions(AbstractSynthesisExtensions):
    """ generated source for class UtilityExtensions """
    _kGraphFactory = KGraphFactory.eINSTANCE

    #      * Returns true if the reactor is the primary reactor
    #      
    def isMainOrFederated(self, reactor):
        """ generated source for method isMainOrFederated """
        return reactor.isMain() or reactor.isFederated()

    #      * Returns true if the instance is a bank of reactors
    #      
    #     def boolean isBank(Instantiation ins) {
    #         return ins?.widthSpec !== null ? ins.widthSpec.width !== 1 : false
    #     }
    #      * Returns true if the reactor as has inner reactions or instances
    #      
    def hasContent(self, reactor):
        """ generated source for method hasContent """
        return not reactor.reactions.isEmpty() or not reactor.instantiations().isEmpty()

    #      *
    #      
    def isRoot(self, ri):
        """ generated source for method isRoot """
        return ri.getParent() == None

    #      * Trims the hostcode of reactions.
    #      
    def trimCode(self, tokenizedCode):
        """ generated source for method trimCode """
        if tokenizedCode == None or len(tokenizedCode.getBody())==0:
            return ""
        try:

            node = NodeModelUtils.findActualNodeFor(tokenizedCode)
            code_ = node.getText() if node != None else None
            contentStart = 0
            lines = []
            #             Arrays.stream(code.split("\n")).dropWhile(line -> !line.contains("{=")).forEachOrdered(lines.add);
            #  Remove start pattern
            if not lines.isEmpty():
                if IterableExtensions.head(lines).trim() == "{=":
                    lines.remove(0)
                else:
                    lines.set(0, IterableExtensions.head(lines).replace("{=", "").trim())
                    contentStart = 1
            if not lines.isEmpty():
                if IterableExtensions.last(lines).trim() == "=}":
                    lines.remove(len(lines) - 1)
                else:
                    lines.set(len(lines) - 1, IterableExtensions.last(lines).replace("=}", ""))
            indentation = None
            while indentation == None and len(lines) > contentStart:
                firstLine = lines.get(contentStart)
                trimmed = firstLine.trim()
                if trimmed.isEmpty():
                    lines.set(contentStart, "")
                    contentStart += 1
                else:
                    firstCharIdx = firstLine.indexOf(trimmed.charAt(0))
                    indentation = firstLine.substring(0, firstCharIdx)
            if not lines.isEmpty():
                i = 0
                while i < len(lines):
                    if lines.get(i).startsWith(indentation):
                        lines.set(i, lines.get(i).substring(len(indentation)))
                    i += 1
            return "\n".join(lines)
        except Exception as e:
            e.printStackTrace()
            return tokenizedCode.getBody()

    def setID(self, kge, id):
        """ generated source for method setID """
        identifier = self._kGraphFactory.createKIdentifier()
        identifier.setId(id)
        return kge.getData().append(identifier)

    def sourceElement(self, elem):
        """ generated source for method sourceElement """
        return elem.getProperty(KlighdInternalProperties.MODEL_ELEMEMT)

    def sourceIsReactor(self, node):
        """ generated source for method sourceIsReactor """
        return isinstance(node, Reactor)

    def getPortMarginsInitIfAbsent(self, node):
        """ generated source for method getPortMarginsInitIfAbsent """
        spacing = node.getProperty(CoreOptions.SPACING_INDIVIDUAL)
        if spacing == None:
            spacing = IndividualSpacings()
            node.setProperty(CoreOptions.SPACING_INDIVIDUAL, spacing)
        margin = spacing.getProperty(CoreOptions.SPACING_PORTS_SURROUNDING)
        if margin == None:
            margin = ElkMargin()
            node.setProperty(CoreOptions.SPACING_PORTS_SURROUNDING, margin)
        return margin
