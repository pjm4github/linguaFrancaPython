#!/usr/bin/env python
""" generated source for module LetInferenceTests """
# package: org.lflang.tests.compiler
#  Parsing unit tests. 
# 
#  Copyright (c) 2022, The University of California at Berkeley.
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# import java.nio.file.Path
# import javax.inject.Inject
# import org.eclipse.emf.common.util.TreeIterator
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.testing.InjectWith
# import org.eclipse.xtext.testing.extensions.InjectionExtension
# import org.eclipse.xtext.testing.util.ParseHelper
# import org.junit.jupiter.api.Assertions
# import org.junit.jupiter.api.Test
# import org.junit.jupiter.api.extension.ExtendWith

from org.lflang.lf import *


@ExtendWith(InjectionExtension.__class__)
@InjectWith(LFInjectorProvider.__class__)
class LetInferenceTest(object):
    """ generated source for class LetInferenceTest """
    #  * Test for getting minimum delay in reactions.
    #  * Checking the actions and port's delay,then get the minimum reaction delay.
    #  * @author{Wonseo Choi <wonsuh1202@hanyang.ac.kr>}
    #  * @author{Yunsang Cho <snsc7878@hanyang.ac.kr>}
    #  * @author{Marten Lohstroh <marten@berkeley.edu>}
    #  * @author{Hokeun Kim <hokeunkim@berkeley.edu>}
    #  
    parser = None

    def testLet(self):
        """ generated source for method testLet """
        model = self.parser.parse(String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    ramp = new Ramp();", "    print = new Print();", "    print2 = new Print();", "    ramp.y -> print.x after 20 msec;", "    ramp.y -> print2.x after 30 msec;", "}", "reactor Ramp {", "    logical action a(60 msec):int;", "    logical action b(100 msec):int;", "    input x:int;", "    output y:int;", "    output z:int;", "    reaction(startup) -> y, z, a, b{=", "    =}", "}", "reactor Print {", "    input x:int;", "    output z:int;", "    reaction(x) -> z {=", "    =}", "}"))
        Assertions.assertNotNull(model)
        ASTUtils.insertGeneratedDelays(model.eResource(), CGenerator(FileConfig(model.eResource(), Path.of("./a/"), True), DefaultErrorReporter()))
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model.eResource().getErrors())
        mainDef = None
        it = model.eResource().getAllContents()
        while it.hasNext():
            obj = it.next()
            if not (isinstance(obj, (Reactor))):
                continue 
            reactor = obj
            if reactor.isMain():
                mainDef = LfFactory.eINSTANCE.createInstantiation()
                mainDef.setName(reactor.__name__)
                mainDef.setReactorClass(reactor)
        mainInstance = ReactorInstance(toDefinition(mainDef.getReactorClass()), DefaultErrorReporter())
        for reactorInstance in mainInstance.children:
            if reactorInstance.isGeneratedDelay():
                for reactionInstance in reactorInstance.reactions:
                    Assertions.assertEquals(reactionInstance.assignLogicalExecutionTime(), TimeValue.ZERO)
            elif reactorInstance.__name__.contains("ramp"):
                for reactionInstance in reactorInstance.reactions:
                    Assertions.assertEquals(TimeValue(20, TimeUnit.MILLI), reactionInstance.assignLogicalExecutionTime())
            elif reactorInstance.__name__.contains("print"):
                for reactionInstance in reactorInstance.reactions:
                    Assertions.assertEquals(TimeValue.ZERO, reactionInstance.assignLogicalExecutionTime())
