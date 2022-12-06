#!/usr/bin/env python
""" generated source for module TestRegistry """
# package: org.lflang.tests
from include.overloading import overloaded
import os
# import java.io.File
# import java.io.IOException
# import java.nio.file.FileVisitResult
# import java.nio.file.FileVisitor
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.nio.file.SimpleFileVisitor
# import java.nio.file.attribute.BasicFileAttributes
# import java.util.Arrays
# import java.util.HashMap
# import java.util.Iterator
# import java.util.Map
# import java.util.Set
# import java.util.Stack
# import java.util.TreeSet
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.emf.ecore.resource.Resource.Diagnostic
# import org.eclipse.emf.ecore.resource.ResourceSet
# import org.eclipse.xtext.xbase.lib.IteratorExtensions

# from org.lflang.lf


#  * A registry to retrieve tests from, organized by target and category.
#  * 
#  * @author Marten Lohstroh <marten@berkeley.edu>
#
from lflang import Target, LFResourceProvider
import TestBase
from lflang.LFStandaloneSetup import LFStandaloneSetup
from lflang.lf import Reactor
from lflang.tests.LFTest import LFTest


class SimpleFileVisitor:
    pass


class TreeSet:
    pass


class Stack:
    def __init__(self):
        self._the_stack = []

    def peak(self):
        return self._the_stack[-1] if len(self._the_stack) > 0 else None

    def push(self, item):
        self._the_stack.append(item)

    def pop(self):
        r = None
        if len(self._the_stack) > 0:
            r = self._the_stack.pop()
        return r

    def clear(self):
        self._the_stack = []

    def __str__(self):
        return str(self._the_stack)


class TestRegistry:
    """ generated source for class TestRegistry """
    class TestMap:
        """ generated source for class TestMap """
            #           * Registry that maps targets to maps from categories to sets of tests.
        #           
        map = dict()

            #           * Create a new test map.
        #           
        def __init__(self):
            """ generated source for method __init__ """
            #  Populate the internal datastructures.
            for target in Target.values():
                categories = dict()
                for cat in super().TestCategory.values():
                    categories.put(cat, self.TreeSet())
                self.map.put(target, categories)

            #           * Return a set of tests given a target and test category.
        #           * @param t The target.
        #           * @param c The test category.
        #           * @return A set of tests for the given target and test category.
        #           
        def getTests(self, t, c):
            """ generated source for method getTests """
            return self.map.get(t).get(c)

    IGNORED_DIRECTORIES = ["failing", "knownfailed", "failed"]
    LF_REPO_PATH = os.getcwd()
    LF_TEST_PATH = LF_REPO_PATH.resolve("test")
    registered = TestMap()
    ignored = TestMap()
    allTargets = dict()
from enum import Enum
class TestCategory(Enum):
    """ generated source for enum TestCategory """
    CONCURRENT = True
    GENERIC = True
    GENERICS = True
    MULTIPORT = True
    FEDERATED = True
    PROPERTIES = True
    MODAL_MODELS = True
    DOCKER = True
    DOCKER_FEDERATED = True, "docker" + os.sep + "federated"
    SERIALIZATION = False
    ARDUINO = False, TestBase.TestLevel.BUILD
    TARGET = False

    @overloaded
    def __init__(self, isCommon):
        """ generated source for method __init__ """
        self.isCommon = isCommon
        self.path = self.name().lower()
        self.level = TestBase().TestLevel.EXECUTION

    @__init__.register(object, bool, TestBase().TestLevel)
    def __init___0(self, isCommon, level):
        """ generated source for method __init___0 """
        self.isCommon = isCommon
        self.path = self.name().lower()
        self.level = level

    @__init__.register(object, bool, str)
    def __init___1(self, isCommon, path, TestLevel=None):
        """ generated source for method __init___1 """
        self.isCommon = isCommon
        self.path = path
        self.level = TestLevel.EXECUTION

    def getPath(self):
        """ generated source for method getPath """
        return self.path

    def getHeader(self):
        """ generated source for method getHeader """
        return TestBase.THICK_LINE + "Category: " + self.name()

    rs = LFStandaloneSetup().createInjectorAndDoEMFRegistration().getInstance(LFResourceProvider.__class__).getResourceSet()
    LF_TEST_PATH = os.environ("LF_TEST_PATH")
    dir = LF_TEST_PATH.resolve(__name__.getDirectoryName()).resolve("src")

    @classmethod
    def initialize(cls):
        """ generated source for method initialize """

    @classmethod
    def getRegisteredTests(cls, target, category, copy):
        """ generated source for method getRegisteredTests """
        if copy:
            copies = TreeSet()
            for test in super().registered.getTests(target, category):
                copies.append(LFTest(test.target, test.srcFile))
            return copies
        else:
            return cls.registered.getTests(target, category)

    @classmethod
    def getIgnoredTests(cls, target, category):
        """ generated source for method getIgnoredTests """
        return cls.ignored.getTests(target, category)

    @classmethod
    def getCoverageReport(cls, target, category):
        """ generated source for method getCoverageReport """
        s = ""
        ignored = TestRegistry.getIgnoredTests(target, category)
        s += TestBase.THIN_LINE
        s += f"Ignored: {len(ignored)}\n"
        s += TestBase.THIN_LINE
        for test in ignored:
            s += f"No main reactor in: {test.name}\n"
        own = cls.getRegisteredTests(target, category, False)
        if category.isCommon:
            all = cls.allTargets.get(category)
            s += f"\n{TestBase.THIN_LINE}"
            s += f"Covered: {len(own)}/{len(all)}\n"
            s += TestBase.THIN_LINE
            missing = len(all) - len(own)
            if missing > 0:
                #             /*   all.stream().filter(test -> !own.contains(test))
                #                          .forEach(test -> s.append("Missing: ").append(test.toString()).append("\n")); */
                pass
        else:
            s += f"\n{TestBase.THIN_LINE}"
            s += f"Covered: {len(own)}/{len(own)}\n"
            s += TestBase.THIN_LINE
        return s

class TestDirVisitor(SimpleFileVisitor):
    """ generated source for class TestDirVisitor """
    stack = Stack()
    target = None
    rs = None
    srcBasePath = None

    SKIP_SUBTREE = 0
    CONTINUE = 1
    def __init__(self, rs, target, srcBasePath):
        """ generated source for method __init__ """
        super().__init__()
        self.stack.push(self.TestCategory.GENERIC)
        self.rs = rs
        self.target = target
        self.srcBasePath = srcBasePath

    def preVisitDirectory(self, dir, attrs):
        """ generated source for method preVisitDirectory """
        for ignored in super().IGNORED_DIRECTORIES:
            if dir.getFileName().__str__().lower() == self.ignored.lower():
                return self.SKIP_SUBTREE
        for category in super().TestCategory.values():
            relativePathName = self.srcBasePath.relativize(dir).__str__()
            if relativePathName.lower() == category.getPath.lower():
                self.stack.push(category)
        return self.CONTINUE

    def postVisitDirectory(self, dir, exc):
        """ generated source for method postVisitDirectory """
        for category in super().TestCategory.values():
            relativePathName = self.srcBasePath.relativize(dir).__str__()
            if relativePathName.lower() == category.getPath.lower():
                self.stack.pop()
        return self.CONTINUE

    def visitFile(self, path, attr):
        """ generated source for method visitFile """
        if attr.isRegularFile() and path.__str__().endsWith(".lf"):
            r = self.rs.getResource(super().URI.createFileURI(path.toFile().getAbsolutePath()), True)
            test = LFTest(self.target, path)
            errors = r.getErrors()
            if not errors.isEmpty():
                for d in errors:
                    test.issues.append(d.__str__())
                test.result = super().Result.PARSE_FAIL
            else:
                for it in r.getAllContents():
                    if it.__class__==Reactor.__class__:
                        #reactors = IteratorExtensions.filter(r.getAllContents(), Reactor.__class__)
                        if it.isMain() or it.isFederated():
                            self.ignored.getTests(self.target, self.stack.peek()).append(test)
                    return self.CONTINUE
            self.registered.getTests(self.target, self.stack.peek()).append(test)
        return self.CONTINUE

    def walk(self):
        """ generated source for method walk """
        self.walkFileTree(self.srcBasePath, self)
