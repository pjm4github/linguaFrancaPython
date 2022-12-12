#!/usr/bin/env python
""" generated source for module CActionGenerator """
# package: org.lflang.generator.c
# import java.util.List
# import java.util.ArrayList



# 
#  * Generates code for actions (logical or physical) for the C and CCpp target.
#  *
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Mehrdad Niknami <mniknami@berkeley.edu>}
#  * @author{Christian Menard <christian.menard@tu-dresden.de>}
#  * @author{Matt Weber <matt.weber@berkeley.edu>}
#  * @author{Soroush Bateni <soroush@utdallas.edu>
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  * @author{Hou Seng Wong <housengw@berkeley.edu>}
#
from lflang import ASTUtils, Target
from lflang.generator import GeneratorBase
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.c import CUtil, CGenerator
from lflang.generator.c.CGenerator import variableStructType


class CActionGenerator:
    """ generated source for class CActionGenerator """
    #      * For each action of the specified reactor instance, generate initialization code
    #      * for the offset and period fields.
    #      * @param instance The reactor.
    #      * @param currentFederate The federate we are
    #      
    @classmethod
    def generateInitializers(cls, instance, currentFederate):
        """ generated source for method generateInitializers """
        code_ = []
        for action in instance.actions:
            if currentFederate.contains(action.getDefinition()) and not action.isShutdown():
                triggerStructName = CUtil.reactorRef(action.getParent()) + "->_lf__" + action.__name__
                minDelay = action.getMinDelay()
                minSpacing = action.getMinSpacing()
                offsetInitializer = triggerStructName + ".offset = " + GeneratorBase.timeInTargetLanguage(minDelay) + ";"
                periodInitializer = triggerStructName + ".period = " + (GeneratorBase.timeInTargetLanguage(minSpacing) if minSpacing != None else CGenerator.UNDEFINED_MIN_SPACING) + ";"
                code_.extend(["// Initializing action " + action.getFullName(), offsetInitializer, periodInitializer])
                mode = action.getMode(False)
                if mode != None:
                    modeParent = mode.getParent()
                    modeRef = "&" + CUtil.reactorRef(modeParent) + "->_lf__modes[" + modeParent.modes.indexOf(mode) + "];"
                    code_.append(triggerStructName + ".mode = " + modeRef + ";")
                else:
                    code_.append(triggerStructName + ".mode = NULL;")
        return "\n".join(code_)

    #      * Create a reference token initialized to the payload size.
    #      * This token is marked to not be freed so that the trigger_t struct
    #      * always has a reference token.
    #      * At the start of each time step, we need to initialize the is_present field
    #      * of each action's trigger object to false and free a previously
    #      * allocated token if appropriate. This code sets up the table that does that.
    #      *
    #      * @param selfStruct The variable name of the self struct
    #      * @param actionName The action name
    #      * @param payloadSize The code that returns the size of the action's payload in C.
    #      
    @classmethod
    def generateTokenInitializer(cls, selfStruct, actionName, payloadSize):
        """ generated source for method generateTokenInitializer """
        return "\n".join([ selfStruct + "->_lf__" + actionName + ".token = _lf_create_token(" + payloadSize + ");", selfStruct + "->_lf__" + actionName + ".status = absent;", "_lf_tokens_with_ref_count[_lf_tokens_with_ref_count_count].token = &" + selfStruct + "->_lf__" + actionName + ".token;", "_lf_tokens_with_ref_count[_lf_tokens_with_ref_count_count].status = &" + selfStruct + "->_lf__" + actionName + ".status;", "_lf_tokens_with_ref_count[_lf_tokens_with_ref_count_count++].reset_is_present = true;"])

    #      * Generate the declarations of actions in the self struct
    #      *
    #      * @param reactor The reactor to generatet declarations for
    #      * @param decl The reactor's declaration
    #      * @param currentFederate The federate that is being generated
    #      * @param body The content of the self struct
    #      * @param constructorCode The constructor code of the reactor
    #      
    @classmethod
    def generateDeclarations(cls, reactor, decl, currentFederate, body, constructorCode):
        """ generated source for method generateDeclarations """
        for action in ASTUtils.allActions(reactor):
            if currentFederate.contains(action):
                actionName = action.__name__
                body.pr(action, CGenerator.variableStructType(action, decl) + " _lf_" + actionName + ";")
                #  Initialize the trigger pointer in the action.
                constructorCode.pr(action, "self->_lf_" + actionName + ".trigger = &self->_lf__" + actionName + ";")

    #      * Generate the struct type definitions for the action of the
    #      * reactor
    #      *
    #      * @param decl The reactor declaration
    #      * @param action The action to generate the struct for
    #      * @param target The target of the code generation (C, CCpp or Python)
    #      * @param types The helper object for types related stuff
    #      * @param federatedExtension The code needed to support federated execution
    #      * @return The auxiliary struct for the port as a string
    #      
    @classmethod
    def generateAuxiliaryStruct(cls, decl, action, target, types, federatedExtension):
        """ generated source for method generateAuxiliaryStruct """
        code_ = CodeBuilder()
        code_.pr("typedef struct {")
        code_.indent()
        code_.pr("trigger_t* trigger;")
        code_.pr(cls.valueDeclaration(action, target, types))
        code_.pr("\n".join(["bool is_present;",
                            "bool has_value;",
                            "lf_token_t* token;"]))
        code_.pr(str(federatedExtension))
        code_.unindent()
        code_.pr("} " + variableStructType(action, decl) + ";")
        return str(code_)

    #      * For the specified action, return a declaration for action struct to
    #      * contain the value of the action. An action of
    #      * type int[10], for example, will result in this:
    #      * ```
    #      *     int* value;
    #      * ```
    #      * This will return an empty string for an action with no type.
    #      * @param action The action.
    #      * @return A string providing the value field of the action struct.
    #      
    @classmethod
    def valueDeclaration(cls, action, target, types):
        """ generated source for method valueDeclaration """
        if target == Target.Python:
            return "PyObject* value;"
        #  Do not convert to lf_token_t* using lfTypeToTokenType because there
        #  will be a separate field pointing to the token.
        return "" if action.getType() == None and target.requiresTypes else types.getTargetType(action) + " value;"
