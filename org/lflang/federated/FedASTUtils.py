#!/usr/bin/env python
""" generated source for module FedASTUtils """
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
# package: org.lflang.federated
# import java.util.ArrayList
# import java.util.Collections
# import java.util.LinkedList
# import java.util.List
# import java.util.Objects
# import java.util.Optional
# import java.util.stream.Collectors
# import org.eclipse.emf.ecore.util.EcoreUtil

from lflang.ASTUtils import ASTUtils
from lflang.InferredType import InferredType
from lflang.TargetProperty import CoordinationType
from lflang.TimeValue import TimeValue
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import EcoreUtil
from lflang.federated.serialization.SupportedSerializers import SupportedSerializers
from lflang.lf.ActionOrigin import Collections, ActionOrigin
from lflang.lf.LfFactory import LfFactory
from lflang.lf.ParameterReference import ParameterReference
from lflang.lf.VarRef import VarRef


class FedASTUtils(object):
    #  A helper class for AST transformations needed for federated
    #  execution.
    #
    #  @author Soroush Bateni {soroush@utdallas.edu}
    #  @author Edward A. Lee {eal@berkeley.edu}
    #
    @classmethod
    def safe(cls, list):
        """
        Return a null-safe List
        * @param <E> The type of the list
        :param list: The potentially null List
        :return: Empty list or the original list
        """
        return Collections.emptyList() if list == None else list


    @classmethod
    def createNetworkAction(cls, connection, serializer, type, networkBufferType):
        """
        Create a "network action" in the reactor that contains the given
        connection and return it.
              *
        The purpose of this action is to serve as a trigger for a "network
        input reaction" that is responsible for relaying messages to the
        port that is on the receiving side of the given connection. The
        connection is assumed to be between two reactors that reside in
        distinct federates. Hence, the container of the connection is
        assumed to be top-level.

        :param connection: A connection between to federates.
        :param serializer: The serializer used on the connection.
        :param type: The type of the source port (indicating the type of
                     data to be received).
        :param networkBufferType: The type of the buffer used for network
                                communication in the target (e.g., uint8_t* in C).
        :return: The newly created action.
        """
        top = connection.eContainer()
        factory = LfFactory.eINSTANCE
        action = factory.createAction()
        #  Name the newly created action; set its delay and type.
        action.setName(ASTUtils.getUniqueIdentifier(top, "networkMessage"))
        if serializer == SupportedSerializers.NATIVE:
            action.setType(type)
        else:
            action_type = factory.createType()
            action_type.setId(networkBufferType)
            action.setType(action_type)
        #  The connection is 'physical' if it uses the ~> notation.
        if connection.isPhysical():
            action.setOrigin(ActionOrigin.PHYSICAL)
            #  Messages sent on physical connections do not
            #  carry a timestamp, or a delay. The delay
            #  provided using after is enforced by setting
            #  the minDelay.
            if connection.getDelay() != None:
                action.setMinDelay(connection.getDelay())
        else:
            action.setOrigin(ActionOrigin.LOGICAL)
        return action


    @classmethod
    def addNetworkReceiverReaction(cls, networkAction, source, destination, connection, sourceFederate, destinationFederate, rightBankIndex, rightChannelIndex, generator, coordination, serializer):
        """
        Add a network receiver reaction for a given input port 'destination' to
        destination's parent reactor. This reaction will react to a generated
        'networkAction' (triggered asynchronously, e.g., by federate.c). This
        'networkAction' will contain the actual message that is sent by the sender
        in 'action->value'. This value is forwarded to 'destination' in the network
        receiver reaction.

        @note: Used in federated execution

        :param networkAction: The network action (also, @see createNetworkAction)
        :param source: The source port instance.
        :param destination:  The destination port instance.
        :param connection: The network connection.
        :param sourceFederate: The source federate.
        :param destinationFederate: The destination federate.
        :param rightBankIndex:  The right bank index or -1 if the right reactor is not in a bank.
        :param rightChannelIndex: The right channel index or -1 if the right port is not a multiport.
        :param generator:  The GeneratorBase instance used to perform some target-specific actions
        :param coordination: One of CoordinationType.DECENTRALIZED or CoordinationType.CENTRALIZED.
        :param serializer: The serializer used on the connection
        :return:
        """
        factory = LfFactory.eINSTANCE
        sourceRef = factory.createVarRef()
        destRef = factory.createVarRef()
        parent = connection.eContainer()
        networkReceiverReaction = factory.createReaction()
        #  These reactions do not require any dependency relationship
        #  to other reactions in the container.
        generator.makeUnordered(networkReceiverReaction)
        #  If the sender or receiver is in a bank of reactors, then we want
        #  these reactions to appear only in the federate whose bank ID matches.
        generator.setReactionBankIndex(networkReceiverReaction, rightBankIndex)
        #  The connection is 'physical' if it uses the ~> notation.
        if connection.isPhysical():
            destinationFederate.inboundP2PConnections.append(sourceFederate)
        else:
            #  If the connection is logical but coordination
            #  is decentralized, we would need
            #  to make P2P connections
            if coordination == CoordinationType.DECENTRALIZED:
                destinationFederate.inboundP2PConnections.append(sourceFederate)
        #  Record this action in the right federate.
        #  The ID of the receiving port (rightPort) is the position
        #  of the action in this list.
        receivingPortID = len(destinationFederate.networkMessageActions)
        #  Establish references to the involved ports.
        sourceRef.setContainer(source.getParent().getDefinition())
        sourceRef.setVariable(source.getDefinition())
        destRef.setContainer(destination.getParent().getDefinition())
        destRef.setVariable(destination.getDefinition())
        if not connection.isPhysical() and connection.getDelay() == None:
            #  If the connection is not physical and there is no delay,
            #  add the original output port of the source federate
            #  as a trigger to keep the overall dependency structure.
            #  This is useful when assigning levels.
            senderOutputPort = factory.createVarRef()
            senderOutputPort.setContainer(source.getParent().getDefinition())
            senderOutputPort.setVariable(source.getDefinition())
            networkReceiverReaction.getTriggers().append(senderOutputPort)
            #  Add this trigger to the list of disconnected network reaction triggers
            destinationFederate.remoteNetworkReactionTriggers.append(senderOutputPort)
        #  Add the input port at the receiver federate reactor as an effect
        networkReceiverReaction.getEffects().append(destRef)
        triggerRef = factory.createVarRef()
        #  Establish references to the action.
        triggerRef.setVariable(networkAction)
        #  Add the action as a trigger to the receiver reaction
        networkReceiverReaction.getTriggers().append(triggerRef)
        #  Generate code for the network receiver reaction
        networkReceiverReaction.setCode(factory.createCode())
        networkReceiverReaction.getCode().setBody(
            generator.generateNetworkReceiverBody(
                networkAction, sourceRef, destRef,
                receivingPortID, sourceFederate,
                destinationFederate, rightBankIndex,
                rightChannelIndex,
                ASTUtils.getInferredType(networkAction),
                connection.isPhysical(), serializer))
        #  Add the receiver reaction to the parent
        parent.getReactions().append(networkReceiverReaction)
        #  Add the network receiver reaction to the federate instance's list
        #  of network reactions
        destinationFederate.networkReactions.append(networkReceiverReaction)


    @classmethod
    def addNetworkInputControlReaction(cls, source, destination, connection, receivingPortID, bankIndex, instance, generator):
        """
        Add a network control reaction for a given input port 'destination' to
        destination's parent reactor. This reaction will block for
        any valid logical time until it is known whether the trigger for the
        action corresponding to the given port is present or absent.

        @note Used in federated execution

        :param source: The output port of the source federate reactor.
                       Added as a trigger to the network control reaction to preserve the
                       overall dependency structure of the program across federates.
        :param destination: The input port of the destination federate reactor.
        :param connection: The network connection.
        :param receivingPortID: The ID of the receiving port
        :param bankIndex: The bank index of the receiving federate, or -1 if not in a bank.
        :param instance: The federate instance is used to keep track of all
                          network input ports globally
        :param generator: The GeneratorBase instance used to perform some target-specific actions
        :return:
        """
        factory = LfFactory.eINSTANCE
        reaction = factory.createReaction()
        destRef = factory.createVarRef()
        #  If the sender or receiver is in a bank of reactors, then we want
        #  these reactions to appear only in the federate whose bank ID matches.
        generator.setReactionBankIndex(reaction, bankIndex)
        #  Create a new action that will be used to trigger the
        #  input control reactions.
        newTriggerForControlReactionInput = factory.createAction()
        newTriggerForControlReactionInput.setOrigin(ActionOrigin.LOGICAL)
        #  Set the container and variable according to the network port
        destRef.setContainer(destination.getParent().getDefinition())
        destRef.setVariable(destination.getDefinition())
        top = destination.getParent().getParent().reactorDefinition
        newTriggerForControlReactionInput.setName(ASTUtils.getUniqueIdentifier(top, "inputControlReactionTrigger"))
        # Add the newly created Action to the action list of the federated reactor.
        top.getActions().append(newTriggerForControlReactionInput)
        # Create the trigger for the reaction
        newTriggerForControlReaction = factory.createVarRef()
        newTriggerForControlReaction.setVariable(newTriggerForControlReactionInput)
        # Add the appropriate triggers to the list of triggers of the reaction
        reaction.getTriggers().append(newTriggerForControlReaction)
        # Add the original output port of the source federate
        # as a trigger to keep the overall dependency structure.
        # This is useful when assigning levels.

        sourceRef = factory.createVarRef()
        sourceRef.setContainer(source.getParent().getDefinition())
        sourceRef.setVariable(source.getDefinition())
        reaction.getTriggers().append(sourceRef)
        # Add this trigger to the list of disconnected network reaction triggers
        instance.remoteNetworkReactionTriggers.append(sourceRef)
        # Add the destination port as an effect of the reaction
        reaction.getEffects().append(destRef)
        # Generate code for the network input control reaction
        reaction.setCode(factory.createCode())
        maxSTP = cls.findMaxSTP(destination.getDefinition(), instance, generator, destination.getParent().reactorDefinition)
        reaction.getCode().setBody(generator.generateNetworkInputControlReactionBody(receivingPortID, maxSTP))
        generator.makeUnordered(reaction)
        # Insert the reaction
        top.getReactions().append(reaction)
        # Add the trigger for this reaction to the list of triggers, used to actually
        # trigger the reaction at the beginning of each logical time.
        instance.networkInputControlReactionsTriggers.append(newTriggerForControlReactionInput)
        # Add the network input control reaction to the federate instance's list
        # of network reactions
        instance.networkReactions.append(reaction)

    @classmethod
    def findMaxSTP(cls, port, instance, generator, reactor):
        """
        Find the maximum STP offset for the given 'port'.

        An STP offset predicate can be nested in contained reactors in
        the federate.

        :param port: The port to generate the STP list for.
        :param instance:
        :param generator: The GeneratorBase instance used to perform some target-specific actions
        :param reactor: The top-level reactor (not the federate reactor)
        :return: The maximum STP as a TimeValue
        """

        # Find a list of STP offsets (if any exists)
        STPList = []
        #
        # First, check if there are any connections to contained reactors that
        # need to be handled
        connectionsWithPort = [any(reactor)==port]
        # Find the list of reactions that have the port as trigger or source
        # (could be a variable name)
        v = False
        pl = []
        for r in ASTUtils.allReactions(reactor):
            if isinstance(r, VarRef):
                v = r.getVariable() == port
            else:
                v = False
            for s in r.getSources():
                if s.getVariable() == port:
                    pl.append(s)
        reactionsWithPort = False if not v else pl
        #  Find a list of STP offsets (if any exists)
        if generator.isFederatedAndDecentralized():
            for r in reactionsWithPort:
                if r.find(instance)<0:
                    continue
                # If STP offset is determined, add it
                # If not, assume it is zero
                if r.getStp() is not None:
                    if isinstance(r.getStp().getValue(), ParameterReference):
                        instantList = []
                        instantList.append(instance.instantiation)
                        param = r.getStp().getValue().getParameter()
                        STPList.extend(ASTUtils.initialValue(param, instantList))
                    else:
                        STPList.append(r.getStp().getValue())
            # Check the children for STPs as well
            for c in connectionsWithPort:
                childPort = c.getRightPorts().get(0)
                childReactor = childPort.getVariable().eContainer()
                # Find the list of reactions that have the port as trigger or
                # source (could be a variable name)
                v = False
                pl = []
                for r in ASTUtils.allReactions(childReactor):
                    t = r.getTriggers()
                    if isinstance(t, VarRef):
                        # Check if the variables match
                        v = t.getVariable() == childPort.getVariable()
                    else:
                        # Not a network port (startup or shutdown)
                        v = False
                    if r.getVariable() == childPort.getVariable():
                        pl.append(r)
                childReactionsWithPort = False if not v else pl

                for r in childReactionsWithPort:
                    if r.find(instance)<0:
                        continue
                    # If STP offset is determined, add it
                    #If not, assume it is zero
                    if r.getStp() is not None:
                        if isinstance(r.getStp().getValue(), ParameterReference):
                            instantList = []
                            instantList.append(childPort.getContainer())
                            param = r.getStp().getValue().getParameter()
                            STPList.extend(ASTUtils.initialValue(param, instantList))
                        else:
                            STPList.append(r.getStp().getValue())
        sl = []
        for s in STPList:
            if s:
                sl.append(TimeValue.max(ASTUtils.getLiteralTimeValue(s), TimeValue.ZERO))
        return sl

    @classmethod
    def addNetworkSenderReaction(cls, source, destination, connection,
                                 sourceFederate, leftBankIndex,
                                 leftChannelIndex, destinationFederate,
                                 generator, coordination, serializer):
        """
        Add a network sender reaction for a given input port 'source' to
        source's parent reactor. This reaction will react to the 'source'
        and then send a message on the network destined for the destinationFederate.

        @note Used in federated execution

        :param source: The source port instance.
        :param destination: The destination port instance.
        :param connection: The network connection.
        :param sourceFederate: The source federate.
        :param leftBankIndex: The left bank index or -1 if the left reactor is not in a bank.
        :param leftChannelIndex: The left channel index or -1 if the left port is not a multiport.
        :param destinationFederate: The destination federate.
        :param generator: The GeneratorBase instance used to perform some target-specific actions
        :param coordination: One of CoordinationType.DECENTRALIZED or CoordinationType.CENTRALIZED.
        :param serializer: The serializer used on the connection
        :return:
        """
        factory = LfFactory.eINSTANCE
        # // Assume all the types are the same, so just use the first on the right.
        #
        type = EcoreUtil.copy(source.getDefinition().getType())
        sourceRef = factory.createVarRef()
        destRef = factory.createVarRef()
        parent = connection.eContainer()
        # // Configure the sending reaction.
        networkSenderReaction = factory.createReaction()
        # // These reactions do not require any dependency relationship
        #          // to other reactions in the container.
        generator.makeUnordered(networkSenderReaction)
        #          // If the sender or receiver is in a bank of reactors, then we want
        #          // these reactions to appear only in the federate whose bank ID matches.
        generator.setReactionBankIndex(networkSenderReaction, leftBankIndex)
        # // The connection is 'physical' if it uses the ~> notation.
        #
        if connection.isPhysical():
            sourceFederate.outboundP2PConnections.append(destinationFederate)
        else:
            #              // If the connection is logical but coordination
            #              // is decentralized, we would need
            #              // to make P2P connections
            if coordination == CoordinationType.DECENTRALIZED:
                sourceFederate.outboundP2PConnections.append(destinationFederate)
        #          // Record this action in the right federate.
        #          // The ID of the receiving port (rightPort) is the position
        #          // of the action in this list.
        receivingPortID = len(destinationFederate.networkMessageActions)
        #  // Establish references to the involved ports.
        sourceRef.setContainer(source.getParent().getDefinition())
        sourceRef.setVariable(source.getDefinition())
        destRef.setContainer(destination.getParent().getDefinition())
        destRef.setVariable(destination.getDefinition())
        networkSenderReaction.getTriggers().append(sourceRef)
        networkSenderReaction.setCode(factory.createCode())
        networkSenderReaction.getCode().setBody(
            generator.generateNetworkSenderBody(
                sourceRef, destRef, receivingPortID,
                sourceFederate, leftBankIndex,
                leftChannelIndex, destinationFederate,
                InferredType.fromAST(type),
                connection.isPhysical(),
                connection.getDelay(), serializer))
        #  // Add the sending reaction to the parent.
        parent.getReactions().append(networkSenderReaction)
        #          // Add the network sender reaction to the federate instance's list
        #          // of network reactions
        sourceFederate.networkReactions.append(networkSenderReaction)

    @classmethod
    def addNetworkOutputControlReaction(cls, source, instance, receivingPortID, bankIndex, channelIndex, receivingFedID, generator, delay):
        """
        Add a network control reaction for a given output port 'source' to
        source's parent reactor. This reaction will send a port absent
        message if the status of the output port is absent.
        @note Used in federated execution

        :param source: The output port of the source federate
        :param instance: The federate instance is used to keep track of all
                         network reactions and some relevant triggers
        :param receivingPortID: The ID of the receiving port
        :param bankIndex: The bank index of the sending federate, if it is a bank.
        :param channelIndex: The channel index of the sending port, if it is a multiport.
        :param receivingFedID: The ID of destination federate.
        :param generator: The GeneratorBase instance used to perform some target-specific actions
        :param delay: The delay value imposed on the connection using after
        :return:
        """
        factory = LfFactory.eINSTANCE
        reaction = factory.createReaction()
        top = source.getParent().getParent().reactorDefinition
        # If the sender or receiver is in a bank of reactors, then we want
        # these reactions to appear only in the federate whose bank ID matches.
        generator.setReactionBankIndex(reaction, bankIndex)
        # Add the output from the contained reactor as a source to
        #  the reaction to preserve precedence order.
        newPortRef = factory.createVarRef()
        newPortRef.setContainer(source.getParent().getDefinition())
        newPortRef.setVariable(source.getDefinition())
        reaction.getSources().append(newPortRef)
        # We use an action at the top-level to manually
        # trigger output control reactions. That action is created once
        # and recorded in the federate instance.
        # Check whether the action already has been created.

        if instance.networkOutputControlReactionsTrigger == None:
            # Find the trigger definition in the reactor definition, which could have been
            # generated for another federate instance if there are multiple instances
            # of the same reactor that are each distinct federates.
            triggerName = "outputControlReactionTrigger"
            optTriggerInput = None
            for I in top.getActions():
                if I.getName() == triggerName:
                    optTriggerInput = I
            if optTriggerInput is None:
                newTriggerForControlReactionVariable = factory.createAction()
                newTriggerForControlReactionVariable.setName(triggerName)
                newTriggerForControlReactionVariable.setOrigin(ActionOrigin.LOGICAL)
                top.getActions().append(newTriggerForControlReactionVariable)
                instance.networkOutputControlReactionsTrigger = newTriggerForControlReactionVariable
            else:
                instance.networkOutputControlReactionsTrigger = optTriggerInput.get()
        triggerRef = factory.createVarRef()
        triggerRef.setVariable(instance.networkOutputControlReactionsTrigger)
        reaction.getTriggers().append(triggerRef)
        reaction.setCode(factory.createCode())
        reaction.getCode().setBody(generator.generateNetworkOutputControlReactionBody(newPortRef, receivingPortID, receivingFedID, bankIndex, channelIndex, delay))
        generator.makeUnordered(reaction)
        top.getReactions().append(reaction)
        instance.networkReactions.append(reaction)

    @classmethod
    def makeCommunication(cls, source, destination, connection, sourceFederate, leftBankIndex, leftChannelIndex, destinationFederate, rightBankIndex, rightChannelIndex, generator, coordination):
        """ generated source for method makeCommunication """
        serializer = SupportedSerializers.NATIVE
        if connection.getSerializer() != None:
            serializer = SupportedSerializers.valueOf(connection.getSerializer().getType().toUpperCase())
        generator.enabledSerializers.append(serializer)
        cls.addNetworkSenderReaction(source, destination, connection, sourceFederate, leftBankIndex, leftChannelIndex, destinationFederate, generator, coordination, serializer)
        if not connection.isPhysical() and connection.getDelay() == None:
            receivingPortID = len(destinationFederate.networkMessageActions)
            FedASTUtils.addNetworkOutputControlReaction(source, sourceFederate, receivingPortID, leftBankIndex, leftChannelIndex, destinationFederate.id, generator, connection.getDelay())
            FedASTUtils.addNetworkInputControlReaction(source, destination, connection, receivingPortID, rightBankIndex, destinationFederate, generator)
        networkAction = cls.createNetworkAction(connection, serializer, EcoreUtil.copy(source.getDefinition().getType()), generator.getNetworkBufferType())
        destinationFederate.networkMessageActions.append(networkAction)
        (connection.eContainer()).getActions().append(networkAction)
        cls.addNetworkReceiverReaction(networkAction, source, destination, connection, sourceFederate, destinationFederate, rightBankIndex, rightChannelIndex, generator, coordination, serializer)
