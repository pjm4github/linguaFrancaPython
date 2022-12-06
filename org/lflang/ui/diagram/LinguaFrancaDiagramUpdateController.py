#!/usr/bin/env python
""" generated source for module LinguaFrancaDiagramUpdateController """
# 
# Copyright (c) 2022, Kiel University.
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
# package: org.lflang.ui.diagram
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.util.EcoreUtil
# import org.eclipse.jface.viewers.SelectionChangedEvent
# import org.eclipse.xtext.ui.editor.LanguageSpecificURIEditorOpener
# import org.eclipse.xtext.ui.editor.XtextEditor
from include.KeilerClasses import KlighdInputEvent, KlighdTreeSelection, KlighdCanvas
from include.MiscClasses import EcoreXtextSaveUpdateController, PInputEventListener, LflangActivator, \
    LanguageSpecificURIEditorOpener, XtextEditor, XtextSelectionHighlighter
from lflang.diagram.synthesis.styles.LinguaFrancaStyleExtensions import EcoreUtil
from lflang.diagram.synthesis.util.LayoutPostProcessing import EObject
from lflang.ui.diagram.LinguaFrancaAdjustedKlighdTreeSelection import LinguaFrancaAdjustedKlighdTreeSelection
from org.lflang.lf import Model

# from org.lflang.ui.internal.LflangActivator import LflangActivator
# import com.google.inject.Injector
# import de.cau.cs.kieler.klighd.KlighdTreeSelection
# import de.cau.cs.kieler.klighd.piccolo.internal.KlighdCanvas
# import de.cau.cs.kieler.klighd.piccolo.internal.events.KlighdInputManager.KlighdInputEvent
# import de.cau.cs.kieler.klighd.piccolo.internal.nodes.KlighdMainCamera
# import de.cau.cs.kieler.klighd.ui.view.DiagramView
# import de.cau.cs.kieler.klighd.ui.view.controllers.EcoreXtextSaveUpdateController
# import de.cau.cs.kieler.klighd.ui.view.controllers.XtextSelectionHighlighter
# import de.cau.cs.kieler.klighd.util.KlighdSynthesisProperties

# import edu.umd.cs.piccolo.event.PInputEvent

# import edu.umd.cs.piccolo.event.PInputEventListener

# 
#  * Controller that handles the behavior between the diagram view and the Lingua Franca editor.
#  * 
#  * This class is registered and associated with the LF editor via the plugin.xml, if the class name
#  * changes, update the plugin.xml!
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  


class LinguaFrancaDiagramUpdateController(EcoreXtextSaveUpdateController, PInputEventListener):
    """ generated source for class LinguaFrancaDiagramUpdateController """

    #      * {@inheritDoc}
    #
    def __init__(self, parentDiagramView):
        #  The xtext injector for LF
        self.injector = None

        #  Xtext utility class that is normally used for jumpt-to-declaration actions in the editor
        self.uriOpener = None

        #  The camera the key listener is registered on
        self.camera = None

        #  Flag to activate code association for diagram elements which source is outside the current editor
        self.jumpToFile = False
        self.initialize(parentDiagramView)

    def getID(self):
        """ generated source for method getID """
        return self.__class__.__name__

    def initialize(self, parentDiagramView):
        """ generated source for method initialize """
        super(LinguaFrancaDiagramUpdateController, self).initialize(parentDiagramView)
        self.injector = LflangActivator.getInstance().getInjector(LflangActivator.ORG_LFLANG_LF)
        self.uriOpener = self.injector.getInstance(LanguageSpecificURIEditorOpener.__class__)

    def onDiagramUpdate(self, model, properties):
        """ generated source for method onDiagramUpdate """
        if self.getDiagramView().getViewer() is not None \
                and isinstance(self.getDiagramView().getViewer().getControl(), KlighdCanvas):
            canvas = self.getDiagramView().getViewer().getControl()
            cam = canvas.getCamera()
            if self.camera != cam:
                if self.camera != None:
                    self.camera.removeInputEventListener(self)
                self.camera = cam
                self.jumpToFile = False
                self.camera.addInputEventListener(self)

    def onDispose(self):
        """ generated source for method onDispose """
        if self.camera != None:
            self.camera.removeInputEventListener(self)

    def processEvent(self, event, type):
        """ generated source for method processEvent """
        if isinstance(event, KlighdInputEvent):
            self.jumpToFile = (event).isAltDown()

    def selectionChanged(self, event):
        """ generated source for method selectionChanged """
        if isinstance(event, XtextEditor):
            if isinstance(event.getSelection(), KlighdTreeSelection):
                selection = event.getSelection()
                if self.jumpToFile and len(selection) == 1:
                    source = selection.sourceElementIterator().next()
                    if isinstance(source, EObject):
                        sourceURI = EcoreUtil.getURI(source)
                        if self.uriOpener != None and sourceURI != None:
                            editor = self.uriOpener.open(sourceURI, False)
                            if isinstance(editor, (XtextEditor)):
                                XtextSelectionHighlighter.highlightSelection(editor, event.getSelection())
                            return
                if isinstance(self.getModel(), Model):
                    selection = LinguaFrancaAdjustedKlighdTreeSelection(selection, self.getModel())
                XtextSelectionHighlighter.highlightSelection(self.getEditor(), selection)
