#!/usr/bin/env python
""" generated source for module CycleVisualization """
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
# import com.google.common.collect.HashMultimap
# import com.google.inject.Inject
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KGraphElement
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import java.util.Map
# import java.util.Set
# import java.util.function_.Consumer
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.xtext.xbase.lib.Extension
from include.Multimap import HashMultimap
from org.lflang.diagram.synthesis import AbstractSynthesisExtensions

from org.lflang.generator import NamedInstance

from org.lflang.generator import ReactorInstance

from org.lflang.lf import Connection

import configparser
config = configparser.RawConfigParser()

# 
#  * Dependency cycle detection for Lingua Franca diagrams.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class NamedInstanceUtil:
    pass


class CycleVisualization(AbstractSynthesisExtensions):
    """ generated source for class CycleVisualization """
    #  Properties for marking diagram elements
    DEPENDENCY_CYCLE = config.get("org.lflang.diagram.synthesis.dependency.cycle", False)
    _utilityExtensions = None

    def detectAndHighlightCycles(self, rootReactorInstance, allReactorNodes, highlighter):
        """
        * Performs cycle detection based on the diagram's graph structure and applies given highlighting to the included elements
        :param rootReactorInstance:
        :param allReactorNodes:
        :param highlighter:
        :return:
        """
        """ generated source for method detectAndHighlightCycles """
        if rootReactorInstance.hasCycles() and highlighter != None:
            #  Highlight cycles
            #  A cycle consists of reactions and ports.
            cycleElementsByReactor = HashMultimap()
            cycles = rootReactorInstance.getCycles()
            for element in cycles:
                #  First find the involved reactor instances
                if isinstance(element, (ReactorInstance)):
                    cycleElementsByReactor.put(element, element)
                else:
                    cycleElementsByReactor.put(element.getParent(), element)
            for reactor in cycleElementsByReactor.keySet():
                node = allReactorNodes.get(reactor)
                if node != None:
                    node.setProperty(self.DEPENDENCY_CYCLE, True)
                    highlighter.accept(node)
                    reactorContentInCycle = cycleElementsByReactor.get(reactor)
                    #  Reactor edges
                    for edge in node.getOutgoingEdges():
                        if self.connectsCycleElements(edge, cycles):
                            edge.setProperty(self.DEPENDENCY_CYCLE, True)
                            highlighter.accept(edge)
                    #  Reactor ports
                    for port in node.getPorts():
                        if reactorContentInCycle.contains(NamedInstanceUtil.getLinkedInstance(port)):
                            port.setProperty(self.DEPENDENCY_CYCLE, True)
                            highlighter.accept(port)
                    #  Child Nodes
                    for childNode in node.getChildren():
                        if reactorContentInCycle.contains(NamedInstanceUtil.getLinkedInstance(childNode)) and not self._utilityExtensions.sourceIsReactor(childNode):
                            childNode.setProperty(self.DEPENDENCY_CYCLE, True)
                            highlighter.accept(childNode)
                            for edge in childNode.getOutgoingEdges():
                                if self.connectsCycleElements(edge, cycles):
                                    edge.setProperty(self.DEPENDENCY_CYCLE, True)
                                    highlighter.accept(edge)
            return True
        return False

    def connectsCycleElements(self, edge, cycle):
        """
        * Checks whether an edge connects two elements that are part of the cycle.
        * Assumes that the source node is always part of the cycle!

        :param edge:
        :param cycle:
        :return: True if 2 elements are part of cycle
        """
        # if source is not a reactor, there is nothing to check
        source_not_reactor = not self._utilityExtensions.sourceIsReactor(edge.getSource())
        # otherwise, the source port must be on the cycle
        source_on_cycle = cycle.contains(NamedInstanceUtil.getLinkedInstance(edge.getSourcePort()))
        #  leads to reactor port in cycle
        leads_to_reactor_port_on_cycle = self._utilityExtensions.sourceIsReactor(edge.getTarget()) and cycle.contains(NamedInstanceUtil.getLinkedInstance(edge.getTargetPort()))
        # leads to reaction in cycle
        leads_to_reaction_in_cycle = not self._utilityExtensions.sourceIsReactor(edge.getTarget()) and cycle.contains(NamedInstanceUtil.getLinkedInstance(edge.getTarget()))
        # Special case only for connections
        special_case_only_for_connections = not isinstance(self._utilityExtensions.sourceElement(edge), Connection)
        # If the edge represents a connections between two ports in the cycle (checked before),
        # then it is only included in the actual cycle, if it is neither delayed nor physical.
        only_included_if_neither_delayed_nor_physical = \
            self._utilityExtensions.sourceElement(edge).getDelay() == None \
             and not (self._utilityExtensions.sourceElement(edge)).isPhysical()

        return (source_not_reactor or source_on_cycle ) \
            and (leads_to_reactor_port_on_cycle or leads_to_reaction_in_cycle) \
            and (special_case_only_for_connections or only_included_if_neither_delayed_nor_physical)

