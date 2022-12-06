#!/usr/bin/env python
""" generated source for module LFProjectTemplateProvider """
# package: org.lflang.ui.wizard
# import java.io.BufferedReader
# import java.io.InputStreamReader
# import java.util.List
# import java.util.stream.Collectors
# import org.eclipse.xtext.ui.XtextProjectHelper
# import org.eclipse.xtext.ui.util.PluginProjectFactory
# import org.eclipse.xtext.ui.util.ProjectFactory
# import org.eclipse.xtext.ui.wizard.template.AbstractProjectTemplate
# import org.eclipse.xtext.ui.wizard.template.GroupTemplateVariable
# import org.eclipse.xtext.ui.wizard.template.IProjectGenerator
# import org.eclipse.xtext.ui.wizard.template.IProjectTemplateProvider
# import org.eclipse.xtext.ui.wizard.template.ProjectTemplate
# import org.eclipse.xtext.ui.wizard.template.StringSelectionTemplateVariable

# 
#  * Create a list with all project templates to be shown in the template new
#  * project wizard. Each template is able to generate one or more projects. Each
#  * project can be configured such that any number of files are included. 
#  * 
#  * NOTE:
#  * Xtext is responsible for automatically populating the contents of several
#  * files in this package based on the parameters given to the @ProjectTemplate 
#  * annotations. However, this mechanism appears to be broken.
#  * Upon adding a new template, manually add entries to messages.properties and
#  * Messages.java in order to get the template registered properly in the wizard.
#  
class LFProjectTemplateProvider(IProjectTemplateProvider):
    """ generated source for class LFProjectTemplateProvider """
    def getProjectTemplates(self):
        """ generated source for method getProjectTemplates """
        return [None] * 


class LFProjectTemplate(AbstractProjectTemplate):
    """ generated source for class LFProjectTemplate """
    def setup(self, folders):
        """ generated source for method setup """
        proj = PluginProjectFactory()
        proj.setProjectName(self.getProjectInfo().getProjectName())
        proj.setLocation(self.getProjectInfo().getLocationPath())
        proj.addProjectNatures(XtextProjectHelper.NATURE_ID)
        proj.addBuilderIds(XtextProjectHelper.BUILDER_ID)
        proj.addFolders(folders)
        return proj

    def readFromFile(self, target, fileName):
        """ generated source for method readFromFile """
        stream = self.__class__.getResourceAsStream("templates/" + target + "/" + fileName)
        str = ""
        if stream != None:
            str = BufferedReader(InputStreamReader(stream)).lines().collect(Collectors.joining("\n"))
        else:
            raise RuntimeException("Unable to open template for '" + fileName + "'")
        return str


@ProjectTemplate(label="Default", icon="project_template.png", description="<p><b>Default</b></p><p>Project with an empty main reactor.</p>")
class DefaultProject(LFProjectTemplate):
    """ generated source for class DefaultProject """
    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/Main.lf"
        self.addFile(proj, fileName, readFromFile("c", fileName))
        generator.generate(proj)


@ProjectTemplate(label="Pipeline", icon="project_template.png", description="<p><b>Parallel</b></p><p>A simple" + " pipeline pattern that exploits parallelism.</p>")
class PipelineProject(LFProjectTemplate):
    """ generated source for class PipelineProject """
    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/Pipeline.lf"
        self.addFile(proj, fileName, readFromFile("c", fileName))
        generator.generate(proj)


@ProjectTemplate(label="Federated", icon="project_template.png", description="<p><b>Federated</b></p>" + "<p>A federated \"Hello World\" program.</p>")
class FederatedProject(LFProjectTemplate):
    """ generated source for class FederatedProject """
    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/FederatedHelloWorld.lf"
        self.addFile(proj, fileName, readFromFile("c", fileName))
        generator.generate(proj)


@ProjectTemplate(label="Parallel", icon="project_template.png", description="<p><b>Parallel</b></p>" + "<p>A simple fork-join pattern that exploits parallelism.</p>")
class ParallelProject(LFProjectTemplate):
    """ generated source for class ParallelProject """
    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/Parallel.lf"
        self.addFile(proj, fileName, readFromFile("c", fileName))
        generator.generate(proj)


@ProjectTemplate(label="Hello World", icon="project_template.png", description="<p><b>Hello World</b></p>" + "<p>Print \"Hello world!\" in a target language of choice.</p>")
class HelloWorldProject(LFProjectTemplate):
    """ generated source for class HelloWorldProject """
    config = group("Configuration")
    target = combo("Target:", [None] * , "The target language to compile down to", config)

    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/HelloWorld.lf"
        if self.target.getValue() == "C++":
            addFile(proj, fileName, readFromFile("cpp", fileName))
        elif self.target.getValue() == "C":
            addFile(proj, fileName, readFromFile("c", fileName))
        elif self.target.getValue() == "Python":
            addFile(proj, fileName, readFromFile("py", fileName))
        elif self.target.getValue() == "TypeScript":
            addFile(proj, fileName, readFromFile("ts", fileName))
        generator.generate(proj)


@ProjectTemplate(label="Interactive", icon="project_template.png", description="<p><b>Interactive</b></p>" + "<p>Simulate sensor input through key strokes.</p>")
class InteractiveProject(LFProjectTemplate):
    """ generated source for class InteractiveProject """
    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src", "src/include"))
        fileName = "src/Interactive.lf"
        self.addFile(proj, fileName, readFromFile("c", fileName))
        cmakeFile = "src/include/ncurses-cmake-extension.txt"
        self.addFile(proj, cmakeFile, readFromFile("c", cmakeFile))
        generator.generate(proj)


@ProjectTemplate(label="WebServer", icon="project_template.png", description="<p><b>Web Server</b></p>" + "<p>A simple web server implemented using TypeScript.</p>")
class WebServerProject(LFProjectTemplate):
    """ generated source for class WebServerProject """
    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/WebServer.lf"
        self.addFile(proj, fileName, readFromFile("ts", fileName))
        generator.generate(proj)


@ProjectTemplate(label="ReflexGame", icon="project_template.png", description="<p><b>ReflexGame</b></p>" + "<p>A simple reflex game.</p>")
class ReflexGameProject(LFProjectTemplate):
    """ generated source for class ReflexGameProject """
    config = group("Configuration")
    target = combo("Target:", [None] * , "The target language to compile down to", config)

    def generateProjects(self, generator):
        """ generated source for method generateProjects """
        proj = setup(list("src"))
        fileName = "src/ReflexGame.lf"
        if self.target.getValue() == "C":
            self.addFile(proj, fileName, readFromFile("c", fileName))
        generator.generate(proj)
