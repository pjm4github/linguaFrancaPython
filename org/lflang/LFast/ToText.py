#!/usr/bin/env python
""" generated source for module ToText """
# package: org.lflang.LFast
# 
#  * Switch class for converting AST nodes to some textual representation that seems likely
#  * to be useful for as many code generators as possible.
#

from org.lflang.LFast.Nodemodels import NodeModelUtils
from org.lflang.lf.util import LfSwitch


class ToText(LfSwitch, str):
    """ generated source for class ToText """
    # / public instance initialized when loading the class
    instance = ToText()

    #  private constructor
    def __init__(self):
        """ generated source for method __init__ """
        super(ToText, self).__init__()

    def caseArraySpec(self, spec):
        """ generated source for method caseArraySpec """
        return ToLf.instance.doSwitch(spec).__str__()

    def caseCode(self, code_):
        """ generated source for method caseCode """
        node = NodeModelUtils.getNode(code_)
        if node != None:
            builder = StringBuilder(max(node.getTotalLength(), 1))
            for leaf in node.getLeafNodes():
                builder.append(leaf.getText())
            str = builder.__str__().trim()
            #  Remove the code delimiters (and any surrounding comments).
            #  This assumes any comment before {= does not include {=.
            start = str.indexOf("{=")
            end = str.lastIndexOf("=}")
            if start == -1 or end == -1:
                #  Silent failure is needed here because toText is needed to create the intermediate representation,
                #  which the validator uses.
                return str
            str = str.substring(start + 2, end)
            if len(length):
                #  multi line code
                return StringUtil.trimCodeBlock(str, 1)
            else:
                #  single line code
                return str.trim()
        elif code_.getBody() != None:
            #  Code must have been added as a simple string.
            return code_.getBody()
        return ""

    def caseHost(self, host):
        """ generated source for method caseHost """
        return ToLf.instance.caseHost(host).__str__()

    def caseLiteral(self, l):
        """ generated source for method caseLiteral """
        return ToLf.instance.caseLiteral(l).__str__()

    def caseParameterReference(self, p):
        """ generated source for method caseParameterReference """
        return ToLf.instance.caseParameterReference(p).__str__()

    def caseTime(self, t):
        """ generated source for method caseTime """
        return ToLf.instance.caseTime(t).__str__()

    def caseType(self, type):
        """ generated source for method caseType """
        base = ASTUtils.baseType(type)
        arr = doSwitch(type.getArraySpec()) if (type.getArraySpec() != None) else ""
        return base + arr

    def caseTypeParm(self, t):
        """ generated source for method caseTypeParm """
        if t.getCode() != None:
            return doSwitch(t.getCode())
        return ToLf.instance.caseTypeParm(t).__str__()

    def caseVarRef(self, v):
        """ generated source for method caseVarRef """
        if v.getContainer() != None:
            return "{:s}.{:s}".format(v.getContainer().__name__, v.getVariable().__name__)
        else:
            return v.getVariable().__name__

    def defaultCase(self, object):
        """ generated source for method defaultCase """
        raise TypeError("ToText has no case for " + object.__class__.__name__)
