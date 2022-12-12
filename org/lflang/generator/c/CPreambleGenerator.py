#!/usr/bin/env python
""" generated source for module CPreambleGenerator """
# package: org.lflang.generator.c
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.List
from lflang.generator.c import CCoreFilesUtils
from org.lflang import TargetConfig

from org.lflang.TargetConfig import ClockSyncOptions

from org.lflang.TargetProperty import Platform

from org.lflang.TargetProperty import ClockSyncMode

from org.lflang.TargetProperty import CoordinationType

from org.lflang.generator import CodeBuilder

from org.lflang.generator import GeneratorBase

from org.lflang.util import StringUtil

# 
#  * Generates code for preambles for the C and CCpp target.
#  * This includes #include and #define directives at the top
#  * of each generated ".c" file.
#  *
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Mehrdad Niknami <mniknami@berkeley.edu>}
#  * @author{Christian Menard <christian.menard@tu-dresden.de>}
#  * @author{Matt Weber <matt.weber@berkeley.edu>}
#  * @author{Soroush Bateni <soroush@utdallas.edu>
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  * @author{Hou Seng Wong <housengw@berkeley.edu>}
#  
class CPreambleGenerator:
    """ generated source for class CPreambleGenerator """
    #  Add necessary source files specific to the target language.  
    @classmethod
    def generateIncludeStatements(cls, targetConfig, isFederated):
        """ generated source for method generateIncludeStatements """
        tracing = targetConfig.tracing
        code_ = CodeBuilder()
        if targetConfig.platform == Platform.ARDUINO:
            for it in CCoreFilesUtils.getArduinoTargetHeaders():
                # CCoreFilesUtils.getArduinoTargetHeaders().forEach(
                # it ->
                code_.pr("#include " + StringUtil.addDoubleQuotes(it))
                #  );
        for it in CCoreFilesUtils.getCTargetHeader():
            # CCoreFilesUtils.getCTargetHeader().forEach(
            #  it ->
            code_.pr("#include " + StringUtil.addDoubleQuotes(it))
            # );
        if targetConfig.threading:
            code_.pr("#include \"core/threaded/reactor_threaded.c\"")
            code_.pr("#include \"core/threaded/scheduler.h\"")
        else:
            code_.pr("#include \"core/reactor.c\"")
        if isFederated:
            code_.pr("#include \"core/federated/federate.c\"")
        if tracing != None:
            code_.pr("#include \"core/trace.c\"")
        code_.pr("#include \"core/mixed_radix.h\"")
        code_.pr("#include \"core/port.h\"")
        return str(code_)

    @classmethod
    def generateDefineDirectives(cls, targetConfig, numFederates, isFederated, srcGenPath, clockSyncIsOn, hasModalReactors):
        """ generated source for method generateDefineDirectives """
        logLevel = targetConfig.logLevel.ordinal()
        coordinationType = targetConfig.coordination
        advanceMessageInterval = targetConfig.coordinationOptions.advance_message_interval
        tracing = targetConfig.tracing
        code_ = CodeBuilder()
        code_.pr("#define LOG_LEVEL " + logLevel)
        code_.pr("#define TARGET_FILES_DIRECTORY " + addDoubleQuotes(srcGenPath.__str__()))
        if targetConfig.platform == Platform.ARDUINO:
            code_.pr("#define MICROSECOND_TIME")
            code_.pr("#define BIT_32")
        if isFederated:
            code_.pr("#define NUMBER_OF_FEDERATES " + numFederates)
            code_.pr(generateFederatedDefineDirective(coordinationType))
            if advanceMessageInterval != None:
                code_.pr("#define ADVANCE_MESSAGE_INTERVAL " + GeneratorBase.timeInTargetLanguage(advanceMessageInterval))
        if tracing != None:
            code_.pr(generateTracingDefineDirective(targetConfig, tracing.traceFileName))
        if hasModalReactors:
            code_.pr("#define MODAL_REACTORS")
        if clockSyncIsOn:
            code_.pr(generateClockSyncDefineDirective(targetConfig.clockSync, targetConfig.clockSyncOptions))
        code_.newLine()
        return str(code_)

    #      * Returns the #define directive for the given coordination type.
    #      *
    #      * NOTE: Instead of checking #ifdef FEDERATED, we could
    #      *       use #if (NUMBER_OF_FEDERATES > 1).
    #      *       To Soroush Bateni, the former is more accurate.
    #      
    @classmethod
    def generateFederatedDefineDirective(cls, coordinationType):
        """ generated source for method generateFederatedDefineDirective """
        directives = []
        directives.append("#define FEDERATED")
        if coordinationType == CoordinationType.CENTRALIZED:
            directives.append("#define FEDERATED_CENTRALIZED")
        elif coordinationType == CoordinationType.DECENTRALIZED:
            directives.append("#define FEDERATED_DECENTRALIZED")
        return "\n".join([ directives])

    @classmethod
    def generateTracingDefineDirective(cls, targetConfig, traceFileName):
        """ generated source for method generateTracingDefineDirective """
        if traceFileName == None:
            targetConfig.compileDefinitions.put("LINGUA_FRANCA_TRACE", "")
            return "#define LINGUA_FRANCA_TRACE"
        targetConfig.compileDefinitions.put("LINGUA_FRANCA_TRACE", traceFileName)
        return "#define LINGUA_FRANCA_TRACE " + traceFileName

    #      * Initialize clock synchronization (if enabled) and its related options for a given federate.
    #      *
    #      * Clock synchronization can be enabled using the clock-sync target property.
    #      * @see <a href="https://github.com/icyphy/lingua-franca/wiki/Distributed-Execution#clock-synchronization">Documentation</a>
    #      
    @classmethod
    def generateClockSyncDefineDirective(cls, mode, options):
        """ generated source for method generateClockSyncDefineDirective """
        code_ = ArrayList(list("#define _LF_CLOCK_SYNC_INITIAL", "#define _LF_CLOCK_SYNC_PERIOD_NS " + GeneratorBase.timeInTargetLanguage(options.period), "#define _LF_CLOCK_SYNC_EXCHANGES_PER_INTERVAL " + options.trials, "#define _LF_CLOCK_SYNC_ATTENUATION " + options.attenuation))
        if mode == ClockSyncMode.ON:
            code_.append("#define _LF_CLOCK_SYNC_ON")
            if options.collectStats:
                code_.append("#define _LF_CLOCK_SYNC_COLLECT_STATS")
        return "\n".join([ code_])
