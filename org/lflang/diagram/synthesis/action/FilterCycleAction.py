#!/usr/bin/env python
""" generated source for module FilterCycleAction """
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
# import com.google.common.collect.Iterables
# import com.google.common.collect.Iterators
# import de.cau.cs.kieler.klighd.IAction
# import de.cau.cs.kieler.klighd.ViewContext
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.krendering.KText
# import java.util.Iterator
# import java.util.List
# import java.util.WeakHashMap
# import java.util.function_.Predicate
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.xtext.xbase.lib.Functions.Function1
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.IteratorExtensions
# import org.eclipse.xtext.xbase.lib.ListExtensions

from org.lflang.diagram.synthesis import LinguaFrancaSynthesis

from org.lflang.diagram.synthesis.util import CycleVisualization
import configparser
config = configparser.RawConfigParser()

# 
#  * Action that filters the diagram for only those elements included in a cycle.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class KText:
    pass

class KNode:
    pass

class KEdge:
    pass


class AbstractAction:
    def createResult(self, v):
        self.a = v


class FilterCycleAction(AbstractAction):
    """ generated source for class FilterCycleAction """
    ID = "org.lflang.diagram.synthesis.action.FilterCycleAction"

    #      * Memory-leak-free cache of filtered states
    #      
    FILTERING_STATES = {}

    #      * INTERNAL property to mark filter button.
    #      
    FILTER_BUTTON = config.get("org.lflang.diagram.synthesis.action.cyclefilter.button", False)

    def execute(self, context):
        vc = context.getViewContext()
        all = vc.getOptionValue(self.SHOW_ALL_REACTORS)
        nodes = [vc.getViewModel().getChildren()]
        if isinstance(all, bool) and bool(all):
            new_nodes = []
            for it in nodes:
                new_nodes.append(it.getChildren())
            nodes = new_nodes

        if nodes.index(self.isCycleFiltered) > -1:
            for i, n in enumerate(nodes):
                nodes[i].apply(self.resetCycleFiltering)
            #  re-synthesize everything
            vc.getViewModel().getChildren().clear()
            vc.update()
        else:
            # filter
            #             nodes.forEach(it -> {
            #                 this.markCycleFiltered(it);
            #                 this.filterCycle(it);
            #             });
            for it in nodes:
                self.markCycleFiltered(it)
                self.filterCycle(it)
            #
            #   Function1<KNode, Boolean> knodeFilterButton = it -> {
            #       return it.getProperty(FILTER_BUTTON);
            #   };
            def knodeFilterButton(it):
                it.getProperty(self.FILTER_BUTTON)
            #
            #    Function1<KText, Boolean> ktextFilterButton = it -> {
            #        return it.getProperty(FILTER_BUTTON);
            #    };
            def ktextFilterButton(it):
                 it.getProperty(self.FILTER_BUTTON)
            #
            #  // switch filter label
            #  for (KNode node : IterableExtensions.filter(nodes, knodeFilterButton)) {
            #      Iterator<KText> ktexts = Iterators.filter(node.eAllContents(), KText.class);
            #      KText text = IteratorExtensions.findFirst(ktexts, ktextFilterButton);
            #      if (text != null) {
            #          text.setText(LinguaFrancaSynthesis.TEXT_ERROR_CYCLE_BTN_UNFILTER);
            #      }
            #  }

            for n in nodes:
                if knodeFilterButton(n):
                    ktexts= [c for c in n.eAllContents() if type(n) == type(KText)]
                    text = ktexts[0]
                    if text is not None:
                        text.setText(LinguaFrancaSynthesis.TEXT_ERROR_CYCLE_BTN_UNFILTER)


        return self.createResult(True)

    def filterCycle(self, root):
        """ generated source for method filterCycle """
        def knodeNotInCycle(it):
            return not it.getProperty(CycleVisualization.DEPENDENCY_CYCLE)

        def kedgeNotInCycle(it):
            return not it.getProperty(CycleVisualization.DEPENDENCY_CYCLE)

        root.getChildren().removeIf(knodeNotInCycle)
        for node in root.getChildren():
            node.getOutgoingEdges().removeIf(kedgeNotInCycle)
            self.filterCycle(node)

    def markCycleFiltered(self, node):
        """ generated source for method markCycleFiltered """
        source = self.sourceElement(node)
        if source != None:
            self.FILTERING_STATES.put(source, True)

    def resetCycleFiltering(self, node):
        """ generated source for method resetCycleFiltering """
        source = self.sourceElement(node)
        if source != None:
            self.FILTERING_STATES.remove(source)

    def isCycleFiltered(self, node):
        """ generated source for method isCycleFiltered """
        source = self.sourceElement(node)
        result = self.FILTERING_STATES.get(source)
        return False if result == None else result

    def markCycleFilterText(self, text, node):
        """ generated source for method markCycleFilterText """
        text.setProperty(self.FILTER_BUTTON, True)
        node.setProperty(self.FILTER_BUTTON, True)
