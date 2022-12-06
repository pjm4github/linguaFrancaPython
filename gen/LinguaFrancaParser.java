// Generated from C:/Users/pmora/Documents/Git/GitHub/LinguaFranca\LinguaFranca.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LinguaFrancaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, Boolean=56, Time=57, Type=58, ArraySpec=59, 
		IPV4Host=60, IPV6Host=61, NamedHost=62, HostName=63, DottedName=64, SignedInt=65, 
		Literal=66, WS=67, TRUE=68, FALSE=69, ID=70, INT=71, NEGINT=72, FLOAT_EXP_SUFFIX=73, 
		SL_COMMENT=74, ML_COMMENT=75, LT_ANNOT=76, STRING=77, CHAR_LIT=78, ANY_OTHER=79, 
		Kebab=80, IPV4Addr=81, IPV6Seg=82, IPV6Addr=83, SignedFloat=84, Code=85, 
		FSName=86, Path=87, TimeUnit=88, Body=89, DOUBLE_COLON=90, OPEN_CLOSE_SQ_BR=91, 
		Token=92;
	public static final int
		RULE_model = 0, RULE_importDecl = 1, RULE_reactorDecl = 2, RULE_importedReactor = 3, 
		RULE_reactor = 4, RULE_typeParm = 5, RULE_typeExpr = 6, RULE_targetDecl = 7, 
		RULE_stateVar = 8, RULE_method = 9, RULE_methodArgument = 10, RULE_inputDecl = 11, 
		RULE_outputDecl = 12, RULE_timer = 13, RULE_modeDecl = 14, RULE_action = 15, 
		RULE_reaction = 16, RULE_triggerRef = 17, RULE_builtinTriggerRef = 18, 
		RULE_deadline = 19, RULE_sTP = 20, RULE_preamble = 21, RULE_instantiation = 22, 
		RULE_connection = 23, RULE_serializer = 24, RULE_attribute = 25, RULE_attrParm = 26, 
		RULE_attrParmValue = 27, RULE_keyValuePairs = 28, RULE_keyValuePair = 29, 
		RULE_array = 30, RULE_element = 31, RULE_typedVariable = 32, RULE_variable = 33, 
		RULE_varRef = 34, RULE_varRefOrModeTransition = 35, RULE_assignment = 36, 
		RULE_parameter = 37, RULE_expression = 38, RULE_parameterReference = 39, 
		RULE_portDecl = 40, RULE_widthSpec = 41, RULE_widthTerm = 42, RULE_host = 43, 
		RULE_actionOrigin = 44, RULE_visibility = 45, RULE_builtinTrigger = 46, 
		RULE_modeTransition = 47;
	private static String[] makeRuleNames() {
		return new String[] {
			"model", "importDecl", "reactorDecl", "importedReactor", "reactor", "typeParm", 
			"typeExpr", "targetDecl", "stateVar", "method", "methodArgument", "inputDecl", 
			"outputDecl", "timer", "modeDecl", "action", "reaction", "triggerRef", 
			"builtinTriggerRef", "deadline", "sTP", "preamble", "instantiation", 
			"connection", "serializer", "attribute", "attrParm", "attrParmValue", 
			"keyValuePairs", "keyValuePair", "array", "element", "typedVariable", 
			"variable", "varRef", "varRefOrModeTransition", "assignment", "parameter", 
			"expression", "parameterReference", "portDecl", "widthSpec", "widthTerm", 
			"host", "actionOrigin", "visibility", "builtinTrigger", "modeTransition"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'import'", "','", "'from'", "';'", "'as'", "'federated'", "'main'", 
			"'realtime'", "'reactor'", "'<'", "'>'", "'('", "')'", "'at'", "'extends'", 
			"'{'", "'}'", "'target'", "'reset'", "'state'", "':'", "'const'", "'method'", 
			"'mutable'", "'input'", "'output'", "'timer'", "'initial'", "'mode'", 
			"'action'", "'reaction'", "'mutation'", "'->'", "'deadline'", "'STP'", 
			"'preamble'", "'='", "'new'", "'+'", "'~>'", "'after'", "'serializer'", 
			"'@'", "'['", "']'", "'.'", "'interleaved'", "'widthof('", "'logical'", 
			"'physical'", "'private'", "'public'", "'startup'", "'shutdown'", "'history'", 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "'::'", "'[]'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "Boolean", "Time", "Type", 
			"ArraySpec", "IPV4Host", "IPV6Host", "NamedHost", "HostName", "DottedName", 
			"SignedInt", "Literal", "WS", "TRUE", "FALSE", "ID", "INT", "NEGINT", 
			"FLOAT_EXP_SUFFIX", "SL_COMMENT", "ML_COMMENT", "LT_ANNOT", "STRING", 
			"CHAR_LIT", "ANY_OTHER", "Kebab", "IPV4Addr", "IPV6Seg", "IPV6Addr", 
			"SignedFloat", "Code", "FSName", "Path", "TimeUnit", "Body", "DOUBLE_COLON", 
			"OPEN_CLOSE_SQ_BR", "Token"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LinguaFranca.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LinguaFrancaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ModelContext extends ParserRuleContext {
		public TargetDeclContext targetDecl() {
			return getRuleContext(TargetDeclContext.class,0);
		}
		public List<ImportDeclContext> importDecl() {
			return getRuleContexts(ImportDeclContext.class);
		}
		public ImportDeclContext importDecl(int i) {
			return getRuleContext(ImportDeclContext.class,i);
		}
		public List<PreambleContext> preamble() {
			return getRuleContexts(PreambleContext.class);
		}
		public PreambleContext preamble(int i) {
			return getRuleContext(PreambleContext.class,i);
		}
		public List<ReactorContext> reactor() {
			return getRuleContexts(ReactorContext.class);
		}
		public ReactorContext reactor(int i) {
			return getRuleContext(ReactorContext.class,i);
		}
		public ModelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_model; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterModel(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitModel(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitModel(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ModelContext model() throws RecognitionException {
		ModelContext _localctx = new ModelContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_model);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			targetDecl();
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(97);
				importDecl();
				}
				}
				setState(102);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__35) | (1L << T__50) | (1L << T__51))) != 0)) {
				{
				{
				setState(103);
				preamble();
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(110); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(109);
				reactor();
				}
				}
				setState(112); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__42))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImportDeclContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(LinguaFrancaParser.STRING, 0); }
		public List<ImportedReactorContext> importedReactor() {
			return getRuleContexts(ImportedReactorContext.class);
		}
		public ImportedReactorContext importedReactor(int i) {
			return getRuleContext(ImportedReactorContext.class,i);
		}
		public ImportDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterImportDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitImportDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitImportDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ImportDeclContext importDecl() throws RecognitionException {
		ImportDeclContext _localctx = new ImportDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_importDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(T__0);
			setState(116); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(115);
				importedReactor();
				}
				}
				setState(118); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__42))) != 0) );
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(120);
				match(T__1);
				setState(122); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(121);
					importedReactor();
					}
					}
					setState(124); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__42))) != 0) );
				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(131);
			match(T__2);
			setState(132);
			match(STRING);
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(133);
				match(T__3);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReactorDeclContext extends ParserRuleContext {
		public ReactorContext reactor() {
			return getRuleContext(ReactorContext.class,0);
		}
		public ImportedReactorContext importedReactor() {
			return getRuleContext(ImportedReactorContext.class,0);
		}
		public ReactorDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reactorDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterReactorDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitReactorDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitReactorDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReactorDeclContext reactorDecl() throws RecognitionException {
		ReactorDeclContext _localctx = new ReactorDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_reactorDecl);
		try {
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(136);
				reactor();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(137);
				importedReactor();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImportedReactorContext extends ParserRuleContext {
		public ReactorContext reactor() {
			return getRuleContext(ReactorContext.class,0);
		}
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public ImportedReactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importedReactor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterImportedReactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitImportedReactor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitImportedReactor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ImportedReactorContext importedReactor() throws RecognitionException {
		ImportedReactorContext _localctx = new ImportedReactorContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_importedReactor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			reactor();
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(141);
				match(T__4);
				setState(142);
				match(ID);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReactorContext extends ParserRuleContext {
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<TypeParmContext> typeParm() {
			return getRuleContexts(TypeParmContext.class);
		}
		public TypeParmContext typeParm(int i) {
			return getRuleContext(TypeParmContext.class,i);
		}
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public HostContext host() {
			return getRuleContext(HostContext.class,0);
		}
		public List<ReactorDeclContext> reactorDecl() {
			return getRuleContexts(ReactorDeclContext.class);
		}
		public ReactorDeclContext reactorDecl(int i) {
			return getRuleContext(ReactorDeclContext.class,i);
		}
		public List<PreambleContext> preamble() {
			return getRuleContexts(PreambleContext.class);
		}
		public PreambleContext preamble(int i) {
			return getRuleContext(PreambleContext.class,i);
		}
		public List<StateVarContext> stateVar() {
			return getRuleContexts(StateVarContext.class);
		}
		public StateVarContext stateVar(int i) {
			return getRuleContext(StateVarContext.class,i);
		}
		public List<MethodContext> method() {
			return getRuleContexts(MethodContext.class);
		}
		public MethodContext method(int i) {
			return getRuleContext(MethodContext.class,i);
		}
		public List<InputDeclContext> inputDecl() {
			return getRuleContexts(InputDeclContext.class);
		}
		public InputDeclContext inputDecl(int i) {
			return getRuleContext(InputDeclContext.class,i);
		}
		public List<OutputDeclContext> outputDecl() {
			return getRuleContexts(OutputDeclContext.class);
		}
		public OutputDeclContext outputDecl(int i) {
			return getRuleContext(OutputDeclContext.class,i);
		}
		public List<TimerContext> timer() {
			return getRuleContexts(TimerContext.class);
		}
		public TimerContext timer(int i) {
			return getRuleContext(TimerContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public List<InstantiationContext> instantiation() {
			return getRuleContexts(InstantiationContext.class);
		}
		public InstantiationContext instantiation(int i) {
			return getRuleContext(InstantiationContext.class,i);
		}
		public List<ConnectionContext> connection() {
			return getRuleContexts(ConnectionContext.class);
		}
		public ConnectionContext connection(int i) {
			return getRuleContext(ConnectionContext.class,i);
		}
		public List<ReactionContext> reaction() {
			return getRuleContexts(ReactionContext.class);
		}
		public ReactionContext reaction(int i) {
			return getRuleContext(ReactionContext.class,i);
		}
		public List<ModeDeclContext> modeDecl() {
			return getRuleContexts(ModeDeclContext.class);
		}
		public ModeDeclContext modeDecl(int i) {
			return getRuleContext(ModeDeclContext.class,i);
		}
		public ReactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reactor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterReactor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitReactor(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitReactor(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReactorContext reactor() throws RecognitionException {
		ReactorContext _localctx = new ReactorContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_reactor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(145);
				attribute();
				}
				}
				setState(150);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			{
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5 || _la==T__6) {
				{
				setState(151);
				_la = _input.LA(1);
				if ( !(_la==T__5 || _la==T__6) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__7) {
				{
				setState(154);
				match(T__7);
				}
			}

			}
			setState(157);
			match(T__8);
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(158);
				match(ID);
				}
			}

			setState(172);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(161);
				match(T__9);
				setState(162);
				typeParm();
				setState(167);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(163);
					match(T__1);
					setState(164);
					typeParm();
					}
					}
					setState(169);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(170);
				match(T__10);
				}
			}

			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(174);
				match(T__11);
				setState(175);
				parameter();
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(176);
					match(T__1);
					setState(177);
					parameter();
					}
					}
					setState(182);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(183);
				match(T__12);
				}
			}

			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(187);
				match(T__13);
				setState(188);
				host();
				}
			}

			setState(200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(191);
				match(T__14);
				{
				setState(192);
				reactorDecl();
				setState(197);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(193);
					match(T__1);
					setState(194);
					reactorDecl();
					}
					}
					setState(199);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
			}

			setState(202);
			match(T__15);
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 12)) & ~0x3f) == 0 && ((1L << (_la - 12)) & ((1L << (T__11 - 12)) | (1L << (T__18 - 12)) | (1L << (T__19 - 12)) | (1L << (T__21 - 12)) | (1L << (T__22 - 12)) | (1L << (T__23 - 12)) | (1L << (T__24 - 12)) | (1L << (T__25 - 12)) | (1L << (T__26 - 12)) | (1L << (T__27 - 12)) | (1L << (T__28 - 12)) | (1L << (T__29 - 12)) | (1L << (T__30 - 12)) | (1L << (T__31 - 12)) | (1L << (T__35 - 12)) | (1L << (T__42 - 12)) | (1L << (T__46 - 12)) | (1L << (T__48 - 12)) | (1L << (T__49 - 12)) | (1L << (T__50 - 12)) | (1L << (T__51 - 12)) | (1L << (ID - 12)))) != 0)) {
				{
				setState(214);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
				case 1:
					{
					{
					setState(203);
					preamble();
					}
					}
					break;
				case 2:
					{
					{
					setState(204);
					stateVar();
					}
					}
					break;
				case 3:
					{
					{
					setState(205);
					method();
					}
					}
					break;
				case 4:
					{
					{
					setState(206);
					inputDecl();
					}
					}
					break;
				case 5:
					{
					{
					setState(207);
					outputDecl();
					}
					}
					break;
				case 6:
					{
					{
					setState(208);
					timer();
					}
					}
					break;
				case 7:
					{
					{
					setState(209);
					action();
					}
					}
					break;
				case 8:
					{
					{
					setState(210);
					instantiation();
					}
					}
					break;
				case 9:
					{
					{
					setState(211);
					connection();
					}
					}
					break;
				case 10:
					{
					{
					setState(212);
					reaction();
					}
					}
					break;
				case 11:
					{
					{
					setState(213);
					modeDecl();
					}
					}
					break;
				}
				}
				setState(218);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(219);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeParmContext extends ParserRuleContext {
		public TypeExprContext typeExpr() {
			return getRuleContext(TypeExprContext.class,0);
		}
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public TypeParmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeParm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterTypeParm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitTypeParm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitTypeParm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeParmContext typeParm() throws RecognitionException {
		TypeParmContext _localctx = new TypeParmContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_typeParm);
		try {
			setState(223);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				typeExpr();
				}
				break;
			case Code:
				enterOuterAlt(_localctx, 2);
				{
				setState(222);
				match(Code);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeExprContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(LinguaFrancaParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LinguaFrancaParser.ID, i);
		}
		public TypeExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeExpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterTypeExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitTypeExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitTypeExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeExprContext typeExpr() throws RecognitionException {
		TypeExprContext _localctx = new TypeExprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_typeExpr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(225);
				match(ID);
				}
				}
				setState(228); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TargetDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public KeyValuePairsContext keyValuePairs() {
			return getRuleContext(KeyValuePairsContext.class,0);
		}
		public TargetDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_targetDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterTargetDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitTargetDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitTargetDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TargetDeclContext targetDecl() throws RecognitionException {
		TargetDeclContext _localctx = new TargetDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_targetDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			match(T__17);
			setState(231);
			match(ID);
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(232);
				keyValuePairs();
				}
			}

			setState(236);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(235);
				match(T__3);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StateVarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public StateVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stateVar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterStateVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitStateVar(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitStateVar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StateVarContext stateVar() throws RecognitionException {
		StateVarContext _localctx = new StateVarContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_stateVar);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(238);
				attribute();
				}
				}
				setState(243);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(245);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(244);
				match(T__18);
				}
			}

			setState(247);
			match(T__19);
			setState(248);
			match(ID);
			{
			setState(251);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(249);
				match(T__20);
				{
				setState(250);
				match(Type);
				}
				}
			}

			setState(277);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				{
				{
				setState(253);
				match(T__11);
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (Time - 43)) | (1L << (Literal - 43)) | (1L << (ID - 43)) | (1L << (Code - 43)))) != 0)) {
					{
					setState(254);
					expression();
					setState(259);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__1) {
						{
						{
						setState(255);
						match(T__1);
						setState(256);
						expression();
						}
						}
						setState(261);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(264);
				match(T__12);
				}
				}
				break;
			case 2:
				{
				{
				setState(265);
				match(T__15);
				setState(274);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (Time - 43)) | (1L << (Literal - 43)) | (1L << (ID - 43)) | (1L << (Code - 43)))) != 0)) {
					{
					setState(266);
					expression();
					setState(271);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__1) {
						{
						{
						setState(267);
						match(T__1);
						setState(268);
						expression();
						}
						}
						setState(273);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(276);
				match(T__16);
				}
				}
				break;
			}
			}
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(279);
				match(T__3);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public List<MethodArgumentContext> methodArgument() {
			return getRuleContexts(MethodArgumentContext.class);
		}
		public MethodArgumentContext methodArgument(int i) {
			return getRuleContext(MethodArgumentContext.class,i);
		}
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public MethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterMethod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitMethod(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitMethod(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MethodContext method() throws RecognitionException {
		MethodContext _localctx = new MethodContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_method);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__21) {
				{
				setState(282);
				match(T__21);
				}
			}

			setState(285);
			match(T__22);
			setState(286);
			match(ID);
			setState(287);
			match(T__11);
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(288);
				methodArgument();
				setState(293);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(289);
					match(T__1);
					setState(290);
					methodArgument();
					}
					}
					setState(295);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(298);
			match(T__12);
			setState(301);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(299);
				match(T__20);
				setState(300);
				match(Type);
				}
			}

			setState(303);
			match(Code);
			setState(305);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(304);
				match(T__3);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MethodArgumentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public MethodArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodArgument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterMethodArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitMethodArgument(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitMethodArgument(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MethodArgumentContext methodArgument() throws RecognitionException {
		MethodArgumentContext _localctx = new MethodArgumentContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_methodArgument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(307);
			match(ID);
			setState(310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(308);
				match(T__20);
				setState(309);
				match(Type);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InputDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public WidthSpecContext widthSpec() {
			return getRuleContext(WidthSpecContext.class,0);
		}
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public InputDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inputDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterInputDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitInputDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitInputDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InputDeclContext inputDecl() throws RecognitionException {
		InputDeclContext _localctx = new InputDeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_inputDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(312);
				attribute();
				}
				}
				setState(317);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(319);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__23) {
				{
				setState(318);
				match(T__23);
				}
			}

			setState(321);
			match(T__24);
			setState(323);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__43 || _la==OPEN_CLOSE_SQ_BR) {
				{
				setState(322);
				widthSpec();
				}
			}

			setState(325);
			match(ID);
			setState(328);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(326);
				match(T__20);
				setState(327);
				match(Type);
				}
			}

			setState(331);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				{
				setState(330);
				match(T__3);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OutputDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public WidthSpecContext widthSpec() {
			return getRuleContext(WidthSpecContext.class,0);
		}
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public OutputDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_outputDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterOutputDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitOutputDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitOutputDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OutputDeclContext outputDecl() throws RecognitionException {
		OutputDeclContext _localctx = new OutputDeclContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_outputDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(333);
				attribute();
				}
				}
				setState(338);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(339);
			match(T__25);
			setState(341);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__43 || _la==OPEN_CLOSE_SQ_BR) {
				{
				setState(340);
				widthSpec();
				}
			}

			setState(343);
			match(ID);
			setState(346);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(344);
				match(T__20);
				setState(345);
				match(Type);
				}
			}

			setState(349);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				{
				setState(348);
				match(T__3);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TimerContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TimerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_timer; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterTimer(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitTimer(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitTimer(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TimerContext timer() throws RecognitionException {
		TimerContext _localctx = new TimerContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_timer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(354);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(351);
				attribute();
				}
				}
				setState(356);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(357);
			match(T__26);
			setState(358);
			match(ID);
			setState(367);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,52,_ctx) ) {
			case 1:
				{
				setState(359);
				match(T__11);
				setState(360);
				expression();
				setState(363);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(361);
					match(T__1);
					setState(362);
					expression();
					}
				}

				setState(365);
				match(T__12);
				}
				break;
			}
			setState(370);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,53,_ctx) ) {
			case 1:
				{
				setState(369);
				match(T__3);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ModeDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<StateVarContext> stateVar() {
			return getRuleContexts(StateVarContext.class);
		}
		public StateVarContext stateVar(int i) {
			return getRuleContext(StateVarContext.class,i);
		}
		public List<TimerContext> timer() {
			return getRuleContexts(TimerContext.class);
		}
		public TimerContext timer(int i) {
			return getRuleContext(TimerContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public List<InstantiationContext> instantiation() {
			return getRuleContexts(InstantiationContext.class);
		}
		public InstantiationContext instantiation(int i) {
			return getRuleContext(InstantiationContext.class,i);
		}
		public List<ConnectionContext> connection() {
			return getRuleContexts(ConnectionContext.class);
		}
		public ConnectionContext connection(int i) {
			return getRuleContext(ConnectionContext.class,i);
		}
		public List<ReactionContext> reaction() {
			return getRuleContexts(ReactionContext.class);
		}
		public ReactionContext reaction(int i) {
			return getRuleContext(ReactionContext.class,i);
		}
		public ModeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modeDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterModeDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitModeDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitModeDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ModeDeclContext modeDecl() throws RecognitionException {
		ModeDeclContext _localctx = new ModeDeclContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_modeDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			modeDecl
			setState(374);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__27) {
				{
				setState(373);
				match(T__27);
				}
			}

			setState(376);
			match(T__28);
			setState(378);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(377);
				match(ID);
				}
			}

			setState(380);
			match(T__15);
			setState(389);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 12)) & ~0x3f) == 0 && ((1L << (_la - 12)) & ((1L << (T__11 - 12)) | (1L << (T__18 - 12)) | (1L << (T__19 - 12)) | (1L << (T__23 - 12)) | (1L << (T__24 - 12)) | (1L << (T__25 - 12)) | (1L << (T__26 - 12)) | (1L << (T__27 - 12)) | (1L << (T__28 - 12)) | (1L << (T__29 - 12)) | (1L << (T__30 - 12)) | (1L << (T__31 - 12)) | (1L << (T__42 - 12)) | (1L << (T__46 - 12)) | (1L << (T__48 - 12)) | (1L << (T__49 - 12)) | (1L << (ID - 12)))) != 0)) {
				{
				setState(387);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,56,_ctx) ) {
				case 1:
					{
					{
					setState(381);
					stateVar();
					}
					}
					break;
				case 2:
					{
					{
					setState(382);
					timer();
					}
					}
					break;
				case 3:
					{
					{
					setState(383);
					action();
					}
					}
					break;
				case 4:
					{
					{
					setState(384);
					instantiation();
					}
					}
					break;
				case 5:
					{
					{
					setState(385);
					connection();
					}
					}
					break;
				case 6:
					{
					{
					setState(386);
					reaction();
					}
					}
					break;
				}
				}
				setState(391);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(392);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ActionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public ActionOriginContext actionOrigin() {
			return getRuleContext(ActionOriginContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public TerminalNode STRING() { return getToken(LinguaFrancaParser.STRING, 0); }
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitAction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitAction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(394);
				attribute();
				}
				}
				setState(399);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(401);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__48 || _la==T__49) {
				{
				setState(400);
				actionOrigin();
				}
			}

			setState(403);
			match(T__29);
			setState(404);
			match(ID);
			setState(417);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,62,_ctx) ) {
			case 1:
				{
				setState(405);
				match(T__11);
				setState(406);
				expression();
				setState(413);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(407);
					match(T__1);
					setState(408);
					expression();
					setState(411);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__1) {
						{
						setState(409);
						match(T__1);
						setState(410);
						match(STRING);
						}
					}

					}
				}

				setState(415);
				match(T__12);
				}
				break;
			}
			setState(421);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(419);
				match(T__20);
				setState(420);
				match(Type);
				}
			}

			setState(424);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,64,_ctx) ) {
			case 1:
				{
				setState(423);
				match(T__3);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReactionContext extends ParserRuleContext {
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public List<VarRefContext> varRef() {
			return getRuleContexts(VarRefContext.class);
		}
		public VarRefContext varRef(int i) {
			return getRuleContext(VarRefContext.class,i);
		}
		public List<VarRefOrModeTransitionContext> varRefOrModeTransition() {
			return getRuleContexts(VarRefOrModeTransitionContext.class);
		}
		public VarRefOrModeTransitionContext varRefOrModeTransition(int i) {
			return getRuleContext(VarRefOrModeTransitionContext.class,i);
		}
		public STPContext sTP() {
			return getRuleContext(STPContext.class,0);
		}
		public DeadlineContext deadline() {
			return getRuleContext(DeadlineContext.class,0);
		}
		public List<TriggerRefContext> triggerRef() {
			return getRuleContexts(TriggerRefContext.class);
		}
		public TriggerRefContext triggerRef(int i) {
			return getRuleContext(TriggerRefContext.class,i);
		}
		public ReactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterReaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitReaction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitReaction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReactionContext reaction() throws RecognitionException {
		ReactionContext _localctx = new ReactionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_reaction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(426);
				attribute();
				}
				}
				setState(431);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(434);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__30:
				{
				{
				setState(432);
				match(T__30);
				}
				}
				break;
			case T__31:
				{
				setState(433);
				match(T__31);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(448);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(436);
				match(T__11);
				setState(445);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 19)) & ~0x3f) == 0 && ((1L << (_la - 19)) & ((1L << (T__18 - 19)) | (1L << (T__23 - 19)) | (1L << (T__24 - 19)) | (1L << (T__25 - 19)) | (1L << (T__26 - 19)) | (1L << (T__27 - 19)) | (1L << (T__28 - 19)) | (1L << (T__29 - 19)) | (1L << (T__42 - 19)) | (1L << (T__46 - 19)) | (1L << (T__48 - 19)) | (1L << (T__49 - 19)) | (1L << (T__52 - 19)) | (1L << (T__53 - 19)) | (1L << (ID - 19)))) != 0)) {
					{
					setState(437);
					triggerRef();
					setState(442);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__1) {
						{
						{
						setState(438);
						match(T__1);
						setState(439);
						triggerRef();
						}
						}
						setState(444);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(447);
				match(T__12);
				}
			}

			setState(458);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 24)) & ~0x3f) == 0 && ((1L << (_la - 24)) & ((1L << (T__23 - 24)) | (1L << (T__24 - 24)) | (1L << (T__25 - 24)) | (1L << (T__26 - 24)) | (1L << (T__27 - 24)) | (1L << (T__28 - 24)) | (1L << (T__29 - 24)) | (1L << (T__42 - 24)) | (1L << (T__46 - 24)) | (1L << (T__48 - 24)) | (1L << (T__49 - 24)) | (1L << (ID - 24)))) != 0)) {
				{
				setState(450);
				varRef();
				setState(455);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(451);
					match(T__1);
					setState(452);
					varRef();
					}
					}
					setState(457);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(469);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32) {
				{
				setState(460);
				match(T__32);
				setState(461);
				varRefOrModeTransition();
				setState(466);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(462);
					match(T__1);
					setState(463);
					varRefOrModeTransition();
					}
					}
					setState(468);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(471);
			match(Code);
			setState(473);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__34) {
				{
				setState(472);
				sTP();
				}
			}

			setState(476);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__33) {
				{
				setState(475);
				deadline();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TriggerRefContext extends ParserRuleContext {
		public BuiltinTriggerRefContext builtinTriggerRef() {
			return getRuleContext(BuiltinTriggerRefContext.class,0);
		}
		public VarRefContext varRef() {
			return getRuleContext(VarRefContext.class,0);
		}
		public TriggerRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_triggerRef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterTriggerRef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitTriggerRef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitTriggerRef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TriggerRefContext triggerRef() throws RecognitionException {
		TriggerRefContext _localctx = new TriggerRefContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_triggerRef);
		try {
			setState(480);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__18:
			case T__52:
			case T__53:
				enterOuterAlt(_localctx, 1);
				{
				setState(478);
				builtinTriggerRef();
				}
				break;
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__42:
			case T__46:
			case T__48:
			case T__49:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(479);
				varRef();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BuiltinTriggerRefContext extends ParserRuleContext {
		public BuiltinTriggerContext builtinTrigger() {
			return getRuleContext(BuiltinTriggerContext.class,0);
		}
		public BuiltinTriggerRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_builtinTriggerRef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterBuiltinTriggerRef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitBuiltinTriggerRef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitBuiltinTriggerRef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BuiltinTriggerRefContext builtinTriggerRef() throws RecognitionException {
		BuiltinTriggerRefContext _localctx = new BuiltinTriggerRefContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_builtinTriggerRef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(482);
			builtinTrigger();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeadlineContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public DeadlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deadline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterDeadline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitDeadline(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitDeadline(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DeadlineContext deadline() throws RecognitionException {
		DeadlineContext _localctx = new DeadlineContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_deadline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(484);
			match(T__33);
			setState(485);
			match(T__11);
			setState(486);
			expression();
			setState(487);
			match(T__12);
			setState(488);
			match(Code);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class STPContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public STPContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sTP; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterSTP(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitSTP(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitSTP(this);
			else return visitor.visitChildren(this);
		}
	}

	public final STPContext sTP() throws RecognitionException {
		STPContext _localctx = new STPContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_sTP);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(490);
			match(T__34);
			setState(491);
			match(T__11);
			setState(492);
			expression();
			setState(493);
			match(T__12);
			setState(494);
			match(Code);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PreambleContext extends ParserRuleContext {
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public VisibilityContext visibility() {
			return getRuleContext(VisibilityContext.class,0);
		}
		public PreambleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preamble; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterPreamble(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitPreamble(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitPreamble(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PreambleContext preamble() throws RecognitionException {
		PreambleContext _localctx = new PreambleContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_preamble);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(497);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__50 || _la==T__51) {
				{
				setState(496);
				visibility();
				}
			}

			setState(499);
			match(T__35);
			setState(500);
			match(Code);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstantiationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public ReactorDeclContext reactorDecl() {
			return getRuleContext(ReactorDeclContext.class,0);
		}
		public WidthSpecContext widthSpec() {
			return getRuleContext(WidthSpecContext.class,0);
		}
		public List<TypeParmContext> typeParm() {
			return getRuleContexts(TypeParmContext.class);
		}
		public TypeParmContext typeParm(int i) {
			return getRuleContext(TypeParmContext.class,i);
		}
		public List<AssignmentContext> assignment() {
			return getRuleContexts(AssignmentContext.class);
		}
		public AssignmentContext assignment(int i) {
			return getRuleContext(AssignmentContext.class,i);
		}
		public HostContext host() {
			return getRuleContext(HostContext.class,0);
		}
		public InstantiationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instantiation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterInstantiation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitInstantiation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitInstantiation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InstantiationContext instantiation() throws RecognitionException {
		InstantiationContext _localctx = new InstantiationContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_instantiation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(502);
			match(ID);
			setState(503);
			match(T__36);
			setState(504);
			match(T__37);
			setState(506);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__43 || _la==OPEN_CLOSE_SQ_BR) {
				{
				setState(505);
				widthSpec();
				}
			}

			setState(508);
			reactorDecl();
			setState(520);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(509);
				match(T__9);
				setState(510);
				typeParm();
				setState(515);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(511);
					match(T__1);
					setState(512);
					typeParm();
					}
					}
					setState(517);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(518);
				match(T__10);
				}
			}

			setState(522);
			match(T__11);
			setState(531);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__42 || _la==ID) {
				{
				setState(523);
				assignment();
				setState(528);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(524);
					match(T__1);
					setState(525);
					assignment();
					}
					}
					setState(530);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(533);
			match(T__12);
			setState(541);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
				{
				{
				setState(534);
				match(T__13);
				setState(535);
				host();
				setState(536);
				match(T__3);
				}
				}
				break;
			case T__3:
			case T__11:
			case T__16:
			case T__18:
			case T__19:
			case T__21:
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
			case T__31:
			case T__35:
			case T__42:
			case T__45:
			case T__46:
			case T__48:
			case T__49:
			case T__50:
			case T__51:
			case ID:
				{
				setState(539);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__3) {
					{
					setState(538);
					match(T__3);
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConnectionContext extends ParserRuleContext {
		public List<VarRefContext> varRef() {
			return getRuleContexts(VarRefContext.class);
		}
		public VarRefContext varRef(int i) {
			return getRuleContext(VarRefContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public SerializerContext serializer() {
			return getRuleContext(SerializerContext.class,0);
		}
		public ConnectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_connection; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterConnection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitConnection(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitConnection(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ConnectionContext connection() throws RecognitionException {
		ConnectionContext _localctx = new ConnectionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_connection);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(564);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__42:
			case T__46:
			case T__48:
			case T__49:
			case ID:
				{
				{
				setState(543);
				varRef();
				setState(548);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(544);
					match(T__1);
					setState(545);
					varRef();
					}
					}
					setState(550);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				break;
			case T__11:
				{
				{
				setState(551);
				match(T__11);
				setState(552);
				varRef();
				setState(557);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(553);
					match(T__1);
					setState(554);
					varRef();
					}
					}
					setState(559);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(560);
				match(T__12);
				setState(562);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__38) {
					{
					setState(561);
					match(T__38);
					}
				}

				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(566);
			_la = _input.LA(1);
			if ( !(_la==T__32 || _la==T__39) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(567);
			varRef();
			setState(572);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(568);
				match(T__1);
				setState(569);
				varRef();
				}
				}
				setState(574);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(577);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__40) {
				{
				setState(575);
				match(T__40);
				setState(576);
				expression();
				}
			}

			setState(580);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__41) {
				{
				setState(579);
				serializer();
				}
			}

			setState(583);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(582);
				match(T__3);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SerializerContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(LinguaFrancaParser.STRING, 0); }
		public SerializerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_serializer; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterSerializer(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitSerializer(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitSerializer(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SerializerContext serializer() throws RecognitionException {
		SerializerContext _localctx = new SerializerContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_serializer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(585);
			match(T__41);
			setState(586);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttributeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttrParmContext> attrParm() {
			return getRuleContexts(AttrParmContext.class);
		}
		public AttrParmContext attrParm(int i) {
			return getRuleContext(AttrParmContext.class,i);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterAttribute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitAttribute(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitAttribute(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_attribute);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(588);
			match(T__42);
			setState(589);
			match(ID);
			setState(605);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(590);
				match(T__11);
				setState(602);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (Boolean - 56)) | (1L << (SignedInt - 56)) | (1L << (ID - 56)) | (1L << (STRING - 56)) | (1L << (SignedFloat - 56)))) != 0)) {
					{
					setState(591);
					attrParm();
					setState(596);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,93,_ctx);
					while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
						if ( _alt==1 ) {
							{
							{
							setState(592);
							match(T__1);
							setState(593);
							attrParm();
							}
							} 
						}
						setState(598);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,93,_ctx);
					}
					setState(600);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__1) {
						{
						setState(599);
						match(T__1);
						}
					}

					}
				}

				setState(604);
				match(T__12);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttrParmContext extends ParserRuleContext {
		public AttrParmValueContext attrParmValue() {
			return getRuleContext(AttrParmValueContext.class,0);
		}
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public AttrParmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrParm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterAttrParm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitAttrParm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitAttrParm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AttrParmContext attrParm() throws RecognitionException {
		AttrParmContext _localctx = new AttrParmContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_attrParm);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(609);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(607);
				match(ID);
				setState(608);
				match(T__36);
				}
			}

			setState(611);
			attrParmValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttrParmValueContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(LinguaFrancaParser.STRING, 0); }
		public TerminalNode SignedInt() { return getToken(LinguaFrancaParser.SignedInt, 0); }
		public TerminalNode Boolean() { return getToken(LinguaFrancaParser.Boolean, 0); }
		public TerminalNode SignedFloat() { return getToken(LinguaFrancaParser.SignedFloat, 0); }
		public AttrParmValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrParmValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterAttrParmValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitAttrParmValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitAttrParmValue(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AttrParmValueContext attrParmValue() throws RecognitionException {
		AttrParmValueContext _localctx = new AttrParmValueContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_attrParmValue);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(613);
			_la = _input.LA(1);
			if ( !(((((_la - 56)) & ~0x3f) == 0 && ((1L << (_la - 56)) & ((1L << (Boolean - 56)) | (1L << (SignedInt - 56)) | (1L << (STRING - 56)) | (1L << (SignedFloat - 56)))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KeyValuePairsContext extends ParserRuleContext {
		public List<KeyValuePairContext> keyValuePair() {
			return getRuleContexts(KeyValuePairContext.class);
		}
		public KeyValuePairContext keyValuePair(int i) {
			return getRuleContext(KeyValuePairContext.class,i);
		}
		public KeyValuePairsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyValuePairs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterKeyValuePairs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitKeyValuePairs(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitKeyValuePairs(this);
			else return visitor.visitChildren(this);
		}
	}

	public final KeyValuePairsContext keyValuePairs() throws RecognitionException {
		KeyValuePairsContext _localctx = new KeyValuePairsContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_keyValuePairs);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			keyValuePairs
			setState(616);
			match(T__15);
			setState(628);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==Kebab) {
				{
				setState(617);
				keyValuePair();
				setState(622);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,98,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(618);
						match(T__1);
						{
						setState(619);
						keyValuePair();
						}
						}
						} 
					}
					setState(624);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,98,_ctx);
				}
				setState(626);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(625);
					match(T__1);
					}
				}

				}
			}

			setState(630);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KeyValuePairContext extends ParserRuleContext {
		public TerminalNode Kebab() { return getToken(LinguaFrancaParser.Kebab, 0); }
		public ElementContext element() {
			return getRuleContext(ElementContext.class,0);
		}
		public KeyValuePairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keyValuePair; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterKeyValuePair(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitKeyValuePair(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitKeyValuePair(this);
			else return visitor.visitChildren(this);
		}
	}

	public final KeyValuePairContext keyValuePair() throws RecognitionException {
		KeyValuePairContext _localctx = new KeyValuePairContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_keyValuePair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(632);
			match(Kebab);
			setState(633);
			match(T__20);
			setState(634);
			element();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayContext extends ParserRuleContext {
		public List<ElementContext> element() {
			return getRuleContexts(ElementContext.class);
		}
		public ElementContext element(int i) {
			return getRuleContext(ElementContext.class,i);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitArray(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitArray(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_array);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(636);
			match(T__43);
			setState(637);
			element();
			setState(642);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,101,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(638);
					match(T__1);
					{
					setState(639);
					element();
					}
					}
					} 
				}
				setState(644);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,101,_ctx);
			}
			setState(646);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(645);
				match(T__1);
				}
			}

			setState(648);
			match(T__44);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ElementContext extends ParserRuleContext {
		public KeyValuePairsContext keyValuePairs() {
			return getRuleContext(KeyValuePairsContext.class,0);
		}
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public TerminalNode Literal() { return getToken(LinguaFrancaParser.Literal, 0); }
		public TerminalNode INT() { return getToken(LinguaFrancaParser.INT, 0); }
		public TerminalNode TimeUnit() { return getToken(LinguaFrancaParser.TimeUnit, 0); }
		public TerminalNode Path() { return getToken(LinguaFrancaParser.Path, 0); }
		public ElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitElement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitElement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ElementContext element() throws RecognitionException {
		ElementContext _localctx = new ElementContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_element);
		try {
			setState(656);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(650);
				keyValuePairs();
				}
				break;
			case T__43:
				enterOuterAlt(_localctx, 2);
				{
				setState(651);
				array();
				}
				break;
			case Literal:
				enterOuterAlt(_localctx, 3);
				{
				setState(652);
				match(Literal);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 4);
				{
				{
				setState(653);
				match(INT);
				setState(654);
				match(TimeUnit);
				}
				}
				break;
			case Path:
				enterOuterAlt(_localctx, 5);
				{
				setState(655);
				match(Path);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypedVariableContext extends ParserRuleContext {
		public PortDeclContext portDecl() {
			return getRuleContext(PortDeclContext.class,0);
		}
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TypedVariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typedVariable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterTypedVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitTypedVariable(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitTypedVariable(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypedVariableContext typedVariable() throws RecognitionException {
		TypedVariableContext _localctx = new TypedVariableContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_typedVariable);
		try {
			setState(660);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,104,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(658);
				portDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(659);
				action();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TypedVariableContext typedVariable() {
			return getRuleContext(TypedVariableContext.class,0);
		}
		public TimerContext timer() {
			return getRuleContext(TimerContext.class,0);
		}
		public ModeDeclContext modeDecl() {
			return getRuleContext(ModeDeclContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitVariable(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitVariable(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_variable);
		try {
			setState(665);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,105,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(662);
				typedVariable();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(663);
				timer();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(664);
				modeDecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarRefContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public InstantiationContext instantiation() {
			return getRuleContext(InstantiationContext.class,0);
		}
		public VarRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varRef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterVarRef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitVarRef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitVarRef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarRefContext varRef() throws RecognitionException {
		VarRefContext _localctx = new VarRefContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_varRef);
		try {
			setState(683);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__42:
			case T__48:
			case T__49:
				enterOuterAlt(_localctx, 1);
				{
				setState(667);
				variable();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(668);
				instantiation();
				setState(669);
				match(T__45);
				setState(670);
				variable();
				}
				break;
			case T__46:
				enterOuterAlt(_localctx, 3);
				{
				setState(672);
				match(T__46);
				setState(673);
				match(T__11);
				setState(679);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__23:
				case T__24:
				case T__25:
				case T__26:
				case T__27:
				case T__28:
				case T__29:
				case T__42:
				case T__48:
				case T__49:
					{
					setState(674);
					variable();
					}
					break;
				case ID:
					{
					setState(675);
					instantiation();
					setState(676);
					match(T__45);
					setState(677);
					variable();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(681);
				match(T__12);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarRefOrModeTransitionContext extends ParserRuleContext {
		public VarRefContext varRef() {
			return getRuleContext(VarRefContext.class,0);
		}
		public ModeTransitionContext modeTransition() {
			return getRuleContext(ModeTransitionContext.class,0);
		}
		public ModeDeclContext modeDecl() {
			return getRuleContext(ModeDeclContext.class,0);
		}
		public VarRefOrModeTransitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varRefOrModeTransition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterVarRefOrModeTransition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitVarRefOrModeTransition(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitVarRefOrModeTransition(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarRefOrModeTransitionContext varRefOrModeTransition() throws RecognitionException {
		VarRefOrModeTransitionContext _localctx = new VarRefOrModeTransitionContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_varRefOrModeTransition);
		try {
			setState(691);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__42:
			case T__46:
			case T__48:
			case T__49:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(685);
				varRef();
				}
				break;
			case T__18:
			case T__54:
				enterOuterAlt(_localctx, 2);
				{
				setState(686);
				modeTransition();
				setState(687);
				match(T__11);
				setState(688);
				modeDecl();
				setState(689);
				match(T__12);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitAssignment(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(693);
			parameter();
			setState(725);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,115,_ctx) ) {
			case 1:
				{
				{
				setState(694);
				match(T__36);
				setState(695);
				expression();
				}
				}
				break;
			case 2:
				{
				{
				setState(697);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__36) {
					{
					setState(696);
					match(T__36);
					}
				}

				setState(723);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__11:
					{
					setState(699);
					match(T__11);
					setState(708);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (Time - 43)) | (1L << (Literal - 43)) | (1L << (ID - 43)) | (1L << (Code - 43)))) != 0)) {
						{
						setState(700);
						expression();
						setState(705);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==T__1) {
							{
							{
							setState(701);
							match(T__1);
							setState(702);
							expression();
							}
							}
							setState(707);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
					}

					setState(710);
					match(T__12);
					}
					break;
				case T__15:
					{
					setState(711);
					match(T__15);
					setState(720);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (Time - 43)) | (1L << (Literal - 43)) | (1L << (ID - 43)) | (1L << (Code - 43)))) != 0)) {
						{
						setState(712);
						expression();
						setState(717);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==T__1) {
							{
							{
							setState(713);
							match(T__1);
							setState(714);
							expression();
							}
							}
							setState(719);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
					}

					setState(722);
					match(T__16);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				break;
			}
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LinguaFrancaParser.ID, 0); }
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public TerminalNode Type() { return getToken(LinguaFrancaParser.Type, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitParameter(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitParameter(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_parameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(730);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__42) {
				{
				{
				setState(727);
				attribute();
				}
				}
				setState(732);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(733);
			match(ID);
			setState(736);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(734);
				match(T__20);
				{
				setState(735);
				match(Type);
				}
				}
			}

			setState(762);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,122,_ctx) ) {
			case 1:
				{
				{
				setState(738);
				match(T__11);
				setState(747);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (Time - 43)) | (1L << (Literal - 43)) | (1L << (ID - 43)) | (1L << (Code - 43)))) != 0)) {
					{
					setState(739);
					expression();
					setState(744);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__1) {
						{
						{
						setState(740);
						match(T__1);
						setState(741);
						expression();
						}
						}
						setState(746);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(749);
				match(T__12);
				}
				}
				break;
			case 2:
				{
				{
				setState(750);
				match(T__15);
				setState(759);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 43)) & ~0x3f) == 0 && ((1L << (_la - 43)) & ((1L << (T__42 - 43)) | (1L << (Time - 43)) | (1L << (Literal - 43)) | (1L << (ID - 43)) | (1L << (Code - 43)))) != 0)) {
					{
					setState(751);
					expression();
					setState(756);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__1) {
						{
						{
						setState(752);
						match(T__1);
						setState(753);
						expression();
						}
						}
						setState(758);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(761);
				match(T__16);
				}
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode Literal() { return getToken(LinguaFrancaParser.Literal, 0); }
		public TerminalNode Time() { return getToken(LinguaFrancaParser.Time, 0); }
		public ParameterReferenceContext parameterReference() {
			return getRuleContext(ParameterReferenceContext.class,0);
		}
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_expression);
		try {
			setState(769);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Literal:
				enterOuterAlt(_localctx, 1);
				{
				Literal
				setState(765);
				match(Literal);
				}
				break;
			case Time:
				enterOuterAlt(_localctx, 2);
				{
				setState(766);
				match(Time);
				}
				break;
			case T__42:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(767);
				parameterReference();
				}
				break;
			case Code:
				enterOuterAlt(_localctx, 4);
				{
				setState(768);
				match(Code);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterReferenceContext extends ParserRuleContext {
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public ParameterReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterParameterReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitParameterReference(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitParameterReference(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParameterReferenceContext parameterReference() throws RecognitionException {
		ParameterReferenceContext _localctx = new ParameterReferenceContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_parameterReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(771);
			parameter();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PortDeclContext extends ParserRuleContext {
		public InputDeclContext inputDecl() {
			return getRuleContext(InputDeclContext.class,0);
		}
		public OutputDeclContext outputDecl() {
			return getRuleContext(OutputDeclContext.class,0);
		}
		public PortDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_portDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterPortDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitPortDecl(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitPortDecl(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PortDeclContext portDecl() throws RecognitionException {
		PortDeclContext _localctx = new PortDeclContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_portDecl);
		try {
			setState(775);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,124,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(773);
				inputDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(774);
				outputDecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WidthSpecContext extends ParserRuleContext {
		public TerminalNode OPEN_CLOSE_SQ_BR() { return getToken(LinguaFrancaParser.OPEN_CLOSE_SQ_BR, 0); }
		public List<WidthTermContext> widthTerm() {
			return getRuleContexts(WidthTermContext.class);
		}
		public WidthTermContext widthTerm(int i) {
			return getRuleContext(WidthTermContext.class,i);
		}
		public WidthSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_widthSpec; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterWidthSpec(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitWidthSpec(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitWidthSpec(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WidthSpecContext widthSpec() throws RecognitionException {
		WidthSpecContext _localctx = new WidthSpecContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_widthSpec);
		int _la;
		try {
			setState(789);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_CLOSE_SQ_BR:
				enterOuterAlt(_localctx, 1);
				{
				setState(777);
				match(OPEN_CLOSE_SQ_BR);
				}
				break;
			case T__43:
				enterOuterAlt(_localctx, 2);
				{
				setState(778);
				match(T__43);
				{
				setState(779);
				widthTerm();
				}
				setState(784);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__38) {
					{
					{
					setState(780);
					match(T__38);
					setState(781);
					widthTerm();
					}
					}
					setState(786);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(787);
				match(T__44);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WidthTermContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(LinguaFrancaParser.INT, 0); }
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public VarRefContext varRef() {
			return getRuleContext(VarRefContext.class,0);
		}
		public TerminalNode Code() { return getToken(LinguaFrancaParser.Code, 0); }
		public WidthTermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_widthTerm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterWidthTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitWidthTerm(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitWidthTerm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WidthTermContext widthTerm() throws RecognitionException {
		WidthTermContext _localctx = new WidthTermContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_widthTerm);
		try {
			setState(798);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(791);
				match(INT);
				}
				break;
			case T__42:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(792);
				parameter();
				}
				break;
			case T__47:
				enterOuterAlt(_localctx, 3);
				{
				setState(793);
				match(T__47);
				setState(794);
				varRef();
				setState(795);
				match(T__12);
				}
				break;
			case Code:
				enterOuterAlt(_localctx, 4);
				{
				setState(797);
				match(Code);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class HostContext extends ParserRuleContext {
		public TerminalNode IPV4Host() { return getToken(LinguaFrancaParser.IPV4Host, 0); }
		public TerminalNode IPV6Host() { return getToken(LinguaFrancaParser.IPV6Host, 0); }
		public TerminalNode NamedHost() { return getToken(LinguaFrancaParser.NamedHost, 0); }
		public HostContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_host; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterHost(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitHost(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitHost(this);
			else return visitor.visitChildren(this);
		}
	}

	public final HostContext host() throws RecognitionException {
		HostContext _localctx = new HostContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_host);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(800);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << IPV4Host) | (1L << IPV6Host) | (1L << NamedHost))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ActionOriginContext extends ParserRuleContext {
		public ActionOriginContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actionOrigin; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterActionOrigin(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitActionOrigin(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitActionOrigin(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ActionOriginContext actionOrigin() throws RecognitionException {
		ActionOriginContext _localctx = new ActionOriginContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_actionOrigin);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(802);
			_la = _input.LA(1);
			if ( !(_la==T__48 || _la==T__49) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VisibilityContext extends ParserRuleContext {
		public VisibilityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_visibility; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterVisibility(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitVisibility(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitVisibility(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VisibilityContext visibility() throws RecognitionException {
		VisibilityContext _localctx = new VisibilityContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_visibility);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(804);
			_la = _input.LA(1);
			if ( !(_la==T__50 || _la==T__51) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BuiltinTriggerContext extends ParserRuleContext {
		public BuiltinTriggerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_builtinTrigger; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterBuiltinTrigger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitBuiltinTrigger(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitBuiltinTrigger(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BuiltinTriggerContext builtinTrigger() throws RecognitionException {
		BuiltinTriggerContext _localctx = new BuiltinTriggerContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_builtinTrigger);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(806);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__18) | (1L << T__52) | (1L << T__53))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ModeTransitionContext extends ParserRuleContext {
		public ModeTransitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modeTransition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).enterModeTransition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof LinguaFrancaListener ) ((LinguaFrancaListener)listener).exitModeTransition(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof LinguaFrancaVisitor ) return ((LinguaFrancaVisitor<? extends T>)visitor).visitModeTransition(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ModeTransitionContext modeTransition() throws RecognitionException {
		ModeTransitionContext _localctx = new ModeTransitionContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_modeTransition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(808);
			_la = _input.LA(1);
			if ( !(_la==T__18 || _la==T__54) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\\\u032b\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0002.\u0007.\u0002/\u0007/\u0001\u0000\u0001\u0000\u0005\u0000"+
		"c\b\u0000\n\u0000\f\u0000f\t\u0000\u0001\u0000\u0005\u0000i\b\u0000\n"+
		"\u0000\f\u0000l\t\u0000\u0001\u0000\u0004\u0000o\b\u0000\u000b\u0000\f"+
		"\u0000p\u0001\u0001\u0001\u0001\u0004\u0001u\b\u0001\u000b\u0001\f\u0001"+
		"v\u0001\u0001\u0001\u0001\u0004\u0001{\b\u0001\u000b\u0001\f\u0001|\u0005"+
		"\u0001\u007f\b\u0001\n\u0001\f\u0001\u0082\t\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u0087\b\u0001\u0001\u0002\u0001\u0002\u0003\u0002"+
		"\u008b\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003\u0090\b"+
		"\u0003\u0001\u0004\u0005\u0004\u0093\b\u0004\n\u0004\f\u0004\u0096\t\u0004"+
		"\u0001\u0004\u0003\u0004\u0099\b\u0004\u0001\u0004\u0003\u0004\u009c\b"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00a0\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00a6\b\u0004\n\u0004\f\u0004"+
		"\u00a9\t\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00ad\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00b3\b\u0004\n"+
		"\u0004\f\u0004\u00b6\t\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00ba"+
		"\b\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u00be\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00c4\b\u0004\n\u0004"+
		"\f\u0004\u00c7\t\u0004\u0003\u0004\u00c9\b\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004\u00d7\b\u0004"+
		"\n\u0004\f\u0004\u00da\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0003\u0005\u00e0\b\u0005\u0001\u0006\u0004\u0006\u00e3\b\u0006"+
		"\u000b\u0006\f\u0006\u00e4\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"\u00ea\b\u0007\u0001\u0007\u0003\u0007\u00ed\b\u0007\u0001\b\u0005\b\u00f0"+
		"\b\b\n\b\f\b\u00f3\t\b\u0001\b\u0003\b\u00f6\b\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\b\u00fc\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\b\u0102"+
		"\b\b\n\b\f\b\u0105\t\b\u0003\b\u0107\b\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0005\b\u010e\b\b\n\b\f\b\u0111\t\b\u0003\b\u0113\b\b\u0001"+
		"\b\u0003\b\u0116\b\b\u0001\b\u0003\b\u0119\b\b\u0001\t\u0003\t\u011c\b"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0005\t\u0124\b\t\n"+
		"\t\f\t\u0127\t\t\u0003\t\u0129\b\t\u0001\t\u0001\t\u0001\t\u0003\t\u012e"+
		"\b\t\u0001\t\u0001\t\u0003\t\u0132\b\t\u0001\n\u0001\n\u0001\n\u0003\n"+
		"\u0137\b\n\u0001\u000b\u0005\u000b\u013a\b\u000b\n\u000b\f\u000b\u013d"+
		"\t\u000b\u0001\u000b\u0003\u000b\u0140\b\u000b\u0001\u000b\u0001\u000b"+
		"\u0003\u000b\u0144\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"\u0149\b\u000b\u0001\u000b\u0003\u000b\u014c\b\u000b\u0001\f\u0005\f\u014f"+
		"\b\f\n\f\f\f\u0152\t\f\u0001\f\u0001\f\u0003\f\u0156\b\f\u0001\f\u0001"+
		"\f\u0001\f\u0003\f\u015b\b\f\u0001\f\u0003\f\u015e\b\f\u0001\r\u0005\r"+
		"\u0161\b\r\n\r\f\r\u0164\t\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\r\u016c\b\r\u0001\r\u0001\r\u0003\r\u0170\b\r\u0001\r\u0003\r"+
		"\u0173\b\r\u0001\u000e\u0001\u000e\u0003\u000e\u0177\b\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u017b\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u0184\b\u000e"+
		"\n\u000e\f\u000e\u0187\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0005"+
		"\u000f\u018c\b\u000f\n\u000f\f\u000f\u018f\t\u000f\u0001\u000f\u0003\u000f"+
		"\u0192\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u019c\b\u000f\u0003\u000f"+
		"\u019e\b\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u01a2\b\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u01a6\b\u000f\u0001\u000f\u0003\u000f\u01a9"+
		"\b\u000f\u0001\u0010\u0005\u0010\u01ac\b\u0010\n\u0010\f\u0010\u01af\t"+
		"\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u01b3\b\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u01b9\b\u0010\n\u0010\f\u0010"+
		"\u01bc\t\u0010\u0003\u0010\u01be\b\u0010\u0001\u0010\u0003\u0010\u01c1"+
		"\b\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u01c6\b\u0010"+
		"\n\u0010\f\u0010\u01c9\t\u0010\u0003\u0010\u01cb\b\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u01d1\b\u0010\n\u0010\f\u0010"+
		"\u01d4\t\u0010\u0003\u0010\u01d6\b\u0010\u0001\u0010\u0001\u0010\u0003"+
		"\u0010\u01da\b\u0010\u0001\u0010\u0003\u0010\u01dd\b\u0010\u0001\u0011"+
		"\u0001\u0011\u0003\u0011\u01e1\b\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0003\u0015\u01f2\b\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u01fb\b\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u0202\b\u0016"+
		"\n\u0016\f\u0016\u0205\t\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u0209"+
		"\b\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u020f"+
		"\b\u0016\n\u0016\f\u0016\u0212\t\u0016\u0003\u0016\u0214\b\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003"+
		"\u0016\u021c\b\u0016\u0003\u0016\u021e\b\u0016\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0005\u0017\u0223\b\u0017\n\u0017\f\u0017\u0226\t\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u022c\b\u0017\n"+
		"\u0017\f\u0017\u022f\t\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u0233"+
		"\b\u0017\u0003\u0017\u0235\b\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0017\u0005\u0017\u023b\b\u0017\n\u0017\f\u0017\u023e\t\u0017\u0001"+
		"\u0017\u0001\u0017\u0003\u0017\u0242\b\u0017\u0001\u0017\u0003\u0017\u0245"+
		"\b\u0017\u0001\u0017\u0003\u0017\u0248\b\u0017\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0005\u0019\u0253\b\u0019\n\u0019\f\u0019\u0256\t\u0019\u0001"+
		"\u0019\u0003\u0019\u0259\b\u0019\u0003\u0019\u025b\b\u0019\u0001\u0019"+
		"\u0003\u0019\u025e\b\u0019\u0001\u001a\u0001\u001a\u0003\u001a\u0262\b"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0005\u001c\u026d\b\u001c\n"+
		"\u001c\f\u001c\u0270\t\u001c\u0001\u001c\u0003\u001c\u0273\b\u001c\u0003"+
		"\u001c\u0275\b\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0005"+
		"\u001e\u0281\b\u001e\n\u001e\f\u001e\u0284\t\u001e\u0001\u001e\u0003\u001e"+
		"\u0287\b\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0001\u001f"+
		"\u0001\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0291\b\u001f\u0001 "+
		"\u0001 \u0003 \u0295\b \u0001!\u0001!\u0001!\u0003!\u029a\b!\u0001\"\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0001\"\u0003\"\u02a8\b\"\u0001\"\u0001\"\u0003\"\u02ac\b\"\u0001#"+
		"\u0001#\u0001#\u0001#\u0001#\u0001#\u0003#\u02b4\b#\u0001$\u0001$\u0001"+
		"$\u0001$\u0003$\u02ba\b$\u0001$\u0001$\u0001$\u0001$\u0005$\u02c0\b$\n"+
		"$\f$\u02c3\t$\u0003$\u02c5\b$\u0001$\u0001$\u0001$\u0001$\u0001$\u0005"+
		"$\u02cc\b$\n$\f$\u02cf\t$\u0003$\u02d1\b$\u0001$\u0003$\u02d4\b$\u0003"+
		"$\u02d6\b$\u0001%\u0005%\u02d9\b%\n%\f%\u02dc\t%\u0001%\u0001%\u0001%"+
		"\u0003%\u02e1\b%\u0001%\u0001%\u0001%\u0001%\u0005%\u02e7\b%\n%\f%\u02ea"+
		"\t%\u0003%\u02ec\b%\u0001%\u0001%\u0001%\u0001%\u0001%\u0005%\u02f3\b"+
		"%\n%\f%\u02f6\t%\u0003%\u02f8\b%\u0001%\u0003%\u02fb\b%\u0001&\u0001&"+
		"\u0001&\u0001&\u0001&\u0003&\u0302\b&\u0001\'\u0001\'\u0001(\u0001(\u0003"+
		"(\u0308\b(\u0001)\u0001)\u0001)\u0001)\u0001)\u0005)\u030f\b)\n)\f)\u0312"+
		"\t)\u0001)\u0001)\u0003)\u0316\b)\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0001*\u0003*\u031f\b*\u0001+\u0001+\u0001,\u0001,\u0001-\u0001-\u0001"+
		".\u0001.\u0001/\u0001/\u0001/\u0000\u00000\u0000\u0002\u0004\u0006\b\n"+
		"\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.0246"+
		"8:<>@BDFHJLNPRTVXZ\\^\u0000\b\u0001\u0000\u0006\u0007\u0002\u0000!!(("+
		"\u0004\u000088AAMMTT\u0001\u0000<>\u0001\u000012\u0001\u000034\u0002\u0000"+
		"\u0013\u001356\u0002\u0000\u0013\u001377\u0392\u0000`\u0001\u0000\u0000"+
		"\u0000\u0002r\u0001\u0000\u0000\u0000\u0004\u008a\u0001\u0000\u0000\u0000"+
		"\u0006\u008c\u0001\u0000\u0000\u0000\b\u0094\u0001\u0000\u0000\u0000\n"+
		"\u00df\u0001\u0000\u0000\u0000\f\u00e2\u0001\u0000\u0000\u0000\u000e\u00e6"+
		"\u0001\u0000\u0000\u0000\u0010\u00f1\u0001\u0000\u0000\u0000\u0012\u011b"+
		"\u0001\u0000\u0000\u0000\u0014\u0133\u0001\u0000\u0000\u0000\u0016\u013b"+
		"\u0001\u0000\u0000\u0000\u0018\u0150\u0001\u0000\u0000\u0000\u001a\u0162"+
		"\u0001\u0000\u0000\u0000\u001c\u0174\u0001\u0000\u0000\u0000\u001e\u018d"+
		"\u0001\u0000\u0000\u0000 \u01ad\u0001\u0000\u0000\u0000\"\u01e0\u0001"+
		"\u0000\u0000\u0000$\u01e2\u0001\u0000\u0000\u0000&\u01e4\u0001\u0000\u0000"+
		"\u0000(\u01ea\u0001\u0000\u0000\u0000*\u01f1\u0001\u0000\u0000\u0000,"+
		"\u01f6\u0001\u0000\u0000\u0000.\u0234\u0001\u0000\u0000\u00000\u0249\u0001"+
		"\u0000\u0000\u00002\u024c\u0001\u0000\u0000\u00004\u0261\u0001\u0000\u0000"+
		"\u00006\u0265\u0001\u0000\u0000\u00008\u0267\u0001\u0000\u0000\u0000:"+
		"\u0278\u0001\u0000\u0000\u0000<\u027c\u0001\u0000\u0000\u0000>\u0290\u0001"+
		"\u0000\u0000\u0000@\u0294\u0001\u0000\u0000\u0000B\u0299\u0001\u0000\u0000"+
		"\u0000D\u02ab\u0001\u0000\u0000\u0000F\u02b3\u0001\u0000\u0000\u0000H"+
		"\u02b5\u0001\u0000\u0000\u0000J\u02da\u0001\u0000\u0000\u0000L\u0301\u0001"+
		"\u0000\u0000\u0000N\u0303\u0001\u0000\u0000\u0000P\u0307\u0001\u0000\u0000"+
		"\u0000R\u0315\u0001\u0000\u0000\u0000T\u031e\u0001\u0000\u0000\u0000V"+
		"\u0320\u0001\u0000\u0000\u0000X\u0322\u0001\u0000\u0000\u0000Z\u0324\u0001"+
		"\u0000\u0000\u0000\\\u0326\u0001\u0000\u0000\u0000^\u0328\u0001\u0000"+
		"\u0000\u0000`d\u0003\u000e\u0007\u0000ac\u0003\u0002\u0001\u0000ba\u0001"+
		"\u0000\u0000\u0000cf\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000"+
		"de\u0001\u0000\u0000\u0000ej\u0001\u0000\u0000\u0000fd\u0001\u0000\u0000"+
		"\u0000gi\u0003*\u0015\u0000hg\u0001\u0000\u0000\u0000il\u0001\u0000\u0000"+
		"\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000kn\u0001\u0000"+
		"\u0000\u0000lj\u0001\u0000\u0000\u0000mo\u0003\b\u0004\u0000nm\u0001\u0000"+
		"\u0000\u0000op\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000pq\u0001"+
		"\u0000\u0000\u0000q\u0001\u0001\u0000\u0000\u0000rt\u0005\u0001\u0000"+
		"\u0000su\u0003\u0006\u0003\u0000ts\u0001\u0000\u0000\u0000uv\u0001\u0000"+
		"\u0000\u0000vt\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000w\u0080"+
		"\u0001\u0000\u0000\u0000xz\u0005\u0002\u0000\u0000y{\u0003\u0006\u0003"+
		"\u0000zy\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|z\u0001\u0000"+
		"\u0000\u0000|}\u0001\u0000\u0000\u0000}\u007f\u0001\u0000\u0000\u0000"+
		"~x\u0001\u0000\u0000\u0000\u007f\u0082\u0001\u0000\u0000\u0000\u0080~"+
		"\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0083"+
		"\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0083\u0084"+
		"\u0005\u0003\u0000\u0000\u0084\u0086\u0005M\u0000\u0000\u0085\u0087\u0005"+
		"\u0004\u0000\u0000\u0086\u0085\u0001\u0000\u0000\u0000\u0086\u0087\u0001"+
		"\u0000\u0000\u0000\u0087\u0003\u0001\u0000\u0000\u0000\u0088\u008b\u0003"+
		"\b\u0004\u0000\u0089\u008b\u0003\u0006\u0003\u0000\u008a\u0088\u0001\u0000"+
		"\u0000\u0000\u008a\u0089\u0001\u0000\u0000\u0000\u008b\u0005\u0001\u0000"+
		"\u0000\u0000\u008c\u008f\u0003\b\u0004\u0000\u008d\u008e\u0005\u0005\u0000"+
		"\u0000\u008e\u0090\u0005F\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000"+
		"\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0007\u0001\u0000\u0000\u0000"+
		"\u0091\u0093\u00032\u0019\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0093"+
		"\u0096\u0001\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0001\u0000\u0000\u0000\u0095\u0098\u0001\u0000\u0000\u0000\u0096"+
		"\u0094\u0001\u0000\u0000\u0000\u0097\u0099\u0007\u0000\u0000\u0000\u0098"+
		"\u0097\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099"+
		"\u009b\u0001\u0000\u0000\u0000\u009a\u009c\u0005\b\u0000\u0000\u009b\u009a"+
		"\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000\u0000\u009c\u009d"+
		"\u0001\u0000\u0000\u0000\u009d\u009f\u0005\t\u0000\u0000\u009e\u00a0\u0005"+
		"F\u0000\u0000\u009f\u009e\u0001\u0000\u0000\u0000\u009f\u00a0\u0001\u0000"+
		"\u0000\u0000\u00a0\u00ac\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005\n\u0000"+
		"\u0000\u00a2\u00a7\u0003\n\u0005\u0000\u00a3\u00a4\u0005\u0002\u0000\u0000"+
		"\u00a4\u00a6\u0003\n\u0005\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a9\u0001\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a8\u0001\u0000\u0000\u0000\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9"+
		"\u00a7\u0001\u0000\u0000\u0000\u00aa\u00ab\u0005\u000b\u0000\u0000\u00ab"+
		"\u00ad\u0001\u0000\u0000\u0000\u00ac\u00a1\u0001\u0000\u0000\u0000\u00ac"+
		"\u00ad\u0001\u0000\u0000\u0000\u00ad\u00b9\u0001\u0000\u0000\u0000\u00ae"+
		"\u00af\u0005\f\u0000\u0000\u00af\u00b4\u0003J%\u0000\u00b0\u00b1\u0005"+
		"\u0002\u0000\u0000\u00b1\u00b3\u0003J%\u0000\u00b2\u00b0\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b6\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b4\u00b5\u0001\u0000\u0000\u0000\u00b5\u00b7\u0001\u0000\u0000"+
		"\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005\r\u0000\u0000"+
		"\u00b8\u00ba\u0001\u0000\u0000\u0000\u00b9\u00ae\u0001\u0000\u0000\u0000"+
		"\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba\u00bd\u0001\u0000\u0000\u0000"+
		"\u00bb\u00bc\u0005\u000e\u0000\u0000\u00bc\u00be\u0003V+\u0000\u00bd\u00bb"+
		"\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000\u0000\u0000\u00be\u00c8"+
		"\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\u000f\u0000\u0000\u00c0\u00c5"+
		"\u0003\u0004\u0002\u0000\u00c1\u00c2\u0005\u0002\u0000\u0000\u00c2\u00c4"+
		"\u0003\u0004\u0002\u0000\u00c3\u00c1\u0001\u0000\u0000\u0000\u00c4\u00c7"+
		"\u0001\u0000\u0000\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000\u00c5\u00c6"+
		"\u0001\u0000\u0000\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7\u00c5"+
		"\u0001\u0000\u0000\u0000\u00c8\u00bf\u0001\u0000\u0000\u0000\u00c8\u00c9"+
		"\u0001\u0000\u0000\u0000\u00c9\u00ca\u0001\u0000\u0000\u0000\u00ca\u00d8"+
		"\u0005\u0010\u0000\u0000\u00cb\u00d7\u0003*\u0015\u0000\u00cc\u00d7\u0003"+
		"\u0010\b\u0000\u00cd\u00d7\u0003\u0012\t\u0000\u00ce\u00d7\u0003\u0016"+
		"\u000b\u0000\u00cf\u00d7\u0003\u0018\f\u0000\u00d0\u00d7\u0003\u001a\r"+
		"\u0000\u00d1\u00d7\u0003\u001e\u000f\u0000\u00d2\u00d7\u0003,\u0016\u0000"+
		"\u00d3\u00d7\u0003.\u0017\u0000\u00d4\u00d7\u0003 \u0010\u0000\u00d5\u00d7"+
		"\u0003\u001c\u000e\u0000\u00d6\u00cb\u0001\u0000\u0000\u0000\u00d6\u00cc"+
		"\u0001\u0000\u0000\u0000\u00d6\u00cd\u0001\u0000\u0000\u0000\u00d6\u00ce"+
		"\u0001\u0000\u0000\u0000\u00d6\u00cf\u0001\u0000\u0000\u0000\u00d6\u00d0"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d1\u0001\u0000\u0000\u0000\u00d6\u00d2"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d3\u0001\u0000\u0000\u0000\u00d6\u00d4"+
		"\u0001\u0000\u0000\u0000\u00d6\u00d5\u0001\u0000\u0000\u0000\u00d7\u00da"+
		"\u0001\u0000\u0000\u0000\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d8\u00d9"+
		"\u0001\u0000\u0000\u0000\u00d9\u00db\u0001\u0000\u0000\u0000\u00da\u00d8"+
		"\u0001\u0000\u0000\u0000\u00db\u00dc\u0005\u0011\u0000\u0000\u00dc\t\u0001"+
		"\u0000\u0000\u0000\u00dd\u00e0\u0003\f\u0006\u0000\u00de\u00e0\u0005U"+
		"\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00df\u00de\u0001\u0000"+
		"\u0000\u0000\u00e0\u000b\u0001\u0000\u0000\u0000\u00e1\u00e3\u0005F\u0000"+
		"\u0000\u00e2\u00e1\u0001\u0000\u0000\u0000\u00e3\u00e4\u0001\u0000\u0000"+
		"\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e5\r\u0001\u0000\u0000\u0000\u00e6\u00e7\u0005\u0012\u0000\u0000"+
		"\u00e7\u00e9\u0005F\u0000\u0000\u00e8\u00ea\u00038\u001c\u0000\u00e9\u00e8"+
		"\u0001\u0000\u0000\u0000\u00e9\u00ea\u0001\u0000\u0000\u0000\u00ea\u00ec"+
		"\u0001\u0000\u0000\u0000\u00eb\u00ed\u0005\u0004\u0000\u0000\u00ec\u00eb"+
		"\u0001\u0000\u0000\u0000\u00ec\u00ed\u0001\u0000\u0000\u0000\u00ed\u000f"+
		"\u0001\u0000\u0000\u0000\u00ee\u00f0\u00032\u0019\u0000\u00ef\u00ee\u0001"+
		"\u0000\u0000\u0000\u00f0\u00f3\u0001\u0000\u0000\u0000\u00f1\u00ef\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0001\u0000\u0000\u0000\u00f2\u00f5\u0001"+
		"\u0000\u0000\u0000\u00f3\u00f1\u0001\u0000\u0000\u0000\u00f4\u00f6\u0005"+
		"\u0013\u0000\u0000\u00f5\u00f4\u0001\u0000\u0000\u0000\u00f5\u00f6\u0001"+
		"\u0000\u0000\u0000\u00f6\u00f7\u0001\u0000\u0000\u0000\u00f7\u00f8\u0005"+
		"\u0014\u0000\u0000\u00f8\u00fb\u0005F\u0000\u0000\u00f9\u00fa\u0005\u0015"+
		"\u0000\u0000\u00fa\u00fc\u0005:\u0000\u0000\u00fb\u00f9\u0001\u0000\u0000"+
		"\u0000\u00fb\u00fc\u0001\u0000\u0000\u0000\u00fc\u0115\u0001\u0000\u0000"+
		"\u0000\u00fd\u0106\u0005\f\u0000\u0000\u00fe\u0103\u0003L&\u0000\u00ff"+
		"\u0100\u0005\u0002\u0000\u0000\u0100\u0102\u0003L&\u0000\u0101\u00ff\u0001"+
		"\u0000\u0000\u0000\u0102\u0105\u0001\u0000\u0000\u0000\u0103\u0101\u0001"+
		"\u0000\u0000\u0000\u0103\u0104\u0001\u0000\u0000\u0000\u0104\u0107\u0001"+
		"\u0000\u0000\u0000\u0105\u0103\u0001\u0000\u0000\u0000\u0106\u00fe\u0001"+
		"\u0000\u0000\u0000\u0106\u0107\u0001\u0000\u0000\u0000\u0107\u0108\u0001"+
		"\u0000\u0000\u0000\u0108\u0116\u0005\r\u0000\u0000\u0109\u0112\u0005\u0010"+
		"\u0000\u0000\u010a\u010f\u0003L&\u0000\u010b\u010c\u0005\u0002\u0000\u0000"+
		"\u010c\u010e\u0003L&\u0000\u010d\u010b\u0001\u0000\u0000\u0000\u010e\u0111"+
		"\u0001\u0000\u0000\u0000\u010f\u010d\u0001\u0000\u0000\u0000\u010f\u0110"+
		"\u0001\u0000\u0000\u0000\u0110\u0113\u0001\u0000\u0000\u0000\u0111\u010f"+
		"\u0001\u0000\u0000\u0000\u0112\u010a\u0001\u0000\u0000\u0000\u0112\u0113"+
		"\u0001\u0000\u0000\u0000\u0113\u0114\u0001\u0000\u0000\u0000\u0114\u0116"+
		"\u0005\u0011\u0000\u0000\u0115\u00fd\u0001\u0000\u0000\u0000\u0115\u0109"+
		"\u0001\u0000\u0000\u0000\u0115\u0116\u0001\u0000\u0000\u0000\u0116\u0118"+
		"\u0001\u0000\u0000\u0000\u0117\u0119\u0005\u0004\u0000\u0000\u0118\u0117"+
		"\u0001\u0000\u0000\u0000\u0118\u0119\u0001\u0000\u0000\u0000\u0119\u0011"+
		"\u0001\u0000\u0000\u0000\u011a\u011c\u0005\u0016\u0000\u0000\u011b\u011a"+
		"\u0001\u0000\u0000\u0000\u011b\u011c\u0001\u0000\u0000\u0000\u011c\u011d"+
		"\u0001\u0000\u0000\u0000\u011d\u011e\u0005\u0017\u0000\u0000\u011e\u011f"+
		"\u0005F\u0000\u0000\u011f\u0128\u0005\f\u0000\u0000\u0120\u0125\u0003"+
		"\u0014\n\u0000\u0121\u0122\u0005\u0002\u0000\u0000\u0122\u0124\u0003\u0014"+
		"\n\u0000\u0123\u0121\u0001\u0000\u0000\u0000\u0124\u0127\u0001\u0000\u0000"+
		"\u0000\u0125\u0123\u0001\u0000\u0000\u0000\u0125\u0126\u0001\u0000\u0000"+
		"\u0000\u0126\u0129\u0001\u0000\u0000\u0000\u0127\u0125\u0001\u0000\u0000"+
		"\u0000\u0128\u0120\u0001\u0000\u0000\u0000\u0128\u0129\u0001\u0000\u0000"+
		"\u0000\u0129\u012a\u0001\u0000\u0000\u0000\u012a\u012d\u0005\r\u0000\u0000"+
		"\u012b\u012c\u0005\u0015\u0000\u0000\u012c\u012e\u0005:\u0000\u0000\u012d"+
		"\u012b\u0001\u0000\u0000\u0000\u012d\u012e\u0001\u0000\u0000\u0000\u012e"+
		"\u012f\u0001\u0000\u0000\u0000\u012f\u0131\u0005U\u0000\u0000\u0130\u0132"+
		"\u0005\u0004\u0000\u0000\u0131\u0130\u0001\u0000\u0000\u0000\u0131\u0132"+
		"\u0001\u0000\u0000\u0000\u0132\u0013\u0001\u0000\u0000\u0000\u0133\u0136"+
		"\u0005F\u0000\u0000\u0134\u0135\u0005\u0015\u0000\u0000\u0135\u0137\u0005"+
		":\u0000\u0000\u0136\u0134\u0001\u0000\u0000\u0000\u0136\u0137\u0001\u0000"+
		"\u0000\u0000\u0137\u0015\u0001\u0000\u0000\u0000\u0138\u013a\u00032\u0019"+
		"\u0000\u0139\u0138\u0001\u0000\u0000\u0000\u013a\u013d\u0001\u0000\u0000"+
		"\u0000\u013b\u0139\u0001\u0000\u0000\u0000\u013b\u013c\u0001\u0000\u0000"+
		"\u0000\u013c\u013f\u0001\u0000\u0000\u0000\u013d\u013b\u0001\u0000\u0000"+
		"\u0000\u013e\u0140\u0005\u0018\u0000\u0000\u013f\u013e\u0001\u0000\u0000"+
		"\u0000\u013f\u0140\u0001\u0000\u0000\u0000\u0140\u0141\u0001\u0000\u0000"+
		"\u0000\u0141\u0143\u0005\u0019\u0000\u0000\u0142\u0144\u0003R)\u0000\u0143"+
		"\u0142\u0001\u0000\u0000\u0000\u0143\u0144\u0001\u0000\u0000\u0000\u0144"+
		"\u0145\u0001\u0000\u0000\u0000\u0145\u0148\u0005F\u0000\u0000\u0146\u0147"+
		"\u0005\u0015\u0000\u0000\u0147\u0149\u0005:\u0000\u0000\u0148\u0146\u0001"+
		"\u0000\u0000\u0000\u0148\u0149\u0001\u0000\u0000\u0000\u0149\u014b\u0001"+
		"\u0000\u0000\u0000\u014a\u014c\u0005\u0004\u0000\u0000\u014b\u014a\u0001"+
		"\u0000\u0000\u0000\u014b\u014c\u0001\u0000\u0000\u0000\u014c\u0017\u0001"+
		"\u0000\u0000\u0000\u014d\u014f\u00032\u0019\u0000\u014e\u014d\u0001\u0000"+
		"\u0000\u0000\u014f\u0152\u0001\u0000\u0000\u0000\u0150\u014e\u0001\u0000"+
		"\u0000\u0000\u0150\u0151\u0001\u0000\u0000\u0000\u0151\u0153\u0001\u0000"+
		"\u0000\u0000\u0152\u0150\u0001\u0000\u0000\u0000\u0153\u0155\u0005\u001a"+
		"\u0000\u0000\u0154\u0156\u0003R)\u0000\u0155\u0154\u0001\u0000\u0000\u0000"+
		"\u0155\u0156\u0001\u0000\u0000\u0000\u0156\u0157\u0001\u0000\u0000\u0000"+
		"\u0157\u015a\u0005F\u0000\u0000\u0158\u0159\u0005\u0015\u0000\u0000\u0159"+
		"\u015b\u0005:\u0000\u0000\u015a\u0158\u0001\u0000\u0000\u0000\u015a\u015b"+
		"\u0001\u0000\u0000\u0000\u015b\u015d\u0001\u0000\u0000\u0000\u015c\u015e"+
		"\u0005\u0004\u0000\u0000\u015d\u015c\u0001\u0000\u0000\u0000\u015d\u015e"+
		"\u0001\u0000\u0000\u0000\u015e\u0019\u0001\u0000\u0000\u0000\u015f\u0161"+
		"\u00032\u0019\u0000\u0160\u015f\u0001\u0000\u0000\u0000\u0161\u0164\u0001"+
		"\u0000\u0000\u0000\u0162\u0160\u0001\u0000\u0000\u0000\u0162\u0163\u0001"+
		"\u0000\u0000\u0000\u0163\u0165\u0001\u0000\u0000\u0000\u0164\u0162\u0001"+
		"\u0000\u0000\u0000\u0165\u0166\u0005\u001b\u0000\u0000\u0166\u016f\u0005"+
		"F\u0000\u0000\u0167\u0168\u0005\f\u0000\u0000\u0168\u016b\u0003L&\u0000"+
		"\u0169\u016a\u0005\u0002\u0000\u0000\u016a\u016c\u0003L&\u0000\u016b\u0169"+
		"\u0001\u0000\u0000\u0000\u016b\u016c\u0001\u0000\u0000\u0000\u016c\u016d"+
		"\u0001\u0000\u0000\u0000\u016d\u016e\u0005\r\u0000\u0000\u016e\u0170\u0001"+
		"\u0000\u0000\u0000\u016f\u0167\u0001\u0000\u0000\u0000\u016f\u0170\u0001"+
		"\u0000\u0000\u0000\u0170\u0172\u0001\u0000\u0000\u0000\u0171\u0173\u0005"+
		"\u0004\u0000\u0000\u0172\u0171\u0001\u0000\u0000\u0000\u0172\u0173\u0001"+
		"\u0000\u0000\u0000\u0173\u001b\u0001\u0000\u0000\u0000\u0174\u0176\u0006"+
		"\u000e\uffff\uffff\u0000\u0175\u0177\u0005\u001c\u0000\u0000\u0176\u0175"+
		"\u0001\u0000\u0000\u0000\u0176\u0177\u0001\u0000\u0000\u0000\u0177\u0178"+
		"\u0001\u0000\u0000\u0000\u0178\u017a\u0005\u001d\u0000\u0000\u0179\u017b"+
		"\u0005F\u0000\u0000\u017a\u0179\u0001\u0000\u0000\u0000\u017a\u017b\u0001"+
		"\u0000\u0000\u0000\u017b\u017c\u0001\u0000\u0000\u0000\u017c\u0185\u0005"+
		"\u0010\u0000\u0000\u017d\u0184\u0003\u0010\b\u0000\u017e\u0184\u0003\u001a"+
		"\r\u0000\u017f\u0184\u0003\u001e\u000f\u0000\u0180\u0184\u0003,\u0016"+
		"\u0000\u0181\u0184\u0003.\u0017\u0000\u0182\u0184\u0003 \u0010\u0000\u0183"+
		"\u017d\u0001\u0000\u0000\u0000\u0183\u017e\u0001\u0000\u0000\u0000\u0183"+
		"\u017f\u0001\u0000\u0000\u0000\u0183\u0180\u0001\u0000\u0000\u0000\u0183"+
		"\u0181\u0001\u0000\u0000\u0000\u0183\u0182\u0001\u0000\u0000\u0000\u0184"+
		"\u0187\u0001\u0000\u0000\u0000\u0185\u0183\u0001\u0000\u0000\u0000\u0185"+
		"\u0186\u0001\u0000\u0000\u0000\u0186\u0188\u0001\u0000\u0000\u0000\u0187"+
		"\u0185\u0001\u0000\u0000\u0000\u0188\u0189\u0005\u0011\u0000\u0000\u0189"+
		"\u001d\u0001\u0000\u0000\u0000\u018a\u018c\u00032\u0019\u0000\u018b\u018a"+
		"\u0001\u0000\u0000\u0000\u018c\u018f\u0001\u0000\u0000\u0000\u018d\u018b"+
		"\u0001\u0000\u0000\u0000\u018d\u018e\u0001\u0000\u0000\u0000\u018e\u0191"+
		"\u0001\u0000\u0000\u0000\u018f\u018d\u0001\u0000\u0000\u0000\u0190\u0192"+
		"\u0003X,\u0000\u0191\u0190\u0001\u0000\u0000\u0000\u0191\u0192\u0001\u0000"+
		"\u0000\u0000\u0192\u0193\u0001\u0000\u0000\u0000\u0193\u0194\u0005\u001e"+
		"\u0000\u0000\u0194\u01a1\u0005F\u0000\u0000\u0195\u0196\u0005\f\u0000"+
		"\u0000\u0196\u019d\u0003L&\u0000\u0197\u0198\u0005\u0002\u0000\u0000\u0198"+
		"\u019b\u0003L&\u0000\u0199\u019a\u0005\u0002\u0000\u0000\u019a\u019c\u0005"+
		"M\u0000\u0000\u019b\u0199\u0001\u0000\u0000\u0000\u019b\u019c\u0001\u0000"+
		"\u0000\u0000\u019c\u019e\u0001\u0000\u0000\u0000\u019d\u0197\u0001\u0000"+
		"\u0000\u0000\u019d\u019e\u0001\u0000\u0000\u0000\u019e\u019f\u0001\u0000"+
		"\u0000\u0000\u019f\u01a0\u0005\r\u0000\u0000\u01a0\u01a2\u0001\u0000\u0000"+
		"\u0000\u01a1\u0195\u0001\u0000\u0000\u0000\u01a1\u01a2\u0001\u0000\u0000"+
		"\u0000\u01a2\u01a5\u0001\u0000\u0000\u0000\u01a3\u01a4\u0005\u0015\u0000"+
		"\u0000\u01a4\u01a6\u0005:\u0000\u0000\u01a5\u01a3\u0001\u0000\u0000\u0000"+
		"\u01a5\u01a6\u0001\u0000\u0000\u0000\u01a6\u01a8\u0001\u0000\u0000\u0000"+
		"\u01a7\u01a9\u0005\u0004\u0000\u0000\u01a8\u01a7\u0001\u0000\u0000\u0000"+
		"\u01a8\u01a9\u0001\u0000\u0000\u0000\u01a9\u001f\u0001\u0000\u0000\u0000"+
		"\u01aa\u01ac\u00032\u0019\u0000\u01ab\u01aa\u0001\u0000\u0000\u0000\u01ac"+
		"\u01af\u0001\u0000\u0000\u0000\u01ad\u01ab\u0001\u0000\u0000\u0000\u01ad"+
		"\u01ae\u0001\u0000\u0000\u0000\u01ae\u01b2\u0001\u0000\u0000\u0000\u01af"+
		"\u01ad\u0001\u0000\u0000\u0000\u01b0\u01b3\u0005\u001f\u0000\u0000\u01b1"+
		"\u01b3\u0005 \u0000\u0000\u01b2\u01b0\u0001\u0000\u0000\u0000\u01b2\u01b1"+
		"\u0001\u0000\u0000\u0000\u01b3\u01c0\u0001\u0000\u0000\u0000\u01b4\u01bd"+
		"\u0005\f\u0000\u0000\u01b5\u01ba\u0003\"\u0011\u0000\u01b6\u01b7\u0005"+
		"\u0002\u0000\u0000\u01b7\u01b9\u0003\"\u0011\u0000\u01b8\u01b6\u0001\u0000"+
		"\u0000\u0000\u01b9\u01bc\u0001\u0000\u0000\u0000\u01ba\u01b8\u0001\u0000"+
		"\u0000\u0000\u01ba\u01bb\u0001\u0000\u0000\u0000\u01bb\u01be\u0001\u0000"+
		"\u0000\u0000\u01bc\u01ba\u0001\u0000\u0000\u0000\u01bd\u01b5\u0001\u0000"+
		"\u0000\u0000\u01bd\u01be\u0001\u0000\u0000\u0000\u01be\u01bf\u0001\u0000"+
		"\u0000\u0000\u01bf\u01c1\u0005\r\u0000\u0000\u01c0\u01b4\u0001\u0000\u0000"+
		"\u0000\u01c0\u01c1\u0001\u0000\u0000\u0000\u01c1\u01ca\u0001\u0000\u0000"+
		"\u0000\u01c2\u01c7\u0003D\"\u0000\u01c3\u01c4\u0005\u0002\u0000\u0000"+
		"\u01c4\u01c6\u0003D\"\u0000\u01c5\u01c3\u0001\u0000\u0000\u0000\u01c6"+
		"\u01c9\u0001\u0000\u0000\u0000\u01c7\u01c5\u0001\u0000\u0000\u0000\u01c7"+
		"\u01c8\u0001\u0000\u0000\u0000\u01c8\u01cb\u0001\u0000\u0000\u0000\u01c9"+
		"\u01c7\u0001\u0000\u0000\u0000\u01ca\u01c2\u0001\u0000\u0000\u0000\u01ca"+
		"\u01cb\u0001\u0000\u0000\u0000\u01cb\u01d5\u0001\u0000\u0000\u0000\u01cc"+
		"\u01cd\u0005!\u0000\u0000\u01cd\u01d2\u0003F#\u0000\u01ce\u01cf\u0005"+
		"\u0002\u0000\u0000\u01cf\u01d1\u0003F#\u0000\u01d0\u01ce\u0001\u0000\u0000"+
		"\u0000\u01d1\u01d4\u0001\u0000\u0000\u0000\u01d2\u01d0\u0001\u0000\u0000"+
		"\u0000\u01d2\u01d3\u0001\u0000\u0000\u0000\u01d3\u01d6\u0001\u0000\u0000"+
		"\u0000\u01d4\u01d2\u0001\u0000\u0000\u0000\u01d5\u01cc\u0001\u0000\u0000"+
		"\u0000\u01d5\u01d6\u0001\u0000\u0000\u0000\u01d6\u01d7\u0001\u0000\u0000"+
		"\u0000\u01d7\u01d9\u0005U\u0000\u0000\u01d8\u01da\u0003(\u0014\u0000\u01d9"+
		"\u01d8\u0001\u0000\u0000\u0000\u01d9\u01da\u0001\u0000\u0000\u0000\u01da"+
		"\u01dc\u0001\u0000\u0000\u0000\u01db\u01dd\u0003&\u0013\u0000\u01dc\u01db"+
		"\u0001\u0000\u0000\u0000\u01dc\u01dd\u0001\u0000\u0000\u0000\u01dd!\u0001"+
		"\u0000\u0000\u0000\u01de\u01e1\u0003$\u0012\u0000\u01df\u01e1\u0003D\""+
		"\u0000\u01e0\u01de\u0001\u0000\u0000\u0000\u01e0\u01df\u0001\u0000\u0000"+
		"\u0000\u01e1#\u0001\u0000\u0000\u0000\u01e2\u01e3\u0003\\.\u0000\u01e3"+
		"%\u0001\u0000\u0000\u0000\u01e4\u01e5\u0005\"\u0000\u0000\u01e5\u01e6"+
		"\u0005\f\u0000\u0000\u01e6\u01e7\u0003L&\u0000\u01e7\u01e8\u0005\r\u0000"+
		"\u0000\u01e8\u01e9\u0005U\u0000\u0000\u01e9\'\u0001\u0000\u0000\u0000"+
		"\u01ea\u01eb\u0005#\u0000\u0000\u01eb\u01ec\u0005\f\u0000\u0000\u01ec"+
		"\u01ed\u0003L&\u0000\u01ed\u01ee\u0005\r\u0000\u0000\u01ee\u01ef\u0005"+
		"U\u0000\u0000\u01ef)\u0001\u0000\u0000\u0000\u01f0\u01f2\u0003Z-\u0000"+
		"\u01f1\u01f0\u0001\u0000\u0000\u0000\u01f1\u01f2\u0001\u0000\u0000\u0000"+
		"\u01f2\u01f3\u0001\u0000\u0000\u0000\u01f3\u01f4\u0005$\u0000\u0000\u01f4"+
		"\u01f5\u0005U\u0000\u0000\u01f5+\u0001\u0000\u0000\u0000\u01f6\u01f7\u0005"+
		"F\u0000\u0000\u01f7\u01f8\u0005%\u0000\u0000\u01f8\u01fa\u0005&\u0000"+
		"\u0000\u01f9\u01fb\u0003R)\u0000\u01fa\u01f9\u0001\u0000\u0000\u0000\u01fa"+
		"\u01fb\u0001\u0000\u0000\u0000\u01fb\u01fc\u0001\u0000\u0000\u0000\u01fc"+
		"\u0208\u0003\u0004\u0002\u0000\u01fd\u01fe\u0005\n\u0000\u0000\u01fe\u0203"+
		"\u0003\n\u0005\u0000\u01ff\u0200\u0005\u0002\u0000\u0000\u0200\u0202\u0003"+
		"\n\u0005\u0000\u0201\u01ff\u0001\u0000\u0000\u0000\u0202\u0205\u0001\u0000"+
		"\u0000\u0000\u0203\u0201\u0001\u0000\u0000\u0000\u0203\u0204\u0001\u0000"+
		"\u0000\u0000\u0204\u0206\u0001\u0000\u0000\u0000\u0205\u0203\u0001\u0000"+
		"\u0000\u0000\u0206\u0207\u0005\u000b\u0000\u0000\u0207\u0209\u0001\u0000"+
		"\u0000\u0000\u0208\u01fd\u0001\u0000\u0000\u0000\u0208\u0209\u0001\u0000"+
		"\u0000\u0000\u0209\u020a\u0001\u0000\u0000\u0000\u020a\u0213\u0005\f\u0000"+
		"\u0000\u020b\u0210\u0003H$\u0000\u020c\u020d\u0005\u0002\u0000\u0000\u020d"+
		"\u020f\u0003H$\u0000\u020e\u020c\u0001\u0000\u0000\u0000\u020f\u0212\u0001"+
		"\u0000\u0000\u0000\u0210\u020e\u0001\u0000\u0000\u0000\u0210\u0211\u0001"+
		"\u0000\u0000\u0000\u0211\u0214\u0001\u0000\u0000\u0000\u0212\u0210\u0001"+
		"\u0000\u0000\u0000\u0213\u020b\u0001\u0000\u0000\u0000\u0213\u0214\u0001"+
		"\u0000\u0000\u0000\u0214\u0215\u0001\u0000\u0000\u0000\u0215\u021d\u0005"+
		"\r\u0000\u0000\u0216\u0217\u0005\u000e\u0000\u0000\u0217\u0218\u0003V"+
		"+\u0000\u0218\u0219\u0005\u0004\u0000\u0000\u0219\u021e\u0001\u0000\u0000"+
		"\u0000\u021a\u021c\u0005\u0004\u0000\u0000\u021b\u021a\u0001\u0000\u0000"+
		"\u0000\u021b\u021c\u0001\u0000\u0000\u0000\u021c\u021e\u0001\u0000\u0000"+
		"\u0000\u021d\u0216\u0001\u0000\u0000\u0000\u021d\u021b\u0001\u0000\u0000"+
		"\u0000\u021e-\u0001\u0000\u0000\u0000\u021f\u0224\u0003D\"\u0000\u0220"+
		"\u0221\u0005\u0002\u0000\u0000\u0221\u0223\u0003D\"\u0000\u0222\u0220"+
		"\u0001\u0000\u0000\u0000\u0223\u0226\u0001\u0000\u0000\u0000\u0224\u0222"+
		"\u0001\u0000\u0000\u0000\u0224\u0225\u0001\u0000\u0000\u0000\u0225\u0235"+
		"\u0001\u0000\u0000\u0000\u0226\u0224\u0001\u0000\u0000\u0000\u0227\u0228"+
		"\u0005\f\u0000\u0000\u0228\u022d\u0003D\"\u0000\u0229\u022a\u0005\u0002"+
		"\u0000\u0000\u022a\u022c\u0003D\"\u0000\u022b\u0229\u0001\u0000\u0000"+
		"\u0000\u022c\u022f\u0001\u0000\u0000\u0000\u022d\u022b\u0001\u0000\u0000"+
		"\u0000\u022d\u022e\u0001\u0000\u0000\u0000\u022e\u0230\u0001\u0000\u0000"+
		"\u0000\u022f\u022d\u0001\u0000\u0000\u0000\u0230\u0232\u0005\r\u0000\u0000"+
		"\u0231\u0233\u0005\'\u0000\u0000\u0232\u0231\u0001\u0000\u0000\u0000\u0232"+
		"\u0233\u0001\u0000\u0000\u0000\u0233\u0235\u0001\u0000\u0000\u0000\u0234"+
		"\u021f\u0001\u0000\u0000\u0000\u0234\u0227\u0001\u0000\u0000\u0000\u0235"+
		"\u0236\u0001\u0000\u0000\u0000\u0236\u0237\u0007\u0001\u0000\u0000\u0237"+
		"\u023c\u0003D\"\u0000\u0238\u0239\u0005\u0002\u0000\u0000\u0239\u023b"+
		"\u0003D\"\u0000\u023a\u0238\u0001\u0000\u0000\u0000\u023b\u023e\u0001"+
		"\u0000\u0000\u0000\u023c\u023a\u0001\u0000\u0000\u0000\u023c\u023d\u0001"+
		"\u0000\u0000\u0000\u023d\u0241\u0001\u0000\u0000\u0000\u023e\u023c\u0001"+
		"\u0000\u0000\u0000\u023f\u0240\u0005)\u0000\u0000\u0240\u0242\u0003L&"+
		"\u0000\u0241\u023f\u0001\u0000\u0000\u0000\u0241\u0242\u0001\u0000\u0000"+
		"\u0000\u0242\u0244\u0001\u0000\u0000\u0000\u0243\u0245\u00030\u0018\u0000"+
		"\u0244\u0243\u0001\u0000\u0000\u0000\u0244\u0245\u0001\u0000\u0000\u0000"+
		"\u0245\u0247\u0001\u0000\u0000\u0000\u0246\u0248\u0005\u0004\u0000\u0000"+
		"\u0247\u0246\u0001\u0000\u0000\u0000\u0247\u0248\u0001\u0000\u0000\u0000"+
		"\u0248/\u0001\u0000\u0000\u0000\u0249\u024a\u0005*\u0000\u0000\u024a\u024b"+
		"\u0005M\u0000\u0000\u024b1\u0001\u0000\u0000\u0000\u024c\u024d\u0005+"+
		"\u0000\u0000\u024d\u025d\u0005F\u0000\u0000\u024e\u025a\u0005\f\u0000"+
		"\u0000\u024f\u0254\u00034\u001a\u0000\u0250\u0251\u0005\u0002\u0000\u0000"+
		"\u0251\u0253\u00034\u001a\u0000\u0252\u0250\u0001\u0000\u0000\u0000\u0253"+
		"\u0256\u0001\u0000\u0000\u0000\u0254\u0252\u0001\u0000\u0000\u0000\u0254"+
		"\u0255\u0001\u0000\u0000\u0000\u0255\u0258\u0001\u0000\u0000\u0000\u0256"+
		"\u0254\u0001\u0000\u0000\u0000\u0257\u0259\u0005\u0002\u0000\u0000\u0258"+
		"\u0257\u0001\u0000\u0000\u0000\u0258\u0259\u0001\u0000\u0000\u0000\u0259"+
		"\u025b\u0001\u0000\u0000\u0000\u025a\u024f\u0001\u0000\u0000\u0000\u025a"+
		"\u025b\u0001\u0000\u0000\u0000\u025b\u025c\u0001\u0000\u0000\u0000\u025c"+
		"\u025e\u0005\r\u0000\u0000\u025d\u024e\u0001\u0000\u0000\u0000\u025d\u025e"+
		"\u0001\u0000\u0000\u0000\u025e3\u0001\u0000\u0000\u0000\u025f\u0260\u0005"+
		"F\u0000\u0000\u0260\u0262\u0005%\u0000\u0000\u0261\u025f\u0001\u0000\u0000"+
		"\u0000\u0261\u0262\u0001\u0000\u0000\u0000\u0262\u0263\u0001\u0000\u0000"+
		"\u0000\u0263\u0264\u00036\u001b\u0000\u02645\u0001\u0000\u0000\u0000\u0265"+
		"\u0266\u0007\u0002\u0000\u0000\u02667\u0001\u0000\u0000\u0000\u0267\u0268"+
		"\u0006\u001c\uffff\uffff\u0000\u0268\u0274\u0005\u0010\u0000\u0000\u0269"+
		"\u026e\u0003:\u001d\u0000\u026a\u026b\u0005\u0002\u0000\u0000\u026b\u026d"+
		"\u0003:\u001d\u0000\u026c\u026a\u0001\u0000\u0000\u0000\u026d\u0270\u0001"+
		"\u0000\u0000\u0000\u026e\u026c\u0001\u0000\u0000\u0000\u026e\u026f\u0001"+
		"\u0000\u0000\u0000\u026f\u0272\u0001\u0000\u0000\u0000\u0270\u026e\u0001"+
		"\u0000\u0000\u0000\u0271\u0273\u0005\u0002\u0000\u0000\u0272\u0271\u0001"+
		"\u0000\u0000\u0000\u0272\u0273\u0001\u0000\u0000\u0000\u0273\u0275\u0001"+
		"\u0000\u0000\u0000\u0274\u0269\u0001\u0000\u0000\u0000\u0274\u0275\u0001"+
		"\u0000\u0000\u0000\u0275\u0276\u0001\u0000\u0000\u0000\u0276\u0277\u0005"+
		"\u0011\u0000\u0000\u02779\u0001\u0000\u0000\u0000\u0278\u0279\u0005P\u0000"+
		"\u0000\u0279\u027a\u0005\u0015\u0000\u0000\u027a\u027b\u0003>\u001f\u0000"+
		"\u027b;\u0001\u0000\u0000\u0000\u027c\u027d\u0005,\u0000\u0000\u027d\u0282"+
		"\u0003>\u001f\u0000\u027e\u027f\u0005\u0002\u0000\u0000\u027f\u0281\u0003"+
		">\u001f\u0000\u0280\u027e\u0001\u0000\u0000\u0000\u0281\u0284\u0001\u0000"+
		"\u0000\u0000\u0282\u0280\u0001\u0000\u0000\u0000\u0282\u0283\u0001\u0000"+
		"\u0000\u0000\u0283\u0286\u0001\u0000\u0000\u0000\u0284\u0282\u0001\u0000"+
		"\u0000\u0000\u0285\u0287\u0005\u0002\u0000\u0000\u0286\u0285\u0001\u0000"+
		"\u0000\u0000\u0286\u0287\u0001\u0000\u0000\u0000\u0287\u0288\u0001\u0000"+
		"\u0000\u0000\u0288\u0289\u0005-\u0000\u0000\u0289=\u0001\u0000\u0000\u0000"+
		"\u028a\u0291\u00038\u001c\u0000\u028b\u0291\u0003<\u001e\u0000\u028c\u0291"+
		"\u0005B\u0000\u0000\u028d\u028e\u0005G\u0000\u0000\u028e\u0291\u0005X"+
		"\u0000\u0000\u028f\u0291\u0005W\u0000\u0000\u0290\u028a\u0001\u0000\u0000"+
		"\u0000\u0290\u028b\u0001\u0000\u0000\u0000\u0290\u028c\u0001\u0000\u0000"+
		"\u0000\u0290\u028d\u0001\u0000\u0000\u0000\u0290\u028f\u0001\u0000\u0000"+
		"\u0000\u0291?\u0001\u0000\u0000\u0000\u0292\u0295\u0003P(\u0000\u0293"+
		"\u0295\u0003\u001e\u000f\u0000\u0294\u0292\u0001\u0000\u0000\u0000\u0294"+
		"\u0293\u0001\u0000\u0000\u0000\u0295A\u0001\u0000\u0000\u0000\u0296\u029a"+
		"\u0003@ \u0000\u0297\u029a\u0003\u001a\r\u0000\u0298\u029a\u0003\u001c"+
		"\u000e\u0000\u0299\u0296\u0001\u0000\u0000\u0000\u0299\u0297\u0001\u0000"+
		"\u0000\u0000\u0299\u0298\u0001\u0000\u0000\u0000\u029aC\u0001\u0000\u0000"+
		"\u0000\u029b\u02ac\u0003B!\u0000\u029c\u029d\u0003,\u0016\u0000\u029d"+
		"\u029e\u0005.\u0000\u0000\u029e\u029f\u0003B!\u0000\u029f\u02ac\u0001"+
		"\u0000\u0000\u0000\u02a0\u02a1\u0005/\u0000\u0000\u02a1\u02a7\u0005\f"+
		"\u0000\u0000\u02a2\u02a8\u0003B!\u0000\u02a3\u02a4\u0003,\u0016\u0000"+
		"\u02a4\u02a5\u0005.\u0000\u0000\u02a5\u02a6\u0003B!\u0000\u02a6\u02a8"+
		"\u0001\u0000\u0000\u0000\u02a7\u02a2\u0001\u0000\u0000\u0000\u02a7\u02a3"+
		"\u0001\u0000\u0000\u0000\u02a8\u02a9\u0001\u0000\u0000\u0000\u02a9\u02aa"+
		"\u0005\r\u0000\u0000\u02aa\u02ac\u0001\u0000\u0000\u0000\u02ab\u029b\u0001"+
		"\u0000\u0000\u0000\u02ab\u029c\u0001\u0000\u0000\u0000\u02ab\u02a0\u0001"+
		"\u0000\u0000\u0000\u02acE\u0001\u0000\u0000\u0000\u02ad\u02b4\u0003D\""+
		"\u0000\u02ae\u02af\u0003^/\u0000\u02af\u02b0\u0005\f\u0000\u0000\u02b0"+
		"\u02b1\u0003\u001c\u000e\u0000\u02b1\u02b2\u0005\r\u0000\u0000\u02b2\u02b4"+
		"\u0001\u0000\u0000\u0000\u02b3\u02ad\u0001\u0000\u0000\u0000\u02b3\u02ae"+
		"\u0001\u0000\u0000\u0000\u02b4G\u0001\u0000\u0000\u0000\u02b5\u02d5\u0003"+
		"J%\u0000\u02b6\u02b7\u0005%\u0000\u0000\u02b7\u02d6\u0003L&\u0000\u02b8"+
		"\u02ba\u0005%\u0000\u0000\u02b9\u02b8\u0001\u0000\u0000\u0000\u02b9\u02ba"+
		"\u0001\u0000\u0000\u0000\u02ba\u02d3\u0001\u0000\u0000\u0000\u02bb\u02c4"+
		"\u0005\f\u0000\u0000\u02bc\u02c1\u0003L&\u0000\u02bd\u02be\u0005\u0002"+
		"\u0000\u0000\u02be\u02c0\u0003L&\u0000\u02bf\u02bd\u0001\u0000\u0000\u0000"+
		"\u02c0\u02c3\u0001\u0000\u0000\u0000\u02c1\u02bf\u0001\u0000\u0000\u0000"+
		"\u02c1\u02c2\u0001\u0000\u0000\u0000\u02c2\u02c5\u0001\u0000\u0000\u0000"+
		"\u02c3\u02c1\u0001\u0000\u0000\u0000\u02c4\u02bc\u0001\u0000\u0000\u0000"+
		"\u02c4\u02c5\u0001\u0000\u0000\u0000\u02c5\u02c6\u0001\u0000\u0000\u0000"+
		"\u02c6\u02d4\u0005\r\u0000\u0000\u02c7\u02d0\u0005\u0010\u0000\u0000\u02c8"+
		"\u02cd\u0003L&\u0000\u02c9\u02ca\u0005\u0002\u0000\u0000\u02ca\u02cc\u0003"+
		"L&\u0000\u02cb\u02c9\u0001\u0000\u0000\u0000\u02cc\u02cf\u0001\u0000\u0000"+
		"\u0000\u02cd\u02cb\u0001\u0000\u0000\u0000\u02cd\u02ce\u0001\u0000\u0000"+
		"\u0000\u02ce\u02d1\u0001\u0000\u0000\u0000\u02cf\u02cd\u0001\u0000\u0000"+
		"\u0000\u02d0\u02c8\u0001\u0000\u0000\u0000\u02d0\u02d1\u0001\u0000\u0000"+
		"\u0000\u02d1\u02d2\u0001\u0000\u0000\u0000\u02d2\u02d4\u0005\u0011\u0000"+
		"\u0000\u02d3\u02bb\u0001\u0000\u0000\u0000\u02d3\u02c7\u0001\u0000\u0000"+
		"\u0000\u02d4\u02d6\u0001\u0000\u0000\u0000\u02d5\u02b6\u0001\u0000\u0000"+
		"\u0000\u02d5\u02b9\u0001\u0000\u0000\u0000\u02d6I\u0001\u0000\u0000\u0000"+
		"\u02d7\u02d9\u00032\u0019\u0000\u02d8\u02d7\u0001\u0000\u0000\u0000\u02d9"+
		"\u02dc\u0001\u0000\u0000\u0000\u02da\u02d8\u0001\u0000\u0000\u0000\u02da"+
		"\u02db\u0001\u0000\u0000\u0000\u02db\u02dd\u0001\u0000\u0000\u0000\u02dc"+
		"\u02da\u0001\u0000\u0000\u0000\u02dd\u02e0\u0005F\u0000\u0000\u02de\u02df"+
		"\u0005\u0015\u0000\u0000\u02df\u02e1\u0005:\u0000\u0000\u02e0\u02de\u0001"+
		"\u0000\u0000\u0000\u02e0\u02e1\u0001\u0000\u0000\u0000\u02e1\u02fa\u0001"+
		"\u0000\u0000\u0000\u02e2\u02eb\u0005\f\u0000\u0000\u02e3\u02e8\u0003L"+
		"&\u0000\u02e4\u02e5\u0005\u0002\u0000\u0000\u02e5\u02e7\u0003L&\u0000"+
		"\u02e6\u02e4\u0001\u0000\u0000\u0000\u02e7\u02ea\u0001\u0000\u0000\u0000"+
		"\u02e8\u02e6\u0001\u0000\u0000\u0000\u02e8\u02e9\u0001\u0000\u0000\u0000"+
		"\u02e9\u02ec\u0001\u0000\u0000\u0000\u02ea\u02e8\u0001\u0000\u0000\u0000"+
		"\u02eb\u02e3\u0001\u0000\u0000\u0000\u02eb\u02ec\u0001\u0000\u0000\u0000"+
		"\u02ec\u02ed\u0001\u0000\u0000\u0000\u02ed\u02fb\u0005\r\u0000\u0000\u02ee"+
		"\u02f7\u0005\u0010\u0000\u0000\u02ef\u02f4\u0003L&\u0000\u02f0\u02f1\u0005"+
		"\u0002\u0000\u0000\u02f1\u02f3\u0003L&\u0000\u02f2\u02f0\u0001\u0000\u0000"+
		"\u0000\u02f3\u02f6\u0001\u0000\u0000\u0000\u02f4\u02f2\u0001\u0000\u0000"+
		"\u0000\u02f4\u02f5\u0001\u0000\u0000\u0000\u02f5\u02f8\u0001\u0000\u0000"+
		"\u0000\u02f6\u02f4\u0001\u0000\u0000\u0000\u02f7\u02ef\u0001\u0000\u0000"+
		"\u0000\u02f7\u02f8\u0001\u0000\u0000\u0000\u02f8\u02f9\u0001\u0000\u0000"+
		"\u0000\u02f9\u02fb\u0005\u0011\u0000\u0000\u02fa\u02e2\u0001\u0000\u0000"+
		"\u0000\u02fa\u02ee\u0001\u0000\u0000\u0000\u02fa\u02fb\u0001\u0000\u0000"+
		"\u0000\u02fbK\u0001\u0000\u0000\u0000\u02fc\u02fd\u0006&\uffff\uffff\u0000"+
		"\u02fd\u0302\u0005B\u0000\u0000\u02fe\u0302\u00059\u0000\u0000\u02ff\u0302"+
		"\u0003N\'\u0000\u0300\u0302\u0005U\u0000\u0000\u0301\u02fc\u0001\u0000"+
		"\u0000\u0000\u0301\u02fe\u0001\u0000\u0000\u0000\u0301\u02ff\u0001\u0000"+
		"\u0000\u0000\u0301\u0300\u0001\u0000\u0000\u0000\u0302M\u0001\u0000\u0000"+
		"\u0000\u0303\u0304\u0003J%\u0000\u0304O\u0001\u0000\u0000\u0000\u0305"+
		"\u0308\u0003\u0016\u000b\u0000\u0306\u0308\u0003\u0018\f\u0000\u0307\u0305"+
		"\u0001\u0000\u0000\u0000\u0307\u0306\u0001\u0000\u0000\u0000\u0308Q\u0001"+
		"\u0000\u0000\u0000\u0309\u0316\u0005[\u0000\u0000\u030a\u030b\u0005,\u0000"+
		"\u0000\u030b\u0310\u0003T*\u0000\u030c\u030d\u0005\'\u0000\u0000\u030d"+
		"\u030f\u0003T*\u0000\u030e\u030c\u0001\u0000\u0000\u0000\u030f\u0312\u0001"+
		"\u0000\u0000\u0000\u0310\u030e\u0001\u0000\u0000\u0000\u0310\u0311\u0001"+
		"\u0000\u0000\u0000\u0311\u0313\u0001\u0000\u0000\u0000\u0312\u0310\u0001"+
		"\u0000\u0000\u0000\u0313\u0314\u0005-\u0000\u0000\u0314\u0316\u0001\u0000"+
		"\u0000\u0000\u0315\u0309\u0001\u0000\u0000\u0000\u0315\u030a\u0001\u0000"+
		"\u0000\u0000\u0316S\u0001\u0000\u0000\u0000\u0317\u031f\u0005G\u0000\u0000"+
		"\u0318\u031f\u0003J%\u0000\u0319\u031a\u00050\u0000\u0000\u031a\u031b"+
		"\u0003D\"\u0000\u031b\u031c\u0005\r\u0000\u0000\u031c\u031f\u0001\u0000"+
		"\u0000\u0000\u031d\u031f\u0005U\u0000\u0000\u031e\u0317\u0001\u0000\u0000"+
		"\u0000\u031e\u0318\u0001\u0000\u0000\u0000\u031e\u0319\u0001\u0000\u0000"+
		"\u0000\u031e\u031d\u0001\u0000\u0000\u0000\u031fU\u0001\u0000\u0000\u0000"+
		"\u0320\u0321\u0007\u0003\u0000\u0000\u0321W\u0001\u0000\u0000\u0000\u0322"+
		"\u0323\u0007\u0004\u0000\u0000\u0323Y\u0001\u0000\u0000\u0000\u0324\u0325"+
		"\u0007\u0005\u0000\u0000\u0325[\u0001\u0000\u0000\u0000\u0326\u0327\u0007"+
		"\u0006\u0000\u0000\u0327]\u0001\u0000\u0000\u0000\u0328\u0329\u0007\u0007"+
		"\u0000\u0000\u0329_\u0001\u0000\u0000\u0000\u0080djpv|\u0080\u0086\u008a"+
		"\u008f\u0094\u0098\u009b\u009f\u00a7\u00ac\u00b4\u00b9\u00bd\u00c5\u00c8"+
		"\u00d6\u00d8\u00df\u00e4\u00e9\u00ec\u00f1\u00f5\u00fb\u0103\u0106\u010f"+
		"\u0112\u0115\u0118\u011b\u0125\u0128\u012d\u0131\u0136\u013b\u013f\u0143"+
		"\u0148\u014b\u0150\u0155\u015a\u015d\u0162\u016b\u016f\u0172\u0176\u017a"+
		"\u0183\u0185\u018d\u0191\u019b\u019d\u01a1\u01a5\u01a8\u01ad\u01b2\u01ba"+
		"\u01bd\u01c0\u01c7\u01ca\u01d2\u01d5\u01d9\u01dc\u01e0\u01f1\u01fa\u0203"+
		"\u0208\u0210\u0213\u021b\u021d\u0224\u022d\u0232\u0234\u023c\u0241\u0244"+
		"\u0247\u0254\u0258\u025a\u025d\u0261\u026e\u0272\u0274\u0282\u0286\u0290"+
		"\u0294\u0299\u02a7\u02ab\u02b3\u02b9\u02c1\u02c4\u02cd\u02d0\u02d3\u02d5"+
		"\u02da\u02e0\u02e8\u02eb\u02f4\u02f7\u02fa\u0301\u0307\u0310\u0315\u031e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}