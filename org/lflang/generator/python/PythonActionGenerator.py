#!/usr/bin/env python
""" generated source for module PythonActionGenerator """
# package: org.lflang.generator.python
from org.lflang.lf import Action

from org.lflang.lf import ReactorDecl

from org.lflang.generator.c import CGenerator

class PythonActionGenerator(object):
    """ generated source for class PythonActionGenerator """
    @classmethod
    def generateAliasTypeDef(cls, decl, action, genericActionType):
        """ generated source for method generateAliasTypeDef """
        return "typedef " + genericActionType + " " + CGenerator.variableStructType(action, decl) + ";"
