#!/usr/bin/env python
""" generated source for module PythonPortGenerator """
# package: org.lflang.generator.python
from include.overloading import overloaded
from org.lflang.lf import Input

from org.lflang.lf import Instantiation

from org.lflang.lf import Output

from org.lflang.lf import Port

from org.lflang.lf import Action

from org.lflang.lf import ReactorDecl

from org.lflang.lf import VarRef
# import java.util.List

from org.lflang import ASTUtils

from org.lflang.generator import CodeBuilder

from org.lflang.generator.c import CGenerator


class PythonPortGenerator(object):
    """ generated source for class PythonPortGenerator """
    NONMULTIPORT_WIDTHSPEC = "-2"

    #      * Generate code to convert C actions to Python action capsules
    #      * @see pythontarget.h.
    #      * @param pyObjectDescriptor A string representing a list of Python format types (e.g., "O") that
    #      *  can be passed to Py_BuildValue. The object type for the converted action will
    #      *  be appended to this string (e.g., "OO").
    #      * @param pyObjects A string containing a list of comma-separated expressions that will create the
    #      *  action capsules.
    #      * @param action The action itself.
    #      * @param decl The reactor decl that contains the action.
    #      
    @classmethod
    def generateActionVariableToSendToPythonReaction(cls, pyObjects, action, decl):
        """ generated source for method generateActionVariableToSendToPythonReaction """
        #  Values passed to an action are always stored in the token->value.
        #  However, sometimes token might not be initialized. Therefore, this function has an internal check for NULL in case token is not initialized.
        pyObjects.append("convert_C_action_to_py({:s})".format(action.__name__))

    #      * Generate code to convert C ports to Python ports capsules (@see pythontarget.h).
    #      *
    #      * The port may be an input of the reactor or an output of a contained reactor.
    #      *
    #      * @param pyObjectDescriptor A string representing a list of Python format types (e.g., "O") that
    #      *  can be passed to Py_BuildValue. The object type for the converted port will
    #      *  be appended to this string (e.g., "OO").
    #      * @param pyObjects A string containing a list of comma-separated expressions that will create the
    #      *  port capsules.
    #      * @param port The port itself.
    #      * @param decl The reactor decl that contains the port.
    #      
    @classmethod
    def generatePortVariablesToSendToPythonReaction(cls, pyObjects, port, decl):
        """ generated source for method generatePortVariablesToSendToPythonReaction """
        if port.isinstance(Input):
            cls.generateInputVariablesToSendToPythonReaction(pyObjects, port.getVariable(), decl)
            return ""
        else:
            #  port is an output of a contained reactor.
            return cls.generateVariablesForSendingToContainedReactors(pyObjects, port.getContainer(), port.getVariable())

    #  Generate into the specified string builder the code to
    #      *  send local variables for output ports to a Python reaction function
    #      *  from the "self" struct.
    #      *  @param builder The string builder into which to write the code.
    #      *  @param structs A map from reactor instantiations to a place to write
    #      *   struct fields.
    #      *  @param output The output port.
    #      *  @param decl The reactor declaration.
    #      
    @classmethod
    def generateOutputVariablesToSendToPythonReaction(cls, pyObjects, output):
        """ generated source for method generateOutputVariablesToSendToPythonReaction """
        #  Unfortunately, for the lf_set macros to work out-of-the-box for
        #  multiports, we need an array of *pointers* to the output structs,
        #  but what we have on the self struct is an array of output structs.
        #  So we have to handle multiports specially here a construct that
        #  array of pointers.
        #  FIXME: The C Generator also has this awkwardness. It makes the code generators
        #  unnecessarily difficult to maintain, and it may have performance consequences as well.
        #  Maybe we should change the lf_set macros.
        if not ASTUtils.isMultiport(output):
            pyObjects.append(cls.generateConvertCPortToPy(output.__name__, cls.NONMULTIPORT_WIDTHSPEC))
        else:
            pyObjects.append(cls.generateConvertCPortToPy(output.__name__))

    #  Generate into the specified string builder the code to
    #      *  send local variables for input ports to a Python reaction function
    #      *  from the "self" struct.
    #      *  @param builder The string builder into which to write the code.
    #      *  @param structs A map from reactor instantiations to a place to write
    #      *   struct fields.
    #      *  @param input The input port.
    #      *  @param reactor The reactor.
    #      
    @classmethod
    def generateInputVariablesToSendToPythonReaction(cls, pyObjects, input, decl):
        """ generated source for method generateInputVariablesToSendToPythonReaction """
        #  Create the local variable whose name matches the input.__name__.
        #  If the input has not been declared mutable, then this is a pointer
        #  to the upstream output. Otherwise, it is a copy of the upstream output,
        #  which nevertheless points to the same token and value (hence, as done
        #  below, we have to use writable_copy()). There are 8 cases,
        #  depending on whether the input is mutable, whether it is a multiport,
        #  and whether it is a token type.
        #  Easy case first.
        if not input.isMutable() and not ASTUtils.isMultiport(input):
            #  Non-mutable, non-multiport, primitive type.
            pyObjects.append(cls.generateConvertCPortToPy(input.__name__))
        elif input.isMutable() and not ASTUtils.isMultiport(input):
            #  Mutable, non-multiport, primitive type.
            #  TODO: handle mutable
            pyObjects.append(cls.generateConvertCPortToPy(input.__name__))
        elif not input.isMutable() and ASTUtils.isMultiport(input):
            #  Non-mutable, multiport, primitive.
            #  TODO: support multiports
            pyObjects.append(cls.generateConvertCPortToPy(input.__name__))
        else:
            #  Mutable, multiport, primitive type
            #  TODO: support mutable multiports
            pyObjects.append(cls.generateConvertCPortToPy(input.__name__))

    #  Generate into the specified string builder the code to
    #      *  pass local variables for sending data to an input
    #      *  of a contained reaction (e.g. for a deadline violation).
    #      *  @param definition AST node defining the reactor within which this occurs
    #      *  @param port Input of the contained reactor.
    #      
    @classmethod
    def generateVariablesForSendingToContainedReactors(cls, pyObjects, definition, port):
        """ generated source for method generateVariablesForSendingToContainedReactors """
        code_ = CodeBuilder()
        if definition.getWidthSpec() != None:
            widthSpec = cls.NONMULTIPORT_WIDTHSPEC
            if ASTUtils.isMultiport(port):
                widthSpec = "self->_lf_" + definition.__name__ + "[i]." + cls.generateWidthVariable(port.__name__)
            #  Contained reactor is a bank.
            #  Create a Python list
            code_.pr(cls.generatePythonListForContainedBank(definition.__name__, port, widthSpec))
            pyObjects.append(definition.__name__ + "_py_list")
        else:
            if ASTUtils.isMultiport(port):
                pyObjects.append(cls.generateConvertCPortToPy(definition.__name__ + "." + port.__name__))
            else:
                pyObjects.append(cls.generateConvertCPortToPy(definition.__name__ + "." + port.__name__, cls.NONMULTIPORT_WIDTHSPEC))
        return code_.__str__()

    #      * Generate code that creates a Python list (i.e., []) for contained banks to be passed to Python reactions.
    #      * The Python reaction will then subsequently be able to address each individual bank member of the contained
    #      * bank using an index or an iterator. Each list member will contain the given <code>port<code>
    #      * (which could be a multiport with a width determined by <code>widthSpec<code>).
    #      *
    #      * This is to accommodate reactions like <code>reaction() -> s.out<code> where s is a bank. In this example,
    #      * the generated Python function will have the signature <code>reaction_function_0(self, s_out)<code>, where
    #      * s_out is a list of out ports. This will later be turned into the proper <code>s.out<code> format using the
    #      * Python code generated in {@link #generatePythonPortVariableInReaction}.
    #      *
    #      * @param reactorName The name of the bank of reactors (which is the name of the reactor class).
    #      * @param port The port that should be put in the Python list.
    #      * @param widthSpec A string that should be -2 for non-multiports and the width expression for multiports.
    #      
    @classmethod
    def generatePythonListForContainedBank(cls, reactorName, port, widthSpec):
        """ generated source for method generatePythonListForContainedBank """
        return "\n".join(["PyObject* " + reactorName + "_py_list = PyList_New(" + cls.generateWidthVariable(reactorName) + ");",
                          "if(" + reactorName + "_py_list == NULL) {",
                          "    lf_print_error(\"Could not create the list needed for " + reactorName + ".\");",
                          "    if (PyErr_Occurred()) {",
                          "        PyErr_PrintEx(0);",
                          "        PyErr_Clear(); // this will reset the error indicator so we can run Python code again",
                          "    }",
                          "    /* Release the thread. No Python API allowed beyond this point. */",
                          "    PyGILState_Release(gstate);",
                          "    Py_FinalizeEx();",
                          "    exit(1);",
                          "}",
                          "for (int i = 0; i < " + cls.generateWidthVariable(reactorName) + "; i++) {",
                          "    if (PyList_SetItem(" + reactorName + "_py_list,",
                          "            i,",
                          "            " + cls.generateConvertCPortToPy(reactorName + "[i]." + port.__name__, widthSpec),
                          "        ) != 0) {",
                          "        lf_print_error(\"Could not add elements to the list for " + reactorName + ".\");",
                          "        if (PyErr_Occurred()) {",
                          "            PyErr_PrintEx(0);",
                          "            PyErr_Clear(); // this will reset the error indicator so we can run Python code again",
                          "        }",
                          "        /* Release the thread. No Python API allowed beyond this point. */",
                          "        PyGILState_Release(gstate);",
                          "        Py_FinalizeEx();",
                          "        exit(1);",
                          "    }",
                          "}"
                          ])

    @classmethod
    def generateAliasTypeDef(cls, decl, port, isTokenType, genericPortType):
        """ generated source for method generateAliasTypeDef """
        return "typedef " + genericPortType + " " + CGenerator.variableStructType(port, decl) + ";"

    @classmethod
    @overloaded
    def generateConvertCPortToPy(cls, port):
        """ generated source for method generateConvertCPortToPy """
        return "convert_C_port_to_py({:s}, {:s})".format(port, cls.generateWidthVariable(port))

    @classmethod
    @generateConvertCPortToPy.register(object, str, str)
    def generateConvertCPortToPy_0(cls, port, widthSpec):
        """ generated source for method generateConvertCPortToPy_0 """
        return "convert_C_port_to_py({:s}, {:s})".format(port, widthSpec)

    #      * Generate into the specified string builder (<code>inits<code>) the code to
    #      * initialize local variable for <code>port<code> so that it can be used in the body of
    #      * the Python reaction.
    #      * @param port The port to generate code for.
    #      
    @classmethod
    def generatePythonPortVariableInReaction(cls, port):
        """ generated source for method generatePythonPortVariableInReaction """
        containerName = port.getContainer().__name__
        variableName = port.getVariable().__name__
        tryStatement = "try: " + containerName + "  # pylint: disable=used-before-assignment"
        if port.getContainer().getWidthSpec() != None:
            #  It's a bank
            return "\n".join([ tryStatement,
                               "except NameError: " + containerName + " = [None] * len(" + containerName + "_" + variableName + ")",
                               "for i in range(len(" + containerName + "_" + variableName + ")):",
                               "    if " + containerName + "[i] is None:",
                               "        " + containerName + "[i] = Make()",
                               "        " + containerName + "[i]." + variableName + " = " + containerName + "_" + variableName + "[i]"
                               ])
        else:
            return "\n".join([ tryStatement,
                               "except NameError:",
                               "    " + containerName + " = Make()",
                               "    " + containerName + "." + variableName + " = " + containerName + "_" + variableName
                               ])
