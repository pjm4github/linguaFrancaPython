#!/usr/bin/env python
""" generated source for module CMethodGenerator """
# package: org.lflang.generator.c


#  * Collection of functions to generate C code to declare methods.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#
from lflang import ASTUtils, InferredType
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.c import CUtil


class CMethodGenerator(object):
    """ generated source for class CMethodGenerator """
    #      * Generate macro definitions for methods.
    #      * @param reactor The reactor.
    #      * @param body The place to put the macro definitions.
    #      
    @classmethod
    def generateMacrosForMethods(cls, reactor, body):
        """ generated source for method generateMacrosForMethods """
        for method_ in allMethods(reactor):
            functionName = methodFunctionName(reactor, method_)
            body.pr("#define " + method_.__name__ + "(...) " + functionName + "(self, ##__VA_ARGS__)")

    #      * Generate macro undefinitions for methods.
    #      * @param reactor The reactor.
    #      * @param body The place to put the macro definitions.
    #      
    @classmethod
    def generateMacroUndefsForMethods(cls, reactor, body):
        """ generated source for method generateMacroUndefsForMethods """
        for method_ in allMethods(reactor):
            body.pr("#undef " + method_.__name__)

    #  
    #      * Generate a method function definition for a reactor.
    #      * This function will have a first argument that is a void* pointing to
    #      * the self struct, followed by any arguments given in its definition.
    #      * @param method The method.
    #      * @param decl The reactor declaration.
    #      * @param types The C-specific type conversion functions.
    #      
    @classmethod
    def generateMethod(cls, method_, decl, types):
        """ generated source for method generateMethod """
        code_ = CodeBuilder()
        body = ASTUtils.toText(method_.getCode())
        code_.prSourceLineNumber(method_)
        code_.prComment("Implementation of method " + method_.__name__ + "()")
        code_.pr(generateMethodSignature(method_, decl, types) + " {")
        code_.indent()
        #  Define the "self" struct.
        structType = CUtil.selfType(decl)
        #  A null structType means there are no inputs, state,
        #  or anything else. No need to declare it.
        if structType != None:
            code_.pr("\n".join([ structType + "* self = (" + structType + "*)instance_args;" + " SUPPRESS_UNUSED_WARNING(self);")])
        code_.prSourceLineNumber(method_.getCode())
        code_.pr(body)
        code_.unindent()
        code_.pr("}")
        return code_.__str__()

    #  
    #      * Generate method functions definition for a reactor.
    #      * These functions have a first argument that is a void* pointing to
    #      * the self struct.
    #      * @param decl The reactor.
    #      * @param code The place to put the code.
    #      * @param types The C-specific type conversion functions.
    #      
    @classmethod
    def generateMethods(cls, decl, code_, types):
        """ generated source for method generateMethods """
        reactor = ASTUtils.toDefinition(decl)
        code_.prComment("***** Start of method declarations.")
        signatures(decl, code_, types)
        cls.generateMacrosForMethods(reactor, code_)
        for method_ in allMethods(reactor):
            code_.pr(CMethodGenerator.generateMethod(method_, decl, types))
        cls.generateMacroUndefsForMethods(reactor, code_)
        code_.prComment("***** End of method declarations.")

    #      * Generate function signatures for methods.
    #      * This can be used to declare all the methods with signatures only
    #      * before giving the full definition so that methods may call each other
    #      * (and themselves) regardless of the order of definition.
    #      * @param decl The reactor declaration.
    #      * @param types The C-specific type conversion functions.
    #      
    @classmethod
    def signatures(cls, decl, body, types):
        """ generated source for method signatures """
        reactor = ASTUtils.toDefinition(decl)
        for method_ in allMethods(reactor):
            body.pr(generateMethodSignature(method_, decl, types) + ";")

    #      * Return the function name for specified method of the specified reactor.
    #      * @param reactor The reactor
    #      * @param method The method.
    #      * @return The function name for the method.
    #      
    @classmethod
    def methodFunctionName(cls, reactor, method_):
        """ generated source for method methodFunctionName """
        return reactor.__name__.lower() + "_method_" + method_.__name__

    #  
    #      * Generate a method function signature for a reactor.
    #      * This function will have a first argument that is a void* pointing to
    #      * the self struct, followed by any arguments given in its definition.
    #      * @param method The method.
    #      * @param decl The reactor declaration.
    #      * @param types The C-specific type conversion functions.
    #      
    @classmethod
    def generateMethodSignature(cls, method_, decl, types):
        """ generated source for method generateMethodSignature """
        functionName = cls.methodFunctionName(decl, method_)
        result = ""
        if method_.getReturn() != None:
            result.append(types.getTargetType(InferredType.fromAST(method_.getReturn())))
            result.append(" ")
        else:
            result.append("void ")
        result.append(functionName)
        result.append("(void* instance_args")
        if method_.getArguments() != None:
            for arg in method_.getArguments():
                result.append(", ")
                result.append(types.getTargetType(InferredType.fromAST(arg.getType())))
                result.append(" ")
                result.append(arg.__name__)
        result.append(")")
        return result.__str__()
