#!/usr/bin/env python
""" generated source for module ShowCycleAction """
# 
# Copyright (c) 2020, Kiel University.
# *
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# *
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# *
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# *
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
# package: org.lflang.diagram.synthesis.action
# import de.cau.cs.kieler.klighd.IAction
# import de.cau.cs.kieler.klighd.ViewContext
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.util.ModelingUtil
# import java.util.Iterator
# import java.util.LinkedList
# import java.util.Set
# import org.eclipse.xtext.xbase.lib.IteratorExtensions
from lflang.diagram.synthesis.action.CollapseAllReactorsAction import CollapseAllReactorsAction
from lflang.diagram.synthesis.action.FilterCycleAction import KNode
from org.lflang.diagram.synthesis.util import CycleVisualization

from org.lflang.diagram.synthesis.util import NamedInstanceUtil

# 
#  * Action that expands all reactor nodes that are included in a cycle.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class ModelingUtil:
    pass


class AbstractAction:
    pass


class MemorizingExpandCollapseAction:
    pass


class IAction:
    pass


class ShowCycleAction(AbstractAction):
    """ generated source for class ShowCycleAction """
    ID = "org.lflang.diagram.synthesis.action.ShowCycleAction"
    collapseAll = CollapseAllReactorsAction()

    def execute(self, context):
        """ generated source for method execute """
        vc = context.getViewContext()
        #  Collapse all
        self.collapseAll.execute(context)
        #  Expand only errors
        knodes = ModelingUtil.eAllContentsOfType(vc.getViewModel(), KNode.__class__)
        #  Filter out nodes that are not in cycle or not a reactor
        #          knodes = IteratorExtensions.filter(knodes, it -> {
        #              return it.getProperty(CycleVisualization.DEPENDENCY_CYCLE) && sourceIsReactor(it);
        #          });
        #  Remove duplicates
        cycleNodes = set(knodes)
        #  Include parents
        check = list(cycleNodes)
        while not check.isEmpty():
            parent = check.pop().getParent()
            if parent != None and not cycleNodes.intersection(parent):
                cycleNodes.append(parent)
                check.append(parent)
        #  Expand
        for node in cycleNodes:
            MemorizingExpandCollapseAction.setExpansionState(node, NamedInstanceUtil.getLinkedInstance(node), vc.getViewer(), True)
        return IAction.ActionResult.createResult(True)
