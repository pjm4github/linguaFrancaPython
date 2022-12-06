#package org.lflang.generator.c;

#import java.util.regex.Matcher;
#import java.util.regex.Pattern;

from  org.lflang import ErrorReporter
from org.lflang import InferredType
from org.lflang.generator import TargetTypes
import re

class CTypes(TargetTypes):

    # Regular expression pattern for array types.
    # For example, for "foo[10]", the first match will be "foo" and the second "[10]".
    # For "foo[]", the first match will be "foo" and the second "".
    arrayPattern = re.compile("^\\s*(?:/\\*.*?\\*/)?\\s*(\\w+)\\s*\\[([0-9]*)]\\s*$")

    # FIXME: Instead of using the ErrorReporter, perhaps we should be raising assertion errors or
    #  UnsupportedOperationExceptions or some other non-recoverable errors.
    errorReporter = ErrorReporter()

    # /**
    #  * Initializes a {@code CTargetTypes} with the given
    #  * error reporter.
    #  * @param errorReporter The error reporter for any
    #  *                      errors raised in the code
    #  *                      generation process.
    #  */
    def __init__(self, errorReporter):
        self.errorReporter = errorReporter

    @Override
    def supportsGenerics(self):
        return False

    @Override
    def getTargetTimeType(self):
        return "interval_t"

    @Override
    def getTargetTagType(self):
        return "tag_t"

    @Override
    def getTargetFixedSizeListType(self, baseType, size):
        return f"{baseType}[{size}]"

    @Override
    def getTargetVariableSizeListType(self, baseType):
        return f"%{baseType}[]"

    @Override
    def getTargetUndefinedType(self):
        return f'/* {self.errorReporter.reportError("undefined type")} */'

    # /**
    #  * Given a type, return a C representation of the type. Note that
    #  * C types are very idiosyncratic. For example, {@code int[]} is not always accepted
    #  * as a type, and {@code int*} must be used instead, except when initializing
    #  * a variable using a static initializer, as in {@code int[] foo = {1, 2, 3};}.
    #  * When initializing a variable using a static initializer, use
    #  * {@link #getVariableDeclaration(InferredType, String, boolean)} instead.
    #  * @param type The type.
    #  */
    @Override
    def getTargetType(self, type):
        result = super.getTargetType(type)
        matcher = self.arrayPattern.match(result)
        if matcher.find():
            return matcher.group(1) + '*'
        return result

    # /**
    #  * Return a variable declaration of the form "{@code type name}".
    #  * The type is as returned by {@link #getTargetType(InferredType)}, except with
    #  * the array syntax {@code [size]} preferred over the pointer syntax
    #  * {@code *} (if applicable). This also includes the variable name
    #  * because C requires the array type specification to be placed after
    #  * the variable name rather than with the type.
    #  * The result is of the form {@code type variable_name[size]} or
    #  * {@code type variable_name} depending on whether the given type
    #  * is an array type, unless the array type has no size (it is given
    #  * as {@code []}. In that case, the returned form depends on the
    #  * third argument, initializer. If true, the then the returned
    #  * declaration will have the form {@code type variable_name[]},
    #  * and otherwise it will have the form {@code type* variable_name}.
    #  * @param type The type.
    #  * @param variableName The name of the variable.
    #  * @param initializer True to return a form usable in a static initializer.
    #  */
    def getVariableDeclaration(self, type, variableName, initializer):
        t = super.getTargetType(type)
        matcher = self.arrayPattern.match(t)
        declaration = f"{t} {variableName}"
        if matcher.find():
            # For array types, we have to move the []
            # because C is very picky about where this goes. It has to go
            # after the variable name. Also, in an initializer, it has to have
            # form [], and in a struct definition, it has to use *.
            if matcher.group(2) == "" and not initializer:
                declaration = f"{matcher.group(1)}* {variableName}"
            else:
                declaration = f"{matcher.group(1)} {variableName}[{matcher.group(2)}]"
        return declaration
