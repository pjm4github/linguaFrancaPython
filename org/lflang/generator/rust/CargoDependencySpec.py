#!/usr/bin/env python
""" generated source for module CargoDependencySpec """
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
# package: org.lflang.generator.rust
# import java.util.LinkedHashMap
# import java.util.List
# import java.util.Map
# import java.util.stream.Collectors
from include.overloading import overloaded

from org.lflang import ASTUtils

from org.lflang import TargetProperty

from org.lflang.TargetProperty import TargetPropertyType

from org.lflang.generator import InvalidLfSourceException

from org.lflang.lf import Array

from org.lflang.lf import Element

from org.lflang.lf import KeyValuePair

from org.lflang.util import StringUtil

from org.lflang.validation import LFValidator

# 
#  * Info about a cargo dependency. See {@link TargetProperty#CARGO_DEPENDENCIES}.
#  *
#  * @author Clément Fournier - TU Dresden, INSA Rennes
#  
class CargoDependencySpec(object):
    """ generated source for class CargoDependencySpec """
    version = None
    gitRepo = None
    rev = None
    gitTag = None
    localPath = None
    features = None

    def __init__(self, version, gitRepo, rev, gitTag, localPath, features):
        """ generated source for method __init__ """
        self.version = StringUtil.removeQuotes(version)
        self.gitRepo = gitRepo
        self.rev = rev
        self.gitTag = gitTag
        self.localPath = StringUtil.removeQuotes(localPath)
        self.features = features

    #  The version. May be null. 
    def getVersion(self):
        """ generated source for method getVersion """
        return self.version

    #  Local path to the crate. May be null. 
    def getLocalPath(self):
        """ generated source for method getLocalPath """
        return self.localPath

    #  Returns the git path. 
    def getGitRepo(self):
        """ generated source for method getGitRepo """
        return self.gitRepo

    #  Returns the revision number to use with git/localPath. 
    def getRev(self):
        """ generated source for method getRev """
        return self.rev

    def getTag(self):
        """ generated source for method getTag """
        return self.gitTag

    def setGitRepo(self, gitRepo):
        """ generated source for method setGitRepo """
        self.gitRepo = gitRepo
        if gitRepo != None:
            self.localPath = None

    def setRev(self, rev):
        """ generated source for method setRev """
        self.rev = rev

    def setLocalPath(self, localPath):
        """ generated source for method setLocalPath """
        self.localPath = localPath
        if localPath != None:
            self.gitRepo = None
            self.rev = None
            self.gitTag = None

    #  Returns the list of features that are enabled on the crate. May be null. 
    def getFeatures(self):
        """ generated source for method getFeatures """
        return self.features

    #      * Parse the given element. It must be a JSON map, whose
    #      * keys are dependency names, and values are {@link CargoDependencySpec}s.
    #      *
    #      * @throws InvalidLfSourceException If the element is somehow invalid
    #      
    @classmethod
    def parseAll(cls, element):
        """ generated source for method parseAll """
        result = {}
        if element.getKeyvalue() == None:
            raise InvalidLfSourceException(element, "Expected key-value pairs")
        for pair in element.getKeyvalue().getPairs():
            result.put(pair.__name__, parseValue(pair))
        return result

    @classmethod
    @overloaded
    def parseValue(cls, pair):
        """ generated source for method parseValue """
        #  note that we hardcode the value because RustEmitterBase is a
        #  kotlin class and we can't depend on it to use a constant.
        isRuntimeCrate = pair.__name__ == "reactor_rt"
        return cls.parseValue(pair.getValue(), isRuntimeCrate)

    #      * for values of the {@link TargetProperty#CARGO_DEPENDENCIES}
    #      * map.
    #      *
    #      * @throws InvalidLfSourceException If the element is somehow invalid
    #      
    @classmethod
    @parseValue.register(object, Element, bool)
    def parseValue_0(cls, element, isRuntimeCrate):
        """ generated source for method parseValue_0 """
        if element.getLiteral() != None:
            return CargoDependencySpec(element.getLiteral(), None, None, None, None, None)
        elif element.getKeyvalue() != None:
            version = None
            localPath = None
            gitRepo = None
            rev = None
            tag = None
            features = None
            for pair in element.getKeyvalue().getPairs():
                name = pair.__name__
                if "features" == name:
                    array = pair.getValue().getArray()
                    if array == None:
                        raise InvalidLfSourceException(pair.getValue(), "Expected an array of strings for key '" + name + "'")
                    cls.features = array.getElements().stream().map(ASTUtils.elementToSingleString).map(StringUtil.removeQuotes).collect(Collectors.toList())
                    continue 
                literal = pair.getValue().getLiteral()
                if literal == None:
                    raise InvalidLfSourceException(pair.getValue(), "Expected string literal for key '" + name + "'")
                if name == "version":
                    cls.version = literal
                elif name == "git":
                    cls.gitRepo = literal
                elif name == "rev":
                    cls.rev = literal
                elif name == "tag":
                    tag = literal
                elif name == "path":
                    cls.localPath = literal
                else:
                    raise InvalidLfSourceException(pair, "Unknown key: '" + name + "'")
            if isRuntimeCrate or cls.version != None or cls.localPath != None or cls.gitRepo != None:
                return CargoDependencySpec(cls.version, cls.gitRepo, cls.rev, tag, cls.localPath, cls.features)
            else:
                raise InvalidLfSourceException(element.getKeyvalue(), "Must specify one of 'version', 'path', or 'git'")
        raise InvalidLfSourceException(element, "Expected string or dictionary")

class CargoDependenciesPropertyType(TargetPropertyType):
    """ generated source for class CargoDependenciesPropertyType """
    INSTANCE = CargoDependenciesPropertyType()

    def __init__(self):
        """ generated source for method __init__ """
        super(CargoDependenciesPropertyType, self).__init__()

    def validate(self, e):
        """ generated source for method validate """
        return e.getKeyvalue() != None

    def check(self, element, name, v):
        """ generated source for method check """
        for pair in element.getKeyvalue().getPairs():
            try:
                self.parseValue(pair)
            except InvalidLfSourceException as e:
                v.getErrorReporter().reportError(e.getNode(), e.getProblem())

    def __str__(self):
        """ generated source for method toString """
        return "<cargo dependency spec>"

