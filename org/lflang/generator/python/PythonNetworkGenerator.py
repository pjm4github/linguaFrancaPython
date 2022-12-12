#!/usr/bin/env python
""" generated source for module PythonNetworkGenerator """
# package: org.lflang.generator.python
from lflang.generator.python import PyUtil
from org.lflang.federated import FederateInstance

from org.lflang.federated import PythonGeneratorExtension

from org.lflang.lf import Expression

from org.lflang.lf import VarRef

from org.lflang.lf import Action

from org.lflang import InferredType

from org.lflang.TargetProperty import CoordinationType

from org.lflang.federated.serialization import SupportedSerializers

from org.lflang.generator import ReactionInstance

class PythonNetworkGenerator:
    """ generated source for class PythonNetworkGenerator """
    #      * Generate code for the body of a reaction that handles the
    #      * action that is triggered by receiving a message from a remote
    #      * federate.
    #      * @param action The action.
    #      * @param sendingPort The output port providing the data to send.
    #      * @param receivingPort The ID of the destination port.
    #      * @param receivingPortID The ID of the destination port.
    #      * @param sendingFed The sending federate.
    #      * @param receivingFed The destination federate.
    #      * @param receivingBankIndex The receiving federate's bank index, if it is in a bank.
    #      * @param receivingChannelIndex The receiving federate's channel index, if it is a multiport.
    #      * @param type The type.
    #      * @param isPhysical Indicates whether or not the connection is physical
    #      * @param serializer The serializer used on the connection.
    #      * @param coordinationType The coordination type
    #      
    @classmethod
    def generateNetworkReceiverBody(cls, action, sendingPort, receivingPort, receivingPortID, sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, type, isPhysical, serializer, coordinationType):
        """ generated source for method generateNetworkReceiverBody """
        result = ""
        #  We currently have no way to mark a reaction "unordered"
        #  in the AST, so we use a magic string at the start of the body.
        result.append("// " + ReactionInstance.UNORDERED_REACTION_MARKER + "\n")
        result.append(PyUtil.generateGILAcquireCode() + "\n")
        result.append(PythonGeneratorExtension.generateNetworkReceiverBody(action, sendingPort, receivingPort, receivingPortID, sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, type, isPhysical, serializer, coordinationType))
        result.append(PyUtil.generateGILReleaseCode() + "\n")
        return str(result)

    #      * Generate code for the body of a reaction that handles an output
    #      * that is to be sent over the network.
    #      * @param sendingPort The output port providing the data to send.
    #      * @param receivingPort The variable reference to the destination port.
    #      * @param receivingPortID The ID of the destination port.
    #      * @param sendingFed The sending federate.
    #      * @param sendingBankIndex The bank index of the sending federate, if it is a bank.
    #      * @param sendingChannelIndex The channel index of the sending port, if it is a multiport.
    #      * @param receivingFed The destination federate.
    #      * @param type The type.
    #      * @param isPhysical Indicates whether the connection is physical or not
    #      * @param delay The delay value imposed on the connection using after
    #      * @param serializer The serializer used on the connection.
    #      
    @classmethod
    def generateNetworkSenderBody(cls, sendingPort, receivingPort, receivingPortID, sendingFed, sendingBankIndex, sendingChannelIndex, receivingFed, type, isPhysical, delay, serializer, coordinationType):
        """ generated source for method generateNetworkSenderBody """
        result = ""
        #  We currently have no way to mark a reaction "unordered"
        #  in the AST, so we use a magic string at the start of the body.
        result.append("// " + ReactionInstance.UNORDERED_REACTION_MARKER + "\n")
        result.append(PyUtil.generateGILAcquireCode() + "\n")
        result.append(PythonGeneratorExtension.generateNetworkSenderBody(sendingPort, receivingPort, receivingPortID, sendingFed, sendingBankIndex, sendingChannelIndex, receivingFed, type, isPhysical, delay, serializer, coordinationType))
        result.append(PyUtil.generateGILReleaseCode() + "\n")
        return str(result)
