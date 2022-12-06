#!/usr/bin/env python
""" generated source for module Deadline """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Deadline</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Deadline#getDelay <em>Delay</em>}</li>
#  *   <li>{@link org.lflang.lf.Deadline#getCode <em>Code</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getDeadline()
#  * @model
#  * @generated
#  
class Deadline(EObject):
    """ generated source for interface Deadline """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Delay</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Delay</em>' containment reference.
    #    * @see #setDelay(Expression)
    #    * @see org.lflang.lf.LfPackage#getDeadline_Delay()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getDelay(self):
        """ generated source for method getDelay """

    #    * Sets the value of the '{@link org.lflang.lf.Deadline#getDelay <em>Delay</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Delay</em>' containment reference.
    #    * @see #getDelay()
    #    * @generated
    #    
    @abstractmethod
    def setDelay(self, value):
        """ generated source for method setDelay """

    #    * Returns the value of the '<em><b>Code</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Code</em>' containment reference.
    #    * @see #setCode(Code)
    #    * @see org.lflang.lf.LfPackage#getDeadline_Code()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getCode(self):
        """ generated source for method getCode """

    #    * Sets the value of the '{@link org.lflang.lf.Deadline#getCode <em>Code</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Code</em>' containment reference.
    #    * @see #getCode()
    #    * @generated
    #    
    @abstractmethod
    def setCode(self, value):
        """ generated source for method setCode """

#  Deadline