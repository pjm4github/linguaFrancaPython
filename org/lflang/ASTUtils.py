#!/usr/bin/env python
""" generated source for module ASTUtils """
# 
# Copyright (c) 2020, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang
# 
#  * A helper class for modifying and analyzing the AST.
#  * @author {Marten Lohstroh <marten@berkeley.edu>}
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Christian Menard <christian.menard@tu-dresden.de>}
#
from lflang.lf import LfFactory, LfPackage
import re

class ASTUtils(object):
    """ generated source for class ASTUtils """
    #      * The Lingua Franca factory for creating new AST nodes.
    #      
    factory = LfFactory.eINSTANCE

    #      * The Lingua Franca feature package.
    #      
    featurePackage = LfPackage.eINSTANCE

    #  Match an abbreviated form of a float literal. 
    ABBREVIATED_FLOAT = re.compile("[+\\-]?\\.\\d+[\\deE+\\-]*")

    #      * A mapping from Reactor features to corresponding Mode features for collecting contained elements.
    #      
    reactorModeFeatureMap = Map.of(featurePackage.getReactor_Actions(), featurePackage.getMode_Actions(), featurePackage.getReactor_Connections(), featurePackage.getMode_Connections(), featurePackage.getReactor_Instantiations(), featurePackage.getMode_Instantiations(), featurePackage.getReactor_Reactions(), featurePackage.getMode_Reactions(), featurePackage.getReactor_StateVars(), featurePackage.getMode_StateVars(), featurePackage.getReactor_Timers(), featurePackage.getMode_Timers())

    # Get all reactors defined in the given resource.
    # @param resource the resource to extract reactors from
    # @return An iterable over all reactors found in the resource
    #       
    @classmethod
    def getAllReactors(cls, resource):
        """ generated source for method getAllReactors """
        return StreamSupport.stream(IteratorExtensions.toIterable(resource.getAllContents()).spliterator(), False).filter(Reactor.__class__.isInstance).map(Reactor.__class__.cast).collect(Collectors.toList())

    @classmethod
    def insertGeneratedDelays(cls, resource, generator):
        """ generated source for method insertGeneratedDelays """
        oldConnections = []
        newConnections = {}
        Map()
        for container in getAllReactors(resource):
            for connection in allConnections(container):
                if connection.getDelay() != None:
                    parent = connection.eContainer()
                    type = (connection.getRightPorts().get(0).getVariable()).getType()
                    delayClass = getDelayClass(type, generator)
                    generic = generator.getTargetTypes().getTargetType(InferredType.fromAST(type)) if generator.getTargetTypes().supportsGenerics() else ""
                    delayInstance = getDelayInstance(delayClass, connection, generic, not generator.generateAfterDelaysWithVariableWidth())
                    connections = convertToEmptyListIfNull(newConnections.get(parent))
                    connections.extend(rerouteViaDelay(connection, delayInstance))
                    newConnections.put(parent, connections)
                    oldConnections.append(connection)
                    instances = convertToEmptyListIfNull(delayInstances.get(parent))
                    instances.append(delayInstance)
                    delayInstances.put(parent, instances)
        for connection in oldConnections:
            container = connection.eContainer()
            if isinstance(container, (Reactor)):
                (container).getConnections().remove(connection)
            elif isinstance(container, (Mode)):
                (container).getConnections().remove(connection)
        for connections in newConnections:
            if isinstance(container, (Reactor)):
                (container).getConnections().extend(connections)
            elif isinstance(container, (Mode)):
                (container).getConnections().addAll(connections)
        for container in delayInstances:
            for instantiation in instantiations:
                if isinstance(container, (Reactor)):
                    instantiation.setName(getUniqueIdentifier(container, "delay"))
                    (container).getInstantiations().append(instantiation)
                elif isinstance(container, (Mode)):
                    instantiation.setName(getUniqueIdentifier(container.eContainer(), "delay"))
                    (container).getInstantiations().append(instantiation)

    @classmethod
    def findConflictingConnectionsInModalReactors(cls, resource):
        """ generated source for method findConflictingConnectionsInModalReactors """
        transform = set()
        for reactor in getAllReactors(resource):
            if not reactor.getModes().isEmpty():
                allWriters = HashMultimap()
                for rea in allReactions(reactor):
                    for eff in rea.getEffects():
                        if isinstance(, (Port)):
                            allWriters.put(Tuples.pair(eff.getContainer(), eff.getVariable()), rea)
                for con in ASTUtils.collectElements(reactor, featurePackage.getReactor_Connections(), False, True):
                    for port in con.getRightPorts():
                        allWriters.put(Tuples.pair(port.getContainer(), port.getVariable()), con)
                for key in allWriters.keySet():
                    writers = allWriters.get(key)
                    if len(writers) > 1:
                        writerModes = HashMultimap()
                        for writer in writers:
                            if isinstance(, (Mode)):
                                writerModes.put(writer.eContainer(), writer)
                            else:
                                writerModes.put(None, writer)
                        if not writerModes.containsKey(None) and writerModes.keySet().stream().map("writerModes.get").allMatch(len(writersInMode) == 1 or writersInMode.stream().allMatch(isinstance(w, (Reaction)))):
                            writers.stream().filter(isinstance(w, (Connection))).forEach(transform.append(c))
        return transform

    @classmethod
    def getEnclosingReactor(cls, obj):
        """ generated source for method getEnclosingReactor """
        if isinstance(, (Reactor)):
            return obj.eContainer()
        elif isinstance(, (Mode)):
            return obj.eContainer().eContainer()
        return None

    @classmethod
    def makeFederated(cls, resource):
        """ generated source for method makeFederated """
        r = IteratorExtensions.findFirst(Iterators.filter(resource.getAllContents(), Reactor.__class__), "Reactor.isMain")
        if r == None:
            return False
        r.setMain(False)
        r.setFederated(True)
        return True

    @classmethod
    def changeTargetName(cls, resource, newTargetName):
        """ generated source for method changeTargetName """
        targetDecl(resource).setName(newTargetName)
        return True

    @classmethod
    def addTargetProperty(cls, resource, name, value):
        """ generated source for method addTargetProperty """
        config = targetDecl(resource).getConfig()
        if config == None:
            config = LfFactory.eINSTANCE.createKeyValuePairs()
            targetDecl(resource).setConfig(config)
        newProperty = LfFactory.eINSTANCE.createKeyValuePair()
        newProperty.setName(name)
        newProperty.setValue(value)
        config.getPairs().append(newProperty)
        return True

    @classmethod
    def hasMultipleConnections(cls, connection):
        """ generated source for method hasMultipleConnections """
        if connection.getLeftPorts().size() > 1 or connection.getRightPorts().size() > 1:
            return True
        leftPort = connection.getLeftPorts().get(0)
        rightPort = connection.getRightPorts().get(0)
        leftContainer = leftPort.getContainer()
        rightContainer = rightPort.getContainer()
        leftPortAsPort = leftPort.getVariable()
        rightPortAsPort = rightPort.getVariable()
        return leftPortAsPort.getWidthSpec() != None or leftContainer != None and leftContainer.getWidthSpec() != None or rightPortAsPort.getWidthSpec() != None or rightContainer != None and rightContainer.getWidthSpec() != None

    @classmethod
    def rerouteViaDelay(cls, connection, delayInstance):
        """ generated source for method rerouteViaDelay """
        connections = []
        upstream = cls.factory.createConnection()
        downstream = cls.factory.createConnection()
        input = cls.factory.createVarRef()
        output = cls.factory.createVarRef()
        delayClass = toDefinition(delayInstance.getReactorClass())
        input.setContainer(delayInstance)
        input.setVariable(delayClass.getInputs().get(0))
        output.setContainer(delayInstance)
        output.setVariable(delayClass.getOutputs().get(0))
        upstream.getLeftPorts().addAll(connection.getLeftPorts())
        upstream.getRightPorts().append(input)
        downstream.getLeftPorts().append(output)
        downstream.getRightPorts().addAll(connection.getRightPorts())
        downstream.setIterated(connection.isIterated())
        connections.append(upstream)
        connections.append(downstream)
        return connections

    @classmethod
    def getDelayInstance(cls, delayClass, connection, generic, defineWidthFromConnection):
        """ generated source for method getDelayInstance """
        delay = connection.getDelay()
        delayInstance = cls.factory.createInstantiation()
        delayInstance.setReactorClass(delayClass)
        if not StringExtensions.isNullOrEmpty(generic):
            typeParm = cls.factory.createTypeParm()
            typeParm.setLiteral(generic)
            delayInstance.getTypeParms().append(typeParm)
        if cls.hasMultipleConnections(connection):
            widthSpec = cls.factory.createWidthSpec()
            if defineWidthFromConnection:
                for port in connection.getLeftPorts():
                    term = cls.factory.createWidthTerm()
                    term.setPort(EcoreUtil.copy(port))
                    widthSpec.getTerms().append(term)
            else:
                widthSpec.setOfVariableLength(True)
            delayInstance.setWidthSpec(widthSpec)
        assignment = cls.factory.createAssignment()
        assignment.setLhs(delayClass.getParameters().get(0))
        assignment.getRhs().append(delay)
        delayInstance.getParameters().append(assignment)
        delayInstance.setName("delay")
        return delayInstance

    @classmethod
    def getDelayClass(cls, type, generator):
        """ generated source for method getDelayClass """
        className = None
        if generator.getTargetTypes().supportsGenerics():
            className = GeneratorBase.GEN_DELAY_CLASS_NAME
        else:
            id = Integer.toHexString(InferredType.fromAST(type).toText().hashCode())
            className = "{:s}_{:s}".format(GeneratorBase.GEN_DELAY_CLASS_NAME, id)
        classDef = generator.findDelayClass(className)
        if classDef != None:
            return classDef
        delayClass = cls.factory.createReactor()
        delayParameter = cls.factory.createParameter()
        action = cls.factory.createAction()
        triggerRef = cls.factory.createVarRef()
        effectRef = cls.factory.createVarRef()
        input = cls.factory.createInput()
        output = cls.factory.createOutput()
        inRef = cls.factory.createVarRef()
        outRef = cls.factory.createVarRef()
        r1 = cls.factory.createReaction()
        r2 = cls.factory.createReaction()
        delayParameter.setName("delay")
        delayParameter.setType(cls.factory.createType())
        delayParameter.getType().setId("time")
        delayParameter.getType().setTime(True)
        defaultTime = cls.factory.createTime()
        defaultTime.setUnit(None)
        defaultTime.setInterval(0)
        delayParameter.getInit().append(defaultTime)
        action.setName("act")
        paramRef = cls.factory.createParameterReference()
        paramRef.setParameter(delayParameter)
        action.setMinDelay(paramRef)
        action.setOrigin(ActionOrigin.LOGICAL)
        if generator.getTargetTypes().supportsGenerics():
            action.setType(cls.factory.createType())
            action.getType().setId("T")
        else:
            action.setType(EcoreUtil.copy(type))
        input.setName("inp")
        input.setType(EcoreUtil.copy(action.getType()))
        output.setName("out")
        output.setType(EcoreUtil.copy(action.getType()))
        inRef.setVariable(input)
        outRef.setVariable(output)
        triggerRef.setVariable(action)
        effectRef.setVariable(action)
        delayClass.setName(className)
        delayClass.getActions().append(action)
        r1.getTriggers().append(inRef)
        r1.getEffects().append(effectRef)
        r1.setCode(cls.factory.createCode())
        r1.getCode().setBody(generator.generateDelayBody(action, inRef))
        r2.getTriggers().append(triggerRef)
        r2.getEffects().append(outRef)
        r2.setCode(cls.factory.createCode())
        r2.getCode().setBody(generator.generateForwardBody(action, outRef))
        delayClass.getReactions().append(r2)
        delayClass.getReactions().append(r1)
        if generator.getTargetTypes().supportsGenerics():
            parm = cls.factory.createTypeParm()
            parm.setLiteral(generator.generateDelayGeneric())
            delayClass.getTypeParms().append(parm)
        delayClass.getInputs().append(input)
        delayClass.getOutputs().append(output)
        delayClass.getParameters().append(delayParameter)
        generator.addDelayClass(delayClass)
        return delayClass

    @classmethod
    def getUniqueIdentifier(cls, reactor, name):
        """ generated source for method getUniqueIdentifier """
        vars = {}
        allActions(reactor).forEach(vars.append(it.__name__))
        allTimers(reactor).forEach(vars.append(it.__name__))
        allParameters(reactor).forEach(vars.append(it.__name__))
        allInputs(reactor).forEach(vars.append(it.__name__))
        allOutputs(reactor).forEach(vars.append(it.__name__))
        allStateVars(reactor).forEach(vars.append(it.__name__))
        allInstantiations(reactor).forEach(vars.append(it.__name__))
        index = 0
        suffix = ""
        exists = True
        while exists:
            id = name + suffix
            if IterableExtensions.exists(vars, it == id):
                suffix = "_" + index
                index += 1
            else:
                exists = False
        return name + suffix

    @classmethod
    def allActions(cls, definition):
        """ generated source for method allActions """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Actions())

    @classmethod
    def allConnections(cls, definition):
        """ generated source for method allConnections """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Connections())

    @classmethod
    def allInputs(cls, definition):
        """ generated source for method allInputs """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Inputs())

    @classmethod
    def allInstantiations(cls, definition):
        """ generated source for method allInstantiations """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Instantiations())

    @classmethod
    def allMethods(cls, definition):
        """ generated source for method allMethods """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Methods())

    @classmethod
    def allOutputs(cls, definition):
        """ generated source for method allOutputs """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Outputs())

    @classmethod
    def allParameters(cls, definition):
        """ generated source for method allParameters """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Parameters())

    @classmethod
    def allReactions(cls, definition):
        """ generated source for method allReactions """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Reactions())

    @classmethod
    def allStateVars(cls, definition):
        """ generated source for method allStateVars """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_StateVars())

    @classmethod
    def allTimers(cls, definition):
        """ generated source for method allTimers """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Timers())

    @classmethod
    def allModes(cls, definition):
        """ generated source for method allModes """
        return ASTUtils.collectElements(definition, cls.featurePackage.getReactor_Modes())

    @classmethod
    @overloaded
    def superClasses(cls, reactor):
        """ generated source for method superClasses """
        return cls.superClasses(reactor, {})

    @classmethod
    @overloaded
    def collectElements(cls, definition, feature):
        """ generated source for method collectElements """
        return ASTUtils.collectElements(definition, feature, True, True)

    @classmethod
    @collectElements.register(object, Reactor, EStructuralFeature, bool, bool)
    @SuppressWarnings("unchecked")
    def collectElements_0(cls, definition, feature, includeSuperClasses, includeModes):
        """ generated source for method collectElements_0 """
        result = []
        if includeSuperClasses:
            s = cls.superClasses(definition)
            if s != None:
                for superClass in s:
                    result.addAll(superClass.eGet(feature))
        result.addAll(definition.eGet(feature))
        if includeModes and cls.reactorModeFeatureMap.containsKey(feature):
            modeFeature = cls.reactorModeFeatureMap.get(feature)
            for mode in allModes(definition) if includeSuperClasses else definition.getModes():
                insertModeElementsAtTextualPosition(result, mode.eGet(modeFeature), mode)
        return result

    @classmethod
    def insertModeElementsAtTextualPosition(cls, list, elements, mode):
        """ generated source for method insertModeElementsAtTextualPosition """
        if elements.isEmpty():
            return
        idx = len(list)
        if idx > 0:
            if mode.eContainer() == list.get(len(list) - 1).eContainer():
                modeAstNode = NodeModelUtils.getNode(mode)
                if modeAstNode != None:
                    modePos = modeAstNode.getOffset()
                    while True:
                        astNode = NodeModelUtils.getNode(list.get(idx - 1))
                        if astNode != None and astNode.getOffset() > modePos:
                            idx -= 1
                        else:
                            break
                        if not ((idx > 0)):
                            break
        list.addAll(idx, elements)

    @classmethod
    def toText(cls, node):
        """ generated source for method toText """
        if node == None:
            return ""
        return CodeMap.Correspondence.tag(node, toOriginalText(node), isinstance(node, (Code)))

    @classmethod
    def toOriginalText(cls, node):
        """ generated source for method toOriginalText """
        if node == None:
            return ""
        return ToText.instance.doSwitch(node)

    @classmethod
    def toInteger(cls, e):
        """ generated source for method toInteger """
        return Integer.decode(e.getLiteral())

    @classmethod
    @overloaded
    def toTimeValue(cls, e):
        """ generated source for method toTimeValue """
        return TimeValue(e.getTime(), TimeUnit.fromName(e.getUnit()))

    @classmethod
    @toTimeValue.register(object, Time)
    def toTimeValue_0(cls, e):
        """ generated source for method toTimeValue_0 """
        if not isValidTime(e):
            raise IllegalArgumentException()
        return TimeValue(e.getInterval(), TimeUnit.fromName(e.getUnit()))

    @classmethod
    def toBoolean(cls, e):
        """ generated source for method toBoolean """
        return elementToSingleString(e).lower() == "true".lower()

    @classmethod
    def elementToSingleString(cls, e):
        """ generated source for method elementToSingleString """
        if e.getLiteral() != None:
            return StringUtil.removeQuotes(e.getLiteral()).trim()
        elif e.getId() != None:
            return e.getId()
        return ""

    @classmethod
    def elementToListOfStrings(cls, value):
        """ generated source for method elementToListOfStrings """
        elements = []
        if value.getArray() != None:
            for element in value.getArray().getElements():
                elements.addAll(cls.elementToListOfStrings(element))
            return elements
        else:
            v = cls.elementToSingleString(value)
            if not v.isEmpty():
                elements.append(v)
        return elements

    @classmethod
    def baseType(cls, type):
        """ generated source for method baseType """
        if type != None:
            if type.getCode() != None:
                return cls.toText(type.getCode())
            else:
                if type.isTime():
                    return "time"
                else:
                    stars = ""
                    iterList = convertToEmptyListIfNull(type.getStars())
                    for s in iterList:
                        stars.append(s)
                    if not IterableExtensions.isNullOrEmpty(type.getTypeParms()):
                        typeParamsStr = []
                        type.getTypeParms().forEach(typeParamsStr.append(cls.toText(it)))
                        return "{:s}<{:s}>".format(type.getId(), ", ".join( typeParamsStr))
                    else:
                        return type.getId() + stars
        return ""

    @classmethod
    @overloaded
    def isZero(cls, literal):
        """ generated source for method isZero """
        try:
            if literal != None and Integer.parseInt(literal) == 0:
                return True
        except NumberFormatException as e:
            pass
        return False

    @classmethod
    @isZero.register(object, Code)
    def isZero_0(cls, code_):
        """ generated source for method isZero_0 """
        return code_ != None and cls.isZero(cls.toOriginalText(code_))

    @classmethod
    @isZero.register(object, Expression)
    def isZero_1(cls, expr):
        """ generated source for method isZero_1 """
        if isinstance(expr, (Literal)):
            return cls.isZero((expr).getLiteral())
        elif isinstance(expr, (Code)):
            return cls.isZero(expr)
        return False

    @classmethod
    @overloaded
    def isInteger(cls, literal):
        """ generated source for method isInteger """
        try:
            Integer.decode(literal)
        except NumberFormatException as e:
            return False
        return True

    @classmethod
    @isInteger.register(object, Code)
    def isInteger_0(cls, code_):
        """ generated source for method isInteger_0 """
        return cls.isInteger(cls.toText(code_))

    @classmethod
    @isInteger.register(object, Expression)
    def isInteger_1(cls, expr):
        """ generated source for method isInteger_1 """
        if isinstance(expr, (Literal)):
            return cls.isInteger((expr).getLiteral())
        elif isinstance(expr, (Code)):
            return cls.isInteger(expr)
        return False

    @classmethod
    @overloaded
    def isValidTime(cls, expr):
        """ generated source for method isValidTime """
        if isinstance(expr, (ParameterReference)):
            return isOfTimeType((expr).getParameter())
        elif isinstance(expr, (Time)):
            return cls.isValidTime(expr)
        elif isinstance(expr, (Literal)):
            return cls.isZero((expr).getLiteral())
        elif isinstance(expr, (Code)):
            return cls.isZero(expr)
        return False

    @classmethod
    @isValidTime.register(object, Time)
    def isValidTime_0(cls, t):
        """ generated source for method isValidTime_0 """
        if t == None:
            return False
        unit = t.getUnit()
        return t.getInterval() == 0 or TimeUnit.isValidUnit(unit)

    @classmethod
    @overloaded
    def getInferredType(cls, type, initList):
        """ generated source for method getInferredType """
        if type != None:
            return InferredType.fromAST(type)
        elif initList == None:
            return InferredType.undefined()
        if len(initList) == 1:
            expr = initList.get(0)
            if isinstance(expr, (ParameterReference)):
                return cls.getInferredType((expr).getParameter())
            elif ASTUtils.isValidTime(expr) and not ASTUtils.isZero(expr):
                return InferredType.time()
        elif len(initList) > 1:
            allValidTime = True
            foundNonZero = False
            for expr in initList:
                if not ASTUtils.isValidTime(expr):
                    allValidTime = False
                if not ASTUtils.isZero(expr):
                    foundNonZero = True
            if allValidTime and foundNonZero:
                return InferredType.timeList()
        return InferredType.undefined()

    @classmethod
    @getInferredType.register(object, Parameter)
    def getInferredType_0(cls, p):
        """ generated source for method getInferredType_0 """
        return cls.getInferredType(p.getType(), p.getInit())

    @classmethod
    @getInferredType.register(object, StateVar)
    def getInferredType_1(cls, s):
        """ generated source for method getInferredType_1 """
        return cls.getInferredType(s.getType(), s.getInit())

    @classmethod
    @getInferredType.register(object, Action)
    def getInferredType_2(cls, a):
        """ generated source for method getInferredType_2 """
        return cls.getInferredType(a.getType(), None)

    @classmethod
    @getInferredType.register(object, Port)
    def getInferredType_3(cls, p):
        """ generated source for method getInferredType_3 """
        return cls.getInferredType(p.getType(), None)

    @classmethod
    def addZeroToLeadingDot(cls, literal):
        """ generated source for method addZeroToLeadingDot """
        m = cls.ABBREVIATED_FLOAT.matcher(literal)
        if m.matches():
            return literal.replace(".", "0.")
        return literal

    @classmethod
    def isMultiport(cls, port):
        """ generated source for method isMultiport """
        return port.getWidthSpec() != None

    @classmethod
    def generateVarRef(cls, reference):
        """ generated source for method generateVarRef """
        prefix = ""
        if reference.getContainer() != None:
            prefix = reference.getContainer().__name__ + "."
        return prefix + reference.getVariable().__name__

    @classmethod
    def getLiteralTimeValue(cls, expr):
        """ generated source for method getLiteralTimeValue """
        if isinstance(expr, (Time)):
            return cls.toTimeValue(expr)
        elif isinstance(expr, (Literal)) and cls.isZero((expr).getLiteral()):
            return TimeValue.ZERO
        else:
            return None

    @classmethod
    def getDefaultAsTimeValue(cls, p):
        """ generated source for method getDefaultAsTimeValue """
        if isOfTimeType(p):
            init = p.getInit().get(0)
            if init != None:
                return cls.getLiteralTimeValue(init)
        return None

    @classmethod
    @overloaded
    def isOfTimeType(cls, state):
        """ generated source for method isOfTimeType """
        t = cls.getInferredType(state)
        return t.isTime and not t.isList

    @classmethod
    @isOfTimeType.register(object, Parameter)
    def isOfTimeType_0(cls, param):
        """ generated source for method isOfTimeType_0 """
        t = cls.getInferredType(param)
        return t.isTime and not t.isList

    @classmethod
    def initialValue(cls, parameter, instantiations):
        """ generated source for method initialValue """
        if instantiations != None and len(instantiations) > 0:
            instantiation = instantiations.get(0)
            if not belongsTo(parameter, instantiation):
                raise IllegalArgumentException("Parameter " + parameter.__name__ + " is not a parameter of reactor instance " + instantiation.__name__ + ".")
            lastAssignment = None
            for assignment in instantiation.getParameters():
                if assignment.getLhs() == parameter:
                    lastAssignment = assignment
            if lastAssignment != None:
                result = []
                for expr in lastAssignment.getRhs():
                    if isinstance(expr, (ParameterReference)):
                        if len(instantiations) > 1 and instantiation.eContainer() != instantiations.get(1).getReactorClass():
                            raise IllegalArgumentException("Reactor instance " + instantiation.__name__ + " is not contained by instance " + instantiations.get(1).__name__ + ".")
                        result.addAll(cls.initialValue((expr).getParameter(), instantiations.subList(1, len(instantiations))))
                    else:
                        result.append(expr)
                return result
        return parameter.getInit()

    @classmethod
    @overloaded
    def belongsTo(cls, eobject, instantiation):
        """ generated source for method belongsTo """
        reactor = toDefinition(instantiation.getReactorClass())
        return cls.belongsTo(eobject, reactor)

    @classmethod
    @belongsTo.register(object, EObject, Reactor)
    def belongsTo_0(cls, eobject, reactor):
        """ generated source for method belongsTo_0 """
        if eobject.eContainer() == reactor:
            return True
        for baseClass in reactor.getSuperClasses():
            if cls.belongsTo(eobject, toDefinition(baseClass)):
                return True
        return False

    @classmethod
    def initialValueInt(cls, parameter, instantiations):
        """ generated source for method initialValueInt """
        expressions = cls.initialValue(parameter, instantiations)
        result = 0
        for expr in expressions:
            if not (isinstance(expr, (Literal))):
                return None
            try:
                result += Integer.decode((expr).getLiteral())
            except NumberFormatException as ex:
                return None
        return result

    @classmethod
    def width(cls, spec, instantiations):
        """ generated source for method width """
        if spec == None:
            return 1
        if spec.isOfVariableLength() and isinstance(, (Instantiation)):
            return inferWidthFromConnections(spec, instantiations)
        result = 0
        for term in spec.getTerms():
            if term.getParameter() != None:
                termWidth = cls.initialValueInt(term.getParameter(), instantiations)
                if termWidth != None:
                    result += termWidth
                else:
                    return -1
            elif term.getWidth() > 0:
                result += term.getWidth()
            else:
                if isinstance(, (Instantiation)):
                    try:
                        return inferWidthFromConnections(spec, instantiations)
                    except InvalidSourceException as e:
                        return -1
        return result

    @classmethod
    def inferPortWidth(cls, reference, connection, instantiations):
        """ generated source for method inferPortWidth """
        if isinstance(, (Port)):
            extended = instantiations
            if reference.getContainer() != None:
                extended = []
                extended.append(reference.getContainer())
                if instantiations != None:
                    extended.addAll(instantiations)
            portWidth = cls.width((reference.getVariable()).getWidthSpec(), extended)
            if portWidth < 0:
                return -1
            bankWidth = 1
            if reference.getContainer() != None:
                bankWidth = cls.width(reference.getContainer().getWidthSpec(), instantiations)
                if bankWidth < 0 and connection != None:
                    if reference.getContainer().getWidthSpec().isOfVariableLength():
                        leftWidth = 0
                        rightWidth = 0
                        leftOrRight = 0
                        for leftPort in connection.getLeftPorts():
                            if leftPort == reference:
                                if leftOrRight != 0:
                                    raise InvalidSourceException("Multiple ports with variable width on a connection.")
                                leftOrRight = -1
                            else:
                                otherWidth = cls.inferPortWidth(leftPort, connection, instantiations)
                                if otherWidth < 0:
                                    return -1
                                leftWidth += otherWidth
                        for rightPort in connection.getRightPorts():
                            if rightPort == reference:
                                if leftOrRight != 0:
                                    raise InvalidSourceException("Multiple ports with variable width on a connection.")
                                leftOrRight = 1
                            else:
                                otherWidth = cls.inferPortWidth(rightPort, connection, instantiations)
                                if otherWidth < 0:
                                    return -1
                                rightWidth += otherWidth
                        discrepancy = 0
                        if leftOrRight < 0:
                            discrepancy = rightWidth - leftWidth
                        elif leftOrRight > 0:
                            discrepancy = leftWidth - rightWidth
                        if discrepancy % portWidth != 0:
                            return -1
                        bankWidth = discrepancy / portWidth
                    else:
                        return -1
            return portWidth * bankWidth
        return -1

    @classmethod
    def widthSpecification(cls, instantiation):
        """ generated source for method widthSpecification """
        result = cls.width(instantiation.getWidthSpec(), None)
        if result < 0:
            raise InvalidSourceException("Cannot determine width for the instance " + instantiation.__name__)
        return result

    @classmethod
    def isInitialized(cls, v):
        """ generated source for method isInitialized """
        return v != None and (v.getParens().size() == 2 or v.getBraces().size() == 2)

    @classmethod
    def isParameterized(cls, s):
        """ generated source for method isParameterized """
        return s.getInit() != None and IterableExtensions.exists(s.getInit(), isinstance(it, (ParameterReference)))

    @classmethod
    def isGeneric(cls, r):
        """ generated source for method isGeneric """
        if r == None:
            return False
        return r.getTypeParms().size() != 0

    @classmethod
    def toDefinition(cls, r):
        """ generated source for method toDefinition """
        if r == None:
            return None
        if isinstance(r, (Reactor)):
            return r
        elif isinstance(r, (ImportedReactor)):
            return (r).getReactorClass()
        return None

    @classmethod
    def getPrecedingComments(cls, compNode, filter):
        """ generated source for method getPrecedingComments """
        return getPrecedingCommentNodes(compNode, filter).map("INode.getText")

    @classmethod
    def getPrecedingCommentNodes(cls, compNode, filter):
        """ generated source for method getPrecedingCommentNodes """
        if compNode == None:
            return Stream.of()
        ret = ArrayList()
        for node in compNode.getAsTreeIterable():
            if not (isinstance(node, (ICompositeNode))):
                if isComment(node):
                    if filter.test(node):
                        ret.append(node)
                elif not node.getText().isBlank():
                    break
        return ret.stream()

    @classmethod
    def isComment(cls, node):
        """ generated source for method isComment """
        t0 = isinstance(node, (HiddenLeafNode))
        hlNode = None
        t1 = isinstance(, (TerminalRule))
        tRule = None
        t2 = tRule.__name__.endsWith("_COMMENT")
        return t0 and t1 and t2

    @classmethod
    def sameLine(cls, compNode):
        """ generated source for method sameLine """
        return False

    @classmethod
    def findAnnotationInComments(cls, object, key):
        """ generated source for method findAnnotationInComments """
        if not (isinstance(, (XtextResource))):
            return None
        node = NodeModelUtils.findActualNodeFor(object)
        return cls.getPrecedingComments(node, True).flatMap("String.lines").filter(line.contains(key)).map("String.trim").map(it.substring(it.indexOf(key) + len(key))).map(it.substring(0, "*/".length() - len(it)) if it.endsWith("*/") else it).findFirst().orElse(None)

    @classmethod
    def setMainName(cls, resource, name):
        """ generated source for method setMainName """
        main = IteratorExtensions.findFirst(Iterators.filter(resource.getAllContents(), Reactor.__class__), it.isMain() or it.isFederated())
        if main != None and StringExtensions.isNullOrEmpty(main.__name__):
            main.setName(name)

    @classmethod
    def createInstantiation(cls, reactor):
        """ generated source for method createInstantiation """
        inst = LfFactory.eINSTANCE.createInstantiation()
        inst.setReactorClass(reactor)
        if reactor.__name__ == None:
            if reactor.isFederated() or reactor.isMain():
                inst.setName("main")
            else:
                inst.setName("")
        else:
            inst.setName(reactor.__name__)
        return inst

    @classmethod
    @overloaded
    def targetDecl(cls, model):
        """ generated source for method targetDecl """
        return IteratorExtensions.head(Iterators.filter(model.eAllContents(), TargetDecl.__class__))

    @classmethod
    @targetDecl.register(object, Resource)
    def targetDecl_0(cls, model):
        """ generated source for method targetDecl_0 """
        return IteratorExtensions.head(Iterators.filter(model.getAllContents(), TargetDecl.__class__))

    @classmethod
    def convertToEmptyListIfNull(cls, list):
        """ generated source for method convertToEmptyListIfNull """
        return list if list != None else ArrayList()

    @classmethod
    @superClasses.register(object, Reactor, Set)
    def superClasses_0(cls, reactor, extensions):
        """ generated source for method superClasses_0 """
        result = {}
        for superDecl in convertToEmptyListIfNull(reactor.getSuperClasses()):
            r = cls.toDefinition(superDecl)
            if r == reactor or r == None:
                return None
            if extensions.contains(r):
                return None
            extensions.append(r)
            baseExtends = cls.superClasses(r, extensions)
            extensions.remove(r)
            if baseExtends == None:
                return None
            result.addAll(baseExtends)
            result.append(r)
        return result

    @classmethod
    def inferWidthFromConnections(cls, spec, instantiations):
        """ generated source for method inferWidthFromConnections """
        for c in (spec.eContainer().eContainer()).getConnections():
            leftWidth = 0
            rightWidth = 0
            leftOrRight = 0
            for leftPort in c.getLeftPorts():
                if leftPort.getContainer() == spec.eContainer():
                    if leftOrRight != 0:
                        raise InvalidSourceException("Multiple ports with variable width on a connection.")
                    leftOrRight = -1
                else:
                    leftWidth += cls.inferPortWidth(leftPort, c, instantiations)
            for rightPort in c.getRightPorts():
                if rightPort.getContainer() == spec.eContainer():
                    if leftOrRight != 0:
                        raise InvalidSourceException("Multiple ports with variable width on a connection.")
                    leftOrRight = 1
                else:
                    rightWidth += cls.inferPortWidth(rightPort, c, instantiations)
            if leftOrRight < 0:
                return rightWidth - leftWidth
            elif leftOrRight > 0:
                return leftWidth - rightWidth
        return -1
