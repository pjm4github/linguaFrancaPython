// Generated from C:/Users/pmora/Documents/Git/GitHub/LinguaFranca\LinguaFranca.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link LinguaFrancaParser}.
 */
public interface LinguaFrancaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(LinguaFrancaParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(LinguaFrancaParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#importDecl}.
	 * @param ctx the parse tree
	 */
	void enterImportDecl(LinguaFrancaParser.ImportDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#importDecl}.
	 * @param ctx the parse tree
	 */
	void exitImportDecl(LinguaFrancaParser.ImportDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#reactorDecl}.
	 * @param ctx the parse tree
	 */
	void enterReactorDecl(LinguaFrancaParser.ReactorDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#reactorDecl}.
	 * @param ctx the parse tree
	 */
	void exitReactorDecl(LinguaFrancaParser.ReactorDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#importedReactor}.
	 * @param ctx the parse tree
	 */
	void enterImportedReactor(LinguaFrancaParser.ImportedReactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#importedReactor}.
	 * @param ctx the parse tree
	 */
	void exitImportedReactor(LinguaFrancaParser.ImportedReactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#reactor}.
	 * @param ctx the parse tree
	 */
	void enterReactor(LinguaFrancaParser.ReactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#reactor}.
	 * @param ctx the parse tree
	 */
	void exitReactor(LinguaFrancaParser.ReactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#typeParm}.
	 * @param ctx the parse tree
	 */
	void enterTypeParm(LinguaFrancaParser.TypeParmContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#typeParm}.
	 * @param ctx the parse tree
	 */
	void exitTypeParm(LinguaFrancaParser.TypeParmContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#typeExpr}.
	 * @param ctx the parse tree
	 */
	void enterTypeExpr(LinguaFrancaParser.TypeExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#typeExpr}.
	 * @param ctx the parse tree
	 */
	void exitTypeExpr(LinguaFrancaParser.TypeExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#targetDecl}.
	 * @param ctx the parse tree
	 */
	void enterTargetDecl(LinguaFrancaParser.TargetDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#targetDecl}.
	 * @param ctx the parse tree
	 */
	void exitTargetDecl(LinguaFrancaParser.TargetDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#stateVar}.
	 * @param ctx the parse tree
	 */
	void enterStateVar(LinguaFrancaParser.StateVarContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#stateVar}.
	 * @param ctx the parse tree
	 */
	void exitStateVar(LinguaFrancaParser.StateVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#method}.
	 * @param ctx the parse tree
	 */
	void enterMethod(LinguaFrancaParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#method}.
	 * @param ctx the parse tree
	 */
	void exitMethod(LinguaFrancaParser.MethodContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#methodArgument}.
	 * @param ctx the parse tree
	 */
	void enterMethodArgument(LinguaFrancaParser.MethodArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#methodArgument}.
	 * @param ctx the parse tree
	 */
	void exitMethodArgument(LinguaFrancaParser.MethodArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#inputDecl}.
	 * @param ctx the parse tree
	 */
	void enterInputDecl(LinguaFrancaParser.InputDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#inputDecl}.
	 * @param ctx the parse tree
	 */
	void exitInputDecl(LinguaFrancaParser.InputDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#outputDecl}.
	 * @param ctx the parse tree
	 */
	void enterOutputDecl(LinguaFrancaParser.OutputDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#outputDecl}.
	 * @param ctx the parse tree
	 */
	void exitOutputDecl(LinguaFrancaParser.OutputDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#timer}.
	 * @param ctx the parse tree
	 */
	void enterTimer(LinguaFrancaParser.TimerContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#timer}.
	 * @param ctx the parse tree
	 */
	void exitTimer(LinguaFrancaParser.TimerContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#modeDecl}.
	 * @param ctx the parse tree
	 */
	void enterModeDecl(LinguaFrancaParser.ModeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#modeDecl}.
	 * @param ctx the parse tree
	 */
	void exitModeDecl(LinguaFrancaParser.ModeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(LinguaFrancaParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(LinguaFrancaParser.ActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#reaction}.
	 * @param ctx the parse tree
	 */
	void enterReaction(LinguaFrancaParser.ReactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#reaction}.
	 * @param ctx the parse tree
	 */
	void exitReaction(LinguaFrancaParser.ReactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#triggerRef}.
	 * @param ctx the parse tree
	 */
	void enterTriggerRef(LinguaFrancaParser.TriggerRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#triggerRef}.
	 * @param ctx the parse tree
	 */
	void exitTriggerRef(LinguaFrancaParser.TriggerRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#builtinTriggerRef}.
	 * @param ctx the parse tree
	 */
	void enterBuiltinTriggerRef(LinguaFrancaParser.BuiltinTriggerRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#builtinTriggerRef}.
	 * @param ctx the parse tree
	 */
	void exitBuiltinTriggerRef(LinguaFrancaParser.BuiltinTriggerRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#deadline}.
	 * @param ctx the parse tree
	 */
	void enterDeadline(LinguaFrancaParser.DeadlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#deadline}.
	 * @param ctx the parse tree
	 */
	void exitDeadline(LinguaFrancaParser.DeadlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#sTP}.
	 * @param ctx the parse tree
	 */
	void enterSTP(LinguaFrancaParser.STPContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#sTP}.
	 * @param ctx the parse tree
	 */
	void exitSTP(LinguaFrancaParser.STPContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#preamble}.
	 * @param ctx the parse tree
	 */
	void enterPreamble(LinguaFrancaParser.PreambleContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#preamble}.
	 * @param ctx the parse tree
	 */
	void exitPreamble(LinguaFrancaParser.PreambleContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#instantiation}.
	 * @param ctx the parse tree
	 */
	void enterInstantiation(LinguaFrancaParser.InstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#instantiation}.
	 * @param ctx the parse tree
	 */
	void exitInstantiation(LinguaFrancaParser.InstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#connection}.
	 * @param ctx the parse tree
	 */
	void enterConnection(LinguaFrancaParser.ConnectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#connection}.
	 * @param ctx the parse tree
	 */
	void exitConnection(LinguaFrancaParser.ConnectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#serializer}.
	 * @param ctx the parse tree
	 */
	void enterSerializer(LinguaFrancaParser.SerializerContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#serializer}.
	 * @param ctx the parse tree
	 */
	void exitSerializer(LinguaFrancaParser.SerializerContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#attribute}.
	 * @param ctx the parse tree
	 */
	void enterAttribute(LinguaFrancaParser.AttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#attribute}.
	 * @param ctx the parse tree
	 */
	void exitAttribute(LinguaFrancaParser.AttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#attrParm}.
	 * @param ctx the parse tree
	 */
	void enterAttrParm(LinguaFrancaParser.AttrParmContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#attrParm}.
	 * @param ctx the parse tree
	 */
	void exitAttrParm(LinguaFrancaParser.AttrParmContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#attrParmValue}.
	 * @param ctx the parse tree
	 */
	void enterAttrParmValue(LinguaFrancaParser.AttrParmValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#attrParmValue}.
	 * @param ctx the parse tree
	 */
	void exitAttrParmValue(LinguaFrancaParser.AttrParmValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#keyValuePairs}.
	 * @param ctx the parse tree
	 */
	void enterKeyValuePairs(LinguaFrancaParser.KeyValuePairsContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#keyValuePairs}.
	 * @param ctx the parse tree
	 */
	void exitKeyValuePairs(LinguaFrancaParser.KeyValuePairsContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#keyValuePair}.
	 * @param ctx the parse tree
	 */
	void enterKeyValuePair(LinguaFrancaParser.KeyValuePairContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#keyValuePair}.
	 * @param ctx the parse tree
	 */
	void exitKeyValuePair(LinguaFrancaParser.KeyValuePairContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(LinguaFrancaParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(LinguaFrancaParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#element}.
	 * @param ctx the parse tree
	 */
	void enterElement(LinguaFrancaParser.ElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#element}.
	 * @param ctx the parse tree
	 */
	void exitElement(LinguaFrancaParser.ElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#typedVariable}.
	 * @param ctx the parse tree
	 */
	void enterTypedVariable(LinguaFrancaParser.TypedVariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#typedVariable}.
	 * @param ctx the parse tree
	 */
	void exitTypedVariable(LinguaFrancaParser.TypedVariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(LinguaFrancaParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(LinguaFrancaParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#varRef}.
	 * @param ctx the parse tree
	 */
	void enterVarRef(LinguaFrancaParser.VarRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#varRef}.
	 * @param ctx the parse tree
	 */
	void exitVarRef(LinguaFrancaParser.VarRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#varRefOrModeTransition}.
	 * @param ctx the parse tree
	 */
	void enterVarRefOrModeTransition(LinguaFrancaParser.VarRefOrModeTransitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#varRefOrModeTransition}.
	 * @param ctx the parse tree
	 */
	void exitVarRefOrModeTransition(LinguaFrancaParser.VarRefOrModeTransitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(LinguaFrancaParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(LinguaFrancaParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(LinguaFrancaParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(LinguaFrancaParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(LinguaFrancaParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(LinguaFrancaParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#parameterReference}.
	 * @param ctx the parse tree
	 */
	void enterParameterReference(LinguaFrancaParser.ParameterReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#parameterReference}.
	 * @param ctx the parse tree
	 */
	void exitParameterReference(LinguaFrancaParser.ParameterReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#portDecl}.
	 * @param ctx the parse tree
	 */
	void enterPortDecl(LinguaFrancaParser.PortDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#portDecl}.
	 * @param ctx the parse tree
	 */
	void exitPortDecl(LinguaFrancaParser.PortDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#widthSpec}.
	 * @param ctx the parse tree
	 */
	void enterWidthSpec(LinguaFrancaParser.WidthSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#widthSpec}.
	 * @param ctx the parse tree
	 */
	void exitWidthSpec(LinguaFrancaParser.WidthSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#widthTerm}.
	 * @param ctx the parse tree
	 */
	void enterWidthTerm(LinguaFrancaParser.WidthTermContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#widthTerm}.
	 * @param ctx the parse tree
	 */
	void exitWidthTerm(LinguaFrancaParser.WidthTermContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#host}.
	 * @param ctx the parse tree
	 */
	void enterHost(LinguaFrancaParser.HostContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#host}.
	 * @param ctx the parse tree
	 */
	void exitHost(LinguaFrancaParser.HostContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#actionOrigin}.
	 * @param ctx the parse tree
	 */
	void enterActionOrigin(LinguaFrancaParser.ActionOriginContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#actionOrigin}.
	 * @param ctx the parse tree
	 */
	void exitActionOrigin(LinguaFrancaParser.ActionOriginContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#visibility}.
	 * @param ctx the parse tree
	 */
	void enterVisibility(LinguaFrancaParser.VisibilityContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#visibility}.
	 * @param ctx the parse tree
	 */
	void exitVisibility(LinguaFrancaParser.VisibilityContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#builtinTrigger}.
	 * @param ctx the parse tree
	 */
	void enterBuiltinTrigger(LinguaFrancaParser.BuiltinTriggerContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#builtinTrigger}.
	 * @param ctx the parse tree
	 */
	void exitBuiltinTrigger(LinguaFrancaParser.BuiltinTriggerContext ctx);
	/**
	 * Enter a parse tree produced by {@link LinguaFrancaParser#modeTransition}.
	 * @param ctx the parse tree
	 */
	void enterModeTransition(LinguaFrancaParser.ModeTransitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link LinguaFrancaParser#modeTransition}.
	 * @param ctx the parse tree
	 */
	void exitModeTransition(LinguaFrancaParser.ModeTransitionContext ctx);
}