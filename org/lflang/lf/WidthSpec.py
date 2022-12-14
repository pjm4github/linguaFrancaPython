#!/usr/bin/env python
""" generated source for module WidthSpec """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Width Spec</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.WidthSpec#isOfVariableLength <em>Of Variable Length</em>}</li>
#  *   <li>{@link org.lflang.lf.WidthSpec#getTerms <em>Terms</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getWidthSpec()
#  * @model
#  * @generated
#  
class WidthSpec(EObject):
    """ generated source for interface WidthSpec """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Of Variable Length</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Of Variable Length</em>' attribute.
    #    * @see #setOfVariableLength(boolean)
    #    * @see org.lflang.lf.LfPackage#getWidthSpec_OfVariableLength()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def isOfVariableLength(self):
        """ generated source for method isOfVariableLength """

    #    * Sets the value of the '{@link org.lflang.lf.WidthSpec#isOfVariableLength <em>Of Variable Length</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Of Variable Length</em>' attribute.
    #    * @see #isOfVariableLength()
    #    * @generated
    #    
    @abstractmethod
    def setOfVariableLength(self, value):
        """ generated source for method setOfVariableLength """

    #    * Returns the value of the '<em><b>Terms</b></em>' containment reference list.
    #    * The list contents are of type {@link org.lflang.lf.WidthTerm}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Terms</em>' containment reference list.
    #    * @see org.lflang.lf.LfPackage#getWidthSpec_Terms()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getTerms(self):
        """ generated source for method getTerms """

#  WidthSpec
