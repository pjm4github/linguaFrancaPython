#!/usr/bin/env python
""" generated source for module PythonParameterGenerator """
# package: org.lflang.generator.python
# import java.util.ArrayList
# import java.util.LinkedList
# import java.util.List
# import java.util.stream.Collectors
# import com.google.common.base.Objects
from lflang.generator.python import PyUtil
from include.overloading import overloaded
from org.lflang import ASTUtils

from org.lflang.generator import GeneratorBase

from org.lflang.generator import ParameterInstance

from org.lflang.lf import Expression

from org.lflang.lf import ParameterReference

from org.lflang.lf import ReactorDecl

from org.lflang.lf import Assignment

from org.lflang.lf import Parameter

class PythonParameterGenerator(object):
    """ generated source for class PythonParameterGenerator """
    #      * Generate Python code that instantiates and initializes parameters for a reactor 'decl'.
    #      *
    #      * @param decl The reactor declaration
    #      * @return The generated code as a StringBuilder
    #      
    @classmethod
    def generatePythonInstantiations(cls, decl, types):
        """ generated source for method generatePythonInstantiations """
        lines = []
        lines.append("# Define parameters and their default values")
        for param in getAllParameters(decl):
            if not types.getTargetType(param) == "PyObject*":
                #  If type is given, use it
                type = types.getPythonType(ASTUtils.getInferredType(param))
                lines.append("self._" + param.__name__ + ":" + type + " = " + generatePythonInitializer(param))
            else:
                #  If type is not given, just pass along the initialization
                lines.append("self._" + param.__name__ + " = " + generatePythonInitializer(param))
        #  Handle parameters that are set in instantiation
        lines.extend(["# Handle parameters that are set in instantiation", "self.__dict__.update(kwargs)", ""])
        return "\n".join([ lines])

    #      * Generate Python code getters for parameters of reactor 'decl'.
    #      *
    #      * @param decl The reactor declaration
    #      * @return The generated code as a StringBuilder
    #      
    @classmethod
    def generatePythonGetters(cls, decl):
        """ generated source for method generatePythonGetters """
        lines = []
        for param in getAllParameters(decl):
            if not param.__name__ == "bank_index":
                lines.extend(["", "@property", "def " + param.__name__ + "(self):", "    return self._" + param.__name__ + " # pylint: disable=no-member", ""])
        #  Create a special property for bank_index
        lines.extend(["", "@property", "def bank_index(self):", "    return self._bank_index # pylint: disable=no-member", ""])
        lines.append("\n")
        return "\n".join([ lines])

    #      * Return a list of all parameters of reactor 'decl'.
    #      *
    #      * @param decl The reactor declaration
    #      * @return The list of all parameters of 'decl'
    #      
    @classmethod
    def getAllParameters(cls, decl):
        """ generated source for method getAllParameters """
        return ASTUtils.allParameters(ASTUtils.toDefinition(decl))

    #      * Create a Python list for parameter initialization in target code.
    #      *
    #      * @param p The parameter to create initializers for
    #      * @return Initialization code
    #      
    @classmethod
    @overloaded
    def generatePythonInitializer(cls, p):
        """ generated source for method generatePythonInitializer """
        values = p.getInit().stream().map(PyUtil.getPythonTargetValue).collect(Collectors.toList())
        return "(" + ", ".join( values) + ")" if len(values) > 1 else values.get(0)

    @classmethod
    @generatePythonInitializer.register(object, ParameterInstance)
    def generatePythonInitializer_0(cls, p):
        """ generated source for method generatePythonInitializer_0 """
        lastAssignment = getLastAssignment(p)
        list = LinkedList()
        if lastAssignment != None:
            for expr in lastAssignment.getRhs():
                if isinstance(expr, (ParameterReference)):
                    param = (expr).getParameter()
                    list.append(PyUtil.reactorRef(p.getParent().getParent()) + "." + param.__name__)
                else:
                    list.append(GeneratorBase.getTargetTime(expr))
        else:
            for expr in p.getParent().initialParameterValue(p.getDefinition()):
                list.append(PyUtil.getPythonTargetValue(expr))
        return "(" + ", ".join( list) + ")" if len(list) > 1 else list.get(0)

    @classmethod
    def getLastAssignment(cls, p):
        """ generated source for method getLastAssignment """
        lastAssignment = None
        for assignment in p.getParent().getDefinition().getParameters():
            if Objects.equal(assignment.getLhs(), p.getDefinition()):
                lastAssignment = assignment
        return lastAssignment
