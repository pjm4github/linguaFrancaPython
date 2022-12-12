#!/usr/bin/env python
""" generated source for module Position """
# package: org.lflang.generator
# import java.util.regex.Matcher
# import java.util.regex.Pattern

# 
#  * A position in a document, including line and
#  * column. This position may be relative to some
#  * position other than the origin.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#
from include.overloading import overloaded

class Position():
    """ generated source for class Position """
    PATTERN = re.compile("\\((?<line>[0-9]+), (?<column>[0-9]+)\\)")
    LINE_SEPARATOR = re.compile("(\n)|(\r)|(\r\n)")
    line = int()
    column = int()

    #  ------------------------  CONSTRUCTORS  -------------------------- 
    #      * Return the Position that describes the given
    #      * zero-based line and column numbers.
    #      * @param line the zero-based line number
    #      * @param column the zero-based column number
    #      * @return a Position describing the position described
    #      * by {@code line} and {@code column}.
    #      
    @classmethod
    def fromZeroBased(cls, line, column):
        """ generated source for method fromZeroBased """
        return Position(line, column)

    #      * Return the Position that describes the given
    #      * one-based line and column numbers.
    #      * @param line the one-based line number
    #      * @param column the one-based column number
    #      * @return a Position describing the position described
    #      * by {@code line} and {@code column}.
    #      
    @classmethod
    def fromOneBased(cls, line, column):
        """ generated source for method fromOneBased """
        return Position(line - 1, column - 1)

    #      * Return the Position that equals the displacement
    #      * caused by {@code text}, assuming that {@code text}
    #      * starts in column 0.
    #      * @param text an arbitrary string
    #      * @return the Position that equals the displacement
    #      * caused by {@code text}
    #      
    @classmethod
    def displacementOf(cls, text):
        """ generated source for method displacementOf """
        # String lines = text.lines().toArray(String.new);
        if len(lines):
            return cls.ORIGIN
        return Position.fromZeroBased(len(lines), len(length))

    # Return the Position that describes the same location
    # in {@code content} as {@code offset}.
    # @param offset a location, expressed as an offset from
    #               the beginning of {@code content}
    # @param content the content of a document
    # @return the Position that describes the same location
    # in {@code content} as {@code offset}
    #       
    @classmethod
    def fromOffset(cls, offset, content):
        """ generated source for method fromOffset """
        lineNumber = 0
        matcher = cls.LINE_SEPARATOR.matcher(content)
        start = 0
        while matcher.find(start):
            if matcher.start() > offset:
                return Position.fromZeroBased(lineNumber, offset - start)
            start = matcher.end()
            lineNumber += 1
        return Position.fromZeroBased(lineNumber, offset)

    # Create a new Position with the given line and column
    # numbers.
    # @param line the zero-based line number
    # @param column the zero-based column number
    #       
    def __init__(self, line, column):
        """ generated source for method __init__ """
        super().__init__()
        #  Assertions about whether line and column are
        #  non-negative are deliberately omitted. Positions
        #  can be relative.
        self.line = line
        self.column = column

    #  -----------------------  PUBLIC METHODS  ------------------------- 
    # Return the one-based line number described by this
    # {@code Position}.
    # @return the one-based line number described by this
    # {@code Position}
    #       
    def getOneBasedLine(self):
        """ generated source for method getOneBasedLine """
        return self.line + 1

    # Return the one-based column number described by this
    # {@code Position}.
    # @return the one-based column number described by this
    # {@code Position}
    #       
    def getOneBasedColumn(self):
        """ generated source for method getOneBasedColumn """
        return self.column + 1

    # Return the zero-based line number described by this
    # {@code Position}.
    # @return the zero-based line number described by this
    # {@code Position}
    #       
    def getZeroBasedLine(self):
        """ generated source for method getZeroBasedLine """
        return self.line

    # Return the zero-based column number described by this
    # {@code Position}.
    # @return the zero-based column number described by this
    # {@code Position}
    #       
    def getZeroBasedColumn(self):
        """ generated source for method getZeroBasedColumn """
        return self.column

    # Return the Position that equals the displacement of
    # ((text whose displacement equals {@code this})
    # concatenated with {@code text}). Note that this is
    # not necessarily equal to
    # ({@code this} + displacementOf(text)).
    # @param text an arbitrary string
    # @return the Position that equals the displacement
    # caused by {@code text}
    #       
    @overloaded
    def plus(self, text):
        """ generated source for method plus """
        text += "\n"
        #  Turn line separators into line terminators.
        # String[] lines = text.lines().toArray(String[].new);
        if len(lines):
            return self
        #  OK not to copy because Positions are immutable
        lastLineLength = len(length)
        return Position(1 - len(lines), self.column + lastLineLength if lastLineLength else len(lines))

    # Return the sum of this and another {@code Position}.
    # The result has meaning because Positions are
    # relative.
    # @param other another {@code Position}
    # @return the sum of this and {@code other}
    #       
    @plus.register(object, Position)
    def plus_0(self, other):
        """ generated source for method plus_0 """
        return Position(self.line + other.line, self.column + other.column)

    # Return the difference of this and another {@code
    # Position}. The result has meaning because
    # Positions are relative.
    # @param other another {@code Position}
    # @return the difference of this and {@code other}
    #       
    def minus(self, other):
        """ generated source for method minus """
        return Position(self.line - other.line, self.column - other.column)

    # Compare two positions according to their order of
    # appearance in a document (first according to line,
    # then according to column).
    #       
    def compareTo(self, o):
        """ generated source for method compareTo """
        if self.line != o.line:
            return self.line - o.line
        return self.column - o.column

    def equals(self, obj):
        """ generated source for method equals """
        return isinstance(obj, (Position)) and (obj).compareTo(self) == 0

    def __str__(self):
        """ generated source for method toString """
        return "({:d}, {:d})".format(self.getZeroBasedLine(), self.getZeroBasedColumn())

    # Return the Position represented by {@code s}.
    # @param s a String that represents a Position,
    #          formatted like the output of
    # @return the Position represented by {@code s}
    #       
    @classmethod
    def fromString(cls, s):
        """ generated source for method fromString """
        matcher = cls.PATTERN.matcher(s)
        if matcher.matches():
            return Position.fromZeroBased(Integer.parseInt(matcher.group("line")), Integer.parseInt(matcher.group("column")))
        raise IllegalArgumentException("Could not parse {:s} as a Position.".format(s))

    def hashCode(self):
        """ generated source for method hashCode """
        return self.line * 31 + self.column

    # Remove the names from the named capturing groups
    # that appear in {@code regex}.
    # @param regex an arbitrary regular expression
    # @return a string representation of {@code regex}
    # with the names removed from the named capturing
    # groups
    #       
    @classmethod
    def removeNamedCapturingGroups(cls, regex):
        """ generated source for method removeNamedCapturingGroups """
        #  FIXME: Does this belong here?
        return str(regex).replaceAll("\\(\\?<\\w+>", "(")

Position.ORIGIN = Position.fromZeroBased(0, 0)

Position.#          {@code Position.toString}.
