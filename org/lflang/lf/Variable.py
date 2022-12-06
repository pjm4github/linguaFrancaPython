#!/usr/bin/env python
""" generated source for module Variable """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Variable</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Variable#getName <em>Name</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getVariable()
#  * @model
#  * @generated
#  
class Variable(EObject):
    """ generated source for interface Variable """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Name</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Name</em>' attribute.
    #    * @see #setName(String)
    #    * @see org.lflang.lf.LfPackage#getVariable_Name()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getName(self):
        """ generated source for method getName """

    #    * Sets the value of the '{@link org.lflang.lf.Variable#getName <em>Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Name</em>' attribute.
    #    * @see #getName()
    #    * @generated
    #    
    @abstractmethod
    def setName(self, value):
        """ generated source for method setName """

#  Variable
