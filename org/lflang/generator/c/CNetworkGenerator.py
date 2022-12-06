#!/usr/bin/env python
""" generated source for module CNetworkGenerator """
# package: org.lflang.generator.c
from org.lflang.federated import CGeneratorExtension

from org.lflang.federated import FederateInstance

from org.lflang.lf import Expression

from org.lflang.lf import VarRef

from org.lflang.lf import Action

from org.lflang.lf import Port
# import java.util.regex.Pattern

from org.lflang import ASTUtils

from org.lflang import InferredType

from org.lflang import TimeValue

from org.lflang.TargetProperty import CoordinationType

from org.lflang.federated.serialization import FedROS2CPPSerialization

from org.lflang.federated.serialization import SupportedSerializers

from org.lflang.generator import CodeBuilder

from org.lflang.generator import GeneratorBase

from org.lflang.generator import ReactionInstance

# 
#  * Generates C code to support messaging-related functionalities
#  * in federated execution.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#  
class CNetworkGenerator(object):
    """ generated source for class CNetworkGenerator """
    @classmethod
    def isSharedPtrType(cls, type, types):
        """ generated source for method isSharedPtrType """
        return not type.isUndefined() and sharedPointerVariable.matcher(types.getTargetType(type)).find()

    #  Regular expression pattern for shared_ptr types.
    sharedPointerVariable = re.compile("^(/\\*.*?\\*/)?std::shared_ptr<(?<type>((/\\*.*?\\*/)?(\\S+))+)>$")

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
    def generateNetworkReceiverBody(cls, action, sendingPort, receivingPort, receivingPortID, sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, type, isPhysical, serializer, types, coordinationType):
        """ generated source for method generateNetworkReceiverBody """
        #  Adjust the type of the action and the receivingPort.
        #  If it is "string", then change it to "char*".
        #  This string is dynamically allocated, and type 'string' is to be
        #  used only for statically allocated strings.
        #  FIXME: Is the getTargetType method not responsible for generating the desired C code
        #   (e.g., char* rather than string)? If not, what exactly is that method
        #   responsible for? If generateNetworkReceiverBody has different requirements
        #   than those that the method was designed to satisfy, should we use a different
        #   method? The best course of action is not obvious, but we have a pattern of adding
        #   downstream patches to generated strings rather than fixing them at their source.
        if types.getTargetType(action) == "string":
            action.getType().setCode(None)
            action.getType().setId("char*")
        if types.getTargetType(receivingPort.getVariable()) == "string":
            (receivingPort.getVariable()).getType().setCode(None)
            (receivingPort.getVariable()).getType().setId("char*")
        receiveRef = CUtil.portRefInReaction(receivingPort, receivingBankIndex, receivingChannelIndex)
        result = CodeBuilder()
        result.pr("// " + ReactionInstance.UNORDERED_REACTION_MARKER)
        result.pr(receiveRef + "->physical_time_of_arrival = self->_lf__" + action.__name__ + ".physical_time_of_arrival;")
        if coordinationType == CoordinationType.DECENTRALIZED and not isPhysical:
            result.pr(receiveRef + "->intended_tag = self->_lf__" + action.__name__ + ".intended_tag;\n")
        value = ""
        if serializer == NATIVE:
            value = action.__name__ + "->value"
            if CUtil.isTokenType(type, types):
                result.pr("lf_set_token(" + receiveRef + ", " + action.__name__ + "->token);")
            else:
                result.pr("lf_set(" + receiveRef + ", " + value + ");")
        elif serializer == PROTO:
            raise TypeError("Protobuf serialization is not supported yet.")
        elif serializer == ROS2:
            portType = ASTUtils.getInferredType((receivingPort.getVariable()))
            portTypeStr = types.getTargetType(portType)
            if CUtil.isTokenType(portType, types):
                raise TypeError("Cannot handle ROS serialization when ports are pointers.")
            elif cls.isSharedPtrType(portType, types):
                matcher = cls.sharedPointerVariable.matcher(portTypeStr)
                if matcher.find():
                    portTypeStr = matcher.group("type")
            ROSDeserializer = FedROS2CPPSerialization()
            value = FedROS2CPPSerialization.deserializedVarName
            result.pr(ROSDeserializer.generateNetworkDeserializerCode("self->_lf__" + action.__name__, portTypeStr))
            if cls.isSharedPtrType(portType, types):
                result.pr("auto msg_shared_ptr = std::make_shared<" + portTypeStr + ">(" + value + ");")
                result.pr("lf_set(" + receiveRef + ", msg_shared_ptr);")
            else:
                result.pr("lf_set(" + receiveRef + ", std::move(" + value + "));")
        return result.__str__()

    @classmethod
    def generateNetworkSenderBody(cls, sendingPort, receivingPort, receivingPortID, sendingFed, sendingBankIndex, sendingChannelIndex, receivingFed, type, isPhysical, delay, serializer, types, coordinationType):
        """ generated source for method generateNetworkSenderBody """
        sendRef = CUtil.portRefInReaction(sendingPort, sendingBankIndex, sendingChannelIndex)
        receiveRef = ASTUtils.generateVarRef(receivingPort)
        result = CodeBuilder()
        result.pr("// " + ReactionInstance.UNORDERED_REACTION_MARKER + "\n")
        result.pr("// Sending from " + sendRef + " in federate " + sendingFed.name + " to " + receiveRef + " in federate " + receivingFed.name)
        if sendingBankIndex != -1 or sendingChannelIndex != -1:
            result.pr("if (!" + sendRef + "->is_present) return;")
        messageType = None
        next_destination_name = "\"federate " + receivingFed.id + "\""
        additionalDelayString = CGeneratorExtension.getNetworkDelayLiteral(delay)
        if isPhysical:
            messageType = "MSG_TYPE_P2P_MESSAGE"
        elif coordinationType == CoordinationType.DECENTRALIZED:
            messageType = "MSG_TYPE_P2P_TAGGED_MESSAGE"
        else:
            messageType = "MSG_TYPE_TAGGED_MESSAGE"
            next_destination_name = "\"federate " + receivingFed.id + " via the RTI\""
        sendingFunction = "send_timed_message"
        commonArgs = ", ".join([ additionalDelayString, messageType, receivingPortID + "", receivingFed.id + "", next_destination_name, "message_length"])
        if isPhysical:
            sendingFunction = "send_message"
            commonArgs = messageType + ", " + receivingPortID + ", " + receivingFed.id + ", " + next_destination_name + ", message_length"
        lengthExpression = ""
        pointerExpression = ""
        if serializer == NATIVE:
            if CUtil.isTokenType(type, types):
                result.pr("size_t message_length = " + sendRef + "->token->length * " + sendRef + "->token->element_size;")
                result.pr(sendingFunction + "(" + commonArgs + ", (unsigned char*) " + sendRef + "->value);")
            else:
                lengthExpression = "sizeof(" + types.getTargetType(type) + ")"
                pointerExpression = "(unsigned char*)&" + sendRef + "->value"
                targetType = types.getTargetType(type)
                if targetType == "string":
                    lengthExpression = "strlen(" + sendRef + "->value) + 1"
                    pointerExpression = "(unsigned char*) " + sendRef + "->value"
                elif targetType == "void":
                    lengthExpression = "0"
                result.pr("size_t message_length = " + lengthExpression + ";")
                result.pr(sendingFunction + "(" + commonArgs + ", " + pointerExpression + ");")
        elif serializer == PROTO:
            raise TypeError("Protobuf serialization is not supported yet.")
        elif serializer == ROS2:
            variableToSerialize = sendRef
            typeStr = types.getTargetType(type)
            if CUtil.isTokenType(type, types):
                raise TypeError("Cannot handle ROS serialization when ports are pointers.")
            elif cls.isSharedPtrType(type, types):
                matcher = cls.sharedPointerVariable.matcher(typeStr)
                if matcher.find():
                    typeStr = matcher.group("type")
            ROSSerializer = FedROS2CPPSerialization()
            lengthExpression = ROSSerializer.serializedBufferLength()
            pointerExpression = ROSSerializer.seializedBufferVar()
            result.pr(ROSSerializer.generateNetworkSerializerCode(variableToSerialize, typeStr, cls.isSharedPtrType(type, types)))
            result.pr("size_t message_length = " + lengthExpression + ";")
            result.pr(sendingFunction + "(" + commonArgs + ", " + pointerExpression + ");")
        return result.__str__()

    @classmethod
    def generateNetworkInputControlReactionBody(cls, receivingPortID, maxSTP, isFederatedAndDecentralized):
        """ generated source for method generateNetworkInputControlReactionBody """
        result = CodeBuilder()
        result.pr("// " + ReactionInstance.UNORDERED_REACTION_MARKER + "\n")
        result.pr("interval_t max_STP = 0LL;")
        if isFederatedAndDecentralized:
            result.pr("max_STP = " + GeneratorBase.timeInTargetLanguage(maxSTP) + ";")
        result.pr("// Wait until the port status is known")
        result.pr("wait_until_port_status_known(" + receivingPortID + ", max_STP);")
        return result.__str__()

    @classmethod
    def generateNetworkOutputControlReactionBody(cls, port, portID, receivingFederateID, sendingBankIndex, sendingChannelIndex, delay):
        """ generated source for method generateNetworkOutputControlReactionBody """
        result = CodeBuilder()
        result.pr("// " + ReactionInstance.UNORDERED_REACTION_MARKER + "\n")
        sendRef = CUtil.portRefInReaction(port, sendingBankIndex, sendingChannelIndex)
        additionalDelayString = CGeneratorExtension.getNetworkDelayLiteral(delay)
        result.pr("\n".join([ "// If the output port has not been lf_set for the current logical time,", "// send an ABSENT message to the receiving federate            ", "LF_PRINT_LOG(\"Contemplating whether to send port \"", "          \"absent for port %d to federate %d.\", ", "          " + portID + ", " + receivingFederateID + ");", "if (" + sendRef + " == NULL || !" + sendRef + "->is_present) {", "    // The output port is NULL or it is not present.", "    send_port_absent_to_federate(" + additionalDelayString + ", " + portID + ", " + receivingFederateID + ");", "}")])
        return result.__str__()
