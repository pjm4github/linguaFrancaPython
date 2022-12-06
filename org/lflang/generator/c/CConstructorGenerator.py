#!/usr/bin/env python
""" generated source for module CConstructorGenerator """
# package: org.lflang.generator.c
from org.lflang.federated import FederateInstance

from org.lflang.generator import CodeBuilder

from org.lflang.lf import ReactorDecl

# 
#  * Generates C constructor code for a reactor.
#  *
#  
class CConstructorGenerator(object):
    """ generated source for class CConstructorGenerator """
    #      * Generate a constructor for the specified reactor in the specified federate.
    #      * @param reactor The parsed reactor data structure.
    #      * @param federate A federate name, or null to unconditionally generate.
    #      * @param constructorCode Lines of code previously generated that need to
    #      *  go into the constructor.
    #      
    @classmethod
    def generateConstructor(cls, reactor, federate, constructorCode):
        """ generated source for method generateConstructor """
        structType = CUtil.selfType(reactor)
        code_ = CodeBuilder()
        code_.pr(structType + "* new_" + reactor.__name__ + "() {")
        code_.indent()
        code_.pr(structType + "* self = (" + structType + "*)_lf_new_reactor(sizeof(" + structType + "));")
        code_.pr(constructorCode)
        code_.pr("return self;")
        code_.unindent()
        code_.pr("}")
        return code_.__str__()
