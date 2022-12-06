#!/usr/bin/env python
""" generated source for module ReactionPortAdjustment """
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
# package: org.lflang.diagram.synthesis.postprocessor
# import java.util.stream.Collectors
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.elk.core.options.PortSide
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.xtext.xbase.lib.Extension
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.Pair
import configparser

from lflang.diagram.synthesis.action.FilterCycleAction import KNode
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import KRenderingFactory
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import CoreOptions

config = configparser.RawConfigParser()
from org.lflang.diagram.synthesis.styles import LinguaFrancaShapeExtensions
# import de.cau.cs.kieler.klighd.IStyleModifier
# import de.cau.cs.kieler.klighd.IViewer
# import de.cau.cs.kieler.klighd.internal.ILayoutRecorder
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KGraphElement
# import de.cau.cs.kieler.klighd.kgraph.KGraphFactory
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.kgraph.KPoint
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import de.cau.cs.kieler.klighd.krendering.KRenderingFactory
import configparser

config = configparser.RawConfigParser()
# 
#  * Adjusts the port position of reactions node AFTER layout, to allow free port order but also adapt (snuggle) to pointy shape of reaction node.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#


class IStyleModifier:
    pass


class KGraphFactory:
    pass


class IViewer:
    pass


class ReactionPortAdjustment(IStyleModifier):
    """ generated source for class ReactionPortAdjustment """
    ID = "org.lflang.diagram.synthesis.postprocessor.ReactionPortAdjustment"

    #      * INTERNAL property to mark node as processed.
    #


    PROCESSED = config.get("org.lflang.diagram.synthesis.postprocessor.reaction.ports.processed", False)
    _kGraphFactory = KGraphFactory.eINSTANCE
    _kRenderingFactory = KRenderingFactory.eINSTANCE

    #      * Register this modifier on a reaction rendering.
    #      
    @classmethod
    def apply(cls, node, rendering):
        """ generated source for method apply """
        #  Add modifier that fixes port positions such that edges are properly attached to the shape
        invisible = cls._kRenderingFactory.createKInvisibility()
        invisible.setInvisible(False)
        #  make it ineffective (just for purpose of holding modifier)
        invisible.setModifierId(ReactionPortAdjustment.ID)
        #  Add modifier to receive callback after layout
        rendering.getStyles().append(invisible)
        node.setProperty(cls.PROCESSED, False)

    def modify(self, context):
        """ generated source for method modify """
        try:
            node = context.getGraphElement()
            if isinstance(node, KNode):
                knode = node
                #  Find root node
                parent = knode
                while parent.eContainer() != None:
                    parent = parent.eContainer()
                #  Get viewer (this is a bit brittle because it fetches the viewer from some internal property)
                viewer = None
                #                   =
                #                          parent.getAllProperties().entrySet().stream().filter(
                #                          entry ->
                #                                      entry.getKey().getId() == "de.cau.cs.kieler.klighd.viewer"
                #                                      || entry.getKey().getId() == "klighd.layout.viewer")
                #                                  .findAny().map(entry -> entry.getValue()).orElse(null);
                recorder = None
                if isinstance(viewer, (IViewer)):
                    recorder = (viewer).getViewContext().getLayoutRecorder()
                if not knode.getPorts().isEmpty():
                    if knode.getPorts()[0].getYpos() != 0 and not knode.getProperty(ReactionPortAdjustment.PROCESSED):
                        if recorder != None:
                            recorder.startRecording()
                        in_ = None
                        out = None
                        knode.setProperty(ReactionPortAdjustment.PROCESSED, True)
                        if recorder != None:
                            recorder.stopRecording(0)
                    elif knode.getPorts()[0].getYpos() == 0:
                        knode.setProperty(self.PROCESSED, False)
        except Exception as e:
            e.printStackTrace()
        return False

    def adjustPositions(self, indexedPorts, count, input):
        """ generated source for method adjustPositions """
        segments = LinguaFrancaShapeExtensions.REACTION_POINTINESS * 2 / (count + 1)
        for indexedPort in indexedPorts:
            port = indexedPort.getValue()
            idx = indexedPort.getKey()
            offset = 0
            if count % 2 != 0 and idx == count / 2:
                offset += LinguaFrancaShapeExtensions.REACTION_POINTINESS
            elif idx < count / 2:
                offset += segments * (idx + 1)
            else:
                offset += segments * (count - idx)
            if not input:
                offset -= LinguaFrancaShapeExtensions.REACTION_POINTINESS
            port.setPos(port.getXpos() + offset, port.getYpos())
            for edge in port.getEdges():
                if input:
                    edge.setTargetPoint(self.adjustedKPoint(edge.getTargetPoint(), offset))
                else:
                    edge.setSourcePoint(self.adjustedKPoint(edge.getSourcePoint(), offset))
            port.setProperty(CoreOptions.PORT_BORDER_OFFSET, float((-offset if input else offset)))

    def adjustedKPoint(self, point, xOffset):
        """ generated source for method adjustedKPoint """
        kPoint = self._kGraphFactory.createKPoint()
        kPoint.setX(point.getX() + xOffset)
        kPoint.setY(point.getY())
        return kPoint
