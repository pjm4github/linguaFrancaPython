#!/usr/bin/env python
""" generated source for module ConnectionImpl """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf.impl
# import java.util.Collection
# import org.eclipse.emf.common.notify.Notification
# import org.eclipse.emf.common.notify.NotificationChain
# import org.eclipse.emf.common.util.EList
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.emf.ecore.InternalEObject
# import org.eclipse.emf.ecore.impl.ENotificationImpl
# import org.eclipse.emf.ecore.impl.MinimalEObjectImpl
# import org.eclipse.emf.ecore.util.EObjectContainmentEList
# import org.eclipse.emf.ecore.util.InternalEList

from org.lflang.lf import Connection

from org.lflang.lf import Expression

from org.lflang.lf import LfPackage

from org.lflang.lf import Serializer

from org.lflang.lf import VarRef

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Connection</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.ConnectionImpl#getLeftPorts <em>Left Ports</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ConnectionImpl#isIterated <em>Iterated</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ConnectionImpl#isPhysical <em>Physical</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ConnectionImpl#getRightPorts <em>Right Ports</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ConnectionImpl#getDelay <em>Delay</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ConnectionImpl#getSerializer <em>Serializer</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class ConnectionImpl(MinimalEObjectImpl, Container, Connection):
    """ generated source for class ConnectionImpl """
    #    * The cached value of the '{@link #getLeftPorts() <em>Left Ports</em>}' containment reference list.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getLeftPorts()
    #    * @generated
    #    * @ordered
    #    
    leftPorts = None

    #    * The default value of the '{@link #isIterated() <em>Iterated</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #isIterated()
    #    * @generated
    #    * @ordered
    #    
    ITERATED_EDEFAULT = False

    #    * The cached value of the '{@link #isIterated() <em>Iterated</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #isIterated()
    #    * @generated
    #    * @ordered
    #    
    iterated = ITERATED_EDEFAULT

    #    * The default value of the '{@link #isPhysical() <em>Physical</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #isPhysical()
    #    * @generated
    #    * @ordered
    #    
    PHYSICAL_EDEFAULT = False

    #    * The cached value of the '{@link #isPhysical() <em>Physical</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #isPhysical()
    #    * @generated
    #    * @ordered
    #    
    physical = PHYSICAL_EDEFAULT

    #    * The cached value of the '{@link #getRightPorts() <em>Right Ports</em>}' containment reference list.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getRightPorts()
    #    * @generated
    #    * @ordered
    #    
    rightPorts = None

    #    * The cached value of the '{@link #getDelay() <em>Delay</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getDelay()
    #    * @generated
    #    * @ordered
    #    
    delay = None

    #    * The cached value of the '{@link #getSerializer() <em>Serializer</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getSerializer()
    #    * @generated
    #    * @ordered
    #    
    serializer = None

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(ConnectionImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.CONNECTION

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getLeftPorts(self):
        """ generated source for method getLeftPorts """
        if self.leftPorts == None:
            self.leftPorts = EObjectContainmentEList(VarRef.__class__, self, LfPackage.CONNECTION__LEFT_PORTS)
        return self.leftPorts

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def isIterated(self):
        """ generated source for method isIterated """
        return self.iterated

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setIterated(self, newIterated):
        """ generated source for method setIterated """
        oldIterated = self.iterated
        self.iterated = newIterated
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.CONNECTION__ITERATED, oldIterated, self.iterated))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def isPhysical(self):
        """ generated source for method isPhysical """
        return self.physical

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setPhysical(self, newPhysical):
        """ generated source for method setPhysical """
        oldPhysical = self.physical
        self.physical = newPhysical
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.CONNECTION__PHYSICAL, oldPhysical, self.physical))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getRightPorts(self):
        """ generated source for method getRightPorts """
        if self.rightPorts == None:
            self.rightPorts = EObjectContainmentEList(VarRef.__class__, self, LfPackage.CONNECTION__RIGHT_PORTS)
        return self.rightPorts

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getDelay(self):
        """ generated source for method getDelay """
        return self.delay

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetDelay(self, newDelay, msgs):
        """ generated source for method basicSetDelay """
        oldDelay = self.delay
        self.delay = newDelay
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.CONNECTION__DELAY, oldDelay, newDelay)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setDelay(self, newDelay):
        """ generated source for method setDelay """
        if newDelay != self.delay:
            msgs = None
            if self.delay != None:
                msgs = (self.delay).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.CONNECTION__DELAY, None, msgs)
            if newDelay != None:
                msgs = (newDelay).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.CONNECTION__DELAY, None, msgs)
            msgs = self.basicSetDelay(newDelay, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.CONNECTION__DELAY, newDelay, newDelay))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getSerializer(self):
        """ generated source for method getSerializer """
        return self.serializer

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetSerializer(self, newSerializer, msgs):
        """ generated source for method basicSetSerializer """
        oldSerializer = self.serializer
        self.serializer = newSerializer
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.CONNECTION__SERIALIZER, oldSerializer, newSerializer)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setSerializer(self, newSerializer):
        """ generated source for method setSerializer """
        if newSerializer != self.serializer:
            msgs = None
            if self.serializer != None:
                msgs = (self.serializer).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.CONNECTION__SERIALIZER, None, msgs)
            if newSerializer != None:
                msgs = (newSerializer).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.CONNECTION__SERIALIZER, None, msgs)
            msgs = self.basicSetSerializer(newSerializer, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.CONNECTION__SERIALIZER, newSerializer, newSerializer))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eInverseRemove(self, otherEnd, featureID, msgs):
        """ generated source for method eInverseRemove """
        if featureID == LfPackage.CONNECTION__LEFT_PORTS:
            return (self.getLeftPorts()).basicRemove(otherEnd, msgs)
        elif featureID == LfPackage.CONNECTION__RIGHT_PORTS:
            return (self.getRightPorts()).basicRemove(otherEnd, msgs)
        elif featureID == LfPackage.CONNECTION__DELAY:
            return self.basicSetDelay(None, msgs)
        elif featureID == LfPackage.CONNECTION__SERIALIZER:
            return self.basicSetSerializer(None, msgs)
        return super(ConnectionImpl, self).eInverseRemove(otherEnd, featureID, msgs)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.CONNECTION__LEFT_PORTS:
            return self.getLeftPorts()
        elif featureID == LfPackage.CONNECTION__ITERATED:
            return self.isIterated()
        elif featureID == LfPackage.CONNECTION__PHYSICAL:
            return self.isPhysical()
        elif featureID == LfPackage.CONNECTION__RIGHT_PORTS:
            return self.getRightPorts()
        elif featureID == LfPackage.CONNECTION__DELAY:
            return self.getDelay()
        elif featureID == LfPackage.CONNECTION__SERIALIZER:
            return self.getSerializer()
        return super(ConnectionImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    @SuppressWarnings("unchecked")
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.CONNECTION__LEFT_PORTS:
            self.getLeftPorts().clear()
            self.getLeftPorts().extend(newValue)
            return
        elif featureID == LfPackage.CONNECTION__ITERATED:
            self.setIterated(bool(newValue))
            return
        elif featureID == LfPackage.CONNECTION__PHYSICAL:
            self.setPhysical(bool(newValue))
            return
        elif featureID == LfPackage.CONNECTION__RIGHT_PORTS:
            self.getRightPorts().clear()
            self.getRightPorts().extend(newValue)
            return
        elif featureID == LfPackage.CONNECTION__DELAY:
            self.setDelay(newValue)
            return
        elif featureID == LfPackage.CONNECTION__SERIALIZER:
            self.setSerializer(newValue)
            return
        super(ConnectionImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.CONNECTION__LEFT_PORTS:
            self.getLeftPorts().clear()
            return
        elif featureID == LfPackage.CONNECTION__ITERATED:
            self.setIterated(self.ITERATED_EDEFAULT)
            return
        elif featureID == LfPackage.CONNECTION__PHYSICAL:
            self.setPhysical(self.PHYSICAL_EDEFAULT)
            return
        elif featureID == LfPackage.CONNECTION__RIGHT_PORTS:
            self.getRightPorts().clear()
            return
        elif featureID == LfPackage.CONNECTION__DELAY:
            self.setDelay(None)
            return
        elif featureID == LfPackage.CONNECTION__SERIALIZER:
            self.setSerializer(None)
            return
        super(ConnectionImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.CONNECTION__LEFT_PORTS:
            return self.leftPorts != None and not self.leftPorts.isEmpty()
        elif featureID == LfPackage.CONNECTION__ITERATED:
            return self.iterated != self.ITERATED_EDEFAULT
        elif featureID == LfPackage.CONNECTION__PHYSICAL:
            return self.physical != self.PHYSICAL_EDEFAULT
        elif featureID == LfPackage.CONNECTION__RIGHT_PORTS:
            return self.rightPorts != None and not self.rightPorts.isEmpty()
        elif featureID == LfPackage.CONNECTION__DELAY:
            return self.delay != None
        elif featureID == LfPackage.CONNECTION__SERIALIZER:
            return self.serializer != None
        return super(ConnectionImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(ConnectionImpl, self).__str__()
        result = StringBuilder(super(ConnectionImpl, self).__str__())
        result.append(" (iterated: ")
        result.append(self.iterated)
        result.append(", physical: ")
        result.append(self.physical)
        result.append(')')
        return result.__str__()

# ConnectionImpl
