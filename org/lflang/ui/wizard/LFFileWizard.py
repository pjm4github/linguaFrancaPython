#!/usr/bin/env python
""" generated source for module LFFileWizard """
# package: org.lflang.ui.wizard
# import java.io.ByteArrayInputStream
# import java.io.InputStream
# import java.nio.charset.StandardCharsets
# import org.eclipse.core.resources.IFile
# import org.eclipse.jface.viewers.IStructuredSelection
# import org.eclipse.ui.IWorkbench
# import org.eclipse.ui.IWorkbenchPage
# import org.eclipse.ui.IWorkbenchWindow
# import org.eclipse.ui.PartInitException
# import org.eclipse.ui.dialogs.WizardNewFileCreationPage
# import org.eclipse.ui.ide.IDE
# import org.eclipse.ui.internal.ide.DialogUtil
# import org.eclipse.ui.internal.wizards.newresource.ResourceMessages
# import org.eclipse.ui.plugin.AbstractUIPlugin
# import org.eclipse.ui.wizards.newresource.BasicNewResourceWizard

class LFFileWizard(BasicNewResourceWizard):
    """ generated source for class LFFileWizard """
    FILE_EXT = "lf"
    CONTENT = ""
    mainPage = None

    def addPages(self):
        """ generated source for method addPages """
        super(LFFileWizard, self).addPages()
        selection = self.getSelection()
        self.mainPage = WizardNewFileCreationPage("newFilePage", selection)
        self.mainPage.setTitle("Create Lingua Franca File")
        self.mainPage.setDescription("Create a new Lingua Franca file.")
        self.mainPage.setFileExtension(LFFileWizard.FILE_EXT)
        self.addPage(self.mainPage)

    def init(self, workbench, currentSelection):
        """ generated source for method init """
        super(LFFileWizard, self).init(workbench, currentSelection)
        self.setWindowTitle("Create new Lingua Franca File")
        self.setNeedsProgressMonitor(True)

    def initializeDefaultPageImageDescriptor(self):
        """ generated source for method initializeDefaultPageImageDescriptor """
        self.setDefaultPageImageDescriptor(AbstractUIPlugin.imageDescriptorFromPlugin("org.lflang.ui", "icons/new-lf-file-wiz.png"))

    def performFinish(self):
        """ generated source for method performFinish """
        file = self.mainPage.createNewFile()
        if file == None:
            return False
        self.selectAndReveal(file)
        dw = self.getWorkbench().getActiveWorkbenchWindow()
        try:
            if (dw != None):
                page = dw.getActivePage()
                if (page != None):
                    IDE.openEditor(page, file, True)
        except PartInitException as e:
            DialogUtil.openError(dw.getShell(), ResourceMessages.FileResource_errorMessage, e.getMessage(), e)
        return True
