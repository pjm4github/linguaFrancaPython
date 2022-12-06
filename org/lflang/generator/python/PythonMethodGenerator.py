#!/usr/bin/env python
""" generated source for module PythonMethodGenerator """
# package: org.lflang.generator.python
# import java.util.stream.Collectors

#  * Collection of functions to generate Python code to declare methods.
#  *
#  * @author {Soroush Bateni <soroush@berkeley.edu>}
#  
class PythonMethodGenerator(object):
    """ generated source for class PythonMethodGenerator """
    #      * Generate a Python method definition for {@code method}.
    #      
    @classmethod
    def generateMethod(cls, method_):
        """ generated source for method generateMethod """
        return "\n".join([ "# Implementation of method " + method_.__name__ + "().", "def " + method_.__name__ + "(self, " + generateMethodArgumentList(method_) + "):", ASTUtils.toText(method_.getCode()).indent(4)])

    #      * Generate methods for a reactor class.
    #      *
    #      * @param reactor The reactor.
    #      
    @classmethod
    def generateMethods(cls, reactor):
        """ generated source for method generateMethods """
        return ""
        #          ASTUtils.allMethods(reactor)
        #                         .stream()
        #                         .map(m -> generateMethod(m))
        #                         .collect(Collectors.joining());

    #      * Generate a list of arguments for {@code method} delimited with ', '.
    #      
    @classmethod
    def generateMethodArgumentList(cls, method_):
        """ generated source for method generateMethodArgumentList """
        return ", ".join( method_.getArguments().stream().map(MethodArgument.getName).collect(Collectors.toList()))
