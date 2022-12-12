#!/usr/bin/env python
""" generated source for module ModeInstance """
# 
# Copyright (c) 2021, Kiel University.
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
# import java.util.LinkedList
# import java.util.List

from org.lflang.lf import Mode

from org.lflang.lf import ModeTransition

from org.lflang.lf import VarRef

# 
#  * Representation of a runtime instance of a mode.
#  *  
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  


# //////////////////////////////////////////////////
#  Data class.
class Transition(NamedInstance, VarRef):
    """ generated source for class Transition """
    source = None
    target = None
    reaction = None
    type = None

    def __init__(self, source, target, reaction, definition):
        """ generated source for method __init__ """
        super().__init__(source.parent)
        self.source = source
        self.target = target
        self.reaction = reaction
        self.type = ModeTransition.RESET if definition.getTransition() == None else definition.getTransition()

    def getName(self):
        """ generated source for method getName """
        return self.source.__name__ + " -> " + self.target + " by " + self.reaction.__name__

    def root(self):
        """ generated source for method root """
        return self.parent.root()

    def getType(self):
        """ generated source for method getType """
        return self.type


class ModeInstance(NamedInstance, Mode):
    """ generated source for class ModeInstance """
    #      * Create a new reaction instance from the specified definition
    #      * within the specified parent. This constructor should be called
    #      * only by the ReactorInstance class after all other contents
    #      * (reactions, etc.) are registered because this constructor call
    #      * will look them up.
    #      * @param definition A mode definition.
    #      * @param parent The parent reactor instance, which cannot be null.
    #      
    def __init__(self, definition, parent):
        """ generated source for method __init__ """
        super().__init__(parent)
        collectMembers()

    # //////////////////////////////////////////////////
    #  Member fields.
    #  The action instances belonging to this mode instance. 
    actions = LinkedList()

    #  The reactor instances belonging to this mode instance, in order of declaration. 
    instantiations = LinkedList()

    #  List of reaction instances for this reactor instance. 
    reactions = LinkedList()

    #  The timer instances belonging to this reactor instance. 
    timers = LinkedList()

    #  The outgoing transitions of this mode. 
    transitions = LinkedList()

    # //////////////////////////////////////////////////
    #  Public methods.
    #      * Return the name of this mode.
    #      * @return The name of this mode.
    #      
    def getName(self):
        """ generated source for method getName """
        return self.definition.__name__

    #      * {@inheritDoc}
    #      
    def root(self):
        """ generated source for method root """
        return parent.root()

    #      * Return a descriptive string.
    #      
    def __str__(self):
        """ generated source for method toString """
        return self.__name__ + " of " + parent.getFullName()

    #      * Returns true iff this mode is the initial mode of this reactor instance.
    #      
    def isInitial(self):
        """ generated source for method isInitial """
        return definition.isInitial()

    #      * Sets up all transitions that leave this mode.
    #      * Requires that all mode instances and other contents
    #      * (reactions, etc.) of the parent reactor are created.
    #      
    def setupTranstions(self):
        """ generated source for method setupTranstions """
        self.transitions = []
        for reaction in reactions:
            for effect in reaction.definition.getEffects():
                if isinstance(effect, (VarRef)):
                    target = effect.getVariable()
                    if isinstance(target, (Mode)):
                        self.transitions.append(Transition(self, parent.lookupModeInstance(target), reaction, effect))

    #      * Returns true iff this mode contains the given instance.
    #      
    def contains(self, instance):
        """ generated source for method contains """
        if isinstance(instance, (TimerInstance)):
            return self.timers.contains(instance)
        elif isinstance(instance, (ActionInstance)):
            return self.actions.contains(instance)
        elif isinstance(instance, (ReactorInstance)):
            return self.instantiations.contains(instance)
        elif isinstance(instance, (ReactionInstance)):
            return self.reactions.contains(instance)
        else:
            return False

    # //////////////////////////////////////////////////
    #  Private methods.
    def collectMembers(self):
        """ generated source for method collectMembers """
        #  Collect timers
        for decl in definition.getTimers():
            instance = parent.lookupTimerInstance(decl)
            if instance != None:
                self.timers.append(instance)
        #  Collect actions
        for decl in definition.getActions():
            instance = parent.lookupActionInstance(decl)
            if instance != None:
                self.actions.append(instance)
        #  Collect reactor instantiation
        for decl in definition.getInstantiations():
            instance = parent.lookupReactorInstance(decl)
            if instance != None:
                self.instantiations.append(instance)
        #  Collect reactions
        for decl in definition.getReactions():
            instance = parent.lookupReactionInstance(decl)
            if instance != None:
                self.reactions.append(instance)

