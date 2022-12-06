#!/usr/bin/env python
""" generated source for module AttributeUtils """
# 
# Copyright (c) 2022, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
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
# package: org.lflang
# import java.util.List
# import org.eclipse.emf.ecore.EObject
from include.SpecialExceptions import IllegalArgumentException
from include.overloading import overloaded
from lflang.ASTUtils import ASTUtils
from lflang.lf.Action import Action
from lflang.lf.Input import Input
from lflang.lf.Output import Output
from lflang.lf.Parameter import Parameter
from lflang.lf.Reaction import Reaction
from lflang.lf.Reactor import Reactor
from lflang.lf.StateVar import StateVar
from lflang.lf.Timer import Timer
# from org.lflang.lf


#  * A helper class for processing attributes in the AST.
#  * 
#  * @author{Shaokai Lin <shaokai@berkeley.edu>}
#  * @author{Clément Fournier, TU Dresden, INSA Rennes}
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class AttributeUtils(object):
    """ generated source for class AttributeUtils """
    #      * Return the attributes declared on the given node. Throws
    #      * if the node does not support declaring attributes.
    #      *
    #      * @throws IllegalArgumentException If the node cannot have attributes
    #      
    @classmethod
    def getAttributes(cls, node):
        """ generated source for method getAttributes """
        if isinstance(node, Reactor):
            return node.getAttributes()
        elif isinstance(node, Reaction):
            return node.getAttributes()
        elif isinstance(node, Action):
            return node.getAttributes()
        elif isinstance(node, Timer):
            return node.getAttributes()
        elif isinstance(node, StateVar):
            return node.getAttributes()
        elif isinstance(node, Parameter):
            return node.getAttributes()
        elif isinstance(node, Input):
            return node.getAttributes()
        elif isinstance(node, Output):
            return node.getAttributes()
        raise IllegalArgumentException("Not annotatable: " + node)

    #      * Return the value of the attribute with the given name
    #      * if present, otherwise return null.
    #      *
    #      * @throws IllegalArgumentException If the node cannot have attributes
    #      
    @classmethod
    def findAttributeByName(cls, node, name):
        """ generated source for method findAttributeByName """
        r = ''
        attrs = cls.getAttributes(node)
        for it in attrs:
            if it.getAttrName().lower() == name.lower():
                s = it.getAttrParms().get(0).getValue().getStr()
                if len(s) > 0:
                    r = s[0]

        #          return attrs.stream()
        #  .filter(it -> it.getAttrName().lower() == name.lower())
        #  // case-insensitive search (more user-friendly)
        #  .map(it -> it.getAttrParms().get(0).getValue().getStr())
        #  .findFirst()
        #  .orElse(null);
        return r

    # Return the value of the {@code @label} attribute if
    # present, otherwise return null.
    #
    # @throws IllegalArgumentException If the node cannot have attributes
    #      
    @classmethod
    def findLabelAttribute(cls, node):
        """ generated source for method findLabelAttribute """
        return cls.findAttributeByName(node, "label")

    # Return true if the specified node is an Input and has an {@code @sparse}
    # attribute.
    # @param node An AST node.
    #      
    @classmethod
    def isSparse(cls, node):
        """ generated source for method isSparse """
        if isinstance(node, Input):
            for attribute in cls.getAttributes(node):
                if attribute.getAttrName().lower() == "sparse".lower():
                    return True
        return False

    # Return the declared label of the node, as given by the @label
    # annotation (or an @label comment).
    #
    # @throws IllegalArgumentException If the node cannot have attributes
    #
    @classmethod
    @overloaded
    def label(cls, n):
        """ generated source for method label """
        fromAttr = cls.findLabelAttribute(n)
        if fromAttr is None:
            return ASTUtils.findAnnotationInComments(n, "@label")
        return fromAttr

    # Search for an `@label` annotation for a given reaction.
    #
    # @param n the reaction for which the label should be searched
    # @return The annotated string if an `@label` annotation was found. `null` otherwise.
    #      
    @classmethod
    @label.register(object, Reaction)
    def label_0(cls, n):
        """ generated source for method label_0 """
        return cls.label(n)
