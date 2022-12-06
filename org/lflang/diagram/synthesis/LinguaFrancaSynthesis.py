#!/usr/bin/env python
""" generated source for module LinguaFrancaSynthesis """
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
# import java.util.ArrayList
# import java.util.Collection
# import java.util.EnumSet
# import java.util.HashMap
# import java.util.HashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Map
# import java.util.Set
# import java.util.stream.Collectors
# import java.util.stream.Stream
# import org.eclipse.elk.alg.layered.options.EdgeStraighteningStrategy
# import org.eclipse.elk.alg.layered.options.FixedAlignment
# import org.eclipse.elk.alg.layered.options.GreedySwitchType
# import org.eclipse.elk.alg.layered.options.LayerConstraint
# import org.eclipse.elk.alg.layered.options.LayeredOptions
# import org.eclipse.elk.alg.layered.options.NodePlacementStrategy
# import org.eclipse.elk.core.math.ElkMargin
# import org.eclipse.elk.core.math.ElkPadding
# import org.eclipse.elk.core.math.KVector
# import org.eclipse.elk.core.options.BoxLayouterOptions
# import org.eclipse.elk.core.options.ContentAlignment
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.elk.core.options.Direction
# import org.eclipse.elk.core.options.PortConstraints
# import org.eclipse.elk.core.options.PortLabelPlacement
# import org.eclipse.elk.core.options.PortSide
# import org.eclipse.elk.core.options.SizeConstraint
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.util.EcoreUtil
# import org.eclipse.xtext.xbase.lib.Conversions
# import org.eclipse.xtext.xbase.lib.Exceptions
# import org.eclipse.xtext.xbase.lib.Extension
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.ListExtensions
# import org.eclipse.xtext.xbase.lib.Pair
# import org.eclipse.xtext.xbase.lib.StringExtensions
# import com.google.common.collect.HashBasedTable
# import com.google.common.collect.HashMultimap
# import com.google.common.collect.Iterables
# import com.google.common.collect.Multimap
# import com.google.common.collect.Table
# import de.cau.cs.kieler.klighd.DisplayedActionData
# import de.cau.cs.kieler.klighd.SynthesisOption
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KLabel
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.Colors
# import de.cau.cs.kieler.klighd.krendering.HorizontalAlignment
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KPolyline
# import de.cau.cs.kieler.klighd.krendering.KRectangle
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import de.cau.cs.kieler.klighd.krendering.KRoundedRectangle
# import de.cau.cs.kieler.klighd.krendering.KStyle
# import de.cau.cs.kieler.klighd.krendering.KText
# import de.cau.cs.kieler.klighd.krendering.LineCap
# import de.cau.cs.kieler.klighd.krendering.LineStyle
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.krendering.extensions.KContainerRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KEdgeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KLabelExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KNodeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPolylineExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPortExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KRenderingExtensions
# import de.cau.cs.kieler.klighd.syntheses.AbstractDiagramSynthesis
# import de.cau.cs.kieler.klighd.util.KlighdProperties

# 
#  * Diagram synthesis for Lingua Franca programs.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#
import configparser

from include.KeilerClasses import KEdge, KPort
from include.MiscClasses import ElkPadding, HashSet
from include.overloading import overloaded
from lflang.ASTUtils import ASTUtils
from lflang.AttributeUtils import AttributeUtils
from lflang.InferredType import InferredType
from lflang.diagram.synthesis.ReactorParameterDisplayModes import ReactorParameterDisplayModes
from lflang.diagram.synthesis.action.CollapseAllReactorsAction import CollapseAllReactorsAction
from lflang.diagram.synthesis.action.ExpandAllReactorsAction import ExpandAllReactorsAction
from lflang.diagram.synthesis.action.FilterCycleAction import KNode
from lflang.diagram.synthesis.action.MemorizingExpandCollapseAction import MemorizingExpandCollapseAction
from lflang.diagram.synthesis.styles.LinguaFrancaShapeExtensions import Direction, NodePlacementStrategy, \
    PortConstraints, PortLabelPlacement, HorizontalAlignment
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import Colors
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import SynthesisOption, CoreOptions, LineStyle
from lflang.diagram.synthesis.util.LayoutPostProcessing import LayeredOptions, LayoutPostProcessing
from lflang.diagram.synthesis.util.ModeDiagrams import ModeDiagrams
from lflang.diagram.synthesis.util.SynthesisErrorReporter import SynthesisErrorReporter
from lflang.generator.ReactorInstance import ReactorInstance

config = configparser.RawConfigParser()


class DisplayedActionData:
    pass


class AbstractDiagramSynthesis:
    pass


class BoxLayouterOptions:
    pass


class Conversions:
    pass


class HashBasedTable:
    pass


class ContentAlignment:
    pass


class SizeConstraint:
    pass


class IterableExtensions:
    pass


class LineCap:
    pass


class LinguaFrancaSynthesis(AbstractDiagramSynthesis):
    """ generated source for class LinguaFrancaSynthesis """


    #  -------------------------------------------------------------------------
    ID = "org.lflang.diagram.synthesis.LinguaFrancaSynthesis"


    #  -- INTERNAL --
    REACTOR_RECURSIVE_INSTANTIATION = config.get("org.lflang.linguafranca.diagram.synthesis.reactor.recursive.instantiation", False)
    REACTOR_HAS_BANK_PORT_OFFSET = config.get("org.lflang.linguafranca.diagram.synthesis.reactor.bank.offset", False)
    REACTOR_INPUT = config.get("org.lflang.linguafranca.diagram.synthesis.reactor.input", False)
    REACTOR_OUTPUT = config.get("org.lflang.linguafranca.diagram.synthesis.reactor.output", False)
    REACTION_SPECIAL_TRIGGER = config.get("org.lflang.linguafranca.diagram.synthesis.reaction.special.trigger", False)

    #  -- STYLE --    
    ALTERNATIVE_DASH_PATTERN = list(3.0)

    #  -- TEXT --
    TEXT_ERROR_RECURSIVE = "Recursive reactor instantiation!"
    TEXT_ERROR_CONTAINS_RECURSION = "Reactor contains recursive instantiation!"
    TEXT_ERROR_CONTAINS_CYCLE = "Reactor contains cyclic dependencies!"
    TEXT_ERROR_CYCLE_DETECTION = "Dependency cycle detection failed.\nCould not detect dependency cycles due to unexpected graph structure."
    TEXT_ERROR_CYCLE_BTN_SHOW = "Show Cycle"
    TEXT_ERROR_CYCLE_BTN_FILTER = "Filter Cycle"
    TEXT_ERROR_CYCLE_BTN_UNFILTER = "Remove Cycle Filter"
    TEXT_NO_MAIN_REACTOR = "No Main Reactor"
    TEXT_REACTOR_NULL = "Reactor is null"
    TEXT_HIDE_ACTION = "[Hide]"
    TEXT_SHOW_ACTION = "[Details]"

    #  -------------------------------------------------------------------------
    #  Synthesis category 
    APPEARANCE = SynthesisOption.createCategory("Appearance", True)
    EXPERIMENTAL = SynthesisOption.createCategory("Experimental", True)

    LAYOUT = SynthesisOption.createCategory("Layout", False).setCategory(APPEARANCE)


    #  Synthesis options 
    SHOW_ALL_REACTORS = SynthesisOption.createCheckOption("All Reactors", False)
    CYCLE_DETECTION = SynthesisOption.createCheckOption("Dependency Cycle Detection", True)
    SHOW_USER_LABELS = SynthesisOption.createCheckOption("User Labels (@label in JavaDoc)", True).setCategory(APPEARANCE)
    SHOW_HYPERLINKS = SynthesisOption.createCheckOption("Expand/Collapse Hyperlinks", False).setCategory(APPEARANCE)
    REACTIONS_USE_HYPEREDGES = SynthesisOption.createCheckOption("Bundled Dependencies", False).setCategory(APPEARANCE)
    USE_ALTERNATIVE_DASH_PATTERN = SynthesisOption.createCheckOption("Alternative Dependency Line Style", False).setCategory(APPEARANCE)
    SHOW_PORT_NAMES = SynthesisOption.createCheckOption("Port names", True).setCategory(APPEARANCE)
    SHOW_MULTIPORT_WIDTH = SynthesisOption.createCheckOption("Multiport Widths", False).setCategory(APPEARANCE)
    SHOW_REACTION_CODE = SynthesisOption.createCheckOption("Reaction Code", False).setCategory(APPEARANCE)
    SHOW_REACTION_LEVEL = SynthesisOption.createCheckOption("Reaction Level", False).setCategory(APPEARANCE)
    SHOW_REACTION_ORDER_EDGES = SynthesisOption.createCheckOption("Reaction Order Edges", False).setCategory(APPEARANCE)
    SHOW_REACTOR_HOST = SynthesisOption.createCheckOption("Reactor Host Addresses", True).setCategory(APPEARANCE)
    SHOW_INSTANCE_NAMES = SynthesisOption.createCheckOption("Reactor Instance Names", False).setCategory(APPEARANCE)
    REACTOR_PARAMETER_MODE = SynthesisOption.createChoiceOption("Reactor Parameters", (Conversions.doWrapArray(ReactorParameterDisplayModes.values())), ReactorParameterDisplayModes.NONE).setCategory(APPEARANCE)
    SHOW_STATE_VARIABLES = SynthesisOption.createCheckOption("Reactor State Variables", False).setCategory(APPEARANCE)
    REACTOR_BODY_TABLE_COLS = SynthesisOption.createRangeOption("Reactor Parameter/Variable Columns", 1, 10, 1).setCategory(APPEARANCE)
    SPACING = SynthesisOption.createRangeOption("Spacing (%)", 0, 150, 5, 75).setCategory(LAYOUT)

    #  Synthesis actions 
    COLLAPSE_ALL = DisplayedActionData.create(CollapseAllReactorsAction.ID, "Hide all Details")
    EXPAND_ALL = DisplayedActionData.create(ExpandAllReactorsAction.ID, "Show all Details")


    def __init__(self):
        self._kNodeExtensions = None
        self._kEdgeExtensions = None
        self._kPortExtensions = None
        self._kLabelExtensions = None
        self._kRenderingExtensions = None
        self._kContainerRenderingExtensions = None
        self._kPolylineExtensions = None
        self._linguaFrancaStyleExtensions = None
        self._linguaFrancaShapeExtensions = None
        self._utilityExtensions = None
        self._cycleVisualization = None
        self._interfaceDependenciesVisualization = None
        self._filterCycleAction = None
        self._reactorIcons = None
        self._modeDiagrams = None
        self._layoutPostProcessing = None

    def getDisplayedSynthesisOptions(self):
        """ generated source for method getDisplayedSynthesisOptions """
        return [LinguaFrancaSynthesis.SHOW_ALL_REACTORS,
                    MemorizingExpandCollapseAction.MEMORIZE_EXPANSION_STATES,
                    LinguaFrancaSynthesis.CYCLE_DETECTION,
                    LinguaFrancaSynthesis.APPEARANCE,
                    ModeDiagrams.MODES_CATEGORY,
                    ModeDiagrams.SHOW_TRANSITION_LABELS,
                    ModeDiagrams.INITIALLY_COLLAPSE_MODES,
                    LinguaFrancaSynthesis.SHOW_USER_LABELS,
                    LinguaFrancaSynthesis.SHOW_HYPERLINKS,
                    LinguaFrancaSynthesis.REACTIONS_USE_HYPEREDGES,
                    LinguaFrancaSynthesis.USE_ALTERNATIVE_DASH_PATTERN,
                    LinguaFrancaSynthesis.SHOW_PORT_NAMES,
                    LinguaFrancaSynthesis.SHOW_MULTIPORT_WIDTH,
                    LinguaFrancaSynthesis.SHOW_REACTION_CODE,
                    LinguaFrancaSynthesis.SHOW_REACTION_LEVEL,
                    LinguaFrancaSynthesis.SHOW_REACTION_ORDER_EDGES,
                    LinguaFrancaSynthesis.SHOW_REACTOR_HOST,
                    LinguaFrancaSynthesis.SHOW_INSTANCE_NAMES,
                    LinguaFrancaSynthesis.REACTOR_PARAMETER_MODE,
                    LinguaFrancaSynthesis.SHOW_STATE_VARIABLES,
                    LinguaFrancaSynthesis.REACTOR_BODY_TABLE_COLS,
                    LinguaFrancaSynthesis.LAYOUT,
                    LayoutPostProcessing.MODEL_ORDER,
                    LinguaFrancaSynthesis.SPACING]

    def getDisplayedActions(self):
        """ generated source for method getDisplayedActions """
        return [LinguaFrancaSynthesis.COLLAPSE_ALL, LinguaFrancaSynthesis.EXPAND_ALL]

    #  -------------------------------------------------------------------------
    def transform(self, model):
        """ generated source for method transform """
        rootNode = self._kNodeExtensions.createNode()
        self.setLayoutOption(rootNode, CoreOptions.ALGORITHM, LayeredOptions.ALGORITHM_ID)
        self.setLayoutOption(rootNode, CoreOptions.DIRECTION, Direction.RIGHT)
        self.setLayoutOption(rootNode, CoreOptions.PADDING, ElkPadding(0))
        try:
            #  Find main
            main = None
            for m in model.getReactors():
                if isinstance(m, self._utilityExtensions.isMainOrFederated):
                    main = m
            if main is not None:
                reactorInstance = ReactorInstance(main, SynthesisErrorReporter())
                rootNode.getChildren().addAll(self.createReactorNode(reactorInstance, True, None, None, dict()))
            elif not self.getBooleanValue(LinguaFrancaSynthesis.SHOW_ALL_REACTORS):
                messageNode = self._kNodeExtensions.createNode()
                self._linguaFrancaShapeExtensions.addErrorMessage(messageNode, LinguaFrancaSynthesis.TEXT_NO_MAIN_REACTOR, None)
                rootNode.getChildren().append(messageNode)
            #  Show all reactors
            if main is None or self.getBooleanValue(LinguaFrancaSynthesis.SHOW_ALL_REACTORS):
                reactorNodes = []
                for reactor in model.getReactors():
                    if reactor == main:
                        continue 
                    reactorInstance = ReactorInstance(reactor, SynthesisErrorReporter(), HashSet())
                    reactorNodes.addAll(self.createReactorNode(reactorInstance, main == None, HashBasedTable.create(), HashBasedTable.create(), dict()))
                if not reactorNodes.isEmpty():
                    #  To allow ordering, we need box layout but we also need layered layout for ports thus wrap all node
                    reactorNodes.extend(rootNode.getChildren())
                    index = 0
                    for node in reactorNodes:
                        #  Element could be null if there is no main reactor and Show All Reactors is checked.
                        if node == None:
                            continue 
                        if node.getProperty(CoreOptions.COMMENT_BOX):
                            continue 
                        child = self._kNodeExtensions.createNode()
                        child.getChildren().append(node)
                        #  Add comment nodes
                        for edge in node.getIncomingEdges():
                            if not edge.getSource().getProperty(CoreOptions.COMMENT_BOX):
                                continue 
                            child.getChildren().append(edge.getSource())
                        self._kRenderingExtensions.addInvisibleContainerRendering(child)
                        self.setLayoutOption(child, CoreOptions.ALGORITHM, LayeredOptions.ALGORITHM_ID)
                        self.setLayoutOption(child, CoreOptions.DIRECTION, Direction.RIGHT)
                        self.setLayoutOption(child, CoreOptions.PADDING, ElkPadding(0))
                        #  Legacy ordering option.
                        self.setLayoutOption(child, CoreOptions.PRIORITY, len(reactorNodes) - index)
                        #  Order!
                        rootNode.getChildren().append(child)
                        index += 1
                    self.setLayoutOption(rootNode, CoreOptions.ALGORITHM, BoxLayouterOptions.ALGORITHM_ID)
                    self.setLayoutOption(rootNode, CoreOptions.SPACING_NODE_NODE, 25.0)
        except Exception as e:
            e.printStackTrace()
            messageNode = self._kNodeExtensions.createNode()
            self._linguaFrancaShapeExtensions.addErrorMessage(messageNode, "Error in Diagram Synthesis", e.__class__.getSimpleName() + " occurred. Could not create diagram.")
            rootNode.getChildren().append(messageNode)
        return rootNode

    def createReactorNode(self, reactorInstance, expandDefault, inputPortsReg, outputPortsReg, allReactorNodes):
        """ generated source for method createReactorNode """
        #          Reactor reactor = reactorInstance.reactorDefinition;
        #          KNode node = _kNodeExtensions.createNode();
        #          allReactorNodes.put(reactorInstance, node);
        #          associateWith(node, reactor);
        #          _utilityExtensions.setID(node, reactorInstance.uniqueID());
        #          // save to distinguish nodes associated with the same reactor
        #          NamedInstanceUtil.linkInstance(node, reactorInstance);
            #          List nodes = new [];
        #          nodes.append(node);
        #          String label = createReactorLabel(reactorInstance);
            #          if (reactorInstance.recursive) {
        #              // Mark this node
        #              node.setProperty(REACTOR_RECURSIVE_INSTANTIATION, true);
        #              // Mark root
        #              allReactorNodes.get(reactorInstance.root()).setProperty(REACTOR_RECURSIVE_INSTANTIATION, true);
        #          }
            #          if (reactor == null) {
        #              _linguaFrancaShapeExtensions.addErrorMessage(node, TEXT_REACTOR_NULL, null);
        #          } else if (reactorInstance.isMainOrFederated()) {
        #              KRoundedRectangle figure = _linguaFrancaShapeExtensions.addMainReactorFigure(node, reactorInstance, label);
            #              if (getObjectValue(REACTOR_PARAMETER_MODE) == ReactorParameterDisplayModes.TABLE
        #                  && !reactorInstance.parameters.isEmpty()
        #              ) {
        #                  KRectangle rectangle = _kContainerRenderingExtensions.addRectangle(figure);
        #                  _kRenderingExtensions.setInvisible(rectangle, true);
        #                  _kRenderingExtensions.to(
        #                          _kRenderingExtensions.from(
        #                                  _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                  _kRenderingExtensions.LEFT, 6, 0,
        #                                  _kRenderingExtensions.TOP, 0, 0),
        #                          _kRenderingExtensions.RIGHT, 6, 0,
        #                          _kRenderingExtensions.BOTTOM, 4, 0);
        #                  _kRenderingExtensions.setHorizontalAlignment(rectangle, HorizontalAlignment.LEFT);
        #                  addParameterList(rectangle, reactorInstance.parameters);
        #              }
            #              if (self.getBooleanValue(SHOW_STATE_VARIABLES)) {
        #                  var variables = ASTUtils.collectElements(reactor, LfPackage.eINSTANCE.getReactor_StateVars(), true, false);
        #                  if (!variables.isEmpty()) {
        #                      KRectangle rectangle = _kContainerRenderingExtensions.addRectangle(figure);
        #                      _kRenderingExtensions.setInvisible(rectangle, true);
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                      _kRenderingExtensions.LEFT, 6, 0,
        #                                      _kRenderingExtensions.TOP, 0, 0),
        #                              _kRenderingExtensions.RIGHT, 6, 0,
        #                              _kRenderingExtensions.BOTTOM, 4, 0);
        #                      _kRenderingExtensions.setHorizontalAlignment(rectangle, HorizontalAlignment.LEFT);
        #                      addStateVariableList(rectangle, variables);
        #                  }
        #              }
            #              if (reactorInstance.recursive) {
        #                  nodes.append(addErrorComment(node, TEXT_ERROR_RECURSIVE));
        #                  _linguaFrancaStyleExtensions.errorStyle(figure);
        #              } else {
        #                  _kContainerRenderingExtensions.addChildArea(figure);
        #                  node.getChildren().addAll(transformReactorNetwork(reactorInstance,
        #                          new dict(),
        #                          new dict(),
        #                          allReactorNodes));
        #              }
        #              Iterables.addAll(nodes, createUserComments(reactor, node));
        #              configureReactorNodeLayout(node, true);
        #              _layoutPostProcessing.configureMainReactor(node);
        #          } else {
        #              ReactorInstance instance = reactorInstance;
            #              // Expanded Rectangle
        #              ReactorFigureComponents comps = _linguaFrancaShapeExtensions.addReactorFigure(node, reactorInstance, label);
        #              comps.getOuter().setProperty(KlighdProperties.EXPANDED_RENDERING, true);
        #              for (KRendering figure : comps.getFigures()) {
        #                  associateWith(figure, reactor);
        #                  _kRenderingExtensions.addDoubleClickAction(figure, MemorizingExpandCollapseAction.ID);
        #              }
        #              _reactorIcons.handleIcon(comps.getReactor(), reactor, false);
            #              if (self.getBooleanValue(SHOW_HYPERLINKS)) {
        #                  // Collapse button
        #                  KText button = _linguaFrancaShapeExtensions.addTextButton(comps.getReactor(), TEXT_HIDE_ACTION);
        #                  _kRenderingExtensions.to(
        #                          _kRenderingExtensions.from(
        #                                  _kRenderingExtensions.setGridPlacementData(button),
        #                                  _kRenderingExtensions.LEFT, 8, 0,
        #                                  _kRenderingExtensions.TOP, 0, 0),
        #                          _kRenderingExtensions.RIGHT, 8, 0,
        #                          _kRenderingExtensions.BOTTOM, 0, 0);
        #                  _kRenderingExtensions.addSingleClickAction(button, MemorizingExpandCollapseAction.ID);
        #                  _kRenderingExtensions.addDoubleClickAction(button, MemorizingExpandCollapseAction.ID);
        #              }
            #              if (getObjectValue(REACTOR_PARAMETER_MODE) == ReactorParameterDisplayModes.TABLE
        #                      && !instance.parameters.isEmpty()) {
        #                  KRectangle rectangle = _kContainerRenderingExtensions.addRectangle(comps.getReactor());
        #                  _kRenderingExtensions.setInvisible(rectangle, true);
        #                  if (!self.getBooleanValue(SHOW_HYPERLINKS)) {
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                      _kRenderingExtensions.LEFT, 6, 0,
        #                                      _kRenderingExtensions.TOP, 0, 0),
        #                              _kRenderingExtensions.RIGHT, 6, 0,
        #                              _kRenderingExtensions.BOTTOM, 4, 0);
        #                  } else {
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                      _kRenderingExtensions.LEFT, 6, 0,
        #                                      _kRenderingExtensions.TOP, 4, 0),
        #                              _kRenderingExtensions.RIGHT, 6, 0,
        #                              _kRenderingExtensions.BOTTOM, 0, 0);
        #                  }
        #                  _kRenderingExtensions.setHorizontalAlignment(rectangle, HorizontalAlignment.LEFT);
        #                  addParameterList(rectangle, instance.parameters);
        #              }
            #              if (self.getBooleanValue(SHOW_STATE_VARIABLES)) {
        #                  var variables = ASTUtils.collectElements(reactor, LfPackage.eINSTANCE.getReactor_StateVars(), true, false);
        #                  if (!variables.isEmpty()) {
        #                      KRectangle rectangle = _kContainerRenderingExtensions.addRectangle(comps.getReactor());
        #                      _kRenderingExtensions.setInvisible(rectangle, true);
        #                      if (!self.getBooleanValue(SHOW_HYPERLINKS)) {
        #                          _kRenderingExtensions.to(
        #                                  _kRenderingExtensions.from(
        #                                          _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                          _kRenderingExtensions.LEFT, 6, 0,
        #                                          _kRenderingExtensions.TOP, 0, 0),
        #                                  _kRenderingExtensions.RIGHT, 6, 0,
        #                                  _kRenderingExtensions.BOTTOM, 4, 0);
        #                      } else {
        #                          _kRenderingExtensions.to(
        #                                  _kRenderingExtensions.from(
        #                                          _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                          _kRenderingExtensions.LEFT, 6, 0,
        #                                          _kRenderingExtensions.TOP, 4, 0),
        #                                  _kRenderingExtensions.RIGHT, 6, 0,
        #                                  _kRenderingExtensions.BOTTOM, 0, 0);
        #                      }
        #                      _kRenderingExtensions.setHorizontalAlignment(rectangle, HorizontalAlignment.LEFT);
        #                      addStateVariableList(rectangle, variables);
        #                  }
        #              }
            #              if (instance.recursive) {
        #                  comps.getFigures().forEach(_linguaFrancaStyleExtensions.errorStyle);
        #              } else {
        #                  _kContainerRenderingExtensions.addChildArea(comps.getReactor());
        #              }
            #              // Collapse Rectangle
        #              comps = _linguaFrancaShapeExtensions.addReactorFigure(node, reactorInstance, label);
        #              comps.getOuter().setProperty(KlighdProperties.COLLAPSED_RENDERING, true);
        #              for (KRendering figure : comps.getFigures()) {
        #                  associateWith(figure, reactor);
        #                  if (_utilityExtensions.hasContent(instance) && !instance.recursive) {
        #                      _kRenderingExtensions.addDoubleClickAction(figure, MemorizingExpandCollapseAction.ID);
        #                  }
        #              }
        #              _reactorIcons.handleIcon(comps.getReactor(), reactor, true);
            #              if (self.getBooleanValue(SHOW_HYPERLINKS)) {
        #                  // Expand button
        #                  if (_utilityExtensions.hasContent(instance) && !instance.recursive) {
        #                      KText button = _linguaFrancaShapeExtensions.addTextButton(comps.getReactor(), TEXT_SHOW_ACTION);
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(button),
        #                                      _kRenderingExtensions.LEFT, 8, 0,
        #                                      _kRenderingExtensions.TOP, 0, 0),
        #                              _kRenderingExtensions.RIGHT, 8, 0,
        #                              _kRenderingExtensions.BOTTOM, 8, 0);
        #                      _kRenderingExtensions.addSingleClickAction(button, MemorizingExpandCollapseAction.ID);
        #                      _kRenderingExtensions.addDoubleClickAction(button, MemorizingExpandCollapseAction.ID);
        #                  }
        #              }
            #              if (instance.recursive) {
        #                  comps.getFigures().forEach(_linguaFrancaStyleExtensions.errorStyle);
        #              }
                #              // Create ports
        #              Map inputPorts = new dict();
        #              Map outputPorts = new dict();
        #              List inputs = instance.inputs;
        #              if (LayoutPostProcessing.LEGACY == (String getObjectValue(LayoutPostProcessing.MODEL_ORDER))) {
        #                  inputs = ListExtensions.reverseView(instance.inputs);
        #              }
        #              for (PortInstance input : inputs) {
        #                  inputPorts.put(input, addIOPort(node, input, true, input.isMultiport(), reactorInstance.isBank()));
        #              }
        #              for (PortInstance output : instance.outputs) {
        #                  outputPorts.put(output, addIOPort(node, output, false, output.isMultiport(), reactorInstance.isBank()));
        #              }
        #              // Mark ports
        #              for (it: inputPorts.values() ){
        #                  it.setProperty(REACTOR_INPUT, true)};
        #              for (it: outputPorts.values()) {
        #                  it.setProperty(REACTOR_OUTPUT, true)};
            #              // Add content
        #              if (_utilityExtensions.hasContent(instance) && !instance.recursive) {
        #                  node.getChildren().addAll(transformReactorNetwork(instance, inputPorts, outputPorts, allReactorNodes));
        #              }
            #              // Pass port to given tables
        #              if (!_utilityExtensions.isRoot(instance)) {
        #                  if (inputPortsReg != null) {
        #                      for (Map.Entry entry : inputPorts.entrySet()) {
        #                          inputPortsReg.put(instance, entry.getKey(), entry.getValue());
        #                      }
        #                  }
        #                  if (outputPortsReg != null) {
        #                      for (Map.Entry entry : outputPorts.entrySet()) {
        #                          outputPortsReg.put(instance, entry.getKey(), entry.getValue());
        #                      }
        #                  }
        #              }
            #              if (instance.recursive) {
        #                  self.setLayoutOption(node, KlighdProperties.EXPAND, false);
        #                  nodes.append(addErrorComment(node, TEXT_ERROR_RECURSIVE));
        #              } else {
        #                  self.setLayoutOption(node, KlighdProperties.EXPAND, expandDefault);
            #                  // Interface Dependencies
        #                  _interfaceDependenciesVisualization.addInterfaceDependencies(node, expandDefault);
        #              }
            #              if (!_utilityExtensions.isRoot(instance)) {
        #                  // If all reactors are being shown, then only put the label on
        #                  // the reactor definition, not on its instances. Otherwise,
        #                  // add the annotation now.
        #                  if (!self.getBooleanValue(SHOW_ALL_REACTORS)) {
        #                      Iterables.addAll(nodes, createUserComments(reactor, node));
        #                  }
        #              } else {
        #                  Iterables.addAll(nodes, createUserComments(reactor, node));
        #              }
        #              configureReactorNodeLayout(node, false);
        #              _layoutPostProcessing.configureReactor(node);
        #          }
            #          // Find and annotate cycles
        #          if (self.getBooleanValue(CYCLE_DETECTION) &&
        #                  _utilityExtensions.isRoot(reactorInstance)) {
        #              KNode errNode = detectAndAnnotateCycles(node, reactorInstance, allReactorNodes);
        #              if (errNode != null) {
        #                  nodes.append(errNode);
        #              }
        #          }
            #          return nodes;

    def configureReactorNodeLayout(self, node, main):
        """ generated source for method configureReactorNodeLayout """
        #  Set layered algorithm
        self.setLayoutOption(node, CoreOptions.ALGORITHM, LayeredOptions.ALGORITHM_ID)
        #  Left to right layout
        self.setLayoutOption(node, CoreOptions.DIRECTION, Direction.RIGHT)
        #  Center free floating children
        self.setLayoutOption(node, CoreOptions.CONTENT_ALIGNMENT, ContentAlignment.centerCenter())
        #  Balanced placement with straight long edges.
        self.setLayoutOption(node, LayeredOptions.NODE_PLACEMENT_STRATEGY, NodePlacementStrategy.NETWORK_SIMPLEX)
        #  Do not shrink nodes below content
        self.setLayoutOption(node, CoreOptions.NODE_SIZE_CONSTRAINTS, (SizeConstraint.MINIMUM_SIZE, SizeConstraint.PORTS))
        #  Allows to freely shuffle ports on each side
        self.setLayoutOption(node, CoreOptions.PORT_CONSTRAINTS, PortConstraints.FIXED_SIDE)
        #  Adjust port label spacing to be closer to edge but not overlap with port figure
        #  TODO: Add PortLabelPlacement.NEXT_TO_PORT_IF_POSSIBLE back into the configuration, as soon as ELK provides a fix for LF issue #1273
        self.setLayoutOption(node, CoreOptions.PORT_LABELS_PLACEMENT, (PortLabelPlacement.ALWAYS_OTHER_SAME_SIDE, PortLabelPlacement.OUTSIDE))
        self.setLayoutOption(node, CoreOptions.SPACING_LABEL_PORT_HORIZONTAL, 2.0)
        self.setLayoutOption(node, CoreOptions.SPACING_LABEL_PORT_VERTICAL, -3.0)
        #  Configure spacing
        if not self.getBooleanValue(self.SHOW_HYPERLINKS):
            #  Hyperlink version is more relaxed in terms of space
            factor = float(int(self.SPACING)) / 100
            self.setLayoutOption(node, LayeredOptions.SPACING_COMPONENT_COMPONENT, LayeredOptions.SPACING_COMPONENT_COMPONENT.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_NODE_NODE, LayeredOptions.SPACING_NODE_NODE.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_NODE_NODE_BETWEEN_LAYERS, LayeredOptions.SPACING_NODE_NODE_BETWEEN_LAYERS.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_PORT_PORT, LayeredOptions.SPACING_PORT_PORT.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_NODE, LayeredOptions.SPACING_EDGE_NODE.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_NODE_BETWEEN_LAYERS, LayeredOptions.SPACING_EDGE_NODE_BETWEEN_LAYERS.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_EDGE, LayeredOptions.SPACING_EDGE_EDGE.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_EDGE_BETWEEN_LAYERS, LayeredOptions.SPACING_EDGE_EDGE_BETWEEN_LAYERS.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_EDGE, LayeredOptions.SPACING_EDGE_EDGE.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_EDGE_BETWEEN_LAYERS, LayeredOptions.SPACING_EDGE_EDGE_BETWEEN_LAYERS.getDefault() * factor)
            self.setLayoutOption(node, LayeredOptions.SPACING_EDGE_LABEL, LayeredOptions.SPACING_EDGE_LABEL.getDefault() * factor)
            #  Padding for sub graph
            if main:
                #  Special handing for main reactors
                self.setLayoutOption(node, CoreOptions.PADDING, ElkPadding(-1, 6, 6, 6))
            else:
                self.setLayoutOption(node, CoreOptions.PADDING, ElkPadding(2, 6, 6, 6))
        return node

    def detectAndAnnotateCycles(self, node, reactorInstance, allReactorNodes):
        """ generated source for method detectAndAnnotateCycles """
        #          if (node.getProperty(REACTOR_RECURSIVE_INSTANTIATION)) {
        #              _filterCycleAction.resetCycleFiltering(node);
        #              return addErrorComment(node, TEXT_ERROR_CONTAINS_RECURSION);
        #          } else { // only detect dependency cycles if not recursive
        #              try {
        #                  boolean hasCycle = _cycleVisualization.detectAndHighlightCycles(reactorInstance,
        #                          allReactorNodes,
        #                          /* it -> {
        #                              if (it instanceof KNode) {
        #                                  List renderings = IterableExtensions.toList(
        #                                          Iterables.filter(((KNode) it).getData(), KRendering.class));
        #                                  if (len(renderings) == 1) {
        #                                       _linguaFrancaStyleExtensions.errorStyle(IterableExtensions.head(renderings));
        #                                  } else {
        #                                      IterableExtensions.filter(renderings, rendering -> {
        #                                          return rendering.getProperty(KlighdProperties.COLLAPSED_RENDERING);
        #                                      }).forEach(_linguaFrancaStyleExtensions.errorStyle);
        #                                  }
        #                              } else if (it instanceof KEdge) {
        #                                  Iterables.filter(((KEdge) it).getData(),
        #                                          KRendering.class).forEach(_linguaFrancaStyleExtensions.errorStyle);
        #                                  // TODO initiallyHide does not work with incremental (https://github.com/kieler/KLighD/issues/37)
        #                                  // cycleEgde.initiallyShow() // Show hidden order dependencies
        #                                  _kRenderingExtensions.setInvisible(_kRenderingExtensions.getKRendering(it), false);
        #                              } else if (it instanceof KPort) {
        #                                  Iterables.filter(((KPort) it).getData(),
        #                                          KRendering.class).forEach(_linguaFrancaStyleExtensions.errorStyle);
        #                                  //it.reverseTrianglePort()
        #                              }
        #                          }
        #                           
        #                           );
            #                  if (hasCycle) {
        #                      KNode err = addErrorComment(node, TEXT_ERROR_CONTAINS_CYCLE);
            #                      // Add to existing figure
        #                      KRectangle rectangle = _kContainerRenderingExtensions.addRectangle(_kRenderingExtensions.getKContainerRendering(err));
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(rectangle),
        #                                      _kRenderingExtensions.LEFT, 3, 0,
        #                                      _kRenderingExtensions.TOP, (-1), 0),
        #                              _kRenderingExtensions.RIGHT, 3, 0,
        #                              _kRenderingExtensions.BOTTOM, 3, 0);
        #                      _linguaFrancaStyleExtensions.noSelectionStyle(rectangle);
        #                      _kRenderingExtensions.setInvisible(rectangle, true);
        #                      _kContainerRenderingExtensions.setGridPlacement(rectangle, 2);
            #                      KRectangle subrectangle = _kContainerRenderingExtensions.addRectangle(rectangle);
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(subrectangle),
        #                                      _kRenderingExtensions.LEFT, 0, 0,
        #                                      _kRenderingExtensions.TOP, 0, 0),
        #                              _kRenderingExtensions.RIGHT, 2, 0,
        #                              _kRenderingExtensions.BOTTOM, 0, 0);
        #                      _linguaFrancaStyleExtensions.noSelectionStyle(subrectangle);
        #                      _kRenderingExtensions.addSingleClickAction(subrectangle, ShowCycleAction.ID);
            #                      KText subrectangleText = _kContainerRenderingExtensions.addText(subrectangle, TEXT_ERROR_CYCLE_BTN_SHOW);
        #                      // Copy text style
        #                      List styles = ListExtensions.map(
        #                              IterableExtensions.head(
        #                                      _kRenderingExtensions.getKContainerRendering(err).getChildren()).getStyles(),
        #                              EcoreUtil.copy);
        #                      subrectangleText.getStyles().addAll(styles);
        #                      _kRenderingExtensions.setFontSize(subrectangleText, 5);
        #                      _kRenderingExtensions.setSurroundingSpace(subrectangleText, 1, 0);
        #                      _linguaFrancaStyleExtensions.noSelectionStyle(subrectangleText);
        #                      _kRenderingExtensions.addSingleClickAction(subrectangleText, ShowCycleAction.ID);
            #                      subrectangle = _kContainerRenderingExtensions.addRectangle(rectangle);
        #                      _kRenderingExtensions.to(
        #                              _kRenderingExtensions.from(
        #                                      _kRenderingExtensions.setGridPlacementData(subrectangle),
        #                                      _kRenderingExtensions.LEFT, 0, 0,
        #                                      _kRenderingExtensions.TOP, 0, 0),
        #                              _kRenderingExtensions.RIGHT, 0, 0,
        #                              _kRenderingExtensions.BOTTOM, 0, 0);
        #                      _linguaFrancaStyleExtensions.noSelectionStyle(subrectangle);
        #                      _kRenderingExtensions.addSingleClickAction(subrectangle, FilterCycleAction.ID);
            #                      subrectangleText = _kContainerRenderingExtensions.addText(subrectangle,
        #                              _filterCycleAction.isCycleFiltered(node) ?
        #                                      TEXT_ERROR_CYCLE_BTN_UNFILTER : TEXT_ERROR_CYCLE_BTN_FILTER);
        #                      // Copy text style
        #                      styles = ListExtensions.map(
        #                              IterableExtensions.head(
        #                                      _kRenderingExtensions.getKContainerRendering(err).getChildren()).getStyles(),
        #                              EcoreUtil.copy);
        #                      subrectangleText.getStyles().addAll(styles);
        #                      _kRenderingExtensions.setFontSize(subrectangleText, 5);
        #                      _kRenderingExtensions.setSurroundingSpace(subrectangleText, 1, 0);
        #                      _linguaFrancaStyleExtensions.noSelectionStyle(subrectangleText);
        #                      _kRenderingExtensions.addSingleClickAction(subrectangleText, FilterCycleAction.ID);
        #                      _filterCycleAction.markCycleFilterText(subrectangleText, err);
            #                      // if user interactively requested a filtered diagram keep it filtered during updates
        #                      if (_filterCycleAction.isCycleFiltered(node)) {
        #                          _filterCycleAction.filterCycle(node);
        #                      }
        #                      return err;
        #                  }
        #              } catch(Exception e) {
        #                  _filterCycleAction.resetCycleFiltering(node);
        #                  e.printStackTrace();
        #                  return addErrorComment(node, TEXT_ERROR_CYCLE_DETECTION);
        #              }
        #          }
        #          return null;

    def transformReactorNetwork(self, reactorInstance, parentInputPorts, parentOutputPorts, allReactorNodes):
        """ generated source for method transformReactorNetwork """
        #          List nodes = new [];
        #          Table inputPorts = HashBasedTable.create();
        #          Table outputPorts = HashBasedTable.create();
        #          Map reactionNodes = new dict();
        #          Map directConnectionDummyNodes = new dict();
        #          Multimap actionDestinations = HashMultimap();
        #          Multimap actionSources = HashMultimap();
        #          Map timerNodes = new dict();
        #          KNode startupNode = _kNodeExtensions.createNode();
        #          TriggerInstance startup = null;
        #          KNode shutdownNode = _kNodeExtensions.createNode();
        #          TriggerInstance shutdown = null;
        #          KNode resetNode = _kNodeExtensions.createNode();
        #          TriggerInstance reset = null;
            #          // Transform instances
        #          int index = 0;
        #          for (ReactorInstance child : reactorInstance.children) {
        #              Boolean expansionState = MemorizingExpandCollapseAction.getExpansionState(child);
        #              Collection rNodes = self.createReactorNode(
        #                      child,
        #                      expansionState != null ? expansionState : false,
        #                      inputPorts,
        #                      outputPorts,
        #                      allReactorNodes);
        #              nodes.addAll(rNodes);
        #              index++;
        #          }
            #          // Create timers
        #          for (TimerInstance timer : reactorInstance.timers) {
        #              KNode node = associateWith(_kNodeExtensions.createNode(), timer.getDefinition());
        #              NamedInstanceUtil.linkInstance(node, timer);
        #              _utilityExtensions.setID(node, timer.uniqueID());
        #              nodes.append(node);
        #              Iterables.addAll(nodes, createUserComments(timer.getDefinition(), node));
        #              timerNodes.put(timer, node);
        #              _linguaFrancaShapeExtensions.addTimerFigure(node, timer);
        #              _layoutPostProcessing.configureTimer(node);
        #          }
            #          // Create reactions
        #          for (ReactionInstance reaction : reactorInstance.reactions) {
        #              int idx = reactorInstance.reactions.indexOf(reaction);
        #              KNode node = associateWith(_kNodeExtensions.createNode(), reaction.getDefinition());
        #              NamedInstanceUtil.linkInstance(node, reaction);
        #              _utilityExtensions.setID(node, reaction.uniqueID());
        #              nodes.append(node);
        #              Iterables.addAll(nodes, createUserComments(reaction.getDefinition(), node));
        #              reactionNodes.put(reaction, node);
            #              self.setLayoutOption(node, CoreOptions.PORT_CONSTRAINTS, PortConstraints.FIXED_SIDE);
        #              _layoutPostProcessing.configureReaction(node);
        #              self.setLayoutOption(node, LayeredOptions.POSITION, new KVector(0, idx + 1)); // try order reactions vertically if in one layer (+1 to account for startup)
            #              var figure = _linguaFrancaShapeExtensions.addReactionFigure(node, reaction);
            #              int inputSize = Stream.concat(reaction.triggers.stream(), reaction.sources.stream()).collect(Collectors.toSet()).size();
        #              int outputSize = len(reaction.effects);
        #              if (!self.getBooleanValue(REACTIONS_USE_HYPEREDGES) && (inputSize > 1 || outputSize > 1)) {
        #                  // If this node will have more than one input/output port, the port positions must be adjusted to the
        #                  // pointy shape. However, this is only possible after the layout.
        #                  ReactionPortAdjustment.apply(node, figure);
        #              }
            #              // connect input
        #              KPort port = null;
        #              for (TriggerInstance trigger : reaction.triggers) {
        #                  // Create new port if there is no previous one or each dependency should have its own one
        #                  if (port == null || !self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) {
        #                      port = addInvisiblePort(node);
        #                      self.setLayoutOption(port, CoreOptions.PORT_SIDE, PortSide.WEST);
            #                      if (self.getBooleanValue(REACTIONS_USE_HYPEREDGES) || inputSize == 1) {
        #                          // manual adjustment disabling automatic one
        #                          self.setLayoutOption(port, CoreOptions.PORT_BORDER_OFFSET,
        #                                  (double) -LinguaFrancaShapeExtensions.REACTION_POINTINESS);
        #                      }
        #                  }
            #                  if (trigger.isStartup()) {
        #                      connect(createDependencyEdge(((TriggerInstance.BuiltinTriggerVariable) trigger.getDefinition()).definition),
        #                              startupNode,
        #                              port);
        #                      startup = trigger;
        #                  } else if (trigger.isShutdown()) {
        #                      connect(createDelayEdge(((TriggerInstance.BuiltinTriggerVariable) trigger.getDefinition()).definition),
        #                              shutdownNode,
        #                              port);
        #                      shutdown = trigger;
        #                  } else if (trigger.isReset()) {
        #                      connect(createDependencyEdge(((TriggerInstance.BuiltinTriggerVariable) trigger.getDefinition()).definition),
        #                              resetNode,
        #                              port);
        #                      reset = trigger;
        #                  } else if (trigger instanceof ActionInstance) {
        #                      actionDestinations.put(((ActionInstance) trigger), port);
        #                  } else if (trigger instanceof PortInstance) {
        #                      KPort src = null;
        #                      PortInstance triggerAsPort = (PortInstance) trigger;
        #                      if (triggerAsPort.getParent() == reactorInstance) {
        #                          src = parentInputPorts.get(trigger);
        #                      } else {
        #                          src = outputPorts.get(triggerAsPort.getParent(), trigger);
        #                      }
        #                      if (src != null) {
        #                          connect(createDependencyEdge(triggerAsPort.getDefinition()), src, port);
        #                      }
        #                  } else if (trigger instanceof TimerInstance) {
        #                      KNode src = timerNodes.get(trigger);
        #                      if (src != null) {
        #                          connect(createDependencyEdge(trigger.getDefinition()), src, port);
        #                      }
        #                  }
        #              }
            #              // connect dependencies
        #              for (TriggerInstance dep : reaction.sources) {
        #                  if (reaction.triggers.contains(dep)) continue; // skip
            #                  // Create new port if there is no previous one or each dependency should have its own one
        #                  if (port == null || !self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) {
        #                      port = addInvisiblePort(node);
        #                      self.setLayoutOption(port, CoreOptions.PORT_SIDE, PortSide.WEST);
            #                      if (self.getBooleanValue(REACTIONS_USE_HYPEREDGES) || inputSize == 1) {
        #                          // manual adjustment disabling automatic one
        #                          self.setLayoutOption(port, CoreOptions.PORT_BORDER_OFFSET,
        #                                  (double) -LinguaFrancaShapeExtensions.REACTION_POINTINESS);
        #                      }
        #                  }
            #                  if (dep instanceof PortInstance) {
        #                      KPort src = null;
        #                      PortInstance depAsPort = (PortInstance) dep;
        #                      if (dep.getParent() == reactorInstance) {
        #                          src = parentInputPorts.get(dep);
        #                      } else {
        #                          src = outputPorts.get(depAsPort.getParent(), dep);
        #                      }
        #                      if (src != null) {
        #                          connect(createDependencyEdge(dep.getDefinition()), src, port);
        #                      }
        #                  }
        #              }
            #              // connect outputs
        #              port = null; // enforce new ports for outputs
        #              Set iterSet = reaction.effects != null ? reaction.effects : new HashSet();
        #              for (TriggerInstance effect : iterSet) {
        #                  // Create new port if there is no previous one or each dependency should have its own one
        #                  if (port == null || !self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) {
        #                      port = addInvisiblePort(node);
        #                      self.setLayoutOption(port, CoreOptions.PORT_SIDE, PortSide.EAST);
        #                  }
            #                  if (effect instanceof ActionInstance) {
        #                      actionSources.put((ActionInstance) effect, port);
        #                  } else if (effect instanceof PortInstance) {
        #                      KPort dst = null;
        #                      PortInstance effectAsPort = (PortInstance) effect;
        #                      if (effectAsPort.isOutput()) {
        #                          dst = parentOutputPorts.get(effect);
        #                      } else {
        #                          dst = inputPorts.get(effectAsPort.getParent(), effect);
        #                      }
        #                      if (dst != null) {
        #                          connect(createDependencyEdge(effect), port, dst);
        #                      }
        #                  }
        #              }
        #          }
            #          // Connect actions
        #          Set actions = new HashSet();
        #          actions.addAll(actionSources.keySet());
        #          actions.addAll(actionDestinations.keySet());
            #          for (ActionInstance action : actions) {
        #              KNode node = associateWith(_kNodeExtensions.createNode(), action.getDefinition());
        #              NamedInstanceUtil.linkInstance(node, action);
        #              _utilityExtensions.setID(node, action.uniqueID());
        #              nodes.append(node);
        #              Iterables.addAll(nodes, createUserComments(action.getDefinition(), node));
        #              self.setLayoutOption(node, CoreOptions.PORT_CONSTRAINTS, PortConstraints.FIXED_SIDE);
        #              _layoutPostProcessing.configureAction(node);
        #              Pair ports = _linguaFrancaShapeExtensions.addActionFigureAndPorts(
        #                      node,
        #                      action.isPhysical() ? "P" : "L");
        #              // TODO handle variables?
        #              if (action.getMinDelay() != null && action.getMinDelay() != ActionInstance.DEFAULT_MIN_DELAY) {
        #                  _kLabelExtensions.addOutsideBottomCenteredNodeLabel(
        #                          node,
        #                          String.format("min delay: %s", action.getMinDelay().__str__()),
        #                          7);
        #              }
        #              // TODO default value?
        #              if (action.getDefinition().getMinSpacing() != null) {
        #                  _kLabelExtensions.addOutsideBottomCenteredNodeLabel(node,
        #                          String.format("min spacing: %s", action.getMinSpacing().__str__()),
        #                          7);
        #              }
        #              if (!StringExtensions.isNullOrEmpty(action.getDefinition().getPolicy())) {
        #                  _kLabelExtensions.addOutsideBottomCenteredNodeLabel(node,
        #                          String.format("policy: %s", action.getPolicy().__str__()),
        #                          7);
        #              }
        #              // connect source
        #              for (KPort source : actionSources.get(action)) {
        #                  connect(createDelayEdge(action), source, ports.getKey());
        #              }
            #              // connect targets
        #              for (KPort target : actionDestinations.get(action)) {
        #                  connect(createDelayEdge(action), ports.getValue(), target);
        #              }
        #          }
            #          // Transform connections.
        #          // First, collect all the source ports.
        #          List sourcePorts = new LinkedList(reactorInstance.inputs);
        #          for (ReactorInstance child : reactorInstance.children) {
        #              sourcePorts.addAll(child.outputs);
        #          }
            #          for (PortInstance leftPort : sourcePorts) {
        #              KPort source = leftPort.getParent() == reactorInstance ?
        #                      parentInputPorts.get(leftPort) :
        #                      outputPorts.get(leftPort.getParent(), leftPort);
            #              for (SendRange sendRange : leftPort.getDependentPorts()) {
        #                  for (RuntimeRange rightRange : sendRange.destinations) {
        #                      PortInstance rightPort = rightRange.instance;
        #                      KPort target = rightPort.getParent() == reactorInstance ?
        #                              parentOutputPorts.get(rightPort) :
        #                              inputPorts.get(rightPort.getParent(), rightPort);
        #                      // There should be a connection, but skip if not.
        #                      Connection connection = sendRange.connection;
        #                      if (connection != null) {
        #                          KEdge edge = createIODependencyEdge(connection, (leftPort.isMultiport() || rightPort.isMultiport()));
        #                          if (connection.getDelay() != null) {
        #                              KLabel delayLabel = _kLabelExtensions.addCenterEdgeLabel(edge, ASTUtils.toOriginalText(connection.getDelay()));
        #                              associateWith(delayLabel, connection.getDelay());
        #                              if (connection.isPhysical()) {
        #                                  _linguaFrancaStyleExtensions.applyOnEdgePysicalDelayStyle(delayLabel,
        #                                          reactorInstance.isMainOrFederated() ? Colors.WHITE : Colors.GRAY_95);
        #                              } else {
        #                                  _linguaFrancaStyleExtensions.applyOnEdgeDelayStyle(delayLabel);
        #                              }
        #                          } else if (connection.isPhysical()) {
        #                              KLabel physicalConnectionLabel = _kLabelExtensions.addCenterEdgeLabel(edge, "---");
        #                              _linguaFrancaStyleExtensions.applyOnEdgePysicalStyle(physicalConnectionLabel,
        #                                      reactorInstance.isMainOrFederated() ? Colors.WHITE : Colors.GRAY_95);
        #                          }
        #                          if (source != null && target != null) {
        #                              // check for inside loop (direct in -> out connection with delay)
        #                              if (parentInputPorts.values().contains(source) &&
        #                                      parentOutputPorts.values().contains(target)) {
        #                                  // edge.self.setLayoutOption(CoreOptions.INSIDE_SELF_LOOPS_YO, true) // Does not work as expected
        #                                  // Introduce dummy node to enable direct connection (that is also hidden when collapsed)
        #                                  KNode dummy = _kNodeExtensions.createNode();
        #                                  if (directConnectionDummyNodes.containsKey(target)) {
        #                                      dummy = directConnectionDummyNodes.get(target);
        #                                  } else {
        #                                      nodes.append(dummy);
        #                                      directConnectionDummyNodes.put(target, dummy);
        #                                      _kRenderingExtensions.addInvisibleContainerRendering(dummy);
        #                                      _kNodeExtensions.setNodeSize(dummy, 0, 0);
        #                                      KEdge extraEdge = createIODependencyEdge(null,
        #                                              (leftPort.isMultiport() || rightPort.isMultiport()));
        #                                      connect(extraEdge, dummy, target);
        #                                  }
        #                                  connect(edge, source, dummy);
        #                              } else {
        #                                  connect(edge, source, target);
        #                              }
        #                          }
        #                      }
        #                  }
        #              }
        #          }
            #          // Add startup/shutdown
        #          if (startup != null) {
        #              _linguaFrancaShapeExtensions.addStartupFigure(startupNode);
        #              _utilityExtensions.setID(startupNode, reactorInstance.uniqueID() + "_startup");
        #              NamedInstanceUtil.linkInstance(startupNode, startup);
        #              startupNode.setProperty(REACTION_SPECIAL_TRIGGER, true);
        #              nodes.append(0, startupNode); // add at the start (ordered first)
        #              // try to order with reactions vertically if in one layer
        #              self.setLayoutOption(startupNode, LayeredOptions.POSITION, new KVector(0, 0));
        #              self.setLayoutOption(startupNode, LayeredOptions.LAYERING_LAYER_CONSTRAINT, LayerConstraint.FIRST);
        #              _layoutPostProcessing.configureAction(startupNode);
            #              if (self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) {
        #                  KPort port = addInvisiblePort(startupNode);
        #                  for (it : startupNode.getOutgoingEdges()) {
        #                      it.setSourcePort(port);
        #                  );
        #              }
        #          }
        #          if (shutdown != null) {
        #              _linguaFrancaShapeExtensions.addShutdownFigure(shutdownNode);
        #              _utilityExtensions.setID(shutdownNode, reactorInstance.uniqueID() + "_shutdown");
        #              NamedInstanceUtil.linkInstance(shutdownNode, shutdown);
        #              shutdownNode.setProperty(REACTION_SPECIAL_TRIGGER, true);
        #              nodes.append(shutdownNode); // add at the end (ordered last)
        #              // try to order with reactions vertically if in one layer
        #              _layoutPostProcessing.configureShutDown(shutdownNode);
        #              self.setLayoutOption(shutdownNode, LayeredOptions.POSITION, new KVector(0, len(reactorInstance.reactions) + 1));
            #              if (self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) { // connect all edges to one port
        #                  KPort port = addInvisiblePort(shutdownNode);
        #                  for (it: shutdownNode.getOutgoingEdges()) {
        #                      it.setSourcePort(port);
        #                  };
        #              }
        #          }
        #          if (reset != null) {
        #              _linguaFrancaShapeExtensions.addResetFigure(resetNode);
        #              _utilityExtensions.setID(resetNode, reactorInstance.uniqueID() + "_reset");
        #              NamedInstanceUtil.linkInstance(resetNode, reset);
        #              resetNode.setProperty(REACTION_SPECIAL_TRIGGER, true);
        #              nodes.append(startup != null ? 1 : 0, resetNode); // after startup
        #              // try to order with reactions vertically if in one layer
        #              self.setLayoutOption(resetNode, LayeredOptions.POSITION, new KVector(0, 0.5));
        #              self.setLayoutOption(resetNode, LayeredOptions.LAYERING_LAYER_CONSTRAINT, LayerConstraint.FIRST);
            #              if (self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) { // connect all edges to one port
        #                  KPort port = addInvisiblePort(resetNode);
        #                  for (it : resetNode.getOutgoingEdges()) {
        #                      it.setSourcePort(port);
        #                  };
        #              }
        #          }
            #          // Postprocess timer nodes
        #          if (self.getBooleanValue(REACTIONS_USE_HYPEREDGES)) { // connect all edges to one port
        #              for (KNode timerNode : timerNodes.values()) {
        #                  KPort port = addInvisiblePort(timerNode);
        #                  for (it: timerNode.getOutgoingEdges())  {
        #                      it.setSourcePort(port);
        #                  };
        #              }
        #          }
            #          // Add reaction order edges (add last to have them on top of other edges)
        #          if (len(reactorInstance.reactions) > 1) {
        #              KNode prevNode = reactionNodes.get(IterableExtensions.head(reactorInstance.reactions));
        #              Iterable iterList = IterableExtensions.map(
        #                      IterableExtensions.drop(reactorInstance.reactions, 1),
        #                      reactionNodes.get);
        #              for (KNode node : iterList) {
        #                  KEdge edge = createOrderEdge();
        #                  edge.setSource(prevNode);
        #                  edge.setTarget(node);
        #                  edge.setProperty(CoreOptions.NO_LAYOUT, true);
            #                  // Do not remove them, as they are needed for cycle detection
        #                  KRendering edgeRendering = _kRenderingExtensions.getKRendering(edge);
        #                  _kRenderingExtensions.setInvisible(edgeRendering, !self.getBooleanValue(SHOW_REACTION_ORDER_EDGES));
        #                  _kRenderingExtensions.getInvisible(edgeRendering).setPropagateToChildren(true);
        #                 // TODO this does not work work with incremental update (https://github.com/kieler/KLighD/issues/37)
        #                 // if (!self.getBooleanValue(SHOW_REACTION_ORDER_EDGES)) edge.initiallyHide()
            #                  prevNode = node;
        #              }
        #          }
            #          _layoutPostProcessing.orderChildren(nodes);
        #          _modeDiagrams.handleModes(nodes, reactorInstance);
            #          return nodes;

    def createReactorLabel(self, reactorInstance):
        """ generated source for method createReactorLabel """
        #          StringBuilder b = new "";
        #          if (self.getBooleanValue(SHOW_INSTANCE_NAMES) && !_utilityExtensions.isRoot(reactorInstance)) {
        #              if (!reactorInstance.isMainOrFederated()) {
        #                  b.append(reactorInstance.__name__).append(" : ");
        #              }
        #          }
        #          if (reactorInstance.isMainOrFederated()) {
        #              try {
        #                  b.append(FileUtil.nameWithoutExtension(reactorInstance.reactorDeclaration.eResource()));
        #              } catch (Exception e) {
        #                  throw Exceptions.sneakyThrow(e);
        #              }
        #          } else if (reactorInstance.reactorDeclaration == null) {
        #              // There is an error in the graph.
        #              b.append("<Unresolved Reactor>");
        #          } else {
        #              b.append(reactorInstance.reactorDeclaration.__name__);
        #          }
        #          if (getObjectValue(REACTOR_PARAMETER_MODE) == ReactorParameterDisplayModes.TITLE) {
        #              if (reactorInstance.parameters.isEmpty()) {
        #                  b.append("()");
        #              } else {
        #                  for (it: reactorInstance.parameters){
        #                      b.append(IterableExtensions.join(
        #                              "(",
        #                              ", ",
        #                              ")",
        #                              createParameterLabel(it)
        #                              )
        #                        };
        #              }
        #          }
        #          return b.__str__();

    def addParameterList(self, container, parameters):
        """ generated source for method addParameterList """
        cols = 1
        try:
            cols = int(LinguaFrancaSynthesis.REACTOR_BODY_TABLE_COLS)
        except Exception as e:
            pass
        #  ignore
        if cols > len(parameters):
            cols = len(parameters)
        self._kContainerRenderingExtensions.setGridPlacement(container, cols)
        for param in parameters:
            entry = self._linguaFrancaShapeExtensions.addParameterEntry(container,
                                                                        param.getDefinition(),
                                                                        self.createParameterLabel(param))
            self._kRenderingExtensions.setHorizontalAlignment(entry, HorizontalAlignment.LEFT)

    def createParameterLabel(self, param):
        """ generated source for method createParameterLabel """
        b = ""
        b += param.__name__
        t = param.type.toOriginalText()
        if len(t) > 0:
            b += ":" + t
        if param.getInitialValue():
            b += "("
            b += ', '.join([param.getInitialValue(), ASTUtils.toOriginalText])
            b += ")"
        return b

    def addStateVariableList(self, container, variables):
        """ generated source for method addStateVariableList """
        cols = 1
        try:
            cols = int(LinguaFrancaSynthesis.REACTOR_BODY_TABLE_COLS)
        except Exception as e:
            pass
        #  ignore
        if cols > len(variables):
            cols = len(variables)
        self._kContainerRenderingExtensions.setGridPlacement(container, cols)
        for variable in variables:
            entry = self._linguaFrancaShapeExtensions.addStateEntry(container,
                                                                    variable,
                                                                    self.createStateVariableLabel(variable),
                                                                    variable.isReset())
            self._kRenderingExtensions.setHorizontalAlignment(entry, HorizontalAlignment.LEFT)

    def createStateVariableLabel(self, variable):
        """ generated source for method createStateVariableLabel """
        b = ""
        b += variable.__name__
        if variable.getType() is not None:
            t = InferredType.fromAST(variable.getType())
            b += ":" + t.toOriginalText()
        if variable.getInit() is not None:
            b += "("
            b += ', '.join(variable.getInit(), ASTUtils.toOriginalText)
            b += ")"
        return b

    def createDelayEdge(self, associate):
        """ generated source for method createDelayEdge """
        edge = self._kEdgeExtensions.createEdge()
        self.associateWith(edge, associate)
        line = self._kEdgeExtensions.addPolyline(edge)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(line)
        self._kPolylineExtensions.addJunctionPointDecorator(line)
        if self.getBooleanValue(LinguaFrancaSynthesis.USE_ALTERNATIVE_DASH_PATTERN):
            self._kRenderingExtensions.setLineStyle(line, LineStyle.CUSTOM)
            self._kRenderingExtensions.getLineStyle(line).getDashPattern().\
                addAll(LinguaFrancaSynthesis.ALTERNATIVE_DASH_PATTERN)
        else:
            self._kRenderingExtensions.setLineStyle(line, LineStyle.DASH)
        return edge

    def createIODependencyEdge(self, associate, multiport):
        """ generated source for method createIODependencyEdge """
        edge = self._kEdgeExtensions.createEdge()
        if associate != None:
            self.associateWith(edge, associate)
        line = self._kEdgeExtensions.addPolyline(edge)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(line)
        self._kPolylineExtensions.addJunctionPointDecorator(line)
        if multiport:
            self._kRenderingExtensions.setLineWidth(line, 2.2)
            self._kRenderingExtensions.setLineCap(line, LineCap.CAP_SQUARE)
            self._kPolylineExtensions.setJunctionPointDecorator(line, line.getJunctionPointRendering(), 6, 6)
        return edge

    def createDependencyEdge(self, associate):
        """ generated source for method createDependencyEdge """
        edge = self._kEdgeExtensions.createEdge()
        if associate != None:
            self.associateWith(edge, associate)
        line = self._kEdgeExtensions.addPolyline(edge)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(line)
        self._kPolylineExtensions.addJunctionPointDecorator(line)
        if self.getBooleanValue(LinguaFrancaSynthesis.USE_ALTERNATIVE_DASH_PATTERN):
            self._kRenderingExtensions.setLineStyle(line, LineStyle.CUSTOM)
            self._kRenderingExtensions.getLineStyle(line).getDashPattern().addAll(LinguaFrancaSynthesis.ALTERNATIVE_DASH_PATTERN)
        else:
            self._kRenderingExtensions.setLineStyle(line, LineStyle.DASH)
        return edge

    def createOrderEdge(self):
        """ generated source for method createOrderEdge """
        edge = self._kEdgeExtensions.createEdge()
        line = self._kEdgeExtensions.addPolyline(edge)
        self._kRenderingExtensions.setLineWidth(line, 1.5)
        self._kRenderingExtensions.setLineStyle(line, LineStyle.DOT)
        self._kRenderingExtensions.setForeground(line, Colors.CHOCOLATE_1)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(line)
        self._kPolylineExtensions.addHeadArrowDecorator(line)
        return edge

    @overloaded
    def connect(self, edge, src, dst):
        """ generated source for method connect """
        edge.setSource(src)
        edge.setTarget(dst)
        return edge

    @connect.register(object, KEdge, KNode, KPort)
    def connect_0(self, edge, src, dst):
        """ generated source for method connect_0 """
        edge.setSource(src)
        edge.setTargetPort(dst)
        edge.setTarget(dst.getNode() if dst != None else None)
        return edge

    @connect.register(object, KEdge, KPort, KNode)
    def connect_1(self, edge, src, dst):
        """ generated source for method connect_1 """
        edge.setSourcePort(src)
        edge.setSource(src.getNode() if src != None else None)
        edge.setTarget(dst)
        return edge

    @connect.register(object, KEdge, KPort, KPort)
    def connect_2(self, edge, src, dst):
        """ generated source for method connect_2 """
        edge.setSourcePort(src)
        edge.setSource(src.getNode() if src != None else None)
        edge.setTargetPort(dst)
        edge.setTarget(dst.getNode() if dst != None else None)
        return edge

    def addIOPort(self, node, lfPort, input, multiport, bank):
        """ generated source for method addIOPort """

    def addInvisiblePort(self, node):
        """ generated source for method addInvisiblePort """
        port = self._kPortExtensions.createPort()
        node.getPorts().append(port)
        port.setSize(0, 0)
        return port

    def addErrorComment(self, node, message):
        """ generated source for method addErrorComment """
        comment = self._kNodeExtensions.createNode()
        self.setLayoutOption(comment, CoreOptions.COMMENT_BOX, True)
        commentFigure = self._linguaFrancaShapeExtensions.addCommentFigure(comment, message)
        self._linguaFrancaStyleExtensions.errorStyle(commentFigure)
        self._kRenderingExtensions.setBackground(commentFigure, Colors.PEACH_PUFF_2)
        edge = self._kEdgeExtensions.createEdge()
        edge.setSource(comment)
        edge.setTarget(node)
        self._linguaFrancaStyleExtensions.errorStyle(self._linguaFrancaShapeExtensions.addCommentPolyline(edge))
        return comment

    def createUserComments(self, element, targetNode):
        """ generated source for method createUserComments """
        if self.getBooleanValue(self.SHOW_USER_LABELS):
            commentText = AttributeUtils.label(element)
            if len(commentText) > 0:
                comment = self._kNodeExtensions.createNode()
                self.setLayoutOption(comment, CoreOptions.COMMENT_BOX, True)
                commentFigure = self._linguaFrancaShapeExtensions.addCommentFigure(comment, commentText)
                self._linguaFrancaStyleExtensions.commentStyle(commentFigure)
                edge = self._kEdgeExtensions.createEdge()
                edge.setSource(comment)
                edge.setTarget(targetNode)
                self._linguaFrancaStyleExtensions.commentStyle(self._linguaFrancaShapeExtensions.addCommentPolyline(edge))
                return list(comment)
        return list()
