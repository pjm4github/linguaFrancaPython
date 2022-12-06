#!/usr/bin/env python
""" generated source for module MethodArgumentImpl """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf.impl
# import org.eclipse.emf.common.notify.Notification
# import org.eclipse.emf.common.notify.NotificationChain
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.emf.ecore.InternalEObject
# import org.eclipse.emf.ecore.impl.ENotificationImpl
# import org.eclipse.emf.ecore.impl.MinimalEObjectImpl

from org.lflang.lf import LfPackage

from org.lflang.lf import MethodArgument

from org.lflang.lf import Type

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Method Argument</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.MethodArgumentImpl#getName <em>Name</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.MethodArgumentImpl#getType <em>Type</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class MethodArgumentImpl(MinimalEObjectImpl, Container, MethodArgument):
    """ generated source for class MethodArgumentImpl """
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

    #    * The cached value of the '{@link #getType() <em>Type</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getType()
    #    * @generated
    #    * @ordered
    #    
    type = None

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(MethodArgumentImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.METHOD_ARGUMENT

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
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.METHOD_ARGUMENT__NAME, oldName, self.name))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getType(self):
        """ generated source for method getType """
        return self.type

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetType(self, newType, msgs):
        """ generated source for method basicSetType """
        oldType = self.type
        self.type = newType
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.METHOD_ARGUMENT__TYPE, oldType, newType)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setType(self, newType):
        """ generated source for method setType """
        if newType != self.type:
            msgs = None
            if self.type != None:
                msgs = (self.type).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.METHOD_ARGUMENT__TYPE, None, msgs)
            if newType != None:
                msgs = (newType).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.METHOD_ARGUMENT__TYPE, None, msgs)
            msgs = self.basicSetType(newType, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.METHOD_ARGUMENT__TYPE, newType, newType))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eInverseRemove(self, otherEnd, featureID, msgs):
        """ generated source for method eInverseRemove """
        if featureID == LfPackage.METHOD_ARGUMENT__TYPE:
            return self.basicSetType(None, msgs)
        return super(MethodArgumentImpl, self).eInverseRemove(otherEnd, featureID, msgs)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.METHOD_ARGUMENT__NAME:
            return self.__name__
        elif featureID == LfPackage.METHOD_ARGUMENT__TYPE:
            return self.getType()
        return super(MethodArgumentImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.METHOD_ARGUMENT__NAME:
            self.setName(str(newValue))
            return
        elif featureID == LfPackage.METHOD_ARGUMENT__TYPE:
            self.setType(newValue)
            return
        super(MethodArgumentImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.METHOD_ARGUMENT__NAME:
            self.setName(self.NAME_EDEFAULT)
            return
        elif featureID == LfPackage.METHOD_ARGUMENT__TYPE:
            self.setType(None)
            return
        super(MethodArgumentImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.METHOD_ARGUMENT__NAME:
            return self.name != None if self.NAME_EDEFAULT == None else not self.NAME_EDEFAULT == self.name
        elif featureID == LfPackage.METHOD_ARGUMENT__TYPE:
            return self.type != None
        return super(MethodArgumentImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(MethodArgumentImpl, self).__str__()
        result = StringBuilder(super(MethodArgumentImpl, self).__str__())
        result.append(" (name: ")
        result.append(self.name)
        result.append(')')
        return result.__str__()

# MethodArgumentImpl
