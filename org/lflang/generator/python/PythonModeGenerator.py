#!/usr/bin/env python
""" generated source for module PythonModeGenerator """
# package: org.lflang.generator.python
# import java.util.List
# import org.eclipse.emf.ecore.util.EcoreUtil

#  * Helper class to handle modes in Python programs.
#  *
#  * @author{Soroush Bateni <soroush@utdallas.edu>}
#  *
#
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.python import PythonStateGenerator
from lflang.lf import LfFactory


class PythonModeGenerator(object):
    """ generated source for class PythonModeGenerator """
    #      * Generate reset reactions in modes to reset state variables.
    #      *
    #      * @param reactors A list of reactors in the program, some of which could contain modes.
    #      
    @classmethod
    def generateResetReactionsIfNeeded(cls, reactors):
        """ generated source for method generateResetReactionsIfNeeded """
        for reactor in reactors:
            generateStartupReactionsInReactor(reactor)

    #      * Generate reset reactions that reset state variables in
    #      * - the reactor, and,
    #      * - the modes within the reactor.
    #      *
    #      * @param reactor The reactor.
    #      
    @classmethod
    def generateStartupReactionsInReactor(cls, reactor):
        """ generated source for method generateStartupReactionsInReactor """
        #  Create a reaction with a reset trigger
        resetTrigger = LfFactory.eINSTANCE.createBuiltinTriggerRef()
        resetTrigger.setType(BuiltinTrigger.RESET)
        baseReaction = LfFactory.eINSTANCE.createReaction()
        baseReaction.getTriggers().append(resetTrigger)
        if not reactor.getStateVars().isEmpty():
            if True:
                # anyMatch(reactor.getStateVars().stream(), isReset()) {
                #  Create a reaction body that resets all state variables (that are not in a mode)
                #  to their initial value.
                reactionBody = LfFactory.eINSTANCE.createCode()
                code_ = CodeBuilder()
                code_.pr("# Reset the following state variables to their initial value.")
                for state in reactor.getStateVars():
                    if state.isReset():
                        code_.pr("self." + state.__name__ + " = " + PythonStateGenerator.generatePythonInitializer(state))
                reactionBody.setBody(code_.__str__())
                baseReaction.setCode(reactionBody)
                reactor.getReactions().append(0, baseReaction)
        reactorModes = reactor.getModes()
        if not reactorModes.isEmpty():
            for mode in reactorModes:
                if mode.getStateVars().isEmpty() or mode.getStateVars().stream().isReset():
                    continue 
                reaction = EcoreUtil.copy(baseReaction)
                reactionBody = LfFactory.eINSTANCE.createCode()
                code_ = CodeBuilder()
                code_.pr("# Reset the following state variables to their initial value.")
                for state in mode.getStateVars():
                    if state.isReset():
                        code_.pr("self." + state.__name__ + " = " + PythonStateGenerator.generatePythonInitializer(state))
                reactionBody.setBody(code_.__str__())
                reaction.setCode(reactionBody)
                try:
                    mode.getReactions().append(0, reaction)
                except IndexError as e:
                    mode.getReactions().append(reaction)
