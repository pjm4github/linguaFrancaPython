#!/usr/bin/env python
# C:\Users\pmora\Documents\Git\GitHub\lingua-franca\org.lflang\src\org\lflang\LFast\ToLf.java
""" generated source for module ToLf """
# package: org.lflang.LFast
# 
#  * Switch class for converting AST nodes to their textual representation as
#  * it would appear in LF code.
#

import re
from gc import collect

from MalleableString import Builder, Joiner
from include.SpecialExceptions import IllegalArgumentException
from lflang import ASTUtils
from lflang.LFast import ToText, MalleableString
from lflang.LFast.Nodemodels import NodeModelUtils
from lflang.lf import Visibility
from lflang.util import StringUtil
from org.lflang.lf.util import LfSwitch
from include.overloading import overloaded


class ICompositeNode:
    pass


class Collectors:
    pass


class ToLf(LfSwitch):
    """ generated source for class ToLf """
    KEEP_FORMAT_COMMENT = re.compile("\\s*(//|#)\\s*keep-format\\s*")

    # / public instance initialized when loading the class

    #  private constructor
    def __init__(self):
        """ generated source for method __init__ """
        #        super(ToLf, self).__init__()
        pass


    def caseArraySpec(self, spec):
        """ generated source for method caseArraySpec """
        if spec.isOfVariableLength():
            return MalleableString.anyOf("[]")
        return ["", "[", "]", False, False, spec.getLength()]

        #      @Override
        #      public MalleableString self.doSwitch(EObject eObject) {
    def doSwitch(self, eObject):

        #          ICompositeNode node = NodeModelUtils.findActualNodeFor(eObject);
        node = NodeModelUtils.findActualNodeFor(eObject)
        #          var ancestorComments = getAncestorComments(node);
        ancestorComments = self.getAncestorComments(node)
        #          Predicate doesNotBelongToAncestor = !ancestorComments.contains(n);
        doesNotBelongToAncestor = not ancestorComments.contains(node)
        #          List followingComments = getFollowingComments(
        #              node,
        #              ASTUtils.sameLine(node).and(doesNotBelongToAncestor)
        #          ).toList();
        followingComments = [self.getFollowingComments(node, ASTUtils.sameLine(node) and doesNotBelongToAncestor)]
        #          var previous = getNextCompositeSibling(node, "INode.getPreviousSibling");
        previous = self.getNextCompositeSibling(node, "INode.getPreviousSibling")
        #          Predicate doesNotBelongToPrevious = doesNotBelongToAncestor.and(
        #              previous == null ? true : ASTUtils.sameLine(previous).negate()
        #          );
        doesNotBelongToPrevious = doesNotBelongToAncestor and (True if previous == None else ASTUtils.sameLine(previous).negate())
        #          Stream precedingComments = ASTUtils.getPrecedingComments(
        #              node,
        #              doesNotBelongToPrevious
        #          ).map("String.strip");

        precedingComments = ASTUtils.getPrecedingComments(node, doesNotBelongToPrevious).strip()
        #          Collection allComments = new [];
        allComments = []
        #          precedingComments.forEachOrdered("allComments.add");
        for c in precedingComments:
            allComments.append(c)
        #          getContainedComments(node).stream()
        #              .filter(doesNotBelongToAncestor)
        #              .map("INode.getText")
        #              .forEachOrdered("allComments.add");

        for c in self.getContainedComments(node):
            if doesNotBelongToAncestor:
                allComments.append(c)


        #          allComments.extend([followingComments]);
        allComments.extend([followingComments])
        #          if (allComments.stream().anyMatch(KEEP_FORMAT_COMMENT.matcher(s).matches())) {
        #              return MalleableString.anyOf(StringUtil.trimCodeBlock(node.getText(), 0))
        #                  .addComments(followingComments.stream());
        #          }
        #          return super.doSwitch(eObject).addComments(allComments.stream());
        #      }
        for L in  allComments:
            if self.KEEP_FORMAT_COMMENT.match(L).groups():

                ss = node.getText()
                ms = ss.strip()
            return ms.addComments(followingComments)
        return self.doSwitch(eObject).addComments(allComments)


    @classmethod
    def getAncestorComments(cls, node):
        # Return all comments contained by ancestors of {@code node} that belong to
        # said ancestors.
        """ generated source for method getAncestorComments """
        ancestorComments = set()
        ancestor = node.getParent()
        while ancestor != None:
            ancestorComments.extend([cls.getContainedComments(ancestor)])
            from lflang import ASTUtils
            ASTUtils.getPrecedingCommentNodes(ancestor, True).forEachOrdered("ancestorComments.add")
            ancestor = ancestor.getParent()
        return ancestorComments


    @classmethod
    def getNextCompositeSibling(cls, node, getNextSibling):
        # Return the next composite sibling of {@code node}, as given by sequential
        # application of {@code getNextSibling}.
        """ generated source for method getNextCompositeSibling """
        sibling = node
        while sibling != None:
            pass
        #               if (
        #                   sibling instanceof ICompositeNode compositeSibling && !sibling.getText().isBlank()
        #               ) return compositeSibling;
        return None


    @classmethod
    def getFollowingNonCompositeSiblings(cls, node):
        # Return the siblings following {@code node} up to (and not including) the
        # next non-leaf sibling.
        """ generated source for method getFollowingNonCompositeSiblings """
        sibling = node
        ret = []
        while sibling != None and not sibling.instance(ICompositeNode):
            ret.append(sibling)
        return ret


    @classmethod
    def getFollowingComments(cls, node, filter):
        # Return comments that follow {@code node} in the source code and that
        # either satisfy {@code filter} or that cannot belong to any following
        # sibling of {@code node}.
        """ generated source for method getFollowingComments """
        sibling = cls.getNextCompositeSibling(node, "INode.getNextSibling")
        followingSiblingComments = cls.getFollowingNonCompositeSiblings(node).filter("ASTUtils.isComment").map("INode.getText")
        if sibling == None:
            return followingSiblingComments
        return followingSiblingComments + ASTUtils.getPrecedingComments(sibling, filter)

    @classmethod
    def getContainedComments(cls, node):
        #      /**
        # Return comments contained by {@code node} that logically belong to this
        # node (and not to any of its children).
        #       */
        """ generated source for method getContainedComments """
        ret = []
        inSemanticallyInsignificantLeadingRubbish = True
        for child in node.getAsTreeIterable():
            if not inSemanticallyInsignificantLeadingRubbish and ASTUtils.isComment(child):
                ret.append(child)
            elif not (isinstance(child, (ICompositeNode))) and not child.getText().isBlank():
                inSemanticallyInsignificantLeadingRubbish = False
            if not (isinstance(child, (ICompositeNode))) and (child.getText().contains("\n") or child.getText().contains("\r")) and not inSemanticallyInsignificantLeadingRubbish:
                break
        return ret

    def caseCode(self, code_):
        """ generated source for method caseCode """
        content = '\n'.join([l.strip() for l in code_])
        
        singleLineRepresentation = MalleableString.anyOf("{= {:s} =}".format(content.strip()))
        multilineRepresentation = Builder().append("{=\n".format()).append(MalleableString.anyOf(content).indent()).append("\n=}".format()).get()
        if content.lines().count() > 1 or content.contains("#") or content.contains("//"):
            return multilineRepresentation
        return MalleableString.anyOf(singleLineRepresentation, multilineRepresentation)

    def caseHost(self, host):
        """ generated source for method caseHost """
        msb = Builder()
        if not host.getUser():
            msb.append(host.getUser()).append("@")
        if not host.getAddr():
            msb.append(host.getAddr())
        if host.getPort() != 0:
            msb.append(":").append(host.getPort())
        return msb.get()

    def caseLiteral(self, l):
        #  STRING | CHAR_LIT | SignedFloat | SignedInt | Boolean
        """ generated source for method caseLiteral """
        return MalleableString.anyOf(l.getLiteral())

    def caseParameterReference(self, p):
        #  parameter=[Parameter]
        """ generated source for method caseParameterReference """
        return MalleableString.anyOf(p.getParameter().__name__)

    def caseAttribute(self, object):
        # '@' attrName=ID ('(' (attrParms+=AttrParm (',' attrParms+=AttrParm)* ','?)? ')')?
        """ generated source for method caseAttribute """
        builder = MalleableString.Builder().append("@").append(object.getAttrName())
        if object.getAttrParms() != None:
            builder.append(list(True, object.getAttrParms()))
        return builder.get()

    def caseAttrParm(self, object):
        #  (name=ID '=')? value=AttrParmValue;
        """ generated source for method caseAttrParm """
        builder = Builder()
        if object.__name__ != None:
            builder.append(object.__name__).append(" = ")
        return builder.append(self.doSwitch(object.getValue())).get()

    def caseAttrParmValue(self, object):
        """ generated source for method caseAttrParmValue """
        #  str=STRING
        #      | int=SignedInt
        #      | bool=Boolean
        #      | float=SignedFloat
        if object.getStr() != None:
            return MalleableString.anyOf(StringUtil.addDoubleQuotes(object.getStr()))
        if object.getInt() != None:
            return MalleableString.anyOf(object.getInt())
        if object.getBool() != None:
            return MalleableString.anyOf(object.getBool())
        if object.getFloat() != None:
            return MalleableString.anyOf(object.getFloat())
        raise IllegalArgumentException("The attributes of an AttrParmValue should not all be null.")

    def caseTime(self, t):
        # (interval=INT unit=TimeUnit)
        """ generated source for method caseTime """
        return MalleableString.anyOf(ASTUtils.toTimeValue(t).__str__())

    def caseType(self, type):
        # // time?='time' (arraySpec=ArraySpec)?
        #          // | id=DottedName ('<' typeParms+=Type (',' typeParms+=Type)* '>')? (stars+='*')*
        #          //     (arraySpec=ArraySpec)?
        #          // | code=Code
        """ generated source for method caseType """
        if type.getCode() != None:
            return self.doSwitch(type.getCode())
        msb = Builder()
        if type.isTime():
            msb.append("time")
        elif type.getId() != None:
            msb.append(type.getId())
            if type.getTypeParms() != None:
                msb.append(list(", ", "<", ">", True, False, type.getTypeParms()))
            msb.append("*".repeat(type.getStars().size()))
        if type.getArraySpec() != None:
            msb.append(self.doSwitch(type.getArraySpec()))
        return msb.get()

    def caseTypeParm(self, t):
        """ generated source for method caseTypeParm """
        # literal=TypeExpr | code=Code
        return MalleableString.anyOf(MalleableString.anyOf(t.getLiteral()) if not t.getLiteral() else self.doSwitch(t.getCode()))

    def casevarRef(self, v):
        """ generated source for method caseself.varRef """
        #          // variable=[Variable] | container=[Instantiation] '.' variable=[Variable]
        #          // | interleaved?='interleaved' '(' (variable=[Variable] | container=[Instantiation] '.'
        #          //     variable=[Variable]) ')'
        if not v.isInterleaved():
            return MalleableString.anyOf(ToText.instance.doSwitch(v))
        return Builder().append("interleaved ").append(list(False, ToText.instance.doSwitch(v))).get()

    def caseModel(self, object):
        """ generated source for method caseModel """
        #          // target=TargetDecl
        #          // (imports+=Import)*
        #          // (preambles+=Preamble)*
        #          // (reactors+=Reactor)+
        msb = Builder()
        msb.append(self.doSwitch(object.getTarget())).append("\n".repeat(2))
        for i in object.getImports():
            msb.append(self.doSwitch(i)).append("\n")
        if not object.getImports().isEmpty():
            msb.append("\n")
        for p in object.getPreambles():
            msb.append(self.doSwitch(p)).append("\n".repeat(2))
        msb.append(object.getReactors().stream().map("this.doSwitch").collect(Joiner("\n".repeat(2)))).append("\n")
        return msb.get()

    def caseImport(self, object):
        # // 'import' reactorClasses+=ImportedReactor (',' reactorClasses+=ImportedReactor)*
        #          //     'from' importURI=STRING ';'?
        #          // TODO: Break this. Break string, break at whitespace outside the string.
        """ generated source for method caseImport """
        return Builder().append("import ").append(list(", ", "", "", False, True, object.getReactorClasses())).append(" from \"").append(object.getImportURI()).append("\"").get()

    def caseReactorDecl(self, object):
        # // Reactor | ImportedReactor
        """ generated source for method caseReactorDecl """
        return self.defaultCase(object)

    def caseImportedReactor(self, object):
        # // reactorClass=[Reactor] ('as' name=ID)?
        """ generated source for method caseImportedReactor """
        if object.__name__ != None:
            return MalleableString.anyOf("{:s} as {:s}".format(object.getReactorClass().__name__, object.__name__))
        return MalleableString.anyOf(object.getReactorClass().__name__)

    def caseReactor(self, object):
        #          // {Reactor} ((federated?='federated' | main?='main')? & realtime?='realtime'?)
        #          //     'reactor' (name=ID)?
        #          // ('<' typeParms+=TypeParm (',' typeParms+=TypeParm)* '>')?
        #          // ('(' parameters+=Parameter (',' parameters+=Parameter)* ')')?
        #          // ('at' host=Host)?
        #          // ('extends' (superClasses+=[ReactorDecl] (',' superClasses+=[ReactorDecl])*))?
        #          // '{'
        #          // (     (preambles+=Preamble)
        #          //     | (stateVars+=StateVar)
        #          //     | (methods+=Method)
        #          //     | (inputs+=Input)
        #          //     | (outputs+=Output)
        #          //     | (timers+=Timer)
        #          //     | (actions+=Action)
        #          //     | (instantiations+=Instantiation)
        #          //     | (connections+=Connection)
        #          //     | (reactions+=Reaction)
        #          //     | (modes+=Mode)
        #          //     | (mutations+=Mutation)
        #          // )* '}
        """ generated source for method caseReactor """
        msb = Builder()
        self.addAttributes(msb, "object.getAttributes")
        msb.append(self.reactorHeader(object))
        smallFeatures = self.indentedStatements(list(object.getPreambles(), object.getInputs(), object.getOutputs(), object.getTimers(), object.getActions(), object.getInstantiations(), object.getConnections(), object.getStateVars()), False)
        bigFeatures = self.indentedStatements(list(object.getReactions(), object.getMethods(), object.getModes()), True)
        msb.append(smallFeatures)
        if not smallFeatures.isEmpty() and not bigFeatures.isEmpty():
            msb.append("\n".repeat(1))
        msb.append(bigFeatures)
        msb.append("}")
        return msb.get()

    def reactorHeader(self, object):
        """ generated source for method reactorHeader """
        # /** Return the signature of the given reactor. */
        msb = Builder()
        if object.isFederated():
            msb.append("federated ")
        if object.isMain():
            msb.append("main ")
        if object.isRealtime():
            msb.append("realtime ")
        msb.append("reactor")
        if object.__name__ != None:
            msb.append(" ").append(object.__name__)
        msb.append(list(", ", "<", ">", True, False, object.getTypeParms()))
        msb.append(list(True, object.getParameters()))
        if object.getHost() != None:
            msb.append(" at ").append(self.doSwitch(object.getHost()))
        if object.getSuperClasses() != None and not object.getSuperClasses().isEmpty():
            msb.append(MalleableString.anyOf(" extends "), Builder().append("\n").
                       append(MalleableString.anyOf("extends ").indent().indent()).get()).\
                append(object.getSuperClasses().stream().map("ReactorDecl.getName").collect(Collectors.joining(", ")))
        msb.append(" {\n".format())
        return msb.get()

    def caseTargetDecl(self, object):
        """ generated source for method caseTargetDecl """
        # // 'target' name=ID (config=KeyValuePairs)? ';'?
        msb = Builder()
        msb.append("target ").append(object.__name__)
        if object.getConfig() != None and not object.getConfig().getPairs().isEmpty():
            msb.append(" ").append(self.doSwitch(object.getConfig()))
        return msb.get()

    def caseStateVar(self, object):
        """ generated source for method caseStateVar """
        #          // 'state' name=ID (
        #          //     (':' (type=Type))?
        #          //     ((parens+='(' (init+=Expression (','  init+=Expression)*)? parens+=')')
        #          //         | (braces+='{' (init+=Expression (','  init+=Expression)*)? braces+='}')
        #          //     )?
        #          // ) ';'?

        msb = Builder()
        self.addAttributes(msb, "object.getAttributes")
        if object.isReset():
            msb.append("reset ")
        msb.append("state ").append(object.__name__)
        msb.append(self.typeAnnotationFor(object.getType()))
        if not object.getParens().isEmpty():
            msb.append(list(True, object.getInit()))
        if not object.getBraces().isEmpty():
            msb.append(list(", ", "{", "}", True, False, object.getInit()))
        return msb.get()

    def caseMethod(self, object):
        """ generated source for method caseMethod """
        #          // const?='const'? 'method' name=ID
        #          // '(' (arguments+=MethodArgument (',' arguments+=MethodArgument)*)? ')'
        #          // (':' return=Type)?
        #          // code=Code
        #          // ';'?
        msb = Builder()
        if object.isConst():
            msb.append("const ")
        msb.append("method ").append(object.__name__)
        msb.append(list(False, object.getArguments()))
        msb.append(self.typeAnnotationFor(object.getReturn())).append(" ").append(self.doSwitch(object.getCode()))
        return msb.get()

    def caseMethodArgument(self, object):
        #  // name=ID (':' type=Type)?
        """ generated source for method caseMethodArgument """
        return Builder().append(object.__name__).append(self.typeAnnotationFor(object.getType())).get()

    def caseInput(self, object):
        # // mutable?='mutable'? 'input' (widthSpec=WidthSpec)? name=ID (':' type=Type)? ';'?
        """ generated source for method caseInput """
        msb = Builder()
        self.addAttributes(msb, "object.getAttributes")
        if object.isMutable():
            msb.append("mutable ")
        msb.append("input")
        if object.getWidthSpec() != None:
            msb.append(self.doSwitch(object.getWidthSpec()))
        msb.append(" ").append(object.__name__).append(self.typeAnnotationFor(object.getType()))
        return msb.get()

    def caseOutput(self, object):
        # // 'output' (widthSpec=WidthSpec)? name=ID (':' type=Type)? ';'?
        """ generated source for method caseOutput """
        msb = Builder()
        self.addAttributes(msb, "object.getAttributes")
        msb.append("output")
        if object.getWidthSpec() != None:
            msb.append(self.doSwitch(object.getWidthSpec()))
        msb.append(" ").append(object.__name__)
        msb.append(self.typeAnnotationFor(object.getType()))
        return msb.get()

    def caseTimer(self, object):
        #          // 'timer' name=ID ('(' offset=Expression (',' period=Expression)? ')')? ';'?
        """ generated source for method caseTimer """
        builder = Builder()
        self.addAttributes(builder, "object.getAttributes")
        return builder.append("timer ").append(object.__name__).append(list(True, object.getOffset(), object.getPeriod())).get()

    def caseMode(self, object):
        #          // {Mode} (initial?='initial')? 'mode' (name=ID)?
        #          // '{' (
        #          //     (stateVars+=StateVar) |
        #          //     (timers+=Timer) |
        #          //     (actions+=Action) |
        #          //     (instantiations+=Instantiation) |
        #          //     (connections+=Connection) |
        #          //     (reactions+=Reaction)
        #          // )* '}'
        """ generated source for method caseMode """
        msb = Builder()
        if object.isInitial():
            msb.append("initial ")
        msb.append("mode ")
        if object.__name__ != None:
            msb.append(object.__name__).append(" ")
        msb.append("{\n".format())
        msb.append(self.indentedStatements(list(object.getStateVars(), object.getTimers(), object.getActions(), object.getInstantiations(), object.getConnections()), False))
        msb.append(self.indentedStatements(list(object.getReactions()), True))
        msb.append("}")
        return msb.get()

    def caseAction(self, object):
        #          // (origin=ActionOrigin)? 'action' name=ID
        #          // ('(' minDelay=Expression (',' minSpacing=Expression (',' policy=STRING)? )? ')')?
        #          // (':' type=Type)? ';'?
        """ generated source for method caseAction """
        msb = Builder()
        self.addAttributes(msb, "object.getAttributes")
        if object.getOrigin() != None:
            msb.append(object.getOrigin().getLiteral()).append(" ")
        return msb.append("action ").append(object.__name__).append(list(True, object.getMinDelay(), object.getMinSpacing(), "\"{:s}\"".format(object.getPolicy()) if object.getPolicy() != None else None)).append(self.typeAnnotationFor(object.getType())).get()

    def caseReaction(self, object):
        #          // ('reaction')
        #          // ('(' (triggers+=TriggerRef (',' triggers+=TriggerRef)*)? ')')?
        #          // (sources+=self.varRef (',' sources+=self.varRef)*)?
        #          // ('->' effects+=self.varRefOrModeTransition (',' effects+=self.varRefOrModeTransition)*)?
        #          // code=Code
        #          // (stp=STP)?
        #          // (deadline=Deadline)?
        """ generated source for method caseReaction """
        msb = Builder()
        self.addAttributes(msb, "object.getAttributes")
        if object.isMutation():
            msb.append("mutation")
        else:
            msb.append("reaction")
        msb.append(list(True, object.getTriggers()))
        msb.append(list(", ", " ", "", True, False, object.getSources()))
        if not object.getEffects().isEmpty():
            allModes = ASTUtils.allModes(ASTUtils.getEnclosingReactor(object))
            # msb.append(" -> ", " ->\n").\
            #     append(object.getEffects().stream().map(Builder().append(self.varRef.getTransition()).\
            #                                             append("(").append(self.doSwitch(self.varRef)).append(")").\
            #                                             get() if (allModes.stream().anyMatch(m.__name__ == self.varRef.getVariable(.__name__))) else self.doSwitch(self.varRef)).\
            #         collect(Joiner(", ")))
        msb.append(" ").append(self.doSwitch(object.getCode()))
        if object.getStp() != None:
            msb.append(" ").append(self.doSwitch(object.getStp()))
        if object.getDeadline() != None:
            msb.append(" ").append(self.doSwitch(object.getDeadline()))
        return msb.get()

    def caseTriggerRef(self, object):
        # // BuiltinTriggerRef | self.varRef
        """ generated source for method caseTriggerRef """
        raise TypeError("TriggerRefs are BuiltinTriggerRefs or self.varRefs, so the methods " + "corresponding to those types should be invoked instead.")

    def caseBuiltinTriggerRef(self, object):
        #   // type = BuiltinTrigger
        """ generated source for method caseBuiltinTriggerRef """
        return MalleableString.anyOf(object.getType().getLiteral())

    def caseDeadline(self, object):
        #  // 'deadline' '(' delay=Expression ')' code=Code
        """ generated source for method caseDeadline """
        return self.handler(object, "deadline", "Deadline.getDelay", "Deadline.getCode")

    def caseSTP(self, object):
        # // 'STP' '(' value=Expression ')' code=Code
        """ generated source for method caseSTP """
        return self.handler(object, "STP", "STP.getValue", "STP.getCode")

    def handler(self, object, name, getTrigger, getCode):
        """ generated source for method handler """
        return Builder().append(name).append(list(False, getTrigger.apply(object))).append(" ").append(self.doSwitch(getCode.apply(object))).get()

    def casePreamble(self, object):
        #  // (visibility=Visibility)? 'preamble' code=Code
        """ generated source for method casePreamble """
        msb = Builder()
        if object.getVisibility() != None and object.getVisibility() != Visibility.NONE:
            msb.append(object.getVisibility().getLiteral()).append(" ")
        return msb.append("preamble ").append(self.doSwitch(object.getCode())).get()

    def caseInstantiation(self, object):
        #          // name=ID '=' 'new' (widthSpec=WidthSpec)?
        #          // reactorClass=[ReactorDecl] ('<' typeParms+=TypeParm (',' typeParms+=TypeParm)* '>')? '('
        #          // (parameters+=Assignment (',' parameters+=Assignment)*)?
        #          // ')' ('at' host=Host)? ';'?;
        """ generated source for method caseInstantiation """
        msb = Builder()
        msb.append(object.__name__).append(" = new")
        if object.getWidthSpec() != None:
            msb.append(self.doSwitch(object.getWidthSpec()))
        msb.append(" ").append(object.getReactorClass().__name__)
        msb.append(list(", ", "<", ">", True, False, object.getTypeParms()))
        msb.append(list(False, object.getParameters()))
        if object.getHost() != None:
            msb.append(" at ").append(self.doSwitch(object.getHost()))
        return msb.get()

    def caseConnection(self, object):
        #          // ((leftPorts += self.varRef (',' leftPorts += self.varRef)*)
        #          //     | ( '(' leftPorts += self.varRef (',' leftPorts += self.varRef)* ')' iterated ?= '+'?))
        #          // ('->' | physical?='~>')
        #          // rightPorts += self.varRef (',' rightPorts += self.varRef)*
        #          //     ('after' delay=Expression)?
        #          // (serializer=Serializer)?
        #          // ';'?

        """ generated source for method caseConnection """
        msb = Builder()
        if object.isIterated():
            msb.append(list(False, object.getLeftPorts())).append("+")
        else:
            msb.append(object.getLeftPorts().stream().map("this.doSwitch").collect(Joiner(", ")), object.getLeftPorts().stream().map("this.doSwitch").collect(Joiner(",\n".format())))
        msb.append("", MalleableString.anyOf("\n").indent())
        msb.append(" ~>" if object.isPhysical() else " ->")
        msb.append(self.minimallyDelimitedList(object.getRightPorts()))
        if object.getDelay() != None:
            msb.append(" after ").append(self.doSwitch(object.getDelay()))
        if object.getSerializer() != None:
            msb.append(" ").append(self.doSwitch(object.getSerializer()))
        return msb.get()

    def minimallyDelimitedList(self, items):
        """ generated source for method minimallyDelimitedList """
        return MalleableString.anyOf(list(", ", " ", "", True, True, items), Builder().append("\n".format()).append(list(",\n".format(), "", "", True, True, items).indent()).get())

    def caseSerializer(self, object):
        #  // 'serializer' type=STRING
        """ generated source for method caseSerializer """
        return Builder().append("serializer \"").append(object.getType()).append("\"").get()

    def caseKeyValuePairs(self, object):
        # // {KeyValuePairs} '{' (pairs+=KeyValuePair (',' (pairs+=KeyValuePair))* ','?)? '}'
        """ generated source for method caseKeyValuePairs """
        if object.getPairs().isEmpty():
            return MalleableString.anyOf("")
        return Builder().append("{\n").append(list(",\n", "", "\n", True, True, object.getPairs()).indent()).append("}").get()

    def caseKeyValuePair(self, object):
        #          // name=Kebab ':' value=Element
        """ generated source for method caseKeyValuePair """
        return Builder().append(object.__name__).append(": ").append(self.doSwitch(object.getValue())).get()

    def caseArray(self, object):
        #          // '[' elements+=Element (',' (elements+=Element))* ','? ']'
        """ generated source for method caseArray """
        return list(", ", "[", "]", False, False, object.getElements())

    def caseElement(self, object):
        #          // keyvalue=KeyValuePairs
        #          // | array=Array
        #          // | literal=Literal
        #          // | (time=INT unit=TimeUnit)
        #          // | id=Path
        """ generated source for method caseElement """
        if object.getKeyvalue() != None:
            return self.doSwitch(object.getKeyvalue())
        if object.getArray() != None:
            return self.doSwitch(object.getArray())
        if object.getLiteral() != None:
            return MalleableString.anyOf(object.getLiteral())
        if object.getId() != None:
            return MalleableString.anyOf(object.getId())
        if object.getUnit() != None:
            return MalleableString.anyOf("{:d} {:s}".format(object.getTime(), object.getUnit()))
        return MalleableString.anyOf(str(object.getTime()))

    def caseTypedVariable(self, object):
        # // Port | Action
        """ generated source for method caseTypedVariable """
        return self.defaultCase(object)

    def caseVariable(self, object):
        #    // TypedVariable | Timer | Mode
        """ generated source for method caseVariable """
        return self.defaultCase(object)

    def caseAssignment(self, object):
        #         // (lhs=[Parameter] (
        #         //     (equals='=' rhs+=Expression)
        #         //     | ((equals='=')? (
        #         //         parens+='(' (rhs+=Expression (',' rhs+=Expression)*)? parens+=')'
        #         //         | braces+='{' (rhs+=Expression (',' rhs+=Expression)*)? braces+='}'))
        #         // ));
        """ generated source for method caseAssignment """
        msb = Builder()
        msb.append(object.getLhs().__name__)
        if object.getEquals() != None:
            msb.append(" = ")
        prefix = ""
        suffix = ""
        if not object.getParens().isEmpty():
            prefix = "("
            suffix = ")"
        elif not object.getBraces().isEmpty():
            prefix = "{"
            suffix = "}"
        msb.append(list(", ", prefix, suffix, False, prefix.isBlank(), object.getRhs()))
        return msb.get()

    def caseParameter(self, object):
        #          // name=ID (':' (type=Type))?
        #          // ((parens+='(' (init+=Expression (','  init+=Expression)*)? parens+=')')
        #          // | (braces+='{' (init+=Expression (','  init+=Expression)*)? braces+='}')
        #          // )?
        """ generated source for method caseParameter """
        builder = Builder()
        self.addAttributes(builder, "object.getAttributes")
        return builder.append(object.__name__).append(self.typeAnnotationFor(object.getType())).append(list(", ", "(" if object.getBraces().isEmpty() else "{", ")" if object.getBraces().isEmpty() else "}", True, False, object.getInit())).get()

    def caseExpression(self, object):
        #        // {Literal} literal = Literal
        #          // | Time
        #          // | ParameterReference
        #          // | Code
        """ generated source for method caseExpression """
        return self.defaultCase(object)

    def casePort(self, object):
        #  // Input | Output
        """ generated source for method casePort """
        return self.defaultCase(object)

    def caseWidthSpec(self, object):
        #         // ofVariableLength?='[]' | '[' (terms+=WidthTerm) ('+' terms+=WidthTerm)* ']';
        """ generated source for method caseWidthSpec """
        if object.isOfVariableLength():
            return MalleableString.anyOf("[]")
        return list(" + ", "[", "]", False, False, object.getTerms())

    def caseWidthTerm(self, object):
        #          // width=INT
        #          // | parameter=[Parameter]
        #          // | 'widthof(' port=self.varRef ')'
        #          // | code=Code;
        """ generated source for method caseWidthTerm """
        if object.getWidth() != 0:
            return MalleableString.anyOf(object.getWidth())
        elif object.getParameter() != None:
            return MalleableString.anyOf(object.getParameter().__name__)
        elif object.getPort() != None:
            return Builder().append("widthof").append(list(False, object.getPort())).get()
        elif object.getCode() != None:
            return self.doSwitch(object.getCode())
        raise IllegalArgumentException("A WidthTerm should not be totally nullish/zeroish.")

    def caseIPV4Host(self, object):
        #         // (user=Kebab '@')? addr=IPV4Addr (':' port=INT)?
        """ generated source for method caseIPV4Host """
        return self.caseHost(object)

    def caseIPV6Host(self, object):
        #          // ('[' (user=Kebab '@')? addr=IPV6Addr ']' (':' port=INT)?)
        """ generated source for method caseIPV6Host """
        return self.caseHost(object)

    def caseNamedHost(self, object):
        #          // (user=Kebab '@')? addr=HostName (':' port=INT)?
        """ generated source for method caseNamedHost """
        return self.caseHost(object)

    def defaultCase(self, object):
        """ generated source for method defaultCase """
        raise TypeError("ToText has no case for {:s} or any of its supertypes, or it does have such a case, but the return value of that case was null.".format(object.__class__.__name__))

    @overloaded
    def list(self, separator, prefix, suffix, nothingIfEmpty, whitespaceRigid, items):
        #  /**
        # Represent the given EList as a string.
        # @param suffix The token marking the end of the list.
        # @param separator The separator separating elements of the list.
        # @param prefix The token marking the start of the list.
        # @param nothingIfEmpty Whether the result should be simplified to the
        # empty string as opposed to just the prefix and suffix.
        # @param whitespaceRigid Whether any whitespace appearing in the
        #       */
        """ generated source for method list """
        return self.list(separator, prefix, suffix, nothingIfEmpty, whitespaceRigid, items.toArray("EObject[].new"))

    @list.register(object, str, str, str, bool, bool, ...)
    def list_0(self, separator, prefix, suffix, nothingIfEmpty, whitespaceRigid, *items):
        """ generated source for method list_0 """
        if nothingIfEmpty and items.allMatch("Objects.isNull"):
            return MalleableString.anyOf("")
        # //          MalleableString rigid = Arrays.stream(items).sequential()
        # //              .filter("Objects.nonNull")
        # //              .map({
        # //                  if (it instanceof MalleableString ms) return ms;
        # //                  if (it instanceof EObject eObject) return self.doSwitch(eObject);
        # //                  return MalleableString.anyOf(Objects.toString(it));
        # //              }).collect(new Joiner(separator, prefix, suffix));
        if whitespaceRigid:
            return self.rigid
        return MalleableString.anyOf(self.rigid, Builder().append(prefix.stripTrailing() + "\n").append(self.list(separator.strip() + "\n", "", "\n", nothingIfEmpty, True, items).indent()).append(suffix.stripLeading()).get())

    @list.register(object, bool, list)
    def list_1(self, nothingIfEmpty, items):
        """ generated source for method list_1 """
        return self.list(", ", "(", ")", nothingIfEmpty, False, items)

    @list.register(object, bool, ...)
    def list_2(self, nothingIfEmpty, *items):
        """ generated source for method list_2 """
        return self.list(", ", "(", ")", nothingIfEmpty, False, items)

    def typeAnnotationFor(self, type):
        """ generated source for method self.typeAnnotationFor """
        if type == None:
            return MalleableString.anyOf("")
        return Builder().append(": ").append(self.doSwitch(type)).get()

    def addAttributes(self, builder, getAttributes):
        """ generated source for method self.addAttributes """
        if getAttributes.get() == None:
            return
        for attribute in getAttributes.get():
            builder.append(self.doSwitch(attribute)).append("\n")

    def indentedStatements(self, statementListList, forceWhitespace):
        #      /**
        # Represent a list of groups of statements.
        # @param statementListList A list of groups of statements.
        # @param forceWhitespace Whether to force a line of vertical whitespace
        # regardless of textual input
        # @return A string representation of {@code statementListList}.
        #       */
        """ generated source for method indentedStatements """

        #sorted = statementListList.stream().flatMap("List.stream").sorted(Comparator.comparing(NodeModelUtils.getNode(object).getStartLine())).toList()
        sorts = sorted([s.getstartLine() for s in statementListList])
        if not sorts:
            return MalleableString.anyOf("")
        ret = Builder()
        first = True
        for object in sorts:
            if not first:
                node = NodeModelUtils.getNode(object)
                leadingText = ""
                if not forceWhitespace:
                    for n in node.getAsTreeIterable():
                        if n.instance(ICompositeNode):
                            continue 
                        if not ASTUtils.isComment(n) and not n.getText().isBlank():
                            break
                        leadingText.append(n.getText())
                hasLeadingBlankLines = leadingText.__str__().lines().skip(1).filter("String.isBlank").count() > 1
                ret.append("\n".repeat(2 if forceWhitespace or hasLeadingBlankLines else 1))
            ret.append(self.doSwitch(object))
            first = False
        return ret.append("\n").get().indent()
