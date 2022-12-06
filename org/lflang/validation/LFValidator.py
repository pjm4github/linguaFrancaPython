#!/usr/bin/env python
""" generated source for module LFValidator """
#  Validation checks for Lingua Franca code. 
# 
#  * Copyright (c) 2019-2020, The University of California at Berkeley.
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.validation
import 

import 

import 

import 

import 

import 

import 
# import java.io.File
# import java.io.IOException
# import java.util.ArrayList
# import java.util.Arrays
# import java.util.HashSet
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Optional
# import java.util.Set
# import java.util.stream.Collectors
# import org.eclipse.emf.common.util.BasicEList
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.common.util.TreeIterator
# import org.eclipse.emf.ecore.EAttribute
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.EReference
# import org.eclipse.emf.ecore.EStructuralFeature
# import org.eclipse.xtext.nodemodel.util.NodeModelUtils
# import org.eclipse.xtext.validation.Check
# import org.eclipse.xtext.validation.CheckType
# import org.eclipse.xtext.validation.ValidationMessageAcceptor

from org.lflang.lf

# import com.google.inject.Inject

# 
#  * Custom validation checks for Lingua Franca programs.
#  *
#  * Also see: https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#validation
#  *
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Matt Weber <matt.weber@berkeley.edu>}
#  * @author{Christian Menard <christian.menard@tu-dresden.de>}
#  * @author{Hou Seng Wong <stevenhouseng@gmail.com>}
#  * @author{Clément Fournier <clement.fournier76@gmail.com>}
#  
@Inject(optional=True)
class LFValidator(BaseLFValidator):
    """ generated source for class LFValidator """
    # ////////////////////////////////////////////////////////////
    # // Public check methods.
    #  These methods are automatically invoked on AST nodes matching
    #  the types of their arguments.
    #  CheckType.FAST ensures that these checks run whenever a file is modified.
    #  Alternatives are CheckType.NORMAL (when saving) and
    #  CheckType.EXPENSIVE (only when right-click, validate).
    #  FIXME: What is the default when nothing is specified?
    #  These methods are listed in alphabetical order, and, although
    #  it is isn't strictly required, follow a naming convention
    #  checkClass, where Class is the AST class, where possible.
    @Check(CheckType.FAST)
    def checkAction(self, action):
        """ generated source for method checkAction """
        checkName(action.__name__, Literals.VARIABLE__NAME)
        if action.getOrigin() == ActionOrigin.NONE:
            error("Action must have modifier `logical` or `physical`.", Literals.ACTION__ORIGIN)
        if action.getPolicy() != None and not SPACING_VIOLATION_POLICIES.contains(action.getPolicy()):
            error("Unrecognized spacing violation policy: " + action.getPolicy() + ". Available policies are: " + ", ".join( SPACING_VIOLATION_POLICIES) + ".", Literals.ACTION__POLICY)
        checkExpressionAsTime(action.getMinDelay(), Literals.ACTION__MIN_DELAY)
        checkExpressionAsTime(action.getMinSpacing(), Literals.ACTION__MIN_SPACING)

    @Check(CheckType.FAST)
    def checkAssignment(self, assignment):
        """ generated source for method checkAssignment """
        #  If the left-hand side is a time parameter, make sure the assignment has units
        if isOfTimeType(assignment.getLhs()):
            if assignment.getRhs().size() > 1:
                error("Incompatible type.", Literals.ASSIGNMENT__RHS)
            elif assignment.getRhs().size() > 0:
                expr = assignment.getRhs().get(0)
                checkExpressionAsTime(expr, Literals.ASSIGNMENT__RHS)
            #  If this assignment overrides a parameter that is used in a deadline,
            #  report possible overflow.
            if isCBasedTarget() and self.info.overflowingAssignments.contains(assignment):
                error("Time value used to specify a deadline exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.", Literals.ASSIGNMENT__RHS)
        braces = assignment.getBraces()
        if not (braces == None or braces.isEmpty()) and self.target != Target.CPP:
            error("Brace initializers are only supported for the C++ target", Literals.ASSIGNMENT__BRACES)
        #  FIXME: lhs is list => rhs is list
        #  lhs is fixed with size n => rhs is fixed with size n
        #  FIXME": similar checks for decl/init
        #  Specifically for C: list can only be literal or time lists

    @Check(CheckType.FAST)
    def checkConnection(self, connection):
        """ generated source for method checkConnection """
        #  Report if connection is part of a cycle.
        cycles = self.info.topologyCycles()
        for lp in connection.getLeftPorts():
            for rp in connection.getRightPorts():
                leftInCycle = False
                for it in cycles:
                    if (lp.getContainer() == None and it.getDefinition() == lp.getVariable()) or (it.getDefinition() == lp.getVariable() and it.getParent() == lp.getContainer()):
                        leftInCycle = True
                        break
                for it in cycles:
                    if (rp.getContainer() == None and it.getDefinition() == rp.getVariable()) or (it.getDefinition() == rp.getVariable() and it.getParent() == rp.getContainer()):
                        if leftInCycle:
                            reactor = ASTUtils.getEnclosingReactor(connection)
                            reactorName = reactor.__name__
                            error("Connection in reactor {:s} creates".format(reactorName) + "a cyclic dependency between {:s} and {:s}.".format(toOriginalText(lp), toOriginalText(rp)), Literals.CONNECTION__DELAY)
        #  FIXME: look up all ReactorInstance objects that have a definition equal to the
        #  container of this connection. For each of those occurrences, the widths have to match.
        #  For the C target, since C has such a weak type system, check that
        #  the types on both sides of every connection match. For other languages,
        #  we leave type compatibility that language's compiler or interpreter.
        if isCBasedTarget():
            type = None
            for port in connection.getLeftPorts():
                #  If the variable is not a port, then there is some other
                #  error. Avoid a class cast exception.
                if isinstance(, (Port)):
                    if type == None:
                        type = (port.getVariable()).getType()
                    else:
                        #  Unfortunately, xtext does not generate a suitable equals()
                        #  method for AST types, so we have to manually check the types.
                        if not sameType(type, (port.getVariable()).getType()):
                            error("Types do not match.", Literals.CONNECTION__LEFT_PORTS)
            for port in connection.getRightPorts():
                #  If the variable is not a port, then there is some other
                #  error. Avoid a class cast exception.
                if isinstance(, (Port)):
                    if type == None:
                        type = (port.getVariable()).getType()
                    else:
                        if not sameType(type, type = (port.getVariable()).getType()):
                            error("Types do not match.", Literals.CONNECTION__RIGHT_PORTS)
        #  Check whether the total width of the left side of the connection
        #  matches the total width of the right side. This cannot be determined
        #  here if the width is not given as a constant. In that case, it is up
        #  to the code generator to check it.
        leftWidth = 0
        for port in connection.getLeftPorts():
            width = inferPortWidth(port, None, None)
            #  null args imply incomplete check.
            if width < 0 or leftWidth < 0:
                #  Cannot determine the width of the left ports.
                leftWidth = -1
            else:
                leftWidth += width
        rightWidth = 0
        for port in connection.getRightPorts():
            width = inferPortWidth(port, None, None)
            #  null args imply incomplete check.
            if width < 0 or rightWidth < 0:
                #  Cannot determine the width of the left ports.
                rightWidth = -1
            else:
                rightWidth += width
        if leftWidth != -1 and rightWidth != -1 and leftWidth != rightWidth:
            if connection.isIterated():
                if leftWidth == 0 or rightWidth % leftWidth != 0:
                    #  FIXME: The second argument should be Literals.CONNECTION, but
                    #  stupidly, xtext will not accept that. There seems to be no way to
                    #  report an error for the whole connection statement.
                    warning("Left width {:s} does not divide right width {:s}".format(leftWidth, rightWidth), Literals.CONNECTION__LEFT_PORTS)
            else:
                #  FIXME: The second argument should be Literals.CONNECTION, but
                #  stupidly, xtext will not accept that. There seems to be no way to
                #  report an error for the whole connection statement.
                warning("Left width {:s} does not match right width {:s}".format(leftWidth, rightWidth), Literals.CONNECTION__LEFT_PORTS)
        reactor = ASTUtils.getEnclosingReactor(connection)
        #  Make sure the right port is not already an effect of a reaction.
        for reaction in ASTUtils.allReactions(reactor):
            for effect in reaction.getEffects():
                for rightPort in connection.getRightPorts():
                    if rightPort.getVariable() == effect.getVariable() and rightPort.getContainer() == effect.getContainer() and (isinstance(, (Reactor)) or isinstance(, (Reactor)) or connection.eContainer() == reaction.eContainer()):
                        error("Cannot connect: Port named '" + effect.getVariable().__name__ + "' is already effect of a reaction.", Literals.CONNECTION__RIGHT_PORTS)
        #  Check that the right port does not already have some other
        #  upstream connection.
        for c in reactor.getConnections():
            if c != connection:
                for thisRightPort in connection.getRightPorts():
                    for thatRightPort in c.getRightPorts():
                        if thisRightPort.getVariable() == thatRightPort.getVariable() and thisRightPort.getContainer() == thatRightPort.getContainer() and (isinstance(, (Reactor)) or isinstance(, (Reactor)) or connection.eContainer() == c.eContainer()):
                            error("Cannot connect: Port named '" + thisRightPort.getVariable().__name__ + "' may only appear once on the right side of a connection.", Literals.CONNECTION__RIGHT_PORTS)
        #  Check the after delay
        if connection.getDelay() != None:
            delay = connection.getDelay()
            if isinstance(delay, (ParameterReference)) or isinstance(delay, (Time)) or isinstance(delay, (Literal)):
                checkExpressionAsTime(delay, Literals.CONNECTION__DELAY)
            else:
                error("After delays can only be given by time literals or parameters.", Literals.CONNECTION__DELAY)

    @Check(CheckType.FAST)
    def checkDeadline(self, deadline):
        """ generated source for method checkDeadline """
        if isCBasedTarget() and self.info.overflowingDeadlines.contains(deadline):
            error("Deadline exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.", Literals.DEADLINE__DELAY)
        checkExpressionAsTime(deadline.getDelay(), Literals.DEADLINE__DELAY)

    @Check(CheckType.FAST)
    def checkHost(self, host):
        """ generated source for method checkHost """
        addr = host.getAddr()
        user = host.getUser()
        if user != None and not user.matches(USERNAME_REGEX):
            warning("Invalid user name.", Literals.HOST__USER)
        if isinstance(host, (IPV4Host)) and not addr.matches(IPV4_REGEX):
            warning("Invalid IP address.", Literals.HOST__ADDR)
        elif isinstance(host, (IPV6Host)) and not addr.matches(IPV6_REGEX):
            warning("Invalid IP address.", Literals.HOST__ADDR)
        elif isinstance(host, (NamedHost)) and not addr.matches(HOST_OR_FQN_REGEX):
            warning("Invalid host name or fully qualified domain name.", Literals.HOST__ADDR)

    def checkImport(self, imp):
        """ generated source for method checkImport """
        if toDefinition(imp.getReactorClasses().get(0)).eResource().getErrors().size() > 0:
            error("Error loading resource.", Literals.IMPORT__IMPORT_URI)
            return
        for reactor in imp.getReactorClasses():
            if not isUnused(reactor):
                return
        warning("Unused import.", Literals.IMPORT__IMPORT_URI)

    def checkImportedReactor(self, reactor):
        """ generated source for method checkImportedReactor """
        if isUnused(reactor):
            warning("Unused reactor class.", Literals.IMPORTED_REACTOR__REACTOR_CLASS)
        if info.instantiationGraph.hasCycles():
            cycleSet = set()
            for cycle in info.instantiationGraph.getCycles():
                cycleSet.extend(cycle)
            if dependsOnCycle(toDefinition(reactor), cycleSet, HashSet()):
                error("Imported reactor '" + toDefinition(reactor).__name__ + "' has cyclic instantiation in it.", Literals.IMPORTED_REACTOR__REACTOR_CLASS)

    @Check(CheckType.FAST)
    def checkInput(self, input):
        """ generated source for method checkInput """
        parent = input.eContainer()
        if parent.isMain() or parent.isFederated():
            error("Main reactor cannot have inputs.", Literals.VARIABLE__NAME)
        checkName(input.__name__, Literals.VARIABLE__NAME)
        if target.requiresTypes:
            if input.getType() == None:
                error("Input must have a type.", Literals.TYPED_VARIABLE__TYPE)
        if input.isMutable() and self.target == Target.CPP:
            warning("The mutable qualifier has no meaning for the C++ target and should be removed. " + "In C++, any value can be made mutable by calling get_mutable_copy().", Literals.INPUT__MUTABLE)
        if input.getWidthSpec() != None and input.getWidthSpec().isOfVariableLength():
            error("Variable-width multiports are not supported.", Literals.PORT__WIDTH_SPEC)

    @Check(CheckType.FAST)
    def checkInstantiation(self, instantiation):
        """ generated source for method checkInstantiation """
        checkName(instantiation.__name__, Literals.INSTANTIATION__NAME)
        reactor = toDefinition(instantiation.getReactorClass())
        if reactor.isMain() or reactor.isFederated():
            error("Cannot instantiate a main (or federated) reactor: " + instantiation.getReactorClass().__name__, Literals.INSTANTIATION__REACTOR_CLASS)
        if self.info.instantiationGraph.getCycles().size() > 0:
            for cycle in self.info.instantiationGraph.getCycles():
                container = instantiation.eContainer()
                if cycle.contains(container) and cycle.contains(reactor):
                    names = []
                    for r in cycle:
                        names.append(r.__name__)
                    error("Instantiation is part of a cycle: " + ", ".join( names) + ".", Literals.INSTANTIATION__REACTOR_CLASS)
        if instantiation.getWidthSpec() != None and instantiation.getWidthSpec().isOfVariableLength():
            if isCBasedTarget():
                warning("Variable-width banks are for internal use only.", Literals.INSTANTIATION__WIDTH_SPEC)
            else:
                error("Variable-width banks are not supported.", Literals.INSTANTIATION__WIDTH_SPEC)

    @Check(CheckType.FAST)
    def checkKeyValuePair(self, param):
        """ generated source for method checkKeyValuePair """
        if isinstance(, (TargetDecl)):
            prop = TargetProperty.forName(param.__name__)
            if prop == None:
                options = ""
                warning("Unrecognized target parameter: " + param.__name__ + ". Recognized parameters are: " + options, Literals.KEY_VALUE_PAIR__NAME)
            else:
                if not prop.supportedBy.contains(self.target):
                    warning("The target parameter: " + param.__name__ + " is not supported by the " + self.target + " target and will thus be ignored.", Literals.KEY_VALUE_PAIR__NAME)
                prop.type.check(param.getValue(), param.__name__, self)
            for it in targetPropertyErrors:
                error(it, Literals.KEY_VALUE_PAIR__VALUE)
            targetPropertyErrors = []
            for it in targetPropertyWarnings:
                error(it, Literals.KEY_VALUE_PAIR__VALUE)
            targetPropertyWarnings = []

    @Check(CheckType.FAST)
    def checkModel(self, model):
        """ generated source for method checkModel """
        if not info.updated:
            info.update(model, errorReporter)

    @Check(CheckType.NORMAL)
    def updateModelInfo(self, model):
        """ generated source for method updateModelInfo """
        info.update(model, errorReporter)

    @Check(CheckType.FAST)
    def checkOutput(self, output):
        """ generated source for method checkOutput """
        parent = output.eContainer()
        if parent.isMain() or parent.isFederated():
            error("Main reactor cannot have outputs.", Literals.VARIABLE__NAME)
        checkName(output.__name__, Literals.VARIABLE__NAME)
        if self.target.requiresTypes:
            if output.getType() == None:
                error("Output must have a type.", Literals.TYPED_VARIABLE__TYPE)
        if output.getWidthSpec() != None and output.getWidthSpec().isOfVariableLength():
            error("Variable-width multiports are not supported.", Literals.PORT__WIDTH_SPEC)

    @Check(CheckType.FAST)
    def checkParameter(self, param):
        """ generated source for method checkParameter """
        checkName(param.__name__, Literals.PARAMETER__NAME)
        for expr in param.getInit():
            if isinstance(expr, (ParameterReference)):
                error("Parameter cannot be initialized using parameter.", Literals.PARAMETER__INIT)
        if param.getInit() == None or param.getInit().size() == 0:
            error("Uninitialized parameter.", Literals.PARAMETER__INIT)
        elif isOfTimeType(param):
            if param.getInit().size() > 1 and param.getType().getArraySpec() == None:
                error("Time parameter cannot be initialized using a list.", Literals.PARAMETER__INIT)
            else:
                expr = param.getInit().get(0)
                if not (isinstance(expr, (Time))):
                    if not ASTUtils.isZero(expr):
                        if ASTUtils.isInteger(expr):
                            error("Missing time unit.", Literals.PARAMETER__INIT)
                        else:
                            error("Invalid time literal.", Literals.PARAMETER__INIT)
        elif self.target.requiresTypes:
            if (ASTUtils.getInferredType(param).isUndefined()):
                error("Type declaration missing.", Literals.PARAMETER__TYPE)
        if self.target == Target.CPP:
            container = param.eContainer()
            reactor = container
            if reactor.isMain():
                cliParams = list("t", "threads", "o", "timeout", "k", "keepalive", "f", "fast", "help")
                if cliParams.contains(param.__name__):
                    error("Parameter '" + param.__name__ + "' is already in use as command line argument by Lingua Franca,", Literals.PARAMETER__NAME)
        if isCBasedTarget() and self.info.overflowingParameters.contains(param):
            error("Time value used to specify a deadline exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.", Literals.PARAMETER__INIT)
        braces = param.getBraces()
        if not (braces == None or braces.isEmpty()) and self.target != Target.CPP:
            error("Brace initializers are only supported for the C++ target", Literals.PARAMETER__BRACES)

    @Check(CheckType.FAST)
    def checkPreamble(self, preamble):
        """ generated source for method checkPreamble """
        if self.target == Target.CPP:
            if preamble.getVisibility() == Visibility.NONE:
                error("Preambles for the C++ target need a visibility qualifier (private or public)!", Literals.PREAMBLE__VISIBILITY)
            elif preamble.getVisibility() == Visibility.PRIVATE:
                container = preamble.eContainer()
                if container != None and isinstance(container, (Reactor)):
                    reactor = container
                    if isGeneric(reactor):
                        warning("Private preambles in generic reactors are not truly private. " + "Since the generated code is placed in a *_impl.hh file, it will " + "be visible on the public interface. Consider using a public " + "preamble within the reactor or a private preamble on file scope.", Literals.PREAMBLE__VISIBILITY)
        elif preamble.getVisibility() != Visibility.NONE:
            warning("The {:s} qualifier has no meaning for the {:s} target. It should be removed.".format(preamble.getVisibility(), self.target.name()), Literals.PREAMBLE__VISIBILITY)

    @Check(CheckType.FAST)
    def checkReaction(self, reaction):
        """ generated source for method checkReaction """
        if reaction.getTriggers() == None or reaction.getTriggers().size() == 0:
            warning("Reaction has no trigger.", Literals.REACTION__TRIGGERS)
        triggers = set()
        for trigger in reaction.getTriggers():
            if isinstance(trigger, (VarRef)):
                triggerVarRef = trigger
                triggers.append(triggerVarRef.getVariable())
                if isinstance(triggerVarRef, (Input)):
                    if triggerVarRef.getContainer() != None:
                        error("Cannot have an input of a contained reactor as a trigger: {:s}.{:s}".format(triggerVarRef.getContainer().__name__, triggerVarRef.getVariable().__name__), Literals.REACTION__TRIGGERS)
                elif isinstance(, (Output)):
                    if triggerVarRef.getContainer() == None:
                        error("Cannot have an output of this reactor as a trigger: {:s}".format(triggerVarRef.getVariable().__name__), Literals.REACTION__TRIGGERS)
        for source in reaction.getSources():
            if triggers.contains(source.getVariable()):
                error("Source is already listed as a trigger: {:s}".format(source.getVariable().__name__), Literals.REACTION__SOURCES)
            if isinstance(, (Input)):
                if source.getContainer() != None:
                    error("Cannot have an input of a contained reactor as a source: {:s}.{:s}".format(source.getContainer().__name__, source.getVariable().__name__), Literals.REACTION__SOURCES)
            elif isinstance(, (Output)):
                if source.getContainer() == None:
                    error("Cannot have an output of this reactor as a source: {:s}".format(source.getVariable().__name__), Literals.REACTION__SOURCES)
        for effect in reaction.getEffects():
            if isinstance(, (Input)):
                if effect.getContainer() == None:
                    error("Cannot have an input of this reactor as an effect: {:s}".format(effect.getVariable().__name__), Literals.REACTION__EFFECTS)
            elif isinstance(, (Output)):
                if effect.getContainer() != None:
                    error("Cannot have an output of a contained reactor as an effect: {:s}.{:s}".format(effect.getContainer().__name__, effect.getVariable().__name__), Literals.REACTION__EFFECTS)
        cycles = self.info.topologyCycles()
        reactor = ASTUtils.getEnclosingReactor(reaction)
        reactionInCycle = False
        for it in cycles:
            if it.getDefinition() == reaction:
                reactionInCycle = True
                break
        if reactionInCycle:
            trigs = []
            for t in reaction.getTriggers():
                if not (isinstance(t, (VarRef))):
                    continue 
                tVarRef = t
                triggerExistsInCycle = False
                for c in cycles:
                    if c.getDefinition() == tVarRef.getVariable():
                        triggerExistsInCycle = True
                        break
                if triggerExistsInCycle:
                    trigs.append(toOriginalText(tVarRef))
            if len(trigs) > 0:
                error("Reaction triggers involved in cyclic dependency in reactor {:s}: {:s}.".format(reactor.__name__, ", ".join( trigs)), Literals.REACTION__TRIGGERS)
            sources = []
            for t in reaction.getSources():
                sourceExistInCycle = False
                for c in cycles:
                    if c.getDefinition() == t.getVariable():
                        sourceExistInCycle = True
                        break
                if sourceExistInCycle:
                    sources.append(toOriginalText(t))
            if len(sources) > 0:
                error("Reaction sources involved in cyclic dependency in reactor {:s}: {:s}.".format(reactor.__name__, ", ".join( sources)), Literals.REACTION__SOURCES)
            effects = []
            for t in reaction.getEffects():
                effectExistInCycle = False
                for c in cycles:
                    if c.getDefinition() == t.getVariable():
                        effectExistInCycle = True
                        break
                if effectExistInCycle:
                    effects.append(toOriginalText(t))
            if len(effects) > 0:
                error("Reaction effects involved in cyclic dependency in reactor {:s}: {:s}.".format(reactor.__name__, ", ".join( effects)), Literals.REACTION__EFFECTS)
            if len(trigs) + len(sources) == 0:
                error("Cyclic dependency due to preceding reaction. Consider reordering reactions within reactor {:s} to avoid causality loop.".format(reactor.__name__), reaction.eContainer(), Literals.REACTOR__REACTIONS, reactor.getReactions().indexOf(reaction))
            elif len(effects) == 0:
                error("Cyclic dependency due to succeeding reaction. Consider reordering reactions within reactor {:s} to avoid causality loop.".format(reactor.__name__), reaction.eContainer(), Literals.REACTOR__REACTIONS, reactor.getReactions().indexOf(reaction))

    @Check(CheckType.FAST)
    def checkReactor(self, reactor):
        """ generated source for method checkReactor """
        superClasses = ASTUtils.superClasses(reactor)
        if superClasses == None:
            error("Problem with superclasses: Either they form a cycle or are not defined", Literals.REACTOR_DECL__NAME)
            superClasses = {}
        name = FileUtil.nameWithoutExtension(reactor.eResource())
        if reactor.__name__ == None:
            if not reactor.isFederated() and not reactor.isMain():
                error("Reactor must be named.", Literals.REACTOR_DECL__NAME)
                return
        iter = reactor.eResource().getAllContents()
        if reactor.isFederated() or reactor.isMain():
            if reactor.__name__ != None and not reactor.__name__ == name:
                error("Name of main reactor must match the file name (or be omitted).", Literals.REACTOR_DECL__NAME)
            nMain = countMainOrFederated(iter)
            if nMain > 1:
                attribute = Literals.REACTOR__MAIN
                if reactor.isFederated():
                    attribute = Literals.REACTOR__FEDERATED
                error("Multiple definitions of main or federated reactor.", attribute)
        else:
            nMain = countMainOrFederated(iter)
            if nMain > 0 and reactor.__name__ == name:
                error("Name conflict with main reactor.", Literals.REACTOR_DECL__NAME)
        checkName(reactor.__name__, Literals.REACTOR_DECL__NAME)
        if self.target == Target.CPP and reactor.__name__.lower() == "preamble".lower():
            error("Reactor cannot be named '" + reactor.__name__ + "'", Literals.REACTOR_DECL__NAME)
        if reactor.getHost() != None:
            if not reactor.isFederated():
                error("Cannot assign a host to reactor '" + reactor.__name__ + "' because it is not federated.", Literals.REACTOR__HOST)
        variables = []
        variables.addAll(reactor.getInputs())
        variables.addAll(reactor.getOutputs())
        variables.addAll(reactor.getActions())
        variables.addAll(reactor.getTimers())
        for superClass in superClasses:
            conflicts = set()
            checkConflict(superClass.getInputs(), reactor.getInputs(), variables, conflicts)
            checkConflict(superClass.getOutputs(), reactor.getOutputs(), variables, conflicts)
            checkConflict(superClass.getActions(), reactor.getActions(), variables, conflicts)
            for timer in superClass.getTimers():
                filteredVariables = ArrayList(variables)
                if hasNameConflict(timer, filteredVariables):
                    conflicts.append(timer)
                else:
                    variables.append(timer)
            if len(conflicts) > 0:
                names = []
                for it in conflicts:
                    names.append(it.__name__)
                error("Cannot extend {:s} due to the following conflicts: {:s}.".format(superClass.__name__, ",".join(names)), Literals.REACTOR__SUPER_CLASSES)

    @Check(CheckType.FAST)
    def checkSerializer(self, serializer):
        """ generated source for method checkSerializer """
        isValidSerializer = False
        for method_ in SupportedSerializers.values():
            if method_.name().lower() == serializer.getType(.lower()):
                isValidSerializer = True
        if not isValidSerializer:
            error("Serializer can be " + Arrays.asList(SupportedSerializers.values()), Literals.SERIALIZER__TYPE)

    @Check(CheckType.FAST)
    def checkState(self, stateVar):
        """ generated source for method checkState """
        checkName(stateVar.__name__, Literals.STATE_VAR__NAME)
        if isOfTimeType(stateVar):
            if stateVar.getInit() != None:
                for expr in stateVar.getInit():
                    checkExpressionAsTime(expr, Literals.STATE_VAR__INIT)
        elif self.target.requiresTypes and ASTUtils.getInferredType(stateVar).isUndefined():
            error("State must have a type.", Literals.STATE_VAR__TYPE)
        if isCBasedTarget() and stateVar.getInit().size() > 1:
            for expr in stateVar.getInit():
                if isinstance(expr, (ParameterReference)):
                    error("List items cannot refer to a parameter.", Literals.STATE_VAR__INIT)
                    break
        braces = stateVar.getBraces()
        if not (braces == None or braces.isEmpty()) and self.target != Target.CPP:
            error("Brace initializers are only supported for the C++ target", Literals.STATE_VAR__BRACES)

    @Check(CheckType.FAST)
    def checkSTPOffset(self, stp):
        """ generated source for method checkSTPOffset """
        if isCBasedTarget() and self.info.overflowingSTP.contains(stp):
            error("STP offset exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.", Literals.STP__VALUE)

    @Check(CheckType.FAST)
    def checkTargetDecl(self, target):
        """ generated source for method checkTargetDecl """
        targetOpt = Target.forName(target.__name__)
        if targetOpt.isEmpty():
            error("Unrecognized target: " + target.__name__, Literals.TARGET_DECL__NAME)
        else:
            self.target = targetOpt.get()
        lfFileName = FileUtil.nameWithoutExtension(target.eResource())
        if Character.isDigit(lfFileName.charAt(0)):
            errorReporter.reportError("LF file names must not start with a number")

    @Check(CheckType.EXPENSIVE)
    def checkTargetProperties(self, targetProperties):
        """ generated source for method checkTargetProperties """
        validateFastTargetProperty(targetProperties)
        validateClockSyncTargetProperties(targetProperties)
        validateSchedulerTargetProperties(targetProperties)
        validateRos2TargetProperties(targetProperties)

    def getKeyValuePair(self, targetProperties, property):
        """ generated source for method getKeyValuePair """
        properties = targetProperties.getPairs().stream()
        assert (len(properties) <= 1)
        return properties.get(0) if len(properties) > 0 else None

    def validateFastTargetProperty(self, targetProperties):
        """ generated source for method validateFastTargetProperty """
        fastTargetProperty = self.getKeyValuePair(targetProperties, TargetProperty.FAST)
        if fastTargetProperty != None:
            for reactor in info.model.getReactors():
                if reactor.isFederated():
                    error("The fast target property is incompatible with federated programs.", fastTargetProperty, Literals.KEY_VALUE_PAIR__NAME)
                    break
            for reactor in info.model.getReactors():
                for action in reactor.getActions():
                    if action.getOrigin() == ActionOrigin.PHYSICAL:
                        error("The fast target property is incompatible with physical actions.", fastTargetProperty, Literals.KEY_VALUE_PAIR__NAME)
                        break

    def validateClockSyncTargetProperties(self, targetProperties):
        """ generated source for method validateClockSyncTargetProperties """
        clockSyncTargetProperty = self.getKeyValuePair(targetProperties, TargetProperty.CLOCK_SYNC)
        if clockSyncTargetProperty != None:
            federatedExists = False
            for reactor in info.model.getReactors():
                if reactor.isFederated():
                    federatedExists = True
            if not federatedExists:
                warning("The clock-sync target property is incompatible with non-federated programs.", clockSyncTargetProperty, Literals.KEY_VALUE_PAIR__NAME)

    def validateSchedulerTargetProperties(self, targetProperties):
        """ generated source for method validateSchedulerTargetProperties """
        schedulerTargetProperty = self.getKeyValuePair(targetProperties, TargetProperty.SCHEDULER)
        if schedulerTargetProperty != None:
            schedulerName = ASTUtils.elementToSingleString(schedulerTargetProperty.getValue())
            try:
                if not TargetProperty.SchedulerOption.valueOf(schedulerName).prioritizesDeadline():
                    if info.model.getReactors().stream().anyMatch():
                        warning("This program contains deadlines, but the chosen " + schedulerName + " scheduler does not prioritize reaction execution " + "based on deadlines. This might result in a sub-optimal " + "scheduling.", schedulerTargetProperty, Literals.KEY_VALUE_PAIR__VALUE)
            except IllegalArgumentException as e:
                pass

    def validateRos2TargetProperties(self, targetProperties):
        """ generated source for method validateRos2TargetProperties """
        ros2 = self.getKeyValuePair(targetProperties, TargetProperty.ROS2)
        ros2Dependencies = self.getKeyValuePair(targetProperties, TargetProperty.ROS2_DEPENDENCIES)
        if not ASTUtils.toBoolean(ros2.getValue()) and ros2Dependencies != None:
            warning("Ignoring ros2-dependencies as ros2 compilation is disabled", ros2Dependencies, Literals.KEY_VALUE_PAIR__NAME)

    @Check(CheckType.FAST)
    def checkTimer(self, timer):
        """ generated source for method checkTimer """
        checkName(timer.__name__, Literals.VARIABLE__NAME)
        checkExpressionAsTime(timer.getOffset(), Literals.TIMER__OFFSET)
        checkExpressionAsTime(timer.getPeriod(), Literals.TIMER__PERIOD)

    @Check(CheckType.FAST)
    def checkType(self, type):
        """ generated source for method checkType """
        if self.target == Target.CPP:
            if type.getStars().size() > 0:
                warning("Raw pointers should be avoided in conjunction with LF. Ports " + "and actions implicitly use smart pointers. In this case, " + "the pointer here is likely not needed. For parameters and state " + "smart pointers should be used explicitly if pointer semantics " + "are really needed.", Literals.TYPE__STARS)
        elif self.target == Target.Python:
            if type != None:
                error("Types are not allowed in the Python target", Literals.TYPE__ID)

    @Check(CheckType.FAST)
    def checkVarRef(self, varRef):
        """ generated source for method checkVarRef """
        if varRef.isInterleaved():
            supportedTargets = list(Target.CPP, Target.Python, Target.Rust)
            if not supportedTargets.contains(self.target) and not isCBasedTarget():
                error("This target does not support interleaved port references.", Literals.VAR_REF__INTERLEAVED)
            if not (isinstance(, (Connection))):
                error("interleaved can only be used in connections.", Literals.VAR_REF__INTERLEAVED)
            if isinstance(, (Port)):
                if varRef.getContainer() == None or varRef.getContainer().getWidthSpec() == None or (varRef.getVariable()).getWidthSpec() == None:
                    error("interleaved can only be used for multiports contained within banks.", Literals.VAR_REF__INTERLEAVED)

    @Check(CheckType.FAST)
    def checkAttributes(self, attr):
        """ generated source for method checkAttributes """
        name = attr.getAttrName().__str__()
        spec = AttributeSpec.ATTRIBUTE_SPECS_BY_NAME.get(name)
        if spec == None:
            error("Unknown attribute.", Literals.ATTRIBUTE__ATTR_NAME)
            return
        spec.check(self, attr)

    @Check(CheckType.FAST)
    def checkWidthSpec(self, widthSpec):
        """ generated source for method checkWidthSpec """
        if not self.target.supportsMultiports():
            error("Multiports and banks are currently not supported by the given target.", Literals.WIDTH_SPEC__TERMS)
        else:
            for term in widthSpec.getTerms():
                if term.getParameter() != None:
                    if not self.target.supportsParameterizedWidths():
                        error("Parameterized widths are not supported by this target.", Literals.WIDTH_SPEC__TERMS)
                elif term.getPort() != None:
                    error("widthof is not supported.", Literals.WIDTH_SPEC__TERMS)
                elif term.getCode() != None:
                    if self.target != Target.CPP:
                        error("This target does not support width given as code.", Literals.WIDTH_SPEC__TERMS)
                elif term.getWidth() < 0:
                    error("Width must be a positive integer.", Literals.WIDTH_SPEC__TERMS)

    @Check(CheckType.FAST)
    def checkReactorIconAttribute(self, reactor):
        """ generated source for method checkReactorIconAttribute """
        attrs = AttributeUtils.getAttributes(reactor)
        iconAttr = attrs.stream()
        if iconAttr != None:
            path = iconAttr.getAttrParms().get(0).getValue().getStr()
            validExtensions = Set.of("bmp", "png", "gif", "ico", "jpeg")
            extensionStrart = path.lastIndexOf(".")
            extension = path.substring(extensionStrart + 1) if extensionStrart != -1 else ""
            if not validExtensions.contains(extension.lower()):
                warning("File extension '" + extension + "' is not supported. Provide any of: " + ", ".join( validExtensions), iconAttr.getAttrParms().get(0), Literals.ATTR_PARM__VALUE)
                return
            iconLocation = FileUtil.locateFile(path, reactor.eResource())
            if iconLocation == None:
                warning("Cannot locate icon file.", iconAttr.getAttrParms().get(0), Literals.ATTR_PARM__VALUE)
            if ("file" == iconLocation.getScheme() or iconLocation.getScheme() == None) and not (File(iconLocation.getPath()).exists()):
                warning("Icon does not exist.", iconAttr.getAttrParms().get(0), Literals.ATTR_PARM__VALUE)

    @Check(CheckType.FAST)
    def checkInitialMode(self, reactor):
        """ generated source for method checkInitialMode """
        if not reactor.getModes().isEmpty():
            initialModesCount = 0
            if initialModesCount == 0:
                error("Every modal reactor requires one initial mode.", Literals.REACTOR__MODES, 0)
            elif initialModesCount > 1:

    @Check(CheckType.FAST)
    def checkModeStateNamespace(self, reactor):
        """ generated source for method checkModeStateNamespace """
        if not reactor.getModes().isEmpty():
            names = []
            for mode in reactor.getModes():
                for stateVar in mode.getStateVars():
                    if names.contains(stateVar.__name__):
                        error("Duplicate state variable '{:s}'. (State variables are currently scoped on reactor level not modes)".format(stateVar.__name__), stateVar, Literals.STATE_VAR__NAME)
                    names.append(stateVar.__name__)

    @Check(CheckType.FAST)
    def checkModeTimerNamespace(self, reactor):
        """ generated source for method checkModeTimerNamespace """
        if not reactor.getModes().isEmpty():
            names = []
            for mode in reactor.getModes():
                for timer in mode.getTimers():
                    if names.contains(timer.__name__):
                        error("Duplicate Timer '{:s}'. (Timers are currently scoped on reactor level not modes)".format(timer.__name__), timer, Literals.VARIABLE__NAME)
                    names.append(timer.__name__)

    @Check(CheckType.FAST)
    def checkModeActionNamespace(self, reactor):
        """ generated source for method checkModeActionNamespace """
        if not reactor.getModes().isEmpty():
            names = []
            for mode in reactor.getModes():
                for action in mode.getActions():
                    if names.contains(action.__name__):
                        error("Duplicate Action '{:s}'. (Actions are currently scoped on reactor level not modes)".format(action.__name__), action, Literals.VARIABLE__NAME)
                    names.append(action.__name__)

    @Check(CheckType.FAST)
    def checkModeInstanceNamespace(self, reactor):
        """ generated source for method checkModeInstanceNamespace """
        if not reactor.getModes().isEmpty():
            names = []
            for mode in reactor.getModes():
                for instantiation in mode.getInstantiations():
                    if names.contains(instantiation.__name__):
                        error("Duplicate Instantiation '{:s}'. (Instantiations are currently scoped on reactor level not modes)".format(instantiation.__name__), instantiation, Literals.INSTANTIATION__NAME)
                    names.append(instantiation.__name__)

    @Check(CheckType.FAST)
    def checkMissingStateResetInMode(self, reactor):
        """ generated source for method checkMissingStateResetInMode """
        if not reactor.getModes().isEmpty():
            resetModes = set()
            for m in reactor.getModes():
                for r in m.getReactions():
                    for e in r.getEffects():
                        if isinstance(, (Mode)) and e.getTransition() != ModeTransition.HISTORY:
                            resetModes.append(e.getVariable())
            for m in resetModes:
                if not m.getStateVars().isEmpty():
                    hasResetReaction = None
                    if not hasResetReaction:
                        for s in m.getStateVars():
                            if not s.isReset():
                                error("State variable is not reset upon mode entry. It is neither marked for automatic reset nor is there a reset reaction.", m, Literals.MODE__STATE_VARS, m.getStateVars().indexOf(s))
                if not m.getInstantiations().isEmpty():
                    for i in m.getInstantiations():
                        error = {}
                        checked = set()
                        toCheck = LinkedList()
                        toCheck.append(i.getReactorClass())
                        while not toCheck.isEmpty():
                            check = toCheck.pop()
                            checked.append(check)
                            if not check.getStateVars().isEmpty():
                                hasResetReaction = None
                                if not hasResetReaction:
                            for innerInstance in check.getInstantiations():
                                next = innerInstance.getReactorClass()
                                if not checked.contains(next):
                                    toCheck.push(next)
                        if not error.isEmpty():
                            error("This reactor contains state variables that are not reset upon mode entry: ")

    @Check(CheckType.FAST)
    def checkStateResetWithoutInitialValue(self, state):
        """ generated source for method checkStateResetWithoutInitialValue """
        if state.isReset() and (state.getInit() == None or state.getInit().isEmpty()):
            error("The state variable can not be automatically reset without an initial value.", state, Literals.STATE_VAR__RESET)

    @Check(CheckType.FAST)
    def checkUnspecifiedTransitionType(self, reaction):
        """ generated source for method checkUnspecifiedTransitionType """
        for effect in reaction.getEffects():
            variable = effect.getVariable()
            if isinstance(variable, (Mode)):
                transitionAssignment = NodeModelUtils.findNodesForFeature(effect, Literals.VAR_REF__TRANSITION)
                if transitionAssignment.isEmpty():
                    mode = variable
                    makesDifference = None
                    if not makesDifference and not mode.getInstantiations().isEmpty():
                        for i in mode.getInstantiations():
                            checked = set()
                            toCheck = LinkedList()
                            toCheck.append(i.getReactorClass())
                            while not toCheck.isEmpty() and not makesDifference:
                                check = toCheck.pop()
                                checked.append(check)
                                makesDifference |= None
                                for innerInstance in check.getInstantiations():
                                    next = innerInstance.getReactorClass()
                                    if not checked.contains(next):
                                        toCheck.push(next)
                    if makesDifference:
                        warning("You should specifiy a transition type! " + "Reset and history transitions have different effects on this target mode. " + "Currently, a reset type is implicitly assumed.", reaction, Literals.REACTION__EFFECTS, reaction.getEffects().indexOf(effect))

    def getErrorReporter(self):
        """ generated source for method getErrorReporter """
        return self.errorReporter

    def getMessageAcceptor(self):
        """ generated source for method getMessageAcceptor """
        return self if messageAcceptor == None else messageAcceptor

    def getTargetPropertyErrors(self):
        """ generated source for method getTargetPropertyErrors """
        return self.targetPropertyErrors

    def error(self, message, feature):
        """ generated source for method error """
        super(LFValidator, self).error(message, feature)

    def checkConflict(self, superVars, sameKind, allOwn, conflicts):
        """ generated source for method checkConflict """
        for superVar in superVars:
            match = None
            for it in sameKind:
                if it.__name__ == superVar.__name__:
                    match = it
                    break
            rest = ArrayList(allOwn)
            if (match != None and superVar.getType() != match.getType()) or hasNameConflict(superVar, rest):
                conflicts.append(superVar)
            else:
                allOwn.append(superVar)

    def checkName(self, name, feature):
        """ generated source for method checkName """
        if 2 >= len(name) and name.substring(0, 2) == "__":
            self.error(UNDERSCORE_MESSAGE + name, feature)
        if self.target.isReservedIdent(name):
            self.error(RESERVED_MESSAGE + name, feature)
        if self.target == Target.TS:
            if name == "actions":
                self.error(ACTIONS_MESSAGE + name, feature)

    def checkExpressionAsTime(self, expr, eReference):
        """ generated source for method checkExpressionAsTime """
        if expr == None:
            return
        if isinstance(expr, (ParameterReference)):
            param = (expr).getParameter()
            if not isOfTimeType(param) and target.requiresTypes:
                self.error("Parameter is not of time type.", eReference)
        elif isinstance(expr, (Literal)) and isInteger(expr):
            if not isZero(expr):
                self.error("Missing time unit.", eReference)
        elif not (isinstance(expr, (Time))):
            self.error("Invalid time literal.", eReference)

    def countMainOrFederated(self, iter):
        """ generated source for method countMainOrFederated """
        nMain = 0
        while iter.hasNext():
            obj = iter.next()
            if not (isinstance(obj, (Reactor))):
                continue 
            r = obj
            if r.isMain() or r.isFederated():
                nMain += 1
        return nMain

    def dependsOnCycle(self, reactor, cycleSet, visited):
        """ generated source for method dependsOnCycle """
        origins = info.instantiationGraph.getUpstreamAdjacentNodes(reactor)
        if visited.contains(reactor):
            return False
        else:
            visited.append(reactor)
            for it in origins:
                if cycleSet.contains(it) or self.dependsOnCycle(it, cycleSet, visited):
                    return True
        return False

    def hasNameConflict(self, element, toCheckAgainst):
        """ generated source for method hasNameConflict """
        numNameConflicts = 0
        for it in toCheckAgainst:
            if it.__name__ == element.__name__:
                numNameConflicts += 1
        return numNameConflicts > 0

    def isCBasedTarget(self):
        """ generated source for method isCBasedTarget """
        return (self.target == Target.C or self.target == Target.CCPP)

    def isUnused(self, reactor):
        """ generated source for method isUnused """
        instantiations = reactor.eResource().getAllContents()
        subclasses = reactor.eResource().getAllContents()
        instantiationsCheck = True
        while instantiations.hasNext() and instantiationsCheck:
            obj = instantiations.next()
            if not (isinstance(obj, (Instantiation))):
                continue 
            inst = obj
            instantiationsCheck &= (inst.getReactorClass() != reactor and inst.getReactorClass() != reactor.getReactorClass())
        subclassesCheck = True
        while subclasses.hasNext() and subclassesCheck:
            obj = subclasses.next()
            if not (isinstance(obj, (Reactor))):
                continue 
            subclass = obj
            for decl in subclass.getSuperClasses():
                subclassesCheck &= (decl != reactor and decl != reactor.getReactorClass())
        return instantiationsCheck and subclassesCheck

    def sameType(self, type1, type2):
        """ generated source for method sameType """
        if type1 == None:
            return type2 == None
        if type2 == None:
            return type1 == None
        if type1.getId() != None:
            if type1.getStars() != None:
                if type2.getStars() == None:
                    return False
                if type1.getStars().size() != type2.getStars().size():
                    return False
            return (type1.getId() == type2.getId())
        if type1.isTime():
            if not type2.isTime():
                return False
            return True
        return type1.getCode().getBody() == type2.getCode(.getBody())

    errorReporter = ValidatorErrorReporter(getMessageAcceptor(), ValidatorStateAccess())
    info = ModelInfo()
    messageAcceptor = None
    target = None
    targetPropertyErrors = ArrayList()
    targetPropertyWarnings = ArrayList()
    ACTIONS_MESSAGE = "\"actions\" is a reserved word for the TypeScript target for objects " + "(inputs, outputs, actions, timers, parameters, state, reactor definitions, " + "and reactor instantiation): "
    HOST_OR_FQN_REGEX = "^([a-z0-9]+(-[a-z0-9]+)*)|(([a-z0-9]+(-[a-z0-9]+)*\\.)+[a-z]{2,})$"
    IPV4_REGEX = "((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}" + "(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])"
    IPV6_REGEX = "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|" + "([0-9a-fA-F]{1,4}:){1,7}:|" + "([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|" + "([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|" + "([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|" + "([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|" + "([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|" + "[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|" + ":((:[0-9a-fA-F]{1,4}){1,7}|:)|" + "fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|" + "::(ffff(:0{1,4}){0,1}:){0,1}" + IPV4_REGEX + "|" + "([0-9a-fA-F]{1,4}:){1,4}:" + IPV4_REGEX + "|" + "([0-9a-fA-F]{1,4}:){1,6}" + IPV4_REGEX + ")"
    RESERVED_MESSAGE = "Reserved words in the target language are not allowed for objects " + "(inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation): "
    SPACING_VIOLATION_POLICIES = list("defer", "drop", "replace")
    UNDERSCORE_MESSAGE = "Names of objects (inputs, outputs, actions, timers, parameters, " + "state, reactor definitions, and reactor instantiation) may not start with \"__\": "
    USERNAME_REGEX = "^[a-z_]([a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\\$)$"
