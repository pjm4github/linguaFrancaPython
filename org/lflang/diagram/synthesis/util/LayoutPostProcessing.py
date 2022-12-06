#!/usr/bin/env python
""" generated source for module LayoutPostProcessing """
# 
# Copyright (c) 2022, Kiel University.
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
# import java.util.Arrays
# import java.util.Comparator
# import java.util.List
# import org.eclipse.elk.alg.layered.components.ComponentOrderingStrategy
# import org.eclipse.elk.alg.layered.options.CrossingMinimizationStrategy
# import org.eclipse.elk.alg.layered.options.CycleBreakingStrategy
# import org.eclipse.elk.alg.layered.options.GreedySwitchType
# import org.eclipse.elk.alg.layered.options.LayeredOptions
# import org.eclipse.elk.alg.layered.options.OrderingStrategy
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.nodemodel.util.NodeModelUtils
from lflang.LFast.Nodemodels import NodeModelUtils
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import SynthesisOption, DiagramSyntheses, \
    CoreOptions
from org.lflang.diagram.synthesis import AbstractSynthesisExtensions

from org.lflang.diagram.synthesis import LinguaFrancaSynthesis

from org.lflang.generator.TriggerInstance import *
# import de.cau.cs.kieler.klighd.SynthesisOption
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.syntheses.DiagramSyntheses

# 
# Set layout configuration options for the Lingua Franca diagram synthesis.
# @author{Sören Domrös <sdo@informatik.uni-kiel.de>}
#  
class Comparator:
    pass


class NamedInstanceUtil:
    pass


class BuiltinTriggerVariable:
    pass


class LayeredOptions:
    pass


class CycleBreakingStrategy:
    pass


class GreedySwitchType:
    pass


class EObject:
    pass


class OrderingStrategy:
    pass


class ComponentOrderingStrategy:
    pass


class CrossingMinimizationStrategy:
    pass


class LayoutPostProcessing(AbstractSynthesisExtensions):
    STARTUP, RESET, SHUTDOWN, MAX_VALUE = range(4)
    """ generated source for class LayoutPostProcessing """
    #  Synthesis option to control the order of nodes and edges by model order. 
    MODEL_ORDER_OPTION = "Model Order"

    #  Uses semi-automatic layout. 
    LEGACY = "Legacy"

    #  Only reactions are strictly ordered by their model order. 
    STRICT_REACTION_ONLY = "Reactions Only"

    #  Reactions and reactor are strictly ordered by their model order. 
    STRICT = "Reactions and Reactors"

    #  Reactions and reactors are ordered by their model order if no additional crossing are created. 
    TIE_BREAKER = "Optimize Crossings"

    # No crossing minimization is done at all. This requires that actions and timers are sorted based on their model
    # order.
    FULL_CONTROL = "Full Control"
    MODEL_ORDER = SynthesisOption.createChoiceOption(MODEL_ORDER_OPTION, [TIE_BREAKER, STRICT_REACTION_ONLY, STRICT, FULL_CONTROL], STRICT_REACTION_ONLY).setCategory(LinguaFrancaSynthesis.LAYOUT)

    # Comparator to sort KNodes based on the textual order of their linked instances.
    #
    # Startup, reset and shutdown actions are not in the model and are handled separately:
    # Startup actions will always be first.
    # Reset actions follow after the startup action.
    # Shutdown is always sorted last. However, shutdown actions will not have a model order set and are, therefore,
    # implicitly ordered by their connection.
    #      
    TEXTUAL_ORDER = Comparator()

    def compare(self, node1, node2):
        """ generated source for method compare """
        pos1 = self.getTextPosition(node1)
        pos2 = self.getTextPosition(node2)
        if pos1 >= 0 and pos1 >= 0:
            return pos1 > pos2
        elif pos1 >= 0:
            return -1
        elif pos2 >= 0:
            return 1
        return node1.hashCode() > node2.hashCode()

    def getTextPosition(self, node):
        """ generated source for method getTextPosition """
        instance = NamedInstanceUtil.getLinkedInstance(node)
        if instance != None:
            definition = instance.getDefinition()
            if isinstance(definition, BuiltinTriggerVariable):
                if (definition).type == NamedInstanceUtil.STARTUP:
                    return 0
                elif (definition).type == NamedInstanceUtil.RESET:
                    return 1
                elif (definition).type == NamedInstanceUtil.SHUTDOWN:
                    return int.MAX_VALUE
            elif isinstance(definition, EObject):
                ast = NodeModelUtils.getNode(definition)
                if ast != None:
                    return ast.getOffset()
        return -1

    def configureMainReactor(self, node):
        """
        Configures layout options for main reactor.
        :param node: The KNode of the main reactor.
        :return:
        """
        """ generated source for method configureMainReactor """
        self.configureReactor(node)

    def configureReactor(self, node):
        """
        Configures layout options for a reactor.
        :param node: The KNode of a reactor.
        :return:
        """
        """ generated source for method configureReactor """
        modelOrderStrategy = str(self.MODEL_ORDER.getObjectValue())
        if modelOrderStrategy == self.LEGACY:
            #  Otherwise nodes are not sorted if they are not connected
            DiagramSyntheses.setLayoutOption(node, CoreOptions.SEPARATE_CONNECTED_COMPONENTS, False)
            #  Needed to enforce node positions.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_SEMI_INTERACTIVE, True)
            #  Costs a little more time but layout is quick, therefore, we can do that.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.THOROUGHNESS, 100)
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_GREEDY_SWITCH_TYPE, GreedySwitchType.TWO_SIDED)
        elif modelOrderStrategy == self.STRICT_REACTION_ONLY:
            #  Only set model order for reactions.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, True)
            #  Do tie-breaking model order cycle breaking. 
            #  Minimize number of backward edges but make decisions based on the model order if no greedy best alternative exists.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CYCLE_BREAKING_STRATEGY, CycleBreakingStrategy.GREEDY_MODEL_ORDER)
            #  Before crossing minimization sort all nodes and edges/ports but also consider the node model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_STRATEGY, OrderingStrategy.NODES_AND_EDGES)
            #  Separate connected components should be drawn separately.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.SEPARATE_CONNECTED_COMPONENTS, True)
            #  Component order is enforced by looking at the minimum element with respect to model order of each component.
            #  Remember that the startUp action is always the first node.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_COMPONENTS, ComponentOrderingStrategy.FORCE_MODEL_ORDER)
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.COMPACTION_CONNECTED_COMPONENTS, True)
            #  Node order should not change during crossing minimization.
            #  Since only reactions will have a model order set in this approach the order of reactions in their respective
            #  separate connected components always respects the model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_FORCE_NODE_MODEL_ORDER, True)
            #  Disable greedy switch since this does otherwise change the node order after crossing minimization.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_GREEDY_SWITCH_TYPE, GreedySwitchType.OFF)
        elif modelOrderStrategy == self.STRICT:
            #  Do tie-breaking model order cycle breaking. 
            #  Minimize number of backward edges but make decisions based on the model order if no greedy best alternative exists.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CYCLE_BREAKING_STRATEGY, CycleBreakingStrategy.GREEDY_MODEL_ORDER)
            #  Before crossing minimization sort all nodes and edges/ports but also consider the node model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_STRATEGY, OrderingStrategy.NODES_AND_EDGES)
            #  Separate connected components should be drawn separately.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.SEPARATE_CONNECTED_COMPONENTS, True)
            #  Component order is enforced by looking at the minimum element with respect to model order of each component.
            #  Remember that the startUp action is always the first node.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_COMPONENTS, ComponentOrderingStrategy.FORCE_MODEL_ORDER)
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.COMPACTION_CONNECTED_COMPONENTS, True)
            #  Node order should not change during crossing minimization.
            #  Since only reactions and reactors will have a model order set in this approach the order of reactions and reactors in their respective
            #  separate connected components always respects the model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_FORCE_NODE_MODEL_ORDER, True)
            #  Disable greedy switch since this does otherwise change the node order after crossing minimization.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_GREEDY_SWITCH_TYPE, GreedySwitchType.OFF)
        elif modelOrderStrategy == self.TIE_BREAKER:
            #  Do tie-breaking model order cycle breaking. 
            #  Minimize number of backward edges but make decisions based on the model order if no greedy best alternative exists.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CYCLE_BREAKING_STRATEGY, CycleBreakingStrategy.GREEDY_MODEL_ORDER)
            #  Before crossing minimization sort all nodes and edges/ports but also consider the node model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_STRATEGY, OrderingStrategy.NODES_AND_EDGES)
            #  Separate connected components should be drawn separately.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.SEPARATE_CONNECTED_COMPONENTS, True)
            #  Component order is enforced by looking at the minimum element with respect to model order of each component.
            #  Remember that the startUp action is always the first node.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_COMPONENTS, ComponentOrderingStrategy.FORCE_MODEL_ORDER)
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.COMPACTION_CONNECTED_COMPONENTS, True)
            #  During crossing minimization 10 node order violations are regarded as important as 1 edge crossing.
            #  In reality this chooses the best node order from all tries.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_CROSSING_COUNTER_NODE_INFLUENCE, 0.1)
            #  Increase the number of tries with different starting configurations.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.THOROUGHNESS, 100)
        elif modelOrderStrategy == self.FULL_CONTROL:
            #  Do strict model order cycle breaking. This may introduce unnecessary backward edges.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CYCLE_BREAKING_STRATEGY, CycleBreakingStrategy.MODEL_ORDER)
            #  Before crossing minimization sort all nodes and edges/ports but also consider the node model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_STRATEGY, OrderingStrategy.NODES_AND_EDGES)
            #  Separate connected components should be drawn separately.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.SEPARATE_CONNECTED_COMPONENTS, True)
            #  Component order is enforced by looking at the minimum element with respect to model order of each component.
            #  Remember that the startUp action is always the first node.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_COMPONENTS, ComponentOrderingStrategy.FORCE_MODEL_ORDER)
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.COMPACTION_CONNECTED_COMPONENTS, True)
            #  Disable all kinds of crossing minimization entirely. Just take what is in the model and just do it.
            #  This requires that the list of nodes is not ordered by type, e.g. first all reactions, then all reactors, then all actions, ...
            #  but by their model order. In other approaches ordering actions between the reactions has no effect.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_STRATEGY, CrossingMinimizationStrategy.NONE)
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CROSSING_MINIMIZATION_GREEDY_SWITCH_TYPE, GreedySwitchType.OFF)
        else:
            pass
        #  Do nothing.

    def configureAction(self, node):
        """
        Configures layout options for an action.
        :param node: The KNode of an action.
        :return:
        """
        """ generated source for method configureAction """
        modelOrderStrategy = str(self.MODEL_ORDER.getObjectValue())
        if modelOrderStrategy == self.STRICT_REACTION_ONLY:
            pass
        elif modelOrderStrategy == self.STRICT:
            pass
        elif modelOrderStrategy == self.TIE_BREAKER:
            #  Actions have no model order since their ordering in the model cannot be compared to the order of
            #  for example reactions since they are generally defined below in inputs/outputs and above the reactions.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, True)
        elif modelOrderStrategy == self.FULL_CONTROL:
            #  Give actions a model order since they should be controllable too.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, False)
        else:
            pass
        #  Do nothing.

    def configureTimer(self, node):
        """
        Configures layout options for a timer.
        :param node: The KNode of a timer.
        :return:
        """
        """ generated source for method configureTimer """
        modelOrderStrategy = str(self.MODEL_ORDER.getObjectValue())
        if modelOrderStrategy == self.STRICT_REACTION_ONLY:
            pass
        elif modelOrderStrategy == self.STRICT:
            pass
        elif modelOrderStrategy == self.TIE_BREAKER:
            #  Timers have no model order since their ordering in the model cannot be compared to the order of
            #  for example reactions since they are generally defined below in inputs/outputs and above the reactions.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, True)
        elif modelOrderStrategy == self.FULL_CONTROL:
            #  Give timers a model order since they should be controllable too.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, False)
        else:
            pass
        #  Do nothing.


    def configureStartUp(self, node):
        """
        Configures layout options for a startup action.
        :param node: The KNode of a startup action.
        :return:
        """
        #  Nothing should be done. Model order is considered per default value.
        #  The actual ordering of this node has to be done in the synthesis.
        pass

    def configureShutDown(self, node):
        """
        Configures layout options for a shutdown action.
        :param node: The KNode of a shutdown action.
        :return:
        """
        """ generated source for method configureShutDown """
        modelOrderStrategy = str(self.MODEL_ORDER.getObjectValue())
        if modelOrderStrategy == self.STRICT_REACTION_ONLY:
            pass
        elif modelOrderStrategy == self.STRICT:
            pass
        elif modelOrderStrategy == self.TIE_BREAKER:
            pass
        elif modelOrderStrategy == self.FULL_CONTROL:
            #  The shutdown node cannot have a high model order, since this would confuse cycle breaking.
            #  It  also cannot have a low model order.
            #  It should have none at all and the other nodes should define its position.
            #  This is no problem since the shutdown node has only outgoing edges.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, True)
        else:
            pass
        #  Do nothing.

    def configureReaction(self, node):
        """
        Configures layout options for a reaction.
        Currently a reaction does not have internal behavior that is visualized and its order is always considered,
        therefore, nothing needs to be done.

        :param node: The KNode of a reaction.
        :return:
        """
        #  Has no internal behavior and model order is set by default.
        pass


    def configureDummy(self, node):
        """
        Configures layout options for a dummy node.
        :param node: The KNode of a dummy node.
        :return:
        """
        """ generated source for method configureDummy """
        modelOrderStrategy = str(self.MODEL_ORDER.getObjectValue())
        if modelOrderStrategy == self.STRICT_REACTION_ONLY:
            pass
        elif modelOrderStrategy == self.STRICT:
            pass
        elif modelOrderStrategy == self.TIE_BREAKER:
            pass
        elif modelOrderStrategy == self.FULL_CONTROL:
            #  A dummy node has no model order.
            DiagramSyntheses.setLayoutOption(node, LayeredOptions.CONSIDER_MODEL_ORDER_NO_MODEL_ORDER, True)
        else:
            pass
        #  Do nothing.

    def orderChildren(self, nodes):
        """
        Orders a list of nodes by their corresponding linked instance if synthesis option for full control is enabled.
        Ordering is done by the {@link #TEXTUAL_ORDER} comparator.
        :param nodes: List of KNodes to be ordered.
        :return:
        """
        """ generated source for method orderChildren """
        modelOrderStrategy = str(self.MODEL_ORDER.getObjectValue())
        if self.FULL_CONTROL == modelOrderStrategy:
            nodes.sort(self.TEXTUAL_ORDER)
