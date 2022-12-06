// $ANTLR 3.5 C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g 2022-12-01 20:48:48

package org.lflang.parser.antlr.internal;

// Hack: Use our own Lexer superclass by means of import. 
// Currently there is no other way to specify the superclass for the lexer.
import org.eclipse.xtext.parser.antlr.Lexer;


import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

@SuppressWarnings("all")
public class InternalLFLexer extends Lexer {
	public static final int EOF=-1;
	public static final int T__17=17;
	public static final int T__18=18;
	public static final int T__19=19;
	public static final int T__20=20;
	public static final int T__21=21;
	public static final int T__22=22;
	public static final int T__23=23;
	public static final int T__24=24;
	public static final int T__25=25;
	public static final int T__26=26;
	public static final int T__27=27;
	public static final int T__28=28;
	public static final int T__29=29;
	public static final int T__30=30;
	public static final int T__31=31;
	public static final int T__32=32;
	public static final int T__33=33;
	public static final int T__34=34;
	public static final int T__35=35;
	public static final int T__36=36;
	public static final int T__37=37;
	public static final int T__38=38;
	public static final int T__39=39;
	public static final int T__40=40;
	public static final int T__41=41;
	public static final int T__42=42;
	public static final int T__43=43;
	public static final int T__44=44;
	public static final int T__45=45;
	public static final int T__46=46;
	public static final int T__47=47;
	public static final int T__48=48;
	public static final int T__49=49;
	public static final int T__50=50;
	public static final int T__51=51;
	public static final int T__52=52;
	public static final int T__53=53;
	public static final int T__54=54;
	public static final int T__55=55;
	public static final int T__56=56;
	public static final int T__57=57;
	public static final int T__58=58;
	public static final int T__59=59;
	public static final int T__60=60;
	public static final int T__61=61;
	public static final int T__62=62;
	public static final int T__63=63;
	public static final int T__64=64;
	public static final int T__65=65;
	public static final int T__66=66;
	public static final int T__67=67;
	public static final int T__68=68;
	public static final int T__69=69;
	public static final int T__70=70;
	public static final int T__71=71;
	public static final int T__72=72;
	public static final int T__73=73;
	public static final int T__74=74;
	public static final int T__75=75;
	public static final int T__76=76;
	public static final int T__77=77;
	public static final int T__78=78;
	public static final int T__79=79;
	public static final int T__80=80;
	public static final int T__81=81;
	public static final int T__82=82;
	public static final int T__83=83;
	public static final int T__84=84;
	public static final int T__85=85;
	public static final int RULE_ANY_OTHER=4;
	public static final int RULE_CHAR_LIT=5;
	public static final int RULE_FALSE=6;
	public static final int RULE_FLOAT_EXP_SUFFIX=7;
	public static final int RULE_ID=8;
	public static final int RULE_INT=9;
	public static final int RULE_LT_ANNOT=10;
	public static final int RULE_ML_COMMENT=11;
	public static final int RULE_NEGINT=12;
	public static final int RULE_SL_COMMENT=13;
	public static final int RULE_STRING=14;
	public static final int RULE_TRUE=15;
	public static final int RULE_WS=16;

	// delegates
	// delegators
	public Lexer[] getDelegates() {
		return new Lexer[] {};
	}

	public InternalLFLexer() {} 
	public InternalLFLexer(CharStream input) {
		this(input, new RecognizerSharedState());
	}
	public InternalLFLexer(CharStream input, RecognizerSharedState state) {
		super(input,state);
	}
	@Override public String getGrammarFileName() { return "C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g"; }

	// $ANTLR start "T__17"
	public final void mT__17() throws RecognitionException {
		try {
			int _type = T__17;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:10:7: ( '%' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:10:9: '%'
			{
			match('%'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__17"

	// $ANTLR start "T__18"
	public final void mT__18() throws RecognitionException {
		try {
			int _type = T__18;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:11:7: ( '(' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:11:9: '('
			{
			match('('); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__18"

	// $ANTLR start "T__19"
	public final void mT__19() throws RecognitionException {
		try {
			int _type = T__19;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:12:7: ( ')' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:12:9: ')'
			{
			match(')'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__19"

	// $ANTLR start "T__20"
	public final void mT__20() throws RecognitionException {
		try {
			int _type = T__20;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:13:7: ( '*' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:13:9: '*'
			{
			match('*'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__20"

	// $ANTLR start "T__21"
	public final void mT__21() throws RecognitionException {
		try {
			int _type = T__21;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:14:7: ( '+' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:14:9: '+'
			{
			match('+'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__21"

	// $ANTLR start "T__22"
	public final void mT__22() throws RecognitionException {
		try {
			int _type = T__22;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:15:7: ( ',' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:15:9: ','
			{
			match(','); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__22"

	// $ANTLR start "T__23"
	public final void mT__23() throws RecognitionException {
		try {
			int _type = T__23;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:16:7: ( '-' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:16:9: '-'
			{
			match('-'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__23"

	// $ANTLR start "T__24"
	public final void mT__24() throws RecognitionException {
		try {
			int _type = T__24;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:17:7: ( '->' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:17:9: '->'
			{
			match("->"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__24"

	// $ANTLR start "T__25"
	public final void mT__25() throws RecognitionException {
		try {
			int _type = T__25;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:18:7: ( '.' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:18:9: '.'
			{
			match('.'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__25"

	// $ANTLR start "T__26"
	public final void mT__26() throws RecognitionException {
		try {
			int _type = T__26;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:19:7: ( '/' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:19:9: '/'
			{
			match('/'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__26"

	// $ANTLR start "T__27"
	public final void mT__27() throws RecognitionException {
		try {
			int _type = T__27;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:20:7: ( ':' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:20:9: ':'
			{
			match(':'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__27"

	// $ANTLR start "T__28"
	public final void mT__28() throws RecognitionException {
		try {
			int _type = T__28;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:21:7: ( '::' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:21:9: '::'
			{
			match("::"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__28"

	// $ANTLR start "T__29"
	public final void mT__29() throws RecognitionException {
		try {
			int _type = T__29;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:22:7: ( ':\\\\' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:22:9: ':\\\\'
			{
			match(":\\"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__29"

	// $ANTLR start "T__30"
	public final void mT__30() throws RecognitionException {
		try {
			int _type = T__30;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:23:7: ( ';' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:23:9: ';'
			{
			match(';'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__30"

	// $ANTLR start "T__31"
	public final void mT__31() throws RecognitionException {
		try {
			int _type = T__31;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:24:7: ( '<' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:24:9: '<'
			{
			match('<'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__31"

	// $ANTLR start "T__32"
	public final void mT__32() throws RecognitionException {
		try {
			int _type = T__32;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:25:7: ( '=' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:25:9: '='
			{
			match('='); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__32"

	// $ANTLR start "T__33"
	public final void mT__33() throws RecognitionException {
		try {
			int _type = T__33;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:26:7: ( '=}' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:26:9: '=}'
			{
			match("=}"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__33"

	// $ANTLR start "T__34"
	public final void mT__34() throws RecognitionException {
		try {
			int _type = T__34;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:27:7: ( '>' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:27:9: '>'
			{
			match('>'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__34"

	// $ANTLR start "T__35"
	public final void mT__35() throws RecognitionException {
		try {
			int _type = T__35;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:28:7: ( '@' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:28:9: '@'
			{
			match('@'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__35"

	// $ANTLR start "T__36"
	public final void mT__36() throws RecognitionException {
		try {
			int _type = T__36;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:29:7: ( 'NONE' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:29:9: 'NONE'
			{
			match("NONE"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__36"

	// $ANTLR start "T__37"
	public final void mT__37() throws RecognitionException {
		try {
			int _type = T__37;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:30:7: ( 'STP' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:30:9: 'STP'
			{
			match("STP"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__37"

	// $ANTLR start "T__38"
	public final void mT__38() throws RecognitionException {
		try {
			int _type = T__38;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:31:7: ( '[' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:31:9: '['
			{
			match('['); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__38"

	// $ANTLR start "T__39"
	public final void mT__39() throws RecognitionException {
		try {
			int _type = T__39;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:32:7: ( '\\'' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:32:9: '\\''
			{
			match('\''); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__39"

	// $ANTLR start "T__40"
	public final void mT__40() throws RecognitionException {
		try {
			int _type = T__40;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:33:7: ( '\\\\' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:33:9: '\\\\'
			{
			match('\\'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__40"

	// $ANTLR start "T__41"
	public final void mT__41() throws RecognitionException {
		try {
			int _type = T__41;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:34:7: ( ']' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:34:9: ']'
			{
			match(']'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__41"

	// $ANTLR start "T__42"
	public final void mT__42() throws RecognitionException {
		try {
			int _type = T__42;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:35:7: ( '_' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:35:9: '_'
			{
			match('_'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__42"

	// $ANTLR start "T__43"
	public final void mT__43() throws RecognitionException {
		try {
			int _type = T__43;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:36:7: ( 'action' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:36:9: 'action'
			{
			match("action"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__43"

	// $ANTLR start "T__44"
	public final void mT__44() throws RecognitionException {
		try {
			int _type = T__44;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:37:7: ( 'after' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:37:9: 'after'
			{
			match("after"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__44"

	// $ANTLR start "T__45"
	public final void mT__45() throws RecognitionException {
		try {
			int _type = T__45;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:38:7: ( 'as' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:38:9: 'as'
			{
			match("as"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__45"

	// $ANTLR start "T__46"
	public final void mT__46() throws RecognitionException {
		try {
			int _type = T__46;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:39:7: ( 'at' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:39:9: 'at'
			{
			match("at"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__46"

	// $ANTLR start "T__47"
	public final void mT__47() throws RecognitionException {
		try {
			int _type = T__47;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:40:7: ( 'const' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:40:9: 'const'
			{
			match("const"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__47"

	// $ANTLR start "T__48"
	public final void mT__48() throws RecognitionException {
		try {
			int _type = T__48;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:41:7: ( 'deadline' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:41:9: 'deadline'
			{
			match("deadline"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__48"

	// $ANTLR start "T__49"
	public final void mT__49() throws RecognitionException {
		try {
			int _type = T__49;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:42:7: ( 'extends' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:42:9: 'extends'
			{
			match("extends"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__49"

	// $ANTLR start "T__50"
	public final void mT__50() throws RecognitionException {
		try {
			int _type = T__50;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:43:7: ( 'federated' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:43:9: 'federated'
			{
			match("federated"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__50"

	// $ANTLR start "T__51"
	public final void mT__51() throws RecognitionException {
		try {
			int _type = T__51;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:44:7: ( 'from' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:44:9: 'from'
			{
			match("from"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__51"

	// $ANTLR start "T__52"
	public final void mT__52() throws RecognitionException {
		try {
			int _type = T__52;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:45:7: ( 'history' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:45:9: 'history'
			{
			match("history"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__52"

	// $ANTLR start "T__53"
	public final void mT__53() throws RecognitionException {
		try {
			int _type = T__53;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:46:7: ( 'import' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:46:9: 'import'
			{
			match("import"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__53"

	// $ANTLR start "T__54"
	public final void mT__54() throws RecognitionException {
		try {
			int _type = T__54;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:47:7: ( 'initial' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:47:9: 'initial'
			{
			match("initial"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__54"

	// $ANTLR start "T__55"
	public final void mT__55() throws RecognitionException {
		try {
			int _type = T__55;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:48:7: ( 'input' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:48:9: 'input'
			{
			match("input"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__55"

	// $ANTLR start "T__56"
	public final void mT__56() throws RecognitionException {
		try {
			int _type = T__56;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:49:7: ( 'interleaved' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:49:9: 'interleaved'
			{
			match("interleaved"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__56"

	// $ANTLR start "T__57"
	public final void mT__57() throws RecognitionException {
		try {
			int _type = T__57;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:50:7: ( 'logical' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:50:9: 'logical'
			{
			match("logical"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__57"

	// $ANTLR start "T__58"
	public final void mT__58() throws RecognitionException {
		try {
			int _type = T__58;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:51:7: ( 'main' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:51:9: 'main'
			{
			match("main"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__58"

	// $ANTLR start "T__59"
	public final void mT__59() throws RecognitionException {
		try {
			int _type = T__59;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:52:7: ( 'method' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:52:9: 'method'
			{
			match("method"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__59"

	// $ANTLR start "T__60"
	public final void mT__60() throws RecognitionException {
		try {
			int _type = T__60;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:53:7: ( 'mode' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:53:9: 'mode'
			{
			match("mode"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__60"

	// $ANTLR start "T__61"
	public final void mT__61() throws RecognitionException {
		try {
			int _type = T__61;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:54:7: ( 'mutable' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:54:9: 'mutable'
			{
			match("mutable"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__61"

	// $ANTLR start "T__62"
	public final void mT__62() throws RecognitionException {
		try {
			int _type = T__62;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:55:7: ( 'mutation' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:55:9: 'mutation'
			{
			match("mutation"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__62"

	// $ANTLR start "T__63"
	public final void mT__63() throws RecognitionException {
		try {
			int _type = T__63;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:56:7: ( 'new' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:56:9: 'new'
			{
			match("new"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__63"

	// $ANTLR start "T__64"
	public final void mT__64() throws RecognitionException {
		try {
			int _type = T__64;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:57:7: ( 'output' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:57:9: 'output'
			{
			match("output"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__64"

	// $ANTLR start "T__65"
	public final void mT__65() throws RecognitionException {
		try {
			int _type = T__65;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:58:7: ( 'physical' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:58:9: 'physical'
			{
			match("physical"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__65"

	// $ANTLR start "T__66"
	public final void mT__66() throws RecognitionException {
		try {
			int _type = T__66;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:59:7: ( 'preamble' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:59:9: 'preamble'
			{
			match("preamble"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__66"

	// $ANTLR start "T__67"
	public final void mT__67() throws RecognitionException {
		try {
			int _type = T__67;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:60:7: ( 'private' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:60:9: 'private'
			{
			match("private"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__67"

	// $ANTLR start "T__68"
	public final void mT__68() throws RecognitionException {
		try {
			int _type = T__68;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:61:7: ( 'public' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:61:9: 'public'
			{
			match("public"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__68"

	// $ANTLR start "T__69"
	public final void mT__69() throws RecognitionException {
		try {
			int _type = T__69;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:62:7: ( 'reaction' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:62:9: 'reaction'
			{
			match("reaction"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__69"

	// $ANTLR start "T__70"
	public final void mT__70() throws RecognitionException {
		try {
			int _type = T__70;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:63:7: ( 'reactor' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:63:9: 'reactor'
			{
			match("reactor"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__70"

	// $ANTLR start "T__71"
	public final void mT__71() throws RecognitionException {
		try {
			int _type = T__71;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:64:7: ( 'realtime' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:64:9: 'realtime'
			{
			match("realtime"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__71"

	// $ANTLR start "T__72"
	public final void mT__72() throws RecognitionException {
		try {
			int _type = T__72;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:65:7: ( 'reset' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:65:9: 'reset'
			{
			match("reset"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__72"

	// $ANTLR start "T__73"
	public final void mT__73() throws RecognitionException {
		try {
			int _type = T__73;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:66:7: ( 'serializer' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:66:9: 'serializer'
			{
			match("serializer"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__73"

	// $ANTLR start "T__74"
	public final void mT__74() throws RecognitionException {
		try {
			int _type = T__74;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:67:7: ( 'shutdown' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:67:9: 'shutdown'
			{
			match("shutdown"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__74"

	// $ANTLR start "T__75"
	public final void mT__75() throws RecognitionException {
		try {
			int _type = T__75;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:68:7: ( 'startup' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:68:9: 'startup'
			{
			match("startup"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__75"

	// $ANTLR start "T__76"
	public final void mT__76() throws RecognitionException {
		try {
			int _type = T__76;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:69:7: ( 'state' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:69:9: 'state'
			{
			match("state"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__76"

	// $ANTLR start "T__77"
	public final void mT__77() throws RecognitionException {
		try {
			int _type = T__77;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:70:7: ( 'target' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:70:9: 'target'
			{
			match("target"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__77"

	// $ANTLR start "T__78"
	public final void mT__78() throws RecognitionException {
		try {
			int _type = T__78;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:71:7: ( 'time' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:71:9: 'time'
			{
			match("time"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__78"

	// $ANTLR start "T__79"
	public final void mT__79() throws RecognitionException {
		try {
			int _type = T__79;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:72:7: ( 'timer' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:72:9: 'timer'
			{
			match("timer"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__79"

	// $ANTLR start "T__80"
	public final void mT__80() throws RecognitionException {
		try {
			int _type = T__80;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:73:7: ( 'widthof' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:73:9: 'widthof'
			{
			match("widthof"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__80"

	// $ANTLR start "T__81"
	public final void mT__81() throws RecognitionException {
		try {
			int _type = T__81;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:74:7: ( 'widthof(' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:74:9: 'widthof('
			{
			match("widthof("); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__81"

	// $ANTLR start "T__82"
	public final void mT__82() throws RecognitionException {
		try {
			int _type = T__82;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:75:7: ( '{' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:75:9: '{'
			{
			match('{'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__82"

	// $ANTLR start "T__83"
	public final void mT__83() throws RecognitionException {
		try {
			int _type = T__83;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:76:7: ( '{=' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:76:9: '{='
			{
			match("{="); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__83"

	// $ANTLR start "T__84"
	public final void mT__84() throws RecognitionException {
		try {
			int _type = T__84;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:77:7: ( '}' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:77:9: '}'
			{
			match('}'); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__84"

	// $ANTLR start "T__85"
	public final void mT__85() throws RecognitionException {
		try {
			int _type = T__85;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:78:7: ( '~>' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:78:9: '~>'
			{
			match("~>"); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "T__85"

	// $ANTLR start "RULE_WS"
	public final void mRULE_WS() throws RecognitionException {
		try {
			int _type = RULE_WS;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7171:9: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7171:11: ( ' ' | '\\t' | '\\r' | '\\n' )+
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7171:11: ( ' ' | '\\t' | '\\r' | '\\n' )+
			int cnt1=0;
			loop1:
			while (true) {
				int alt1=2;
				int LA1_0 = input.LA(1);
				if ( ((LA1_0 >= '\t' && LA1_0 <= '\n')||LA1_0=='\r'||LA1_0==' ') ) {
					alt1=1;
				}

				switch (alt1) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:
					{
					if ( (input.LA(1) >= '\t' && input.LA(1) <= '\n')||input.LA(1)=='\r'||input.LA(1)==' ' ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					if ( cnt1 >= 1 ) break loop1;
					EarlyExitException eee = new EarlyExitException(1, input);
					throw eee;
				}
				cnt1++;
			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_WS"

	// $ANTLR start "RULE_TRUE"
	public final void mRULE_TRUE() throws RecognitionException {
		try {
			int _type = RULE_TRUE;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7173:11: ( ( 'true' | 'True' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7173:13: ( 'true' | 'True' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7173:13: ( 'true' | 'True' )
			int alt2=2;
			int LA2_0 = input.LA(1);
			if ( (LA2_0=='t') ) {
				alt2=1;
			}
			else if ( (LA2_0=='T') ) {
				alt2=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 2, 0, input);
				throw nvae;
			}

			switch (alt2) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7173:14: 'true'
					{
					match("true"); 

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7173:21: 'True'
					{
					match("True"); 

					}
					break;

			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_TRUE"

	// $ANTLR start "RULE_FALSE"
	public final void mRULE_FALSE() throws RecognitionException {
		try {
			int _type = RULE_FALSE;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7175:12: ( ( 'false' | 'False' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7175:14: ( 'false' | 'False' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7175:14: ( 'false' | 'False' )
			int alt3=2;
			int LA3_0 = input.LA(1);
			if ( (LA3_0=='f') ) {
				alt3=1;
			}
			else if ( (LA3_0=='F') ) {
				alt3=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 3, 0, input);
				throw nvae;
			}

			switch (alt3) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7175:15: 'false'
					{
					match("false"); 

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7175:23: 'False'
					{
					match("False"); 

					}
					break;

			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_FALSE"

	// $ANTLR start "RULE_ID"
	public final void mRULE_ID() throws RecognitionException {
		try {
			int _type = RULE_ID;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7177:9: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7177:11: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
			{
			if ( (input.LA(1) >= 'A' && input.LA(1) <= 'Z')||input.LA(1)=='_'||(input.LA(1) >= 'a' && input.LA(1) <= 'z') ) {
				input.consume();
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				recover(mse);
				throw mse;
			}
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7177:35: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
			loop4:
			while (true) {
				int alt4=2;
				int LA4_0 = input.LA(1);
				if ( ((LA4_0 >= '0' && LA4_0 <= '9')||(LA4_0 >= 'A' && LA4_0 <= 'Z')||LA4_0=='_'||(LA4_0 >= 'a' && LA4_0 <= 'z')) ) {
					alt4=1;
				}

				switch (alt4) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:
					{
					if ( (input.LA(1) >= '0' && input.LA(1) <= '9')||(input.LA(1) >= 'A' && input.LA(1) <= 'Z')||input.LA(1)=='_'||(input.LA(1) >= 'a' && input.LA(1) <= 'z') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					break loop4;
				}
			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_ID"

	// $ANTLR start "RULE_INT"
	public final void mRULE_INT() throws RecognitionException {
		try {
			int _type = RULE_INT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7179:10: ( ( '0' .. '9' )+ )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7179:12: ( '0' .. '9' )+
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7179:12: ( '0' .. '9' )+
			int cnt5=0;
			loop5:
			while (true) {
				int alt5=2;
				int LA5_0 = input.LA(1);
				if ( ((LA5_0 >= '0' && LA5_0 <= '9')) ) {
					alt5=1;
				}

				switch (alt5) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:
					{
					if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					if ( cnt5 >= 1 ) break loop5;
					EarlyExitException eee = new EarlyExitException(5, input);
					throw eee;
				}
				cnt5++;
			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_INT"

	// $ANTLR start "RULE_NEGINT"
	public final void mRULE_NEGINT() throws RecognitionException {
		try {
			int _type = RULE_NEGINT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7181:13: ( '-' ( '0' .. '9' )+ )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7181:15: '-' ( '0' .. '9' )+
			{
			match('-'); 
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7181:19: ( '0' .. '9' )+
			int cnt6=0;
			loop6:
			while (true) {
				int alt6=2;
				int LA6_0 = input.LA(1);
				if ( ((LA6_0 >= '0' && LA6_0 <= '9')) ) {
					alt6=1;
				}

				switch (alt6) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:
					{
					if ( (input.LA(1) >= '0' && input.LA(1) <= '9') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					if ( cnt6 >= 1 ) break loop6;
					EarlyExitException eee = new EarlyExitException(6, input);
					throw eee;
				}
				cnt6++;
			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_NEGINT"

	// $ANTLR start "RULE_FLOAT_EXP_SUFFIX"
	public final void mRULE_FLOAT_EXP_SUFFIX() throws RecognitionException {
		try {
			int _type = RULE_FLOAT_EXP_SUFFIX;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7183:23: ( RULE_INT ( 'e' | 'E' ) ( '+' | '-' )? RULE_INT )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7183:25: RULE_INT ( 'e' | 'E' ) ( '+' | '-' )? RULE_INT
			{
			mRULE_INT(); 

			if ( input.LA(1)=='E'||input.LA(1)=='e' ) {
				input.consume();
			}
			else {
				MismatchedSetException mse = new MismatchedSetException(null,input);
				recover(mse);
				throw mse;
			}
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7183:44: ( '+' | '-' )?
			int alt7=2;
			int LA7_0 = input.LA(1);
			if ( (LA7_0=='+'||LA7_0=='-') ) {
				alt7=1;
			}
			switch (alt7) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:
					{
					if ( input.LA(1)=='+'||input.LA(1)=='-' ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

			}

			mRULE_INT(); 

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_FLOAT_EXP_SUFFIX"

	// $ANTLR start "RULE_SL_COMMENT"
	public final void mRULE_SL_COMMENT() throws RecognitionException {
		try {
			int _type = RULE_SL_COMMENT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:17: ( ( '//' | '#' ) (~ ( ( '\\n' | '\\r' ) ) )* ( ( '\\r' )? '\\n' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:19: ( '//' | '#' ) (~ ( ( '\\n' | '\\r' ) ) )* ( ( '\\r' )? '\\n' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:19: ( '//' | '#' )
			int alt8=2;
			int LA8_0 = input.LA(1);
			if ( (LA8_0=='/') ) {
				alt8=1;
			}
			else if ( (LA8_0=='#') ) {
				alt8=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 8, 0, input);
				throw nvae;
			}

			switch (alt8) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:20: '//'
					{
					match("//"); 

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:25: '#'
					{
					match('#'); 
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:30: (~ ( ( '\\n' | '\\r' ) ) )*
			loop9:
			while (true) {
				int alt9=2;
				int LA9_0 = input.LA(1);
				if ( ((LA9_0 >= '\u0000' && LA9_0 <= '\t')||(LA9_0 >= '\u000B' && LA9_0 <= '\f')||(LA9_0 >= '\u000E' && LA9_0 <= '\uFFFF')) ) {
					alt9=1;
				}

				switch (alt9) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:
					{
					if ( (input.LA(1) >= '\u0000' && input.LA(1) <= '\t')||(input.LA(1) >= '\u000B' && input.LA(1) <= '\f')||(input.LA(1) >= '\u000E' && input.LA(1) <= '\uFFFF') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

				default :
					break loop9;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:46: ( ( '\\r' )? '\\n' )?
			int alt11=2;
			int LA11_0 = input.LA(1);
			if ( (LA11_0=='\n'||LA11_0=='\r') ) {
				alt11=1;
			}
			switch (alt11) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:47: ( '\\r' )? '\\n'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:47: ( '\\r' )?
					int alt10=2;
					int LA10_0 = input.LA(1);
					if ( (LA10_0=='\r') ) {
						alt10=1;
					}
					switch (alt10) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7185:47: '\\r'
							{
							match('\r'); 
							}
							break;

					}

					match('\n'); 
					}
					break;

			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_SL_COMMENT"

	// $ANTLR start "RULE_ML_COMMENT"
	public final void mRULE_ML_COMMENT() throws RecognitionException {
		try {
			int _type = RULE_ML_COMMENT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:17: ( ( '/*' ( options {greedy=false; } : . )* '*/' | '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\'' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:19: ( '/*' ( options {greedy=false; } : . )* '*/' | '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\'' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:19: ( '/*' ( options {greedy=false; } : . )* '*/' | '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\'' )
			int alt14=2;
			int LA14_0 = input.LA(1);
			if ( (LA14_0=='/') ) {
				alt14=1;
			}
			else if ( (LA14_0=='\'') ) {
				alt14=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 14, 0, input);
				throw nvae;
			}

			switch (alt14) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:20: '/*' ( options {greedy=false; } : . )* '*/'
					{
					match("/*"); 

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:25: ( options {greedy=false; } : . )*
					loop12:
					while (true) {
						int alt12=2;
						int LA12_0 = input.LA(1);
						if ( (LA12_0=='*') ) {
							int LA12_1 = input.LA(2);
							if ( (LA12_1=='/') ) {
								alt12=2;
							}
							else if ( ((LA12_1 >= '\u0000' && LA12_1 <= '.')||(LA12_1 >= '0' && LA12_1 <= '\uFFFF')) ) {
								alt12=1;
							}

						}
						else if ( ((LA12_0 >= '\u0000' && LA12_0 <= ')')||(LA12_0 >= '+' && LA12_0 <= '\uFFFF')) ) {
							alt12=1;
						}

						switch (alt12) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:53: .
							{
							matchAny(); 
							}
							break;

						default :
							break loop12;
						}
					}

					match("*/"); 

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:62: '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\''
					{
					match("'''"); 

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:71: ( options {greedy=false; } : . )*
					loop13:
					while (true) {
						int alt13=2;
						int LA13_0 = input.LA(1);
						if ( (LA13_0=='\'') ) {
							int LA13_1 = input.LA(2);
							if ( (LA13_1=='\'') ) {
								int LA13_3 = input.LA(3);
								if ( (LA13_3=='\'') ) {
									alt13=2;
								}
								else if ( ((LA13_3 >= '\u0000' && LA13_3 <= '&')||(LA13_3 >= '(' && LA13_3 <= '\uFFFF')) ) {
									alt13=1;
								}

							}
							else if ( ((LA13_1 >= '\u0000' && LA13_1 <= '&')||(LA13_1 >= '(' && LA13_1 <= '\uFFFF')) ) {
								alt13=1;
							}

						}
						else if ( ((LA13_0 >= '\u0000' && LA13_0 <= '&')||(LA13_0 >= '(' && LA13_0 <= '\uFFFF')) ) {
							alt13=1;
						}

						switch (alt13) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7187:99: .
							{
							matchAny(); 
							}
							break;

						default :
							break loop13;
						}
					}

					match("'''"); 

					}
					break;

			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_ML_COMMENT"

	// $ANTLR start "RULE_LT_ANNOT"
	public final void mRULE_LT_ANNOT() throws RecognitionException {
		try {
			int _type = RULE_LT_ANNOT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7189:15: ( '\\'' ( RULE_ID )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7189:17: '\\'' ( RULE_ID )?
			{
			match('\''); 
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7189:22: ( RULE_ID )?
			int alt15=2;
			int LA15_0 = input.LA(1);
			if ( ((LA15_0 >= 'A' && LA15_0 <= 'Z')||LA15_0=='_'||(LA15_0 >= 'a' && LA15_0 <= 'z')) ) {
				alt15=1;
			}
			switch (alt15) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7189:22: RULE_ID
					{
					mRULE_ID(); 

					}
					break;

			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_LT_ANNOT"

	// $ANTLR start "RULE_STRING"
	public final void mRULE_STRING() throws RecognitionException {
		try {
			int _type = RULE_STRING;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:13: ( ( '\"' ( '\\\\' . |~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"' | '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:15: ( '\"' ( '\\\\' . |~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"' | '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:15: ( '\"' ( '\\\\' . |~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"' | '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' )
			int alt18=2;
			int LA18_0 = input.LA(1);
			if ( (LA18_0=='\"') ) {
				int LA18_1 = input.LA(2);
				if ( (LA18_1=='\"') ) {
					int LA18_2 = input.LA(3);
					if ( (LA18_2=='\"') ) {
						alt18=2;
					}

					else {
						alt18=1;
					}

				}
				else if ( ((LA18_1 >= '\u0000' && LA18_1 <= '\b')||(LA18_1 >= '\u000B' && LA18_1 <= '\f')||(LA18_1 >= '\u000E' && LA18_1 <= '!')||(LA18_1 >= '#' && LA18_1 <= '\uFFFF')) ) {
					alt18=1;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 18, 1, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 18, 0, input);
				throw nvae;
			}

			switch (alt18) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:16: '\"' ( '\\\\' . |~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"'
					{
					match('\"'); 
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:20: ( '\\\\' . |~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )*
					loop16:
					while (true) {
						int alt16=3;
						int LA16_0 = input.LA(1);
						if ( (LA16_0=='\\') ) {
							alt16=1;
						}
						else if ( ((LA16_0 >= '\u0000' && LA16_0 <= '\b')||(LA16_0 >= '\u000B' && LA16_0 <= '\f')||(LA16_0 >= '\u000E' && LA16_0 <= '!')||(LA16_0 >= '#' && LA16_0 <= '[')||(LA16_0 >= ']' && LA16_0 <= '\uFFFF')) ) {
							alt16=2;
						}

						switch (alt16) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:21: '\\\\' .
							{
							match('\\'); 
							matchAny(); 
							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:28: ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) )
							{
							if ( (input.LA(1) >= '\u0000' && input.LA(1) <= '\b')||(input.LA(1) >= '\u000B' && input.LA(1) <= '\f')||(input.LA(1) >= '\u000E' && input.LA(1) <= '!')||(input.LA(1) >= '#' && input.LA(1) <= '[')||(input.LA(1) >= ']' && input.LA(1) <= '\uFFFF') ) {
								input.consume();
							}
							else {
								MismatchedSetException mse = new MismatchedSetException(null,input);
								recover(mse);
								throw mse;
							}
							}
							break;

						default :
							break loop16;
						}
					}

					match('\"'); 
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:63: '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"'
					{
					match("\"\"\""); 

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:69: ( options {greedy=false; } : . )*
					loop17:
					while (true) {
						int alt17=2;
						int LA17_0 = input.LA(1);
						if ( (LA17_0=='\"') ) {
							int LA17_1 = input.LA(2);
							if ( (LA17_1=='\"') ) {
								int LA17_3 = input.LA(3);
								if ( (LA17_3=='\"') ) {
									alt17=2;
								}
								else if ( ((LA17_3 >= '\u0000' && LA17_3 <= '!')||(LA17_3 >= '#' && LA17_3 <= '\uFFFF')) ) {
									alt17=1;
								}

							}
							else if ( ((LA17_1 >= '\u0000' && LA17_1 <= '!')||(LA17_1 >= '#' && LA17_1 <= '\uFFFF')) ) {
								alt17=1;
							}

						}
						else if ( ((LA17_0 >= '\u0000' && LA17_0 <= '!')||(LA17_0 >= '#' && LA17_0 <= '\uFFFF')) ) {
							alt17=1;
						}

						switch (alt17) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7191:97: .
							{
							matchAny(); 
							}
							break;

						default :
							break loop17;
						}
					}

					match("\"\"\""); 

					}
					break;

			}

			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_STRING"

	// $ANTLR start "RULE_CHAR_LIT"
	public final void mRULE_CHAR_LIT() throws RecognitionException {
		try {
			int _type = RULE_CHAR_LIT;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7193:15: ( '\\'' ( '\\\\' . |~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) ) ) '\\'' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7193:17: '\\'' ( '\\\\' . |~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) ) ) '\\''
			{
			match('\''); 
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7193:22: ( '\\\\' . |~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) ) )
			int alt19=2;
			int LA19_0 = input.LA(1);
			if ( (LA19_0=='\\') ) {
				alt19=1;
			}
			else if ( ((LA19_0 >= '\u0000' && LA19_0 <= '\b')||(LA19_0 >= '\u000B' && LA19_0 <= '\f')||(LA19_0 >= '\u000E' && LA19_0 <= '&')||(LA19_0 >= '(' && LA19_0 <= '[')||(LA19_0 >= ']' && LA19_0 <= '\uFFFF')) ) {
				alt19=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 19, 0, input);
				throw nvae;
			}

			switch (alt19) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7193:23: '\\\\' .
					{
					match('\\'); 
					matchAny(); 
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7193:30: ~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) )
					{
					if ( (input.LA(1) >= '\u0000' && input.LA(1) <= '\b')||(input.LA(1) >= '\u000B' && input.LA(1) <= '\f')||(input.LA(1) >= '\u000E' && input.LA(1) <= '&')||(input.LA(1) >= '(' && input.LA(1) <= '[')||(input.LA(1) >= ']' && input.LA(1) <= '\uFFFF') ) {
						input.consume();
					}
					else {
						MismatchedSetException mse = new MismatchedSetException(null,input);
						recover(mse);
						throw mse;
					}
					}
					break;

			}

			match('\''); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_CHAR_LIT"

	// $ANTLR start "RULE_ANY_OTHER"
	public final void mRULE_ANY_OTHER() throws RecognitionException {
		try {
			int _type = RULE_ANY_OTHER;
			int _channel = DEFAULT_TOKEN_CHANNEL;
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7195:16: ( . )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7195:18: .
			{
			matchAny(); 
			}

			state.type = _type;
			state.channel = _channel;
		}
		finally {
			// do for sure before leaving
		}
	}
	// $ANTLR end "RULE_ANY_OTHER"

	@Override
	public void mTokens() throws RecognitionException {
		// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:8: ( T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | RULE_WS | RULE_TRUE | RULE_FALSE | RULE_ID | RULE_INT | RULE_NEGINT | RULE_FLOAT_EXP_SUFFIX | RULE_SL_COMMENT | RULE_ML_COMMENT | RULE_LT_ANNOT | RULE_STRING | RULE_CHAR_LIT | RULE_ANY_OTHER )
		int alt20=82;
		alt20 = dfa20.predict(input);
		switch (alt20) {
			case 1 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:10: T__17
				{
				mT__17(); 

				}
				break;
			case 2 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:16: T__18
				{
				mT__18(); 

				}
				break;
			case 3 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:22: T__19
				{
				mT__19(); 

				}
				break;
			case 4 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:28: T__20
				{
				mT__20(); 

				}
				break;
			case 5 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:34: T__21
				{
				mT__21(); 

				}
				break;
			case 6 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:40: T__22
				{
				mT__22(); 

				}
				break;
			case 7 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:46: T__23
				{
				mT__23(); 

				}
				break;
			case 8 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:52: T__24
				{
				mT__24(); 

				}
				break;
			case 9 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:58: T__25
				{
				mT__25(); 

				}
				break;
			case 10 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:64: T__26
				{
				mT__26(); 

				}
				break;
			case 11 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:70: T__27
				{
				mT__27(); 

				}
				break;
			case 12 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:76: T__28
				{
				mT__28(); 

				}
				break;
			case 13 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:82: T__29
				{
				mT__29(); 

				}
				break;
			case 14 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:88: T__30
				{
				mT__30(); 

				}
				break;
			case 15 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:94: T__31
				{
				mT__31(); 

				}
				break;
			case 16 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:100: T__32
				{
				mT__32(); 

				}
				break;
			case 17 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:106: T__33
				{
				mT__33(); 

				}
				break;
			case 18 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:112: T__34
				{
				mT__34(); 

				}
				break;
			case 19 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:118: T__35
				{
				mT__35(); 

				}
				break;
			case 20 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:124: T__36
				{
				mT__36(); 

				}
				break;
			case 21 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:130: T__37
				{
				mT__37(); 

				}
				break;
			case 22 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:136: T__38
				{
				mT__38(); 

				}
				break;
			case 23 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:142: T__39
				{
				mT__39(); 

				}
				break;
			case 24 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:148: T__40
				{
				mT__40(); 

				}
				break;
			case 25 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:154: T__41
				{
				mT__41(); 

				}
				break;
			case 26 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:160: T__42
				{
				mT__42(); 

				}
				break;
			case 27 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:166: T__43
				{
				mT__43(); 

				}
				break;
			case 28 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:172: T__44
				{
				mT__44(); 

				}
				break;
			case 29 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:178: T__45
				{
				mT__45(); 

				}
				break;
			case 30 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:184: T__46
				{
				mT__46(); 

				}
				break;
			case 31 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:190: T__47
				{
				mT__47(); 

				}
				break;
			case 32 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:196: T__48
				{
				mT__48(); 

				}
				break;
			case 33 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:202: T__49
				{
				mT__49(); 

				}
				break;
			case 34 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:208: T__50
				{
				mT__50(); 

				}
				break;
			case 35 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:214: T__51
				{
				mT__51(); 

				}
				break;
			case 36 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:220: T__52
				{
				mT__52(); 

				}
				break;
			case 37 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:226: T__53
				{
				mT__53(); 

				}
				break;
			case 38 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:232: T__54
				{
				mT__54(); 

				}
				break;
			case 39 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:238: T__55
				{
				mT__55(); 

				}
				break;
			case 40 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:244: T__56
				{
				mT__56(); 

				}
				break;
			case 41 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:250: T__57
				{
				mT__57(); 

				}
				break;
			case 42 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:256: T__58
				{
				mT__58(); 

				}
				break;
			case 43 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:262: T__59
				{
				mT__59(); 

				}
				break;
			case 44 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:268: T__60
				{
				mT__60(); 

				}
				break;
			case 45 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:274: T__61
				{
				mT__61(); 

				}
				break;
			case 46 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:280: T__62
				{
				mT__62(); 

				}
				break;
			case 47 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:286: T__63
				{
				mT__63(); 

				}
				break;
			case 48 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:292: T__64
				{
				mT__64(); 

				}
				break;
			case 49 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:298: T__65
				{
				mT__65(); 

				}
				break;
			case 50 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:304: T__66
				{
				mT__66(); 

				}
				break;
			case 51 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:310: T__67
				{
				mT__67(); 

				}
				break;
			case 52 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:316: T__68
				{
				mT__68(); 

				}
				break;
			case 53 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:322: T__69
				{
				mT__69(); 

				}
				break;
			case 54 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:328: T__70
				{
				mT__70(); 

				}
				break;
			case 55 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:334: T__71
				{
				mT__71(); 

				}
				break;
			case 56 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:340: T__72
				{
				mT__72(); 

				}
				break;
			case 57 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:346: T__73
				{
				mT__73(); 

				}
				break;
			case 58 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:352: T__74
				{
				mT__74(); 

				}
				break;
			case 59 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:358: T__75
				{
				mT__75(); 

				}
				break;
			case 60 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:364: T__76
				{
				mT__76(); 

				}
				break;
			case 61 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:370: T__77
				{
				mT__77(); 

				}
				break;
			case 62 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:376: T__78
				{
				mT__78(); 

				}
				break;
			case 63 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:382: T__79
				{
				mT__79(); 

				}
				break;
			case 64 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:388: T__80
				{
				mT__80(); 

				}
				break;
			case 65 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:394: T__81
				{
				mT__81(); 

				}
				break;
			case 66 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:400: T__82
				{
				mT__82(); 

				}
				break;
			case 67 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:406: T__83
				{
				mT__83(); 

				}
				break;
			case 68 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:412: T__84
				{
				mT__84(); 

				}
				break;
			case 69 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:418: T__85
				{
				mT__85(); 

				}
				break;
			case 70 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:424: RULE_WS
				{
				mRULE_WS(); 

				}
				break;
			case 71 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:432: RULE_TRUE
				{
				mRULE_TRUE(); 

				}
				break;
			case 72 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:442: RULE_FALSE
				{
				mRULE_FALSE(); 

				}
				break;
			case 73 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:453: RULE_ID
				{
				mRULE_ID(); 

				}
				break;
			case 74 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:461: RULE_INT
				{
				mRULE_INT(); 

				}
				break;
			case 75 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:470: RULE_NEGINT
				{
				mRULE_NEGINT(); 

				}
				break;
			case 76 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:482: RULE_FLOAT_EXP_SUFFIX
				{
				mRULE_FLOAT_EXP_SUFFIX(); 

				}
				break;
			case 77 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:504: RULE_SL_COMMENT
				{
				mRULE_SL_COMMENT(); 

				}
				break;
			case 78 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:520: RULE_ML_COMMENT
				{
				mRULE_ML_COMMENT(); 

				}
				break;
			case 79 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:536: RULE_LT_ANNOT
				{
				mRULE_LT_ANNOT(); 

				}
				break;
			case 80 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:550: RULE_STRING
				{
				mRULE_STRING(); 

				}
				break;
			case 81 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:562: RULE_CHAR_LIT
				{
				mRULE_CHAR_LIT(); 

				}
				break;
			case 82 :
				// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1:576: RULE_ANY_OTHER
				{
				mRULE_ANY_OTHER(); 

				}
				break;

		}
	}


	protected DFA20 dfa20 = new DFA20(this);
	static final String DFA20_eotS =
		"\7\uffff\1\71\1\uffff\1\76\1\101\2\uffff\1\105\2\uffff\2\111\1\uffff\1"+
		"\114\2\uffff\1\121\20\111\1\162\1\uffff\1\61\1\uffff\2\111\1\uffff\1\170"+
		"\1\uffff\1\61\27\uffff\1\111\1\uffff\1\111\2\uffff\1\176\4\uffff\2\111"+
		"\1\u0081\1\u0082\33\111\5\uffff\2\111\1\uffff\1\170\2\uffff\1\111\1\u00a5"+
		"\1\uffff\2\111\2\uffff\20\111\1\u00b8\20\111\1\u00cb\1\uffff\6\111\1\u00d2"+
		"\7\111\1\u00da\1\111\1\u00dc\1\111\1\uffff\15\111\1\u00ed\1\u00ee\1\111"+
		"\1\u00ee\1\111\1\uffff\1\111\1\u00f2\1\u00f3\3\111\1\uffff\1\u00f7\3\111"+
		"\1\u00fb\2\111\1\uffff\1\111\1\uffff\11\111\1\u0109\3\111\1\u010d\1\111"+
		"\1\u010f\2\uffff\1\111\1\u00f7\1\u0111\2\uffff\3\111\1\uffff\1\111\1\u0116"+
		"\1\111\1\uffff\2\111\1\u011a\2\111\1\u011d\3\111\1\u0121\3\111\1\uffff"+
		"\3\111\1\uffff\1\u0128\1\uffff\1\111\1\uffff\1\111\1\u012b\1\111\1\u012d"+
		"\1\uffff\1\u012e\1\111\1\u0130\1\uffff\1\u0131\1\111\1\uffff\2\111\1\u0135"+
		"\1\uffff\1\111\1\u0137\3\111\1\u013b\1\uffff\1\u013d\1\u013e\1\uffff\1"+
		"\111\2\uffff\1\111\2\uffff\1\u0141\1\u0142\1\u0143\1\uffff\1\u0144\1\uffff"+
		"\1\u0145\1\111\1\u0147\4\uffff\1\u0148\1\111\5\uffff\1\111\2\uffff\1\111"+
		"\1\u014c\1\u014d\2\uffff";
	static final String DFA20_eofS =
		"\u014e\uffff";
	static final String DFA20_minS =
		"\1\0\6\uffff\1\60\1\uffff\1\52\1\72\2\uffff\1\175\2\uffff\1\117\1\124"+
		"\1\uffff\1\0\2\uffff\1\60\1\143\1\157\1\145\1\170\1\141\1\151\1\155\1"+
		"\157\1\141\1\145\1\165\1\150\2\145\1\141\1\151\1\75\1\uffff\1\76\1\uffff"+
		"\1\162\1\141\1\uffff\1\60\1\uffff\1\0\27\uffff\1\116\1\uffff\1\120\2\uffff"+
		"\1\47\4\uffff\2\164\2\60\1\156\1\141\1\164\1\144\1\157\1\154\1\163\1\160"+
		"\1\151\1\147\1\151\1\164\1\144\1\164\1\167\1\164\1\171\1\145\1\142\1\141"+
		"\1\162\1\165\1\141\1\162\1\155\1\165\1\144\5\uffff\1\165\1\154\1\uffff"+
		"\1\60\2\uffff\1\105\1\60\1\uffff\1\151\1\145\2\uffff\1\163\1\144\2\145"+
		"\1\155\1\163\1\164\1\157\1\164\1\165\1\145\1\151\1\156\1\150\1\145\1\141"+
		"\1\60\1\160\1\163\1\141\1\166\1\154\1\143\1\145\1\151\1\164\1\162\1\147"+
		"\2\145\1\164\1\145\1\163\1\60\1\uffff\1\157\1\162\1\164\1\154\1\156\1"+
		"\162\1\60\1\145\1\157\1\162\1\151\1\164\1\162\1\143\1\60\1\157\1\60\1"+
		"\142\1\uffff\1\165\1\151\1\155\1\141\1\151\3\164\1\141\1\144\1\164\2\145"+
		"\2\60\1\150\1\60\1\145\1\uffff\1\156\2\60\1\151\1\144\1\141\1\uffff\1"+
		"\60\1\162\1\164\1\141\1\60\1\154\1\141\1\uffff\1\144\1\uffff\1\154\1\151"+
		"\1\164\1\143\1\142\1\164\1\143\2\151\1\60\1\154\1\157\1\165\1\60\1\164"+
		"\1\60\2\uffff\1\157\2\60\2\uffff\1\156\1\163\1\164\1\uffff\1\171\1\60"+
		"\1\154\1\uffff\1\145\1\154\1\60\1\145\1\157\1\60\1\141\1\154\1\145\1\60"+
		"\1\157\1\162\1\155\1\uffff\1\151\1\167\1\160\1\uffff\1\60\1\uffff\1\146"+
		"\1\uffff\1\145\1\60\1\145\1\60\1\uffff\1\60\1\141\1\60\1\uffff\1\60\1"+
		"\156\1\uffff\1\154\1\145\1\60\1\uffff\1\156\1\60\1\145\1\172\1\156\1\60"+
		"\1\uffff\1\50\1\60\1\uffff\1\144\2\uffff\1\166\2\uffff\3\60\1\uffff\1"+
		"\60\1\uffff\1\60\1\145\1\60\4\uffff\1\60\1\145\5\uffff\1\162\2\uffff\1"+
		"\144\2\60\2\uffff";
	static final String DFA20_maxS =
		"\1\uffff\6\uffff\1\76\1\uffff\1\57\1\134\2\uffff\1\175\2\uffff\1\117\1"+
		"\124\1\uffff\1\uffff\2\uffff\1\172\1\164\1\157\1\145\1\170\1\162\1\151"+
		"\1\156\1\157\1\165\1\145\2\165\1\145\1\164\1\162\1\151\1\75\1\uffff\1"+
		"\76\1\uffff\1\162\1\141\1\uffff\1\145\1\uffff\1\uffff\27\uffff\1\116\1"+
		"\uffff\1\120\2\uffff\1\47\4\uffff\2\164\2\172\1\156\1\141\1\164\1\144"+
		"\1\157\1\154\1\163\1\160\1\164\1\147\1\151\1\164\1\144\1\164\1\167\1\164"+
		"\1\171\1\151\1\142\1\163\1\162\1\165\1\141\1\162\1\155\1\165\1\144\5\uffff"+
		"\1\165\1\154\1\uffff\1\145\2\uffff\1\105\1\172\1\uffff\1\151\1\145\2\uffff"+
		"\1\163\1\144\2\145\1\155\1\163\1\164\1\157\1\164\1\165\1\145\1\151\1\156"+
		"\1\150\1\145\1\141\1\172\1\160\1\163\1\141\1\166\2\154\1\145\1\151\2\164"+
		"\1\147\2\145\1\164\1\145\1\163\1\172\1\uffff\1\157\1\162\1\164\1\154\1"+
		"\156\1\162\1\172\1\145\1\157\1\162\1\151\1\164\1\162\1\143\1\172\1\157"+
		"\1\172\1\164\1\uffff\1\165\1\151\1\155\1\141\1\151\3\164\1\141\1\144\1"+
		"\164\2\145\2\172\1\150\1\172\1\145\1\uffff\1\156\2\172\1\151\1\144\1\141"+
		"\1\uffff\1\172\1\162\1\164\1\141\1\172\1\154\1\141\1\uffff\1\144\1\uffff"+
		"\1\154\1\151\1\164\1\143\1\142\1\164\1\143\1\157\1\151\1\172\1\154\1\157"+
		"\1\165\1\172\1\164\1\172\2\uffff\1\157\2\172\2\uffff\1\156\1\163\1\164"+
		"\1\uffff\1\171\1\172\1\154\1\uffff\1\145\1\154\1\172\1\145\1\157\1\172"+
		"\1\141\1\154\1\145\1\172\1\157\1\162\1\155\1\uffff\1\151\1\167\1\160\1"+
		"\uffff\1\172\1\uffff\1\146\1\uffff\1\145\1\172\1\145\1\172\1\uffff\1\172"+
		"\1\141\1\172\1\uffff\1\172\1\156\1\uffff\1\154\1\145\1\172\1\uffff\1\156"+
		"\1\172\1\145\1\172\1\156\1\172\1\uffff\2\172\1\uffff\1\144\2\uffff\1\166"+
		"\2\uffff\3\172\1\uffff\1\172\1\uffff\1\172\1\145\1\172\4\uffff\1\172\1"+
		"\145\5\uffff\1\162\2\uffff\1\144\2\172\2\uffff";
	static final String DFA20_acceptS =
		"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\uffff\1\11\2\uffff\1\16\1\17\1\uffff"+
		"\1\22\1\23\2\uffff\1\26\1\uffff\1\30\1\31\22\uffff\1\104\1\uffff\1\106"+
		"\2\uffff\1\111\1\uffff\1\115\1\uffff\1\122\1\1\1\2\1\3\1\4\1\5\1\6\1\10"+
		"\1\7\1\113\1\11\1\115\1\116\1\12\1\14\1\15\1\13\1\16\1\17\1\21\1\20\1"+
		"\22\1\23\1\uffff\1\111\1\uffff\1\26\1\27\1\uffff\1\121\1\30\1\31\1\32"+
		"\37\uffff\1\103\1\102\1\104\1\105\1\106\2\uffff\1\112\1\uffff\1\114\1"+
		"\120\2\uffff\1\117\2\uffff\1\35\1\36\42\uffff\1\25\22\uffff\1\57\22\uffff"+
		"\1\24\6\uffff\1\43\7\uffff\1\52\1\uffff\1\54\20\uffff\1\76\1\107\3\uffff"+
		"\1\34\1\37\3\uffff\1\110\3\uffff\1\47\15\uffff\1\70\3\uffff\1\74\1\uffff"+
		"\1\77\1\uffff\1\33\4\uffff\1\45\3\uffff\1\53\2\uffff\1\60\3\uffff\1\64"+
		"\6\uffff\1\75\2\uffff\1\41\1\uffff\1\44\1\46\1\uffff\1\51\1\55\3\uffff"+
		"\1\63\1\uffff\1\66\3\uffff\1\73\1\101\1\100\1\40\2\uffff\1\56\1\61\1\62"+
		"\1\65\1\67\1\uffff\1\72\1\42\3\uffff\1\71\1\50";
	static final String DFA20_specialS =
		"\1\0\22\uffff\1\2\34\uffff\1\1\u011d\uffff}>";
	static final String[] DFA20_transitionS = {
			"\11\61\2\52\2\61\1\52\22\61\1\52\1\61\1\60\1\57\1\61\1\1\1\61\1\23\1"+
			"\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\12\56\1\12\1\13\1\14\1\15\1\16\1\61"+
			"\1\17\5\55\1\54\7\55\1\20\4\55\1\21\1\53\6\55\1\22\1\24\1\25\1\61\1\26"+
			"\1\61\1\27\1\55\1\30\1\31\1\32\1\33\1\55\1\34\1\35\2\55\1\36\1\37\1\40"+
			"\1\41\1\42\1\55\1\43\1\44\1\45\2\55\1\46\3\55\1\47\1\61\1\50\1\51\uff81"+
			"\61",
			"",
			"",
			"",
			"",
			"",
			"",
			"\12\72\4\uffff\1\70",
			"",
			"\1\75\4\uffff\1\74",
			"\1\77\41\uffff\1\100",
			"",
			"",
			"\1\104",
			"",
			"",
			"\1\110",
			"\1\112",
			"",
			"\11\116\2\uffff\2\116\1\uffff\31\116\1\75\31\116\32\115\4\116\1\115"+
			"\1\116\32\115\uff85\116",
			"",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\122\2\uffff\1\123\14\uffff\1\124\1\125",
			"\1\126",
			"\1\127",
			"\1\130",
			"\1\133\3\uffff\1\131\14\uffff\1\132",
			"\1\134",
			"\1\135\1\136",
			"\1\137",
			"\1\140\3\uffff\1\141\11\uffff\1\142\5\uffff\1\143",
			"\1\144",
			"\1\145",
			"\1\146\11\uffff\1\147\2\uffff\1\150",
			"\1\151",
			"\1\152\2\uffff\1\153\13\uffff\1\154",
			"\1\155\7\uffff\1\156\10\uffff\1\157",
			"\1\160",
			"\1\161",
			"",
			"\1\164",
			"",
			"\1\166",
			"\1\167",
			"",
			"\12\171\13\uffff\1\172\37\uffff\1\172",
			"",
			"\11\173\2\uffff\2\173\1\uffff\ufff2\173",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"",
			"\1\174",
			"",
			"\1\175",
			"",
			"",
			"\1\116",
			"",
			"",
			"",
			"",
			"\1\177",
			"\1\u0080",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0083",
			"\1\u0084",
			"\1\u0085",
			"\1\u0086",
			"\1\u0087",
			"\1\u0088",
			"\1\u0089",
			"\1\u008a",
			"\1\u008b\6\uffff\1\u008c\3\uffff\1\u008d",
			"\1\u008e",
			"\1\u008f",
			"\1\u0090",
			"\1\u0091",
			"\1\u0092",
			"\1\u0093",
			"\1\u0094",
			"\1\u0095",
			"\1\u0096\3\uffff\1\u0097",
			"\1\u0098",
			"\1\u0099\21\uffff\1\u009a",
			"\1\u009b",
			"\1\u009c",
			"\1\u009d",
			"\1\u009e",
			"\1\u009f",
			"\1\u00a0",
			"\1\u00a1",
			"",
			"",
			"",
			"",
			"",
			"\1\u00a2",
			"\1\u00a3",
			"",
			"\12\171\13\uffff\1\172\37\uffff\1\172",
			"",
			"",
			"\1\u00a4",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\1\u00a6",
			"\1\u00a7",
			"",
			"",
			"\1\u00a8",
			"\1\u00a9",
			"\1\u00aa",
			"\1\u00ab",
			"\1\u00ac",
			"\1\u00ad",
			"\1\u00ae",
			"\1\u00af",
			"\1\u00b0",
			"\1\u00b1",
			"\1\u00b2",
			"\1\u00b3",
			"\1\u00b4",
			"\1\u00b5",
			"\1\u00b6",
			"\1\u00b7",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00b9",
			"\1\u00ba",
			"\1\u00bb",
			"\1\u00bc",
			"\1\u00bd",
			"\1\u00be\10\uffff\1\u00bf",
			"\1\u00c0",
			"\1\u00c1",
			"\1\u00c2",
			"\1\u00c3\1\uffff\1\u00c4",
			"\1\u00c5",
			"\1\u00c6",
			"\1\u00c7",
			"\1\u00c8",
			"\1\u00c9",
			"\1\u00ca",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\1\u00cc",
			"\1\u00cd",
			"\1\u00ce",
			"\1\u00cf",
			"\1\u00d0",
			"\1\u00d1",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00d3",
			"\1\u00d4",
			"\1\u00d5",
			"\1\u00d6",
			"\1\u00d7",
			"\1\u00d8",
			"\1\u00d9",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00db",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00dd\21\uffff\1\u00de",
			"",
			"\1\u00df",
			"\1\u00e0",
			"\1\u00e1",
			"\1\u00e2",
			"\1\u00e3",
			"\1\u00e4",
			"\1\u00e5",
			"\1\u00e6",
			"\1\u00e7",
			"\1\u00e8",
			"\1\u00e9",
			"\1\u00ea",
			"\1\u00eb",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\21\111\1\u00ec\10\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00ef",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00f0",
			"",
			"\1\u00f1",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00f4",
			"\1\u00f5",
			"\1\u00f6",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00f8",
			"\1\u00f9",
			"\1\u00fa",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u00fc",
			"\1\u00fd",
			"",
			"\1\u00fe",
			"",
			"\1\u00ff",
			"\1\u0100",
			"\1\u0101",
			"\1\u0102",
			"\1\u0103",
			"\1\u0104",
			"\1\u0105",
			"\1\u0106\5\uffff\1\u0107",
			"\1\u0108",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u010a",
			"\1\u010b",
			"\1\u010c",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u010e",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"",
			"\1\u0110",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"",
			"\1\u0112",
			"\1\u0113",
			"\1\u0114",
			"",
			"\1\u0115",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0117",
			"",
			"\1\u0118",
			"\1\u0119",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u011b",
			"\1\u011c",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u011e",
			"\1\u011f",
			"\1\u0120",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0122",
			"\1\u0123",
			"\1\u0124",
			"",
			"\1\u0125",
			"\1\u0126",
			"\1\u0127",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\1\u0129",
			"",
			"\1\u012a",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u012c",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u012f",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0132",
			"",
			"\1\u0133",
			"\1\u0134",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\1\u0136",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0138",
			"\1\u0139",
			"\1\u013a",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\1\u013c\7\uffff\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\1\u013f",
			"",
			"",
			"\1\u0140",
			"",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0146",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			"",
			"",
			"",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\1\u0149",
			"",
			"",
			"",
			"",
			"",
			"\1\u014a",
			"",
			"",
			"\1\u014b",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"\12\111\7\uffff\32\111\4\uffff\1\111\1\uffff\32\111",
			"",
			""
	};

	static final short[] DFA20_eot = DFA.unpackEncodedString(DFA20_eotS);
	static final short[] DFA20_eof = DFA.unpackEncodedString(DFA20_eofS);
	static final char[] DFA20_min = DFA.unpackEncodedStringToUnsignedChars(DFA20_minS);
	static final char[] DFA20_max = DFA.unpackEncodedStringToUnsignedChars(DFA20_maxS);
	static final short[] DFA20_accept = DFA.unpackEncodedString(DFA20_acceptS);
	static final short[] DFA20_special = DFA.unpackEncodedString(DFA20_specialS);
	static final short[][] DFA20_transition;

	static {
		int numStates = DFA20_transitionS.length;
		DFA20_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA20_transition[i] = DFA.unpackEncodedString(DFA20_transitionS[i]);
		}
	}

	protected class DFA20 extends DFA {

		public DFA20(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 20;
			this.eot = DFA20_eot;
			this.eof = DFA20_eof;
			this.min = DFA20_min;
			this.max = DFA20_max;
			this.accept = DFA20_accept;
			this.special = DFA20_special;
			this.transition = DFA20_transition;
		}
		@Override
		public String getDescription() {
			return "1:1: Tokens : ( T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | RULE_WS | RULE_TRUE | RULE_FALSE | RULE_ID | RULE_INT | RULE_NEGINT | RULE_FLOAT_EXP_SUFFIX | RULE_SL_COMMENT | RULE_ML_COMMENT | RULE_LT_ANNOT | RULE_STRING | RULE_CHAR_LIT | RULE_ANY_OTHER );";
		}
		@Override
		public int specialStateTransition(int s, IntStream _input) throws NoViableAltException {
			IntStream input = _input;
			int _s = s;
			switch ( s ) {
					case 0 : 
						int LA20_0 = input.LA(1);
						s = -1;
						if ( (LA20_0=='%') ) {s = 1;}
						else if ( (LA20_0=='(') ) {s = 2;}
						else if ( (LA20_0==')') ) {s = 3;}
						else if ( (LA20_0=='*') ) {s = 4;}
						else if ( (LA20_0=='+') ) {s = 5;}
						else if ( (LA20_0==',') ) {s = 6;}
						else if ( (LA20_0=='-') ) {s = 7;}
						else if ( (LA20_0=='.') ) {s = 8;}
						else if ( (LA20_0=='/') ) {s = 9;}
						else if ( (LA20_0==':') ) {s = 10;}
						else if ( (LA20_0==';') ) {s = 11;}
						else if ( (LA20_0=='<') ) {s = 12;}
						else if ( (LA20_0=='=') ) {s = 13;}
						else if ( (LA20_0=='>') ) {s = 14;}
						else if ( (LA20_0=='@') ) {s = 15;}
						else if ( (LA20_0=='N') ) {s = 16;}
						else if ( (LA20_0=='S') ) {s = 17;}
						else if ( (LA20_0=='[') ) {s = 18;}
						else if ( (LA20_0=='\'') ) {s = 19;}
						else if ( (LA20_0=='\\') ) {s = 20;}
						else if ( (LA20_0==']') ) {s = 21;}
						else if ( (LA20_0=='_') ) {s = 22;}
						else if ( (LA20_0=='a') ) {s = 23;}
						else if ( (LA20_0=='c') ) {s = 24;}
						else if ( (LA20_0=='d') ) {s = 25;}
						else if ( (LA20_0=='e') ) {s = 26;}
						else if ( (LA20_0=='f') ) {s = 27;}
						else if ( (LA20_0=='h') ) {s = 28;}
						else if ( (LA20_0=='i') ) {s = 29;}
						else if ( (LA20_0=='l') ) {s = 30;}
						else if ( (LA20_0=='m') ) {s = 31;}
						else if ( (LA20_0=='n') ) {s = 32;}
						else if ( (LA20_0=='o') ) {s = 33;}
						else if ( (LA20_0=='p') ) {s = 34;}
						else if ( (LA20_0=='r') ) {s = 35;}
						else if ( (LA20_0=='s') ) {s = 36;}
						else if ( (LA20_0=='t') ) {s = 37;}
						else if ( (LA20_0=='w') ) {s = 38;}
						else if ( (LA20_0=='{') ) {s = 39;}
						else if ( (LA20_0=='}') ) {s = 40;}
						else if ( (LA20_0=='~') ) {s = 41;}
						else if ( ((LA20_0 >= '\t' && LA20_0 <= '\n')||LA20_0=='\r'||LA20_0==' ') ) {s = 42;}
						else if ( (LA20_0=='T') ) {s = 43;}
						else if ( (LA20_0=='F') ) {s = 44;}
						else if ( ((LA20_0 >= 'A' && LA20_0 <= 'E')||(LA20_0 >= 'G' && LA20_0 <= 'M')||(LA20_0 >= 'O' && LA20_0 <= 'R')||(LA20_0 >= 'U' && LA20_0 <= 'Z')||LA20_0=='b'||LA20_0=='g'||(LA20_0 >= 'j' && LA20_0 <= 'k')||LA20_0=='q'||(LA20_0 >= 'u' && LA20_0 <= 'v')||(LA20_0 >= 'x' && LA20_0 <= 'z')) ) {s = 45;}
						else if ( ((LA20_0 >= '0' && LA20_0 <= '9')) ) {s = 46;}
						else if ( (LA20_0=='#') ) {s = 47;}
						else if ( (LA20_0=='\"') ) {s = 48;}
						else if ( ((LA20_0 >= '\u0000' && LA20_0 <= '\b')||(LA20_0 >= '\u000B' && LA20_0 <= '\f')||(LA20_0 >= '\u000E' && LA20_0 <= '\u001F')||LA20_0=='!'||LA20_0=='$'||LA20_0=='&'||LA20_0=='?'||LA20_0=='^'||LA20_0=='`'||LA20_0=='|'||(LA20_0 >= '\u007F' && LA20_0 <= '\uFFFF')) ) {s = 49;}
						if ( s>=0 ) return s;
						break;

					case 1 : 
						int LA20_48 = input.LA(1);
						s = -1;
						if ( ((LA20_48 >= '\u0000' && LA20_48 <= '\b')||(LA20_48 >= '\u000B' && LA20_48 <= '\f')||(LA20_48 >= '\u000E' && LA20_48 <= '\uFFFF')) ) {s = 123;}
						else s = 49;
						if ( s>=0 ) return s;
						break;

					case 2 : 
						int LA20_19 = input.LA(1);
						s = -1;
						if ( (LA20_19=='\'') ) {s = 61;}
						else if ( ((LA20_19 >= 'A' && LA20_19 <= 'Z')||LA20_19=='_'||(LA20_19 >= 'a' && LA20_19 <= 'z')) ) {s = 77;}
						else if ( ((LA20_19 >= '\u0000' && LA20_19 <= '\b')||(LA20_19 >= '\u000B' && LA20_19 <= '\f')||(LA20_19 >= '\u000E' && LA20_19 <= '&')||(LA20_19 >= '(' && LA20_19 <= '@')||(LA20_19 >= '[' && LA20_19 <= '^')||LA20_19=='`'||(LA20_19 >= '{' && LA20_19 <= '\uFFFF')) ) {s = 78;}
						else s = 76;
						if ( s>=0 ) return s;
						break;
			}
			NoViableAltException nvae =
				new NoViableAltException(getDescription(), 20, _s, input);
			error(nvae);
			throw nvae;
		}
	}

}
