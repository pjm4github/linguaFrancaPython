#!/usr/bin/env python
""" generated source for module PythonReactionGenerator """
# package: org.lflang.generator.python
# import java.util.ArrayList
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Set
from lflang import ASTUtils, Target
from lflang.generator import GeneratorBase
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.c import CReactionGenerator, CUtil, CCoreFilesUtils
from lflang.generator.python import PyUtil, PythonPortGenerator
from lflang.lf import Action, Mode, Output, Input, VarRef, Port


class PythonReactionGenerator(object):
    """ generated source for class PythonReactionGenerator """
    #      * Generate code to call reaction numbered "reactionIndex" in reactor "decl".
    #      * @param decl The reactor containing the reaction
    #      * @param reactionIndex The index of the reaction
    #      * @param pyObjectDescriptor CPython related descriptors for each object in "pyObjects".
    #      * @param pyObjects CPython related objects
    #      
    @classmethod
    def generateCPythonReactionCaller(cls, decl, reactionIndex, pyObjects, inits):
        """ generated source for method generateCPythonReactionCaller """
        pythonFunctionName = cls.generatePythonReactionFunctionName(reactionIndex)
        cpythonFunctionName = cls.generateCPythonReactionFunctionName(reactionIndex)
        return cls.generateCPythonFunctionCaller(decl.__name__, pythonFunctionName, cpythonFunctionName, pyObjects, inits)

    #      * Generate code to call deadline function numbered "reactionIndex" in reactor "decl".
    #      * @param decl The reactor containing the reaction
    #      * @param reactionIndex The index of the reaction
    #      * @param pyObjectDescriptor CPython related descriptors for each object in "pyObjects".
    #      * @param pyObjects CPython related objects
    #      
    @classmethod
    def generateCPythonDeadlineCaller(cls, decl, reactionIndex, pyObjects):
        """ generated source for method generateCPythonDeadlineCaller """
        pythonFunctionName = cls.generatePythonDeadlineFunctionName(reactionIndex)
        cpythonFunctionName = cls.generateCPythonDeadlineFunctionName(reactionIndex)
        return cls.generateCPythonFunctionCaller(decl.__name__, pythonFunctionName, cpythonFunctionName, pyObjects, "")

    #      * Generate code to call deadline function numbered "reactionIndex" in reactor "decl".
    #      * @param decl The reactor containing the reaction
    #      * @param reactionIndex The index of the reaction
    #      * @param pyObjectDescriptor CPython related descriptors for each object in "pyObjects".
    #      * @param pyObjects CPython related objects
    #      
    @classmethod
    def generateCPythonSTPCaller(cls, decl, reactionIndex, pyObjects):
        """ generated source for method generateCPythonSTPCaller """
        pythonFunctionName = cls.generatePythonSTPFunctionName(reactionIndex)
        cpythonFunctionName = cls.generateCPythonSTPFunctionName(reactionIndex)
        return cls.generateCPythonFunctionCaller(decl.__name__, pythonFunctionName, cpythonFunctionName, pyObjects, "")

    #      * Generate code to call a CPython function.
    #      * @param reactorDeclName The name of the reactor for debugging purposes
    #      * @param pythonFunctionName The name of the function in the .py file.
    #      * @param cpythonFunctionName The name of the function in self struct of the .c file.
    #      * @param pyObjects CPython related objects
    #      
    @classmethod
    def generateCPythonFunctionCaller(cls, reactorDeclName, pythonFunctionName, cpythonFunctionName, pyObjects, inits):
        """ generated source for method generateCPythonFunctionCaller """
        pyObjectsJoined = ", " + ", ".join(pyObjects) if len(pyObjects) > 0 else ""
        code_ = CodeBuilder()
        code_.pr(PyUtil.generateGILAcquireCode())
        code_.pr(inits)
        code_.pr("\n".join([ 'LF_PRINT_DEBUG(\"Calling reaction function ' + reactorDeclName + "." + pythonFunctionName + '");',
                             "PyObject *rValue = PyObject_CallObject(",
                             "    self->" + cpythonFunctionName + ", ",
                             "    Py_BuildValue(\"(" + "O"*len(pyObjects) + ")\"" + pyObjectsJoined + ")",
                             ");",
                             "if (rValue == NULL) {",
                             "    lf_print_error(\"FATAL: Calling reaction " + reactorDeclName + "." + pythonFunctionName + " failed.\");",
                             "    if (PyErr_Occurred()) {",
                             "        PyErr_PrintEx(0);",
                             "        PyErr_Clear(); // this will reset the error indicator so we can run Python code again",
                             "    }",
                             "    " + PyUtil.generateGILReleaseCode(),
                             "    Py_FinalizeEx();",
                             "    exit(1);",
                             "}",
                             "",
                             "/* Release the thread. No Python API allowed beyond this point. */",
                             PyUtil.generateGILReleaseCode()]))
        return code_.__str__()

    #      * Generate the reaction in the .c file, which calls the Python reaction through the CPython interface.
    #      *
    #      * @param reaction The reaction to generate Python-specific initialization for.
    #      * @param decl The reactor to which <code>reaction<code> belongs to.
    #      * @param reactionIndex The index number of the reaction in decl.
    #      * @param mainDef The main reactor.
    #      * @param errorReporter An error reporter.
    #      * @param types A helper class for type-related stuff.
    #      * @param isFederatedAndDecentralized True if program is federated and coordination type is decentralized.
    #      
    @classmethod
    def generateCReaction(cls, reaction, decl, reactionIndex, mainDef, errorReporter, types, isFederatedAndDecentralized):
        """ generated source for method generateCReaction """
        #  Contains the actual comma separated list of inputs to the reaction of type generic_port_instance_struct.
        #  Each input must be cast to (PyObject *) (aka their descriptors for Py_BuildValue are "O")
        pyObjects = []
        code_ = CodeBuilder()
        cPyInit = cls.generateCPythonInitializers(reaction, decl, pyObjects, errorReporter)
        cInit = CReactionGenerator.generateInitializationForReaction("", reaction, decl, reactionIndex, types, errorReporter, mainDef, isFederatedAndDecentralized, Target.Python.requiresTypes)
        code_.pr("#include " + f'"{CCoreFilesUtils.getCTargetSetHeader()}"')
        code_.pr(cls.generateFunction(CReactionGenerator.generateReactionFunctionHeader(decl, reactionIndex), cInit, reaction.getCode(), cls.generateCPythonReactionCaller(decl, reactionIndex, pyObjects, cPyInit)))
        #  Generate code for the STP violation handler, if there is one.
        if reaction.getStp() != None:
            code_.pr(cls.generateFunction(CReactionGenerator.generateStpFunctionHeader(decl, reactionIndex), cInit, reaction.getStp().getCode(), cls.generateCPythonSTPCaller(decl, reactionIndex, pyObjects)))
        #  Generate code for the deadline violation function, if there is one.
        if reaction.getDeadline() != None:
            code_.pr(cls.generateFunction(CReactionGenerator.generateDeadlineFunctionHeader(decl, reactionIndex), cInit, reaction.getDeadline().getCode(), cls.generateCPythonDeadlineCaller(decl, reactionIndex, pyObjects)))
        code_.pr("#include " + f'"{CCoreFilesUtils.getCTargetSetUndefHeader()}"')
        return code_.__str__()

    @classmethod
    def generateFunction(cls, header, init, code_, pyCaller):
        """ generated source for method generateFunction """
        function_ = CodeBuilder()
        function_.pr(header + "{")
        function_.indent()
        function_.pr(init)
        function_.prSourceLineNumber(code_)
        function_.pr(pyCaller)
        function_.unindent()
        function_.pr("}")
        return function_.__str__()

    #      * Generate necessary Python-specific initialization code for <code>reaction<code> that belongs to reactor
    #      * <code>decl<code>.
    #      *
    #      * @param reaction The reaction to generate Python-specific initialization for.
    #      * @param decl The reactor to which <code>reaction<code> belongs to.
    #      * @param pyObjects A list of expressions that can be used as additional arguments to <code>Py_BuildValue<code>
    #      *  (@see <a href="https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue">docs.python.org/3/c-api</a>).
    #      *  We will use as a format string, "(O...O)" where the number of O's is equal to the length of the list.
    #      
    @classmethod
    def generateCPythonInitializers(cls, reaction, decl, pyObjects, errorReporter):
        """ generated source for method generateCPythonInitializers """
        actionsAsTriggers = set()
        reactor = ASTUtils.toDefinition(decl)
        code_ = CodeBuilder()
        #  Next, add the triggers (input and actions; timers are not needed).
        #  TODO: handle triggers
        for trigger in ASTUtils.convertToEmptyListIfNull(reaction.getTriggers()):
            if trigger.isinstance(VarRef):
                triggerAsVarRef = trigger
                code_.pr(cls.generateVariableToSendPythonReaction(triggerAsVarRef, actionsAsTriggers, decl, pyObjects))
        if reaction.getTriggers() == None or reaction.getTriggers().size() == 0:
            #  No triggers are given, which means react to any input.
            #  Declare an argument for every input.
            #  NOTE: this does not include contained outputs.
            for input in reactor.getInputs():
                PythonPortGenerator.generateInputVariablesToSendToPythonReaction(pyObjects, input, decl)
        #  Next add non-triggering inputs.
        for src in ASTUtils.convertToEmptyListIfNull(reaction.getSources()):
            code_.pr(cls.generateVariableToSendPythonReaction(src, actionsAsTriggers, decl, pyObjects))
        #  Next, handle effects
        if reaction.getEffects() != None:
            for effect in reaction.getEffects():
                if effect.isinstance(Action):
                    #  It is an action, not an output.
                    #  If it has already appeared as trigger, do not redefine it.
                    if not actionsAsTriggers.contains(effect.getVariable()):
                        PythonPortGenerator.generateActionVariableToSendToPythonReaction(pyObjects, effect.getVariable(), decl)
                elif effect.isinstance(Mode):
                    name = effect.getVariable().__name__
                    pyObjects.append("convert_C_mode_to_py(" + name + ",(self_base_t*)self, _lf_" + name + "_change_type)")
                else:
                    if effect.isinstance(Output):
                        PythonPortGenerator.generateOutputVariablesToSendToPythonReaction(pyObjects, effect.getVariable())
                    elif effect.isinstance(Input):
                        #  It is the input of a contained reactor.
                        code_.pr(PythonPortGenerator.generateVariablesForSendingToContainedReactors(pyObjects, effect.getContainer(), effect.getVariable()))
                    else:
                        errorReporter.reportError(reaction, "In generateReaction(): " + effect.getVariable().__name__ + " is neither an input nor an output.")
        return code_.__str__()

    #      * Generate parameters and their respective initialization code for a reaction function
    #      * The initialization code is put at the beginning of the reaction before user code
    #      * @param parameters The parameters used for function definition
    #      * @param inits The initialization code for those paramters
    #      * @param decl Reactor declaration
    #      * @param reaction The reaction to be used to generate parameters for
    #      
    @classmethod
    def generatePythonReactionParametersAndInitializations(cls, parameters, inits, decl, reaction):
        """ generated source for method generatePythonReactionParametersAndInitializations """
        reactor = ASTUtils.toDefinition(decl)
        generatedParams = set()
        #  Handle triggers
        for trigger in ASTUtils.convertToEmptyListIfNull(reaction.getTriggers()):
            if not trigger.isinstance(VarRef):
                continue 
            triggerAsVarRef = trigger
            if trigger.isinstance(Port):
                if trigger.isinstance(Input):
                    if (triggerAsVarRef.getVariable()).isMutable():
                        generatedParams.append("mutable_" + triggerAsVarRef.getVariable().__name__ + "")
                        #  Create a deep copy
                        if ASTUtils.isMultiport(triggerAsVarRef.getVariable()):
                            inits.pr(triggerAsVarRef.getVariable().__name__ + " = [Make() for i in range(len(mutable_" + triggerAsVarRef.getVariable().__name__ + "))]")
                            inits.pr("for i in range(len(mutable_" + triggerAsVarRef.getVariable().__name__ + ")):")
                            inits.pr("    " + triggerAsVarRef.getVariable().__name__ + "[i].value = copy.deepcopy(mutable_" + triggerAsVarRef.getVariable().__name__ + "[i].value)")
                        else:
                            inits.pr(triggerAsVarRef.getVariable().__name__ + " = Make()")
                            inits.pr(triggerAsVarRef.getVariable().__name__ + ".value = copy.deepcopy(mutable_" + triggerAsVarRef.getVariable().__name__ + ".value)")
                    else:
                        generatedParams.append(triggerAsVarRef.getVariable().__name__)
                else:
                    #  Handle contained reactors' ports
                    generatedParams.append(triggerAsVarRef.getContainer().__name__ + "_" + triggerAsVarRef.getVariable().__name__)
                    inits.pr(PythonPortGenerator.generatePythonPortVariableInReaction(triggerAsVarRef))
            elif trigger.isinstance(Action):
                generatedParams.append(triggerAsVarRef.getVariable().__name__)
        #  Handle non-triggering inputs
        if reaction.getTriggers() == None or reaction.getTriggers().size() == 0:
            for input in ASTUtils.convertToEmptyListIfNull(reactor.getInputs()):
                generatedParams.append(input.__name__)
                if input.isMutable():
                    #  Create a deep copy
                    inits.pr(input.__name__ + " = copy.deepcopy(" + input.__name__ + ")")
        for src in ASTUtils.convertToEmptyListIfNull(reaction.getSources()):
            if src.isinstance(Output):
                #  Output of a contained reactor
                generatedParams.append(src.getContainer().__name__ + "_" + src.getVariable().__name__)
                inits.pr(PythonPortGenerator.generatePythonPortVariableInReaction(src))
            else:
                generatedParams.append(src.getVariable().__name__)
                if src.isinstance(Input):
                    if src.getVariable().isMutable():
                        #  Create a deep copy
                        inits.pr(src.getVariable().__name__ + " = copy.deepcopy(" + src.getVariable().__name__ + ")")
        #  Handle effects
        for effect in ASTUtils.convertToEmptyListIfNull(reaction.getEffects()):
            if effect.isinstance(Input):
                generatedParams.append(effect.getContainer().__name__ + "_" + effect.getVariable().__name__)
                inits.pr(PythonPortGenerator.generatePythonPortVariableInReaction(effect))
            else:
                generatedParams.append(effect.getVariable().__name__)
                if effect.isinstance(Port):
                    if ASTUtils.isMultiport(effect.getVariable()):
                        pass
                        #  Handle multiports
        for s in generatedParams:
            parameters.append(s)

    @classmethod
    def generateVariableToSendPythonReaction(cls, varRef, actionsAsTriggers, decl, pyObjects):
        """ generated source for method generateVariableToSendPythonReaction """
        if varRef.isinstance(Port):
            return PythonPortGenerator.generatePortVariablesToSendToPythonReaction(pyObjects, varRef, decl)
        elif varRef.isinstance(Action):
            actionsAsTriggers.append(varRef.getVariable())
            PythonPortGenerator.generateActionVariableToSendToPythonReaction(pyObjects, varRef.getVariable(), decl)
        return ""

    #      * Generate code for the body of a reaction that takes an input and
    #      * schedules an action with the value of that input.
    #      * @param action The action to schedule
    #      * @param port The port to read from
    #      
    @classmethod
    def generateCDelayBody(cls, action, port, isTokenType):
        """ generated source for method generateCDelayBody """
        ref = ASTUtils.generateVarRef(port)
        #  Note that the action.type set by the base class is actually
        #  the port type.
        if isTokenType:
            return "\n".join([ "if (" + ref + "->is_present) {", "    // Put the whole token on the event queue, not just the payload.", "    // This way, the length and element_size are transported.", "    lf_schedule_token(" + action.__name__ + ", 0, " + ref + "->token);", "}"])
        else:
            return "\n".join([ "// Create a token.", "#if NUMBER_OF_WORKERS > 0", "// Need to lock the mutex first.", "lf_mutex_lock(&mutex);", "#endif", "lf_token_t* t = create_token(sizeof(PyObject*));", "#if NUMBER_OF_WORKERS > 0", "lf_mutex_unlock(&mutex);", "#endif", "t->value = self->_lf_" + ref + "->value;", "t->length = 1; // Length is 1", "", "// Pass the token along", "lf_schedule_token(" + action.__name__ + ", 0, t);"])

    #      * Generate Python code to link cpython functions to python functions for each reaction.
    #      * @param instance The reactor instance.
    #      * @param reactions The reactions of this instance.
    #      * @param mainDef The definition of the main reactor
    #      
    @classmethod
    def generateCPythonReactionLinkers(cls, instance, mainDef):
        """ generated source for method generateCPythonReactionLinkers """
        nameOfSelfStruct = CUtil.reactorRef(instance)
        reactor = ASTUtils.toDefinition(instance.getDefinition().getReactorClass())
        code_ = CodeBuilder()
        #  Delay reactors and top-level reactions used in the top-level reactor(s) in federated execution are generated in C
        if reactor.__name__.contains(GeneratorBase.GEN_DELAY_CLASS_NAME) or instance.getDefinition().getReactorClass() == (mainDef.getReactorClass() if mainDef != None else None) and reactor.isFederated():
            return ""
        #  Initialize the name field to the unique name of the instance
        code_.pr(nameOfSelfStruct + "->_lf_name = \"" + instance.uniqueID() + "_lf\";")
        for reaction in instance.reactions:
            #  Create a PyObject for each reaction
            code_.pr(cls.generateCPythonReactionLinker(instance, reaction, nameOfSelfStruct))
        return code_.__str__()

    #      * Generate Python code to link cpython functions to python functions for a reaction.
    #      * @param instance The reactor instance.
    #      * @param reaction The reaction of this instance to link.
    #      * @param nameOfSelfStruct The name of the self struct in cpython.
    #      
    @classmethod
    def generateCPythonReactionLinker(cls, instance, reaction, nameOfSelfStruct):
        """ generated source for method generateCPythonReactionLinker """
        code_ = CodeBuilder()
        code_.pr(cls.generateCPythonFunctionLinker(nameOfSelfStruct, cls.generateCPythonReactionFunctionName(reaction.index), instance, cls.generatePythonReactionFunctionName(reaction.index)))
        if reaction.getDefinition().getStp() != None:
            code_.pr(cls.generateCPythonFunctionLinker(nameOfSelfStruct, cls.generateCPythonSTPFunctionName(reaction.index), instance, cls.generatePythonSTPFunctionName(reaction.index)))
        if reaction.getDefinition().getDeadline() != None:
            code_.pr(cls.generateCPythonFunctionLinker(nameOfSelfStruct, cls.generateCPythonDeadlineFunctionName(reaction.index), instance, cls.generatePythonDeadlineFunctionName(reaction.index)))
        return code_.__str__()

    #      * Generate code to link "pythonFunctionName" to "cpythonFunctionName" in "nameOfSelfStruct" of "instance".
    #      * @param nameOfSelfStruct the self struct name of instance
    #      * @param cpythonFunctionName the name of the cpython function
    #      * @param instance the reactor instance
    #      * @param pythonFunctionName the name of the python function
    #      
    @classmethod
    def generateCPythonFunctionLinker(cls, nameOfSelfStruct, cpythonFunctionName, instance, pythonFunctionName):
        """ generated source for method generateCPythonFunctionLinker """
        return "\n".join([ nameOfSelfStruct + "->" + cpythonFunctionName + " = ", "get_python_function(\"__main__\", ", "    " + nameOfSelfStruct + "->_lf_name,", "    " + CUtil.runtimeIndex(instance) + ",", "    \"" + pythonFunctionName + "\");", "if(" + nameOfSelfStruct + "->" + cpythonFunctionName + " == NULL) {", "    lf_print_error_and_exit(\"Could not load function " + pythonFunctionName + "\");", "}"])

    #      * Generate the function that is executed whenever the deadline of the reaction
    #      * with the given reaction index is missed
    #      * @param reaction The reaction to generate deadline miss code for
    #      * @param reactionIndex The agreed-upon index of the reaction in the reactor (should match the C generated code)
    #      * @param reactionParameters The parameters to the deadline violation function, which are the same as the reaction function
    #      
    @classmethod
    def generatePythonFunction(cls, pythonFunctionName, inits, reactionBody, reactionParameters):
        """ generated source for method generatePythonFunction """
        params = ", " + ", ".join( reactionParameters) if len(reactionParameters) > 0 else ""
        code_ = CodeBuilder()
        code_.pr("def " + pythonFunctionName + "(self" + params + "):")
        code_.indent()
        code_.pr(inits)
        code_.pr(reactionBody)
        code_.pr("return 0")
        return code_.__str__()

    #      * Generate the Python code for reactions in reactor
    #      * @param reactor The reactor
    #      * @param reactions The reactions of reactor
    #      
    @classmethod
    def generatePythonReactions(cls, reactor, reactions):
        """ generated source for method generatePythonReactions """
        code_ = CodeBuilder()
        reactionIndex = 0
        for reaction in reactions:
            code_.pr(cls.generatePythonReaction(reactor, reaction, reactionIndex))
            reactionIndex += 1
        return code_.__str__()

    #      * Generate the Python code for reaction in reactor
    #      * @param reactor The reactor
    #      * @param reaction The reaction of reactor
    #      
    @classmethod
    def generatePythonReaction(cls, reactor, reaction, reactionIndex):
        """ generated source for method generatePythonReaction """
        code_ = CodeBuilder()
        reactionParameters = []
        #  Will contain parameters for the function (e.g., Foo(x,y,z,...)
        inits = CodeBuilder()
        #  Will contain initialization code for some parameters
        PythonReactionGenerator.generatePythonReactionParametersAndInitializations(reactionParameters, inits, reactor, reaction)
        code_.pr(cls.generatePythonFunction(cls.generatePythonReactionFunctionName(reactionIndex), inits.__str__(), ASTUtils.toText(reaction.getCode()), reactionParameters))
        #  Generate code for the STP violation handler function, if there is one.
        if reaction.getStp() != None:
            code_.pr(cls.generatePythonFunction(cls.generatePythonSTPFunctionName(reactionIndex), "", ASTUtils.toText(reaction.getStp().getCode()), reactionParameters))
        #  Generate code for the deadline violation function, if there is one.
        if reaction.getDeadline() != None:
            code_.pr(cls.generatePythonFunction(cls.generatePythonDeadlineFunctionName(reactionIndex), "", ASTUtils.toText(reaction.getDeadline().getCode()), reactionParameters))
        return code_.__str__()

    #  Return the function name of the reaction inside the self struct in the .c file.
    #      *  @param reactionIndex The reaction index.
    #      *  @return The function name for the reaction.
    #      
    @classmethod
    def generateCPythonReactionFunctionName(cls, reactionIndex):
        """ generated source for method generateCPythonReactionFunctionName """
        return "_lf_py_reaction_function_" + reactionIndex

    #  Return the function name of the deadline function inside the self struct in the .c file.
    #      *  @param reactionIndex The reaction index.
    #      *  @return The function name for the reaction.
    #      
    @classmethod
    def generateCPythonDeadlineFunctionName(cls, reactionIndex):
        """ generated source for method generateCPythonDeadlineFunctionName """
        return "_lf_py_deadline_function_" + reactionIndex

    #  Return the function name of the STP violation handler function inside the self struct in the .c file.
    #      *  @param reactionIndex The reaction index.
    #      *  @return The function name for the reaction.
    #      
    @classmethod
    def generateCPythonSTPFunctionName(cls, reactionIndex):
        """ generated source for method generateCPythonSTPFunctionName """
        return "_lf_py_STP_function_" + reactionIndex

    #  Return the function name of the reaction in the .py file.
    #      *  @param reactionIndex The reaction index.
    #      *  @return The function name for the reaction.
    #      
    @classmethod
    def generatePythonReactionFunctionName(cls, reactionIndex):
        """ generated source for method generatePythonReactionFunctionName """
        return "reaction_function_" + reactionIndex

    #  Return the function name of the deadline function in the .py file.
    #      *  @param reactionIndex The reaction index.
    #      *  @return The function name for the reaction.
    #      
    @classmethod
    def generatePythonDeadlineFunctionName(cls, reactionIndex):
        """ generated source for method generatePythonDeadlineFunctionName """
        return "deadline_function_" + reactionIndex

    #  Return the function name of the STP violation handler function in the .py file.
    #      *  @param reactionIndex The reaction index.
    #      *  @return The function name for the reaction.
    #      
    @classmethod
    def generatePythonSTPFunctionName(cls, reactionIndex):
        """ generated source for method generatePythonSTPFunctionName """
        return "STP_function_" + reactionIndex
