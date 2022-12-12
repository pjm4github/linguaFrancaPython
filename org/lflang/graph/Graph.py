#!/usr/bin/env python
""" generated source for module Graph """
from abc import ABCMeta, abstractmethod
# 
#  Copyright (c) 2020, The University of California at Berkeley.
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.graph
# import java.util.List
# import java.util.Set

# 
#  * Root interface for graph implementations.
#  *
#  * @param <T> Type of vertices of the graph
#  
class Graph:
    """ generated source for interface Graph """
    __metaclass__ = ABCMeta
    #      * Return an unmodifiable set of nodes in this graph.
    #      
    @abstractmethod
    def nodes(self):
        """ generated source for method nodes """

    @abstractmethod
    def hasNode(self, node):
        """ generated source for method hasNode """

    #  Add the given node to the graph. 
    @abstractmethod
    def addNode(self, node):
        """ generated source for method addNode """

    #      * Remove the given node from the graph. This also eliminates any
    #      * edges from upstream and to downstream neighbors of this node.
    #      *
    #      * @param node The node to remove.
    #      
    @abstractmethod
    def removeNode(self, node):
        """ generated source for method removeNode """

    #  todo order of parameters here is unintuitive... from -> to is more usual
    @abstractmethod
    def addEdge(self, to, from_):
        """ generated source for method addEdge """

    @abstractmethod
    def addEdges(self, to, from_):
        """ generated source for method addEdges """

    @abstractmethod
    def removeEdge(self, to, from_):
        """ generated source for method removeEdge """

    #      * Return the number of nodes in this graph.
    #      
    @abstractmethod
    def nodeCount(self):
        """ generated source for method nodeCount """

    #  Return the number of directed edges in this graph. 
    @abstractmethod
    def edgeCount(self):
        """ generated source for method edgeCount """
