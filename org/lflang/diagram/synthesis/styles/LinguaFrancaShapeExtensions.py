#!/usr/bin/env python
""" generated source for module LinguaFrancaShapeExtensions """
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
# package: org.lflang.diagram.synthesis.styles
# import java.util.ArrayList
# import java.util.List
# import javax.inject.Inject
# import org.eclipse.elk.core.options.CoreOptions
# import org.eclipse.elk.core.options.PortSide
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.xtext.xbase.lib.Extension
# import org.eclipse.xtext.xbase.lib.Functions.Function1
# import org.eclipse.xtext.xbase.lib.IterableExtensions
# import org.eclipse.xtext.xbase.lib.Pair
# import org.eclipse.xtext.xbase.lib.StringExtensions
from include.KeilerClasses import KRenderingFactory, KNodeExtensions, KEdgeExtensions, KPortExtensions, \
    KLabelExtensions, KRenderingExtensions, KContainerRenderingExtensions, KPolylineExtensions, LEFT, TOP, RIGHT, BOTTOM
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import LinguaFrancaStyleExtensions, Colors
from lflang.diagram.synthesis.styles.ReactorFigureComponents import ReactorFigureComponents
from lflang.diagram.synthesis.util.InterfaceDependenciesVisualization import DiagramSyntheses, CoreOptions, LineStyle
from org.lflang import ASTUtils

from org.lflang.diagram.synthesis import AbstractSynthesisExtensions

from org.lflang.diagram.synthesis import LinguaFrancaSynthesis

from org.lflang.diagram.synthesis.util import UtilityExtensions

from org.lflang.generator import ReactionInstance

from org.lflang.generator import ReactorInstance

from org.lflang.generator import TimerInstance

from org.lflang.lf import Parameter

from org.lflang.lf import StateVar
# import de.cau.cs.kieler.klighd.KlighdConstants
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KNode
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.Arc
# import de.cau.cs.kieler.klighd.krendering.Colors
# import de.cau.cs.kieler.klighd.krendering.HorizontalAlignment
# import de.cau.cs.kieler.klighd.krendering.KArc
# import de.cau.cs.kieler.klighd.krendering.KAreaPlacementData
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KDecoratorPlacementData
# import de.cau.cs.kieler.klighd.krendering.KEllipse
# import de.cau.cs.kieler.klighd.krendering.KGridPlacement
# import de.cau.cs.kieler.klighd.krendering.KPolygon
# import de.cau.cs.kieler.klighd.krendering.KPolyline
# import de.cau.cs.kieler.klighd.krendering.KPosition
# import de.cau.cs.kieler.klighd.krendering.KRectangle
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import de.cau.cs.kieler.klighd.krendering.KRenderingFactory
# import de.cau.cs.kieler.klighd.krendering.KRoundedRectangle
# import de.cau.cs.kieler.klighd.krendering.KText
# import de.cau.cs.kieler.klighd.krendering.LineStyle
# import de.cau.cs.kieler.klighd.krendering.VerticalAlignment
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.krendering.extensions.KColorExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KContainerRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KEdgeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KLabelExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KNodeExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPolylineExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPortExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.PositionReferenceX
# import de.cau.cs.kieler.klighd.krendering.extensions.PositionReferenceY
# import de.cau.cs.kieler.klighd.syntheses.DiagramSyntheses

#
#  * Extension class that provides shapes and figures for the Lingua France diagram synthesis.
#  *
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#
import configparser
config = configparser.RawConfigParser()


class PortLabelPlacement:
    pass


class EdgeRouting:
    pass


class Direction:
    pass


class NodePlacementStrategy:
    pass



class EdgeStraighteningStrategy:
    pass


class CenterEdgeLabelPlacementStrategy:
    pass


class HorizontalAlignment:
    pass


class PortConstraints:
    pass


class PortSide:
    pass


class ITextRenderingProvider:
    pass


class RectangleDecorator:
    pass


class KColorExtensions:
    pass


class VerticalAlignment:
    pass


class KlighdConstants:
    pass


class PositionReferenceX:
    pass


class Arc:
    pass


class PositionReferenceY:
    pass


class LinguaFrancaShapeExtensions(AbstractSynthesisExtensions):
    """ generated source for class LinguaFrancaShapeExtensions """
    REACTION_POINTINESS = 6

    #  arrow point length
    #  Property for marking the KContainterRendering in Reactor figures that is supposed to hold the content
    REACTOR_CONTENT_CONTAINER = config.get("org.lflang.diagram.synthesis.shapes.reactor.content", False)

    BANK_FIGURE_X_OFFSET_SUM = 6.0
    BANK_FIGURE_Y_OFFSET_SUM = 9.0

    #      * Creates the main reactor frame.
    #

    def __init__(self):
        """

        """
        self._kNodeExtensions = KNodeExtensions()
        self._kEdgeExtensions = KEdgeExtensions()
        self._kPortExtensions = KPortExtensions()
        self._kLabelExtensions = KLabelExtensions()
        self._kRenderingExtensions = KRenderingExtensions()
        self._kContainerRenderingExtensions = KContainerRenderingExtensions()
        self._kPolylineExtensions = KPolylineExtensions()
        self._kColorExtensions = KColorExtensions()
        self._linguaFrancaStyleExtensions = LinguaFrancaStyleExtensions()
        self._utilityExtensions = UtilityExtensions()
        self._kRenderingFactory = KRenderingFactory.eINSTANCE

    def addMainReactorFigure(self, node, reactorInstance, text):
        """
        * Creates the main reactor frame.
        generated source for method addMainReactorFigure """
        padding = 8 if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_HYPERLINKS) else 6
        figure = self._kRenderingExtensions.addRoundedRectangle(node, 8, 8, 1)
        self._kContainerRenderingExtensions.setGridPlacement(figure, 1)
        self._kRenderingExtensions.setLineWidth(figure, 1)
        self._kRenderingExtensions.setForeground(figure, Colors.GRAY)
        self._kRenderingExtensions.setBackground(figure, Colors.WHITE)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        #  Create parent container
        parentContainer = self._kContainerRenderingExtensions.addRectangle(figure)
        self._kRenderingExtensions.setInvisible(parentContainer, True)
        self.setGridPlacementDataFromPointToPoint(parentContainer, LEFT, padding, 0, TOP, padding, 0, RIGHT, padding, 0, BOTTOM, 4, 0)
        #  Create child container
        childContainer = self._kContainerRenderingExtensions.addRectangle(parentContainer)
        self._kRenderingExtensions.setInvisible(childContainer, True)
        self._kRenderingExtensions.setPointPlacementData(childContainer, self._kRenderingExtensions.LEFT, 0, 0.5, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_CENTRAL, self._kRenderingExtensions.V_CENTRAL, 0, 0, 0, 0)
        placement = self._kContainerRenderingExtensions.setGridPlacement(childContainer, 1)
        #  Add text to the child container
        childText = self._kContainerRenderingExtensions.addText(childContainer, text)
        DiagramSyntheses.suppressSelectability(childText)
        self._linguaFrancaStyleExtensions.underlineSelectionStyle(childText)
        if reactorInstance.reactorDefinition.isFederated():
            cloudIcon = self._linguaFrancaStyleExtensions.addCloudIcon(childContainer)
            self.setGridPlacementDataFromPointToPoint(cloudIcon, LEFT, 3, 0, TOP, 0, 0, RIGHT, 0, 0, BOTTOM, 0, 0)
            placement.setNumColumns(2)
            if reactorInstance.reactorDefinition.getHost() != None and self.getBooleanValue(LinguaFrancaSynthesis.SHOW_REACTOR_HOST):
                hostNameText = self._kContainerRenderingExtensions.addText(childContainer, ASTUtils.toOriginalText(reactorInstance.reactorDefinition.getHost()))
                DiagramSyntheses.suppressSelectability(hostNameText)
                self._linguaFrancaStyleExtensions.underlineSelectionStyle(hostNameText)
                self.setGridPlacementDataFromPointToPoint(hostNameText, LEFT, 3, 0, TOP, 0, 0, RIGHT, 0, 0, BOTTOM, 0, 0)
                placement.setNumColumns(3)
        return figure

    def addReactorFigure(self, node, reactorInstance, text):
        """ Creates the visual representation of a reactor node """
        padding = 8 if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_HYPERLINKS) else 6
        style = None
        #           = r -> {
        #              _kRenderingExtensions.setLineWidth(r, 1);
        #              _kRenderingExtensions.setForeground(r, Colors.GRAY);
        #              _kRenderingExtensions.setBackground(r, Colors.GRAY_95);
        #              return _linguaFrancaStyleExtensions.boldLineSelectionStyle(r);
        #          };
        figure = self._kRenderingExtensions.addRoundedRectangle(node, 8, 8, 1)
        self._kContainerRenderingExtensions.setGridPlacement(figure, 1)
        style.apply(figure)
        figure.setProperty(self.REACTOR_CONTENT_CONTAINER, True)
        #  minimal node size is necessary if no text will be added
        minSize = list(2 * figure.getCornerWidth(), 2 * figure.getCornerHeight())
        self._kNodeExtensions.setMinimalNodeSize(node, minSize.get(0), minSize.get(1))
        #  Add parent container
        parentContainer = self._kContainerRenderingExtensions.addRectangle(figure)
        self._kRenderingExtensions.setInvisible(parentContainer, True)
        self.setGridPlacementDataFromPointToPoint(parentContainer, LEFT, padding, 0, TOP, padding, 0, RIGHT, padding, 0, BOTTOM, 4 if self._utilityExtensions.hasContent(reactorInstance) else padding, 0)
        #  Add centered child container
        childContainer = self._kContainerRenderingExtensions.addRectangle(parentContainer)
        self._kRenderingExtensions.setInvisible(childContainer, True)
        self._kRenderingExtensions.setPointPlacementData(childContainer, self._kRenderingExtensions.LEFT, 0, 0.5, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_CENTRAL, self._kRenderingExtensions.V_CENTRAL, 0, 0, 0, 0)
        placement = self._kContainerRenderingExtensions.setGridPlacement(childContainer, 1)
        childText = self._kContainerRenderingExtensions.addText(childContainer, text)
        DiagramSyntheses.suppressSelectability(childText)
        self._linguaFrancaStyleExtensions.underlineSelectionStyle(childText)
        if not self._utilityExtensions.isRoot(reactorInstance) and reactorInstance.getDefinition().getHost() != None:
            cloudUploadIcon = self._linguaFrancaStyleExtensions.addCloudUploadIcon(childContainer)
            self.setGridPlacementDataFromPointToPoint(cloudUploadIcon, LEFT, 3, 0, TOP, 0, 0, RIGHT, 0, 0, BOTTOM, 0, 0)
            placement.setNumColumns(2)
            if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_REACTOR_HOST):
                reactorHostText = self._kContainerRenderingExtensions.addText(childContainer, ASTUtils.toOriginalText(reactorInstance.getDefinition().getHost()))
                DiagramSyntheses.suppressSelectability(reactorHostText)
                self._linguaFrancaStyleExtensions.underlineSelectionStyle(reactorHostText)
                self.setGridPlacementDataFromPointToPoint(reactorHostText, LEFT, 3, 0, TOP, 0, 0, RIGHT, 0, 0, BOTTOM, 0, 0)
                placement.setNumColumns(3)
        if reactorInstance.isBank():
            bank = []
            container = self._kRenderingExtensions.addInvisibleContainerRendering(node)
            #  TODO handle unresolved width
            banks = self._kContainerRenderingExtensions.addRoundedRectangle(container, 8, 8, 1)
            style.apply(banks)
            self.setGridPlacementDataFromPointToPoint(banks, LEFT, self.BANK_FIGURE_X_OFFSET_SUM, 0, TOP, self.BANK_FIGURE_Y_OFFSET_SUM, 0, RIGHT, 0, 0, BOTTOM, 0, 0)
            if reactorInstance.getWidth() == 3:
                banks = self._kContainerRenderingExtensions.addRoundedRectangle(container, 8, 8, 1)
                style.apply(banks)
                self.setGridPlacementDataFromPointToPoint(banks, LEFT, self.BANK_FIGURE_X_OFFSET_SUM / 2, 0, TOP, self.BANK_FIGURE_Y_OFFSET_SUM / 2, 0, RIGHT, self.BANK_FIGURE_X_OFFSET_SUM / 2, 0, BOTTOM, self.BANK_FIGURE_Y_OFFSET_SUM / 2, 0)
            elif reactorInstance.getWidth() != 2 and reactorInstance.getWidth() != 3:
                banks = self._kContainerRenderingExtensions.addRoundedRectangle(container, 8, 8, 1)
                style.apply(banks)
                self.setGridPlacementDataFromPointToPoint(banks, LEFT, 2 * self.BANK_FIGURE_X_OFFSET_SUM / 3, 0, TOP, 2 * self.BANK_FIGURE_Y_OFFSET_SUM / 3, 0, RIGHT, self.BANK_FIGURE_X_OFFSET_SUM / 3, 0, BOTTOM, self.BANK_FIGURE_Y_OFFSET_SUM / 3, 0)
                banks = self._kContainerRenderingExtensions.addRoundedRectangle(container, 8, 8, 1)
                style.apply(banks)
                self.setGridPlacementDataFromPointToPoint(banks, LEFT, self.BANK_FIGURE_X_OFFSET_SUM / 3, 0, TOP, self.BANK_FIGURE_Y_OFFSET_SUM / 3, 0, RIGHT, 2 * self.BANK_FIGURE_X_OFFSET_SUM / 3, 0, BOTTOM, 2 * self.BANK_FIGURE_Y_OFFSET_SUM / 3, 0)
            container.getChildren().append(figure)
            self.setGridPlacementDataFromPointToPoint(figure, LEFT, 0, 0, TOP, 0, 0, RIGHT, self.BANK_FIGURE_X_OFFSET_SUM, 0, BOTTOM, self.BANK_FIGURE_Y_OFFSET_SUM, 0)
            bank.addAll(container.getChildren())
            widthLabelContainer = self._kContainerRenderingExtensions.addRectangle(container)
            self._kRenderingExtensions.setInvisible(widthLabelContainer, True)
            self.setGridPlacementDataFromPointToPoint(widthLabelContainer, LEFT, 12, 0, BOTTOM, 9, 0, RIGHT, 6, 0, BOTTOM, 0.5, 0)
            #  Handle unresolved width.
            widthLabel = f"{reactorInstance.getWidth()}" if reactorInstance.getWidth() >= 0 else "?"
            widthLabelText = self._kContainerRenderingExtensions.addText(widthLabelContainer, widthLabel)
            self._kRenderingExtensions.setHorizontalAlignment(widthLabelText, HorizontalAlignment.LEFT)
            self._kRenderingExtensions.setVerticalAlignment(widthLabelText, VerticalAlignment.BOTTOM)
            self._kRenderingExtensions.setFontSize(widthLabelText, 6)
            self._linguaFrancaStyleExtensions.noSelectionStyle(widthLabelText)
            self.associateWith(widthLabelText, reactorInstance.getDefinition().getWidthSpec())
            return ReactorFigureComponents(container, figure, bank)
        else:
            return ReactorFigureComponents(figure, figure, list(figure))

    def addReactionFigure(self, node, reaction):
        """
        Creates the visual representation of a reaction node
        :param node:
        :param reaction:
        :return:
        """
        minHeight = 22
        minWidth = 45
        reactor = reaction.getParent()
        self._kNodeExtensions.setMinimalNodeSize(node, minWidth, minHeight)
        #  Create base shape
        baseShape = self._kRenderingExtensions.addPolygon(node)
        self.associateWith(baseShape, reaction)
        self._kRenderingExtensions.setLineWidth(baseShape, 1)
        self._kRenderingExtensions.setForeground(baseShape, Colors.GRAY_45)
        self._kRenderingExtensions.setBackground(baseShape, Colors.GRAY_65)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(baseShape)
        baseShape.getPoints().extend([self._kRenderingExtensions.createKPosition(LEFT, 0, 0, TOP, 0, 0),
                                      self._kRenderingExtensions.createKPosition(RIGHT, self.REACTION_POINTINESS, 0, TOP, 0, 0),
                                      self._kRenderingExtensions.createKPosition(RIGHT, 0, 0, TOP, 0, 0.5),
                                      self._kRenderingExtensions.createKPosition(RIGHT, self.REACTION_POINTINESS, 0, BOTTOM, 0, 0),
                                      self._kRenderingExtensions.createKPosition(LEFT, 0, 0, BOTTOM, 0, 0),
                                      self._kRenderingExtensions.createKPosition(LEFT, self.REACTION_POINTINESS, 0, BOTTOM, 0, 0.5)])
        contentContainer = self._kContainerRenderingExtensions.addRectangle(baseShape)
        self.associateWith(contentContainer, reaction)
        self._kRenderingExtensions.setInvisible(contentContainer, True)
        self._kRenderingExtensions.setPointPlacementData(contentContainer, self._kRenderingExtensions.LEFT, self.REACTION_POINTINESS, 0, self._kRenderingExtensions.TOP, 0, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_TOP, self.REACTION_POINTINESS, 0, minWidth - self.REACTION_POINTINESS * 2, minHeight)
        self._kContainerRenderingExtensions.setGridPlacement(contentContainer, 1)
        if len(reactor.reactions) > 1:
            textToAdd = self._kContainerRenderingExtensions.addText(contentContainer, f"{reactor.reactions.indexOf(reaction) + 1}")
            self._kRenderingExtensions.setFontBold(textToAdd, True)
            self._linguaFrancaStyleExtensions.noSelectionStyle(textToAdd)
            DiagramSyntheses.suppressSelectability(textToAdd)
        #  optional reaction level
        if self.getBooleanValue(LinguaFrancaSynthesis.SHOW_REACTION_LEVEL):
            #  Force calculation of levels for reactions. This calculation
            #  will only be done once. Note that if this fails due to a causality loop,
            #  then some reactions will have level -1.
            try:
                levels = ", ".join(reaction.getLevels())
                levelsText = self._kContainerRenderingExtensions.addText(contentContainer, ("level: " + levels))
                self._kRenderingExtensions.setFontBold(levelsText, False)
                self._linguaFrancaStyleExtensions.noSelectionStyle(levelsText)
                DiagramSyntheses.suppressSelectability(levelsText)
            except Exception as ex:
                pass
                #  If the graph has cycles, the above fails. Continue without showing levels.
        #  optional code content
        hasCode = self.getBooleanValue(LinguaFrancaSynthesis.SHOW_REACTION_CODE) and len(reaction.getDefinition().getCode().getBody()) > 0
        if hasCode:
            hasCodeText = self._kContainerRenderingExtensions.addText(contentContainer, self._utilityExtensions.trimCode(reaction.getDefinition().getCode()))
            self.associateWith(hasCodeText, reaction)
            self._kRenderingExtensions.setFontSize(hasCodeText, 6)
            self._kRenderingExtensions.setFontName(hasCodeText, KlighdConstants.DEFAULT_MONOSPACE_FONT_NAME)
            self._linguaFrancaStyleExtensions.noSelectionStyle(hasCodeText)
            self._kRenderingExtensions.setHorizontalAlignment(hasCodeText, HorizontalAlignment.LEFT)
            self._kRenderingExtensions.setVerticalAlignment(hasCodeText, VerticalAlignment.TOP)
            self.setGridPlacementDataFromPointToPoint(hasCodeText, self._kRenderingExtensions.LEFT, 5, 0, self._kRenderingExtensions.TOP, 5, 0, self._kRenderingExtensions.RIGHT, 5, 0, self._kRenderingExtensions.BOTTOM, 5, 0)
        if reaction.declaredDeadline != None:
            hasDeadlineCode = self.getBooleanValue(LinguaFrancaSynthesis.SHOW_REACTION_CODE) and len(reaction.getDefinition().getDeadline().getCode().getBody()) > 0
            if hasCode or hasDeadlineCode:
                line = self._kContainerRenderingExtensions.addHorizontalLine(contentContainer, 0)
                self.setGridPlacementDataFromPointToPoint(line, self._kRenderingExtensions.LEFT, 5, 0, self._kRenderingExtensions.TOP, 3, 0, self._kRenderingExtensions.RIGHT, 5, 0, self._kRenderingExtensions.BOTTOM, 6, 0)
            #  delay with stopwatch
            labelContainer = self._kContainerRenderingExtensions.addRectangle(contentContainer)
            self._kRenderingExtensions.setInvisible(labelContainer, True)
            placement = self.setGridPlacementDataFromPointToPoint(labelContainer, self._kRenderingExtensions.LEFT, 0 if hasDeadlineCode else -self.REACTION_POINTINESS * 0.5, 0, self._kRenderingExtensions.TOP, 0, 0 if len(reactor.reactions) > 1 or hasCode or hasDeadlineCode else 0.5, self._kRenderingExtensions.RIGHT, 0, 0, self._kRenderingExtensions.BOTTOM, 0, 0)
            self._kRenderingExtensions.setHorizontalAlignment(placement, HorizontalAlignment.LEFT)
            stopWatchFigure = self.addStopwatchFigure(labelContainer)
            self._kRenderingExtensions.setLeftTopAlignedPointPlacementData(stopWatchFigure, 0, 0, 0, 0)
            stopWatchText = self._kContainerRenderingExtensions.addText(labelContainer, str(reaction.declaredDeadline.maxDelay))
            self.associateWith(stopWatchText, reaction.getDefinition().getDeadline().getDelay())
            self._kRenderingExtensions.setForeground(stopWatchText, Colors.BROWN)
            self._kRenderingExtensions.setFontBold(stopWatchText, True)
            self._kRenderingExtensions.setFontSize(stopWatchText, 7)
            self._linguaFrancaStyleExtensions.underlineSelectionStyle(stopWatchText)
            self._kRenderingExtensions.setLeftTopAlignedPointPlacementData(stopWatchText, 15, 0, 0, 0)
            # optional code content
            if hasDeadlineCode:
                contentContainerText = self._kContainerRenderingExtensions.addText(contentContainer, self._utilityExtensions.trimCode(reaction.getDefinition().getDeadline().getCode()))
                self.associateWith(contentContainerText, reaction.deadline)
                self._kRenderingExtensions.setForeground(contentContainerText, Colors.BROWN)
                self._kRenderingExtensions.setFontSize(contentContainerText, 6)
                self._kRenderingExtensions.setFontName(contentContainerText, KlighdConstants.DEFAULT_MONOSPACE_FONT_NAME)
                self.setGridPlacementDataFromPointToPoint(contentContainerText, self._kRenderingExtensions.LEFT, 5, 0, self._kRenderingExtensions.TOP, 0, 0, self._kRenderingExtensions.RIGHT, 5, 0, self._kRenderingExtensions.BOTTOM, 5, 0)
                self._kRenderingExtensions.setHorizontalAlignment(contentContainerText, HorizontalAlignment.LEFT)
                self._linguaFrancaStyleExtensions.noSelectionStyle(contentContainerText)
        return baseShape

    def addStopwatchFigure(self, parent):
        """
        Stopwatch figure for deadlines.
        :param parent:
        :return:
        """
        size = 12
        container = self._kContainerRenderingExtensions.addRectangle(parent)
        self._kRenderingExtensions.setInvisible(container, True)
        self._kRenderingExtensions.setPointPlacementData(container, self._kRenderingExtensions.LEFT, 0, 0, self._kRenderingExtensions.TOP, 0, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_TOP, 0, 0, size, size)
        polyline = self._kContainerRenderingExtensions.addPolyline(container, 2, list(self._kRenderingExtensions.createKPosition(LEFT, 3, 0.5, TOP, (-2), 0), self._kRenderingExtensions.createKPosition(LEFT, (-3), 0.5, TOP, (-2), 0)))
        self._kRenderingExtensions.setForeground(polyline, Colors.BROWN)
        polyline = self._kContainerRenderingExtensions.addPolyline(container, 2, list(self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, (-2), 0), self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 1, 0)))
        self._kRenderingExtensions.setForeground(polyline, Colors.BROWN)
        body = self._kContainerRenderingExtensions.addEllipse(container)
        self._kRenderingExtensions.setLineWidth(body, 1)
        self._kRenderingExtensions.setForeground(body, Colors.BROWN)
        self._kRenderingExtensions.setPointPlacementData(body,
                                                         self._kRenderingExtensions.LEFT,
                                                         0, 0,
                                                         self._kRenderingExtensions.TOP,
                                                         0, 0,
                                                         self._kRenderingExtensions.H_LEFT,
                                                         self._kRenderingExtensions.V_TOP,
                                                         0, 0,
                                                         size, size)
        self._linguaFrancaStyleExtensions.noSelectionStyle(body)
        arc = self._kContainerRenderingExtensions.addArc(body)
        arc.setStartAngle((-20))
        arc.setArcAngle(110)
        arc.setArcType(Arc.PIE)
        self._kRenderingExtensions.setLineWidth(arc, 0)
        self._kRenderingExtensions.setBackground(arc, Colors.BROWN)
        self._kRenderingExtensions.setPointPlacementData(arc,
                                                         self._kRenderingExtensions.LEFT,
                                                         2, 0,
                                                         self._kRenderingExtensions.TOP,
                                                         2, 0,
                                                         self._kRenderingExtensions.H_LEFT,
                                                         self._kRenderingExtensions.V_TOP,
                                                         2, 2,
                                                         size - 4, size - 4)
        self._linguaFrancaStyleExtensions.noSelectionStyle(arc)
        return container

    def addTimerFigure(self, node, timer):
        """
        Creates the visual representation of a timer node
        :param node:
        :param timer:
        :return:
        """
        self._kNodeExtensions.setMinimalNodeSize(node, 30, 30)
        figure = self._kRenderingExtensions.addEllipse(node)
        self._kRenderingExtensions.setBackground(figure, Colors.GRAY_95)
        self._linguaFrancaStyleExtensions.noSelectionStyle(figure)
        self._kRenderingExtensions.setLineWidth(figure, 1)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        polylinePoints = [self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 0, 0.1),
                              self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 0, 0.5),
                              self._kRenderingExtensions.createKPosition(LEFT, 0, 0.7, TOP, 0, 0.7)]
        polyline = self._kContainerRenderingExtensions.addPolyline(figure, 1, polylinePoints)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(polyline)
        labelParts = []
        if timer.getOffset() != TimerInstance.DEFAULT_OFFSET and timer.getOffset() != None:
            labelParts.append(timer.getOffset().__str__())
        if timer.getPeriod() != TimerInstance.DEFAULT_PERIOD and timer.getPeriod() != None:
            if timer.getOffset() == TimerInstance.DEFAULT_OFFSET:
                labelParts.append(timer.getOffset().__str__())
            labelParts.append(timer.getPeriod().__str__())
        if not labelParts.isEmpty():
            self._kLabelExtensions.addOutsideBottomCenteredNodeLabel(node, "(" + ", ".join( labelParts) + ")", 8)
        return figure

    def addStartupFigure(self, node):
        """
        Creates the visual representation of a startup trigger.
        :param node:
        :return:
        """
        self._kNodeExtensions.setMinimalNodeSize(node, 18, 18)
        figure = self._kRenderingExtensions.addEllipse(node)
        self._kRenderingExtensions.setLineWidth(figure, 1)
        self._kRenderingExtensions.setBackground(figure, Colors.WHITE)
        self._linguaFrancaStyleExtensions.noSelectionStyle(figure)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        return figure

    def addShutdownFigure(self, node):
        """
        Creates the visual representation of a shutdown trigger
        :param node:
        :return:
        """
        self._kNodeExtensions.setMinimalNodeSize(node, 18, 18)
        figure = self._kRenderingExtensions.addPolygon(node)
        self._kRenderingExtensions.setLineWidth(figure, 1)
        self._kRenderingExtensions.setBackground(figure, Colors.WHITE)
        self._linguaFrancaStyleExtensions.noSelectionStyle(figure)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        pointsToAdd = list(self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 0, 0), self._kRenderingExtensions.createKPosition(RIGHT, 0, 0, TOP, 0, 0.5), self._kRenderingExtensions.createKPosition(RIGHT, 0, 0.5, BOTTOM, 0, 0), self._kRenderingExtensions.createKPosition(LEFT, 0, 0, BOTTOM, 0, 0.5))
        figure.getPoints().addAll(pointsToAdd)
        return figure

    def addResetFigure(self, node):
        """
        Creates the visual representation of a reset figure
        :param node:
        :return:
        """
        self._kNodeExtensions.setMinimalNodeSize(node, 18, 18)
        figure = self._kRenderingExtensions.addEllipse(node)
        self._kRenderingExtensions.setLineWidth(figure, 1)
        self._kRenderingExtensions.setBackground(figure, Colors.WHITE)
        self._linguaFrancaStyleExtensions.noSelectionStyle(figure)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        resetCircle = self._kContainerRenderingExtensions.addEllipse(figure)
        self._kRenderingExtensions.setSurroundingSpace(resetCircle, 3, 0)
        self._kRenderingExtensions.setLineWidth(resetCircle, 1.5)
        self._kRenderingExtensions.setBackground(resetCircle, Colors.WHITE)
        self._linguaFrancaStyleExtensions.noSelectionStyle(resetCircle)
        resetCycleGap = self._kContainerRenderingExtensions.addPolygon(resetCircle)
        resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0, 0, PositionReferenceY.TOP, 0.0, 0))
        resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 0, 0, PositionReferenceY.TOP, 0.0, 0))
        resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 1.1, 0, PositionReferenceY.BOTTOM, 0, 0))
        resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 1.1, 0, PositionReferenceY.BOTTOM, 0, 0))
        self._kRenderingExtensions.setLineWidth(resetCycleGap, 0.3)
        self._kRenderingExtensions.setForeground(resetCycleGap, Colors.WHITE)
        self._kRenderingExtensions.setBackground(resetCycleGap, Colors.WHITE)
        self._linguaFrancaStyleExtensions.noSelectionStyle(resetCycleGap)
        self._kRenderingExtensions.setPointPlacementData(resetCycleGap, self._kRenderingExtensions.LEFT, -2, 0.5, self._kRenderingExtensions.TOP, 1.5, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 4.0, 3.0)
        resetArrow = self._kContainerRenderingExtensions.addPolygon(resetCircle)
        resetArrow.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0, 0, PositionReferenceY.TOP, 0.0, 0.1))
        resetArrow.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0.0, 0.3, PositionReferenceY.BOTTOM, 0, 0))
        resetArrow.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 0.0, 0, PositionReferenceY.TOP, 0.0, 0.0))
        self._kRenderingExtensions.setLineWidth(resetArrow, 0.3)
        self._kRenderingExtensions.setBackground(resetArrow, Colors.BLACK)
        self._linguaFrancaStyleExtensions.noSelectionStyle(resetArrow)
        self._kRenderingExtensions.setPointPlacementData(resetArrow, self._kRenderingExtensions.LEFT, 1.0, 0.5, self._kRenderingExtensions.TOP, 1.8, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 3.2, 3.2)
        return figure

    def addTrianglePort(self, port, multiport):
        """
        Creates the visual representation of a reactor port.
        :param port:
        :param multiport:
        :return:
        """
        port.setSize(8, 8)
        # Create triangle port
        trianglePort = self._kRenderingExtensions.addPolygon(port)
        # Set line width and background color according to multiport or not
        lineWidth = 2.2 if multiport else 1
        self._kRenderingExtensions.setLineWidth(trianglePort, lineWidth)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(trianglePort)
        background = Colors.WHITE if multiport else Colors.BLACK
        self._kRenderingExtensions.setBackground(trianglePort, background)
        pointsToAdd = None
        if multiport:
            # Compensate for line width by making triangle smaller
            # Do not adjust by port size because this will affect port distribution and cause offsets between parallel connections
            pointsToAdd = [self._kRenderingExtensions.createKPosition(LEFT, 0, 0, TOP, 0.6, 0),
                           self._kRenderingExtensions.createKPosition(RIGHT, 1.2, 0, TOP, 0, 0.5),
                           self._kRenderingExtensions.createKPosition(LEFT, 0, 0, BOTTOM, 0.6, 0)]
        else:
            pointsToAdd = [self._kRenderingExtensions.createKPosition(LEFT, 0, 0, TOP, 0, 0),
                           self._kRenderingExtensions.createKPosition(RIGHT, 0, 0, TOP, 0, 0.5),
                           self._kRenderingExtensions.createKPosition(LEFT, 0, 0, BOTTOM, 0, 0)]
        trianglePort.getPoints().addAll(pointsToAdd)
        return trianglePort

    def addTextButton(self, container, text):
        """
        Added a text as collapse expand button.
        :param container:
        :param text:
        :return:
        """
        textToAdd = self._kContainerRenderingExtensions.addText(container, text)
        self._kRenderingExtensions.setForeground(textToAdd, Colors.BLUE)
        self._kRenderingExtensions.setFontSize(textToAdd, 8)
        self._linguaFrancaStyleExtensions.noSelectionStyle(textToAdd)
        return textToAdd

    def addActionDecorator(self, line, text):
        """
        Creates the triangular line decorator with text.
        :param line:
        :param text:
        :return:
        """
        size = 18
        # Create action decorator
        actionDecorator = self._kContainerRenderingExtensions.addPolygon(line)
        self._kRenderingExtensions.setBackground(actionDecorator, Colors.WHITE)
        pointsToAdd = [self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 0, 0),
                           self._kRenderingExtensions.createKPosition(RIGHT, 0, 0, BOTTOM, 0, 0),
                           self._kRenderingExtensions.createKPosition(LEFT, 0, 0, BOTTOM, 0, 0)]
        actionDecorator.getPoints().addAll(pointsToAdd)
        # Set placement data of the action decorator
        placementData = self._kRenderingFactory.createKDecoratorPlacementData()
        placementData.setRelative(0.5)
        placementData.setAbsolute(-size / 2)
        placementData.setWidth(size)
        placementData.setHeight(size)
        placementData.setYOffset(-size * 0.66)
        placementData.setRotateWithLine(True)
        actionDecorator.setPlacementData(placementData)
        # Add text to the action decorator
        textToAdd = self._kContainerRenderingExtensions.addText(actionDecorator, text)
        self._kRenderingExtensions.setFontSize(textToAdd, 8)
        self._linguaFrancaStyleExtensions.noSelectionStyle(textToAdd)
        DiagramSyntheses.suppressSelectability(textToAdd)
        self._kRenderingExtensions.setPointPlacementData(textToAdd,
                                                         self._kRenderingExtensions.LEFT,
                                                         0, 0.5,
                                                         self._kRenderingExtensions.TOP,
                                                         size * 0.15, 0.5,
                                                         self._kRenderingExtensions.H_CENTRAL,
                                                         self._kRenderingExtensions.V_CENTRAL,
                                                         0, 0,
                                                         size, size)
        return actionDecorator

    def addActionFigureAndPorts(self, node, text):
        """
        Creates the triangular action node with text and ports.
        :param node:
        :param text:
        :return:
        """
        size = 18
        self._kNodeExtensions.setMinimalNodeSize(node, size, size)
        figure = self._kRenderingExtensions.addPolygon(node)
        self._kRenderingExtensions.setBackground(figure, Colors.WHITE)
        self._linguaFrancaStyleExtensions.boldLineSelectionStyle(figure)
        pointsToAdd = [self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 0, 0),
                           self._kRenderingExtensions.createKPosition(RIGHT, 0, 0, BOTTOM, 0, 0),
                           self._kRenderingExtensions.createKPosition(LEFT, 0, 0, BOTTOM, 0, 0)]
        figure.getPoints().addAll(pointsToAdd)
        # Add text to the action figure
        textToAdd = self._kContainerRenderingExtensions.addText(figure, text)
        self._kRenderingExtensions.setFontSize(textToAdd, 8)
        self._linguaFrancaStyleExtensions.noSelectionStyle(textToAdd)
        DiagramSyntheses.suppressSelectability(textToAdd)
        self._kRenderingExtensions.setPointPlacementData(textToAdd,
                                                         self._kRenderingExtensions.LEFT,
                                                         0, 0.5,
                                                         self._kRenderingExtensions.TOP,
                                                         (size * 0.15), 0.5,
                                                         self._kRenderingExtensions.H_CENTRAL,
                                                         self._kRenderingExtensions.V_CENTRAL,
                                                         0, 0,
                                                         size, size)
        # Add input port
        in_ = self._kPortExtensions.createPort()
        node.getPorts().append(in_)
        in_.setSize(0, 0)
        DiagramSyntheses.setLayoutOption(in_, CoreOptions.PORT_SIDE, PortSide.WEST)
        DiagramSyntheses.setLayoutOption(in_, CoreOptions.PORT_BORDER_OFFSET, -size / (float(4)))
        # Add output port
        out = self._kPortExtensions.createPort()
        node.getPorts().append(out)
        DiagramSyntheses.setLayoutOption(out, CoreOptions.PORT_SIDE, PortSide.EAST)
        DiagramSyntheses.setLayoutOption(out, CoreOptions.PORT_BORDER_OFFSET, -size / (float(4)))
        return (in_, out)

    def addErrorMessage(self, node, title, message):
        """
        Creates and adds an error message figure
        :param node:
        :param title:
        :param message:
        :return:
        """

        # Create figure for error message
        figure = self._kRenderingExtensions.addRectangle(node)
        self._kRenderingExtensions.setInvisible(figure, True)
        # Add error message box
        errMsgBox = self._kContainerRenderingExtensions.addRoundedRectangle(figure, 7, 7)
        self._kContainerRenderingExtensions.setGridPlacement(errMsgBox, 1)
        self._kRenderingExtensions.setLineWidth(errMsgBox, 2)
        self._linguaFrancaStyleExtensions.noSelectionStyle(errMsgBox)
        if title is not None:
            # Add title to error message box
            titleText = self._kContainerRenderingExtensions.addText(errMsgBox, title)
            self._kRenderingExtensions.setFontSize(titleText, 12)
            self._kRenderingExtensions.setFontBold(titleText, True)
            self._kRenderingExtensions.setForeground(titleText, Colors.RED)
            self.setGridPlacementDataFromPointToPoint(titleText,
                                                      self._kRenderingExtensions.LEFT,
                                                      8, 0,
                                                      self._kRenderingExtensions.TOP,
                                                      8, 0,
                                                      self._kRenderingExtensions.RIGHT,
                                                      8, 0,
                                                      self._kRenderingExtensions.BOTTOM,
                                                      4, 0)
            DiagramSyntheses.suppressSelectability(titleText)
            self._linguaFrancaStyleExtensions.noSelectionStyle(titleText)
        if message is not None:
            # Add message to error message box
            msgText = self._kContainerRenderingExtensions.addText(errMsgBox, message)
            if title is not None:
                self.setGridPlacementDataFromPointToPoint(msgText,
                                                          self._kRenderingExtensions.LEFT,
                                                          8, 0,
                                                          self._kRenderingExtensions.TOP,
                                                          0, 0,
                                                          self._kRenderingExtensions.RIGHT,
                                                          8, 0,
                                                          self._kRenderingExtensions.BOTTOM,
                                                          4, 0)
            else:
                self.setGridPlacementDataFromPointToPoint(msgText,
                                                          self._kRenderingExtensions.LEFT,
                                                          8, 0,
                                                          self._kRenderingExtensions.TOP,
                                                          8, 0,
                                                          self._kRenderingExtensions.RIGHT,
                                                          8, 0,
                                                          self._kRenderingExtensions.BOTTOM,
                                                          8, 0)
            self._linguaFrancaStyleExtensions.noSelectionStyle(msgText)
        return figure

    def addCommentFigure(self, node, message):
        """

        :param node:
        :param message:
        :return:
        """
        # Create rectangle for comment figure
        commentFigure = self._kRenderingExtensions.addRoundedRectangle(node, 1, 1, 1)
        self._kContainerRenderingExtensions.setGridPlacement(commentFigure, 1)
        # Add message
        text = self._kContainerRenderingExtensions.addText(commentFigure, message)
        self._kRenderingExtensions.setFontSize(text, 6)
        self.setGridPlacementDataFromPointToPoint(text,
                                                  self._kRenderingExtensions.LEFT,
                                                  3, 0,
                                                  self._kRenderingExtensions.TOP,
                                                  3, 0,
                                                  self._kRenderingExtensions.RIGHT,
                                                  3, 0,
                                                  self._kRenderingExtensions.BOTTOM,
                                                  3, 0)
        self._linguaFrancaStyleExtensions.noSelectionStyle(text)
        return commentFigure

    def setGridPlacementDataFromPointToPoint(self, rendering,
                                             fPx, fAbsoluteLR, fRelativeLR,
                                             fPy, fAbsoluteTB, fRelativeTB,
                                             tPx, tAbsoluteLR, tRelativeLR,
                                             tPy, tAbsoluteTB, tRelativeTB):
        """ generated source for method setGridPlacementDataFromPointToPoint """
        fromPoint = self._kRenderingExtensions.from_(self._kRenderingExtensions.setGridPlacementData(rendering),
                                                     fPx, fAbsoluteLR, fRelativeLR,
                                                     fPy, fAbsoluteTB, fRelativeTB)
        return self._kRenderingExtensions.to(fromPoint,
                                             tPx, tAbsoluteLR, tRelativeLR,
                                             tPy, tAbsoluteTB, tRelativeTB)

    def addCommentPolyline(self, edge):
        """ generated source for method addCommentPolyline """
        polyline = self._kEdgeExtensions.addPolyline(edge)
        self._kRenderingExtensions.setLineWidth(polyline, 1)
        self._kRenderingExtensions.setLineStyle(polyline, LineStyle.DOT)
        return polyline

    def addParameterEntry(self, parent, associate, text):
        """ generated source for method addParameterEntry """
        container = self._kContainerRenderingExtensions.addRectangle(parent)
        self._kRenderingExtensions.setInvisible(container, True)
        ktext = self._kContainerRenderingExtensions.addText(container, text)
        self._kRenderingExtensions.setFontSize(ktext, 8)
        self._kRenderingExtensions.setPointPlacementData(ktext, self._kRenderingExtensions.LEFT, 10, 0, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 0, 0)
        self.associateWith(ktext, associate)
        dot = self._kContainerRenderingExtensions.addEllipse(container)
        self._kRenderingExtensions.setLineWidth(dot, 1)
        self._linguaFrancaStyleExtensions.noSelectionStyle(dot)
        self._kRenderingExtensions.setPointPlacementData(dot, self._kRenderingExtensions.LEFT, 2, 0, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 5, 5)
        return container

    def addStateEntry(self, parent, associate, text, reset):
        """ generated source for method addStateEntry """
        container = self._kContainerRenderingExtensions.addRectangle(parent)
        self._kRenderingExtensions.setInvisible(container, True)
        ktext = self._kContainerRenderingExtensions.addText(container, text)
        self._kRenderingExtensions.setFontSize(ktext, 8)
        self._kRenderingExtensions.setPointPlacementData(ktext, self._kRenderingExtensions.LEFT, 10, 0, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 0, 0)
        self.associateWith(ktext, associate)
        outerCircle = None
        if reset:
            outerCircle = self._kContainerRenderingExtensions.addEllipse(container)
            self._kRenderingExtensions.setLineWidth(outerCircle, 0.9)
            self._kRenderingExtensions.setBackground(outerCircle, Colors.WHITE)
            self._linguaFrancaStyleExtensions.noSelectionStyle(outerCircle)
            self._kRenderingExtensions.setPointPlacementData(outerCircle, self._kRenderingExtensions.LEFT, 1.5, 0, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 6.3, 6.3)
            resetCycleGap = self._kContainerRenderingExtensions.addPolygon(outerCircle)
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0, 0, PositionReferenceY.TOP, 0.26, 0))
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0, 0.2, PositionReferenceY.TOP, 0.1, 0))
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0, 0.5, PositionReferenceY.TOP, 0.0, 0))
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 0, 0.2, PositionReferenceY.TOP, 0.1, 0))
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 0, 0, PositionReferenceY.TOP, 0.26, 0))
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 0.5, 0, PositionReferenceY.BOTTOM, 0, 0))
            resetCycleGap.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0.5, 0, PositionReferenceY.BOTTOM, 0, 0))
            self._kRenderingExtensions.setLineWidth(resetCycleGap, 0.3)
            self._kRenderingExtensions.setForeground(resetCycleGap, Colors.WHITE)
            self._kRenderingExtensions.setBackground(resetCycleGap, Colors.WHITE)
            self._linguaFrancaStyleExtensions.noSelectionStyle(resetCycleGap)
            self._kRenderingExtensions.setPointPlacementData(resetCycleGap, self._kRenderingExtensions.LEFT, -1.2, 0.5, self._kRenderingExtensions.TOP, 0.75, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 2.5, 1.3)
            resetArrow = self._kContainerRenderingExtensions.addPolygon(outerCircle)
            resetArrow.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0, 0, PositionReferenceY.TOP, 0.0, 0.1))
            resetArrow.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.LEFT, 0.0, 0.3, PositionReferenceY.BOTTOM, 0, 0))
            resetArrow.getPoints().append(self._kRenderingExtensions.createKPosition(PositionReferenceX.RIGHT, 0.0, 0, PositionReferenceY.TOP, 0.0, 0.0))
            self._kRenderingExtensions.setLineWidth(resetArrow, 0.3)
            self._kRenderingExtensions.setBackground(resetArrow, Colors.BLACK)
            self._linguaFrancaStyleExtensions.noSelectionStyle(resetArrow)
            self._kRenderingExtensions.setPointPlacementData(resetArrow, self._kRenderingExtensions.LEFT, 0.8, 0.5, self._kRenderingExtensions.TOP, 1.1, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 1.5, 1.5)
        else:
            outerCircle = self._kContainerRenderingExtensions.addEllipse(container)
            self._kRenderingExtensions.setLineWidth(outerCircle, 1)
            self._kRenderingExtensions.setBackground(outerCircle, Colors.WHITE)
            self._linguaFrancaStyleExtensions.noSelectionStyle(outerCircle)
            self._kRenderingExtensions.setPointPlacementData(outerCircle, self._kRenderingExtensions.LEFT, 1.5, 0, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_CENTRAL, 0, 0, 6, 6)
        innerDot = self._kContainerRenderingExtensions.addEllipse(outerCircle)
        self._kRenderingExtensions.setLineWidth(innerDot, 0.5)
        self._kRenderingExtensions.setBackground(innerDot, Colors.BLACK)
        self._linguaFrancaStyleExtensions.noSelectionStyle(innerDot)
        self._kRenderingExtensions.setPointPlacementData(innerDot, self._kRenderingExtensions.LEFT, 0, 0.5, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_CENTRAL, self._kRenderingExtensions.V_CENTRAL, 0, 0, 2.5, 2.5)
        return container
