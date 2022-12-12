#!/usr/bin/env python
""" generated source for module LFNamesAreUniqueValidationHelper """
# package: org.lflang.validation
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.xtext.validation.NamesAreUniqueValidationHelper

from org.lflang.lf import LfPackage

class LFNamesAreUniqueValidationHelper(NamesAreUniqueValidationHelper):
    """ generated source for class LFNamesAreUniqueValidationHelper """
    #      * Lump all inputs, outputs, timers, actions, parameters, and 
    #      * instantiations in the same cluster type. This ensures that
    #      * names amongst them are checked for uniqueness.
    #      
    def getAssociatedClusterType(self, eClass):
        """ generated source for method getAssociatedClusterType """
        if LfPackage.Literals.INPUT == eClass or LfPackage.Literals.OUTPUT == eClass or LfPackage.Literals.TIMER == eClass or LfPackage.Literals.ACTION == eClass or LfPackage.Literals.PARAMETER == eClass or LfPackage.Literals.INSTANTIATION == eClass:
            return LfPackage.Literals.VARIABLE
        return super().getAssociatedClusterType(eClass)
