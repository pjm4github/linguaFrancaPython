#!/usr/bin/env python
""" generated source for module LFResourceProvider """
# package: org.lflang
# import org.eclipse.emf.ecore.resource.ResourceSet
# import com.google.inject.Inject
# import com.google.inject.Provider

# 
#  * Class that provides access to a resource set.
#  * 
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  *
#  
class LFResourceProvider(object):
    """ generated source for class LFResourceProvider """
    #      * Injected resource set provider.
    #      
    resourceSetProvider = None

    #      * Return a resource set obtained from the injected provider.
    #      * @return
    #      
    def getResourceSet(self):
        """ generated source for method getResourceSet """
        return self.resourceSetProvider.get()
