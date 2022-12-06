#!/usr/bin/env python
""" generated source for module MethodArgument """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Method Argument</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.MethodArgument#getName <em>Name</em>}</li>
#  *   <li>{@link org.lflang.lf.MethodArgument#getType <em>Type</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getMethodArgument()
#  * @model
#  * @generated
#  
class MethodArgument(EObject):
    """ generated source for interface MethodArgument """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Name</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Name</em>' attribute.
    #    * @see #setName(String)
    #    * @see org.lflang.lf.LfPackage#getMethodArgument_Name()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getName(self):
        """ generated source for method getName """

    #    * Sets the value of the '{@link org.lflang.lf.MethodArgument#getName <em>Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Name</em>' attribute.
    #    * @see #getName()
    #    * @generated
    #    
    @abstractmethod
    def setName(self, value):
        """ generated source for method setName """

    #    * Returns the value of the '<em><b>Type</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Type</em>' containment reference.
    #    * @see #setType(Type)
    #    * @see org.lflang.lf.LfPackage#getMethodArgument_Type()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getType(self):
        """ generated source for method getType """

    #    * Sets the value of the '{@link org.lflang.lf.MethodArgument#getType <em>Type</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Type</em>' containment reference.
    #    * @see #getType()
    #    * @generated
    #    
    @abstractmethod
    def setType(self, value):
        """ generated source for method setType """

#  MethodArgument