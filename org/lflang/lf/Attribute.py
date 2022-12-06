#!/usr/bin/env python
""" generated source for module Attribute """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Attribute</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Attribute#getAttrName <em>Attr Name</em>}</li>
#  *   <li>{@link org.lflang.lf.Attribute#getAttrParms <em>Attr Parms</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getAttribute()
#  * @model
#  * @generated
#  
class Attribute(EObject):
    """ generated source for interface Attribute """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Attr Name</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Attr Name</em>' attribute.
    #    * @see #setAttrName(String)
    #    * @see org.lflang.lf.LfPackage#getAttribute_AttrName()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getAttrName(self):
        """ generated source for method getAttrName """

    #    * Sets the value of the '{@link org.lflang.lf.Attribute#getAttrName <em>Attr Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Attr Name</em>' attribute.
    #    * @see #getAttrName()
    #    * @generated
    #    
    @abstractmethod
    def setAttrName(self, value):
        """ generated source for method setAttrName """

    #    * Returns the value of the '<em><b>Attr Parms</b></em>' containment reference list.
    #    * The list contents are of type {@link org.lflang.lf.AttrParm}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Attr Parms</em>' containment reference list.
    #    * @see org.lflang.lf.LfPackage#getAttribute_AttrParms()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getAttrParms(self):
        """ generated source for method getAttrParms """

#  Attribute
