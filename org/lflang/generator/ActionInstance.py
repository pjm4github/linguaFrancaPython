#!/usr/bin/env python
""" generated source for module ActionInstance """
#  Instance of an action. 
# 
# Copyright (c) 2019, The University of California at Berkeley.
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
from lflang.TimeValue import TimeValue
from lflang.generator.InvalidSourceException import InvalidSourceException
from lflang.generator.TriggerInstance import TriggerInstance
from org.lflang import TimeValue

from org.lflang.lf import Action

from org.lflang.lf import ActionOrigin

# 
#  * Instance of an action.
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  
class ActionInstance(TriggerInstance, Action):
    """ generated source for class ActionInstance """
    #  The constant default for a minimum delay. 
    DEFAULT_MIN_DELAY = TimeValue.ZERO

    #  The minimum delay for this action. 
    minDelay = DEFAULT_MIN_DELAY

    #  The minimum spacing between action events. 
    minSpacing = None

    #  The replacement policy for when minimum spacing is violated. 
    policy = None

    #  Indicator of whether the action is physical. 
    physical = bool()

    #      * Create a new action instance.
    #      * If the definition is null, then this is a shutdown action.
    #      * @param definition The AST definition, or null for startup.
    #      * @param parent The parent reactor.
    #      
    def __init__(self, definition, parent):
        """ generated source for method __init__ """
        super().__init__(parent)
        if parent == None:
            raise InvalidSourceException("Cannot create an ActionInstance with no parent.")
        if definition != None:
            if definition.getMinDelay() != None:
                self.minDelay = parent.getTimeValue(definition.getMinDelay())
            if definition.getMinSpacing() != None:
                self.minSpacing = parent.getTimeValue(definition.getMinSpacing())
            if definition.getOrigin() == ActionOrigin.PHYSICAL:
                self.physical = True
            self.policy = definition.getPolicy()

    #  Return the minimum delay for this action. 
    def getMinDelay(self):
        """ generated source for method getMinDelay """
        return self.minDelay

    #  Return the minimum spacing between action events. 
    def getMinSpacing(self):
        """ generated source for method getMinSpacing """
        return self.minSpacing

    #  Return the replacement policy for when minimum spacing is violated. 
    def getPolicy(self):
        """ generated source for method getPolicy """
        return self.policy

    #  Return the indicator of whether the action is physical. 
    def isPhysical(self):
        """ generated source for method isPhysical """
        return self.physical
