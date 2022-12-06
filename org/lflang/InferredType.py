#!/usr/bin/env python
""" generated source for module InferredType """
# 
# Copyright (c) 2020, The University of California at Berkeley.
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
# import java.util.function_.Function
# import org.eclipse.emf.ecore.EObject

from org.lflang.lf import Type

# 
#  * A helper class that represents an inferred type.
#  *
#  * <p>This class helps to separate the rules of type inference from code generation
#  * for types. It is particularly useful in cases when the type is not given directly
#  * in LF code, but is inferred from the context. In this case it could happen that
#  * no ASTNode representing the type does not exist. For instance when a
#  * parameter type is inferred from a time value. All in all, this class provides a
#  * clean interface between type inference in ASTUtils and code generation.
#  *
#  * <p>ASTUtils provides functionality to create an inferred type from
#  * Lingua Franca variables (getInferredType). This inferred type can than be
#  * translated to target code using the code generators or be converted to a general
#  * textual representation using toText().
#  *
#  * @author Christian Menard <christian.menard@tu-dresden.de>
#  
class InferredType(object):
    """ generated source for class InferredType """
    #      * The AST node representing the inferred type if such a node exists.
    #      
    astType = None

    #      * A flag indicating whether the inferred type has the base type time.
    #      
    isTime = bool()

    #      * A flag indicating whether the inferred type is a list.
    #      
    isList = bool()

    #      * A flag indicating whether the inferred type is a list of variable size.
    #      
    isVariableSizeList = bool()

    #      * A flag indicating whether the inferred type is a list of fixed size.
    #      
    isFixedSizeList = bool()

    #      * The list size if the inferred type is a fixed size list.
    #      * Otherwise, null.
    #      
    listSize = None

    #      * Private constructor
    #      
    def __init__(self, astType, isTime, isVariableSizeList, isFixedSizeList, listSize):
        """ generated source for method __init__ """
        self.astType = astType
        self.isTime = isTime
        self.isList = isVariableSizeList or isFixedSizeList
        self.isVariableSizeList = isVariableSizeList
        self.isFixedSizeList = isFixedSizeList
        self.listSize = listSize

    #      * Check if the inferred type is undefined.
    #      
    def isUndefined(self):
        """ generated source for method isUndefined """
        return self.astType == None and not self.isTime

    #      * Convert the inferred type to its textual representation as it would appear in LF code,
    #      * with CodeMap tags inserted.
    #      
    def toText(self):
        """ generated source for method toText """
        return toTextHelper(ASTUtils.toText)

    #      * Convert the inferred type to its textual representation as it would appear in LF code,
    #      * without CodeMap tags inserted.
    #      
    def toOriginalText(self):
        """ generated source for method toOriginalText """
        return toTextHelper(ASTUtils.toOriginalText)

    def toTextHelper(self, toText):
        """ generated source for method toTextHelper """
        if self.astType != None:
            return toText.apply(self.astType)
        elif self.isTime:
            if self.isFixedSizeList:
                return "time[" + self.listSize + "]"
            elif self.isVariableSizeList:
                return "time[]"
            else:
                return "time"
        return ""

    #      * Convert the inferred type to its textual representation while ignoring any list qualifiers.
    #      *
    #      * @return Textual representation of this inferred type without list qualifiers
    #      
    def baseType(self):
        """ generated source for method baseType """
        if self.astType != None:
            return ASTUtils.baseType(self.astType)
        elif self.isTime:
            return "time"
        return ""

    #      * Create an inferred type from an AST node.
    #      *
    #      * @param type an AST node
    #      * @return A new inferred type representing the given AST node
    #      
    @classmethod
    def fromAST(cls, type):
        """ generated source for method fromAST """
        if type == None:
            return undefined()
        return InferredType(type, type.isTime(), type.getArraySpec() != None and type.getArraySpec().isOfVariableLength(), type.getArraySpec() != None and not type.getArraySpec().isOfVariableLength(), type.getArraySpec().getLength() if type.getArraySpec() != None else None)

    #      * Create an undefined inferred type.
    #      
    @classmethod
    def undefined(cls):
        """ generated source for method undefined """
        return InferredType(None, False, False, False, None)

    #      * Create an inferred type representing time.
    #      
    @classmethod
    def time(cls):
        """ generated source for method time """
        return InferredType(None, True, False, False, None)

    #      * Create an inferred type representing a list of time values.
    #      *
    #      * <p>This creates a fixed size list if size is non-null,
    #      * otherwise a variable size list.
    #      *
    #      * @param size The list size, may be null
    #      
    @classmethod
    @overloaded
    def timeList(cls, size):
        """ generated source for method timeList """
        return InferredType(None, True, size == None, size != None, size)

    #      * Create an inferred type representing a variable size time list.
    #      
    @classmethod
    @timeList.register(object)
    def timeList_0(cls):
        """ generated source for method timeList_0 """
        return cls.timeList(None)
