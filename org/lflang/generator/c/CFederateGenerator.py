#!/usr/bin/env python
""" generated source for module CFederateGenerator """
# package: org.lflang.generator.c
from org.lflang import ASTUtils

from org.lflang.federated import FederateInstance

from org.lflang.generator.CodeBuilder import CodeBuilder

from org.lflang.generator.GeneratorBase import GeneratorBase

from org.lflang.lf import Expression

from org.lflang.lf import ParameterReference

# 
#  * Generate code for federate related functionality
#  *
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#  
class CFederateGenerator:
    """ generated source for class CFederateGenerator """
    #      * Generate code that sends the neighbor structure message to the RTI.
    #      * @see MSG_TYPE_NEIGHBOR_STRUCTURE in net_common.h
    #      *
    #      * @param federate The federate that is sending its neighbor structure
    #      
    @classmethod
    def generateFederateNeighborStructure(cls, federate):
        """ generated source for method generateFederateNeighborStructure """
        code_ = CodeBuilder()
        code_.pr("\n".join([ "/**",
                             "* Generated function that sends information about connections between this federate and",
                             "* other federates where messages are routed through the RTI. Currently, this",
                             "* only includes logical connections when the coordination is centralized. This",
                             "* information is needed for the RTI to perform the centralized coordination.",
                             "* @see MSG_TYPE_NEIGHBOR_STRUCTURE in net_common.h",
                             "*/",
                             "void send_neighbor_structure_to_RTI(int rti_socket) {"]))
        code_.indent()
        #  Initialize the array of information about the federate's immediate upstream
        #  and downstream relayed (through the RTI) logical connections, to send to the
        #  RTI.
        code_.pr("\n".join(["interval_t candidate_tmp;",
                            "size_t buffer_size = 1 + 8 + ",
                            "                " + federate.dependsOn.keySet().size() +
                            " * ( sizeof(uint16_t) + sizeof(int64_t) ) +",
                            "                " + federate.sendsTo.keySet().size() +
                            " * sizeof(uint16_t);",
                            "unsigned char buffer_to_send[buffer_size];",
                            "",
                            "size_t message_head = 0;",
                            "buffer_to_send[message_head] = MSG_TYPE_NEIGHBOR_STRUCTURE;",
                            "message_head++;",
                            "encode_int32((int32_t)" + federate.dependsOn.keySet().size() +
                            ", &(buffer_to_send[message_head]));",
                            "message_head+=sizeof(int32_t);",
                            "encode_int32((int32_t)" + federate.sendsTo.keySet().size() +
                            ", &(buffer_to_send[message_head]));",
                            "message_head+=sizeof(int32_t);"]))
        if not federate.dependsOn.keySet().isEmpty():
            #  Next, populate these arrays.
            #  Find the minimum delay in the process.
            #  FIXME: Zero delay is not really the same as a microstep delay.
            for upstreamFederate in federate.dependsOn.keySet():
                code_.pr("\n".join(["encode_uint16((uint16_t)" + upstreamFederate.id + ", &(buffer_to_send[message_head]));",
                                    "message_head += sizeof(uint16_t);"]))
                #  The minimum delay calculation needs to be made in the C code because it
                #  may depend on parameter values.
                #  FIXME: These would have to be top-level parameters, which don't really
                #  have any support yet. Ideally, they could be overridden on the command line.
                #  When that is done, they will need to be in scope here.
                delays = federate.dependsOn.get(upstreamFederate)
                if delays != None:
                    #  There is at least one delay, so find the minimum.
                    #  If there is no delay at all, this is encoded as NEVER.
                    code_.pr("candidate_tmp = FOREVER;")
                    for delay in delays:
                        if delay == None:
                            #  Use NEVER to encode no delay at all.
                            code_.pr("candidate_tmp = NEVER;")
                        else:
                            delayTime = GeneratorBase.getTargetTime(delay)
                            if isinstance(delay, (ParameterReference)):
                                #  The delay is given as a parameter reference. Find its value.
                                param = (delay).getParameter()
                                delayTime = GeneratorBase.timeInTargetLanguage(ASTUtils.getDefaultAsTimeValue(param))
                            code_.pr("\n".join(["if (" + delayTime + " < candidate_tmp) {",
                                                "    candidate_tmp = " + delayTime + ";",
                                                "}"]))
                    code_.pr("\n".join(["encode_int64((int64_t)candidate_tmp, &(buffer_to_send[message_head]));",
                                        "message_head += sizeof(int64_t);"]))
                else:
                    #  Use NEVER to encode no delay at all.
                    code_.pr("\n".join([ "encode_int64(NEVER, &(buffer_to_send[message_head]));",
                                         "message_head += sizeof(int64_t);"]))
        #  Next, set up the downstream array.
        if not federate.sendsTo.keySet().isEmpty():
            #  Next, populate the array.
            #  Find the minimum delay in the process.
            #  FIXME: Zero delay is not really the same as a microstep delay.
            for downstreamFederate in federate.sendsTo.keySet():
                code_.pr("\n".join(["encode_uint16(" + downstreamFederate.id + ", &(buffer_to_send[message_head]));",
                                    "message_head += sizeof(uint16_t);"]))
        code_.pr("\n".join(["write_to_socket_errexit(",
                            "    rti_socket, ",
                            "    buffer_size,",
                            "    buffer_to_send,",
                            "    \"Failed to send the neighbor structure message to the RTI.\"",
                            ");"]))
        code_.unindent()
        code_.pr("}")
        return str(code_)
