#!/usr/bin/env python
""" generated source for module GeneratorBase """
# 
# Copyright (c) 2019-2020, The University of California at Berkeley.
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
# package: org.lflang.generator
# import java.io.IOException
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.ArrayList
# import java.util.HashSet
# import java.util.LinkedHashMap
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Map
# import java.util.Set
# import java.util.regex.Matcher
# import java.util.regex.Pattern
# import org.eclipse.core.resources.IMarker
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.emf.ecore.util.EcoreUtil
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.xbase.lib.CollectionLiterals
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.IteratorExtensions
# import org.eclipse.xtext.xbase.lib.Pair
import os
import sys

from lflang import ASTUtils, TimeUnit
from lflang.MainConflictChecker import MainConflictChecker
from lflang.TargetConfig import TargetConfig
from lflang.TargetProperty import CoordinationType
from lflang.TimeValue import TimeValue
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import EcoreUtil
from lflang.federated import FedASTUtils
from lflang.federated.FederateInstance import FederateInstance
from lflang.generator import GeneratorUtils, LFGeneratorContext, EclipseErrorReporter
from lflang.generator.GeneratorCommandFactory import GeneratorCommandFactory
from lflang.generator.ReactorInstance import ReactorInstance
from lflang.generator.c.CGenerator import IteratorExtensions
from lflang.graph.InstantiationGraph import InstantiationGraph
from lflang.lf import Reactor, LfFactory, Model, Time, Expression
import re
from include.overloading import *
# import com.google.common.base.Objects
# import com.google.common.collect.Iterables

# 
# Generator base class for specifying core functionality
# that all code generators should have.
# 
# @author{Edward A. Lee <eal@berkeley.edu>}
# @author{Marten Lohstroh <marten@berkeley.edu>}
# @author{Christian Menard <christian.menard@tu-dresden.de}
# @author{Matt Weber <matt.weber@berkeley.edu>}
# @author{Soroush Bateni <soroush@utdallas.edu>}
#
from lflang.validation import AbstractLFValidator

class IMarker:
    pass

class GeneratorBase(AbstractLFValidator):
    # Constant that specifies how to name generated delay reactors.
    GEN_DELAY_CLASS_NAME = "_lf_GenDelay"

    def __init__(self, fileConfig, errorReporter):
        super().__init__()
        # The current file configuration.

        self.fileConfig = fileConfig
        #  An error reporter for reporting any errors or warnings during the code generation 

        self.errorReporter = errorReporter
        # A factory for compiler commands.

        self.commandFactory = GeneratorCommandFactory(errorReporter, fileConfig)
        # //////////////////////////////////////////
        # // Public fields.
        # The main (top-level) reactor instance.
        self.main = None
        
        # //////////////////////////////////////////
        # // Protected fields.
        # The current target configuration.
        self.targetConfig = TargetConfig()

        # Collection of generated delay classes.
        self.delayClasses = set()

        # Definition of the main (top-level) reactor.
        # This is an automatically generated AST node for the top-level
        # reactor.
        self.mainDef = None
    
        # A list of Reactor definitions in the main resource, including non-main
        # reactors defined in imported resources. These are ordered in the list in
        # such a way that each reactor is preceded by any reactor that it instantiates
        # using a command like `foo = new Foo();`
        self.reactors = []
    
        # The set of resources referenced reactor classes reside in.
        self.resources = set()
    
        # Graph that tracks dependencies between instantiations.
        # This is a graph where each node is a Reactor (not a ReactorInstance)
        # and an arc from Reactor A to Reactor B means that B contains an instance of A, constructed with a statement
        # like `a = new A();`  After creating the graph,
        # sort the reactors in topological order and assign them to the reactors class variable.
        # Hence, after this method returns, `this.reactors` will be a list of Reactors such that any
        # reactor is preceded in the list by reactors that it instantiates.
        self.instantiationGraph = None
        
        # The set of unordered reactions. An unordered reaction is one that does
        # not have any dependency on other reactions in the containing reactor,
        # and where no other reaction in the containing reactor depends on it.
        # There is currently no way in the syntax of LF to make a reaction
        # unordered, deliberately, because it can introduce unexpected
        # nondeterminacy. However, certain automatically generated reactions are
        # known to be safe to be unordered because they do not interact with the
        # state of the containing reactor. To make a reaction unordered, when
        # the Reaction instance is created, add that instance to this set.
        self.unorderedReactions = set()
    
        # Map from reactions to bank indices
        self.reactionBankIndices = None
    
        # Keep a unique list of enabled serializers
        self.enabledSerializers = set()
    
        # Indicates whether or not the current Lingua Franca program
        # contains a federation.
        self.isFederated = False
    
        # Indicates whether or not the current Lingua Franca program
        # contains model reactors.
        self.hasModalReactors = False
    
        #  //////////////////////////////////////////
        #  // Target properties, if they are included.
        # A list of federate instances or a list with a single empty string
        # if there are no federates specified.
        # FIXME: Why put a single empty string there? It should be just empty...
        self.federates = set()
    
        # A map from federate IDs to federate instances.
        self.federateByID = {}
    
        # A map from instantiations to the federate instances for that instantiation.
        # If the instantiation has a width, there may be more than one federate instance.
        self.federatesByInstantiation = None
    
        # The federation RTI properties, which defaults to 'localhost: 15045'.
        self.federationRTIProperties = [{"host": "localhost"}, {"port", 0}]
    
        # Contents of $LF_CLASSPATH, if it was set.
        self.classpathLF = None

    def getTargetConfig(self):
        """ generated source for method getTargetConfig """
        return self.targetConfig

    def getCommandFactory(self):
        """ generated source for method getCommandFactory """
        return self.commandFactory

    def getMainDef(self):
        """ generated source for method getMainDef """
        return self.mainDef

    def addDelayClass(self, generatedDelay):
        """
        Code generation functions to override for a concrete code generator.
        Store the given reactor in the collection of generated delay classes
        and insert it in the AST under the top-level reactor's node.
        :param generatedDelay: 
        :return: 
        """
        #  Record this class, so it can be reused.
        self.delayClasses.append(generatedDelay)
        #  And hook it into the AST.
        for node in self.fileConfig.resource.getAllContents():
            if type(node) == type(Model):  #.__class__.isInstance
                node.getReactors().append(generatedDelay)
                break

    def findDelayClass(self, className):
        """
        Return the generated delay reactor that corresponds to the given class
        name if it had been created already, `null` otherwise.
        :param className:
        :return:
        """
        c = None
        for it in self.delayClasses:
            if it.getName().equals(className):
                c = it
                break
        return c

    def createMainInstantiation(self):
        """
        If there is a main or federated reactor, then create a synthetic Instantiation
        for that top-level reactor and set the field mainDef to refer to it.
        :return:
        """
        """ generated source for method createMainInstantiation """
        nodes = IteratorExtensions.toIterable(self.fileConfig.resource.getAllContents())
        for reactor in nodes:
            if type(reactor) == type(Reactor):
                if reactor.isMain() or reactor.isFederated():
                    self.mainDef = LfFactory.eINSTANCE.createInstantiation()
                    self.mainDef.setName(reactor.__name__)
                    self.mainDef.setReactorClass(reactor)

    def doGenerate(self, resource, context):
        """
        Generate code from the Lingua Franca model contained by the specified resource.
        This is the main entry point for code generation. This base class finds all
        reactor class definitions, including any reactors defined in imported .lf files
        (except any main reactors in those imported files), and adds them to the
        {@link GeneratorBase#reactors reactors} list. If errors occur during
        generation, then a subsequent call to errorsOccurred() will return true.
        In standalone mode, this object is also used to relay CLI arguments.

        :param resource: The resource containing the source code.
        :param context: Context relating to invocation of the code generator.
        :return:
        """
        GeneratorUtils.setTargetConfig(context, GeneratorUtils.findTarget(self.fileConfig.resource),
                                       self.targetConfig, self.errorReporter)
        self.cleanIfNeeded(context)
        print(context.getMode())
        if isinstance(self.errorReporter, (EclipseErrorReporter)):
            (self.errorReporter).clearMarkers()
        ASTUtils.setMainName(self.fileConfig.resource, self.fileConfig.name)
        self.createMainInstantiation()
        if context.getMode() == LFGeneratorContext.Mode.STANDALONE and self.mainDef is not None:
            for conflict in MainConflictChecker(self.fileConfig).conflicts:
                self.errorReporter.reportError(self.mainDef.getReactorClass(), 
                                               "Conflicting main reactor in " + conflict)
        self.commandFactory.setVerbose()
        if context.getMode() == LFGeneratorContext.Mode.STANDALONE and context.getArgs().containsKey("quiet"):
            self.commandFactory.setQuiet()
        # This must be done before desugaring delays below.
        self.analyzeFederates(context)
        # Process target files. Copy each of them into the src-gen dir.
        # FIXME: Should we do this here? This doesn't make sense for federates the way it is
        #           done here.
        self.copyUserFiles(self.targetConfig, self.fileConfig)
        # Collect reactors and create an instantiation graph.
        # These are needed to figure out which resources we need
        # to validate, which happens in setResources().
        self.setReactorsAndInstantiationGraph(context.getMode())
        GeneratorUtils.validate(context, self.fileConfig, self.instantiationGraph, self.errorReporter)
        allResources = GeneratorUtils.getResources(self.reactors)
        # FIXME: This filter reproduces the behavior of the method it replaces.
        #  But why must it be so complicated? Why are we worried about weird corner cases like this?
        res = []
        for it in allResources:
            if not (type(it) == self.fileConfig.resource) or \
                    ((self.mainDef is not None) and (it == self.mainDef.getReactorClass().eResource())):
                res.extend(list(GeneratorUtils.getLFResource(it, self.fileConfig.getSrcGenBasePath(),
                                                        context, self.errorReporter)))
        self.resources.append(res)
        GeneratorUtils.accommodatePhysicalActionsIfPresent(allResources, self.getTarget().setsKeepAliveOptionAutomatically(),
                                                           self.targetConfig, self.errorReporter)
        # FIXME: Should the GeneratorBase pull in `files` from imported
        #     resources?
        #
        # Reroute connections that have delays associated with them via
        # generated delay reactors.
        self.transformDelays()

        # Transform connections that reside in mutually exclusive modes and are otherwise conflicting
        # This should be done before creating the instantiation graph
        self.transformConflictingConnectionsInModalReactors()

        # Invoke these functions a second time because transformations
        # may have introduced new reactors!
        self.setReactorsAndInstantiationGraph(context.getMode())
        # Check for existence and support of modes
        r = False
        for it in self.reactors:
            if not it.getModes().isEmpty():
                r = True
                break
        self.hasModalReactors = r
        self.checkModalReactorSupport(False)
        self.additionalPostProcessingForModes()
        self.enableSupportForSerializationIfApplicable(context.getCancelIndicator())

    def cleanIfNeeded(self, context):
        """
        Check if a clean was requested from the standalone compiler and perform
        the clean step.
        :param context:
        :return:
        """
        """ generated source for method cleanIfNeeded """
        if context.getArgs().containsKey("clean"):
            try:
                self.fileConfig.doClean()
            except IOError as e:
                print(sys.stderr, "WARNING: IO Error during clean")

    def setReactorsAndInstantiationGraph(self, mode):
        """
        Create a new instantiation graph. This is a graph where each node is a Reactor (not a ReactorInstance)
        and an arc from Reactor A to Reactor B means that B contains an instance of A, constructed with a statement
        like `a = new A();`  After creating the graph,
        sort the reactors in topological order and assign them to the reactors class variable.
        Hence, after this method returns, `this.reactors` will be a list of Reactors such that any
        reactor is preceded in the list by reactors that it instantiates.

        :param mode:
        :return:
        """
        # Build the instantiation graph
        self.instantiationGraph = InstantiationGraph(self.fileConfig.resource, False)
        # Topologically sort the reactors such that all of a reactor's instantiation dependencies occur earlier in
        # the sorted list of reactors. This helps the code generator output code in the correct order.
        # For example if `reactor Foo {bar = new Bar()}` then the definition of `Bar` has to be generated before
        # the definition of `Foo`.
        self.reactors = self.instantiationGraph.nodesInTopologicalOrder()
        # If there is no main reactor or if all reactors in the file need to be validated, then make sure the reactors
        # list includes even reactors that are not instantiated anywhere.
        if self.mainDef == None or mode == LFGeneratorContext.Mode.LSP_MEDIUM:
            nodes = IteratorExtensions.toIterable(self.fileConfig.resource.getAllContents())
            for r in nodes:
                if type(r) == type(Reactor):
                    if not self.reactors.contains(r):
                        self.reactors.append(r)

    def transformDelays(self):
        """
        For each involved resource, replace connections with delays with generated delay reactors.
        :return:
        """
        for r in self.resources:
            ASTUtils.insertGeneratedDelays(r.eResource, self)

    def copyUserFiles(self, targetConfig, fileConfig):
        """
        Copy user specific files to the src-gen folder.
        This should be overridden by the target generators.

        :param targetConfig: The targetConfig to read the `files` from.
        :param fileConfig: The fileConfig used to make the copy and resolve paths.
        :return:
        """
        pass

    def errorsOccurred(self):
        """
        * Return true if errors occurred in the last call to doGenerate().
        * This will return true if any of the reportError methods was called.
        :return: True if errors occurred.
        """
        return self.errorReporter.getErrorsOccurred()

    def getTargetTypes(self):
        """
        Return the TargetTypes instance associated with this
        :return:
        """
        pass

    def generateDelayBody(self, action, port):
        """
        Generate code for the body of a reaction that takes an input and
        schedules an action with the value of that input.
        :param action: the action to schedule
        :param port: the port to read from
        :return:
        """
        pass

    def generateForwardBody(self, action, port):
        """
        Generate code for the body of a reaction that is triggered by the
        given action and writes its value to the given port.
        :param action:the action that triggers the reaction
        :param port:the port to write to
        :return:
        """
        pass

    def generateDelayGeneric(self):
        """
        Generate code for the generic type to be used in the class definition
        of a generated delay reactor.
        :return:
        """
        pass

    def isUnordered(self, reaction):
        """
        Return true if the reaction is unordered. An unordered reaction is one
        that does not have any dependency on other reactions in the containing
        reactor, and where no other reaction in the containing reactor depends
        on it. There is currently no way in the syntax of LF to make a reaction
        unordered, deliberately, because it can introduce unexpected
        nondeterminacy. However, certain automatically generated reactions are
        known to be safe to be unordered because they do not interact with the
        state of the containing reactor. To make a reaction unordered, when
        the Reaction instance is created, add that instance to this set.
        :param reaction:
        :return: True if the reaction has been marked unordered.
        """
        return (self.unorderedReactions is not None) and self.unorderedReactions.contains(reaction)

    def makeUnordered(self, reaction):
        """
        Mark the reaction unordered. An unordered reaction is one that does not
        have any dependency on other reactions in the containing reactor, and
        where no other reaction in the containing reactor depends on it. There
        is currently no way in the syntax of LF to make a reaction unordered,
        deliberately, because it can introduce unexpected nondeterminacy.
        However, certain automatically generated reactions are known to be safe
        to be unordered because they do not interact with the state of the
        containing reactor. To make a reaction unordered, when the Reaction
        instance is created, add that instance to this set.
        :param reaction: The reaction to make unordered.
        :return:
        """

        if self.unorderedReactions == None:
            self.unorderedReactions = set()
        self.unorderedReactions.append(reaction)

    def setReactionBankIndex(self, reaction, bankIndex):
        """
        Mark the specified reaction to belong to only the specified
        bank index. This is needed because reactions cannot declare
        a specific bank index as an effect or trigger. Reactions that
        send messages between federates, including absent messages,
        need to be specific to a bank member.

        :param reaction: The reaction.
        :param bankIndex: The bank index, or -1 if there is no bank.
        :return:
        """
        if bankIndex < 0:
            return
        if self.reactionBankIndices == None:
            self.reactionBankIndices = {}
        self.reactionBankIndices[reaction] = bankIndex

    def getReactionBankIndex(self, reaction):
        """
        Return the reaction bank index.
        @see setReactionBankIndex(reaction, bankIndex)
        :param reaction: The reaction.
        :return: The reaction bank index, if one has been set, and -1 otherwise.
        """
        if self.reactionBankIndices is None:
            return -1
        if self.reactionBankIndices.get(reaction) is None:
            return -1
        return self.reactionBankIndices.get(reaction)

    @classmethod
    def timeInTargetLanguage(cls, time):
        """
        Given a representation of time that may possibly include units, return
        a string that the target language can recognize as a value. In this base
        class, if units are given, e.g. "msec", then we convert the units to upper
        case and return an expression of the form "MSEC(value)". Particular target
        generators will need to either define functions or macros for each possible
        time unit or override this method to return something acceptable to the
        target language.

        :param time: A TimeValue that represents a time.
        :return: A string, such as "MSEC(100)" for 100 milliseconds.
        """
        """ generated source for method timeInTargetLanguage """
        if time is not None:
            if time.unit is not None:
                return f"{time.unit}({time.getMagnitude()})"
            else:
                return f"{time.getMagnitude()}"
        return "0"

    @classmethod
    def cMacroName(cls, unit):
        """
        note that this is moved out by #544
        :param unit:
        :return:
        """
        return unit.getCanonicalName().toUpperCase()

    def checkModalReactorSupport(self, isSupported):
        """
        Checks whether modal reactors are present and require appropriate code generation.
        This will set the hasModalReactors variable.
        :param isSupported: indicates if modes are supported by this code generation.
        :return:
        """
        if self.hasModalReactors and not isSupported:
            self.errorReporter.reportError("The currently selected code generation or " + "target configuration does not support modal reactors!")

    def transformConflictingConnectionsInModalReactors(self):
        """
        Finds and transforms connections into forwarding reactions iff the connections have the same destination as other
        connections or reaction in mutually exclusive modes.
        :return:
        """
        for r in self.resources:
            transform = ASTUtils.findConflictingConnectionsInModalReactors(r.eResource)
            if not transform.isEmpty():
                factory = LfFactory.eINSTANCE
                for connection in transform:
                    if connection.isPhysical() or connection.getDelay() != None or connection.isIterated() or connection.getLeftPorts().size() > 1 or connection.getRightPorts().size() > 1:
                        self.errorReporter.reportError(connection, "Cannot transform connection in modal reactor. Connection uses currently not supported features.")
                    else:
                        reaction = factory.createReaction()
                        (connection.eContainer()).getReactions().append(reaction)
                        sourceRef = connection.getLeftPorts().get(0)
                        destRef = connection.getRightPorts().get(0)
                        reaction.getTriggers().append(sourceRef)
                        reaction.getEffects().append(destRef)
                        code_ = factory.createCode()
                        source = (sourceRef.getContainer().__name__ + "." if sourceRef.getContainer() != None else "") + sourceRef.getVariable().__name__
                        dest = (destRef.getContainer().__name__ + "." if destRef.getContainer() != None else "") + destRef.getVariable().__name__
                        code_.setBody(self.getConflictingConnectionsInModalReactorsBody(source, dest))
                        reaction.setCode(code_)
                        EcoreUtil.remove(connection)

    def getConflictingConnectionsInModalReactorsBody(self, source, dest):
        """
        Return target code for forwarding reactions iff the connections have the
        same destination as other connections or reaction in mutually exclusive modes.

        This method needs to be overridden in target specific code generators that
        support modal reactors.
        :param source:
        :param dest:
        :return:
        """
        self.errorReporter.reportError("The currently selected code generation " +
                                       "is missing an implementation for conflicting " +
                                       "transforming connections in modal reactors.")
        return "MODAL MODELS NOT SUPPORTED"

    def additionalPostProcessingForModes(self):
        """
        Hook for additional post-processing of the model.
        :return:
        """
        pass

    def generateNetworkReceiverBody(self, action, sendingPort, receivingPort, receivingPortID,
                                    sendingFed, receivingFed, receivingBankIndex, receivingChannelIndex, type,
                                    isPhysical, serializer):
        """
        Generate code for the body of a reaction that handles the
        action that is triggered by receiving a message from a remote
        federate.

        :param action: The action.
        :param sendingPort: The output port providing the data to send.
        :param receivingPort: The ID of the destination port.
        :param receivingPortID: The ID of the destination port.
        :param sendingFed: The sending federate.
        :param receivingFed: The destination federate.
        :param receivingBankIndex: The receiving federate's bank index, if it is in a bank.
        :param receivingChannelIndex: The receiving federate's channel index, if it is a multiport.
        :param type: The type.
        :param isPhysical: Indicates whether or not the connection is physical
        :param serializer: The serializer used on the connection.
        :return:
        """
        raise TypeError("This target does not support network connections between federates.")

    def generateNetworkSenderBody(self, sendingPort, receivingPort, receivingPortID, sendingFed,
                                  sendingBankIndex, sendingChannelIndex, receivingFed, type, isPhysical,
                                  delay, serializer):
        """
        Generate code for the body of a reaction that handles an output
        that is to be sent over the network. This base class throws an exception.
        :param sendingPort:The output port providing the data to send.
        :param receivingPort:The ID of the destination port.
        :param receivingPortID: The ID of the destination port.
        :param sendingFed: The sending federate.
        :param sendingBankIndex: The bank index of the sending federate, if it is a bank.
        :param sendingChannelIndex: The channel index of the sending port, if it is a multiport.
        :param receivingFed: The destination federate.
        :param type: The type.
        :param isPhysical: Indicates whether the connection is physical or not
        :param delay: The delay value imposed on the connection using after
        :param serializer: The serializer used on the connection
        :throws: UnsupportedOperationException If the target does not support this operation.
        :return:
        """
        raise TypeError("This target does not support network connections between federates.")

    def generateNetworkInputControlReactionBody(self, receivingPortID, maxSTP):
        """
        Generate code for the body of a reaction that waits long enough so that the status
        of the trigger for the given port becomes known for the current logical time.
        :param receivingPortID: port The port to generate the control reaction for
        :param maxSTP: The maximum value of STP is assigned to reactions (if any)
                       that have port as their trigger or source
        :return:
        """
        raise TypeError("This target does not support network connections between federates.")

    def generateNetworkOutputControlReactionBody(self, port, portID, receivingFederateID, sendingBankIndex, sendingChannelIndex, delay):
        """
        Generate code for the body of a reaction that sends a port status message for the given
        port if it is absent.
        :param port: The port to generate the control reaction for
        :param portID: The ID assigned to the port in the AST transformation
        :param receivingFederateID: The ID of the receiving federate
        :param sendingBankIndex: The bank index of the sending federate, if it is a bank.
        :param sendingChannelIndex: The channel if a multiport
        :param delay: The delay value imposed on the connection using after
        :return:
        """
        raise TypeError("This target does not support network connections between federates.")

    def enableSupportForSerializationIfApplicable(self, cancelIndicator):
        """
        * Add necessary code to the source and necessary build support to
        * enable the requested serializations in 'enabledSerializations'
        :param cancelIndicator:
        :return:
        """
        if not (self.enabledSerializers is None):
            raise TypeError("Serialization is target-specific " + " and is not implemented for the " +
                            self.getTarget().__str__() + " target.")

    def isFederatedAndDecentralized(self):
        """
        * Returns true if the program is federated and uses the decentralized
        * coordination mechanism.
        :return:
        """
        return self.isFederated and self.targetConfig.coordination == CoordinationType.DECENTRALIZED

    def isFederatedAndCentralized(self):
        """
        * Returns true if the program is federated and uses the centralized
        * coordination mechanism.
        :return:
        """
        return self.isFederated and self.targetConfig.coordination == CoordinationType.CENTRALIZED

    class ErrorFileAndLine(object):
        """
        * Parsed error message from a compiler is returned here.
        """
        filepath = None
        line = "1"
        character = "0"
        message = ""
        isError = True

        def __str__(self):
            """ generated source for method toString """
            return ("Error" if self.isError else "Non-error") + " at " + self.line + ":" \
                   + self.character + " of file " + self.filepath + ": " + self.message

    def parseCommandOutput(self, line):
        """
        Given a line of text from the output of a compiler, return
        an instance of ErrorFileAndLine if the line is recognized as
        the first line of an error message. Otherwise, return null.
        This base class simply returns null.
        :param line: A line of output from a compiler or other external
                     tool that might generate errors.
        :return: If the line is recognized as the start of an error message,
                 then return a class containing the path to the file on which the
                 error occurred (or null if there is none), the line number (or the
                 string "1" if there is none), the character position (or the string
                 "0" if there is none), and the message (or an empty string if there
                 is none).
        """
        return None

    def reportCommandErrors(self, stderr):
        """
        * Parse the specified string for command errors that can be reported
        * using marks in the Eclipse IDE. In this class, we attempt to parse
        * the messages to look for file and line information, thereby generating
        * marks on the appropriate lines. This should not be called in standalone
        * mode.

        :param stderr: The output on standard error of executing a command.
        :return:
        """
        lines = stderr.split("\\r?\\n")
        message = ""
        lineNumber = None
        path = self.fileConfig.srcFile
        originalPath = path
        severity = IMarker.SEVERITY_ERROR
        for line in lines:
            parsed = self.parseCommandOutput(line)
            if parsed != None:
                if 0 > len(message):
                    if severity == IMarker.SEVERITY_ERROR:
                        self.errorReporter.reportError(path, lineNumber, message.__str__())
                    else:
                        self.errorReporter.reportWarning(path, lineNumber, message.__str__())
                    if not (originalPath.toFile() == path.toFile()):
                        if severity == IMarker.SEVERITY_ERROR:
                            self.errorReporter.reportError(originalPath, 1, "Error in imported file: " + path)
                        else:
                            self.errorReporter.reportWarning(originalPath, 1, "Warning in imported file: " + path)
                if parsed.isError:
                    severity = IMarker.SEVERITY_ERROR
                else:
                    severity = IMarker.SEVERITY_WARNING
                message = ""
                message.append(parsed.message)
                try:
                    lineNumber = int(parsed.line)
                except Exception as ex:
                    lineNumber = None

                path = os.path.abspath(parsed.filepath)
            else:
                if 0 > len(message):
                    message.append("\n")
                else:
                    if not line.lower().contains("error:"):
                        severity = IMarker.SEVERITY_WARNING
                message.append(line)
        if 0 > len(message):
            if severity == IMarker.SEVERITY_ERROR:
                self.errorReporter.reportError(path, lineNumber, message.__str__())
            else:
                self.errorReporter.reportWarning(path, lineNumber, message.__str__())
            if originalPath.toFile() != path.toFile():
                if severity == IMarker.SEVERITY_ERROR:
                    self.errorReporter.reportError(originalPath, 1, "Error in imported file: " + path)
                else:
                    self.errorReporter.reportWarning(originalPath, 1, "Warning in imported file: " + path)

    def getTargetReference(self, param):
        """
        Generate target code for a parameter reference.
        :param param:  The parameter to generate code for
        :return:  Parameter reference in target code
        """
        return param.__name__

    def removeRemoteFederateConnectionPorts(self, instance):
        """
        Remove triggers in each federates' network reactions that are defined
        in remote federates.

        This must be done in code generators after the dependency graphs
        are built and levels are assigned. Otherwise, these disconnected ports
        might reference data structures in remote federates and cause
        compile/runtime errors.

        :param instance:  The reactor instance to remove these ports from if any. Can be null.
        :return:
        """
        if not self.isFederated:
            return
        for federate in self.federates:
            federate.removeRemoteFederateConnectionPorts()
            if instance == None:
                continue 
            for reaction in federate.networkReactions:
                networkReaction = instance.lookupReactionInstance(reaction)
                if networkReaction == None:
                    continue 
                for port in federate.remoteNetworkReactionTriggers:
                    disconnectedPortInstance = instance.lookupPortInstance(port)
                    if disconnectedPortInstance != None:
                        networkReaction.removePortInstance(disconnectedPortInstance)

    def setFederationRTIProperties(self, context):
        """
        Set the RTI hostname, port and username if given as compiler arguments

        :param context:
        :return:
        """
        """ generated source for method setFederationRTIProperties """
        rtiAddr = context.getArgs().getProperty("rti")
        pattern = re.compile("([a-zA-Z0-9]+@)?([a-zA-Z0-9]+\\.?[a-z]{2,}|[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+):?([0-9]+)?")
        matcher = pattern.matcher(rtiAddr)
        if not matcher.find():
            return
        userWithAt = matcher.group(1)
        user = None if userWithAt == None else userWithAt.substring(0, 1 - len(userWithAt))
        host = matcher.group(2)
        port = matcher.group(3)
        if host != None:
            self.federationRTIProperties.append({"host", host})
        if port != None:
            self.federationRTIProperties.append({"port", port})
        if user != None:
            self.federationRTIProperties.append({"user", user})

    def analyzeFederates(self, context):
        """
        Analyze the AST to determine whether code is being mapped to
        single or to multiple target machines. If it is being mapped
        to multiple machines, then set the {@link #isFederated} field to true,
        create a FederateInstance for each federate, and record various
        properties of the federation

        In addition, for each top-level connection, add top-level reactions to the AST
        that send and receive messages over the network.

        This class is target independent, so the target code
        generator still has quite a bit of work to do.
        It needs to provide the body of the sending and
        receiving reactions. It also needs to provide the
        runtime infrastructure that uses the dependency
        information between federates. See the C target
        for a reference implementation.
        :param context:
        :return:
        """
        mainReactor = ASTUtils.toDefinition(self.mainDef.getReactorClass()) if self.mainDef != None else None
        if self.mainDef == None or not mainReactor.isFederated():
            federateInstance = FederateInstance(None, 0, 0, self, self.errorReporter)
            self.federates.append(federateInstance)
            self.federateByID.put(0, federateInstance)
        else:
            self.isFederated = True
            if context.getArgs().containsKey("rti"):
                self.setFederationRTIProperties(context)
            elif mainReactor.getHost() != None:
                if mainReactor.getHost().getAddr() != None:
                    self.federationRTIProperties.append({"host", mainReactor.getHost().getAddr()})
                if mainReactor.getHost().getPort() != 0:
                    self.federationRTIProperties.append({"port", mainReactor.getHost().getPort()})
                if mainReactor.getHost().getUser() != None:
                    self.federationRTIProperties.append({"user", mainReactor.getHost().getUser()})
            mainReactorContext = []
            mainReactorContext.append(self.mainDef)
            for instantiation in ASTUtils.allInstantiations(mainReactor):
                bankWidth = ASTUtils.width(instantiation.getWidthSpec(), mainReactorContext)
                if bankWidth < 0:
                    self.errorReporter.reportError(instantiation, "Cannot determine bank width! Assuming width of 1.")
                    bankWidth = 1
                federateInstances = [None] * bankWidth
                i = 0
                while i < bankWidth:
                    federateID = len(self.federates)
                    federateInstance = FederateInstance(instantiation, federateID, i, self, self.errorReporter)
                    federateInstance.bankIndex = i
                    self.federates.append(federateInstance)
                    federateInstances.append(federateInstance)
                    self.federateByID.put(federateID, federateInstance)
                    if instantiation.getHost() != None:
                        federateInstance.host = instantiation.getHost().getAddr()
                        federateInstance.port = instantiation.getHost().getPort()
                        federateInstance.user = instantiation.getHost().getUser()
                        if federateInstance.host != None and not federateInstance.host == "localhost" and not federateInstance.host == "0.0.0.0":
                            federateInstance.isRemote = True
                    i += 1
                if self.federatesByInstantiation == None:
                    self.federatesByInstantiation = {}
                self.federatesByInstantiation.put(instantiation, federateInstances)
            self.targetConfig.keepalive = True
            self.replaceFederateConnectionsWithActions()
            mainReactor.getConnections().clear()

    def replaceFederateConnectionsWithActions(self):
        """
        Replace connections between federates in the AST with actions that
        handle sending and receiving data.
        :return:
        """
        mainReactor = ASTUtils.toDefinition(self.mainDef.getReactorClass()) if self.mainDef is not None else None
        # Each connection in the AST may represent more than one connection between
        # federate instances because of banks and multiports. We need to generate communication
        # for each of these. To do this, we create a ReactorInstance so that we don't have
        # to duplicate the rather complicated logic in that class. We specify a depth of 1,
        # so it only creates the reactors immediately within the top level, not reactors
        # that those contain.
        mainInstance = ReactorInstance(mainReactor, self.errorReporter, 1)
        for child in mainInstance.children:
            for output in child.outputs:
                self.replaceConnectionFromFederate(output, child, mainInstance)

    def replaceConnectionFromFederate(self, output, federateReactor, mainInstance):
        """
        Replace the connections from the specified output port for the specified federate reactor.
        :param output: The output port instance.
        :param federateReactor: The reactor instance for that federate.
        :param mainInstance: The main reactor instance.
        :return:
        """
        for srcRange in output.dependentPorts:
            for dstRange in srcRange.destinations:
                srcID = srcRange.startMR()
                dstID = dstRange.startMR()
                dstCount = 0
                srcCount = 0
                __dstCount_0 = dstCount
                dstCount += 1
                while __dstCount_0 < dstRange.width:
                    srcChannel = srcID.getDigits().get(0)
                    srcBank = srcID.get(1)
                    dstChannel = dstID.getDigits().get(0)
                    dstBank = dstID.get(1)
                    srcFederate = self.federatesByInstantiation.get(srcRange.instance.parent.definition).get(srcBank)
                    dstFederate = self.federatesByInstantiation.get(dstRange.instance.parent.definition).get(dstBank)
                    connection = srcRange.connection
                    if connection == None:
                        self.errorReporter.reportError(output.definition, "Unexpected error. Cannot find output connection for port")
                    else:
                        if not connection.isPhysical() and self.targetConfig.coordination != CoordinationType.DECENTRALIZED:
                            # Map the delays on connections between federates.
                            dependsOnDelays = dstFederate.dependsOn.computeIfAbsent(
                                srcFederate, {})
                            #  Put the delay on the cache.
                            if connection.getDelay() is not None:
                                dependsOnDelays.append(connection.getDelay())
                            else:
                                # To indicate that at least one connection has no delay, add a null entry.
                                dependsOnDelays.append(None)
                            # Map the connections between federates.
                            sendsToDelays = srcFederate.sendsTo.computeIfAbsent(dstFederate, {})
                            if connection.getDelay() is not None:
                                sendsToDelays.append(connection.getDelay())
                            else:
                                # To indicate that at least one connection has no delay, add a null entry.
                                sendsToDelays.append(None)
                        FedASTUtils.makeCommunication(srcRange.instance,
                                                      dstRange.instance,
                                                      connection,
                                                      srcFederate,
                                                      srcBank,
                                                      srcChannel,
                                                      dstFederate,
                                                      dstBank,
                                                      dstChannel,
                                                      self,
                                                      self.targetConfig.coordination)
                    dstID.increment()
                    srcID.increment()
                    srcCount += 1
                    if srcCount == srcRange.width:
                        srcID = srcRange.startMR()

    def printInfo(self, mode):
        """
        Print to stdout information about what source file is being generated,
        what mode the generator is in, and where the generated sources are to be put.
        :param mode:
        :return:
        """
        print("Generating code for: " + self.fileConfig.resource.getURI().__str__())
        print("******** mode: " + mode)
        print("******** generated sources: " + self.fileConfig.getSrcGenPath())

    def generateAfterDelaysWithVariableWidth(self):
        """
        Indicates whether delay banks generated from after delays should have a variable length width.

        If this is true, any delay reactors that are inserted for after delays on multiport connections
        will have an unspecified variable length width. The code generator is then responsible for inferring the
        correct width of the delay bank, which is only possible if the precise connection width is known at compile time.

        If this is false, the width specification of the generated bank will list all the ports listed on the right
        side of the connection. This gives the code generator the information needed to infer the correct width at
        runtime.
        :return:
        """
        return True

    def getNetworkBufferType(self):
        """
        Get the buffer type used for network messages
        :return:
        """
        return ""

    def getTarget(self):
        """
        Return the Targets enum for the current target
        :return:
        """

    @classmethod
    @overloaded
    def getTargetTime(cls, t):
        """
        Get textual representation of a time in the target language.
        :param t: A time AST node
        :return:  A time string in the target language
        """
        #  FIXME: this should be placed in ExpressionGenerator
        value = TimeValue(t.getInterval(), TimeUnit.fromName(t.getUnit()))
        return cls.timeInTargetLanguage(value)

    @classmethod
    def getTargetValue(cls, expr):
        """
        Get textual representation of a value in the target language.
        If the value evaluates to 0, it is interpreted as a normal value.
        :param expr: An AST node
        :return: A string in the target language
        """
        """ generated source for method getTargetValue """
        if expr.isinstance(Time):
            return cls.getTargetTime(expr)
        return ASTUtils.toText(expr)

    @classmethod
    @getTargetTime.register(object, Expression)
    def getTargetTime_0(cls, expr):
        """
        Get textual representation of a value in the target language.
        If the value evaluates to 0, it is interpreted as a time.

        :param expr: A time AST node
        :return: A time string in the target language
        """
        # FIXME: this should be placed in ExpressionGenerator
        if expr.isinstance(Time):
            return cls.getTargetTime(expr)
        elif ASTUtils.isZero(expr):
            value = TimeValue.ZERO
            return cls.timeInTargetLanguage(value)
        return ASTUtils.toText(expr)

