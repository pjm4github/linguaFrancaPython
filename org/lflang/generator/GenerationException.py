#!/usr/bin/env python
""" generated source for module GenerationException """
# 
#  * Copyright (c) 2021, TU Dresden.
#  *
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  *
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  *
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  * THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  * THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.generator
# import org.eclipse.emf.ecore.EObject
from include.SpecialExceptions import RuntimeException
from include.overloading import overloaded

#  import org.jetbrains.annotations.Nullable;
# 
#  * An exception that occurred during code generation. May also
#  * wrap another exception.
#
from lflang.diagram.synthesis.util.LayoutPostProcessing import EObject


class Throwable:
    pass


class GenerationException(RuntimeException):
    """ generated source for class GenerationException """
    #  note that this is an unchecked exception.
    #  @Nullable 
    location = None

    @overloaded
    def __init__(self, message):
        """ generated source for method __init__ """
        super(GenerationException, self).__init__()
        self.__init__(None, message, None)

    @__init__.register(object, EObject, str)
    def __init___0(self, location, message):
        """ generated source for method __init___0 """
        super(GenerationException, self).__init__()
        #  @Nullable 
        self.__init__(location, message, None)

    @__init__.register(object, str, Throwable)
    def __init___1(self, message, cause):
        """ generated source for method __init___1 """
        super(GenerationException, self).__init__()
        self.__init__(None, message, cause)

    @__init__.register(object, EObject, str, Throwable)
    def __init___2(self, location, message, cause):
        """ generated source for method __init___2 """
        #  @Nullable 
        super(GenerationException, self).__init__(cause)
        self.location = location

    @__init__.register(object, Throwable)
    def __init___3(self, cause):
        """ generated source for method __init___3 """
        super(GenerationException, self).__init__()
        self.__init__(None, None, cause)

    #  @Nullable 
    def getLocation(self):
        """ generated source for method getLocation """
        return self.location
