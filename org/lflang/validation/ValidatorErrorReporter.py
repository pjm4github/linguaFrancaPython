#!/usr/bin/env python
""" generated source for module ValidatorErrorReporter """
# 
#  * Copyright (c) 2021, TU Dresden.
#  * 
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  * 
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  * 
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
#  * 
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  * POSSIBILITY OF SUCH DAMAGE.
from include.overloading import overloaded
# package: org.lflang.validation
# import java.nio.file.Path
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.validation.ValidationMessageAcceptor

from org.lflang import ErrorReporter

# 
#  * This class translates messages reported via the ErrorReporrter interface to
#  * the interface of a given ValidationMessageAcceptor.
#  * 
#  * Effectively this allows to report errors via the ErrorReporter interface
#  * during validator checks, while having the validator still track all the
#  * reported warnings and messages. This is required for some functionality, like
#  * the construction of an instance graph in LFValidator.checkModel(). Since the
#  * instance graph is also used in other components, it does not report directly
#  * to the validator, but uses our custom ErrorReporter interface that we use
#  * during code generation. This class bridges the gap between the ErrorReporter
#  * interface and the messages that the validator expects.
#  * 
#  * @author Christian Menard <christian.menard@tu-dresden.de>
#  
class ValidatorErrorReporter(ErrorReporter):
    """ generated source for class ValidatorErrorReporter """
    acceptor = None
    validatorState = None
    errorsOccurred = False

    def __init__(self, acceptor, stateAccess):
        """ generated source for method __init__ """
        super(ValidatorErrorReporter, self).__init__()
        self.acceptor = acceptor
        self.validatorState = stateAccess

    #      * Report the given message as an error on the object currently under
    #      * validation.
    #      
    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """
        self.errorsOccurred = True
        self.acceptor.acceptError(message, self.validatorState.getCurrentObject(), None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return message

    #      * Report the given message as an error on the given object.
    #      
    @reportError.register(object, EObject, str)
    def reportError_0(self, object, message):
        """ generated source for method reportError_0 """
        self.errorsOccurred = True
        self.acceptor.acceptError(message, object, None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return message

    #      * Report the given message as an error on the current object.
    #      * 
    #      * Unfortunately, there is no way to provide a path and a line number to the
    #      * ValidationMessageAcceptor as messages can only be reported directly as
    #      * EObjects. While it is not an ideal solution, this method composes a
    #      * messages indicating the location of the error and reports this on the
    #      * object currently under validation. This way, the error message is not
    #      * lost, but it is not necessarily reported precisely at the location of the
    #      * actual error.
    #      
    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """
        self.errorsOccurred = True
        fullMessage = message + " (Reported from " + file.__str__() + " on line " + line.__str__() + ")"
        self.acceptor.acceptError(fullMessage, self.validatorState.getCurrentObject(), None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return fullMessage

    #      * Report the given message as a waring on the object currently under
    #      * validation.
    #      
    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """
        self.acceptor.acceptWarning(message, self.validatorState.getCurrentObject(), None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return message

    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """
        self.acceptor.acceptInfo(message, self.validatorState.getCurrentObject(), None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return message

    #      * Report the given message as a warning on the given object.
    #      
    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, object, message):
        """ generated source for method reportWarning_0 """
        self.acceptor.acceptWarning(message, object, None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return message

    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, object, message):
        """ generated source for method reportInfo_0 """
        self.acceptor.acceptInfo(message, object, None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return message

    #      * Report the given message as an warning on the current object.
    #      * 
    #      * Unfortunately, there is no way to provide a path and a line number to the
    #      * ValidationMessageAcceptor as messages can only be reported directly as
    #      * EObjects. While it is not an ideal solution, this method composes a
    #      * messages indicating the location of the warning and reports this on the
    #      * object currently under validation. This way, the warning message is not
    #      * lost, but it is not necessarily reported precisely at the location of the
    #      * actual warning.
    #      
    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """
        fullMessage = message + " (Reported from " + file.__str__() + " on line " + line.__str__() + ")"
        self.acceptor.acceptWarning(fullMessage, self.validatorState.getCurrentObject(), None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return fullMessage

    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """
        fullMessage = message + " (Reported from " + file.__str__() + " on line " + line.__str__() + ")"
        self.acceptor.acceptInfo(fullMessage, self.validatorState.getCurrentObject(), None, ValidationMessageAcceptor.INSIGNIFICANT_INDEX, None)
        return fullMessage

    #      * Check if errors where reported.
    #      *
    #      * @return true if errors where reported
    #      
    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return self.errorsOccurred
