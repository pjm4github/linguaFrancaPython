#!/usr/bin/env python
""" generated source for module ModelInfo """
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
# package: org.lflang
import 

import 
# import java.util.HashSet
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Set

#  * A helper class for analyzing the AST. This class is instantiated once for each compilation.
#  * <p>
#  * NOTE: the validator used on imported files uses the same instance! Hence, this class should not contain any info
#  * specific to any particular resource that is involved in the compilation.
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class ModelInfo(object):
    """ generated source for class ModelInfo """
    #      * Data structure for tracking dependencies between reactor classes. An
    #      * instantiation of class A inside of class B implies that B depends on A.
    #      
    instantiationGraph = None

    #      * The AST that the info gathered in this class pertains to.
    #      
    model = None

    #      * The set of assignments that assign a too-large constant to a parameter
    #      * that is used to specify a deadline. These assignments are to be reported
    #      * during validation.
    #      
    overflowingAssignments = None

    #      * The set of deadlines that use a too-large constant to specify their time
    #      * interval.
    #      
    overflowingDeadlines = None

    #      * The set of STP offsets that use a too-large constant to specify their time
    #      * interval.
    #      
    overflowingSTP = None

    #      * The set of parameters used to specify a deadline while having been
    #      * assigned a default value the is too large for this purpose. These
    #      * parameters are to be reported during validation.
    #      
    overflowingParameters = None

    #  Cycles found during topology analysis. 
    topologyCycles = {}

    #      * Whether or not the model information has been updated at least once.
    #      
    updated = bool()

    #      * Redo all analysis based on the given model.
    #      *
    #      * @param model the model to analyze.
    #      
    def update(self, model, reporter):
        """ generated source for method update """
        self.updated = True
        self.model = model
        self.instantiationGraph = InstantiationGraph(model, True)
        if self.instantiationGraph.getCycles().size() == 0:
            topLevelReactorInstances = LinkedList()
            main = model.getReactors().stream().filter(it.isMain() or it.isFederated()).findFirst()
            if main.isPresent():
                inst = ReactorInstance(main.get(), reporter)
                topLevelReactorInstances.append(inst)
            else:
                pass
            for top in topLevelReactorInstances:
                self.topologyCycles.extend(top.getCycles())
        target = Target.forName(model.getTarget().__name__).orElse(None)
        if target == Target.C:
            self.collectOverflowingNodes()

    def topologyCycles(self):
        """ generated source for method topologyCycles """
        return self.topologyCycles

    def collectOverflowingNodes(self):
        """ generated source for method collectOverflowingNodes """
        self.overflowingAssignments = set()
        self.overflowingDeadlines = set()
        self.overflowingParameters = set()
        self.overflowingSTP = set()
        for deadline in filter(toIterable(model.eAllContents()), Deadline.__class__):
            if isTooLarge(ASTUtils.getLiteralTimeValue(deadline.getDelay())):
                self.overflowingDeadlines.append(deadline)
            delay = deadline.getDelay()
            if isinstance(delay, (ParameterReference)) and detectOverflow(HashSet(), (deadline.getDelay()).getParameter()):
                self.overflowingDeadlines.append(deadline)
        for stp in filter(toIterable(model.eAllContents()), STP.__class__):
            if isTooLarge(ASTUtils.getLiteralTimeValue(stp.getValue())):
                self.overflowingSTP.append(stp)

    def isTooLarge(self, time):
        """ generated source for method isTooLarge """
        return time != None and time.toNanoSeconds() > TimeValue.MAX_LONG_DEADLINE

    def detectOverflow(self, visited, current):
        """ generated source for method detectOverflow """
        overflow = False
        if self.isTooLarge(ASTUtils.getDefaultAsTimeValue(current)):
            self.overflowingParameters.append(current)
            overflow = True
        instantiations = self.instantiationGraph.getInstantiations(current.eContainer())
        for instantiation in instantiations:
            if not visited.contains(instantiation):
                visited.append(instantiation)
                for assignment in instantiation.getParameters():
                    if assignment.getLhs() == current:
                        if assignment.getRhs().isEmpty():
                            continue 
                        expr = assignment.getRhs().get(0)
                        if isinstance(expr, (ParameterReference)):
                            overflow = self.detectOverflow(visited, (expr).getParameter()) or overflow
                        else:
                            if self.isTooLarge(ASTUtils.getLiteralTimeValue(assignment.getRhs().get(0))):
                                self.overflowingAssignments.append(assignment)
                                overflow = True
        return overflow
