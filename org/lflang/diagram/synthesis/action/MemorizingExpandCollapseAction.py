#!/usr/bin/env python
""" generated source for module MemorizingExpandCollapseAction """
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
# import java.util.WeakHashMap
from lflang.diagram.synthesis.action.AbstractAction import AbstractAction, IAction
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import SynthesisOption
from org.lflang.diagram.synthesis.util import InterfaceDependenciesVisualization

from org.lflang.diagram.synthesis.util import NamedInstanceUtil

from org.lflang.generator import NamedInstance

from org.lflang.generator import ReactorInstance
# import com.google.common.base.Preconditions
# import de.cau.cs.kieler.klighd.IAction
# import de.cau.cs.kieler.klighd.IViewer
# import de.cau.cs.kieler.klighd.SynthesisOption
# import de.cau.cs.kieler.klighd.ViewContext
# import de.cau.cs.kieler.klighd.kgraph.KNode

# 
#  * Action for toggling collapse/expand state of reactors that memorizes the state and
#  * allows correct initialization synthesis runs for the same model.
#  * Prevents automatic collapsing of manually expanded nodes.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class Preconditions:
    pass


class MemorizingExpandCollapseAction(AbstractAction):
    """ generated source for class MemorizingExpandCollapseAction """
    ID = "org.lflang.diagram.synthesis.action.MemorizingExpandCollapseAction"

    #      * The related synthesis option
    #      
    MEMORIZE_EXPANSION_STATES = SynthesisOption.createCheckOption("Remember Collapsed/Expanded Reactors", True)

    #      * Memory-leak-free cache of expansion states
    #      
    EXPANSION_STATES = {}

    #      * Sets the expansion state of a node and saves it for future synthesis.
    #      
    @classmethod
    def setExpansionState(cls, node, memorizableObj, viewer, expand):
        """ generated source for method setExpansionState """
        Preconditions.checkNotNull(node)
        #  Store new state if activated
        if (bool(viewer.getViewContext().getOptionValue(cls.MEMORIZE_EXPANSION_STATES))) and memorizableObj != None:
            if isinstance(memorizableObj, (NamedInstance)):
                cls.EXPANSION_STATES.put((memorizableObj).uniqueID(), expand)
            else:
                cls.EXPANSION_STATES.put(memorizableObj, expand)
        #  Apply state
        if expand:
            viewer.expand(node)
        else:
            viewer.collapse(node)
        #  Handle edges that should only appear for one of the renderings
        InterfaceDependenciesVisualization.updateInterfaceDependencyVisibility(node, expand)

    #      * @return the memorized expansion state of the given model element or null if not memorized
    #      
    @classmethod
    def getExpansionState(cls, obj):
        """ generated source for method getExpansionState """
        if isinstance(obj, (NamedInstance)):
            return cls.EXPANSION_STATES.get((obj).uniqueID())
        return cls.EXPANSION_STATES.get(obj)

    # -----------------------------------------------------------------------------------------------------------------
    def execute(self, context):
        """ generated source for method execute """
        vc = context.getViewContext()
        v = vc.getViewer()
        node = context.getKNode()
        linkedInstance = NamedInstanceUtil.getLinkedInstance(node)
        #  Find node that is properly linked
        while node != None and linkedInstance == None:
            node = node.getParent()
            linkedInstance = NamedInstanceUtil.getLinkedInstance(node)
        if node == None or (isinstance(linkedInstance, (ReactorInstance)) and (linkedInstance).isMainOrFederated()):
            return IAction.ActionResult.createResult(False)
        else:
            self.setExpansionState(node, linkedInstance, v, not v.isExpanded(node))
            #  toggle
            return IAction.ActionResult.createResult(True)
