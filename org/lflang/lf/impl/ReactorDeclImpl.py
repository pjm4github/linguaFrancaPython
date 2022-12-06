#!/usr/bin/env python
""" generated source for module ReactorDeclImpl """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf.impl
# import org.eclipse.emf.common.notify.Notification
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.emf.ecore.impl.ENotificationImpl
# import org.eclipse.emf.ecore.impl.MinimalEObjectImpl

from org.lflang.lf import LfPackage

from org.lflang.lf import ReactorDecl

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Reactor Decl</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.ReactorDeclImpl#getName <em>Name</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class ReactorDeclImpl(MinimalEObjectImpl, Container, ReactorDecl):
    """ generated source for class ReactorDeclImpl """
    #    * The default value of the '{@link #getName() <em>Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getName()
    #    * @generated
    #    * @ordered
    #    
    NAME_EDEFAULT = None

    #    * The cached value of the '{@link #getName() <em>Name</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getName()
    #    * @generated
    #    * @ordered
    #    
    name = NAME_EDEFAULT

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(ReactorDeclImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.REACTOR_DECL

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getName(self):
        """ generated source for method getName """
        return self.name

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setName(self, newName):
        """ generated source for method setName """
        oldName = self.name
        self.name = newName
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.REACTOR_DECL__NAME, oldName, self.name))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.REACTOR_DECL__NAME:
            return self.__name__
        return super(ReactorDeclImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.REACTOR_DECL__NAME:
            self.setName(str(newValue))
            return
        super(ReactorDeclImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.REACTOR_DECL__NAME:
            self.setName(self.NAME_EDEFAULT)
            return
        super(ReactorDeclImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.REACTOR_DECL__NAME:
            return self.name != None if self.NAME_EDEFAULT == None else not self.NAME_EDEFAULT == self.name
        return super(ReactorDeclImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(ReactorDeclImpl, self).__str__()
        result = StringBuilder(super(ReactorDeclImpl, self).__str__())
        result.append(" (name: ")
        result.append(self.name)
        result.append(')')
        return result.__str__()

# ReactorDeclImpl
