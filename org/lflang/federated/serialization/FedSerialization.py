#!/usr/bin/env python
""" generated source for module FedSerialization """
from abc import ABCMeta, abstractmethod
# package: org.lflang.federated.serialization
# 
#  * Interface to enable support for automatic data serialization 
#  * in target code.
#  * 
#  * @author Soroush Bateni <soroush@utdallas.edu>
#  *
#  
class FedSerialization(object):
    """ generated source for interface FedSerialization """
    __metaclass__ = ABCMeta
    #      * Variable name in the target language for the serialized data.
    #      
    serializedVarName = "serialized_message"

    #      * Variable name in the target language for the deserialized data.
    #      
    deserializedVarName = "deserialized_message"

    #      * Check whether the current generator is compatible with the given
    #      * serialization technique or not.
    #      * 
    #      * @param generator The current generator.
    #      * @return true if compatible, false if not.
    #      
    @abstractmethod
    def isCompatible(self, generator):
        """ generated source for method isCompatible """

    #  
    #      * @return Expression in target language that corresponds to the length
    #      *  of the serialized buffer.
    #      
    @abstractmethod
    def serializedBufferLength(self):
        """ generated source for method serializedBufferLength """

    #      * @return Expression in target language that is the buffer variable
    #      *  itself.
    #      
    @abstractmethod
    def seializedBufferVar(self):
        """ generated source for method seializedBufferVar """

    #      * Generate code in target language that serializes 'varName'. This code
    #      * will convert the data in 'varName' from its 'originalType' into an 
    #      * unsigned byte array. The serialized data will be put in a variable 
    #      * with the name defined by @see serializedVarName.
    #      * 
    #      * @param varName The variable to be serialized.
    #      * @param originalType The original type of the variable.
    #      * @return Target code that serializes the 'varName' from 'type'
    #      *  to an unsigned byte array.
    #      
    @abstractmethod
    def generateNetworkSerializerCode(self, varName, originalType):
        """ generated source for method generateNetworkSerializerCode """

    #      * Generate code in target language that deserializes 'varName'. This code will
    #      * convert the data in 'varName' from an unsigned byte array into the 'targetType'.
    #      * The deserialized data will be put in a variable with the name defined by 
    #      * @see deserializedVarName.
    #      *  
    #      * @param varName The variable to deserialize.
    #      * @param targetType The type to deserialize into.
    #      * @return Target code that deserializes 'varName' from an unsigned byte array
    #      *  to 'type'.
    #      
    @abstractmethod
    def generateNetworkDeserializerCode(self, varName, targetType):
        """ generated source for method generateNetworkDeserializerCode """

    #      * @return Code in target language that includes all the necessary preamble to enable
    #      *  support for the current serializer.
    #      
    @abstractmethod
    def generatePreambleForSupport(self):
        """ generated source for method generatePreambleForSupport """

    #  
    #      * @return Code that should be appended to the compiler instructions (e.g., flags to gcc or
    #      *  additional lines to a CMakeLists.txt) to enable support for the current serializer.
    #      
    @abstractmethod
    def generateCompilerExtensionForSupport(self):
        """ generated source for method generateCompilerExtensionForSupport """
