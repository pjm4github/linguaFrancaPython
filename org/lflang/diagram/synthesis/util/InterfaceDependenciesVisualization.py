#!/usr/bin/env python
""" generated source for module InterfaceDependenciesVisualization """
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
# import com.google.common.collect.ImmutableList
# import com.google.common.collect.Iterables
# import com.google.common.collect.Iterators
# import com.google.common.collect.Sets
# import com.google.inject.Inject
# import C.SynthesisOption
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KInvisibility
# import de.cau.cs.kieler.klighd.krendering.KPolyline
# import de.cau.cs.kieler.klighd.krendering.KRectangle
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import de.cau.cs.kieler.klighd.krendering.KRenderingFactory
# import de.cau.cs.kieler.klighd.krendering.LineStyle
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.krendering.extensions.KContainerRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KEdgeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KRenderingExtensions
# import de.cau.cs.kieler.klighd.syntheses.DiagramSyntheses
# import de.cau.cs.kieler.klighd.util.KlighdProperties
# import java.util.List
# import java.util.Random
# import java.util.Set
# import org.eclipse.elk.core.math.ElkMargin
# import org.eclipse.elk.core.math.Spacing
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.xtext.xbase.lib.Extension
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.IteratorExtensions
# import org.eclipse.xtext.xbase.lib.Pair
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import KRenderingFactory
from org.lflang.diagram.synthesis import AbstractSynthesisExtensions

from org.lflang.diagram.synthesis import LinguaFrancaSynthesis

from org.lflang.diagram.synthesis.styles import LinguaFrancaShapeExtensions

from org.lflang.diagram.synthesis.styles import LinguaFrancaStyleExtensions
import configparser
config = configparser.RawConfigParser()

# 
#  * Utility class to handle dependency edges for collapsed reactors in Lingua Franca diagrams.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class SynthesisOption:
    pass


class KRendering:
    pass


class KInvisibility:
    pass


class KContainerRendering:
    pass


class ElkMargin:
    pass


class CoreOptions:
    pass


class DiagramSyntheses:
    pass


class LineStyle:
    pass



class InterfaceDependenciesVisualization(AbstractSynthesisExtensions):
    """ generated source for class InterfaceDependenciesVisualization """
    #  Related synthesis option
    SHOW_INTERFACE_DEPENDENCIES = SynthesisOption.createCheckOption("Port Dependencies in Collapsed Reactors", False).setCategory(LinguaFrancaSynthesis.APPEARANCE)

    #  Properties for marking diagram elements
    INTERFACE_DEPENDENCY = config.get("org.lflang.linguafranca.diagram.synthesis.dependency.interface", False)
    _kEdgeExtensions = None
    _kRenderingExtensions = None
    _kContainerRenderingExtensions = None
    _linguaFrancaStyleExtensions = None
    _utilityExtensions = None

    #      * Updates the visibility of interface dependencies edges based on the expansion state.
    #      
    @classmethod
    def updateInterfaceDependencyVisibility(cls, node, expanded):
        """ generated source for method updateInterfaceDependencyVisibility """
        edges = []
        for it in node.getOutgoingEdges():
            if it.getProperty(cls.INTERFACE_DEPENDENCY):
                edges.append(it)
        renders = []
        for it in edges:
            if type(it.getData()) ==  type(KRendering):
                renders.append(it)
        for it in renders:
            the_styles = it.getStyles()
            inv = the_styles[-1]
            if type(inv) == type(KInvisibility):
                inv.setInvisible(expanded)
            else:
                inv = KRenderingFactory.eINSTANCE.createKInvisibility()
                it.getStyles().append(inv)

    def addInterfaceDependencies(self, node, expanded):
        """
        * Adds interface dependencies to the node if this option is active.
        * Visibility will be adjusted based on expansion state.
        :param node:
        :param expanded:
        :return:
        """
        """ generated source for method addInterfaceDependencies """
        marginInit = None
        if self.SHOW_INTERFACE_DEPENDENCIES.getBooleanValue():
            deps = self.getPortDependencies(node)
            if not deps.isEmpty():
                for pair in deps:
                    self.createDependencyEdge(pair, expanded)
                #  Fix content (label) of collapsed rendering
                contentContainer = None
                #                   = IterableExtensions.findFirst(
                #                          Iterables.filter(node.getData(), KContainerRendering.class),
                #                          it -> { return it.getProperty(KlighdProperties.COLLAPSED_RENDERING); }
                #                  );
                if contentContainer != None:
                    if not contentContainer.getProperty(LinguaFrancaShapeExtensions.REACTOR_CONTENT_CONTAINER):
                        # contentContainer = IteratorExtensions.findFirst(

                        #     Iterators.filter(contentContainer.eAllContents(), KContainerRendering.class),
                        #     it -> { return it.getProperty(LinguaFrancaShapeExtensions.REACTOR_CONTENT_CONTAINER); }
                        # );
                        for it in contentContainer.eAllContents():
                            if type(it) == type(KContainerRendering):
                                contentContainer = it.getProperty(LinguaFrancaShapeExtensions.REACTOR_CONTENT_CONTAINER)
                    if contentContainer != None:
                        content = list(contentContainer.getChildren())
                        #  Put into two new containers such that they are not centered/maximized
                        firstContainer = self._kContainerRenderingExtensions.addRectangle(contentContainer)
                        self._kRenderingExtensions.setInvisible(firstContainer, True)
                        secondContainer = self._kContainerRenderingExtensions.addRectangle(firstContainer)
                        self._kRenderingExtensions.setInvisible(secondContainer, True)
                        self._kContainerRenderingExtensions.setGridPlacement(secondContainer, 1)
                        content.extend(secondContainer.getChildren())
                        self._kRenderingExtensions.setPointPlacementData(secondContainer, self._kRenderingExtensions.LEFT, 0, 0.5, self._kRenderingExtensions.TOP, 0, 0, self._kRenderingExtensions.H_CENTRAL, self._kRenderingExtensions.V_TOP, 0, 0, 0, 0)
                        #  Adjust ports separate dependency edges from label/content
                        if len(content) > 0:
                            marginInit = self._utilityExtensions.getPortMarginsInitIfAbsent(node).append(ElkMargin((len(content) * 20) - 8, 0, 0, 0))
        return marginInit

    def getPortDependencies(self, node):
        """
        * Find dependencies between ports.
        :param node:
        :return:
        """
        inputPorts = []
        for it in node.getPorts():
            if it.getProperty(LinguaFrancaSynthesis.REACTOR_INPUT):
                inputPorts.append(it)

        outputPorts = []
        for it in node.getPorts():
            if it.getProperty(LinguaFrancaSynthesis.REACTOR_OUTPUT):
                outputPorts.append(it)
        ins = []
        outs = []
        for ip in inputPorts:
            for op in outputPorts:
                ins.append(ip)
                outs.append(op)

        return (ins, outs)

    def createDependencyEdge(self, connection, expanded):
        """
        * Create an edges for interface dependencies and adjust visibility based on the expansion state of the node.
        :param connection:
        :param expanded:
        :return:
        """
        """ generated source for method createDependencyEdge """
        depEdge = self._kEdgeExtensions.createEdge()
        depEdge.setSource(connection.getKey().getNode())
        depEdge.setSourcePort(connection.getKey())
        depEdge.setTarget(connection.getValue().getNode())
        depEdge.setTargetPort(connection.getValue())
        depEdge.setProperty(InterfaceDependenciesVisualization.INTERFACE_DEPENDENCY, True)
        depEdge.setProperty(CoreOptions.NO_LAYOUT, True)
        #  no routing!
        DiagramSyntheses.suppressSelectability(depEdge)
        polyline = self._kEdgeExtensions.addPolyline(depEdge)
        self._kRenderingExtensions.setLineStyle(polyline, LineStyle.DOT)
        self._linguaFrancaStyleExtensions.noSelectionStyle(polyline)
        self._kRenderingExtensions.setInvisible(polyline, expanded)
        #  make sure there is a style to toggle!
        return depEdge
