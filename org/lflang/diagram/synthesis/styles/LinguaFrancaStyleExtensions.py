#!/usr/bin/env python
""" generated source for module LinguaFrancaStyleExtensions """
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
# import de.cau.cs.kieler.klighd.internal.util.KlighdInternalProperties
# import de.cau.cs.kieler.klighd.kgraph.KEdge
# import de.cau.cs.kieler.klighd.kgraph.KLabel
# import de.cau.cs.kieler.klighd.kgraph.KPort
# import de.cau.cs.kieler.klighd.krendering.Colors
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KDecoratorPlacementData
# import de.cau.cs.kieler.klighd.krendering.KEllipse
# import de.cau.cs.kieler.klighd.krendering.KPolygon
# import de.cau.cs.kieler.klighd.krendering.KPolyline
# import de.cau.cs.kieler.klighd.krendering.KRectangle
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import de.cau.cs.kieler.klighd.krendering.KRenderingFactory
# import de.cau.cs.kieler.klighd.krendering.KRoundedRectangle
# import de.cau.cs.kieler.klighd.krendering.KSpline
# import de.cau.cs.kieler.klighd.krendering.KText
# import de.cau.cs.kieler.klighd.krendering.Underline
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.krendering.extensions.KContainerRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KPolylineExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KRenderingExtensions
# import de.cau.cs.kieler.klighd.labels.decoration.IDecoratorRenderingProvider
# import de.cau.cs.kieler.klighd.labels.decoration.LabelDecorationConfigurator
# import java.util.List
# import javax.inject.Inject
# import org.eclipse.elk.core.math.ElkPadding
# import org.eclipse.elk.graph.properties.Property
# import org.eclipse.emf.ecore.util.EcoreUtil
# import org.eclipse.xtext.xbase.lib.Extension
from io import BytesIO

from include.KeilerClasses import KRenderingFactory, KPort, KPolyline, KEdge, KRenderingExtensions, \
    KContainerRenderingExtensions, KPolylineExtensions
from org.lflang.diagram.synthesis import AbstractSynthesisExtensions
import configparser
config = configparser.RawConfigParser()

# 
#  * Extension class that provides styles and coloring for the Lingua France diagram synthesis.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#


class LayerConstraint:
    pass


class LinesDecorator:
    pass


class FixedAlignment:
    pass


class Colors:
    pass


class Color:
    pass


class Underline:
    pass


class LabelDecorationConfigurator:
    pass


class IDecoratorRenderingProvider:
    pass


class EcoreUtil:
    pass


class LinguaFrancaStyleExtensions(AbstractSynthesisExtensions):
    """ generated source for class LinguaFrancaStyleExtensions """
    #  
    #      * INTERNAL property to communicate a node's background color. 
    #      
    LABEL_PARENT_BACKGROUND = config.get("org.lflang.linguafranca.diagram.synthesis.styles.label.parent.background", Colors.WHITE)
    CLOUD_WIDTH = 20

    def __init__(self):
        self._kRenderingExtensions = KRenderingExtensions()
        self._kContainerRenderingExtensions = KContainerRenderingExtensions()
        self._kPolylineExtensions = KPolylineExtensions()
        self._kRenderingFactory = KRenderingFactory.eINSTANCE
        self._onEdgeLabelConfigurator = None
        self._onEdgeDelayLabelConfigurator = None
        self._onEdgePysicalDelayLabelConfigurator = None
        self._onEdgePysicalLabelConfigurator = None

    def noSelectionStyle(self, r):
        """ generated source for method noSelectionStyle """
        return self._kRenderingExtensions.setSelectionTextStrikeout(r, False)

    def underlineSelectionStyle(self, r):
        """ generated source for method underlineSelectionStyle """
        return self._kRenderingExtensions.setSelectionTextUnderline(r, Underline.SINGLE)

    def boldLineSelectionStyle(self, r):
        """ generated source for method boldLineSelectionStyle """
        lineWidthValue = self._kRenderingExtensions.getLineWidthValue(r)
        return self._kRenderingExtensions.setSelectionLineWidth(r, lineWidthValue * 2)

    def boldTextSelectionStyle(self, t):
        """ generated source for method boldTextSelectionStyle """
        return self._kRenderingExtensions.setSelectionFontBold(t, True)

    def errorStyle(self, r):
        """ generated source for method errorStyle """
        self._kRenderingExtensions.setForeground(r, Colors.RED)
        self._kRenderingExtensions.setLineWidth(r, 2)
        self._kRenderingExtensions.setSelectionLineWidth(r, 3)
        #  Set background color the body if its a port or an line decorator
        if isinstance(r.eContainer(), KPort) or isinstance(r.eContainer(), KPolyline):
            self._kRenderingExtensions.setBackground(r, Colors.RED)
            self._kRenderingExtensions.getBackground(r).setPropagateToChildren(True)
            self._kRenderingExtensions.getForeground(r).setPropagateToChildren(True)
            self._kRenderingExtensions.getLineWidth(r).setPropagateToChildren(True)
        elif isinstance(r.eContainer(), KEdge) and isinstance(r, KPolyline):
            #  As a workaround for a rendering issue in Klighd VSCode, the style is applied to polyline
            #  children directly because a propagated background would lead to a filled edge area.
            #  See https://github.com/kieler/klighd-vscode/issues/67
            #  If fixed this commit can be reverted
            for c in r.getChildren():
                BytesIO.print(r.getChildren().errorStyle(c))

    def commentStyle(self, r):
        """ generated source for method commentStyle """
        self._kRenderingExtensions.setForeground(r, Colors.LIGHT_GOLDENROD)
        self._kRenderingExtensions.setBackground(r, Colors.PALE_GOLDENROD)
        self._kRenderingExtensions.setLineWidth(r, 1)
        self._kRenderingExtensions.setSelectionLineWidth(r, 2)
        if isinstance(r.eContainer(), KEdge):
            #  also color potential arrow heads
            self._kRenderingExtensions.setBackground(r, Colors.LIGHT_GOLDENROD)
            self._kRenderingExtensions.getBackground(r).setPropagateToChildren(True)
            self._kRenderingExtensions.getForeground(r).setPropagateToChildren(True)
            self._kRenderingExtensions.getLineWidth(r).setPropagateToChildren(True)

    def addCloudIcon(self, parent):
        """ generated source for method addCloudIcon """
        figure = self._kContainerRenderingExtensions.addRectangle(parent)
        self._kRenderingExtensions.setInvisible(figure, True)
        roundRectangle = self._kContainerRenderingExtensions.addRoundedRectangle(figure, self.CLOUD_WIDTH / 7, self.CLOUD_WIDTH / 7)
        self._kRenderingExtensions.setBackground(roundRectangle, Colors.GRAY)
        self._kRenderingExtensions.setForeground(roundRectangle, Colors.GRAY)
        self._kRenderingExtensions.setPointPlacementData(roundRectangle, self._kRenderingExtensions.LEFT, 2, 0, self._kRenderingExtensions.TOP, 0, 0.5, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_TOP, 0, 0, self.CLOUD_WIDTH, self.CLOUD_WIDTH / 3)
        childEllipse = self._kContainerRenderingExtensions.addEllipse(figure)
        self._kRenderingExtensions.setBackground(childEllipse, Colors.GRAY)
        self._kRenderingExtensions.setForeground(childEllipse, Colors.GRAY)
        self._kRenderingExtensions.setPointPlacementData(childEllipse, self._kRenderingExtensions.LEFT, 0, 0, self._kRenderingExtensions.TOP, 0, 0.38, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_TOP, 0, 0, self.CLOUD_WIDTH / 2.5, self.CLOUD_WIDTH / 2.5)
        childEllipse = self._kContainerRenderingExtensions.addEllipse(figure)
        self._kRenderingExtensions.setBackground(childEllipse, Colors.GRAY)
        self._kRenderingExtensions.setForeground(childEllipse, Colors.GRAY)
        self._kRenderingExtensions.setPointPlacementData(childEllipse, self._kRenderingExtensions.LEFT, 0, 0.5, self._kRenderingExtensions.TOP, 0, 0.25, self._kRenderingExtensions.H_RIGHT, self._kRenderingExtensions.V_TOP, 0, 0, self.CLOUD_WIDTH / 3, self.CLOUD_WIDTH / 3)
        childEllipse = self._kContainerRenderingExtensions.addEllipse(figure)
        self._kRenderingExtensions.setBackground(childEllipse, Colors.GRAY)
        self._kRenderingExtensions.setForeground(childEllipse, Colors.GRAY)
        self._kRenderingExtensions.setPointPlacementData(childEllipse, self._kRenderingExtensions.LEFT, 0, 0.4, self._kRenderingExtensions.TOP, self.CLOUD_WIDTH / 10, 0, self._kRenderingExtensions.H_LEFT, self._kRenderingExtensions.V_TOP, 0, 0, self.CLOUD_WIDTH / 2, self.CLOUD_WIDTH / 2)
        return figure

    def addCloudUploadIcon(self, parent):
        """ generated source for method addCloudUploadIcon """
        cloudIcon = self.addCloudIcon(parent)
        cloudPolygon = self._kContainerRenderingExtensions.addPolygon(cloudIcon)
        self._kRenderingExtensions.setBackground(cloudPolygon, Colors.WHITE)
        self._kRenderingExtensions.setForeground(cloudPolygon, Colors.WHITE)
        TOP = 0
        LEFT = 0
        cloudPolygon.getPoints().extend([self._kRenderingExtensions.createKPosition(LEFT, -1.5, 0.5, TOP, self.CLOUD_WIDTH / 3, 0.5),
                                         self._kRenderingExtensions.createKPosition(LEFT, -1.5, 0.5, TOP, 0, 0.58),
                                         self._kRenderingExtensions.createKPosition(LEFT, (-4), 0.5, TOP, 0, 0.58),
                                         self._kRenderingExtensions.createKPosition(LEFT, 0, 0.5, TOP, 0, 0.35),
                                         self._kRenderingExtensions.createKPosition(LEFT, 4, 0.5, TOP, 0, 0.58),
                                         self._kRenderingExtensions.createKPosition(LEFT, 1.5, 0.5, TOP, 0, 0.58),
                                         self._kRenderingExtensions.createKPosition(LEFT, 1.5, 0.5, TOP,
                                                                                    self.CLOUD_WIDTH / 3, 0.5)])
        return cloudIcon

    #  ONLY for use in applyOnEdgeStyle
    def applyOnEdgeStyle(self, label):
        """ generated source for method applyOnEdgeStyle """
        if self._onEdgeLabelConfigurator == None:
            configurator = LabelDecorationConfigurator.create().withInlineLabels(True)
            #               _onEdgeLabelConfigurator = configurator.withLabelTextRenderingProvider(
            #                       (KContainerRendering container, KLabel klabel) -> {
            #                   KText kText = _kRenderingFactory.createKText();
            #                   _kRenderingExtensions.setFontSize(kText, 9);
            #                   container.getChildren().append(kText);
            #                   return kText;
            #               });
        self._onEdgeLabelConfigurator.applyTo(label)

    #  ONLY for use in applyOnEdgeDelayStyle
    def applyOnEdgeDelayStyle(self, label):
        """ generated source for method applyOnEdgeDelayStyle """
        #          if (_onEdgeDelayLabelConfigurator == null) {
        #              LabelDecorationConfigurator configurator = LabelDecorationConfigurator.create().withInlineLabels(true);
        #              configurator = configurator.withLabelTextRenderingProvider(
        #                  (KContainerRendering container, KLabel klabel) -> {
        #                      KText kText = _kRenderingFactory.createKText();
        #                      _kRenderingExtensions.setFontSize(kText, 8);
        #                      boldTextSelectionStyle(kText);
        #                      kText.setProperty(KlighdInternalProperties.MODEL_ELEMEMT,
        #                              klabel.getProperty(KlighdInternalProperties.MODEL_ELEMEMT));
        #                      container.getChildren().append(kText);
        #                      return kText;
        #                  }
        #              );
        #              configurator = configurator.addDecoratorRenderingProvider(new IDecoratorRenderingProvider() {
        #                  @Override
        #                  public ElkPadding createDecoratorRendering(
        #                          KContainerRendering container, KLabel label,
        #                          LabelDecorationConfigurator.LayoutMode layoutMode) {
        #                      ElkPadding padding =  new ElkPadding();
        #                      padding.top = 1;
        #                      padding.bottom = 1;
        #                      padding.left = 2;
        #                      padding.right = 2;
            #                      KPolygon polygon = _kRenderingFactory.createKPolygon();
        #                      _kRenderingExtensions.from(polygon, LEFT, (-2), 0, BOTTOM, 0, 0);
        #                      _kRenderingExtensions.to(polygon, LEFT, 2, 0, TOP, 0, 0);
        #                      _kRenderingExtensions.to(polygon, RIGHT, (-2), 0, TOP, 0, 0);
        #                      _kRenderingExtensions.to(polygon, RIGHT, 2, 0, BOTTOM, 0, 0);
        #                      _kRenderingExtensions.setBackground(polygon, Colors.WHITE);
        #                      _kRenderingExtensions.setForeground(polygon, Colors.WHITE);
        #                      container.getChildren().append(polygon);
            #                      KPolyline polyline = _kRenderingFactory.createKPolyline();
        #                      _kRenderingExtensions.from(polyline, LEFT, (-2), 0, BOTTOM, 0, 0);
        #                      _kRenderingExtensions.to(polyline, LEFT, 2, 0, TOP, 0, 0);
        #                      container.getChildren().append(polyline);
            #                      polyline = _kRenderingFactory.createKPolyline();
        #                      _kRenderingExtensions.from(polyline, RIGHT, 2, 0, BOTTOM, 0, 0);
        #                      _kRenderingExtensions.to(polyline, RIGHT, (-2), 0, TOP, 0, 0);
        #                      container.getChildren().append(polyline);
            #                      return padding;
        #                  }
        #              });
        #              _onEdgeDelayLabelConfigurator = configurator;
        #          }
        self._onEdgeDelayLabelConfigurator.applyTo(label)

    #  ONLY for use in applyOnEdgePysicalDelayStyle
    def applyOnEdgePysicalDelayStyle(self, label, parentBackgroundColor):
        """ generated source for method applyOnEdgePysicalDelayStyle """
        if self._onEdgePysicalDelayLabelConfigurator == None:
            configurator = LabelDecorationConfigurator.create().withInlineLabels(True)
            #              configurator = configurator.withLabelTextRenderingProvider(
            #                  (KContainerRendering container, KLabel klabel) -> {
            #                      KText kText = _kRenderingFactory.createKText();
            #                      _kRenderingExtensions.setFontSize(kText, 8);
            #                      boldTextSelectionStyle(kText);
            #                      kText.setProperty(KlighdInternalProperties.MODEL_ELEMEMT,
            #                              klabel.getProperty(KlighdInternalProperties.MODEL_ELEMEMT));
            #                      container.getChildren().append(kText);
            #                      return kText;
            #                  }
            #              );
            configurator = configurator.addDecoratorRenderingProvider(IDecoratorRenderingProvider())
            self._onEdgePysicalDelayLabelConfigurator = configurator
        label.setProperty(self.LABEL_PARENT_BACKGROUND, parentBackgroundColor)
        self._onEdgePysicalDelayLabelConfigurator.applyTo(label)

    #  ONLY for use in applyOnEdgePysicalStyle
    def applyOnEdgePysicalStyle(self, label, parentBackgroundColor):
        """ generated source for method applyOnEdgePysicalStyle """
        if self._onEdgePysicalLabelConfigurator == None:
            configurator = LabelDecorationConfigurator.create().withInlineLabels(True)
            #              configurator = configurator.withLabelTextRenderingProvider(
            #                  (KContainerRendering container, KLabel klabel) -> {
            #                      KText kText = _kRenderingFactory.createKText();
            #                      _kRenderingExtensions.setInvisible(kText, true);
            #                      container.getChildren().append(kText);
            #                      return kText;
            #                  }
            #              );
            #              configurator = configurator.addDecoratorRenderingProvider(new IDecoratorRenderingProvider() {
            #                  @Override
            #                  public ElkPadding createDecoratorRendering(final KContainerRendering container, final KLabel label, final LabelDecorationConfigurator.LayoutMode layoutMode) {
            #                      ElkPadding padding = new ElkPadding();
            #                      padding.top = 1;
            #                      padding.bottom = 1;
            #                      padding.left = 3;
            #                      padding.right = 3;
                    #                      KPolygon polygon = _kRenderingFactory.createKPolygon();
            #                      _kRenderingExtensions.from(polygon, LEFT, 0, 0, BOTTOM, 0, 0.5f);
            #                      _kRenderingExtensions.to(polygon, LEFT, 0, 0, TOP, 1, 0.5f);
            #                      _kRenderingExtensions.to(polygon, RIGHT, 0, 0, TOP, 1, 0.5f);
            #                      _kRenderingExtensions.to(polygon, RIGHT, 0, 0, BOTTOM, 0, 0.5f);
            #                      _kRenderingExtensions.setBackground(polygon, label.getProperty(LABEL_PARENT_BACKGROUND));
            #                      _kRenderingExtensions.setForeground(polygon, label.getProperty(LABEL_PARENT_BACKGROUND));
            #                      container.getChildren().append(polygon);
                    #                      KSpline kSpline = _kRenderingFactory.createKSpline();
            #                      _kRenderingExtensions.from(kSpline, LEFT, (-0.66f), 0, BOTTOM, (-0.5f), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 1, 0, BOTTOM, (-0.5f), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.1f, BOTTOM, 8, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.2f, BOTTOM, 0, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.3f, BOTTOM, (-8), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.4f, BOTTOM, 0, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.45f, BOTTOM, 4f, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.5f, BOTTOM, 8, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.55f, BOTTOM, 4f, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.6f, BOTTOM, 0, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.65f, BOTTOM, (-4), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.7f, BOTTOM, (-8), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.8f, BOTTOM, (-4), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0, 0.9f, BOTTOM, 0, 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, (-1), 1, BOTTOM, (-0.5f), 0.5f);
            #                      _kRenderingExtensions.to(kSpline, LEFT, 0.66f, 1, BOTTOM, (-0.5f), 0.5f);
            #                      container.getChildren().append(kSpline);
            #                      return padding;
            #                  }
            #              });
            self._onEdgePysicalLabelConfigurator = configurator
        label.setProperty(self.LABEL_PARENT_BACKGROUND, parentBackgroundColor)
        self._onEdgePysicalLabelConfigurator.applyTo(label)

    def addFixedTailArrowDecorator(self, pl):
        """ generated source for method addFixedTailArrowDecorator """
        head = self._kPolylineExtensions.addTailArrowDecorator(pl)
        placement = self._kRenderingFactory.createKDecoratorPlacementData()
        placement.setRotateWithLine(True)
        placement.setRelative(0)
        placement.setAbsolute(2)
        placement.setWidth(8)
        placement.setHeight(6)
        placement.setXOffset(-3)
        placement.setYOffset(-4)
        head.setPlacementData(placement)
        return head

    def addArrayDecorator(self, edge, size):
        """ generated source for method addArrayDecorator """
        line = self._kRenderingExtensions.getKRendering(edge)
        if isinstance(line, (KPolyline)):
            placement = self._kRenderingFactory.createKDecoratorPlacementData()
            placement.setRotateWithLine(True)
            placement.setRelative(0)
            placement.setAbsolute(6)
            slash = self._kContainerRenderingExtensions.addChild(line, self._kRenderingFactory.createKPolyline())
            slash.getPoints().append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.RIGHT, 0, 0, self._kRenderingExtensions.TOP, 0, 0))
            slash.getPoints().append(self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.LEFT, 0, 0, self._kRenderingExtensions.BOTTOM, 0, 0))
            slashPlacement = EcoreUtil.copy(placement)
            slashPlacement.setWidth(5)
            slashPlacement.setHeight(10)
            slashPlacement.setYOffset(-5)
            slash.setPlacementData(slashPlacement)
            if size != None:
                num = self._kContainerRenderingExtensions.addChild(line, self._kRenderingFactory.createKText())
                num.setText(size.__str__())
                self._kRenderingExtensions.setFontSize(num, 5)
                self.noSelectionStyle(num)
                numPlacement = EcoreUtil.copy(placement)
                numPlacement.setXOffset(2)
                num.setPlacementData(numPlacement)
