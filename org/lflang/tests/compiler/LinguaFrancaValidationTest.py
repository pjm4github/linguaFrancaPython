#!/usr/bin/env python
""" generated source for module LinguaFrancaValidationTest """
#  Scoping unit tests. 
# 
# Copyright (c) 2019, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.tests.compiler
# import java.util.LinkedList
# import java.util.List
# import java.util.Map
# import org.eclipse.xtext.testing.InjectWith
# import org.eclipse.xtext.testing.extensions.InjectionExtension
# import org.eclipse.xtext.testing.util.ParseHelper
# import org.eclipse.xtext.testing.validation.ValidationTestHelper
# import org.eclipse.xtext.validation.Issue
from include.overloading import overloaded
# import org.junit.jupiter.api.Assertions
# import org.junit.jupiter.api.Test
# import org.junit.jupiter.api.extension.ExtendWith
# from org.lflang.Target

from org.lflang import TargetProperty

#from org.lflang.TargetProperty.ArrayType
#from org.lflang.TargetProperty.DictionaryElement
#from org.lflang.TargetProperty.DictionaryType
#from org.lflang.TargetProperty.PrimitiveType
#from org.lflang.TargetProperty.TargetPropertyType
#from org.lflang.TargetProperty.UnionType

from org.lflang import TimeValue
from org.lflang.lf import LfPackage
from org.lflang.lf import Model
from org.lflang.lf import Visibility
#from org.lflang.tests import LFInjectorProvider
from org.lflang.util import StringUtil
# import com.google.inject.Inject

@ExtendWith(InjectionExtension.__class__)
@InjectWith(LFInjectorProvider.__class__)
class LinguaFrancaValidationTest(object):
    """ generated source for class LinguaFrancaValidationTest """
    #  * Collection of unit tests to ensure validation is done correctly.
    #  * 
    #  * @author{Edward A. Lee <eal@berkeley.edu>}
    #  * @author{Marten Lohstroh <marten@berkeley.edu>}
    #  * @author{Matt Weber <matt.weber@berkeley.edu>}
    #  * @author(Christian Menard <christian.menard@tu-dresden.de>}
    #  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
    #  
    parser = None
    validator = None

    # Helper function to parse a Lingua Franca program and expect no errors.
    # @return A model representing the parsed string.
    #       
    def parseWithoutError(self, s):
        """ generated source for method parseWithoutError """
        model = self.parser.parse(s)
        Assertions.assertNotNull(model)
        Assertions.assertTrue(model.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model.eResource().getErrors())
        return model

    def parseWithError(self, s):
        """ generated source for method parseWithError """
        model = self.parser.parse(s)
        Assertions.assertNotNull(model)
        Assertions.assertFalse(model.eResource().getErrors().isEmpty())
        return model

    def duplicateVariable(self):
        """ generated source for method duplicateVariable """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor Foo {", "    logical action bar;", "    physical action bar;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAction(), None, "Duplicate Variable 'bar' in Reactor 'Foo'")

    def disallowReactorCalledPreamble(self):
        """ generated source for method disallowReactorCalledPreamble """
        model_no_errors = self.parser.parse(String.join(System.getProperty("line.separator"), "target Cpp;", "main reactor {", "}"))
        model_error_1 = self.parser.parse(String.join(System.getProperty("line.separator"), "target Cpp;", "main reactor Preamble {", "}"))
        model_error_2 = self.parser.parse(String.join(System.getProperty("line.separator"), "target Cpp;", "reactor Preamble {", "}", "main reactor Main {", "}"))
        Assertions.assertNotNull(model_no_errors)
        Assertions.assertNotNull(model_error_1)
        Assertions.assertNotNull(model_error_2)
        Assertions.assertTrue(model_no_errors.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model_no_errors.eResource().getErrors())
        Assertions.assertTrue(model_error_1.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model_error_1.eResource().getErrors())
        Assertions.assertTrue(model_error_2.eResource().getErrors().isEmpty(), "Encountered unexpected error while parsing: " + model_error_2.eResource().getErrors())
        self.validator.assertNoIssues(model_no_errors)
        self.validator.assertError(model_error_1, LfPackage.eINSTANCE.getReactor(), None, "Reactor cannot be named 'Preamble'")
        self.validator.assertError(model_error_2, LfPackage.eINSTANCE.getReactor(), None, "Reactor cannot be named 'Preamble'")

    def disallowUnderscoreInputs(self):
        """ generated source for method disallowUnderscoreInputs """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor {", "    input __bar;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInput(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __bar")

    def disallowMainWithDifferentNameThanFile(self):
        """ generated source for method disallowMainWithDifferentNameThanFile """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor Foo {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Name of main reactor must match the file name (or be omitted)")

    def disallowUnderscoreOutputs(self):
        """ generated source for method disallowUnderscoreOutputs """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor Foo {", "    output __bar;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getOutput(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __bar")

    def disallowUnderscoreActions(self):
        """ generated source for method disallowUnderscoreActions """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor Foo {", "    logical action __bar;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAction(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __bar")

    def disallowUnderscoreTimers(self):
        """ generated source for method disallowUnderscoreTimers """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor Foo {", "    timer __bar(0);", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getTimer(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __bar")

    def disallowUnderscoreParameters(self):
        """ generated source for method disallowUnderscoreParameters """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor Foo(__bar) {", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getParameter(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __bar")

    def disallowUnderscoreStates(self):
        """ generated source for method disallowUnderscoreStates """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor Foo {", "    state __bar;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getStateVar(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __bar")

    def disallowUnderscoreReactorDef(self):
        """ generated source for method disallowUnderscoreReactorDef """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "main reactor __Foo {", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __Foo")

    def disallowUnderscoreReactorInstantiation(self):
        """ generated source for method disallowUnderscoreReactorInstantiation """
        testCase = String.join(System.getProperty("line.separator"), "target TypeScript;", "reactor Foo {", "}", "main reactor Bar {", "   __x = new Foo();", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInstantiation(), None, "Names of objects (inputs, outputs, actions, timers, parameters, state, reactor definitions, and reactor instantiation) may not start with \"__\": __x")

    def connectionToEffectPort(self):
        """ generated source for method connectionToEffectPort """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor Foo {", "   output out:int;", "}", "main reactor Bar {", "   output out:int;", "   x = new Foo();", "   x.out -> out;", "   reaction(startup) -> out {=", "   =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getConnection(), None, "Cannot connect: Port named 'out' is already effect of a reaction.")

    def connectionToEffectPort2(self):
        """ generated source for method connectionToEffectPort2 """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor Foo {", "   input inp:int;", "   output out:int;", "}", "main reactor {", "   output out:int;", "   x = new Foo();", "   y = new Foo();", "", "   y.out -> x.inp;", "   reaction(startup) -> x.inp {=", "   =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getConnection(), None, "Cannot connect: Port named 'inp' is already effect of a reaction.")

    def connectionToEffectPort3(self):
        """ generated source for method connectionToEffectPort3 """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "", "reactor Foo {", "   input in:int;", "}", "reactor Bar {", "   input in:int;", "   x1 = new Foo();", "   x2 = new Foo();", "   in -> x1.in;", "   reaction(startup) -> x2.in {=", "   =}", "}")
        self.validator.assertNoErrors(self.parseWithoutError(testCase))

    def connectionToEffectPort3_5(self):
        """ generated source for method connectionToEffectPort3_5 """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "", "reactor Foo {", "   input in:int;", "}", "main reactor {", "   input in:int;", "   x1 = new Foo();", "   x2 = new Foo();", "   in -> x1.in;", "   reaction(startup) -> x2.in {=", "   =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getVariable(), None, "Main reactor cannot have inputs.")

    def connectionToEffectPort4(self):
        """ generated source for method connectionToEffectPort4 """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "", "reactor Foo {", "   input in:int;", "}", "main reactor {", "   input in:int;", "   x1 = new Foo();", "   in -> x1.in;", "   reaction(startup) -> x1.in {=", "   =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getConnection(), None, "Cannot connect: Port named 'in' is already effect of a reaction.")

    def multipleConnectionsToInputTest(self):
        """ generated source for method multipleConnectionsToInputTest """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor Source {", "   output out:int;", "}", "reactor Sink {", "   input in:int;", "}", "main reactor {", "   input in:int;", "   src = new Source();", "   sink = new Sink();", "   in -> sink.in;", "   src.out -> sink.in;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getConnection(), None, "Cannot connect: Port named 'in' may only appear once on the right side of a connection.")

    def detectInstantiationCycle(self):
        """ generated source for method detectInstantiationCycle """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor Contained {", "    x = new Contained();", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInstantiation(), None, "Instantiation is part of a cycle: Contained")

    def detectInstantiationCycle2(self):
        """ generated source for method detectInstantiationCycle2 """
        model = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Intermediate {", "   x = new Contained();", "}", "", "reactor Contained {", "   x = new Intermediate();", "}"))
        self.validator.assertError(model, LfPackage.eINSTANCE.getInstantiation(), None, "Instantiation is part of a cycle: Intermediate, Contained.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getInstantiation(), None, "Instantiation is part of a cycle: Intermediate, Contained.")

    def detectCausalityLoop(self):
        """ generated source for method detectCausalityLoop """
        model = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "", "reactor X {", "   input x:int;", "   output y:int;", "   reaction(x) -> y {=", "   =}", "}", "", "main reactor {", "   a = new X()", "   b = new X()", "   a.y -> b.x", "   b.y -> a.x", "}"))
        self.validator.assertError(model, LfPackage.eINSTANCE.getReaction(), None, "Reaction triggers involved in cyclic dependency in reactor X: x.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getReaction(), None, "Reaction effects involved in cyclic dependency in reactor X: y.")

    def afterBreaksCycle(self):
        """ generated source for method afterBreaksCycle """
        testCase = String.join(System.getProperty("line.separator"), "target C", "            ", "reactor X {", "    input x:int;", "    output y:int;", "    reaction(x) -> y {=", "    =}", "}", "", "main reactor {", "    a = new X()", "    b = new X()", "    a.y -> b.x after 5 msec", "    b.y -> a.x", "}")
        self.validator.assertNoErrors(self.parseWithoutError(testCase))

    def afterBreaksCycle2(self):
        """ generated source for method afterBreaksCycle2 """
        testCase = String.join(System.getProperty("line.separator"), "target C", "            ", "reactor X {", "    input x:int;", "    output y:int;", "    reaction(x) -> y {=", "    =}", "}", "", "main reactor {", "    a = new X()", "    b = new X()", "    a.y -> b.x after 0 sec", "    b.y -> a.x", "}")
        self.validator.assertNoErrors(self.parseWithoutError(testCase))

    def afterBreaksCycle3(self):
        """ generated source for method afterBreaksCycle3 """
        testCase = String.join(System.getProperty("line.separator"), "target C", "            ", "reactor X {", "    input x:int;", "    output y:int;", "    reaction(x) -> y {=", "    =}", "}", "", "main reactor {", "    a = new X()", "    b = new X()", "    a.y -> b.x after 0", "    b.y -> a.x", "}")
        self.validator.assertNoErrors(self.parseWithoutError(testCase))

    def nonzeroAfterMustHaveUnits(self):
        """ generated source for method nonzeroAfterMustHaveUnits """
        testCase = String.join(System.getProperty("line.separator"), "target C", "            ", "reactor X {", "    input x:int;", "    output y:int;", "    reaction(x) -> y {=", "    =}", "}", "", "main reactor {", "    a = new X()", "    b = new X()", "    a.y -> b.x after 1", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getConnection(), None, "Missing time unit.")

    def nonZeroTimeValueWithoutUnits(self):
        """ generated source for method nonZeroTimeValueWithoutUnits """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    timer t(42, 1 sec);", "    reaction(t) {=", "        printf(\"Hello World.\\n\");", "    =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getTimer(), None, "Missing time unit.")

    def parameterTypeMismatch(self):
        """ generated source for method parameterTypeMismatch """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor (p:int(0)) {", "    timer t(p, 1 sec);", "    reaction(t) {=", "        printf(\"Hello World.\\n\");", "    =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getTimer(), None, "Parameter is not of time type.")

    def targetCodeInTimeArgument(self):
        """ generated source for method targetCodeInTimeArgument """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    timer t({=foo()=}, 1 sec);", "    reaction(t) {=", "        printf(\"Hello World.\\n\");", "    =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getTimer(), None, "Invalid time literal.")

    def overflowingDeadlineC(self):
        """ generated source for method overflowingDeadlineC """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "timer t;", "    reaction(t) {=", "        printf(\"Hello World.\\n\");", "    =} deadline (40 hours) {=", "    =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getDeadline(), None, "Deadline exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.")

    def overflowingParameterC(self):
        """ generated source for method overflowingParameterC """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor(d:time(40 hours)) {", "timer t;", "    reaction(t) {=", "        printf(\"Hello World.\\n\");", "    =} deadline (d) {=", "    =}", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getParameter(), None, "Time value used to specify a deadline exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.")

    def overflowingAssignmentC(self):
        """ generated source for method overflowingAssignmentC """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor Print(d:time(39 hours)) {", "    timer t;", "    reaction(t) {=", "        printf(\"Hello World.\\n\");", "    =} deadline (d) {=", "    =}", "}", "main reactor {", "    p = new Print(d=40 hours);", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAssignment(), None, "Time value used to specify a deadline exceeds the maximum of " + TimeValue.MAX_LONG_DEADLINE + " nanoseconds.")

    def missingTrigger(self):
        """ generated source for method missingTrigger """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor X {", "    reaction() {=", "        //", "    =}", "}")
        self.validator.assertWarning(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReaction(), None, "Reaction has no trigger.")

    def testPreambleVisibility(self):
        """ generated source for method testPreambleVisibility """
        for target in Target.values():
            for visibility in Visibility.values():
                model_reactor_scope = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target {:s};".format(target), "reactor Foo {", "    {:s}preamble {==}".format(visibility + " " if visibility != Visibility.NONE else ""), "}"))
                model_file_scope = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target {:s};".format(target), "    {:s}preamble {==}".format(visibility + " " if visibility != Visibility.NONE else ""), "reactor Foo {", "}"))
                model_no_preamble = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target {:s};".format(target), "reactor Foo {", "}"))
                self.validator.assertNoIssues(model_no_preamble)
                if target == Target.CPP:
                    if visibility == Visibility.NONE:
                        self.validator.assertError(model_file_scope, LfPackage.eINSTANCE.getPreamble(), None, "Preambles for the C++ target need a visibility qualifier (private or public)!")
                        self.validator.assertError(model_reactor_scope, LfPackage.eINSTANCE.getPreamble(), None, "Preambles for the C++ target need a visibility qualifier (private or public)!")
                    else:
                        self.validator.assertNoIssues(model_file_scope)
                        self.validator.assertNoIssues(model_reactor_scope)
                else:
                    if visibility == Visibility.NONE:
                        self.validator.assertNoIssues(model_file_scope)
                        self.validator.assertNoIssues(model_reactor_scope)
                    else:
                        self.validator.assertWarning(model_file_scope, LfPackage.eINSTANCE.getPreamble(), None, "The {:s} qualifier has no meaning for the {:s} target. It should be removed.".format(visibility, target.name()))
                        self.validator.assertWarning(model_reactor_scope, LfPackage.eINSTANCE.getPreamble(), None, "The {:s} qualifier has no meaning for the {:s} target. It should be removed.".format(visibility, target.name()))

    def stateAndParameterDeclarationsInC(self):
        """ generated source for method stateAndParameterDeclarationsInC """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor Bar(a(0),              // ERROR: type missing", "            b:int,             // ERROR: uninitialized", "            t:time(42),        // ERROR: units missing", "            x:int(0),", "            h:time(\"bla\"),   // ERROR: not a type ", "            q:time(1 msec, 2 msec),  // ERROR: not a list", "            y:int(t)           // ERROR: init using parameter", ") {", "    state offset:time(42);     // ERROR: units missing", "    state w:time(x);           // ERROR: parameter is not a time", "    state foo:time(\"bla\");   // ERROR: assigned value not a time", "    timer tick(1);             // ERROR: not a time", "}")
        model = self.parseWithoutError(testCase)
        self.validator.assertError(model, LfPackage.eINSTANCE.getParameter(), None, "Type declaration missing.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getParameter(), None, "Missing time unit.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getParameter(), None, "Invalid time literal.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getParameter(), None, "Time parameter cannot be initialized using a list.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getParameter(), None, "Parameter cannot be initialized using parameter.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getStateVar(), None, "Missing time unit.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getStateVar(), None, "Parameter is not of time type.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getStateVar(), None, "Invalid time literal.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getParameter(), None, "Uninitialized parameter.")
        self.validator.assertError(model, LfPackage.eINSTANCE.getTimer(), None, "Missing time unit.")

    def recognizeIPV4(self):
        """ generated source for method recognizeIPV4 """
        correct = list("127.0.0.1", "10.0.0.1", "192.168.1.1", "0.0.0.0", "192.168.1.1")
        parseError = list("10002.3.4", "1.2.3.4.5")
        validationError = list("256.0.0.0", "260.0.0.0")
        for addr in correct:
            self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at foo@{:s}:4242 {".format(addr), "    y = new Y() at {:s}:2424; ".format(addr), "}"))
        for addr in parseError:
            self.parseWithError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at foo@{:s}:4242 {".format(addr), "    y = new Y() at {:s}:2424; ".format(addr), "}"))
        for addr in validationError:
            model = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at foo@{:s}:4242 {".format(addr), "    y = new Y() at {:s}:2424; ".format(addr), "}"))
            self.validator.assertWarning(model, LfPackage.eINSTANCE.getHost(), None, "Invalid IP address.")

    def recognizeIPV6(self):
        """ generated source for method recognizeIPV6 """
        correct = list("1:2:3:4:5:6:7:8", "1:2:3:4:5:6:7::", "1:2:3:4:5:6::8", "1:2:3:4:5::8", "1:2:3:4::8", "1:2:3::8", "1:2::8", "1::8", "::8", "::", "1::3:4:5:6:7:8", "1::4:5:6:7:8", "1::5:6:7:8", "1::6:7:8", "1::7:8", "1::8", "1::", "1:2:3:4:5::7:8", "1:2:3:4::6:7:8", "1:2:3::5:6:7:8", "1:2::4:5:6:7:8", "1::3:4:5:6:7:8", "::2:3:4:5:6:7:8", "fe80::7:8", "fe80::7:8%eth0", "fe80::7:8%1", "::255.255.255.255", "::ffff:255.255.255.255", "::ffff:0:255.255.255.0", "::ffff:00:255.255.255.0", "::ffff:000:255.255.255.0", "::ffff:0000:255.255.255.0", "::ffff:0.0.0.0", "::ffff:1.2.3.4", "::ffff:10.0.0.1", "1:2:3:4:5:6:77:88", "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", "2001:db8:3:4::192.0.2.33", "64:ff9b::192.0.2.33", "0:0:0:0:0:0:10.0.0.1")
        validationError = list("1:2:3:4:5:6:7:8:9", "1:2:3:4:5:6::7:8", "1:2:3:4:5:6:7:8:", "::1:2:3:4:5:6:7:8", "1:2:3:4:5:6:7:8::", "1:2:3:4:5:6:7:88888", "2001:db8:3:4:5::192.0.2.33", "fe08::7:8interface", "fe08::7:8interface", "fe08::7:8i")
        parseError = list("fe08::7:8%", ":1:2:3:4:5:6:7:8")
        for addr in correct:
            model = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor at [foo@{:s}]:4242 {".format(addr), "    y = new Y() at [{:s}]:2424; ".format(addr), "}"))
            self.validator.assertNoIssues(model)
        for addr in parseError:
            self.parseWithError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at [foo@{:s}]:4242 {".format(addr), "    y = new Y() at [{:s}]:2424; ".format(addr), "}"))
        for addr in validationError:
            model = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at [foo@{:s}]:4242 {".format(addr), "    y = new Y() at [{:s}]:2424; ".format(addr), "}"))
            self.validator.assertWarning(model, LfPackage.eINSTANCE.getHost(), None, "Invalid IP address.")

    def recognizeHostNames(self):
        """ generated source for method recognizeHostNames """
        correct = list("localhost")
        validationError = list("x.y.z")
        parseError = list("..xyz")
        for addr in correct:
            self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at foo@{:s}:4242 {".format(addr), "    y = new Y() at {:s}:2424; ".format(addr), "}"))
        for addr in parseError:
            self.parseWithError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at foo@{:s}:4242 {".format(addr), "    y = new Y() at {:s}:2424; ".format(addr), "}"))
        for addr in validationError:
            model = self.parseWithoutError(String.join(System.getProperty("line.separator"), "target C;", "reactor Y {}", "federated reactor X at foo@{:s}:4242 {".format(addr), "    y = new Y() at {:s}:2424; ".format(addr), "}"))
            self.validator.assertWarning(model, LfPackage.eINSTANCE.getHost(), None, "Invalid host name or fully qualified domain name.")

    primitiveTypeToKnownGood = Map.of(PrimitiveType.BOOLEAN, list("true", "\"true\"", "false", "\"false\""), PrimitiveType.INTEGER, list("0", "1", "\"42\"", "\"-1\"", "-2"), PrimitiveType.NON_NEGATIVE_INTEGER, list("0", "1", "42"), PrimitiveType.TIME_VALUE, list("1 msec", "2 sec"), PrimitiveType.STRING, list("1", "\"foo\"", "bar"), PrimitiveType.FILE, list("valid.file", "something.json", "\"foobar.proto\""))
    primitiveTypeToKnownBad = Map.of(PrimitiveType.BOOLEAN, list("1 sec", "foo", "\"foo\"", "[1]", "{baz: 42}", "'c'"), PrimitiveType.INTEGER, list("foo", "\"bar\"", "1 sec", "[1, 2]", "{foo: \"bar\"}", "'c'"), PrimitiveType.NON_NEGATIVE_INTEGER, list("-42", "foo", "\"bar\"", "1 sec", "[1, 2]", "{foo: \"bar\"}", "'c'"), PrimitiveType.TIME_VALUE, list("foo", "\"bar\"", "\"3 sec\"", "\"4 weeks\"", "[1, 2]", "{foo: \"bar\"}", "'c'"), PrimitiveType.STRING, list("1 msec", "[1, 2]", "{foo: \"bar\"}", "'c'"))
    compositeTypeToKnownBad = Map.of(ArrayType.STRING_ARRAY, list(list("[1 msec]", "[0]", PrimitiveType.STRING), list("[foo, {bar: baz}]", "[1]", PrimitiveType.STRING), list("{bar: baz}", "", ArrayType.STRING_ARRAY)), UnionType.STRING_OR_STRING_ARRAY, list(list("[1 msec]", "[0]", PrimitiveType.STRING), list("[foo, {bar: baz}]", "[1]", PrimitiveType.STRING), list("{bar: baz}", "", UnionType.STRING_OR_STRING_ARRAY)), UnionType.FILE_OR_FILE_ARRAY, list(list("[1 msec]", "[0]", PrimitiveType.FILE), list("[foo, {bar: baz}]", "[1]", PrimitiveType.FILE), list("{bar: baz}", "", UnionType.FILE_OR_FILE_ARRAY)), UnionType.DOCKER_UNION, list(list("foo", "", UnionType.DOCKER_UNION), list("[1]", "", UnionType.DOCKER_UNION), list("{bar: baz}", "", DictionaryType.DOCKER_DICT), list("{FROM: [1, 2, 3]}", ".FROM", PrimitiveType.STRING)), UnionType.TRACING_UNION, list(list("foo", "", UnionType.TRACING_UNION), list("[1]", "", UnionType.TRACING_UNION), list("{bar: baz}", "", DictionaryType.TRACING_DICT), list("{trace-file-name: [1, 2, 3]}", ".trace-file-name", PrimitiveType.STRING)))

    @overloaded
    def synthesizeExamples(self, type, correct):
        """ generated source for method synthesizeExamples """
        values = self.primitiveTypeToKnownGood if correct else self.primitiveTypeToKnownBad
        examples = LinkedList()
        if correct:
            entries = values.get(type.type)
            if not (entries == None or entries.isEmpty()):
                examples.append("[{:s}]".format(", ".join( entries)))
        return examples

    @synthesizeExamples.register(object, UnionType, bool)
    def synthesizeExamples_0(self, type, correct):
        """ generated source for method synthesizeExamples_0 """
        examples = LinkedList()
        if correct:
            for it in type.options:
                if isinstance(it, (TargetPropertyType)):
                    for ex in synthesizeExamples(it, correct):
                        examples.append(ex)
                else:
                    examples.append(it.__str__())
        else:
            pass
        return examples

    @synthesizeExamples.register(object, DictionaryType, bool)
    def synthesizeExamples_1(self, type, correct):
        """ generated source for method synthesizeExamples_1 """
        examples = LinkedList()
        for option in type.options:
            for it in synthesizeExamples(option.getType(), correct):
                correct_test = "iamwrong: " if not correct else ": "
                s = "{" + option + correct_test + it + "}"
        return examples

    @synthesizeExamples.register(object, TargetPropertyType, bool)
    def synthesizeExamples_2(self, type, correct):
        """ generated source for method synthesizeExamples_2 """
        if isinstance(type, (PrimitiveType)):
            values = self.primitiveTypeToKnownGood if correct else self.primitiveTypeToKnownBad
            examples = values.get(type)
            Assertions.assertNotNull(examples)
            return examples
        else:
            if isinstance(type, (UnionType)):
                return self.synthesizeExamples(type, correct)
            elif isinstance(type, (ArrayType)):
                return self.synthesizeExamples(type, correct)
            elif isinstance(type, (DictionaryType)):
                return self.synthesizeExamples(type, correct)
            else:
                Assertions.fail("Encountered an unknown type: " + type)
        return LinkedList()

    def createModel(self, key, value):
        """ generated source for method createModel """
        target = key.supportedBy.get(0).getDisplayName()
        print("{:s}: {:s}".format(key, value))
        return self.parseWithoutError(String.join(System.getProperty("line.separator"), "target {:s} {{:s}: {:s}};".format(target, key, value), "reactor Y {}", "main reactor {", "    y = new Y() ", "}"))

    def checkTargetProperties(self):
        """ generated source for method checkTargetProperties """
        for prop in TargetProperty.getOptions():
            if prop == TargetProperty.CARGO_DEPENDENCIES:
                return
            print("Testing target property {:s} which is {:s}".format(prop, prop.type))
            print("====")
            print("Known good assignments:")
            knownCorrect = self.synthesizeExamples(prop.type, True)
            for it in knownCorrect:
                model = self.createModel(prop, it)
                self.validator.assertNoErrors(model)
                if prop.type == PrimitiveType.FILE:
                    self.validator.assertWarning(model, LfPackage.eINSTANCE.getKeyValuePair(), None, "Could not find file: '{:s}'.".format(StringUtil.removeQuotes(it)))
            print("Known bad assignments:")
            knownIncorrect = self.synthesizeExamples(prop.type, False)
            if not (knownIncorrect == None or knownIncorrect.isEmpty()):
                for it in knownIncorrect:
                    self.validator.assertError(self.createModel(prop, it), LfPackage.eINSTANCE.getKeyValuePair(), None, "Target property '{:s}' is required to be {:s}.".format(prop.__str__(), prop.type))
            else:
                list = self.compositeTypeToKnownBad.get(prop.type)
                if list == None:
                    print("No known incorrect values provided for target property '{:s}'. Aborting test.".format(prop))
                    Assertions.assertTrue(False)
                else:
                    for it in list:
                        self.validator.assertError(self.createModel(prop, it.get(0).__str__()), LfPackage.eINSTANCE.getKeyValuePair(), None, "Target property '{:s}{:s}' is required to be {:s}.".format(prop.__str__(), it.get(1), it.get(2)))
            print("====")
        print("Done!")

    def checkCargoDependencyProperty(self):
        """ generated source for method checkCargoDependencyProperty """
        prop = TargetProperty.CARGO_DEPENDENCIES
        knownCorrect = list("{}", "{ dep: \"8.2\" }", "{ dep: { version: \"8.2\"} }", "{ dep: { version: \"8.2\", features: [\"foo\"]} }")
        for it in knownCorrect:
            self.validator.assertNoErrors(self.createModel(prop, it))
        self.validator.assertError(self.createModel(prop, "{ dep: {/*empty*/} }"), LfPackage.eINSTANCE.getKeyValuePairs(), None, "Must specify one of 'version', 'path', or 'git'")
        self.validator.assertError(self.createModel(prop, "{ dep: { unknown_key: \"\"} }"), LfPackage.eINSTANCE.getKeyValuePair(), None, "Unknown key: 'unknown_key'")
        self.validator.assertError(self.createModel(prop, "{ dep: { features: \"\" } }"), LfPackage.eINSTANCE.getElement(), None, "Expected an array of strings for key 'features'")

    def testImportedCyclicReactor(self):
        """ generated source for method testImportedCyclicReactor """

    def testUnusedImport(self):
        """ generated source for method testUnusedImport """

    def testMissingInputType(self):
        """ generated source for method testMissingInputType """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    input i;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInput(), None, "Input must have a type.")

    def testMissingOutputType(self):
        """ generated source for method testMissingOutputType """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    output i;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getOutput(), None, "Output must have a type.")

    def testMissingStateType(self):
        """ generated source for method testMissingStateType """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    state i;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getStateVar(), None, "State must have a type.")

    def testListWithParam(self):
        """ generated source for method testListWithParam """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor (A:int(1)) { state i:int(A, 2, 3) }")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getStateVar(), None, "List items cannot refer to a parameter.")

    def testCppMutableInput(self):
        """ generated source for method testCppMutableInput """
        testCase = String.join(System.getProperty("line.separator"), "target Cpp;", "main reactor {", "    mutable input i:int;", "}")
        self.validator.assertWarning(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInput(), None, "The mutable qualifier has no meaning for the C++ target and should be removed. " + "In C++, any value can be made mutable by calling get_mutable_copy().")

    def testOverflowingSTP(self):
        """ generated source for method testOverflowingSTP """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    reaction(startup) {==} STP(2147483648) {==}", "}")

    def testOverflowingDeadline(self):
        """ generated source for method testOverflowingDeadline """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    reaction(startup) {==} deadline(2147483648) {==}", "}")

    def testInvalidTargetParam(self):
        """ generated source for method testInvalidTargetParam """
        testCase = String.join(System.getProperty("line.separator"), "target C { beefyDesktop: true }", "main reactor {}")
        issues = self.validator.validate(self.parseWithoutError(testCase))
        Assertions.assertTrue(len(issues) == 1 and issues.get(0).getMessage().contains("Unrecognized target parameter: beefyDesktop"))

    def testTargetParamNotSupportedForTarget(self):
        """ generated source for method testTargetParamNotSupportedForTarget """
        testCase = String.join(System.getProperty("line.separator"), "target Python { build: \"\" }", "main reactor {}")
        issues = self.validator.validate(self.parseWithoutError(testCase))
        Assertions.assertTrue(len(issues) == 1 and issues.get(0).getMessage().contains("The target parameter: build" + " is not supported by the Python target and will thus be ignored."))

    def testUnnamedReactor(self):
        """ generated source for method testUnnamedReactor """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "reactor {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Reactor must be named.")

    def testMainHasInput(self):
        """ generated source for method testMainHasInput """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    input x:int;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInput(), None, "Main reactor cannot have inputs.")

    def testFederatedHasInput(self):
        """ generated source for method testFederatedHasInput """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "federated reactor {", "    input x:int;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInput(), None, "Main reactor cannot have inputs.")

    def testMainHasOutput(self):
        """ generated source for method testMainHasOutput """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {", "    output x:int;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getOutput(), None, "Main reactor cannot have outputs.")

    def testFederatedHasOutput(self):
        """ generated source for method testFederatedHasOutput """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "federated reactor {", "    output x:int;", "}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getOutput(), None, "Main reactor cannot have outputs.")

    def testMultipleMainReactor(self):
        """ generated source for method testMultipleMainReactor """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor A {}", "main reactor A {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Multiple definitions of main or federated reactor.")

    def testMultipleMainReactorUnnamed(self):
        """ generated source for method testMultipleMainReactorUnnamed """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor {}", "main reactor {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Multiple definitions of main or federated reactor.")

    def testMultipleFederatedReactor(self):
        """ generated source for method testMultipleFederatedReactor """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "federated reactor A {}", "federated reactor A {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Multiple definitions of main or federated reactor.")

    def testMultipleMainOrFederatedReactor(self):
        """ generated source for method testMultipleMainOrFederatedReactor """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor A {}", "federated reactor A {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Multiple definitions of main or federated reactor.")

    def testMainReactorHasHost(self):
        """ generated source for method testMainReactorHasHost """
        testCase = String.join(System.getProperty("line.separator"), "target C;", "main reactor at 127.0.0.1{}")

    def testUnrecognizedTarget(self):
        """ generated source for method testUnrecognizedTarget """
        testCase = String.join(System.getProperty("line.separator"), "target Pjthon;", "main reactor {}")
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getTargetDecl(), None, "Unrecognized target: Pjthon")

    def testWrongStructureForLabelAttribute(self):
        """ generated source for method testWrongStructureForLabelAttribute """
        testCase = "\n                target C;\n                @label(name=\"something\")\n                main reactor { }\n            "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAttribute(), None, "Unknown attribute parameter.")

    def testMissingName(self):
        """ generated source for method testMissingName """
        testCase = "\n                target C;\n                @label(\"something\", \"else\")\n                main reactor { }            "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAttribute(), None, "Missing name for attribute parameter.")

    def testWrongParamType(self):
        """ generated source for method testWrongParamType """
        testCase = "\n                target C;\n                @label(value=1)\n                main reactor { }\n            "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAttribute(), None, "Incorrect type: \"value\" should have type String.")

    def testInitialMode(self):
        """ generated source for method testInitialMode """
        testCase = "\n            target C;\n            main reactor {\n                mode M {}\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "Every modal reactor requires one initial mode.")

    def testInitialModes(self):
        """ generated source for method testInitialModes """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM1 {}\n                initial mode IM2 {}\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReactor(), None, "A modal reactor can only have one initial mode.")

    def testModeStateNamespace(self):
        """ generated source for method testModeStateNamespace """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM {\n                    state s:int;\n                }\n                mode M {\n                    state s:int;\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getStateVar(), None, "Duplicate state variable 's'. (State variables are currently scoped on reactor level not modes)")

    def testModeTimerNamespace(self):
        """ generated source for method testModeTimerNamespace """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM {\n                    timer t;\n                }\n                mode M {\n                    timer t;\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getTimer(), None, "Duplicate Timer 't'. (Timers are currently scoped on reactor level not modes)")

    def testModeActionNamespace(self):
        """ generated source for method testModeActionNamespace """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM {\n                    logical action a;\n                }\n                mode M {\n                    logical action a;\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getAction(), None, "Duplicate Action 'a'. (Actions are currently scoped on reactor level not modes)")

    def testModeInstanceNamespace(self):
        """ generated source for method testModeInstanceNamespace """
        testCase = "\n            target C;\n            reactor R {}\n            main reactor {\n                initial mode IM {\n                    r = new R();\n                }\n                mode M {\n                    r = new R();\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getInstantiation(), None, "Duplicate Instantiation 'r'. (Instantiations are currently scoped on reactor level not modes)")

    def testMissingModeStateReset(self):
        """ generated source for method testMissingModeStateReset """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM {\n                    reaction(startup) -> M {==}\n                }\n                mode M {\n                    state s:int(0);\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getMode(), None, "State variable is not reset upon mode entry. It is neither marked for automatic reset nor is there a reset reaction.")

    def testMissingModeStateResetInstance(self):
        """ generated source for method testMissingModeStateResetInstance """
        testCase = "\n            target C;\n            reactor R {\n                state s:int(0);\n            }\n            main reactor {\n                initial mode IM {\n                    reaction(startup) -> M {==}\n                }\n                mode M {\n                    r = new R();\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getMode(), None, "This reactor contains state variables that are not reset upon mode entry: " + "s in R" + ".\nThe state variables are neither marked for automatic reset nor have a dedicated reset reaction. " + "It is usafe to instatiate this reactor inside a mode entered with reset.")

    def testModeStateResetWithoutInitialValue(self):
        """ generated source for method testModeStateResetWithoutInitialValue """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM {\n                    reset state s:int;\n                }\n            }\n        "
        self.validator.assertError(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getStateVar(), None, "The state variable can not be automatically reset without an initial value.")

    def testUnspecifiedTransitionType(self):
        """ generated source for method testUnspecifiedTransitionType """
        testCase = "\n            target C;\n            main reactor {\n                initial mode IM {\n                    reaction(startup) -> M {==}\n                }\n                mode M {\n                    reset state s:int(0);\n                }\n            }\n        "
        self.validator.assertWarning(self.parseWithoutError(testCase), LfPackage.eINSTANCE.getReaction(), None, "You should specifiy a transition type! " + "Reset and history transitions have different effects on this target mode. " + "Currently, a reset type is implicitly assumed.")
