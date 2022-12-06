#!/usr/bin/env python
""" generated source for module SynthesisRegistration """
# package: org.lflang.diagram.synthesis
from lflang.diagram.synthesis import LinguaFrancaSynthesis
from org.lflang.diagram.synthesis.action import CollapseAllReactorsAction

from org.lflang.diagram.synthesis.action import ExpandAllReactorsAction

from org.lflang.diagram.synthesis.action import FilterCycleAction

from org.lflang.diagram.synthesis.action import MemorizingExpandCollapseAction

from org.lflang.diagram.synthesis.action import ShowCycleAction

from org.lflang.diagram.synthesis.postprocessor import ReactionPortAdjustment

from org.lflang.diagram.synthesis.styles import LinguaFrancaShapeExtensions

from org.lflang.diagram.synthesis.styles import LinguaFrancaStyleExtensions

from org.lflang.diagram.synthesis.util import NamedInstanceUtil
# import de.cau.cs.kieler.klighd.IKlighdStartupHook
# import de.cau.cs.kieler.klighd.KlighdDataManager

# 
#  * Registration of all diagram synthesis related classes in Klighd.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class IKlighdStartupHook:
    pass


class KlighdDataManager:
    pass


class SynthesisRegistration(IKlighdStartupHook):
    """ generated source for class SynthesisRegistration """
    def execute(self):
        """ generated source for method execute """
        reg = KlighdDataManager.getInstance()
        #  Synthesis
        reg.registerDiagramSynthesisClass(LinguaFrancaSynthesis.ID, LinguaFrancaSynthesis.__class__)
        #  Actions
        reg.registerAction(MemorizingExpandCollapseAction.ID, MemorizingExpandCollapseAction())
        reg.registerAction(ExpandAllReactorsAction.ID, ExpandAllReactorsAction())
        reg.registerAction(CollapseAllReactorsAction.ID, CollapseAllReactorsAction())
        reg.registerAction(ShowCycleAction.ID, ShowCycleAction())
        reg.registerAction(FilterCycleAction.ID, FilterCycleAction())
        #  Style Mod
        reg.registerStyleModifier(ReactionPortAdjustment.ID, ReactionPortAdjustment())
        #  Blacklist LF-specific properties that should be removed when a diagram is sent from the diagram server to a client.
        reg.registerBlacklistedProperty(FilterCycleAction.FILTER_BUTTON)
        reg.registerBlacklistedProperty(LinguaFrancaSynthesis.REACTOR_HAS_BANK_PORT_OFFSET)
        reg.registerBlacklistedProperty(LinguaFrancaSynthesis.REACTOR_INPUT)
        reg.registerBlacklistedProperty(LinguaFrancaSynthesis.REACTOR_OUTPUT)
        reg.registerBlacklistedProperty(LinguaFrancaSynthesis.REACTION_SPECIAL_TRIGGER)
        reg.registerBlacklistedProperty(ReactionPortAdjustment.PROCESSED)
        reg.registerBlacklistedProperty(LinguaFrancaShapeExtensions.REACTOR_CONTENT_CONTAINER)
        reg.registerBlacklistedProperty(LinguaFrancaStyleExtensions.LABEL_PARENT_BACKGROUND)
        reg.registerBlacklistedProperty(NamedInstanceUtil.LINKED_INSTANCE)
        #  Very important since its values can not be synthesized easily!
