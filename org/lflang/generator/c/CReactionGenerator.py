#!/usr/bin/env python
""" generated source for module CReactionGenerator """
# package: org.lflang.generator.c
# import java.util.LinkedHashMap
# import java.util.LinkedHashSet
# import java.util.LinkedList
# import java.util.List
# import java.util.Map
# import java.util.Set
from lflang import ASTUtils
from lflang.federated import CGeneratorExtension
from lflang.generator.CodeBuilder import CodeBuilder
from lflang.generator.c import CUtil, CGenerator, CCoreFilesUtils, CMethodGenerator


class CReactionGenerator:
    """ generated source for class CReactionGenerator """
    DISABLE_REACTION_INITIALIZATION_MARKER = "// **** Do not include initialization code in this reaction."

    # Generate necessary initialization code inside the body of the reaction that belongs to reactor decl.
    # @param body The body of the reaction. Used to check for the DISABLE_REACTION_INITIALIZATION_MARKER.
    # @param reaction The initialization code will be generated for this specific reaction
    # @param decl The reactor that has the reaction
    # @param reactionIndex The index of the reaction relative to other reactions in the reactor, starting from 0
    #       
    @classmethod
    def generateInitializationForReaction(cls, body, reaction, decl, reactionIndex, types, errorReporter, mainDef, isFederatedAndDecentralized, requiresTypes):
        """ generated source for method generateInitializationForReaction """
        reactor = ASTUtils.toDefinition(decl)
        #  Construct the reactionInitialization code to go into
        #  the body of the function before the verbatim code.
        reactionInitialization = CodeBuilder()
        code_ = CodeBuilder()
        #  Define the "self" struct.
        structType = CUtil.selfType(decl)
        #  A null structType means there are no inputs, state,
        #  or anything else. No need to declare it.
        if structType != None:
            code_.pr("\n".join([ structType + "* self = (" + structType + "*)instance_args; SUPPRESS_UNUSED_WARNING(self);")])
        #  Do not generate the initialization code if the body is marked
        #  to not generate it.
        if body.startsWith(cls.DISABLE_REACTION_INITIALIZATION_MARKER):
            return str(code_)
        #  A reaction may send to or receive from multiple ports of
        #  a contained reactor. The variables for these ports need to
        #  all be declared as fields of the same struct. Hence, we first
        #  collect the fields to be defined in the structs and then
        #  generate the structs.
        fieldsForStructsForContainedReactors = {}
        #  Actions may appear twice, first as a trigger, then with the outputs.
        #  But we need to declare it only once. Collect in this data structure
        #  the actions that are declared as triggered so that if they appear
        #  again with the outputs, they are not defined a second time.
        #  That second redefinition would trigger a compile error.
        actionsAsTriggers = {}
        #  Next, add the triggers (input and actions; timers are not needed).
        #  This defines a local variable in the reaction function whose
        #  name matches that of the trigger. The value of the local variable
        #  is a struct with a value and is_present field, the latter a boolean
        #  that indicates whether the input/action is present.
        #  If the trigger is an output, then it is an output of a
        #  contained reactor. In this case, a struct with the name
        #  of the contained reactor is created with one field that is
        #  a pointer to a struct with a value and is_present field.
        #  E.g., if the contained reactor is named 'c' and its output
        #  port is named 'out', then c.out->value c.out->is_present are
        #  defined so that they can be used in the verbatim code.
        for trigger in ASTUtils.convertToEmptyListIfNull(reaction.getTriggers()):
            if isinstance(trigger, (VarRef)):
                #  and (triggerAsVarRef instanceof VarRef) {
                if isinstance(, (Port)):
                    generatePortVariablesInReaction(reactionInitialization, fieldsForStructsForContainedReactors, triggerAsVarRef, decl, types)
                elif isinstance(, (Action)):
                    reactionInitialization.pr(generateActionVariablesInReaction(triggerAsVarRef.getVariable(), decl, types))
                    actionsAsTriggers.append(triggerAsVarRef.getVariable())
        if reaction.getTriggers() == None or reaction.getTriggers().size() == 0:
            #  No triggers are given, which means react to any input.
            #  Declare an argument for every input.
            #  NOTE: this does not include contained outputs.
            for input in reactor.getInputs():
                reactionInitialization.pr(generateInputVariablesInReaction(input, decl, types))
        #  Define argument for non-triggering inputs.
        for src in ASTUtils.convertToEmptyListIfNull(reaction.getSources()):
            if isinstance(, (Port)):
                generatePortVariablesInReaction(reactionInitialization, fieldsForStructsForContainedReactors, src, decl, types)
            elif isinstance(, (Action)):
                #  It's a bit odd to read but not be triggered by an action, but
                #  OK, I guess we allow it.
                reactionInitialization.pr(generateActionVariablesInReaction(src.getVariable(), decl, types))
                actionsAsTriggers.append(src.getVariable())
        #  Define variables for each declared output or action.
        #  In the case of outputs, the variable is a pointer to where the
        #  output is stored. This gives the reaction code access to any previous
        #  value that may have been written to that output in an earlier reaction.
        if reaction.getEffects() != None:
            for effect in reaction.getEffects():
                variable = effect.getVariable()
                if isinstance(variable, (Action)):
                    #  It is an action, not an output.
                    #  If it has already appeared as trigger, do not redefine it.
                    if not actionsAsTriggers.contains(effect.getVariable()):
                        reactionInitialization.pr(CGenerator.variableStructType(variable, decl) + "* " + variable.__name__ + " = &self->_lf_" + variable.__name__ + ";")
                elif isinstance(, (Mode)):
                    #  Mode change effect
                    idx = ASTUtils.allModes(reactor).indexOf(effect.getVariable())
                    name = effect.getVariable().__name__
                    if idx >= 0:
                        reactionInitialization.pr("reactor_mode_t* " + name + " = &self->_lf__modes[" + idx + "];\nlf_mode_change_type_t _lf_" + name + "_change_type = " + ("history_transition" if effect.getTransition() == ModeTransition.HISTORY else "reset_transition") + ";")
                    else:
                        errorReporter.reportError(reaction, "In generateReaction(): " + name + " not a valid mode of this reactor.")
                else:
                    if isinstance(variable, (Output)):
                        reactionInitialization.pr(generateOutputVariablesInReaction(effect, decl, errorReporter, requiresTypes))
                    elif isinstance(variable, (Input)):
                        #  It is the input of a contained reactor.
                        generateVariablesForSendingToContainedReactors(reactionInitialization, fieldsForStructsForContainedReactors, effect.getContainer(), variable)
                    else:
                        errorReporter.reportError(reaction, "In generateReaction(): effect is neither an input nor an output.")
        #  Before the reaction initialization,
        #  generate the structs used for communication to and from contained reactors.
        for containedReactor in fieldsForStructsForContainedReactors.keySet():
            array = ""
            if containedReactor.getWidthSpec() != None:
                containedReactorWidthVar = generateWidthVariable(containedReactor.__name__)
                code_.pr("int " + containedReactorWidthVar + " = self->_lf_" + containedReactorWidthVar + ";")
                #  Windows does not support variables in arrays declared on the stack,
                #  so we use the maximum size over all bank members.
                array = "[" + maxContainedReactorBankWidth(containedReactor, None, 0, mainDef) + "]"
            code_.pr("\n".join([ "struct " + containedReactor.__name__ + " {", "    " + fieldsForStructsForContainedReactors.get(containedReactor) + "", "} " + containedReactor.__name__ + array + ";")])
        #  Next generate all the collected setup code.
        code_.pr(reactionInitialization.__str__())
        return str(code_)

    # Return the maximum bank width for the given instantiation within all
    # instantiations of its parent reactor.
    # On the first call to this method, the breadcrumbs should be null and the max
    # argument should be zero. On recursive calls, breadcrumbs is a list of nested
    # instantiations, the max is the maximum width found so far.  The search for
    # instances of the parent reactor will begin with the last instantiation
    # in the specified list.
    #       *
    # This rather complicated method is used when a reaction sends or receives data
    # to or from a bank of contained reactors. There will be an array of structs on
    # the self struct of the parent, and the size of the array is conservatively set
    # to the maximum of all the identified bank widths.  This is a bit wasteful of
    # memory, but it avoids having to malloc the array for each instance, and in
    # typical usage, there will be few instances or instances that are all the same
    # width.
    #       *
    # @param containedReactor The contained reactor instantiation.
    # @param breadcrumbs null on first call (non-recursive).
    # @param max 0 on first call.
    #       
    @classmethod
    def maxContainedReactorBankWidth(cls, containedReactor, breadcrumbs, max, mainDef):
        """ generated source for method maxContainedReactorBankWidth """
        #  If the instantiation is not a bank, return 1.
        if containedReactor.getWidthSpec() == None:
            return 1
        #  If there is no main, then we just use the default width.
        if mainDef == None:
            return ASTUtils.width(containedReactor.getWidthSpec(), None)
        nestedBreadcrumbs = breadcrumbs
        if nestedBreadcrumbs == None:
            nestedBreadcrumbs = LinkedList()
            nestedBreadcrumbs.append(mainDef)
        result = max
        parent = containedReactor.eContainer()
        if parent == ASTUtils.toDefinition(mainDef.getReactorClass()):
            #  The parent is main, so there can't be any other instantiations of it.
            return ASTUtils.width(containedReactor.getWidthSpec(), None)
        #  Search for instances of the parent within the tail of the breadcrumbs list.
        container = ASTUtils.toDefinition(nestedBreadcrumbs.get(0).getReactorClass())
        for instantiation in container.getInstantiations():
            #  Put this new instantiation at the head of the list.
            nestedBreadcrumbs.append(0, instantiation)
            if ASTUtils.toDefinition(instantiation.getReactorClass()) == parent:
                #  Found a matching instantiation of the parent.
                #  Evaluate the original width specification in this context.
                candidate = ASTUtils.width(containedReactor.getWidthSpec(), nestedBreadcrumbs)
                if candidate > result:
                    result = candidate
            else:
                #  Found some other instantiation, not the parent.
                #  Search within it for instantiations of the parent.
                #  Note that we assume here that the parent cannot contain
                #  instances of itself.
                candidate = cls.maxContainedReactorBankWidth(containedReactor, nestedBreadcrumbs, result, mainDef)
                if candidate > result:
                    result = candidate
            nestedBreadcrumbs.remove()
        return result

    # Generate code for the body of a reaction that takes an input and
    # schedules an action with the value of that input.
    # @param actionName The action to schedule
    #       
    @classmethod
    def generateDelayBody(cls, ref, actionName, isTokenType):
        """ generated source for method generateDelayBody """
        #  Note that the action.type set by the base class is actually
        #  the port type.
        return "\n".join([ "if (" + ref + "->is_present) {", "    // Put the whole token on the event queue, not just the payload.", "    // This way, the length and element_size are transported.", "    lf_schedule_token(" + actionName + ", 0, " + ref + "->token);", "}") if isTokenType else "lf_schedule_copy(" + actionName + ", 0, &" + ref + "->value, 1]);  // Length is 1."

    @classmethod
    def generateForwardBody(cls, outputName, targetType, actionName, isTokenType):
        """ generated source for method generateForwardBody """
        return "\n".join([ cls.DISABLE_REACTION_INITIALIZATION_MARKER, "self->_lf_" + outputName + ".value = (" + targetType + ")self->_lf__" + actionName + ".token->value;", "self->_lf_" + outputName + ".token = (lf_token_t*)self->_lf__" + actionName + ".token;", "((lf_token_t*)self->_lf__" + actionName + ".token)->ref_count++;", "self->_lf_" + outputName + ".is_present = true;") if isTokenType else "lf_set(" + outputName + ", " + actionName + "->value]);"

    # Generate into the specified string builder the code to
    # initialize local variables for sending data to an input
    # of a contained reactor. This will also, if necessary,
    # generate entries for local struct definitions into the
    # struct argument. These entries point to where the data
    # is stored.
    #       *
    # @param builder The string builder.
    # @param structs A map from reactor instantiations to a place to write
    #  struct fields.
    # @param definition AST node defining the reactor within which this occurs
    # @param input Input of the contained reactor.
    #       
    @classmethod
    def generateVariablesForSendingToContainedReactors(cls, builder, structs, definition, input):
        """ generated source for method generateVariablesForSendingToContainedReactors """
        structBuilder = structs.get(definition)
        if structBuilder == None:
            structBuilder = CodeBuilder()
            structs.put(definition, structBuilder)
        inputStructType = CGenerator.variableStructType(input, definition.getReactorClass())
        defName = definition.__name__
        defWidth = generateWidthVariable(defName)
        inputName = input.__name__
        inputWidth = generateWidthVariable(inputName)
        if not ASTUtils.isMultiport(input):
            #  Contained reactor's input is not a multiport.
            structBuilder.pr(inputStructType + "* " + inputName + ";")
            if definition.getWidthSpec() != None:
                #  Contained reactor is a bank.
                builder.pr("\n".join([ "for (int bankIndex = 0; bankIndex < self->_lf_" + defWidth + "; bankIndex++) {", "    " + defName + "[bankIndex]." + inputName + " = &(self->_lf_" + defName + "[bankIndex]." + inputName + ");", "}")])
            else:
                #  Contained reactor is not a bank.
                builder.pr(defName + "." + inputName + " = &(self->_lf_" + defName + "." + inputName + ");")
        else:
            #  Contained reactor's input is a multiport.
            structBuilder.pr("\n".join([ inputStructType + "** " + inputName + ";", "int " + inputWidth + ";")])
            #  If the contained reactor is a bank, then we have to set the
            #  pointer for each element of the bank.
            if definition.getWidthSpec() != None:
                builder.pr("\n".join([ "for (int _i = 0; _i < self->_lf_" + defWidth + "; _i++) {", "    " + defName + "[_i]." + inputName + " = self->_lf_" + defName + "[_i]." + inputName + ";", "    " + defName + "[_i]." + inputWidth + " = self->_lf_" + defName + "[_i]." + inputWidth + ";", "}")])
            else:
                builder.pr("\n".join([ defName + "." + inputName + " = self->_lf_" + defName + "." + inputName + ";", defName + "." + inputWidth + " = self->_lf_" + defName + "." + inputWidth + ";")])

    # Generate into the specified string builder the code to
    # initialize local variables for ports in a reaction function
    # from the "self" struct. The port may be an input of the
    # reactor or an output of a contained reactor. The second
    # argument provides, for each contained reactor, a place to
    # write the declaration of the output of that reactor that
    # is triggering reactions.
    # @param builder The place into which to write the code.
    # @param structs A map from reactor instantiations to a place to write
    #  struct fields.
    # @param port The port.
    # @param decl The reactor or import statement.
    #       
    @classmethod
    def generatePortVariablesInReaction(cls, builder, structs, port, decl, types):
        """ generated source for method generatePortVariablesInReaction """
        if isinstance(, (Input)):
            builder.pr(generateInputVariablesInReaction(port.getVariable(), decl, types))
        else:
            #  port is an output of a contained reactor.
            output = port.getVariable()
            portStructType = CGenerator.variableStructType(output, port.getContainer().getReactorClass())
            structBuilder = structs.get(port.getContainer())
            if structBuilder == None:
                structBuilder = CodeBuilder()
                structs.put(port.getContainer(), structBuilder)
            reactorName = port.getContainer().__name__
            reactorWidth = generateWidthVariable(reactorName)
            outputName = output.__name__
            outputWidth = generateWidthVariable(outputName)
            #  First define the struct containing the output value and indicator
            #  of its presence.
            if not ASTUtils.isMultiport(output):
                #  Output is not a multiport.
                structBuilder.pr(portStructType + "* " + outputName + ";")
            else:
                #  Output is a multiport.
                structBuilder.pr("\n".join([ portStructType + "** " + outputName + ";", "int " + outputWidth + ";")])
            #  Next, initialize the struct with the current values.
            if port.getContainer().getWidthSpec() != None:
                #  Output is in a bank.
                builder.pr("\n".join([ "for (int i = 0; i < " + reactorWidth + "; i++) {", "    " + reactorName + "[i]." + outputName + " = self->_lf_" + reactorName + "[i]." + outputName + ";", "}")])
                if ASTUtils.isMultiport(output):
                    builder.pr("\n".join([ "for (int i = 0; i < " + reactorWidth + "; i++) {", "    " + reactorName + "[i]." + outputWidth + " = self->_lf_" + reactorName + "[i]." + outputWidth + ";", "}")])
            else:
                #  Output is not in a bank.
                builder.pr(reactorName + "." + outputName + " = self->_lf_" + reactorName + "." + outputName + ";")
                if ASTUtils.isMultiport(output):
                    builder.pr(reactorName + "." + outputWidth + " = self->_lf_" + reactorName + "." + outputWidth + ";")

    #  Generate action variables for a reaction.
    #  @param action The action.
    #  @param decl The reactor.
    #       
    @classmethod
    def generateActionVariablesInReaction(cls, action, decl, types):
        """ generated source for method generateActionVariablesInReaction """
        structType = CGenerator.variableStructType(action, decl)
        #  If the action has a type, create variables for accessing the value.
        type = ASTUtils.getInferredType(action)
        #  Pointer to the lf_token_t sent as the payload in the trigger.
        tokenPointer = "(self->_lf__" + action.__name__ + ".token)"
        builder = CodeBuilder()
        builder.pr("\n".join([ "// Expose the action struct as a local variable whose name matches the action name.", structType + "* " + action.__name__ + " = &self->_lf_" + action.__name__ + ";", "// Set the fields of the action struct to match the current trigger.", action.__name__ + "->is_present = (bool)self->_lf__" + action.__name__ + ".status;", action.__name__ + "->has_value = (" + tokenPointer + " != NULL && " + tokenPointer + "->value != NULL);", action.__name__ + "->token = " + tokenPointer + ";")])
        #  Set the value field only if there is a type.
        if not type.isUndefined():
            #  The value field will either be a copy (for primitive types)
            #  or a pointer (for types ending in *).
            builder.pr("if (" + action.__name__ + "->has_value) {")
            builder.indent()
            if CUtil.isTokenType(type, types):
                builder.pr(action.__name__ + "->value = (" + types.getTargetType(type) + ")" + tokenPointer + "->value;")
            else:
                builder.pr(action.__name__ + "->value = *(" + types.getTargetType(type) + "*)" + tokenPointer + "->value;")
            builder.unindent()
            builder.pr("}")
        return str(builder)

    #  Generate into the specified string builder the code to
    #  initialize local variables for the specified input port
    #  in a reaction function from the "self" struct.
    #  @param input The input statement from the AST.
    #  @param decl The reactor.
    #       
    @classmethod
    def generateInputVariablesInReaction(cls, input, decl, types):
        """ generated source for method generateInputVariablesInReaction """
        structType = CGenerator.variableStructType(input, decl)
        inputType = ASTUtils.getInferredType(input)
        builder = CodeBuilder()
        inputName = input.__name__
        inputWidth = generateWidthVariable(inputName)
        #  Create the local variable whose name matches the input name.
        #  If the input has not been declared mutable, then this is a pointer
        #  to the upstream output. Otherwise, it is a copy of the upstream output,
        #  which nevertheless points to the same token and value (hence, as done
        #  below, we have to use writable_copy()). There are 8 cases,
        #  depending on whether the input is mutable, whether it is a multiport,
        #  and whether it is a token type.
        #  Easy case first.
        if not input.isMutable() and not CUtil.isTokenType(inputType, types) and not ASTUtils.isMultiport(input):
            #  Non-mutable, non-multiport, primitive type.
            builder.pr(structType + "* " + inputName + " = self->_lf_" + inputName + ";")
        elif input.isMutable() and not CUtil.isTokenType(inputType, types) and not ASTUtils.isMultiport(input):
            #  Mutable, non-multiport, primitive type.
            builder.pr(String.join("\n", "// Mutable input, so copy the input into a temporary variable.", "// The input value on the struct is a copy.", structType + " _lf_tmp_" + inputName + " = *(self->_lf_" + inputName + ");", structType + "* " + inputName + " = &_lf_tmp_" + inputName + ";"))
        elif not input.isMutable() and CUtil.isTokenType(inputType, types) and not ASTUtils.isMultiport(input):
            #  Non-mutable, non-multiport, token type.
            builder.pr(String.join("\n", structType + "* " + inputName + " = self->_lf_" + inputName + ";", "if (" + inputName + "->is_present) {", "    " + inputName + "->length = " + inputName + "->token->length;", "    " + inputName + "->value = (" + types.getTargetType(inputType) + ")" + inputName + "->token->value;", "} else {", "    " + inputName + "->length = 0;", "}"))
        elif input.isMutable() and CUtil.isTokenType(inputType, types) and not ASTUtils.isMultiport(input):
            #  Mutable, non-multiport, token type.
            builder.pr(String.join("\n", "// Mutable input, so copy the input struct into a temporary variable.", structType + " _lf_tmp_" + inputName + " = *(self->_lf_" + inputName + ");", structType + "* " + inputName + " = &_lf_tmp_" + inputName + ";", "if (" + inputName + "->is_present) {", "    " + inputName + "->length = " + inputName + "->token->length;", "    lf_token_t* _lf_input_token = " + inputName + "->token;", "    " + inputName + "->token = writable_copy(_lf_input_token);", "    if (" + inputName + "->token != _lf_input_token) {", "        // A copy of the input token has been made.", "        // This needs to be reference counted.", "        " + inputName + "->token->ref_count = 1;", "        // Repurpose the next_free pointer on the token to add to the list.", "        " + inputName + "->token->next_free = _lf_more_tokens_with_ref_count;", "        _lf_more_tokens_with_ref_count = " + inputName + "->token;", "    }", "    " + inputName + "->value = (" + types.getTargetType(inputType) + ")" + inputName + "->token->value;", "} else {", "    " + inputName + "->length = 0;", "}"))
        elif not input.isMutable() and ASTUtils.isMultiport(input):
            #  Non-mutable, multiport, primitive or token type.
            builder.pr(structType + "** " + inputName + " = self->_lf_" + inputName + ";")
        elif CUtil.isTokenType(inputType, types):
            #  Mutable, multiport, token type
            builder.pr(String.join("\n", "// Mutable multiport input, so copy the input structs", "// into an array of temporary variables on the stack.", structType + " _lf_tmp_" + inputName + "[" + CUtil.multiportWidthExpression(input) + "];", structType + "* " + inputName + "[" + CUtil.multiportWidthExpression(input) + "];", "for (int i = 0; i < " + CUtil.multiportWidthExpression(input) + "; i++) {", "    " + inputName + "[i] = &_lf_tmp_" + inputName + "[i];", "    _lf_tmp_" + inputName + "[i] = *(self->_lf_" + inputName + "[i]);", "    // If necessary, copy the tokens.", "    if (" + inputName + "[i]->is_present) {", "        " + inputName + "[i]->length = " + inputName + "[i]->token->length;", "        lf_token_t* _lf_input_token = " + inputName + "[i]->token;", "        " + inputName + "[i]->token = writable_copy(_lf_input_token);", "        if (" + inputName + "[i]->token != _lf_input_token) {", "            // A copy of the input token has been made.", "            // This needs to be reference counted.", "            " + inputName + "[i]->token->ref_count = 1;", "            // Repurpose the next_free pointer on the token to add to the list.", "            " + inputName + "[i]->token->next_free = _lf_more_tokens_with_ref_count;", "            _lf_more_tokens_with_ref_count = " + inputName + "[i]->token;", "        }", "        " + inputName + "[i]->value = (" + types.getTargetType(inputType) + ")" + inputName + "[i]->token->value;", "    } else {", "        " + inputName + "[i]->length = 0;", "    }", "}"))
        else:
            #  Mutable, multiport, primitive type
            builder.pr(String.join("\n", "// Mutable multiport input, so copy the input structs", "// into an array of temporary variables on the stack.", structType + " _lf_tmp_" + inputName + "[" + CUtil.multiportWidthExpression(input) + "];", structType + "* " + inputName + "[" + CUtil.multiportWidthExpression(input) + "];", "for (int i = 0; i < " + CUtil.multiportWidthExpression(input) + "; i++) {", "    " + inputName + "[i]  = &_lf_tmp_" + inputName + "[i];", "    // Copy the struct, which includes the value.", "    _lf_tmp_" + inputName + "[i] = *(self->_lf_" + inputName + "[i]);", "}"))
        #  Set the _width variable for all cases. This will be -1
        #  for a variable-width multiport, which is not currently supported.
        #  It will be -2 if it is not multiport.
        builder.pr("int " + inputWidth + " = self->_lf_" + inputWidth + "; SUPPRESS_UNUSED_WARNING(" + inputWidth + ");")
        return str(builder)

    # Generate into the specified string builder the code to
    # initialize local variables for outputs in a reaction function
    # from the "self" struct.
    # @param effect The effect declared by the reaction. This must refer to an output.
    # @param decl The reactor containing the reaction or the import statement.
    #       
    @classmethod
    def generateOutputVariablesInReaction(cls, effect, decl, errorReporter, requiresTypes):
        """ generated source for method generateOutputVariablesInReaction """
        output = effect.getVariable()
        outputName = output.__name__
        outputWidth = generateWidthVariable(outputName)
        if output.getType() == None and requiresTypes:
            errorReporter.reportError(output, "Output is required to have a type: " + outputName)
            return ""
        else:
            #  The container of the output may be a contained reactor or
            #  the reactor containing the reaction.
            outputStructType = CGenerator.variableStructType(output, decl) if (effect.getContainer() == None) else CGenerator.variableStructType(output, effect.getContainer().getReactorClass())
            if not ASTUtils.isMultiport(output):
                #  Output port is not a multiport.
                return outputStructType + "* " + outputName + " = &self->_lf_" + outputName + ";"
            else:
                #  Output port is a multiport.
                #  Set the _width variable.
                return String.join("\n", "int " + outputWidth + " = self->_lf_" + outputWidth + "; SUPPRESS_UNUSED_WARNING(" + outputWidth + ");", outputStructType + "** " + outputName + " = self->_lf_" + outputName + "_pointers;")

    # Generate the fields of the self struct and statements for the constructor
    # to create and initialize a reaction_t struct for each reaction in the
    # specified reactor and a trigger_t struct for each trigger (input, action,
    # timer, or output of a contained reactor).
    # @param body The place to put the code for the self struct.
    # @param decl The reactor.
    # @param constructorCode The place to put the constructor code.
    #       
    @classmethod
    def generateReactionAndTriggerStructs(cls, currentFederate, body, decl, constructorCode, types, isFederated, isFederatedAndDecentralized):
        """ generated source for method generateReactionAndTriggerStructs """
        reactionCount = 0
        reactor = ASTUtils.toDefinition(decl)
        #  Iterate over reactions and create initialize the reaction_t struct
        #  on the self struct. Also, collect a map from triggers to the reactions
        #  that are triggered by that trigger. Also, collect a set of sources
        #  that are read by reactions but do not trigger reactions.
        #  Finally, collect a set of triggers and sources that are outputs
        #  of contained reactors.
        triggerMap = {}
        sourceSet = {}
        outputsOfContainedReactors = {}
        startupReactions = {}
        shutdownReactions = {}
        resetReactions = {}
        for reaction in ASTUtils.allReactions(reactor):
            if currentFederate.contains(reaction):
                #  Create the reaction_t struct.
                body.pr(reaction, "reaction_t _lf__reaction_" + reactionCount + ";")
                #  Create the map of triggers to reactions.
                for trigger in reaction.getTriggers():
                    #  trigger may not be a VarRef (it could be "startup" or "shutdown").
                    if isinstance(trigger, (VarRef)):
                        triggerAsVarRef = trigger
                        reactionList = triggerMap.get(triggerAsVarRef.getVariable())
                        if reactionList == None:
                            reactionList = LinkedList()
                            triggerMap.put(triggerAsVarRef.getVariable(), reactionList)
                        reactionList.append(reactionCount)
                        if triggerAsVarRef.getContainer() != None:
                            outputsOfContainedReactors.put(triggerAsVarRef.getVariable(), triggerAsVarRef.getContainer())
                    elif isinstance(trigger, (BuiltinTriggerRef)):
                        if (trigger).getType() == STARTUP:
                            startupReactions.append(reactionCount)
                        elif (trigger).getType() == SHUTDOWN:
                            shutdownReactions.append(reactionCount)
                        elif (trigger).getType() == RESET:
                            resetReactions.append(reactionCount)
                #  Create the set of sources read but not triggering.
                for source in reaction.getSources():
                    sourceSet.append(source.getVariable())
                    if source.getContainer() != None:
                        outputsOfContainedReactors.put(source.getVariable(), source.getContainer())
                deadlineFunctionPointer = "NULL"
                if reaction.getDeadline() != None:
                    #  The following has to match the name chosen in generateReactions
                    deadlineFunctionName = generateDeadlineFunctionName(decl, reactionCount)
                    deadlineFunctionPointer = "&" + deadlineFunctionName
                #  Assign the STP handler
                STPFunctionPointer = "NULL"
                if reaction.getStp() != None:
                    #  The following has to match the name chosen in generateReactions
                    STPFunctionName = generateStpFunctionName(decl, reactionCount)
                    STPFunctionPointer = "&" + STPFunctionName
                #  Set the defaults of the reaction_t struct in the constructor.
                #  Since the self struct is allocated using calloc, there is no need to set:
                #  self->_lf__reaction_"+reactionCount+".index = 0;
                #  self->_lf__reaction_"+reactionCount+".chain_id = 0;
                #  self->_lf__reaction_"+reactionCount+".pos = 0;
                #  self->_lf__reaction_"+reactionCount+".status = inactive;
                #  self->_lf__reaction_"+reactionCount+".deadline = 0LL;
                #  self->_lf__reaction_"+reactionCount+".is_STP_violated = false;
                constructorCode.pr(reaction, String.join("\n", "self->_lf__reaction_" + reactionCount + ".number = " + reactionCount + ";", "self->_lf__reaction_" + reactionCount + ".function = " + CReactionGenerator.generateReactionFunctionName(decl, reactionCount) + ";", "self->_lf__reaction_" + reactionCount + ".self = self;", "self->_lf__reaction_" + reactionCount + ".deadline_violation_handler = " + deadlineFunctionPointer + ";", "self->_lf__reaction_" + reactionCount + ".STP_handler = " + STPFunctionPointer + ";", "self->_lf__reaction_" + reactionCount + ".name = " + addDoubleQuotes("?") + ";", ("self->_lf__reaction_" + reactionCount + ".mode = &self->_lf__modes[" + reactor.getModes().indexOf(reaction.eContainer()) + "];" if isinstance(, (Mode)) else "self->_lf__reaction_" + reactionCount + ".mode = NULL;")))
            #  Increment the reactionCount even if the reaction is not in the federate
            #  so that reaction indices are consistent across federates.
            reactionCount += 1
        #  Next, create and initialize the trigger_t objects.
        #  Start with the timers.
        for timer in ASTUtils.allTimers(reactor):
            createTriggerT(body, timer, triggerMap, constructorCode, types, isFederated, isFederatedAndDecentralized)
            #  Since the self struct is allocated using calloc, there is no need to set:
            #  self->_lf__"+timer.name+".is_physical = false;
            #  self->_lf__"+timer.name+".drop = false;
            #  self->_lf__"+timer.name+".element_size = 0;
            constructorCode.pr("self->_lf__" + timer.__name__ + ".is_timer = true;")
            if isFederatedAndDecentralized:
                constructorCode.pr("self->_lf__" + timer.__name__ + ".intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};")
        #  Handle builtin triggers.
        if len(startupReactions) > 0:
            generateBuiltinTriggerdReactionsArray(startupReactions, "startup", body, constructorCode, isFederatedAndDecentralized)
        #  Handle shutdown triggers.
        if len(shutdownReactions) > 0:
            generateBuiltinTriggerdReactionsArray(shutdownReactions, "shutdown", body, constructorCode, isFederatedAndDecentralized)
        if len(resetReactions) > 0:
            generateBuiltinTriggerdReactionsArray(resetReactions, "reset", body, constructorCode, isFederatedAndDecentralized)
        #  Next handle actions.
        for action in ASTUtils.allActions(reactor):
            if currentFederate.contains(action):
                createTriggerT(body, action, triggerMap, constructorCode, types, isFederated, isFederatedAndDecentralized)
                isPhysical = "true"
                if action.getOrigin() == ActionOrigin.LOGICAL:
                    isPhysical = "false"
                elementSize = "0"
                #  If the action type is 'void', we need to avoid generating the code
                #  'sizeof(void)', which some compilers reject.
                rootType = CUtil.rootType(types.getTargetType(action)) if action.getType() != None else None
                if rootType != None and not rootType == "void":
                    elementSize = "sizeof(" + rootType + ")"
                #  Since the self struct is allocated using calloc, there is no need to set:
                #  self->_lf__"+action.__name__+".is_timer = false;
                constructorCode.pr(String.join("\n", "self->_lf__" + action.__name__ + ".is_physical = " + isPhysical + ";", ("self->_lf__" + action.__name__ + ".policy = " + action.getPolicy() + ";" if not (action.getPolicy() == None or action.getPolicy().isEmpty()) else ""), "self->_lf__" + action.__name__ + ".element_size = " + elementSize + ";"))
        #  Next handle inputs.
        for input in ASTUtils.allInputs(reactor):
            createTriggerT(body, input, triggerMap, constructorCode, types, isFederated, isFederatedAndDecentralized)

    # Define the trigger_t object on the self struct, an array of
    # reaction_t pointers pointing to reactions triggered by this variable,
    # and initialize the pointers in the array in the constructor.
    # @param body The place to write the self struct entries.
    # @param variable The trigger variable (Timer, Action, or Input).
    # @param triggerMap A map from Variables to a list of the reaction indices
    #  triggered by the variable.
    # @param constructorCode The place to write the constructor code.
    #       
    @classmethod
    def createTriggerT(cls, body, variable, triggerMap, constructorCode, types, isFederated, isFederatedAndDecentralized):
        """ generated source for method createTriggerT """
        varName = variable.__name__
        #  variable is a port, a timer, or an action.
        body.pr(variable, "trigger_t _lf__" + varName + ";")
        constructorCode.pr(variable, "self->_lf__" + varName + ".last = NULL;")
        if isFederatedAndDecentralized:
            constructorCode.pr(variable, "self->_lf__" + varName + ".intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};")
        #  Generate the reactions triggered table.
        reactionsTriggered = triggerMap.get(variable)
        if reactionsTriggered != None:
            body.pr(variable, "reaction_t* _lf__" + varName + "_reactions[" + len(reactionsTriggered) + "];")
            count = 0
            for reactionTriggered in reactionsTriggered:
                constructorCode.prSourceLineNumber(variable)
                constructorCode.pr(variable, "self->_lf__" + varName + "_reactions[" + count + "] = &self->_lf__reaction_" + reactionTriggered + ";")
                count += 1
            #  Set up the trigger_t struct's pointer to the reactions.
            constructorCode.pr(variable, String.join("\n", "self->_lf__" + varName + ".reactions = &self->_lf__" + varName + "_reactions[0];", "self->_lf__" + varName + ".number_of_reactions = " + count + ";"))
            if isFederated:
                #  Set the physical_time_of_arrival
                constructorCode.pr(variable, "self->_lf__" + varName + ".physical_time_of_arrival = NEVER;")
        if isinstance(variable, (Input)):
            rootType = CUtil.rootType(types.getTargetType(variable))
            #  Since the self struct is allocated using calloc, there is no need to set:
            #  self->_lf__"+input.name+".is_timer = false;
            #  self->_lf__"+input.name+".offset = 0LL;
            #  self->_lf__"+input.name+".period = 0LL;
            #  self->_lf__"+input.name+".is_physical = false;
            #  self->_lf__"+input.name+".drop = false;
            #  If the input type is 'void', we need to avoid generating the code
            #  'sizeof(void)', which some compilers reject.
            size = "0" if (rootType == "void") else "sizeof(" + rootType + ")"
            constructorCode.pr("self->_lf__" + varName + ".element_size = " + size + ";")
            if isFederated:
                body.pr(CGeneratorExtension.createPortStatusFieldForInput(variable))

    @classmethod
    def generateBuiltinTriggerdReactionsArray(cls, reactions, name, body, constructorCode, isFederatedAndDecentralized):
        """ generated source for method generateBuiltinTriggerdReactionsArray """
        body.pr(String.join("\n", "trigger_t _lf__" + name + ";", "reaction_t* _lf__" + name + "_reactions[" + len(reactions) + "];"))
        if isFederatedAndDecentralized:
            constructorCode.pr("self->_lf__" + name + ".intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};")
        i = 0
        for reactionIndex in reactions:
        __i_0 = i
        i += 1
            constructorCode.pr("self->_lf__" + name + "_reactions[" + __i_0 + "] = &self->_lf__reaction_" + reactionIndex + ";")
        constructorCode.pr(String.join("\n", "self->_lf__" + name + ".last = NULL;", "self->_lf__" + name + ".reactions = &self->_lf__" + name + "_reactions[0];", "self->_lf__" + name + ".number_of_reactions = " + len(reactions) + ";", "self->_lf__" + name + ".is_timer = false;"))

    @classmethod
    def generateBuiltinTriggersTable(cls, reactionCount, name):
        """ generated source for method generateBuiltinTriggersTable """
        return String.join("\n", list("// Array of pointers to " + name + " triggers.", ("reaction_t* _lf_" + name + "_reactions[" + reactionCount + "]" if reactionCount > 0 else "reaction_t** _lf_" + name + "_reactions = NULL") + ";", "int _lf_" + name + "_reactions_size = " + reactionCount + ";"))

    # Generate the _lf_trigger_startup_reactions function.
    #       
    @classmethod
    def generateLfTriggerStartupReactions(cls, startupReactionCount, hasModalReactors):
        """ generated source for method generateLfTriggerStartupReactions """
        s = ""
        s.append("void _lf_trigger_startup_reactions() {")
        if startupReactionCount > 0:
            s.append("\n")
            if hasModalReactors:
                s.append(String.join("\n", "    for (int i = 0; i < _lf_startup_reactions_size; i++) {", "        if (_lf_startup_reactions[i] != NULL) {", "            if (_lf_startup_reactions[i]->mode != NULL) {", "                // Skip reactions in modes", "                continue;", "            }", "            _lf_trigger_reaction(_lf_startup_reactions[i], -1);", "        }", "    }", "    _lf_handle_mode_startup_reset_reactions(", "        _lf_startup_reactions, _lf_startup_reactions_size,", "        NULL, 0,", "        _lf_modal_reactor_states, _lf_modal_reactor_states_size);"))
            else:
                s.append(String.join("\n", "    for (int i = 0; i < _lf_startup_reactions_size; i++) {", "        if (_lf_startup_reactions[i] != NULL) {", "            _lf_trigger_reaction(_lf_startup_reactions[i], -1);", "        }", "    }"))
            s.append("\n")
        s.append("}\n")
        return str(s)

    # Generate the _lf_trigger_shutdown_reactions function.
    #       
    @classmethod
    def generateLfTriggerShutdownReactions(cls, shutdownReactionCount, hasModalReactors):
        """ generated source for method generateLfTriggerShutdownReactions """
        s = ""
        s.append("bool _lf_trigger_shutdown_reactions() {\n")
        if shutdownReactionCount > 0:
            if hasModalReactors:
                s.append(String.join("\n", "    for (int i = 0; i < _lf_shutdown_reactions_size; i++) {", "        if (_lf_shutdown_reactions[i] != NULL) {", "            if (_lf_shutdown_reactions[i]->mode != NULL) {", "                // Skip reactions in modes", "                continue;", "            }", "            _lf_trigger_reaction(_lf_shutdown_reactions[i], -1);", "        }", "    }", "    _lf_handle_mode_shutdown_reactions(_lf_shutdown_reactions, _lf_shutdown_reactions_size);", "    return true;"))
            else:
                s.append(String.join("\n", "    for (int i = 0; i < _lf_shutdown_reactions_size; i++) {", "        if (_lf_shutdown_reactions[i] != NULL) {", "            _lf_trigger_reaction(_lf_shutdown_reactions[i], -1);", "        }", "    }", "    return true;"))
            s.append("\n")
        else:
            s.append("    return false;\n")
        s.append("}\n")
        return str(s)

    # Generate the _lf_handle_mode_triggered_reactions function.
    #       
    @classmethod
    def generateLfModeTriggeredReactions(cls, startupReactionCount, resetReactionCount, hasModalReactors):
        """ generated source for method generateLfModeTriggeredReactions """
        if not hasModalReactors:
            return ""
        s = ""
        s.append("void _lf_handle_mode_triggered_reactions() {\n")
        s.append("    _lf_handle_mode_startup_reset_reactions(\n")
        if startupReactionCount > 0:
            s.append("        _lf_startup_reactions, _lf_startup_reactions_size,\n")
        else:
            s.append("        NULL, 0,\n")
        if resetReactionCount > 0:
            s.append("        _lf_reset_reactions, _lf_reset_reactions_size,\n")
        else:
            s.append("        NULL, 0,\n")
        s.append("        _lf_modal_reactor_states, _lf_modal_reactor_states_size);\n")
        s.append("}\n")
        return str(s)

    #  Generate a reaction function definition for a reactor.
    #  This function will have a single argument that is a void* pointing to
    #  a struct that contains parameters, state variables, inputs (triggering or not),
    #  actions (triggering or produced), and outputs.
    #  @param reaction The reaction.
    #  @param decl The reactor.
    #  @param reactionIndex The position of the reaction within the reactor.
    #       
    @classmethod
    def generateReaction(cls, reaction, decl, reactionIndex, mainDef, errorReporter, types, isFederatedAndDecentralized, requiresType):
        """ generated source for method generateReaction """
        code_ = CodeBuilder()
        body = ASTUtils.toText(reaction.getCode())
        init = cls.generateInitializationForReaction(body, reaction, decl, reactionIndex, types, errorReporter, mainDef, isFederatedAndDecentralized, requiresType)
        code_.pr("#include " + StringUtil.addDoubleQuotes(CCoreFilesUtils.getCTargetSetHeader()))
        CMethodGenerator.generateMacrosForMethods(ASTUtils.toDefinition(decl), code_)
        code_.pr(generateFunction(generateReactionFunctionHeader(decl, reactionIndex), init, reaction.getCode()))
        #  Now generate code for the late function, if there is one
        #  Note that this function can only be defined on reactions
        #  in federates that have inputs from a logical connection.
        if reaction.getStp() != None:
            code_.pr(generateFunction(generateStpFunctionHeader(decl, reactionIndex), init, reaction.getStp().getCode()))
        #  Now generate code for the deadline violation function, if there is one.
        if reaction.getDeadline() != None:
            code_.pr(generateFunction(generateDeadlineFunctionHeader(decl, reactionIndex), init, reaction.getDeadline().getCode()))
        CMethodGenerator.generateMacroUndefsForMethods(ASTUtils.toDefinition(decl), code_)
        code_.pr("#include " + StringUtil.addDoubleQuotes(CCoreFilesUtils.getCTargetSetUndefHeader()))
        return str(code_)

    @classmethod
    def generateFunction(cls, header, init, code_):
        """ generated source for method generateFunction """
        function_ = CodeBuilder()
        function_.pr(header + " {")
        function_.indent()
        function_.pr(init)
        function_.prSourceLineNumber(code_)
        function_.pr(ASTUtils.toText(code_))
        function_.unindent()
        function_.pr("}")
        return str(function_)

    # Returns the name of the deadline function for reaction.
    # @param decl The reactor with the deadline
    # @param reactionIndex The number assigned to this reaction deadline
    #       
    @classmethod
    def generateDeadlineFunctionName(cls, decl, reactionIndex):
        """ generated source for method generateDeadlineFunctionName """
        return decl.__name__.lower() + "_deadline_function" + reactionIndex

    # Return the function name for specified reaction of the
    # specified reactor.
    # @param reactor The reactor
    # @param reactionIndex The reaction index.
    # @return The function name for the reaction.
    #       
    @classmethod
    def generateReactionFunctionName(cls, reactor, reactionIndex):
        """ generated source for method generateReactionFunctionName """
        return reactor.__name__.lower() + "reaction_function_" + reactionIndex

    # Returns the name of the stp function for reaction.
    # @param decl The reactor with the stp
    # @param reactionIndex The number assigned to this reaction deadline
    #       
    @classmethod
    def generateStpFunctionName(cls, decl, reactionIndex):
        """ generated source for method generateStpFunctionName """
        return decl.__name__.lower() + "_STP_function" + reactionIndex

    #  Return the top level C function header for the deadline function numbered "reactionIndex" in "decl"
    #  @param decl The reactor declaration
    #  @param reactionIndex The reaction index.
    #  @return The function name for the deadline function.
    #       
    @classmethod
    def generateDeadlineFunctionHeader(cls, decl, reactionIndex):
        """ generated source for method generateDeadlineFunctionHeader """
        functionName = cls.generateDeadlineFunctionName(decl, reactionIndex)
        return generateFunctionHeader(functionName)

    #  Return the top level C function header for the reaction numbered "reactionIndex" in "decl"
    #  @param decl The reactor declaration
    #  @param reactionIndex The reaction index.
    #  @return The function name for the reaction.
    #       
    @classmethod
    def generateReactionFunctionHeader(cls, decl, reactionIndex):
        """ generated source for method generateReactionFunctionHeader """
        functionName = cls.generateReactionFunctionName(decl, reactionIndex)
        return generateFunctionHeader(functionName)

    @classmethod
    def generateStpFunctionHeader(cls, decl, reactionIndex):
        """ generated source for method generateStpFunctionHeader """
        functionName = cls.generateStpFunctionName(decl, reactionIndex)
        return generateFunctionHeader(functionName)

    @classmethod
    def generateFunctionHeader(cls, functionName):
        """ generated source for method generateFunctionHeader """
        return "void " + functionName + "(void* instance_args)"
