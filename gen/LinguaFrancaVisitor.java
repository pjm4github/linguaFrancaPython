// Generated from C:/Users/pmora/Documents/Git/GitHub/LinguaFranca\LinguaFranca.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link LinguaFrancaParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface LinguaFrancaVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#model}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModel(LinguaFrancaParser.ModelContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#importDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImportDecl(LinguaFrancaParser.ImportDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#reactorDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReactorDecl(LinguaFrancaParser.ReactorDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#importedReactor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImportedReactor(LinguaFrancaParser.ImportedReactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#reactor}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReactor(LinguaFrancaParser.ReactorContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#typeParm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeParm(LinguaFrancaParser.TypeParmContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#typeExpr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeExpr(LinguaFrancaParser.TypeExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#targetDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTargetDecl(LinguaFrancaParser.TargetDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#stateVar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStateVar(LinguaFrancaParser.StateVarContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#method}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod(LinguaFrancaParser.MethodContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#methodArgument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodArgument(LinguaFrancaParser.MethodArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#inputDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInputDecl(LinguaFrancaParser.InputDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#outputDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOutputDecl(LinguaFrancaParser.OutputDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#timer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTimer(LinguaFrancaParser.TimerContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#modeDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModeDecl(LinguaFrancaParser.ModeDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#action}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAction(LinguaFrancaParser.ActionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#reaction}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReaction(LinguaFrancaParser.ReactionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#triggerRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTriggerRef(LinguaFrancaParser.TriggerRefContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#builtinTriggerRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBuiltinTriggerRef(LinguaFrancaParser.BuiltinTriggerRefContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#deadline}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeadline(LinguaFrancaParser.DeadlineContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#sTP}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSTP(LinguaFrancaParser.STPContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#preamble}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPreamble(LinguaFrancaParser.PreambleContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#instantiation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInstantiation(LinguaFrancaParser.InstantiationContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#connection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConnection(LinguaFrancaParser.ConnectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#serializer}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSerializer(LinguaFrancaParser.SerializerContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#attribute}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttribute(LinguaFrancaParser.AttributeContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#attrParm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttrParm(LinguaFrancaParser.AttrParmContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#attrParmValue}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttrParmValue(LinguaFrancaParser.AttrParmValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#keyValuePairs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKeyValuePairs(LinguaFrancaParser.KeyValuePairsContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#keyValuePair}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKeyValuePair(LinguaFrancaParser.KeyValuePairContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#array}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray(LinguaFrancaParser.ArrayContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#element}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElement(LinguaFrancaParser.ElementContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#typedVariable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypedVariable(LinguaFrancaParser.TypedVariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(LinguaFrancaParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#varRef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarRef(LinguaFrancaParser.VarRefContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#varRefOrModeTransition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarRefOrModeTransition(LinguaFrancaParser.VarRefOrModeTransitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(LinguaFrancaParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(LinguaFrancaParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(LinguaFrancaParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#parameterReference}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameterReference(LinguaFrancaParser.ParameterReferenceContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#portDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPortDecl(LinguaFrancaParser.PortDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#widthSpec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWidthSpec(LinguaFrancaParser.WidthSpecContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#widthTerm}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWidthTerm(LinguaFrancaParser.WidthTermContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#host}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHost(LinguaFrancaParser.HostContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#actionOrigin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitActionOrigin(LinguaFrancaParser.ActionOriginContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#visibility}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVisibility(LinguaFrancaParser.VisibilityContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#builtinTrigger}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBuiltinTrigger(LinguaFrancaParser.BuiltinTriggerContext ctx);
	/**
	 * Visit a parse tree produced by {@link LinguaFrancaParser#modeTransition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModeTransition(LinguaFrancaParser.ModeTransitionContext ctx);
}