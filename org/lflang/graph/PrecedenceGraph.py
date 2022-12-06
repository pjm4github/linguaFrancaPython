#!/usr/bin/env python
""" generated source for module PrecedenceGraph """
# 
# Copyright (c) 2019, The University of California at Berkeley.
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
# package: org.lflang.graph
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Set
# import java.util.Stack
# import org.eclipse.xtext.xbase.lib.ListExtensions
# import java.util.ArrayList

#  
#  * Elaboration of `DirectedGraph` that is capable of identifying strongly
#  * connected components and topologically sorting its nodes.
#  * 
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#
from lflang.graph.DirectedGraph import DirectedGraph
from lflang.graph.NodeAnnotations import NodeAnnotations
from lflang.tests.TestRegistry import Stack


class PrecedenceGraph(DirectedGraph):

    def __init__(self):
        """
          Construct a new dependency graph.
        """

        super(PrecedenceGraph, self).__init__()
        # Annotations used during the execution of Tarjan's algorithm.
        self.annotations = NodeAnnotations()
        # Indicates whether the graph has been analyzed for cycles.
        # If this variable is false, Tarjan's algorithm needs to be run to find out
        # whether this graph has cycles.
        self.cycleAnalysisDone = False
        # Indicates whether the graph has been sorted.
        # If this variable is false, a new DFS has to be done to compute a
        # topological sort.
        self.isSorted = False
        # Index used in Tarjan's algorithm.
        self.index = 0
        # After analysis has completed, this list contains all nodes in reverse
        # topological order.
        self.sortedNodes = []
        # Stack used in Tarjan's algorithm.
        self.stack = Stack()
        # After analysis has completed, this list contains all sets of nodes
        # that are part of the same strongly connected component.
        self.cycles = []

    def graphChanged(self):
        """
        Invalidate cached analysis due to changes in the graph structure.
        :return:
        """
        self.cycleAnalysisDone = False
        self.isSorted = False

    def sortNodes(self):
        """
        Topologically sort the nodes in the graph.
        :return:
        """
        if not self.isSorted:
            #  Cleanup.
            self.sortedNodes = []
            for it in self.nodes():
                # this.nodes().forEach(
                #   it -> {
                self.annotations.get(it).hasTempMark = False
                self.annotations.get(it).hasPermMark = False
            for node in self.nodes():
                if not self.annotations.get(node).hasPermMark:
                    self.visit(node)
            self.isSorted = True

    def visit(self, node):
        """
        Recursively visit all nodes reachable from the given node; after all
        those nodes have been visited add the current node to a list which will
        be sorted in reverse order.
        :param node:
        :return:
        """
        annotation = self.annotations.get(node)
        if annotation.hasPermMark:
            return
        if annotation.hasTempMark:
            raise Exception("Cannot order nodes due to cycle in the graph.")
        annotation.hasTempMark = True
        for dep in self.getDownstreamAdjacentNodes(node):
            self.visit(dep)
        annotation.hasTempMark = False
        annotation.hasPermMark = True
        self.sortedNodes.append(node)

    def detectCycles(self):
        """
        Run Tarjan's algorithm for finding strongly connected components.
        After invoking this method, the detected cycles with be listed
        in the class variable `cycles`.
        :return:
        """
        if not self.cycleAnalysisDone:
            self.index = 0
            self.stack = Stack()
            self.cycles = []
            for it in self.nodes():
                self.annotations.get(it).index = -1
            for node in self.nodes():
                if self.annotations.get(node).index == -1:
                    self.strongConnect(node)
            self.cycleAnalysisDone = True
            self.stack = None

    def hasCycles(self):
        """
        Report whether this graph has any cycles in it.
        :return:
        """
        self.detectCycles()
        return len(self.cycles) > 0

    def getCycles(self):
        """
        Return a list of strongly connected components that exist in this graph.
        :return:
        """
        self.detectCycles()
        return self.cycles

    def strongConnect(self, node):
        """
        Traverse the graph to visit unvisited dependencies and determine
        whether they are part of a cycle.
        :param node:
        :return:
        """
        annotation = self.annotations.get(node)
        annotation.index = self.index
        annotation.lowLink = self.index
        annotation.onStack = True
        self.index += 1
        self.stack.push(node)
        for dep in self.getUpstreamAdjacentNodes(node):
            depAnnotation = self.annotations.get(dep)
            if depAnnotation.onStack:
                annotation.lowLink = min(annotation.lowLink, depAnnotation.index)
                if node == dep:
                    annotation.selfLoop = True
            elif depAnnotation.index == -1:
                self.strongConnect(dep)
                annotation.lowLink = min(annotation.lowLink, depAnnotation.lowLink)
        if annotation.lowLink == annotation.index:
            scc = []
            while True:
                dep = self.stack.pop()
                self.annotations.get(dep).onStack = False
                scc.append(dep)
                if node == dep:
                    break
            if len(scc) > 1 or annotation.selfLoop:
                self.cycles.append(scc)

    def nodesInReverseTopologicalOrder(self):
        """
        Return the nodes of this graph in reverse topological order. Each node
        in the returned list is succeeded by the nodes that it depends on
        :return:
        """

        self.sortNodes()
        return self.sortedNodes

    def nodesInTopologicalOrder(self):
        """
        Return the nodes of this graph in reverse topological order. Each node
        in the returned list is preceded by the nodes that it depends on.
        :return:
        """

        self.sortNodes()
        return self.sortedNodes.reverse()
