#!/usr/bin/env python
""" generated source for module GeneratorUtils """
# package: org.lflang.generator
# import java.io.IOException
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.ArrayList
# import java.util.HashSet
# import java.util.Iterator
# import java.util.List
# import org.eclipse.core.resources.IResource
# import org.eclipse.core.resources.ResourcesPlugin
# import org.eclipse.core.runtime.CoreException
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.generator.IGeneratorContext
# import org.eclipse.xtext.resource.XtextResource
# import org.eclipse.xtext.validation.CheckMode
# import org.eclipse.xtext.validation.IResourceValidator
# import org.eclipse.xtext.validation.Issue

#  * A helper class with functions that may be useful for code
#  * generators.
#  * This is created to ease our transition from Xtend and
#  * possibly Eclipse. All functions in this class should
#  * instead be in GeneratorUtils.kt, but Eclipse cannot
#  * handle Kotlin files.
#
import os
import sys

from traitlets import Integer

from include.MiscClasses import Paths, CheckMode
from include.SpecialExceptions import RuntimeException
from lflang.FileConfig import FileConfig
from lflang.TargetConfig import TargetConfig
from lflang.TargetProperty import TargetProperty, LogLevel, SchedulerOption
from lflang.generator.EclipseErrorReporter import IResource, CoreException
from lflang.generator.GeneratorResult import GeneratorResult
from lflang.generator.LFGeneratorContext import LFGeneratorContext
from lflang.generator.LFResource import LFResource
from lflang.lf.Action import Action
from lflang.lf.ActionOrigin import ActionOrigin
from lflang.lf.TargetDecl import TargetDecl
from lflang.util.FileUtil import FileUtil


class ResourcesPlugin:
    pass


class GeneratorUtils:
    """ generated source for class GeneratorUtils """
    def __init__(self):
        """ generated source for method __init__ """
        #  utility class

    #      * Return the target declaration found in the given resource.
    #      
    @classmethod
    def findTarget(cls, resource):
        """ generated source for method findTarget """
        ans = []
        for n in TargetDecl.__class__:
            ans.append(n.find(resource))
        return ans

    @classmethod
    def setTargetConfig(cls, context, target, targetConfig, errorReporter):
        """ generated source for method setTargetConfig """
        if target.getConfig() != None:
            pairs = target.getConfig().getPairs()
            TargetProperty.set(targetConfig, pairs if pairs != None else list(), errorReporter)
        if context.getArgs().containsKey("no-compile"):
            targetConfig.noCompile = True
        if context.getArgs().containsKey("logging"):
            targetConfig.logLevel = LogLevel.valueOf(context.getArgs().getProperty("logging").toUpperCase())
        if context.getArgs().containsKey("workers"):
            targetConfig.workers = Integer.parseInt(context.getArgs().getProperty("workers"))
        if context.getArgs().containsKey("threading"):
            targetConfig.threading = bool(int(context.getArgs().getProperty("threading")))
        if context.getArgs().containsKey("target-compiler"):
            targetConfig.compiler = context.getArgs().getProperty("target-compiler")
        if context.getArgs().containsKey("scheduler"):
            targetConfig.schedulerType = SchedulerOption.valueOf(context.getArgs().getProperty("scheduler"))
            targetConfig.setByUser.append(TargetProperty.SCHEDULER)
        if context.getArgs().containsKey("target-flags"):
            targetConfig.compilerFlags = []
            if not context.getArgs().getProperty("target-flags").isEmpty():
                targetConfig.compilerFlags.extend([list(context.getArgs().getProperty("target-flags").split(" "))])
        if context.getArgs().containsKey("runtime-version"):
            targetConfig.runtimeVersion = context.getArgs().getProperty("runtime-version")
        if context.getArgs().containsKey("external-runtime-path"):
            targetConfig.externalRuntimePath = context.getArgs().getProperty("external-runtime-path")
        if context.getArgs().containsKey(TargetProperty.KEEPALIVE.description):
            targetConfig.keepalive = bool(int(context.getArgs().getProperty(TargetProperty.KEEPALIVE.description)))

    @classmethod
    def accommodatePhysicalActionsIfPresent(cls, resources, setsKeepAliveOptionAutomatically, targetConfig, errorReporter):
        """ generated source for method accommodatePhysicalActionsIfPresent """
        if not setsKeepAliveOptionAutomatically:
            return
        for resource in resources:
            actions =[]
            for r in Action.__class__:
                if r.find(resource):
                    actions.append(r)
            for action in actions:
                if action.getOrigin() == ActionOrigin.PHYSICAL and not targetConfig.setByUser.contains(TargetProperty.KEEPALIVE) and not targetConfig.keepalive:
                    targetConfig.keepalive = True
                    errorReporter.reportWarning(action, "Setting {:s} to true because of the physical action {:s}.".format(TargetProperty.KEEPALIVE.getDisplayName(), action.__name__))
                    return

    @classmethod
    def findAll(cls, resource, nodeType):
        """ generated source for method findAll """
        contents = resource.getAllContents()
        assert contents is not None
        temp = None
        while not nodeType.isInstance(temp) and contents.hasNext():
            next_ = temp
        return None

    @classmethod
    def validate(cls, context, fileConfig, instantiationGraph, errorReporter):
        """ generated source for method validate """
        validator = (fileConfig.resource).getResourceServiceProvider().getResourceValidator()
        bad = set()
        visited = set()
        for reactor in instantiationGraph.nodesInTopologicalOrder():
            resource = reactor.eResource()
            if visited.intersection(resource):
                continue 
            visited.add(resource)
            issues = validator.validate(resource, CheckMode.ALL, context.getCancelIndicator())
            if bad.intersection(resource) or len(issues) > 0:
                path = None
                try:
                    path = FileUtil.toPath(resource)
                except IOError as e:
                    path = Paths.get("Unknown file")
                for issue in issues:
                    errorReporter.reportError(path, issue.getLineNumber(), issue.getMessage())
                for downstreamReactor in instantiationGraph.getDownstreamAdjacentNodes(reactor):
                    for importStatement in (downstreamReactor.eContainer()).getImports():
                        bad.add(downstreamReactor.eResource())

    @classmethod
    def getResources(cls, reactors):
        """ generated source for method getResources """
        visited = set()
        resources = []
        for r in reactors:
            resource = r.eResource()
            if not visited.intersection(resource):
                visited.add(resource)
                resources.append(resource)
        return resources

    @classmethod
    def getLFResource(cls, resource, srcGenBasePath, context, errorReporter):
        """ generated source for method getLFResource """
        target = GeneratorUtils.findTarget(resource)
        config = target.getConfig()
        targetConfig = TargetConfig()
        if config != None:
            pairs = config.getPairs()
            TargetProperty.set(targetConfig, pairs if pairs != None else list(), errorReporter)
        try:
            fc = FileConfig(resource, srcGenBasePath, context.useHierarchicalBin())
            return LFResource(resource, fc, targetConfig)
        except IOError as e:
            raise RuntimeException("Failed to instantiate an imported resource because an I/O error " + "occurred.")

    @classmethod
    def refreshProject(cls, resource, compilerMode):
        """ generated source for method refreshProject """
        if compilerMode == LFGeneratorContext.Mode.EPOCH:
            uri = resource.getURI()
            if uri.isPlatformResource():
                member = ResourcesPlugin.getWorkspace().getRoot().findMember(uri.toPlatformString(True))
                try:
                    member.getProject().refreshLocal(IResource.DEPTH_INFINITE, None)
                except CoreException as e:
                    sys.stderr("Unable to refresh workspace: " + e)

    @classmethod
    def isHostWindows(cls):
        """ generated source for method isHostWindows """
        return os.environ("os.name").lower().contains("win")

    @classmethod
    def canGenerate(cls, errorsOccurred, mainDef, errorReporter, context):
        """ generated source for method canGenerate """
        if errorsOccurred:
            context.finish(GeneratorResult.FAILED)
            return False
        if mainDef == None:
            errorReporter.reportInfo("INFO: The given Lingua Franca program does not define a main reactor. Therefore, no code was generated.")
            context.finish(GeneratorResult.NOTHING)
            return False
        return True
