#!/usr/bin/env python
""" generated source for module EclipseBasedShouldGenerateLF """
# 
#  * Copyright (c) 2015, 2020 itemis AG (http://www.itemis.eu) and others.
#  * This program and the accompanying materials are made available under the
#  * terms of the Eclipse Public License 2.0 which is available at
#  * http://www.eclipse.org/legal/epl-2.0.
#  * 
#  * SPDX-License-Identifier: EPL-2.0
#  
# package: org.lflang.ui
# import java.util.Objects

import org.apache.log4j.Logger
# import org.eclipse.core.resources.IMarker
# import org.eclipse.core.resources.IResource
# import org.eclipse.core.resources.ResourcesPlugin
# import org.eclipse.core.runtime.CoreException
# import org.eclipse.core.runtime.Path
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.generator.IShouldGenerate
# import org.eclipse.xtext.util.CancelIndicator
# import org.eclipse.xtext.workspace.IProjectConfig
# import org.eclipse.xtext.workspace.ProjectConfigAdapter

from org.lflang.generator import EclipseErrorReporter
# import com.google.inject.Singleton

# 
#  * The class checks if the resource does not contain any error markers, and is contained in an Eclipse project. It returns true if both the
#  * conditions are met.
#  * 
#  * Original: org.eclipse.xtext.ui.generator.EclipseBasedShouldGenerate
#  * 
#  * @author Sven Efftinge - Initial contribution and API
#  * @author Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de> - adjustment for LF
#  
class EclipseBasedShouldGenerateLF(IShouldGenerate):
    """ generated source for class EclipseBasedShouldGenerateLF """
    def shouldGenerate(self, resource, cancelIndicator):
        """ generated source for method shouldGenerate """
        uri = resource.getURI()
        if uri == None or not uri.isPlatformResource():
            return False
        member = ResourcesPlugin.getWorkspace().getRoot().findMember(Path(uri.toPlatformString(True)))
        if member != None and member.getType() == IResource.FILE:
            projectConfigAdapter = ProjectConfigAdapter.findInEmfObject(resource.getResourceSet())
            if projectConfigAdapter != None:
                projectConfig = projectConfigAdapter.getProjectConfig()
                if projectConfig != None and Objects == member.getProject(.__name__, projectConfig.__name__):
                    try:
                        for marker in member.findMarkers(None, True, IResource.DEPTH_INFINITE):
                            if marker.getAttribute(IMarker.SEVERITY, IMarker.SEVERITY_INFO) == IMarker.SEVERITY_ERROR and not marker.getAttribute(EclipseErrorReporter.__class__.__name__, False):
                                return False
                        return True
                    except CoreException as e:
                        self.LOG.error("The resource " + member.__name__ + " does not exist", e)
                        return False
        return False

EclipseBasedShouldGenerateLF.LOG = Logger.getLogger(EclipseBasedShouldGenerateLF.__class__)
