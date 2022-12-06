#!/usr/bin/env python
""" generated source for module IsEqual """
# package: org.lflang.LFast
# 
#  * Switch class that checks if subtrees of the AST are semantically equivalent
#  * to each other. Return {@code false} if they are not equivalent; return
#  * {@code true} or {@code false} (but preferably {@code true}) if they are
#  * equivalent.
#
import re
from include.SpecialExceptions import IllegalArgumentError, IllegalArgumentException
from pyclbr import Function

from include.overloading import overloaded
from org.lflang.lf.util.LfSwitch import LfSwitch
from org.lflang.lf import Action
from org.lflang.lf import ActionOrigin
from org.lflang.lf import Array
from org.lflang.lf import ArraySpec
from org.lflang.lf import Assignment
from org.lflang.lf import AttrParm
from org.lflang.lf import AttrParmValue
from org.lflang.lf import Attribute
from org.lflang.lf import BuiltinTrigger
from org.lflang.lf import BuiltinTriggerRef
from org.lflang.lf import LFCode
from org.lflang.lf import Connection
from org.lflang.lf import Deadline
from org.lflang.lf import Element
from org.lflang.lf import Expression
from org.lflang.lf import Host
from org.lflang.lf import IPV4Host
from org.lflang.lf import IPV6Host
from org.lflang.lf import Import
from org.lflang.lf import ImportedReactor
from org.lflang.lf import Input
from org.lflang.lf import Instantiation
from org.lflang.lf import KeyValuePair
from org.lflang.lf import KeyValuePairs
from org.lflang.lf import LfFactory
from org.lflang.lf import LfPackage
from org.lflang.lf import Literal
from org.lflang.lf import Method
from org.lflang.lf import MethodArgument
from org.lflang.lf import Mode
from org.lflang.lf import ModeTransition
from org.lflang.lf import Model
from org.lflang.lf import NamedHost
from org.lflang.lf import Output
from org.lflang.lf import Parameter
from org.lflang.lf import ParameterReference
from org.lflang.lf import Port
from org.lflang.lf import Preamble
from org.lflang.lf import Reaction
from org.lflang.lf import Reactor
from org.lflang.lf import ReactorDecl
from org.lflang.lf import STP
from org.lflang.lf import Serializer
from org.lflang.lf import StateVar
from org.lflang.lf import TargetDecl
from org.lflang.lf import Time
from org.lflang.lf import Timer
from org.lflang.lf import TriggerRef
from org.lflang.lf import Type
from org.lflang.lf import TypeParm
from org.lflang.lf import TypedVariable
from org.lflang.lf import VarRef
from org.lflang.lf import Variable
from org.lflang.lf import Visibility
from org.lflang.lf import WidthSpec
from org.lflang.lf import WidthTerm

class IsEqual(LfSwitch):
    """ generated source for class IsEqual """

    @overloaded
    def __init__(self, other):
        """ generated source for method __init__ """
        super(IsEqual, self).__init__()
        self.otherObject = other
        self.conclusion = False

    @__init__.register(object, Function, Function)
    def __init___0(self, propertyGetter, projectionToClassRepresentatives):
        """ generated source for method __init___0 """
        super(IsEqual, self).__init__()
        if propertyGetter.apply(object).instance(self.otherObject):
            raise IllegalArgumentException("EObjects should be compared for semantic equivalence, not object equality.")
        propertyGetter = projectionToClassRepresentatives.compose(propertyGetter)
        if self.conclusion:
            self.conclusion = self.otherObject == propertyGetter.apply(object, propertyGetter.apply(self.otherObject))
        return self

    def doSwitch(self, eObject):
        """ generated source for method doSwitch """
        if self.otherObject == eObject:
            return True
        if eObject == None:
            return False
        return super(IsEqual, self).doSwitch(eObject)

    def caseModel(self, object):
        """ generated source for method caseModel """
        return ComparisonMachine(object, Model.__class__).\
            equivalent("Model.getTarget").\
            listsEquivalent("Model.getImports").\
            listsEquivalent("Model.getPreambles").\
            listsEquivalent("Model.getReactors").\
            conclusion

    def caseImport(self, object):
        """ generated source for method caseImport """
        return ComparisonMachine(object, Import.__class__).\
            equalAsObjects("Import.getImportURI").\
            listsEquivalent("Import.getReactorClasses").\
            conclusion

    def caseReactorDecl(self, object):
        """ generated source for method caseReactorDecl """
        return ComparisonMachine(object, ReactorDecl.__class__).\
            equalAsObjects("ReactorDecl.getName").\
            conclusion

    def caseImportedReactor(self, object):
        """ generated source for method caseImportedReactor """
        return ComparisonMachine(object, ImportedReactor.__class__).\
            equalAsObjects("ImportedReactor.getName").\
            equivalent("ImportedReactor.getReactorClass").\
            conclusion

    def caseReactor(self, object):
        """ generated source for method caseReactor """
        return ComparisonMachine(object, Reactor.__class__).\
            listsEquivalent("Reactor.getAttributes").\
            equalAsObjects("Reactor.isFederated").\
            equalAsObjects("Reactor.isRealtime").\
            equalAsObjects("Reactor.isMain").\
            equalAsObjects("Reactor.getName").\
            listsEquivalent("Reactor.getTypeParms").\
            listsEquivalent("Reactor.getParameters").\
            equivalent("Reactor.getHost").\
            listsEquivalent("Reactor.getSuperClasses").\
            listsEquivalent("Reactor.getPreambles").\
            listsEquivalent("Reactor.getInputs").\
            listsEquivalent("Reactor.getOutputs").\
            listsEquivalent("Reactor.getTimers").\
            listsEquivalent("Reactor.getActions").\
            listsEquivalent("Reactor.getInstantiations").\
            listsEquivalent("Reactor.getConnections").\
            listsEquivalent("Reactor.getStateVars").\
            listsEquivalent("Reactor.getReactions").\
            listsEquivalent("Reactor.getMethods").\
            listsEquivalent("Reactor.getModes").\
            conclusion

    def caseTypeParm(self, object):
        """ generated source for method caseTypeParm """
        return ComparisonMachine(object, TypeParm.__class__).\
            equalAsObjects("TypeParm.getLiteral").\
            equivalent("TypeParm.getCode").\
            conclusion

    def caseTargetDecl(self, object):
        """ generated source for method caseTargetDecl """
        r = None
        for it in ComparisonMachine(object, TargetDecl.__class__).\
                equalAsObjects("TargetDecl.getName").\
                equivalentModulo("TargetDecl.getConfig"):
            v = None if (it != None and it.getPairs().isEmpty()) else it
            if v is not None:
               r = v.conclusion
               break
        return r

    def caseStateVar(self, object):
        """ generated source for method caseStateVar """
        return ComparisonMachine(object, StateVar.__class__).\
            listsEquivalent("StateVar.getAttributes").\
            equalAsObjects("StateVar.getName").\
            equivalent("StateVar.getType").\
            listsEquivalent("StateVar.getInit").\
            listsEqualAsObjects("stateVar -> stateVar.getInit().isEmpty() ? null : stateVar.getBraces()").\
            listsEqualAsObjects("stateVar -> stateVar.getInit().isEmpty() ? null : stateVar.getParens()").\
            conclusion

    def caseMethod(self, object):
        """ generated source for method caseMethod """
        return ComparisonMachine(object, Method.__class__).\
            equalAsObjects("Method.isConst").\
            equalAsObjects("Method.getName").\
            listsEquivalent("Method.getArguments").\
            equivalent("Method.getReturn").\
            equivalent("Method.getCode").\
            conclusion

    def caseMethodArgument(self, object):
        """ generated source for method caseMethodArgument """
        return ComparisonMachine(object, MethodArgument.__class__).\
            equalAsObjects("MethodArgument.getName").\
            equivalent("MethodArgument.getType").\
            conclusion

    def caseInput(self, object):
        """ generated source for method caseInput """
        return ComparisonMachine(object, Input.__class__).\
            listsEquivalent("Input.getAttributes").\
            equalAsObjects("Input.isMutable").\
            equivalent("Input.getWidthSpec").\
            equivalent("Input.getType").\
            conclusion

    def caseOutput(self, object):
        """ generated source for method caseOutput """
        return ComparisonMachine(object, Output.__class__).\
            listsEquivalent("Output.getAttributes").\
            equivalent("Output.getWidthSpec").\
            equalAsObjects("Output.getName").\
            equivalent("Output.getType").\
            conclusion

    def caseTimer(self, object):
        """ generated source for method caseTimer """
        return ComparisonMachine(object, Timer.__class__).\
            listsEquivalent("Timer.getAttributes").\
            equalAsObjects("Timer.getName").\
            equivalent("Timer.getOffset").\
            equivalent("Timer.getPeriod").\
            conclusion

    def caseMode(self, object):
        """ generated source for method caseMode """
        return ComparisonMachine(object, Mode.__class__).\
            equalAsObjects("Mode.isInitial").\
            equalAsObjects("Mode.getName").\
            listsEquivalent("Mode.getStateVars").\
            listsEquivalent("Mode.getTimers").\
            listsEquivalent("Mode.getActions").\
            listsEquivalent("Mode.getInstantiations").\
            listsEquivalent("Mode.getConnections").\
            listsEquivalent("Mode.getReactions").\
            conclusion

    def caseAction(self, object):
        """ generated source for method caseAction """
        return ComparisonMachine(object, Action.__class__).\
            listsEquivalent("Action.getAttributes").\
            equalAsObjects("Action.getOrigin").\
            equalAsObjects("Action.getName").\
            equivalent("Action.getMinDelay").\
            equivalent("Action.getMinSpacing").\
            equalAsObjects("Action.getPolicy").\
            equivalent("Action.getType").\
            conclusion

    def caseAttribute(self, object):
        """ generated source for method caseAttribute """
        return ComparisonMachine(object, Attribute.__class__).\
            equalAsObjects("Attribute.getAttrName").\
            listsEquivalent("Attribute.getAttrParms").\
            conclusion

    def caseAttrParm(self, object):
        """ generated source for method caseAttrParm """
        return ComparisonMachine(object, AttrParm.__class__).\
            equalAsObjects("AttrParm.getName").\
            equivalent("AttrParm.getValue").\
            conclusion

    def caseAttrParmValue(self, object):
        """ generated source for method caseAttrParmValue """
        return ComparisonMachine(object, AttrParmValue.__class__).\
            equalAsObjects("AttrParmValue.getBool").\
            equalAsObjects("AttrParmValue.getFloat").\
            equalAsObjects("AttrParmValue.getInt").\
            equalAsObjects("AttrParmValue.getStr").\
            conclusion

    def caseReaction(self, object):
        """ generated source for method caseReaction """
        return ComparisonMachine(object, Reaction.__class__).\
            listsEquivalent("Reaction.getAttributes").\
            listsEquivalent("Reaction.getTriggers").\
            listsEquivalent("Reaction.getSources").\
            listsEquivalent("Reaction.getEffects").\
            equalAsObjects("Reaction.isMutation").\
            equivalent("Reaction.getCode").\
            equivalent("Reaction.getStp").\
            equivalent("Reaction.getDeadline").\
            conclusion

    def caseTriggerRef(self, object):
        """ generated source for method caseTriggerRef """
        raise self.thereIsAMoreSpecificCase(TriggerRef.__class__, BuiltinTriggerRef.__class__, VarRef.__class__)

    def caseBuiltinTriggerRef(self, object):
        """ generated source for method caseBuiltinTriggerRef """
        return ComparisonMachine(object, BuiltinTriggerRef.__class__).\
            equalAsObjects("BuiltinTriggerRef.getType").\
            conclusion

    def caseDeadline(self, object):
        """ generated source for method caseDeadline """
        return ComparisonMachine(object, Deadline.__class__).\
            equivalent("Deadline.getDelay").\
            equivalent("Deadline.getCode").\
            conclusion

    def caseSTP(self, object):
        """ generated source for method caseSTP """
        return ComparisonMachine(object, STP.__class__).\
            equivalent("STP.getValue").\
            equivalent("STP.getCode").\
            conclusion

    def casePreamble(self, object):
        """ generated source for method casePreamble """
        return ComparisonMachine(object, Preamble.__class__).\
            equalAsObjects("Preamble.getVisibility").\
            equivalent("Preamble.getCode").\
            conclusion

    def caseInstantiation(self, object):
        """ generated source for method caseInstantiation """
        return ComparisonMachine(object, Instantiation.__class__).\
            equalAsObjects("Instantiation.getName").\
            equivalent("Instantiation.getWidthSpec").\
            equivalent("Instantiation.getReactorClass").\
            listsEquivalent("Instantiation.getTypeParms").\
            listsEquivalent("Instantiation.getParameters").\
            equivalent("Instantiation.getHost").\
            conclusion

    def caseConnection(self, object):
        """ generated source for method caseConnection """
        return ComparisonMachine(object, Connection.__class__).\
            listsEquivalent("Connection.getLeftPorts").\
            equalAsObjects("Connection.isIterated").\
            equalAsObjects("Connection.isPhysical").\
            listsEquivalent("Connection.getRightPorts").\
            equivalent("Connection.getDelay").\
            equivalent("Connection.getSerializer").\
            conclusion

    def caseSerializer(self, object):
        """ generated source for method caseSerializer """
        return ComparisonMachine(object, Serializer.__class__).\
            equalAsObjects("Serializer.getType").\
            conclusion

    def caseKeyValuePairs(self, object):
        """ generated source for method caseKeyValuePairs """
        return ComparisonMachine(object, KeyValuePairs.__class__).\
            listsEquivalent("KeyValuePairs.getPairs").\
            conclusion

    def caseKeyValuePair(self, object):
        """ generated source for method caseKeyValuePair """
        return ComparisonMachine(object, KeyValuePair.__class__).\
            equalAsObjects("KeyValuePair.getName").\
            equivalent("KeyValuePair.getValue").\
            conclusion

    def caseArray(self, object):
        """ generated source for method caseArray """
        return ComparisonMachine(object, Array.__class__).\
            listsEquivalent("Array.getElements").\
            conclusion

    def caseElement(self, object):
        """ generated source for method caseElement """
        return ComparisonMachine(object, Element.__class__).\
            equivalent("Element.getKeyvalue").\
            equivalent("Element.getArray").\
            equalAsObjects("Element.getLiteral").\
            equalAsObjects("Element.getId").\
            equalAsObjects("Element.getUnit").\
            conclusion

    def caseTypedVariable(self, object):
        """ generated source for method caseTypedVariable """
        raise self.thereIsAMoreSpecificCase(TypedVariable.__class__, Port.__class__, Action.__class__)

    def caseVariable(self, object):
        """ generated source for method caseVariable """
        raise self.thereIsAMoreSpecificCase(Variable.__class__, TypedVariable.__class__, Timer.__class__, Mode.__class__)

    def caseVarRef(self, object):
        """ generated source for method caseVarRef """
        return ComparisonMachine(object, VarRef.__class__).\
            equalAsObjects("varRef -> varRef.getVariable() instanceof Mode ? null : varRef.getVariable().__name__").\
            equivalent("varRef -> varRef.getVariable() instanceof Mode ? null : varRef.getVariable()").\
            equalAsObjects("varRef -> varRef.getContainer() == null ? null : varRef.getContainer().__name__").\
            equalAsObjects("VarRef.isInterleaved").\
            equalAsObjects("VarRef.getTransition").\
            conclusion

    def caseAssignment(self, object):
        """ generated source for method caseAssignment """
        return ComparisonMachine(object, Assignment.__class__).\
            equivalent("Assignment.getLhs").\
            equalAsObjects("Assignment.getEquals").\
            listsEqualAsObjects("Assignment.getBraces").\
            listsEqualAsObjects("Assignment.getParens").\
            listsEquivalent("Assignment.getRhs").\
            conclusion

    def caseParameter(self, object):
        """ generated source for method caseParameter """
        return ComparisonMachine(object, Parameter.__class__).\
            listsEquivalent("Parameter.getAttributes").\
            equalAsObjects("Parameter.getName").\
            equivalent("Parameter.getType").\
            listsEqualAsObjects("Parameter.getParens").\
            listsEqualAsObjects("Parameter.getBraces").\
            listsEquivalent("Parameter.getInit").\
            conclusion

    def caseExpression(self, object):
        """ generated source for method caseExpression """
        raise self.thereIsAMoreSpecificCase(Expression.__class__, Literal.__class__, Time.__class__, ParameterReference.__class__, Code.__class__)

    def caseParameterReference(self, object):
        """ generated source for method caseParameterReference """
        return ComparisonMachine(object, ParameterReference.__class__).\
            equivalent("ParameterReference.getParameter").\
            conclusion

    def caseTime(self, object):
        """ generated source for method caseTime """
        return ComparisonMachine(object, Time.__class__).\
            equalAsObjects("Time.getInterval").\
            equalAsObjectsModulo("Time.getUnit", ("TimeUnit.getCanonicalName").compose("TimeUnit.fromName")).\
            conclusion

    def casePort(self, object):
        """ generated source for method casePort """
        raise self.thereIsAMoreSpecificCase(Port.__class__, Input.__class__, Output.__class__)

    def caseType(self, object):
        """ generated source for method caseType """
        return ComparisonMachine(object, Type.__class__).\
            equivalent("Type.getCode").\
            equalAsObjects("Type.isTime").\
            equivalent("Type.getArraySpec").\
            equalAsObjects("Type.getId").\
            listsEquivalent("Type.getTypeParms").\
            listsEqualAsObjects("Type.getStars").\
            equivalent("Type.getArraySpec").\
            equivalent("Type.getCode").\
            conclusion

    def caseArraySpec(self, object):
        """ generated source for method caseArraySpec """
        return ComparisonMachine(object, ArraySpec.__class__).\
            equalAsObjects("ArraySpec.isOfVariableLength").\
            equalAsObjects("ArraySpec.getLength").\
            conclusion

    def caseWidthSpec(self, object):
        """ generated source for method caseWidthSpec """
        return ComparisonMachine(object, WidthSpec.__class__).\
            equalAsObjects("WidthSpec.isOfVariableLength").\
            listsEquivalent("WidthSpec.getTerms").\
            conclusion

    def caseWidthTerm(self, object):
        """ generated source for method caseWidthTerm """
        return ComparisonMachine(object, WidthTerm.__class__).\
            equalAsObjects("WidthTerm.getWidth").\
            equivalent("WidthTerm.getParameter").\
            equivalent("WidthTerm.getPort").\
            equivalent("WidthTerm.getCode").\
            conclusion

    def caseIPV4Host(self, object):
        """ generated source for method caseIPV4Host """
        return self.caseHost(object)

    def caseIPV6Host(self, object):
        """ generated source for method caseIPV6Host """
        return self.caseHost(object)

    def caseNamedHost(self, object):
        """ generated source for method caseNamedHost """
        return self.caseHost(object)

    def caseHost(self, object):
        """ generated source for method caseHost """
        return ComparisonMachine(object, Host.__class__).\
            equalAsObjects("Host.getUser").\
            equalAsObjects("Host.getAddr").\
            equalAsObjects("Host.getPort").\
            conclusion

    def caseCode(self, object):
        """ generated source for method caseCode """
        return ComparisonMachine(object, Code.__class__).\
            equalAsObjectsModulo("Code.getBody", "s -> s == null ? null : s.strip().stripIndent()").\
            conclusion

    def caseLiteral(self, object):
        """ generated source for method caseLiteral """
        return ComparisonMachine(object, Literal.__class__).\
            equalAsObjects("Literal.getLiteral").\
            conclusion

    def defaultCase(self, object):
        """ generated source for method defaultCase """
        return super(IsEqual, self).defaultCase(object)

    def thereIsAMoreSpecificCase(self, thisCase, moreSpecificCases):
        """ generated source for method thereIsAMoreSpecificCase """
        r = []
        for it in moreSpecificCases:
            ending = 'es' if it.getName().endwith('s') else 's'
            r.append(TypeError(f"{thisCase.__name__}s are {ending},"
                          " so the methods corresponding to those types should be "
                          "invoked instead."))
        return '\n'.join(r)


    def listsEquivalent(self, listGetter):
        """ generated source for method listsEquivalent """


        if self.conclusion:
            self.conclusion = self.listsEqualish(listGetter, IsEqual(a).doSwitch(b))
        return self

    def listsEqualAsObjects(self, listGetter):
        """ generated source for method listsEqualAsObjects """
        if self.conclusion:
            self.conclusion = self.listsEqualish(listGetter, "Objects.equals")
        return self

    def listsEqualish(self, listGetter, equalish):
        """ generated source for method listsEqualish """
        if not self.conclusion:
            return False
        list0 = listGetter.apply(object)
        list1 = listGetter.apply(self.otherObject)
        if list0 == list1:
            return True
        if len(list0) != len(list1):
            return False
        i = 0
        while i < len(list0):
            if not equalish.test(list0.get(i), list1.get(i)):
                return False
            i += 1
        return True

    def equalAsObjects(self, propertyGetter):
        """ generated source for method equalAsObjects """
        return ComparisonMachine(propertyGetter, Function.identity()).equalAsObjectsModulo()

    def equivalent(self, propertyGetter):
        """ generated source for method equivalent """
        return self.equivalentModulo(propertyGetter, Function.identity())

    def equivalentModulo(self, propertyGetter, projectionToClassRepresentatives):
        """ generated source for method equivalentModulo """
        propertyGetter = projectionToClassRepresentatives.compose(propertyGetter)
        if self.conclusion:
            self.conclusion = IsEqual(propertyGetter.apply(object)).doSwitch(propertyGetter.apply(self.otherObject))
        return self

class ComparisonMachine(IsEqual):
    """ generated source for class ComparisonMachine """
    object = None
    other = None
    conclusion = bool()

    def __init__(self, object, clz, other):
        """ generated source for method __init__ """
        super().__init__(other)
        self.object = object
        self.conclusion = clz.isInstance(self.otherObject)
        self.other = "conclusion ? clz.cast(otherObject) : null"
    def equalAsObjectsModulo(self):
        pass
