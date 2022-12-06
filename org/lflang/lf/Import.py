#!/usr/bin/env python
""" generated source for module Import """
from abc import ABCMeta, abstractmethod
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EObject

# 
#  * <!-- begin-user-doc -->
#  * A representation of the model object '<em><b>Import</b></em>'.
#  * <!-- end-user-doc -->
#  *
#  * <p>
#  * The following features are supported:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.Import#getReactorClasses <em>Reactor Classes</em>}</li>
#  *   <li>{@link org.lflang.lf.Import#getImportURI <em>Import URI</em>}</li>
#  * </ul>
#  *
#  * @see org.lflang.lf.LfPackage#getImport()
#  * @model
#  * @generated
#  
class Import(EObject):
    """ generated source for interface Import """
    __metaclass__ = ABCMeta
    #    * Returns the value of the '<em><b>Reactor Classes</b></em>' containment reference list.
    #    * The list contents are of type {@link org.lflang.lf.ImportedReactor}.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Reactor Classes</em>' containment reference list.
    #    * @see org.lflang.lf.LfPackage#getImport_ReactorClasses()
    #    * @model containment="true"
    #    * @generated
    #    
    @abstractmethod
    def getReactorClasses(self):
        """ generated source for method getReactorClasses """

    #    * Returns the value of the '<em><b>Import URI</b></em>' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @return the value of the '<em>Import URI</em>' attribute.
    #    * @see #setImportURI(String)
    #    * @see org.lflang.lf.LfPackage#getImport_ImportURI()
    #    * @model
    #    * @generated
    #    
    @abstractmethod
    def getImportURI(self):
        """ generated source for method getImportURI """

    #    * Sets the value of the '{@link org.lflang.lf.Import#getImportURI <em>Import URI</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @param value the new value of the '<em>Import URI</em>' attribute.
    #    * @see #getImportURI()
    #    * @generated
    #    
    @abstractmethod
    def setImportURI(self, value):
        """ generated source for method setImportURI """

#  Import
