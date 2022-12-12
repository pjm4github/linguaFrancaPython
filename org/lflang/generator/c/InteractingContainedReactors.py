#!/usr/bin/env python
""" generated source for module InteractingContainedReactors """
# package: org.lflang.generator.c
# import java.util.LinkedHashMap
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Set

#  * Helper class to handle code generation of contained reactors.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#
from lflang import ASTUtils


class InteractingContainedReactors:
    """ generated source for class InteractingContainedReactors """
    #      * Data structure that for each instantiation of a contained
    #      * reactor. This provides a set of input and output ports that trigger
    #      * reactions of the container, are read by a reaction of the
    #      * container, or that receive data from a reaction of the container.
    #      * For each port, this provides a list of reaction indices that
    #      * are triggered by the port, or an empty list if there are no
    #      * reactions triggered by the port.
    #      
    #  This horrible data structure is a collection, indexed by instantiation
    #  of a contained reactor, of lists, indexed by ports of the contained reactor
    #  that are referenced by reactions of the container, of reactions that are
    #  triggered by the port of the contained reactor. The list is empty if
    #  the port does not trigger reactions but is read by the reaction or
    #  is written to by the reaction.
    portsByContainedReactor = {}

    #      * Scan the reactions of the specified reactor and record which ports are
    #      * referenced by reactions and which reactions are triggered by such ports.
    #      
    def __init__(self, reactor, federate):
        """ generated source for method __init__ """
        reactionCount = 0
        for reaction in ASTUtils.allReactions(reactor):
            if federate == None or federate.contains(reaction):
                #  First, handle reactions that produce data sent to inputs
                #  of contained reactors.
                for effect in ASTUtils.convertToEmptyListIfNull(reaction.getEffects()):
                    #  If an effect is an input, then it must be an input
                    #  of a contained reactor.
                    if isinstance(, (Input)):
                        #  This reaction is not triggered by the port, so
                        #  we do not add it to the list returned by the following.
                        addPort(effect.getContainer(), effect.getVariable())
                #  Second, handle reactions that are triggered by outputs
                #  of contained reactors.
                for trigger in ASTUtils.convertToEmptyListIfNull(reaction.getTriggers()):
                    if isinstance(trigger, (VarRef)):
                        #  triggerAsVarRef) {
                        #  If an trigger is an output, then it must be an output
                        #  of a contained reactor.
                        if isinstance(, (Output)):
                            list = addPort(triggerAsVarRef.getContainer(), triggerAsVarRef.getVariable())
                            list.append(reactionCount)
                #  Third, handle reading (but not triggered by)
                #  outputs of contained reactors.
                for source in ASTUtils.convertToEmptyListIfNull(reaction.getSources()):
                    if isinstance(, (Output)):
                        #  If an source is an output, then it must be an output
                        #  of a contained reactor.
                        #  This reaction is not triggered by the port, so
                        #  we do not add it to the list returned by the following.
                        addPort(source.getContainer(), source.getVariable())
            #  Increment the reaction count even if not in the federate for consistency.
            reactionCount += 1

    # Return or create the list to which reactions triggered by the specified port
    # are to be added. This also records that the port is referenced by the
    # container's reactions.
    # @param containedReactor The contained reactor.
    # @param port The port.
    #       
    def addPort(self, containedReactor, port):
        """ generated source for method addPort """
        #  Get or create the entry for the containedReactor.
        containedReactorEntry = None
        #          portsByContainedReactor.computeIfAbsent(
        #              containedReactor,
        #              k -> new {}
        #          );
        #  Get or create the entry for the port.
        return None
        # containedReactorEntry.computeIfAbsent(port, k -> new LinkedList());

    # Return the set of contained reactors that have ports that are referenced
    # by reactions of the container reactor.
    #       
    def containedReactors(self):
        """ generated source for method containedReactors """
        return self.portsByContainedReactor.keySet()

    # Return the set of ports of the specified contained reactor that are
    # referenced by reactions of the container reactor. Return an empty
    # set if there are none.
    # @param containedReactor The contained reactor.
    #       
    def portsOfInstance(self, containedReactor):
        """ generated source for method portsOfInstance """
        result = None
        ports = self.portsByContainedReactor.get(containedReactor)
        if ports == None:
            result = {}
        else:
            result = ports.keySet()
        return result

    # Return the indices of the reactions triggered by the specified port
    # of the specified contained reactor or an empty list if there are none.
    # @param containedReactor The contained reactor.
    # @param port The port.
    #       
    def reactionsTriggered(self, containedReactor, port):
        """ generated source for method reactionsTriggered """
        ports = self.portsByContainedReactor.get(containedReactor)
        if ports != None:
            list = ports.get(port)
            if list != None:
                return list
        return LinkedList()
