#!/usr/bin/env python
""" generated source for module CTracingGenerator """
# package: org.lflang.generator.c
# import java.util.ArrayList
# import java.util.List
from lflang.generator.c import CUtil
from org.lflang.federated import FederateInstance

from org.lflang.generator import ActionInstance

from org.lflang.generator import ReactorInstance

from org.lflang.generator import TimerInstance

# 
#  * Generates C code to support tracing.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#  
class CTracingGenerator:
    """ generated source for class CTracingGenerator """
    #      * If tracing is turned on, then generate code that records
    #      * the full name of the specified reactor instance in the
    #      * trace table. If tracing is not turned on, do nothing.
    #      *
    #      * If tracing is turned on, record the address of this reaction
    #      * in the _lf_trace_object_descriptions table that is used to generate
    #      * the header information in the trace file.
    #      *
    #      * @param instance The reactor instance.
    #      * @param currentFederate The federate instance we are generating code for.
    #      
    @classmethod
    def generateTraceTableEntries(cls, instance, currentFederate):
        """ generated source for method generateTraceTableEntries """
        code_ = []
        description = CUtil.getShortenedName(instance)
        selfStruct = CUtil.reactorRef(instance)
        code_.append(registerTraceEvent(selfStruct, "NULL", "trace_reactor", description))
        for action in instance.actions:
            if currentFederate.contains(action.getDefinition()):
                code_.append(registerTraceEvent(selfStruct, getTrigger(selfStruct, action.__name__), "trace_trigger", description + "." + action.__name__))
        for timer in instance.timers:
            if currentFederate.contains(timer.getDefinition()):
                code_.append(registerTraceEvent(selfStruct, getTrigger(selfStruct, timer.__name__), "trace_trigger", description + "." + timer.__name__))
        return "\n".join([ code_])

    @classmethod
    def registerTraceEvent(cls, obj, trigger, type, description):
        """ generated source for method registerTraceEvent """
        return "_lf_register_trace_event(" + obj + ", " + trigger + ", " + type + ", " + addDoubleQuotes(description) + ");"

    @classmethod
    def getTrigger(cls, obj, triggerName):
        """ generated source for method getTrigger """
        return "&(" + obj + "->_lf__" + triggerName + ")"
