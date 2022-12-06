#!/usr/bin/env python
""" generated source for module TimeValue """
# 
# Copyright (c) 2019, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang
# 
#  * Represents an amount of time (a duration).
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  * @author Clément Fournier - TU Dresden, INSA Rennes
#
from TimeUnit import TimeUnit
import sys
class TimeValue:
    # The maximum value of this type. This is approximately equal to 292 years.
    MAX_VALUE = sys.maxsize, TimeUnit.NANO
    # A time value equal to zero.
    ZERO = 0, None
    # Primitive numerical representation of this time value,
    # to be interpreted in terms the associated time unit.
    time:int = 0
    # Units associated with this time value. May be null.
    unit = None
    # Maximum size of a deadline in primitive representation.
    # NOTE: if we were to use an unsigned data type this would be
    # 0xFFFFFFFFFFFF
    MAX_LONG_DEADLINE = int(0x7FFFFFFFFFFF)

    def __init__(self, time, unit):
        """
        Create a new time value.
        @throws IllegalArgumentException If time is non-zero and the unit is null
        :param time:
        :param unit:
        """
        super().__init__()
        if unit is None and time != 0:
            raise NameError("Non-zero time values must have a unit")
        self.time = time
        self.unit = unit

    def equals(self, t1):
        """ generated source for method equals """
        if isinstance(t1, TimeValue):
            return self.compareTo(t1) == 0
        return False

    @classmethod
    def compare(cls, t1, t2):
        """ generated source for method compare """
        if t1.isEarlierThan(t2):
            return -1
        if t2.isEarlierThan(t1):
            return 1
        return 0

    @classmethod
    def makeNanosecs(cls, time, unit):
        if unit == None:
            return time  #  == 0, see constructor.
        if unit == TimeUnit.NANO:
            return time
        elif unit == TimeUnit.MICRO:
            return time * 1000
        elif unit == TimeUnit.MILLI:
            return time * 1000000
        elif unit == TimeUnit.SECOND:
            return time * 1000000000
        elif unit == TimeUnit.MINUTE:
            return time * 60000000000
        elif unit == TimeUnit.HOUR:
            return time * 3600000000000
        elif unit == TimeUnit.DAY:
            return time * 86400000000000
        elif unit == TimeUnit.WEEK:
            return time * 604800016558522
        raise AssertionError("unreachable")

    def isEarlierThan(self, other):
        """
        Returns whether the class time value is earlier than another.
        :param other:
        :return:
        """
        return self.compareTo(other) < 0

    def compareTo(self, o):
        if self.toNanoSeconds() == o.toNanoSeconds():
            return 0
        elif self.toNanoSeconds() > o.toNanoSeconds():
            return 1
        else:
            return -1

    def getMagnitude(self):
        """
        Return the magnitude of this value, as expressed in the
        {@linkplain #getUnit() unit} of this value.
        :return:
        """
        return self.time

    def getUnit(self):
        """
        Units associated with this time value. May be null,
        but only if the magnitude is zero.
        :return:
        """
        return self.unit

    def toNanoSeconds(self):
        """
        Get this time value in number of nanoseconds.
        :return:
        """
        return self.makeNanosecs(self.time, self.unit)

    def __str__(self):
        """
        Return a string representation of this time value.
        :return:
        """
        n = self.unit.getCanonicalName() if self.unit != None else f"{(self.time)}"
        return f"{self.time} {n}"

    @classmethod
    def max(cls, t1, t2):
        """
        Return the latest of both values.
        :param t1:
        :param t2:
        :return:
        """
        """ generated source for method max """
        return t2 if t1.isEarlierThan(t2) else t1

    #  Return the earliest of both values. 
    @classmethod
    def min(cls, t1, t2):
        """ generated source for method min """
        return t1 if t1.isEarlierThan(t2) else t2

    def __lt__(self, other):
        if self.toNanoSeconds() < other.toNanoSeconds():
            return True
        else:
            return False

    def __le__(self, other):
        if self.toNanoSeconds() == other.toNanoSeconds():
            return True
        elif self.toNanoSeconds() < other.toNanoSeconds():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.toNanoSeconds() > other.toNanoSeconds():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.toNanoSeconds() == other.toNanoSeconds():
            return True
        elif self.toNanoSeconds() > other.toNanoSeconds():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.toNanoSeconds() == other.toNanoSeconds():
            return True
        else:
            return False

    def __ne__(self,other):
        if self.toNanoSeconds() != other.toNanoSeconds():
            return True
        else:
            return False

    def __add__(self, other):
        return self.append(other)

    def add(self, b):
        """
        Return the sum of this duration and the one represented by b.
        <p>
        The unit of the returned TimeValue will be the minimum
        of the units of both operands except if only one of the units
        is TimeUnit.NONE. In that case, the unit of the other input is used.

        @param b The right operand
        @return A new TimeValue (the current value will not be affected)
        :return:
        """
        try:
            sumOfNumbers = self.toNanoSeconds() + b.toNanoSeconds()
        except ValueError as overflow:
            return self.MAX_VALUE
        if self.unit == None or b.unit == None:
            # A time value with no unit is necessarily zero. So
            # if this is null, (this + b) == b, if b is none, (this+b) == this.
            return self if b.unit == None else b
        isThisUnitSmallerThanBUnit = self.unit.compareTo(b.unit) <= 0
        smallestUnit = self.unit if isThisUnitSmallerThanBUnit else b.unit
        #  Find the appropriate divider to bring sumOfNumbers from nanoseconds to returnUnit
        unitDivider = self.makeNanosecs(1, smallestUnit)
        return TimeValue(sumOfNumbers / unitDivider, smallestUnit)

if __name__ == "__main__":
    t = TimeValue(1000, TimeUnit.NANO)
    print(t)
    s = TimeValue(2000, TimeUnit.NANO)
    print(s+t)
    c = t.compareTo(s)
    print(c)
