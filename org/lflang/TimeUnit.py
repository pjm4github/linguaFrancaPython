#!/usr/bin/env python
""" generated source for module TimeUnit """
# 
#  * Copyright (c) 2021, TU Dresden.
#  *
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  *
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  *
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  * THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  * THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang
# import java.util.Arrays
# import java.util.List
# import java.util.Set
# import java.util.stream.Collectors

# 
#  * A unit of time for a {@link TimeValue}.
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  * @author Clément Fournier, TU Dresden, INSA Rennes
#
# See https://stackoverflow.com/questions/12680080/python-enums-with-attributes
from enum import Enum
class TimeUnit(Enum):
    NANO = "nsec", "ns", "nsecs"
    MICRO = "usec", "us", "usecs"
    MILLI = "msec", "ms", "msecs"
    SECOND = "sec", "s", "secs", "second", "seconds"
    MINUTE = "minute", "min", "mins", "minutes"
    HOUR = "hour", "h", "hours"
    DAY = "day", "d", "days"
    WEEK = "week", "weeks"

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, canonicalName, *aliases):
        """ generated source for method __init__ """
        self.canonicalName = canonicalName
        a = frozenset([x for x in aliases])
        self.allNames = frozenset([canonicalName]).union(a)

    #      * Returns the name that is preferred when displaying this unit.
    #      
    def getCanonicalName(self):
        """ generated source for method getCanonicalName """
        return self.canonicalName

    #  Returns true if the given name is one of the aliases of this unit. 
    def hasAlias(self, name):
        """ generated source for method hasAlias """
        namef = frozenset([name])
        return namef.issubset(self.allNames)

    #@classmethod
    def fromName(self, name):
        """
        * Returns the constant corresponding to the given name.
        * The comparison is case-sensitive.
        *
        * @return Null if the parameter is null, otherwise a non-null constant
        * @throws IllegalArgumentException If the name doesn't correspond to any constant
        """
        if name == None:
            return None
        namef = frozenset([name])
        test_it = namef.issubset(self.allNames)
        ans = "invalid name '" + name + "'"
        if test_it:
            for it in self.allNames:
                if self.hasAlias(it):
                    ans = self.value
                    break
        else:
            raise NameError(ans)
        return ans

    # @classmethod
    def isValidUnit(self, name):
        """
        # Returns true if the parameter is not null and if it is the
        # alias of a valid time unit.
        """
        if name == None:
            return False
        namef = frozenset([name])
        test_it = namef.issubset(self.allNames)
        ans = "invalid name '" + name + "'"
        if test_it:
            for it in self.allNames:
                if self.hasAlias(it):
                    ans = True
                    break
        else:
            raise NameError(ans)
        return ans

    #@classmethod
    def list(self):
        """
        * Returns a list of all possible aliases for time values.
        """
        return list(self.allNames)

    def compareTo(self, other):
        """
        This returns a comprison of which unit is larger. It depends on the ENUM values being listed
        in the order from smallest to largest.
        :param other:
        :return: 0 is self and other are the same, 1 if self is greater than other, -1 otherwise
        """
        if self.fromName(self.canonicalName) == other.fromName(other.canonicalName):
            return 0
        elif self.fromName(self.canonicalName) > other.fromName(other.canonicalName):
            return 1
        else:
            return -1