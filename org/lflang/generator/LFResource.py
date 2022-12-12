#!/usr/bin/env python
""" generated source for module LFResource """
# package: org.lflang.generator
# import org.eclipse.emf.ecore.resource.Resource

from org.lflang.FileConfig

from org.lflang.TargetConfig

# 
#  * A class that keeps metadata for discovered resources
#  * during code generation and the supporting structures
#  * associated with that resource.
#  * 
#  * @author Soroush Bateni <soroush@utdallas.edu>
#  
class LFResource:
    """ generated source for class LFResource """
    def __init__(self, resource, fileConfig, targetConfig):
        """ generated source for method __init__ """
        self.eResource = resource
        self.fileConfig = fileConfig
        self.targetConfig = targetConfig

    #      * Resource associated with a file either from the main .lf
    #      * file or one of the imported ones.
    #      
    eResource = None

    def getEResource(self):
        """ generated source for method getEResource """
        return self.eResource

    #      * The file config associated with 'resource' that can be
    #      * used to discover files relative to that resource.
    #      
    fileConfig = None

    def getFileConfig(self):
        """ generated source for method getFileConfig """
        return self.fileConfig

    #      * The target config read from the resource.
    #      
    targetConfig = None

    def getTargetConfig(self):
        """ generated source for method getTargetConfig """
        return self.targetConfig
