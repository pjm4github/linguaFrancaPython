#!/usr/bin/env python
""" generated source for module MixedRadixInt """
#  A representation for a mixed radix number. 
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
# import java.util.Iterator
# import java.util.LinkedList
# import java.util.List
# import java.util.Set
from include.overloading import overloaded
# 
#  * Representation of a permuted mixed radix (PMR) integer.
#  * A mixed radix number is a number representation where each digit can have
#  * a distinct radix. The radixes are given by a list of numbers, r0, r1, ... , rn,
#  * where r0 is the radix of the lowest-order digit and rn is the radix of the
#  * highest order digit that has a specified radix.
#  *
#  * A PMR is a mixed radix number that, when incremented,
#  * increments the digits in the order given by the permutation matrix.
#  * For an ordinary mixed radix number, the permutation matrix is
#  * [0, 1, ..., n-1]. The permutation matrix may be any permutation of
#  * these digits, [d0, d1, ..., dn-1], in which case, when incremented,
#  * the d0 digit will be incremented first. If it overflows, it will be
#  * set to 0 and the d1 digit will be incremented. If it overflows, the
#  * next digit is incremented.  If the last digit overflows, then the
#  * number wraps around so that all digits become zero.
#  * 
#  * This implementation realizes a finite set of numbers, where incrementing
#  * past the end of the range wraps around to the beginning. As a consequence,
#  * the increment() function from any starting point is guaranteed to eventually
#  * cover all possible values.
#  * 
#  * The {@link #toString()} method gives a string representation of the number
#  * where each digit is represented by the string "d%r", where d is the digit
#  * and r is the radix. For example, the number "1%2, 2%3, 1%4" has value 11,
#  * 1 + (2*2) + (1*2*3).
#  * 
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class MixedRadixInt(object):
    """ generated source for class MixedRadixInt """
    #      * Create a mixed radix number with the specified digits and radixes,
    #      * which are given low-order digits first.
    #      * If there is one more digit than radixes, throw an exception.
    #      * @param digits The digits, or null to get a zero-valued number.
    #      * @param radixes The radixes.
    #      * @param permutation The permutation matrix, or null for the default permutation.
    #      
    def __init__(self, digits, radixes, permutation):
        """ generated source for method __init__ """
        if radixes == None or (digits != None and len(digits) > len(radixes)) or (permutation != None and len(permutation) != len(radixes)) or radixes.contains(0):
            raise IllegalArgumentException("Invalid constructor arguments.")
        self.radixes = radixes
        if digits != None:
            self.digits = digits
        else:
            self.digits = ArrayList(1)
            self.digits.append(0)
        if permutation != None:
            #  Check the permutation matrix.
            indices = set()
            for p in permutation:
                if p < 0 or p >= len(radixes) or indices.contains(p):
                    raise IllegalArgumentException("Permutation list is required to be a permutation of [0, 1, ... , n-1].")
                indices.append(p)
            self.permutation = permutation

    #      * A zero-valued mixed radix number with just one digit will radix 1.
    #      
    ZERO = MixedRadixInt(None, list(1), None)

    # ////////////////////////////////////////////////////////
    # // Public methods
    #      * Get the value as an integer.
    #      
    @overloaded
    def get(self):
        """ generated source for method get """
        return self.get(0)

    #      * Get the value as an integer after dropping the first n digits.
    #      * @param n The number of digits to drop.
    #      
    @get.register(object, int)
    def get_0(self, n):
        """ generated source for method get_0 """
        result = 0
        scale = 1
        if n < 0:
            n = 0
        i = n
        while i < len(radixes):
            if i >= len(digits):
                return result
            result += digits.get(i) * scale
            scale *= radixes.get(i)
            i += 1
        return result

    #      * Return the digits. This is assured of returning as many
    #      * digits as there are radixes.
    #      
    def getDigits(self):
        """ generated source for method getDigits """
        while len(digits) < len(radixes):
            digits.append(0)
        return digits

    #      * Return the permutation list.
    #      
    def getPermutation(self):
        """ generated source for method getPermutation """
        if permutation == None:
            #  Construct a default permutation.
            permutation = ArrayList(len(radixes))
            i = 0
            while i < len(radixes):
                permutation.append(i)
                i += 1
        return permutation

    #      * Return the radixes.
    #      
    def getRadixes(self):
        """ generated source for method getRadixes """
        return radixes

    #      * Increment the number by one, using the permutation vector to
    #      * determine the order in which the digits are incremented.
    #      * If an overflow occurs, then a radix-infinity digit will be added
    #      * to the digits array if there isn't one there already.
    #      
    def increment(self):
        """ generated source for method increment """
        i = 0
        while i < len(radixes):
            digit_to_increment = self.getPermutation().get(i)
            while digit_to_increment >= len(digits):
                digits.append(0)
            digits.set(digit_to_increment, digits.get(digit_to_increment) + 1)
            if digits.get(digit_to_increment) >= radixes.get(digit_to_increment):
                digits.set(digit_to_increment, 0)
                i += 1
            else:
                return
                #  All done.

    #      * Return the magnitude of this PMR, which is defined to be the number
    #      * of times that increment() would need to invoked starting with zero
    #      * before the value returned by {@link #get()} would be reached.
    #      
    def magnitude(self):
        """ generated source for method magnitude """
        factor = 1
        result = 0
        p = self.getPermutation()
        i = 0
        while i < len(radixes):
            if len(digits) <= i:
                return result
            result += factor * digits.get(p.get(i))
            factor *= radixes.get(p.get(i))
            i += 1
        return result

    #      * Return the number of digits in this mixed radix number.
    #      * This is the size of the radixes list.
    #      
    def numDigits(self):
        """ generated source for method numDigits """
        return len(radixes)

    #      * Set the value of this number to equal that of the specified integer.
    #      * @param v The ordinary integer value of this number.
    #      
    def set(self, v):
        """ generated source for method set """
        temp = v
        count = 0
        for radix in radixes:
            if count >= len(digits):
                digits.append(temp % radix)
            else:
                digits.set(count, temp % radix)
            count += 1
            temp = temp / radix

    #      * Set the magnitude of this number to equal that of the specified integer,
    #      * which is the number of times that increment must be invoked from zero
    #      * for the value returned by {@link #get()} to equal v.
    #      * @param v The new magnitude of this number.
    #      
    def setMagnitude(self, v):
        """ generated source for method setMagnitude """
        temp = v
        i = 0
        while i < len(radixes):
            p = self.getPermutation().get(i)
            while len(digits) < p + 1:
            digits.set(p, temp % radixes.get(p))
            temp = temp / radixes.get(p)
            i += 1

    #      * Give a string representation of the number, where each digit is
    #      * represented as n%r, where r is the radix.
    #      
    def __str__(self):
        """ generated source for method toString """
        pieces = LinkedList()
        radixIterator = radixes.iterator()
        for digit in digits:
            if not radixIterator.hasNext():
                pieces.append(digit + "%infinity")
            else:
                pieces.append(digit + "%" + radixIterator.next())
        return ", ".join( pieces)

    # ////////////////////////////////////////////////////////
    # // Private variables
    radixes = None
    digits = None
    permutation = None
