#!/usr/bin/env python
""" generated source for module SendRange """
#  Abstract class for ranges of NamedInstance. 
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
# package: org.lflang.generator
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Map
# import java.util.Set
from include.overloading import overloaded

from org.lflang.lf import Connection

# 
#  * Class representing a range of a port that sources data
#  * together with a list of destination ranges of other ports that should all
#  * receive the same data sent in this range.
#  * All ranges in the destinations list have widths that are an integer
#  * multiple N of this range but not necessarily the same start offsets.
#  * 
#  * This class and subclasses are designed to be immutable.
#  * Modifications always return a new RuntimeRange.
#  *
#  * @author{Edward A. Lee <eal@berkeley.edu>}
# 
class SendRange(RuntimeRange, Port):
    """ generated source for class SendRange """
    #      * Create a new send range.
    #      * @param instance The instance over which this is a range of.
    #      * @param start The starting index.
    #      * @param width The width.
    #      * @param interleaved A list of parents that are interleaved or null if none.
    #      * @param connection The connection that establishes this send or null if not unique or none.
    #      
    @overloaded
    def __init__(self, instance, start, width, interleaved, connection):
        """ generated source for method __init__ """
        super().__init__(interleaved)
        self.connection = connection

    #      * Create a new send range representing sending from the specified
    #      * src to the specified dst.  This preserves the interleaved status
    #      * of both the src and dst.
    #      * @param src The source range.
    #      * @param dst The destination range.
    #      * @param interleaved A list of parents that are interleaved or null if none.
    #      * @param connection The connection that establishes this send or null if not unique or none.
    #      
    @__init__.register(object, RuntimeRange, RuntimeRange, Set, Connection)
    def __init___0(self, src, dst, interleaved, connection):
        """ generated source for method __init___0 """
        super().__init__(interleaved)
        destinations.append(dst)
        _interleaved.extend(src._interleaved)
        self.connection = connection

    # ////////////////////////////////////////////////////////
    # // Public variables
    #  The connection that establishes this relationship or null if not unique or none. 
    connection = None

    #  The list of destination ranges to which this broadcasts. 
    destinations = []

    # ////////////////////////////////////////////////////////
    # // Public methods
    #      * Add a destination to the list of destinations of this range.
    #      * If the width of the destination is not a multiple of the width
    #      * of this range, throw an exception.
    #      * @throws IllegalArgumentException If the width doesn't match.
    #      
    def addDestination(self, dst):
        """ generated source for method addDestination """
        if dst.width % width != 0:
            raise IllegalArgumentException("Destination range width is not a multiple of sender's width")
        self.destinations.append(dst)
        #  Void any precomputed number of destinations.
        _numberOfDestinationReactors = -1

    #      * Override the base class to add additional comparisons so that
    #      * ordering is never ambiguous. This means that sorting will be deterministic.
    #      * Note that this can return 0 even if equals() does not return true.
    #      
    def compareTo(self, o):
        """ generated source for method compareTo """
        result = super().compareTo(o)
        if result == 0:
            #  Longer destination lists come first.
            if len(self.destinations) > (o)len(.destinations):
                return -1
            elif len(self.destinations) == (o)len(.destinations):
                return instance.getFullName().compareTo(o.instance.getFullName())
            else:
                return 1
        return result

    #      * Return the total number of destination reactors for this range.
    #      * Specifically, this is the number of distinct runtime reactor instances
    #      * that react to messages from this send range.
    #      
    def getNumberOfDestinationReactors(self):
        """ generated source for method getNumberOfDestinationReactors """
        if _numberOfDestinationReactors < 0:
            #  Has not been calculated before. Calculate now.
            _numberOfDestinationReactors = 0
            result = dict()
            for destination in self.destinations:
                #  The following set contains unique identifiers the parent reactors
                #  of destination ports.
                parentIDs = destination.parentInstances(1)
                previousParentIDs = result.get(destination.instance.parent)
                if previousParentIDs == None:
                    result.put(destination.instance.parent, parentIDs)
                else:
                    previousParentIDs.extend(parentIDs)
            for parent in result.keySet():
                _numberOfDestinationReactors += result.get(parent).size()
        return _numberOfDestinationReactors

    #      * Return a new SendRange that is identical to this range but
    #      * with width reduced to the specified width.
    #      * If the new width is greater than or equal to the width
    #      * of this range, then return this range.
    #      * If the newWidth is 0 or negative, return null.
    #      * This overrides the base class to also apply head()
    #      * to the destination list.
    #      * @param newWidth The new width.
    #      
    def head(self, newWidth):
        """ generated source for method head """
        #  NOTE: Cannot use the superclass because it returns a RuntimeRange, not a SendRange.
        #  Also, cannot return this without applying head() to the destinations.
        if newWidth <= 0:
            return None
        result = SendRange(instance, start, newWidth, _interleaved, self.connection)
        for destination in destinations:
            result.destinations.append(destination.head(newWidth))
        return result

    #      * Return a range that is the subset of this range that overlaps with the
    #      * specified range or null if there is no overlap.
    #      
    def overlap(self, range):
        """ generated source for method overlap """
        if not overlaps(range):
            return None
        if range.start == start and range.width == width:
            return self
        newStart = max(start, range.start)
        newEnd = min(start + width, range.start + range.width)
        newWidth = newEnd - newStart
        result = SendRange(instance, newStart, newWidth, _interleaved, self.connection)
        result._interleaved.extend(_interleaved)
        for destination in destinations:
            #  The destination width is a multiple of this range's width.
            #  If the multiple is greater than 1, then the destination needs to
            #  split into multiple destinations.
            while destination != None:
                dstStart = destination.start + (newStart - start)
                dst = RuntimeRange.Port(destination.instance, dstStart, newWidth, destination._interleaved)
                result.addDestination(dst)
                destination = destination.tail(width)
        return result

    #      * Return a new SendRange that represents the leftover elements
    #      * starting at the specified offset. If the offset is greater
    #      * than or equal to the width, then this returns null.
    #      * If this offset is 0 then this returns this range unmodified.
    #      * This overrides the base class to also apply tail()
    #      * to the destination list.
    #      * @param offset The number of elements to consume. 
    #      
    def tail(self, offset):
        """ generated source for method tail """
        #  NOTE: Cannot use the superclass because it returns a RuntimeRange, not a SendRange.
        #  Also, cannot return this without applying tail() to the destinations.
        if offset >= width:
            return None
        result = SendRange(instance, start + offset, width - offset, _interleaved, self.connection)
        for destination in destinations:
            result.destinations.append(destination.tail(offset))
        return result

    def __str__(self):
        """ generated source for method toString """
        result = ""
        result.append(super().__str__())
        result.append("->[")
        dsts = LinkedList()
        for dst in destinations:
            dsts.append(dst.__str__())
        result.append(", ".join( dsts))
        result.append("]")
        return str(result)

    # ////////////////////////////////////////////////////////
    # // Protected methods
    #      * Assuming that this SendRange is completely contained by one
    #      * of the destinations of the specified srcRange, return a new SendRange
    #      * where the send range is the subrange of the specified srcRange that
    #      * overlaps with this SendRange and the destinations include all the
    #      * throw an IllegalArgumentException.
    #      * 
    #      * If any parent of this range is marked interleaved and is also a parent of the
    #      * specified srcRange, then that parent will be marked interleaved
    #      * in the result.
    #      * 
    #      * @param srcRange A new source range.
    #      * @param srcRangeOffset An offset into the source range.
    #      
    def newSendRange(self, srcRange, srcRangeOffset):
        """ generated source for method newSendRange """
        #  Every destination of srcRange receives all channels of srcRange (multicast).
        #  Find which multicast destination overlaps with this srcRange.
        for srcDestination in srcRange.destinations:
            overlap = srcDestination.overlap(self)
            if self.overlap == None:
                continue 
            #  Not this one.
            if self.overlap.width == width:
                #  Found an overlap that is completely contained.
                #  If this width is greater than the srcRange width,
                #  then assume srcRange is multicasting via this.
                newWidth = min(width, srcRange.width)
                #  The interleaving of the result is the union of the two interleavings.
                interleaving = {}
                interleaving.extend(_interleaved)
                interleaving.extend(srcRange._interleaved)
                result = SendRange(srcRange.instance, srcRange.start + srcRangeOffset, newWidth, interleaving, self.connection)
                for dst in destinations:
                    result.addDestination(dst)
                return result
        raise IllegalArgumentException("Expected this SendRange " + self + " to be completely contained by a destination of " + srcRange)

    # ////////////////////////////////////////////////////////
    # // Private variables
    _numberOfDestinationReactors = -1

    #  Never access this directly.

SendRange.#      * destinations of this SendRange. If the assumption is not satisfied,
