#!/usr/bin/env python
""" generated source for module PyUtil """
#  Utilities for Python code generation. 
# 
# Copyright (c) 2019-2021, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.generator.python
from lflang import ASTUtils
from include.overloading import overloaded
from org.lflang.generator import ReactorInstance

from org.lflang.generator import GeneratorBase

from org.lflang.generator.c import CUtil

from org.lflang.lf import Expression

from org.lflang.lf import ParameterReference

from org.lflang import ASTUtils

# 
#  * A collection of utilities for Python code generation.
#  * This class inherits from CUtil but overrides a few methods to
#  * codify the coding conventions for the Python target code generator.
#  * I.e., it defines how some variables are named and referenced.
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  * @author{Soroush Bateni <soroush@utdallas.edu>}
#  
class PyUtil(CUtil):
    """ generated source for class PyUtil """
    #      * Return the name of the list of Python class instances that contains the
    #      * specified reactor instance. This is similar to
    #      * {@link #reactorRef(ReactorInstance)} except that it does not index into
    #      * the list.
    #      *
    #      * @param instance The reactor instance.
    #      
    @classmethod
    def reactorRefName(cls, instance):
        """ generated source for method reactorRefName """
        return instance.uniqueID() + "_lf"

    #      * Return a reference to the list of Python class instances that contains
    #      * the specified reactor instance. The returned string has the form
    #      * list_name[runtimeIndex], where list_name is the name of the list of
    #      * Python class instances that contains this reactor instance. If
    #      * runtimeIndex is null, then it is replaced by the expression returned by
    #      * {@link runtimeIndex(ReactorInstance)} or 0 if there are no banks.
    #      *
    #      * @param instance     The reactor instance.
    #      * @param runtimeIndex An optional expression to use to address bank
    #      *                     members. If this is null, the expression used will be
    #      *                     that returned by
    #      *                     {@link #runtimeIndex(ReactorInstance)}.
    #      
    @classmethod
    @overloaded
    def reactorRef(cls, instance, runtimeIndex):
        """ generated source for method reactorRef """
        if runtimeIndex == None:
            runtimeIndex = runtimeIndex(instance)
        return PyUtil.reactorRefName(instance) + "[" + runtimeIndex + "]"

    #      * Return a reference to the list of Python class instances that contains
    #      * the specified reactor instance. The returned string has the form
    #      * list_name[j], where list_name is the name of the list of of Python class
    #      * instances that contains this reactor instance and j is the expression
    #      * returned by {@link #runtimeIndex(ReactorInstance)} or 0 if there are no
    #      * banks.
    #      *
    #      * @param instance The reactor instance.
    #      
    @classmethod
    @reactorRef.register(object, ReactorInstance)
    def reactorRef_0(cls, instance):
        """ generated source for method reactorRef_0 """
        return PyUtil.reactorRef(instance, None)

    #      * Convert C types to formats used in Py_BuildValue and PyArg_PurseTuple.
    #      * This is unused but will be useful to enable inter-compatibility between
    #      * C and Python reactors.
    #      * @param type C type
    #      
    @classmethod
    def pyBuildValueArgumentType(cls, type):
        """ generated source for method pyBuildValueArgumentType """
        if type == "int":
            return "i"
        elif type == "string":
            return "s"
        elif type == "char":
            return "b"
        elif type == "short int":
            return "h"
        elif type == "long":
            return "l"
        elif type == "unsigned char":
            return "B"
        elif type == "unsigned short int":
            return "H"
        elif type == "unsigned int":
            return "I"
        elif type == "unsigned long":
            return "k"
        elif type == "long long":
            return "L"
        elif type == "interval_t":
            return "L"
        elif type == "unsigned long long":
            return "K"
        elif type == "double":
            return "d"
        elif type == "float":
            return "f"
        elif type == "Py_complex":
            return "D"
        elif type == "Py_complex*":
            return "D"
        elif type == "Py_Object":
            return "O"
        elif type == "Py_Object*":
            return "O"
        else:
            return "O"

    @classmethod
    def generateGILAcquireCode(cls):
        """ generated source for method generateGILAcquireCode """
        return "\n".join([ "// Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.", "PyGILState_STATE gstate;", "gstate = PyGILState_Ensure();"])

    @classmethod
    def generateGILReleaseCode(cls):
        """ generated source for method generateGILReleaseCode """
        return "\n".join([ "/* Release the thread. No Python API allowed beyond this point. */", "PyGILState_Release(gstate);"])

    #      * Override to convert some C types to their
    #      * Python equivalent.
    #      * Examples:
    #      * true/false -> True/False
    #      * @param expr A value
    #      * @return A value string in the target language
    #      
    @classmethod
    def getPythonTargetValue(cls, expr):
        """ generated source for method getPythonTargetValue """
        returnValue = None
        if ASTUtils.toOriginalText(expr) == "false":
            returnValue = "False"
        elif ASTUtils.toOriginalText(expr) == "true":
            returnValue = "True"
        else:
            returnValue = GeneratorBase.getTargetValue(expr)
        #  Parameters in Python are always prepended with a 'self.'
        #  predicate. Therefore, we need to append the returned value
        #  if it is a parameter.
        if isinstance(expr, (ParameterReference)):
            returnValue = "self." + returnValue
        return returnValue
