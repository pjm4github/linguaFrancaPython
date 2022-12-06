#!/usr/bin/env python
""" generated source for module LFStandaloneSetupGenerated """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang
import com.google.inject.Guice

import com.google.inject.Injector
# import org.eclipse.emf.ecore.EPackage
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.emf.ecore.xmi.impl.EcoreResourceFactoryImpl
# import org.eclipse.emf.ecore.xmi.impl.XMIResourceFactoryImpl
# import org.eclipse.xtext.ISetup
# import org.eclipse.xtext.XtextPackage
# import org.eclipse.xtext.resource.IResourceFactory
# import org.eclipse.xtext.resource.IResourceServiceProvider
# import org.eclipse.xtext.resource.impl.BinaryGrammarResourceFactoryImpl

from org.lflang.lf import LfPackage

@SuppressWarnings("all")
class LFStandaloneSetupGenerated(ISetup):
    """ generated source for class LFStandaloneSetupGenerated """
    def createInjectorAndDoEMFRegistration(self):
        """ generated source for method createInjectorAndDoEMFRegistration """
        #  register default ePackages
        if not Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().containsKey("ecore"):
            Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().put("ecore", EcoreResourceFactoryImpl())
        if not Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().containsKey("xmi"):
            Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().put("xmi", XMIResourceFactoryImpl())
        if not Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().containsKey("xtextbin"):
            Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().put("xtextbin", BinaryGrammarResourceFactoryImpl())
        if not EPackage.Registry.INSTANCE.containsKey(XtextPackage.eNS_URI):
            EPackage.Registry.INSTANCE.put(XtextPackage.eNS_URI, XtextPackage.eINSTANCE)
        injector = createInjector()
        register(injector)
        return injector

    def createInjector(self):
        """ generated source for method createInjector """
        return Guice.createInjector(LFRuntimeModule())

    def register(self, injector):
        """ generated source for method register """
        if not EPackage.Registry.INSTANCE.containsKey("https://lf-lang.org"):
            EPackage.Registry.INSTANCE.put("https://lf-lang.org", LfPackage.eINSTANCE)
        resourceFactory = injector.getInstance(IResourceFactory.__class__)
        serviceProvider = injector.getInstance(IResourceServiceProvider.__class__)
        Resource.Factory.Registry.INSTANCE.getExtensionToFactoryMap().put("lf", resourceFactory)
        IResourceServiceProvider.Registry.INSTANCE.getExtensionToFactoryMap().put("lf", serviceProvider)