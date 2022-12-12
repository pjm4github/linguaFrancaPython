#!/usr/bin/env python
""" generated source for module ErrorInserter """
# package: org.lflang.tests.lsp
# import java.io.Closeable
# import java.io.IOException
# import java.io.PrintWriter
# import java.nio.file.Files
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.Iterator
# import java.util.LinkedList
# import java.util.List
# import java.util.ListIterator
# import java.util.Random
# import java.util.function_.BiFunction
# import java.util.function_.BiPredicate
# import java.util.function_.Function
# import java.util.function_.Predicate
# import java.util.stream.Stream
# import com.google.common.collect.ImmutableList
from include.overloading import overloaded

# 
#  * Insert problems into integration tests.
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
@SuppressWarnings("ClassCanBeRecord")
class ErrorInserter:
    """ generated source for class ErrorInserter """
    #  A basic error inserter builder on which more specific error inserters can be built. 
    BASE_ERROR_INSERTER = Builder().insertable("    0 = 1;").insertable("some_undeclared_var1524263 = 9;").insertable("        ++;")
    C = BASE_ERROR_INSERTER.replacer("lf_set(", "UNDEFINED_NAME2828376(").replacer("lf_schedule(", "undefined_name15291838(")
    CPP = BASE_ERROR_INSERTER.replacer(".get", ".undefined_name15291838").replacer("std::", "undefined_name3286634::")
    PYTHON_SYNTAX_ONLY = Builder().insertable("        +++++;").insertable("        ..")
    PYTHON = PYTHON_SYNTAX_ONLY.replacer("print(", "undefined_name15291838(")
    RUST = BASE_ERROR_INSERTER.replacer("println!", "undefined_name15291838!").replacer("ctx.", "undefined_name3286634.")
    TYPESCRIPT = BASE_ERROR_INSERTER.replacer("requestErrorStop(", "not_an_attribute_of_util9764(").replacer("const ", "var ")


    MAX_ALTERATION_ATTEMPTS = 100
    random = None
    replacers = None
    insertables = None
    insertCondition = None

    def __init__(self, random, replacers, insertables, insertCondition):
        """ generated source for method __init__ """
        self.random = random
        self.replacers = replacers
        self.insertables = insertables
        self.insertCondition = insertCondition

    def alterTest(self, test):
        """ generated source for method alterTest """
        alterable = self.AlteredTest(test, self.insertCondition)
        remainingAlterationAttempts = self.MAX_ALTERATION_ATTEMPTS
        __remainingAlterationAttempts_0 = remainingAlterationAttempts
        remainingAlterationAttempts -= 1
        while alterable.getBadLines().isEmpty() and __remainingAlterationAttempts_0 > 0:
            if self.random.nextBoolean() and not self.replacers.isEmpty():
                alterable.replace(self.replacers.get(self.random.nextInt(len(self.replacers))), self.random)
            elif not self.insertables.isEmpty():
                alterable.insert(self.insertables.get(self.random.nextInt(len(self.insertables))), self.random)
        alterable.write()
        return alterable

class AlteredTest(Closeable):
    """ generated source for class AlteredTest """
    class OnceTrue:
        """ generated source for class OnceTrue """
        beenTrue = bool()
        random = None

        def __init__(self, random):
            """ generated source for method __init__ """
            self.beenTrue = False
            self.random = random

        def get(self):
            """ generated source for method get """
            if self.beenTrue:
                return False
            return self.beenTrue = self.random.nextBoolean() and self.random.nextBoolean()

    badLines = None
    path = None
    lines = None
    insertCondition = None

    def __init__(self, originalTest, insertCondition):
        """ generated source for method __init__ """
        super(AlteredTest, self).__init__()
        self.badLines = []
        self.path = originalTest
        self.lines = LinkedList()
        self.lines.extend(Files.readAllLines(originalTest))

    def getPath(self):
        """ generated source for method getPath """
        return self.path

    def write(self):
        """ generated source for method write """
        if not self.path.toFile().renameTo(swapFile(self.path).toFile()):
            raise IOError("Failed to create a swap file.")

    def close(self):
        """ generated source for method close """
        if not swapFile(self.path).toFile().exists():
            raise IllegalStateException("Swap file does not exist.")
        if not self.path.toFile().delete():
            raise IOError("Failed to delete the file associated with the original test.")
        if not swapFile(self.path).toFile().renameTo(self.path.toFile()):
            raise IOError("Failed to restore the altered LF file to its original state.")

    def __str__(self):
        """ generated source for method toString """
        lengthOfPrefix = 6
        ret = StringBuilder(self.lines.stream().mapToInt().reduce(0, Integer.sum) + len(self.lines) * lengthOfPrefix)
        i = 0
        while i < len(self.lines):
            ret.append("-> " if self.badLines.contains(i) else "   ").append("{0:2s} ".format(i)).append(self.lines.get(i)).append("\n")
            i += 1
        return str(ret)

    def getBadLines(self):
        """ generated source for method getBadLines """
        return ImmutableList.copyOf(self.badLines)

    def replace(self, replacer, random):
        """ generated source for method replace """
        onceTrue = self.OnceTrue(random)

    def insert(self, line, random):
        """ generated source for method insert """
        onceTrue = self.OnceTrue(random)

    def alter(self, alterer):
        """ generated source for method alter """
        it = self.lines.listIterator()
        inCodeBlock = False
        lineNumber = 0
        while it.hasNext():
            current = it.next()
            uncommented = current.substring(0, current.indexOf("//")) if current.contains("//") else current
            if uncommented.contains("=}"):
                inCodeBlock = False
            if inCodeBlock and alterer.apply(it, current):
                self.badLines.append(lineNumber)
            if uncommented.contains("{="):
                inCodeBlock = True
            if uncommented.contains("{=") and uncommented.contains("=}"):
                inCodeBlock = uncommented.lastIndexOf("{=") > uncommented.lastIndexOf("=}")
            lineNumber += 1

    @classmethod
    def swapFile(cls, p):
        """ generated source for method swapFile """
        return p.getParent().resolve("." + p.getFileName() + ".swp")


class Builder:
    """ generated source for class Builder """

    replacers = None
    insertables = None
    insertCondition = None

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.__init__(None, None, True)

    @__init__.register(object, self.Node, self.Node, BiPredicate)
    def __init___0(self, replacers, insertables, insertCondition):
        """ generated source for method __init___0 """
        self.replacers = replacers
        self.insertables = insertables
        self.insertCondition = insertCondition

    def replacer(self, phrase, alternativePhrase):
        """ generated source for method replacer """
        return self.Builder(self.Node(self.replacers, line), self.insertables, self.insertCondition)

    def insertable(self, line):
        """ generated source for method insertable """
        return self.Builder(self.replacers, self.Node(self.insertables, line), self.insertCondition)

    def insertCondition(self, insertCondition):
        """ generated source for method insertCondition """
        return self.Builder(self.replacers, self.insertables, self.insertCondition.and_(insertCondition))

    def get(self, random):
        """ generated source for method get """
        return ErrorInserter(random, ImmutableList.of() if self.replacers == None else ImmutableList.copyOf(self.replacers), ImmutableList.of() if self.insertables == None else ImmutableList.copyOf(self.insertables), self.insertCondition)

class Node(Iterable):
    """ generated source for class Node """
    previous = None
    item = None

    def __init__(self, previous, item):
        """ generated source for method __init__ """
        super(Node, self).__init__()
        self.previous = previous
        self.item = item

    def iterator(self):
        """ generated source for method iterator """
        ret = NodeIterator()
        ret.current = self
        return ret

class NodeIterator(Iterator):
    """ generated source for class NodeIterator """
    current = None

    def hasNext(self):
        """ generated source for method hasNext """
        return self.current != None

    def next(self):
        """ generated source for method next """
        ret = self.current.item
        self.current = self.current.previous
        return ret
