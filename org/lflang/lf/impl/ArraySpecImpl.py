#!/usr/bin/env python
""" generated source for module ArraySpecImpl """
# 
#  * generated by Xtext 2.28.0
#  
# package: org.lflang.lf.impl
# import org.eclipse.emf.common.notify.Notification
# import org.eclipse.emf.ecore.EClass
# import org.eclipse.emf.ecore.impl.ENotificationImpl
# import org.eclipse.emf.ecore.impl.MinimalEObjectImpl

from org.lflang.lf import ArraySpec

from org.lflang.lf import LfPackage

# 
#  * <!-- begin-user-doc -->
#  * An implementation of the model object '<em><b>Array Spec</b></em>'.
#  * <!-- end-user-doc -->
#  * <p>
#  * The following features are implemented:
#  * </p>
#  * <ul>
#  *   <li>{@link org.lflang.lf.impl.ArraySpecImpl#isOfVariableLength <em>Of Variable Length</em>}</li>
#  *   <li>{@link org.lflang.lf.impl.ArraySpecImpl#getLength <em>Length</em>}</li>
#  * </ul>
#  *
#  * @generated
#  
class ArraySpecImpl(MinimalEObjectImpl, Container, ArraySpec):
    """ generated source for class ArraySpecImpl """
    #    * The default value of the '{@link #isOfVariableLength() <em>Of Variable Length</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #isOfVariableLength()
    #    * @generated
    #    * @ordered
    #    
    OF_VARIABLE_LENGTH_EDEFAULT = False

    #    * The cached value of the '{@link #isOfVariableLength() <em>Of Variable Length</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #isOfVariableLength()
    #    * @generated
    #    * @ordered
    #    
    ofVariableLength = OF_VARIABLE_LENGTH_EDEFAULT

    #    * The default value of the '{@link #getLength() <em>Length</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getLength()
    #    * @generated
    #    * @ordered
    #    
    LENGTH_EDEFAULT = 0

    #    * The cached value of the '{@link #getLength() <em>Length</em>}' attribute.
    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @see #getLength()
    #    * @generated
    #    * @ordered
    #    
    length = LENGTH_EDEFAULT

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __init__(self):
        """ generated source for method __init__ """
        super(ArraySpecImpl, self).__init__()

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eStaticClass(self):
        """ generated source for method eStaticClass """
        return LfPackage.Literals.ARRAY_SPEC

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def isOfVariableLength(self):
        """ generated source for method isOfVariableLength """
        return self.ofVariableLength

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setOfVariableLength(self, newOfVariableLength):
        """ generated source for method setOfVariableLength """
        oldOfVariableLength = self.ofVariableLength
        self.ofVariableLength = newOfVariableLength
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.ARRAY_SPEC__OF_VARIABLE_LENGTH, oldOfVariableLength, self.ofVariableLength))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def getLength(self):
        """ generated source for method getLength """
        return self.length

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def setLength(self, newLength):
        """ generated source for method setLength """
        oldLength = self.length
        self.length = newLength
        if eNotificationRequired():
            eNotify(ENotificationImpl(self, Notification.SET, LfPackage.ARRAY_SPEC__LENGTH, oldLength, self.length))

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eGet(self, featureID, resolve, coreType):
        """ generated source for method eGet """
        if featureID == LfPackage.ARRAY_SPEC__OF_VARIABLE_LENGTH:
            return self.isOfVariableLength()
        elif featureID == LfPackage.ARRAY_SPEC__LENGTH:
            return self.getLength()
        return super(ArraySpecImpl, self).eGet(featureID, resolve, coreType)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eSet(self, featureID, newValue):
        """ generated source for method eSet """
        if featureID == LfPackage.ARRAY_SPEC__OF_VARIABLE_LENGTH:
            self.setOfVariableLength(bool(newValue))
            return
        elif featureID == LfPackage.ARRAY_SPEC__LENGTH:
            self.setLength(int(newValue))
            return
        super(ArraySpecImpl, self).eSet(featureID, newValue)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eUnset(self, featureID):
        """ generated source for method eUnset """
        if featureID == LfPackage.ARRAY_SPEC__OF_VARIABLE_LENGTH:
            self.setOfVariableLength(self.OF_VARIABLE_LENGTH_EDEFAULT)
            return
        elif featureID == LfPackage.ARRAY_SPEC__LENGTH:
            self.setLength(self.LENGTH_EDEFAULT)
            return
        super(ArraySpecImpl, self).eUnset(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def eIsSet(self, featureID):
        """ generated source for method eIsSet """
        if featureID == LfPackage.ARRAY_SPEC__OF_VARIABLE_LENGTH:
            return self.ofVariableLength != self.OF_VARIABLE_LENGTH_EDEFAULT
        elif featureID == LfPackage.ARRAY_SPEC__LENGTH:
            return self.length != self.LENGTH_EDEFAULT
        return super(ArraySpecImpl, self).eIsSet(featureID)

    #    * <!-- begin-user-doc -->
    #    * <!-- end-user-doc -->
    #    * @generated
    #    
    def __str__(self):
        """ generated source for method toString """
        if eIsProxy():
            return super(ArraySpecImpl, self).__str__()
        result = StringBuilder(super(ArraySpecImpl, self).__str__())
        result.append(" (ofVariableLength: ")
        result.append(self.ofVariableLength)
        result.append(", length: ")
        result.append(self.length)
        result.append(')')
        return result.__str__()

# ArraySpecImpl
