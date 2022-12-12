#!/usr/bin/env python
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
from include.SpecialExceptions import IllegalArgumentException
from lflang.generator.InvalidSourceException import InvalidSourceException
from lflang.generator.TriggerInstance import TriggerInstance
from org.lflang.TimeValue import TimeValue
from org.lflang.lf import Timer

# Instance of a timer.
#
# @author{Marten Lohstroh <marten@berkeley.edu>}
# @author{Edward A. Lee <eal@berkeley.edu>}


class TimerInstance(TriggerInstance, Timer):
    """ generated source for class TimerInstance """
    #  The global default for offset. 
    DEFAULT_OFFSET = TimeValue.ZERO

    #  The global default for period. 
    DEFAULT_PERIOD = TimeValue.ZERO

    def __init__(self, definition, parent):
        """
        Create a new timer instance.
        If the definition is null, then this is a startup timer.
        :param definition: The AST definition, or null for startup.
        :param parent: The parent reactor.
        """
        super().__init__(parent)
        self.offset = self.DEFAULT_OFFSET
        self.period = self.DEFAULT_PERIOD

        if parent == None:
            raise InvalidSourceException("Cannot create an TimerInstance with no parent.")
        if definition is not None:
            if definition.getOffset() is not None:
                try:
                    self.offset = parent.getTimeValue(definition.getOffset())
                except IllegalArgumentException as ex:
                    parent.reporter.reportError(definition.getOffset(), f"Invalid time. {ex}")
            if definition.getPeriod() is not None:
                try:
                    self.period = parent.getTimeValue(definition.getPeriod())
                except IllegalArgumentException as ex:
                    parent.reporter.reportError(definition.getPeriod(), f"Invalid time. {ex}")

    def getOffset(self):
        """ Get the value of the offset parameter. """
        return self.offset

    def getPeriod(self):
        """  Get the value of the offset parameter. """
        return self.period
