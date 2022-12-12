#!/usr/bin/env python
""" generated source for module PythonStateGenerator """
# package: org.lflang.generator.python
# import java.util.ArrayList
# import java.util.List
# import java.util.stream.Collectors
from lflang.generator.python import PyUtil
from org.lflang import ASTUtils

from org.lflang.lf import ReactorDecl

from org.lflang.lf import StateVar

class PythonStateGenerator:
    """ generated source for class PythonStateGenerator """
    #      * Generate state variable instantiations for reactor "decl"
    #      * @param decl The reactor declaration to generate state variables.
    #      
    @classmethod
    def generatePythonInstantiations(cls, decl):
        """ generated source for method generatePythonInstantiations """
        lines = []
        lines.append("# Define state variables")
        #  Next, handle state variables
        for state in ASTUtils.allStateVars(ASTUtils.toDefinition(decl)):
            lines.append("self." + state.__name__ + " = " + generatePythonInitializer(state))
        lines.append("")
        return "\n".join(lines)

    #      * Handle initialization for state variable
    #      * @param state a state variable
    #      
    @classmethod
    def generatePythonInitializer(cls, state):
        """ generated source for method generatePythonInitializer """
        if not ASTUtils.isInitialized(state):
            return "None"
        list = state.getInit().stream().map(PyUtil.getPythonTargetValue).collect(Collectors.toList())
        return "[" + ", ".join(list) + "]" if len(list) > 1 else list.get(0)
