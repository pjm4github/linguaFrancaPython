#!/usr/bin/env python
""" generated source for module InvalidLfSourceException """
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
from include.overloading import overloaded

# 
#  * An exception that indicates invalid source, which should
#  * be reported to the user. This is an error, it should not
#  * be used for warnings.
#  *
#  * @author Clément Fournier
#  
class InvalidLfSourceException(RuntimeException):
    """ generated source for class InvalidLfSourceException """
    node = None
    problem = None

    @overloaded
    def __init__(self, node, problem):
        """ generated source for method __init__ """
        super(InvalidLfSourceException, self).__init__(problem)
        self.node = node
        self.problem = problem

    @__init__.register(object, str, EObject)
    def __init___0(self, problem, node):
        """ generated source for method __init___0 """
        super(InvalidLfSourceException, self).__init__()
        self.__init__(node, problem)

    def getNode(self):
        """ generated source for method getNode """
        return self.node

    def getProblem(self):
        """ generated source for method getProblem """
        return self.problem
