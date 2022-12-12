#!/usr/bin/env python
""" generated source for module CTimerGenerator """
# package: org.lflang.generator.c
# import java.util.List
from lflang.generator.c import CUtil
from org.lflang.generator import GeneratorBase

from org.lflang.generator import TimerInstance

# 
#  * Generates C code to declare and initialize timers.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>
#  
class CTimerGenerator:
    """ generated source for class CTimerGenerator """
    #      * Generate code to initialize the given timer.
    #      *
    #      * @param timer The timer to initialize for.
    #      
    @classmethod
    def generateInitializer(cls, timer):
        """ generated source for method generateInitializer """
        triggerStructName = CUtil.reactorRef(timer.getParent()) + "->_lf__" + timer.__name__
        offset = GeneratorBase.timeInTargetLanguage(timer.getOffset())
        period = GeneratorBase.timeInTargetLanguage(timer.getPeriod())
        mode = timer.getMode(False)
        modeRef = "&" + CUtil.reactorRef(mode.getParent()) + "->_lf__modes[" + mode.getParent().modes.indexOf(mode) + "];" if mode != None else "NULL"
        return "\n".join([ list("// Initializing timer " + timer.getFullName() + ".", triggerStructName + ".offset = " + offset + ";", triggerStructName + ".period = " + period + ";", "_lf_timer_triggers[_lf_timer_triggers_count++] = &" + triggerStructName + ";", triggerStructName + ".mode = " + modeRef + ";")])

    #      * Generate code to declare the timer table.
    #      *
    #      * @param timerCount The total number of timers in the program
    #      
    @classmethod
    def generateDeclarations(cls, timerCount):
        """ generated source for method generateDeclarations """
        return "\n".join([ list("// Array of pointers to timer triggers to be scheduled in _lf_initialize_timers().", ("trigger_t* _lf_timer_triggers[" + timerCount + "]" if timerCount > 0 else "trigger_t** _lf_timer_triggers = NULL") + ";", "int _lf_timer_triggers_size = " + timerCount + ";")])

    #      * Generate code to call `_lf_initialize_timer` on each timer.
    #      *
    #      * @param timerCount The total number of timers in the program
    #      
    @classmethod
    def generateLfInitializeTimer(cls, timerCount):
        """ generated source for method generateLfInitializeTimer """
        return "\n".join([ "void _lf_initialize_timers() {", "\nfor (int i = 0; i < _lf_timer_triggers_size; i++) {\n                    if (_lf_timer_triggers[i] != NULL) {\n                        _lf_initialize_timer(_lf_timer_triggers[i]);\n                    }\n}".indent(4) if timerCount > 0 else "", "}"])
