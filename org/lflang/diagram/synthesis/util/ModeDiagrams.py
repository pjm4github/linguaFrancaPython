#!/usr/bin/env python
""" generated source for module ModeDiagrams """
# 
# Copyright (c) 2021, Kiel University.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES 
# LOSS OF USE, DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.diagram.synthesis.util
# import java.awt.Color
# import java.util.EnumSet
# import java.util.HashMap
# import java.util.HashSet
# import java.util.LinkedHashMap
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.stream.Collectors
# import org.eclipse.elk.alg.layered.options.CenterEdgeLabelPlacementStrategy
# import org.eclipse.elk.alg.layered.options.EdgeStraighteningStrategy
# import org.eclipse.elk.alg.layered.options.FixedAlignment
# import org.eclipse.elk.alg.layered.options.LayerConstraint
# import org.eclipse.elk.alg.layered.options.LayeredOptions
# import org.eclipse.elk.alg.layered.options.NodePlacementStrategy
# import org.eclipse.elk.core.math.ElkPadding
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.elk.core.options.Direction
# import org.eclipse.elk.core.options.EdgeRouting
# import org.eclipse.elk.core.options.PortConstraints
# import org.eclipse.elk.core.options.PortLabelPlacement
# import org.eclipse.elk.core.options.PortSide
# import org.eclipse.emf.ecore.util.EcoreUtil
# import org.eclipse.xtext.xbase.lib.Extension
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.Pair
# import com.google.common.collect.LinkedHashMultimap
# import com.google.inject.Inject
# import de.cau.cs.kieler.klighd.SynthesisOption
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KIdentifier
# import de.cau.cs.kieler.klighd.kgraph.KLabel
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.Colors
# import de.cau.cs.kieler.klighd.krendering.HorizontalAlignment
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KDecoratorPlacementData
# import de.cau.cs.kieler.klighd.krendering.KEllipse
# import de.cau.cs.kieler.klighd.krendering.KPolyline
# import de.cau.cs.kieler.klighd.krendering.KRectangle
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import de.cau.cs.kieler.klighd.krendering.KRenderingFactory
# import de.cau.cs.kieler.klighd.krendering.KText
# import de.cau.cs.kieler.klighd.krendering.LineStyle
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.krendering.extensions.KContainerRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KEdgeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KLabelExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KNodeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPolylineExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPortExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KRenderingExtensions
# import de.cau.cs.kieler.klighd.labels.decoration.ITextRenderingProvider
# import de.cau.cs.kieler.klighd.labels.decoration.LabelDecorationConfigurator
# import de.cau.cs.kieler.klighd.labels.decoration.LinesDecorator
# import de.cau.cs.kieler.klighd.labels.decoration.RectangleDecorator
# import de.cau.cs.kieler.klighd.syntheses.DiagramSyntheses
# import de.cau.cs.kieler.klighd.util.KlighdProperties

# 
# Transformations to support modes in the Lingua Franca diagram synthesis.
#
# @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#
from include.KeilerClasses import KNodeExtensions, KEdgeExtensions, KPortExtensions, KLabelExtensions, \
    KPolylineExtensions, KRenderingExtensions, KContainerRenderingExtensions, KRenderingFactory, KlighdProperties
from include.MiscClasses import ElkPadding, LinkedHashSet, HashSet
from include.Multimap import LinkedHashMap, LinkedHashMultimap, HashMap
from lflang.diagram.synthesis.AbstractSynthesisExtensions import AbstractSynthesisExtensions
from lflang.diagram.synthesis.LinguaFrancaSynthesis import LinguaFrancaSynthesis
from lflang.diagram.synthesis.action.MemorizingExpandCollapseAction import MemorizingExpandCollapseAction
from lflang.diagram.synthesis.styles.LinguaFrancaShapeExtensions import ITextRenderingProvider, RectangleDecorator, \
    PortConstraints, HorizontalAlignment, Direction, NodePlacementStrategy, EdgeRouting, EdgeStraighteningStrategy, \
    CenterEdgeLabelPlacementStrategy, PortSide, PortLabelPlacement
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import LabelDecorationConfigurator, \
    EcoreUtil, Colors, LinesDecorator, Color, LayerConstraint, FixedAlignment
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import SynthesisOption, DiagramSyntheses, \
    CoreOptions, LineStyle
from lflang.diagram.synthesis.util.LayoutPostProcessing import LayeredOptions
from lflang.diagram.synthesis.util.NamedInstanceUtil import NamedInstanceUtil
from lflang.generator.ReactorInstance import ReactorInstance
from lflang.lf.Action import Action
from lflang.lf.ModeTransition import ModeTransition
from lflang.lf.Reactor import Reactor
from lflang.lf.Timer import Timer




class ModeDiagrams(AbstractSynthesisExtensions):
    """ generated source for class ModeDiagrams """
    #  Related synthesis option
    MODES_CATEGORY = SynthesisOption.createCategory("Modes", False).setCategory(LinguaFrancaSynthesis.APPEARANCE)
    SHOW_TRANSITION_LABELS = SynthesisOption.createCheckOption("Transition Labels", True).setCategory(MODES_CATEGORY)
    INITIALLY_COLLAPSE_MODES = SynthesisOption.createCheckOption("Initially Collapse Modes", True).setCategory(MODES_CATEGORY)
    MODE_FG = Colors.SLATE_GRAY
    MODE_BG = Colors.SLATE_GRAY_3
    MODE_BG_ALPHA = 50
    
    def __init__(self):
        super.__init__()

        self._kNodeExtensions = KNodeExtensions()
        self._kEdgeExtensions = KEdgeExtensions()
        self._kPortExtensions = KPortExtensions()
        self._kLabelExtensions = KLabelExtensions()
        self._kPolylineExtensions = KPolylineExtensions()
        self._kRenderingExtensions = KRenderingExtensions()
        self._kContainerRenderingExtensions = KContainerRenderingExtensions()
        self._linguaFrancaShapeExtensions = None
        self._linguaFrancaStyleExtensions = None
        self._utilityExtensions = None
        self._layoutPostProcessing = None
        self._kRenderingFactory = KRenderingFactory.eINSTANCE
        self._onEdgeTransitionLabelConfigurator = None


    def hasContent(self, mode):
        """ generated source for method hasContent """
        return not mode.reactions.isEmpty() or not mode.instantiations.isEmpty()

    def addModeFigure(self, node, mode, expanded):
        """ generated source for method addModeFigure """
        padding = 8 if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_HYPERLINKS) else 6
        figure = self._kRenderingExtensions.addRoundedRectangle(node, 13, 13, 1)
        self._kContainerRenderingExtensions.setGridPlacement(figure, 1)
        self._kRenderingExtensions.setLineWidth(figure, 3 if mode.isInitial() else 1.5)
        self._kRenderingExtensions.setForeground(figure, self.MODE_FG)
        self._kRenderingExtensions.setBackground(figure, self.MODE_BG)
        background = self._kRenderingExtensions.getBackground(figure)
        background.setAlpha(self.MODE_BG_ALPHA)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        #  Invisible container
        container = self._kContainerRenderingExtensions.addRectangle(figure)
        self._kRenderingExtensions.setInvisible(container, True)
        bottomPadding = 4 if self.hasContent(mode) and expanded else padding
        from_ = self._kRenderingExtensions.from_(self._kRenderingExtensions.setGridPlacementData(container), 
                                                 self._kRenderingExtensions.LEFT, padding, 0, 
                                                 self._kRenderingExtensions.TOP, padding, 0)
        self._kRenderingExtensions.to(from_, self._kRenderingExtensions.RIGHT, padding, 0, 
                                      self._kRenderingExtensions.BOTTOM, bottomPadding, 0)
        #  Centered child container
        childContainer = self._kContainerRenderingExtensions.addRectangle(container)
        self._kRenderingExtensions.setInvisible(childContainer, True)
        self._kRenderingExtensions.setPointPlacementData(childContainer, self._kRenderingExtensions.LEFT, 
                                                         0, 0.5, self._kRenderingExtensions.TOP, 0, 0.5, 
                                                         self._kRenderingExtensions.H_CENTRAL, 
                                                         self._kRenderingExtensions.V_CENTRAL, 0, 0, 0, 0)
        self._kContainerRenderingExtensions.setGridPlacement(childContainer, 1)
        text = self._kContainerRenderingExtensions.addText(childContainer, mode.__name__)
        DiagramSyntheses.suppressSelectability(text)
        self._linguaFrancaStyleExtensions.underlineSelectionStyle(text)
        return figure

    def addModeContainerFigure(self, node):
        """ generated source for method addModeContainerFigure """
        rect = self._kRenderingExtensions.addRectangle(node)
        self._kRenderingExtensions.setLineWidth(rect, 1)
        self._kRenderingExtensions.setLineStyle(rect, LineStyle.DOT)
        self._kRenderingExtensions.setForeground(rect, self.MODE_FG)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(rect)
        return rect

    def addTransitionFigure(self, edge, transition):
        """ generated source for method addTransitionFigure """
        spline = self._kEdgeExtensions.addSpline(edge)
        self._kRenderingExtensions.setLineWidth(spline, 1.5)
        self._kRenderingExtensions.setForeground(spline, self.MODE_FG)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(spline)
        if transition.type == ModeTransition.HISTORY:
            self.addHistoryDecorator(spline)
        else:
            arrowDecorator = self._kPolylineExtensions.addHeadArrowDecorator(spline)
            self._kRenderingExtensions.setForeground(arrowDecorator, self.MODE_FG)
            self._kRenderingExtensions.setBackground(arrowDecorator, self.MODE_FG)
        if self.getBooleanValue(self.SHOW_TRANSITION_LABELS):
            self.associateWith(spline, transition.getDefinition())
            centerEdgeLabel = self._kLabelExtensions.addCenterEdgeLabel(edge, self.toTransitionLabel(transition))
            self.associateWith(centerEdgeLabel, transition.getDefinition())
            self.applyTransitionOnEdgeStyle(centerEdgeLabel)

    def toTransitionLabel(self, transition):
        """ generated source for method toTransitionLabel """
        text = ""
        #         text.append(transition.reaction.triggers.stream().map(t -> t.getDefinition().__name__).\
        #         collect(Collectors.joining(", ")))
        return text.__str__()

    #  ONLY for use in applyTransitionOnEdgeStyle
    def applyTransitionOnEdgeStyle(self, label):
        """ generated source for method applyTransitionOnEdgeStyle """
        if self._onEdgeTransitionLabelConfigurator == None:
            foreground = Color(self.MODE_FG.getRed(), self.MODE_FG.getGreen(), self.MODE_FG.getBlue())
            background = Color(Colors.GRAY_95.getRed(), Colors.GRAY_95.getGreen(), Colors.GRAY_95.getBlue())
            self._onEdgeTransitionLabelConfigurator = LabelDecorationConfigurator.create().withInlineLabels(True).\
                withLabelTextRenderingProvider(ITextRenderingProvider()).\
                addDecoratorRenderingProvider(RectangleDecorator.create().withBackground(background)).\
                addDecoratorRenderingProvider(LinesDecorator.create().withColor(foreground))
        self._onEdgeTransitionLabelConfigurator.applyTo(label)

    def addHistoryDecorator(self, line):
        """ generated source for method addHistoryDecorator """
        decorator = self._kPolylineExtensions.addHeadArrowDecorator(line)
        (decorator.getPlacementData()).setAbsolute((-15.0))
        ellipse = self._kContainerRenderingExtensions.addEllipse(line)
        self._kRenderingExtensions.setDecoratorPlacementData(ellipse, 16, 16, (-6), 1, False)
        self._kRenderingExtensions.setLineWidth(ellipse, 0.8)
        self._kRenderingExtensions.setForeground(ellipse, self.MODE_FG)
        self._kRenderingExtensions.setBackground(ellipse, Colors.WHITE)
        innerLine = self._kContainerRenderingExtensions.addPolyline(ellipse)
        self._kRenderingExtensions.setLineWidth(innerLine, 2)
        points = innerLine.getPoints()
        points.append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.LEFT, 
                                                                 5, 0, self._kRenderingExtensions.TOP, 4, 0))
        points.append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.LEFT, 
                                                                 5, 0, self._kRenderingExtensions.BOTTOM, 4, 0))
        points.append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.LEFT, 
                                                                 5, 0, self._kRenderingExtensions.TOP, 0, 0.5))
        points.append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.RIGHT, 
                                                                 5, 0, self._kRenderingExtensions.TOP, 0, 0.5))
        points.append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.RIGHT, 
                                                                 5, 0, self._kRenderingExtensions.BOTTOM, 4, 0))
        points.append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.RIGHT, 
                                                                 5, 0, self._kRenderingExtensions.TOP, 4, 0))
        self._kRenderingExtensions.setForeground(innerLine, self.MODE_FG)

    
    def handleModes(self, nodes, reactor):
        """ generated source for method handleModes """
        if not reactor.modes.isEmpty():
            modeNodes = LinkedHashMap()
            modeDefinitionMap = LinkedHashMap()
            for mode in reactor.modes:
                node = self._kNodeExtensions.createNode()
                self.associateWith(node, mode.getDefinition())
                NamedInstanceUtil.linkInstance(node, mode)
                self._utilityExtensions.setID(node, mode.uniqueID())
    
                modeNodes.put(mode, node)
                modeDefinitionMap.put(mode.getDefinition(), mode)
    
                #  Layout
                if mode.isInitial():
                    DiagramSyntheses.setLayoutOption(node, LayeredOptions.LAYERING_LAYER_CONSTRAINT, LayerConstraint.FIRST)
                #  Use general layout configuration of reactors
                self.getRootSynthesis().configureReactorNodeLayout(node, False)
                self._layoutPostProcessing.configureReactor(node)
                #  Adjust for modes
                DiagramSyntheses.setLayoutOption(node, CoreOptions.PORT_CONSTRAINTS, PortConstraints.FREE)
    
                expansionState = MemorizingExpandCollapseAction.getExpansionState(mode)
                test1 = expansionState if (expansionState is not None) else \
                    not self.getBooleanValue(ModeDiagrams.INITIALLY_COLLAPSE_MODES)
                # //
                DiagramSyntheses.setLayoutOption(node, KlighdProperties.EXPAND,  test1)
    
                #  Expanded Rectangle
                expandFigure = self.addModeFigure(node, mode, True)
                expandFigure.setProperty(KlighdProperties.EXPANDED_RENDERING, True)
                self._kRenderingExtensions.addDoubleClickAction(expandFigure, MemorizingExpandCollapseAction.ID)
    
                if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_HYPERLINKS):
                    #  Collapse button
                    textButton = self._linguaFrancaShapeExtensions.addTextButton(expandFigure, LinguaFrancaSynthesis.TEXT_HIDE_ACTION)
                    self._kRenderingExtensions.to(
                            self._kRenderingExtensions.fro(self._kRenderingExtensions.setGridPlacementData(textButton),
                                                       self._kRenderingExtensions.LEFT, 8, 0, self._kRenderingExtensions.TOP, 0, 0),
                            self._kRenderingExtensions.RIGHT, 8, 0, self._kRenderingExtensions.BOTTOM, 0, 0)
                    self._kRenderingExtensions.addSingleClickAction(textButton, MemorizingExpandCollapseAction.ID)
                    self._kRenderingExtensions.addDoubleClickAction(textButton, MemorizingExpandCollapseAction.ID)
    
                if LinguaFrancaSynthesis.SHOW_STATE_VARIABLES:
                    #  Add mode-local state variables
                    variables = mode.getDefinition().getStateVars()
                    if not variables.isEmpty():
                        rectangle = self._kContainerRenderingExtensions.addRectangle(expandFigure)
                        self._kRenderingExtensions.setInvisible(rectangle, True)
                        if not self.getBooleanValue(LinguaFrancaSynthesis.SHOW_HYPERLINKS):
                            self._kRenderingExtensions.to(
                                    self._kRenderingExtensions.fro(
                                            self._kRenderingExtensions.setGridPlacementData(rectangle),
                                            self._kRenderingExtensions.LEFT, 6, 0,
                                            self._kRenderingExtensions.TOP, 0, 0),
                                    self._kRenderingExtensions.RIGHT, 6, 0,
                                    self._kRenderingExtensions.BOTTOM, 4, 0)
                        else:
                            self._kRenderingExtensions.to(
                                    self._kRenderingExtensions.fro(
                                            self._kRenderingExtensions.setGridPlacementData(rectangle),
                                            self._kRenderingExtensions.LEFT, 6, 0,
                                            self._kRenderingExtensions.TOP, 4, 0),
                                    self._kRenderingExtensions.RIGHT, 6, 0,
                                    self._kRenderingExtensions.BOTTOM, 0, 0)
                        self._kRenderingExtensions.setHorizontalAlignment(rectangle, HorizontalAlignment.LEFT)
                        self.getRootSynthesis().addStateVariableList(rectangle, variables)
    
                self._kContainerRenderingExtensions.addChildArea(expandFigure)
    
                #  Collapse Rectangle
                collapseFigure = self.addModeFigure(node, mode, False)
                collapseFigure.setProperty(KlighdProperties.COLLAPSED_RENDERING, True)
                if self.hasContent(mode):
                    self._kRenderingExtensions.addDoubleClickAction(collapseFigure, MemorizingExpandCollapseAction.ID)
    
                    if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_HYPERLINKS):
                        #  Expand button
                        textButton = self._linguaFrancaShapeExtensions.addTextButton(collapseFigure, LinguaFrancaSynthesis.TEXT_SHOW_ACTION)
                        self._kRenderingExtensions.to(self._kRenderingExtensions.fro(
                                    self._kRenderingExtensions.setGridPlacementData(textButton),
                                    self._kRenderingExtensions.LEFT, 8, 0, self._kRenderingExtensions.TOP, 0, 0),
                                self._kRenderingExtensions.RIGHT, 8, 0, self._kRenderingExtensions.BOTTOM, 8, 0)
                        self._kRenderingExtensions.addSingleClickAction(textButton, MemorizingExpandCollapseAction.ID)
                        self._kRenderingExtensions.addDoubleClickAction(textButton, MemorizingExpandCollapseAction.ID)

            modeChildren = LinkedHashMultimap()
            nodeModes = HashMap()
            for node in nodes:
                instance = NamedInstanceUtil.getLinkedInstance(node)
                if instance == None and node.getProperty(CoreOptions.COMMENT_BOX):
                    firstEdge = node.getOutgoingEdges().head()
                    if firstEdge != None and firstEdge.getTarget() != None:
                        instance = NamedInstanceUtil.getLinkedInstance(firstEdge.getTarget())
                if instance != None:
                    mode = instance.getMode(True)
                    modeChildren.put(mode, node)
                    nodeModes.put(node, mode)
                else:
                    modeChildren.put(None, node)

            modeContainer = self._kNodeExtensions.createNode()
            modeContainer.getChildren().addAll(modeNodes.values())
            modeContainerFigure = self.addModeContainerFigure(modeContainer)
            self._kRenderingExtensions.addDoubleClickAction(modeContainerFigure, MemorizingExpandCollapseAction.ID)

            #  Use general layout configuration of reactors
            self.getRootSynthesis().configureReactorNodeLayout(modeContainer, False)
            self._layoutPostProcessing.configureReactor(modeContainer)
            #  Adjust for state machine style
            #  Create alternating directions to make the model more compact
            DiagramSyntheses.setLayoutOption(modeContainer, CoreOptions.DIRECTION, Direction.DOWN)
            #  More state machine like node placement
            DiagramSyntheses.setLayoutOption(modeContainer, LayeredOptions.NODE_PLACEMENT_STRATEGY, NodePlacementStrategy.BRANDES_KOEPF)
            DiagramSyntheses.setLayoutOption(modeContainer, LayeredOptions.NODE_PLACEMENT_BK_FIXED_ALIGNMENT, FixedAlignment.BALANCED)
            DiagramSyntheses.setLayoutOption(modeContainer, LayeredOptions.NODE_PLACEMENT_BK_EDGE_STRAIGHTENING, EdgeStraighteningStrategy.IMPROVE_STRAIGHTNESS)
            #  Splines
            DiagramSyntheses.setLayoutOption(modeContainer, CoreOptions.EDGE_ROUTING, EdgeRouting.SPLINES)
            DiagramSyntheses.setLayoutOption(modeContainer, LayeredOptions.EDGE_LABELS_CENTER_LABEL_PLACEMENT_STRATEGY, CenterEdgeLabelPlacementStrategy.TAIL_LAYER)
            DiagramSyntheses.setLayoutOption(modeContainer, CoreOptions.SPACING_NODE_SELF_LOOP, 18.0)
            #  Unreachable states are unlikely
            DiagramSyntheses.setLayoutOption(modeContainer, CoreOptions.SEPARATE_CONNECTED_COMPONENTS, False)
            #  Equal padding
            DiagramSyntheses.setLayoutOption(modeContainer, CoreOptions.PADDING, ElkPadding(6))
            # if reactor.modes.stream().anyMatch(m -> m.transitions.stream().anyMatch(t -> t.type == ModeTransition.HISTORY)):
            #     #  Make additional space for history indicator
            #     DiagramSyntheses.setLayoutOption(modeContainer, LayeredOptions.SPACING_NODE_NODE_BETWEEN_LAYERS,
            #             modeContainer.getProperty(LayeredOptions.SPACING_NODE_NODE_BETWEEN_LAYERS)
            #             + (self.getBooleanValue(SHOW_TRANSITION_LABELS) ? 6.0 : 10.0))

            modeContainerPorts = HashMap()
            for mode in reactor.modes:
                modeNode = modeNodes.get(mode)
                edges = LinkedHashSet()
                #  add children
                for child in modeChildren.get(mode):
                    nodes.remove(child)
                    modeNode.getChildren().add(child)

                    edges.addAll(child.getIncomingEdges())
                    edges.addAll(child.getOutgoingEdges())

                #  add transitions
                representedTargets = HashSet()
                for transition in mode.transitions:
                    if not representedTargets.contains((transition.target, transition.type)):
                        edge = self._kEdgeExtensions.createEdge()
                        edge.setSource(modeNode)
                        edge.setTarget(modeNodes.get(transition.target))
                        self.addTransitionFigure(edge, transition)

                        if self.getBooleanValue(ModeDiagrams.SHOW_TRANSITION_LABELS):
                            self.associateWith(edge, transition.getDefinition())
                        else:#  Bundle similar transitions
                            representedTargets.add((transition.target, transition.type))

                #  handle cross hierarchy edges
                portCopies = HashMap()
                triggerCopies = HashMap()
                for edge in edges:
                    if not edge.getProperty(CoreOptions.NO_LAYOUT):
                        sourceNodeMode = nodeModes.get(edge.getSource())
                        if sourceNodeMode is None:
                            sourceNodeMode = nodeModes.get(edge.getSource().getParent())
                        sourceIsInMode = sourceNodeMode != None
                        targetNodeMode = nodeModes.get(edge.getTarget())
                        if targetNodeMode is None:
                            targetNodeMode = nodeModes.get(edge.getTarget().getParent())
                        targetIsInMode = targetNodeMode != None

                        if not sourceIsInMode or not targetIsInMode:
                            node = edge.getTarget() if sourceIsInMode else edge.getSource()

                            if node.getProperty(LinguaFrancaSynthesis.REACTION_SPECIAL_TRIGGER):
                                #  Duplicate trigger node
                                if not triggerCopies.containsKey(node):
                                    copy = EcoreUtil.copy(node)
                                    modeNode.getChildren().add(modeNode.getChildren().indexOf(edge.getTarget()), copy)
                                    triggerCopies.put(node, copy)

                                    #  Adjust copy
                                    for e in copy.getOutgoingEdges():
                                        e.setTarget(None)
                                        e.setTargetPort(None)
                                    copy.getOutgoingEdges().clear()
                                    # copy.getData().stream().filter(d -> d instanceof KIdentifier).forEach(d -> {
                                    #     kid = (KIdentifier) d
                                    #     kid.setId(kid.getId() + "_" + mode.getName())
                                    # })

                                newNode = triggerCopies.get(node)
                                edge.setSource(newNode)

                                #  Remove trigger on top level if only used in modes
                                if node.getOutgoingEdges().isEmpty():
                                    nodes.remove(node)
                            else:
                                port = edge.getTargetPort() if sourceIsInMode else edge.getSourcePort()
                                isLocal = modeChildren.get(None).contains(node)
                                if isLocal:
                                    #  Add port to mode container
                                    if modeContainerPorts.containsKey(port):
                                        node = modeContainer
                                        port = modeContainerPorts.get(port)
                                    else:
                                        containerPort = self._kPortExtensions.createPort()
                                        modeContainerPorts.put(port, containerPort)
                                        modeContainer.getPorts().add(containerPort)

                                        self._kPortExtensions.setPortSize(containerPort, 8, 8)
                                        rect = self._kRenderingExtensions.addRectangle(containerPort)
                                        self._kRenderingExtensions.setPointPlacementData(rect,
                                                self._kRenderingExtensions.LEFT, 0, 0.5,
                                                self._kRenderingExtensions.BOTTOM, 0, 0.5,
                                                self._kRenderingExtensions.H_CENTRAL, self._kRenderingExtensions.V_CENTRAL,
                                                0, 0, 8, 4)
                                        self._kRenderingExtensions.setBackground(rect, Colors.BLACK)
                                        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(rect)

                                        DiagramSyntheses.setLayoutOption(containerPort, CoreOptions.PORT_BORDER_OFFSET, -4.0)
                                        DiagramSyntheses.setLayoutOption(containerPort, CoreOptions.PORT_SIDE, PortSide.EAST if sourceIsInMode else PortSide.WEST)

                                        source = self._utilityExtensions.sourceElement(node)
                                        label = ""
                                        if  isinstance(source, Action):
                                            label = source.getName()
                                        elif isinstance(source, Timer):
                                            label = source.getName()
                                        elif not port.getLabels().isEmpty():
                                            label = port.getLabels().get(0).getText()
                                            if isinstance(source, Reactor) and self.getBooleanValue(LinguaFrancaSynthesis.SHOW_INSTANCE_NAMES):
                                                linkedInstance = NamedInstanceUtil.getLinkedInstance(node)
                                                if isinstance(linkedInstance, ReactorInstance):
                                                    label = linkedInstance.getName() + "." + label
                                        portLabel = self._kLabelExtensions.createLabel(containerPort)
                                        portLabel.setText(label)
                                        portLabelKText = self._kRenderingFactory.createKText()
                                        self._kRenderingExtensions.setFontSize(portLabelKText, 8)
                                        portLabel.getData().add(portLabelKText)

                                        #  new connection
                                        copy = EcoreUtil.copy(edge)
                                        if sourceIsInMode:
                                            copy.setSource(modeContainer)
                                            copy.setSourcePort(containerPort)
                                            copy.setTarget(edge.getTarget())
                                        else:
                                            copy.setTarget(modeContainer)
                                            copy.setTargetPort(containerPort)
                                            copy.setSource(edge.getSource())
                                        node = modeContainer
                                        port = containerPort

                                #  Duplicate port
                                if not portCopies.containsKey(port):
                                    copy = EcoreUtil.copy(port)
                                    portCopies.put(port, copy)

                                    dummyNode = self._kNodeExtensions.createNode()
                                    newID = mode.uniqueID() + "_"
                                    if not port.getLabels().isEmpty():
                                        newID += port.getLabels().getText().head()
                                    self._utilityExtensions.setID(dummyNode, newID)
                                    self._kRenderingExtensions.addInvisibleContainerRendering(dummyNode)
                                    dummyNode.getPorts().add(copy)
                                    #  Assign layer
                                    DiagramSyntheses.setLayoutOption(dummyNode, LayeredOptions.LAYERING_LAYER_CONSTRAINT,
                                            port.getProperty(CoreOptions.PORT_SIDE) == LayerConstraint.FIRST 
                                            if PortSide.WEST else LayerConstraint.LAST)
                                    #  Configure port spacing
                                    DiagramSyntheses.setLayoutOption(dummyNode, CoreOptions.PORT_LABELS_PLACEMENT, 
                                         (PortLabelPlacement.ALWAYS_OTHER_SAME_SIDE, PortLabelPlacement.OUTSIDE))
                                    #  Place freely
                                    DiagramSyntheses.setLayoutOption(dummyNode, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, True)
                                    #  Switch port side
                                    DiagramSyntheses.setLayoutOption(copy, CoreOptions.PORT_SIDE,
                                            port.getProperty(CoreOptions.PORT_SIDE) == PortSide.EAST 
                                            if PortSide.WEST else PortSide.WEST)

                                    modeNode.getChildren().add(dummyNode)
                                newPort = portCopies.get(port)
                                if sourceIsInMode:
                                    edge.setTarget(newPort.getNode())
                                    edge.setTargetPort(newPort)
                                else:
                                    edge.setSource(newPort.getNode())
                                    edge.setSourcePort(newPort)

            #  If mode container is unused (no ports for local connections) -> hide it
            if modeContainer.getPorts().isEmpty():
                self._kRenderingExtensions.setInvisible(modeContainerFigure, True)
                DiagramSyntheses.setLayoutOption(modeContainer, CoreOptions.PADDING, ElkPadding(2))
            elif bool(LinguaFrancaSynthesis.SHOW_INSTANCE_NAMES):
                #  Remove mode container port labels of ports representing internal connections
                #  because their association to reactor instances is unambiguous due to instance names
                for p in modeContainer.getPorts():
                    pass
                    #  p.getLabels().removeIf(l -> l.getText().contains("."))
            nodes.append(modeContainer)



