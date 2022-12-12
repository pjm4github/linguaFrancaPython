#!/usr/bin/env python
""" generated source for module CodeMap """
# package: org.lflang.generator
# import java.nio.file.Path
# import java.util.Iterator
# import java.util.Map
# import java.util.NavigableMap
# import java.util.Set
# import java.util.TreeMap
# import java.util.HashMap
# import java.util.regex.Matcher
# import java.util.regex.Pattern
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.nodemodel.INode
# import org.eclipse.xtext.nodemodel.util.NodeModelUtils
# import org.eclipse.xtext.util.LineAndColumn
import re

from include.SpecialExceptions import RuntimeException
from include.overloading import overloaded
from lflang.LFast.Nodemodels import NodeModelUtils
from lflang.cli.StandaloneErrorReporter import Path
from lflang.generator.Position import Position
from lflang.generator.Range import Range
from org.lflang.lf.impl import ParameterReferenceImpl

# 
#  * Encapsulates data about the correspondence between
#  * ranges of generated code and ranges of a Lingua Franca
#  * file.
#  
class TreeMap:
    pass

class Correspondence:
    @overloaded
    def __init__(self, generatedCode, map, isVerbatimByLfSourceByRange):
        # The content of the generated file represented by
        # this.
        self.generatedCode = generatedCode
        # A mapping from Lingua Franca source paths to mappings
        # from ranges in the generated file represented by this
        # to ranges in Lingua Franca files.
        self.map = map
        # A mapping from Lingua Franca source paths to mappings
        # from ranges in the generated file represented by this
        # to whether those ranges are copied verbatim from the
        # source.
        self.isVerbatimByLfSourceByRange = isVerbatimByLfSourceByRange
        # This pattern has the markers "/* */", which some languages use as line comments. This does not
        #  represent any serious effort to embed the string representation of this object in generated code
        #  without introducing a syntax error. Instead, it is done simply because it is easy.
        self.PATTERN = re.compile(
            f"/\\*Correspondence: (?P(lfRange){Position.removeNamedCapturingGroups(Range.PATTERN)}) \\-> "
            f"(?P(generatedRange){Position.removeNamedCapturingGroups(Range.PATTERN)}) \\(verbatim=(?P(verbatim)true|false); src=(?P(path)%s)\\)\\*/",
            ".*?"
        )

    @overloaded
    @__init__.register(object, Path, Range, Range, bool)
    def __init___0(self, path, lfRange, generatedRange, verbatim):
        self.path = path
        self.lfRange = lfRange
        self.generatedRange = generatedRange
        self.verbatim = verbatim

    def getPath(self):
        """
        Returns a path to the LF source file described by
        @return a path to the LF source file described by
        this Correspondence
        :return:
        """
        return self.path

    def getLfRange(self):
        """
        Returns a range in an LF source file.
        @return a range in an LF source file
        :return:
        """
        return self.lfRange

    def getGeneratedRange(self):
        """
        Returns a range in a generated file that
        corresponds to a range in an LF file.
        @return a range in a generated file that
        corresponds to a range in an LF file

        :return:
        """
        return self.generatedRange

    def toString(self):
        return f"/*Correspondence: {self.lfRange.__str__()} -> {self.generatedRange.__str__()} " \
               f"(verbatim={self.verbatim}; src={self.path.__str__()})*/",

    def fromString(self, s, relativeTo):
        """
        Returns the Correspondence represented by
        {@code s}.
        :param s: a String that represents a
                 Correspondence, formatted like the
                 output of Correspondence::toString
        :param relativeTo: the offset relative to which
                          the offsets given are given
        :return: the Correspondence represented by
                 {@code s}
        """
        matcher = self.PATTERN.match(s)
        if matcher.matches():
            lfRange = Range.fromString(matcher.group("lfRange"))
            generatedRange = Range.fromString(matcher.group("generatedRange"), relativeTo)
            return self.__init__(
                Path.of(matcher.group("path")),
                lfRange,
                generatedRange,
                bool(matcher.group("verbatim"))
            )

    def tag(self, astNode, representation, verbatim):
        """
        Returns {@code representation}, tagged with
        a Correspondence to the source code associated
        with {@code astNode}.

        :param astNode: an arbitrary AST node
        :param representation: the code generated from
                               that AST node
        :param verbatim: whether {@code representation}
                         is copied verbatim from the
                         part of the source code
                         associated with {@code astNode}
        :return: {@code representation}, tagged with
                 a Correspondence to the source code associated
                 with {@code astNode}
        """
        node = NodeModelUtils.getNode(astNode)
        # If the EObject originates from an AST transformation, then it does not correspond directly
        # to any LF code, and it need not be tagged at all.
        if node == None:
            return representation
        oneBasedLfLineAndColumn = NodeModelUtils.getLineAndColumn(node, node.getTotalOffset())
        lfStart = Position.fromOneBased(
            oneBasedLfLineAndColumn.getLine(), oneBasedLfLineAndColumn.getColumn()
        )
        lfPath = Path.of(self.bestEffortGetEResource(astNode).getURI().path())
        if verbatim:
            lfStart = lfStart.plus(node.getText().substring(0, node.getText().find(representation)))
        t =  representation if verbatim else node.getText()
        return self.__init__(
            lfPath,
            Range(lfStart, lfStart.plus(t)),
            Range(Position.ORIGIN, Position.displacementOf(representation)),
            verbatim) + representation

    @classmethod
    def bestEffortGetEResource(cls, astNode):
        """
        Return the {@code eResource} associated with the given AST node.
        This is a dangerous operation which can cause an unrecoverable error.

        :param astNode:
        :return:
        """
        """ generated source for method bestEffortGetEResource """
        #                if (astNode instanceof ParameterReferenceImpl pri)
        #                  return pri.getParameter().eResource();
        ret = astNode.eResource()
        if ret is not None:
            return ret
        raise RuntimeException("Every non-null AST node should have an EResource, but \""
                               + astNode + "\" does not.")

    @classmethod
    def indexOf(cls, s, imperfectSubstring):
        """
        Make a best-effort attempt to find the index of
        a near substring whose first line is expected to
        be an exact substring of {@code s}. Return 0
        upon failure.

        :param s: an arbitrary string
        :param imperfectSubstring: an approximate substring of {@code s}
        :return: the index of {@code imperfectSubstring}
                 within {@code s}
        """
        firstLine = imperfectSubstring.lines().findFirst().orElse("")
        return max(0, s.indexOf(firstLine))


class CodeMap:
    """ generated source for class CodeMap """

    @classmethod
    def fromGeneratedCode(cls, internalGeneratedCode):
        """
        Instantiates a {@code CodeMap} from
        {@code internalGeneratedCode}.
        {@code internalGeneratedCode} may be invalid
        code that is different from the final generated code
        because it should contain deserializable
        representations of {@code Correspondences}.
        @param internalGeneratedCode code from a code
                                     generator that contains
                                     serialized
                                     Correspondences
        @return a CodeMap documenting the provided code

        :param internalGeneratedCode:
        :return:
        """
        map = dict()
        isVerbatimByLfSourceByRange = dict()
        generatedCode = ""
        it = internalGeneratedCode.lines().iterator()
        zeroBasedLine = 0
        __zeroBasedLine_0 = zeroBasedLine
        zeroBasedLine += 1
        while it.hasNext():
            generatedCode.append(
                cls.processGeneratedLine(it.next(), __zeroBasedLine_0, map, isVerbatimByLfSourceByRange)).append('\n')
        return CodeMap(generatedCode.__str__(), map, isVerbatimByLfSourceByRange)

    def getGeneratedCode(self):
        """
        Returns the generated code (without Correspondences).
        @return the generated code (without Correspondences)

        :return:
        """
        return self.generatedCode

    def lfSourcePaths(self):
        """
        Returns the set of all paths to Lingua Franca files
        that are known to contain code that corresponds to
        code in the generated file represented by this.
        @return the set of all paths to Lingua Franca files
        that are known to contain code that corresponds to
        code in the generated file represented by this

        :return:
        """
        return self.map.keySet()

    @overloaded
    def adjusted(self, lfFile, generatedFilePosition):
        """
        Returns the range in {@code lfFile}
        corresponding to {@code generatedFileRange}
        if such a range is known, or a degenerate Range
        otherwise.

        :param lfFile:the path to an arbitrary Lingua Franca
                      source file
        :param generatedFilePosition:a position in a
                                     generated file
        :return: the range in {@code lfFile}
                 corresponding to {@code generatedFileRange}
        """
        mapOfInterest = self.map.get(lfFile)
        isVerbatimByRange = self.isVerbatimByLfSourceByRange.get(lfFile)
        nearestEntry = mapOfInterest.floorEntry(Range.degenerateRange(generatedFilePosition))
        if nearestEntry == None:
            return Position.ORIGIN
        if not isVerbatimByRange.get(nearestEntry.getKey()):
            return nearestEntry.getValue().getStartInclusive()
        if nearestEntry.getKey().contains(generatedFilePosition):
            return nearestEntry.getValue().getStartInclusive().plus(generatedFilePosition.minus(nearestEntry.getKey().getStartInclusive()))
        return Position.ORIGIN

    @adjusted.register(object, Path, Range)
    def adjusted_0(self, lfFile, generatedFileRange):
        """ generated source for method adjusted_0 """
        start = self.adjusted(lfFile, generatedFileRange.getStartInclusive())
        end = self.adjusted(lfFile, generatedFileRange.getEndExclusive())
        return Range(start, end) if start.compareTo(end) <= 0 else Range(start, start)


    @classmethod
    def processGeneratedLine(cls, line, zeroBasedLineIndex, map,
                             isVerbatimByLfSourceByRange):
        """
        Removes serialized Correspondences from {@code line}
        and updates {@code map} according to those
        Correspondences.

        :param line:a line of generated code
        :param zeroBasedLineIndex:the index of the given line
        :param map:a map that stores Correspondences
        :param isVerbatimByLfSourceByRange:
        :return:the line of generated code with all Correspondences removed
        """
        matcher = cls.Correspondence.PATTERN.matcher(line)
        cleanedLine = ""
        lastEnd = 0
        while matcher.find():
            cleanedLine.append(line, lastEnd, matcher.start())
            c = cls.Correspondence.fromString(matcher.group(), Position.fromZeroBased(zeroBasedLineIndex, len(cleanedLine)))
            if not map.containsKey(c.path):
                map.put(c.path, TreeMap())
            map.get(c.path).put(c.generatedRange, c.lfRange)
            if not isVerbatimByLfSourceByRange.containsKey(c.path):
                isVerbatimByLfSourceByRange.put(c.path, dict())
            isVerbatimByLfSourceByRange.get(c.path).put(c.generatedRange, c.verbatim)
            lastEnd = matcher.end()
        cleanedLine.append(line.substring(lastEnd))
        return str(cleanedLine)()
