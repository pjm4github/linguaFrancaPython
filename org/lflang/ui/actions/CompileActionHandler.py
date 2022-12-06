#!/usr/bin/env python
""" generated source for module CompileActionHandler """
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
# package: org.lflang.ui.actions
# import java.util.Collections
# import java.util.HashMap
# import java.util.LinkedList
# import java.util.List
# import java.util.stream.Collectors
# import org.eclipse.core.commands.AbstractHandler
# import org.eclipse.core.commands.ExecutionEvent
# import org.eclipse.core.commands.ExecutionException
# import org.eclipse.core.resources.IFile
# import org.eclipse.core.resources.IFolder
# import org.eclipse.core.resources.IMarker
# import org.eclipse.core.resources.IProject
# import org.eclipse.core.resources.IResource
# import org.eclipse.core.runtime.CoreException
# import org.eclipse.core.runtime.IProgressMonitor
# import org.eclipse.core.runtime.IStatus
# import org.eclipse.core.runtime.NullProgressMonitor
# import org.eclipse.core.runtime.Status
# import org.eclipse.core.runtime.jobs.Job
# import org.eclipse.emf.common.util.URI
# import org.eclipse.jface.text.ITextSelection
# import org.eclipse.jface.viewers.IStructuredSelection
# import org.eclipse.ui.PlatformUI
# import org.eclipse.ui.handlers.HandlerUtil
# import org.eclipse.ui.statushandlers.StatusManager
# import org.eclipse.xtext.builder.EclipseResourceFileSystemAccess2
# import org.eclipse.xtext.builder.MonitorBasedCancelIndicator
# import org.eclipse.xtext.generator.GeneratorContext
# import org.eclipse.xtext.generator.GeneratorDelegate
# import org.eclipse.xtext.generator.IOutputConfigurationProvider
# import org.eclipse.xtext.generator.OutputConfiguration
# import org.eclipse.xtext.resource.XtextResource
# import org.eclipse.xtext.resource.XtextResourceSet
# import org.eclipse.xtext.ui.editor.XtextEditor
# import org.eclipse.xtext.ui.editor.utils.EditorUtils
# import org.eclipse.xtext.ui.editor.validation.MarkerCreator
# import org.eclipse.xtext.ui.editor.validation.MarkerIssueProcessor
# import org.eclipse.xtext.ui.validation.MarkerTypeProvider
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.validation.CheckMode
# import org.eclipse.xtext.validation.IResourceValidator
from include.overloading import overloaded

from org.lflang.ui import LFUiModuleImpl
# import com.google.inject.Inject
# import com.google.inject.Injector

# 
#  * Action handler for invoking compilation.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class CompileActionHandler(AbstractHandler):
    """ generated source for class CompileActionHandler """
    #  -- UI Constants --
    LF_EXTENSION = "lf"
    JOB_LABEL = "Lingua Franca Compilation"
    VALIDATE_LABEL = "Validating %s"
    VALIDATE_ERROR = "Unexpected exception while validating %s: %s"
    COMPILE_LABEL = "Compiling %s"
    COMPILE_ERROR = "Unexpected exception while compiling %s: %s"
    REFRESH_LABEL = "Refreshing resources"

    #  -- Xtext classes of the LF language, provided by an Xtext injector.
    generator = None
    validator = None
    config = None
    markerCreator = None
    markerTypeProvider = None
    injector = None

    #      * Internal class for an LF file, possibly open in an editor.
    #      
    class LFFile(object):
        """ generated source for class LFFile """
        resource = None
        file = None
        project = None
        editor = None

        def __init__(self, resource, file, project, editor):
            """ generated source for method __init__ """
            self.resource = resource
            self.file = file
            self.project = project
            self.editor = editor

    def execute(self, event):
        """ generated source for method execute """
        lfFiles = LinkedList()
        selection = HandlerUtil.getActiveWorkbenchWindow(event).getActivePage().getSelection()
        if isinstance(selection, (ITextSelection)):
            xtextEditor = EditorUtils.getActiveXtextEditor(event)
            if xtextEditor != None:
                xtextDocument = xtextEditor.getDocument()
                resource = xtextEditor.getResource()
                if xtextDocument != None:
                    if xtextEditor.isDirty():
                        xtextEditor.doSave(NullProgressMonitor())
                    if resource != None:
                        lfFiles.extend(collect(resource))
        elif isinstance(selection, (IStructuredSelection)):
            for element in (selection):
                lfFiles.extend(collect(element))
        if not lfFiles.isEmpty():
            self.config.configureConsole()
            Job(self.JOB_LABEL).schedule()
        return self

    @overloaded
    def collect(self, file):
        """ generated source for method collect """
        try:
            if isinstance(file, (IFile)):
                return self.collect(file)
            elif isinstance(file, (IFolder)):
                return self.collect(file)
            elif isinstance(file, (IProject)):
                return self.collect(file)
            else:
                return Collections.emptyList()
        except Exception as e:
            return Collections.emptyList()

    @collect.register(object, IProject)
    def collect_0(self, project):
        """ generated source for method collect_0 """
        list = LinkedList()
        for member in project.members():
            list.extend(self.collect(member))
        return list

    @collect.register(object, IFolder)
    def collect_1(self, folder):
        """ generated source for method collect_1 """
        list = LinkedList()
        for member in folder.members():
            list.extend(self.collect(member))
        return list

    @collect.register(object, IFile)
    def collect_2(self, file):
        """ generated source for method collect_2 """
        list = LinkedList()
        if ((file.exists() and (file.getFileExtension() != None)) and file.getFileExtension().endsWith(CompileActionHandler.LF_EXTENSION)):
            uri = URI.createPlatformResourceURI(file.getFullPath().__str__(), True)
            resourceSet = self.injector.getInstance(XtextResourceSet.__class__)
            resource = resourceSet.getResource(uri, True)
            list.append(self.LFFile(resource, file, file.getProject(), getEditor(file)))
        return list

    def getEditor(self, file):
        """ generated source for method getEditor """
        workbench = PlatformUI.getWorkbench()
        if workbench != None:
            workbenchWindow = workbench.getActiveWorkbenchWindow()
            if workbenchWindow != None:
                page = workbenchWindow.getActivePage()
                if page != None:
                    for editorRef in page.getEditorReferences():
                        editor = editorRef.getEditor(False)
                        if (isinstance(editor, (XtextEditor))):
                            if file == (editor.getResource()):
                                return (editor)
        return None
