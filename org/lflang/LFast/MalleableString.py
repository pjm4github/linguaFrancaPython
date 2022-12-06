#!/usr/bin/env python
# C:\Users\pmora\Documents\Git\GitHub\lingua-franca\org.lflang\src\org\lflang\LFast\MalleableString.java

""" generated source for module MalleableString """
# package: org.lflang.LFast
# 
#  * A {@code MalleableString} is an object with multiple valid textual
#  * representations. These textual representations are code that may have
#  * associated comments.
#
from antlr4 import IllegalStateException

from include.overloading import overloaded
from lflang.LFast import FormattingUtils


class MalleableString(object):
    """ generated source for class MalleableString """
    comments = []

    #  Return this, indented by one more level. 
    def indent(self):
        """ generated source for method indent """
        return Indented(self)

    #      * Change the state of this such that the badness of the supplied render
    #      * result is minimized.
    #      * @param providedRender A supplier of render results that should be
    #      * optimized.
    #      * @param badness A badness computer for render results.
    #      * @param width The number of columns permitted for this, excluding
    #      * indentation applied to the whole of this.
    #      * @param indentation The number of spaces used per level of indentation.
    #      * @param singleLineCommentPrefix The prefix that marks the start of a
    #      * single-line comment.
    #      
    def findBestRepresentation(self, providedRender, badness, width, indentation, singleLineCommentPrefix):
        """ generated source for method findBestRepresentation """

    #  Return whether any representation of this contains text. 
    def isEmpty(self):
        """ generated source for method isEmpty """

    #        /** Associate comments with this. 
    #        public MalleableString addComments(Stream comments) {
    #            comments.filter(!s.isBlank()).map("String.strip").forEach(this."comments.add");
    #            return this;
    #        }
    #        * Render this using {@code indentation} spaces per indentation level and
    #        * {@code singleLineCommentMarker} to mark the beginnings of single-line comments.
    #        
    def render(self, indentation, singleLineCommentMarker):
        """ generated source for method render """

    #        * Return an object that can be represented as any one of the given
    #        * alternatives.
    #        
    @classmethod
    @overloaded
    def anyOf(cls, *possibilities):
        """ generated source for method anyOf """
        return Fork(possibilities)

    #        * Return an object that can be represented as any one of the given
    #        * alternatives.
    #        
    @classmethod
    @anyOf.register(object, A)
    def anyOf_0(cls, *possibilities):
        """ generated source for method anyOf_0 """
        return Leaf(possibilities)

    #        * Return an object that can be represented as any one of the given
    #        * alternatives.
    #        
    @classmethod
    @anyOf.register(object, A)
    def anyOf_1(cls, *possibilities):
        """ generated source for method anyOf_1 """
        return Leaf(cls.objectArrayToString(possibilities))

    @classmethod
    def objectArrayToString(self, objects):
        """ generated source for method objectArrayToString """
        ret = objects.len()
        i = 0
        while len(objects):
            ret[i] = str(objects[i])
            i += 1
        return ret

    # Build a {@code MalleableString} in a manner analogous to the way we build
    # {@code String}s.
    #       
class Builder(object):
    """ generated source for class Builder """
    components = []

    #
    #           * Append something that can be represented as any of the given
    #           * possibilities.
    #
    @overloaded
    def append(self, *possibilities):
        """ generated source for method append """
        return insert(Function.identity(), "Fork.new", possibilities, "components.add")

    #
    #           * Prepend something that can be represented as any of the given
    #           * possibilities.
    #
    def prepend(self, *possibilities):
        """ generated source for method prepend """
        return insert(Function.identity(), "Fork.new", possibilities, self.components.append(0, ms))

    #
    #           * Append something that can be represented as any of the given
    #           * possibilities.
    #
    @append.register(object, A)
    def append_0(self, *content):
        """ generated source for method append_0 """
        return insert("Leaf.new", "Leaf.new", content, "components.add")

    #
    #           * Append something that can be represented as any of the given
    #           * possibilities.
    #
    @append.register(object, A)
    @SuppressWarnings("UnusedReturnValue")
    def append_1(self, *content):
        """ generated source for method append_1 """
        return self.append(self.objectArrayToString(content))

    #
    #           * Append something that can be represented as any of the given
    #           * possibilities.
    #
    def get(self):
        """ generated source for method get """
        return self.Sequence(ImmutableList.copyOf(self.components))

    #
    #           * Append something that can be represented as any of the given
    #           * possibilities.
    #
    def insert(self, toMalleableString, multiplePossibilitiesRepresenter, possibilities, addToComponents):
        """ generated source for method insert """
        allEmpty = Arrays.stream(possibilities).map(toMalleableString).allMatch("MalleableString.isEmpty")
        if not allEmpty:
            addToComponents.accept(multiplePossibilitiesRepresenter.apply(possibilities))
        return self


class Joiner(Collector):
    """ generated source for class Joiner """
    appendSeparator = None
    prependPrefix = None
    appendSuffix = None

    @overloaded
    def __init__(self, separator):
        """ generated source for method __init__ """
        super(Joiner, self).__init__()
        self.__init__(MalleableString.anyOf(separator))

    @__init__.register(object, MalleableString)
    def __init___0(self, separator):
        """ generated source for method __init___0 """
        super(Joiner, self).__init__()
        self.__init__(separator, MalleableString.anyOf(""), MalleableString.anyOf(""))

    @__init__.register(object, MalleableString, MalleableString, MalleableString)
    def __init___1(self, separator, prefix, suffix):
        """ generated source for method __init___1 """
        super(Joiner, self).__init__()
        self.appendSeparator = builder if builder.components.isEmpty() else builder.append(separator)
        self.prependPrefix = builder.prepend(prefix)
        self.appendSuffix = builder.append(suffix)

    @__init__.register(object, str, str, str)
    def __init___2(self, separator, prefix, suffix):
        """ generated source for method __init___2 """
        super(Joiner, self).__init__()
        self.__init__(MalleableString.anyOf(separator), MalleableString.anyOf(prefix), MalleableString.anyOf(suffix))

    @__init__.register(object)
    def __init___3(self):
        """ generated source for method __init___3 """
        super(Joiner, self).__init__()
        return self.appendSeparator.apply(b).append(ms)


    def supplier(self):
        """ generated source for method supplier """
        return "Builder.new"


    def combiner(self):
        """ generated source for method combiner """
        return True

    def finisher(self):
        """ generated source for method finisher """
        return ("Builder.get").compose(self.appendSuffix).compose(self.prependPrefix)

    def characteristics(self):
        """ generated source for method characteristics """
        return Set.of()

    def RenderResult(self, unplacedComments, rendering, levelsOfCommentDisplacement):
        pass
        """ generated source for method RenderResult """

class Sequence(MalleableString):
    """ generated source for class Sequence """
    components = None

    def __init__(self, components):
        """ generated source for method __init__ """
        super(Sequence, self).__init__()
        self.components = components

    keepCommentsOnSameLine = False
    width = 0

    def render(self, indentation, singleLineCommentPrefix):
        """ generated source for method render """
        componentRenderings = self.components.stream().map(malleableString.render(indentation, singleLineCommentPrefix)).toList()
        commentsFromChildren = componentRenderings.stream().map(it.unplacedComments).map("Stream.toList").toList()
        stringComponents = componentRenderings.stream().map(it.rendering).map("StringUtil.normalizeEol").collect("ArrayList.new", "ArrayList.add", "ArrayList.addAll")
        commentsThatCouldNotBeHandledHere = []
        startColumn = self.inlineCommentStartColumn(stringComponents, commentsFromChildren)
        numCommentsDisplacedHere = 0
        if commentsFromChildren.stream().anyMatch(not s.isEmpty()):
            i = 0
            while i < len(commentsFromChildren):
                if not FormattingUtils.placeComment(commentsFromChildren.get(i), stringComponents, i, self.width, self.keepCommentsOnSameLine, singleLineCommentPrefix, startColumn):
                    commentsThatCouldNotBeHandledHere.extend(commentsFromChildren.get(i))
                    if i != 0:
                        numCommentsDisplacedHere += 1
                i += 1
        return self.RenderResult(Stream.concat(self.comments.stream(), commentsThatCouldNotBeHandledHere.stream()), String.join("", stringComponents), componentRenderings.stream().mapToInt("RenderResult.levelsOfCommentDisplacement").sum() + numCommentsDisplacedHere)

    def inlineCommentStartColumn(self, stringComponents, comments):
        """ generated source for method inlineCommentStartColumn """
        lineLengths = self.getLinesOfInterest(stringComponents, comments).stream().mapToInt("String.length").toArray()
        minNonCommentWidth = Integer.MAX_VALUE
        maxNonIgnoredCommentWidth = 0
        numIgnored = int()
        for i in lineLengths:
            if i > 0:
                minNonCommentWidth = min(minNonCommentWidth, i)
        for i in lineLengths:
            if i < minNonCommentWidth + FormattingUtils.MAX_WHITESPACE_USED_FOR_ALIGNMENT:
                maxNonIgnoredCommentWidth = max(maxNonIgnoredCommentWidth, i)
                numIgnored -= 1
        if numIgnored > len(lineLengths):
            return 0
        padding = 2
        maxCommentWidth = comments.stream().mapToInt(list.stream().mapToInt("String.length").sum()).max().orElse(0)
        return maxNonIgnoredCommentWidth + padding if maxNonIgnoredCommentWidth + padding + maxCommentWidth <= self.width else 0

    def getLinesOfInterest(self, stringComponents, comments):
        """ generated source for method getLinesOfInterest """
        lineNumbersOfInterest = []
        line = 0
        i = 0
        while i < len(stringComponents):
            if not comments.get(i).isEmpty():
                lineNumbersOfInterest.append(line)
            idx = 0
            while idx.indexOf("\n", idx) + 1 > 0:
                i += 1
        lines = String.join("", stringComponents).lines().toList()
        return lineNumbersOfInterest.stream().map("lines.get").toList()

    def findBestRepresentation(self, providedRender, badness, width, indentation, singleLineCommentPrefix):
        """ generated source for method findBestRepresentation """
        self.width = width
        self.keepCommentsOnSameLine = True
        self.optimizeChildren(providedRender, badness, width, indentation, singleLineCommentPrefix)
        if self.components.stream().noneMatch(it.render(indentation, singleLineCommentPrefix).unplacedComments.findAny().isPresent()):
            return
        badnessTrue = badness.applyAsLong(providedRender.get())
        self.keepCommentsOnSameLine = False
        self.optimizeChildren(providedRender, badness, width, indentation, singleLineCommentPrefix)
        badnessFalse = badness.applyAsLong(providedRender.get())
        self.keepCommentsOnSameLine = badnessTrue < badnessFalse
        self.optimizeChildren(providedRender, badness, width, indentation, singleLineCommentPrefix)
        self.optimizeChildren(providedRender, badness, width, indentation, singleLineCommentPrefix)

    def optimizeChildren(self, providedRender, badness, width, indentation, singleLineCommentPrefix):
        """ generated source for method optimizeChildren """
        self.components.reverse().forEach(it.findBestRepresentation(providedRender, badness, width, indentation, singleLineCommentPrefix))

    def isEmpty(self):
        """ generated source for method isEmpty """
        return self.components.stream().allMatch("MalleableString.isEmpty")

class Indented(MalleableString):
    """ generated source for class Indented """
    nested = None
    width = int()

    def __init__(self, toIndent):
        """ generated source for method __init__ """
        super(Indented, self).__init__()
        self.nested = toIndent

    def indent(self):
        """ generated source for method indent """
        return self.Indented(self)

    def findBestRepresentation(self, providedRender, badness, width, indentation, singleLineCommentPrefix):
        """ generated source for method findBestRepresentation """
        self.width = width
        self.nested.findBestRepresentation(providedRender, badness, width - indentation, indentation, singleLineCommentPrefix)

    def isEmpty(self):
        """ generated source for method isEmpty """
        return self.nested.isEmpty()

    def render(self, indentation, singleLineCommentPrefix):
        """ generated source for method render """
        result = self.nested.render(indentation, singleLineCommentPrefix)
        renderedComments = FormattingUtils.lineWrapComments(result.unplacedComments.toList(), self.width - indentation, singleLineCommentPrefix)
        return self.RenderResult(self.comments.stream(), (result.rendering if renderedComments.isBlank() else renderedComments + "\n" + result.rendering).replaceAll("(?<=\n|^)(?=\\h*\\S)", " ".repeat(indentation)), result.levelsOfCommentDisplacement())

class MalleableStringWithAlternatives(MalleableString):
    """ generated source for class MalleableStringWithAlternatives """
    def getPossibilities(self):
        """ generated source for method getPossibilities """

    def __str__(self):
        """ generated source for method toString """
        return self.getChosenPossibility().__str__()

    def findBestRepresentation(self, providedRender, badness, width, indentation, singleLineCommentPrefix):
        """ generated source for method findBestRepresentation """

    def getChosenPossibility(self):
        """ generated source for method getChosenPossibility """
        if self.getPossibilities().isEmpty():
            raise IllegalStateException("A MalleableString must be directly or transitively backed " + "by at least one String.")
        return self.getPossibilities().get(0) if bestPossibility == None else bestPossibility

class Fork(MalleableStringWithAlternatives):
    """ generated source for class Fork """
    possibilities = None

    def __init__(self, possibilities):
        """ generated source for method __init__ """
        super(Fork, self).__init__()
        self.possibilities = ImmutableList.copyOf(possibilities)

    def getPossibilities(self):
        """ generated source for method getPossibilities """
        return self.possibilities

    def isEmpty(self):
        """ generated source for method isEmpty """
        return self.possibilities.stream().allMatch("MalleableString.isEmpty")

    def render(self, indentation, singleLineCommentPrefix):
        """ generated source for method render """
        return getChosenPossibility().render(indentation, singleLineCommentPrefix).with_(self.comments.stream())

class Leaf(MalleableStringWithAlternatives):
    """ generated source for class Leaf """
    possibilities = None

    @overloaded
    def __init__(self, possibilities):
        """ generated source for method __init__ """
        super(Leaf, self).__init__()
        self.possibilities = ImmutableList.copyOf(possibilities)

    @__init__.register(object, str)
    def __init___0(self, possibility):
        """ generated source for method __init___0 """
        super(Leaf, self).__init__()
        self.possibilities = ImmutableList.of(possibility)

    def getPossibilities(self):
        """ generated source for method getPossibilities """
        return self.possibilities

    def isEmpty(self):
        """ generated source for method isEmpty """
        return self.possibilities.stream().allMatch("String.isEmpty")

    def render(self, indentation, singleLineCommentPrefix):
        """ generated source for method render """
        return self.RenderResult(self.comments.stream(), getChosenPossibility(), 0)
