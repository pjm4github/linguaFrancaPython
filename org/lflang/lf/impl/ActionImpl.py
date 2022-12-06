#!/usr/bin/env python
""" generated source for module ActionImpl """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf.impl
# import org.eclipse.emf.common.notify.Notification
# import org.eclipse.emf.common.notify.NotificationChain
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.emf.ecore.InternalEObject
# import org.eclipse.emf.ecore.impl.ENotificationImpl

from org.lflang.lf import Action

from org.lflang.lf import ActionOrigin

from org.lflang.lf import Expression

from org.lflang.lf import LfPackage

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Action</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.ActionImpl#getOrigin <em>Origin</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ActionImpl#getMinDelay <em>Min Delay</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ActionImpl#getMinSpacing <em>Min Spacing</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ActionImpl#getPolicy <em>Policy</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class ActionImpl(TypedVariableImpl, Action):
    """ generated source for class ActionImpl """
    #    * The default value of the '{@link #getOrigin() <em>Origin</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getOrigin()
    #    * @generated
    #    * @ordered
    #    
    ORIGIN_EDEFAULT = ActionOrigin.NONE

    #    * The cached value of the '{@link #getOrigin() <em>Origin</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getOrigin()
    #    * @generated
    #    * @ordered
    #    
    origin = ORIGIN_EDEFAULT

    #    * The cached value of the '{@link #getMinDelay() <em>Min Delay</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getMinDelay()
    #    * @generated
    #    * @ordered
    #    
    minDelay = None

    #    * The cached value of the '{@link #getMinSpacing() <em>Min Spacing</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getMinSpacing()
    #    * @generated
    #    * @ordered
    #    
    minSpacing = None

    #    * The default value of the '{@link #getPolicy() <em>Policy</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getPolicy()
    #    * @generated
    #    * @ordered
    #    
    POLICY_EDEFAULT = None

    #    * The cached value of the '{@link #getPolicy() <em>Policy</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getPolicy()
    #    * @generated
    #    * @ordered
    #    
    policy = POLICY_EDEFAULT

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(ActionImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.ACTION

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getOrigin(self):
        """ generated source for method getOrigin """
        return self.origin

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setOrigin(self, newOrigin):
        """ generated source for method setOrigin """
        oldOrigin = self.origin
        self.origin = self.ORIGIN_EDEFAULT if newOrigin == None else newOrigin
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.ACTION__ORIGIN, oldOrigin, self.origin))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getMinDelay(self):
        """ generated source for method getMinDelay """
        return self.minDelay

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetMinDelay(self, newMinDelay, msgs):
        """ generated source for method basicSetMinDelay """
        oldMinDelay = self.minDelay
        self.minDelay = newMinDelay
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.ACTION__MIN_DELAY, oldMinDelay, newMinDelay)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setMinDelay(self, newMinDelay):
        """ generated source for method setMinDelay """
        if newMinDelay != self.minDelay:
            msgs = None
            if self.minDelay != None:
                msgs = (self.minDelay).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.ACTION__MIN_DELAY, None, msgs)
            if newMinDelay != None:
                msgs = (newMinDelay).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.ACTION__MIN_DELAY, None, msgs)
            msgs = self.basicSetMinDelay(newMinDelay, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.ACTION__MIN_DELAY, newMinDelay, newMinDelay))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getMinSpacing(self):
        """ generated source for method getMinSpacing """
        return self.minSpacing

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetMinSpacing(self, newMinSpacing, msgs):
        """ generated source for method basicSetMinSpacing """
        oldMinSpacing = self.minSpacing
        self.minSpacing = newMinSpacing
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.ACTION__MIN_SPACING, oldMinSpacing, newMinSpacing)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setMinSpacing(self, newMinSpacing):
        """ generated source for method setMinSpacing """
        if newMinSpacing != self.minSpacing:
            msgs = None
            if self.minSpacing != None:
                msgs = (self.minSpacing).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.ACTION__MIN_SPACING, None, msgs)
            if newMinSpacing != None:
                msgs = (newMinSpacing).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.ACTION__MIN_SPACING, None, msgs)
            msgs = self.basicSetMinSpacing(newMinSpacing, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.ACTION__MIN_SPACING, newMinSpacing, newMinSpacing))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getPolicy(self):
        """ generated source for method getPolicy """
        return self.policy

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setPolicy(self, newPolicy):
        """ generated source for method setPolicy """
        oldPolicy = self.policy
        self.policy = newPolicy
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.ACTION__POLICY, oldPolicy, self.policy))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eInverseRemove(self, otherEnd, featureID, msgs):
        """ generated source for method eInverseRemove """
        if featureID == LfPackage.ACTION__MIN_DELAY:
            return self.basicSetMinDelay(None, msgs)
        elif featureID == LfPackage.ACTION__MIN_SPACING:
            return self.basicSetMinSpacing(None, msgs)
        return super(ActionImpl, self).eInverseRemove(otherEnd, featureID, msgs)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.ACTION__ORIGIN:
            return self.getOrigin()
        elif featureID == LfPackage.ACTION__MIN_DELAY:
            return self.getMinDelay()
        elif featureID == LfPackage.ACTION__MIN_SPACING:
            return self.getMinSpacing()
        elif featureID == LfPackage.ACTION__POLICY:
            return self.getPolicy()
        return super(ActionImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.ACTION__ORIGIN:
            self.setOrigin(newValue)
            return
        elif featureID == LfPackage.ACTION__MIN_DELAY:
            self.setMinDelay(newValue)
            return
        elif featureID == LfPackage.ACTION__MIN_SPACING:
            self.setMinSpacing(newValue)
            return
        elif featureID == LfPackage.ACTION__POLICY:
            self.setPolicy(str(newValue))
            return
        super(ActionImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.ACTION__ORIGIN:
            self.setOrigin(self.ORIGIN_EDEFAULT)
            return
        elif featureID == LfPackage.ACTION__MIN_DELAY:
            self.setMinDelay(None)
            return
        elif featureID == LfPackage.ACTION__MIN_SPACING:
            self.setMinSpacing(None)
            return
        elif featureID == LfPackage.ACTION__POLICY:
            self.setPolicy(self.POLICY_EDEFAULT)
            return
        super(ActionImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.ACTION__ORIGIN:
            return self.origin != self.ORIGIN_EDEFAULT
        elif featureID == LfPackage.ACTION__MIN_DELAY:
            return self.minDelay != None
        elif featureID == LfPackage.ACTION__MIN_SPACING:
            return self.minSpacing != None
        elif featureID == LfPackage.ACTION__POLICY:
            return self.policy != None if self.POLICY_EDEFAULT == None else not self.POLICY_EDEFAULT == self.policy
        return super(ActionImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(ActionImpl, self).__str__()
        result = StringBuilder(super(ActionImpl, self).__str__())
        result.append(" (origin: ")
        result.append(self.origin)
        result.append(", policy: ")
        result.append(self.policy)
        result.append(')')
        return result.__str__()

# ActionImpl