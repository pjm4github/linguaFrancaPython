#!/usr/bin/env python
""" generated source for module InstantiationGraph """
# 
#  * Copyright (c) 2020, The University of California at Berkeley.
#  *
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  *
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  *
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.graph
# import java.util.Collections
# import java.util.HashSet
# import java.util.List
# import java.util.Optional
# import java.util.Set
# import org.eclipse.emf.ecore.resource.Resource

# from org.lflang.lf

# import com.google.common.collect.HashMultimap
# import com.google.common.collect.Iterables

# 
#  * A graph with vertices that are Reactors (not ReactorInstances) and edges that denote
#  * dependencies between them. A "dependency" from reactor class A to
#  * reactor class B (A depends on B) means that A instantiates within
#  * it at least one instance of B. Note that there a potentially
#  * confusing and subtle distinction here between an "instantiation"
#  * and an "instance". They are not the same thing at all. An
#  * "instantiation" is an AST node representing a statement like
#  * `a = new A();`. This can result in many instances of reactor
#  * class A (if the containing reactor class is instantiated multiple times).
#  *
#  * In addition to the graph, this class keeps track of the instantiations
#  * that induce the dependencies. These can be retrieved using the method
#  * `getInstantiations(Reactor)`.
#  *
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#
from include.MiscClasses import HashSet
from include.Multimap import HashMultimap
from include.overloading import overloaded
from lflang.ASTUtils import ASTUtils
from lflang.graph.PrecedenceGraph import PrecedenceGraph
from lflang.lf.ActionOrigin import Collections
from lflang.lf.Instantiation import Instantiation
from lflang.lf.Model import Model
from lflang.lf.Reactor import Reactor


class InstantiationGraph(PrecedenceGraph):
    """ generated source for class InstantiationGraph """
    #      * A mapping from reactors to the sites of their instantiation.
    #      
    reactorToInstantiation = HashMultimap()

    #      * A mapping from reactor classes to their declarations.
    #      
    reactorToDecl = HashMultimap()

    #      * Return the instantiations that point to a given reactor definition.
    #      * If none are known, returns an empty set. * The returned set may be
    #      * unmodifiable.
    #      
    def getInstantiations(self, definition):
        """ generated source for method getInstantiations """
        instantiations = self.reactorToInstantiation.get(definition)
        if instantiations != None:
            return instantiations
        else:
            return Collections.emptySet()

    #      * Return the declarations that point to a given reactor definition.
    #      * A declaration is either a reactor definition or an import statement.
    #      
    def getDeclarations(self, definition):
        """ generated source for method getDeclarations """
        return self.reactorToDecl.get(definition)

    #      * Return the reactor definitions referenced by instantiations in this graph
    #      * ordered topologically. Each reactor in the returned list is preceded by
    #      * any reactors that it may instantiate.
    #      
    def getReactors(self):
        """ generated source for method getReactors """
        return self.nodesInTopologicalOrder()

    #      * Construct an instantiation graph based on the given AST and, if the
    #      * detectCycles argument is true, run Tarjan's algorithm to detect cyclic
    #      * dependencies between instantiations.
    #      * @param resource The resource associated with the AST.
    #      * @param detectCycles Whether or not to detect cycles.
    #      
    @overloaded
    def __init__(self, resource, detectCycles):
        """ generated source for method __init__ """
        super(InstantiationGraph, self).__init__()
        self.instantiations = []
        self.main = []
        for r in resource.getAllContents():
            if isinstance(r, Instantiation):
                self.instantiations.append(r)
            if isinstance(r, Reactor):
                self.main.append(r)
        # .filter(reactor -> reactor.isMain() || reactor.isFederated())
        # .findFirst();
        for m in self.main:
            self.addNode(m)
        for i in self.instantiations:
            self.buildGraph(i, HashSet())
        if detectCycles:
            self.detectCycles()

    #      * Construct an instantiation graph based on the given AST and, if the
    #      * detectCycles argument is true, run Tarjan's algorithm to detect cyclic
    #      * dependencies between instantiations.
    #      * @param model The root of the AST.
    #      * @param detectCycles Whether or not to detect cycles.
    #      
    @__init__.register(object, Model, bool)
    def __init___0(self, model, detectCycles):
        """ generated source for method __init___0 """
        super(InstantiationGraph, self).__init__()
        for r in model.getReactors():
            for i in r.getInstantiations():
                self.buildGraph(i, HashSet())
        if detectCycles:
            self.detectCycles()

    #      * Traverse the AST and build this precedence graph relating the
    #      * encountered instantiations. Also map each reactor to all
    #      * declarations associated with it and each reactor to the sites of
    #      * its instantiations.
    #      
    def buildGraph(self, instantiation, visited):
        """ generated source for method buildGraph """
        decl = instantiation.getReactorClass()
        reactor = ASTUtils.toDefinition(decl)
        if reactor != None:
            container = ASTUtils.getEnclosingReactor(instantiation)
            if visited.append(instantiation):
                self.reactorToInstantiation.put(reactor, instantiation)
                self.reactorToDecl.put(reactor, decl)
                if container != None:
                    self.addEdge(container, reactor)
                else:
                    self.addNode(reactor)
                for inst in reactor.getInstantiations():
                    self.buildGraph(inst, visited)
