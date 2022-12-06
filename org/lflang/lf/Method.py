#!/usr/bin/env python
""" generated source for module Method """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Method</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Method#isConst <em>Const</em>}</li>
#  *   <li>{@link org.lflang.lf.Method#getName <em>Name</em>}</li>
#  *   <li>{@link org.lflang.lf.Method#getArguments <em>Arguments</em>}</li>
#  *   <li>{@link org.lflang.lf.Method#getReturn <em>Return</em>}</li>
#  *   <li>{@link org.lflang.lf.Method#getCode <em>Code</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getMethod()
#  * @model
#  * @generated
#  
class Method(EObject):
    """ generated source for interface Method """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Const</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Const</em>' attribute.
    #    * @see #setConst(boolean)
    #    * @see org.lflang.lf.LfPackage#getMethod_Const()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def isConst(self):
        """ generated source for method isConst """

    #    * Sets the value of the '{@link org.lflang.lf.Method#isConst <em>Const</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Const</em>' attribute.
    #    * @see #isConst()
    #    * @generated
    #    
    @abstractmethod
    def setConst(self, value):
        """ generated source for method setConst """

    #    * Returns the value of the '<em><b>Name</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Name</em>' attribute.
    #    * @see #setName(String)
    #    * @see org.lflang.lf.LfPackage#getMethod_Name()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getName(self):
        """ generated source for method getName """

    #    * Sets the value of the '{@link org.lflang.lf.Method#getName <em>Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Name</em>' attribute.
    #    * @see #getName()
    #    * @generated
    #    
    @abstractmethod
    def setName(self, value):
        """ generated source for method setName """

    #    * Returns the value of the '<em><b>Arguments</b></em>' containment reference list.
    #    * The list contents are of type {@link org.lflang.lf.MethodArgument}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Arguments</em>' containment reference list.
    #    * @see org.lflang.lf.LfPackage#getMethod_Arguments()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getArguments(self):
        """ generated source for method getArguments """

    #    * Returns the value of the '<em><b>Return</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Return</em>' containment reference.
    #    * @see #setReturn(Type)
    #    * @see org.lflang.lf.LfPackage#getMethod_Return()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getReturn(self):
        """ generated source for method getReturn """

    #    * Sets the value of the '{@link org.lflang.lf.Method#getReturn <em>Return</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Return</em>' containment reference.
    #    * @see #getReturn()
    #    * @generated
    #    
    @abstractmethod
    def setReturn(self, value):
        """ generated source for method setReturn """

    #    * Returns the value of the '<em><b>Code</b></em>' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Code</em>' containment reference.
    #    * @see #setCode(Code)
    #    * @see org.lflang.lf.LfPackage#getMethod_Code()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getCode(self):
        """ generated source for method getCode """

    #    * Sets the value of the '{@link org.lflang.lf.Method#getCode <em>Code</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Code</em>' containment reference.
    #    * @see #getCode()
    #    * @generated
    #    
    @abstractmethod
    def setCode(self, value):
        """ generated source for method setCode """

#  Method