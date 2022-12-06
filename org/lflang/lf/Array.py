#!/usr/bin/env python
""" generated source for module Array """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Array</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Array#getElements <em>Elements</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getArray()
#  * @model
#  * @generated
#  
class Array(EObject):
    """ generated source for interface Array """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Elements</b></em>' containment reference list.
    #    * The list contents are of type {@link org.lflang.lf.Element}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Elements</em>' containment reference list.
    #    * @see org.lflang.lf.LfPackage#getArray_Elements()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getElements(self):
        """ generated source for method getElements """

#  Array
