#!/usr/bin/env python
""" generated source for module FederateInstance """
#  Instance of a federate specification. 
# 
# Copyright (c) 2020, The University of California at Berkeley.
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
from include.SpecialExceptions import IllegalStateException
from include.overloading import overloaded
# package: org.lflang.federated
# import java.util.ArrayList
# import java.util.LinkedHashMap
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Map
# import java.util.Set
# import java.util.stream.Collectors
# import java.util.stream.Stream
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import com.google.common.base.Objects

#  
#  * Instance of a federate, or marker that no federation has been defined
#  * (if isSingleton() returns true). Every top-level reactor (contained
#  * directly by the main reactor) is a federate, so there will be one
#  * instance of this class for each top-level reactor.
#  * 
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#
from lflang import generator
from lflang.ASTUtils import ASTUtils
from lflang.TimeValue import TimeValue
from lflang.generator.ReactorInstance import ReactorInstance
from lflang.lf.Action import Action
from lflang.lf.ActionOrigin import ActionOrigin
from lflang.lf.Output import Output
from lflang.lf.Reaction import Reaction
from lflang.lf.Timer import Timer
from lflang.lf.VarRef import VarRef


class FederateInstance(object):
    def __init__(self, instantiation, id, bankIndex, generator, errorReporter):
        """
        Construct a new instance with the specified instantiation of
        of a top-level reactor. The federate will be given the specified
        integer ID.
        :param instantiation: The instantiation of the top-level reactor, or null if there is no federation.
        :param id: The integer ID of this federate.
        :param bankIndex: The position within a bank of reactors for this federate.
                          This is 0 if the instantiation is not a bank of reactors.
        :param generator: The generator using this
        FIXME: Do we really need to pass the complete generator here? It is only used to determine the number of federates.
        :param errorReporter: An error reporter
        """
        self.instantiation = instantiation
        self.id = id
        self.generator = generator
        self.bankIndex = bankIndex
        # A list of outputs that can be triggered directly or indirectly by physical actions.
        self.outputsConnectedToPhysicalActions = []
        # The host, if specified using the 'at' keyword.
        self.host = "localhost"

        # Cached result of analysis of which reactions to exclude from main.
        self.excludeReactions = None
        self.errorReporter = errorReporter
        # The name of this federate instance. This will be the instantiation
        # name, poassibly appended with "__n", where n is the bank position of
        # this instance if the instantiation is of a bank of reactors.
        self.name = "Unnamed"
        if instantiation is not None:
            self.name = instantiation.__name__
            #  If the instantiation is in a bank, then we have to append
            #  the bank index to the name.
            if instantiation.getWidthSpec()is not None:
                self.name = instantiation.__name__ + "__" + bankIndex

        # Map from the federates that this federate receives messages from
        # to the delays on connections from that federate. The delay set
        # may may include null, meaning that there is a connection
        # from the federate instance that has no delay.
        #
        self.dependsOn = {}

        # The directory, if specified using the 'at' keyword.
        #
        self.dir = None

        # The port, if specified using the 'at' keyword.
        #
        self.port = 0

        # Map from the federates that this federate sends messages to
        # to the delays on connections to that federate. The delay set
        # may may include null, meaning that there is a connection
        # from the federate instance that has no delay.
        #
        self.sendsTo = {}

        # The user, if specified using the 'at' keyword.
        #
        self.user = None

        # List of networkMessage actions. Each of these handles a message
        #  received from another federate over the network. The ID of
        #  receiving port is simply the position of the action in the list.
        #  The sending federate needs to specify this ID.
        #
        self.networkMessageActions = []

        #  A set of federates with which this federate has an inbound connection
        #  There will only be one physical connection even if federate A has defined multiple
        #  physical connections to federate B. The message handler on federate A will be
        #  responsible for including the appropriate information in the message header (such as port ID)
        #  to help the receiver distinguish different events.
        self.inboundP2PConnections = {}

        # A list of federate with which this federate has an outbound physical connection.
        # There will only be one physical connection even if federate A has defined multiple
        # physical connections to federate B. The message handler on federate B will be
        # responsible for distinguishing the incoming messages by parsing their header and
        # scheduling the appropriate action.
        self.outboundP2PConnections = {}

        # A list of triggers for network input control reactions. This is used to trigger
        # all the input network control reactions that might be nested in a hierarchy.
        self.networkInputControlReactionsTriggers = []

        # The trigger that triggers the output control reaction of this
        # federate.
        #
        # The network output control reactions send a PORT_ABSENT message for a network output port,
        # if it is absent at the current tag, to notify all downstream federates that no value will
        # be present on the given network port, allowing input control reactions on those federates
        # to stop blocking.
        self.networkOutputControlReactionsTrigger = None

        #  Indicates whether the federate is remote or local
        self.isRemote = False

        # List of generated network reactions (network receivers,
        # network input control reactions, network senders, and network output control
        # reactions) that belong to this federate instance.
        #
        self.networkReactions = []

        # List of triggers of network reactions that belong to remote federates.
        # These might need to be removed before code generation to avoid unnecessary compile
        # errors, since they might reference structures that are not present in
        # the current federate. Even though it is impossible for a trigger that is on a remote
        # federate to trigger a reaction on this federate, these triggers need to be here
        # to ensure that dependency analysis between reactions is done correctly.
        # Without these triggers, the reaction precedence graph is broken and
        # dependencies not properly represented.
        #
        self.remoteNetworkReactionTriggers = []

    def getGenerator(self):
        """
        Returns the generator that is using this federate instance
        generated source for method getGenerator
        """
        return self.generator

    # ///////////////////////////////////////////
    # // Public Methods

    @overloaded
    def contains(self, action):
        """
        Return true if the specified action should be included in the code generated
        for the federate. This means that either the action is used as a trigger,
        a source, or an effect in a top-level reaction that belongs to this federate.
        This returns true if the program is not federated.
        :param action: The action
        :return: True if this federate contains the action in the specified reactor
        """
        reactor = ASTUtils.getEnclosingReactor(action)
        if not reactor.isFederated() or self.isSingleton():
            return True
        #  If the action is used as a trigger, a source, or an effect for a top-level reaction
        #  that belongs to this federate, then generate it.
        for react in ASTUtils.allReactions(reactor):
            if self.contains(react):
                #  Look in triggers
                for trigger in (react.getTriggers()):
                    if isinstance(trigger, VarRef):
                        triggerAsVarRef = trigger
                        if triggerAsVarRef.getVariable() == action:
                            return True
                #  Look in sources
                for source in react.getSources():
                    if source.getVariable() == action:
                        return True
                #  Look in effects
                for effect in react.getEffects():
                    if effect.getVariable() == action:
                        return True
        return False

    @contains.register(object, Reaction)
    def contains_0(self, reaction):
        """
        Return true if the specified reaction should be included in the code generated for this
        federate at the top-level. This means that if the reaction is triggered by or
        sends data to a port of a contained reactor, then that reaction
        is in the federate. Otherwise, return false.
        NOTE: This method assumes that it will not be called with reaction arguments
        that are within other federates. It should only be called on reactions that are
        either at the top level or within this federate. For this reason, for any reaction
        not at the top level, it returns true.

        :param reaction: The reaction.
        :return:
        """
        reactor = ASTUtils.getEnclosingReactor(reaction)
        if not reactor.isFederated() or self.isSingleton():
            return True
        if not reactor.getReactions().contains(reaction):
            return False
        if self.networkReactions.contains(reaction):
            #  Reaction is a network reaction that belongs to this federate
            return True
        reactionBankIndex = generator.getReactionBankIndex(reaction)
        if reactionBankIndex >= 0 and self.bankIndex >= 0 and reactionBankIndex != self.bankIndex:
            return False
        #  If this has been called before, then the result of the
        #  following check is cached.
        if self.excludeReactions != None:
            return not self.excludeReactions.contains(reaction)
        self.indexExcludedTopLevelReactions(reactor)
        return not self.excludeReactions.contains(reaction)

    @contains.register(object, ReactorInstance)
    def contains_1(self, instance):
        """
        Return true if the specified reactor instance or any parent
        reactor instance is contained by this federate.
        If the specified instance is the top-level reactor, return true
        (the top-level reactor belongs to all federates).
        If this federate instance is a singleton, then return true if the
        instance is non null.
        NOTE: If the instance is bank within the top level, then this
        returns true even though only one of the bank members is in the federate.

        :param instance:  The reactor instance.
        :return: True if this federate contains the reactor instance
        """
        """ generated source for method contains_1 """
        if self.isSingleton():
            return instance != None
        if instance.getParent() == None:
            return True
            #  Top-level reactor
        #  Start with this instance, then check its parents.
        i = instance
        while i != None:
            if i.getDefinition() == self.instantiation:
                return True
            i = i.getParent()
        return False

    @contains.register(object, Timer)
    def contains_2(self, timer):
        """
        Return true if the specified timer should be included in the code generated
        for the federate. This means that the timer is used as a trigger
        in a top-level reaction that belongs to this federate.
        This also returns true if the program is not federated.
        :param timer: The action
        :return: True if this federate contains the action in the specified reactor
        """
        """ generated source for method contains_2 """
        reactor = ASTUtils.getEnclosingReactor(timer)
        if not reactor.isFederated() or self.isSingleton():
            return True
        #  If the action is used as a trigger, a source, or an effect for a top-level reaction
        #  that belongs to this federate, then generate it.
        for r in ASTUtils.allReactions(reactor):
            if self.contains(r):
                #  Look in triggers
                for trigger in self.convertToEmptyListIfNull(r.getTriggers()):
                    if isinstance(trigger, (VarRef)):
                        triggerAsVarRef = trigger
                        if triggerAsVarRef.getVariable() == timer:
                            return True
        return False

    def numRuntimeInstances(self, reactor):
        """
        Return the total number of runtime instances of the specified reactor
        instance in this federate. This is zero if the reactor is not in the
        federate at all, and otherwise is the product of the bank widths of
        all the parent containers of the instance, except that if the depth
        one parent is bank, its width is ignored (only one bank member can be
        in any federate).

        :param reactor:
        :return:
        """
        """ generated source for method numRuntimeInstances """
        if not self.contains(reactor):
            return 0
        depth = 0 if self.isSingleton() else 1
        return reactor.getTotalWidth(depth)

    def indexExcludedTopLevelReactions(self, federatedReactor):
        """
        Build an index of reactions at the top-level (in the
        federatedReactor) that don't belong to this federate
        instance. This index is put in the excludeReactions
        class variable.
        :param federatedReactor: The top-level federated reactor
        :return:
        """
        """ generated source for method indexExcludedTopLevelReactions """
        inFederate = False
        if self.excludeReactions != None:
            raise IllegalStateException("The index for excluded reactions at the top level is already built.")
        excludeReactions = {}
        #  Construct the set of excluded reactions for this federate.
        #  If a reaction is a network reaction that belongs to this federate, we
        #  don't need to perform this analysis.
        #   Iterable reactions = IterableExtensions.filter(ASTUtils.allReactions(federatedReactor),
        reactions = []
        for it in ASTUtils.allReactions(federatedReactor):
            if self.networkReactions.find(it) <= 0:
                reactions.append(it)
        for react in reactions:
            #  Create a collection of all the VarRefs (i.e., triggers, sources, and effects) in the react 
            #  signature that are ports that reference federates.
            #  We then later check that all these VarRefs reference this federate. If not, we will add this
            #  react to the list of reactions that have to be excluded (note that mixing VarRefs from
            #  different federates is not allowed).
            allVarRefsReferencingFederates = []
            #  Add all the triggers that are outputs
            #              Stream triggersAsVarRef = react.getTriggers().stream().filter(it -> it instanceof VarRef).map(it -> (VarRef) it);
            #             allVarRefsReferencingFederates.addAll(
            #                 triggersAsVarRef.filter(it -> it.getVariable() instanceof Output).collect(Collectors.toList())
            #             );
            #  Add all the sources that are outputs
            #             allVarRefsReferencingFederates.addAll(
            #                 react.getSources().stream().filter(it -> it.getVariable() instanceof Output).collect(Collectors.toList())
            #             );
            #  Add all the effects that are inputs
            #             allVarRefsReferencingFederates.addAll(
            #                 react.getEffects().stream().filter(it -> it.getVariable() instanceof Input).collect(Collectors.toList())
            #             ); 
            inFederate = self.containsAllVarRefs(allVarRefsReferencingFederates)
            if not inFederate:
                excludeReactions.append(react)

    def containsAllVarRefs(self, varRefs):
        """
        Return true if all members of 'varRefs' belong to this federate.
        As a convenience measure, if some members of 'varRefs' are from
        different federates, also report an error.

        :param varRefs: A collection of VarRefs
        :return:
        """
        """ generated source for method containsAllVarRefs """
        referencesFederate = False
        inFederate = True
        for varRef in varRefs:
            if varRef.getContainer() == self.instantiation:
                referencesFederate = True
            else:
                if referencesFederate:
                    self.errorReporter.reportError(varRef, "Mixed triggers and effects from" + " different federates. This is not permitted")
                inFederate = False
        return inFederate

    def isSingleton(self):
        """
        Return true if this is singleton, meaning either that no federation
        has been defined or that there is only one federate.
        :return: True if no federation has been defined or there is only one federate.
        """
        """ generated source for method isSingleton """
        return ((self.instantiation == None) or (len(generator.federates) <= 1))

    def findOutputsConnectedToPhysicalActions(self, instance):
        """
        Find output ports that are connected to a physical action trigger upstream
        in the same reactor. Return a list of such outputs paired with the minimum delay
        from the nearest physical action.
        :param instance: The reactor instance containing the output ports
        :return: A LinkedHashMap
        """


        """ generated source for method findOutputsConnectedToPhysicalActions """
        physicalActionToOutputMinDelay = {}
        #  Find reactions that write to the output port of the reactor
        for output in instance.outputs:
            for reaction in output.getDependsOnReactions():
                minDelay = self.findNearestPhysicalActionTrigger(reaction)
                if not minDelay == TimeValue.MAX_VALUE:
                    physicalActionToOutputMinDelay.put(output.getDefinition(), minDelay)
        return physicalActionToOutputMinDelay

    def __str__(self):
        """ generated source for method toString """
        return "Federate " + self.id + ": " + self.instantiation.__name__

    def findNearestPhysicalActionTrigger(self, reaction):
        """
        Find the nearest (shortest) path to a physical action trigger from this
         'reaction' in terms of minimum delay.
        :param reaction: The reaction to start with
        :return: The minimum delay found to the nearest physical action and TimeValue.MAX_VALUE otherwise
        """
        minDelay = TimeValue.MAX_VALUE
        for trigger in reaction.triggers:
            if isinstance(trigger, Action):
                action = trigger.getDefinition()
                actionInstance = trigger
                if action.getOrigin() == ActionOrigin.PHYSICAL:
                    if actionInstance.getMinDelay().isEarlierThan(minDelay):
                        minDelay = actionInstance.getMinDelay()
                elif action.getOrigin() == ActionOrigin.LOGICAL:
                    #  Logical action
                    #  Follow it upstream inside the reactor
                    for uReaction in actionInstance.getDependsOnReactions():
                        #  Avoid a loop
                        if not uReaction == reaction:
                            uMinDelay = actionInstance.getMinDelay().append(self.findNearestPhysicalActionTrigger(uReaction))
                            if uMinDelay.isEarlierThan(minDelay):
                                minDelay = uMinDelay
            elif isinstance(trigger, Output):
                #  Outputs of contained reactions
                outputInstance = trigger
                for uReaction in outputInstance.getDependsOnReactions():
                    uMinDelay = self.findNearestPhysicalActionTrigger(uReaction)
                    if uMinDelay.isEarlierThan(minDelay):
                        minDelay = uMinDelay
        return minDelay

    #      * Remove triggers in this federate's network reactions that are defined in remote federates.
    #      
    def removeRemoteFederateConnectionPorts(self):
        """ generated source for method removeRemoteFederateConnectionPorts """
        for reaction in self.networkReactions:
            reaction.getTriggers().removeAll(self.remoteNetworkReactionTriggers)

    #  TODO: Put this function into a utils file instead
    def convertToEmptyListIfNull(self, list):
        """ generated source for method convertToEmptyListIfNull """
        return [] if list == None else list
