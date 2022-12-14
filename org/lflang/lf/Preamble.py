#!/usr/bin/env python
""" generated source for module Preamble """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Preamble</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Preamble#getVisibility <em>Visibility</em>}</li>
#  *   <li>{@link org.lflang.lf.Preamble#getCode <em>Code</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getPreamble()
#  * @model
#  * @generated
#  
class Preamble(EObject):
    """ generated source for interface Preamble """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Visibility</b></em>' attribute.
    #    * The literals are from the enumeration {@link org.lflang.lf.Visibility}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Visibility</em>' attribute.
    #    * @see org.lflang.lf.Visibility
    #    * @see #setVisibility(Visibility)
    #    * @see org.lflang.lf.LfPackage#getPreamble_Visibility()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getVisibility(self):
        """ generated source for method getVisibility """

    #    * Sets the value of the '{@link org.lflang.lf.Preamble#getVisibility <em>Visibility</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Visibility</em>' attribute.
    #    * @see org.lflang.lf.Visibility
    #    * @see #getVisibility()
    #    * @generated
    #    
    @abstractmethod
    def setVisibility(self, value):
        """ generated source for method setVisibility """

    #    * Returns the value of the '<em><b>Code</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Code</em>' containment reference.
    #    * @see #setCode(Code)
    #    * @see org.lflang.lf.LfPackage#getPreamble_Code()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getCode(self):
        """ generated source for method getCode """

    #    * Sets the value of the '{@link org.lflang.lf.Preamble#getCode <em>Code</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Code</em>' containment reference.
    #    * @see #getCode()
    #    * @generated
    #    
    @abstractmethod
    def setCode(self, value):
        """ generated source for method setCode """

#  Preamble
