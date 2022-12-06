#!/usr/bin/env python
""" generated source for module AttrParm """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Attr Parm</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.AttrParm#getName <em>Name</em>}</li>
#  *   <li>{@link org.lflang.lf.AttrParm#getValue <em>Value</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getAttrParm()
#  * @model
#  * @generated
#  
class AttrParm(EObject):
    """ generated source for interface AttrParm """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Name</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Name</em>' attribute.
    #    * @see #setName(String)
    #    * @see org.lflang.lf.LfPackage#getAttrParm_Name()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getName(self):
        """ generated source for method getName """

    #    * Sets the value of the '{@link org.lflang.lf.AttrParm#getName <em>Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Name</em>' attribute.
    #    * @see #getName()
    #    * @generated
    #    
    @abstractmethod
    def setName(self, value):
        """ generated source for method setName """

    #    * Returns the value of the '<em><b>Value</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Value</em>' containment reference.
    #    * @see #setValue(AttrParmValue)
    #    * @see org.lflang.lf.LfPackage#getAttrParm_Value()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getValue(self):
        """ generated source for method getValue """

    #    * Sets the value of the '{@link org.lflang.lf.AttrParm#getValue <em>Value</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Value</em>' containment reference.
    #    * @see #getValue()
    #    * @generated
    #    
    @abstractmethod
    def setValue(self, value):
        """ generated source for method setValue """

#  AttrParm