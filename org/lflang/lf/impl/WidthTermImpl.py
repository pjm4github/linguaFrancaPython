#!/usr/bin/env python
""" generated source for module WidthTermImpl """
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

from org.lflang.lf import LFCode

from org.lflang.lf import LfPackage

from org.lflang.lf import Parameter

from org.lflang.lf import VarRef

from org.lflang.lf import WidthTerm

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Width Term</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.WidthTermImpl#getWidth <em>Width</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.WidthTermImpl#getParameter <em>Parameter</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.WidthTermImpl#getPort <em>Port</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.WidthTermImpl#getCode <em>Code</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class WidthTermImpl(MinimalEObjectImpl, Container, WidthTerm):
    """ generated source for class WidthTermImpl """
    #    * The default value of the '{@link #getWidth() <em>Width</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getWidth()
    #    * @generated
    #    * @ordered
    #    
    WIDTH_EDEFAULT = 0

    #    * The cached value of the '{@link #getWidth() <em>Width</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getWidth()
    #    * @generated
    #    * @ordered
    #    
    width = WIDTH_EDEFAULT

    #    * The cached value of the '{@link #getParameter() <em>Parameter</em>}' reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getParameter()
    #    * @generated
    #    * @ordered
    #    
    parameter = None

    #    * The cached value of the '{@link #getPort() <em>Port</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getPort()
    #    * @generated
    #    * @ordered
    #    
    port = None

    #    * The cached value of the '{@link #getCode() <em>Code</em>}' containment reference.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getCode()
    #    * @generated
    #    * @ordered
    #    
    code_ = None

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(WidthTermImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.WIDTH_TERM

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getWidth(self):
        """ generated source for method getWidth """
        return self.width

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setWidth(self, newWidth):
        """ generated source for method setWidth """
        oldWidth = self.width
        self.width = newWidth
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.WIDTH_TERM__WIDTH, oldWidth, self.width))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getParameter(self):
        """ generated source for method getParameter """
        if self.parameter != None and self.parameter.eIsProxy():
            oldParameter = self.parameter
            self.parameter = eResolveProxy(oldParameter)
            if self.parameter != oldParameter:
                if eNotificationRequired():
                    eNotify(ENotificationImpl(self, Notification.RESOLVE, LfPackage.WIDTH_TERM__PARAMETER, oldParameter, self.parameter))
        return self.parameter

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicGetParameter(self):
        """ generated source for method basicGetParameter """
        return self.parameter

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setParameter(self, newParameter):
        """ generated source for method setParameter """
        oldParameter = self.parameter
        self.parameter = newParameter
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.WIDTH_TERM__PARAMETER, oldParameter, self.parameter))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getPort(self):
        """ generated source for method getPort """
        return self.port

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetPort(self, newPort, msgs):
        """ generated source for method basicSetPort """
        oldPort = self.port
        self.port = newPort
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.WIDTH_TERM__PORT, oldPort, newPort)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setPort(self, newPort):
        """ generated source for method setPort """
        if newPort != self.port:
            msgs = None
            if self.port != None:
                msgs = (self.port).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.WIDTH_TERM__PORT, None, msgs)
            if newPort != None:
                msgs = (newPort).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.WIDTH_TERM__PORT, None, msgs)
            msgs = self.basicSetPort(newPort, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.WIDTH_TERM__PORT, newPort, newPort))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getCode(self):
        """ generated source for method getCode """
        return self.code_

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def basicSetCode(self, newCode, msgs):
        """ generated source for method basicSetCode """
        oldCode = self.code_
        self.code_ = newCode
        if eNotificationRequired():
            notification = ENotificationImpl(self, Notification.SET, LfPackage.WIDTH_TERM__CODE, oldCode, newCode)
            if msgs == None:
                msgs = notification
            else:
                msgs.append(notification)
        return msgs

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setCode(self, newCode):
        """ generated source for method setCode """
        if newCode != self.code_:
            msgs = None
            if self.code_ != None:
                msgs = (self.code_).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.WIDTH_TERM__CODE, None, msgs)
            if newCode != None:
                msgs = (newCode).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.WIDTH_TERM__CODE, None, msgs)
            msgs = self.basicSetCode(newCode, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.WIDTH_TERM__CODE, newCode, newCode))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eInverseRemove(self, otherEnd, featureID, msgs):
        """ generated source for method eInverseRemove """
        if featureID == LfPackage.WIDTH_TERM__PORT:
            return self.basicSetPort(None, msgs)
        elif featureID == LfPackage.WIDTH_TERM__CODE:
            return self.basicSetCode(None, msgs)
        return super(WidthTermImpl, self).eInverseRemove(otherEnd, featureID, msgs)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.WIDTH_TERM__WIDTH:
            return self.getWidth()
        elif featureID == LfPackage.WIDTH_TERM__PARAMETER:
            if resolve:
                return self.getParameter()
            return self.basicGetParameter()
        elif featureID == LfPackage.WIDTH_TERM__PORT:
            return self.getPort()
        elif featureID == LfPackage.WIDTH_TERM__CODE:
            return self.getCode()
        return super(WidthTermImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.WIDTH_TERM__WIDTH:
            self.setWidth(int(newValue))
            return
        elif featureID == LfPackage.WIDTH_TERM__PARAMETER:
            self.setParameter(newValue)
            return
        elif featureID == LfPackage.WIDTH_TERM__PORT:
            self.setPort(newValue)
            return
        elif featureID == LfPackage.WIDTH_TERM__CODE:
            self.setCode(newValue)
            return
        super(WidthTermImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.WIDTH_TERM__WIDTH:
            self.setWidth(self.WIDTH_EDEFAULT)
            return
        elif featureID == LfPackage.WIDTH_TERM__PARAMETER:
            self.setParameter(None)
            return
        elif featureID == LfPackage.WIDTH_TERM__PORT:
            self.setPort(None)
            return
        elif featureID == LfPackage.WIDTH_TERM__CODE:
            self.setCode(None)
            return
        super(WidthTermImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.WIDTH_TERM__WIDTH:
            return self.width != self.WIDTH_EDEFAULT
        elif featureID == LfPackage.WIDTH_TERM__PARAMETER:
            return self.parameter != None
        elif featureID == LfPackage.WIDTH_TERM__PORT:
            return self.port != None
        elif featureID == LfPackage.WIDTH_TERM__CODE:
            return self.code_ != None
        return super(WidthTermImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(WidthTermImpl, self).__str__()
        result = StringBuilder(super(WidthTermImpl, self).__str__())
        result.append(" (width: ")
        result.append(self.width)
        result.append(')')
        return result.__str__()

# WidthTermImpl