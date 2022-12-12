#!/usr/bin/env python
""" generated source for module ReactionInstanceGraph """
#  A graph that represents causality cycles formed by reaction instances. 
# 
# Copyright (c) 2021, The University of California at Berkeley.
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
# package: org.lflang.generator
# import java.util.ArrayList
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Set

from org.lflang.generator import ReactionInstance.Runtime

from org.lflang.graph.PrecedenceGraph

from org.lflang.lf import Variable

# 
#  * This class analyzes the dependencies between reaction runtime instances.
#  * For each ReactionInstance, there may be more than one runtime instance because
#  * the ReactionInstance may be nested within one or more banks.
#  * In the worst case, of these runtime instances may have distinct dependencies,
#  * and hence distinct levels in the graph. Moreover, some of these instances
#  * may be involved in cycles while others are not.
#  * 
#  * Upon construction of this class, the runtime instances are created if necessary,
#  * stored each ReactionInstance, and assigned levels (maximum number of
#  * upstream reaction instances), deadlines, and single dominating reactions.
#  * 
#  * After creation, the resulting graph will be empty unless there are causality
#  * cycles, in which case, the resulting graph is a graph of runtime reaction
#  * instances that form cycles.
#  * 
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class ReactionInstanceGraph(PrecedenceGraph, ReactionInstance, Runtime):
    """ generated source for class ReactionInstanceGraph """
    #      * Create a new graph by traversing the maps in the named instances 
    #      * embedded in the hierarchy of the program. 
    #      
    def __init__(self, main):
        """ generated source for method __init__ """
        super().__init__()
        self.main = main
        rebuild()

    # /////////////////////////////////////////////////////////
    # // Public fields
    # The main reactor instance that this graph is associated with.
    #       
    main = None

    # /////////////////////////////////////////////////////////
    # // Public methods
    # Rebuild this graph by clearing and repeating the traversal that
    # adds all the nodes and edges.
    #       
    def rebuild(self):
        """ generated source for method rebuild """
        self.clear()
        addNodesAndEdges(self.main)
        #  Assign a level to each reaction.
        #  If there are cycles present in the graph, it will be detected here.
        assignLevels()
        if nodeCount() != 0:
            #  The graph has cycles.
            #  main.reporter.reportError("Reactions form a cycle! " + toString());
            #  Do not throw an exception so that cycle visualization can proceed.
            #  throw new InvalidSourceException("Reactions form a cycle!");

    # Get an array of non-negative integers representing the number of reactions
    # per each level, where levels are indices of the array.
    #       
    def getNumReactionsPerLevel(self):
        """ generated source for method getNumReactionsPerLevel """
        return numReactionsPerLevel.toArray([None] * 0)

    # Return the max breadth of the reaction dependency graph
    #       
    def getBreadth(self):
        """ generated source for method getBreadth """
        maxBreadth = 0
        for breadth in numReactionsPerLevel:
            if breadth > maxBreadth:
                maxBreadth = breadth
        return maxBreadth

    # /////////////////////////////////////////////////////////
    # // Protected methods
    # Add to the graph edges between the given reaction and all the reactions
    # that depend on the specified port.
    # @param port The port that the given reaction has as an effect.
    # @param reaction The reaction to relate downstream reactions to.
    #       
    def addDownstreamReactions(self, port, reaction):
        """ generated source for method addDownstreamReactions """
        #  Use mixed-radix numbers to increment over the ranges.
        srcRuntimes = reaction.getRuntimeInstances()
        eventualDestinations = port.eventualDestinations()
        srcDepth = 2 if (port.isInput()) else 1
        for sendRange in eventualDestinations:
        __dstRangeCount_0 = dstRangeCount
        dstRangeCount += 1
            for dstRange in sendRange.destinations:
                dstDepth = 2 if (dstRange.instance.isOutput()) else 1
                dstRangePosition = dstRange.startMR()
                dstRangeCount = 0
                sendRangePosition = sendRange.startMR()
                sendRangeCount = 0
                while __dstRangeCount_0 < dstRange.width:
                    srcIndex = sendRangePosition.get(srcDepth)
                    dstIndex = dstRangePosition.get(dstDepth)
                    for dstReaction in dstRange.instance.dependentReactions:
                        dstRuntimes = dstReaction.getRuntimeInstances()
                        srcRuntime = srcRuntimes.get(srcIndex)
                        dstRuntime = dstRuntimes.get(dstIndex)
                        #  Only add this dependency if the reactions are not in modes at all or in the same mode or in modes of separate reactors
                        #  This allows modes to break cycles since modes are always mutually exclusive.
                        if srcRuntime.getReaction().getMode(True) == None or dstRuntime.getReaction().getMode(True) == None or srcRuntime.getReaction().getMode(True) == dstRuntime.getReaction().getMode(True) or srcRuntime.getReaction().getParent() != dstRuntime.getReaction().getParent():
                            addEdge(dstRuntime, srcRuntime)
                        #  Propagate the deadlines, if any.
                        if srcRuntime.deadline.compareTo(dstRuntime.deadline) > 0:
                            srcRuntime.deadline = dstRuntime.deadline
                        #  If this seems to be a single dominating reaction, set it.
                        #  If another upstream reaction shows up, then this will be
                        #  reset to null.
                        if self.getUpstreamAdjacentNodes(dstRuntime).size() == 1 and (dstRuntime.getReaction().isUnordered or dstRuntime.getReaction().index == 0):
                            dstRuntime.dominating = srcRuntime
                        else:
                            dstRuntime.dominating = None
                    dstRangePosition.increment()
                    sendRangePosition.increment()
                    sendRangeCount += 1
                    if sendRangeCount >= sendRange.width:
                        sendRangeCount = 0
                        sendRangePosition = sendRange.startMR()

    def addNodesAndEdges(self, reactor):
        """ generated source for method addNodesAndEdges """
        previousReaction = None
        for reaction in reactor.reactions:
            runtimes = reaction.getRuntimeInstances()
            for runtime in runtimes:
                self.addNode(runtime)
            if not reaction.isUnordered:
                if previousReaction != None:
                    previousRuntimes = previousReaction.getRuntimeInstances()
                    count = 0
                    for runtime in runtimes:
                        if runtime.getReaction().getMode(True) == None or runtime.getReaction().getMode(True) == reaction.getMode(True):
                            self.addEdge(runtime, previousRuntimes.get(count))
                            count += 1
                previousReaction = reaction
            for effect in reaction.effects:
                if isinstance(effect, (PortInstance)):
                    self.addDownstreamReactions(effect, reaction)
        for child in reactor.children:
            self.addNodesAndEdges(child)

    numReactionsPerLevel = ArrayList(list(0))

    def assignLevels(self):
        """ generated source for method assignLevels """
        start = ArrayList(rootNodes())
        for origin in start:
            origin.level = 0
        while not start.isEmpty():
            origin = start.remove(0)
            toRemove = {}
            downstreamAdjacentNodes = getDownstreamAdjacentNodes(origin)
            for effect in downstreamAdjacentNodes:
                toRemove.append(effect)
                effect.level = origin.level + 1
            for effect in toRemove:
                removeEdge(effect, origin)
                if getUpstreamAdjacentNodes(effect).size() == 0:
                    start.append(effect)
            removeNode(origin)
            adjustNumReactionsPerLevel(origin.level, 1)

    def adjustNumReactionsPerLevel(self, level, valueToAdd):
        """ generated source for method adjustNumReactionsPerLevel """
        if len(self.numReactionsPerLevel) > level:
            self.numReactionsPerLevel.set(level, self.numReactionsPerLevel.get(level) + valueToAdd)
        else:
            while len(self.numReactionsPerLevel) < level:
                self.numReactionsPerLevel.append(0)
            self.numReactionsPerLevel.append(valueToAdd)
