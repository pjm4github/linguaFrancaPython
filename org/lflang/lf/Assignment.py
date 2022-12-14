#!/usr/bin/env python
""" generated source for module Assignment """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Assignment</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Assignment#getLhs <em>Lhs</em>}</li>
#  *   <li>{@link org.lflang.lf.Assignment#getEquals <em>Equals</em>}</li>
#  *   <li>{@link org.lflang.lf.Assignment#getRhs <em>Rhs</em>}</li>
#  *   <li>{@link org.lflang.lf.Assignment#getParens <em>Parens</em>}</li>
#  *   <li>{@link org.lflang.lf.Assignment#getBraces <em>Braces</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getAssignment()
#  * @model
#  * @generated
#  
class Assignment(EObject):
    """ generated source for interface Assignment """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Lhs</b></em>' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Lhs</em>' reference.
    #    * @see #setLhs(Parameter)
    #    * @see org.lflang.lf.LfPackage#getAssignment_Lhs()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getLhs(self):
        """ generated source for method getLhs """

    #    * Sets the value of the '{@link org.lflang.lf.Assignment#getLhs <em>Lhs</em>}' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Lhs</em>' reference.
    #    * @see #getLhs()
    #    * @generated
    #    
    @abstractmethod
    def setLhs(self, value):
        """ generated source for method setLhs """

    #    * Returns the value of the '<em><b>Equals</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Equals</em>' attribute.
    #    * @see #setEquals(String)
    #    * @see org.lflang.lf.LfPackage#getAssignment_Equals()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getEquals(self):
        """ generated source for method getEquals """

    #    * Sets the value of the '{@link org.lflang.lf.Assignment#getEquals <em>Equals</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Equals</em>' attribute.
    #    * @see #getEquals()
    #    * @generated
    #    
    @abstractmethod
    def setEquals(self, value):
        """ generated source for method setEquals """

    #    * Returns the value of the '<em><b>Rhs</b></em>' containment reference list.
    #    * The list contents are of type {@link org.lflang.lf.Expression}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Rhs</em>' containment reference list.
    #    * @see org.lflang.lf.LfPackage#getAssignment_Rhs()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getRhs(self):
        """ generated source for method getRhs """

    #    * Returns the value of the '<em><b>Parens</b></em>' attribute list.
    #    * The list contents are of type {@link java.lang.String}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Parens</em>' attribute list.
    #    * @see org.lflang.lf.LfPackage#getAssignment_Parens()
    #    * @model unique="false"
    #    * @generated
    #    
    @abstractmethod
    def getParens(self):
        """ generated source for method getParens """

    #    * Returns the value of the '<em><b>Braces</b></em>' attribute list.
    #    * The list contents are of type {@link java.lang.String}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Braces</em>' attribute list.
    #    * @see org.lflang.lf.LfPackage#getAssignment_Braces()
    #    * @model unique="false"
    #    * @generated
    #    
    @abstractmethod
    def getBraces(self):
        """ generated source for method getBraces """

#  Assignment
