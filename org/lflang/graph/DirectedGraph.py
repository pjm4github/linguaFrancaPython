#!/usr/bin/env python
""" generated source for module DirectedGraph """
# 
#  Copyright (c) 2019, The University of California at Berkeley.
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.graph
# import java.util
# import java.util.Map.Entry
# import java.util.stream.Collectors

from org.lflang.util.CollectionUtil

# 
#  * Directed graph that maps nodes to its upstream and downstream neighbors.
#  *
#  * @author Marten Lohstroh {@literal <marten@berkeley.edu>}
#  * @author Clément Fournier {@literal <clement.fournier@mailbox.tu-dresden.de>}
#  
class DirectedGraph(Graph):
    """ generated source for class DirectedGraph """
    #  Note that while both those maps are mutable, the sets
    #  they use as values may not be. They should only be
    #  manipulated through CollectionUtil
    #  If a node has no neighbors, it is still in the map with an empty set as a value.
    #      * Adjacency map from vertices to their downstream immediate neighbors.
    #      
    downstreamAdjacentNodes = {}

    #      * Adjacency map from vertices to their upstream immediate neighbors.
    #      
    upstreamAdjacentNodes = {}

    #      * Mark the graph to have changed so that any cached analysis is refreshed
    #      * accordingly.
    #      
    def graphChanged(self):
        """ generated source for method graphChanged """
        #  To be overridden by subclasses that perform analysis.

    #      * Return true if this graph has the given node in it.
    #      *
    #      * @param node The node to look for.
    #      
    def hasNode(self, node):
        """ generated source for method hasNode """
        return nodes().contains(node)

    #      * Return all immediate upstream neighbors of a given node.
    #      *
    #      * @param node The node to report the immediate upstream neighbors of.
    #      
    def getUpstreamAdjacentNodes(self, node):
        """ generated source for method getUpstreamAdjacentNodes """
        return Collections.unmodifiableSet(self.upstreamAdjacentNodes.getOrDefault(node, Set.of()))

    #      * Return all immediate downstream neighbors of a given node.
    #      *
    #      * @param node The node to report the immediate downstream neighbors of.
    #      
    def getDownstreamAdjacentNodes(self, node):
        """ generated source for method getDownstreamAdjacentNodes """
        return Collections.unmodifiableSet(self.downstreamAdjacentNodes.getOrDefault(node, Set.of()))

    def addNode(self, node):
        """ generated source for method addNode """
        self.graphChanged()
        self.upstreamAdjacentNodes.putIfAbsent(node, Set.of())
        self.downstreamAdjacentNodes.putIfAbsent(node, Set.of())

    def removeNode(self, node):
        """ generated source for method removeNode """
        self.graphChanged()
        self.upstreamAdjacentNodes.remove(node)
        self.downstreamAdjacentNodes.remove(node)
        #  The node also needs to be removed from the sets that represent connections to the node.
        CollectionUtil.removeFromValues(self.upstreamAdjacentNodes, node)
        CollectionUtil.removeFromValues(self.downstreamAdjacentNodes, node)

    #      * Add a new directed edge to the graph. The first argument is
    #      * the downstream node, the second argument the upstream node.
    #      * If either argument is null, do nothing.
    #      *
    #      * @param sink   The downstream immediate neighbor.
    #      * @param source The upstream immediate neighbor.
    #      
    def addEdge(self, sink, source):
        """ generated source for method addEdge """
        self.graphChanged()
        if sink != None and source != None:
            #             this.downstreamAdjacentNodes.compute(source, (k, set) -> CollectionUtil.plus(set, sink));
            #             this.upstreamAdjacentNodes.compute(sink, (k, set) -> CollectionUtil.plus(set, source));

    #      * Add new directed edges to the graph. The first argument is the
    #      * downstream node, the second argument a set of upstream nodes.
    #      *
    #      * @param sink    The downstream immediate neighbor.
    #      * @param sources The upstream immediate neighbors.
    #      
    def addEdges(self, sink, sources):
        """ generated source for method addEdges """
        for source in sources:
            self.addEdge(sink, source)

    #      * Remove a directed edge from the graph.
    #      *
    #      * @param sink   The downstream immediate neighbor.
    #      * @param source The upstream immediate neighbor.
    #      
    def removeEdge(self, sink, source):
        """ generated source for method removeEdge """
        self.graphChanged()
        #         this.upstreamAdjacentNodes.computeIfPresent(sink, (k, upstream) -> CollectionUtil.minus(upstream, source));
        #         this.downstreamAdjacentNodes.computeIfPresent(source, (k, downstream) -> CollectionUtil.minus(downstream, sink));

    #      * Obtain a copy of this graph by creating an new instance and copying
    #      * the adjacency maps.
    #      
    def copy(self):
        """ generated source for method copy """
        graph = DirectedGraph()
        for entry in self.upstreamAdjacentNodes.entrySet():
            graph.upstreamAdjacentNodes.put(entry.getKey(), CollectionUtil.copy(entry.getValue()))
        for entry in self.downstreamAdjacentNodes.entrySet():
            graph.downstreamAdjacentNodes.put(entry.getKey(), CollectionUtil.copy(entry.getValue()))
        return graph

    #      * For a given a two adjacency maps, copy missing edges from the first
    #      * map to the second.
    #      *
    #      * @param srcMap The adjacency map to copy edges from.
    #      * @param dstMap The adjacency map to copy edges to.
    #      
    def mirror(self, srcMap, dstMap):
        """ generated source for method mirror """
        if srcMap != None and dstMap != None:
            for entry in srcMap.entrySet():
                node = entry.getKey()
                srcEdges = entry.getValue()
                #                  dstMap.compute(node, (_node, dstEdges) -> {
                #                      // Node does not exist; add it.
                #                      if (dstEdges == null) {
                #                          return CollectionUtil.copy(srcEdges);
                #                      }
                            #                      // Node does exist; add the missing edges.
                #                      var set = dstEdges;
                #                      for (T edge : srcEdges) {
                #                          set = CollectionUtil.plus(set, edge);
                #                      }
                #                      return set;
                #                  });

    #      * Merge another directed graph into this one.
    #      *
    #      * @param another The graph to merge into this one.
    #      
    def merge(self, another):
        """ generated source for method merge """
        self.graphChanged()
        self.mirror(another.upstreamAdjacentNodes, self.upstreamAdjacentNodes)
        self.mirror(another.downstreamAdjacentNodes, self.downstreamAdjacentNodes)

    #      * Return the set of nodes that have no neighbors listed in the given
    #      * adjacency map.
    #      
    def independentNodes(self, adjacencyMap):
        """ generated source for method independentNodes """
        independent = {}
        for node in nodes():
            neighbors = adjacencyMap.get(node)
            if neighbors == None or len(neighbors) == 0:
                independent.append(node)
        return independent

    #      * Return the root nodes of this graph.
    #      * Root nodes have no upstream neighbors.
    #      
    def rootNodes(self):
        """ generated source for method rootNodes """
        return self.independentNodes(self.upstreamAdjacentNodes)

    #      * Return the leaf nodes of this graph.
    #      * Leaf nodes have no downstream neighbors.
    #      
    def leafNodes(self):
        """ generated source for method leafNodes """
        return self.independentNodes(self.downstreamAdjacentNodes)

    def nodeCount(self):
        """ generated source for method nodeCount """
        return len(self.downstreamAdjacentNodes)

    def edgeCount(self):
        """ generated source for method edgeCount """
        return self.upstreamAdjacentNodes.values().stream().mapToInt(Set.size).sum()

    def nodes(self):
        """ generated source for method nodes """
        return Collections.unmodifiableSet(self.downstreamAdjacentNodes.keySet())

    def clear(self):
        """ generated source for method clear """
        self.graphChanged()
        self.downstreamAdjacentNodes = []
        self.upstreamAdjacentNodes = []

    def __str__(self):
        """ generated source for method toString """
        return self.nodes().stream().map(Objects.toString).collect(Collectors.joining(", ", "{", "}"))
