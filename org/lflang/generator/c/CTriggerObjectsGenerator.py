#!/usr/bin/env python
""" generated source for module CTriggerObjectsGenerator """
# package: org.lflang.generator.c
# import java.util.Arrays
# import java.util.HashSet
# import java.util.LinkedHashMap
# import java.util.Map
# import java.util.stream.Collectors
from include.overloading import overloaded
from lflang.generator.c import CUtil
from org.lflang import ASTUtils

from org.lflang import AttributeUtils

from org.lflang import TargetConfig

from org.lflang.TargetProperty import CoordinationType

from org.lflang.TargetProperty import LogLevel

from org.lflang.federated import CGeneratorExtension

from org.lflang.federated import FederateInstance

from org.lflang.generator import CodeBuilder

from org.lflang.generator import GeneratorBase

from org.lflang.generator import ParameterInstance

from org.lflang.generator import PortInstance

from org.lflang.generator import ReactionInstance

from org.lflang.generator import ReactorInstance

from org.lflang.generator import RuntimeRange

from org.lflang.generator import SendRange
# import com.google.common.collect.Iterables

# 
#  * Generate code for the "_lf_initialize_trigger_objects" function
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#  
class CTriggerObjectsGenerator:
    """ generated source for class CTriggerObjectsGenerator """
    #      * Generate the _lf_initialize_trigger_objects function for 'federate'.
    #      
    @classmethod
    def generateInitializeTriggerObjects(cls, federate, main, targetConfig, initializeTriggerObjects, startTimeStep, types, lfModuleName, federationRTIProperties, startTimeStepTokens, startTimeStepIsPresentCount, isFederated, isFederatedAndDecentralized, clockSyncIsOn):
        """ generated source for method generateInitializeTriggerObjects """
        code_ = CodeBuilder()
        code_.pr("void _lf_initialize_trigger_objects() {")
        code_.indent()
        #  Initialize the LF clock.
        code_.pr("\n".join([ "// Initialize the _lf_clock", "lf_initialize_clock();")])
        #  Initialize tracing if it is enabled
        if targetConfig.tracing != None:
            traceFileName = lfModuleName
            if targetConfig.tracing.traceFileName != None:
                traceFileName = targetConfig.tracing.traceFileName
                #  Since all federates would have the same name, we need to append the federate name.
                if isFederated:
                    traceFileName += "_" + federate.name
            code_.pr("\n".join([ "// Initialize tracing", "start_trace(" + addDoubleQuotes(traceFileName + ".lft") + ");")])
            #  .lft is for Lingua Franca trace
        #  Create the table used to decrement reference counts between time steps.
        if startTimeStepTokens > 0:
            #  Allocate the initial (before mutations) array of pointers to tokens.
            code_.pr("\n".join([ "_lf_tokens_with_ref_count_size = " + startTimeStepTokens + ";", "_lf_tokens_with_ref_count = (token_present_t*)calloc(" + startTimeStepTokens + ", sizeof(token_present_t));", "if (_lf_tokens_with_ref_count == NULL) lf_print_error_and_exit(" + addDoubleQuotes("Out of memory!") + ");")])
        #  Create the table to initialize is_present fields to false between time steps.
        if startTimeStepIsPresentCount > 0:
            #  Allocate the initial (before mutations) array of pointers to _is_present fields.
            code_.pr("\n".join([ "// Create the array that will contain pointers to is_present fields to reset on each step.", "_lf_is_present_fields_size = " + startTimeStepIsPresentCount + ";", "_lf_is_present_fields = (bool**)calloc(" + startTimeStepIsPresentCount + ", sizeof(bool*));", "if (_lf_is_present_fields == NULL) lf_print_error_and_exit(" + addDoubleQuotes("Out of memory!") + ");", "_lf_is_present_fields_abbreviated = (bool**)calloc(" + startTimeStepIsPresentCount + ", sizeof(bool*));", "if (_lf_is_present_fields_abbreviated == NULL) lf_print_error_and_exit(" + addDoubleQuotes("Out of memory!") + ");", "_lf_is_present_fields_abbreviated_size = 0;")])
        #  Allocate the memory for triggers used in federated execution
        code_.pr(CGeneratorExtension.allocateTriggersForFederate(federate, startTimeStepIsPresentCount, isFederated, isFederatedAndDecentralized))
        code_.pr(initializeTriggerObjects.__str__())
        #  Assign appropriate pointers to the triggers
        #  FIXME: For python target, almost surely in the wrong place.
        code_.pr(CGeneratorExtension.initializeTriggerForControlReactions(main, main, federate))
        reactionsInFederate = None
        #          Iterables.filter(
        #              main.reactions,
        #              r -> federate.contains(r.getDefinition())
        #          );
        code_.pr(deferredInitialize(federate, main, reactionsInFederate, targetConfig, types, isFederated))
        code_.pr(deferredInitializeNonNested(federate, main, main, reactionsInFederate, isFederated))
        #  Next, for every input port, populate its "self" struct
        #  fields with pointers to the output port that sends it data.
        code_.pr(deferredConnectInputsToOutputs(federate, main, isFederated))
        #  Put the code here to set up the tables that drive resetting is_present and
        #  decrementing reference counts between time steps. This code has to appear
        #  in _lf_initialize_trigger_objects() after the code that makes connections
        #  between inputs and outputs.
        code_.pr(startTimeStep.__str__())
        code_.pr(setReactionPriorities(federate, main, isFederated))
        code_.pr(initializeFederate(federate, main, targetConfig, federationRTIProperties, isFederated, clockSyncIsOn))
        code_.pr(generateSchedulerInitializer(main, targetConfig))
        code_.unindent()
        code_.pr("}\n")
        return str(code_)

    #     * Generate code to initialize the scheduler for the threaded C runtime.
    #     
    @classmethod
    def generateSchedulerInitializer(cls, main, targetConfig):
        """ generated source for method generateSchedulerInitializer """
        if not targetConfig.threading:
            return ""
        code_ = CodeBuilder()
        numReactionsPerLevel = main.assignLevels().getNumReactionsPerLevel()
        numReactionsPerLevelJoined = Arrays.stream(numReactionsPerLevel).map(String.valueOf).collect(Collectors.joining(", "))
        code_.pr("\n".join([ "// Initialize the scheduler", "] = " + len(numReactionsPerLevel), "    {" + numReactionsPerLevelJoined + "};", "sched_params_t sched_params = (sched_params_t) {", "                        .num_reactions_per_level = &num_reactions_per_level[0],", "};" + len(numReactionsPerLevel), "lf_sched_init(", "    (size_t)_lf_number_of_workers,", "    &sched_params", ");")])
        return str(code_)

    @classmethod
    def initializeFederate(cls, federate, main, targetConfig, federationRTIProperties, isFederated, clockSyncIsOn):
        """ generated source for method initializeFederate """
        code_ = CodeBuilder()
        if not isFederated:
            return ""
        code_.pr("// ***** Start initializing the federated execution. */")
        code_.pr("\n".join([ "// Initialize the socket mutex", "lf_mutex_init(&outbound_socket_mutex);", "lf_cond_init(&port_status_changed);")])
        if isFederated and targetConfig.coordination == CoordinationType.DECENTRALIZED:
            reactorInstance = main.getChildReactorInstance(federate.instantiation)
            for param in reactorInstance.parameters:
                if param.__name__.lower() == "STP_offset".lower() and param.type.isTime:
                    stp = ASTUtils.getLiteralTimeValue(param.getInitialValue().get(0))
                    if stp != None:
                        code_.pr("lf_set_stp_offset(" + GeneratorBase.timeInTargetLanguage(stp) + ");")
        if len(federate.dependsOn) > 0:
            code_.pr("_fed.has_upstream  = true;")
        if len(federate.sendsTo) > 0:
            code_.pr("_fed.has_downstream = true;")
        code_.pr("_lf_my_fed_id = " + federate.id + ";")
        numberOfInboundConnections = len(federate.inboundP2PConnections)
        numberOfOutboundConnections = len(federate.outboundP2PConnections)
        code_.pr("\n".join([ "_fed.number_of_inbound_p2p_connections = " + numberOfInboundConnections + ";", "_fed.number_of_outbound_p2p_connections = " + numberOfOutboundConnections + ";")])
        if numberOfInboundConnections > 0:
            code_.pr("\n".join([ "// Initialize the array of socket for incoming connections to -1.", "for (int i = 0; i < NUMBER_OF_FEDERATES; i++) {", "    _fed.sockets_for_inbound_p2p_connections[i] = -1;", "}")])
        if numberOfOutboundConnections > 0:
            code_.pr("\n".join([ "// Initialize the array of socket for outgoing connections to -1.", "for (int i = 0; i < NUMBER_OF_FEDERATES; i++) {", "    _fed.sockets_for_outbound_p2p_connections[i] = -1;", "}")])
        if targetConfig.clockSyncOptions.testOffset != None:
            code_.pr("lf_set_physical_clock_offset((1 + " + federate.id + ") * " + targetConfig.clockSyncOptions.testOffset.toNanoSeconds() + "LL);")
        code_.pr("\n".join([ "// Connect to the RTI. This sets _fed.socket_TCP_RTI and _lf_rti_socket_UDP.", "connect_to_rti(" + addDoubleQuotes(federationRTIProperties.get("host").__str__()) + ", " + federationRTIProperties.get("port") + ");")])
        if clockSyncIsOn:
            code_.pr("synchronize_initial_physical_clock_with_rti(_fed.socket_TCP_RTI);")
        if numberOfInboundConnections > 0:
            code_.pr("\n".join([ "// Create a socket server to listen to other federates.", "// If a port is specified by the user, that will be used", "// as the only possibility for the server. If not, the port", "// will start from STARTING_PORT. The function will", "// keep incrementing the port until the number of tries reaches PORT_RANGE_LIMIT.", "create_server(" + federate.port + ");", "// Connect to remote federates for each physical connection.", "// This is done in a separate thread because this thread will call", "// connect_to_federate for each outbound physical connection at the same", "// time that the new thread is listening for such connections for inbound", "// physical connections. The thread will live until all connections", "// have been established.", "lf_thread_create(&_fed.inbound_p2p_handling_thread_id, handle_p2p_connections_from_federates, NULL);")])
        for remoteFederate in federate.outboundP2PConnections:
            code_.pr("connect_to_federate(" + remoteFederate.id + ");")
        return str(code_)

    @classmethod
    @overloaded
    def setReactionPriorities(cls, currentFederate, reactor, isFederated):
        """ generated source for method setReactionPriorities """
        code_ = CodeBuilder()
        cls.setReactionPriorities(currentFederate, reactor, code_, isFederated)
        return str(code_)

    @classmethod
    @setReactionPriorities.register(object, FederateInstance, ReactorInstance, CodeBuilder, bool)
    def setReactionPriorities_0(cls, currentFederate, reactor, builder, isFederated):
        """ generated source for method setReactionPriorities_0 """
        foundOne = False
        reactor.assignLevels()
        prolog = CodeBuilder()
        epilog = CodeBuilder()
        for r in reactor.reactions:
            if currentFederate.contains(r.getDefinition()):
                levels = r.getLevels()
                if len(levels) != 1:
                    if 0 == len(prolog):
                        prolog.startScopedBlock()
                        epilog.endScopedBlock()
                    prolog.pr("int " + r.uniqueID() + "_levels[] = { " + joinObjects(r.getLevelsList(), ", ") + " };")
        temp = CodeBuilder()
        temp.pr("// Set reaction priorities for " + reactor)
        temp.startScopedBlock(reactor, currentFederate, isFederated, True)
        for r in reactor.reactions:
            if currentFederate.contains(r.getDefinition()):
                foundOne = True
                levels = r.getLevels()
                if len(levels) == 1:
                    level = -1
                    for l in levels:
                        level = l
                    indexValue = r.deadline.toNanoSeconds() << 16 | level
                    reactionIndex = "0x" + Long.toString(indexValue, 16) + "LL"
                    temp.pr("\n".join([ CUtil.reactionRef(r) + ".chain_id = " + r.chainID + ";", "// index is the OR of level " + level + " and ", "// deadline " + r.deadline.toNanoSeconds() + " shifted left 16 bits.", CUtil.reactionRef(r) + ".index = " + reactionIndex + ";")])
                else:
                    reactionDeadline = "0x" + Long.toString(r.deadline.toNanoSeconds(), 16) + "LL"
                    temp.pr(String.join("\n", CUtil.reactionRef(r) + ".chain_id = " + r.chainID + ";", "// index is the OR of levels[" + CUtil.runtimeIndex(r.getParent()) + "] and ", "// deadline " + r.deadline.toNanoSeconds() + " shifted left 16 bits.", CUtil.reactionRef(r) + ".index = (" + reactionDeadline + " << 16) | " + r.uniqueID() + "_levels[" + CUtil.runtimeIndex(r.getParent()) + "];"))
        for child in reactor.children:
            if currentFederate.contains(child):
                foundOne = cls.setReactionPriorities(currentFederate, child, temp, isFederated) or foundOne
        temp.endScopedBlock()
        if foundOne:
            builder.pr(prolog.__str__())
            builder.pr(temp.__str__())
            builder.pr(epilog.__str__())
        return foundOne

    @classmethod
    def deferredConnectInputsToOutputs(cls, currentFederate, instance, isFederated):
        """ generated source for method deferredConnectInputsToOutputs """
        code_ = CodeBuilder()
        code_.pr("// Connect inputs and outputs for reactor " + instance.getFullName() + ".")
        for input in instance.inputs:
            if not input.getDependsOnReactions().isEmpty():
                code_.pr(connectPortToEventualDestinations(currentFederate, input, isFederated))
        for output in instance.outputs:
            if not output.getDependsOnReactions().isEmpty():
                code_.pr(connectPortToEventualDestinations(currentFederate, output, isFederated))
        for child in instance.children:
            code_.pr(cls.deferredConnectInputsToOutputs(currentFederate, child, isFederated))
        return str(code_)

    @classmethod
    def connectPortToEventualDestinations(cls, currentFederate, src, isFederated):
        """ generated source for method connectPortToEventualDestinations """
        if not currentFederate.contains(src.getParent()):
            return ""
        code_ = CodeBuilder()
        for srcRange in src.eventualDestinations():
            for dstRange in srcRange.destinations:
                dst = dstRange.instance
                destStructType = CGenerator.variableStructType(dst)
                if currentFederate.contains(dst.getParent()):
                    mod = "" if (dst.isMultiport() or (src.isInput() and src.isMultiport())) else "&"
                    code_.pr("// Connect " + srcRange + " to port " + dstRange)
                    code_.startScopedRangeBlock(currentFederate, srcRange, dstRange, isFederated)
                    if src.isInput():
                        code_.pr(CUtil.portRef(dst, dr, db, dc) + " = (" + destStructType + "*)" + mod + CUtil.portRefNested(src, sr, sb, sc) + ";")
                    elif dst.isOutput():
                        code_.pr(CUtil.portRefNested(dst, dr, db, dc) + " = (" + destStructType + "*)&" + CUtil.portRef(src, sr, sb, sc) + ";")
                    else:
                        code_.pr(CUtil.portRef(dst, dr, db, dc) + " = (" + destStructType + "*)&" + CUtil.portRef(src, sr, sb, sc) + ";")
                        if AttributeUtils.isSparse(dst.getDefinition()):
                            code_.pr(CUtil.portRef(dst, dr, db, dc) + "->sparse_record = " + CUtil.portRefName(dst, dr, db, dc) + "__sparse;")
                            code_.pr(CUtil.portRef(dst, dr, db, dc) + "->destination_channel = " + dc + ";")
                    code_.endScopedRangeBlock(srcRange, dstRange, isFederated)
        return str(code_)

    @classmethod
    def deferredOptimizeForSingleDominatingReaction(cls, currentFederate, r, isFederated):
        """ generated source for method deferredOptimizeForSingleDominatingReaction """
        code_ = CodeBuilder()
        for reaction in r.reactions:
            if currentFederate.contains(reaction.getDefinition()) and currentFederate.contains(reaction.getParent()):
                divisor = 1
                if isFederated:
                    parent = reaction.getParent()
                    while parent.getDepth() > 1:
                        divisor *= parent.getWidth()
                        parent = parent.getParent()
                start = 0
                end = 0
                domStart = 0
                same = False
                previousRuntime = None
                first = True
                for runtime in reaction.getRuntimeInstances():
                    if not first:
                        if same:
                            if runtime.dominating != previousRuntime.dominating:
                                code_.pr(printOptimizeForSingleDominatingReaction(currentFederate, previousRuntime, start, end, domStart, same, divisor, isFederated))
                                same = False
                                start = runtime.id
                                domStart = runtime.dominating.id if (runtime.dominating != None) else 0
                        elif runtime.dominating == previousRuntime.dominating:
                            same = True
                        elif runtime.dominating != None and previousRuntime.dominating != None and runtime.dominating.getReaction() == previousRuntime.dominating.getReaction():
                            if runtime.dominating.id != previousRuntime.dominating.id + 1:
                                printOptimizeForSingleDominatingReaction(currentFederate, previousRuntime, start, end, domStart, same, divisor, isFederated)
                                same = False
                                start = runtime.id
                                domStart = runtime.dominating.id
                        else:
                            printOptimizeForSingleDominatingReaction(currentFederate, previousRuntime, start, end, domStart, same, divisor, isFederated)
                            same = False
                            start = runtime.id
                            domStart = runtime.dominating.id if (runtime.dominating != None) else 0
                    first = False
                    previousRuntime = runtime
                    end += 1
                if end > start:
                    printOptimizeForSingleDominatingReaction(currentFederate, previousRuntime, start, end, domStart, same, divisor, isFederated)
        return str(code_)

    @classmethod
    def printOptimizeForSingleDominatingReaction(cls, currentFederate, runtime, start, end, domStart, same, divisor, isFederated):
        """ generated source for method printOptimizeForSingleDominatingReaction """
        code_ = CodeBuilder()
        domDivisor = 1
        if isFederated and runtime.dominating != None:
            domReaction = runtime.dominating.getReaction()
            if not currentFederate.contains(domReaction.getDefinition()) or not currentFederate.contains(domReaction.getParent()):
                return ""
            parent = runtime.dominating.getReaction().getParent()
            while parent.getDepth() > 1:
                domDivisor *= parent.getWidth()
                parent = parent.getParent()
        dominatingRef = "NULL"
        if end > start + 1:
            code_.startScopedBlock()
            reactionRef = CUtil.reactionRef(runtime.getReaction(), "i")
            if runtime.dominating != None:
                if same:
                    dominatingRef = "&(" + CUtil.reactionRef(runtime.dominating.getReaction(), "" + domStart) + ")"
                else:
                    dominatingRef = "&(" + CUtil.reactionRef(runtime.dominating.getReaction(), "j++") + ")"
            code_.pr(String.join("\n", "// " + runtime.getReaction().getFullName() + " dominating upstream reaction.", "int j = " + domStart + ";", "for (int i = " + start + "; i < " + end + "; i++) {", ("    if (i / " + divisor + " != " + currentFederate.bankIndex + ") continue; // Reaction is not in the federate." if isFederated else ""), ("    if (j / " + domDivisor + " != " + currentFederate.bankIndex + ") continue; // Dominating reaction is not in the federate." if runtime.dominating != None else ""), "    " + reactionRef + ".last_enabling_reaction = " + dominatingRef + ";", "}"))
            code_.endScopedBlock()
        elif end == start + 1:
            reactionRef = CUtil.reactionRef(runtime.getReaction(), "" + start)
            if runtime.dominating != None and (domDivisor == 1 or domStart / domDivisor == currentFederate.bankIndex):
                dominatingRef = "&(" + CUtil.reactionRef(runtime.dominating.getReaction(), "" + domStart) + ")"
            if not isFederated or (start / divisor == currentFederate.bankIndex) and (runtime.dominating == None or domStart / domDivisor == currentFederate.bankIndex):
                code_.pr(String.join("\n", "// " + runtime.getReaction().getFullName() + " dominating upstream reaction.", reactionRef + ".last_enabling_reaction = " + dominatingRef + ";"))
        return str(code_)

    @classmethod
    def deferredFillTriggerTable(cls, currentFederate, reactions, isFederated):
        """ generated source for method deferredFillTriggerTable """
        code_ = CodeBuilder()
        for reaction in reactions:
            name = reaction.getParent().getFullName()
            reactorSelfStruct = CUtil.reactorRef(reaction.getParent(), sr)
            foundPort = False
            for port in Iterables.filter(reaction.effects, PortInstance.__class__):
                if not foundPort:
                    code_.startScopedBlock()
                    code_.pr("int triggers_index[" + reaction.getParent().getTotalWidth() + "] = { 0 }; // Number of bank members with the reaction.")
                    foundPort = True
                for srcRange in port.eventualDestinations():
                    srcNested = True if (port.isInput()) else False
                    code_.startScopedRangeBlock(currentFederate, srcRange, sr, sb, sc, srcNested, isFederated, True)
                    triggerArray = CUtil.reactionRef(reaction, sr) + ".triggers[triggers_index[" + sr + "]++]"
                    if currentFederate.contains(port.getParent()):
                        code_.pr(String.join("\n", "// Reaction " + reaction.index + " of " + name + " triggers " + len(srcRange.destinations) + " downstream reactions", "// through port " + port.getFullName() + ".", CUtil.reactionRef(reaction, sr) + ".triggered_sizes[triggers_index[" + sr + "]] = " + len(srcRange.destinations) + ";", "// For reaction " + reaction.index + " of " + name + ", allocate an", "// array of trigger pointers for downstream reactions through port " + port.getFullName(), "trigger_t** trigger_array = (trigger_t**)_lf_allocate(", "        " + len(srcRange.destinations) + ", sizeof(trigger_t*),", "        &" + reactorSelfStruct + "->base.allocations); ", triggerArray + " = trigger_array;"))
                    else:
                        code_.pr(CUtil.reactionRef(reaction, sr) + ".triggered_sizes[" + sc + "] = 0;")
                    code_.endScopedRangeBlock(srcRange, isFederated)
            cumulativePortWidth = 0
            for port in Iterables.filter(reaction.effects, PortInstance.__class__):
                if port.eventualDestinations().isEmpty():
                    continue 
                code_.pr("for (int i = 0; i < " + reaction.getParent().getTotalWidth() + "; i++) triggers_index[i] = " + cumulativePortWidth + ";")
                for srcRange in port.eventualDestinations():
                    if currentFederate.contains(port.getParent()):
                        srcNested = srcRange.instance.isInput()
                        multicastCount = 0
                        for dstRange in srcRange.destinations:
                            dst = dstRange.instance
                            code_.startScopedRangeBlock(currentFederate, srcRange, dstRange, isFederated)
                            triggerArray = ""
                            if srcNested and port.getParent().getWidth() > 1 and not (isFederated and port.getParent().getDepth() == 1):
                                triggerArray = CUtil.reactionRef(reaction, sr) + ".triggers[triggers_index[" + sr + "] + " + sc + " + src_range_mr.digits[1] * src_range_mr.radixes[0]]"
                            else:
                                triggerArray = CUtil.reactionRef(reaction, sr) + ".triggers[triggers_index[" + sr + "] + " + sc + "]"
                            if dst.isOutput():
                                belongs = False
                                for destinationReaction in dst.getDependentReactions():
                                    if currentFederate.contains(destinationReaction.getParent()):
                                        belongs = True
                                if belongs:
                                    code_.pr(String.join("\n", "// Port " + port.getFullName() + " has reactions in its parent's parent.", "// Point to the trigger struct for those reactions.", triggerArray + "[" + multicastCount + "] = &" + CUtil.triggerRefNested(dst, dr, db) + ";"))
                                else:
                                    code_.pr(String.join("\n", "// Port " + port.getFullName() + " has reactions in its parent's parent.", "// But those are not in the federation.", triggerArray + "[" + multicastCount + "] = NULL;"))
                            else:
                                code_.pr(String.join("\n", "// Point to destination port " + dst.getFullName() + "'s trigger struct.", triggerArray + "[" + multicastCount + "] = &" + CUtil.triggerRef(dst, dr) + ";"))
                            code_.endScopedRangeBlock(srcRange, dstRange, isFederated)
                            multicastCount += 1
                if port.getParent() != reaction.getParent():
                    cumulativePortWidth += port.getWidth() * port.getParent().getWidth()
                else:
                    cumulativePortWidth += port.getWidth()
            if foundPort:
                code_.endScopedBlock()
        return str(code_)

    @classmethod
    def deferredInputNumDestinations(cls, currentFederate, reactions, isFederated):
        """ generated source for method deferredInputNumDestinations """
        portsHandled = set()
        code_ = CodeBuilder()
        for reaction in reactions:
            for port in Iterables.filter(reaction.effects, PortInstance.__class__):
                if port.isInput() and not portsHandled.contains(port):
                    portsHandled.append(port)
                    code_.pr("// For reference counting, set num_destinations for port " + port.getParent().__name__ + "." + port.__name__ + ".")
                    for sendingRange in port.eventualDestinations():
                        code_.startScopedRangeBlock(currentFederate, sendingRange, sr, sb, sc, sendingRange.instance.isInput(), isFederated, True)
                        connector = "->" if (port.isMultiport()) else "."
                        code_.pr(CUtil.portRefNested(port, sr, sb, sc) + connector + "num_destinations = " + sendingRange.getNumberOfDestinationReactors() + ";")
                        code_.endScopedRangeBlock(sendingRange, isFederated)
        return str(code_)

    @classmethod
    def deferredOutputNumDestinations(cls, currentFederate, reactor, isFederated):
        """ generated source for method deferredOutputNumDestinations """
        code_ = CodeBuilder()
        for output in reactor.outputs:
            for sendingRange in output.eventualDestinations():
                code_.pr("// For reference counting, set num_destinations for port " + output.getFullName() + ".")
                code_.startScopedRangeBlock(currentFederate, sendingRange, sr, sb, sc, sendingRange.instance.isInput(), isFederated, True)
                code_.pr(CUtil.portRef(output, sr, sb, sc) + ".num_destinations = " + sendingRange.getNumberOfDestinationReactors() + ";")
                code_.endScopedRangeBlock(sendingRange, isFederated)
        return str(code_)

    @classmethod
    def deferredInitializeNonNested(cls, currentFederate, reactor, main, reactions, isFederated):
        """ generated source for method deferredInitializeNonNested """
        code_ = CodeBuilder()
        code_.pr("// **** Start non-nested deferred initialize for " + reactor.getFullName())
        code_.pr(cls.deferredInputNumDestinations(currentFederate, reactions, isFederated))
        if reactor != main:
            code_.pr(cls.deferredOutputNumDestinations(currentFederate, reactor, isFederated))
        code_.pr(cls.deferredFillTriggerTable(currentFederate, reactions, isFederated))
        code_.pr(cls.deferredOptimizeForSingleDominatingReaction(currentFederate, reactor, isFederated))
        for child in reactor.children:
            if currentFederate.contains(child):
                code_.pr(cls.deferredInitializeNonNested(currentFederate, child, main, child.reactions, isFederated))
        code_.pr("// **** End of non-nested deferred initialize for " + reactor.getFullName())
        return str(code_)

    @classmethod
    def deferredCreateDefaultTokens(cls, reactor, types):
        """ generated source for method deferredCreateDefaultTokens """
        code_ = CodeBuilder()
        for output in reactor.outputs:
            type = ASTUtils.getInferredType(output.getDefinition())
            if CUtil.isTokenType(type, types):
                rootType = CUtil.rootType(types.getTargetType(type))
                size = "0" if (rootType == "void") else "sizeof(" + rootType + ")"
                code_.startChannelIteration(output)
                code_.pr(CUtil.portRef(output) + ".token = _lf_create_token(" + size + ");")
                code_.endChannelIteration(output)
        return str(code_)

    @classmethod
    def deferredReactionOutputs(cls, currentFederate, reaction, targetConfig, isFederated):
        """ generated source for method deferredReactionOutputs """
        code_ = CodeBuilder()
        name = reaction.getParent().getFullName()
        if targetConfig.logLevel.compareTo(LogLevel.LOG) >= 0:
            code_.pr(CUtil.reactionRef(reaction) + ".name = " + addDoubleQuotes(name + " reaction " + reaction.index) + ";")
        reactorSelfStruct = CUtil.reactorRef(reaction.getParent())
        outputCount = 0
        init = CodeBuilder()
        init.startScopedBlock()
        init.pr("int count = 0; SUPPRESS_UNUSED_WARNING(count);")
        for effect in Iterables.filter(reaction.effects, PortInstance.__class__):
            bankWidth = 1
            portRef = ""
            if effect.isInput():
                init.pr("// Reaction writes to an input of a contained reactor.")
                bankWidth = effect.getParent().getWidth()
                init.startScopedBlock(effect.getParent(), currentFederate, isFederated, True)
                portRef = CUtil.portRefNestedName(effect)
            else:
                init.startScopedBlock()
                portRef = CUtil.portRefName(effect)
            if effect.isMultiport():
                connector = "."
                if effect.isInput():
                    connector = "->"
                init.pr(String.join("\n", "for (int i = 0; i < " + effect.getWidth() + "; i++) {", "    " + CUtil.reactionRef(reaction) + ".output_produced[i + count]", "            = &" + portRef + "[i]" + connector + "is_present;", "}", "count += " + effect.getWidth() + ";"))
                outputCount += effect.getWidth() * bankWidth
            else:
                init.pr(CUtil.reactionRef(reaction) + ".output_produced[count++] = &" + portRef + ".is_present;")
                outputCount += bankWidth
            init.endScopedBlock()
        init.endScopedBlock()
        code_.pr(String.join("\n", "// Total number of outputs (single ports and multiport channels)", "// produced by " + reaction + ".", CUtil.reactionRef(reaction) + ".num_outputs = " + outputCount + ";"))
        if outputCount > 0:
            code_.pr(String.join("\n", "// Allocate memory for triggers[] and triggered_sizes[] on the reaction_t", "// struct for this reaction.", CUtil.reactionRef(reaction) + ".triggers = (trigger_t***)_lf_allocate(", "        " + outputCount + ", sizeof(trigger_t**),", "        &" + reactorSelfStruct + "->base.allocations);", CUtil.reactionRef(reaction) + ".triggered_sizes = (int*)_lf_allocate(", "        " + outputCount + ", sizeof(int),", "        &" + reactorSelfStruct + "->base.allocations);", CUtil.reactionRef(reaction) + ".output_produced = (bool**)_lf_allocate(", "        " + outputCount + ", sizeof(bool*),", "        &" + reactorSelfStruct + "->base.allocations);"))
        code_.pr(String.join("\n", str(init), "// ** End initialization for reaction " + reaction.index + " of " + name))
        return str(code_)

    @classmethod
    def deferredReactionMemory(cls, currentFederate, reactions, targetConfig, isFederated):
        """ generated source for method deferredReactionMemory """
        code_ = CodeBuilder()
        for reaction in reactions:
            code_.pr(cls.deferredReactionOutputs(currentFederate, reaction, targetConfig, isFederated))
            reactorSelfStruct = CUtil.reactorRef(reaction.getParent())
            for trigger in Iterables.filter(reaction.triggers, PortInstance.__class__):
                if trigger.isMultiport() and trigger.getParent() != None and trigger.isOutput():
                    code_.pr(String.join("\n", "// Allocate memory to store pointers to the multiport output " + trigger.__name__ + " ", "// of a contained reactor " + trigger.getParent().getFullName()))
                    code_.startScopedBlock(trigger.getParent(), currentFederate, isFederated, True)
                    width = trigger.getWidth()
                    portStructType = CGenerator.variableStructType(trigger)
                    code_.pr(String.join("\n", CUtil.reactorRefNested(trigger.getParent()) + "." + trigger.__name__ + "_width = " + width + ";", CUtil.reactorRefNested(trigger.getParent()) + "." + trigger.__name__, "        = (" + portStructType + "**)_lf_allocate(", "                " + width + ", sizeof(" + portStructType + "*),", "                &" + reactorSelfStruct + "->base.allocations); "))
                    code_.endScopedBlock()
        return str(code_)

    @classmethod
    def deferredAllocationForEffectsOnInputs(cls, currentFederate, reactor, isFederated):
        """ generated source for method deferredAllocationForEffectsOnInputs """
        code_ = CodeBuilder()
        portsHandled = set()
        reactorSelfStruct = CUtil.reactorRef(reactor)
        for reaction in reactor.reactions:
            for effect in Iterables.filter(reaction.effects, PortInstance.__class__):
                if effect.getParent().getDepth() > reactor.getDepth() and effect.isMultiport() and not portsHandled.contains(effect) and currentFederate.contains(effect.getParent()):
                    code_.pr("// A reaction writes to a multiport of a child. Allocate memory.")
                    portsHandled.append(effect)
                    code_.startScopedBlock(effect.getParent(), currentFederate, isFederated, True)
                    portStructType = CGenerator.variableStructType(effect)
                    effectRef = CUtil.portRefNestedName(effect)
                    code_.pr(String.join("\n", effectRef + "_width = " + effect.getWidth() + ";", "// Allocate memory to store output of reaction feeding ", "// a multiport input of a contained reactor.", effectRef + " = (" + portStructType + "**)_lf_allocate(", "        " + effect.getWidth() + ", sizeof(" + portStructType + "*),", "        &" + reactorSelfStruct + "->base.allocations); ", "for (int i = 0; i < " + effect.getWidth() + "; i++) {", "    " + effectRef + "[i] = (" + portStructType + "*)_lf_allocate(", "            1, sizeof(" + portStructType + "),", "            &" + reactorSelfStruct + "->base.allocations); ", "}"))
                    code_.endScopedBlock()
        return str(code_)

    @classmethod
    def deferredInitialize(cls, currentFederate, reactor, reactions, targetConfig, types, isFederated):
        """ generated source for method deferredInitialize """
        if not currentFederate.contains(reactor):
            return ""
        code_ = CodeBuilder()
        code_.pr("// **** Start deferred initialize for " + reactor.getFullName())
        code_.startScopedBlock(reactor, currentFederate, isFederated, True)
        code_.pr(cls.deferredAllocationForEffectsOnInputs(currentFederate, reactor, isFederated))
        code_.pr(cls.deferredReactionMemory(currentFederate, reactions, targetConfig, isFederated))
        code_.pr(cls.deferredCreateDefaultTokens(reactor, types))
        for child in reactor.children:
            if currentFederate.contains(child):
                code_.pr(cls.deferredInitialize(currentFederate, child, child.reactions, targetConfig, types, isFederated))
        code_.endScopedBlock()
        code_.pr("// **** End of deferred initialize for " + reactor.getFullName())
        return code_.__str__()
