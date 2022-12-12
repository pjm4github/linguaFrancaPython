#!/usr/bin/env python
""" generated source for module PythonTypes """
# package: org.lflang.generator.python
# import java.util.regex.Pattern
import re
from org.lflang import ErrorReporter

from org.lflang import InferredType

from org.lflang.generator.c import CTypes

class PythonTypes(CTypes):
    """ generated source for class PythonTypes """
    #  Regular expression pattern for pointer types. The star at the end has to be visible.
    pointerPatternVariable = re.compile("^\\s+(\\w+)\\s*\\*\\s*$")

    #      * Initializes a {@code CTargetTypes} with the given
    #      * error reporter.
    #      *
    #      * @param errorReporter The error reporter for any
    #      *                      errors raised in the code
    #      *                      generation process.
    #      
    def __init__(self, errorReporter):
        """ generated source for method __init__ """
        super().__init__(errorReporter)

    def getTargetUndefinedType(self):
        """ generated source for method getTargetUndefinedType """
        return "PyObject*"

    #      * This generator inherits types from the CGenerator.
    #      * This function reverts them back to Python types
    #      * For example, the types double is converted to float,
    #      * the * for pointer types is removed, etc.
    #      * @param type The type
    #      * @return The Python equivalent of a C type
    #      
    def getPythonType(self, type):
        """ generated source for method getPythonType """
        result = super().getTargetType(type)
        if result == "double":
            result = "float"
        elif result == "string":
            result = "object"
        matcher = self.pointerPatternVariable.matcher(result)
        if matcher.find():
            return matcher.group(1)
        return result
