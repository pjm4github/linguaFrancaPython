#!/usr/bin/env python
""" generated source for module FedNativePythonSerialization """
# 
#  * Copyright (c) 2021, The University of California at Berkeley.
#  * Copyright (c) 2021, The University of Texas at Dallas.
#  * 
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  * 
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  * 
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
#  * 
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  * POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.federated.serialization
from org.lflang import Target

from org.lflang.generator import GeneratorBase
import FedSerialization
# 
#  * Enables support for Python pickle serialization.
#  * 
#  * @author Soroush Bateni <soroush@utdallas.edu>
#  *
#  
class FedNativePythonSerialization(FedSerialization):
    """ generated source for class FedNativePythonSerialization """
    def isCompatible(self, generator):
        """ generated source for method isCompatible """
        if generator.getTarget() != Target.Python:
            raise TypeError("This class only support Python serialization.")
        return True

    def serializedBufferLength(self):
        """ generated source for method serializedBufferLength """
        return serializedVarName + ".len"

    def seializedBufferVar(self):
        """ generated source for method seializedBufferVar """
        return serializedVarName + ".buf"

    def generateNetworkSerializerCode(self, varName, originalType):
        """ generated source for method generateNetworkSerializerCode """
        serializerCode = ""
        #  Check that global_pickler is not null
        serializerCode.append("if (global_pickler == NULL) lf_print_error_and_exit(\"The pickle module is not loaded.\");\n")
        #  Define the serialized PyObject
        serializerCode.append("PyObject* serialized_pyobject = PyObject_CallMethod(global_pickler, \"dumps\", \"O\", " + varName + ");\n")
        #  Error check
        serializerCode.append("if (serialized_pyobject == NULL) {\n")
        serializerCode.append("    if (PyErr_Occurred()) PyErr_Print();\n")
        serializerCode.append("    lf_print_error_and_exit(\"Could not serialize serialized_pyobject.\");\n")
        serializerCode.append("}\n")
        serializerCode.append("Py_buffer " + serializedVarName + ";\n")
        serializerCode.append("int returnValue = PyBytes_AsStringAndSize(serialized_pyobject, &" + serializedVarName + ".buf, &" + serializedVarName + ".len);\n")
        #  Error check
        serializerCode.append("if (returnValue == -1) {\n")
        serializerCode.append("    if (PyErr_Occurred()) PyErr_Print();\n")
        serializerCode.append("    lf_print_error_and_exit(\"Could not serialize " + serializedVarName + ".\");\n")
        serializerCode.append("}\n")
        return serializerCode

    def generateNetworkDeserializerCode(self, varName, targetType):
        """ generated source for method generateNetworkDeserializerCode """
        deserializerCode = ""
        #  Convert the network message to a Python ByteArray
        deserializerCode.append("PyObject* message_byte_array = " + "PyBytes_FromStringAndSize((char*)" + varName + "->token->value, " + varName + "->token->length);\n")
        #  Deserialize using Pickle
        deserializerCode.append("Py_XINCREF(message_byte_array);\n")
        deserializerCode.append("PyObject* " + deserializedVarName + " = PyObject_CallMethod(global_pickler, \"loads\", \"O\", message_byte_array);\n")
        #  Error check
        deserializerCode.append("if (" + deserializedVarName + " == NULL) {\n")
        deserializerCode.append("    if (PyErr_Occurred()) PyErr_Print();\n")
        deserializerCode.append("    lf_print_error_and_exit(\"Could not deserialize " + deserializedVarName + ".\");\n")
        deserializerCode.append("}\n")
        #  Decrment the reference count
        deserializerCode.append("Py_XDECREF(message_byte_array);\n")
        return deserializerCode

    def generatePreambleForSupport(self):
        """ generated source for method generatePreambleForSupport """
        return StringBuilder("")

    def generateCompilerExtensionForSupport(self):
        """ generated source for method generateCompilerExtensionForSupport """
        return StringBuilder("")
