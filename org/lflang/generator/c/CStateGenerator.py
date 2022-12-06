#!/usr/bin/env python
""" generated source for module CStateGenerator """
# package: org.lflang.generator.c
# import java.util.LinkedList
from lflang import ASTUtils
from lflang.generator import GeneratorBase
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.c import CUtil, CModesGenerator
from lflang.lf import ParameterReference


class CStateGenerator(object):
    """ generated source for class CStateGenerator """
    #      * Generate code for state variables of a reactor in the form "stateVar.type stateVar.name;"
    #      * @param reactor The reactor
    #      * @param types A helper object for types
    #      
    @classmethod
    def generateDeclarations(cls, reactor, types):
        """ generated source for method generateDeclarations """
        code_ = CodeBuilder()
        for stateVar in ASTUtils.allStateVars(reactor):
            code_.prSourceLineNumber(stateVar)
            code_.pr(types.getTargetType(stateVar) + " " + stateVar.__name__ + ";")
        return code_.__str__()

    #      * If the state is initialized with a parameter, then do not use
    #      * a temporary variable. Otherwise, do, because
    #      * static initializers for arrays and structs have to be handled
    #      * this way, and there is no way to tell whether the type of the array
    #      * is a struct.
    #      *
    #      * @param instance
    #      * @param stateVar
    #      * @param mode
    #      * @return
    #      
    @classmethod
    def generateInitializer(cls, instance, selfRef, stateVar, mode, types):
        """ generated source for method generateInitializer """
        initExpr = getInitializerExpr(stateVar, instance)
        baseInitializer = generateBaseInitializer(selfRef, stateVar, initExpr, types)
        modalReset = generateModalReset(instance, selfRef, stateVar, initExpr, mode, types)
        return "\n".join([ baseInitializer, modalReset])

    @classmethod
    def generateBaseInitializer(cls, selfRef, stateVar, initExpr, types):
        """ generated source for method generateBaseInitializer """
        if ASTUtils.isOfTimeType(stateVar) or ASTUtils.isParameterized(stateVar) and stateVar.getInit().size() > 0:
            return selfRef + "->" + stateVar.__name__ + " = " + initExpr + ";"
        else:
            declaration = types.getVariableDeclaration(ASTUtils.getInferredType(stateVar), "_initial", True)
            return "\n".join([ "{ // For scoping", "    static " + declaration + " = " + initExpr + ";", "    " + selfRef + "->" + stateVar.__name__ + " = _initial;", "} // End scoping."])

    @classmethod
    def generateModalReset(cls, instance, selfRef, stateVar, initExpr, mode, types):
        """ generated source for method generateModalReset """
        if mode == None or not stateVar.isReset():
            return ""
        modeRef = "&" + CUtil.reactorRef(mode.getParent()) + "->_lf__modes[" + mode.getParent().modes.indexOf(mode) + "]"
        type = types.getTargetType(ASTUtils.getInferredType(stateVar))
        if ASTUtils.isOfTimeType(stateVar) or ASTUtils.isParameterized(stateVar) and stateVar.getInit().size() > 0:
            return CModesGenerator.generateStateResetStructure(modeRef, selfRef, stateVar.__name__, initExpr, type)
        else:
            code_ = CodeBuilder()
            source = "_initial"
            declaration = types.getVariableDeclaration(ASTUtils.getInferredType(stateVar), source, True)
            code_.pr("{ // For scoping")
            code_.indent()
            code_.pr("static " + declaration + " = " + initExpr + ";")
            code_.pr(CModesGenerator.generateStateResetStructure(modeRef, selfRef, stateVar.__name__, source, type))
            code_.unindent()
            code_.pr("} // End scoping.")
            return code_.__str__()

    #      * Return a C expression that can be used to initialize the specified
    #      * state variable within the specified parent. If the state variable
    #      * initializer refers to parameters of the parent, then those parameter
    #      * references are replaced with accesses to the self struct of the parent.
    #      
    @classmethod
    def getInitializerExpr(cls, state, parent):
        """ generated source for method getInitializerExpr """
        list = LinkedList()
        for expr in state.getInit():
            if isinstance(expr, (ParameterReference)):
                param = (expr).getParameter()
                list.append(CUtil.reactorRef(parent) + "->" + param.__name__)
            else:
                list.append(GeneratorBase.getTargetTime(expr))
        return list.get(0) if len(list) == 1 else "{" + ", ".join( list) + "}"
