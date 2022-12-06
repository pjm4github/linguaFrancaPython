#!/usr/bin/env python
""" generated source for module PythonReactorGenerator """
# package: org.lflang.generator_.python
from include.overloading import overloaded

# import java.util.ArrayList
# import java.util.List
from lflang.generator.python import PythonPreambleGenerator, PythonParameterGenerator, PythonMethodGenerator, \
    PythonReactionGenerator, PythonStateGenerator, PyUtil, PythonTypes
from org.lflang import ASTUtils

from org.lflang.federated import FederateInstance

from org.lflang.generator import CodeBuilder

from org.lflang.generator import GeneratorBase

from org.lflang.generator import ParameterInstance

from org.lflang.generator import ReactorInstance

from org.lflang.lf import Reaction

from org.lflang.lf import Reactor

from org.lflang.lf import ReactorDecl

class PythonReactorGenerator(object):
    """ generated source for class PythonReactorGenerator """
    #      * Wrapper function for the more elaborate generatePythonReactorClass that keeps track
    #      * of visited reactors to avoid duplicate generation
    #      * @param instance The reactor instance to be generated
    #      * @param pythonClasses The class definition is appended to this code builder
    #      * @param federate The federate instance for the reactor instance
    #      * @param instantiatedClasses A list of visited instances to avoid generating duplicates
    #      
    @classmethod
    @overloaded
    def generatePythonClass(cls, instance, federate, main, types):
        """ generated source for method generatePythonClass """
        instantiatedClasses = []
        return cls.generatePythonClass(instance, federate, instantiatedClasses, main, types)

    #      * Generate a Python class corresponding to decl
    #      * @param instance The reactor instance to be generated
    #      * @param pythonClasses The class definition is appended to this code builder
    #      * @param federate The federate instance for the reactor instance
    #      * @param instantiatedClasses A list of visited instances to avoid generating duplicates
    #      
    @classmethod
    @generatePythonClass.register(object, ReactorInstance, FederateInstance, list, ReactorInstance, PythonTypes)
    def generatePythonClass_0(cls, instance, federate, instantiatedClasses, main, types):
        """ generated source for method generatePythonClass_0 """
        pythonClasses = CodeBuilder()
        decl = instance.getDefinition().getReactorClass()
        reactor = ASTUtils.toDefinition(decl)
        className = instance.getDefinition().getReactorClass().__name__
        if instance != main and not federate.contains(instance) or instantiatedClasses == None or className.contains(GeneratorBase.GEN_DELAY_CLASS_NAME):
            return ""
        if federate.contains(instance) and not instantiatedClasses.contains(className):
            pythonClasses.pr(cls.generatePythonClassHeader(className))
            pythonClasses.indent()
            pythonClasses.pr(PythonPreambleGenerator.generatePythonPreambles(reactor.getPreambles()))
            pythonClasses.pr(cls.generatePythonConstructor(decl, types))
            pythonClasses.pr(PythonParameterGenerator.generatePythonGetters(decl))
            pythonClasses.pr(PythonMethodGenerator.generateMethods(reactor))
            reactionToGenerate = ASTUtils.allReactions(reactor)
            if reactor.isFederated():
                new_reactionToGenerate = []
                for it in reactionToGenerate:
                    if it in federate or it in  federate.networkReactions:
                        pass
                    else:
                        new_reactionToGenerate.append(it)
                reactionToGenerate = new_reactionToGenerate

            pythonClasses.pr(PythonReactionGenerator.generatePythonReactions(reactor, reactionToGenerate))
            pythonClasses.unindent()
            pythonClasses.pr("\n")
            instantiatedClasses.append(className)
        for child in instance.children:
            pythonClasses.pr(cls.generatePythonClass(child, federate, instantiatedClasses, main, types))
        return pythonClasses.getCode()

    @classmethod
    def generatePythonClassHeader(cls, className):
        """ generated source for method generatePythonClassHeader """
        return "\n".join(["# Python class for reactor " + className + "", "class _" + className + ":"])

    @classmethod
    def generatePythonConstructor(cls, decl, types):
        """ generated source for method generatePythonConstructor """
        code_ = CodeBuilder()
        code_.pr("# Constructor")
        code_.pr("def __init__(self, **kwargs):")
        code_.indent()
        code_.pr(PythonParameterGenerator.generatePythonInstantiations(decl, types))
        code_.pr(PythonStateGenerator.generatePythonInstantiations(decl))
        return code_.__str__()

    @classmethod
    def generateListsToHoldClassInstances(cls, instance, federate):
        """ generated source for method generateListsToHoldClassInstances """
        code_ = CodeBuilder()
        if federate != None and not federate.contains(instance):
            return ""
        code_.pr(PyUtil.reactorRefName(instance) + " = [None] * " + instance.getTotalWidth())
        for child in instance.children:
            code_.pr(cls.generateListsToHoldClassInstances(child, federate))
        return code_.__str__()

    @classmethod
    def generatePythonClassInstantiations(cls, instance, federate, main):
        """ generated source for method generatePythonClassInstantiations """
        code_ = CodeBuilder()
        if instance != main and not federate.contains(instance):
            return ""
        className = instance.getDefinition().getReactorClass().__name__
        if className.contains(GeneratorBase.GEN_DELAY_CLASS_NAME):
            return ""
        if federate.contains(instance) and instance.getWidth() > 0:
            fullName = instance.getFullName()
            code_.pr("\n".join(["# Start initializing " + fullName + " of class " + className,
                                "for " + PyUtil.bankIndexName(instance) + " in range(" + instance.getWidth() + "):"]
                               )
                     )
            code_.indent()
            code_.pr("bank_index = " + PyUtil.bankIndexName(instance))
            code_.pr(cls.generatePythonClassInstantiation(instance, className))
        for child in instance.children:
            code_.pr(cls.generatePythonClassInstantiations(child, federate, main))
        code_.unindent()
        return code_.__str__()

    @classmethod
    def generatePythonClassInstantiation(cls, instance, className):
        """ generated source for method generatePythonClassInstantiation """
        code_ = CodeBuilder()
        code_.pr(PyUtil.reactorRef(instance) + " = _" + className + "(")
        code_.indent()
        code_.pr("_bank_index = " + PyUtil.bankIndex(instance) + ",")
        for param in instance.parameters:
            if not param.__name__ == "bank_index":
                code_.pr("_" + param.__name__ + "=" + PythonParameterGenerator.generatePythonInitializer(param) + ",")
        code_.unindent()
        code_.pr(")")
        return code_.__str__()
