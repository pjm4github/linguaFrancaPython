# Generated from C:\Users\pmora\Documents\Git\GitHub\LinguaFranca/LinguaFranca.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LinguaFrancaParser import LinguaFrancaParser
else:
    from LinguaFrancaParser import LinguaFrancaParser

# This class defines a complete listener for a parse tree produced by LinguaFrancaParser.
class LinguaFrancaListener(ParseTreeListener):

    # Enter a parse tree produced by LinguaFrancaParser#model.
    def enterModel(self, ctx:LinguaFrancaParser.ModelContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#model.
    def exitModel(self, ctx:LinguaFrancaParser.ModelContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#targetDecl.
    def enterTargetDecl(self, ctx:LinguaFrancaParser.TargetDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#targetDecl.
    def exitTargetDecl(self, ctx:LinguaFrancaParser.TargetDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#importDecl.
    def enterImportDecl(self, ctx:LinguaFrancaParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#importDecl.
    def exitImportDecl(self, ctx:LinguaFrancaParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#reactorDecl.
    def enterReactorDecl(self, ctx:LinguaFrancaParser.ReactorDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#reactorDecl.
    def exitReactorDecl(self, ctx:LinguaFrancaParser.ReactorDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#importedReactor.
    def enterImportedReactor(self, ctx:LinguaFrancaParser.ImportedReactorContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#importedReactor.
    def exitImportedReactor(self, ctx:LinguaFrancaParser.ImportedReactorContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#reactor.
    def enterReactor(self, ctx:LinguaFrancaParser.ReactorContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#reactor.
    def exitReactor(self, ctx:LinguaFrancaParser.ReactorContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#typeParm.
    def enterTypeParm(self, ctx:LinguaFrancaParser.TypeParmContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#typeParm.
    def exitTypeParm(self, ctx:LinguaFrancaParser.TypeParmContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#typeExpr.
    def enterTypeExpr(self, ctx:LinguaFrancaParser.TypeExprContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#typeExpr.
    def exitTypeExpr(self, ctx:LinguaFrancaParser.TypeExprContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#stateVar.
    def enterStateVar(self, ctx:LinguaFrancaParser.StateVarContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#stateVar.
    def exitStateVar(self, ctx:LinguaFrancaParser.StateVarContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#method.
    def enterMethod(self, ctx:LinguaFrancaParser.MethodContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#method.
    def exitMethod(self, ctx:LinguaFrancaParser.MethodContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#methodArgument.
    def enterMethodArgument(self, ctx:LinguaFrancaParser.MethodArgumentContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#methodArgument.
    def exitMethodArgument(self, ctx:LinguaFrancaParser.MethodArgumentContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#inputDecl.
    def enterInputDecl(self, ctx:LinguaFrancaParser.InputDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#inputDecl.
    def exitInputDecl(self, ctx:LinguaFrancaParser.InputDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#outputDecl.
    def enterOutputDecl(self, ctx:LinguaFrancaParser.OutputDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#outputDecl.
    def exitOutputDecl(self, ctx:LinguaFrancaParser.OutputDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#timer.
    def enterTimer(self, ctx:LinguaFrancaParser.TimerContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#timer.
    def exitTimer(self, ctx:LinguaFrancaParser.TimerContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#modeDecl.
    def enterModeDecl(self, ctx:LinguaFrancaParser.ModeDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#modeDecl.
    def exitModeDecl(self, ctx:LinguaFrancaParser.ModeDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#action.
    def enterAction(self, ctx:LinguaFrancaParser.ActionContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#action.
    def exitAction(self, ctx:LinguaFrancaParser.ActionContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#reaction.
    def enterReaction(self, ctx:LinguaFrancaParser.ReactionContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#reaction.
    def exitReaction(self, ctx:LinguaFrancaParser.ReactionContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#triggerRef.
    def enterTriggerRef(self, ctx:LinguaFrancaParser.TriggerRefContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#triggerRef.
    def exitTriggerRef(self, ctx:LinguaFrancaParser.TriggerRefContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#builtinTriggerRef.
    def enterBuiltinTriggerRef(self, ctx:LinguaFrancaParser.BuiltinTriggerRefContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#builtinTriggerRef.
    def exitBuiltinTriggerRef(self, ctx:LinguaFrancaParser.BuiltinTriggerRefContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#deadline.
    def enterDeadline(self, ctx:LinguaFrancaParser.DeadlineContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#deadline.
    def exitDeadline(self, ctx:LinguaFrancaParser.DeadlineContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#sTP.
    def enterSTP(self, ctx:LinguaFrancaParser.STPContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#sTP.
    def exitSTP(self, ctx:LinguaFrancaParser.STPContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#preamble.
    def enterPreamble(self, ctx:LinguaFrancaParser.PreambleContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#preamble.
    def exitPreamble(self, ctx:LinguaFrancaParser.PreambleContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#instantiation.
    def enterInstantiation(self, ctx:LinguaFrancaParser.InstantiationContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#instantiation.
    def exitInstantiation(self, ctx:LinguaFrancaParser.InstantiationContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#connection.
    def enterConnection(self, ctx:LinguaFrancaParser.ConnectionContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#connection.
    def exitConnection(self, ctx:LinguaFrancaParser.ConnectionContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#serializer.
    def enterSerializer(self, ctx:LinguaFrancaParser.SerializerContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#serializer.
    def exitSerializer(self, ctx:LinguaFrancaParser.SerializerContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#attribute.
    def enterAttribute(self, ctx:LinguaFrancaParser.AttributeContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#attribute.
    def exitAttribute(self, ctx:LinguaFrancaParser.AttributeContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#attrParm.
    def enterAttrParm(self, ctx:LinguaFrancaParser.AttrParmContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#attrParm.
    def exitAttrParm(self, ctx:LinguaFrancaParser.AttrParmContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#attrParmValue.
    def enterAttrParmValue(self, ctx:LinguaFrancaParser.AttrParmValueContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#attrParmValue.
    def exitAttrParmValue(self, ctx:LinguaFrancaParser.AttrParmValueContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#keyValuePairs.
    def enterKeyValuePairs(self, ctx:LinguaFrancaParser.KeyValuePairsContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#keyValuePairs.
    def exitKeyValuePairs(self, ctx:LinguaFrancaParser.KeyValuePairsContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#keyValuePair.
    def enterKeyValuePair(self, ctx:LinguaFrancaParser.KeyValuePairContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#keyValuePair.
    def exitKeyValuePair(self, ctx:LinguaFrancaParser.KeyValuePairContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#array.
    def enterArray(self, ctx:LinguaFrancaParser.ArrayContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#array.
    def exitArray(self, ctx:LinguaFrancaParser.ArrayContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#element.
    def enterElement(self, ctx:LinguaFrancaParser.ElementContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#element.
    def exitElement(self, ctx:LinguaFrancaParser.ElementContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#typedVariable.
    def enterTypedVariable(self, ctx:LinguaFrancaParser.TypedVariableContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#typedVariable.
    def exitTypedVariable(self, ctx:LinguaFrancaParser.TypedVariableContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#variable.
    def enterVariable(self, ctx:LinguaFrancaParser.VariableContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#variable.
    def exitVariable(self, ctx:LinguaFrancaParser.VariableContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#varRef.
    def enterVarRef(self, ctx:LinguaFrancaParser.VarRefContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#varRef.
    def exitVarRef(self, ctx:LinguaFrancaParser.VarRefContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#varRefOrModeTransition.
    def enterVarRefOrModeTransition(self, ctx:LinguaFrancaParser.VarRefOrModeTransitionContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#varRefOrModeTransition.
    def exitVarRefOrModeTransition(self, ctx:LinguaFrancaParser.VarRefOrModeTransitionContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#assignment.
    def enterAssignment(self, ctx:LinguaFrancaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#assignment.
    def exitAssignment(self, ctx:LinguaFrancaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#parameter.
    def enterParameter(self, ctx:LinguaFrancaParser.ParameterContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#parameter.
    def exitParameter(self, ctx:LinguaFrancaParser.ParameterContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#argumentsForm1.
    def enterArgumentsForm1(self, ctx:LinguaFrancaParser.ArgumentsForm1Context):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#argumentsForm1.
    def exitArgumentsForm1(self, ctx:LinguaFrancaParser.ArgumentsForm1Context):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#argumentsForm2.
    def enterArgumentsForm2(self, ctx:LinguaFrancaParser.ArgumentsForm2Context):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#argumentsForm2.
    def exitArgumentsForm2(self, ctx:LinguaFrancaParser.ArgumentsForm2Context):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#argumentsForm3.
    def enterArgumentsForm3(self, ctx:LinguaFrancaParser.ArgumentsForm3Context):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#argumentsForm3.
    def exitArgumentsForm3(self, ctx:LinguaFrancaParser.ArgumentsForm3Context):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#argumentsForm4.
    def enterArgumentsForm4(self, ctx:LinguaFrancaParser.ArgumentsForm4Context):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#argumentsForm4.
    def exitArgumentsForm4(self, ctx:LinguaFrancaParser.ArgumentsForm4Context):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#expression.
    def enterExpression(self, ctx:LinguaFrancaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#expression.
    def exitExpression(self, ctx:LinguaFrancaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#value.
    def enterValue(self, ctx:LinguaFrancaParser.ValueContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#value.
    def exitValue(self, ctx:LinguaFrancaParser.ValueContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#valueArray.
    def enterValueArray(self, ctx:LinguaFrancaParser.ValueArrayContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#valueArray.
    def exitValueArray(self, ctx:LinguaFrancaParser.ValueArrayContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#portDecl.
    def enterPortDecl(self, ctx:LinguaFrancaParser.PortDeclContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#portDecl.
    def exitPortDecl(self, ctx:LinguaFrancaParser.PortDeclContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#type.
    def enterType(self, ctx:LinguaFrancaParser.TypeContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#type.
    def exitType(self, ctx:LinguaFrancaParser.TypeContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#arraySpec.
    def enterArraySpec(self, ctx:LinguaFrancaParser.ArraySpecContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#arraySpec.
    def exitArraySpec(self, ctx:LinguaFrancaParser.ArraySpecContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#widthSpec.
    def enterWidthSpec(self, ctx:LinguaFrancaParser.WidthSpecContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#widthSpec.
    def exitWidthSpec(self, ctx:LinguaFrancaParser.WidthSpecContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#widthTerm.
    def enterWidthTerm(self, ctx:LinguaFrancaParser.WidthTermContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#widthTerm.
    def exitWidthTerm(self, ctx:LinguaFrancaParser.WidthTermContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#ipV4host.
    def enterIpV4host(self, ctx:LinguaFrancaParser.IpV4hostContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#ipV4host.
    def exitIpV4host(self, ctx:LinguaFrancaParser.IpV4hostContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#ipV6host.
    def enterIpV6host(self, ctx:LinguaFrancaParser.IpV6hostContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#ipV6host.
    def exitIpV6host(self, ctx:LinguaFrancaParser.IpV6hostContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#namedHost.
    def enterNamedHost(self, ctx:LinguaFrancaParser.NamedHostContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#namedHost.
    def exitNamedHost(self, ctx:LinguaFrancaParser.NamedHostContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#host.
    def enterHost(self, ctx:LinguaFrancaParser.HostContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#host.
    def exitHost(self, ctx:LinguaFrancaParser.HostContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#hostName.
    def enterHostName(self, ctx:LinguaFrancaParser.HostNameContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#hostName.
    def exitHostName(self, ctx:LinguaFrancaParser.HostNameContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#code.
    def enterCode(self, ctx:LinguaFrancaParser.CodeContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#code.
    def exitCode(self, ctx:LinguaFrancaParser.CodeContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#actionOrigin.
    def enterActionOrigin(self, ctx:LinguaFrancaParser.ActionOriginContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#actionOrigin.
    def exitActionOrigin(self, ctx:LinguaFrancaParser.ActionOriginContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#visibility.
    def enterVisibility(self, ctx:LinguaFrancaParser.VisibilityContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#visibility.
    def exitVisibility(self, ctx:LinguaFrancaParser.VisibilityContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#builtinTrigger.
    def enterBuiltinTrigger(self, ctx:LinguaFrancaParser.BuiltinTriggerContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#builtinTrigger.
    def exitBuiltinTrigger(self, ctx:LinguaFrancaParser.BuiltinTriggerContext):
        pass


    # Enter a parse tree produced by LinguaFrancaParser#modeTransition.
    def enterModeTransition(self, ctx:LinguaFrancaParser.ModeTransitionContext):
        pass

    # Exit a parse tree produced by LinguaFrancaParser#modeTransition.
    def exitModeTransition(self, ctx:LinguaFrancaParser.ModeTransitionContext):
        pass



del LinguaFrancaParser