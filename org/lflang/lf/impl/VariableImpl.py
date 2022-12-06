#!/usr/bin/env python
""" generated source for module VariableImpl """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf.impl
# import org.eclipse.emf.common.notify.Notification
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.emf.ecore.impl.ENotificationImpl
# import org.eclipse.emf.ecore.impl.MinimalEObjectImpl

from org.lflang.lf import LfPackage

from org.lflang.lf import Variable

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Variable</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.VariableImpl#getName <em>Name</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class VariableImpl(MinimalEObjectImpl, Container, Variable):
    """ generated source for class VariableImpl """
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
        super(VariableImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.VARIABLE

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
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.VARIABLE__NAME, oldName, self.name))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.VARIABLE__NAME:
            return self.__name__
        return super(VariableImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.VARIABLE__NAME:
            self.setName(str(newValue))
            return
        super(VariableImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.VARIABLE__NAME:
            self.setName(self.NAME_EDEFAULT)
            return
        super(VariableImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.VARIABLE__NAME:
            return self.name != None if self.NAME_EDEFAULT == None else not self.NAME_EDEFAULT == self.name
        return super(VariableImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(VariableImpl, self).__str__()
        result = StringBuilder(super(VariableImpl, self).__str__())
        result.append(" (name: ")
        result.append(self.name)
        result.append(')')
        return result.__str__()

# VariableImpl