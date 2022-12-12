#!/usr/bin/env python
""" generated source for module ReactionInstance """
#  Representation of a runtime instance of a reaction. 
# 
# Copyright (c) 2019-2022, The University of California at Berkeley.
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
# package: lflang.generator
# import java.util.ArrayList
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Set
from lflang.generator.ActionInstance import ActionInstance
from lflang.generator.DeadlineInstance import DeadlineInstance
from lflang.generator.InvalidSourceException import InvalidSourceException
from lflang.generator.NamedInstance import NamedInstance
from lflang.TimeUnit import TimeUnit
from lflang.TimeValue import TimeValue
from lflang.generator.PortInstance import PortInstance
from lflang.lf.Action import Action
from lflang.lf.BuiltinTriggerRef import BuiltinTriggerRef
from lflang.lf.Port import Port
from lflang.lf.Timer import Timer
from lflang.lf.VarRef import VarRef
# 
#  * Representation of a compile-time instance of a reaction.
#  * Like {@link ReactorInstance}, one or more parents of this reaction
#  * is a bank of reactors, then there will be more than one runtime instance
#  * corresponding to this compile-time instance.  The {@link #getRuntimeInstances()}
#  * method returns a list of these runtime instances, each an instance of the
#  * inner class {@link ReactionInstance.Runtime}.  Each runtime instance has a "level", which is
#  * its depth an acyclic precedence graph representing the dependencies between
#  * reactions at a tag.
#  *  
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  
class ReactionInstance(NamedInstance):
    #     UNORDERED_REACTION_MARKER: Sadly, we have no way to mark reaction "unordered" in the AST,
    #      * so instead, we use a magic comment at the start of the reaction body.
    #      * This is that magic comment.
    UNORDERED_REACTION_MARKER = "**** This reaction is unordered."


    def __init__(self, definition, parent, isUnordered, index):
        """
        Create a new reaction instance from the specified definition
        within the specified parent. This constructor should be called
        only by the ReactorInstance class, but it is public to enable unit tests.

        :param definition: A reaction definition.
        :param parent: The parent reactor instance, which cannot be null.
        :param isUnordered: Indicator that this reaction is unordered w.r.t. other reactions.
        :param index: The index of the reaction within the reactor (0 for the
                      first reaction, 1 for the second, etc.).
        """
        super().__init__(definition, parent)
        #
        #  chainID: Indicates the chain this reaction is a part of. It is constructed
        #  through a bit-wise or among all upstream chains. Each fork in the
        #  dependency graph setting a new, unused bit to true in order to
        #  disambiguate it from parallel chains. Note that zero results in
        #  no overlap with any other reaction, which means the reaction can
        #  execute in parallel with any other reaction. The default is 1L.
        #  If left at the default, parallel execution will be based purely
        #  on levels.
        self.chainID = 1

        # effects: The ports or actions that this reaction may write to.
        self.effects = []

        #    sources: The ports, actions, or timers that this reaction is triggered by or uses.
        # FIXME: Above sources is misnamed because in the grammar,
        # "sources" are only the inputs a reaction reads without being
        # triggered by them. The name "reads" used here would be a better
        # choice in the grammar.
        self.sources = []

        #  declaredDeadline: Deadline for this reaction instance, if declared.
        self.declaredDeadline = None

        #  Cache of the set of downstream reactions.
        self.dependentReactionsCache = []
        #  Cache of the set of upstream reactions.
        self.dependsOnReactionsCache = []

        # Array of runtime instances of this reaction.
        # This has length 1 unless the reaction is contained
        # by one or more banks.  Suppose that this reaction
        # has depth 3, with full name r0.r1.r2.r. The top-level
        # reactor is r0, which contains r1, which contains r2,
        # which contains this reaction r.  Suppose the widths
        # of the containing reactors are w0, w1, and w2, and
        # we are interested in the instance at bank indexes
        # b0, b1, and b2.  That instance is in this array at
        # location given by the **natural ordering**, which
        # is the mixed radix number b2%w2; b1%w1.
        self.runtimeInstances = []

        # logical execution times for each instance
        self.let = []
        #    deadline: Inferred deadline. Defaults to the maximum long value.
        self.deadline = TimeValue(TimeValue.MAX_LONG_DEADLINE, TimeUnit.NANO)

        #    index: Index of order of occurrence within the reactor definition.
        #      * The first reaction has index 0, the second index 1, etc.
        self.index = index
        #     isUnordered: Whether or not this reaction is ordered with respect to other
        #      * reactions in the same reactor.
        self.isUnordered = isUnordered
        #     reads: The ports that this reaction reads but that do not trigger it.
        self.reads = []

        #      triggers: The trigger instances (input ports, timers, and actions
        #      * that trigger reactions) that trigger this reaction.
        self.triggers = []
        #  If the reaction body starts with the magic string
        #  UNORDERED_REACTION_MARKER, then mark it unordered,
        #  overriding the argument.
        body = f"{definition.getCode()}"
        if body.find(self.UNORDERED_REACTION_MARKER) > -1:
            self.isUnordered = True
        #  Identify the dependencies for this reaction.
        #  First handle the triggers.
        for trigger in definition.getTriggers():
            if isinstance(trigger, VarRef):
                variable = trigger.getVariable()
                if isinstance(variable, Port):
                    portInstance = parent.lookupPortInstance(variable)
                    #  If the trigger is the port of a contained bank, then the
                    #  portInstance will be null and we have to instead search for
                    #  each port instance in the bank.
                    if portInstance is not None:
                        self.sources.append(portInstance)
                        portInstance.dependentReactions.append(self)
                        self.triggers.append(portInstance)
                    elif trigger.getContainer() is not None:
                        #  Port belongs to a contained reactor or bank.
                        containedReactor = parent.lookupReactorInstance(trigger.getContainer())
                        if containedReactor is not None:
                            portInstance = containedReactor.lookupPortInstance(variable)
                            if portInstance is not None:
                                self.sources.append(portInstance)
                                portInstance.dependentReactions.append(self)
                                self.triggers.append(portInstance)
                elif isinstance(variable, Action):
                    actionInstance = parent.lookupActionInstance(trigger.getVariable())
                    self.triggers.append(actionInstance)
                    actionInstance.dependentReactions.append(self)
                    self.sources.append(actionInstance)
                elif isinstance(variable, Timer):
                    timerInstance = parent.lookupTimerInstance(trigger.getVariable())
                    self.triggers.append(timerInstance)
                    timerInstance.dependentReactions.append(self)
                    self.sources.append(timerInstance)
            elif isinstance(trigger, BuiltinTriggerRef):
                self.triggers.append(parent.getOrCreateBuiltinTrigger(trigger))
        #  Next handle the ports that this reaction reads.
        for source in definition.getSources():
            variable = source.getVariable()
            if isinstance(variable, Port):
                portInstance = parent.lookupPortInstance(variable)
                #  If the trigger is the port of a contained bank, then the
                #  portInstance will be null and we have to instead search for
                #  each port instance in the bank.
                if portInstance is not None:
                    self.sources.append(portInstance)
                    self.reads.append(portInstance)
                    portInstance.dependentReactions.append(self)
                elif source.getContainer() is not None:
                    containedReactor = parent.lookupReactorInstance(source.getContainer())
                    if containedReactor is not None:
                        portInstance = containedReactor.lookupPortInstance(variable)
                        if portInstance is not None:
                            self.sources.append(portInstance)
                            portInstance.dependentReactions.append(self)
                            self.triggers.append(portInstance)
        #  Finally, handle the effects.
        for effect in definition.getEffects():
            variable = effect.getVariable()
            if isinstance(variable, Port):
                portInstance = parent.lookupPortInstance(effect)
                if portInstance is not None:
                    self.effects.append(portInstance)
                    portInstance.dependsOnReactions.append(self)
                else:
                    raise InvalidSourceException("Unexpected effect. Cannot find port " +
                                                 variable.__name__)
            elif isinstance(variable, Action):
                #  Effect is an Action.
                actionInstance = parent.lookupActionInstance(variable)
                self.effects.append(actionInstance)
                actionInstance.dependsOnReactions.append(self)
            else:
                pass
            #  Effect is either a mode or an unresolved reference.
            #  Do nothing, transitions will be set up by the ModeInstance.
        #  Create a deadline instance if one has been defined.
        if self.definition.getDeadline() is not None:
            self.declaredDeadline = DeadlineInstance(self.definition.getDeadline(), self)

    def clearCaches(self, includingRuntimes):
        """
        Clear caches used in reporting dependentReactions() and dependsOnReactions()
        This method should be called if any changes are made to triggers, sources,
        or effects.

        :param includingRuntimes: If false, leave the runtime instances intact.
                 This is useful for federated execution where levels are computed using
                 the top-level connections, but then those connections are discarded.
        :return:
        """
        self.dependentReactionsCache = []
        self.dependsOnReactionsCache = []
        if includingRuntimes:
            self.runtimeInstances = []

    def dependentReactions(self):
        """
        Return the set of immediate downstream reactions, which are reactions
        that receive data produced by this reaction plus
        at most one reaction in the same reactor whose definition
        lexically follows this one (unless this reaction is unordered).
        :return:
        """
        #  Cache the result.
        if len(self.dependentReactionsCache): #  is not None:
            return self.dependentReactionsCache
        self.dependentReactionsCache = []
        #  First, add the next lexical reaction, if appropriate.
        if not self.isUnordered and len(self.parent.reactions) > self.index + 1:
            #  Find the next reaction in the parent's reaction list.
            self.dependentReactionsCache.append(self.parent.reactions.get(self.index + 1))
        #  Next, add reactions that get data from this one via a port.
        for effect in self.effects:
            if isinstance(effect, PortInstance):
                for senderRange in effect.eventualDestinations():
                    for destinationRange in senderRange.destinations:
                        self.dependentReactionsCache.extend(destinationRange.instance.dependentReactions)
        return self.dependentReactionsCache

    def dependsOnReactions(self):
        """
        Return the set of immediate upstream reactions, which are reactions
        that send data to this one plus at most one reaction in the same
        reactor whose definition immediately precedes the definition of this one
        (unless this reaction is unordered).
        :return:
        """
        if len(self.dependsOnReactionsCache) > 0:
            return self.dependsOnReactionsCache
        self.dependsOnReactionsCache = []
        #  First, add the previous lexical reaction, if appropriate.
        if not self.isUnordered and self.index > 0:
            #  Find the previous ordered reaction in the parent's reaction list.
            earlierIndex = self.index - 1
            earlierOrderedReaction = self.parent.reactions.get(earlierIndex)
            earlierIndex -= 1
            while earlierOrderedReaction.isUnordered and earlierIndex >= 0:
                earlierOrderedReaction = self.parent.reactions.get(earlierIndex)
                earlierIndex -= 1
            if earlierIndex >= 0:
                self.dependsOnReactionsCache.append(self.parent.reactions.get(self.index - 1))
        #  Next, add reactions that send data to this one.
        for source in self.sources:
            if isinstance(source, PortInstance):
                #  First, add reactions that send data through an intermediate port.
                for senderRange in source.eventualSources():
                    self.dependsOnReactionsCache.extend(senderRange.instance.dependsOnReactions)
                #  Then, add reactions that send directly to this port.
                self.dependsOnReactionsCache.extend(source.dependsOnReactions)
        return self.dependsOnReactionsCache

    def getLevels(self):
        """
        Return a set of levels that runtime instances of this reaction have.
        A ReactionInstance may have more than one level if it lies within
        a bank and its dependencies on other reactions pass through multiports.
        :return:
        """
        result = []
        #  Force calculation of levels if it has not been done.
        self.parent.assignLevels()
        for runtime in self.runtimeInstances:
            result.append(runtime.level)
        return result

    def getLevelsList(self):
        """
        Return a list of levels that runtime instances of this reaction have.
        The size of this list is the total number of runtime instances.
        A ReactionInstance may have more than one level if it lies within
        a bank and its dependencies on other reactions pass through multiports.
        :return:
        """
        result = []
        #  Force calculation of levels if it has not been done.
        self.parent.assignLevels()
        for runtime in self.runtimeInstances:
            result.append(runtime.level)
        return result

    def getName(self):
        """
        Return the name of this reaction, which is 'reaction_n',
        where n is replaced by the reaction index.
        @return The name of this reaction.
        :return:
        """
        return "reaction_" + self.index

    def getRuntimeInstances(self):
        """
        Return an array of runtime instances of this reaction in a
        **natural order**, defined as follows.  The position within the
        returned list of the runtime instance is given by a mixed-radix
        number where the low-order digit is the bank index within the
        container reactor (or 0 if it is not a bank), the second low order
        digit is the bank index of the container's container (or 0 if
        it is not a bank), etc., until the container that is directly
        contained by the top level (the top-level reactor need not be
        included because its index is always 0).

        The size of the returned array is the product of the widths of all of the
        container ReactorInstance objects. If none of these is a bank,
        then the size will be 1.

        This method creates this array the first time it is called, but then
        holds on to it.  The array is used by {@link ReactionInstanceGraph}
        to determine and record levels and deadline for runtime instances
        of reactors.
        :return:
        """
        if len(self.runtimeInstances) > 0:
            return self.runtimeInstances
        size = self.parent.getTotalWidth()
        #  If the width cannot be determined, assume there is only one instance.
        if size < 0:
            size = 1
        self.runtimeInstances = []
        i = 0
        while i < size:
            r = Runtime(self)
            r.id = i
            if self.declaredDeadline is not None:
                r.deadline = self.declaredDeadline.maxDelay
            self.runtimeInstances.append(r)
            i += 1
        return self.runtimeInstances

    def removePortInstance(self, portInstance):
        """
        Purge 'portInstance' from this reaction, removing it from the list
        of triggers, sources, effects, and reads.  Note that this leaves
        the runtime instances intact, including their level information.
        :param portInstance:
        :return:
        """
        self.triggers.remove(portInstance)
        self.sources.remove(portInstance)
        self.effects.remove(portInstance)
        self.reads.remove(portInstance)
        self.clearCaches(False)
        portInstance.clearCaches()

    def __str__(self):
        """ Return a descriptive string. """
        return self.__name__ + " of " + self.parent.getFullName()

    @property
    def assignLogicalExecutionTime(self):
        """
        Determine logical execution time for each reaction during compile
        time based on immediate downstream logical delays (after delays and actions)
        and label each reaction with the minimum of all such delays.
        :return:
        """
        if len(self.let) > 0:
            return self.let
        if self.parent.isGeneratedDelay():
            self.let = TimeValue.ZERO
            return self.let
        let = None
        #  Iterate over effect and find minimum delay.
        for effect in self.effects:
            if isinstance(effect, PortInstance):
                child_stream = self.parent.getParent().children.stream()

                for c in child_stream:
                    t = False
                    afters: PortInstance = None
                    if c.isGeneratedDelay():
                        if afters == effect:
                            afters = c.inputs.get(0).getDependsOnPorts().get(0).instance
                            t = True
                    # afters.actions.get(0).getMinDelay()
                    if t:
                        if let is None:
                            let = afters.get()
                        else:
                            let = TimeValue.min(afters.get(), let)
            elif isinstance(effect, ActionInstance):
                action = effect.getMinDelay()
                if let is None:
                    let = action
                else:
                    let = TimeValue.min(action, let)
        if let is None:
            let = TimeValue.ZERO
        self.let = let
        return self.let


# /////////////////////////////////////////////////////////
# Inner classes
class Runtime:
    """ Inner class representing a runtime instance.  """
    def __init__(self, parent):
        self.parent = parent
        #  ID ranging from 0 to parent.getTotalWidth() - 1.
        self.id = 0
        self.level = 0
        self.deadline = TimeValue.MAX_VALUE
        self.dominating = None

    def getReaction(self):
        """ generated source for method getReaction """
        return self.parent  # ReactionInstance.self

    def __str__(self):
        """ generated source for method toString """
        result = self.parent + "(level: " + self.level
        if self.deadline is not None and self.deadline != TimeValue.MAX_VALUE:
            result += ", deadline: " + self.deadline
        if self.dominating is not None:
            result += ", dominating: " + self.dominating.getReaction()
        result += ")"
        return result
