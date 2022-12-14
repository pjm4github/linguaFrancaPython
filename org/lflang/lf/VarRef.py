#!/usr/bin/env python
""" generated source for module VarRef """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Var Ref</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.VarRef#getVariable <em>Variable</em>}</li>
#  *   <li>{@link org.lflang.lf.VarRef#getContainer <em>Container</em>}</li>
#  *   <li>{@link org.lflang.lf.VarRef#isInterleaved <em>Interleaved</em>}</li>
#  *   <li>{@link org.lflang.lf.VarRef#getTransition <em>Transition</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getVarRef()
#  * @model
#  * @generated
#  
class VarRef(TriggerRef):
    """ generated source for interface VarRef """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Variable</b></em>' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Variable</em>' reference.
    #    * @see #setVariable(Variable)
    #    * @see org.lflang.lf.LfPackage#getVarRef_Variable()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getVariable(self):
        """ generated source for method getVariable """

    #    * Sets the value of the '{@link org.lflang.lf.VarRef#getVariable <em>Variable</em>}' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Variable</em>' reference.
    #    * @see #getVariable()
    #    * @generated
    #    
    @abstractmethod
    def setVariable(self, value):
        """ generated source for method setVariable """

    #    * Returns the value of the '<em><b>Container</b></em>' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Container</em>' reference.
    #    * @see #setContainer(Instantiation)
    #    * @see org.lflang.lf.LfPackage#getVarRef_Container()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getContainer(self):
        """ generated source for method getContainer """

    #    * Sets the value of the '{@link org.lflang.lf.VarRef#getContainer <em>Container</em>}' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Container</em>' reference.
    #    * @see #getContainer()
    #    * @generated
    #    
    @abstractmethod
    def setContainer(self, value):
        """ generated source for method setContainer """

    #    * Returns the value of the '<em><b>Interleaved</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Interleaved</em>' attribute.
    #    * @see #setInterleaved(boolean)
    #    * @see org.lflang.lf.LfPackage#getVarRef_Interleaved()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def isInterleaved(self):
        """ generated source for method isInterleaved """

    #    * Sets the value of the '{@link org.lflang.lf.VarRef#isInterleaved <em>Interleaved</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Interleaved</em>' attribute.
    #    * @see #isInterleaved()
    #    * @generated
    #    
    @abstractmethod
    def setInterleaved(self, value):
        """ generated source for method setInterleaved """

    #    * Returns the value of the '<em><b>Transition</b></em>' attribute.
    #    * The literals are from the enumeration {@link org.lflang.lf.ModeTransition}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Transition</em>' attribute.
    #    * @see org.lflang.lf.ModeTransition
    #    * @see #setTransition(ModeTransition)
    #    * @see org.lflang.lf.LfPackage#getVarRef_Transition()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getTransition(self):
        """ generated source for method getTransition """

    #    * Sets the value of the '{@link org.lflang.lf.VarRef#getTransition <em>Transition</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Transition</em>' attribute.
    #    * @see org.lflang.lf.ModeTransition
    #    * @see #getTransition()
    #    * @generated
    #    
    @abstractmethod
    def setTransition(self, value):
        """ generated source for method setTransition """

#  VarRef
