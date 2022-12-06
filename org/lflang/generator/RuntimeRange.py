#!/usr/bin/env python
""" generated source for module RuntimeRange """
#  A representation of a range of runtime instances for a NamedInstance. 
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
# import java.util.HashSet
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Set
from include.overloading import overloaded

# 
#  * Class representing a range of runtime instance objects
#  * (port channels, reactors, reactions, etc.). This class and its derived classes
#  * have the most detailed information about the structure of a Lingua Franca
#  * program.  There are three levels of detail:
#  * 
#  * * The abstract syntax tree (AST).
#  * * The compile-time instance graph (CIG).
#  * * The runtime instance graph (RIG).
#  * 
#  * In the AST, each reactor class is represented once.
#  * In the CIG, each reactor class is represented as many times as it is
#  * instantiated, except that a bank has only one representation (as
#  * in the graphical rendition). Equivalently, each CIG node has a unique
#  * full name, even though it may represent many runtime instances.
#  * The CIG is represented by
#  * {@link NamedInstance} and its derived classes.
#  * In the RIG, each bank is expanded so each bank member and
#  * each port channel is represented.
#  * 
#  * In general, determining dependencies between reactions requires analysis
#  * at the level of the RIG.  But a brute-force representation of the RIG
#  * can get very large, and for most programs it has a great deal of
#  * redundancy. In a fully detailed representation of the RIG, for example,
#  * a bank of width N that contains a bank of width M within which there
#  * is a reactor R with port P will have N*M runtime instances of the port.
#  * If the port is a multiport with width L, then there are N*M*L
#  * edges connected to instances of that port, each of which may go
#  * to a distinct set of other remote runtime port instances.
#  * 
#  * This class and its subclasses give a more compact representation of the
#  * RIG in most common cases where collections of runtime instances all have
#  * the same dependencies or dependencies form a range that can be represented
#  * compactly.
#  * 
#  * A RuntimeRange represents an adjacent set of RIG objects (port channels, reactions
#  * reactors). For example, it can represent port channels 2 through 5 in a multiport
#  * of width 10.  The width in this case is 4. If such a port is
#  * contained by one or more banks of reactors, then channels 2 through 5
#  * of one bank member form a contiguous range. If you want channels 2 through 5
#  * of all bank members, then this needs to be represented with multiple ranges.
#  * 
#  * The maxWidth is the width of the instance multiplied by the widths of
#  * each of its containers. For example, if a port of width 4 is contained by
#  * a bank of width 2 that is then contained by a bank of width 3, then
#  * the maxWidth will be 2*3*4 = 24.
#  * 
#  * The function iterationOrder returns a list that includes the instance
#  * of this range and all its containers, except the top-level reactor (main
#  * or federated).  The order of this list is the order in which an
#  * iteration over the RIG objects represented by this range should be
#  * iterated. If the instance is a PortInstance, then this order will
#  * depend on whether connections at any level of the hierarchy are
#  * interleaved.
#  * 
#  * The simplest Ranges are those where the corresponding CIG node represents
#  * only one runtime instance (its instance is not (deeply) within a bank 
#  * and is not a multiport). In this case, the RuntimeRange and all the objects
#  * returned by iterationOrder will have width 1.
#  * 
#  * In a more complex instance, consider a bank A of width 2 that contains a
#  * bank B of width 2 that contains a port instance P with width 2. .
#  * There are a total of 8 instances of P, which we can name:
#  * 
#  *      A0.B0.P0
#  *      A0.B0.P1
#  *      A0.B1.P0
#  *      A0.B1.P1
#  *      A1.B0.P0
#  *      A1.B0.P1
#  *      A1.B1.P0
#  *      A1.B1.P1
#  * 
#  * If there is no interleaving, iterationOrder() returns [P, B, A],
#  * indicating that they should be iterated by incrementing the index of P
#  * first, then the index of B, then the index of A, as done above.
#  * 
#  * If the connection within B to port P is interleaved, then the order
#  * of iteration order will be [B, P, A], resulting in the list:
#  * 
#  *      A0.B0.P0
#  *      A0.B1.P0
#  *      A0.B0.P1
#  *      A0.B1.P1
#  *      A1.B0.P0
#  *      A1.B1.P0
#  *      A1.B0.P1
#  *      A1.B1.P1
#  *      
#  *  If the connection within A to B is also interleaved, then the order
#  *  will be [A, B, P], resulting in the list:
#  *  
#  *      A0.B0.P0
#  *      A1.B0.P0
#  *      A0.B1.P0
#  *      A1.B1.P0
#  *      A0.B0.P1
#  *      A1.B0.P1
#  *      A0.B1.P1
#  *      A1.B1.P1
#  * 
#  * Finally, if the connection within A to B is interleaved, but not the
#  * connection within B to P, then the order will be [A, P, B], resulting in
#  * the list:
#  * 
#  *      A0.B0.P0
#  *      A1.B0.P0
#  *      A0.B0.P1
#  *      A1.B0.P1
#  *      A0.B1.P0
#  *      A1.B1.P0
#  *      A0.B1.P1
#  *      A1.B1.P1
#  * 
#  * A RuntimeRange is a contiguous subset of one of the above lists, given by
#  * a start offset and a width that is less than or equal to maxWidth.
#  * 
#  * Each element of the above lists can be represented as a permuted mixed-radix (PMR) number,
#  * where the low-order digit has radix equal to the width of P, the second digit
#  * has radix equal to the width of B, and the final digit has radix equal to the
#  * width of A. Each PMR has a permutation vector that defines how to increment
#  * PMR number. This permutation vector is derived from the iteration order as
#  * follows.  When there is no interleaving, the iteration order is [P, B, A],
#  * and the permutation vector is [0, 1, 2].  When there is interleaving, the permutation
#  * vector simply specifies the iteration order. For example, if the iteration order
#  * is [A, P, B], then the permutation vector is [2, 0, 1], indicating that digit 2
#  * of the PMR (corresponding to A) should be incremented first, then digit 0 (for P),
#  * then digit 1 (for B).
#  * 
#  * For a RuntimeRange with width greater than 1,
#  * the head() and tail() functions split the range.
#  * 
#  * This class and subclasses are designed to be immutable.
#  * Modifications always return a new RuntimeRange.
#  *
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class RuntimeRange():
    """ generated source for class RuntimeRange """
    #      * Create a new range representing the full width of the specified instance
    #      * with no interleaving. The instances will be a list with the specified instance
    #      * first, its parent next, and on up the hierarchy until the depth 1 parent (the
    #      * top-level reactor is not included because it can never be a bank).
    #      * @param instance The instance.
    #      * @param interleaved A list of parents that are interleaved or null if none.
    #      
    @overloaded
    def __init__(self, instance, interleaved):
        """ generated source for method __init__ """
        super(RuntimeRange, self).__init__()
        self.__init__(instance, 0, 0, interleaved)

    #      * Create a new range representing a range of the specified instance
    #      * with no interleaving. The instances will be a list with the specified instance
    #      * first, its parent next, and on up the hierarchy until the depth 1 parent (the
    #      * top-level reactor is not included because it can never be a bank).
    #      * @param instance The instance over which this is a range (port, reaction, etc.)
    #      * @param start The starting index for the range.
    #      * @param width The width of the range or 0 to specify the maximum possible width.
    #      * @param interleaved A list of parents that are interleaved or null if none.
    #      
    @__init__.register(object, T, int, int, Set)
    def __init___0(self, instance, start, width, interleaved):
        """ generated source for method __init___0 """
        super(RuntimeRange, self).__init__()
        self.instance = instance
        self.start = start
        if interleaved != None:
            self._interleaved.extend(interleaved)
        maxWidth = instance.width
        #  Initial value.
        parent = instance.parent
        while parent.depth > 0:
            maxWidth *= parent.width
            parent = parent.parent
        self.maxWidth = maxWidth
        if width > 0 and width + start < maxWidth:
            self.width = width
        else:
            self.width = maxWidth - start

    # ////////////////////////////////////////////////////////
    # // Public variables
    #  The instance that this is a range of. 
    instance = None

    #  The start offset of this range. 
    start = int()

    #  The maximum width of any range with this instance. 
    maxWidth = int()

    #  The width of this range. 
    width = int()

    # ////////////////////////////////////////////////////////
    # // Public methods
    #      * Compare ranges by first comparing their start offset, and then,
    #      * if these are equal, comparing their widths. This comparison is
    #      * meaningful only for ranges that have the same instances.
    #      * Note that this can return 0 even if equals() does not return true.
    #      
    def compareTo(self, o):
        """ generated source for method compareTo """
        if self.start < o.start:
            return -1
        elif self.start == o.start:
            return Integer.compare(self.width, o.width)
        else:
            return 1

    #      * Return a new RuntimeRange that is identical to this range but
    #      * with width reduced to the specified width.
    #      * If the new width is greater than or equal to the width
    #      * of this range, then return this range.
    #      * If the newWidth is 0 or negative, return null.
    #      * @param newWidth The new width.
    #      
    def head(self, newWidth):
        """ generated source for method head """
        if newWidth >= self.width:
            return self
        if newWidth <= 0:
            return None
        return RuntimeRange(self.instance, self.start, newWidth, _interleaved)

    #      * Return the list of **natural identifiers** for the runtime instances
    #      * in this range.  Each returned identifier is an integer representation
    #      * of the mixed-radix number [d0, ... , dn] with radices [w0, ... , wn],
    #      * where d0 is the bank or channel index of this RuntimeRange's instance, which
    #      * has width w0, and dn is the bank index of its topmost parent below the 
    #      * top-level (main) reactor, which has width wn. The depth of this RuntimeRange's 
    #      * instance, therefore, is n - 1.  The order of the returned list is the order
    #      * in which the runtime instances should be iterated.
    #      
    def instances(self):
        """ generated source for method instances """
        result = ArrayList(self.width)
        mr = startMR()
        count = 0
        __count_0 = count
        count += 1
        while __count_0 < self.width:
            result.append(mr.get())
            mr.increment()
        return result

    #      * Return a list containing the instance for this range and all of its
    #      * parents, not including the top level reactor, in the order in which
    #      * their banks and multiport channels should be iterated.
    #      * For each depth at which the connection is interleaved, that parent
    #      * will appear before this instance in depth order (shallower to deeper).
    #      * For each depth at which the connection is not interleaved, that parent
    #      * will appear after this instance in reverse depth order (deeper to
    #      * shallower).
    #      
    def iterationOrder(self):
        """ generated source for method iterationOrder """
        result = []
        result.append(self.instance)
        parent = self.instance.parent
        while parent.depth > 0:
            if _interleaved.contains(parent):
                #  Put the parent at the head of the list.
                result.append(0, parent)
            else:
                result.append(parent)
            parent = parent.parent
        return result

    #      * Return a range that is the subset of this range that overlaps with the
    #      * specified range or null if there is no overlap.
    #      
    def overlap(self, range):
        """ generated source for method overlap """
        if not overlaps(range):
            return None
        newStart = max(self.start, range.start)
        newEnd = min(self.start + self.width, range.start + range.width)
        return tail(newStart - self.start).head(newEnd - newStart)

    #      * Return true if the specified range has the same instance as this range
    #      * and the ranges overlap.
    #      
    def overlaps(self, range):
        """ generated source for method overlaps """
        if not self.instance == range.instance:
            return False
        return self.start < range.start + range.width and self.start + self.width > range.start

    #      * Return a set of identifiers for runtime instances of a parent of this
    #      * RuntimeRange's instance n levels above this RuntimeRange's instance. If n == 1, for
    #      * example, then this return the identifiers for the parent ReactorInstance.
    #      * 
    #      * This returns a list of **natural identifiers**,
    #      * as defined below, for the instances within the range.
    #      * 
    #      * The resulting list can be used to count the number of distinct
    #      * runtime instances of this RuntimeRange's instance (using n == 0) or any of its parents that
    #      * lie within the range and to provide an index into an array of runtime
    #      * instances.
    #      * 
    #      * Each **natural identifier** is the integer value of a mixed-radix number
    #      * defined as follows:
    #      * 
    #      * * The low-order digit is the index of the runtime instance of i
    #      *   within its container. If the NamedInstance
    #      *   is a PortInstance, this will be the multiport channel or 0 if it is not a
    #      *   multiport. If the NamedInstance is a ReactorInstance, then it will be the bank
    #      *   index or 0 if the reactor is not a bank.  The radix for this digit will be
    #      *   the multiport width or bank width or 1 if the NamedInstance is neither a
    #      *   multiport nor a bank.
    #      *   
    #      * * The next digit will be the bank index of the container of the specified
    #      *   NamedInstance or 0 if it is not a bank.
    #      *   
    #      * * The remaining digits will be bank indices of containers up to but not
    #      *   including the top-level reactor (there is no point in including the top-level
    #      *   reactor because it is never a bank).
    #      *   
    #      * Each index that is returned can be used as an index into an array of
    #      * runtime instances that is assumed to be in a **natural order**.
    #      * 
    #      * @param n The number of levels up of the parent. This is required to be
    #      *  less than the depth of this RuntimeRange's instance or an exception will be thrown.
    #      
    def parentInstances(self, n):
        """ generated source for method parentInstances """
        result = LinkedHashSet(self.width)
        mr = startMR()
        count = 0
        __count_1 = count
        count += 1
        while __count_1 < self.width:
            result.append(mr.get(n))
            mr.increment()
        return result

    #      * Return the nearest containing ReactorInstance for this instance.
    #      * If this instance is a ReactorInstance, then return it.
    #      * Otherwise, return its parent.
    #      
    def parentReactor(self):
        """ generated source for method parentReactor """
        if isinstance(self.instance, (ReactorInstance)):
            return self.instance
        else:
            return self.instance.getParent()

    #      * Return the permutation vector that indicates the order in which the digits
    #      * of the permuted mixed-radix representations of indices in this range should
    #      * be incremented.
    #      
    def permutation(self):
        """ generated source for method permutation """
        result = ArrayList(self.instance.depth)
        #  Populate the result with default zeros.
        i = 0
        while i < self.instance.depth:
            result.append(0)
            i += 1
        count = 0
        for i in iterationOrder():
        __count_2 = count
        count += 1
            result.set(__count_2, self.instance.depth - i.depth)
        return result

    #      * Return the radixes vector containing the width of this instance followed
    #      * by the widths of its containers, not including the top level, which always
    #      * has radix 1 and value 0.
    #      
    def radixes(self):
        """ generated source for method radixes """
        result = ArrayList(self.instance.depth)
        width = self.instance.width
        #  If the width cannot be determined, assume 1.
        if width < 0:
            width = 1
        result.append(width)
        p = self.instance.getParent()
        while p != None and p.getDepth() > 0:
            width = p.getWidth()
            #  If the width cannot be determined, assume 1.
            if width < 0:
                width = 1
            result.append(width)
            p = p.getParent()
        return result

    #      * Return the start as a new permuted mixed-radix number.
    #      * For any instance that is neither a multiport nor a bank, the
    #      * corresponding digit will be 0.
    #      
    def startMR(self):
        """ generated source for method startMR """
        result = MixedRadixInt(None, self.radixes(), self.permutation())
        result.setMagnitude(self.start)
        return result

    #      * Return a new range that represents the leftover elements
    #      * starting at the specified offset relative to start.
    #      * If start + offset is greater than or equal to the width, then this returns null.
    #      * If this offset is 0 then this returns this range unmodified.
    #      * @param offset The number of elements to consume. 
    #      
    def tail(self, offset):
        """ generated source for method tail """
        if offset == 0:
            return self
        if offset >= self.width:
            return None
        return RuntimeRange(self.instance, self.start + offset, self.width - offset, _interleaved)

    #      * Toggle the interleaved status of the specified reactor, which is assumed
    #      * to be a parent of the instance of this range.
    #      * If it was previously interleaved, make it not interleaved
    #      * @param reactor The parent reactor at which to toggle interleaving.
    #      
    def toggleInterleaved(self, reactor):
        """ generated source for method toggleInterleaved """
        newInterleaved = HashSet(_interleaved)
        if _interleaved.contains(reactor):
            newInterleaved.remove(reactor)
        else:
            newInterleaved.append(reactor)
        return RuntimeRange(self.instance, self.start, self.width, newInterleaved)

    def __str__(self):
        """ generated source for method toString """
        return self.instance.getFullName() + "(" + self.start + "," + self.width + ")"

    # ////////////////////////////////////////////////////////
    # // Protected variables
    #  Record of which levels are interleaved. 
    _interleaved = set()

    # ////////////////////////////////////////////////////////
    # // Public inner classes
    #      * Special case of RuntimeRange for PortInstance.
    #      
    class Port(RuntimeRange):
        """ generated source for class Port """
        @overloaded
        def __init__(self, instance):
            """ generated source for method __init__ """
            super(Port, self).__init__(None)

        @__init__.register(object, PortInstance, Set)
        def __init___0(self, instance, interleaved):
            """ generated source for method __init___0 """
            super(Port, self).__init__(interleaved)

        @__init__.register(object, PortInstance, int, int, Set)
        def __init___1(self, instance, start, width, interleaved):
            """ generated source for method __init___1 """
            super(Port, self).__init__(interleaved)

RuntimeRange.#      * and vice versa.  This returns a new RuntimeRange.
