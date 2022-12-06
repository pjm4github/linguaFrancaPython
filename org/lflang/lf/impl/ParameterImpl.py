#!/usr/bin/env python
""" generated source for module ParameterImpl """
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
# import org.eclipse.emf.ecore.util.EDataTypeEList
# import org.eclipse.emf.ecore.util.EObjectContainmentEList
# import org.eclipse.emf.ecore.util.InternalEList

from org.lflang.lf import Attribute

from org.lflang.lf import Expression

from org.lflang.lf import LfPackage

from org.lflang.lf import Parameter

from org.lflang.lf import Type

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Parameter</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.ParameterImpl#getAttributes <em>Attributes</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ParameterImpl#getName <em>Name</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ParameterImpl#getType <em>Type</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ParameterImpl#getParens <em>Parens</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ParameterImpl#getInit <em>Init</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ParameterImpl#getBraces <em>Braces</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class ParameterImpl(MinimalEObjectImpl, Container, Parameter):
    """ generated source for class ParameterImpl """
    #    * The cached value of the '{@link #getAttributes() <em>Attributes</em>}' containment reference list.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getAttributes()
    #    * @generated
    #    * @ordered
    #    
    attributes = None

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

    #    * The cached value of the '{@link #getParens() <em>Parens</em>}' attribute list.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getParens()
    #    * @generated
    #    * @ordered
    #    
    parens = None

    #    * The cached value of the '{@link #getInit() <em>Init</em>}' containment reference list.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getInit()
    #    * @generated
    #    * @ordered
    #    
    init = None

    #    * The cached value of the '{@link #getBraces() <em>Braces</em>}' attribute list.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getBraces()
    #    * @generated
    #    * @ordered
    #    
    braces = None

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(ParameterImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.PARAMETER

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getAttributes(self):
        """ generated source for method getAttributes """
        if self.attributes == None:
            self.attributes = EObjectContainmentEList(Attribute.__class__, self, LfPackage.PARAMETER__ATTRIBUTES)
        return self.attributes

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
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.PARAMETER__NAME, oldName, self.name))

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
            notification = ENotificationImpl(self, Notification.SET, LfPackage.PARAMETER__TYPE, oldType, newType)
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
                msgs = (self.type).eInverseRemove(self, EOPPOSITE_FEATURE_BASE - LfPackage.PARAMETER__TYPE, None, msgs)
            if newType != None:
                msgs = (newType).eInverseAdd(self, EOPPOSITE_FEATURE_BASE - LfPackage.PARAMETER__TYPE, None, msgs)
            msgs = self.basicSetType(newType, msgs)
            if msgs != None:
                msgs.dispatch()
        elif eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.PARAMETER__TYPE, newType, newType))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getParens(self):
        """ generated source for method getParens """
        if self.parens == None:
            self.parens = EDataTypeEList(String.__class__, self, LfPackage.PARAMETER__PARENS)
        return self.parens

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getInit(self):
        """ generated source for method getInit """
        if self.init == None:
            self.init = EObjectContainmentEList(Expression.__class__, self, LfPackage.PARAMETER__INIT)
        return self.init

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getBraces(self):
        """ generated source for method getBraces """
        if self.braces == None:
            self.braces = EDataTypeEList(String.__class__, self, LfPackage.PARAMETER__BRACES)
        return self.braces

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eInverseRemove(self, otherEnd, featureID, msgs):
        """ generated source for method eInverseRemove """
        if featureID == LfPackage.PARAMETER__ATTRIBUTES:
            return (self.getAttributes()).basicRemove(otherEnd, msgs)
        elif featureID == LfPackage.PARAMETER__TYPE:
            return self.basicSetType(None, msgs)
        elif featureID == LfPackage.PARAMETER__INIT:
            return (self.getInit()).basicRemove(otherEnd, msgs)
        return super(ParameterImpl, self).eInverseRemove(otherEnd, featureID, msgs)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.PARAMETER__ATTRIBUTES:
            return self.getAttributes()
        elif featureID == LfPackage.PARAMETER__NAME:
            return self.__name__
        elif featureID == LfPackage.PARAMETER__TYPE:
            return self.getType()
        elif featureID == LfPackage.PARAMETER__PARENS:
            return self.getParens()
        elif featureID == LfPackage.PARAMETER__INIT:
            return self.getInit()
        elif featureID == LfPackage.PARAMETER__BRACES:
            return self.getBraces()
        return super(ParameterImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    @SuppressWarnings("unchecked")
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.PARAMETER__ATTRIBUTES:
            self.getAttributes().clear()
            self.getAttributes().extend(newValue)
            return
        elif featureID == LfPackage.PARAMETER__NAME:
            self.setName(str(newValue))
            return
        elif featureID == LfPackage.PARAMETER__TYPE:
            self.setType(newValue)
            return
        elif featureID == LfPackage.PARAMETER__PARENS:
            self.getParens().clear()
            self.getParens().extend(newValue)
            return
        elif featureID == LfPackage.PARAMETER__INIT:
            self.getInit().clear()
            self.getInit().extend(newValue)
            return
        elif featureID == LfPackage.PARAMETER__BRACES:
            self.getBraces().clear()
            self.getBraces().extend(newValue)
            return
        super(ParameterImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.PARAMETER__ATTRIBUTES:
            self.getAttributes().clear()
            return
        elif featureID == LfPackage.PARAMETER__NAME:
            self.setName(self.NAME_EDEFAULT)
            return
        elif featureID == LfPackage.PARAMETER__TYPE:
            self.setType(None)
            return
        elif featureID == LfPackage.PARAMETER__PARENS:
            self.getParens().clear()
            return
        elif featureID == LfPackage.PARAMETER__INIT:
            self.getInit().clear()
            return
        elif featureID == LfPackage.PARAMETER__BRACES:
            self.getBraces().clear()
            return
        super(ParameterImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.PARAMETER__ATTRIBUTES:
            return self.attributes != None and not self.attributes.isEmpty()
        elif featureID == LfPackage.PARAMETER__NAME:
            return self.name != None if self.NAME_EDEFAULT == None else not self.NAME_EDEFAULT == self.name
        elif featureID == LfPackage.PARAMETER__TYPE:
            return self.type != None
        elif featureID == LfPackage.PARAMETER__PARENS:
            return self.parens != None and not self.parens.isEmpty()
        elif featureID == LfPackage.PARAMETER__INIT:
            return self.init != None and not self.init.isEmpty()
        elif featureID == LfPackage.PARAMETER__BRACES:
            return self.braces != None and not self.braces.isEmpty()
        return super(ParameterImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(ParameterImpl, self).__str__()
        result = StringBuilder(super(ParameterImpl, self).__str__())
        result.append(" (name: ")
        result.append(self.name)
        result.append(", parens: ")
        result.append(self.parens)
        result.append(", braces: ")
        result.append(self.braces)
        result.append(')')
        return result.__str__()

# ParameterImpl