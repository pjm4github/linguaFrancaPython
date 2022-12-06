#!/usr/bin/env python
""" generated source for module ReactorIcons """
from functools import wraps
from threading import RLock

from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import Colors


def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    @wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner

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
# package: org.lflang.diagram.synthesis.util
# import java.io.InputStream
# import java.util.HashMap
# import org.eclipse.swt.graphics.ImageData
# import org.eclipse.swt.graphics.ImageLoader
# import org.eclipse.xtext.xbase.lib.Extension

from org.lflang import ASTUtils

from org.lflang import AttributeUtils

from org.lflang.diagram.synthesis import AbstractSynthesisExtensions

from org.lflang.lf import ReactorDecl

from org.lflang.util import FileUtil
# import com.google.inject.Inject
# import de.cau.cs.kieler.klighd.krendering.Colors
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KGridPlacementData
# import de.cau.cs.kieler.klighd.krendering.KRectangle
# import de.cau.cs.kieler.klighd.krendering.ViewSynthesisShared
# import de.cau.cs.kieler.klighd.krendering.extensions.KContainerRenderingExtensions
# import de.cau.cs.kieler.klighd.krendering.extensions.KRenderingExtensions

# 
#  * Utility class to handle icons for reactors in Lingua Franca diagrams.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class ImageLoader:
    pass


class ReactorIcons(AbstractSynthesisExtensions):
    """ generated source for class ReactorIcons """
    _kRenderingExtensions = None
    _kContainerRenderingExtensions = None
    LOADER = ImageLoader()

    #  Image cache during synthesis
    cache = dict()

    #  Error message
    error = None

    def handleIcon(self, rendering, reactor, collapsed):
        """ generated source for method handleIcon """
        if not collapsed:
            return
        #  Reset error
        self.error = None
        #  Get annotation
        iconPath = AttributeUtils.findAttributeByName(reactor, "icon")
        if iconPath == None:
            #  Fallback to old syntax (in comment)
            iconPath = ASTUtils.findAnnotationInComments(reactor, "@icon")
        if iconPath != None and not iconPath.isEmpty():
            iconLocation = FileUtil.locateFile(iconPath, reactor.eResource())
            if iconLocation == None:
                self.error = "Cannot find given icon file."
            else:
                data = self.loadImage(iconLocation)
                if data != None:
                    figure = self._kContainerRenderingExtensions.addRectangle(rendering)
                    self._kRenderingExtensions.setInvisible(figure, True)
                    figurePlacement = self._kRenderingExtensions.setGridPlacementData(figure, data.width, data.height)
                    self._kRenderingExtensions.to(self._kRenderingExtensions.from_(figurePlacement, self._kRenderingExtensions.LEFT, 3, 0, self._kRenderingExtensions.TOP, 0, 0), self._kRenderingExtensions.RIGHT, 3, 0, self._kRenderingExtensions.BOTTOM, 3, 0)
                    icon = self._kContainerRenderingExtensions.addRectangle(figure)
                    self._kRenderingExtensions.setInvisible(icon, True)
                    self._kContainerRenderingExtensions.addImage(icon, data)
                    self._kRenderingExtensions.setPointPlacementData(icon, self._kRenderingExtensions.createKPosition(self._kRenderingExtensions.LEFT, 0, 0.5, self._kRenderingExtensions.TOP, 0, 0.5), self._kRenderingExtensions.H_CENTRAL, self._kRenderingExtensions.V_CENTRAL, 0, 0, data.width, data.height)
                if self.error != None:
                    errorText = self._kContainerRenderingExtensions.addText(rendering, "Icon not found!\n" + self.error)
                    self._kRenderingExtensions.setForeground(errorText, Colors.RED)
                    self._kRenderingExtensions.setFontBold(errorText, True)
                    self._kRenderingExtensions.setSurroundingSpaceGrid(errorText, 8, 0)

    def loadImage(self, uri):
        """ generated source for method loadImage """
        try:
            if self.cache.containsKey(uri):
                return self.cache.get(uri)
            with lock_for_object(self.LOADER):
                inStream = None
                try:
                    inStream = uri.toURL().openStream()
                    data = self.LOADER.load(inStream)
                    if data != None and len(data):
                        img = data[0]
                        self.cache.put(uri, img)
                        return img
                    else:
                        self.error = "Could not load icon image."
                        return None
                finally:
                    if inStream != None:
                        inStream.close()
        except Exception as ex:
            ex.printStackTrace()
            self.error = "Could not load icon image."
            return None
