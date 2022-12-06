#!/usr/bin/env python
""" generated source for module CParameterGenerator """
# package: org.lflang.generator.c
# import java.util.LinkedList
# import java.util.List

#  * Generates C code to declare and initialize parameters.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#
from lflang.ASTUtils import ASTUtils
from lflang.generator import GeneratorBase
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.c import CUtil
from lflang.lf import ParameterReference


class CParameterGenerator(object):
    """ generated source for class CParameterGenerator """
    #      * Return a C expression that can be used to initialize the specified
    #      * parameter instance. If the parameter initializer refers to other
    #      * parameters, then those parameter references are replaced with
    #      * accesses to the self struct of the parents of those parameters.
    #      
    @classmethod
    def getInitializer(cls, p):
        """ generated source for method getInitializer """
        #  Handle the bank_index parameter.
        if p.__name__ == "bank_index":
            return CUtil.bankIndex(p.getParent())
        #  Handle overrides in the intantiation.
        #  In case there is more than one assignment to this parameter, we need to
        #  find the last one.
        lastAssignment = None
        for assignment in p.getParent().getDefinition().getParameters():
            if assignment.getLhs() == p.getDefinition():
                lastAssignment = assignment
        list = LinkedList()
        if lastAssignment != None:
            for expr in lastAssignment.getRhs():
                if isinstance(expr, (ParameterReference)):
                    param = (expr).getParameter()
                    list.append(CUtil.reactorRef(p.getParent().getParent()) + "->" + param.__name__)
                else:
                    list.append(GeneratorBase.getTargetTime(expr))
        else:
            for expr in p.getParent().initialParameterValue(p.getDefinition()):
                if ASTUtils.isOfTimeType(p.getDefinition()):
                    list.append(GeneratorBase.getTargetTime(expr))
                else:
                    list.append(GeneratorBase.getTargetTime(expr))
        if len(list) == 1:
            return list.get(0)
        else:
            return "{" + ", ".join( list) + "}"

    @classmethod
    def generateDeclarations(cls, reactor, types):
        """ generated source for method generateDeclarations """
        code_ = CodeBuilder()
        for parameter in ASTUtils.allParameters(reactor):
            code_.prSourceLineNumber(parameter)
            code_.pr(types.getTargetType(parameter) + " " + parameter.__name__ + ";")
        return code_.__str__()
