#!/usr/bin/env python
""" generated source for module PortInstance """
#  A data structure for a port instance. 
# 
# Copyright (c) 2019-2022, The University of California at Berkeley.
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
# package: org.lflang.generator
# import java.util.ArrayList
# import java.util.Iterator
# import java.util.List
# import java.util.PriorityQueue
from include.overloading import overloaded
from org.lflang import ErrorReporter
from org.lflang.lf import Input
from org.lflang.lf import Output
from org.lflang.lf import Parameter
from org.lflang.lf import Port
from org.lflang.lf import WidthSpec
from org.lflang.lf import WidthTerm

#  
#  * Representation of a compile-time instance of a port.
#  * Like {@link ReactorInstance}, if one or more parents of this port
#  * is a bank of reactors, then there will be more than one runtime instance
#  * corresponding to this compile-time instance.
#  * 
#  * This may be a single port or a multiport. If it is a multiport, then
#  * one instance of this PortInstance class represents all channels.
#  * If in addition any parent is a bank, then it represents all channels of all
#  * bank members. The {@link #eventualDestinations()} and {@link #eventualSources()}
#  * functions report the connectivity of all such channels as lists of
#  * {@link SendRange} and {@link RuntimeRange} objects.
#  *  
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class PortInstance(TriggerInstance, Port):
    """ generated source for class PortInstance """
    #      * Create a runtime instance from the specified definition
    #      * and with the specified parent that instantiated it.
    #      * @param definition The declaration in the AST.
    #      * @param parent The parent.
    #      
    @overloaded
    def __init__(self, definition, parent):
        """ generated source for method __init__ """
        super().__init__()
        self.__init__(definition, parent, None)

    #      * Create a port instance from the specified definition
    #      * and with the specified parent that instantiated it.
    #      * @param definition The declaration in the AST.
    #      * @param parent The parent.
    #      * @param errorReporter An error reporter, or null to throw exceptions.
    #      
    @__init__.register(object, Port, ReactorInstance, ErrorReporter)
    def __init___0(self, definition, parent, errorReporter):
        """ generated source for method __init___0 """
        super().__init__(parent)
        if parent == None:
            raise NullPointerException("Cannot create a PortInstance with no parent.")
        setInitialWidth(errorReporter)

    # ////////////////////////////////////////////////////
    # // Public methods
    #      * Clear cached information about the connectivity of this port.
    #      * In particular, {@link #eventualDestinations()} and {@link #eventualSources()}
    #      * cache the lists they return. To force those methods to recompute
    #      * their lists, call this method. This method also clears the caches
    #      * of any ports that are listed as eventual destinations and sources.
    #      
    def clearCaches(self):
        """ generated source for method clearCaches """
        if clearingCaches:
            return
        #  Prevent stack overflow.
        clearingCaches = True
        try:
            if eventualSourceRanges != None:
                for sourceRange in eventualSourceRanges:
                    sourceRange.instance.clearCaches()
            if eventualDestinationRanges != None:
                for sendRange in eventualDestinationRanges:
                    for destinationRange in sendRange.destinations:
                        destinationRange.instance.clearCaches()
            eventualDestinationRanges = None
            eventualSourceRanges = None
        finally:
            clearingCaches = False

    #      * Return a list of ranges of this port, where each range sends
    #      * to a list of destination ports that receive data from the range of
    #      * this port. Each destination port is annotated with the channel
    #      * range on which it receives data.
    #      * The ports listed are only ports that are sources for reactions,
    #      * not relay ports that the data may go through on the way.
    #      * Also, if there is an "after" delay anywhere along the path,
    #      * then the destination is not in the resulting list.
    #      * 
    #      * If this port itself has dependent reactions,
    #      * then this port will be included as a destination in all items
    #      * on the returned list.
    #      * 
    #      * Each item in the returned list has the following fields:
    #      * * startRange The starting channel index of this port.
    #      * * rangeWidth The number of channels sent to the destinations.
    #      * * destinations A list of port ranges for destination ports, each
    #      *   of which has the same width as rangeWidth.
    #      *   
    #      * Each item also has a method, getNumberOfDestinationReactors(),
    #      * that returns the total number of unique destination reactors for
    #      * its range. This is not necessarily the same as the number
    #      * of ports in its destinations field because some of the ports may 
    #      * share the same container reactor.
    #      
    @overloaded
    def eventualDestinations(self):
        """ generated source for method eventualDestinations """
        if eventualDestinationRanges != None:
            return eventualDestinationRanges
        #  Construct the full range for this port.
        range = RuntimeRange.Port(self)
        eventualDestinationRanges = self.eventualDestinations(range)
        return eventualDestinationRanges

    #      * Return a list of ranges of ports that send data to this port.
    #      * If this port is directly written to by one more more reactions,
    #      * then it is its own eventual source and only this port
    #      * will be represented in the result.
    #      * 
    #      * If this is not a multiport and is not within a bank, then the list will have
    #      * only one item and the range will have a total width of one. Otherwise, it will
    #      * have enough items so that the range widths add up to the width of this
    #      * multiport multiplied by the total number of instances within containing banks.
    #      * 
    #      * The ports listed are only ports that are written to by reactions,
    #      * not relay ports that the data may go through on the way.
    #      
    @overloaded
    def eventualSources(self):
        """ generated source for method eventualSources """
        return self.eventualSources(RuntimeRange.Port(self))

    #  
    #      * Return the list of ranges of this port together with the
    #      * downstream ports that are connected to this port.
    #      * The total with of the ranges in the returned list is a
    #      * multiple N >= 0 of the total width of this port.
    #      
    def getDependentPorts(self):
        """ generated source for method getDependentPorts """
        return dependentPorts

    #  
    #      * Return the list of upstream ports that are connected to this port,
    #      * or an empty set if there are none.
    #      * For an ordinary port, this list will have length 0 or 1.
    #      * For a multiport, it can have a larger size.
    #      
    def getDependsOnPorts(self):
        """ generated source for method getDependsOnPorts """
        return dependsOnPorts

    #  
    #      * Return true if the port is an input.
    #      
    def isInput(self):
        """ generated source for method isInput """
        return (isinstance(definition, (Input)))

    #      * Return true if this is a multiport.
    #      
    def isMultiport(self):
        """ generated source for method isMultiport """
        return self.isMultiport

    #  
    #      * Return true if the port is an output.
    #      
    def isOutput(self):
        """ generated source for method isOutput """
        return (isinstance(definition, (Output)))

    def __str__(self):
        """ generated source for method toString """
        return "PortInstance " + getFullName()

    # ////////////////////////////////////////////////////
    # // Protected fields.
    #  
    #      * Ranges of this port together with downstream ports that
    #      * are connected directly to this port. When there are multiple destinations,
    #      * the destinations are listed in the order they appear in connections
    #      * in the parent reactor instance of this port (inside connections),
    #      * followed by the order in which they appear in the parent's parent (outside
    #      * connections). The total of the widths of these SendRanges is an integer
    #      * multiple N >= 0 of the width of this port (this is checked
    #      * by the validator). Each channel of this port will be broadcast
    #      * to N recipients (or, if there are no connections to zero recipients).
    #      
    dependentPorts = []

    #  
    #      * Upstream ports that are connected directly to this port, if there are any.
    #      * For an ordinary port, this set will have size 0 or 1.
    #      * For a multiport, it can have a larger size.
    #      * This initially has capacity 1 because that is by far the most common case.
    #      
    dependsOnPorts = ArrayList(1)

    #  Indicator of whether this is a multiport. 
    isMultiport = False

    # ////////////////////////////////////////////////////
    # // Private methods.
    #      * Given a RuntimeRange, return a list of SendRange that describes
    #      * the eventual destinations of the given range.
    #      * The sum of the total widths of the send ranges on the returned list
    #      * will be an integer multiple N of the total width of the specified range.
    #      * Each returned SendRange has a list
    #      * of destination RuntimeRanges, each of which represents a port that
    #      * has dependent reactions. Intermediate ports with no dependent
    #      * reactions are not listed.
    #      * @param srcRange The source range.
    #      
    @classmethod
    @eventualDestinations.register(object, RuntimeRange)
    def eventualDestinations_0(cls, srcRange):
        """ generated source for method eventualDestinations_0 """
        #  Getting the destinations is more complex than getting the sources
        #  because of multicast, where there is more than one connection statement
        #  for a source of data. The strategy we follow here is to first get all
        #  the ports that this port eventually sends to. Then, if needed, split
        #  the resulting ranges so that the resulting list covers exactly
        #  srcRange, possibly in pieces.  We make two passes. First, we build
        #  a queue of ranges that may overlap, then we split those ranges
        #  and consolidate their destinations.
        result = []
        queue = PriorityQueue()
        srcPort = srcRange.instance
        #  Start with, if this port has dependent reactions, then add it to 
        #  every range of the result.
        if not srcRange.instance.dependentReactions.isEmpty():
            #  This will be the final result if there are no connections.
            candidate = SendRange(srcRange.instance, srcRange.start, srcRange.width, None, None)
            candidate.destinations.append(srcRange)
            queue.append(candidate)
        #  Need to find send ranges that overlap with this srcRange.
        sendRanges = srcPort.dependentPorts.iterator()
        while sendRanges.hasNext():
            wSendRange = sendRanges.next()
            if wSendRange.connection != None and wSendRange.connection.getDelay() != None:
                continue 
            wSendRange = wSendRange.overlap(srcRange)
            if wSendRange == None:
                #  This send range does not overlap with the desired range. Try the next one.
                continue 
            for dstRange in wSendRange.destinations:
                #  Recursively get the send ranges of that destination port.
                dstSendRanges = cls.eventualDestinations(dstRange)
                sendRangeStart = 0
                for dstSend in dstSendRanges:
                    queue.append(dstSend.newSendRange(wSendRange, sendRangeStart))
                    sendRangeStart += dstSend.width
        #  Now check for overlapping ranges, constructing a new result.
        candidate = queue.poll()
        next = queue.poll()
        while candidate != None:
            if next == None:
                #  No more candidates.  We are done.
                result.append(candidate)
                break
            if candidate.start == next.start:
                #  Ranges have the same starting point. Need to merge them.
                if candidate.width <= next.width:
                    #  Can use all of the channels of candidate.
                    #  Import the destinations of next and split it.
                    for destination in next.destinations:
                        candidate.destinations.append(destination.head(candidate.width))
                    if candidate.width < next.width:
                        #  The next range has more channels connected to this sender.
                        #  Put it back on the queue an poll for a new next.
                        queue.append(next.tail(candidate.width))
                        next = queue.poll()
                    else:
                        #  We are done with next and can discard it.
                        next = queue.poll()
                else:
                    #  candidate is wider than next. Switch them and continue.
                    temp = candidate
                    candidate = next
                    next = temp
            else:
                #  Because the result list is sorted, next starts at
                #  a higher channel than candidate.
                if candidate.start + candidate.width <= next.start:
                    #  Can use candidate as is and make next the new candidate.
                    result.append(candidate)
                    candidate = next
                    next = queue.poll()
                else:
                    #  Ranges overlap. Can use a truncated candidate and make its
                    #  truncated version the new candidate.
                    result.append(candidate.head(next.start))
                    candidate = candidate.tail(next.start)
        return result

    #      * Return a list of ranges of ports that send data to this port within the
    #      * specified range. If this port is directly written to by one more more reactions,
    #      * then it is its own eventual source and only this port
    #      * will be represented in the result.
    #      * 
    #      * If this is not a multiport and is not within a bank, then the list will have
    #      * only one item and the range will have a total width of one. Otherwise, it will
    #      * have enough items so that the range widths add up to the width of this
    #      * multiport multiplied by the total number of instances within containing banks.
    #      * 
    #      * The ports listed are only ports that are written to by reactions,
    #      * not relay ports that the data may go through on the way.
    #      
    @eventualSources.register(object, RuntimeRange)
    def eventualSources_0(self, range):
        """ generated source for method eventualSources_0 """
        if eventualSourceRanges == None:
            #  Cached result has not been created.
            eventualSourceRanges = []
            if not dependsOnReactions.isEmpty():
                eventualSourceRanges.append(RuntimeRange.Port(self))
            else:
                channelsCovered = 0
                for sourceRange in dependsOnPorts:
                    #  Check whether the sourceRange overlaps with the range.
                    if channelsCovered + sourceRange.width >= range.start and channelsCovered < range.start + range.width:
                        eventualSourceRanges.extend(sourceRange.instance.eventualSources(sourceRange))
                    channelsCovered += sourceRange.width
        return eventualSourceRanges

    #      * Set the initial multiport width, if this is a multiport, from the widthSpec
    #      * in the definition. This will be set to -1 if the width cannot be determined.
    #      * @param errorReporter For reporting errors.
    #      
    def setInitialWidth(self, errorReporter):
        """ generated source for method setInitialWidth """
        #  If this is a multiport, determine the width.
        widthSpec = definition.getWidthSpec()
        if widthSpec != None:
            if widthSpec.isOfVariableLength():
                errorReporter.reportError(definition, "Variable-width multiports not supported (yet): " + definition.__name__)
            else:
                self.isMultiport = True
                #  Determine the initial width, if possible.
                #  The width may be given by a parameter or even sum of parameters.
                width = 0
                for term in widthSpec.getTerms():
                    parameter = term.getParameter()
                    if parameter != None:
                        parameterValue = parent.initialIntParameterValue(parameter)
                        #  Only a Literal is supported.
                        if parameterValue != None:
                            width += parameterValue
                        else:
                            width = -1
                            return
                    elif term.getWidth() != 0:
                        width += term.getWidth()
                    else:
                        width = -1
                        return

    # ////////////////////////////////////////////////////
    # // Private fields.
    #  Cached list of destination ports with channel ranges. 
    eventualDestinationRanges = None

    #  Cached list of source ports with channel ranges. 
    eventualSourceRanges = None

    #  Indicator that we are clearing the caches. 
    clearingCaches = False
