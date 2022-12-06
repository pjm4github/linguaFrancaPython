#!/usr/bin/env python
""" generated source for module LFPerspectiveFactory """
# package: org.lflang.product
# import org.eclipse.ui.IFolderLayout
# import org.eclipse.ui.IPageLayout
# import org.eclipse.ui.IPerspectiveFactory

# 
#  * Perspective for modeling with lingua franca.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class LFPerspectiveFactory(IPerspectiveFactory):
    """ generated source for class LFPerspectiveFactory """
    PACKAGE_EXPLORER_ID = "org.eclipse.jdt.ui.PackageExplorer"
    KLIGHD_VIEW_ID = "de.cau.cs.kieler.klighd.ui.view.diagram"
    NEW_FILE_WIZ_ID = "org.eclipse.ui.wizards.new.file"

    #  {@inheritDoc} 
    def createInitialLayout(self, layout):
        """ generated source for method createInitialLayout """
        editor = layout.getEditorArea()
        #  create general areas relative to editor area
        left = layout.createFolder("lf_left", IPageLayout.LEFT, 0.1, editor)
        right = layout.createFolder("lf_right", IPageLayout.RIGHT, 0.4, editor)
        #  add views
        left.addView(self.PACKAGE_EXPLORER_ID)
        right.addView(self.KLIGHD_VIEW_ID)
        #  activate editor
        layout.setEditorAreaVisible(True)
        #  add shortcut in case view is closed
        layout.addShowViewShortcut(self.KLIGHD_VIEW_ID)
        #  add wizard shortcuts
        layout.addNewWizardShortcut(self.NEW_FILE_WIZ_ID)
