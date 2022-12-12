#!/usr/bin/env python
""" generated source for module ReactorInstance """
#  A data structure for a reactor instance. 
# 
# Copyright (c) 2019-2022, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.generator
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.Iterator
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Map
# import java.util.Set
from include.overloading import overloaded

from org.lflang.lf import Reactor


#  * Representation of a compile-time instance of a reactor.
#  * If the reactor is instantiated as a bank of reactors, or if any
#  * of its parents is instantiated as a bank of reactors, then one instance
#  * of this ReactorInstance class represents all the runtime instances within
#  * these banks.  The {@link #getTotalWidth()} method returns the number of such
#  * runtime instances, which is the product of the bank width of this reactor
#  * instance and the bank widths of all of its parents.
#  * There is exactly one instance of this ReactorInstance class for each
#  * graphical rendition of a reactor in the diagram view.
#  * 
#  * For the main reactor, which has no parent, once constructed,
#  * this object represents the entire Lingua Franca program.
#  * If the program has causality loops (a programming error), then
#  * {@link #hasCycles()} will return true and {@link #getCycles()} will
#  * return the ports and reaction instances involved in the cycles.
#  *
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class ReactorInstance(NamedInstance):
    """ generated source for class ReactorInstance """
    #      * Create a new instantiation hierarchy that starts with the given top-level reactor.
    #      * @param reactor The top-level reactor.
    #      * @param reporter The error reporter.
    #      
    @overloaded
    def __init__(self, reactor, reporter):
        """ generated source for method __init__ """
        super().__init__()
        self.__init__(ASTUtils.createInstantiation(reactor), None, reporter, -1, None)

    #      * Create a new instantiation hierarchy that starts with the given top-level reactor
    #      * but only creates contained reactors up to the specified depth.
    #      * @param reactor The top-level reactor.
    #      * @param reporter The error reporter.
    #      * @param desiredDepth The depth to which to go, or -1 to construct the full hierarchy.
    #      
    @__init__.register(object, Reactor, ErrorReporter, int)
    def __init___0(self, reactor, reporter, desiredDepth):
        """ generated source for method __init___0 """
        super().__init__()
        self.__init__(ASTUtils.createInstantiation(reactor), None, reporter, desiredDepth, None)

    #      * Create a new instantiation hierarchy that starts with the given reactor.
    #      * @param reactor The top-level reactor.
    #      * @param reporter The error reporter.
    #      * @param unorderedReactions A list of reactions that should be treated as unordered.
    #      
    @__init__.register(object, Reactor, ErrorReporter, Set)
    def __init___1(self, reactor, reporter, unorderedReactions):
        """ generated source for method __init___1 """
        super().__init__()
        self.__init__(ASTUtils.createInstantiation(reactor), None, reporter, -1, unorderedReactions)

    #      * Create a new instantiation with the specified parent.
    #      * This constructor is here to allow for unit tests.
    #      * It should not be used for any other purpose.
    #      * @param reactor The top-level reactor.
    #      * @param parent The parent reactor instance.
    #      * @param reporter The error reporter.
    #      
    @__init__.register(object, Reactor, ReactorInstance, ErrorReporter)
    def __init___2(self, reactor, parent, reporter):
        """ generated source for method __init___2 """
        super().__init__()
        self.__init__(ASTUtils.createInstantiation(reactor), parent, reporter, -1, None)

    # ////////////////////////////////////////////////////
    # // Public fields.
    #  The action instances belonging to this reactor instance. 
    actions = []

    #      * The contained reactor instances, in order of declaration.
    #      * For banks of reactors, this includes both the bank definition
    #      * Reactor (which has bankIndex == -2) followed by each of the
    #      * bank members (which have bankIndex >= 0).
    #      
    children = []

    #  The input port instances belonging to this reactor instance. 
    inputs = []

    #  The output port instances belonging to this reactor instance. 
    outputs = []

    #  The parameters of this instance. 
    parameters = []

    #  List of reaction instances for this reactor instance. 
    reactions = []

    #  The timer instances belonging to this reactor instance. 
    timers = []

    #  The mode instances belonging to this reactor instance. 
    modes = []

    #  The reactor declaration in the AST. This is either an import or Reactor declaration. 
    reactorDeclaration = None

    #  The reactor after imports are resolve. 
    reactorDefinition = None

    #  Indicator that this reactor has itself as a parent, an error condition. 
    recursive = bool()

    # ////////////////////////////////////////////////////
    # // Public methods.
    #      * Assign levels to all reactions within the same root as this
    #      * reactor. The level of a reaction r is equal to the length of the
    #      * longest chain of reactions that must have the opportunity to
    #      * execute before r at each logical tag. This fails and returns
    #      * false if a causality cycle exists.
    #      * 
    #      * This method uses a variant of Kahn's algorithm, which is linear
    #      * in V + E, where V is the number of vertices (reactions) and E
    #      * is the number of edges (dependencies between reactions).
    #      * 
    #      * @return An empty graph if successful and otherwise a graph
    #      *  with runtime reaction instances that form cycles.
    #      
    def assignLevels(self):
        """ generated source for method assignLevels """
        if depth != 0:
            return root().assignLevels()
        if cachedReactionLoopGraph == None:
            cachedReactionLoopGraph = ReactionInstanceGraph(self)
        return cachedReactionLoopGraph

    #  
    #      * Return the instance of a child rector created by the specified
    #      * definition or null if there is none.
    #      * @param definition The definition of the child reactor ("new" statement).
    #      
    def getChildReactorInstance(self, definition):
        """ generated source for method getChildReactorInstance """
        for child in self.children:
            if child.definition == definition:
                return child
        return None

    #      * Clear any cached data in this reactor and its children.
    #      * This is useful if a mutation has been realized.
    #      
    @overloaded
    def clearCaches(self):
        """ generated source for method clearCaches """
        self.clearCaches(True)

    #      * Clear any cached data in this reactor and its children.
    #      * This is useful if a mutation has been realized.
    #      * @param includingRuntimes If false, leave the runtime instances of reactions intact.
    #      *  This is useful for federated execution where levels are computed using
    #      *  the top-level connections, but then those connections are discarded.
    #      
    @clearCaches.register(object, bool)
    def clearCaches_0(self, includingRuntimes):
        """ generated source for method clearCaches_0 """
        if includingRuntimes:
            cachedReactionLoopGraph = None
        for child in children:
            child.clearCaches(includingRuntimes)
        for port in inputs:
            port.clearCaches()
        for port in outputs:
            port.clearCaches()
        for reaction in reactions:
            reaction.clearCaches(includingRuntimes)
        cachedCycles = None

    #      * Return the set of ReactionInstance and PortInstance that form causality
    #      * loops in the topmost parent reactor in the instantiation hierarchy. This will return an
    #      * empty set if there are no causality loops.
    #      
    def getCycles(self):
        """ generated source for method getCycles """
        if depth != 0:
            return root().getCycles()
        if cachedCycles != None:
            return cachedCycles
        cachedCycles = {}
        reactionRuntimes = self.assignLevels()
        if reactionRuntimes.nodes().size() > 0:
            reactions = {}
            ports = {}
            #  There are cycles. But the nodes set includes not
            #  just the cycles, but also nodes that are downstream of the
            #  cycles.  Use Tarjan's algorithm to get just the cycles.
            cycleNodes = reactionRuntimes.getCycles()
            for cycle in cycleNodes:
                for runtime in cycle:
                    self.reactions.append(runtime.getReaction())
            #  Need to figure out which ports are involved in the cycles.
            #  It may not be all ports that depend on this reaction.
            for r in reactions:
                for p in r.effects:
                    if isinstance(p, (PortInstance)):
                        findPaths(p, self.reactions, ports)
            cachedCycles.extend(self.reactions)
            cachedCycles.extend(ports)
        return cachedCycles

    #      * Return the specified input by name or null if there is no such input.
    #      * @param name The input name.
    #      
    def getInput(self, name):
        """ generated source for method getInput """
        for port in inputs:
            if port.__name__ == name:
                return port
        return None

    #  
    #      * Override the base class to append [i_d], where d is the depth,
    #      * if this reactor is in a bank of reactors.
    #      * @return The name of this instance.
    #      
    def getName(self):
        """ generated source for method getName """
        return self.definition.__name__

    #      * Return the specified output by name or null if there is no such output.
    #      * @param name The output name.
    #      
    def getOutput(self, name):
        """ generated source for method getOutput """
        for port in outputs:
            if port.__name__ == name:
                return port
        return None

    #      * Return a parameter matching the specified name if the reactor has one
    #      * and otherwise return null.
    #      * @param name The parameter name.
    #      
    def getParameter(self, name):
        """ generated source for method getParameter """
        for parameter in parameters:
            if parameter.__name__ == name:
                return parameter
        return None

    #      * Return the startup trigger or null if not used in any reaction.
    #      
    def getStartupTrigger(self):
        """ generated source for method getStartupTrigger """
        return builtinTriggers.get(BuiltinTrigger.STARTUP)

    #      * Return the shutdown trigger or null if not used in any reaction.
    #      
    def getShutdownTrigger(self):
        """ generated source for method getShutdownTrigger """
        return builtinTriggers.get(BuiltinTrigger.SHUTDOWN)

    #      * If this reactor is a bank or any of its parents is a bank,
    #      * return the total number of runtime instances, which is the product
    #      * of the widths of all the parents.
    #      * Return -1 if the width cannot be determined.
    #      
    @overloaded
    def getTotalWidth(self):
        """ generated source for method getTotalWidth """
        return self.getTotalWidth(0)

    #      * If this reactor is a bank or any of its parents is a bank,
    #      * return the total number of runtime instances, which is the product
    #      * of the widths of all the parents.
    #      * Return -1 if the width cannot be determined.
    #      * @param atDepth The depth at which to determine the width.
    #      *  Use 0 to get the total number of instances.
    #      *  Use 1 to get the number of instances within a single top-level
    #      *  bank member (this is useful for federates). 
    #      
    @getTotalWidth.register(object, int)
    def getTotalWidth_0(self, atDepth):
        """ generated source for method getTotalWidth_0 """
        if width <= 0:
            return -1
        if depth <= atDepth:
            return 1
        result = width
        p = parent
        while p != None and p.depth > atDepth:
            if p.width <= 0:
                return -1
            result *= p.width
            p = p.parent
        return result

    #  
    #      * Return the trigger instances (input ports, timers, and actions
    #      * that trigger reactions) belonging to this reactor instance.
    #      
    def getTriggers(self):
        """ generated source for method getTriggers """
        #  FIXME: Cache this.
        triggers = {}
        for reaction in self.reactions:
            triggers.extend(reaction.triggers)
        return triggers

    #  
    #      * Return the trigger instances (input ports, timers, and actions
    #      * that trigger reactions) together the ports that the reaction reads
    #      * but that don't trigger it.
    #      * 
    #      * @return The trigger instances belonging to this reactor instance.
    #      
    def getTriggersAndReads(self):
        """ generated source for method getTriggersAndReads """
        #  FIXME: Cache this.
        triggers = {}
        for reaction in self.reactions:
            triggers.extend(reaction.triggers)
            triggers.extend(reaction.reads)
        return triggers

    #      * Return true if the top-level parent of this reactor has causality cycles.
    #      
    def hasCycles(self):
        """ generated source for method hasCycles """
        return self.assignLevels().nodeCount() != 0

    #      * Given a parameter definition for this reactor, return the initial integer
    #      * value of the parameter. If the parameter is overridden when instantiating
    #      * this reactor or any of its containing reactors, use that value.
    #      * Otherwise, use the default value in the reactor definition.
    #      * If the parameter cannot be found or its value is not an integer, return null.
    #      * 
    #      * @param parameter The parameter definition (a syntactic object in the AST).
    #      * 
    #      * @return An integer value or null.
    #      
    def initialIntParameterValue(self, parameter):
        """ generated source for method initialIntParameterValue """
        return ASTUtils.initialValueInt(parameter, instantiations())

    #      * Given a parameter definition for this reactor, return the initial value
    #      * of the parameter. If the parameter is overridden when instantiating
    #      * this reactor or any of its containing reactors, use that value.
    #      * Otherwise, use the default value in the reactor definition.
    #      * 
    #      * The returned list of Value objects is such that each element is an
    #      * instance of Time, String, or Code, never Parameter.
    #      * For most uses, this list has only one element, but parameter
    #      * values can be lists of elements, so the returned value is a list.
    #      * 
    #      * @param parameter The parameter definition (a syntactic object in the AST).
    #      * 
    #      * @return A list of Value objects, or null if the parameter is not found.
    #      *  Return an empty list if no initial value is given.
    #      *  Each value is an instance of Literal if a literal value is given,
    #      *  a Time if a time value was given, or a Code, if a code value was
    #      *  given (text in the target language delimited by {= ... =}
    #      
    def initialParameterValue(self, parameter):
        """ generated source for method initialParameterValue """
        return ASTUtils.initialValue(parameter, instantiations())

    #      * Return a list of Instantiation objects for evaluating parameter
    #      * values.  The first object in the list is the AST Instantiation
    #      * that created this reactor instance, the second is the AST instantiation
    #      * that created the containing reactor instance, and so on until there
    #      * are no more containing reactor instances. This will return an empty
    #      * list if this reactor instance is at the top level (is main).
    #      
    def instantiations(self):
        """ generated source for method instantiations """
        if _instantiations == None:
            _instantiations = []
            if definition != None:
                _instantiations.append(definition)
                if parent != None:
                    _instantiations.addAll(parent.instantiations())
        return _instantiations

    #      * Returns true if this is a bank of reactors.
    #      * @return true if a reactor is a bank, false otherwise
    #      
    def isBank(self):
        """ generated source for method isBank """
        return definition.getWidthSpec() != None

    #      * Returns whether this is a main or federated reactor.
    #      * @return true if reactor definition is marked as main or federated, false otherwise.
    #      
    def isMainOrFederated(self):
        """ generated source for method isMainOrFederated """
        return self.reactorDefinition != None and (self.reactorDefinition.isMain() or self.reactorDefinition.isFederated())

    #      * Return true if the specified reactor instance is either equal to this
    #      * reactor instance or a parent of it.
    #      * @param r The reactor instance.
    #      
    def isParent(self, r):
        """ generated source for method isParent """
        p = self
        while p != None:
            if p == r:
                return True
            p = p.getParent()
        return False

    # /////////////////////////////////////////////////
    # // Methods for finding instances in this reactor given an AST node.
    #  
    #      * Return the action instance within this reactor 
    #      * instance corresponding to the specified action reference.
    #      * @param action The action as an AST node.
    #      * @return The corresponding action instance or null if the
    #      *  action does not belong to this reactor.
    #      
    def lookupActionInstance(self, action):
        """ generated source for method lookupActionInstance """
        for actionInstance in actions:
            if actionInstance.definition == action:
                return actionInstance
        return None

    #  
    #      * Given a parameter definition, return the parameter instance
    #      * corresponding to that definition, or null if there is
    #      * no such instance.
    #      * @param parameter The parameter definition (a syntactic object in the AST).
    #      * @return A parameter instance, or null if there is none.
    #      
    def lookupParameterInstance(self, parameter):
        """ generated source for method lookupParameterInstance """
        for param in parameters:
            if param.definition == parameter:
                return param
        return None

    #  
    #      * Given a port definition, return the port instance
    #      * corresponding to that definition, or null if there is
    #      * no such instance.
    #      * @param port The port definition (a syntactic object in the AST).
    #      * @return A port instance, or null if there is none.
    #      
    @overloaded
    def lookupPortInstance(self, port):
        """ generated source for method lookupPortInstance """
        #  Search one of the inputs and outputs sets.
        ports = None
        if isinstance(port, (Input)):
            ports = self.inputs
        elif isinstance(port, (Output)):
            ports = self.outputs
        for portInstance in ports:
            if portInstance.definition == port:
                return portInstance
        return None

    #  
    #      * Given a reference to a port belonging to this reactor
    #      * instance, return the port instance.
    #      * Return null if there is no such instance.
    #      * @param reference The port reference.
    #      * @return A port instance, or null if there is none.
    #      
    @lookupPortInstance.register(object, VarRef)
    def lookupPortInstance_0(self, reference):
        """ generated source for method lookupPortInstance_0 """
        if not (isinstance(, (Port))):
            #  Trying to resolve something that is not a port
            return None
        if reference.getContainer() == None:
            #  Handle local reference
            return self.lookupPortInstance(reference.getVariable())
        else:
            #  Handle hierarchical reference
            containerInstance = self.getChildReactorInstance(reference.getContainer())
            if containerInstance == None:
                return None
            return containerInstance.lookupPortInstance(reference.getVariable())

    #  
    #      * Return the reaction instance within this reactor 
    #      * instance corresponding to the specified reaction.
    #      * @param reaction The reaction as an AST node.
    #      * @return The corresponding reaction instance or null if the
    #      *  reaction does not belong to this reactor.
    #      
    def lookupReactionInstance(self, reaction):
        """ generated source for method lookupReactionInstance """
        for reactionInstance in reactions:
            if reactionInstance.definition == reaction:
                return reactionInstance
        return None

    #      * Return the reactor instance within this reactor
    #      * that has the specified instantiation. Note that this
    #      * may be a bank of reactors. Return null if there
    #      * is no such reactor instance.
    #      
    def lookupReactorInstance(self, instantiation):
        """ generated source for method lookupReactorInstance """
        for reactorInstance in children:
            if reactorInstance.definition == instantiation:
                return reactorInstance
        return None

    #  
    #      * Return the timer instance within this reactor 
    #      * instance corresponding to the specified timer reference.
    #      * @param timer The timer as an AST node.
    #      * @return The corresponding timer instance or null if the
    #      *  timer does not belong to this reactor.
    #      
    def lookupTimerInstance(self, timer):
        """ generated source for method lookupTimerInstance """
        for timerInstance in timers:
            if timerInstance.definition == timer:
                return timerInstance
        return None

    #  Returns the mode instance within this reactor 
    #      *  instance corresponding to the specified mode reference.
    #      *  @param mode The mode as an AST node.
    #      *  @return The corresponding mode instance or null if the
    #      *   mode does not belong to this reactor.
    #      
    def lookupModeInstance(self, mode):
        """ generated source for method lookupModeInstance """
        for modeInstance in modes:
            if modeInstance.definition == mode:
                return modeInstance
        return None

    #  
    #      * Return a descriptive string.
    #      
    def __str__(self):
        """ generated source for method toString """
        return "ReactorInstance " + getFullName()

    #      * Assuming that the given expression denotes a valid time, return a time value.
    #      *
    #      * If the value is given as a parameter reference, this will look up the
    #      * precise time value assigned to this reactor instance.
    #      
    def getTimeValue(self, expr):
        """ generated source for method getTimeValue """
        if isinstance(expr, (ParameterReference)):
            param = (expr).getParameter()
            #  Avoid a runtime error in validator for invalid programs.
            if self.lookupParameterInstance(param).getInitialValue().isEmpty():
                return None
            return ASTUtils.getLiteralTimeValue(self.lookupParameterInstance(param).getInitialValue().get(0))
        else:
            return ASTUtils.getLiteralTimeValue(expr)

    reporter = None
    builtinTriggers = dict()
    unorderedReactions = {}
    _instantiations = None

    def createReactionInstances(self):
        """ generated source for method createReactionInstances """
        reactions = ASTUtils.allReactions(self.reactorDefinition)
        if reactions != None:
        __count_0 = count
        count += 1
            count = 0
            for reaction in reactions:
                reactionInstance = ReactionInstance(reaction, self, self.unorderedReactions.contains(reaction), __count_0)
                self.reactions.append(reactionInstance)

    def getOrCreateBuiltinTrigger(self, trigger):
        """ generated source for method getOrCreateBuiltinTrigger """
        if not self.builtinTriggers.containsKey(trigger.getType()):
            self.builtinTriggers.put(trigger.getType(), TriggerInstance(trigger.getType(), trigger, self))
        return self.builtinTriggers.get(trigger.getType())

    @__init__.register(object, Instantiation, ReactorInstance, ErrorReporter, int, Set)
    def __init___3(self, definition, parent, reporter, desiredDepth, unorderedReactions):
        """ generated source for method __init___3 """
        super(ReactorInstance, self).__init__(parent)
        self.reporter = reporter
        self.reactorDeclaration = definition.getReactorClass()
        self.reactorDefinition = ASTUtils.toDefinition(self.reactorDeclaration)
        if unorderedReactions != None:
            self.unorderedReactions = unorderedReactions
        currentParent = parent
        foundSelfAsParent = False
        while True:
            if currentParent != None:
                if currentParent.reactorDefinition == self.reactorDefinition:
                    foundSelfAsParent = True
                    currentParent = None
                else:
                    currentParent = currentParent.parent
            if not ((currentParent != None)):
                break
        self.recursive = foundSelfAsParent
        if self.recursive:
            reporter.reportError(definition, "Recursive reactor instantiation.")
        if self.reactorDefinition == None:
            reporter.reportError(definition, "Reactor instantiation has no matching reactor definition.")
            return
        setInitialWidth()
        for parameter in ASTUtils.allParameters(reactorDefinition):
            self.parameters.append(ParameterInstance(parameter, self))
        for inputDecl in ASTUtils.allInputs(reactorDefinition):
            self.inputs.append(PortInstance(inputDecl, self, reporter))
        for outputDecl in ASTUtils.allOutputs(reactorDefinition):
            self.outputs.append(PortInstance(outputDecl, self, reporter))
        if not self.recursive and (desiredDepth < 0 or self.depth < desiredDepth):
            for child in ASTUtils.allInstantiations(reactorDefinition):
                childInstance = ReactorInstance(child, self, reporter, desiredDepth, self.unorderedReactions)
                self.children.append(childInstance)
            for timerDecl in ASTUtils.allTimers(reactorDefinition):
                self.timers.append(TimerInstance(timerDecl, self))
            for actionDecl in ASTUtils.allActions(reactorDefinition):
                self.actions.append(ActionInstance(actionDecl, self))
            establishPortConnections()
            self.createReactionInstances()
            for modeDecl in ASTUtils.allModes(reactorDefinition):
                self.modes.append(ModeInstance(modeDecl, self))
            for mode in self.modes:
                mode.setupTranstions()

    @classmethod
    def connectPortInstances(cls, src, dst, connection):
        """ generated source for method connectPortInstances """
        range = SendRange(src, dst, src._interleaved, connection)
        src.instance.dependentPorts.append(range)
        dst.instance.dependsOnPorts.append(src)

    def establishPortConnections(self):
        """ generated source for method establishPortConnections """
        for connection in ASTUtils.allConnections(reactorDefinition):
            leftPorts = listPortInstances(connection.getLeftPorts(), connection)
            srcRanges = leftPorts.iterator()
            rightPorts = listPortInstances(connection.getRightPorts(), connection)
            dstRanges = rightPorts.iterator()
            if not srcRanges.hasNext():
                if dstRanges.hasNext():
                    self.reporter.reportWarning(connection, "No sources to provide inputs.")
                return
            elif not dstRanges.hasNext():
                self.reporter.reportWarning(connection, "No destination. Outputs will be lost.")
                return
            src = srcRanges.next()
            dst = dstRanges.next()
            while True:
                if dst.width == src.width:
                    self.connectPortInstances(src, dst, connection)
                    if not dstRanges.hasNext():
                        if srcRanges.hasNext():
                            self.reporter.reportWarning(connection, "Source is wider than the destination. Outputs will be lost.")
                        break
                    if not srcRanges.hasNext():
                        if connection.isIterated():
                            srcRanges = leftPorts.iterator()
                        else:
                            if dstRanges.hasNext():
                                self.reporter.reportWarning(connection, "Destination is wider than the source. Inputs will be missing.")
                            break
                    dst = dstRanges.next()
                    src = srcRanges.next()
                elif dst.width < src.width:
                    self.connectPortInstances(src.head(dst.width), dst, connection)
                    src = src.tail(dst.width)
                    if not dstRanges.hasNext():
                        self.reporter.reportWarning(connection, "Source is wider than the destination. Outputs will be lost.")
                        break
                    dst = dstRanges.next()
                elif src.width < dst.width:
                    self.connectPortInstances(src, dst.head(src.width), connection)
                    dst = dst.tail(src.width)
                    if not srcRanges.hasNext():
                        if connection.isIterated():
                            srcRanges = leftPorts.iterator()
                        else:
                            self.reporter.reportWarning(connection, "Destination is wider than the source. Inputs will be missing.")
                            break
                    src = srcRanges.next()

    def findPaths(self, port, reactions, ports):
        """ generated source for method findPaths """
        if ports.contains(port):
            return False
        result = False
        for d in port.getDependentReactions():
            if reactions.contains(d):
                ports.append(port)
            result = True
        for r in port.dependentPorts:
            for p in r.destinations:
                added = self.findPaths(p.instance, reactions, ports)
                if added:
                    result = True
                    ports.append(port)
        return result

    def listPortInstances(self, references, connection):
        """ generated source for method listPortInstances """
        result = []
        tails = LinkedList()
        count = 0
        for portRef in references:
            if not (isinstance(, (Port))):
                self.reporter.reportError(portRef, "Not a port.")
                return result
            reactor = self
            if portRef.getContainer() != None:
                reactor = self.getChildReactorInstance(portRef.getContainer())
            if reactor != None:
                portInstance = reactor.lookupPortInstance(portRef.getVariable())
                interleaved = {}
                if portRef.isInterleaved():
                    interleaved.append(portInstance.parent)
                range = RuntimeRange.Port(portInstance, interleaved)
                if count < len(references) - 1:
                    portWidth = portInstance.width
                    portParentWidth = portInstance.parent.width
                    if reactor == self and len(references) > 1:
                        portParentWidth = 1
                    widthBound = portWidth * portParentWidth
                    if portWidth < 0:
                        widthBound = Integer.MAX_VALUE
                    if portParentWidth < 0:
                        widthBound = Integer.MAX_VALUE
                    if widthBound < range.width:
                        tails.append(range.tail(widthBound))
                        range = range.head(widthBound)
                result.append(range)
        while len(tails) > 0:
            moreTails = LinkedList()
            count = 0
            for tail in tails:
                if count < len(tails) - 1:
                    widthBound = tail.instance.width
                    if tail._interleaved.contains(tail.instance.parent):
                        widthBound = tail.instance.parent.width
                    if widthBound < 0:
                        widthBound = Integer.MAX_VALUE
                    if widthBound < tail.width:
                        moreTails.append(tail.tail(widthBound))
                        tail = tail.head(widthBound)
                result.append(tail)
            tails = moreTails
        return result

    def setInitialWidth(self):
        """ generated source for method setInitialWidth """
        widthSpec = definition.getWidthSpec()
        if widthSpec != None:
            width = ASTUtils.width(widthSpec, parent.instantiations())

    cachedCycles = None
    cachedReactionLoopGraph = None

    def isGeneratedDelay(self):
        """ generated source for method isGeneratedDelay """
        if self.definition.getReactorClass().__name__.contains(GeneratorBase.GEN_DELAY_CLASS_NAME):
            return True
        return False
