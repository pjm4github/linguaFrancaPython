#!/usr/bin/env python
""" generated source for module ParameterInstance """
#  A data structure for a parameter instance. 
# 
# Copyright (c) 2019, The University of California at Berkeley.
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
# package: org.lflang.generator
# import java.util.List
# import java.util.Optional

from org.lflang.InferredType

from org.lflang.ASTUtils

from org.lflang.lf import Assignment

from org.lflang.lf import Expression

from org.lflang.lf import Parameter

#  
#  * Representation of a compile-time instance of a parameter.
#  * Upon creation, it is checked whether this parameter is overridden by an 
#  * assignment in the instantiation that this parameter instance is a result of.
#  * If it is overridden, the parameter gets initialized using the value looked up
#  * in the instantiation hierarchy.
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class ParameterInstance(NamedInstance):
    """ generated source for class ParameterInstance """
    #  
    #      * Create a runtime instance from the specified definition
    #      * and with the specified parent that instantiated it.
    #      * @param definition The declaration in the AST.
    #      * @param parent The reactor instance this parameter is a part of.
    #      
    def __init__(self, definition, parent):
        """ generated source for method __init__ """
        super(ParameterInstance, self).__init__(parent)
        if parent == None:
            raise InvalidSourceException("Cannot create a ParameterInstance with no parent.")
        self.type = ASTUtils.getInferredType(definition)

    # ///////////////////////////////////////////
    # // Public Fields
    type = None

    # ///////////////////////////////////////////
    # // Public Methods
    #      * Get the initial value(s) of this parameter as a list of
    #      * Value objects, where each Value is either an instance
    #      * of Time, Literal, or Code. That is, references to other
    #      * parameters have been replaced with their initial values.
    #      
    def getInitialValue(self):
        """ generated source for method getInitialValue """
        return parent.initialParameterValue(self.definition)

    #      * Return the name of this parameter. 
    #      * @return The name of this parameter.
    #      
    def getName(self):
        """ generated source for method getName """
        return self.definition.__name__

    #      * Return the assignment that overrides this parameter in
    #      * the parent's instantiation or null if there is no override.
    #      
    def getOverride(self):
        """ generated source for method getOverride """
        assignments = parent.definition.getParameters()
        #          Optional assignment = assignments.stream().filter(
        #              it -> it.getLhs() == definition
        #          ).findFirst();
        return assignment.orElse(None)

    #  Return a descriptive string. 
    def __str__(self):
        """ generated source for method toString """
        return "ParameterInstance " + getFullName()
