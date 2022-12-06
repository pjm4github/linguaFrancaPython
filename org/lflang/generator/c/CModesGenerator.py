#!/usr/bin/env python
""" generated source for module CModesGenerator """
# package: org.lflang.generator.c
# import java.util.List

#  * Generates C code to support modal models.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#
from lflang import ASTUtils
from lflang.generator.c import CUtil


class CModesGenerator(object):
    """ generated source for class CModesGenerator """
    #      * Generate fields in the self struct for mode instances
    #      *
    #      * @param reactor
    #      * @param body
    #      * @param constructorCode
    #      
    @classmethod
    def generateDeclarations(cls, reactor, body, constructorCode):
        """ generated source for method generateDeclarations """
        allModes = ASTUtils.allModes(reactor)
        if not allModes.isEmpty():
            #  Reactor's mode instances and its state.
            body.pr("\n".join([ "reactor_mode_t _lf__modes[" + reactor.getModes().size() + "];")])
            #  Initialize the mode instances
            constructorCode.pr("// Initialize modes")
            constructorCode.pr("self_base_t* _lf_self_base = (self_base_t*)self;")
            initialMode = -1
            i = 0
            while i < len(allModes):
                mode = allModes.get(i)
                constructorCode.pr(mode, "\n".join([ "self->_lf__modes[" + i + "].state = &_lf_self_base->_lf__mode_state;", "self->_lf__modes[" + i + "].name = \"" + mode.__name__ + "\";", "self->_lf__modes[" + i + "].deactivation_time = 0;", "self->_lf__modes[" + i + "].flags = 0;")])
                if initialMode < 0 and mode.isInitial():
                    initialMode = i
                i += 1
            assert initialMode >= 0
            #  Initialize mode state with initial mode active upon start
            constructorCode.pr("\n".join([ "// Initialize mode state", "_lf_self_base->_lf__mode_state.parent_mode = NULL;", "_lf_self_base->_lf__mode_state.initial_mode = &self->_lf__modes[" + initialMode + "];", "_lf_self_base->_lf__mode_state.current_mode = _lf_self_base->_lf__mode_state.initial_mode;", "_lf_self_base->_lf__mode_state.next_mode = NULL;", "_lf_self_base->_lf__mode_state.mode_change = no_transition;")])

    #      * Generate the declaration of modal models state table.
    #      *
    #      * @param hasModalReactors True if there is modal model reactors, false otherwise
    #      * @param modalReactorCount The number of modal model reactors
    #      * @param modalStateResetCount The number of modal model state resets
    #      
    @classmethod
    def generateModeStatesTable(cls, hasModalReactors, modalReactorCount, modalStateResetCount):
        """ generated source for method generateModeStatesTable """
        if hasModalReactors:
            return "\n".join([ "// Array of pointers to mode states to be handled in _lf_handle_mode_changes().", "reactor_mode_state_t* _lf_modal_reactor_states[" + modalReactorCount + "];", "int _lf_modal_reactor_states_size = " + modalReactorCount + ";", (String.join("\n", "// Array of reset data for state variables nested in modes. Used in _lf_handle_mode_changes().", "mode_state_variable_reset_data_t _lf_modal_state_reset[" + modalStateResetCount + "];", "int _lf_modal_state_reset_size = " + modalStateResetCount + ";") if modalStateResetCount > 0 else "")])
        return ""

    #      * Generate counter variable declarations used for registering modal reactors.
    #      * 
    #      * @param hasModalReactors True if there is modal model reactors, false otherwise
    #      
    @classmethod
    def generateModalInitalizationCounters(cls, hasModalReactors):
        """ generated source for method generateModalInitalizationCounters """
        if hasModalReactors:
            return "\n".join([ "int _lf_modal_reactor_states_count = 0;", "int _lf_modal_state_reset_count = 0;"])
        return ""

    #      * Generate code for modal reactor registration and hierarchy.
    #      * 
    #      * @param instance The reactor instance.
    #      * @param code The code builder.
    #      
    @classmethod
    def generateModeStructure(cls, instance, code_):
        """ generated source for method generateModeStructure """
        parentMode = instance.getMode(False)
        nameOfSelfStruct = CUtil.reactorRef(instance)
        #  If this instance is enclosed in another mode
        if parentMode != None:
            parentModeRef = "&" + CUtil.reactorRef(parentMode.getParent()) + "->_lf__modes[" + parentMode.getParent().modes.indexOf(parentMode) + "]"
            code_.pr("// Setup relation to enclosing mode")
            #  If this reactor does not have its own modes, all reactions must be linked to enclosing mode
            if instance.modes.isEmpty():
                i = 0
                for reaction in instance.reactions:
                    code_.pr(CUtil.reactorRef(reaction.getParent()) + "->_lf__reaction_" + i + ".mode = " + parentModeRef + ";")
                    i += 1
            else:
                #  Otherwise, only reactions outside modes must be linked and the mode state itself gets a parent relation
                code_.pr("((self_base_t*)" + nameOfSelfStruct + ")->_lf__mode_state.parent_mode = " + parentModeRef + ";")
                # for (var reaction : (Iterable<ReactionInstance>) instance.reactions.stream().filter(it -> it.getMode(true) == null)::iterator) {
                #     code.pr(CUtil.reactorRef(reaction.getParent())+"->_lf__reaction_"+instance.reactions.indexOf(reaction)+".mode = "+parentModeRef+";");
                # }
        #  If this reactor has modes, register for mode change handling
        if not instance.modes.isEmpty():
            code_.pr("// Register for transition handling")
            code_.pr("_lf_modal_reactor_states[_lf_modal_reactor_states_count++] = &((self_base_t*)" + nameOfSelfStruct + ")->_lf__mode_state;")

    #      * Generate code registering a state variable for automatic reset.
    #      * 
    #      * @param modeRef The code to refer to the mode
    #      * @param selfRef The code to refer to the self struct
    #      * @param varName The variable name in the self struct
    #      * @param source The variable that stores the initial value
    #      * @param type The size of the initial value
    #      
    @classmethod
    def generateStateResetStructure(cls, modeRef, selfRef, varName, source, type):
        """ generated source for method generateStateResetStructure """
        return "\n".join([ "// Register for automatic reset", "_lf_modal_state_reset[_lf_modal_state_reset_count].mode = " + modeRef + ";", "_lf_modal_state_reset[_lf_modal_state_reset_count].target = &(" + selfRef + "->" + varName + ");", "_lf_modal_state_reset[_lf_modal_state_reset_count].source = &" + source + ";", "_lf_modal_state_reset[_lf_modal_state_reset_count].size = sizeof(" + type + ");", "_lf_modal_state_reset_count++;"])

    #      * Generate code to call `_lf_process_mode_changes`.
    #      *
    #      * @param hasModalReactors True if there is modal model reactors, false otherwise
    #      * @param modalStateResetCount The number of modal model state resets
    #      
    @classmethod
    def generateLfHandleModeChanges(cls, hasModalReactors, modalStateResetCount):
        """ generated source for method generateLfHandleModeChanges """
        if not hasModalReactors:
            return ""
        return "\n".join([ "void _lf_handle_mode_changes() {", "    _lf_process_mode_changes(", "        _lf_modal_reactor_states, ", "        _lf_modal_reactor_states_size, ", "        " + ("_lf_modal_state_reset" if modalStateResetCount > 0 else "NULL") + ", ", "        " + ("_lf_modal_state_reset_size" if modalStateResetCount > 0 else "0") + ", ", "        _lf_timer_triggers, ", "        _lf_timer_triggers_size", "    );", "}"])

    #      * Generate code to call `_lf_initialize_modes`.
    #      * 
    #      * @param hasModalReactors True if there is modal model reactors, false otherwise
    #      
    @classmethod
    def generateLfInitializeModes(cls, hasModalReactors):
        """ generated source for method generateLfInitializeModes """
        if not hasModalReactors:
            return ""
        return "\n".join([ "void _lf_initialize_modes() {", "    _lf_initialize_mode_states(", "        _lf_modal_reactor_states, ", "        _lf_modal_reactor_states_size);", "}"])
