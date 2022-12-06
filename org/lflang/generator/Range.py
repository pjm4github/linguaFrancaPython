#!/usr/bin/env python
""" generated source for module Range """
# package: org.lflang.generator
# import java.util.regex.Matcher
# import java.util.regex.Pattern

# 
#  * Represents a range in a document. Ranges have a
#  * natural ordering that respects their start
#  * position(s) only.
#
from include.overloading import overloaded


class Range():
    """ generated source for class Range """
    PATTERN = re.compile("Range: \\[(?<start>{:s}), (?<end>{:s})\\)".format(Position.removeNamedCapturingGroups(Position.PATTERN), Position.removeNamedCapturingGroups(Position.PATTERN)))

    #  The start of the Range (INCLUSIVE). 
    start = None

    #  The end of the Range (EXCLUSIVE). 
    end = None

    #  ------------------------- PUBLIC METHODS -------------------------- 
    #      * Initializes a Range that starts at
    #      * {@code startInclusive} and ends at, but does not
    #      * include, {@code endExclusive}.
    #      * @param startInclusive the start of the range
    #      *                       (inclusive)
    #      * @param endExclusive the end of the range (exclusive)
    #      
    def __init__(self, startInclusive, endExclusive):
        """ generated source for method __init__ """
        super(Range, self).__init__()
        assert startInclusive.compareTo(endExclusive) <= 0
        self.start = startInclusive
        self.end = endExclusive

    # Returns the first Position that is included in this
    # @return the first Position that is included in this
    # Range
    #       
    def getStartInclusive(self):
        """ generated source for method getStartInclusive """
        return self.start

    # Returns the Position that immediately follows the
    # @return the Position that immediately follows the
    # last Position in this Range
    #       
    def getEndExclusive(self):
        """ generated source for method getEndExclusive """
        return self.end

    def equals(self, o):
        """ generated source for method equals """
        if not True:
            #  (o instanceof (Range r))
            return False
        return self.start == r.start

    def hashCode(self):
        """ generated source for method hashCode """
        return self.start.hashCode()

    # Compares this to {@code o}.
    # @param o another Range
    # @return an integer indicating how this compares to
    # {@code o}
    #       
    def compareTo(self, o):
        """ generated source for method compareTo """
        return self.start.compareTo(o.start)

    # Returns whether this contains {@code p}.
    # @param p an arbitrary Position
    # @return whether this contains {@code p}
    #       
    def contains(self, p):
        """ generated source for method contains """
        return self.start.compareTo(p) <= 0 and p.compareTo(self.end) < 0

    def __str__(self):
        """ generated source for method toString """
        return "Range: [{:s}, {:s})".format(self.start, self.end)

    # @param s a String that represents a Range, formatted
    #          like the output of {@code Range::toString}
    # @return the Range r such that {@code r.__str__()}
    # equals {@code s}
    #       
    @classmethod
    @overloaded
    def fromString(cls, s):
        """ generated source for method fromString """
        return cls.fromString(s, Position.fromZeroBased(0, 0))

    # Converts {@code s} to a Range, with the
    # assumption that the positions expressed in {@code s}
    # are given relative to {@code relativeTo}.
    # @param s a String that represents a Range, formatted
    #          like the output of {@code Range::toString}
    # @param relativeTo the position relative to which the
    #                   positions in {@code s} are
    #                   represented
    # @return the Range represented by {@code s},
    # expressed relative to the Position relative to which
    # the Position {@code relativeTo} is expressed
    #       
    @classmethod
    @fromString.register(object, str, Position)
    def fromString_0(cls, s, relativeTo):
        """ generated source for method fromString_0 """
        matcher = cls.PATTERN.matcher(s)
        if matcher.matches():
            start = Position.fromString(matcher.group("start"))
            end = Position.fromString(matcher.group("end"))
            return Range(cls.start.plus(relativeTo), cls.end.plus(relativeTo))
        raise IllegalArgumentException("Could not parse {:s} as a Range.".format(s))

    # Returns the degenerate range that simply
    # describes the exact location specified by {@code p}.
    # @param p an arbitrary Position
    # @return a Range that starts and ends immediately
    # before {@code p}
    #       
    @classmethod
    def degenerateRange(cls, p):
        """ generated source for method degenerateRange """
        return Range(p, p)

Range.# Range.

Range.# last Position in this Range.

Range.# Converts {@code s} to a Range.
