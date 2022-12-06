#!/usr/bin/env python
""" generated source for module TimerInstance """
#  Instance of a timer. 
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
from org.lflang.TimeValue

from org.lflang.lf import Timer

# 
#  * Instance of a timer.
#  * 
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  
class TimerInstance(TriggerInstance, Timer):
    """ generated source for class TimerInstance """
    #  The global default for offset. 
    DEFAULT_OFFSET = TimeValue.ZERO

    #  The global default for period. 
    DEFAULT_PERIOD = TimeValue.ZERO
    offset = DEFAULT_OFFSET
    period = DEFAULT_PERIOD

    # 	 * Create a new timer instance.
    # 	 * If the definition is null, then this is a startup timer.
    # 	 * @param definition The AST definition, or null for startup.
    # 	 * @param parent The parent reactor.
    # 	 
    def __init__(self, definition, parent):
        """ generated source for method __init__ """
        super(TimerInstance, self).__init__(parent)
        if parent == None:
            raise InvalidSourceException("Cannot create an TimerInstance with no parent.")
        if definition != None:
            if definition.getOffset() != None:
                try:
                    self.offset = parent.getTimeValue(definition.getOffset())
                except IllegalArgumentException as ex:
                    parent.reporter.reportError(definition.getOffset(), "Invalid time.")
            if definition.getPeriod() != None:
                try:
                    self.period = parent.getTimeValue(definition.getPeriod())
                except IllegalArgumentException as ex:
                    parent.reporter.reportError(definition.getPeriod(), "Invalid time.")

    #      * Get the value of the offset parameter.
    #      
    def getOffset(self):
        """ generated source for method getOffset """
        return self.offset

    #      * Get the value of the offset parameter.
    #      
    def getPeriod(self):
        """ generated source for method getPeriod """
        return self.period
