// $ANTLR 3.5 C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g 2022-12-01 20:48:48

package org.lflang.parser.antlr.internal;

import org.eclipse.xtext.*;
import org.eclipse.xtext.parser.*;
import org.eclipse.xtext.parser.impl.*;
import org.eclipse.emf.ecore.util.EcoreUtil;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.common.util.Enumerator;
import org.eclipse.xtext.parser.antlr.AbstractInternalAntlrParser;
import org.eclipse.xtext.parser.antlr.XtextTokenStream;
import org.eclipse.xtext.parser.antlr.XtextTokenStream.HiddenTokens;
import org.eclipse.xtext.parser.antlr.AntlrDatatypeRuleToken;
import org.lflang.services.LFGrammarAccess;



import org.antlr.runtime.*;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

@SuppressWarnings("all")
public class InternalLFParser extends AbstractInternalAntlrParser {
	public static final String[] tokenNames = new String[] {
		"<invalid>", "<EOR>", "<DOWN>", "<UP>", "RULE_ANY_OTHER", "RULE_CHAR_LIT", 
		"RULE_FALSE", "RULE_FLOAT_EXP_SUFFIX", "RULE_ID", "RULE_INT", "RULE_LT_ANNOT", 
		"RULE_ML_COMMENT", "RULE_NEGINT", "RULE_SL_COMMENT", "RULE_STRING", "RULE_TRUE", 
		"RULE_WS", "'%'", "'('", "')'", "'*'", "'+'", "','", "'-'", "'->'", "'.'", 
		"'/'", "':'", "'::'", "':\\\\'", "';'", "'<'", "'='", "'=}'", "'>'", "'@'", 
		"'NONE'", "'STP'", "'['", "'\\''", "'\\\\'", "']'", "'_'", "'action'", 
		"'after'", "'as'", "'at'", "'const'", "'deadline'", "'extends'", "'federated'", 
		"'from'", "'history'", "'import'", "'initial'", "'input'", "'interleaved'", 
		"'logical'", "'main'", "'method'", "'mode'", "'mutable'", "'mutation'", 
		"'new'", "'output'", "'physical'", "'preamble'", "'private'", "'public'", 
		"'reaction'", "'reactor'", "'realtime'", "'reset'", "'serializer'", "'shutdown'", 
		"'startup'", "'state'", "'target'", "'time'", "'timer'", "'widthof'", 
		"'widthof('", "'{'", "'{='", "'}'", "'~>'"
	};
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
	public AbstractInternalAntlrParser[] getDelegates() {
		return new AbstractInternalAntlrParser[] {};
	}

	// delegators


	public InternalLFParser(TokenStream input) {
		this(input, new RecognizerSharedState());
	}
	public InternalLFParser(TokenStream input, RecognizerSharedState state) {
		super(input, state);
	}

	@Override public String[] getTokenNames() { return InternalLFParser.tokenNames; }
	@Override public String getGrammarFileName() { return "C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g"; }



	 	private LFGrammarAccess grammarAccess;

	    public InternalLFParser(TokenStream input, LFGrammarAccess grammarAccess) {
	        this(input);
	        this.grammarAccess = grammarAccess;
	        registerRules(grammarAccess.getGrammar());
	    }

	    @Override
	    protected String getFirstRuleName() {
	    	return "Model";
	   	}

	   	@Override
	   	protected LFGrammarAccess getGrammarAccess() {
	   		return grammarAccess;
	   	}




	// $ANTLR start "entryRuleModel"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:65:1: entryRuleModel returns [EObject current=null] :iv_ruleModel= ruleModel EOF ;
	public final EObject entryRuleModel() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleModel =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:65:46: (iv_ruleModel= ruleModel EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:66:2: iv_ruleModel= ruleModel EOF
			{
			 newCompositeNode(grammarAccess.getModelRule()); 
			pushFollow(FOLLOW_ruleModel_in_entryRuleModel66);
			iv_ruleModel=ruleModel();
			state._fsp--;

			 current =iv_ruleModel; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleModel72); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleModel"



	// $ANTLR start "ruleModel"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:72:1: ruleModel returns [EObject current=null] : ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ ) ;
	public final EObject ruleModel() throws RecognitionException {
		EObject current = null;


		EObject lv_target_0_0 =null;
		EObject lv_imports_1_0 =null;
		EObject lv_preambles_2_0 =null;
		EObject lv_reactors_3_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:78:2: ( ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:79:2: ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:79:2: ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:80:3: ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:80:3: ( (lv_target_0_0= ruleTargetDecl ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:81:4: (lv_target_0_0= ruleTargetDecl )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:81:4: (lv_target_0_0= ruleTargetDecl )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:82:5: lv_target_0_0= ruleTargetDecl
			{

								newCompositeNode(grammarAccess.getModelAccess().getTargetTargetDeclParserRuleCall_0_0());
							
			pushFollow(FOLLOW_ruleTargetDecl_in_ruleModel118);
			lv_target_0_0=ruleTargetDecl();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getModelRule());
								}
								set(
									current,
									"target",
									lv_target_0_0,
									"org.lflang.LF.TargetDecl");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:99:3: ( (lv_imports_1_0= ruleImport ) )*
			loop1:
			while (true) {
				int alt1=2;
				int LA1_0 = input.LA(1);
				if ( (LA1_0==53) ) {
					alt1=1;
				}

				switch (alt1) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:100:4: (lv_imports_1_0= ruleImport )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:100:4: (lv_imports_1_0= ruleImport )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:101:5: lv_imports_1_0= ruleImport
					{

										newCompositeNode(grammarAccess.getModelAccess().getImportsImportParserRuleCall_1_0());
									
					pushFollow(FOLLOW_ruleImport_in_ruleModel156);
					lv_imports_1_0=ruleImport();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getModelRule());
										}
										add(
											current,
											"imports",
											lv_imports_1_0,
											"org.lflang.LF.Import");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop1;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:118:3: ( (lv_preambles_2_0= rulePreamble ) )*
			loop2:
			while (true) {
				int alt2=2;
				int LA2_0 = input.LA(1);
				if ( (LA2_0==36||(LA2_0 >= 66 && LA2_0 <= 68)) ) {
					alt2=1;
				}

				switch (alt2) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:119:4: (lv_preambles_2_0= rulePreamble )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:119:4: (lv_preambles_2_0= rulePreamble )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:120:5: lv_preambles_2_0= rulePreamble
					{

										newCompositeNode(grammarAccess.getModelAccess().getPreamblesPreambleParserRuleCall_2_0());
									
					pushFollow(FOLLOW_rulePreamble_in_ruleModel195);
					lv_preambles_2_0=rulePreamble();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getModelRule());
										}
										add(
											current,
											"preambles",
											lv_preambles_2_0,
											"org.lflang.LF.Preamble");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop2;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:137:3: ( (lv_reactors_3_0= ruleReactor ) )+
			int cnt3=0;
			loop3:
			while (true) {
				int alt3=2;
				int LA3_0 = input.LA(1);
				if ( (LA3_0==35||LA3_0==50||LA3_0==58||(LA3_0 >= 70 && LA3_0 <= 71)) ) {
					alt3=1;
				}

				switch (alt3) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:138:4: (lv_reactors_3_0= ruleReactor )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:138:4: (lv_reactors_3_0= ruleReactor )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:139:5: lv_reactors_3_0= ruleReactor
					{

										newCompositeNode(grammarAccess.getModelAccess().getReactorsReactorParserRuleCall_3_0());
									
					pushFollow(FOLLOW_ruleReactor_in_ruleModel234);
					lv_reactors_3_0=ruleReactor();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getModelRule());
										}
										add(
											current,
											"reactors",
											lv_reactors_3_0,
											"org.lflang.LF.Reactor");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					if ( cnt3 >= 1 ) break loop3;
					EarlyExitException eee = new EarlyExitException(3, input);
					throw eee;
				}
				cnt3++;
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleModel"



	// $ANTLR start "entryRuleImport"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:160:1: entryRuleImport returns [EObject current=null] :iv_ruleImport= ruleImport EOF ;
	public final EObject entryRuleImport() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleImport =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:160:47: (iv_ruleImport= ruleImport EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:161:2: iv_ruleImport= ruleImport EOF
			{
			 newCompositeNode(grammarAccess.getImportRule()); 
			pushFollow(FOLLOW_ruleImport_in_entryRuleImport272);
			iv_ruleImport=ruleImport();
			state._fsp--;

			 current =iv_ruleImport; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleImport278); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleImport"



	// $ANTLR start "ruleImport"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:167:1: ruleImport returns [EObject current=null] : (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? ) ;
	public final EObject ruleImport() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_2=null;
		Token otherlv_4=null;
		Token lv_importURI_5_0=null;
		Token otherlv_6=null;
		EObject lv_reactorClasses_1_0 =null;
		EObject lv_reactorClasses_3_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:173:2: ( (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:174:2: (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:174:2: (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:175:3: otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )?
			{
			otherlv_0=(Token)match(input,53,FOLLOW_53_in_ruleImport307); 

						newLeafNode(otherlv_0, grammarAccess.getImportAccess().getImportKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:179:3: ( (lv_reactorClasses_1_0= ruleImportedReactor ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:180:4: (lv_reactorClasses_1_0= ruleImportedReactor )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:180:4: (lv_reactorClasses_1_0= ruleImportedReactor )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:181:5: lv_reactorClasses_1_0= ruleImportedReactor
			{

								newCompositeNode(grammarAccess.getImportAccess().getReactorClassesImportedReactorParserRuleCall_1_0());
							
			pushFollow(FOLLOW_ruleImportedReactor_in_ruleImport334);
			lv_reactorClasses_1_0=ruleImportedReactor();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getImportRule());
								}
								add(
									current,
									"reactorClasses",
									lv_reactorClasses_1_0,
									"org.lflang.LF.ImportedReactor");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:198:3: (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )*
			loop4:
			while (true) {
				int alt4=2;
				int LA4_0 = input.LA(1);
				if ( (LA4_0==22) ) {
					alt4=1;
				}

				switch (alt4) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:199:4: otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) )
					{
					otherlv_2=(Token)match(input,22,FOLLOW_22_in_ruleImport360); 

									newLeafNode(otherlv_2, grammarAccess.getImportAccess().getCommaKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:203:4: ( (lv_reactorClasses_3_0= ruleImportedReactor ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:204:5: (lv_reactorClasses_3_0= ruleImportedReactor )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:204:5: (lv_reactorClasses_3_0= ruleImportedReactor )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:205:6: lv_reactorClasses_3_0= ruleImportedReactor
					{

											newCompositeNode(grammarAccess.getImportAccess().getReactorClassesImportedReactorParserRuleCall_2_1_0());
										
					pushFollow(FOLLOW_ruleImportedReactor_in_ruleImport392);
					lv_reactorClasses_3_0=ruleImportedReactor();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getImportRule());
											}
											add(
												current,
												"reactorClasses",
												lv_reactorClasses_3_0,
												"org.lflang.LF.ImportedReactor");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

				default :
					break loop4;
				}
			}

			otherlv_4=(Token)match(input,51,FOLLOW_51_in_ruleImport421); 

						newLeafNode(otherlv_4, grammarAccess.getImportAccess().getFromKeyword_3());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:227:3: ( (lv_importURI_5_0= RULE_STRING ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:228:4: (lv_importURI_5_0= RULE_STRING )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:228:4: (lv_importURI_5_0= RULE_STRING )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:229:5: lv_importURI_5_0= RULE_STRING
			{
			lv_importURI_5_0=(Token)match(input,RULE_STRING,FOLLOW_RULE_STRING_in_ruleImport442); 

								newLeafNode(lv_importURI_5_0, grammarAccess.getImportAccess().getImportURISTRINGTerminalRuleCall_4_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getImportRule());
								}
								setWithLastConsumed(
									current,
									"importURI",
									lv_importURI_5_0,
									"org.lflang.LF.STRING");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:245:3: (otherlv_6= ';' )?
			int alt5=2;
			int LA5_0 = input.LA(1);
			if ( (LA5_0==30) ) {
				alt5=1;
			}
			switch (alt5) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:246:4: otherlv_6= ';'
					{
					otherlv_6=(Token)match(input,30,FOLLOW_30_in_ruleImport474); 

									newLeafNode(otherlv_6, grammarAccess.getImportAccess().getSemicolonKeyword_5());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleImport"



	// $ANTLR start "entryRuleImportedReactor"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:255:1: entryRuleImportedReactor returns [EObject current=null] :iv_ruleImportedReactor= ruleImportedReactor EOF ;
	public final EObject entryRuleImportedReactor() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleImportedReactor =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:255:56: (iv_ruleImportedReactor= ruleImportedReactor EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:256:2: iv_ruleImportedReactor= ruleImportedReactor EOF
			{
			 newCompositeNode(grammarAccess.getImportedReactorRule()); 
			pushFollow(FOLLOW_ruleImportedReactor_in_entryRuleImportedReactor506);
			iv_ruleImportedReactor=ruleImportedReactor();
			state._fsp--;

			 current =iv_ruleImportedReactor; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleImportedReactor512); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleImportedReactor"



	// $ANTLR start "ruleImportedReactor"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:262:1: ruleImportedReactor returns [EObject current=null] : ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? ) ;
	public final EObject ruleImportedReactor() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_1=null;
		Token lv_name_2_0=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:268:2: ( ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:269:2: ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:269:2: ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:270:3: ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:270:3: ( (otherlv_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:271:4: (otherlv_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:271:4: (otherlv_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:272:5: otherlv_0= RULE_ID
			{

								if (current==null) {
									current = createModelElement(grammarAccess.getImportedReactorRule());
								}
							
			otherlv_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleImportedReactor558); 

								newLeafNode(otherlv_0, grammarAccess.getImportedReactorAccess().getReactorClassReactorCrossReference_0_0());
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:283:3: (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )?
			int alt6=2;
			int LA6_0 = input.LA(1);
			if ( (LA6_0==45) ) {
				alt6=1;
			}
			switch (alt6) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:284:4: otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) )
					{
					otherlv_1=(Token)match(input,45,FOLLOW_45_in_ruleImportedReactor584); 

									newLeafNode(otherlv_1, grammarAccess.getImportedReactorAccess().getAsKeyword_1_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:288:4: ( (lv_name_2_0= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:289:5: (lv_name_2_0= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:289:5: (lv_name_2_0= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:290:6: lv_name_2_0= RULE_ID
					{
					lv_name_2_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleImportedReactor609); 

											newLeafNode(lv_name_2_0, grammarAccess.getImportedReactorAccess().getNameIDTerminalRuleCall_1_1_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getImportedReactorRule());
											}
											setWithLastConsumed(
												current,
												"name",
												lv_name_2_0,
												"org.lflang.LF.ID");
										
					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleImportedReactor"



	// $ANTLR start "entryRuleReactor"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:311:1: entryRuleReactor returns [EObject current=null] :iv_ruleReactor= ruleReactor EOF ;
	public final EObject entryRuleReactor() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleReactor =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:311:48: (iv_ruleReactor= ruleReactor EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:312:2: iv_ruleReactor= ruleReactor EOF
			{
			 newCompositeNode(grammarAccess.getReactorRule()); 
			pushFollow(FOLLOW_ruleReactor_in_entryRuleReactor661);
			iv_ruleReactor=ruleReactor();
			state._fsp--;

			 current =iv_ruleReactor; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleReactor667); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleReactor"



	// $ANTLR start "ruleReactor"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:318:1: ruleReactor returns [EObject current=null] : ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' ) ;
	public final EObject ruleReactor() throws RecognitionException {
		EObject current = null;


		Token lv_federated_3_0=null;
		Token lv_main_4_0=null;
		Token lv_realtime_5_0=null;
		Token otherlv_6=null;
		Token lv_name_7_0=null;
		Token otherlv_8=null;
		Token otherlv_10=null;
		Token otherlv_12=null;
		Token otherlv_13=null;
		Token otherlv_15=null;
		Token otherlv_17=null;
		Token otherlv_18=null;
		Token otherlv_20=null;
		Token otherlv_21=null;
		Token otherlv_22=null;
		Token otherlv_23=null;
		Token otherlv_24=null;
		Token otherlv_36=null;
		EObject lv_attributes_1_0 =null;
		EObject lv_typeParms_9_0 =null;
		EObject lv_typeParms_11_0 =null;
		EObject lv_parameters_14_0 =null;
		EObject lv_parameters_16_0 =null;
		EObject lv_host_19_0 =null;
		EObject lv_preambles_25_0 =null;
		EObject lv_stateVars_26_0 =null;
		EObject lv_methods_27_0 =null;
		EObject lv_inputs_28_0 =null;
		EObject lv_outputs_29_0 =null;
		EObject lv_timers_30_0 =null;
		EObject lv_actions_31_0 =null;
		EObject lv_instantiations_32_0 =null;
		EObject lv_connections_33_0 =null;
		EObject lv_reactions_34_0 =null;
		EObject lv_modes_35_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:324:2: ( ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:325:2: ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:325:2: ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:326:3: () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}'
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:326:3: ()
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:327:4: 
			{

							current = forceCreateModelElement(
								grammarAccess.getReactorAccess().getReactorAction_0(),
								current);
						
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:333:3: ( (lv_attributes_1_0= ruleAttribute ) )*
			loop7:
			while (true) {
				int alt7=2;
				int LA7_0 = input.LA(1);
				if ( (LA7_0==35) ) {
					alt7=1;
				}

				switch (alt7) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:334:4: (lv_attributes_1_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:334:4: (lv_attributes_1_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:335:5: lv_attributes_1_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getReactorAccess().getAttributesAttributeParserRuleCall_1_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleReactor726);
					lv_attributes_1_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getReactorRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_1_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop7;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:352:3: ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:353:4: ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:353:4: ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:354:5: ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* )
			{
			 
							  getUnorderedGroupHelper().enter(grammarAccess.getReactorAccess().getUnorderedGroup_2());
							
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:357:5: ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:358:6: ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )*
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:358:6: ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )*
			loop9:
			while (true) {
				int alt9=3;
				int LA9_0 = input.LA(1);
				if ( (LA9_0==50||LA9_0==58) && ((getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0)))) {
					alt9=1;
				}
				else if ( (LA9_0==71) && ((getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1)))) {
					alt9=2;
				}

				switch (alt9) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:359:4: ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:359:4: ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:360:5: {...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) )
					{
					if ( !((getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0))) ) {
						throw new FailedPredicateException(input, "ruleReactor", "getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0)");
					}
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:360:104: ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:361:6: ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) )
					{

											getUnorderedGroupHelper().select(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0);
										
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:364:9: ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:364:10: {...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) )
					{
					if ( !((true)) ) {
						throw new FailedPredicateException(input, "ruleReactor", "true");
					}
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:364:19: ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) )
					int alt8=2;
					int LA8_0 = input.LA(1);
					if ( (LA8_0==50) ) {
						alt8=1;
					}
					else if ( (LA8_0==58) ) {
						alt8=2;
					}

					else {
						NoViableAltException nvae =
							new NoViableAltException("", 8, 0, input);
						throw nvae;
					}

					switch (alt8) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:364:20: ( (lv_federated_3_0= 'federated' ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:364:20: ( (lv_federated_3_0= 'federated' ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:365:10: (lv_federated_3_0= 'federated' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:365:10: (lv_federated_3_0= 'federated' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:366:11: lv_federated_3_0= 'federated'
							{
							lv_federated_3_0=(Token)match(input,50,FOLLOW_50_in_ruleReactor829); 

																		newLeafNode(lv_federated_3_0, grammarAccess.getReactorAccess().getFederatedFederatedKeyword_2_0_0_0());
																	

																		if (current==null) {
																			current = createModelElement(grammarAccess.getReactorRule());
																		}
																		setWithLastConsumed(current, "federated", lv_federated_3_0 != null, "federated");
																	
							}

							}

							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:379:9: ( (lv_main_4_0= 'main' ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:379:9: ( (lv_main_4_0= 'main' ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:380:10: (lv_main_4_0= 'main' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:380:10: (lv_main_4_0= 'main' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:381:11: lv_main_4_0= 'main'
							{
							lv_main_4_0=(Token)match(input,58,FOLLOW_58_in_ruleReactor923); 

																		newLeafNode(lv_main_4_0, grammarAccess.getReactorAccess().getMainMainKeyword_2_0_1_0());
																	

																		if (current==null) {
																			current = createModelElement(grammarAccess.getReactorRule());
																		}
																		setWithLastConsumed(current, "main", lv_main_4_0 != null, "main");
																	
							}

							}

							}
							break;

					}

					}

					 
											getUnorderedGroupHelper().returnFromSelection(grammarAccess.getReactorAccess().getUnorderedGroup_2());
										
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:399:4: ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:399:4: ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:400:5: {...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) )
					{
					if ( !((getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1))) ) {
						throw new FailedPredicateException(input, "ruleReactor", "getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1)");
					}
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:400:104: ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:401:6: ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) )
					{

											getUnorderedGroupHelper().select(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1);
										
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:404:9: ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:404:10: {...}? => ( (lv_realtime_5_0= 'realtime' ) )
					{
					if ( !((true)) ) {
						throw new FailedPredicateException(input, "ruleReactor", "true");
					}
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:404:19: ( (lv_realtime_5_0= 'realtime' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:404:20: (lv_realtime_5_0= 'realtime' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:404:20: (lv_realtime_5_0= 'realtime' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:405:10: lv_realtime_5_0= 'realtime'
					{
					lv_realtime_5_0=(Token)match(input,71,FOLLOW_71_in_ruleReactor1045); 

															newLeafNode(lv_realtime_5_0, grammarAccess.getReactorAccess().getRealtimeRealtimeKeyword_2_1_0());
														

															if (current==null) {
																current = createModelElement(grammarAccess.getReactorRule());
															}
															setWithLastConsumed(current, "realtime", lv_realtime_5_0 != null, "realtime");
														
					}

					}

					}

					 
											getUnorderedGroupHelper().returnFromSelection(grammarAccess.getReactorAccess().getUnorderedGroup_2());
										
					}

					}

					}
					break;

				default :
					break loop9;
				}
			}

			}

			}

			 
							  getUnorderedGroupHelper().leave(grammarAccess.getReactorAccess().getUnorderedGroup_2());
							
			}

			otherlv_6=(Token)match(input,70,FOLLOW_70_in_ruleReactor1141); 

						newLeafNode(otherlv_6, grammarAccess.getReactorAccess().getReactorKeyword_3());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:433:3: ( (lv_name_7_0= RULE_ID ) )?
			int alt10=2;
			int LA10_0 = input.LA(1);
			if ( (LA10_0==RULE_ID) ) {
				alt10=1;
			}
			switch (alt10) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:434:4: (lv_name_7_0= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:434:4: (lv_name_7_0= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:435:5: lv_name_7_0= RULE_ID
					{
					lv_name_7_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleReactor1162); 

										newLeafNode(lv_name_7_0, grammarAccess.getReactorAccess().getNameIDTerminalRuleCall_4_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getReactorRule());
										}
										setWithLastConsumed(
											current,
											"name",
											lv_name_7_0,
											"org.lflang.LF.ID");
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:451:3: (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )?
			int alt12=2;
			int LA12_0 = input.LA(1);
			if ( (LA12_0==31) ) {
				alt12=1;
			}
			switch (alt12) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:452:4: otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>'
					{
					otherlv_8=(Token)match(input,31,FOLLOW_31_in_ruleReactor1195); 

									newLeafNode(otherlv_8, grammarAccess.getReactorAccess().getLessThanSignKeyword_5_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:456:4: ( (lv_typeParms_9_0= ruleTypeParm ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:457:5: (lv_typeParms_9_0= ruleTypeParm )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:457:5: (lv_typeParms_9_0= ruleTypeParm )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:458:6: lv_typeParms_9_0= ruleTypeParm
					{

											newCompositeNode(grammarAccess.getReactorAccess().getTypeParmsTypeParmParserRuleCall_5_1_0());
										
					pushFollow(FOLLOW_ruleTypeParm_in_ruleReactor1227);
					lv_typeParms_9_0=ruleTypeParm();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"typeParms",
												lv_typeParms_9_0,
												"org.lflang.LF.TypeParm");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:475:4: (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )*
					loop11:
					while (true) {
						int alt11=2;
						int LA11_0 = input.LA(1);
						if ( (LA11_0==22) ) {
							alt11=1;
						}

						switch (alt11) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:476:5: otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) )
							{
							otherlv_10=(Token)match(input,22,FOLLOW_22_in_ruleReactor1258); 

												newLeafNode(otherlv_10, grammarAccess.getReactorAccess().getCommaKeyword_5_2_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:480:5: ( (lv_typeParms_11_0= ruleTypeParm ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:481:6: (lv_typeParms_11_0= ruleTypeParm )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:481:6: (lv_typeParms_11_0= ruleTypeParm )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:482:7: lv_typeParms_11_0= ruleTypeParm
							{

														newCompositeNode(grammarAccess.getReactorAccess().getTypeParmsTypeParmParserRuleCall_5_2_1_0());
													
							pushFollow(FOLLOW_ruleTypeParm_in_ruleReactor1295);
							lv_typeParms_11_0=ruleTypeParm();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getReactorRule());
														}
														add(
															current,
															"typeParms",
															lv_typeParms_11_0,
															"org.lflang.LF.TypeParm");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop11;
						}
					}

					otherlv_12=(Token)match(input,34,FOLLOW_34_in_ruleReactor1329); 

									newLeafNode(otherlv_12, grammarAccess.getReactorAccess().getGreaterThanSignKeyword_5_3());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:505:3: (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )?
			int alt14=2;
			int LA14_0 = input.LA(1);
			if ( (LA14_0==18) ) {
				alt14=1;
			}
			switch (alt14) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:506:4: otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')'
					{
					otherlv_13=(Token)match(input,18,FOLLOW_18_in_ruleReactor1350); 

									newLeafNode(otherlv_13, grammarAccess.getReactorAccess().getLeftParenthesisKeyword_6_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:510:4: ( (lv_parameters_14_0= ruleParameter ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:511:5: (lv_parameters_14_0= ruleParameter )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:511:5: (lv_parameters_14_0= ruleParameter )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:512:6: lv_parameters_14_0= ruleParameter
					{

											newCompositeNode(grammarAccess.getReactorAccess().getParametersParameterParserRuleCall_6_1_0());
										
					pushFollow(FOLLOW_ruleParameter_in_ruleReactor1382);
					lv_parameters_14_0=ruleParameter();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"parameters",
												lv_parameters_14_0,
												"org.lflang.LF.Parameter");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:529:4: (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )*
					loop13:
					while (true) {
						int alt13=2;
						int LA13_0 = input.LA(1);
						if ( (LA13_0==22) ) {
							alt13=1;
						}

						switch (alt13) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:530:5: otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) )
							{
							otherlv_15=(Token)match(input,22,FOLLOW_22_in_ruleReactor1413); 

												newLeafNode(otherlv_15, grammarAccess.getReactorAccess().getCommaKeyword_6_2_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:534:5: ( (lv_parameters_16_0= ruleParameter ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:535:6: (lv_parameters_16_0= ruleParameter )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:535:6: (lv_parameters_16_0= ruleParameter )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:536:7: lv_parameters_16_0= ruleParameter
							{

														newCompositeNode(grammarAccess.getReactorAccess().getParametersParameterParserRuleCall_6_2_1_0());
													
							pushFollow(FOLLOW_ruleParameter_in_ruleReactor1450);
							lv_parameters_16_0=ruleParameter();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getReactorRule());
														}
														add(
															current,
															"parameters",
															lv_parameters_16_0,
															"org.lflang.LF.Parameter");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop13;
						}
					}

					otherlv_17=(Token)match(input,19,FOLLOW_19_in_ruleReactor1484); 

									newLeafNode(otherlv_17, grammarAccess.getReactorAccess().getRightParenthesisKeyword_6_3());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:559:3: (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )?
			int alt15=2;
			int LA15_0 = input.LA(1);
			if ( (LA15_0==46) ) {
				alt15=1;
			}
			switch (alt15) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:560:4: otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) )
					{
					otherlv_18=(Token)match(input,46,FOLLOW_46_in_ruleReactor1505); 

									newLeafNode(otherlv_18, grammarAccess.getReactorAccess().getAtKeyword_7_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:564:4: ( (lv_host_19_0= ruleHost ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:565:5: (lv_host_19_0= ruleHost )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:565:5: (lv_host_19_0= ruleHost )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:566:6: lv_host_19_0= ruleHost
					{

											newCompositeNode(grammarAccess.getReactorAccess().getHostHostParserRuleCall_7_1_0());
										
					pushFollow(FOLLOW_ruleHost_in_ruleReactor1537);
					lv_host_19_0=ruleHost();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											set(
												current,
												"host",
												lv_host_19_0,
												"org.lflang.LF.Host");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:584:3: (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )?
			int alt17=2;
			int LA17_0 = input.LA(1);
			if ( (LA17_0==49) ) {
				alt17=1;
			}
			switch (alt17) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:585:4: otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* )
					{
					otherlv_20=(Token)match(input,49,FOLLOW_49_in_ruleReactor1571); 

									newLeafNode(otherlv_20, grammarAccess.getReactorAccess().getExtendsKeyword_8_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:589:4: ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:590:5: ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )*
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:590:5: ( (otherlv_21= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:591:6: (otherlv_21= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:591:6: (otherlv_21= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:592:7: otherlv_21= RULE_ID
					{

												if (current==null) {
													current = createModelElement(grammarAccess.getReactorRule());
												}
											
					otherlv_21=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleReactor1612); 

												newLeafNode(otherlv_21, grammarAccess.getReactorAccess().getSuperClassesReactorDeclCrossReference_8_1_0_0());
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:603:5: (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )*
					loop16:
					while (true) {
						int alt16=2;
						int LA16_0 = input.LA(1);
						if ( (LA16_0==22) ) {
							alt16=1;
						}

						switch (alt16) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:604:6: otherlv_22= ',' ( (otherlv_23= RULE_ID ) )
							{
							otherlv_22=(Token)match(input,22,FOLLOW_22_in_ruleReactor1648); 

													newLeafNode(otherlv_22, grammarAccess.getReactorAccess().getCommaKeyword_8_1_1_0());
												
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:608:6: ( (otherlv_23= RULE_ID ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:609:7: (otherlv_23= RULE_ID )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:609:7: (otherlv_23= RULE_ID )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:610:8: otherlv_23= RULE_ID
							{

															if (current==null) {
																current = createModelElement(grammarAccess.getReactorRule());
															}
														
							otherlv_23=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleReactor1690); 

															newLeafNode(otherlv_23, grammarAccess.getReactorAccess().getSuperClassesReactorDeclCrossReference_8_1_1_1_0());
														
							}

							}

							}
							break;

						default :
							break loop16;
						}
					}

					}

					}
					break;

			}

			otherlv_24=(Token)match(input,82,FOLLOW_82_in_ruleReactor1737); 

						newLeafNode(otherlv_24, grammarAccess.getReactorAccess().getLeftCurlyBracketKeyword_9());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:628:3: ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )*
			loop18:
			while (true) {
				int alt18=12;
				alt18 = dfa18.predict(input);
				switch (alt18) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:629:4: ( (lv_preambles_25_0= rulePreamble ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:629:4: ( (lv_preambles_25_0= rulePreamble ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:630:5: (lv_preambles_25_0= rulePreamble )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:630:5: (lv_preambles_25_0= rulePreamble )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:631:6: lv_preambles_25_0= rulePreamble
					{

											newCompositeNode(grammarAccess.getReactorAccess().getPreamblesPreambleParserRuleCall_10_0_0());
										
					pushFollow(FOLLOW_rulePreamble_in_ruleReactor1772);
					lv_preambles_25_0=rulePreamble();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"preambles",
												lv_preambles_25_0,
												"org.lflang.LF.Preamble");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:649:4: ( (lv_stateVars_26_0= ruleStateVar ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:649:4: ( (lv_stateVars_26_0= ruleStateVar ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:650:5: (lv_stateVars_26_0= ruleStateVar )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:650:5: (lv_stateVars_26_0= ruleStateVar )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:651:6: lv_stateVars_26_0= ruleStateVar
					{

											newCompositeNode(grammarAccess.getReactorAccess().getStateVarsStateVarParserRuleCall_10_1_0());
										
					pushFollow(FOLLOW_ruleStateVar_in_ruleReactor1826);
					lv_stateVars_26_0=ruleStateVar();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"stateVars",
												lv_stateVars_26_0,
												"org.lflang.LF.StateVar");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:669:4: ( (lv_methods_27_0= ruleMethod ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:669:4: ( (lv_methods_27_0= ruleMethod ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:670:5: (lv_methods_27_0= ruleMethod )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:670:5: (lv_methods_27_0= ruleMethod )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:671:6: lv_methods_27_0= ruleMethod
					{

											newCompositeNode(grammarAccess.getReactorAccess().getMethodsMethodParserRuleCall_10_2_0());
										
					pushFollow(FOLLOW_ruleMethod_in_ruleReactor1880);
					lv_methods_27_0=ruleMethod();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"methods",
												lv_methods_27_0,
												"org.lflang.LF.Method");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:689:4: ( (lv_inputs_28_0= ruleInput ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:689:4: ( (lv_inputs_28_0= ruleInput ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:690:5: (lv_inputs_28_0= ruleInput )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:690:5: (lv_inputs_28_0= ruleInput )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:691:6: lv_inputs_28_0= ruleInput
					{

											newCompositeNode(grammarAccess.getReactorAccess().getInputsInputParserRuleCall_10_3_0());
										
					pushFollow(FOLLOW_ruleInput_in_ruleReactor1934);
					lv_inputs_28_0=ruleInput();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"inputs",
												lv_inputs_28_0,
												"org.lflang.LF.Input");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 5 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:709:4: ( (lv_outputs_29_0= ruleOutput ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:709:4: ( (lv_outputs_29_0= ruleOutput ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:710:5: (lv_outputs_29_0= ruleOutput )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:710:5: (lv_outputs_29_0= ruleOutput )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:711:6: lv_outputs_29_0= ruleOutput
					{

											newCompositeNode(grammarAccess.getReactorAccess().getOutputsOutputParserRuleCall_10_4_0());
										
					pushFollow(FOLLOW_ruleOutput_in_ruleReactor1988);
					lv_outputs_29_0=ruleOutput();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"outputs",
												lv_outputs_29_0,
												"org.lflang.LF.Output");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 6 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:729:4: ( (lv_timers_30_0= ruleTimer ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:729:4: ( (lv_timers_30_0= ruleTimer ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:730:5: (lv_timers_30_0= ruleTimer )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:730:5: (lv_timers_30_0= ruleTimer )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:731:6: lv_timers_30_0= ruleTimer
					{

											newCompositeNode(grammarAccess.getReactorAccess().getTimersTimerParserRuleCall_10_5_0());
										
					pushFollow(FOLLOW_ruleTimer_in_ruleReactor2042);
					lv_timers_30_0=ruleTimer();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"timers",
												lv_timers_30_0,
												"org.lflang.LF.Timer");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 7 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:749:4: ( (lv_actions_31_0= ruleAction ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:749:4: ( (lv_actions_31_0= ruleAction ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:750:5: (lv_actions_31_0= ruleAction )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:750:5: (lv_actions_31_0= ruleAction )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:751:6: lv_actions_31_0= ruleAction
					{

											newCompositeNode(grammarAccess.getReactorAccess().getActionsActionParserRuleCall_10_6_0());
										
					pushFollow(FOLLOW_ruleAction_in_ruleReactor2096);
					lv_actions_31_0=ruleAction();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"actions",
												lv_actions_31_0,
												"org.lflang.LF.Action");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 8 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:769:4: ( (lv_instantiations_32_0= ruleInstantiation ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:769:4: ( (lv_instantiations_32_0= ruleInstantiation ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:770:5: (lv_instantiations_32_0= ruleInstantiation )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:770:5: (lv_instantiations_32_0= ruleInstantiation )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:771:6: lv_instantiations_32_0= ruleInstantiation
					{

											newCompositeNode(grammarAccess.getReactorAccess().getInstantiationsInstantiationParserRuleCall_10_7_0());
										
					pushFollow(FOLLOW_ruleInstantiation_in_ruleReactor2150);
					lv_instantiations_32_0=ruleInstantiation();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"instantiations",
												lv_instantiations_32_0,
												"org.lflang.LF.Instantiation");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 9 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:789:4: ( (lv_connections_33_0= ruleConnection ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:789:4: ( (lv_connections_33_0= ruleConnection ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:790:5: (lv_connections_33_0= ruleConnection )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:790:5: (lv_connections_33_0= ruleConnection )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:791:6: lv_connections_33_0= ruleConnection
					{

											newCompositeNode(grammarAccess.getReactorAccess().getConnectionsConnectionParserRuleCall_10_8_0());
										
					pushFollow(FOLLOW_ruleConnection_in_ruleReactor2204);
					lv_connections_33_0=ruleConnection();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"connections",
												lv_connections_33_0,
												"org.lflang.LF.Connection");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 10 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:809:4: ( (lv_reactions_34_0= ruleReaction ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:809:4: ( (lv_reactions_34_0= ruleReaction ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:810:5: (lv_reactions_34_0= ruleReaction )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:810:5: (lv_reactions_34_0= ruleReaction )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:811:6: lv_reactions_34_0= ruleReaction
					{

											newCompositeNode(grammarAccess.getReactorAccess().getReactionsReactionParserRuleCall_10_9_0());
										
					pushFollow(FOLLOW_ruleReaction_in_ruleReactor2258);
					lv_reactions_34_0=ruleReaction();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"reactions",
												lv_reactions_34_0,
												"org.lflang.LF.Reaction");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 11 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:829:4: ( (lv_modes_35_0= ruleMode ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:829:4: ( (lv_modes_35_0= ruleMode ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:830:5: (lv_modes_35_0= ruleMode )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:830:5: (lv_modes_35_0= ruleMode )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:831:6: lv_modes_35_0= ruleMode
					{

											newCompositeNode(grammarAccess.getReactorAccess().getModesModeParserRuleCall_10_10_0());
										
					pushFollow(FOLLOW_ruleMode_in_ruleReactor2312);
					lv_modes_35_0=ruleMode();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactorRule());
											}
											add(
												current,
												"modes",
												lv_modes_35_0,
												"org.lflang.LF.Mode");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

				default :
					break loop18;
				}
			}

			otherlv_36=(Token)match(input,84,FOLLOW_84_in_ruleReactor2341); 

						newLeafNode(otherlv_36, grammarAccess.getReactorAccess().getRightCurlyBracketKeyword_11());
					
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleReactor"



	// $ANTLR start "entryRuleTypeParm"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:857:1: entryRuleTypeParm returns [EObject current=null] :iv_ruleTypeParm= ruleTypeParm EOF ;
	public final EObject entryRuleTypeParm() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleTypeParm =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:857:49: (iv_ruleTypeParm= ruleTypeParm EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:858:2: iv_ruleTypeParm= ruleTypeParm EOF
			{
			 newCompositeNode(grammarAccess.getTypeParmRule()); 
			pushFollow(FOLLOW_ruleTypeParm_in_entryRuleTypeParm2367);
			iv_ruleTypeParm=ruleTypeParm();
			state._fsp--;

			 current =iv_ruleTypeParm; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTypeParm2373); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTypeParm"



	// $ANTLR start "ruleTypeParm"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:864:1: ruleTypeParm returns [EObject current=null] : ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) ) ;
	public final EObject ruleTypeParm() throws RecognitionException {
		EObject current = null;


		AntlrDatatypeRuleToken lv_literal_0_0 =null;
		EObject lv_code_1_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:870:2: ( ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:871:2: ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:871:2: ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) )
			int alt19=2;
			int LA19_0 = input.LA(1);
			if ( (LA19_0==RULE_ID) ) {
				alt19=1;
			}
			else if ( (LA19_0==83) ) {
				alt19=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 19, 0, input);
				throw nvae;
			}

			switch (alt19) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:872:3: ( (lv_literal_0_0= ruleTypeExpr ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:872:3: ( (lv_literal_0_0= ruleTypeExpr ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:873:4: (lv_literal_0_0= ruleTypeExpr )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:873:4: (lv_literal_0_0= ruleTypeExpr )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:874:5: lv_literal_0_0= ruleTypeExpr
					{

										newCompositeNode(grammarAccess.getTypeParmAccess().getLiteralTypeExprParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleTypeExpr_in_ruleTypeParm2419);
					lv_literal_0_0=ruleTypeExpr();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getTypeParmRule());
										}
										set(
											current,
											"literal",
											lv_literal_0_0,
											"org.lflang.LF.TypeExpr");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:892:3: ( (lv_code_1_0= ruleCode ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:892:3: ( (lv_code_1_0= ruleCode ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:893:4: (lv_code_1_0= ruleCode )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:893:4: (lv_code_1_0= ruleCode )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:894:5: lv_code_1_0= ruleCode
					{

										newCompositeNode(grammarAccess.getTypeParmAccess().getCodeCodeParserRuleCall_1_0());
									
					pushFollow(FOLLOW_ruleCode_in_ruleTypeParm2465);
					lv_code_1_0=ruleCode();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getTypeParmRule());
										}
										set(
											current,
											"code",
											lv_code_1_0,
											"org.lflang.LF.Code");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTypeParm"



	// $ANTLR start "entryRuleTypeExpr"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:915:1: entryRuleTypeExpr returns [String current=null] :iv_ruleTypeExpr= ruleTypeExpr EOF ;
	public final String entryRuleTypeExpr() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleTypeExpr =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:915:48: (iv_ruleTypeExpr= ruleTypeExpr EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:916:2: iv_ruleTypeExpr= ruleTypeExpr EOF
			{
			 newCompositeNode(grammarAccess.getTypeExprRule()); 
			pushFollow(FOLLOW_ruleTypeExpr_in_entryRuleTypeExpr2502);
			iv_ruleTypeExpr=ruleTypeExpr();
			state._fsp--;

			 current =iv_ruleTypeExpr.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTypeExpr2508); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTypeExpr"



	// $ANTLR start "ruleTypeExpr"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:922:1: ruleTypeExpr returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID )+ ;
	public final AntlrDatatypeRuleToken ruleTypeExpr() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_ID_0=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:928:2: ( (this_ID_0= RULE_ID )+ )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:929:2: (this_ID_0= RULE_ID )+
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:929:2: (this_ID_0= RULE_ID )+
			int cnt20=0;
			loop20:
			while (true) {
				int alt20=2;
				int LA20_0 = input.LA(1);
				if ( (LA20_0==RULE_ID) ) {
					alt20=1;
				}

				switch (alt20) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:930:3: this_ID_0= RULE_ID
					{
					this_ID_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleTypeExpr2537); 

								current.merge(this_ID_0);
							

								newLeafNode(this_ID_0, grammarAccess.getTypeExprAccess().getIDTerminalRuleCall());
							
					}
					break;

				default :
					if ( cnt20 >= 1 ) break loop20;
					EarlyExitException eee = new EarlyExitException(20, input);
					throw eee;
				}
				cnt20++;
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTypeExpr"



	// $ANTLR start "entryRuleTargetDecl"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:941:1: entryRuleTargetDecl returns [EObject current=null] :iv_ruleTargetDecl= ruleTargetDecl EOF ;
	public final EObject entryRuleTargetDecl() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleTargetDecl =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:941:51: (iv_ruleTargetDecl= ruleTargetDecl EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:942:2: iv_ruleTargetDecl= ruleTargetDecl EOF
			{
			 newCompositeNode(grammarAccess.getTargetDeclRule()); 
			pushFollow(FOLLOW_ruleTargetDecl_in_entryRuleTargetDecl2568);
			iv_ruleTargetDecl=ruleTargetDecl();
			state._fsp--;

			 current =iv_ruleTargetDecl; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTargetDecl2574); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTargetDecl"



	// $ANTLR start "ruleTargetDecl"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:948:1: ruleTargetDecl returns [EObject current=null] : (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? ) ;
	public final EObject ruleTargetDecl() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token lv_name_1_0=null;
		Token otherlv_3=null;
		EObject lv_config_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:954:2: ( (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:955:2: (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:955:2: (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:956:3: otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )?
			{
			otherlv_0=(Token)match(input,77,FOLLOW_77_in_ruleTargetDecl2603); 

						newLeafNode(otherlv_0, grammarAccess.getTargetDeclAccess().getTargetKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:960:3: ( (lv_name_1_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:961:4: (lv_name_1_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:961:4: (lv_name_1_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:962:5: lv_name_1_0= RULE_ID
			{
			lv_name_1_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleTargetDecl2624); 

								newLeafNode(lv_name_1_0, grammarAccess.getTargetDeclAccess().getNameIDTerminalRuleCall_1_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getTargetDeclRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_1_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:978:3: ( (lv_config_2_0= ruleKeyValuePairs ) )?
			int alt21=2;
			int LA21_0 = input.LA(1);
			if ( (LA21_0==82) ) {
				alt21=1;
			}
			switch (alt21) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:979:4: (lv_config_2_0= ruleKeyValuePairs )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:979:4: (lv_config_2_0= ruleKeyValuePairs )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:980:5: lv_config_2_0= ruleKeyValuePairs
					{

										newCompositeNode(grammarAccess.getTargetDeclAccess().getConfigKeyValuePairsParserRuleCall_2_0());
									
					pushFollow(FOLLOW_ruleKeyValuePairs_in_ruleTargetDecl2668);
					lv_config_2_0=ruleKeyValuePairs();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getTargetDeclRule());
										}
										set(
											current,
											"config",
											lv_config_2_0,
											"org.lflang.LF.KeyValuePairs");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:997:3: (otherlv_3= ';' )?
			int alt22=2;
			int LA22_0 = input.LA(1);
			if ( (LA22_0==30) ) {
				alt22=1;
			}
			switch (alt22) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:998:4: otherlv_3= ';'
					{
					otherlv_3=(Token)match(input,30,FOLLOW_30_in_ruleTargetDecl2695); 

									newLeafNode(otherlv_3, grammarAccess.getTargetDeclAccess().getSemicolonKeyword_3());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTargetDecl"



	// $ANTLR start "entryRuleStateVar"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1007:1: entryRuleStateVar returns [EObject current=null] :iv_ruleStateVar= ruleStateVar EOF ;
	public final EObject entryRuleStateVar() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleStateVar =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1007:49: (iv_ruleStateVar= ruleStateVar EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1008:2: iv_ruleStateVar= ruleStateVar EOF
			{
			 newCompositeNode(grammarAccess.getStateVarRule()); 
			pushFollow(FOLLOW_ruleStateVar_in_entryRuleStateVar2727);
			iv_ruleStateVar=ruleStateVar();
			state._fsp--;

			 current =iv_ruleStateVar; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleStateVar2733); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleStateVar"



	// $ANTLR start "ruleStateVar"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1014:1: ruleStateVar returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? ) ;
	public final EObject ruleStateVar() throws RecognitionException {
		EObject current = null;


		Token lv_reset_1_0=null;
		Token otherlv_2=null;
		Token lv_name_3_0=null;
		Token otherlv_4=null;
		Token lv_parens_6_0=null;
		Token otherlv_8=null;
		Token lv_parens_10_0=null;
		Token lv_braces_11_0=null;
		Token otherlv_13=null;
		Token lv_braces_15_0=null;
		Token otherlv_16=null;
		EObject lv_attributes_0_0 =null;
		EObject lv_type_5_0 =null;
		EObject lv_init_7_0 =null;
		EObject lv_init_9_0 =null;
		EObject lv_init_12_0 =null;
		EObject lv_init_14_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1020:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1021:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1021:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1022:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1022:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop23:
			while (true) {
				int alt23=2;
				int LA23_0 = input.LA(1);
				if ( (LA23_0==35) ) {
					alt23=1;
				}

				switch (alt23) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1023:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1023:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1024:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getStateVarAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleStateVar2779);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getStateVarRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop23;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1041:3: ( (lv_reset_1_0= 'reset' ) )?
			int alt24=2;
			int LA24_0 = input.LA(1);
			if ( (LA24_0==72) ) {
				alt24=1;
			}
			switch (alt24) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1042:4: (lv_reset_1_0= 'reset' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1042:4: (lv_reset_1_0= 'reset' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1043:5: lv_reset_1_0= 'reset'
					{
					lv_reset_1_0=(Token)match(input,72,FOLLOW_72_in_ruleStateVar2812); 

										newLeafNode(lv_reset_1_0, grammarAccess.getStateVarAccess().getResetResetKeyword_1_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getStateVarRule());
										}
										setWithLastConsumed(current, "reset", lv_reset_1_0 != null, "reset");
									
					}

					}
					break;

			}

			otherlv_2=(Token)match(input,76,FOLLOW_76_in_ruleStateVar2840); 

						newLeafNode(otherlv_2, grammarAccess.getStateVarAccess().getStateKeyword_2());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1059:3: ( (lv_name_3_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1060:4: (lv_name_3_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1060:4: (lv_name_3_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1061:5: lv_name_3_0= RULE_ID
			{
			lv_name_3_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleStateVar2861); 

								newLeafNode(lv_name_3_0, grammarAccess.getStateVarAccess().getNameIDTerminalRuleCall_3_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getStateVarRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_3_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1077:3: ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1078:4: (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1078:4: (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )?
			int alt25=2;
			int LA25_0 = input.LA(1);
			if ( (LA25_0==27) ) {
				alt25=1;
			}
			switch (alt25) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1079:5: otherlv_4= ':' ( (lv_type_5_0= ruleType ) )
					{
					otherlv_4=(Token)match(input,27,FOLLOW_27_in_ruleStateVar2899); 

										newLeafNode(otherlv_4, grammarAccess.getStateVarAccess().getColonKeyword_4_0_0());
									
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1083:5: ( (lv_type_5_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1084:6: (lv_type_5_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1084:6: (lv_type_5_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1085:7: lv_type_5_0= ruleType
					{

												newCompositeNode(grammarAccess.getStateVarAccess().getTypeTypeParserRuleCall_4_0_1_0());
											
					pushFollow(FOLLOW_ruleType_in_ruleStateVar2936);
					lv_type_5_0=ruleType();
					state._fsp--;


												if (current==null) {
													current = createModelElementForParent(grammarAccess.getStateVarRule());
												}
												set(
													current,
													"type",
													lv_type_5_0,
													"org.lflang.LF.Type");
												afterParserOrEnumRuleCall();
											
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1103:4: ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )?
			int alt30=3;
			alt30 = dfa30.predict(input);
			switch (alt30) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1104:5: ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1104:5: ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1105:6: ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1105:6: ( (lv_parens_6_0= '(' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1106:7: (lv_parens_6_0= '(' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1106:7: (lv_parens_6_0= '(' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1107:8: lv_parens_6_0= '('
					{
					lv_parens_6_0=(Token)match(input,18,FOLLOW_18_in_ruleStateVar3000); 

													newLeafNode(lv_parens_6_0, grammarAccess.getStateVarAccess().getParensLeftParenthesisKeyword_4_1_0_0_0());
												

													if (current==null) {
														current = createModelElement(grammarAccess.getStateVarRule());
													}
													addWithLastConsumed(current, "parens", lv_parens_6_0, "(");
												
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1119:6: ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )?
					int alt27=2;
					int LA27_0 = input.LA(1);
					if ( ((LA27_0 >= RULE_CHAR_LIT && LA27_0 <= RULE_FALSE)||(LA27_0 >= RULE_ID && LA27_0 <= RULE_INT)||LA27_0==RULE_NEGINT||(LA27_0 >= RULE_STRING && LA27_0 <= RULE_TRUE)||LA27_0==23||LA27_0==25||LA27_0==83) ) {
						alt27=1;
					}
					switch (alt27) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1120:7: ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )*
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1120:7: ( (lv_init_7_0= ruleExpression ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1121:8: (lv_init_7_0= ruleExpression )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1121:8: (lv_init_7_0= ruleExpression )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1122:9: lv_init_7_0= ruleExpression
							{

																newCompositeNode(grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_0_1_0_0());
															
							pushFollow(FOLLOW_ruleExpression_in_ruleStateVar3079);
							lv_init_7_0=ruleExpression();
							state._fsp--;


																if (current==null) {
																	current = createModelElementForParent(grammarAccess.getStateVarRule());
																}
																add(
																	current,
																	"init",
																	lv_init_7_0,
																	"org.lflang.LF.Expression");
																afterParserOrEnumRuleCall();
															
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1139:7: (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )*
							loop26:
							while (true) {
								int alt26=2;
								int LA26_0 = input.LA(1);
								if ( (LA26_0==22) ) {
									alt26=1;
								}

								switch (alt26) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1140:8: otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) )
									{
									otherlv_8=(Token)match(input,22,FOLLOW_22_in_ruleStateVar3125); 

																	newLeafNode(otherlv_8, grammarAccess.getStateVarAccess().getCommaKeyword_4_1_0_1_1_0());
																
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1144:8: ( (lv_init_9_0= ruleExpression ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1145:9: (lv_init_9_0= ruleExpression )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1145:9: (lv_init_9_0= ruleExpression )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1146:10: lv_init_9_0= ruleExpression
									{

																			newCompositeNode(grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_0_1_1_1_0());
																		
									pushFollow(FOLLOW_ruleExpression_in_ruleStateVar3177);
									lv_init_9_0=ruleExpression();
									state._fsp--;


																			if (current==null) {
																				current = createModelElementForParent(grammarAccess.getStateVarRule());
																			}
																			add(
																				current,
																				"init",
																				lv_init_9_0,
																				"org.lflang.LF.Expression");
																			afterParserOrEnumRuleCall();
																		
									}

									}

									}
									break;

								default :
									break loop26;
								}
							}

							}
							break;

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1165:6: ( (lv_parens_10_0= ')' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1166:7: (lv_parens_10_0= ')' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1166:7: (lv_parens_10_0= ')' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1167:8: lv_parens_10_0= ')'
					{
					lv_parens_10_0=(Token)match(input,19,FOLLOW_19_in_ruleStateVar3250); 

													newLeafNode(lv_parens_10_0, grammarAccess.getStateVarAccess().getParensRightParenthesisKeyword_4_1_0_2_0());
												

													if (current==null) {
														current = createModelElement(grammarAccess.getStateVarRule());
													}
													addWithLastConsumed(current, "parens", lv_parens_10_0, ")");
												
					}

					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1181:5: ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1181:5: ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1182:6: ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1182:6: ( (lv_braces_11_0= '{' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1183:7: (lv_braces_11_0= '{' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1183:7: (lv_braces_11_0= '{' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1184:8: lv_braces_11_0= '{'
					{
					lv_braces_11_0=(Token)match(input,82,FOLLOW_82_in_ruleStateVar3331); 

													newLeafNode(lv_braces_11_0, grammarAccess.getStateVarAccess().getBracesLeftCurlyBracketKeyword_4_1_1_0_0());
												

													if (current==null) {
														current = createModelElement(grammarAccess.getStateVarRule());
													}
													addWithLastConsumed(current, "braces", lv_braces_11_0, "{");
												
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1196:6: ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )?
					int alt29=2;
					int LA29_0 = input.LA(1);
					if ( ((LA29_0 >= RULE_CHAR_LIT && LA29_0 <= RULE_FALSE)||(LA29_0 >= RULE_ID && LA29_0 <= RULE_INT)||LA29_0==RULE_NEGINT||(LA29_0 >= RULE_STRING && LA29_0 <= RULE_TRUE)||LA29_0==23||LA29_0==25||LA29_0==83) ) {
						alt29=1;
					}
					switch (alt29) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1197:7: ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )*
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1197:7: ( (lv_init_12_0= ruleExpression ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1198:8: (lv_init_12_0= ruleExpression )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1198:8: (lv_init_12_0= ruleExpression )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1199:9: lv_init_12_0= ruleExpression
							{

																newCompositeNode(grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_1_1_0_0());
															
							pushFollow(FOLLOW_ruleExpression_in_ruleStateVar3410);
							lv_init_12_0=ruleExpression();
							state._fsp--;


																if (current==null) {
																	current = createModelElementForParent(grammarAccess.getStateVarRule());
																}
																add(
																	current,
																	"init",
																	lv_init_12_0,
																	"org.lflang.LF.Expression");
																afterParserOrEnumRuleCall();
															
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1216:7: (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )*
							loop28:
							while (true) {
								int alt28=2;
								int LA28_0 = input.LA(1);
								if ( (LA28_0==22) ) {
									alt28=1;
								}

								switch (alt28) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1217:8: otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) )
									{
									otherlv_13=(Token)match(input,22,FOLLOW_22_in_ruleStateVar3456); 

																	newLeafNode(otherlv_13, grammarAccess.getStateVarAccess().getCommaKeyword_4_1_1_1_1_0());
																
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1221:8: ( (lv_init_14_0= ruleExpression ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1222:9: (lv_init_14_0= ruleExpression )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1222:9: (lv_init_14_0= ruleExpression )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1223:10: lv_init_14_0= ruleExpression
									{

																			newCompositeNode(grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_1_1_1_1_0());
																		
									pushFollow(FOLLOW_ruleExpression_in_ruleStateVar3508);
									lv_init_14_0=ruleExpression();
									state._fsp--;


																			if (current==null) {
																				current = createModelElementForParent(grammarAccess.getStateVarRule());
																			}
																			add(
																				current,
																				"init",
																				lv_init_14_0,
																				"org.lflang.LF.Expression");
																			afterParserOrEnumRuleCall();
																		
									}

									}

									}
									break;

								default :
									break loop28;
								}
							}

							}
							break;

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1242:6: ( (lv_braces_15_0= '}' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1243:7: (lv_braces_15_0= '}' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1243:7: (lv_braces_15_0= '}' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1244:8: lv_braces_15_0= '}'
					{
					lv_braces_15_0=(Token)match(input,84,FOLLOW_84_in_ruleStateVar3581); 

													newLeafNode(lv_braces_15_0, grammarAccess.getStateVarAccess().getBracesRightCurlyBracketKeyword_4_1_1_2_0());
												

													if (current==null) {
														current = createModelElement(grammarAccess.getStateVarRule());
													}
													addWithLastConsumed(current, "braces", lv_braces_15_0, "}");
												
					}

					}

					}

					}
					break;

			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1259:3: (otherlv_16= ';' )?
			int alt31=2;
			int LA31_0 = input.LA(1);
			if ( (LA31_0==30) ) {
				alt31=1;
			}
			switch (alt31) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1260:4: otherlv_16= ';'
					{
					otherlv_16=(Token)match(input,30,FOLLOW_30_in_ruleStateVar3641); 

									newLeafNode(otherlv_16, grammarAccess.getStateVarAccess().getSemicolonKeyword_5());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleStateVar"



	// $ANTLR start "entryRuleMethod"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1269:1: entryRuleMethod returns [EObject current=null] :iv_ruleMethod= ruleMethod EOF ;
	public final EObject entryRuleMethod() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleMethod =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1269:47: (iv_ruleMethod= ruleMethod EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1270:2: iv_ruleMethod= ruleMethod EOF
			{
			 newCompositeNode(grammarAccess.getMethodRule()); 
			pushFollow(FOLLOW_ruleMethod_in_entryRuleMethod3673);
			iv_ruleMethod=ruleMethod();
			state._fsp--;

			 current =iv_ruleMethod; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleMethod3679); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleMethod"



	// $ANTLR start "ruleMethod"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1276:1: ruleMethod returns [EObject current=null] : ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? ) ;
	public final EObject ruleMethod() throws RecognitionException {
		EObject current = null;


		Token lv_const_0_0=null;
		Token otherlv_1=null;
		Token lv_name_2_0=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		Token otherlv_8=null;
		Token otherlv_11=null;
		EObject lv_arguments_4_0 =null;
		EObject lv_arguments_6_0 =null;
		EObject lv_return_9_0 =null;
		EObject lv_code_10_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1282:2: ( ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1283:2: ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1283:2: ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1284:3: ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1284:3: ( (lv_const_0_0= 'const' ) )?
			int alt32=2;
			int LA32_0 = input.LA(1);
			if ( (LA32_0==47) ) {
				alt32=1;
			}
			switch (alt32) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1285:4: (lv_const_0_0= 'const' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1285:4: (lv_const_0_0= 'const' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1286:5: lv_const_0_0= 'const'
					{
					lv_const_0_0=(Token)match(input,47,FOLLOW_47_in_ruleMethod3719); 

										newLeafNode(lv_const_0_0, grammarAccess.getMethodAccess().getConstConstKeyword_0_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getMethodRule());
										}
										setWithLastConsumed(current, "const", lv_const_0_0 != null, "const");
									
					}

					}
					break;

			}

			otherlv_1=(Token)match(input,59,FOLLOW_59_in_ruleMethod3747); 

						newLeafNode(otherlv_1, grammarAccess.getMethodAccess().getMethodKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1302:3: ( (lv_name_2_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1303:4: (lv_name_2_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1303:4: (lv_name_2_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1304:5: lv_name_2_0= RULE_ID
			{
			lv_name_2_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleMethod3768); 

								newLeafNode(lv_name_2_0, grammarAccess.getMethodAccess().getNameIDTerminalRuleCall_2_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getMethodRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_2_0,
									"org.lflang.LF.ID");
							
			}

			}

			otherlv_3=(Token)match(input,18,FOLLOW_18_in_ruleMethod3795); 

						newLeafNode(otherlv_3, grammarAccess.getMethodAccess().getLeftParenthesisKeyword_3());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1324:3: ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )?
			int alt34=2;
			int LA34_0 = input.LA(1);
			if ( (LA34_0==RULE_ID) ) {
				alt34=1;
			}
			switch (alt34) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1325:4: ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )*
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1325:4: ( (lv_arguments_4_0= ruleMethodArgument ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1326:5: (lv_arguments_4_0= ruleMethodArgument )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1326:5: (lv_arguments_4_0= ruleMethodArgument )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1327:6: lv_arguments_4_0= ruleMethodArgument
					{

											newCompositeNode(grammarAccess.getMethodAccess().getArgumentsMethodArgumentParserRuleCall_4_0_0());
										
					pushFollow(FOLLOW_ruleMethodArgument_in_ruleMethod3830);
					lv_arguments_4_0=ruleMethodArgument();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getMethodRule());
											}
											add(
												current,
												"arguments",
												lv_arguments_4_0,
												"org.lflang.LF.MethodArgument");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1344:4: (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )*
					loop33:
					while (true) {
						int alt33=2;
						int LA33_0 = input.LA(1);
						if ( (LA33_0==22) ) {
							alt33=1;
						}

						switch (alt33) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1345:5: otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) )
							{
							otherlv_5=(Token)match(input,22,FOLLOW_22_in_ruleMethod3861); 

												newLeafNode(otherlv_5, grammarAccess.getMethodAccess().getCommaKeyword_4_1_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1349:5: ( (lv_arguments_6_0= ruleMethodArgument ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1350:6: (lv_arguments_6_0= ruleMethodArgument )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1350:6: (lv_arguments_6_0= ruleMethodArgument )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1351:7: lv_arguments_6_0= ruleMethodArgument
							{

														newCompositeNode(grammarAccess.getMethodAccess().getArgumentsMethodArgumentParserRuleCall_4_1_1_0());
													
							pushFollow(FOLLOW_ruleMethodArgument_in_ruleMethod3898);
							lv_arguments_6_0=ruleMethodArgument();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getMethodRule());
														}
														add(
															current,
															"arguments",
															lv_arguments_6_0,
															"org.lflang.LF.MethodArgument");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop33;
						}
					}

					}
					break;

			}

			otherlv_7=(Token)match(input,19,FOLLOW_19_in_ruleMethod3936); 

						newLeafNode(otherlv_7, grammarAccess.getMethodAccess().getRightParenthesisKeyword_5());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1374:3: (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )?
			int alt35=2;
			int LA35_0 = input.LA(1);
			if ( (LA35_0==27) ) {
				alt35=1;
			}
			switch (alt35) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1375:4: otherlv_8= ':' ( (lv_return_9_0= ruleType ) )
					{
					otherlv_8=(Token)match(input,27,FOLLOW_27_in_ruleMethod3951); 

									newLeafNode(otherlv_8, grammarAccess.getMethodAccess().getColonKeyword_6_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1379:4: ( (lv_return_9_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1380:5: (lv_return_9_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1380:5: (lv_return_9_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1381:6: lv_return_9_0= ruleType
					{

											newCompositeNode(grammarAccess.getMethodAccess().getReturnTypeParserRuleCall_6_1_0());
										
					pushFollow(FOLLOW_ruleType_in_ruleMethod3983);
					lv_return_9_0=ruleType();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getMethodRule());
											}
											set(
												current,
												"return",
												lv_return_9_0,
												"org.lflang.LF.Type");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1399:3: ( (lv_code_10_0= ruleCode ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1400:4: (lv_code_10_0= ruleCode )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1400:4: (lv_code_10_0= ruleCode )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1401:5: lv_code_10_0= ruleCode
			{

								newCompositeNode(grammarAccess.getMethodAccess().getCodeCodeParserRuleCall_7_0());
							
			pushFollow(FOLLOW_ruleCode_in_ruleMethod4029);
			lv_code_10_0=ruleCode();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getMethodRule());
								}
								set(
									current,
									"code",
									lv_code_10_0,
									"org.lflang.LF.Code");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1418:3: (otherlv_11= ';' )?
			int alt36=2;
			int LA36_0 = input.LA(1);
			if ( (LA36_0==30) ) {
				alt36=1;
			}
			switch (alt36) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1419:4: otherlv_11= ';'
					{
					otherlv_11=(Token)match(input,30,FOLLOW_30_in_ruleMethod4055); 

									newLeafNode(otherlv_11, grammarAccess.getMethodAccess().getSemicolonKeyword_8());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleMethod"



	// $ANTLR start "entryRuleMethodArgument"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1428:1: entryRuleMethodArgument returns [EObject current=null] :iv_ruleMethodArgument= ruleMethodArgument EOF ;
	public final EObject entryRuleMethodArgument() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleMethodArgument =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1428:55: (iv_ruleMethodArgument= ruleMethodArgument EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1429:2: iv_ruleMethodArgument= ruleMethodArgument EOF
			{
			 newCompositeNode(grammarAccess.getMethodArgumentRule()); 
			pushFollow(FOLLOW_ruleMethodArgument_in_entryRuleMethodArgument4087);
			iv_ruleMethodArgument=ruleMethodArgument();
			state._fsp--;

			 current =iv_ruleMethodArgument; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleMethodArgument4093); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleMethodArgument"



	// $ANTLR start "ruleMethodArgument"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1435:1: ruleMethodArgument returns [EObject current=null] : ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? ) ;
	public final EObject ruleMethodArgument() throws RecognitionException {
		EObject current = null;


		Token lv_name_0_0=null;
		Token otherlv_1=null;
		EObject lv_type_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1441:2: ( ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1442:2: ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1442:2: ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1443:3: ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1443:3: ( (lv_name_0_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1444:4: (lv_name_0_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1444:4: (lv_name_0_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1445:5: lv_name_0_0= RULE_ID
			{
			lv_name_0_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleMethodArgument4133); 

								newLeafNode(lv_name_0_0, grammarAccess.getMethodArgumentAccess().getNameIDTerminalRuleCall_0_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getMethodArgumentRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_0_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1461:3: (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )?
			int alt37=2;
			int LA37_0 = input.LA(1);
			if ( (LA37_0==27) ) {
				alt37=1;
			}
			switch (alt37) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1462:4: otherlv_1= ':' ( (lv_type_2_0= ruleType ) )
					{
					otherlv_1=(Token)match(input,27,FOLLOW_27_in_ruleMethodArgument4165); 

									newLeafNode(otherlv_1, grammarAccess.getMethodArgumentAccess().getColonKeyword_1_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1466:4: ( (lv_type_2_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1467:5: (lv_type_2_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1467:5: (lv_type_2_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1468:6: lv_type_2_0= ruleType
					{

											newCompositeNode(grammarAccess.getMethodArgumentAccess().getTypeTypeParserRuleCall_1_1_0());
										
					pushFollow(FOLLOW_ruleType_in_ruleMethodArgument4197);
					lv_type_2_0=ruleType();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getMethodArgumentRule());
											}
											set(
												current,
												"type",
												lv_type_2_0,
												"org.lflang.LF.Type");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleMethodArgument"



	// $ANTLR start "entryRuleInput"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1490:1: entryRuleInput returns [EObject current=null] :iv_ruleInput= ruleInput EOF ;
	public final EObject entryRuleInput() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleInput =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1490:46: (iv_ruleInput= ruleInput EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1491:2: iv_ruleInput= ruleInput EOF
			{
			 newCompositeNode(grammarAccess.getInputRule()); 
			pushFollow(FOLLOW_ruleInput_in_entryRuleInput4242);
			iv_ruleInput=ruleInput();
			state._fsp--;

			 current =iv_ruleInput; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleInput4248); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleInput"



	// $ANTLR start "ruleInput"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1497:1: ruleInput returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? ) ;
	public final EObject ruleInput() throws RecognitionException {
		EObject current = null;


		Token lv_mutable_1_0=null;
		Token otherlv_2=null;
		Token lv_name_4_0=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		EObject lv_attributes_0_0 =null;
		EObject lv_widthSpec_3_0 =null;
		EObject lv_type_6_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1503:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1504:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1504:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1505:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1505:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop38:
			while (true) {
				int alt38=2;
				int LA38_0 = input.LA(1);
				if ( (LA38_0==35) ) {
					alt38=1;
				}

				switch (alt38) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1506:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1506:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1507:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getInputAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleInput4294);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getInputRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop38;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1524:3: ( (lv_mutable_1_0= 'mutable' ) )?
			int alt39=2;
			int LA39_0 = input.LA(1);
			if ( (LA39_0==61) ) {
				alt39=1;
			}
			switch (alt39) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1525:4: (lv_mutable_1_0= 'mutable' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1525:4: (lv_mutable_1_0= 'mutable' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1526:5: lv_mutable_1_0= 'mutable'
					{
					lv_mutable_1_0=(Token)match(input,61,FOLLOW_61_in_ruleInput4327); 

										newLeafNode(lv_mutable_1_0, grammarAccess.getInputAccess().getMutableMutableKeyword_1_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getInputRule());
										}
										setWithLastConsumed(current, "mutable", lv_mutable_1_0 != null, "mutable");
									
					}

					}
					break;

			}

			otherlv_2=(Token)match(input,55,FOLLOW_55_in_ruleInput4355); 

						newLeafNode(otherlv_2, grammarAccess.getInputAccess().getInputKeyword_2());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1542:3: ( (lv_widthSpec_3_0= ruleWidthSpec ) )?
			int alt40=2;
			int LA40_0 = input.LA(1);
			if ( (LA40_0==38) ) {
				alt40=1;
			}
			switch (alt40) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1543:4: (lv_widthSpec_3_0= ruleWidthSpec )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1543:4: (lv_widthSpec_3_0= ruleWidthSpec )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1544:5: lv_widthSpec_3_0= ruleWidthSpec
					{

										newCompositeNode(grammarAccess.getInputAccess().getWidthSpecWidthSpecParserRuleCall_3_0());
									
					pushFollow(FOLLOW_ruleWidthSpec_in_ruleInput4382);
					lv_widthSpec_3_0=ruleWidthSpec();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getInputRule());
										}
										set(
											current,
											"widthSpec",
											lv_widthSpec_3_0,
											"org.lflang.LF.WidthSpec");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1561:3: ( (lv_name_4_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1562:4: (lv_name_4_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1562:4: (lv_name_4_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1563:5: lv_name_4_0= RULE_ID
			{
			lv_name_4_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleInput4415); 

								newLeafNode(lv_name_4_0, grammarAccess.getInputAccess().getNameIDTerminalRuleCall_4_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getInputRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_4_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1579:3: (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )?
			int alt41=2;
			int LA41_0 = input.LA(1);
			if ( (LA41_0==27) ) {
				alt41=1;
			}
			switch (alt41) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1580:4: otherlv_5= ':' ( (lv_type_6_0= ruleType ) )
					{
					otherlv_5=(Token)match(input,27,FOLLOW_27_in_ruleInput4447); 

									newLeafNode(otherlv_5, grammarAccess.getInputAccess().getColonKeyword_5_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1584:4: ( (lv_type_6_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1585:5: (lv_type_6_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1585:5: (lv_type_6_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1586:6: lv_type_6_0= ruleType
					{

											newCompositeNode(grammarAccess.getInputAccess().getTypeTypeParserRuleCall_5_1_0());
										
					pushFollow(FOLLOW_ruleType_in_ruleInput4479);
					lv_type_6_0=ruleType();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getInputRule());
											}
											set(
												current,
												"type",
												lv_type_6_0,
												"org.lflang.LF.Type");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1604:3: (otherlv_7= ';' )?
			int alt42=2;
			int LA42_0 = input.LA(1);
			if ( (LA42_0==30) ) {
				alt42=1;
			}
			switch (alt42) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1605:4: otherlv_7= ';'
					{
					otherlv_7=(Token)match(input,30,FOLLOW_30_in_ruleInput4513); 

									newLeafNode(otherlv_7, grammarAccess.getInputAccess().getSemicolonKeyword_6());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleInput"



	// $ANTLR start "entryRuleOutput"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1614:1: entryRuleOutput returns [EObject current=null] :iv_ruleOutput= ruleOutput EOF ;
	public final EObject entryRuleOutput() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleOutput =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1614:47: (iv_ruleOutput= ruleOutput EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1615:2: iv_ruleOutput= ruleOutput EOF
			{
			 newCompositeNode(grammarAccess.getOutputRule()); 
			pushFollow(FOLLOW_ruleOutput_in_entryRuleOutput4545);
			iv_ruleOutput=ruleOutput();
			state._fsp--;

			 current =iv_ruleOutput; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleOutput4551); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleOutput"



	// $ANTLR start "ruleOutput"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1621:1: ruleOutput returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? ) ;
	public final EObject ruleOutput() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token lv_name_3_0=null;
		Token otherlv_4=null;
		Token otherlv_6=null;
		EObject lv_attributes_0_0 =null;
		EObject lv_widthSpec_2_0 =null;
		EObject lv_type_5_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1627:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1628:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1628:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1629:3: ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1629:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop43:
			while (true) {
				int alt43=2;
				int LA43_0 = input.LA(1);
				if ( (LA43_0==35) ) {
					alt43=1;
				}

				switch (alt43) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1630:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1630:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1631:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getOutputAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleOutput4597);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getOutputRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop43;
				}
			}

			otherlv_1=(Token)match(input,64,FOLLOW_64_in_ruleOutput4619); 

						newLeafNode(otherlv_1, grammarAccess.getOutputAccess().getOutputKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1652:3: ( (lv_widthSpec_2_0= ruleWidthSpec ) )?
			int alt44=2;
			int LA44_0 = input.LA(1);
			if ( (LA44_0==38) ) {
				alt44=1;
			}
			switch (alt44) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1653:4: (lv_widthSpec_2_0= ruleWidthSpec )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1653:4: (lv_widthSpec_2_0= ruleWidthSpec )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1654:5: lv_widthSpec_2_0= ruleWidthSpec
					{

										newCompositeNode(grammarAccess.getOutputAccess().getWidthSpecWidthSpecParserRuleCall_2_0());
									
					pushFollow(FOLLOW_ruleWidthSpec_in_ruleOutput4646);
					lv_widthSpec_2_0=ruleWidthSpec();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getOutputRule());
										}
										set(
											current,
											"widthSpec",
											lv_widthSpec_2_0,
											"org.lflang.LF.WidthSpec");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1671:3: ( (lv_name_3_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1672:4: (lv_name_3_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1672:4: (lv_name_3_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1673:5: lv_name_3_0= RULE_ID
			{
			lv_name_3_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleOutput4679); 

								newLeafNode(lv_name_3_0, grammarAccess.getOutputAccess().getNameIDTerminalRuleCall_3_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getOutputRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_3_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1689:3: (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )?
			int alt45=2;
			int LA45_0 = input.LA(1);
			if ( (LA45_0==27) ) {
				alt45=1;
			}
			switch (alt45) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1690:4: otherlv_4= ':' ( (lv_type_5_0= ruleType ) )
					{
					otherlv_4=(Token)match(input,27,FOLLOW_27_in_ruleOutput4711); 

									newLeafNode(otherlv_4, grammarAccess.getOutputAccess().getColonKeyword_4_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1694:4: ( (lv_type_5_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1695:5: (lv_type_5_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1695:5: (lv_type_5_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1696:6: lv_type_5_0= ruleType
					{

											newCompositeNode(grammarAccess.getOutputAccess().getTypeTypeParserRuleCall_4_1_0());
										
					pushFollow(FOLLOW_ruleType_in_ruleOutput4743);
					lv_type_5_0=ruleType();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getOutputRule());
											}
											set(
												current,
												"type",
												lv_type_5_0,
												"org.lflang.LF.Type");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1714:3: (otherlv_6= ';' )?
			int alt46=2;
			int LA46_0 = input.LA(1);
			if ( (LA46_0==30) ) {
				alt46=1;
			}
			switch (alt46) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1715:4: otherlv_6= ';'
					{
					otherlv_6=(Token)match(input,30,FOLLOW_30_in_ruleOutput4777); 

									newLeafNode(otherlv_6, grammarAccess.getOutputAccess().getSemicolonKeyword_5());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleOutput"



	// $ANTLR start "entryRuleTimer"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1724:1: entryRuleTimer returns [EObject current=null] :iv_ruleTimer= ruleTimer EOF ;
	public final EObject entryRuleTimer() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleTimer =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1724:46: (iv_ruleTimer= ruleTimer EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1725:2: iv_ruleTimer= ruleTimer EOF
			{
			 newCompositeNode(grammarAccess.getTimerRule()); 
			pushFollow(FOLLOW_ruleTimer_in_entryRuleTimer4809);
			iv_ruleTimer=ruleTimer();
			state._fsp--;

			 current =iv_ruleTimer; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTimer4815); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTimer"



	// $ANTLR start "ruleTimer"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1731:1: ruleTimer returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? ) ;
	public final EObject ruleTimer() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token lv_name_2_0=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		Token otherlv_8=null;
		EObject lv_attributes_0_0 =null;
		EObject lv_offset_4_0 =null;
		EObject lv_period_6_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1737:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1738:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1738:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1739:3: ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1739:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop47:
			while (true) {
				int alt47=2;
				int LA47_0 = input.LA(1);
				if ( (LA47_0==35) ) {
					alt47=1;
				}

				switch (alt47) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1740:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1740:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1741:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getTimerAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleTimer4861);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getTimerRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop47;
				}
			}

			otherlv_1=(Token)match(input,79,FOLLOW_79_in_ruleTimer4883); 

						newLeafNode(otherlv_1, grammarAccess.getTimerAccess().getTimerKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1762:3: ( (lv_name_2_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1763:4: (lv_name_2_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1763:4: (lv_name_2_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1764:5: lv_name_2_0= RULE_ID
			{
			lv_name_2_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleTimer4904); 

								newLeafNode(lv_name_2_0, grammarAccess.getTimerAccess().getNameIDTerminalRuleCall_2_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getTimerRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_2_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1780:3: (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )?
			int alt49=2;
			int LA49_0 = input.LA(1);
			if ( (LA49_0==18) ) {
				int LA49_1 = input.LA(2);
				if ( ((LA49_1 >= RULE_CHAR_LIT && LA49_1 <= RULE_FALSE)||LA49_1==RULE_INT||LA49_1==RULE_NEGINT||(LA49_1 >= RULE_STRING && LA49_1 <= RULE_TRUE)||LA49_1==23||LA49_1==25||LA49_1==83) ) {
					alt49=1;
				}
				else if ( (LA49_1==RULE_ID) ) {
					int LA49_4 = input.LA(3);
					if ( (LA49_4==22) ) {
						int LA49_5 = input.LA(4);
						if ( ((LA49_5 >= RULE_CHAR_LIT && LA49_5 <= RULE_FALSE)||LA49_5==RULE_INT||LA49_5==RULE_NEGINT||(LA49_5 >= RULE_STRING && LA49_5 <= RULE_TRUE)||LA49_5==23||LA49_5==25||LA49_5==83) ) {
							alt49=1;
						}
						else if ( (LA49_5==RULE_ID) ) {
							int LA49_7 = input.LA(5);
							if ( (LA49_7==19) ) {
								int LA49_6 = input.LA(6);
								if ( (LA49_6==EOF||LA49_6==RULE_ID||LA49_6==18||LA49_6==30||(LA49_6 >= 35 && LA49_6 <= 36)||LA49_6==43||LA49_6==47||(LA49_6 >= 54 && LA49_6 <= 57)||(LA49_6 >= 59 && LA49_6 <= 62)||(LA49_6 >= 64 && LA49_6 <= 69)||LA49_6==72||LA49_6==76||LA49_6==79||LA49_6==84) ) {
									alt49=1;
								}
							}
						}
					}
					else if ( (LA49_4==19) ) {
						int LA49_6 = input.LA(4);
						if ( (LA49_6==EOF||LA49_6==RULE_ID||LA49_6==18||LA49_6==30||(LA49_6 >= 35 && LA49_6 <= 36)||LA49_6==43||LA49_6==47||(LA49_6 >= 54 && LA49_6 <= 57)||(LA49_6 >= 59 && LA49_6 <= 62)||(LA49_6 >= 64 && LA49_6 <= 69)||LA49_6==72||LA49_6==76||LA49_6==79||LA49_6==84) ) {
							alt49=1;
						}
					}
				}
			}
			switch (alt49) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1781:4: otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')'
					{
					otherlv_3=(Token)match(input,18,FOLLOW_18_in_ruleTimer4936); 

									newLeafNode(otherlv_3, grammarAccess.getTimerAccess().getLeftParenthesisKeyword_3_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1785:4: ( (lv_offset_4_0= ruleExpression ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1786:5: (lv_offset_4_0= ruleExpression )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1786:5: (lv_offset_4_0= ruleExpression )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1787:6: lv_offset_4_0= ruleExpression
					{

											newCompositeNode(grammarAccess.getTimerAccess().getOffsetExpressionParserRuleCall_3_1_0());
										
					pushFollow(FOLLOW_ruleExpression_in_ruleTimer4968);
					lv_offset_4_0=ruleExpression();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getTimerRule());
											}
											set(
												current,
												"offset",
												lv_offset_4_0,
												"org.lflang.LF.Expression");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1804:4: (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )?
					int alt48=2;
					int LA48_0 = input.LA(1);
					if ( (LA48_0==22) ) {
						alt48=1;
					}
					switch (alt48) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1805:5: otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) )
							{
							otherlv_5=(Token)match(input,22,FOLLOW_22_in_ruleTimer4999); 

												newLeafNode(otherlv_5, grammarAccess.getTimerAccess().getCommaKeyword_3_2_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1809:5: ( (lv_period_6_0= ruleExpression ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1810:6: (lv_period_6_0= ruleExpression )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1810:6: (lv_period_6_0= ruleExpression )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1811:7: lv_period_6_0= ruleExpression
							{

														newCompositeNode(grammarAccess.getTimerAccess().getPeriodExpressionParserRuleCall_3_2_1_0());
													
							pushFollow(FOLLOW_ruleExpression_in_ruleTimer5036);
							lv_period_6_0=ruleExpression();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getTimerRule());
														}
														set(
															current,
															"period",
															lv_period_6_0,
															"org.lflang.LF.Expression");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

					}

					otherlv_7=(Token)match(input,19,FOLLOW_19_in_ruleTimer5070); 

									newLeafNode(otherlv_7, grammarAccess.getTimerAccess().getRightParenthesisKeyword_3_3());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1834:3: (otherlv_8= ';' )?
			int alt50=2;
			int LA50_0 = input.LA(1);
			if ( (LA50_0==30) ) {
				alt50=1;
			}
			switch (alt50) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1835:4: otherlv_8= ';'
					{
					otherlv_8=(Token)match(input,30,FOLLOW_30_in_ruleTimer5091); 

									newLeafNode(otherlv_8, grammarAccess.getTimerAccess().getSemicolonKeyword_4());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTimer"



	// $ANTLR start "entryRuleBoolean"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1844:1: entryRuleBoolean returns [String current=null] :iv_ruleBoolean= ruleBoolean EOF ;
	public final String entryRuleBoolean() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleBoolean =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1844:47: (iv_ruleBoolean= ruleBoolean EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1845:2: iv_ruleBoolean= ruleBoolean EOF
			{
			 newCompositeNode(grammarAccess.getBooleanRule()); 
			pushFollow(FOLLOW_ruleBoolean_in_entryRuleBoolean5123);
			iv_ruleBoolean=ruleBoolean();
			state._fsp--;

			 current =iv_ruleBoolean.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleBoolean5129); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleBoolean"



	// $ANTLR start "ruleBoolean"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1851:1: ruleBoolean returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_TRUE_0= RULE_TRUE |this_FALSE_1= RULE_FALSE ) ;
	public final AntlrDatatypeRuleToken ruleBoolean() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_TRUE_0=null;
		Token this_FALSE_1=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1857:2: ( (this_TRUE_0= RULE_TRUE |this_FALSE_1= RULE_FALSE ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1858:2: (this_TRUE_0= RULE_TRUE |this_FALSE_1= RULE_FALSE )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1858:2: (this_TRUE_0= RULE_TRUE |this_FALSE_1= RULE_FALSE )
			int alt51=2;
			int LA51_0 = input.LA(1);
			if ( (LA51_0==RULE_TRUE) ) {
				alt51=1;
			}
			else if ( (LA51_0==RULE_FALSE) ) {
				alt51=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 51, 0, input);
				throw nvae;
			}

			switch (alt51) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1859:3: this_TRUE_0= RULE_TRUE
					{
					this_TRUE_0=(Token)match(input,RULE_TRUE,FOLLOW_RULE_TRUE_in_ruleBoolean5158); 

								current.merge(this_TRUE_0);
							

								newLeafNode(this_TRUE_0, grammarAccess.getBooleanAccess().getTRUETerminalRuleCall_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1867:3: this_FALSE_1= RULE_FALSE
					{
					this_FALSE_1=(Token)match(input,RULE_FALSE,FOLLOW_RULE_FALSE_in_ruleBoolean5180); 

								current.merge(this_FALSE_1);
							

								newLeafNode(this_FALSE_1, grammarAccess.getBooleanAccess().getFALSETerminalRuleCall_1());
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleBoolean"



	// $ANTLR start "entryRuleMode"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1878:1: entryRuleMode returns [EObject current=null] :iv_ruleMode= ruleMode EOF ;
	public final EObject entryRuleMode() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleMode =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1878:45: (iv_ruleMode= ruleMode EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1879:2: iv_ruleMode= ruleMode EOF
			{
			 newCompositeNode(grammarAccess.getModeRule()); 
			pushFollow(FOLLOW_ruleMode_in_entryRuleMode5210);
			iv_ruleMode=ruleMode();
			state._fsp--;

			 current =iv_ruleMode; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleMode5216); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleMode"



	// $ANTLR start "ruleMode"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1885:1: ruleMode returns [EObject current=null] : ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' ) ;
	public final EObject ruleMode() throws RecognitionException {
		EObject current = null;


		Token lv_initial_1_0=null;
		Token otherlv_2=null;
		Token lv_name_3_0=null;
		Token otherlv_4=null;
		Token otherlv_11=null;
		EObject lv_stateVars_5_0 =null;
		EObject lv_timers_6_0 =null;
		EObject lv_actions_7_0 =null;
		EObject lv_instantiations_8_0 =null;
		EObject lv_connections_9_0 =null;
		EObject lv_reactions_10_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1891:2: ( ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1892:2: ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1892:2: ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1893:3: () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}'
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1893:3: ()
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1894:4: 
			{

							current = forceCreateModelElement(
								grammarAccess.getModeAccess().getModeAction_0(),
								current);
						
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1900:3: ( (lv_initial_1_0= 'initial' ) )?
			int alt52=2;
			int LA52_0 = input.LA(1);
			if ( (LA52_0==54) ) {
				alt52=1;
			}
			switch (alt52) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1901:4: (lv_initial_1_0= 'initial' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1901:4: (lv_initial_1_0= 'initial' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1902:5: lv_initial_1_0= 'initial'
					{
					lv_initial_1_0=(Token)match(input,54,FOLLOW_54_in_ruleMode5269); 

										newLeafNode(lv_initial_1_0, grammarAccess.getModeAccess().getInitialInitialKeyword_1_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getModeRule());
										}
										setWithLastConsumed(current, "initial", lv_initial_1_0 != null, "initial");
									
					}

					}
					break;

			}

			otherlv_2=(Token)match(input,60,FOLLOW_60_in_ruleMode5297); 

						newLeafNode(otherlv_2, grammarAccess.getModeAccess().getModeKeyword_2());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1918:3: ( (lv_name_3_0= RULE_ID ) )?
			int alt53=2;
			int LA53_0 = input.LA(1);
			if ( (LA53_0==RULE_ID) ) {
				alt53=1;
			}
			switch (alt53) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1919:4: (lv_name_3_0= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1919:4: (lv_name_3_0= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1920:5: lv_name_3_0= RULE_ID
					{
					lv_name_3_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleMode5318); 

										newLeafNode(lv_name_3_0, grammarAccess.getModeAccess().getNameIDTerminalRuleCall_3_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getModeRule());
										}
										setWithLastConsumed(
											current,
											"name",
											lv_name_3_0,
											"org.lflang.LF.ID");
									
					}

					}
					break;

			}

			otherlv_4=(Token)match(input,82,FOLLOW_82_in_ruleMode5346); 

						newLeafNode(otherlv_4, grammarAccess.getModeAccess().getLeftCurlyBracketKeyword_4());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1940:3: ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )*
			loop54:
			while (true) {
				int alt54=7;
				alt54 = dfa54.predict(input);
				switch (alt54) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1941:4: ( (lv_stateVars_5_0= ruleStateVar ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1941:4: ( (lv_stateVars_5_0= ruleStateVar ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1942:5: (lv_stateVars_5_0= ruleStateVar )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1942:5: (lv_stateVars_5_0= ruleStateVar )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1943:6: lv_stateVars_5_0= ruleStateVar
					{

											newCompositeNode(grammarAccess.getModeAccess().getStateVarsStateVarParserRuleCall_5_0_0());
										
					pushFollow(FOLLOW_ruleStateVar_in_ruleMode5381);
					lv_stateVars_5_0=ruleStateVar();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getModeRule());
											}
											add(
												current,
												"stateVars",
												lv_stateVars_5_0,
												"org.lflang.LF.StateVar");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1961:4: ( (lv_timers_6_0= ruleTimer ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1961:4: ( (lv_timers_6_0= ruleTimer ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1962:5: (lv_timers_6_0= ruleTimer )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1962:5: (lv_timers_6_0= ruleTimer )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1963:6: lv_timers_6_0= ruleTimer
					{

											newCompositeNode(grammarAccess.getModeAccess().getTimersTimerParserRuleCall_5_1_0());
										
					pushFollow(FOLLOW_ruleTimer_in_ruleMode5435);
					lv_timers_6_0=ruleTimer();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getModeRule());
											}
											add(
												current,
												"timers",
												lv_timers_6_0,
												"org.lflang.LF.Timer");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1981:4: ( (lv_actions_7_0= ruleAction ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1981:4: ( (lv_actions_7_0= ruleAction ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1982:5: (lv_actions_7_0= ruleAction )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1982:5: (lv_actions_7_0= ruleAction )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:1983:6: lv_actions_7_0= ruleAction
					{

											newCompositeNode(grammarAccess.getModeAccess().getActionsActionParserRuleCall_5_2_0());
										
					pushFollow(FOLLOW_ruleAction_in_ruleMode5489);
					lv_actions_7_0=ruleAction();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getModeRule());
											}
											add(
												current,
												"actions",
												lv_actions_7_0,
												"org.lflang.LF.Action");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2001:4: ( (lv_instantiations_8_0= ruleInstantiation ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2001:4: ( (lv_instantiations_8_0= ruleInstantiation ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2002:5: (lv_instantiations_8_0= ruleInstantiation )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2002:5: (lv_instantiations_8_0= ruleInstantiation )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2003:6: lv_instantiations_8_0= ruleInstantiation
					{

											newCompositeNode(grammarAccess.getModeAccess().getInstantiationsInstantiationParserRuleCall_5_3_0());
										
					pushFollow(FOLLOW_ruleInstantiation_in_ruleMode5543);
					lv_instantiations_8_0=ruleInstantiation();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getModeRule());
											}
											add(
												current,
												"instantiations",
												lv_instantiations_8_0,
												"org.lflang.LF.Instantiation");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 5 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2021:4: ( (lv_connections_9_0= ruleConnection ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2021:4: ( (lv_connections_9_0= ruleConnection ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2022:5: (lv_connections_9_0= ruleConnection )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2022:5: (lv_connections_9_0= ruleConnection )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2023:6: lv_connections_9_0= ruleConnection
					{

											newCompositeNode(grammarAccess.getModeAccess().getConnectionsConnectionParserRuleCall_5_4_0());
										
					pushFollow(FOLLOW_ruleConnection_in_ruleMode5597);
					lv_connections_9_0=ruleConnection();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getModeRule());
											}
											add(
												current,
												"connections",
												lv_connections_9_0,
												"org.lflang.LF.Connection");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;
				case 6 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2041:4: ( (lv_reactions_10_0= ruleReaction ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2041:4: ( (lv_reactions_10_0= ruleReaction ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2042:5: (lv_reactions_10_0= ruleReaction )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2042:5: (lv_reactions_10_0= ruleReaction )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2043:6: lv_reactions_10_0= ruleReaction
					{

											newCompositeNode(grammarAccess.getModeAccess().getReactionsReactionParserRuleCall_5_5_0());
										
					pushFollow(FOLLOW_ruleReaction_in_ruleMode5651);
					lv_reactions_10_0=ruleReaction();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getModeRule());
											}
											add(
												current,
												"reactions",
												lv_reactions_10_0,
												"org.lflang.LF.Reaction");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

				default :
					break loop54;
				}
			}

			otherlv_11=(Token)match(input,84,FOLLOW_84_in_ruleMode5680); 

						newLeafNode(otherlv_11, grammarAccess.getModeAccess().getRightCurlyBracketKeyword_6());
					
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleMode"



	// $ANTLR start "entryRuleAction"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2069:1: entryRuleAction returns [EObject current=null] :iv_ruleAction= ruleAction EOF ;
	public final EObject entryRuleAction() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleAction =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2069:47: (iv_ruleAction= ruleAction EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2070:2: iv_ruleAction= ruleAction EOF
			{
			 newCompositeNode(grammarAccess.getActionRule()); 
			pushFollow(FOLLOW_ruleAction_in_entryRuleAction5706);
			iv_ruleAction=ruleAction();
			state._fsp--;

			 current =iv_ruleAction; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleAction5712); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleAction"



	// $ANTLR start "ruleAction"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2076:1: ruleAction returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? ) ;
	public final EObject ruleAction() throws RecognitionException {
		EObject current = null;


		Token otherlv_2=null;
		Token lv_name_3_0=null;
		Token otherlv_4=null;
		Token otherlv_6=null;
		Token otherlv_8=null;
		Token lv_policy_9_0=null;
		Token otherlv_10=null;
		Token otherlv_11=null;
		Token otherlv_13=null;
		EObject lv_attributes_0_0 =null;
		Enumerator lv_origin_1_0 =null;
		EObject lv_minDelay_5_0 =null;
		EObject lv_minSpacing_7_0 =null;
		EObject lv_type_12_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2082:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2083:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2083:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2084:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2084:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop55:
			while (true) {
				int alt55=2;
				int LA55_0 = input.LA(1);
				if ( (LA55_0==35) ) {
					alt55=1;
				}

				switch (alt55) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2085:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2085:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2086:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getActionAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleAction5758);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getActionRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop55;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2103:3: ( (lv_origin_1_0= ruleActionOrigin ) )?
			int alt56=2;
			int LA56_0 = input.LA(1);
			if ( (LA56_0==36||LA56_0==57||LA56_0==65) ) {
				alt56=1;
			}
			switch (alt56) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2104:4: (lv_origin_1_0= ruleActionOrigin )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2104:4: (lv_origin_1_0= ruleActionOrigin )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2105:5: lv_origin_1_0= ruleActionOrigin
					{

										newCompositeNode(grammarAccess.getActionAccess().getOriginActionOriginEnumRuleCall_1_0());
									
					pushFollow(FOLLOW_ruleActionOrigin_in_ruleAction5797);
					lv_origin_1_0=ruleActionOrigin();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getActionRule());
										}
										set(
											current,
											"origin",
											lv_origin_1_0,
											"org.lflang.LF.ActionOrigin");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			otherlv_2=(Token)match(input,43,FOLLOW_43_in_ruleAction5819); 

						newLeafNode(otherlv_2, grammarAccess.getActionAccess().getActionKeyword_2());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2126:3: ( (lv_name_3_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2127:4: (lv_name_3_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2127:4: (lv_name_3_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2128:5: lv_name_3_0= RULE_ID
			{
			lv_name_3_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleAction5840); 

								newLeafNode(lv_name_3_0, grammarAccess.getActionAccess().getNameIDTerminalRuleCall_3_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getActionRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_3_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2144:3: (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )?
			int alt59=2;
			int LA59_0 = input.LA(1);
			if ( (LA59_0==18) ) {
				int LA59_1 = input.LA(2);
				if ( ((LA59_1 >= RULE_CHAR_LIT && LA59_1 <= RULE_FALSE)||LA59_1==RULE_INT||LA59_1==RULE_NEGINT||(LA59_1 >= RULE_STRING && LA59_1 <= RULE_TRUE)||LA59_1==23||LA59_1==25||LA59_1==83) ) {
					alt59=1;
				}
				else if ( (LA59_1==RULE_ID) ) {
					int LA59_4 = input.LA(3);
					if ( (LA59_4==22) ) {
						int LA59_5 = input.LA(4);
						if ( ((LA59_5 >= RULE_CHAR_LIT && LA59_5 <= RULE_FALSE)||LA59_5==RULE_INT||LA59_5==RULE_NEGINT||(LA59_5 >= RULE_STRING && LA59_5 <= RULE_TRUE)||LA59_5==23||LA59_5==25||LA59_5==83) ) {
							alt59=1;
						}
						else if ( (LA59_5==RULE_ID) ) {
							int LA59_7 = input.LA(5);
							if ( (LA59_7==22) ) {
								int LA59_8 = input.LA(6);
								if ( (LA59_8==RULE_STRING) ) {
									alt59=1;
								}
							}
							else if ( (LA59_7==19) ) {
								int LA59_6 = input.LA(6);
								if ( (LA59_6==EOF||LA59_6==RULE_ID||LA59_6==18||LA59_6==27||LA59_6==30||(LA59_6 >= 35 && LA59_6 <= 36)||LA59_6==43||LA59_6==47||(LA59_6 >= 54 && LA59_6 <= 57)||(LA59_6 >= 59 && LA59_6 <= 62)||(LA59_6 >= 64 && LA59_6 <= 69)||LA59_6==72||LA59_6==76||LA59_6==79||LA59_6==84) ) {
									alt59=1;
								}
							}
						}
					}
					else if ( (LA59_4==19) ) {
						int LA59_6 = input.LA(4);
						if ( (LA59_6==EOF||LA59_6==RULE_ID||LA59_6==18||LA59_6==27||LA59_6==30||(LA59_6 >= 35 && LA59_6 <= 36)||LA59_6==43||LA59_6==47||(LA59_6 >= 54 && LA59_6 <= 57)||(LA59_6 >= 59 && LA59_6 <= 62)||(LA59_6 >= 64 && LA59_6 <= 69)||LA59_6==72||LA59_6==76||LA59_6==79||LA59_6==84) ) {
							alt59=1;
						}
					}
				}
			}
			switch (alt59) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2145:4: otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')'
					{
					otherlv_4=(Token)match(input,18,FOLLOW_18_in_ruleAction5872); 

									newLeafNode(otherlv_4, grammarAccess.getActionAccess().getLeftParenthesisKeyword_4_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2149:4: ( (lv_minDelay_5_0= ruleExpression ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2150:5: (lv_minDelay_5_0= ruleExpression )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2150:5: (lv_minDelay_5_0= ruleExpression )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2151:6: lv_minDelay_5_0= ruleExpression
					{

											newCompositeNode(grammarAccess.getActionAccess().getMinDelayExpressionParserRuleCall_4_1_0());
										
					pushFollow(FOLLOW_ruleExpression_in_ruleAction5904);
					lv_minDelay_5_0=ruleExpression();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getActionRule());
											}
											set(
												current,
												"minDelay",
												lv_minDelay_5_0,
												"org.lflang.LF.Expression");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2168:4: (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )?
					int alt58=2;
					int LA58_0 = input.LA(1);
					if ( (LA58_0==22) ) {
						alt58=1;
					}
					switch (alt58) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2169:5: otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )?
							{
							otherlv_6=(Token)match(input,22,FOLLOW_22_in_ruleAction5935); 

												newLeafNode(otherlv_6, grammarAccess.getActionAccess().getCommaKeyword_4_2_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2173:5: ( (lv_minSpacing_7_0= ruleExpression ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2174:6: (lv_minSpacing_7_0= ruleExpression )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2174:6: (lv_minSpacing_7_0= ruleExpression )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2175:7: lv_minSpacing_7_0= ruleExpression
							{

														newCompositeNode(grammarAccess.getActionAccess().getMinSpacingExpressionParserRuleCall_4_2_1_0());
													
							pushFollow(FOLLOW_ruleExpression_in_ruleAction5972);
							lv_minSpacing_7_0=ruleExpression();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getActionRule());
														}
														set(
															current,
															"minSpacing",
															lv_minSpacing_7_0,
															"org.lflang.LF.Expression");
														afterParserOrEnumRuleCall();
													
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2192:5: (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )?
							int alt57=2;
							int LA57_0 = input.LA(1);
							if ( (LA57_0==22) ) {
								alt57=1;
							}
							switch (alt57) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2193:6: otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) )
									{
									otherlv_8=(Token)match(input,22,FOLLOW_22_in_ruleAction6008); 

															newLeafNode(otherlv_8, grammarAccess.getActionAccess().getCommaKeyword_4_2_2_0());
														
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2197:6: ( (lv_policy_9_0= RULE_STRING ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2198:7: (lv_policy_9_0= RULE_STRING )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2198:7: (lv_policy_9_0= RULE_STRING )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2199:8: lv_policy_9_0= RULE_STRING
									{
									lv_policy_9_0=(Token)match(input,RULE_STRING,FOLLOW_RULE_STRING_in_ruleAction6041); 

																	newLeafNode(lv_policy_9_0, grammarAccess.getActionAccess().getPolicySTRINGTerminalRuleCall_4_2_2_1_0());
																

																	if (current==null) {
																		current = createModelElement(grammarAccess.getActionRule());
																	}
																	setWithLastConsumed(
																		current,
																		"policy",
																		lv_policy_9_0,
																		"org.lflang.LF.STRING");
																
									}

									}

									}
									break;

							}

							}
							break;

					}

					otherlv_10=(Token)match(input,19,FOLLOW_19_in_ruleAction6094); 

									newLeafNode(otherlv_10, grammarAccess.getActionAccess().getRightParenthesisKeyword_4_3());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2222:3: (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )?
			int alt60=2;
			int LA60_0 = input.LA(1);
			if ( (LA60_0==27) ) {
				alt60=1;
			}
			switch (alt60) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2223:4: otherlv_11= ':' ( (lv_type_12_0= ruleType ) )
					{
					otherlv_11=(Token)match(input,27,FOLLOW_27_in_ruleAction6115); 

									newLeafNode(otherlv_11, grammarAccess.getActionAccess().getColonKeyword_5_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2227:4: ( (lv_type_12_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2228:5: (lv_type_12_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2228:5: (lv_type_12_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2229:6: lv_type_12_0= ruleType
					{

											newCompositeNode(grammarAccess.getActionAccess().getTypeTypeParserRuleCall_5_1_0());
										
					pushFollow(FOLLOW_ruleType_in_ruleAction6147);
					lv_type_12_0=ruleType();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getActionRule());
											}
											set(
												current,
												"type",
												lv_type_12_0,
												"org.lflang.LF.Type");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2247:3: (otherlv_13= ';' )?
			int alt61=2;
			int LA61_0 = input.LA(1);
			if ( (LA61_0==30) ) {
				alt61=1;
			}
			switch (alt61) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2248:4: otherlv_13= ';'
					{
					otherlv_13=(Token)match(input,30,FOLLOW_30_in_ruleAction6181); 

									newLeafNode(otherlv_13, grammarAccess.getActionAccess().getSemicolonKeyword_6());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleAction"



	// $ANTLR start "entryRuleReaction"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2257:1: entryRuleReaction returns [EObject current=null] :iv_ruleReaction= ruleReaction EOF ;
	public final EObject entryRuleReaction() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleReaction =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2257:49: (iv_ruleReaction= ruleReaction EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2258:2: iv_ruleReaction= ruleReaction EOF
			{
			 newCompositeNode(grammarAccess.getReactionRule()); 
			pushFollow(FOLLOW_ruleReaction_in_entryRuleReaction6213);
			iv_ruleReaction=ruleReaction();
			state._fsp--;

			 current =iv_ruleReaction; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleReaction6219); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleReaction"



	// $ANTLR start "ruleReaction"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2264:1: ruleReaction returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? ) ;
	public final EObject ruleReaction() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token lv_mutation_2_0=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		Token otherlv_9=null;
		Token otherlv_11=null;
		Token otherlv_13=null;
		EObject lv_attributes_0_0 =null;
		EObject lv_triggers_4_0 =null;
		EObject lv_triggers_6_0 =null;
		EObject lv_sources_8_0 =null;
		EObject lv_sources_10_0 =null;
		EObject lv_effects_12_0 =null;
		EObject lv_effects_14_0 =null;
		EObject lv_code_15_0 =null;
		EObject lv_stp_16_0 =null;
		EObject lv_deadline_17_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2270:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2271:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2271:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2272:3: ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2272:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop62:
			while (true) {
				int alt62=2;
				int LA62_0 = input.LA(1);
				if ( (LA62_0==35) ) {
					alt62=1;
				}

				switch (alt62) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2273:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2273:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2274:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getReactionAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleReaction6265);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getReactionRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop62;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2291:3: (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) )
			int alt63=2;
			int LA63_0 = input.LA(1);
			if ( (LA63_0==69) ) {
				alt63=1;
			}
			else if ( (LA63_0==62) ) {
				alt63=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 63, 0, input);
				throw nvae;
			}

			switch (alt63) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2292:4: otherlv_1= 'reaction'
					{
					otherlv_1=(Token)match(input,69,FOLLOW_69_in_ruleReaction6292); 

									newLeafNode(otherlv_1, grammarAccess.getReactionAccess().getReactionKeyword_1_0());
								
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2297:4: ( (lv_mutation_2_0= 'mutation' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2297:4: ( (lv_mutation_2_0= 'mutation' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2298:5: (lv_mutation_2_0= 'mutation' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2298:5: (lv_mutation_2_0= 'mutation' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2299:6: lv_mutation_2_0= 'mutation'
					{
					lv_mutation_2_0=(Token)match(input,62,FOLLOW_62_in_ruleReaction6326); 

											newLeafNode(lv_mutation_2_0, grammarAccess.getReactionAccess().getMutationMutationKeyword_1_1_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getReactionRule());
											}
											setWithLastConsumed(current, "mutation", lv_mutation_2_0 != null, "mutation");
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2312:3: (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )?
			int alt66=2;
			int LA66_0 = input.LA(1);
			if ( (LA66_0==18) ) {
				alt66=1;
			}
			switch (alt66) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2313:4: otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')'
					{
					otherlv_3=(Token)match(input,18,FOLLOW_18_in_ruleReaction6366); 

									newLeafNode(otherlv_3, grammarAccess.getReactionAccess().getLeftParenthesisKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2317:4: ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )?
					int alt65=2;
					int LA65_0 = input.LA(1);
					if ( (LA65_0==RULE_ID||LA65_0==56||LA65_0==72||(LA65_0 >= 74 && LA65_0 <= 75)) ) {
						alt65=1;
					}
					switch (alt65) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2318:5: ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )*
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2318:5: ( (lv_triggers_4_0= ruleTriggerRef ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2319:6: (lv_triggers_4_0= ruleTriggerRef )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2319:6: (lv_triggers_4_0= ruleTriggerRef )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2320:7: lv_triggers_4_0= ruleTriggerRef
							{

														newCompositeNode(grammarAccess.getReactionAccess().getTriggersTriggerRefParserRuleCall_2_1_0_0());
													
							pushFollow(FOLLOW_ruleTriggerRef_in_ruleReaction6407);
							lv_triggers_4_0=ruleTriggerRef();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getReactionRule());
														}
														add(
															current,
															"triggers",
															lv_triggers_4_0,
															"org.lflang.LF.TriggerRef");
														afterParserOrEnumRuleCall();
													
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2337:5: (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )*
							loop64:
							while (true) {
								int alt64=2;
								int LA64_0 = input.LA(1);
								if ( (LA64_0==22) ) {
									alt64=1;
								}

								switch (alt64) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2338:6: otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) )
									{
									otherlv_5=(Token)match(input,22,FOLLOW_22_in_ruleReaction6443); 

															newLeafNode(otherlv_5, grammarAccess.getReactionAccess().getCommaKeyword_2_1_1_0());
														
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2342:6: ( (lv_triggers_6_0= ruleTriggerRef ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2343:7: (lv_triggers_6_0= ruleTriggerRef )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2343:7: (lv_triggers_6_0= ruleTriggerRef )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2344:8: lv_triggers_6_0= ruleTriggerRef
									{

																	newCompositeNode(grammarAccess.getReactionAccess().getTriggersTriggerRefParserRuleCall_2_1_1_1_0());
																
									pushFollow(FOLLOW_ruleTriggerRef_in_ruleReaction6485);
									lv_triggers_6_0=ruleTriggerRef();
									state._fsp--;


																	if (current==null) {
																		current = createModelElementForParent(grammarAccess.getReactionRule());
																	}
																	add(
																		current,
																		"triggers",
																		lv_triggers_6_0,
																		"org.lflang.LF.TriggerRef");
																	afterParserOrEnumRuleCall();
																
									}

									}

									}
									break;

								default :
									break loop64;
								}
							}

							}
							break;

					}

					otherlv_7=(Token)match(input,19,FOLLOW_19_in_ruleReaction6529); 

									newLeafNode(otherlv_7, grammarAccess.getReactionAccess().getRightParenthesisKeyword_2_2());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2368:3: ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )?
			int alt68=2;
			int LA68_0 = input.LA(1);
			if ( (LA68_0==RULE_ID||LA68_0==56) ) {
				alt68=1;
			}
			switch (alt68) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2369:4: ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )*
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2369:4: ( (lv_sources_8_0= ruleVarRef ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2370:5: (lv_sources_8_0= ruleVarRef )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2370:5: (lv_sources_8_0= ruleVarRef )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2371:6: lv_sources_8_0= ruleVarRef
					{

											newCompositeNode(grammarAccess.getReactionAccess().getSourcesVarRefParserRuleCall_3_0_0());
										
					pushFollow(FOLLOW_ruleVarRef_in_ruleReaction6570);
					lv_sources_8_0=ruleVarRef();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactionRule());
											}
											add(
												current,
												"sources",
												lv_sources_8_0,
												"org.lflang.LF.VarRef");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2388:4: (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )*
					loop67:
					while (true) {
						int alt67=2;
						int LA67_0 = input.LA(1);
						if ( (LA67_0==22) ) {
							alt67=1;
						}

						switch (alt67) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2389:5: otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) )
							{
							otherlv_9=(Token)match(input,22,FOLLOW_22_in_ruleReaction6601); 

												newLeafNode(otherlv_9, grammarAccess.getReactionAccess().getCommaKeyword_3_1_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2393:5: ( (lv_sources_10_0= ruleVarRef ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2394:6: (lv_sources_10_0= ruleVarRef )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2394:6: (lv_sources_10_0= ruleVarRef )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2395:7: lv_sources_10_0= ruleVarRef
							{

														newCompositeNode(grammarAccess.getReactionAccess().getSourcesVarRefParserRuleCall_3_1_1_0());
													
							pushFollow(FOLLOW_ruleVarRef_in_ruleReaction6638);
							lv_sources_10_0=ruleVarRef();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getReactionRule());
														}
														add(
															current,
															"sources",
															lv_sources_10_0,
															"org.lflang.LF.VarRef");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop67;
						}
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2414:3: (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )?
			int alt70=2;
			int LA70_0 = input.LA(1);
			if ( (LA70_0==24) ) {
				alt70=1;
			}
			switch (alt70) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2415:4: otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )*
					{
					otherlv_11=(Token)match(input,24,FOLLOW_24_in_ruleReaction6681); 

									newLeafNode(otherlv_11, grammarAccess.getReactionAccess().getHyphenMinusGreaterThanSignKeyword_4_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2419:4: ( (lv_effects_12_0= ruleVarRefOrModeTransition ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2420:5: (lv_effects_12_0= ruleVarRefOrModeTransition )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2420:5: (lv_effects_12_0= ruleVarRefOrModeTransition )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2421:6: lv_effects_12_0= ruleVarRefOrModeTransition
					{

											newCompositeNode(grammarAccess.getReactionAccess().getEffectsVarRefOrModeTransitionParserRuleCall_4_1_0());
										
					pushFollow(FOLLOW_ruleVarRefOrModeTransition_in_ruleReaction6713);
					lv_effects_12_0=ruleVarRefOrModeTransition();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getReactionRule());
											}
											add(
												current,
												"effects",
												lv_effects_12_0,
												"org.lflang.LF.VarRefOrModeTransition");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2438:4: (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )*
					loop69:
					while (true) {
						int alt69=2;
						int LA69_0 = input.LA(1);
						if ( (LA69_0==22) ) {
							alt69=1;
						}

						switch (alt69) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2439:5: otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) )
							{
							otherlv_13=(Token)match(input,22,FOLLOW_22_in_ruleReaction6744); 

												newLeafNode(otherlv_13, grammarAccess.getReactionAccess().getCommaKeyword_4_2_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2443:5: ( (lv_effects_14_0= ruleVarRefOrModeTransition ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2444:6: (lv_effects_14_0= ruleVarRefOrModeTransition )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2444:6: (lv_effects_14_0= ruleVarRefOrModeTransition )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2445:7: lv_effects_14_0= ruleVarRefOrModeTransition
							{

														newCompositeNode(grammarAccess.getReactionAccess().getEffectsVarRefOrModeTransitionParserRuleCall_4_2_1_0());
													
							pushFollow(FOLLOW_ruleVarRefOrModeTransition_in_ruleReaction6781);
							lv_effects_14_0=ruleVarRefOrModeTransition();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getReactionRule());
														}
														add(
															current,
															"effects",
															lv_effects_14_0,
															"org.lflang.LF.VarRefOrModeTransition");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop69;
						}
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2464:3: ( (lv_code_15_0= ruleCode ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2465:4: (lv_code_15_0= ruleCode )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2465:4: (lv_code_15_0= ruleCode )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2466:5: lv_code_15_0= ruleCode
			{

								newCompositeNode(grammarAccess.getReactionAccess().getCodeCodeParserRuleCall_5_0());
							
			pushFollow(FOLLOW_ruleCode_in_ruleReaction6836);
			lv_code_15_0=ruleCode();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getReactionRule());
								}
								set(
									current,
									"code",
									lv_code_15_0,
									"org.lflang.LF.Code");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2483:3: ( (lv_stp_16_0= ruleSTP ) )?
			int alt71=2;
			int LA71_0 = input.LA(1);
			if ( (LA71_0==37) ) {
				alt71=1;
			}
			switch (alt71) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2484:4: (lv_stp_16_0= ruleSTP )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2484:4: (lv_stp_16_0= ruleSTP )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2485:5: lv_stp_16_0= ruleSTP
					{

										newCompositeNode(grammarAccess.getReactionAccess().getStpSTPParserRuleCall_6_0());
									
					pushFollow(FOLLOW_ruleSTP_in_ruleReaction6874);
					lv_stp_16_0=ruleSTP();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getReactionRule());
										}
										set(
											current,
											"stp",
											lv_stp_16_0,
											"org.lflang.LF.STP");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2502:3: ( (lv_deadline_17_0= ruleDeadline ) )?
			int alt72=2;
			int LA72_0 = input.LA(1);
			if ( (LA72_0==48) ) {
				alt72=1;
			}
			switch (alt72) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2503:4: (lv_deadline_17_0= ruleDeadline )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2503:4: (lv_deadline_17_0= ruleDeadline )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2504:5: lv_deadline_17_0= ruleDeadline
					{

										newCompositeNode(grammarAccess.getReactionAccess().getDeadlineDeadlineParserRuleCall_7_0());
									
					pushFollow(FOLLOW_ruleDeadline_in_ruleReaction6913);
					lv_deadline_17_0=ruleDeadline();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getReactionRule());
										}
										set(
											current,
											"deadline",
											lv_deadline_17_0,
											"org.lflang.LF.Deadline");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleReaction"



	// $ANTLR start "entryRuleTriggerRef"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2525:1: entryRuleTriggerRef returns [EObject current=null] :iv_ruleTriggerRef= ruleTriggerRef EOF ;
	public final EObject entryRuleTriggerRef() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleTriggerRef =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2525:51: (iv_ruleTriggerRef= ruleTriggerRef EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2526:2: iv_ruleTriggerRef= ruleTriggerRef EOF
			{
			 newCompositeNode(grammarAccess.getTriggerRefRule()); 
			pushFollow(FOLLOW_ruleTriggerRef_in_entryRuleTriggerRef6951);
			iv_ruleTriggerRef=ruleTriggerRef();
			state._fsp--;

			 current =iv_ruleTriggerRef; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTriggerRef6957); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTriggerRef"



	// $ANTLR start "ruleTriggerRef"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2532:1: ruleTriggerRef returns [EObject current=null] : (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef |this_VarRef_1= ruleVarRef ) ;
	public final EObject ruleTriggerRef() throws RecognitionException {
		EObject current = null;


		EObject this_BuiltinTriggerRef_0 =null;
		EObject this_VarRef_1 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2538:2: ( (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef |this_VarRef_1= ruleVarRef ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2539:2: (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef |this_VarRef_1= ruleVarRef )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2539:2: (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef |this_VarRef_1= ruleVarRef )
			int alt73=2;
			int LA73_0 = input.LA(1);
			if ( (LA73_0==72||(LA73_0 >= 74 && LA73_0 <= 75)) ) {
				alt73=1;
			}
			else if ( (LA73_0==RULE_ID||LA73_0==56) ) {
				alt73=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 73, 0, input);
				throw nvae;
			}

			switch (alt73) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2540:3: this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef
					{

								newCompositeNode(grammarAccess.getTriggerRefAccess().getBuiltinTriggerRefParserRuleCall_0());
							
					pushFollow(FOLLOW_ruleBuiltinTriggerRef_in_ruleTriggerRef6990);
					this_BuiltinTriggerRef_0=ruleBuiltinTriggerRef();
					state._fsp--;


								current = this_BuiltinTriggerRef_0;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2549:3: this_VarRef_1= ruleVarRef
					{

								newCompositeNode(grammarAccess.getTriggerRefAccess().getVarRefParserRuleCall_1());
							
					pushFollow(FOLLOW_ruleVarRef_in_ruleTriggerRef7012);
					this_VarRef_1=ruleVarRef();
					state._fsp--;


								current = this_VarRef_1;
								afterParserOrEnumRuleCall();
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTriggerRef"



	// $ANTLR start "entryRuleBuiltinTriggerRef"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2561:1: entryRuleBuiltinTriggerRef returns [EObject current=null] :iv_ruleBuiltinTriggerRef= ruleBuiltinTriggerRef EOF ;
	public final EObject entryRuleBuiltinTriggerRef() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleBuiltinTriggerRef =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2561:58: (iv_ruleBuiltinTriggerRef= ruleBuiltinTriggerRef EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2562:2: iv_ruleBuiltinTriggerRef= ruleBuiltinTriggerRef EOF
			{
			 newCompositeNode(grammarAccess.getBuiltinTriggerRefRule()); 
			pushFollow(FOLLOW_ruleBuiltinTriggerRef_in_entryRuleBuiltinTriggerRef7038);
			iv_ruleBuiltinTriggerRef=ruleBuiltinTriggerRef();
			state._fsp--;

			 current =iv_ruleBuiltinTriggerRef; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleBuiltinTriggerRef7044); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleBuiltinTriggerRef"



	// $ANTLR start "ruleBuiltinTriggerRef"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2568:1: ruleBuiltinTriggerRef returns [EObject current=null] : ( (lv_type_0_0= ruleBuiltinTrigger ) ) ;
	public final EObject ruleBuiltinTriggerRef() throws RecognitionException {
		EObject current = null;


		Enumerator lv_type_0_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2574:2: ( ( (lv_type_0_0= ruleBuiltinTrigger ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2575:2: ( (lv_type_0_0= ruleBuiltinTrigger ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2575:2: ( (lv_type_0_0= ruleBuiltinTrigger ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2576:3: (lv_type_0_0= ruleBuiltinTrigger )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2576:3: (lv_type_0_0= ruleBuiltinTrigger )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2577:4: lv_type_0_0= ruleBuiltinTrigger
			{

							newCompositeNode(grammarAccess.getBuiltinTriggerRefAccess().getTypeBuiltinTriggerEnumRuleCall_0());
						
			pushFollow(FOLLOW_ruleBuiltinTrigger_in_ruleBuiltinTriggerRef7083);
			lv_type_0_0=ruleBuiltinTrigger();
			state._fsp--;


							if (current==null) {
								current = createModelElementForParent(grammarAccess.getBuiltinTriggerRefRule());
							}
							set(
								current,
								"type",
								lv_type_0_0,
								"org.lflang.LF.BuiltinTrigger");
							afterParserOrEnumRuleCall();
						
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleBuiltinTriggerRef"



	// $ANTLR start "entryRuleDeadline"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2597:1: entryRuleDeadline returns [EObject current=null] :iv_ruleDeadline= ruleDeadline EOF ;
	public final EObject entryRuleDeadline() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleDeadline =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2597:49: (iv_ruleDeadline= ruleDeadline EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2598:2: iv_ruleDeadline= ruleDeadline EOF
			{
			 newCompositeNode(grammarAccess.getDeadlineRule()); 
			pushFollow(FOLLOW_ruleDeadline_in_entryRuleDeadline7114);
			iv_ruleDeadline=ruleDeadline();
			state._fsp--;

			 current =iv_ruleDeadline; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleDeadline7120); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleDeadline"



	// $ANTLR start "ruleDeadline"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2604:1: ruleDeadline returns [EObject current=null] : (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) ;
	public final EObject ruleDeadline() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_1=null;
		Token otherlv_3=null;
		EObject lv_delay_2_0 =null;
		EObject lv_code_4_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2610:2: ( (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2611:2: (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2611:2: (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2612:3: otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) )
			{
			otherlv_0=(Token)match(input,48,FOLLOW_48_in_ruleDeadline7149); 

						newLeafNode(otherlv_0, grammarAccess.getDeadlineAccess().getDeadlineKeyword_0());
					
			otherlv_1=(Token)match(input,18,FOLLOW_18_in_ruleDeadline7159); 

						newLeafNode(otherlv_1, grammarAccess.getDeadlineAccess().getLeftParenthesisKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2620:3: ( (lv_delay_2_0= ruleExpression ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2621:4: (lv_delay_2_0= ruleExpression )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2621:4: (lv_delay_2_0= ruleExpression )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2622:5: lv_delay_2_0= ruleExpression
			{

								newCompositeNode(grammarAccess.getDeadlineAccess().getDelayExpressionParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleExpression_in_ruleDeadline7186);
			lv_delay_2_0=ruleExpression();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getDeadlineRule());
								}
								set(
									current,
									"delay",
									lv_delay_2_0,
									"org.lflang.LF.Expression");
								afterParserOrEnumRuleCall();
							
			}

			}

			otherlv_3=(Token)match(input,19,FOLLOW_19_in_ruleDeadline7207); 

						newLeafNode(otherlv_3, grammarAccess.getDeadlineAccess().getRightParenthesisKeyword_3());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2643:3: ( (lv_code_4_0= ruleCode ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2644:4: (lv_code_4_0= ruleCode )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2644:4: (lv_code_4_0= ruleCode )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2645:5: lv_code_4_0= ruleCode
			{

								newCompositeNode(grammarAccess.getDeadlineAccess().getCodeCodeParserRuleCall_4_0());
							
			pushFollow(FOLLOW_ruleCode_in_ruleDeadline7234);
			lv_code_4_0=ruleCode();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getDeadlineRule());
								}
								set(
									current,
									"code",
									lv_code_4_0,
									"org.lflang.LF.Code");
								afterParserOrEnumRuleCall();
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleDeadline"



	// $ANTLR start "entryRuleSTP"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2666:1: entryRuleSTP returns [EObject current=null] :iv_ruleSTP= ruleSTP EOF ;
	public final EObject entryRuleSTP() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleSTP =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2666:44: (iv_ruleSTP= ruleSTP EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2667:2: iv_ruleSTP= ruleSTP EOF
			{
			 newCompositeNode(grammarAccess.getSTPRule()); 
			pushFollow(FOLLOW_ruleSTP_in_entryRuleSTP7271);
			iv_ruleSTP=ruleSTP();
			state._fsp--;

			 current =iv_ruleSTP; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleSTP7277); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleSTP"



	// $ANTLR start "ruleSTP"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2673:1: ruleSTP returns [EObject current=null] : (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) ;
	public final EObject ruleSTP() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_1=null;
		Token otherlv_3=null;
		EObject lv_value_2_0 =null;
		EObject lv_code_4_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2679:2: ( (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2680:2: (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2680:2: (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2681:3: otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) )
			{
			otherlv_0=(Token)match(input,37,FOLLOW_37_in_ruleSTP7306); 

						newLeafNode(otherlv_0, grammarAccess.getSTPAccess().getSTPKeyword_0());
					
			otherlv_1=(Token)match(input,18,FOLLOW_18_in_ruleSTP7316); 

						newLeafNode(otherlv_1, grammarAccess.getSTPAccess().getLeftParenthesisKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2689:3: ( (lv_value_2_0= ruleExpression ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2690:4: (lv_value_2_0= ruleExpression )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2690:4: (lv_value_2_0= ruleExpression )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2691:5: lv_value_2_0= ruleExpression
			{

								newCompositeNode(grammarAccess.getSTPAccess().getValueExpressionParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleExpression_in_ruleSTP7343);
			lv_value_2_0=ruleExpression();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getSTPRule());
								}
								set(
									current,
									"value",
									lv_value_2_0,
									"org.lflang.LF.Expression");
								afterParserOrEnumRuleCall();
							
			}

			}

			otherlv_3=(Token)match(input,19,FOLLOW_19_in_ruleSTP7364); 

						newLeafNode(otherlv_3, grammarAccess.getSTPAccess().getRightParenthesisKeyword_3());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2712:3: ( (lv_code_4_0= ruleCode ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2713:4: (lv_code_4_0= ruleCode )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2713:4: (lv_code_4_0= ruleCode )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2714:5: lv_code_4_0= ruleCode
			{

								newCompositeNode(grammarAccess.getSTPAccess().getCodeCodeParserRuleCall_4_0());
							
			pushFollow(FOLLOW_ruleCode_in_ruleSTP7391);
			lv_code_4_0=ruleCode();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getSTPRule());
								}
								set(
									current,
									"code",
									lv_code_4_0,
									"org.lflang.LF.Code");
								afterParserOrEnumRuleCall();
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleSTP"



	// $ANTLR start "entryRulePreamble"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2735:1: entryRulePreamble returns [EObject current=null] :iv_rulePreamble= rulePreamble EOF ;
	public final EObject entryRulePreamble() throws RecognitionException {
		EObject current = null;


		EObject iv_rulePreamble =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2735:49: (iv_rulePreamble= rulePreamble EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2736:2: iv_rulePreamble= rulePreamble EOF
			{
			 newCompositeNode(grammarAccess.getPreambleRule()); 
			pushFollow(FOLLOW_rulePreamble_in_entryRulePreamble7428);
			iv_rulePreamble=rulePreamble();
			state._fsp--;

			 current =iv_rulePreamble; 
			match(input,EOF,FOLLOW_EOF_in_entryRulePreamble7434); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRulePreamble"



	// $ANTLR start "rulePreamble"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2742:1: rulePreamble returns [EObject current=null] : ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) ) ;
	public final EObject rulePreamble() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Enumerator lv_visibility_0_0 =null;
		EObject lv_code_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2748:2: ( ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2749:2: ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2749:2: ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2750:3: ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2750:3: ( (lv_visibility_0_0= ruleVisibility ) )?
			int alt74=2;
			int LA74_0 = input.LA(1);
			if ( (LA74_0==36||(LA74_0 >= 67 && LA74_0 <= 68)) ) {
				alt74=1;
			}
			switch (alt74) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2751:4: (lv_visibility_0_0= ruleVisibility )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2751:4: (lv_visibility_0_0= ruleVisibility )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2752:5: lv_visibility_0_0= ruleVisibility
					{

										newCompositeNode(grammarAccess.getPreambleAccess().getVisibilityVisibilityEnumRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleVisibility_in_rulePreamble7480);
					lv_visibility_0_0=ruleVisibility();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getPreambleRule());
										}
										set(
											current,
											"visibility",
											lv_visibility_0_0,
											"org.lflang.LF.Visibility");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			otherlv_1=(Token)match(input,66,FOLLOW_66_in_rulePreamble7502); 

						newLeafNode(otherlv_1, grammarAccess.getPreambleAccess().getPreambleKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2773:3: ( (lv_code_2_0= ruleCode ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2774:4: (lv_code_2_0= ruleCode )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2774:4: (lv_code_2_0= ruleCode )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2775:5: lv_code_2_0= ruleCode
			{

								newCompositeNode(grammarAccess.getPreambleAccess().getCodeCodeParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleCode_in_rulePreamble7529);
			lv_code_2_0=ruleCode();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getPreambleRule());
								}
								set(
									current,
									"code",
									lv_code_2_0,
									"org.lflang.LF.Code");
								afterParserOrEnumRuleCall();
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "rulePreamble"



	// $ANTLR start "entryRuleInstantiation"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2796:1: entryRuleInstantiation returns [EObject current=null] :iv_ruleInstantiation= ruleInstantiation EOF ;
	public final EObject entryRuleInstantiation() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleInstantiation =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2796:54: (iv_ruleInstantiation= ruleInstantiation EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2797:2: iv_ruleInstantiation= ruleInstantiation EOF
			{
			 newCompositeNode(grammarAccess.getInstantiationRule()); 
			pushFollow(FOLLOW_ruleInstantiation_in_entryRuleInstantiation7566);
			iv_ruleInstantiation=ruleInstantiation();
			state._fsp--;

			 current =iv_ruleInstantiation; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleInstantiation7572); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleInstantiation"



	// $ANTLR start "ruleInstantiation"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2803:1: ruleInstantiation returns [EObject current=null] : ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) ) ;
	public final EObject ruleInstantiation() throws RecognitionException {
		EObject current = null;


		Token lv_name_0_0=null;
		Token otherlv_1=null;
		Token otherlv_2=null;
		Token otherlv_4=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		Token otherlv_9=null;
		Token otherlv_10=null;
		Token otherlv_12=null;
		Token otherlv_14=null;
		Token otherlv_15=null;
		Token otherlv_17=null;
		Token otherlv_18=null;
		EObject lv_widthSpec_3_0 =null;
		EObject lv_typeParms_6_0 =null;
		EObject lv_typeParms_8_0 =null;
		EObject lv_parameters_11_0 =null;
		EObject lv_parameters_13_0 =null;
		EObject lv_host_16_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2809:2: ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2810:2: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2810:2: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2811:3: ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2811:3: ( (lv_name_0_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2812:4: (lv_name_0_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2812:4: (lv_name_0_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2813:5: lv_name_0_0= RULE_ID
			{
			lv_name_0_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleInstantiation7612); 

								newLeafNode(lv_name_0_0, grammarAccess.getInstantiationAccess().getNameIDTerminalRuleCall_0_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getInstantiationRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_0_0,
									"org.lflang.LF.ID");
							
			}

			}

			otherlv_1=(Token)match(input,32,FOLLOW_32_in_ruleInstantiation7639); 

						newLeafNode(otherlv_1, grammarAccess.getInstantiationAccess().getEqualsSignKeyword_1());
					
			otherlv_2=(Token)match(input,63,FOLLOW_63_in_ruleInstantiation7649); 

						newLeafNode(otherlv_2, grammarAccess.getInstantiationAccess().getNewKeyword_2());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2837:3: ( (lv_widthSpec_3_0= ruleWidthSpec ) )?
			int alt75=2;
			int LA75_0 = input.LA(1);
			if ( (LA75_0==38) ) {
				alt75=1;
			}
			switch (alt75) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2838:4: (lv_widthSpec_3_0= ruleWidthSpec )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2838:4: (lv_widthSpec_3_0= ruleWidthSpec )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2839:5: lv_widthSpec_3_0= ruleWidthSpec
					{

										newCompositeNode(grammarAccess.getInstantiationAccess().getWidthSpecWidthSpecParserRuleCall_3_0());
									
					pushFollow(FOLLOW_ruleWidthSpec_in_ruleInstantiation7676);
					lv_widthSpec_3_0=ruleWidthSpec();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getInstantiationRule());
										}
										set(
											current,
											"widthSpec",
											lv_widthSpec_3_0,
											"org.lflang.LF.WidthSpec");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2856:3: ( (otherlv_4= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2857:4: (otherlv_4= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2857:4: (otherlv_4= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2858:5: otherlv_4= RULE_ID
			{

								if (current==null) {
									current = createModelElement(grammarAccess.getInstantiationRule());
								}
							
			otherlv_4=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleInstantiation7715); 

								newLeafNode(otherlv_4, grammarAccess.getInstantiationAccess().getReactorClassReactorDeclCrossReference_4_0());
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2869:3: (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )?
			int alt77=2;
			int LA77_0 = input.LA(1);
			if ( (LA77_0==31) ) {
				alt77=1;
			}
			switch (alt77) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2870:4: otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>'
					{
					otherlv_5=(Token)match(input,31,FOLLOW_31_in_ruleInstantiation7741); 

									newLeafNode(otherlv_5, grammarAccess.getInstantiationAccess().getLessThanSignKeyword_5_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2874:4: ( (lv_typeParms_6_0= ruleTypeParm ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2875:5: (lv_typeParms_6_0= ruleTypeParm )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2875:5: (lv_typeParms_6_0= ruleTypeParm )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2876:6: lv_typeParms_6_0= ruleTypeParm
					{

											newCompositeNode(grammarAccess.getInstantiationAccess().getTypeParmsTypeParmParserRuleCall_5_1_0());
										
					pushFollow(FOLLOW_ruleTypeParm_in_ruleInstantiation7773);
					lv_typeParms_6_0=ruleTypeParm();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getInstantiationRule());
											}
											add(
												current,
												"typeParms",
												lv_typeParms_6_0,
												"org.lflang.LF.TypeParm");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2893:4: (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )*
					loop76:
					while (true) {
						int alt76=2;
						int LA76_0 = input.LA(1);
						if ( (LA76_0==22) ) {
							alt76=1;
						}

						switch (alt76) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2894:5: otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) )
							{
							otherlv_7=(Token)match(input,22,FOLLOW_22_in_ruleInstantiation7804); 

												newLeafNode(otherlv_7, grammarAccess.getInstantiationAccess().getCommaKeyword_5_2_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2898:5: ( (lv_typeParms_8_0= ruleTypeParm ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2899:6: (lv_typeParms_8_0= ruleTypeParm )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2899:6: (lv_typeParms_8_0= ruleTypeParm )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2900:7: lv_typeParms_8_0= ruleTypeParm
							{

														newCompositeNode(grammarAccess.getInstantiationAccess().getTypeParmsTypeParmParserRuleCall_5_2_1_0());
													
							pushFollow(FOLLOW_ruleTypeParm_in_ruleInstantiation7841);
							lv_typeParms_8_0=ruleTypeParm();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getInstantiationRule());
														}
														add(
															current,
															"typeParms",
															lv_typeParms_8_0,
															"org.lflang.LF.TypeParm");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop76;
						}
					}

					otherlv_9=(Token)match(input,34,FOLLOW_34_in_ruleInstantiation7875); 

									newLeafNode(otherlv_9, grammarAccess.getInstantiationAccess().getGreaterThanSignKeyword_5_3());
								
					}
					break;

			}

			otherlv_10=(Token)match(input,18,FOLLOW_18_in_ruleInstantiation7891); 

						newLeafNode(otherlv_10, grammarAccess.getInstantiationAccess().getLeftParenthesisKeyword_6());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2927:3: ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )?
			int alt79=2;
			int LA79_0 = input.LA(1);
			if ( (LA79_0==RULE_ID) ) {
				alt79=1;
			}
			switch (alt79) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2928:4: ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )*
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2928:4: ( (lv_parameters_11_0= ruleAssignment ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2929:5: (lv_parameters_11_0= ruleAssignment )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2929:5: (lv_parameters_11_0= ruleAssignment )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2930:6: lv_parameters_11_0= ruleAssignment
					{

											newCompositeNode(grammarAccess.getInstantiationAccess().getParametersAssignmentParserRuleCall_7_0_0());
										
					pushFollow(FOLLOW_ruleAssignment_in_ruleInstantiation7926);
					lv_parameters_11_0=ruleAssignment();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getInstantiationRule());
											}
											add(
												current,
												"parameters",
												lv_parameters_11_0,
												"org.lflang.LF.Assignment");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2947:4: (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )*
					loop78:
					while (true) {
						int alt78=2;
						int LA78_0 = input.LA(1);
						if ( (LA78_0==22) ) {
							alt78=1;
						}

						switch (alt78) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2948:5: otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) )
							{
							otherlv_12=(Token)match(input,22,FOLLOW_22_in_ruleInstantiation7957); 

												newLeafNode(otherlv_12, grammarAccess.getInstantiationAccess().getCommaKeyword_7_1_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2952:5: ( (lv_parameters_13_0= ruleAssignment ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2953:6: (lv_parameters_13_0= ruleAssignment )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2953:6: (lv_parameters_13_0= ruleAssignment )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2954:7: lv_parameters_13_0= ruleAssignment
							{

														newCompositeNode(grammarAccess.getInstantiationAccess().getParametersAssignmentParserRuleCall_7_1_1_0());
													
							pushFollow(FOLLOW_ruleAssignment_in_ruleInstantiation7994);
							lv_parameters_13_0=ruleAssignment();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getInstantiationRule());
														}
														add(
															current,
															"parameters",
															lv_parameters_13_0,
															"org.lflang.LF.Assignment");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop78;
						}
					}

					}
					break;

			}

			otherlv_14=(Token)match(input,19,FOLLOW_19_in_ruleInstantiation8032); 

						newLeafNode(otherlv_14, grammarAccess.getInstantiationAccess().getRightParenthesisKeyword_8());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2977:3: ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? )
			int alt81=2;
			int LA81_0 = input.LA(1);
			if ( (LA81_0==46) ) {
				alt81=1;
			}
			else if ( (LA81_0==EOF||LA81_0==RULE_ID||LA81_0==18||LA81_0==30||(LA81_0 >= 35 && LA81_0 <= 36)||LA81_0==43||LA81_0==47||(LA81_0 >= 54 && LA81_0 <= 57)||(LA81_0 >= 59 && LA81_0 <= 62)||(LA81_0 >= 64 && LA81_0 <= 69)||LA81_0==72||LA81_0==76||LA81_0==79||LA81_0==84) ) {
				alt81=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 81, 0, input);
				throw nvae;
			}

			switch (alt81) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2978:4: (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2978:4: (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2979:5: otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';'
					{
					otherlv_15=(Token)match(input,46,FOLLOW_46_in_ruleInstantiation8053); 

										newLeafNode(otherlv_15, grammarAccess.getInstantiationAccess().getAtKeyword_9_0_0());
									
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2983:5: ( (lv_host_16_0= ruleHost ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2984:6: (lv_host_16_0= ruleHost )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2984:6: (lv_host_16_0= ruleHost )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:2985:7: lv_host_16_0= ruleHost
					{

												newCompositeNode(grammarAccess.getInstantiationAccess().getHostHostParserRuleCall_9_0_1_0());
											
					pushFollow(FOLLOW_ruleHost_in_ruleInstantiation8090);
					lv_host_16_0=ruleHost();
					state._fsp--;


												if (current==null) {
													current = createModelElementForParent(grammarAccess.getInstantiationRule());
												}
												set(
													current,
													"host",
													lv_host_16_0,
													"org.lflang.LF.Host");
												afterParserOrEnumRuleCall();
											
					}

					}

					otherlv_17=(Token)match(input,30,FOLLOW_30_in_ruleInstantiation8119); 

										newLeafNode(otherlv_17, grammarAccess.getInstantiationAccess().getSemicolonKeyword_9_0_2());
									
					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3008:4: (otherlv_18= ';' )?
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3008:4: (otherlv_18= ';' )?
					int alt80=2;
					int LA80_0 = input.LA(1);
					if ( (LA80_0==30) ) {
						alt80=1;
					}
					switch (alt80) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3009:5: otherlv_18= ';'
							{
							otherlv_18=(Token)match(input,30,FOLLOW_30_in_ruleInstantiation8152); 

												newLeafNode(otherlv_18, grammarAccess.getInstantiationAccess().getSemicolonKeyword_9_1());
											
							}
							break;

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleInstantiation"



	// $ANTLR start "entryRuleConnection"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3019:1: entryRuleConnection returns [EObject current=null] :iv_ruleConnection= ruleConnection EOF ;
	public final EObject entryRuleConnection() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleConnection =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3019:51: (iv_ruleConnection= ruleConnection EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3020:2: iv_ruleConnection= ruleConnection EOF
			{
			 newCompositeNode(grammarAccess.getConnectionRule()); 
			pushFollow(FOLLOW_ruleConnection_in_entryRuleConnection8190);
			iv_ruleConnection=ruleConnection();
			state._fsp--;

			 current =iv_ruleConnection; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleConnection8196); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleConnection"



	// $ANTLR start "ruleConnection"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3026:1: ruleConnection returns [EObject current=null] : ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? ) ;
	public final EObject ruleConnection() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		Token lv_iterated_8_0=null;
		Token otherlv_9=null;
		Token lv_physical_10_0=null;
		Token otherlv_12=null;
		Token otherlv_14=null;
		Token otherlv_17=null;
		EObject lv_leftPorts_0_0 =null;
		EObject lv_leftPorts_2_0 =null;
		EObject lv_leftPorts_4_0 =null;
		EObject lv_leftPorts_6_0 =null;
		EObject lv_rightPorts_11_0 =null;
		EObject lv_rightPorts_13_0 =null;
		EObject lv_delay_15_0 =null;
		EObject lv_serializer_16_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3032:2: ( ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3033:2: ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3033:2: ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3034:3: ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3034:3: ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) )
			int alt85=2;
			int LA85_0 = input.LA(1);
			if ( (LA85_0==RULE_ID||LA85_0==56) ) {
				alt85=1;
			}
			else if ( (LA85_0==18) ) {
				alt85=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 85, 0, input);
				throw nvae;
			}

			switch (alt85) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3035:4: ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3035:4: ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3036:5: ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )*
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3036:5: ( (lv_leftPorts_0_0= ruleVarRef ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3037:6: (lv_leftPorts_0_0= ruleVarRef )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3037:6: (lv_leftPorts_0_0= ruleVarRef )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3038:7: lv_leftPorts_0_0= ruleVarRef
					{

												newCompositeNode(grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_0_0_0());
											
					pushFollow(FOLLOW_ruleVarRef_in_ruleConnection8259);
					lv_leftPorts_0_0=ruleVarRef();
					state._fsp--;


												if (current==null) {
													current = createModelElementForParent(grammarAccess.getConnectionRule());
												}
												add(
													current,
													"leftPorts",
													lv_leftPorts_0_0,
													"org.lflang.LF.VarRef");
												afterParserOrEnumRuleCall();
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3055:5: (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )*
					loop82:
					while (true) {
						int alt82=2;
						int LA82_0 = input.LA(1);
						if ( (LA82_0==22) ) {
							alt82=1;
						}

						switch (alt82) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3056:6: otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) )
							{
							otherlv_1=(Token)match(input,22,FOLLOW_22_in_ruleConnection8295); 

													newLeafNode(otherlv_1, grammarAccess.getConnectionAccess().getCommaKeyword_0_0_1_0());
												
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3060:6: ( (lv_leftPorts_2_0= ruleVarRef ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3061:7: (lv_leftPorts_2_0= ruleVarRef )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3061:7: (lv_leftPorts_2_0= ruleVarRef )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3062:8: lv_leftPorts_2_0= ruleVarRef
							{

															newCompositeNode(grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_0_1_1_0());
														
							pushFollow(FOLLOW_ruleVarRef_in_ruleConnection8337);
							lv_leftPorts_2_0=ruleVarRef();
							state._fsp--;


															if (current==null) {
																current = createModelElementForParent(grammarAccess.getConnectionRule());
															}
															add(
																current,
																"leftPorts",
																lv_leftPorts_2_0,
																"org.lflang.LF.VarRef");
															afterParserOrEnumRuleCall();
														
							}

							}

							}
							break;

						default :
							break loop82;
						}
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3082:4: (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3082:4: (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3083:5: otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )?
					{
					otherlv_3=(Token)match(input,18,FOLLOW_18_in_ruleConnection8395); 

										newLeafNode(otherlv_3, grammarAccess.getConnectionAccess().getLeftParenthesisKeyword_0_1_0());
									
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3087:5: ( (lv_leftPorts_4_0= ruleVarRef ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3088:6: (lv_leftPorts_4_0= ruleVarRef )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3088:6: (lv_leftPorts_4_0= ruleVarRef )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3089:7: lv_leftPorts_4_0= ruleVarRef
					{

												newCompositeNode(grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_1_1_0());
											
					pushFollow(FOLLOW_ruleVarRef_in_ruleConnection8432);
					lv_leftPorts_4_0=ruleVarRef();
					state._fsp--;


												if (current==null) {
													current = createModelElementForParent(grammarAccess.getConnectionRule());
												}
												add(
													current,
													"leftPorts",
													lv_leftPorts_4_0,
													"org.lflang.LF.VarRef");
												afterParserOrEnumRuleCall();
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3106:5: (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )*
					loop83:
					while (true) {
						int alt83=2;
						int LA83_0 = input.LA(1);
						if ( (LA83_0==22) ) {
							alt83=1;
						}

						switch (alt83) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3107:6: otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) )
							{
							otherlv_5=(Token)match(input,22,FOLLOW_22_in_ruleConnection8468); 

													newLeafNode(otherlv_5, grammarAccess.getConnectionAccess().getCommaKeyword_0_1_2_0());
												
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3111:6: ( (lv_leftPorts_6_0= ruleVarRef ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3112:7: (lv_leftPorts_6_0= ruleVarRef )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3112:7: (lv_leftPorts_6_0= ruleVarRef )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3113:8: lv_leftPorts_6_0= ruleVarRef
							{

															newCompositeNode(grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_1_2_1_0());
														
							pushFollow(FOLLOW_ruleVarRef_in_ruleConnection8510);
							lv_leftPorts_6_0=ruleVarRef();
							state._fsp--;


															if (current==null) {
																current = createModelElementForParent(grammarAccess.getConnectionRule());
															}
															add(
																current,
																"leftPorts",
																lv_leftPorts_6_0,
																"org.lflang.LF.VarRef");
															afterParserOrEnumRuleCall();
														
							}

							}

							}
							break;

						default :
							break loop83;
						}
					}

					otherlv_7=(Token)match(input,19,FOLLOW_19_in_ruleConnection8549); 

										newLeafNode(otherlv_7, grammarAccess.getConnectionAccess().getRightParenthesisKeyword_0_1_3());
									
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3135:5: ( (lv_iterated_8_0= '+' ) )?
					int alt84=2;
					int LA84_0 = input.LA(1);
					if ( (LA84_0==21) ) {
						alt84=1;
					}
					switch (alt84) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3136:6: (lv_iterated_8_0= '+' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3136:6: (lv_iterated_8_0= '+' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3137:7: lv_iterated_8_0= '+'
							{
							lv_iterated_8_0=(Token)match(input,21,FOLLOW_21_in_ruleConnection8578); 

														newLeafNode(lv_iterated_8_0, grammarAccess.getConnectionAccess().getIteratedPlusSignKeyword_0_1_4_0());
													

														if (current==null) {
															current = createModelElement(grammarAccess.getConnectionRule());
														}
														setWithLastConsumed(current, "iterated", lv_iterated_8_0 != null, "+");
													
							}

							}
							break;

					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3151:3: (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) )
			int alt86=2;
			int LA86_0 = input.LA(1);
			if ( (LA86_0==24) ) {
				alt86=1;
			}
			else if ( (LA86_0==85) ) {
				alt86=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 86, 0, input);
				throw nvae;
			}

			switch (alt86) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3152:4: otherlv_9= '->'
					{
					otherlv_9=(Token)match(input,24,FOLLOW_24_in_ruleConnection8628); 

									newLeafNode(otherlv_9, grammarAccess.getConnectionAccess().getHyphenMinusGreaterThanSignKeyword_1_0());
								
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3157:4: ( (lv_physical_10_0= '~>' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3157:4: ( (lv_physical_10_0= '~>' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3158:5: (lv_physical_10_0= '~>' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3158:5: (lv_physical_10_0= '~>' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3159:6: lv_physical_10_0= '~>'
					{
					lv_physical_10_0=(Token)match(input,85,FOLLOW_85_in_ruleConnection8662); 

											newLeafNode(lv_physical_10_0, grammarAccess.getConnectionAccess().getPhysicalTildeGreaterThanSignKeyword_1_1_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getConnectionRule());
											}
											setWithLastConsumed(current, "physical", lv_physical_10_0 != null, "~>");
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3172:3: ( (lv_rightPorts_11_0= ruleVarRef ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3173:4: (lv_rightPorts_11_0= ruleVarRef )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3173:4: (lv_rightPorts_11_0= ruleVarRef )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3174:5: lv_rightPorts_11_0= ruleVarRef
			{

								newCompositeNode(grammarAccess.getConnectionAccess().getRightPortsVarRefParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleVarRef_in_ruleConnection8714);
			lv_rightPorts_11_0=ruleVarRef();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getConnectionRule());
								}
								add(
									current,
									"rightPorts",
									lv_rightPorts_11_0,
									"org.lflang.LF.VarRef");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3191:3: (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )*
			loop87:
			while (true) {
				int alt87=2;
				int LA87_0 = input.LA(1);
				if ( (LA87_0==22) ) {
					alt87=1;
				}

				switch (alt87) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3192:4: otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) )
					{
					otherlv_12=(Token)match(input,22,FOLLOW_22_in_ruleConnection8740); 

									newLeafNode(otherlv_12, grammarAccess.getConnectionAccess().getCommaKeyword_3_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3196:4: ( (lv_rightPorts_13_0= ruleVarRef ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3197:5: (lv_rightPorts_13_0= ruleVarRef )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3197:5: (lv_rightPorts_13_0= ruleVarRef )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3198:6: lv_rightPorts_13_0= ruleVarRef
					{

											newCompositeNode(grammarAccess.getConnectionAccess().getRightPortsVarRefParserRuleCall_3_1_0());
										
					pushFollow(FOLLOW_ruleVarRef_in_ruleConnection8772);
					lv_rightPorts_13_0=ruleVarRef();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getConnectionRule());
											}
											add(
												current,
												"rightPorts",
												lv_rightPorts_13_0,
												"org.lflang.LF.VarRef");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

				default :
					break loop87;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3216:3: (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )?
			int alt88=2;
			int LA88_0 = input.LA(1);
			if ( (LA88_0==44) ) {
				alt88=1;
			}
			switch (alt88) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3217:4: otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) )
					{
					otherlv_14=(Token)match(input,44,FOLLOW_44_in_ruleConnection8806); 

									newLeafNode(otherlv_14, grammarAccess.getConnectionAccess().getAfterKeyword_4_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3221:4: ( (lv_delay_15_0= ruleExpression ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3222:5: (lv_delay_15_0= ruleExpression )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3222:5: (lv_delay_15_0= ruleExpression )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3223:6: lv_delay_15_0= ruleExpression
					{

											newCompositeNode(grammarAccess.getConnectionAccess().getDelayExpressionParserRuleCall_4_1_0());
										
					pushFollow(FOLLOW_ruleExpression_in_ruleConnection8838);
					lv_delay_15_0=ruleExpression();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getConnectionRule());
											}
											set(
												current,
												"delay",
												lv_delay_15_0,
												"org.lflang.LF.Expression");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3241:3: ( (lv_serializer_16_0= ruleSerializer ) )?
			int alt89=2;
			int LA89_0 = input.LA(1);
			if ( (LA89_0==73) ) {
				alt89=1;
			}
			switch (alt89) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3242:4: (lv_serializer_16_0= ruleSerializer )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3242:4: (lv_serializer_16_0= ruleSerializer )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3243:5: lv_serializer_16_0= ruleSerializer
					{

										newCompositeNode(grammarAccess.getConnectionAccess().getSerializerSerializerParserRuleCall_5_0());
									
					pushFollow(FOLLOW_ruleSerializer_in_ruleConnection8884);
					lv_serializer_16_0=ruleSerializer();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getConnectionRule());
										}
										set(
											current,
											"serializer",
											lv_serializer_16_0,
											"org.lflang.LF.Serializer");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3260:3: (otherlv_17= ';' )?
			int alt90=2;
			int LA90_0 = input.LA(1);
			if ( (LA90_0==30) ) {
				alt90=1;
			}
			switch (alt90) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3261:4: otherlv_17= ';'
					{
					otherlv_17=(Token)match(input,30,FOLLOW_30_in_ruleConnection8911); 

									newLeafNode(otherlv_17, grammarAccess.getConnectionAccess().getSemicolonKeyword_6());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleConnection"



	// $ANTLR start "entryRuleSerializer"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3270:1: entryRuleSerializer returns [EObject current=null] :iv_ruleSerializer= ruleSerializer EOF ;
	public final EObject entryRuleSerializer() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleSerializer =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3270:51: (iv_ruleSerializer= ruleSerializer EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3271:2: iv_ruleSerializer= ruleSerializer EOF
			{
			 newCompositeNode(grammarAccess.getSerializerRule()); 
			pushFollow(FOLLOW_ruleSerializer_in_entryRuleSerializer8943);
			iv_ruleSerializer=ruleSerializer();
			state._fsp--;

			 current =iv_ruleSerializer; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleSerializer8949); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleSerializer"



	// $ANTLR start "ruleSerializer"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3277:1: ruleSerializer returns [EObject current=null] : (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) ) ;
	public final EObject ruleSerializer() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token lv_type_1_0=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3283:2: ( (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3284:2: (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3284:2: (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3285:3: otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) )
			{
			otherlv_0=(Token)match(input,73,FOLLOW_73_in_ruleSerializer8978); 

						newLeafNode(otherlv_0, grammarAccess.getSerializerAccess().getSerializerKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3289:3: ( (lv_type_1_0= RULE_STRING ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3290:4: (lv_type_1_0= RULE_STRING )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3290:4: (lv_type_1_0= RULE_STRING )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3291:5: lv_type_1_0= RULE_STRING
			{
			lv_type_1_0=(Token)match(input,RULE_STRING,FOLLOW_RULE_STRING_in_ruleSerializer8999); 

								newLeafNode(lv_type_1_0, grammarAccess.getSerializerAccess().getTypeSTRINGTerminalRuleCall_1_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getSerializerRule());
								}
								setWithLastConsumed(
									current,
									"type",
									lv_type_1_0,
									"org.lflang.LF.STRING");
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleSerializer"



	// $ANTLR start "entryRuleAttribute"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3311:1: entryRuleAttribute returns [EObject current=null] :iv_ruleAttribute= ruleAttribute EOF ;
	public final EObject entryRuleAttribute() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleAttribute =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3311:50: (iv_ruleAttribute= ruleAttribute EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3312:2: iv_ruleAttribute= ruleAttribute EOF
			{
			 newCompositeNode(grammarAccess.getAttributeRule()); 
			pushFollow(FOLLOW_ruleAttribute_in_entryRuleAttribute9042);
			iv_ruleAttribute=ruleAttribute();
			state._fsp--;

			 current =iv_ruleAttribute; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleAttribute9048); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleAttribute"



	// $ANTLR start "ruleAttribute"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3318:1: ruleAttribute returns [EObject current=null] : (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? ) ;
	public final EObject ruleAttribute() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token lv_attrName_1_0=null;
		Token otherlv_2=null;
		Token otherlv_4=null;
		Token otherlv_6=null;
		Token otherlv_7=null;
		EObject lv_attrParms_3_0 =null;
		EObject lv_attrParms_5_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3324:2: ( (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3325:2: (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3325:2: (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3326:3: otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )?
			{
			otherlv_0=(Token)match(input,35,FOLLOW_35_in_ruleAttribute9077); 

						newLeafNode(otherlv_0, grammarAccess.getAttributeAccess().getCommercialAtKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3330:3: ( (lv_attrName_1_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3331:4: (lv_attrName_1_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3331:4: (lv_attrName_1_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3332:5: lv_attrName_1_0= RULE_ID
			{
			lv_attrName_1_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleAttribute9098); 

								newLeafNode(lv_attrName_1_0, grammarAccess.getAttributeAccess().getAttrNameIDTerminalRuleCall_1_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getAttributeRule());
								}
								setWithLastConsumed(
									current,
									"attrName",
									lv_attrName_1_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3348:3: (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )?
			int alt94=2;
			int LA94_0 = input.LA(1);
			if ( (LA94_0==18) ) {
				alt94=1;
			}
			switch (alt94) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3349:4: otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')'
					{
					otherlv_2=(Token)match(input,18,FOLLOW_18_in_ruleAttribute9130); 

									newLeafNode(otherlv_2, grammarAccess.getAttributeAccess().getLeftParenthesisKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3353:4: ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )?
					int alt93=2;
					int LA93_0 = input.LA(1);
					if ( (LA93_0==RULE_FALSE||(LA93_0 >= RULE_ID && LA93_0 <= RULE_INT)||LA93_0==RULE_NEGINT||(LA93_0 >= RULE_STRING && LA93_0 <= RULE_TRUE)||LA93_0==23||LA93_0==25) ) {
						alt93=1;
					}
					switch (alt93) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3354:5: ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )?
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3354:5: ( (lv_attrParms_3_0= ruleAttrParm ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3355:6: (lv_attrParms_3_0= ruleAttrParm )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3355:6: (lv_attrParms_3_0= ruleAttrParm )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3356:7: lv_attrParms_3_0= ruleAttrParm
							{

														newCompositeNode(grammarAccess.getAttributeAccess().getAttrParmsAttrParmParserRuleCall_2_1_0_0());
													
							pushFollow(FOLLOW_ruleAttrParm_in_ruleAttribute9171);
							lv_attrParms_3_0=ruleAttrParm();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getAttributeRule());
														}
														add(
															current,
															"attrParms",
															lv_attrParms_3_0,
															"org.lflang.LF.AttrParm");
														afterParserOrEnumRuleCall();
													
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3373:5: (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )*
							loop91:
							while (true) {
								int alt91=2;
								int LA91_0 = input.LA(1);
								if ( (LA91_0==22) ) {
									int LA91_1 = input.LA(2);
									if ( (LA91_1==RULE_FALSE||(LA91_1 >= RULE_ID && LA91_1 <= RULE_INT)||LA91_1==RULE_NEGINT||(LA91_1 >= RULE_STRING && LA91_1 <= RULE_TRUE)||LA91_1==23||LA91_1==25) ) {
										alt91=1;
									}

								}

								switch (alt91) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3374:6: otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) )
									{
									otherlv_4=(Token)match(input,22,FOLLOW_22_in_ruleAttribute9207); 

															newLeafNode(otherlv_4, grammarAccess.getAttributeAccess().getCommaKeyword_2_1_1_0());
														
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3378:6: ( (lv_attrParms_5_0= ruleAttrParm ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3379:7: (lv_attrParms_5_0= ruleAttrParm )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3379:7: (lv_attrParms_5_0= ruleAttrParm )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3380:8: lv_attrParms_5_0= ruleAttrParm
									{

																	newCompositeNode(grammarAccess.getAttributeAccess().getAttrParmsAttrParmParserRuleCall_2_1_1_1_0());
																
									pushFollow(FOLLOW_ruleAttrParm_in_ruleAttribute9249);
									lv_attrParms_5_0=ruleAttrParm();
									state._fsp--;


																	if (current==null) {
																		current = createModelElementForParent(grammarAccess.getAttributeRule());
																	}
																	add(
																		current,
																		"attrParms",
																		lv_attrParms_5_0,
																		"org.lflang.LF.AttrParm");
																	afterParserOrEnumRuleCall();
																
									}

									}

									}
									break;

								default :
									break loop91;
								}
							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3398:5: (otherlv_6= ',' )?
							int alt92=2;
							int LA92_0 = input.LA(1);
							if ( (LA92_0==22) ) {
								alt92=1;
							}
							switch (alt92) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3399:6: otherlv_6= ','
									{
									otherlv_6=(Token)match(input,22,FOLLOW_22_in_ruleAttribute9295); 

															newLeafNode(otherlv_6, grammarAccess.getAttributeAccess().getCommaKeyword_2_1_2());
														
									}
									break;

							}

							}
							break;

					}

					otherlv_7=(Token)match(input,19,FOLLOW_19_in_ruleAttribute9322); 

									newLeafNode(otherlv_7, grammarAccess.getAttributeAccess().getRightParenthesisKeyword_2_2());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleAttribute"



	// $ANTLR start "entryRuleAttrParm"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3414:1: entryRuleAttrParm returns [EObject current=null] :iv_ruleAttrParm= ruleAttrParm EOF ;
	public final EObject entryRuleAttrParm() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleAttrParm =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3414:49: (iv_ruleAttrParm= ruleAttrParm EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3415:2: iv_ruleAttrParm= ruleAttrParm EOF
			{
			 newCompositeNode(grammarAccess.getAttrParmRule()); 
			pushFollow(FOLLOW_ruleAttrParm_in_entryRuleAttrParm9354);
			iv_ruleAttrParm=ruleAttrParm();
			state._fsp--;

			 current =iv_ruleAttrParm; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleAttrParm9360); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleAttrParm"



	// $ANTLR start "ruleAttrParm"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3421:1: ruleAttrParm returns [EObject current=null] : ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) ) ;
	public final EObject ruleAttrParm() throws RecognitionException {
		EObject current = null;


		Token lv_name_0_0=null;
		Token otherlv_1=null;
		EObject lv_value_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3427:2: ( ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3428:2: ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3428:2: ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3429:3: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3429:3: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )?
			int alt95=2;
			int LA95_0 = input.LA(1);
			if ( (LA95_0==RULE_ID) ) {
				alt95=1;
			}
			switch (alt95) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3430:4: ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '='
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3430:4: ( (lv_name_0_0= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3431:5: (lv_name_0_0= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3431:5: (lv_name_0_0= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3432:6: lv_name_0_0= RULE_ID
					{
					lv_name_0_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleAttrParm9407); 

											newLeafNode(lv_name_0_0, grammarAccess.getAttrParmAccess().getNameIDTerminalRuleCall_0_0_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getAttrParmRule());
											}
											setWithLastConsumed(
												current,
												"name",
												lv_name_0_0,
												"org.lflang.LF.ID");
										
					}

					}

					otherlv_1=(Token)match(input,32,FOLLOW_32_in_ruleAttrParm9439); 

									newLeafNode(otherlv_1, grammarAccess.getAttrParmAccess().getEqualsSignKeyword_0_1());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3453:3: ( (lv_value_2_0= ruleAttrParmValue ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3454:4: (lv_value_2_0= ruleAttrParmValue )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3454:4: (lv_value_2_0= ruleAttrParmValue )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3455:5: lv_value_2_0= ruleAttrParmValue
			{

								newCompositeNode(grammarAccess.getAttrParmAccess().getValueAttrParmValueParserRuleCall_1_0());
							
			pushFollow(FOLLOW_ruleAttrParmValue_in_ruleAttrParm9472);
			lv_value_2_0=ruleAttrParmValue();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getAttrParmRule());
								}
								set(
									current,
									"value",
									lv_value_2_0,
									"org.lflang.LF.AttrParmValue");
								afterParserOrEnumRuleCall();
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleAttrParm"



	// $ANTLR start "entryRuleAttrParmValue"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3476:1: entryRuleAttrParmValue returns [EObject current=null] :iv_ruleAttrParmValue= ruleAttrParmValue EOF ;
	public final EObject entryRuleAttrParmValue() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleAttrParmValue =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3476:54: (iv_ruleAttrParmValue= ruleAttrParmValue EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3477:2: iv_ruleAttrParmValue= ruleAttrParmValue EOF
			{
			 newCompositeNode(grammarAccess.getAttrParmValueRule()); 
			pushFollow(FOLLOW_ruleAttrParmValue_in_entryRuleAttrParmValue9509);
			iv_ruleAttrParmValue=ruleAttrParmValue();
			state._fsp--;

			 current =iv_ruleAttrParmValue; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleAttrParmValue9515); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleAttrParmValue"



	// $ANTLR start "ruleAttrParmValue"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3483:1: ruleAttrParmValue returns [EObject current=null] : ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) ) ;
	public final EObject ruleAttrParmValue() throws RecognitionException {
		EObject current = null;


		Token lv_str_0_0=null;
		AntlrDatatypeRuleToken lv_int_1_0 =null;
		AntlrDatatypeRuleToken lv_bool_2_0 =null;
		AntlrDatatypeRuleToken lv_float_3_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3489:2: ( ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3490:2: ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3490:2: ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) )
			int alt96=4;
			switch ( input.LA(1) ) {
			case RULE_STRING:
				{
				alt96=1;
				}
				break;
			case RULE_INT:
				{
				int LA96_2 = input.LA(2);
				if ( (LA96_2==EOF||LA96_2==19||LA96_2==22) ) {
					alt96=2;
				}
				else if ( (LA96_2==25) ) {
					alt96=4;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 96, 2, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

				}
				break;
			case RULE_NEGINT:
				{
				int LA96_3 = input.LA(2);
				if ( (LA96_3==EOF||LA96_3==19||LA96_3==22) ) {
					alt96=2;
				}
				else if ( (LA96_3==25) ) {
					alt96=4;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 96, 3, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

				}
				break;
			case RULE_FALSE:
			case RULE_TRUE:
				{
				alt96=3;
				}
				break;
			case 23:
			case 25:
				{
				alt96=4;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 96, 0, input);
				throw nvae;
			}
			switch (alt96) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3491:3: ( (lv_str_0_0= RULE_STRING ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3491:3: ( (lv_str_0_0= RULE_STRING ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3492:4: (lv_str_0_0= RULE_STRING )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3492:4: (lv_str_0_0= RULE_STRING )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3493:5: lv_str_0_0= RULE_STRING
					{
					lv_str_0_0=(Token)match(input,RULE_STRING,FOLLOW_RULE_STRING_in_ruleAttrParmValue9555); 

										newLeafNode(lv_str_0_0, grammarAccess.getAttrParmValueAccess().getStrSTRINGTerminalRuleCall_0_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getAttrParmValueRule());
										}
										setWithLastConsumed(
											current,
											"str",
											lv_str_0_0,
											"org.lflang.LF.STRING");
									
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3510:3: ( (lv_int_1_0= ruleSignedInt ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3510:3: ( (lv_int_1_0= ruleSignedInt ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3511:4: (lv_int_1_0= ruleSignedInt )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3511:4: (lv_int_1_0= ruleSignedInt )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3512:5: lv_int_1_0= ruleSignedInt
					{

										newCompositeNode(grammarAccess.getAttrParmValueAccess().getIntSignedIntParserRuleCall_1_0());
									
					pushFollow(FOLLOW_ruleSignedInt_in_ruleAttrParmValue9607);
					lv_int_1_0=ruleSignedInt();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getAttrParmValueRule());
										}
										set(
											current,
											"int",
											lv_int_1_0,
											"org.lflang.LF.SignedInt");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3530:3: ( (lv_bool_2_0= ruleBoolean ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3530:3: ( (lv_bool_2_0= ruleBoolean ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3531:4: (lv_bool_2_0= ruleBoolean )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3531:4: (lv_bool_2_0= ruleBoolean )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3532:5: lv_bool_2_0= ruleBoolean
					{

										newCompositeNode(grammarAccess.getAttrParmValueAccess().getBoolBooleanParserRuleCall_2_0());
									
					pushFollow(FOLLOW_ruleBoolean_in_ruleAttrParmValue9653);
					lv_bool_2_0=ruleBoolean();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getAttrParmValueRule());
										}
										set(
											current,
											"bool",
											lv_bool_2_0,
											"org.lflang.LF.Boolean");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3550:3: ( (lv_float_3_0= ruleSignedFloat ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3550:3: ( (lv_float_3_0= ruleSignedFloat ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3551:4: (lv_float_3_0= ruleSignedFloat )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3551:4: (lv_float_3_0= ruleSignedFloat )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3552:5: lv_float_3_0= ruleSignedFloat
					{

										newCompositeNode(grammarAccess.getAttrParmValueAccess().getFloatSignedFloatParserRuleCall_3_0());
									
					pushFollow(FOLLOW_ruleSignedFloat_in_ruleAttrParmValue9699);
					lv_float_3_0=ruleSignedFloat();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getAttrParmValueRule());
										}
										set(
											current,
											"float",
											lv_float_3_0,
											"org.lflang.LF.SignedFloat");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleAttrParmValue"



	// $ANTLR start "entryRuleKeyValuePairs"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3573:1: entryRuleKeyValuePairs returns [EObject current=null] :iv_ruleKeyValuePairs= ruleKeyValuePairs EOF ;
	public final EObject entryRuleKeyValuePairs() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleKeyValuePairs =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3573:54: (iv_ruleKeyValuePairs= ruleKeyValuePairs EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3574:2: iv_ruleKeyValuePairs= ruleKeyValuePairs EOF
			{
			 newCompositeNode(grammarAccess.getKeyValuePairsRule()); 
			pushFollow(FOLLOW_ruleKeyValuePairs_in_entryRuleKeyValuePairs9736);
			iv_ruleKeyValuePairs=ruleKeyValuePairs();
			state._fsp--;

			 current =iv_ruleKeyValuePairs; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleKeyValuePairs9742); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleKeyValuePairs"



	// $ANTLR start "ruleKeyValuePairs"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3580:1: ruleKeyValuePairs returns [EObject current=null] : ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' ) ;
	public final EObject ruleKeyValuePairs() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		Token otherlv_6=null;
		EObject lv_pairs_2_0 =null;
		EObject lv_pairs_4_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3586:2: ( ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3587:2: ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3587:2: ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3588:3: () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}'
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3588:3: ()
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3589:4: 
			{

							current = forceCreateModelElement(
								grammarAccess.getKeyValuePairsAccess().getKeyValuePairsAction_0(),
								current);
						
			}

			otherlv_1=(Token)match(input,82,FOLLOW_82_in_ruleKeyValuePairs9784); 

						newLeafNode(otherlv_1, grammarAccess.getKeyValuePairsAccess().getLeftCurlyBracketKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3599:3: ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )?
			int alt99=2;
			int LA99_0 = input.LA(1);
			if ( (LA99_0==RULE_ID||LA99_0==65) ) {
				alt99=1;
			}
			switch (alt99) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3600:4: ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )?
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3600:4: ( (lv_pairs_2_0= ruleKeyValuePair ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3601:5: (lv_pairs_2_0= ruleKeyValuePair )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3601:5: (lv_pairs_2_0= ruleKeyValuePair )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3602:6: lv_pairs_2_0= ruleKeyValuePair
					{

											newCompositeNode(grammarAccess.getKeyValuePairsAccess().getPairsKeyValuePairParserRuleCall_2_0_0());
										
					pushFollow(FOLLOW_ruleKeyValuePair_in_ruleKeyValuePairs9819);
					lv_pairs_2_0=ruleKeyValuePair();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getKeyValuePairsRule());
											}
											add(
												current,
												"pairs",
												lv_pairs_2_0,
												"org.lflang.LF.KeyValuePair");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3619:4: (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )*
					loop97:
					while (true) {
						int alt97=2;
						int LA97_0 = input.LA(1);
						if ( (LA97_0==22) ) {
							int LA97_1 = input.LA(2);
							if ( (LA97_1==RULE_ID||LA97_1==65) ) {
								alt97=1;
							}

						}

						switch (alt97) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3620:5: otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) )
							{
							otherlv_3=(Token)match(input,22,FOLLOW_22_in_ruleKeyValuePairs9850); 

												newLeafNode(otherlv_3, grammarAccess.getKeyValuePairsAccess().getCommaKeyword_2_1_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3624:5: ( (lv_pairs_4_0= ruleKeyValuePair ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3625:6: (lv_pairs_4_0= ruleKeyValuePair )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3625:6: (lv_pairs_4_0= ruleKeyValuePair )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3626:7: lv_pairs_4_0= ruleKeyValuePair
							{

														newCompositeNode(grammarAccess.getKeyValuePairsAccess().getPairsKeyValuePairParserRuleCall_2_1_1_0());
													
							pushFollow(FOLLOW_ruleKeyValuePair_in_ruleKeyValuePairs9887);
							lv_pairs_4_0=ruleKeyValuePair();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getKeyValuePairsRule());
														}
														add(
															current,
															"pairs",
															lv_pairs_4_0,
															"org.lflang.LF.KeyValuePair");
														afterParserOrEnumRuleCall();
													
							}

							}

							}
							break;

						default :
							break loop97;
						}
					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3644:4: (otherlv_5= ',' )?
					int alt98=2;
					int LA98_0 = input.LA(1);
					if ( (LA98_0==22) ) {
						alt98=1;
					}
					switch (alt98) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3645:5: otherlv_5= ','
							{
							otherlv_5=(Token)match(input,22,FOLLOW_22_in_ruleKeyValuePairs9927); 

												newLeafNode(otherlv_5, grammarAccess.getKeyValuePairsAccess().getCommaKeyword_2_2());
											
							}
							break;

					}

					}
					break;

			}

			otherlv_6=(Token)match(input,84,FOLLOW_84_in_ruleKeyValuePairs9950); 

						newLeafNode(otherlv_6, grammarAccess.getKeyValuePairsAccess().getRightCurlyBracketKeyword_3());
					
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleKeyValuePairs"



	// $ANTLR start "entryRuleKeyValuePair"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3659:1: entryRuleKeyValuePair returns [EObject current=null] :iv_ruleKeyValuePair= ruleKeyValuePair EOF ;
	public final EObject entryRuleKeyValuePair() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleKeyValuePair =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3659:53: (iv_ruleKeyValuePair= ruleKeyValuePair EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3660:2: iv_ruleKeyValuePair= ruleKeyValuePair EOF
			{
			 newCompositeNode(grammarAccess.getKeyValuePairRule()); 
			pushFollow(FOLLOW_ruleKeyValuePair_in_entryRuleKeyValuePair9976);
			iv_ruleKeyValuePair=ruleKeyValuePair();
			state._fsp--;

			 current =iv_ruleKeyValuePair; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleKeyValuePair9982); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleKeyValuePair"



	// $ANTLR start "ruleKeyValuePair"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3666:1: ruleKeyValuePair returns [EObject current=null] : ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) ) ;
	public final EObject ruleKeyValuePair() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		AntlrDatatypeRuleToken lv_name_0_0 =null;
		EObject lv_value_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3672:2: ( ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3673:2: ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3673:2: ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3674:3: ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3674:3: ( (lv_name_0_0= ruleKebab ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3675:4: (lv_name_0_0= ruleKebab )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3675:4: (lv_name_0_0= ruleKebab )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3676:5: lv_name_0_0= ruleKebab
			{

								newCompositeNode(grammarAccess.getKeyValuePairAccess().getNameKebabParserRuleCall_0_0());
							
			pushFollow(FOLLOW_ruleKebab_in_ruleKeyValuePair10028);
			lv_name_0_0=ruleKebab();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getKeyValuePairRule());
								}
								set(
									current,
									"name",
									lv_name_0_0,
									"org.lflang.LF.Kebab");
								afterParserOrEnumRuleCall();
							
			}

			}

			otherlv_1=(Token)match(input,27,FOLLOW_27_in_ruleKeyValuePair10049); 

						newLeafNode(otherlv_1, grammarAccess.getKeyValuePairAccess().getColonKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3697:3: ( (lv_value_2_0= ruleElement ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3698:4: (lv_value_2_0= ruleElement )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3698:4: (lv_value_2_0= ruleElement )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3699:5: lv_value_2_0= ruleElement
			{

								newCompositeNode(grammarAccess.getKeyValuePairAccess().getValueElementParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleElement_in_ruleKeyValuePair10076);
			lv_value_2_0=ruleElement();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getKeyValuePairRule());
								}
								set(
									current,
									"value",
									lv_value_2_0,
									"org.lflang.LF.Element");
								afterParserOrEnumRuleCall();
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleKeyValuePair"



	// $ANTLR start "entryRuleArray"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3720:1: entryRuleArray returns [EObject current=null] :iv_ruleArray= ruleArray EOF ;
	public final EObject entryRuleArray() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleArray =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3720:46: (iv_ruleArray= ruleArray EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3721:2: iv_ruleArray= ruleArray EOF
			{
			 newCompositeNode(grammarAccess.getArrayRule()); 
			pushFollow(FOLLOW_ruleArray_in_entryRuleArray10113);
			iv_ruleArray=ruleArray();
			state._fsp--;

			 current =iv_ruleArray; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleArray10119); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleArray"



	// $ANTLR start "ruleArray"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3727:1: ruleArray returns [EObject current=null] : (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' ) ;
	public final EObject ruleArray() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_2=null;
		Token otherlv_4=null;
		Token otherlv_5=null;
		EObject lv_elements_1_0 =null;
		EObject lv_elements_3_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3733:2: ( (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3734:2: (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3734:2: (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3735:3: otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']'
			{
			otherlv_0=(Token)match(input,38,FOLLOW_38_in_ruleArray10148); 

						newLeafNode(otherlv_0, grammarAccess.getArrayAccess().getLeftSquareBracketKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3739:3: ( (lv_elements_1_0= ruleElement ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3740:4: (lv_elements_1_0= ruleElement )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3740:4: (lv_elements_1_0= ruleElement )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3741:5: lv_elements_1_0= ruleElement
			{

								newCompositeNode(grammarAccess.getArrayAccess().getElementsElementParserRuleCall_1_0());
							
			pushFollow(FOLLOW_ruleElement_in_ruleArray10175);
			lv_elements_1_0=ruleElement();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getArrayRule());
								}
								add(
									current,
									"elements",
									lv_elements_1_0,
									"org.lflang.LF.Element");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3758:3: (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )*
			loop100:
			while (true) {
				int alt100=2;
				int LA100_0 = input.LA(1);
				if ( (LA100_0==22) ) {
					int LA100_1 = input.LA(2);
					if ( ((LA100_1 >= RULE_CHAR_LIT && LA100_1 <= RULE_FALSE)||(LA100_1 >= RULE_ID && LA100_1 <= RULE_INT)||LA100_1==RULE_NEGINT||(LA100_1 >= RULE_STRING && LA100_1 <= RULE_TRUE)||LA100_1==23||(LA100_1 >= 25 && LA100_1 <= 26)||LA100_1==38||LA100_1==40||LA100_1==42||LA100_1==82) ) {
						alt100=1;
					}

				}

				switch (alt100) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3759:4: otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) )
					{
					otherlv_2=(Token)match(input,22,FOLLOW_22_in_ruleArray10201); 

									newLeafNode(otherlv_2, grammarAccess.getArrayAccess().getCommaKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3763:4: ( (lv_elements_3_0= ruleElement ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3764:5: (lv_elements_3_0= ruleElement )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3764:5: (lv_elements_3_0= ruleElement )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3765:6: lv_elements_3_0= ruleElement
					{

											newCompositeNode(grammarAccess.getArrayAccess().getElementsElementParserRuleCall_2_1_0());
										
					pushFollow(FOLLOW_ruleElement_in_ruleArray10233);
					lv_elements_3_0=ruleElement();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getArrayRule());
											}
											add(
												current,
												"elements",
												lv_elements_3_0,
												"org.lflang.LF.Element");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

				default :
					break loop100;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3783:3: (otherlv_4= ',' )?
			int alt101=2;
			int LA101_0 = input.LA(1);
			if ( (LA101_0==22) ) {
				alt101=1;
			}
			switch (alt101) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3784:4: otherlv_4= ','
					{
					otherlv_4=(Token)match(input,22,FOLLOW_22_in_ruleArray10267); 

									newLeafNode(otherlv_4, grammarAccess.getArrayAccess().getCommaKeyword_3());
								
					}
					break;

			}

			otherlv_5=(Token)match(input,41,FOLLOW_41_in_ruleArray10283); 

						newLeafNode(otherlv_5, grammarAccess.getArrayAccess().getRightSquareBracketKeyword_4());
					
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleArray"



	// $ANTLR start "entryRuleElement"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3797:1: entryRuleElement returns [EObject current=null] :iv_ruleElement= ruleElement EOF ;
	public final EObject entryRuleElement() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleElement =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3797:48: (iv_ruleElement= ruleElement EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3798:2: iv_ruleElement= ruleElement EOF
			{
			 newCompositeNode(grammarAccess.getElementRule()); 
			pushFollow(FOLLOW_ruleElement_in_entryRuleElement10309);
			iv_ruleElement=ruleElement();
			state._fsp--;

			 current =iv_ruleElement; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleElement10315); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleElement"



	// $ANTLR start "ruleElement"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3804:1: ruleElement returns [EObject current=null] : ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) ) ;
	public final EObject ruleElement() throws RecognitionException {
		EObject current = null;


		Token lv_time_3_0=null;
		EObject lv_keyvalue_0_0 =null;
		EObject lv_array_1_0 =null;
		AntlrDatatypeRuleToken lv_literal_2_0 =null;
		AntlrDatatypeRuleToken lv_unit_4_0 =null;
		AntlrDatatypeRuleToken lv_id_5_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3810:2: ( ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3811:2: ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3811:2: ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) )
			int alt102=5;
			switch ( input.LA(1) ) {
			case 82:
				{
				alt102=1;
				}
				break;
			case 38:
				{
				alt102=2;
				}
				break;
			case RULE_CHAR_LIT:
			case RULE_FALSE:
			case RULE_NEGINT:
			case RULE_STRING:
			case RULE_TRUE:
			case 23:
				{
				alt102=3;
				}
				break;
			case RULE_INT:
				{
				int LA102_4 = input.LA(2);
				if ( (LA102_4==EOF||LA102_4==22||LA102_4==25||LA102_4==41||LA102_4==84) ) {
					alt102=3;
				}
				else if ( (LA102_4==RULE_ID) ) {
					alt102=4;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 102, 4, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

				}
				break;
			case 25:
				{
				int LA102_5 = input.LA(2);
				if ( (LA102_5==RULE_FLOAT_EXP_SUFFIX||LA102_5==RULE_INT) ) {
					alt102=3;
				}
				else if ( (LA102_5==EOF||LA102_5==RULE_ID||LA102_5==22||(LA102_5 >= 25 && LA102_5 <= 26)||LA102_5==29||(LA102_5 >= 40 && LA102_5 <= 42)||LA102_5==84) ) {
					alt102=5;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 102, 5, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

				}
				break;
			case RULE_ID:
			case 26:
			case 40:
			case 42:
				{
				alt102=5;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 102, 0, input);
				throw nvae;
			}
			switch (alt102) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3812:3: ( (lv_keyvalue_0_0= ruleKeyValuePairs ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3812:3: ( (lv_keyvalue_0_0= ruleKeyValuePairs ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3813:4: (lv_keyvalue_0_0= ruleKeyValuePairs )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3813:4: (lv_keyvalue_0_0= ruleKeyValuePairs )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3814:5: lv_keyvalue_0_0= ruleKeyValuePairs
					{

										newCompositeNode(grammarAccess.getElementAccess().getKeyvalueKeyValuePairsParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleKeyValuePairs_in_ruleElement10361);
					lv_keyvalue_0_0=ruleKeyValuePairs();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getElementRule());
										}
										set(
											current,
											"keyvalue",
											lv_keyvalue_0_0,
											"org.lflang.LF.KeyValuePairs");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3832:3: ( (lv_array_1_0= ruleArray ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3832:3: ( (lv_array_1_0= ruleArray ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3833:4: (lv_array_1_0= ruleArray )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3833:4: (lv_array_1_0= ruleArray )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3834:5: lv_array_1_0= ruleArray
					{

										newCompositeNode(grammarAccess.getElementAccess().getArrayArrayParserRuleCall_1_0());
									
					pushFollow(FOLLOW_ruleArray_in_ruleElement10407);
					lv_array_1_0=ruleArray();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getElementRule());
										}
										set(
											current,
											"array",
											lv_array_1_0,
											"org.lflang.LF.Array");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3852:3: ( (lv_literal_2_0= ruleLiteral ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3852:3: ( (lv_literal_2_0= ruleLiteral ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3853:4: (lv_literal_2_0= ruleLiteral )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3853:4: (lv_literal_2_0= ruleLiteral )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3854:5: lv_literal_2_0= ruleLiteral
					{

										newCompositeNode(grammarAccess.getElementAccess().getLiteralLiteralParserRuleCall_2_0());
									
					pushFollow(FOLLOW_ruleLiteral_in_ruleElement10453);
					lv_literal_2_0=ruleLiteral();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getElementRule());
										}
										set(
											current,
											"literal",
											lv_literal_2_0,
											"org.lflang.LF.Literal");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3872:3: ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3872:3: ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3873:4: ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3873:4: ( (lv_time_3_0= RULE_INT ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3874:5: (lv_time_3_0= RULE_INT )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3874:5: (lv_time_3_0= RULE_INT )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3875:6: lv_time_3_0= RULE_INT
					{
					lv_time_3_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleElement10500); 

											newLeafNode(lv_time_3_0, grammarAccess.getElementAccess().getTimeINTTerminalRuleCall_3_0_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getElementRule());
											}
											setWithLastConsumed(
												current,
												"time",
												lv_time_3_0,
												"org.lflang.LF.INT");
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3891:4: ( (lv_unit_4_0= ruleTimeUnit ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3892:5: (lv_unit_4_0= ruleTimeUnit )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3892:5: (lv_unit_4_0= ruleTimeUnit )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3893:6: lv_unit_4_0= ruleTimeUnit
					{

											newCompositeNode(grammarAccess.getElementAccess().getUnitTimeUnitParserRuleCall_3_1_0());
										
					pushFollow(FOLLOW_ruleTimeUnit_in_ruleElement10552);
					lv_unit_4_0=ruleTimeUnit();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getElementRule());
											}
											set(
												current,
												"unit",
												lv_unit_4_0,
												"org.lflang.LF.TimeUnit");
											afterParserOrEnumRuleCall();
										
					}

					}

					}

					}
					break;
				case 5 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3912:3: ( (lv_id_5_0= rulePath ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3912:3: ( (lv_id_5_0= rulePath ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3913:4: (lv_id_5_0= rulePath )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3913:4: (lv_id_5_0= rulePath )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3914:5: lv_id_5_0= rulePath
					{

										newCompositeNode(grammarAccess.getElementAccess().getIdPathParserRuleCall_4_0());
									
					pushFollow(FOLLOW_rulePath_in_ruleElement10605);
					lv_id_5_0=rulePath();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getElementRule());
										}
										set(
											current,
											"id",
											lv_id_5_0,
											"org.lflang.LF.Path");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleElement"



	// $ANTLR start "entryRuleTypedVariable"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3935:1: entryRuleTypedVariable returns [EObject current=null] :iv_ruleTypedVariable= ruleTypedVariable EOF ;
	public final EObject entryRuleTypedVariable() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleTypedVariable =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3935:54: (iv_ruleTypedVariable= ruleTypedVariable EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3936:2: iv_ruleTypedVariable= ruleTypedVariable EOF
			{
			 newCompositeNode(grammarAccess.getTypedVariableRule()); 
			pushFollow(FOLLOW_ruleTypedVariable_in_entryRuleTypedVariable10642);
			iv_ruleTypedVariable=ruleTypedVariable();
			state._fsp--;

			 current =iv_ruleTypedVariable; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTypedVariable10648); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTypedVariable"



	// $ANTLR start "ruleTypedVariable"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3942:1: ruleTypedVariable returns [EObject current=null] : (this_Port_0= rulePort |this_Action_1= ruleAction ) ;
	public final EObject ruleTypedVariable() throws RecognitionException {
		EObject current = null;


		EObject this_Port_0 =null;
		EObject this_Action_1 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3948:2: ( (this_Port_0= rulePort |this_Action_1= ruleAction ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3949:2: (this_Port_0= rulePort |this_Action_1= ruleAction )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3949:2: (this_Port_0= rulePort |this_Action_1= ruleAction )
			int alt103=2;
			alt103 = dfa103.predict(input);
			switch (alt103) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3950:3: this_Port_0= rulePort
					{

								newCompositeNode(grammarAccess.getTypedVariableAccess().getPortParserRuleCall_0());
							
					pushFollow(FOLLOW_rulePort_in_ruleTypedVariable10681);
					this_Port_0=rulePort();
					state._fsp--;


								current = this_Port_0;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3959:3: this_Action_1= ruleAction
					{

								newCompositeNode(grammarAccess.getTypedVariableAccess().getActionParserRuleCall_1());
							
					pushFollow(FOLLOW_ruleAction_in_ruleTypedVariable10703);
					this_Action_1=ruleAction();
					state._fsp--;


								current = this_Action_1;
								afterParserOrEnumRuleCall();
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTypedVariable"



	// $ANTLR start "entryRuleVarRef"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3971:1: entryRuleVarRef returns [EObject current=null] :iv_ruleVarRef= ruleVarRef EOF ;
	public final EObject entryRuleVarRef() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleVarRef =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3971:47: (iv_ruleVarRef= ruleVarRef EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3972:2: iv_ruleVarRef= ruleVarRef EOF
			{
			 newCompositeNode(grammarAccess.getVarRefRule()); 
			pushFollow(FOLLOW_ruleVarRef_in_entryRuleVarRef10729);
			iv_ruleVarRef=ruleVarRef();
			state._fsp--;

			 current =iv_ruleVarRef; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleVarRef10735); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleVarRef"



	// $ANTLR start "ruleVarRef"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3978:1: ruleVarRef returns [EObject current=null] : ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) ) ;
	public final EObject ruleVarRef() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_1=null;
		Token otherlv_2=null;
		Token otherlv_3=null;
		Token lv_interleaved_4_0=null;
		Token otherlv_5=null;
		Token otherlv_6=null;
		Token otherlv_7=null;
		Token otherlv_8=null;
		Token otherlv_9=null;
		Token otherlv_10=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3984:2: ( ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3985:2: ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3985:2: ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) )
			int alt105=3;
			int LA105_0 = input.LA(1);
			if ( (LA105_0==RULE_ID) ) {
				int LA105_1 = input.LA(2);
				if ( (LA105_1==EOF||LA105_1==RULE_ID||(LA105_1 >= 18 && LA105_1 <= 19)||LA105_1==22||LA105_1==24||LA105_1==30||(LA105_1 >= 35 && LA105_1 <= 36)||(LA105_1 >= 43 && LA105_1 <= 44)||LA105_1==47||(LA105_1 >= 54 && LA105_1 <= 57)||(LA105_1 >= 59 && LA105_1 <= 62)||(LA105_1 >= 64 && LA105_1 <= 69)||(LA105_1 >= 72 && LA105_1 <= 73)||LA105_1==76||LA105_1==79||(LA105_1 >= 83 && LA105_1 <= 85)) ) {
					alt105=1;
				}
				else if ( (LA105_1==25) ) {
					alt105=2;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 105, 1, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

			}
			else if ( (LA105_0==56) ) {
				alt105=3;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 105, 0, input);
				throw nvae;
			}

			switch (alt105) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3986:3: ( (otherlv_0= RULE_ID ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3986:3: ( (otherlv_0= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3987:4: (otherlv_0= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3987:4: (otherlv_0= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:3988:5: otherlv_0= RULE_ID
					{

										if (current==null) {
											current = createModelElement(grammarAccess.getVarRefRule());
										}
									
					otherlv_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRef10781); 

										newLeafNode(otherlv_0, grammarAccess.getVarRefAccess().getVariableVariableCrossReference_0_0());
									
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4000:3: ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4000:3: ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4001:4: ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4001:4: ( (otherlv_1= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4002:5: (otherlv_1= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4002:5: (otherlv_1= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4003:6: otherlv_1= RULE_ID
					{

											if (current==null) {
												current = createModelElement(grammarAccess.getVarRefRule());
											}
										
					otherlv_1=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRef10835); 

											newLeafNode(otherlv_1, grammarAccess.getVarRefAccess().getContainerInstantiationCrossReference_1_0_0());
										
					}

					}

					otherlv_2=(Token)match(input,25,FOLLOW_25_in_ruleVarRef10860); 

									newLeafNode(otherlv_2, grammarAccess.getVarRefAccess().getFullStopKeyword_1_1());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4018:4: ( (otherlv_3= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4019:5: (otherlv_3= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4019:5: (otherlv_3= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4020:6: otherlv_3= RULE_ID
					{

											if (current==null) {
												current = createModelElement(grammarAccess.getVarRefRule());
											}
										
					otherlv_3=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRef10892); 

											newLeafNode(otherlv_3, grammarAccess.getVarRefAccess().getVariableVariableCrossReference_1_2_0());
										
					}

					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4033:3: ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4033:3: ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4034:4: ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4034:4: ( (lv_interleaved_4_0= 'interleaved' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4035:5: (lv_interleaved_4_0= 'interleaved' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4035:5: (lv_interleaved_4_0= 'interleaved' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4036:6: lv_interleaved_4_0= 'interleaved'
					{
					lv_interleaved_4_0=(Token)match(input,56,FOLLOW_56_in_ruleVarRef10946); 

											newLeafNode(lv_interleaved_4_0, grammarAccess.getVarRefAccess().getInterleavedInterleavedKeyword_2_0_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getVarRefRule());
											}
											setWithLastConsumed(current, "interleaved", lv_interleaved_4_0 != null, "interleaved");
										
					}

					}

					otherlv_5=(Token)match(input,18,FOLLOW_18_in_ruleVarRef10978); 

									newLeafNode(otherlv_5, grammarAccess.getVarRefAccess().getLeftParenthesisKeyword_2_1());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4052:4: ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) )
					int alt104=2;
					int LA104_0 = input.LA(1);
					if ( (LA104_0==RULE_ID) ) {
						int LA104_1 = input.LA(2);
						if ( (LA104_1==19) ) {
							alt104=1;
						}
						else if ( (LA104_1==25) ) {
							alt104=2;
						}

						else {
							int nvaeMark = input.mark();
							try {
								input.consume();
								NoViableAltException nvae =
									new NoViableAltException("", 104, 1, input);
								throw nvae;
							} finally {
								input.rewind(nvaeMark);
							}
						}

					}

					else {
						NoViableAltException nvae =
							new NoViableAltException("", 104, 0, input);
						throw nvae;
					}

					switch (alt104) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4053:5: ( (otherlv_6= RULE_ID ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4053:5: ( (otherlv_6= RULE_ID ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4054:6: (otherlv_6= RULE_ID )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4054:6: (otherlv_6= RULE_ID )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4055:7: otherlv_6= RULE_ID
							{

														if (current==null) {
															current = createModelElement(grammarAccess.getVarRefRule());
														}
													
							otherlv_6=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRef11019); 

														newLeafNode(otherlv_6, grammarAccess.getVarRefAccess().getVariableVariableCrossReference_2_2_0_0());
													
							}

							}

							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4067:5: ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4067:5: ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4068:6: ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4068:6: ( (otherlv_7= RULE_ID ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4069:7: (otherlv_7= RULE_ID )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4069:7: (otherlv_7= RULE_ID )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4070:8: otherlv_7= RULE_ID
							{

															if (current==null) {
																current = createModelElement(grammarAccess.getVarRefRule());
															}
														
							otherlv_7=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRef11091); 

															newLeafNode(otherlv_7, grammarAccess.getVarRefAccess().getContainerInstantiationCrossReference_2_2_1_0_0());
														
							}

							}

							otherlv_8=(Token)match(input,25,FOLLOW_25_in_ruleVarRef11124); 

													newLeafNode(otherlv_8, grammarAccess.getVarRefAccess().getFullStopKeyword_2_2_1_1());
												
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4085:6: ( (otherlv_9= RULE_ID ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4086:7: (otherlv_9= RULE_ID )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4086:7: (otherlv_9= RULE_ID )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4087:8: otherlv_9= RULE_ID
							{

															if (current==null) {
																current = createModelElement(grammarAccess.getVarRefRule());
															}
														
							otherlv_9=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRef11166); 

															newLeafNode(otherlv_9, grammarAccess.getVarRefAccess().getVariableVariableCrossReference_2_2_1_2_0());
														
							}

							}

							}

							}
							break;

					}

					otherlv_10=(Token)match(input,19,FOLLOW_19_in_ruleVarRef11208); 

									newLeafNode(otherlv_10, grammarAccess.getVarRefAccess().getRightParenthesisKeyword_2_3());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleVarRef"



	// $ANTLR start "entryRuleVarRefOrModeTransition"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4109:1: entryRuleVarRefOrModeTransition returns [EObject current=null] :iv_ruleVarRefOrModeTransition= ruleVarRefOrModeTransition EOF ;
	public final EObject entryRuleVarRefOrModeTransition() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleVarRefOrModeTransition =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4109:63: (iv_ruleVarRefOrModeTransition= ruleVarRefOrModeTransition EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4110:2: iv_ruleVarRefOrModeTransition= ruleVarRefOrModeTransition EOF
			{
			 newCompositeNode(grammarAccess.getVarRefOrModeTransitionRule()); 
			pushFollow(FOLLOW_ruleVarRefOrModeTransition_in_entryRuleVarRefOrModeTransition11239);
			iv_ruleVarRefOrModeTransition=ruleVarRefOrModeTransition();
			state._fsp--;

			 current =iv_ruleVarRefOrModeTransition; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleVarRefOrModeTransition11245); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleVarRefOrModeTransition"



	// $ANTLR start "ruleVarRefOrModeTransition"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4116:1: ruleVarRefOrModeTransition returns [EObject current=null] : (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) ) ;
	public final EObject ruleVarRefOrModeTransition() throws RecognitionException {
		EObject current = null;


		Token otherlv_2=null;
		Token otherlv_3=null;
		Token otherlv_4=null;
		EObject this_VarRef_0 =null;
		Enumerator lv_transition_1_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4122:2: ( (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4123:2: (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4123:2: (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) )
			int alt106=2;
			int LA106_0 = input.LA(1);
			if ( (LA106_0==RULE_ID||LA106_0==56) ) {
				alt106=1;
			}
			else if ( (LA106_0==52||LA106_0==72) ) {
				alt106=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 106, 0, input);
				throw nvae;
			}

			switch (alt106) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4124:3: this_VarRef_0= ruleVarRef
					{

								newCompositeNode(grammarAccess.getVarRefOrModeTransitionAccess().getVarRefParserRuleCall_0());
							
					pushFollow(FOLLOW_ruleVarRef_in_ruleVarRefOrModeTransition11278);
					this_VarRef_0=ruleVarRef();
					state._fsp--;


								current = this_VarRef_0;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4133:3: ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4133:3: ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4134:4: ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4134:4: ( (lv_transition_1_0= ruleModeTransition ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4135:5: (lv_transition_1_0= ruleModeTransition )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4135:5: (lv_transition_1_0= ruleModeTransition )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4136:6: lv_transition_1_0= ruleModeTransition
					{

											newCompositeNode(grammarAccess.getVarRefOrModeTransitionAccess().getTransitionModeTransitionEnumRuleCall_1_0_0());
										
					pushFollow(FOLLOW_ruleModeTransition_in_ruleVarRefOrModeTransition11321);
					lv_transition_1_0=ruleModeTransition();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getVarRefOrModeTransitionRule());
											}
											set(
												current,
												"transition",
												lv_transition_1_0,
												"org.lflang.LF.ModeTransition");
											afterParserOrEnumRuleCall();
										
					}

					}

					otherlv_2=(Token)match(input,18,FOLLOW_18_in_ruleVarRefOrModeTransition11346); 

									newLeafNode(otherlv_2, grammarAccess.getVarRefOrModeTransitionAccess().getLeftParenthesisKeyword_1_1());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4157:4: ( (otherlv_3= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4158:5: (otherlv_3= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4158:5: (otherlv_3= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4159:6: otherlv_3= RULE_ID
					{

											if (current==null) {
												current = createModelElement(grammarAccess.getVarRefOrModeTransitionRule());
											}
										
					otherlv_3=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleVarRefOrModeTransition11378); 

											newLeafNode(otherlv_3, grammarAccess.getVarRefOrModeTransitionAccess().getVariableModeCrossReference_1_2_0());
										
					}

					}

					otherlv_4=(Token)match(input,19,FOLLOW_19_in_ruleVarRefOrModeTransition11403); 

									newLeafNode(otherlv_4, grammarAccess.getVarRefOrModeTransitionAccess().getRightParenthesisKeyword_1_3());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleVarRefOrModeTransition"



	// $ANTLR start "entryRuleAssignment"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4179:1: entryRuleAssignment returns [EObject current=null] :iv_ruleAssignment= ruleAssignment EOF ;
	public final EObject entryRuleAssignment() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleAssignment =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4179:51: (iv_ruleAssignment= ruleAssignment EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4180:2: iv_ruleAssignment= ruleAssignment EOF
			{
			 newCompositeNode(grammarAccess.getAssignmentRule()); 
			pushFollow(FOLLOW_ruleAssignment_in_entryRuleAssignment11434);
			iv_ruleAssignment=ruleAssignment();
			state._fsp--;

			 current =iv_ruleAssignment; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleAssignment11440); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleAssignment"



	// $ANTLR start "ruleAssignment"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4186:1: ruleAssignment returns [EObject current=null] : ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) ) ;
	public final EObject ruleAssignment() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token lv_equals_1_0=null;
		Token lv_equals_3_0=null;
		Token lv_parens_4_0=null;
		Token otherlv_6=null;
		Token lv_parens_8_0=null;
		Token lv_braces_9_0=null;
		Token otherlv_11=null;
		Token lv_braces_13_0=null;
		EObject lv_rhs_2_0 =null;
		EObject lv_rhs_5_0 =null;
		EObject lv_rhs_7_0 =null;
		EObject lv_rhs_10_0 =null;
		EObject lv_rhs_12_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4192:2: ( ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4193:2: ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4193:2: ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4194:3: ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4194:3: ( (otherlv_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4195:4: (otherlv_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4195:4: (otherlv_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4196:5: otherlv_0= RULE_ID
			{

								if (current==null) {
									current = createModelElement(grammarAccess.getAssignmentRule());
								}
							
			otherlv_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleAssignment11486); 

								newLeafNode(otherlv_0, grammarAccess.getAssignmentAccess().getLhsParameterCrossReference_0_0());
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4207:3: ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) )
			int alt113=2;
			int LA113_0 = input.LA(1);
			if ( (LA113_0==32) ) {
				int LA113_1 = input.LA(2);
				if ( ((LA113_1 >= RULE_CHAR_LIT && LA113_1 <= RULE_FALSE)||(LA113_1 >= RULE_ID && LA113_1 <= RULE_INT)||LA113_1==RULE_NEGINT||(LA113_1 >= RULE_STRING && LA113_1 <= RULE_TRUE)||LA113_1==23||LA113_1==25||LA113_1==83) ) {
					alt113=1;
				}
				else if ( (LA113_1==18||LA113_1==82) ) {
					alt113=2;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 113, 1, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

			}
			else if ( (LA113_0==18||LA113_0==82) ) {
				alt113=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 113, 0, input);
				throw nvae;
			}

			switch (alt113) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4208:4: ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4208:4: ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4209:5: ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4209:5: ( (lv_equals_1_0= '=' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4210:6: (lv_equals_1_0= '=' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4210:6: (lv_equals_1_0= '=' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4211:7: lv_equals_1_0= '='
					{
					lv_equals_1_0=(Token)match(input,32,FOLLOW_32_in_ruleAssignment11533); 

												newLeafNode(lv_equals_1_0, grammarAccess.getAssignmentAccess().getEqualsEqualsSignKeyword_1_0_0_0());
											

												if (current==null) {
													current = createModelElement(grammarAccess.getAssignmentRule());
												}
												setWithLastConsumed(current, "equals", lv_equals_1_0, "=");
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4223:5: ( (lv_rhs_2_0= ruleExpression ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4224:6: (lv_rhs_2_0= ruleExpression )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4224:6: (lv_rhs_2_0= ruleExpression )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4225:7: lv_rhs_2_0= ruleExpression
					{

												newCompositeNode(grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_0_1_0());
											
					pushFollow(FOLLOW_ruleExpression_in_ruleAssignment11593);
					lv_rhs_2_0=ruleExpression();
					state._fsp--;


												if (current==null) {
													current = createModelElementForParent(grammarAccess.getAssignmentRule());
												}
												add(
													current,
													"rhs",
													lv_rhs_2_0,
													"org.lflang.LF.Expression");
												afterParserOrEnumRuleCall();
											
					}

					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4244:4: ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4244:4: ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4245:5: ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4245:5: ( (lv_equals_3_0= '=' ) )?
					int alt107=2;
					int LA107_0 = input.LA(1);
					if ( (LA107_0==32) ) {
						alt107=1;
					}
					switch (alt107) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4246:6: (lv_equals_3_0= '=' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4246:6: (lv_equals_3_0= '=' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4247:7: lv_equals_3_0= '='
							{
							lv_equals_3_0=(Token)match(input,32,FOLLOW_32_in_ruleAssignment11656); 

														newLeafNode(lv_equals_3_0, grammarAccess.getAssignmentAccess().getEqualsEqualsSignKeyword_1_1_0_0());
													

														if (current==null) {
															current = createModelElement(grammarAccess.getAssignmentRule());
														}
														setWithLastConsumed(current, "equals", lv_equals_3_0, "=");
													
							}

							}
							break;

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4259:5: ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )
					int alt112=2;
					int LA112_0 = input.LA(1);
					if ( (LA112_0==18) ) {
						alt112=1;
					}
					else if ( (LA112_0==82) ) {
						alt112=2;
					}

					else {
						NoViableAltException nvae =
							new NoViableAltException("", 112, 0, input);
						throw nvae;
					}

					switch (alt112) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4260:6: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4260:6: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4261:7: ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4261:7: ( (lv_parens_4_0= '(' ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4262:8: (lv_parens_4_0= '(' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4262:8: (lv_parens_4_0= '(' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4263:9: lv_parens_4_0= '('
							{
							lv_parens_4_0=(Token)match(input,18,FOLLOW_18_in_ruleAssignment11728); 

																newLeafNode(lv_parens_4_0, grammarAccess.getAssignmentAccess().getParensLeftParenthesisKeyword_1_1_1_0_0_0());
															

																if (current==null) {
																	current = createModelElement(grammarAccess.getAssignmentRule());
																}
																addWithLastConsumed(current, "parens", lv_parens_4_0, "(");
															
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4275:7: ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )?
							int alt109=2;
							int LA109_0 = input.LA(1);
							if ( ((LA109_0 >= RULE_CHAR_LIT && LA109_0 <= RULE_FALSE)||(LA109_0 >= RULE_ID && LA109_0 <= RULE_INT)||LA109_0==RULE_NEGINT||(LA109_0 >= RULE_STRING && LA109_0 <= RULE_TRUE)||LA109_0==23||LA109_0==25||LA109_0==83) ) {
								alt109=1;
							}
							switch (alt109) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4276:8: ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )*
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4276:8: ( (lv_rhs_5_0= ruleExpression ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4277:9: (lv_rhs_5_0= ruleExpression )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4277:9: (lv_rhs_5_0= ruleExpression )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4278:10: lv_rhs_5_0= ruleExpression
									{

																			newCompositeNode(grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_0_1_0_0());
																		
									pushFollow(FOLLOW_ruleExpression_in_ruleAssignment11816);
									lv_rhs_5_0=ruleExpression();
									state._fsp--;


																			if (current==null) {
																				current = createModelElementForParent(grammarAccess.getAssignmentRule());
																			}
																			add(
																				current,
																				"rhs",
																				lv_rhs_5_0,
																				"org.lflang.LF.Expression");
																			afterParserOrEnumRuleCall();
																		
									}

									}

									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4295:8: (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )*
									loop108:
									while (true) {
										int alt108=2;
										int LA108_0 = input.LA(1);
										if ( (LA108_0==22) ) {
											alt108=1;
										}

										switch (alt108) {
										case 1 :
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4296:9: otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) )
											{
											otherlv_6=(Token)match(input,22,FOLLOW_22_in_ruleAssignment11867); 

																				newLeafNode(otherlv_6, grammarAccess.getAssignmentAccess().getCommaKeyword_1_1_1_0_1_1_0());
																			
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4300:9: ( (lv_rhs_7_0= ruleExpression ) )
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4301:10: (lv_rhs_7_0= ruleExpression )
											{
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4301:10: (lv_rhs_7_0= ruleExpression )
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4302:11: lv_rhs_7_0= ruleExpression
											{

																						newCompositeNode(grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_0_1_1_1_0());
																					
											pushFollow(FOLLOW_ruleExpression_in_ruleAssignment11924);
											lv_rhs_7_0=ruleExpression();
											state._fsp--;


																						if (current==null) {
																							current = createModelElementForParent(grammarAccess.getAssignmentRule());
																						}
																						add(
																							current,
																							"rhs",
																							lv_rhs_7_0,
																							"org.lflang.LF.Expression");
																						afterParserOrEnumRuleCall();
																					
											}

											}

											}
											break;

										default :
											break loop108;
										}
									}

									}
									break;

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4321:7: ( (lv_parens_8_0= ')' ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4322:8: (lv_parens_8_0= ')' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4322:8: (lv_parens_8_0= ')' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4323:9: lv_parens_8_0= ')'
							{
							lv_parens_8_0=(Token)match(input,19,FOLLOW_19_in_ruleAssignment12005); 

																newLeafNode(lv_parens_8_0, grammarAccess.getAssignmentAccess().getParensRightParenthesisKeyword_1_1_1_0_2_0());
															

																if (current==null) {
																	current = createModelElement(grammarAccess.getAssignmentRule());
																}
																addWithLastConsumed(current, "parens", lv_parens_8_0, ")");
															
							}

							}

							}

							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4337:6: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4337:6: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4338:7: ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4338:7: ( (lv_braces_9_0= '{' ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4339:8: (lv_braces_9_0= '{' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4339:8: (lv_braces_9_0= '{' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4340:9: lv_braces_9_0= '{'
							{
							lv_braces_9_0=(Token)match(input,82,FOLLOW_82_in_ruleAssignment12096); 

																newLeafNode(lv_braces_9_0, grammarAccess.getAssignmentAccess().getBracesLeftCurlyBracketKeyword_1_1_1_1_0_0());
															

																if (current==null) {
																	current = createModelElement(grammarAccess.getAssignmentRule());
																}
																addWithLastConsumed(current, "braces", lv_braces_9_0, "{");
															
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4352:7: ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )?
							int alt111=2;
							int LA111_0 = input.LA(1);
							if ( ((LA111_0 >= RULE_CHAR_LIT && LA111_0 <= RULE_FALSE)||(LA111_0 >= RULE_ID && LA111_0 <= RULE_INT)||LA111_0==RULE_NEGINT||(LA111_0 >= RULE_STRING && LA111_0 <= RULE_TRUE)||LA111_0==23||LA111_0==25||LA111_0==83) ) {
								alt111=1;
							}
							switch (alt111) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4353:8: ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )*
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4353:8: ( (lv_rhs_10_0= ruleExpression ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4354:9: (lv_rhs_10_0= ruleExpression )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4354:9: (lv_rhs_10_0= ruleExpression )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4355:10: lv_rhs_10_0= ruleExpression
									{

																			newCompositeNode(grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_1_1_0_0());
																		
									pushFollow(FOLLOW_ruleExpression_in_ruleAssignment12184);
									lv_rhs_10_0=ruleExpression();
									state._fsp--;


																			if (current==null) {
																				current = createModelElementForParent(grammarAccess.getAssignmentRule());
																			}
																			add(
																				current,
																				"rhs",
																				lv_rhs_10_0,
																				"org.lflang.LF.Expression");
																			afterParserOrEnumRuleCall();
																		
									}

									}

									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4372:8: (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )*
									loop110:
									while (true) {
										int alt110=2;
										int LA110_0 = input.LA(1);
										if ( (LA110_0==22) ) {
											alt110=1;
										}

										switch (alt110) {
										case 1 :
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4373:9: otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) )
											{
											otherlv_11=(Token)match(input,22,FOLLOW_22_in_ruleAssignment12235); 

																				newLeafNode(otherlv_11, grammarAccess.getAssignmentAccess().getCommaKeyword_1_1_1_1_1_1_0());
																			
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4377:9: ( (lv_rhs_12_0= ruleExpression ) )
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4378:10: (lv_rhs_12_0= ruleExpression )
											{
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4378:10: (lv_rhs_12_0= ruleExpression )
											// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4379:11: lv_rhs_12_0= ruleExpression
											{

																						newCompositeNode(grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_1_1_1_1_0());
																					
											pushFollow(FOLLOW_ruleExpression_in_ruleAssignment12292);
											lv_rhs_12_0=ruleExpression();
											state._fsp--;


																						if (current==null) {
																							current = createModelElementForParent(grammarAccess.getAssignmentRule());
																						}
																						add(
																							current,
																							"rhs",
																							lv_rhs_12_0,
																							"org.lflang.LF.Expression");
																						afterParserOrEnumRuleCall();
																					
											}

											}

											}
											break;

										default :
											break loop110;
										}
									}

									}
									break;

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4398:7: ( (lv_braces_13_0= '}' ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4399:8: (lv_braces_13_0= '}' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4399:8: (lv_braces_13_0= '}' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4400:9: lv_braces_13_0= '}'
							{
							lv_braces_13_0=(Token)match(input,84,FOLLOW_84_in_ruleAssignment12373); 

																newLeafNode(lv_braces_13_0, grammarAccess.getAssignmentAccess().getBracesRightCurlyBracketKeyword_1_1_1_1_2_0());
															

																if (current==null) {
																	current = createModelElement(grammarAccess.getAssignmentRule());
																}
																addWithLastConsumed(current, "braces", lv_braces_13_0, "}");
															
							}

							}

							}

							}
							break;

					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleAssignment"



	// $ANTLR start "entryRuleParameter"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4420:1: entryRuleParameter returns [EObject current=null] :iv_ruleParameter= ruleParameter EOF ;
	public final EObject entryRuleParameter() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleParameter =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4420:50: (iv_ruleParameter= ruleParameter EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4421:2: iv_ruleParameter= ruleParameter EOF
			{
			 newCompositeNode(grammarAccess.getParameterRule()); 
			pushFollow(FOLLOW_ruleParameter_in_entryRuleParameter12454);
			iv_ruleParameter=ruleParameter();
			state._fsp--;

			 current =iv_ruleParameter; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleParameter12460); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleParameter"



	// $ANTLR start "ruleParameter"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4427:1: ruleParameter returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? ) ;
	public final EObject ruleParameter() throws RecognitionException {
		EObject current = null;


		Token lv_name_1_0=null;
		Token otherlv_2=null;
		Token lv_parens_4_0=null;
		Token otherlv_6=null;
		Token lv_parens_8_0=null;
		Token lv_braces_9_0=null;
		Token otherlv_11=null;
		Token lv_braces_13_0=null;
		EObject lv_attributes_0_0 =null;
		EObject lv_type_3_0 =null;
		EObject lv_init_5_0 =null;
		EObject lv_init_7_0 =null;
		EObject lv_init_10_0 =null;
		EObject lv_init_12_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4433:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4434:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4434:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4435:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4435:3: ( (lv_attributes_0_0= ruleAttribute ) )*
			loop114:
			while (true) {
				int alt114=2;
				int LA114_0 = input.LA(1);
				if ( (LA114_0==35) ) {
					alt114=1;
				}

				switch (alt114) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4436:4: (lv_attributes_0_0= ruleAttribute )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4436:4: (lv_attributes_0_0= ruleAttribute )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4437:5: lv_attributes_0_0= ruleAttribute
					{

										newCompositeNode(grammarAccess.getParameterAccess().getAttributesAttributeParserRuleCall_0_0());
									
					pushFollow(FOLLOW_ruleAttribute_in_ruleParameter12506);
					lv_attributes_0_0=ruleAttribute();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getParameterRule());
										}
										add(
											current,
											"attributes",
											lv_attributes_0_0,
											"org.lflang.LF.Attribute");
										afterParserOrEnumRuleCall();
									
					}

					}
					break;

				default :
					break loop114;
				}
			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4454:3: ( (lv_name_1_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4455:4: (lv_name_1_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4455:4: (lv_name_1_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4456:5: lv_name_1_0= RULE_ID
			{
			lv_name_1_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleParameter12539); 

								newLeafNode(lv_name_1_0, grammarAccess.getParameterAccess().getNameIDTerminalRuleCall_1_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getParameterRule());
								}
								setWithLastConsumed(
									current,
									"name",
									lv_name_1_0,
									"org.lflang.LF.ID");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4472:3: (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )?
			int alt115=2;
			int LA115_0 = input.LA(1);
			if ( (LA115_0==27) ) {
				alt115=1;
			}
			switch (alt115) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4473:4: otherlv_2= ':' ( (lv_type_3_0= ruleType ) )
					{
					otherlv_2=(Token)match(input,27,FOLLOW_27_in_ruleParameter12571); 

									newLeafNode(otherlv_2, grammarAccess.getParameterAccess().getColonKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4477:4: ( (lv_type_3_0= ruleType ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4478:5: (lv_type_3_0= ruleType )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4478:5: (lv_type_3_0= ruleType )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4479:6: lv_type_3_0= ruleType
					{

											newCompositeNode(grammarAccess.getParameterAccess().getTypeTypeParserRuleCall_2_1_0());
										
					pushFollow(FOLLOW_ruleType_in_ruleParameter12603);
					lv_type_3_0=ruleType();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getParameterRule());
											}
											set(
												current,
												"type",
												lv_type_3_0,
												"org.lflang.LF.Type");
											afterParserOrEnumRuleCall();
										
					}

					}

					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4497:3: ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )?
			int alt120=3;
			int LA120_0 = input.LA(1);
			if ( (LA120_0==18) ) {
				alt120=1;
			}
			else if ( (LA120_0==82) ) {
				alt120=2;
			}
			switch (alt120) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4498:4: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4498:4: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4499:5: ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4499:5: ( (lv_parens_4_0= '(' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4500:6: (lv_parens_4_0= '(' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4500:6: (lv_parens_4_0= '(' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4501:7: lv_parens_4_0= '('
					{
					lv_parens_4_0=(Token)match(input,18,FOLLOW_18_in_ruleParameter12658); 

												newLeafNode(lv_parens_4_0, grammarAccess.getParameterAccess().getParensLeftParenthesisKeyword_3_0_0_0());
											

												if (current==null) {
													current = createModelElement(grammarAccess.getParameterRule());
												}
												addWithLastConsumed(current, "parens", lv_parens_4_0, "(");
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4513:5: ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )?
					int alt117=2;
					int LA117_0 = input.LA(1);
					if ( ((LA117_0 >= RULE_CHAR_LIT && LA117_0 <= RULE_FALSE)||(LA117_0 >= RULE_ID && LA117_0 <= RULE_INT)||LA117_0==RULE_NEGINT||(LA117_0 >= RULE_STRING && LA117_0 <= RULE_TRUE)||LA117_0==23||LA117_0==25||LA117_0==83) ) {
						alt117=1;
					}
					switch (alt117) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4514:6: ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )*
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4514:6: ( (lv_init_5_0= ruleExpression ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4515:7: (lv_init_5_0= ruleExpression )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4515:7: (lv_init_5_0= ruleExpression )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4516:8: lv_init_5_0= ruleExpression
							{

															newCompositeNode(grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_0_1_0_0());
														
							pushFollow(FOLLOW_ruleExpression_in_ruleParameter12728);
							lv_init_5_0=ruleExpression();
							state._fsp--;


															if (current==null) {
																current = createModelElementForParent(grammarAccess.getParameterRule());
															}
															add(
																current,
																"init",
																lv_init_5_0,
																"org.lflang.LF.Expression");
															afterParserOrEnumRuleCall();
														
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4533:6: (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )*
							loop116:
							while (true) {
								int alt116=2;
								int LA116_0 = input.LA(1);
								if ( (LA116_0==22) ) {
									alt116=1;
								}

								switch (alt116) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4534:7: otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) )
									{
									otherlv_6=(Token)match(input,22,FOLLOW_22_in_ruleParameter12769); 

																newLeafNode(otherlv_6, grammarAccess.getParameterAccess().getCommaKeyword_3_0_1_1_0());
															
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4538:7: ( (lv_init_7_0= ruleExpression ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4539:8: (lv_init_7_0= ruleExpression )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4539:8: (lv_init_7_0= ruleExpression )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4540:9: lv_init_7_0= ruleExpression
									{

																		newCompositeNode(grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_0_1_1_1_0());
																	
									pushFollow(FOLLOW_ruleExpression_in_ruleParameter12816);
									lv_init_7_0=ruleExpression();
									state._fsp--;


																		if (current==null) {
																			current = createModelElementForParent(grammarAccess.getParameterRule());
																		}
																		add(
																			current,
																			"init",
																			lv_init_7_0,
																			"org.lflang.LF.Expression");
																		afterParserOrEnumRuleCall();
																	
									}

									}

									}
									break;

								default :
									break loop116;
								}
							}

							}
							break;

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4559:5: ( (lv_parens_8_0= ')' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4560:6: (lv_parens_8_0= ')' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4560:6: (lv_parens_8_0= ')' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4561:7: lv_parens_8_0= ')'
					{
					lv_parens_8_0=(Token)match(input,19,FOLLOW_19_in_ruleParameter12881); 

												newLeafNode(lv_parens_8_0, grammarAccess.getParameterAccess().getParensRightParenthesisKeyword_3_0_2_0());
											

												if (current==null) {
													current = createModelElement(grammarAccess.getParameterRule());
												}
												addWithLastConsumed(current, "parens", lv_parens_8_0, ")");
											
					}

					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4575:4: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4575:4: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4576:5: ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4576:5: ( (lv_braces_9_0= '{' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4577:6: (lv_braces_9_0= '{' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4577:6: (lv_braces_9_0= '{' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4578:7: lv_braces_9_0= '{'
					{
					lv_braces_9_0=(Token)match(input,82,FOLLOW_82_in_ruleParameter12952); 

												newLeafNode(lv_braces_9_0, grammarAccess.getParameterAccess().getBracesLeftCurlyBracketKeyword_3_1_0_0());
											

												if (current==null) {
													current = createModelElement(grammarAccess.getParameterRule());
												}
												addWithLastConsumed(current, "braces", lv_braces_9_0, "{");
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4590:5: ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )?
					int alt119=2;
					int LA119_0 = input.LA(1);
					if ( ((LA119_0 >= RULE_CHAR_LIT && LA119_0 <= RULE_FALSE)||(LA119_0 >= RULE_ID && LA119_0 <= RULE_INT)||LA119_0==RULE_NEGINT||(LA119_0 >= RULE_STRING && LA119_0 <= RULE_TRUE)||LA119_0==23||LA119_0==25||LA119_0==83) ) {
						alt119=1;
					}
					switch (alt119) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4591:6: ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )*
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4591:6: ( (lv_init_10_0= ruleExpression ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4592:7: (lv_init_10_0= ruleExpression )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4592:7: (lv_init_10_0= ruleExpression )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4593:8: lv_init_10_0= ruleExpression
							{

															newCompositeNode(grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_1_1_0_0());
														
							pushFollow(FOLLOW_ruleExpression_in_ruleParameter13022);
							lv_init_10_0=ruleExpression();
							state._fsp--;


															if (current==null) {
																current = createModelElementForParent(grammarAccess.getParameterRule());
															}
															add(
																current,
																"init",
																lv_init_10_0,
																"org.lflang.LF.Expression");
															afterParserOrEnumRuleCall();
														
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4610:6: (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )*
							loop118:
							while (true) {
								int alt118=2;
								int LA118_0 = input.LA(1);
								if ( (LA118_0==22) ) {
									alt118=1;
								}

								switch (alt118) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4611:7: otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) )
									{
									otherlv_11=(Token)match(input,22,FOLLOW_22_in_ruleParameter13063); 

																newLeafNode(otherlv_11, grammarAccess.getParameterAccess().getCommaKeyword_3_1_1_1_0());
															
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4615:7: ( (lv_init_12_0= ruleExpression ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4616:8: (lv_init_12_0= ruleExpression )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4616:8: (lv_init_12_0= ruleExpression )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4617:9: lv_init_12_0= ruleExpression
									{

																		newCompositeNode(grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_1_1_1_1_0());
																	
									pushFollow(FOLLOW_ruleExpression_in_ruleParameter13110);
									lv_init_12_0=ruleExpression();
									state._fsp--;


																		if (current==null) {
																			current = createModelElementForParent(grammarAccess.getParameterRule());
																		}
																		add(
																			current,
																			"init",
																			lv_init_12_0,
																			"org.lflang.LF.Expression");
																		afterParserOrEnumRuleCall();
																	
									}

									}

									}
									break;

								default :
									break loop118;
								}
							}

							}
							break;

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4636:5: ( (lv_braces_13_0= '}' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4637:6: (lv_braces_13_0= '}' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4637:6: (lv_braces_13_0= '}' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4638:7: lv_braces_13_0= '}'
					{
					lv_braces_13_0=(Token)match(input,84,FOLLOW_84_in_ruleParameter13175); 

												newLeafNode(lv_braces_13_0, grammarAccess.getParameterAccess().getBracesRightCurlyBracketKeyword_3_1_2_0());
											

												if (current==null) {
													current = createModelElement(grammarAccess.getParameterRule());
												}
												addWithLastConsumed(current, "braces", lv_braces_13_0, "}");
											
					}

					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleParameter"



	// $ANTLR start "entryRuleExpression"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4656:1: entryRuleExpression returns [EObject current=null] :iv_ruleExpression= ruleExpression EOF ;
	public final EObject entryRuleExpression() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleExpression =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4656:51: (iv_ruleExpression= ruleExpression EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4657:2: iv_ruleExpression= ruleExpression EOF
			{
			 newCompositeNode(grammarAccess.getExpressionRule()); 
			pushFollow(FOLLOW_ruleExpression_in_entryRuleExpression13236);
			iv_ruleExpression=ruleExpression();
			state._fsp--;

			 current =iv_ruleExpression; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleExpression13242); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleExpression"



	// $ANTLR start "ruleExpression"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4663:1: ruleExpression returns [EObject current=null] : ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) |this_Time_2= ruleTime |this_ParameterReference_3= ruleParameterReference |this_Code_4= ruleCode ) ;
	public final EObject ruleExpression() throws RecognitionException {
		EObject current = null;


		AntlrDatatypeRuleToken lv_literal_1_0 =null;
		EObject this_Time_2 =null;
		EObject this_ParameterReference_3 =null;
		EObject this_Code_4 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4669:2: ( ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) |this_Time_2= ruleTime |this_ParameterReference_3= ruleParameterReference |this_Code_4= ruleCode ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4670:2: ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) |this_Time_2= ruleTime |this_ParameterReference_3= ruleParameterReference |this_Code_4= ruleCode )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4670:2: ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) |this_Time_2= ruleTime |this_ParameterReference_3= ruleParameterReference |this_Code_4= ruleCode )
			int alt121=4;
			alt121 = dfa121.predict(input);
			switch (alt121) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4671:3: ( () ( (lv_literal_1_0= ruleLiteral ) ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4671:3: ( () ( (lv_literal_1_0= ruleLiteral ) ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4672:4: () ( (lv_literal_1_0= ruleLiteral ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4672:4: ()
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4673:5: 
					{

										current = forceCreateModelElement(
											grammarAccess.getExpressionAccess().getLiteralAction_0_0(),
											current);
									
					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4679:4: ( (lv_literal_1_0= ruleLiteral ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4680:5: (lv_literal_1_0= ruleLiteral )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4680:5: (lv_literal_1_0= ruleLiteral )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4681:6: lv_literal_1_0= ruleLiteral
					{

											newCompositeNode(grammarAccess.getExpressionAccess().getLiteralLiteralParserRuleCall_0_1_0());
										
					pushFollow(FOLLOW_ruleLiteral_in_ruleExpression13312);
					lv_literal_1_0=ruleLiteral();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getExpressionRule());
											}
											set(
												current,
												"literal",
												lv_literal_1_0,
												"org.lflang.LF.Literal");
											afterParserOrEnumRuleCall();
										
					}

					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4700:3: this_Time_2= ruleTime
					{

								newCompositeNode(grammarAccess.getExpressionAccess().getTimeParserRuleCall_1());
							
					pushFollow(FOLLOW_ruleTime_in_ruleExpression13352);
					this_Time_2=ruleTime();
					state._fsp--;


								current = this_Time_2;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4709:3: this_ParameterReference_3= ruleParameterReference
					{

								newCompositeNode(grammarAccess.getExpressionAccess().getParameterReferenceParserRuleCall_2());
							
					pushFollow(FOLLOW_ruleParameterReference_in_ruleExpression13374);
					this_ParameterReference_3=ruleParameterReference();
					state._fsp--;


								current = this_ParameterReference_3;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4718:3: this_Code_4= ruleCode
					{

								newCompositeNode(grammarAccess.getExpressionAccess().getCodeParserRuleCall_3());
							
					pushFollow(FOLLOW_ruleCode_in_ruleExpression13396);
					this_Code_4=ruleCode();
					state._fsp--;


								current = this_Code_4;
								afterParserOrEnumRuleCall();
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleExpression"



	// $ANTLR start "entryRuleParameterReference"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4730:1: entryRuleParameterReference returns [EObject current=null] :iv_ruleParameterReference= ruleParameterReference EOF ;
	public final EObject entryRuleParameterReference() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleParameterReference =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4730:59: (iv_ruleParameterReference= ruleParameterReference EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4731:2: iv_ruleParameterReference= ruleParameterReference EOF
			{
			 newCompositeNode(grammarAccess.getParameterReferenceRule()); 
			pushFollow(FOLLOW_ruleParameterReference_in_entryRuleParameterReference13422);
			iv_ruleParameterReference=ruleParameterReference();
			state._fsp--;

			 current =iv_ruleParameterReference; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleParameterReference13428); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleParameterReference"



	// $ANTLR start "ruleParameterReference"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4737:1: ruleParameterReference returns [EObject current=null] : ( (otherlv_0= RULE_ID ) ) ;
	public final EObject ruleParameterReference() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4743:2: ( ( (otherlv_0= RULE_ID ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4744:2: ( (otherlv_0= RULE_ID ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4744:2: ( (otherlv_0= RULE_ID ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4745:3: (otherlv_0= RULE_ID )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4745:3: (otherlv_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4746:4: otherlv_0= RULE_ID
			{

							if (current==null) {
								current = createModelElement(grammarAccess.getParameterReferenceRule());
							}
						
			otherlv_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleParameterReference13467); 

							newLeafNode(otherlv_0, grammarAccess.getParameterReferenceAccess().getParameterParameterCrossReference_0());
						
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleParameterReference"



	// $ANTLR start "entryRuleTime"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4760:1: entryRuleTime returns [EObject current=null] :iv_ruleTime= ruleTime EOF ;
	public final EObject entryRuleTime() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleTime =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4760:45: (iv_ruleTime= ruleTime EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4761:2: iv_ruleTime= ruleTime EOF
			{
			 newCompositeNode(grammarAccess.getTimeRule()); 
			pushFollow(FOLLOW_ruleTime_in_entryRuleTime13498);
			iv_ruleTime=ruleTime();
			state._fsp--;

			 current =iv_ruleTime; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTime13504); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTime"



	// $ANTLR start "ruleTime"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4767:1: ruleTime returns [EObject current=null] : ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) ) ;
	public final EObject ruleTime() throws RecognitionException {
		EObject current = null;


		Token lv_interval_0_0=null;
		AntlrDatatypeRuleToken lv_unit_1_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4773:2: ( ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4774:2: ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4774:2: ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4775:3: ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4775:3: ( (lv_interval_0_0= RULE_INT ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4776:4: (lv_interval_0_0= RULE_INT )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4776:4: (lv_interval_0_0= RULE_INT )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4777:5: lv_interval_0_0= RULE_INT
			{
			lv_interval_0_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleTime13544); 

								newLeafNode(lv_interval_0_0, grammarAccess.getTimeAccess().getIntervalINTTerminalRuleCall_0_0());
							

								if (current==null) {
									current = createModelElement(grammarAccess.getTimeRule());
								}
								setWithLastConsumed(
									current,
									"interval",
									lv_interval_0_0,
									"org.lflang.LF.INT");
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4793:3: ( (lv_unit_1_0= ruleTimeUnit ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4794:4: (lv_unit_1_0= ruleTimeUnit )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4794:4: (lv_unit_1_0= ruleTimeUnit )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4795:5: lv_unit_1_0= ruleTimeUnit
			{

								newCompositeNode(grammarAccess.getTimeAccess().getUnitTimeUnitParserRuleCall_1_0());
							
			pushFollow(FOLLOW_ruleTimeUnit_in_ruleTime13588);
			lv_unit_1_0=ruleTimeUnit();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getTimeRule());
								}
								set(
									current,
									"unit",
									lv_unit_1_0,
									"org.lflang.LF.TimeUnit");
								afterParserOrEnumRuleCall();
							
			}

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTime"



	// $ANTLR start "entryRulePort"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4816:1: entryRulePort returns [EObject current=null] :iv_rulePort= rulePort EOF ;
	public final EObject entryRulePort() throws RecognitionException {
		EObject current = null;


		EObject iv_rulePort =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4816:45: (iv_rulePort= rulePort EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4817:2: iv_rulePort= rulePort EOF
			{
			 newCompositeNode(grammarAccess.getPortRule()); 
			pushFollow(FOLLOW_rulePort_in_entryRulePort13625);
			iv_rulePort=rulePort();
			state._fsp--;

			 current =iv_rulePort; 
			match(input,EOF,FOLLOW_EOF_in_entryRulePort13631); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRulePort"



	// $ANTLR start "rulePort"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4823:1: rulePort returns [EObject current=null] : (this_Input_0= ruleInput |this_Output_1= ruleOutput ) ;
	public final EObject rulePort() throws RecognitionException {
		EObject current = null;


		EObject this_Input_0 =null;
		EObject this_Output_1 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4829:2: ( (this_Input_0= ruleInput |this_Output_1= ruleOutput ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4830:2: (this_Input_0= ruleInput |this_Output_1= ruleOutput )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4830:2: (this_Input_0= ruleInput |this_Output_1= ruleOutput )
			int alt122=2;
			alt122 = dfa122.predict(input);
			switch (alt122) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4831:3: this_Input_0= ruleInput
					{

								newCompositeNode(grammarAccess.getPortAccess().getInputParserRuleCall_0());
							
					pushFollow(FOLLOW_ruleInput_in_rulePort13664);
					this_Input_0=ruleInput();
					state._fsp--;


								current = this_Input_0;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4840:3: this_Output_1= ruleOutput
					{

								newCompositeNode(grammarAccess.getPortAccess().getOutputParserRuleCall_1());
							
					pushFollow(FOLLOW_ruleOutput_in_rulePort13686);
					this_Output_1=ruleOutput();
					state._fsp--;


								current = this_Output_1;
								afterParserOrEnumRuleCall();
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "rulePort"



	// $ANTLR start "entryRuleType"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4852:1: entryRuleType returns [EObject current=null] :iv_ruleType= ruleType EOF ;
	public final EObject entryRuleType() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleType =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4852:45: (iv_ruleType= ruleType EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4853:2: iv_ruleType= ruleType EOF
			{
			 newCompositeNode(grammarAccess.getTypeRule()); 
			pushFollow(FOLLOW_ruleType_in_entryRuleType13712);
			iv_ruleType=ruleType();
			state._fsp--;

			 current =iv_ruleType; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleType13718); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleType"



	// $ANTLR start "ruleType"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4859:1: ruleType returns [EObject current=null] : ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) ) ;
	public final EObject ruleType() throws RecognitionException {
		EObject current = null;


		Token lv_time_0_0=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		Token otherlv_7=null;
		Token lv_stars_8_0=null;
		EObject lv_arraySpec_1_0 =null;
		AntlrDatatypeRuleToken lv_id_2_0 =null;
		EObject lv_typeParms_4_0 =null;
		EObject lv_typeParms_6_0 =null;
		EObject lv_arraySpec_9_0 =null;
		EObject lv_code_10_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4865:2: ( ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4866:2: ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4866:2: ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) )
			int alt128=3;
			switch ( input.LA(1) ) {
			case 78:
				{
				alt128=1;
				}
				break;
			case RULE_ID:
				{
				alt128=2;
				}
				break;
			case 83:
				{
				alt128=3;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 128, 0, input);
				throw nvae;
			}
			switch (alt128) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4867:3: ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4867:3: ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4868:4: ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )?
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4868:4: ( (lv_time_0_0= 'time' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4869:5: (lv_time_0_0= 'time' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4869:5: (lv_time_0_0= 'time' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4870:6: lv_time_0_0= 'time'
					{
					lv_time_0_0=(Token)match(input,78,FOLLOW_78_in_ruleType13765); 

											newLeafNode(lv_time_0_0, grammarAccess.getTypeAccess().getTimeTimeKeyword_0_0_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getTypeRule());
											}
											setWithLastConsumed(current, "time", lv_time_0_0 != null, "time");
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4882:4: ( (lv_arraySpec_1_0= ruleArraySpec ) )?
					int alt123=2;
					int LA123_0 = input.LA(1);
					if ( (LA123_0==38) ) {
						alt123=1;
					}
					switch (alt123) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4883:5: (lv_arraySpec_1_0= ruleArraySpec )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4883:5: (lv_arraySpec_1_0= ruleArraySpec )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4884:6: lv_arraySpec_1_0= ruleArraySpec
							{

													newCompositeNode(grammarAccess.getTypeAccess().getArraySpecArraySpecParserRuleCall_0_1_0());
												
							pushFollow(FOLLOW_ruleArraySpec_in_ruleType13817);
							lv_arraySpec_1_0=ruleArraySpec();
							state._fsp--;


													if (current==null) {
														current = createModelElementForParent(grammarAccess.getTypeRule());
													}
													set(
														current,
														"arraySpec",
														lv_arraySpec_1_0,
														"org.lflang.LF.ArraySpec");
													afterParserOrEnumRuleCall();
												
							}

							}
							break;

					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4903:3: ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4903:3: ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4904:4: ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )?
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4904:4: ( (lv_id_2_0= ruleDottedName ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4905:5: (lv_id_2_0= ruleDottedName )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4905:5: (lv_id_2_0= ruleDottedName )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4906:6: lv_id_2_0= ruleDottedName
					{

											newCompositeNode(grammarAccess.getTypeAccess().getIdDottedNameParserRuleCall_1_0_0());
										
					pushFollow(FOLLOW_ruleDottedName_in_ruleType13879);
					lv_id_2_0=ruleDottedName();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getTypeRule());
											}
											set(
												current,
												"id",
												lv_id_2_0,
												"org.lflang.LF.DottedName");
											afterParserOrEnumRuleCall();
										
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4923:4: (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )?
					int alt125=2;
					int LA125_0 = input.LA(1);
					if ( (LA125_0==31) ) {
						alt125=1;
					}
					switch (alt125) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4924:5: otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>'
							{
							otherlv_3=(Token)match(input,31,FOLLOW_31_in_ruleType13910); 

												newLeafNode(otherlv_3, grammarAccess.getTypeAccess().getLessThanSignKeyword_1_1_0());
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4928:5: ( (lv_typeParms_4_0= ruleType ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4929:6: (lv_typeParms_4_0= ruleType )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4929:6: (lv_typeParms_4_0= ruleType )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4930:7: lv_typeParms_4_0= ruleType
							{

														newCompositeNode(grammarAccess.getTypeAccess().getTypeParmsTypeParserRuleCall_1_1_1_0());
													
							pushFollow(FOLLOW_ruleType_in_ruleType13947);
							lv_typeParms_4_0=ruleType();
							state._fsp--;


														if (current==null) {
															current = createModelElementForParent(grammarAccess.getTypeRule());
														}
														add(
															current,
															"typeParms",
															lv_typeParms_4_0,
															"org.lflang.LF.Type");
														afterParserOrEnumRuleCall();
													
							}

							}

							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4947:5: (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )*
							loop124:
							while (true) {
								int alt124=2;
								int LA124_0 = input.LA(1);
								if ( (LA124_0==22) ) {
									alt124=1;
								}

								switch (alt124) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4948:6: otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) )
									{
									otherlv_5=(Token)match(input,22,FOLLOW_22_in_ruleType13983); 

															newLeafNode(otherlv_5, grammarAccess.getTypeAccess().getCommaKeyword_1_1_2_0());
														
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4952:6: ( (lv_typeParms_6_0= ruleType ) )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4953:7: (lv_typeParms_6_0= ruleType )
									{
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4953:7: (lv_typeParms_6_0= ruleType )
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4954:8: lv_typeParms_6_0= ruleType
									{

																	newCompositeNode(grammarAccess.getTypeAccess().getTypeParmsTypeParserRuleCall_1_1_2_1_0());
																
									pushFollow(FOLLOW_ruleType_in_ruleType14025);
									lv_typeParms_6_0=ruleType();
									state._fsp--;


																	if (current==null) {
																		current = createModelElementForParent(grammarAccess.getTypeRule());
																	}
																	add(
																		current,
																		"typeParms",
																		lv_typeParms_6_0,
																		"org.lflang.LF.Type");
																	afterParserOrEnumRuleCall();
																
									}

									}

									}
									break;

								default :
									break loop124;
								}
							}

							otherlv_7=(Token)match(input,34,FOLLOW_34_in_ruleType14064); 

												newLeafNode(otherlv_7, grammarAccess.getTypeAccess().getGreaterThanSignKeyword_1_1_3());
											
							}
							break;

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4977:4: ( (lv_stars_8_0= '*' ) )*
					loop126:
					while (true) {
						int alt126=2;
						int LA126_0 = input.LA(1);
						if ( (LA126_0==20) ) {
							alt126=1;
						}

						switch (alt126) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4978:5: (lv_stars_8_0= '*' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4978:5: (lv_stars_8_0= '*' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4979:6: lv_stars_8_0= '*'
							{
							lv_stars_8_0=(Token)match(input,20,FOLLOW_20_in_ruleType14096); 

													newLeafNode(lv_stars_8_0, grammarAccess.getTypeAccess().getStarsAsteriskKeyword_1_2_0());
												

													if (current==null) {
														current = createModelElement(grammarAccess.getTypeRule());
													}
													addWithLastConsumed(current, "stars", lv_stars_8_0, "*");
												
							}

							}
							break;

						default :
							break loop126;
						}
					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4991:4: ( (lv_arraySpec_9_0= ruleArraySpec ) )?
					int alt127=2;
					int LA127_0 = input.LA(1);
					if ( (LA127_0==38) ) {
						alt127=1;
					}
					switch (alt127) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4992:5: (lv_arraySpec_9_0= ruleArraySpec )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4992:5: (lv_arraySpec_9_0= ruleArraySpec )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:4993:6: lv_arraySpec_9_0= ruleArraySpec
							{

													newCompositeNode(grammarAccess.getTypeAccess().getArraySpecArraySpecParserRuleCall_1_3_0());
												
							pushFollow(FOLLOW_ruleArraySpec_in_ruleType14149);
							lv_arraySpec_9_0=ruleArraySpec();
							state._fsp--;


													if (current==null) {
														current = createModelElementForParent(grammarAccess.getTypeRule());
													}
													set(
														current,
														"arraySpec",
														lv_arraySpec_9_0,
														"org.lflang.LF.ArraySpec");
													afterParserOrEnumRuleCall();
												
							}

							}
							break;

					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5012:3: ( (lv_code_10_0= ruleCode ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5012:3: ( (lv_code_10_0= ruleCode ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5013:4: (lv_code_10_0= ruleCode )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5013:4: (lv_code_10_0= ruleCode )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5014:5: lv_code_10_0= ruleCode
					{

										newCompositeNode(grammarAccess.getTypeAccess().getCodeCodeParserRuleCall_2_0());
									
					pushFollow(FOLLOW_ruleCode_in_ruleType14203);
					lv_code_10_0=ruleCode();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getTypeRule());
										}
										set(
											current,
											"code",
											lv_code_10_0,
											"org.lflang.LF.Code");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleType"



	// $ANTLR start "entryRuleArraySpec"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5035:1: entryRuleArraySpec returns [EObject current=null] :iv_ruleArraySpec= ruleArraySpec EOF ;
	public final EObject entryRuleArraySpec() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleArraySpec =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5035:50: (iv_ruleArraySpec= ruleArraySpec EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5036:2: iv_ruleArraySpec= ruleArraySpec EOF
			{
			 newCompositeNode(grammarAccess.getArraySpecRule()); 
			pushFollow(FOLLOW_ruleArraySpec_in_entryRuleArraySpec14240);
			iv_ruleArraySpec=ruleArraySpec();
			state._fsp--;

			 current =iv_ruleArraySpec; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleArraySpec14246); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleArraySpec"



	// $ANTLR start "ruleArraySpec"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5042:1: ruleArraySpec returns [EObject current=null] : (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) ) ;
	public final EObject ruleArraySpec() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token lv_ofVariableLength_1_0=null;
		Token lv_length_2_0=null;
		Token otherlv_3=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5048:2: ( (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5049:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5049:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5050:3: otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) )
			{
			otherlv_0=(Token)match(input,38,FOLLOW_38_in_ruleArraySpec14275); 

						newLeafNode(otherlv_0, grammarAccess.getArraySpecAccess().getLeftSquareBracketKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5054:3: ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) )
			int alt129=2;
			int LA129_0 = input.LA(1);
			if ( (LA129_0==41) ) {
				alt129=1;
			}
			else if ( (LA129_0==RULE_INT) ) {
				alt129=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 129, 0, input);
				throw nvae;
			}

			switch (alt129) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5055:4: ( (lv_ofVariableLength_1_0= ']' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5055:4: ( (lv_ofVariableLength_1_0= ']' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5056:5: (lv_ofVariableLength_1_0= ']' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5056:5: (lv_ofVariableLength_1_0= ']' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5057:6: lv_ofVariableLength_1_0= ']'
					{
					lv_ofVariableLength_1_0=(Token)match(input,41,FOLLOW_41_in_ruleArraySpec14303); 

											newLeafNode(lv_ofVariableLength_1_0, grammarAccess.getArraySpecAccess().getOfVariableLengthRightSquareBracketKeyword_1_0_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getArraySpecRule());
											}
											setWithLastConsumed(current, "ofVariableLength", lv_ofVariableLength_1_0 != null, "]");
										
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5070:4: ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5070:4: ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5071:5: ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5071:5: ( (lv_length_2_0= RULE_INT ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5072:6: (lv_length_2_0= RULE_INT )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5072:6: (lv_length_2_0= RULE_INT )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5073:7: lv_length_2_0= RULE_INT
					{
					lv_length_2_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleArraySpec14365); 

												newLeafNode(lv_length_2_0, grammarAccess.getArraySpecAccess().getLengthINTTerminalRuleCall_1_1_0_0());
											

												if (current==null) {
													current = createModelElement(grammarAccess.getArraySpecRule());
												}
												setWithLastConsumed(
													current,
													"length",
													lv_length_2_0,
													"org.lflang.LF.INT");
											
					}

					}

					otherlv_3=(Token)match(input,41,FOLLOW_41_in_ruleArraySpec14402); 

										newLeafNode(otherlv_3, grammarAccess.getArraySpecAccess().getRightSquareBracketKeyword_1_1_1());
									
					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleArraySpec"



	// $ANTLR start "entryRuleWidthSpec"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5099:1: entryRuleWidthSpec returns [EObject current=null] :iv_ruleWidthSpec= ruleWidthSpec EOF ;
	public final EObject entryRuleWidthSpec() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleWidthSpec =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5099:50: (iv_ruleWidthSpec= ruleWidthSpec EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5100:2: iv_ruleWidthSpec= ruleWidthSpec EOF
			{
			 newCompositeNode(grammarAccess.getWidthSpecRule()); 
			pushFollow(FOLLOW_ruleWidthSpec_in_entryRuleWidthSpec14439);
			iv_ruleWidthSpec=ruleWidthSpec();
			state._fsp--;

			 current =iv_ruleWidthSpec; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleWidthSpec14445); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleWidthSpec"



	// $ANTLR start "ruleWidthSpec"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5106:1: ruleWidthSpec returns [EObject current=null] : (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) ) ;
	public final EObject ruleWidthSpec() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token lv_ofVariableLength_1_0=null;
		Token otherlv_3=null;
		Token otherlv_5=null;
		EObject lv_terms_2_0 =null;
		EObject lv_terms_4_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5112:2: ( (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5113:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5113:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5114:3: otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) )
			{
			otherlv_0=(Token)match(input,38,FOLLOW_38_in_ruleWidthSpec14474); 

						newLeafNode(otherlv_0, grammarAccess.getWidthSpecAccess().getLeftSquareBracketKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5118:3: ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) )
			int alt131=2;
			int LA131_0 = input.LA(1);
			if ( (LA131_0==41) ) {
				alt131=1;
			}
			else if ( ((LA131_0 >= RULE_ID && LA131_0 <= RULE_INT)||LA131_0==81||LA131_0==83) ) {
				alt131=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 131, 0, input);
				throw nvae;
			}

			switch (alt131) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5119:4: ( (lv_ofVariableLength_1_0= ']' ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5119:4: ( (lv_ofVariableLength_1_0= ']' ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5120:5: (lv_ofVariableLength_1_0= ']' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5120:5: (lv_ofVariableLength_1_0= ']' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5121:6: lv_ofVariableLength_1_0= ']'
					{
					lv_ofVariableLength_1_0=(Token)match(input,41,FOLLOW_41_in_ruleWidthSpec14502); 

											newLeafNode(lv_ofVariableLength_1_0, grammarAccess.getWidthSpecAccess().getOfVariableLengthRightSquareBracketKeyword_1_0_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getWidthSpecRule());
											}
											setWithLastConsumed(current, "ofVariableLength", lv_ofVariableLength_1_0 != null, "]");
										
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5134:4: ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5134:4: ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5135:5: ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5135:5: ( (lv_terms_2_0= ruleWidthTerm ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5136:6: (lv_terms_2_0= ruleWidthTerm )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5136:6: (lv_terms_2_0= ruleWidthTerm )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5137:7: lv_terms_2_0= ruleWidthTerm
					{

												newCompositeNode(grammarAccess.getWidthSpecAccess().getTermsWidthTermParserRuleCall_1_1_0_0());
											
					pushFollow(FOLLOW_ruleWidthTerm_in_ruleWidthSpec14572);
					lv_terms_2_0=ruleWidthTerm();
					state._fsp--;


												if (current==null) {
													current = createModelElementForParent(grammarAccess.getWidthSpecRule());
												}
												add(
													current,
													"terms",
													lv_terms_2_0,
													"org.lflang.LF.WidthTerm");
												afterParserOrEnumRuleCall();
											
					}

					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5154:5: (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )*
					loop130:
					while (true) {
						int alt130=2;
						int LA130_0 = input.LA(1);
						if ( (LA130_0==21) ) {
							alt130=1;
						}

						switch (alt130) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5155:6: otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) )
							{
							otherlv_3=(Token)match(input,21,FOLLOW_21_in_ruleWidthSpec14608); 

													newLeafNode(otherlv_3, grammarAccess.getWidthSpecAccess().getPlusSignKeyword_1_1_1_0());
												
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5159:6: ( (lv_terms_4_0= ruleWidthTerm ) )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5160:7: (lv_terms_4_0= ruleWidthTerm )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5160:7: (lv_terms_4_0= ruleWidthTerm )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5161:8: lv_terms_4_0= ruleWidthTerm
							{

															newCompositeNode(grammarAccess.getWidthSpecAccess().getTermsWidthTermParserRuleCall_1_1_1_1_0());
														
							pushFollow(FOLLOW_ruleWidthTerm_in_ruleWidthSpec14650);
							lv_terms_4_0=ruleWidthTerm();
							state._fsp--;


															if (current==null) {
																current = createModelElementForParent(grammarAccess.getWidthSpecRule());
															}
															add(
																current,
																"terms",
																lv_terms_4_0,
																"org.lflang.LF.WidthTerm");
															afterParserOrEnumRuleCall();
														
							}

							}

							}
							break;

						default :
							break loop130;
						}
					}

					otherlv_5=(Token)match(input,41,FOLLOW_41_in_ruleWidthSpec14689); 

										newLeafNode(otherlv_5, grammarAccess.getWidthSpecAccess().getRightSquareBracketKeyword_1_1_2());
									
					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleWidthSpec"



	// $ANTLR start "entryRuleWidthTerm"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5189:1: entryRuleWidthTerm returns [EObject current=null] :iv_ruleWidthTerm= ruleWidthTerm EOF ;
	public final EObject entryRuleWidthTerm() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleWidthTerm =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5189:50: (iv_ruleWidthTerm= ruleWidthTerm EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5190:2: iv_ruleWidthTerm= ruleWidthTerm EOF
			{
			 newCompositeNode(grammarAccess.getWidthTermRule()); 
			pushFollow(FOLLOW_ruleWidthTerm_in_entryRuleWidthTerm14726);
			iv_ruleWidthTerm=ruleWidthTerm();
			state._fsp--;

			 current =iv_ruleWidthTerm; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleWidthTerm14732); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleWidthTerm"



	// $ANTLR start "ruleWidthTerm"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5196:1: ruleWidthTerm returns [EObject current=null] : ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) ) ;
	public final EObject ruleWidthTerm() throws RecognitionException {
		EObject current = null;


		Token lv_width_0_0=null;
		Token otherlv_1=null;
		Token otherlv_2=null;
		Token otherlv_4=null;
		EObject lv_port_3_0 =null;
		EObject lv_code_5_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5202:2: ( ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5203:2: ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5203:2: ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) )
			int alt132=4;
			switch ( input.LA(1) ) {
			case RULE_INT:
				{
				alt132=1;
				}
				break;
			case RULE_ID:
				{
				alt132=2;
				}
				break;
			case 81:
				{
				alt132=3;
				}
				break;
			case 83:
				{
				alt132=4;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 132, 0, input);
				throw nvae;
			}
			switch (alt132) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5204:3: ( (lv_width_0_0= RULE_INT ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5204:3: ( (lv_width_0_0= RULE_INT ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5205:4: (lv_width_0_0= RULE_INT )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5205:4: (lv_width_0_0= RULE_INT )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5206:5: lv_width_0_0= RULE_INT
					{
					lv_width_0_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleWidthTerm14772); 

										newLeafNode(lv_width_0_0, grammarAccess.getWidthTermAccess().getWidthINTTerminalRuleCall_0_0());
									

										if (current==null) {
											current = createModelElement(grammarAccess.getWidthTermRule());
										}
										setWithLastConsumed(
											current,
											"width",
											lv_width_0_0,
											"org.lflang.LF.INT");
									
					}

					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5223:3: ( (otherlv_1= RULE_ID ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5223:3: ( (otherlv_1= RULE_ID ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5224:4: (otherlv_1= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5224:4: (otherlv_1= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5225:5: otherlv_1= RULE_ID
					{

										if (current==null) {
											current = createModelElement(grammarAccess.getWidthTermRule());
										}
									
					otherlv_1=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleWidthTerm14824); 

										newLeafNode(otherlv_1, grammarAccess.getWidthTermAccess().getParameterParameterCrossReference_1_0());
									
					}

					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5237:3: (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5237:3: (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5238:4: otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')'
					{
					otherlv_2=(Token)match(input,81,FOLLOW_81_in_ruleWidthTerm14858); 

									newLeafNode(otherlv_2, grammarAccess.getWidthTermAccess().getWidthofKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5242:4: ( (lv_port_3_0= ruleVarRef ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5243:5: (lv_port_3_0= ruleVarRef )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5243:5: (lv_port_3_0= ruleVarRef )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5244:6: lv_port_3_0= ruleVarRef
					{

											newCompositeNode(grammarAccess.getWidthTermAccess().getPortVarRefParserRuleCall_2_1_0());
										
					pushFollow(FOLLOW_ruleVarRef_in_ruleWidthTerm14890);
					lv_port_3_0=ruleVarRef();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getWidthTermRule());
											}
											set(
												current,
												"port",
												lv_port_3_0,
												"org.lflang.LF.VarRef");
											afterParserOrEnumRuleCall();
										
					}

					}

					otherlv_4=(Token)match(input,19,FOLLOW_19_in_ruleWidthTerm14915); 

									newLeafNode(otherlv_4, grammarAccess.getWidthTermAccess().getRightParenthesisKeyword_2_2());
								
					}

					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5267:3: ( (lv_code_5_0= ruleCode ) )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5267:3: ( (lv_code_5_0= ruleCode ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5268:4: (lv_code_5_0= ruleCode )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5268:4: (lv_code_5_0= ruleCode )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5269:5: lv_code_5_0= ruleCode
					{

										newCompositeNode(grammarAccess.getWidthTermAccess().getCodeCodeParserRuleCall_3_0());
									
					pushFollow(FOLLOW_ruleCode_in_ruleWidthTerm14955);
					lv_code_5_0=ruleCode();
					state._fsp--;


										if (current==null) {
											current = createModelElementForParent(grammarAccess.getWidthTermRule());
										}
										set(
											current,
											"code",
											lv_code_5_0,
											"org.lflang.LF.Code");
										afterParserOrEnumRuleCall();
									
					}

					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleWidthTerm"



	// $ANTLR start "entryRuleIPV4Host"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5290:1: entryRuleIPV4Host returns [EObject current=null] :iv_ruleIPV4Host= ruleIPV4Host EOF ;
	public final EObject entryRuleIPV4Host() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleIPV4Host =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5290:49: (iv_ruleIPV4Host= ruleIPV4Host EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5291:2: iv_ruleIPV4Host= ruleIPV4Host EOF
			{
			 newCompositeNode(grammarAccess.getIPV4HostRule()); 
			pushFollow(FOLLOW_ruleIPV4Host_in_entryRuleIPV4Host14992);
			iv_ruleIPV4Host=ruleIPV4Host();
			state._fsp--;

			 current =iv_ruleIPV4Host; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleIPV4Host14998); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleIPV4Host"



	// $ANTLR start "ruleIPV4Host"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5297:1: ruleIPV4Host returns [EObject current=null] : ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) ;
	public final EObject ruleIPV4Host() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token otherlv_3=null;
		Token lv_port_4_0=null;
		AntlrDatatypeRuleToken lv_user_0_0 =null;
		AntlrDatatypeRuleToken lv_addr_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5303:2: ( ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5304:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5304:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5305:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5305:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )?
			int alt133=2;
			int LA133_0 = input.LA(1);
			if ( (LA133_0==RULE_ID||LA133_0==65) ) {
				alt133=1;
			}
			switch (alt133) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5306:4: ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5306:4: ( (lv_user_0_0= ruleKebab ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5307:5: (lv_user_0_0= ruleKebab )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5307:5: (lv_user_0_0= ruleKebab )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5308:6: lv_user_0_0= ruleKebab
					{

											newCompositeNode(grammarAccess.getIPV4HostAccess().getUserKebabParserRuleCall_0_0_0());
										
					pushFollow(FOLLOW_ruleKebab_in_ruleIPV4Host15052);
					lv_user_0_0=ruleKebab();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getIPV4HostRule());
											}
											set(
												current,
												"user",
												lv_user_0_0,
												"org.lflang.LF.Kebab");
											afterParserOrEnumRuleCall();
										
					}

					}

					otherlv_1=(Token)match(input,35,FOLLOW_35_in_ruleIPV4Host15077); 

									newLeafNode(otherlv_1, grammarAccess.getIPV4HostAccess().getCommercialAtKeyword_0_1());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5330:3: ( (lv_addr_2_0= ruleIPV4Addr ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5331:4: (lv_addr_2_0= ruleIPV4Addr )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5331:4: (lv_addr_2_0= ruleIPV4Addr )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5332:5: lv_addr_2_0= ruleIPV4Addr
			{

								newCompositeNode(grammarAccess.getIPV4HostAccess().getAddrIPV4AddrParserRuleCall_1_0());
							
			pushFollow(FOLLOW_ruleIPV4Addr_in_ruleIPV4Host15110);
			lv_addr_2_0=ruleIPV4Addr();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getIPV4HostRule());
								}
								set(
									current,
									"addr",
									lv_addr_2_0,
									"org.lflang.LF.IPV4Addr");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5349:3: (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
			int alt134=2;
			int LA134_0 = input.LA(1);
			if ( (LA134_0==27) ) {
				alt134=1;
			}
			switch (alt134) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5350:4: otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) )
					{
					otherlv_3=(Token)match(input,27,FOLLOW_27_in_ruleIPV4Host15136); 

									newLeafNode(otherlv_3, grammarAccess.getIPV4HostAccess().getColonKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5354:4: ( (lv_port_4_0= RULE_INT ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5355:5: (lv_port_4_0= RULE_INT )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5355:5: (lv_port_4_0= RULE_INT )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5356:6: lv_port_4_0= RULE_INT
					{
					lv_port_4_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV4Host15161); 

											newLeafNode(lv_port_4_0, grammarAccess.getIPV4HostAccess().getPortINTTerminalRuleCall_2_1_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getIPV4HostRule());
											}
											setWithLastConsumed(
												current,
												"port",
												lv_port_4_0,
												"org.lflang.LF.INT");
										
					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleIPV4Host"



	// $ANTLR start "entryRuleIPV6Host"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5377:1: entryRuleIPV6Host returns [EObject current=null] :iv_ruleIPV6Host= ruleIPV6Host EOF ;
	public final EObject entryRuleIPV6Host() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleIPV6Host =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5377:49: (iv_ruleIPV6Host= ruleIPV6Host EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5378:2: iv_ruleIPV6Host= ruleIPV6Host EOF
			{
			 newCompositeNode(grammarAccess.getIPV6HostRule()); 
			pushFollow(FOLLOW_ruleIPV6Host_in_entryRuleIPV6Host15213);
			iv_ruleIPV6Host=ruleIPV6Host();
			state._fsp--;

			 current =iv_ruleIPV6Host; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleIPV6Host15219); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleIPV6Host"



	// $ANTLR start "ruleIPV6Host"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5384:1: ruleIPV6Host returns [EObject current=null] : (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? ) ;
	public final EObject ruleIPV6Host() throws RecognitionException {
		EObject current = null;


		Token otherlv_0=null;
		Token otherlv_2=null;
		Token otherlv_4=null;
		Token otherlv_5=null;
		Token lv_port_6_0=null;
		AntlrDatatypeRuleToken lv_user_1_0 =null;
		AntlrDatatypeRuleToken lv_addr_3_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5390:2: ( (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5391:2: (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5391:2: (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5392:3: otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )?
			{
			otherlv_0=(Token)match(input,38,FOLLOW_38_in_ruleIPV6Host15248); 

						newLeafNode(otherlv_0, grammarAccess.getIPV6HostAccess().getLeftSquareBracketKeyword_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5396:3: ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )?
			int alt135=2;
			int LA135_0 = input.LA(1);
			if ( (LA135_0==RULE_ID) ) {
				int LA135_1 = input.LA(2);
				if ( (LA135_1==23||LA135_1==35) ) {
					alt135=1;
				}
			}
			else if ( (LA135_0==65) ) {
				alt135=1;
			}
			switch (alt135) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5397:4: ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5397:4: ( (lv_user_1_0= ruleKebab ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5398:5: (lv_user_1_0= ruleKebab )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5398:5: (lv_user_1_0= ruleKebab )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5399:6: lv_user_1_0= ruleKebab
					{

											newCompositeNode(grammarAccess.getIPV6HostAccess().getUserKebabParserRuleCall_1_0_0());
										
					pushFollow(FOLLOW_ruleKebab_in_ruleIPV6Host15283);
					lv_user_1_0=ruleKebab();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getIPV6HostRule());
											}
											set(
												current,
												"user",
												lv_user_1_0,
												"org.lflang.LF.Kebab");
											afterParserOrEnumRuleCall();
										
					}

					}

					otherlv_2=(Token)match(input,35,FOLLOW_35_in_ruleIPV6Host15308); 

									newLeafNode(otherlv_2, grammarAccess.getIPV6HostAccess().getCommercialAtKeyword_1_1());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5421:3: ( (lv_addr_3_0= ruleIPV6Addr ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5422:4: (lv_addr_3_0= ruleIPV6Addr )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5422:4: (lv_addr_3_0= ruleIPV6Addr )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5423:5: lv_addr_3_0= ruleIPV6Addr
			{

								newCompositeNode(grammarAccess.getIPV6HostAccess().getAddrIPV6AddrParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleIPV6Addr_in_ruleIPV6Host15341);
			lv_addr_3_0=ruleIPV6Addr();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getIPV6HostRule());
								}
								set(
									current,
									"addr",
									lv_addr_3_0,
									"org.lflang.LF.IPV6Addr");
								afterParserOrEnumRuleCall();
							
			}

			}

			otherlv_4=(Token)match(input,41,FOLLOW_41_in_ruleIPV6Host15362); 

						newLeafNode(otherlv_4, grammarAccess.getIPV6HostAccess().getRightSquareBracketKeyword_3());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5444:3: (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )?
			int alt136=2;
			int LA136_0 = input.LA(1);
			if ( (LA136_0==27) ) {
				alt136=1;
			}
			switch (alt136) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5445:4: otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) )
					{
					otherlv_5=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Host15377); 

									newLeafNode(otherlv_5, grammarAccess.getIPV6HostAccess().getColonKeyword_4_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5449:4: ( (lv_port_6_0= RULE_INT ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5450:5: (lv_port_6_0= RULE_INT )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5450:5: (lv_port_6_0= RULE_INT )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5451:6: lv_port_6_0= RULE_INT
					{
					lv_port_6_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV6Host15402); 

											newLeafNode(lv_port_6_0, grammarAccess.getIPV6HostAccess().getPortINTTerminalRuleCall_4_1_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getIPV6HostRule());
											}
											setWithLastConsumed(
												current,
												"port",
												lv_port_6_0,
												"org.lflang.LF.INT");
										
					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleIPV6Host"



	// $ANTLR start "entryRuleNamedHost"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5472:1: entryRuleNamedHost returns [EObject current=null] :iv_ruleNamedHost= ruleNamedHost EOF ;
	public final EObject entryRuleNamedHost() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleNamedHost =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5472:50: (iv_ruleNamedHost= ruleNamedHost EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5473:2: iv_ruleNamedHost= ruleNamedHost EOF
			{
			 newCompositeNode(grammarAccess.getNamedHostRule()); 
			pushFollow(FOLLOW_ruleNamedHost_in_entryRuleNamedHost15454);
			iv_ruleNamedHost=ruleNamedHost();
			state._fsp--;

			 current =iv_ruleNamedHost; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleNamedHost15460); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleNamedHost"



	// $ANTLR start "ruleNamedHost"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5479:1: ruleNamedHost returns [EObject current=null] : ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) ;
	public final EObject ruleNamedHost() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token otherlv_3=null;
		Token lv_port_4_0=null;
		AntlrDatatypeRuleToken lv_user_0_0 =null;
		AntlrDatatypeRuleToken lv_addr_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5485:2: ( ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5486:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5486:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5487:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5487:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )?
			int alt137=2;
			alt137 = dfa137.predict(input);
			switch (alt137) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5488:4: ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@'
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5488:4: ( (lv_user_0_0= ruleKebab ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5489:5: (lv_user_0_0= ruleKebab )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5489:5: (lv_user_0_0= ruleKebab )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5490:6: lv_user_0_0= ruleKebab
					{

											newCompositeNode(grammarAccess.getNamedHostAccess().getUserKebabParserRuleCall_0_0_0());
										
					pushFollow(FOLLOW_ruleKebab_in_ruleNamedHost15514);
					lv_user_0_0=ruleKebab();
					state._fsp--;


											if (current==null) {
												current = createModelElementForParent(grammarAccess.getNamedHostRule());
											}
											set(
												current,
												"user",
												lv_user_0_0,
												"org.lflang.LF.Kebab");
											afterParserOrEnumRuleCall();
										
					}

					}

					otherlv_1=(Token)match(input,35,FOLLOW_35_in_ruleNamedHost15539); 

									newLeafNode(otherlv_1, grammarAccess.getNamedHostAccess().getCommercialAtKeyword_0_1());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5512:3: ( (lv_addr_2_0= ruleHostName ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5513:4: (lv_addr_2_0= ruleHostName )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5513:4: (lv_addr_2_0= ruleHostName )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5514:5: lv_addr_2_0= ruleHostName
			{

								newCompositeNode(grammarAccess.getNamedHostAccess().getAddrHostNameParserRuleCall_1_0());
							
			pushFollow(FOLLOW_ruleHostName_in_ruleNamedHost15572);
			lv_addr_2_0=ruleHostName();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getNamedHostRule());
								}
								set(
									current,
									"addr",
									lv_addr_2_0,
									"org.lflang.LF.HostName");
								afterParserOrEnumRuleCall();
							
			}

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5531:3: (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
			int alt138=2;
			int LA138_0 = input.LA(1);
			if ( (LA138_0==27) ) {
				alt138=1;
			}
			switch (alt138) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5532:4: otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) )
					{
					otherlv_3=(Token)match(input,27,FOLLOW_27_in_ruleNamedHost15598); 

									newLeafNode(otherlv_3, grammarAccess.getNamedHostAccess().getColonKeyword_2_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5536:4: ( (lv_port_4_0= RULE_INT ) )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5537:5: (lv_port_4_0= RULE_INT )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5537:5: (lv_port_4_0= RULE_INT )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5538:6: lv_port_4_0= RULE_INT
					{
					lv_port_4_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleNamedHost15623); 

											newLeafNode(lv_port_4_0, grammarAccess.getNamedHostAccess().getPortINTTerminalRuleCall_2_1_0());
										

											if (current==null) {
												current = createModelElement(grammarAccess.getNamedHostRule());
											}
											setWithLastConsumed(
												current,
												"port",
												lv_port_4_0,
												"org.lflang.LF.INT");
										
					}

					}

					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleNamedHost"



	// $ANTLR start "entryRuleHost"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5559:1: entryRuleHost returns [EObject current=null] :iv_ruleHost= ruleHost EOF ;
	public final EObject entryRuleHost() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleHost =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5559:45: (iv_ruleHost= ruleHost EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5560:2: iv_ruleHost= ruleHost EOF
			{
			 newCompositeNode(grammarAccess.getHostRule()); 
			pushFollow(FOLLOW_ruleHost_in_entryRuleHost15675);
			iv_ruleHost=ruleHost();
			state._fsp--;

			 current =iv_ruleHost; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleHost15681); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleHost"



	// $ANTLR start "ruleHost"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5566:1: ruleHost returns [EObject current=null] : (this_IPV4Host_0= ruleIPV4Host |this_IPV6Host_1= ruleIPV6Host |this_NamedHost_2= ruleNamedHost ) ;
	public final EObject ruleHost() throws RecognitionException {
		EObject current = null;


		EObject this_IPV4Host_0 =null;
		EObject this_IPV6Host_1 =null;
		EObject this_NamedHost_2 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5572:2: ( (this_IPV4Host_0= ruleIPV4Host |this_IPV6Host_1= ruleIPV6Host |this_NamedHost_2= ruleNamedHost ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5573:2: (this_IPV4Host_0= ruleIPV4Host |this_IPV6Host_1= ruleIPV6Host |this_NamedHost_2= ruleNamedHost )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5573:2: (this_IPV4Host_0= ruleIPV4Host |this_IPV6Host_1= ruleIPV6Host |this_NamedHost_2= ruleNamedHost )
			int alt139=3;
			alt139 = dfa139.predict(input);
			switch (alt139) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5574:3: this_IPV4Host_0= ruleIPV4Host
					{

								newCompositeNode(grammarAccess.getHostAccess().getIPV4HostParserRuleCall_0());
							
					pushFollow(FOLLOW_ruleIPV4Host_in_ruleHost15714);
					this_IPV4Host_0=ruleIPV4Host();
					state._fsp--;


								current = this_IPV4Host_0;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5583:3: this_IPV6Host_1= ruleIPV6Host
					{

								newCompositeNode(grammarAccess.getHostAccess().getIPV6HostParserRuleCall_1());
							
					pushFollow(FOLLOW_ruleIPV6Host_in_ruleHost15736);
					this_IPV6Host_1=ruleIPV6Host();
					state._fsp--;


								current = this_IPV6Host_1;
								afterParserOrEnumRuleCall();
							
					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5592:3: this_NamedHost_2= ruleNamedHost
					{

								newCompositeNode(grammarAccess.getHostAccess().getNamedHostParserRuleCall_2());
							
					pushFollow(FOLLOW_ruleNamedHost_in_ruleHost15758);
					this_NamedHost_2=ruleNamedHost();
					state._fsp--;


								current = this_NamedHost_2;
								afterParserOrEnumRuleCall();
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleHost"



	// $ANTLR start "entryRuleHostName"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5604:1: entryRuleHostName returns [String current=null] :iv_ruleHostName= ruleHostName EOF ;
	public final String entryRuleHostName() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleHostName =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5604:48: (iv_ruleHostName= ruleHostName EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5605:2: iv_ruleHostName= ruleHostName EOF
			{
			 newCompositeNode(grammarAccess.getHostNameRule()); 
			pushFollow(FOLLOW_ruleHostName_in_entryRuleHostName15784);
			iv_ruleHostName=ruleHostName();
			state._fsp--;

			 current =iv_ruleHostName.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleHostName15790); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleHostName"



	// $ANTLR start "ruleHostName"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5611:1: ruleHostName returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* ) ;
	public final AntlrDatatypeRuleToken ruleHostName() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token kw=null;
		AntlrDatatypeRuleToken this_Kebab_0 =null;
		AntlrDatatypeRuleToken this_Kebab_2 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5617:2: ( (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5618:2: (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5618:2: (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5619:3: this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )*
			{

						newCompositeNode(grammarAccess.getHostNameAccess().getKebabParserRuleCall_0());
					
			pushFollow(FOLLOW_ruleKebab_in_ruleHostName15823);
			this_Kebab_0=ruleKebab();
			state._fsp--;


						current.merge(this_Kebab_0);
					

						afterParserOrEnumRuleCall();
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5629:3: (kw= '.' this_Kebab_2= ruleKebab )*
			loop140:
			while (true) {
				int alt140=2;
				int LA140_0 = input.LA(1);
				if ( (LA140_0==25) ) {
					alt140=1;
				}

				switch (alt140) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5630:4: kw= '.' this_Kebab_2= ruleKebab
					{
					kw=(Token)match(input,25,FOLLOW_25_in_ruleHostName15842); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getHostNameAccess().getFullStopKeyword_1_0());
								

									newCompositeNode(grammarAccess.getHostNameAccess().getKebabParserRuleCall_1_1());
								
					pushFollow(FOLLOW_ruleKebab_in_ruleHostName15859);
					this_Kebab_2=ruleKebab();
					state._fsp--;


									current.merge(this_Kebab_2);
								

									afterParserOrEnumRuleCall();
								
					}
					break;

				default :
					break loop140;
				}
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleHostName"



	// $ANTLR start "entryRuleDottedName"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5650:1: entryRuleDottedName returns [String current=null] :iv_ruleDottedName= ruleDottedName EOF ;
	public final String entryRuleDottedName() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleDottedName =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5650:50: (iv_ruleDottedName= ruleDottedName EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5651:2: iv_ruleDottedName= ruleDottedName EOF
			{
			 newCompositeNode(grammarAccess.getDottedNameRule()); 
			pushFollow(FOLLOW_ruleDottedName_in_entryRuleDottedName15896);
			iv_ruleDottedName=ruleDottedName();
			state._fsp--;

			 current =iv_ruleDottedName.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleDottedName15902); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleDottedName"



	// $ANTLR start "ruleDottedName"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5657:1: ruleDottedName returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID ( (kw= '.' |kw= '::' ) this_ID_3= RULE_ID )* ) ;
	public final AntlrDatatypeRuleToken ruleDottedName() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_ID_0=null;
		Token kw=null;
		Token this_ID_3=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5663:2: ( (this_ID_0= RULE_ID ( (kw= '.' |kw= '::' ) this_ID_3= RULE_ID )* ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5664:2: (this_ID_0= RULE_ID ( (kw= '.' |kw= '::' ) this_ID_3= RULE_ID )* )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5664:2: (this_ID_0= RULE_ID ( (kw= '.' |kw= '::' ) this_ID_3= RULE_ID )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5665:3: this_ID_0= RULE_ID ( (kw= '.' |kw= '::' ) this_ID_3= RULE_ID )*
			{
			this_ID_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleDottedName15931); 

						current.merge(this_ID_0);
					

						newLeafNode(this_ID_0, grammarAccess.getDottedNameAccess().getIDTerminalRuleCall_0());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5672:3: ( (kw= '.' |kw= '::' ) this_ID_3= RULE_ID )*
			loop142:
			while (true) {
				int alt142=2;
				int LA142_0 = input.LA(1);
				if ( (LA142_0==25||LA142_0==28) ) {
					alt142=1;
				}

				switch (alt142) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5673:4: (kw= '.' |kw= '::' ) this_ID_3= RULE_ID
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5673:4: (kw= '.' |kw= '::' )
					int alt141=2;
					int LA141_0 = input.LA(1);
					if ( (LA141_0==25) ) {
						alt141=1;
					}
					else if ( (LA141_0==28) ) {
						alt141=2;
					}

					else {
						NoViableAltException nvae =
							new NoViableAltException("", 141, 0, input);
						throw nvae;
					}

					switch (alt141) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5674:5: kw= '.'
							{
							kw=(Token)match(input,25,FOLLOW_25_in_ruleDottedName15956); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getDottedNameAccess().getFullStopKeyword_1_0_0());
											
							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5680:5: kw= '::'
							{
							kw=(Token)match(input,28,FOLLOW_28_in_ruleDottedName15980); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getDottedNameAccess().getColonColonKeyword_1_0_1());
											
							}
							break;

					}

					this_ID_3=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleDottedName15998); 

									current.merge(this_ID_3);
								

									newLeafNode(this_ID_3, grammarAccess.getDottedNameAccess().getIDTerminalRuleCall_1_1());
								
					}
					break;

				default :
					break loop142;
				}
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleDottedName"



	// $ANTLR start "entryRuleSignedInt"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5698:1: entryRuleSignedInt returns [String current=null] :iv_ruleSignedInt= ruleSignedInt EOF ;
	public final String entryRuleSignedInt() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleSignedInt =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5698:49: (iv_ruleSignedInt= ruleSignedInt EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5699:2: iv_ruleSignedInt= ruleSignedInt EOF
			{
			 newCompositeNode(grammarAccess.getSignedIntRule()); 
			pushFollow(FOLLOW_ruleSignedInt_in_entryRuleSignedInt16035);
			iv_ruleSignedInt=ruleSignedInt();
			state._fsp--;

			 current =iv_ruleSignedInt.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleSignedInt16041); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleSignedInt"



	// $ANTLR start "ruleSignedInt"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5705:1: ruleSignedInt returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_INT_0= RULE_INT |this_NEGINT_1= RULE_NEGINT ) ;
	public final AntlrDatatypeRuleToken ruleSignedInt() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_INT_0=null;
		Token this_NEGINT_1=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5711:2: ( (this_INT_0= RULE_INT |this_NEGINT_1= RULE_NEGINT ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5712:2: (this_INT_0= RULE_INT |this_NEGINT_1= RULE_NEGINT )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5712:2: (this_INT_0= RULE_INT |this_NEGINT_1= RULE_NEGINT )
			int alt143=2;
			int LA143_0 = input.LA(1);
			if ( (LA143_0==RULE_INT) ) {
				alt143=1;
			}
			else if ( (LA143_0==RULE_NEGINT) ) {
				alt143=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 143, 0, input);
				throw nvae;
			}

			switch (alt143) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5713:3: this_INT_0= RULE_INT
					{
					this_INT_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleSignedInt16070); 

								current.merge(this_INT_0);
							

								newLeafNode(this_INT_0, grammarAccess.getSignedIntAccess().getINTTerminalRuleCall_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5721:3: this_NEGINT_1= RULE_NEGINT
					{
					this_NEGINT_1=(Token)match(input,RULE_NEGINT,FOLLOW_RULE_NEGINT_in_ruleSignedInt16092); 

								current.merge(this_NEGINT_1);
							

								newLeafNode(this_NEGINT_1, grammarAccess.getSignedIntAccess().getNEGINTTerminalRuleCall_1());
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleSignedInt"



	// $ANTLR start "entryRuleLiteral"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5732:1: entryRuleLiteral returns [String current=null] :iv_ruleLiteral= ruleLiteral EOF ;
	public final String entryRuleLiteral() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleLiteral =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5732:47: (iv_ruleLiteral= ruleLiteral EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5733:2: iv_ruleLiteral= ruleLiteral EOF
			{
			 newCompositeNode(grammarAccess.getLiteralRule()); 
			pushFollow(FOLLOW_ruleLiteral_in_entryRuleLiteral16122);
			iv_ruleLiteral=ruleLiteral();
			state._fsp--;

			 current =iv_ruleLiteral.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleLiteral16128); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleLiteral"



	// $ANTLR start "ruleLiteral"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5739:1: ruleLiteral returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_STRING_0= RULE_STRING |this_CHAR_LIT_1= RULE_CHAR_LIT |this_SignedFloat_2= ruleSignedFloat |this_SignedInt_3= ruleSignedInt |this_Boolean_4= ruleBoolean ) ;
	public final AntlrDatatypeRuleToken ruleLiteral() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_STRING_0=null;
		Token this_CHAR_LIT_1=null;
		AntlrDatatypeRuleToken this_SignedFloat_2 =null;
		AntlrDatatypeRuleToken this_SignedInt_3 =null;
		AntlrDatatypeRuleToken this_Boolean_4 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5745:2: ( (this_STRING_0= RULE_STRING |this_CHAR_LIT_1= RULE_CHAR_LIT |this_SignedFloat_2= ruleSignedFloat |this_SignedInt_3= ruleSignedInt |this_Boolean_4= ruleBoolean ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5746:2: (this_STRING_0= RULE_STRING |this_CHAR_LIT_1= RULE_CHAR_LIT |this_SignedFloat_2= ruleSignedFloat |this_SignedInt_3= ruleSignedInt |this_Boolean_4= ruleBoolean )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5746:2: (this_STRING_0= RULE_STRING |this_CHAR_LIT_1= RULE_CHAR_LIT |this_SignedFloat_2= ruleSignedFloat |this_SignedInt_3= ruleSignedInt |this_Boolean_4= ruleBoolean )
			int alt144=5;
			switch ( input.LA(1) ) {
			case RULE_STRING:
				{
				alt144=1;
				}
				break;
			case RULE_CHAR_LIT:
				{
				alt144=2;
				}
				break;
			case RULE_INT:
				{
				int LA144_3 = input.LA(2);
				if ( (LA144_3==25) ) {
					alt144=3;
				}
				else if ( (LA144_3==EOF||LA144_3==RULE_ID||(LA144_3 >= 18 && LA144_3 <= 19)||LA144_3==22||LA144_3==30||(LA144_3 >= 35 && LA144_3 <= 36)||LA144_3==41||LA144_3==43||LA144_3==47||(LA144_3 >= 54 && LA144_3 <= 57)||(LA144_3 >= 59 && LA144_3 <= 62)||(LA144_3 >= 64 && LA144_3 <= 69)||(LA144_3 >= 72 && LA144_3 <= 73)||LA144_3==76||LA144_3==79||LA144_3==84) ) {
					alt144=4;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 144, 3, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

				}
				break;
			case RULE_NEGINT:
				{
				int LA144_4 = input.LA(2);
				if ( (LA144_4==25) ) {
					alt144=3;
				}
				else if ( (LA144_4==EOF||LA144_4==RULE_ID||(LA144_4 >= 18 && LA144_4 <= 19)||LA144_4==22||LA144_4==30||(LA144_4 >= 35 && LA144_4 <= 36)||LA144_4==41||LA144_4==43||LA144_4==47||(LA144_4 >= 54 && LA144_4 <= 57)||(LA144_4 >= 59 && LA144_4 <= 62)||(LA144_4 >= 64 && LA144_4 <= 69)||(LA144_4 >= 72 && LA144_4 <= 73)||LA144_4==76||LA144_4==79||LA144_4==84) ) {
					alt144=4;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 144, 4, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

				}
				break;
			case 23:
			case 25:
				{
				alt144=3;
				}
				break;
			case RULE_FALSE:
			case RULE_TRUE:
				{
				alt144=5;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 144, 0, input);
				throw nvae;
			}
			switch (alt144) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5747:3: this_STRING_0= RULE_STRING
					{
					this_STRING_0=(Token)match(input,RULE_STRING,FOLLOW_RULE_STRING_in_ruleLiteral16157); 

								current.merge(this_STRING_0);
							

								newLeafNode(this_STRING_0, grammarAccess.getLiteralAccess().getSTRINGTerminalRuleCall_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5755:3: this_CHAR_LIT_1= RULE_CHAR_LIT
					{
					this_CHAR_LIT_1=(Token)match(input,RULE_CHAR_LIT,FOLLOW_RULE_CHAR_LIT_in_ruleLiteral16179); 

								current.merge(this_CHAR_LIT_1);
							

								newLeafNode(this_CHAR_LIT_1, grammarAccess.getLiteralAccess().getCHAR_LITTerminalRuleCall_1());
							
					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5763:3: this_SignedFloat_2= ruleSignedFloat
					{

								newCompositeNode(grammarAccess.getLiteralAccess().getSignedFloatParserRuleCall_2());
							
					pushFollow(FOLLOW_ruleSignedFloat_in_ruleLiteral16205);
					this_SignedFloat_2=ruleSignedFloat();
					state._fsp--;


								current.merge(this_SignedFloat_2);
							

								afterParserOrEnumRuleCall();
							
					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5774:3: this_SignedInt_3= ruleSignedInt
					{

								newCompositeNode(grammarAccess.getLiteralAccess().getSignedIntParserRuleCall_3());
							
					pushFollow(FOLLOW_ruleSignedInt_in_ruleLiteral16231);
					this_SignedInt_3=ruleSignedInt();
					state._fsp--;


								current.merge(this_SignedInt_3);
							

								afterParserOrEnumRuleCall();
							
					}
					break;
				case 5 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5785:3: this_Boolean_4= ruleBoolean
					{

								newCompositeNode(grammarAccess.getLiteralAccess().getBooleanParserRuleCall_4());
							
					pushFollow(FOLLOW_ruleBoolean_in_ruleLiteral16257);
					this_Boolean_4=ruleBoolean();
					state._fsp--;


								current.merge(this_Boolean_4);
							

								afterParserOrEnumRuleCall();
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleLiteral"



	// $ANTLR start "entryRuleKebab"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5799:1: entryRuleKebab returns [String current=null] :iv_ruleKebab= ruleKebab EOF ;
	public final String entryRuleKebab() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleKebab =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5799:45: (iv_ruleKebab= ruleKebab EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5800:2: iv_ruleKebab= ruleKebab EOF
			{
			 newCompositeNode(grammarAccess.getKebabRule()); 
			pushFollow(FOLLOW_ruleKebab_in_entryRuleKebab16287);
			iv_ruleKebab=ruleKebab();
			state._fsp--;

			 current =iv_ruleKebab.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleKebab16293); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleKebab"



	// $ANTLR start "ruleKebab"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5806:1: ruleKebab returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : ( (this_ID_0= RULE_ID |kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* ) ;
	public final AntlrDatatypeRuleToken ruleKebab() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_ID_0=null;
		Token kw=null;
		Token this_ID_3=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5812:2: ( ( (this_ID_0= RULE_ID |kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5813:2: ( (this_ID_0= RULE_ID |kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5813:2: ( (this_ID_0= RULE_ID |kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5814:3: (this_ID_0= RULE_ID |kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )*
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5814:3: (this_ID_0= RULE_ID |kw= 'physical' )
			int alt145=2;
			int LA145_0 = input.LA(1);
			if ( (LA145_0==RULE_ID) ) {
				alt145=1;
			}
			else if ( (LA145_0==65) ) {
				alt145=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 145, 0, input);
				throw nvae;
			}

			switch (alt145) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5815:4: this_ID_0= RULE_ID
					{
					this_ID_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleKebab16327); 

									current.merge(this_ID_0);
								

									newLeafNode(this_ID_0, grammarAccess.getKebabAccess().getIDTerminalRuleCall_0_0());
								
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5823:4: kw= 'physical'
					{
					kw=(Token)match(input,65,FOLLOW_65_in_ruleKebab16353); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getKebabAccess().getPhysicalKeyword_0_1());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5829:3: (kw= '-' this_ID_3= RULE_ID )*
			loop146:
			while (true) {
				int alt146=2;
				int LA146_0 = input.LA(1);
				if ( (LA146_0==23) ) {
					alt146=1;
				}

				switch (alt146) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5830:4: kw= '-' this_ID_3= RULE_ID
					{
					kw=(Token)match(input,23,FOLLOW_23_in_ruleKebab16373); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getKebabAccess().getHyphenMinusKeyword_1_0());
								
					this_ID_3=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleKebab16385); 

									current.merge(this_ID_3);
								

									newLeafNode(this_ID_3, grammarAccess.getKebabAccess().getIDTerminalRuleCall_1_1());
								
					}
					break;

				default :
					break loop146;
				}
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleKebab"



	// $ANTLR start "entryRuleIPV4Addr"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5847:1: entryRuleIPV4Addr returns [String current=null] :iv_ruleIPV4Addr= ruleIPV4Addr EOF ;
	public final String entryRuleIPV4Addr() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleIPV4Addr =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5847:48: (iv_ruleIPV4Addr= ruleIPV4Addr EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5848:2: iv_ruleIPV4Addr= ruleIPV4Addr EOF
			{
			 newCompositeNode(grammarAccess.getIPV4AddrRule()); 
			pushFollow(FOLLOW_ruleIPV4Addr_in_entryRuleIPV4Addr16422);
			iv_ruleIPV4Addr=ruleIPV4Addr();
			state._fsp--;

			 current =iv_ruleIPV4Addr.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleIPV4Addr16428); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleIPV4Addr"



	// $ANTLR start "ruleIPV4Addr"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5854:1: ruleIPV4Addr returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT ) ;
	public final AntlrDatatypeRuleToken ruleIPV4Addr() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_INT_0=null;
		Token kw=null;
		Token this_INT_2=null;
		Token this_INT_4=null;
		Token this_INT_6=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5860:2: ( (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5861:2: (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5861:2: (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5862:3: this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT
			{
			this_INT_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV4Addr16457); 

						current.merge(this_INT_0);
					

						newLeafNode(this_INT_0, grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_0());
					
			kw=(Token)match(input,25,FOLLOW_25_in_ruleIPV4Addr16471); 

						current.merge(kw);
						newLeafNode(kw, grammarAccess.getIPV4AddrAccess().getFullStopKeyword_1());
					
			this_INT_2=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV4Addr16481); 

						current.merge(this_INT_2);
					

						newLeafNode(this_INT_2, grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_2());
					
			kw=(Token)match(input,25,FOLLOW_25_in_ruleIPV4Addr16495); 

						current.merge(kw);
						newLeafNode(kw, grammarAccess.getIPV4AddrAccess().getFullStopKeyword_3());
					
			this_INT_4=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV4Addr16505); 

						current.merge(this_INT_4);
					

						newLeafNode(this_INT_4, grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_4());
					
			kw=(Token)match(input,25,FOLLOW_25_in_ruleIPV4Addr16519); 

						current.merge(kw);
						newLeafNode(kw, grammarAccess.getIPV4AddrAccess().getFullStopKeyword_5());
					
			this_INT_6=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV4Addr16529); 

						current.merge(this_INT_6);
					

						newLeafNode(this_INT_6, grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_6());
					
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleIPV4Addr"



	// $ANTLR start "entryRuleIPV6Seg"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5909:1: entryRuleIPV6Seg returns [String current=null] :iv_ruleIPV6Seg= ruleIPV6Seg EOF ;
	public final String entryRuleIPV6Seg() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleIPV6Seg =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5909:47: (iv_ruleIPV6Seg= ruleIPV6Seg EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5910:2: iv_ruleIPV6Seg= ruleIPV6Seg EOF
			{
			 newCompositeNode(grammarAccess.getIPV6SegRule()); 
			pushFollow(FOLLOW_ruleIPV6Seg_in_entryRuleIPV6Seg16559);
			iv_ruleIPV6Seg=ruleIPV6Seg();
			state._fsp--;

			 current =iv_ruleIPV6Seg.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleIPV6Seg16565); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleIPV6Seg"



	// $ANTLR start "ruleIPV6Seg"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5916:1: ruleIPV6Seg returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) ) ;
	public final AntlrDatatypeRuleToken ruleIPV6Seg() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_INT_0=null;
		Token this_INT_1=null;
		Token this_ID_2=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5922:2: ( (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5923:2: (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5923:2: (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) )
			int alt148=2;
			int LA148_0 = input.LA(1);
			if ( (LA148_0==RULE_INT) ) {
				int LA148_1 = input.LA(2);
				if ( (LA148_1==EOF||LA148_1==17||(LA148_1 >= 27 && LA148_1 <= 28)||LA148_1==41) ) {
					alt148=1;
				}
				else if ( (LA148_1==RULE_ID) ) {
					alt148=2;
				}

				else {
					int nvaeMark = input.mark();
					try {
						input.consume();
						NoViableAltException nvae =
							new NoViableAltException("", 148, 1, input);
						throw nvae;
					} finally {
						input.rewind(nvaeMark);
					}
				}

			}
			else if ( (LA148_0==RULE_ID) ) {
				alt148=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 148, 0, input);
				throw nvae;
			}

			switch (alt148) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5924:3: this_INT_0= RULE_INT
					{
					this_INT_0=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV6Seg16594); 

								current.merge(this_INT_0);
							

								newLeafNode(this_INT_0, grammarAccess.getIPV6SegAccess().getINTTerminalRuleCall_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5932:3: ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5932:3: ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5933:4: (this_INT_1= RULE_INT )? this_ID_2= RULE_ID
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5933:4: (this_INT_1= RULE_INT )?
					int alt147=2;
					int LA147_0 = input.LA(1);
					if ( (LA147_0==RULE_INT) ) {
						alt147=1;
					}
					switch (alt147) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5934:5: this_INT_1= RULE_INT
							{
							this_INT_1=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV6Seg16627); 

												current.merge(this_INT_1);
											

												newLeafNode(this_INT_1, grammarAccess.getIPV6SegAccess().getINTTerminalRuleCall_1_0());
											
							}
							break;

					}

					this_ID_2=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleIPV6Seg16652); 

									current.merge(this_ID_2);
								

									newLeafNode(this_ID_2, grammarAccess.getIPV6SegAccess().getIDTerminalRuleCall_1_1());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleIPV6Seg"



	// $ANTLR start "entryRuleIPV6Addr"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5954:1: entryRuleIPV6Addr returns [String current=null] :iv_ruleIPV6Addr= ruleIPV6Addr EOF ;
	public final String entryRuleIPV6Addr() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleIPV6Addr =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5954:48: (iv_ruleIPV6Addr= ruleIPV6Addr EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5955:2: iv_ruleIPV6Addr= ruleIPV6Addr EOF
			{
			 newCompositeNode(grammarAccess.getIPV6AddrRule()); 
			pushFollow(FOLLOW_ruleIPV6Addr_in_entryRuleIPV6Addr16688);
			iv_ruleIPV6Addr=ruleIPV6Addr();
			state._fsp--;

			 current =iv_ruleIPV6Addr.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleIPV6Addr16694); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleIPV6Addr"



	// $ANTLR start "ruleIPV6Addr"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5961:1: ruleIPV6Addr returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) ) ;
	public final AntlrDatatypeRuleToken ruleIPV6Addr() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token kw=null;
		Token this_ID_9=null;
		Token this_INT_15=null;
		Token this_ID_16=null;
		Token this_ID_20=null;
		Token this_INT_22=null;
		AntlrDatatypeRuleToken this_IPV6Seg_2 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_4 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_5 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_8 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_11 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_13 =null;
		AntlrDatatypeRuleToken this_IPV4Addr_18 =null;
		AntlrDatatypeRuleToken this_IPV4Addr_24 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_25 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_27 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_29 =null;
		AntlrDatatypeRuleToken this_IPV6Seg_31 =null;
		AntlrDatatypeRuleToken this_IPV4Addr_33 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5967:2: ( (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5968:2: (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5968:2: (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) )
			int alt159=7;
			alt159 = dfa159.predict(input);
			switch (alt159) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5969:3: kw= '::'
					{
					kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr16723); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5975:3: (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5975:3: (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5976:4: kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg
					{
					kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr16746); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_1_0());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5981:4: (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )*
					loop149:
					while (true) {
						int alt149=2;
						int LA149_0 = input.LA(1);
						if ( (LA149_0==RULE_INT) ) {
							int LA149_1 = input.LA(2);
							if ( (LA149_1==RULE_ID) ) {
								int LA149_2 = input.LA(3);
								if ( (LA149_2==27) ) {
									alt149=1;
								}

							}
							else if ( (LA149_1==27) ) {
								alt149=1;
							}

						}
						else if ( (LA149_0==RULE_ID) ) {
							int LA149_2 = input.LA(2);
							if ( (LA149_2==27) ) {
								alt149=1;
							}

						}

						switch (alt149) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:5982:5: this_IPV6Seg_2= ruleIPV6Seg kw= ':'
							{

												newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_1_1_0());
											
							pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16770);
							this_IPV6Seg_2=ruleIPV6Seg();
							state._fsp--;


												current.merge(this_IPV6Seg_2);
											

												afterParserOrEnumRuleCall();
											
							kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr16790); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_1_1_1());
											
							}
							break;

						default :
							break loop149;
						}
					}


									newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_1_2());
								
					pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16814);
					this_IPV6Seg_4=ruleIPV6Seg();
					state._fsp--;


									current.merge(this_IPV6Seg_4);
								

									afterParserOrEnumRuleCall();
								
					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6010:3: ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6010:3: ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6011:4: (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )?
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6011:4: (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+
					int cnt151=0;
					loop151:
					while (true) {
						int alt151=2;
						int LA151_0 = input.LA(1);
						if ( (LA151_0==RULE_INT) ) {
							int LA151_1 = input.LA(2);
							if ( (LA151_1==RULE_ID) ) {
								int LA151_2 = input.LA(3);
								if ( ((LA151_2 >= 27 && LA151_2 <= 28)) ) {
									alt151=1;
								}

							}
							else if ( ((LA151_1 >= 27 && LA151_1 <= 28)) ) {
								alt151=1;
							}

						}
						else if ( (LA151_0==RULE_ID) ) {
							int LA151_2 = input.LA(2);
							if ( ((LA151_2 >= 27 && LA151_2 <= 28)) ) {
								alt151=1;
							}

						}

						switch (alt151) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6012:5: this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' )
							{

												newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_2_0_0());
											
							pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16859);
							this_IPV6Seg_5=ruleIPV6Seg();
							state._fsp--;


												current.merge(this_IPV6Seg_5);
											

												afterParserOrEnumRuleCall();
											
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6022:5: (kw= ':' |kw= '::' )
							int alt150=2;
							int LA150_0 = input.LA(1);
							if ( (LA150_0==27) ) {
								alt150=1;
							}
							else if ( (LA150_0==28) ) {
								alt150=2;
							}

							else {
								NoViableAltException nvae =
									new NoViableAltException("", 150, 0, input);
								throw nvae;
							}

							switch (alt150) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6023:6: kw= ':'
									{
									kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr16886); 

															current.merge(kw);
															newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_2_0_1_0());
														
									}
									break;
								case 2 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6029:6: kw= '::'
									{
									kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr16913); 

															current.merge(kw);
															newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_2_0_1_1());
														
									}
									break;

							}

							}
							break;

						default :
							if ( cnt151 >= 1 ) break loop151;
							EarlyExitException eee = new EarlyExitException(151, input);
							throw eee;
						}
						cnt151++;
					}

					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6036:4: (this_IPV6Seg_8= ruleIPV6Seg )?
					int alt152=2;
					int LA152_0 = input.LA(1);
					if ( ((LA152_0 >= RULE_ID && LA152_0 <= RULE_INT)) ) {
						alt152=1;
					}
					switch (alt152) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6037:5: this_IPV6Seg_8= ruleIPV6Seg
							{

												newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_2_1());
											
							pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16951);
							this_IPV6Seg_8=ruleIPV6Seg();
							state._fsp--;


												current.merge(this_IPV6Seg_8);
											

												afterParserOrEnumRuleCall();
											
							}
							break;

					}

					}

					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6050:3: (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6050:3: (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6051:4: this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+
					{
					this_ID_9=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleIPV6Addr16992); 

									current.merge(this_ID_9);
								

									newLeafNode(this_ID_9, grammarAccess.getIPV6AddrAccess().getIDTerminalRuleCall_3_0());
								
					kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr17009); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_3_1());
								

									newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_3_2());
								
					pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17026);
					this_IPV6Seg_11=ruleIPV6Seg();
					state._fsp--;


									current.merge(this_IPV6Seg_11);
								

									afterParserOrEnumRuleCall();
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6073:4: (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )*
					loop153:
					while (true) {
						int alt153=2;
						int LA153_0 = input.LA(1);
						if ( (LA153_0==27) ) {
							alt153=1;
						}

						switch (alt153) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6074:5: kw= ':' this_IPV6Seg_13= ruleIPV6Seg
							{
							kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr17049); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_3_3_0());
											

												newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_3_3_1());
											
							pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17069);
							this_IPV6Seg_13=ruleIPV6Seg();
							state._fsp--;


												current.merge(this_IPV6Seg_13);
											

												afterParserOrEnumRuleCall();
											
							}
							break;

						default :
							break loop153;
						}
					}

					kw=(Token)match(input,17,FOLLOW_17_in_ruleIPV6Addr17094); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getPercentSignKeyword_3_4());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6095:4: (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+
					int cnt154=0;
					loop154:
					while (true) {
						int alt154=3;
						int LA154_0 = input.LA(1);
						if ( (LA154_0==RULE_INT) ) {
							alt154=1;
						}
						else if ( (LA154_0==RULE_ID) ) {
							alt154=2;
						}

						switch (alt154) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6096:5: this_INT_15= RULE_INT
							{
							this_INT_15=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV6Addr17112); 

												current.merge(this_INT_15);
											

												newLeafNode(this_INT_15, grammarAccess.getIPV6AddrAccess().getINTTerminalRuleCall_3_5_0());
											
							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6104:5: this_ID_16= RULE_ID
							{
							this_ID_16=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleIPV6Addr17142); 

												current.merge(this_ID_16);
											

												newLeafNode(this_ID_16, grammarAccess.getIPV6AddrAccess().getIDTerminalRuleCall_3_5_1());
											
							}
							break;

						default :
							if ( cnt154 >= 1 ) break loop154;
							EarlyExitException eee = new EarlyExitException(154, input);
							throw eee;
						}
						cnt154++;
					}

					}

					}
					break;
				case 5 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6114:3: (kw= '::' this_IPV4Addr_18= ruleIPV4Addr )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6114:3: (kw= '::' this_IPV4Addr_18= ruleIPV4Addr )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6115:4: kw= '::' this_IPV4Addr_18= ruleIPV4Addr
					{
					kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr17183); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_4_0());
								

									newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV4AddrParserRuleCall_4_1());
								
					pushFollow(FOLLOW_ruleIPV4Addr_in_ruleIPV6Addr17200);
					this_IPV4Addr_18=ruleIPV4Addr();
					state._fsp--;


									current.merge(this_IPV4Addr_18);
								

									afterParserOrEnumRuleCall();
								
					}

					}
					break;
				case 6 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6132:3: (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6132:3: (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6133:4: kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr
					{
					kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr17233); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_5_0());
								
					this_ID_20=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleIPV6Addr17245); 

									current.merge(this_ID_20);
								

									newLeafNode(this_ID_20, grammarAccess.getIPV6AddrAccess().getIDTerminalRuleCall_5_1());
								
					kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr17262); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_5_2());
								
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6150:4: (this_INT_22= RULE_INT kw= ':' )?
					int alt155=2;
					int LA155_0 = input.LA(1);
					if ( (LA155_0==RULE_INT) ) {
						int LA155_1 = input.LA(2);
						if ( (LA155_1==27) ) {
							alt155=1;
						}
					}
					switch (alt155) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6151:5: this_INT_22= RULE_INT kw= ':'
							{
							this_INT_22=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleIPV6Addr17280); 

												current.merge(this_INT_22);
											

												newLeafNode(this_INT_22, grammarAccess.getIPV6AddrAccess().getINTTerminalRuleCall_5_3_0());
											
							kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr17300); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_5_3_1());
											
							}
							break;

					}


									newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV4AddrParserRuleCall_5_4());
								
					pushFollow(FOLLOW_ruleIPV4Addr_in_ruleIPV6Addr17324);
					this_IPV4Addr_24=ruleIPV4Addr();
					state._fsp--;


									current.merge(this_IPV4Addr_24);
								

									afterParserOrEnumRuleCall();
								
					}

					}
					break;
				case 7 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6176:3: ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6176:3: ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6177:4: ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6177:4: ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) )
					int alt158=2;
					alt158 = dfa158.predict(input);
					switch (alt158) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6178:5: (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6178:5: (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6179:6: this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::'
							{

													newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_0_0());
												
							pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17377);
							this_IPV6Seg_25=ruleIPV6Seg();
							state._fsp--;


													current.merge(this_IPV6Seg_25);
												

													afterParserOrEnumRuleCall();
												
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6189:6: (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )*
							loop156:
							while (true) {
								int alt156=2;
								int LA156_0 = input.LA(1);
								if ( (LA156_0==27) ) {
									alt156=1;
								}

								switch (alt156) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6190:7: kw= ':' this_IPV6Seg_27= ruleIPV6Seg
									{
									kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr17408); 

																current.merge(kw);
																newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_6_0_0_1_0());
															

																newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_0_1_1());
															
									pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17434);
									this_IPV6Seg_27=ruleIPV6Seg();
									state._fsp--;


																current.merge(this_IPV6Seg_27);
															

																afterParserOrEnumRuleCall();
															
									}
									break;

								default :
									break loop156;
								}
							}

							kw=(Token)match(input,28,FOLLOW_28_in_ruleIPV6Addr17467); 

													current.merge(kw);
													newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonColonKeyword_6_0_0_2());
												
							}

							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6213:5: ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' )
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6213:5: ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6214:6: (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':'
							{
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6214:6: (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* )
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6215:7: this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )*
							{

														newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_1_0_0());
													
							pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17521);
							this_IPV6Seg_29=ruleIPV6Seg();
							state._fsp--;


														current.merge(this_IPV6Seg_29);
													

														afterParserOrEnumRuleCall();
													
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6225:7: (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )*
							loop157:
							while (true) {
								int alt157=2;
								int LA157_0 = input.LA(1);
								if ( (LA157_0==27) ) {
									int LA157_1 = input.LA(2);
									if ( (LA157_1==RULE_INT) ) {
										int LA157_2 = input.LA(3);
										if ( (LA157_2==RULE_ID||LA157_2==27) ) {
											alt157=1;
										}

									}
									else if ( (LA157_1==RULE_ID) ) {
										alt157=1;
									}

								}

								switch (alt157) {
								case 1 :
									// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6226:8: kw= ':' this_IPV6Seg_31= ruleIPV6Seg
									{
									kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr17556); 

																	current.merge(kw);
																	newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_6_0_1_0_1_0());
																

																	newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_1_0_1_1());
																
									pushFollow(FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17585);
									this_IPV6Seg_31=ruleIPV6Seg();
									state._fsp--;


																	current.merge(this_IPV6Seg_31);
																

																	afterParserOrEnumRuleCall();
																
									}
									break;

								default :
									break loop157;
								}
							}

							}

							kw=(Token)match(input,27,FOLLOW_27_in_ruleIPV6Addr17628); 

													current.merge(kw);
													newLeafNode(kw, grammarAccess.getIPV6AddrAccess().getColonKeyword_6_0_1_1());
												
							}

							}
							break;

					}


									newCompositeNode(grammarAccess.getIPV6AddrAccess().getIPV4AddrParserRuleCall_6_1());
								
					pushFollow(FOLLOW_ruleIPV4Addr_in_ruleIPV6Addr17658);
					this_IPV4Addr_33=ruleIPV4Addr();
					state._fsp--;


									current.merge(this_IPV4Addr_33);
								

									afterParserOrEnumRuleCall();
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleIPV6Addr"



	// $ANTLR start "entryRuleSignedFloat"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6265:1: entryRuleSignedFloat returns [String current=null] :iv_ruleSignedFloat= ruleSignedFloat EOF ;
	public final String entryRuleSignedFloat() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleSignedFloat =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6265:51: (iv_ruleSignedFloat= ruleSignedFloat EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6266:2: iv_ruleSignedFloat= ruleSignedFloat EOF
			{
			 newCompositeNode(grammarAccess.getSignedFloatRule()); 
			pushFollow(FOLLOW_ruleSignedFloat_in_entryRuleSignedFloat17694);
			iv_ruleSignedFloat=ruleSignedFloat();
			state._fsp--;

			 current =iv_ruleSignedFloat.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleSignedFloat17700); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleSignedFloat"



	// $ANTLR start "ruleSignedFloat"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6272:1: ruleSignedFloat returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : ( (this_SignedInt_0= ruleSignedInt |kw= '-' )? kw= '.' (this_INT_3= RULE_INT |this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) ) ;
	public final AntlrDatatypeRuleToken ruleSignedFloat() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token kw=null;
		Token this_INT_3=null;
		Token this_FLOAT_EXP_SUFFIX_4=null;
		AntlrDatatypeRuleToken this_SignedInt_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6278:2: ( ( (this_SignedInt_0= ruleSignedInt |kw= '-' )? kw= '.' (this_INT_3= RULE_INT |this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6279:2: ( (this_SignedInt_0= ruleSignedInt |kw= '-' )? kw= '.' (this_INT_3= RULE_INT |this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6279:2: ( (this_SignedInt_0= ruleSignedInt |kw= '-' )? kw= '.' (this_INT_3= RULE_INT |this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6280:3: (this_SignedInt_0= ruleSignedInt |kw= '-' )? kw= '.' (this_INT_3= RULE_INT |this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6280:3: (this_SignedInt_0= ruleSignedInt |kw= '-' )?
			int alt160=3;
			int LA160_0 = input.LA(1);
			if ( (LA160_0==RULE_INT||LA160_0==RULE_NEGINT) ) {
				alt160=1;
			}
			else if ( (LA160_0==23) ) {
				alt160=2;
			}
			switch (alt160) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6281:4: this_SignedInt_0= ruleSignedInt
					{

									newCompositeNode(grammarAccess.getSignedFloatAccess().getSignedIntParserRuleCall_0_0());
								
					pushFollow(FOLLOW_ruleSignedInt_in_ruleSignedFloat17739);
					this_SignedInt_0=ruleSignedInt();
					state._fsp--;


									current.merge(this_SignedInt_0);
								

									afterParserOrEnumRuleCall();
								
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6292:4: kw= '-'
					{
					kw=(Token)match(input,23,FOLLOW_23_in_ruleSignedFloat17765); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getSignedFloatAccess().getHyphenMinusKeyword_0_1());
								
					}
					break;

			}

			kw=(Token)match(input,25,FOLLOW_25_in_ruleSignedFloat17781); 

						current.merge(kw);
						newLeafNode(kw, grammarAccess.getSignedFloatAccess().getFullStopKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6303:3: (this_INT_3= RULE_INT |this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX )
			int alt161=2;
			int LA161_0 = input.LA(1);
			if ( (LA161_0==RULE_INT) ) {
				alt161=1;
			}
			else if ( (LA161_0==RULE_FLOAT_EXP_SUFFIX) ) {
				alt161=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 161, 0, input);
				throw nvae;
			}

			switch (alt161) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6304:4: this_INT_3= RULE_INT
					{
					this_INT_3=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleSignedFloat17796); 

									current.merge(this_INT_3);
								

									newLeafNode(this_INT_3, grammarAccess.getSignedFloatAccess().getINTTerminalRuleCall_2_0());
								
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6312:4: this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX
					{
					this_FLOAT_EXP_SUFFIX_4=(Token)match(input,RULE_FLOAT_EXP_SUFFIX,FOLLOW_RULE_FLOAT_EXP_SUFFIX_in_ruleSignedFloat17822); 

									current.merge(this_FLOAT_EXP_SUFFIX_4);
								

									newLeafNode(this_FLOAT_EXP_SUFFIX_4, grammarAccess.getSignedFloatAccess().getFLOAT_EXP_SUFFIXTerminalRuleCall_2_1());
								
					}
					break;

			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleSignedFloat"



	// $ANTLR start "entryRuleCode"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6324:1: entryRuleCode returns [EObject current=null] :iv_ruleCode= ruleCode EOF ;
	public final EObject entryRuleCode() throws RecognitionException {
		EObject current = null;


		EObject iv_ruleCode =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6324:45: (iv_ruleCode= ruleCode EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6325:2: iv_ruleCode= ruleCode EOF
			{
			 newCompositeNode(grammarAccess.getCodeRule()); 
			pushFollow(FOLLOW_ruleCode_in_entryRuleCode17858);
			iv_ruleCode=ruleCode();
			state._fsp--;

			 current =iv_ruleCode; 
			match(input,EOF,FOLLOW_EOF_in_entryRuleCode17864); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleCode"



	// $ANTLR start "ruleCode"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6331:1: ruleCode returns [EObject current=null] : ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' ) ;
	public final EObject ruleCode() throws RecognitionException {
		EObject current = null;


		Token otherlv_1=null;
		Token otherlv_3=null;
		AntlrDatatypeRuleToken lv_body_2_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6337:2: ( ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6338:2: ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6338:2: ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6339:3: () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}'
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6339:3: ()
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6340:4: 
			{

							current = forceCreateModelElement(
								grammarAccess.getCodeAccess().getCodeAction_0(),
								current);
						
			}

			otherlv_1=(Token)match(input,83,FOLLOW_83_in_ruleCode17906); 

						newLeafNode(otherlv_1, grammarAccess.getCodeAccess().getLeftCurlyBracketEqualsSignKeyword_1());
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6350:3: ( (lv_body_2_0= ruleBody ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6351:4: (lv_body_2_0= ruleBody )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6351:4: (lv_body_2_0= ruleBody )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6352:5: lv_body_2_0= ruleBody
			{

								newCompositeNode(grammarAccess.getCodeAccess().getBodyBodyParserRuleCall_2_0());
							
			pushFollow(FOLLOW_ruleBody_in_ruleCode17933);
			lv_body_2_0=ruleBody();
			state._fsp--;


								if (current==null) {
									current = createModelElementForParent(grammarAccess.getCodeRule());
								}
								set(
									current,
									"body",
									lv_body_2_0,
									"org.lflang.LF.Body");
								afterParserOrEnumRuleCall();
							
			}

			}

			otherlv_3=(Token)match(input,33,FOLLOW_33_in_ruleCode17954); 

						newLeafNode(otherlv_3, grammarAccess.getCodeAccess().getEqualsSignRightCurlyBracketKeyword_3());
					
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleCode"



	// $ANTLR start "entryRuleFSName"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6377:1: entryRuleFSName returns [String current=null] :iv_ruleFSName= ruleFSName EOF ;
	public final String entryRuleFSName() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleFSName =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6377:46: (iv_ruleFSName= ruleFSName EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6378:2: iv_ruleFSName= ruleFSName EOF
			{
			 newCompositeNode(grammarAccess.getFSNameRule()); 
			pushFollow(FOLLOW_ruleFSName_in_entryRuleFSName17980);
			iv_ruleFSName=ruleFSName();
			state._fsp--;

			 current =iv_ruleFSName.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleFSName17986); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleFSName"



	// $ANTLR start "ruleFSName"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6384:1: ruleFSName returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID |kw= '.' |kw= '_' )+ ;
	public final AntlrDatatypeRuleToken ruleFSName() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_ID_0=null;
		Token kw=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6390:2: ( (this_ID_0= RULE_ID |kw= '.' |kw= '_' )+ )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6391:2: (this_ID_0= RULE_ID |kw= '.' |kw= '_' )+
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6391:2: (this_ID_0= RULE_ID |kw= '.' |kw= '_' )+
			int cnt162=0;
			loop162:
			while (true) {
				int alt162=4;
				switch ( input.LA(1) ) {
				case RULE_ID:
					{
					alt162=1;
					}
					break;
				case 25:
					{
					alt162=2;
					}
					break;
				case 42:
					{
					alt162=3;
					}
					break;
				}
				switch (alt162) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6392:3: this_ID_0= RULE_ID
					{
					this_ID_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleFSName18015); 

								current.merge(this_ID_0);
							

								newLeafNode(this_ID_0, grammarAccess.getFSNameAccess().getIDTerminalRuleCall_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6400:3: kw= '.'
					{
					kw=(Token)match(input,25,FOLLOW_25_in_ruleFSName18037); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getFSNameAccess().getFullStopKeyword_1());
							
					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6406:3: kw= '_'
					{
					kw=(Token)match(input,42,FOLLOW_42_in_ruleFSName18055); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getFSNameAccess().get_Keyword_2());
							
					}
					break;

				default :
					if ( cnt162 >= 1 ) break loop162;
					EarlyExitException eee = new EarlyExitException(162, input);
					throw eee;
				}
				cnt162++;
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleFSName"



	// $ANTLR start "entryRulePath"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6415:1: entryRulePath returns [String current=null] :iv_rulePath= rulePath EOF ;
	public final String entryRulePath() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_rulePath =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6415:44: (iv_rulePath= rulePath EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6416:2: iv_rulePath= rulePath EOF
			{
			 newCompositeNode(grammarAccess.getPathRule()); 
			pushFollow(FOLLOW_rulePath_in_entryRulePath18082);
			iv_rulePath=rulePath();
			state._fsp--;

			 current =iv_rulePath.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRulePath18088); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRulePath"



	// $ANTLR start "rulePath"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6422:1: rulePath returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' |kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName )* ) ;
	public final AntlrDatatypeRuleToken rulePath() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token kw=null;
		AntlrDatatypeRuleToken this_FSName_0 =null;
		AntlrDatatypeRuleToken this_FSName_4 =null;
		AntlrDatatypeRuleToken this_FSName_7 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6428:2: ( ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' |kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName )* ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6429:2: ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' |kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName )* )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6429:2: ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' |kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6430:3: (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' |kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName )*
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6430:3: (this_FSName_0= ruleFSName kw= ':\\\\' )?
			int alt163=2;
			alt163 = dfa163.predict(input);
			switch (alt163) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6431:4: this_FSName_0= ruleFSName kw= ':\\\\'
					{

									newCompositeNode(grammarAccess.getPathAccess().getFSNameParserRuleCall_0_0());
								
					pushFollow(FOLLOW_ruleFSName_in_rulePath18127);
					this_FSName_0=ruleFSName();
					state._fsp--;


									current.merge(this_FSName_0);
								

									afterParserOrEnumRuleCall();
								
					kw=(Token)match(input,29,FOLLOW_29_in_rulePath18144); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getPathAccess().getColonReverseSolidusKeyword_0_1());
								
					}
					break;

			}

			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6447:3: (kw= '\\\\' |kw= '/' )?
			int alt164=3;
			int LA164_0 = input.LA(1);
			if ( (LA164_0==40) ) {
				alt164=1;
			}
			else if ( (LA164_0==26) ) {
				alt164=2;
			}
			switch (alt164) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6448:4: kw= '\\\\'
					{
					kw=(Token)match(input,40,FOLLOW_40_in_rulePath18165); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getPathAccess().getBackslashKeyword_1_0());
								
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6454:4: kw= '/'
					{
					kw=(Token)match(input,26,FOLLOW_26_in_rulePath18186); 

									current.merge(kw);
									newLeafNode(kw, grammarAccess.getPathAccess().getSolidusKeyword_1_1());
								
					}
					break;

			}


						newCompositeNode(grammarAccess.getPathAccess().getFSNameParserRuleCall_2());
					
			pushFollow(FOLLOW_ruleFSName_in_rulePath18206);
			this_FSName_4=ruleFSName();
			state._fsp--;


						current.merge(this_FSName_4);
					

						afterParserOrEnumRuleCall();
					
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6470:3: ( (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName )*
			loop166:
			while (true) {
				int alt166=2;
				int LA166_0 = input.LA(1);
				if ( (LA166_0==26||LA166_0==40) ) {
					alt166=1;
				}

				switch (alt166) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6471:4: (kw= '\\\\' |kw= '/' ) this_FSName_7= ruleFSName
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6471:4: (kw= '\\\\' |kw= '/' )
					int alt165=2;
					int LA165_0 = input.LA(1);
					if ( (LA165_0==40) ) {
						alt165=1;
					}
					else if ( (LA165_0==26) ) {
						alt165=2;
					}

					else {
						NoViableAltException nvae =
							new NoViableAltException("", 165, 0, input);
						throw nvae;
					}

					switch (alt165) {
						case 1 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6472:5: kw= '\\\\'
							{
							kw=(Token)match(input,40,FOLLOW_40_in_rulePath18231); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getPathAccess().getBackslashKeyword_3_0_0());
											
							}
							break;
						case 2 :
							// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6478:5: kw= '/'
							{
							kw=(Token)match(input,26,FOLLOW_26_in_rulePath18255); 

												current.merge(kw);
												newLeafNode(kw, grammarAccess.getPathAccess().getSolidusKeyword_3_0_1());
											
							}
							break;

					}


									newCompositeNode(grammarAccess.getPathAccess().getFSNameParserRuleCall_3_1());
								
					pushFollow(FOLLOW_ruleFSName_in_rulePath18278);
					this_FSName_7=ruleFSName();
					state._fsp--;


									current.merge(this_FSName_7);
								

									afterParserOrEnumRuleCall();
								
					}
					break;

				default :
					break loop166;
				}
			}

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "rulePath"



	// $ANTLR start "entryRuleTimeUnit"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6499:1: entryRuleTimeUnit returns [String current=null] :iv_ruleTimeUnit= ruleTimeUnit EOF ;
	public final String entryRuleTimeUnit() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleTimeUnit =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6499:48: (iv_ruleTimeUnit= ruleTimeUnit EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6500:2: iv_ruleTimeUnit= ruleTimeUnit EOF
			{
			 newCompositeNode(grammarAccess.getTimeUnitRule()); 
			pushFollow(FOLLOW_ruleTimeUnit_in_entryRuleTimeUnit18315);
			iv_ruleTimeUnit=ruleTimeUnit();
			state._fsp--;

			 current =iv_ruleTimeUnit.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleTimeUnit18321); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleTimeUnit"



	// $ANTLR start "ruleTimeUnit"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6506:1: ruleTimeUnit returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : this_ID_0= RULE_ID ;
	public final AntlrDatatypeRuleToken ruleTimeUnit() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_ID_0=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6512:2: (this_ID_0= RULE_ID )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6513:2: this_ID_0= RULE_ID
			{
			this_ID_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleTimeUnit18346); 

					current.merge(this_ID_0);
				

					newLeafNode(this_ID_0, grammarAccess.getTimeUnitAccess().getIDTerminalRuleCall());
				
			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleTimeUnit"



	// $ANTLR start "entryRuleBody"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6523:1: entryRuleBody returns [String current=null] :iv_ruleBody= ruleBody EOF ;
	public final String entryRuleBody() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleBody =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6523:44: (iv_ruleBody= ruleBody EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6524:2: iv_ruleBody= ruleBody EOF
			{
			 newCompositeNode(grammarAccess.getBodyRule()); 
			pushFollow(FOLLOW_ruleBody_in_entryRuleBody18371);
			iv_ruleBody=ruleBody();
			state._fsp--;

			 current =iv_ruleBody.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleBody18377); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleBody"



	// $ANTLR start "ruleBody"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6530:1: ruleBody returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_Token_0= ruleToken )* ;
	public final AntlrDatatypeRuleToken ruleBody() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		AntlrDatatypeRuleToken this_Token_0 =null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6536:2: ( (this_Token_0= ruleToken )* )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6537:2: (this_Token_0= ruleToken )*
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6537:2: (this_Token_0= ruleToken )*
			loop167:
			while (true) {
				int alt167=2;
				int LA167_0 = input.LA(1);
				if ( ((LA167_0 >= RULE_ANY_OTHER && LA167_0 <= 32)||(LA167_0 >= 34 && LA167_0 <= 35)||(LA167_0 >= 38 && LA167_0 <= 48)||(LA167_0 >= 50 && LA167_0 <= 72)||(LA167_0 >= 74 && LA167_0 <= 80)||LA167_0==82||LA167_0==84) ) {
					alt167=1;
				}

				switch (alt167) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6538:3: this_Token_0= ruleToken
					{

								newCompositeNode(grammarAccess.getBodyAccess().getTokenParserRuleCall());
							
					pushFollow(FOLLOW_ruleToken_in_ruleBody18410);
					this_Token_0=ruleToken();
					state._fsp--;


								current.merge(this_Token_0);
							

								afterParserOrEnumRuleCall();
							
					}
					break;

				default :
					break loop167;
				}
			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleBody"



	// $ANTLR start "entryRuleToken"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6552:1: entryRuleToken returns [String current=null] :iv_ruleToken= ruleToken EOF ;
	public final String entryRuleToken() throws RecognitionException {
		String current = null;


		AntlrDatatypeRuleToken iv_ruleToken =null;

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6552:45: (iv_ruleToken= ruleToken EOF )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6553:2: iv_ruleToken= ruleToken EOF
			{
			 newCompositeNode(grammarAccess.getTokenRule()); 
			pushFollow(FOLLOW_ruleToken_in_entryRuleToken18441);
			iv_ruleToken=ruleToken();
			state._fsp--;

			 current =iv_ruleToken.getText(); 
			match(input,EOF,FOLLOW_EOF_in_entryRuleToken18447); 
			}

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "entryRuleToken"



	// $ANTLR start "ruleToken"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6559:1: ruleToken returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID |this_INT_1= RULE_INT |this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX |this_LT_ANNOT_3= RULE_LT_ANNOT |this_STRING_4= RULE_STRING |this_CHAR_LIT_5= RULE_CHAR_LIT |this_ML_COMMENT_6= RULE_ML_COMMENT |this_SL_COMMENT_7= RULE_SL_COMMENT |this_WS_8= RULE_WS |this_ANY_OTHER_9= RULE_ANY_OTHER |kw= 'target' |kw= 'import' |kw= 'main' |kw= 'realtime' |kw= 'reactor' |kw= 'state' |kw= 'time' |kw= 'mutable' |kw= 'input' |kw= 'output' |kw= 'timer' |kw= 'action' |kw= 'reaction' |kw= 'startup' |kw= 'shutdown' |kw= 'after' |kw= 'deadline' |kw= 'mutation' |kw= 'preamble' |kw= 'new' |kw= 'federated' |kw= 'at' |kw= 'as' |kw= 'from' |kw= 'widthof' |kw= 'const' |kw= 'method' |kw= 'interleaved' |kw= 'mode' |kw= 'initial' |kw= 'reset' |kw= 'history' |this_NEGINT_42= RULE_NEGINT |this_TRUE_43= RULE_TRUE |this_FALSE_44= RULE_FALSE |kw= 'logical' |kw= 'physical' |kw= 'private' |kw= 'public' |kw= '(' |kw= ')' |kw= '{' |kw= '}' |kw= '[' |kw= ']' |kw= '<' |kw= '>' |kw= ':' |kw= ';' |kw= ',' |kw= '.' |kw= '::' |kw= ':\\\\' |kw= '\\\\' |kw= '+' |kw= '-' |kw= '*' |kw= '/' |kw= '_' |kw= '->' |kw= '=' |kw= '%' |kw= '@' |kw= '\\'' ) ;
	public final AntlrDatatypeRuleToken ruleToken() throws RecognitionException {
		AntlrDatatypeRuleToken current = new AntlrDatatypeRuleToken();


		Token this_ID_0=null;
		Token this_INT_1=null;
		Token this_FLOAT_EXP_SUFFIX_2=null;
		Token this_LT_ANNOT_3=null;
		Token this_STRING_4=null;
		Token this_CHAR_LIT_5=null;
		Token this_ML_COMMENT_6=null;
		Token this_SL_COMMENT_7=null;
		Token this_WS_8=null;
		Token this_ANY_OTHER_9=null;
		Token kw=null;
		Token this_NEGINT_42=null;
		Token this_TRUE_43=null;
		Token this_FALSE_44=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6565:2: ( (this_ID_0= RULE_ID |this_INT_1= RULE_INT |this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX |this_LT_ANNOT_3= RULE_LT_ANNOT |this_STRING_4= RULE_STRING |this_CHAR_LIT_5= RULE_CHAR_LIT |this_ML_COMMENT_6= RULE_ML_COMMENT |this_SL_COMMENT_7= RULE_SL_COMMENT |this_WS_8= RULE_WS |this_ANY_OTHER_9= RULE_ANY_OTHER |kw= 'target' |kw= 'import' |kw= 'main' |kw= 'realtime' |kw= 'reactor' |kw= 'state' |kw= 'time' |kw= 'mutable' |kw= 'input' |kw= 'output' |kw= 'timer' |kw= 'action' |kw= 'reaction' |kw= 'startup' |kw= 'shutdown' |kw= 'after' |kw= 'deadline' |kw= 'mutation' |kw= 'preamble' |kw= 'new' |kw= 'federated' |kw= 'at' |kw= 'as' |kw= 'from' |kw= 'widthof' |kw= 'const' |kw= 'method' |kw= 'interleaved' |kw= 'mode' |kw= 'initial' |kw= 'reset' |kw= 'history' |this_NEGINT_42= RULE_NEGINT |this_TRUE_43= RULE_TRUE |this_FALSE_44= RULE_FALSE |kw= 'logical' |kw= 'physical' |kw= 'private' |kw= 'public' |kw= '(' |kw= ')' |kw= '{' |kw= '}' |kw= '[' |kw= ']' |kw= '<' |kw= '>' |kw= ':' |kw= ';' |kw= ',' |kw= '.' |kw= '::' |kw= ':\\\\' |kw= '\\\\' |kw= '+' |kw= '-' |kw= '*' |kw= '/' |kw= '_' |kw= '->' |kw= '=' |kw= '%' |kw= '@' |kw= '\\'' ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6566:2: (this_ID_0= RULE_ID |this_INT_1= RULE_INT |this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX |this_LT_ANNOT_3= RULE_LT_ANNOT |this_STRING_4= RULE_STRING |this_CHAR_LIT_5= RULE_CHAR_LIT |this_ML_COMMENT_6= RULE_ML_COMMENT |this_SL_COMMENT_7= RULE_SL_COMMENT |this_WS_8= RULE_WS |this_ANY_OTHER_9= RULE_ANY_OTHER |kw= 'target' |kw= 'import' |kw= 'main' |kw= 'realtime' |kw= 'reactor' |kw= 'state' |kw= 'time' |kw= 'mutable' |kw= 'input' |kw= 'output' |kw= 'timer' |kw= 'action' |kw= 'reaction' |kw= 'startup' |kw= 'shutdown' |kw= 'after' |kw= 'deadline' |kw= 'mutation' |kw= 'preamble' |kw= 'new' |kw= 'federated' |kw= 'at' |kw= 'as' |kw= 'from' |kw= 'widthof' |kw= 'const' |kw= 'method' |kw= 'interleaved' |kw= 'mode' |kw= 'initial' |kw= 'reset' |kw= 'history' |this_NEGINT_42= RULE_NEGINT |this_TRUE_43= RULE_TRUE |this_FALSE_44= RULE_FALSE |kw= 'logical' |kw= 'physical' |kw= 'private' |kw= 'public' |kw= '(' |kw= ')' |kw= '{' |kw= '}' |kw= '[' |kw= ']' |kw= '<' |kw= '>' |kw= ':' |kw= ';' |kw= ',' |kw= '.' |kw= '::' |kw= ':\\\\' |kw= '\\\\' |kw= '+' |kw= '-' |kw= '*' |kw= '/' |kw= '_' |kw= '->' |kw= '=' |kw= '%' |kw= '@' |kw= '\\'' )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6566:2: (this_ID_0= RULE_ID |this_INT_1= RULE_INT |this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX |this_LT_ANNOT_3= RULE_LT_ANNOT |this_STRING_4= RULE_STRING |this_CHAR_LIT_5= RULE_CHAR_LIT |this_ML_COMMENT_6= RULE_ML_COMMENT |this_SL_COMMENT_7= RULE_SL_COMMENT |this_WS_8= RULE_WS |this_ANY_OTHER_9= RULE_ANY_OTHER |kw= 'target' |kw= 'import' |kw= 'main' |kw= 'realtime' |kw= 'reactor' |kw= 'state' |kw= 'time' |kw= 'mutable' |kw= 'input' |kw= 'output' |kw= 'timer' |kw= 'action' |kw= 'reaction' |kw= 'startup' |kw= 'shutdown' |kw= 'after' |kw= 'deadline' |kw= 'mutation' |kw= 'preamble' |kw= 'new' |kw= 'federated' |kw= 'at' |kw= 'as' |kw= 'from' |kw= 'widthof' |kw= 'const' |kw= 'method' |kw= 'interleaved' |kw= 'mode' |kw= 'initial' |kw= 'reset' |kw= 'history' |this_NEGINT_42= RULE_NEGINT |this_TRUE_43= RULE_TRUE |this_FALSE_44= RULE_FALSE |kw= 'logical' |kw= 'physical' |kw= 'private' |kw= 'public' |kw= '(' |kw= ')' |kw= '{' |kw= '}' |kw= '[' |kw= ']' |kw= '<' |kw= '>' |kw= ':' |kw= ';' |kw= ',' |kw= '.' |kw= '::' |kw= ':\\\\' |kw= '\\\\' |kw= '+' |kw= '-' |kw= '*' |kw= '/' |kw= '_' |kw= '->' |kw= '=' |kw= '%' |kw= '@' |kw= '\\'' )
			int alt168=74;
			switch ( input.LA(1) ) {
			case RULE_ID:
				{
				alt168=1;
				}
				break;
			case RULE_INT:
				{
				alt168=2;
				}
				break;
			case RULE_FLOAT_EXP_SUFFIX:
				{
				alt168=3;
				}
				break;
			case RULE_LT_ANNOT:
				{
				alt168=4;
				}
				break;
			case RULE_STRING:
				{
				alt168=5;
				}
				break;
			case RULE_CHAR_LIT:
				{
				alt168=6;
				}
				break;
			case RULE_ML_COMMENT:
				{
				alt168=7;
				}
				break;
			case RULE_SL_COMMENT:
				{
				alt168=8;
				}
				break;
			case RULE_WS:
				{
				alt168=9;
				}
				break;
			case RULE_ANY_OTHER:
				{
				alt168=10;
				}
				break;
			case 77:
				{
				alt168=11;
				}
				break;
			case 53:
				{
				alt168=12;
				}
				break;
			case 58:
				{
				alt168=13;
				}
				break;
			case 71:
				{
				alt168=14;
				}
				break;
			case 70:
				{
				alt168=15;
				}
				break;
			case 76:
				{
				alt168=16;
				}
				break;
			case 78:
				{
				alt168=17;
				}
				break;
			case 61:
				{
				alt168=18;
				}
				break;
			case 55:
				{
				alt168=19;
				}
				break;
			case 64:
				{
				alt168=20;
				}
				break;
			case 79:
				{
				alt168=21;
				}
				break;
			case 43:
				{
				alt168=22;
				}
				break;
			case 69:
				{
				alt168=23;
				}
				break;
			case 75:
				{
				alt168=24;
				}
				break;
			case 74:
				{
				alt168=25;
				}
				break;
			case 44:
				{
				alt168=26;
				}
				break;
			case 48:
				{
				alt168=27;
				}
				break;
			case 62:
				{
				alt168=28;
				}
				break;
			case 66:
				{
				alt168=29;
				}
				break;
			case 63:
				{
				alt168=30;
				}
				break;
			case 50:
				{
				alt168=31;
				}
				break;
			case 46:
				{
				alt168=32;
				}
				break;
			case 45:
				{
				alt168=33;
				}
				break;
			case 51:
				{
				alt168=34;
				}
				break;
			case 80:
				{
				alt168=35;
				}
				break;
			case 47:
				{
				alt168=36;
				}
				break;
			case 59:
				{
				alt168=37;
				}
				break;
			case 56:
				{
				alt168=38;
				}
				break;
			case 60:
				{
				alt168=39;
				}
				break;
			case 54:
				{
				alt168=40;
				}
				break;
			case 72:
				{
				alt168=41;
				}
				break;
			case 52:
				{
				alt168=42;
				}
				break;
			case RULE_NEGINT:
				{
				alt168=43;
				}
				break;
			case RULE_TRUE:
				{
				alt168=44;
				}
				break;
			case RULE_FALSE:
				{
				alt168=45;
				}
				break;
			case 57:
				{
				alt168=46;
				}
				break;
			case 65:
				{
				alt168=47;
				}
				break;
			case 67:
				{
				alt168=48;
				}
				break;
			case 68:
				{
				alt168=49;
				}
				break;
			case 18:
				{
				alt168=50;
				}
				break;
			case 19:
				{
				alt168=51;
				}
				break;
			case 82:
				{
				alt168=52;
				}
				break;
			case 84:
				{
				alt168=53;
				}
				break;
			case 38:
				{
				alt168=54;
				}
				break;
			case 41:
				{
				alt168=55;
				}
				break;
			case 31:
				{
				alt168=56;
				}
				break;
			case 34:
				{
				alt168=57;
				}
				break;
			case 27:
				{
				alt168=58;
				}
				break;
			case 30:
				{
				alt168=59;
				}
				break;
			case 22:
				{
				alt168=60;
				}
				break;
			case 25:
				{
				alt168=61;
				}
				break;
			case 28:
				{
				alt168=62;
				}
				break;
			case 29:
				{
				alt168=63;
				}
				break;
			case 40:
				{
				alt168=64;
				}
				break;
			case 21:
				{
				alt168=65;
				}
				break;
			case 23:
				{
				alt168=66;
				}
				break;
			case 20:
				{
				alt168=67;
				}
				break;
			case 26:
				{
				alt168=68;
				}
				break;
			case 42:
				{
				alt168=69;
				}
				break;
			case 24:
				{
				alt168=70;
				}
				break;
			case 32:
				{
				alt168=71;
				}
				break;
			case 17:
				{
				alt168=72;
				}
				break;
			case 35:
				{
				alt168=73;
				}
				break;
			case 39:
				{
				alt168=74;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 168, 0, input);
				throw nvae;
			}
			switch (alt168) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6567:3: this_ID_0= RULE_ID
					{
					this_ID_0=(Token)match(input,RULE_ID,FOLLOW_RULE_ID_in_ruleToken18476); 

								current.merge(this_ID_0);
							

								newLeafNode(this_ID_0, grammarAccess.getTokenAccess().getIDTerminalRuleCall_0());
							
					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6575:3: this_INT_1= RULE_INT
					{
					this_INT_1=(Token)match(input,RULE_INT,FOLLOW_RULE_INT_in_ruleToken18498); 

								current.merge(this_INT_1);
							

								newLeafNode(this_INT_1, grammarAccess.getTokenAccess().getINTTerminalRuleCall_1());
							
					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6583:3: this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX
					{
					this_FLOAT_EXP_SUFFIX_2=(Token)match(input,RULE_FLOAT_EXP_SUFFIX,FOLLOW_RULE_FLOAT_EXP_SUFFIX_in_ruleToken18520); 

								current.merge(this_FLOAT_EXP_SUFFIX_2);
							

								newLeafNode(this_FLOAT_EXP_SUFFIX_2, grammarAccess.getTokenAccess().getFLOAT_EXP_SUFFIXTerminalRuleCall_2());
							
					}
					break;
				case 4 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6591:3: this_LT_ANNOT_3= RULE_LT_ANNOT
					{
					this_LT_ANNOT_3=(Token)match(input,RULE_LT_ANNOT,FOLLOW_RULE_LT_ANNOT_in_ruleToken18542); 

								current.merge(this_LT_ANNOT_3);
							

								newLeafNode(this_LT_ANNOT_3, grammarAccess.getTokenAccess().getLT_ANNOTTerminalRuleCall_3());
							
					}
					break;
				case 5 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6599:3: this_STRING_4= RULE_STRING
					{
					this_STRING_4=(Token)match(input,RULE_STRING,FOLLOW_RULE_STRING_in_ruleToken18564); 

								current.merge(this_STRING_4);
							

								newLeafNode(this_STRING_4, grammarAccess.getTokenAccess().getSTRINGTerminalRuleCall_4());
							
					}
					break;
				case 6 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6607:3: this_CHAR_LIT_5= RULE_CHAR_LIT
					{
					this_CHAR_LIT_5=(Token)match(input,RULE_CHAR_LIT,FOLLOW_RULE_CHAR_LIT_in_ruleToken18586); 

								current.merge(this_CHAR_LIT_5);
							

								newLeafNode(this_CHAR_LIT_5, grammarAccess.getTokenAccess().getCHAR_LITTerminalRuleCall_5());
							
					}
					break;
				case 7 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6615:3: this_ML_COMMENT_6= RULE_ML_COMMENT
					{
					this_ML_COMMENT_6=(Token)match(input,RULE_ML_COMMENT,FOLLOW_RULE_ML_COMMENT_in_ruleToken18608); 

								current.merge(this_ML_COMMENT_6);
							

								newLeafNode(this_ML_COMMENT_6, grammarAccess.getTokenAccess().getML_COMMENTTerminalRuleCall_6());
							
					}
					break;
				case 8 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6623:3: this_SL_COMMENT_7= RULE_SL_COMMENT
					{
					this_SL_COMMENT_7=(Token)match(input,RULE_SL_COMMENT,FOLLOW_RULE_SL_COMMENT_in_ruleToken18630); 

								current.merge(this_SL_COMMENT_7);
							

								newLeafNode(this_SL_COMMENT_7, grammarAccess.getTokenAccess().getSL_COMMENTTerminalRuleCall_7());
							
					}
					break;
				case 9 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6631:3: this_WS_8= RULE_WS
					{
					this_WS_8=(Token)match(input,RULE_WS,FOLLOW_RULE_WS_in_ruleToken18652); 

								current.merge(this_WS_8);
							

								newLeafNode(this_WS_8, grammarAccess.getTokenAccess().getWSTerminalRuleCall_8());
							
					}
					break;
				case 10 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6639:3: this_ANY_OTHER_9= RULE_ANY_OTHER
					{
					this_ANY_OTHER_9=(Token)match(input,RULE_ANY_OTHER,FOLLOW_RULE_ANY_OTHER_in_ruleToken18674); 

								current.merge(this_ANY_OTHER_9);
							

								newLeafNode(this_ANY_OTHER_9, grammarAccess.getTokenAccess().getANY_OTHERTerminalRuleCall_9());
							
					}
					break;
				case 11 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6647:3: kw= 'target'
					{
					kw=(Token)match(input,77,FOLLOW_77_in_ruleToken18696); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getTargetKeyword_10());
							
					}
					break;
				case 12 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6653:3: kw= 'import'
					{
					kw=(Token)match(input,53,FOLLOW_53_in_ruleToken18714); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getImportKeyword_11());
							
					}
					break;
				case 13 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6659:3: kw= 'main'
					{
					kw=(Token)match(input,58,FOLLOW_58_in_ruleToken18732); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getMainKeyword_12());
							
					}
					break;
				case 14 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6665:3: kw= 'realtime'
					{
					kw=(Token)match(input,71,FOLLOW_71_in_ruleToken18750); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getRealtimeKeyword_13());
							
					}
					break;
				case 15 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6671:3: kw= 'reactor'
					{
					kw=(Token)match(input,70,FOLLOW_70_in_ruleToken18768); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getReactorKeyword_14());
							
					}
					break;
				case 16 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6677:3: kw= 'state'
					{
					kw=(Token)match(input,76,FOLLOW_76_in_ruleToken18786); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getStateKeyword_15());
							
					}
					break;
				case 17 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6683:3: kw= 'time'
					{
					kw=(Token)match(input,78,FOLLOW_78_in_ruleToken18804); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getTimeKeyword_16());
							
					}
					break;
				case 18 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6689:3: kw= 'mutable'
					{
					kw=(Token)match(input,61,FOLLOW_61_in_ruleToken18822); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getMutableKeyword_17());
							
					}
					break;
				case 19 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6695:3: kw= 'input'
					{
					kw=(Token)match(input,55,FOLLOW_55_in_ruleToken18840); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getInputKeyword_18());
							
					}
					break;
				case 20 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6701:3: kw= 'output'
					{
					kw=(Token)match(input,64,FOLLOW_64_in_ruleToken18858); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getOutputKeyword_19());
							
					}
					break;
				case 21 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6707:3: kw= 'timer'
					{
					kw=(Token)match(input,79,FOLLOW_79_in_ruleToken18876); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getTimerKeyword_20());
							
					}
					break;
				case 22 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6713:3: kw= 'action'
					{
					kw=(Token)match(input,43,FOLLOW_43_in_ruleToken18894); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getActionKeyword_21());
							
					}
					break;
				case 23 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6719:3: kw= 'reaction'
					{
					kw=(Token)match(input,69,FOLLOW_69_in_ruleToken18912); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getReactionKeyword_22());
							
					}
					break;
				case 24 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6725:3: kw= 'startup'
					{
					kw=(Token)match(input,75,FOLLOW_75_in_ruleToken18930); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getStartupKeyword_23());
							
					}
					break;
				case 25 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6731:3: kw= 'shutdown'
					{
					kw=(Token)match(input,74,FOLLOW_74_in_ruleToken18948); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getShutdownKeyword_24());
							
					}
					break;
				case 26 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6737:3: kw= 'after'
					{
					kw=(Token)match(input,44,FOLLOW_44_in_ruleToken18966); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getAfterKeyword_25());
							
					}
					break;
				case 27 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6743:3: kw= 'deadline'
					{
					kw=(Token)match(input,48,FOLLOW_48_in_ruleToken18984); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getDeadlineKeyword_26());
							
					}
					break;
				case 28 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6749:3: kw= 'mutation'
					{
					kw=(Token)match(input,62,FOLLOW_62_in_ruleToken19002); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getMutationKeyword_27());
							
					}
					break;
				case 29 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6755:3: kw= 'preamble'
					{
					kw=(Token)match(input,66,FOLLOW_66_in_ruleToken19020); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getPreambleKeyword_28());
							
					}
					break;
				case 30 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6761:3: kw= 'new'
					{
					kw=(Token)match(input,63,FOLLOW_63_in_ruleToken19038); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getNewKeyword_29());
							
					}
					break;
				case 31 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6767:3: kw= 'federated'
					{
					kw=(Token)match(input,50,FOLLOW_50_in_ruleToken19056); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getFederatedKeyword_30());
							
					}
					break;
				case 32 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6773:3: kw= 'at'
					{
					kw=(Token)match(input,46,FOLLOW_46_in_ruleToken19074); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getAtKeyword_31());
							
					}
					break;
				case 33 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6779:3: kw= 'as'
					{
					kw=(Token)match(input,45,FOLLOW_45_in_ruleToken19092); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getAsKeyword_32());
							
					}
					break;
				case 34 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6785:3: kw= 'from'
					{
					kw=(Token)match(input,51,FOLLOW_51_in_ruleToken19110); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getFromKeyword_33());
							
					}
					break;
				case 35 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6791:3: kw= 'widthof'
					{
					kw=(Token)match(input,80,FOLLOW_80_in_ruleToken19128); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getWidthofKeyword_34());
							
					}
					break;
				case 36 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6797:3: kw= 'const'
					{
					kw=(Token)match(input,47,FOLLOW_47_in_ruleToken19146); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getConstKeyword_35());
							
					}
					break;
				case 37 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6803:3: kw= 'method'
					{
					kw=(Token)match(input,59,FOLLOW_59_in_ruleToken19164); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getMethodKeyword_36());
							
					}
					break;
				case 38 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6809:3: kw= 'interleaved'
					{
					kw=(Token)match(input,56,FOLLOW_56_in_ruleToken19182); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getInterleavedKeyword_37());
							
					}
					break;
				case 39 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6815:3: kw= 'mode'
					{
					kw=(Token)match(input,60,FOLLOW_60_in_ruleToken19200); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getModeKeyword_38());
							
					}
					break;
				case 40 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6821:3: kw= 'initial'
					{
					kw=(Token)match(input,54,FOLLOW_54_in_ruleToken19218); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getInitialKeyword_39());
							
					}
					break;
				case 41 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6827:3: kw= 'reset'
					{
					kw=(Token)match(input,72,FOLLOW_72_in_ruleToken19236); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getResetKeyword_40());
							
					}
					break;
				case 42 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6833:3: kw= 'history'
					{
					kw=(Token)match(input,52,FOLLOW_52_in_ruleToken19254); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getHistoryKeyword_41());
							
					}
					break;
				case 43 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6839:3: this_NEGINT_42= RULE_NEGINT
					{
					this_NEGINT_42=(Token)match(input,RULE_NEGINT,FOLLOW_RULE_NEGINT_in_ruleToken19272); 

								current.merge(this_NEGINT_42);
							

								newLeafNode(this_NEGINT_42, grammarAccess.getTokenAccess().getNEGINTTerminalRuleCall_42());
							
					}
					break;
				case 44 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6847:3: this_TRUE_43= RULE_TRUE
					{
					this_TRUE_43=(Token)match(input,RULE_TRUE,FOLLOW_RULE_TRUE_in_ruleToken19294); 

								current.merge(this_TRUE_43);
							

								newLeafNode(this_TRUE_43, grammarAccess.getTokenAccess().getTRUETerminalRuleCall_43());
							
					}
					break;
				case 45 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6855:3: this_FALSE_44= RULE_FALSE
					{
					this_FALSE_44=(Token)match(input,RULE_FALSE,FOLLOW_RULE_FALSE_in_ruleToken19316); 

								current.merge(this_FALSE_44);
							

								newLeafNode(this_FALSE_44, grammarAccess.getTokenAccess().getFALSETerminalRuleCall_44());
							
					}
					break;
				case 46 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6863:3: kw= 'logical'
					{
					kw=(Token)match(input,57,FOLLOW_57_in_ruleToken19338); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getLogicalKeyword_45());
							
					}
					break;
				case 47 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6869:3: kw= 'physical'
					{
					kw=(Token)match(input,65,FOLLOW_65_in_ruleToken19356); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getPhysicalKeyword_46());
							
					}
					break;
				case 48 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6875:3: kw= 'private'
					{
					kw=(Token)match(input,67,FOLLOW_67_in_ruleToken19374); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getPrivateKeyword_47());
							
					}
					break;
				case 49 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6881:3: kw= 'public'
					{
					kw=(Token)match(input,68,FOLLOW_68_in_ruleToken19392); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getPublicKeyword_48());
							
					}
					break;
				case 50 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6887:3: kw= '('
					{
					kw=(Token)match(input,18,FOLLOW_18_in_ruleToken19410); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getLeftParenthesisKeyword_49());
							
					}
					break;
				case 51 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6893:3: kw= ')'
					{
					kw=(Token)match(input,19,FOLLOW_19_in_ruleToken19428); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getRightParenthesisKeyword_50());
							
					}
					break;
				case 52 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6899:3: kw= '{'
					{
					kw=(Token)match(input,82,FOLLOW_82_in_ruleToken19446); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getLeftCurlyBracketKeyword_51());
							
					}
					break;
				case 53 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6905:3: kw= '}'
					{
					kw=(Token)match(input,84,FOLLOW_84_in_ruleToken19464); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getRightCurlyBracketKeyword_52());
							
					}
					break;
				case 54 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6911:3: kw= '['
					{
					kw=(Token)match(input,38,FOLLOW_38_in_ruleToken19482); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getLeftSquareBracketKeyword_53());
							
					}
					break;
				case 55 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6917:3: kw= ']'
					{
					kw=(Token)match(input,41,FOLLOW_41_in_ruleToken19500); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getRightSquareBracketKeyword_54());
							
					}
					break;
				case 56 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6923:3: kw= '<'
					{
					kw=(Token)match(input,31,FOLLOW_31_in_ruleToken19518); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getLessThanSignKeyword_55());
							
					}
					break;
				case 57 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6929:3: kw= '>'
					{
					kw=(Token)match(input,34,FOLLOW_34_in_ruleToken19536); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getGreaterThanSignKeyword_56());
							
					}
					break;
				case 58 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6935:3: kw= ':'
					{
					kw=(Token)match(input,27,FOLLOW_27_in_ruleToken19554); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getColonKeyword_57());
							
					}
					break;
				case 59 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6941:3: kw= ';'
					{
					kw=(Token)match(input,30,FOLLOW_30_in_ruleToken19572); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getSemicolonKeyword_58());
							
					}
					break;
				case 60 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6947:3: kw= ','
					{
					kw=(Token)match(input,22,FOLLOW_22_in_ruleToken19590); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getCommaKeyword_59());
							
					}
					break;
				case 61 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6953:3: kw= '.'
					{
					kw=(Token)match(input,25,FOLLOW_25_in_ruleToken19608); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getFullStopKeyword_60());
							
					}
					break;
				case 62 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6959:3: kw= '::'
					{
					kw=(Token)match(input,28,FOLLOW_28_in_ruleToken19626); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getColonColonKeyword_61());
							
					}
					break;
				case 63 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6965:3: kw= ':\\\\'
					{
					kw=(Token)match(input,29,FOLLOW_29_in_ruleToken19644); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getColonReverseSolidusKeyword_62());
							
					}
					break;
				case 64 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6971:3: kw= '\\\\'
					{
					kw=(Token)match(input,40,FOLLOW_40_in_ruleToken19662); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getBackslashKeyword_63());
							
					}
					break;
				case 65 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6977:3: kw= '+'
					{
					kw=(Token)match(input,21,FOLLOW_21_in_ruleToken19680); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getPlusSignKeyword_64());
							
					}
					break;
				case 66 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6983:3: kw= '-'
					{
					kw=(Token)match(input,23,FOLLOW_23_in_ruleToken19698); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getHyphenMinusKeyword_65());
							
					}
					break;
				case 67 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6989:3: kw= '*'
					{
					kw=(Token)match(input,20,FOLLOW_20_in_ruleToken19716); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getAsteriskKeyword_66());
							
					}
					break;
				case 68 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:6995:3: kw= '/'
					{
					kw=(Token)match(input,26,FOLLOW_26_in_ruleToken19734); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getSolidusKeyword_67());
							
					}
					break;
				case 69 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7001:3: kw= '_'
					{
					kw=(Token)match(input,42,FOLLOW_42_in_ruleToken19752); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().get_Keyword_68());
							
					}
					break;
				case 70 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7007:3: kw= '->'
					{
					kw=(Token)match(input,24,FOLLOW_24_in_ruleToken19770); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getHyphenMinusGreaterThanSignKeyword_69());
							
					}
					break;
				case 71 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7013:3: kw= '='
					{
					kw=(Token)match(input,32,FOLLOW_32_in_ruleToken19788); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getEqualsSignKeyword_70());
							
					}
					break;
				case 72 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7019:3: kw= '%'
					{
					kw=(Token)match(input,17,FOLLOW_17_in_ruleToken19806); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getPercentSignKeyword_71());
							
					}
					break;
				case 73 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7025:3: kw= '@'
					{
					kw=(Token)match(input,35,FOLLOW_35_in_ruleToken19824); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getCommercialAtKeyword_72());
							
					}
					break;
				case 74 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7031:3: kw= '\\''
					{
					kw=(Token)match(input,39,FOLLOW_39_in_ruleToken19842); 

								current.merge(kw);
								newLeafNode(kw, grammarAccess.getTokenAccess().getApostropheKeyword_73());
							
					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleToken"



	// $ANTLR start "ruleActionOrigin"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7040:1: ruleActionOrigin returns [Enumerator current=null] : ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) ) ;
	public final Enumerator ruleActionOrigin() throws RecognitionException {
		Enumerator current = null;


		Token enumLiteral_0=null;
		Token enumLiteral_1=null;
		Token enumLiteral_2=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7046:2: ( ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7047:2: ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7047:2: ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) )
			int alt169=3;
			switch ( input.LA(1) ) {
			case 36:
				{
				alt169=1;
				}
				break;
			case 57:
				{
				alt169=2;
				}
				break;
			case 65:
				{
				alt169=3;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 169, 0, input);
				throw nvae;
			}
			switch (alt169) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7048:3: (enumLiteral_0= 'NONE' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7048:3: (enumLiteral_0= 'NONE' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7049:4: enumLiteral_0= 'NONE'
					{
					enumLiteral_0=(Token)match(input,36,FOLLOW_36_in_ruleActionOrigin19884); 

									current = grammarAccess.getActionOriginAccess().getNONEEnumLiteralDeclaration_0().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_0, grammarAccess.getActionOriginAccess().getNONEEnumLiteralDeclaration_0());
								
					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7056:3: (enumLiteral_1= 'logical' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7056:3: (enumLiteral_1= 'logical' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7057:4: enumLiteral_1= 'logical'
					{
					enumLiteral_1=(Token)match(input,57,FOLLOW_57_in_ruleActionOrigin19912); 

									current = grammarAccess.getActionOriginAccess().getLOGICALEnumLiteralDeclaration_1().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_1, grammarAccess.getActionOriginAccess().getLOGICALEnumLiteralDeclaration_1());
								
					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7064:3: (enumLiteral_2= 'physical' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7064:3: (enumLiteral_2= 'physical' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7065:4: enumLiteral_2= 'physical'
					{
					enumLiteral_2=(Token)match(input,65,FOLLOW_65_in_ruleActionOrigin19940); 

									current = grammarAccess.getActionOriginAccess().getPHYSICALEnumLiteralDeclaration_2().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_2, grammarAccess.getActionOriginAccess().getPHYSICALEnumLiteralDeclaration_2());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleActionOrigin"



	// $ANTLR start "ruleVisibility"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7075:1: ruleVisibility returns [Enumerator current=null] : ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'private' ) | (enumLiteral_2= 'public' ) ) ;
	public final Enumerator ruleVisibility() throws RecognitionException {
		Enumerator current = null;


		Token enumLiteral_0=null;
		Token enumLiteral_1=null;
		Token enumLiteral_2=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7081:2: ( ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'private' ) | (enumLiteral_2= 'public' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7082:2: ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'private' ) | (enumLiteral_2= 'public' ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7082:2: ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'private' ) | (enumLiteral_2= 'public' ) )
			int alt170=3;
			switch ( input.LA(1) ) {
			case 36:
				{
				alt170=1;
				}
				break;
			case 67:
				{
				alt170=2;
				}
				break;
			case 68:
				{
				alt170=3;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 170, 0, input);
				throw nvae;
			}
			switch (alt170) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7083:3: (enumLiteral_0= 'NONE' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7083:3: (enumLiteral_0= 'NONE' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7084:4: enumLiteral_0= 'NONE'
					{
					enumLiteral_0=(Token)match(input,36,FOLLOW_36_in_ruleVisibility19987); 

									current = grammarAccess.getVisibilityAccess().getNONEEnumLiteralDeclaration_0().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_0, grammarAccess.getVisibilityAccess().getNONEEnumLiteralDeclaration_0());
								
					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7091:3: (enumLiteral_1= 'private' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7091:3: (enumLiteral_1= 'private' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7092:4: enumLiteral_1= 'private'
					{
					enumLiteral_1=(Token)match(input,67,FOLLOW_67_in_ruleVisibility20015); 

									current = grammarAccess.getVisibilityAccess().getPRIVATEEnumLiteralDeclaration_1().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_1, grammarAccess.getVisibilityAccess().getPRIVATEEnumLiteralDeclaration_1());
								
					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7099:3: (enumLiteral_2= 'public' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7099:3: (enumLiteral_2= 'public' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7100:4: enumLiteral_2= 'public'
					{
					enumLiteral_2=(Token)match(input,68,FOLLOW_68_in_ruleVisibility20043); 

									current = grammarAccess.getVisibilityAccess().getPUBLICEnumLiteralDeclaration_2().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_2, grammarAccess.getVisibilityAccess().getPUBLICEnumLiteralDeclaration_2());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleVisibility"



	// $ANTLR start "ruleBuiltinTrigger"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7110:1: ruleBuiltinTrigger returns [Enumerator current=null] : ( (enumLiteral_0= 'startup' ) | (enumLiteral_1= 'shutdown' ) | (enumLiteral_2= 'reset' ) ) ;
	public final Enumerator ruleBuiltinTrigger() throws RecognitionException {
		Enumerator current = null;


		Token enumLiteral_0=null;
		Token enumLiteral_1=null;
		Token enumLiteral_2=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7116:2: ( ( (enumLiteral_0= 'startup' ) | (enumLiteral_1= 'shutdown' ) | (enumLiteral_2= 'reset' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7117:2: ( (enumLiteral_0= 'startup' ) | (enumLiteral_1= 'shutdown' ) | (enumLiteral_2= 'reset' ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7117:2: ( (enumLiteral_0= 'startup' ) | (enumLiteral_1= 'shutdown' ) | (enumLiteral_2= 'reset' ) )
			int alt171=3;
			switch ( input.LA(1) ) {
			case 75:
				{
				alt171=1;
				}
				break;
			case 74:
				{
				alt171=2;
				}
				break;
			case 72:
				{
				alt171=3;
				}
				break;
			default:
				NoViableAltException nvae =
					new NoViableAltException("", 171, 0, input);
				throw nvae;
			}
			switch (alt171) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7118:3: (enumLiteral_0= 'startup' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7118:3: (enumLiteral_0= 'startup' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7119:4: enumLiteral_0= 'startup'
					{
					enumLiteral_0=(Token)match(input,75,FOLLOW_75_in_ruleBuiltinTrigger20090); 

									current = grammarAccess.getBuiltinTriggerAccess().getSTARTUPEnumLiteralDeclaration_0().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_0, grammarAccess.getBuiltinTriggerAccess().getSTARTUPEnumLiteralDeclaration_0());
								
					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7126:3: (enumLiteral_1= 'shutdown' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7126:3: (enumLiteral_1= 'shutdown' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7127:4: enumLiteral_1= 'shutdown'
					{
					enumLiteral_1=(Token)match(input,74,FOLLOW_74_in_ruleBuiltinTrigger20118); 

									current = grammarAccess.getBuiltinTriggerAccess().getSHUTDOWNEnumLiteralDeclaration_1().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_1, grammarAccess.getBuiltinTriggerAccess().getSHUTDOWNEnumLiteralDeclaration_1());
								
					}

					}
					break;
				case 3 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7134:3: (enumLiteral_2= 'reset' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7134:3: (enumLiteral_2= 'reset' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7135:4: enumLiteral_2= 'reset'
					{
					enumLiteral_2=(Token)match(input,72,FOLLOW_72_in_ruleBuiltinTrigger20146); 

									current = grammarAccess.getBuiltinTriggerAccess().getRESETEnumLiteralDeclaration_2().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_2, grammarAccess.getBuiltinTriggerAccess().getRESETEnumLiteralDeclaration_2());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleBuiltinTrigger"



	// $ANTLR start "ruleModeTransition"
	// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7145:1: ruleModeTransition returns [Enumerator current=null] : ( (enumLiteral_0= 'reset' ) | (enumLiteral_1= 'history' ) ) ;
	public final Enumerator ruleModeTransition() throws RecognitionException {
		Enumerator current = null;


		Token enumLiteral_0=null;
		Token enumLiteral_1=null;


			enterRule();

		try {
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7151:2: ( ( (enumLiteral_0= 'reset' ) | (enumLiteral_1= 'history' ) ) )
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7152:2: ( (enumLiteral_0= 'reset' ) | (enumLiteral_1= 'history' ) )
			{
			// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7152:2: ( (enumLiteral_0= 'reset' ) | (enumLiteral_1= 'history' ) )
			int alt172=2;
			int LA172_0 = input.LA(1);
			if ( (LA172_0==72) ) {
				alt172=1;
			}
			else if ( (LA172_0==52) ) {
				alt172=2;
			}

			else {
				NoViableAltException nvae =
					new NoViableAltException("", 172, 0, input);
				throw nvae;
			}

			switch (alt172) {
				case 1 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7153:3: (enumLiteral_0= 'reset' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7153:3: (enumLiteral_0= 'reset' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7154:4: enumLiteral_0= 'reset'
					{
					enumLiteral_0=(Token)match(input,72,FOLLOW_72_in_ruleModeTransition20193); 

									current = grammarAccess.getModeTransitionAccess().getRESETEnumLiteralDeclaration_0().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_0, grammarAccess.getModeTransitionAccess().getRESETEnumLiteralDeclaration_0());
								
					}

					}
					break;
				case 2 :
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7161:3: (enumLiteral_1= 'history' )
					{
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7161:3: (enumLiteral_1= 'history' )
					// C:\\Users\\pmora\\Documents\\Git\\GitHub\\LinguaFranca\\Antlr/InternalLF.g:7162:4: enumLiteral_1= 'history'
					{
					enumLiteral_1=(Token)match(input,52,FOLLOW_52_in_ruleModeTransition20221); 

									current = grammarAccess.getModeTransitionAccess().getHISTORYEnumLiteralDeclaration_1().getEnumLiteral().getInstance();
									newLeafNode(enumLiteral_1, grammarAccess.getModeTransitionAccess().getHISTORYEnumLiteralDeclaration_1());
								
					}

					}
					break;

			}

			}


				leaveRule();

		}

		    catch (RecognitionException re) {
		        recover(input,re);
		        appendSkippedTokens();
		    }

		finally {
			// do for sure before leaving
		}
		return current;
	}
	// $ANTLR end "ruleModeTransition"

	// Delegated rules


	protected DFA18 dfa18 = new DFA18(this);
	protected DFA30 dfa30 = new DFA30(this);
	protected DFA54 dfa54 = new DFA54(this);
	protected DFA103 dfa103 = new DFA103(this);
	protected DFA121 dfa121 = new DFA121(this);
	protected DFA122 dfa122 = new DFA122(this);
	protected DFA137 dfa137 = new DFA137(this);
	protected DFA139 dfa139 = new DFA139(this);
	protected DFA159 dfa159 = new DFA159(this);
	protected DFA158 dfa158 = new DFA158(this);
	protected DFA163 dfa163 = new DFA163(this);
	static final String DFA18_eotS =
		"\52\uffff";
	static final String DFA18_eofS =
		"\52\uffff";
	static final String DFA18_minS =
		"\1\10\1\uffff\1\53\1\uffff\1\10\6\uffff\1\26\3\uffff\1\22\1\uffff\1\6"+
		"\1\40\5\23\1\31\1\7\1\43\2\6\2\23\1\40\5\23\1\31\1\7\1\6\2\23";
	static final String DFA18_maxS =
		"\1\124\1\uffff\1\102\1\uffff\1\10\6\uffff\1\125\3\uffff\1\117\1\uffff"+
		"\1\31\1\40\1\26\2\31\2\26\1\31\1\11\1\117\2\31\2\26\1\40\1\26\2\31\2\26"+
		"\1\31\1\11\1\31\2\26";
	static final String DFA18_acceptS =
		"\1\uffff\1\14\1\uffff\1\1\1\uffff\1\2\1\3\1\4\1\5\1\6\1\7\1\uffff\1\11"+
		"\1\12\1\13\1\uffff\1\10\31\uffff";
	static final String DFA18_specialS =
		"\52\uffff}>";
	static final String[] DFA18_transitionS = {
			"\1\13\11\uffff\1\14\20\uffff\1\4\1\2\6\uffff\1\12\3\uffff\1\6\6\uffff"+
			"\1\16\1\7\1\14\1\12\1\uffff\1\6\1\16\1\7\1\15\1\uffff\1\10\1\12\3\3\1"+
			"\15\2\uffff\1\5\3\uffff\1\5\2\uffff\1\11\4\uffff\1\1",
			"",
			"\1\12\26\uffff\1\3",
			"",
			"\1\17",
			"",
			"",
			"",
			"",
			"",
			"",
			"\1\14\1\uffff\2\14\6\uffff\1\20\64\uffff\1\14",
			"",
			"",
			"",
			"\1\21\20\uffff\1\4\1\12\6\uffff\1\12\13\uffff\1\7\1\uffff\1\12\3\uffff"+
			"\1\7\1\15\1\uffff\1\10\1\12\3\uffff\1\15\2\uffff\1\5\3\uffff\1\5\2\uffff"+
			"\1\11",
			"",
			"\1\27\1\uffff\1\22\1\24\2\uffff\1\25\1\uffff\1\23\1\26\3\uffff\1\32"+
			"\3\uffff\1\30\1\uffff\1\31",
			"\1\33",
			"\1\32\2\uffff\1\34",
			"\1\32\2\uffff\1\34\2\uffff\1\31",
			"\1\32\2\uffff\1\34\2\uffff\1\31",
			"\1\32\2\uffff\1\34",
			"\1\32\2\uffff\1\34",
			"\1\31",
			"\1\36\1\uffff\1\35",
			"\1\4\1\12\6\uffff\1\12\13\uffff\1\7\1\uffff\1\12\3\uffff\1\7\1\15\1"+
			"\uffff\1\10\1\12\3\uffff\1\15\2\uffff\1\5\3\uffff\1\5\2\uffff\1\11",
			"\1\27\2\uffff\1\24\2\uffff\1\25\1\uffff\1\23\1\26\7\uffff\1\30\1\uffff"+
			"\1\31",
			"\1\44\1\uffff\1\37\1\41\2\uffff\1\42\1\uffff\1\40\1\43\3\uffff\1\32"+
			"\3\uffff\1\45\1\uffff\1\46",
			"\1\32\2\uffff\1\34",
			"\1\32\2\uffff\1\34",
			"\1\47",
			"\1\32\2\uffff\1\34",
			"\1\32\2\uffff\1\34\2\uffff\1\46",
			"\1\32\2\uffff\1\34\2\uffff\1\46",
			"\1\32\2\uffff\1\34",
			"\1\32\2\uffff\1\34",
			"\1\46",
			"\1\51\1\uffff\1\50",
			"\1\44\2\uffff\1\41\2\uffff\1\42\1\uffff\1\40\1\43\7\uffff\1\45\1\uffff"+
			"\1\46",
			"\1\32\2\uffff\1\34",
			"\1\32\2\uffff\1\34"
	};

	static final short[] DFA18_eot = DFA.unpackEncodedString(DFA18_eotS);
	static final short[] DFA18_eof = DFA.unpackEncodedString(DFA18_eofS);
	static final char[] DFA18_min = DFA.unpackEncodedStringToUnsignedChars(DFA18_minS);
	static final char[] DFA18_max = DFA.unpackEncodedStringToUnsignedChars(DFA18_maxS);
	static final short[] DFA18_accept = DFA.unpackEncodedString(DFA18_acceptS);
	static final short[] DFA18_special = DFA.unpackEncodedString(DFA18_specialS);
	static final short[][] DFA18_transition;

	static {
		int numStates = DFA18_transitionS.length;
		DFA18_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA18_transition[i] = DFA.unpackEncodedString(DFA18_transitionS[i]);
		}
	}

	protected class DFA18 extends DFA {

		public DFA18(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 18;
			this.eot = DFA18_eot;
			this.eof = DFA18_eof;
			this.min = DFA18_min;
			this.max = DFA18_max;
			this.accept = DFA18_accept;
			this.special = DFA18_special;
			this.transition = DFA18_transition;
		}
		@Override
		public String getDescription() {
			return "()* loopback of 628:3: ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )*";
		}
	}

	static final String DFA30_eotS =
		"\11\uffff";
	static final String DFA30_eofS =
		"\1\3\6\uffff\1\4\1\uffff";
	static final String DFA30_minS =
		"\1\10\1\5\3\uffff\1\23\1\5\1\10\1\23";
	static final String DFA30_maxS =
		"\1\124\1\123\3\uffff\1\31\1\123\1\125\1\31";
	static final String DFA30_acceptS =
		"\2\uffff\1\2\1\3\1\1\4\uffff";
	static final String DFA30_specialS =
		"\11\uffff}>";
	static final String[] DFA30_transitionS = {
			"\1\3\11\uffff\1\1\13\uffff\1\3\4\uffff\2\3\6\uffff\1\3\3\uffff\1\3\6"+
			"\uffff\4\3\1\uffff\4\3\1\uffff\6\3\2\uffff\1\3\3\uffff\1\3\2\uffff\1"+
			"\3\2\uffff\1\2\1\uffff\1\3",
			"\2\4\1\uffff\1\5\1\4\2\uffff\1\4\1\uffff\2\4\3\uffff\1\4\3\uffff\1\4"+
			"\1\uffff\1\4\36\uffff\1\3\32\uffff\1\4",
			"",
			"",
			"",
			"\1\7\2\uffff\1\6\2\uffff\1\3",
			"\2\4\1\uffff\1\10\1\4\2\uffff\1\4\1\uffff\2\4\7\uffff\1\4\1\uffff\1"+
			"\4\36\uffff\1\3\32\uffff\1\4",
			"\1\4\11\uffff\1\4\2\uffff\1\3\2\uffff\1\3\5\uffff\1\4\4\uffff\2\4\6"+
			"\uffff\1\4\3\uffff\1\4\6\uffff\4\4\1\uffff\4\4\1\uffff\6\4\2\uffff\1"+
			"\4\3\uffff\1\4\2\uffff\1\4\4\uffff\1\4\1\3",
			"\1\7\2\uffff\1\6\2\uffff\1\3"
	};

	static final short[] DFA30_eot = DFA.unpackEncodedString(DFA30_eotS);
	static final short[] DFA30_eof = DFA.unpackEncodedString(DFA30_eofS);
	static final char[] DFA30_min = DFA.unpackEncodedStringToUnsignedChars(DFA30_minS);
	static final char[] DFA30_max = DFA.unpackEncodedStringToUnsignedChars(DFA30_maxS);
	static final short[] DFA30_accept = DFA.unpackEncodedString(DFA30_acceptS);
	static final short[] DFA30_special = DFA.unpackEncodedString(DFA30_specialS);
	static final short[][] DFA30_transition;

	static {
		int numStates = DFA30_transitionS.length;
		DFA30_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA30_transition[i] = DFA.unpackEncodedString(DFA30_transitionS[i]);
		}
	}

	protected class DFA30 extends DFA {

		public DFA30(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 30;
			this.eot = DFA30_eot;
			this.eof = DFA30_eof;
			this.min = DFA30_min;
			this.max = DFA30_max;
			this.accept = DFA30_accept;
			this.special = DFA30_special;
			this.transition = DFA30_transition;
		}
		@Override
		public String getDescription() {
			return "1103:4: ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )?";
		}
	}

	static final String DFA54_eotS =
		"\44\uffff";
	static final String DFA54_eofS =
		"\44\uffff";
	static final String DFA54_minS =
		"\1\10\1\uffff\1\10\3\uffff\1\26\2\uffff\1\22\1\uffff\1\6\1\40\5\23\1\31"+
		"\1\7\1\43\2\6\2\23\1\40\5\23\1\31\1\7\1\6\2\23";
	static final String DFA54_maxS =
		"\1\124\1\uffff\1\10\3\uffff\1\125\2\uffff\1\117\1\uffff\1\31\1\40\1\26"+
		"\2\31\2\26\1\31\1\11\1\117\2\31\2\26\1\40\1\26\2\31\2\26\1\31\1\11\1\31"+
		"\2\26";
	static final String DFA54_acceptS =
		"\1\uffff\1\7\1\uffff\1\1\1\2\1\3\1\uffff\1\5\1\6\1\uffff\1\4\31\uffff";
	static final String DFA54_specialS =
		"\44\uffff}>";
	static final String[] DFA54_transitionS = {
			"\1\6\11\uffff\1\7\20\uffff\1\2\1\5\6\uffff\1\5\14\uffff\1\7\1\5\4\uffff"+
			"\1\10\2\uffff\1\5\3\uffff\1\10\2\uffff\1\3\3\uffff\1\3\2\uffff\1\4\4"+
			"\uffff\1\1",
			"",
			"\1\11",
			"",
			"",
			"",
			"\1\7\1\uffff\2\7\6\uffff\1\12\64\uffff\1\7",
			"",
			"",
			"\1\13\20\uffff\1\2\1\5\6\uffff\1\5\15\uffff\1\5\4\uffff\1\10\2\uffff"+
			"\1\5\3\uffff\1\10\2\uffff\1\3\3\uffff\1\3\2\uffff\1\4",
			"",
			"\1\21\1\uffff\1\14\1\16\2\uffff\1\17\1\uffff\1\15\1\20\3\uffff\1\24"+
			"\3\uffff\1\22\1\uffff\1\23",
			"\1\25",
			"\1\24\2\uffff\1\26",
			"\1\24\2\uffff\1\26\2\uffff\1\23",
			"\1\24\2\uffff\1\26\2\uffff\1\23",
			"\1\24\2\uffff\1\26",
			"\1\24\2\uffff\1\26",
			"\1\23",
			"\1\30\1\uffff\1\27",
			"\1\2\1\5\6\uffff\1\5\15\uffff\1\5\4\uffff\1\10\2\uffff\1\5\3\uffff\1"+
			"\10\2\uffff\1\3\3\uffff\1\3\2\uffff\1\4",
			"\1\21\2\uffff\1\16\2\uffff\1\17\1\uffff\1\15\1\20\7\uffff\1\22\1\uffff"+
			"\1\23",
			"\1\36\1\uffff\1\31\1\33\2\uffff\1\34\1\uffff\1\32\1\35\3\uffff\1\24"+
			"\3\uffff\1\37\1\uffff\1\40",
			"\1\24\2\uffff\1\26",
			"\1\24\2\uffff\1\26",
			"\1\41",
			"\1\24\2\uffff\1\26",
			"\1\24\2\uffff\1\26\2\uffff\1\40",
			"\1\24\2\uffff\1\26\2\uffff\1\40",
			"\1\24\2\uffff\1\26",
			"\1\24\2\uffff\1\26",
			"\1\40",
			"\1\43\1\uffff\1\42",
			"\1\36\2\uffff\1\33\2\uffff\1\34\1\uffff\1\32\1\35\7\uffff\1\37\1\uffff"+
			"\1\40",
			"\1\24\2\uffff\1\26",
			"\1\24\2\uffff\1\26"
	};

	static final short[] DFA54_eot = DFA.unpackEncodedString(DFA54_eotS);
	static final short[] DFA54_eof = DFA.unpackEncodedString(DFA54_eofS);
	static final char[] DFA54_min = DFA.unpackEncodedStringToUnsignedChars(DFA54_minS);
	static final char[] DFA54_max = DFA.unpackEncodedStringToUnsignedChars(DFA54_maxS);
	static final short[] DFA54_accept = DFA.unpackEncodedString(DFA54_acceptS);
	static final short[] DFA54_special = DFA.unpackEncodedString(DFA54_specialS);
	static final short[][] DFA54_transition;

	static {
		int numStates = DFA54_transitionS.length;
		DFA54_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA54_transition[i] = DFA.unpackEncodedString(DFA54_transitionS[i]);
		}
	}

	protected class DFA54 extends DFA {

		public DFA54(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 54;
			this.eot = DFA54_eot;
			this.eof = DFA54_eof;
			this.min = DFA54_min;
			this.max = DFA54_max;
			this.accept = DFA54_accept;
			this.special = DFA54_special;
			this.transition = DFA54_transition;
		}
		@Override
		public String getDescription() {
			return "()* loopback of 1940:3: ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )*";
		}
	}

	static final String DFA103_eotS =
		"\36\uffff";
	static final String DFA103_eofS =
		"\36\uffff";
	static final String DFA103_minS =
		"\1\43\1\10\2\uffff\1\22\1\6\1\40\5\23\1\31\1\7\1\43\2\6\2\23\1\40\5\23"+
		"\1\31\1\7\1\6\2\23";
	static final String DFA103_maxS =
		"\1\101\1\10\2\uffff\1\101\1\31\1\40\1\26\2\31\2\26\1\31\1\11\1\101\2\31"+
		"\2\26\1\40\1\26\2\31\2\26\1\31\1\11\1\31\2\26";
	static final String DFA103_acceptS =
		"\2\uffff\1\1\1\2\32\uffff";
	static final String DFA103_specialS =
		"\36\uffff}>";
	static final String[] DFA103_transitionS = {
			"\1\1\1\3\6\uffff\1\3\13\uffff\1\2\1\uffff\1\3\3\uffff\1\2\2\uffff\1\2"+
			"\1\3",
			"\1\4",
			"",
			"",
			"\1\5\20\uffff\1\1\1\3\6\uffff\1\3\13\uffff\1\2\1\uffff\1\3\3\uffff\1"+
			"\2\2\uffff\1\2\1\3",
			"\1\13\1\uffff\1\6\1\10\2\uffff\1\11\1\uffff\1\7\1\12\3\uffff\1\16\3"+
			"\uffff\1\14\1\uffff\1\15",
			"\1\17",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20\2\uffff\1\15",
			"\1\16\2\uffff\1\20\2\uffff\1\15",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20",
			"\1\15",
			"\1\22\1\uffff\1\21",
			"\1\1\1\3\6\uffff\1\3\13\uffff\1\2\1\uffff\1\3\3\uffff\1\2\2\uffff\1"+
			"\2\1\3",
			"\1\13\2\uffff\1\10\2\uffff\1\11\1\uffff\1\7\1\12\7\uffff\1\14\1\uffff"+
			"\1\15",
			"\1\30\1\uffff\1\23\1\25\2\uffff\1\26\1\uffff\1\24\1\27\3\uffff\1\16"+
			"\3\uffff\1\31\1\uffff\1\32",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20",
			"\1\33",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20\2\uffff\1\32",
			"\1\16\2\uffff\1\20\2\uffff\1\32",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20",
			"\1\32",
			"\1\35\1\uffff\1\34",
			"\1\30\2\uffff\1\25\2\uffff\1\26\1\uffff\1\24\1\27\7\uffff\1\31\1\uffff"+
			"\1\32",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20"
	};

	static final short[] DFA103_eot = DFA.unpackEncodedString(DFA103_eotS);
	static final short[] DFA103_eof = DFA.unpackEncodedString(DFA103_eofS);
	static final char[] DFA103_min = DFA.unpackEncodedStringToUnsignedChars(DFA103_minS);
	static final char[] DFA103_max = DFA.unpackEncodedStringToUnsignedChars(DFA103_maxS);
	static final short[] DFA103_accept = DFA.unpackEncodedString(DFA103_acceptS);
	static final short[] DFA103_special = DFA.unpackEncodedString(DFA103_specialS);
	static final short[][] DFA103_transition;

	static {
		int numStates = DFA103_transitionS.length;
		DFA103_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA103_transition[i] = DFA.unpackEncodedString(DFA103_transitionS[i]);
		}
	}

	protected class DFA103 extends DFA {

		public DFA103(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 103;
			this.eot = DFA103_eot;
			this.eof = DFA103_eof;
			this.min = DFA103_min;
			this.max = DFA103_max;
			this.accept = DFA103_accept;
			this.special = DFA103_special;
			this.transition = DFA103_transition;
		}
		@Override
		public String getDescription() {
			return "3949:2: (this_Port_0= rulePort |this_Action_1= ruleAction )";
		}
	}

	static final String DFA121_eotS =
		"\14\uffff";
	static final String DFA121_eofS =
		"\2\uffff\1\1\2\uffff\1\7\6\uffff";
	static final String DFA121_minS =
		"\1\5\1\uffff\1\10\2\uffff\1\10\1\5\1\uffff\1\22\1\5\1\23\1\5";
	static final String DFA121_maxS =
		"\1\123\1\uffff\1\124\2\uffff\1\125\1\123\1\uffff\1\125\1\123\1\125\1\123";
	static final String DFA121_acceptS =
		"\1\uffff\1\1\1\uffff\1\3\1\4\2\uffff\1\2\4\uffff";
	static final String DFA121_specialS =
		"\14\uffff}>";
	static final String[] DFA121_transitionS = {
			"\2\1\1\uffff\1\3\1\2\2\uffff\1\1\1\uffff\2\1\7\uffff\1\1\1\uffff\1\1"+
			"\71\uffff\1\4",
			"",
			"\1\5\11\uffff\2\1\2\uffff\1\1\2\uffff\1\1\4\uffff\1\1\4\uffff\2\1\6"+
			"\uffff\1\1\3\uffff\1\1\6\uffff\4\1\1\uffff\4\1\1\uffff\6\1\2\uffff\2"+
			"\1\2\uffff\1\1\2\uffff\1\1\4\uffff\1\1",
			"",
			"",
			"\1\7\11\uffff\2\7\2\uffff\1\6\1\uffff\2\1\4\uffff\1\7\1\uffff\1\1\2"+
			"\uffff\2\7\6\uffff\1\7\3\uffff\1\7\6\uffff\4\7\1\uffff\4\7\1\uffff\6"+
			"\7\2\uffff\2\7\2\uffff\1\7\2\uffff\1\7\4\uffff\1\7\1\1",
			"\2\7\1\uffff\1\10\1\7\2\uffff\1\7\1\uffff\2\7\7\uffff\1\7\1\uffff\1"+
			"\7\36\uffff\1\1\32\uffff\1\7",
			"",
			"\2\7\2\uffff\1\11\1\uffff\2\1\6\uffff\1\7\61\uffff\1\7\1\uffff\1\7\1"+
			"\1",
			"\2\7\1\uffff\1\12\1\7\2\uffff\1\7\1\uffff\2\7\7\uffff\1\7\1\uffff\1"+
			"\7\36\uffff\1\1\32\uffff\1\7",
			"\1\7\2\uffff\1\13\1\uffff\2\1\72\uffff\1\7\1\1",
			"\2\7\1\uffff\1\12\1\7\2\uffff\1\7\1\uffff\2\7\7\uffff\1\7\1\uffff\1"+
			"\7\36\uffff\1\1\32\uffff\1\7"
	};

	static final short[] DFA121_eot = DFA.unpackEncodedString(DFA121_eotS);
	static final short[] DFA121_eof = DFA.unpackEncodedString(DFA121_eofS);
	static final char[] DFA121_min = DFA.unpackEncodedStringToUnsignedChars(DFA121_minS);
	static final char[] DFA121_max = DFA.unpackEncodedStringToUnsignedChars(DFA121_maxS);
	static final short[] DFA121_accept = DFA.unpackEncodedString(DFA121_acceptS);
	static final short[] DFA121_special = DFA.unpackEncodedString(DFA121_specialS);
	static final short[][] DFA121_transition;

	static {
		int numStates = DFA121_transitionS.length;
		DFA121_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA121_transition[i] = DFA.unpackEncodedString(DFA121_transitionS[i]);
		}
	}

	protected class DFA121 extends DFA {

		public DFA121(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 121;
			this.eot = DFA121_eot;
			this.eof = DFA121_eof;
			this.min = DFA121_min;
			this.max = DFA121_max;
			this.accept = DFA121_accept;
			this.special = DFA121_special;
			this.transition = DFA121_transition;
		}
		@Override
		public String getDescription() {
			return "4670:2: ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) |this_Time_2= ruleTime |this_ParameterReference_3= ruleParameterReference |this_Code_4= ruleCode )";
		}
	}

	static final String DFA122_eotS =
		"\36\uffff";
	static final String DFA122_eofS =
		"\36\uffff";
	static final String DFA122_minS =
		"\1\43\1\10\2\uffff\1\22\1\6\1\40\5\23\1\31\1\7\1\43\2\6\2\23\1\40\5\23"+
		"\1\31\1\7\1\6\2\23";
	static final String DFA122_maxS =
		"\1\100\1\10\2\uffff\1\100\1\31\1\40\1\26\2\31\2\26\1\31\1\11\1\100\2\31"+
		"\2\26\1\40\1\26\2\31\2\26\1\31\1\11\1\31\2\26";
	static final String DFA122_acceptS =
		"\2\uffff\1\1\1\2\32\uffff";
	static final String DFA122_specialS =
		"\36\uffff}>";
	static final String[] DFA122_transitionS = {
			"\1\1\23\uffff\1\2\5\uffff\1\2\2\uffff\1\3",
			"\1\4",
			"",
			"",
			"\1\5\20\uffff\1\1\23\uffff\1\2\5\uffff\1\2\2\uffff\1\3",
			"\1\13\1\uffff\1\6\1\10\2\uffff\1\11\1\uffff\1\7\1\12\3\uffff\1\16\3"+
			"\uffff\1\14\1\uffff\1\15",
			"\1\17",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20\2\uffff\1\15",
			"\1\16\2\uffff\1\20\2\uffff\1\15",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20",
			"\1\15",
			"\1\22\1\uffff\1\21",
			"\1\1\23\uffff\1\2\5\uffff\1\2\2\uffff\1\3",
			"\1\13\2\uffff\1\10\2\uffff\1\11\1\uffff\1\7\1\12\7\uffff\1\14\1\uffff"+
			"\1\15",
			"\1\30\1\uffff\1\23\1\25\2\uffff\1\26\1\uffff\1\24\1\27\3\uffff\1\16"+
			"\3\uffff\1\31\1\uffff\1\32",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20",
			"\1\33",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20\2\uffff\1\32",
			"\1\16\2\uffff\1\20\2\uffff\1\32",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20",
			"\1\32",
			"\1\35\1\uffff\1\34",
			"\1\30\2\uffff\1\25\2\uffff\1\26\1\uffff\1\24\1\27\7\uffff\1\31\1\uffff"+
			"\1\32",
			"\1\16\2\uffff\1\20",
			"\1\16\2\uffff\1\20"
	};

	static final short[] DFA122_eot = DFA.unpackEncodedString(DFA122_eotS);
	static final short[] DFA122_eof = DFA.unpackEncodedString(DFA122_eofS);
	static final char[] DFA122_min = DFA.unpackEncodedStringToUnsignedChars(DFA122_minS);
	static final char[] DFA122_max = DFA.unpackEncodedStringToUnsignedChars(DFA122_maxS);
	static final short[] DFA122_accept = DFA.unpackEncodedString(DFA122_acceptS);
	static final short[] DFA122_special = DFA.unpackEncodedString(DFA122_specialS);
	static final short[][] DFA122_transition;

	static {
		int numStates = DFA122_transitionS.length;
		DFA122_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA122_transition[i] = DFA.unpackEncodedString(DFA122_transitionS[i]);
		}
	}

	protected class DFA122 extends DFA {

		public DFA122(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 122;
			this.eot = DFA122_eot;
			this.eof = DFA122_eof;
			this.min = DFA122_min;
			this.max = DFA122_max;
			this.accept = DFA122_accept;
			this.special = DFA122_special;
			this.transition = DFA122_transition;
		}
		@Override
		public String getDescription() {
			return "4830:2: (this_Input_0= ruleInput |this_Output_1= ruleOutput )";
		}
	}

	static final String DFA137_eotS =
		"\7\uffff";
	static final String DFA137_eofS =
		"\1\uffff\2\5\3\uffff\1\5";
	static final String DFA137_minS =
		"\1\10\2\27\1\10\2\uffff\1\27";
	static final String DFA137_maxS =
		"\1\101\2\122\1\10\2\uffff\1\122";
	static final String DFA137_acceptS =
		"\4\uffff\1\1\1\2\1\uffff";
	static final String DFA137_specialS =
		"\7\uffff}>";
	static final String[] DFA137_transitionS = {
			"\1\1\70\uffff\1\2",
			"\1\3\1\uffff\1\5\1\uffff\1\5\2\uffff\1\5\4\uffff\1\4\15\uffff\1\5\40"+
			"\uffff\1\5",
			"\1\3\1\uffff\1\5\1\uffff\1\5\2\uffff\1\5\4\uffff\1\4\15\uffff\1\5\40"+
			"\uffff\1\5",
			"\1\6",
			"",
			"",
			"\1\3\1\uffff\1\5\1\uffff\1\5\2\uffff\1\5\4\uffff\1\4\15\uffff\1\5\40"+
			"\uffff\1\5"
	};

	static final short[] DFA137_eot = DFA.unpackEncodedString(DFA137_eotS);
	static final short[] DFA137_eof = DFA.unpackEncodedString(DFA137_eofS);
	static final char[] DFA137_min = DFA.unpackEncodedStringToUnsignedChars(DFA137_minS);
	static final char[] DFA137_max = DFA.unpackEncodedStringToUnsignedChars(DFA137_maxS);
	static final short[] DFA137_accept = DFA.unpackEncodedString(DFA137_acceptS);
	static final short[] DFA137_special = DFA.unpackEncodedString(DFA137_specialS);
	static final short[][] DFA137_transition;

	static {
		int numStates = DFA137_transitionS.length;
		DFA137_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA137_transition[i] = DFA.unpackEncodedString(DFA137_transitionS[i]);
		}
	}

	protected class DFA137 extends DFA {

		public DFA137(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 137;
			this.eot = DFA137_eot;
			this.eof = DFA137_eof;
			this.min = DFA137_min;
			this.max = DFA137_max;
			this.accept = DFA137_accept;
			this.special = DFA137_special;
			this.transition = DFA137_transition;
		}
		@Override
		public String getDescription() {
			return "5487:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )?";
		}
	}

	static final String DFA139_eotS =
		"\11\uffff";
	static final String DFA139_eofS =
		"\1\uffff\2\7\5\uffff\1\7";
	static final String DFA139_minS =
		"\1\10\2\27\2\uffff\2\10\1\uffff\1\27";
	static final String DFA139_maxS =
		"\1\101\2\122\2\uffff\1\10\1\101\1\uffff\1\122";
	static final String DFA139_acceptS =
		"\3\uffff\1\1\1\2\2\uffff\1\3\1\uffff";
	static final String DFA139_specialS =
		"\11\uffff}>";
	static final String[] DFA139_transitionS = {
			"\1\1\1\3\34\uffff\1\4\32\uffff\1\2",
			"\1\5\1\uffff\1\7\1\uffff\1\7\2\uffff\1\7\4\uffff\1\6\15\uffff\1\7\40"+
			"\uffff\1\7",
			"\1\5\1\uffff\1\7\1\uffff\1\7\2\uffff\1\7\4\uffff\1\6\15\uffff\1\7\40"+
			"\uffff\1\7",
			"",
			"",
			"\1\10",
			"\1\7\1\3\67\uffff\1\7",
			"",
			"\1\5\1\uffff\1\7\1\uffff\1\7\2\uffff\1\7\4\uffff\1\6\15\uffff\1\7\40"+
			"\uffff\1\7"
	};

	static final short[] DFA139_eot = DFA.unpackEncodedString(DFA139_eotS);
	static final short[] DFA139_eof = DFA.unpackEncodedString(DFA139_eofS);
	static final char[] DFA139_min = DFA.unpackEncodedStringToUnsignedChars(DFA139_minS);
	static final char[] DFA139_max = DFA.unpackEncodedStringToUnsignedChars(DFA139_maxS);
	static final short[] DFA139_accept = DFA.unpackEncodedString(DFA139_acceptS);
	static final short[] DFA139_special = DFA.unpackEncodedString(DFA139_specialS);
	static final short[][] DFA139_transition;

	static {
		int numStates = DFA139_transitionS.length;
		DFA139_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA139_transition[i] = DFA.unpackEncodedString(DFA139_transitionS[i]);
		}
	}

	protected class DFA139 extends DFA {

		public DFA139(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 139;
			this.eot = DFA139_eot;
			this.eof = DFA139_eof;
			this.min = DFA139_min;
			this.max = DFA139_max;
			this.accept = DFA139_accept;
			this.special = DFA139_special;
			this.transition = DFA139_transition;
		}
		@Override
		public String getDescription() {
			return "5573:2: (this_IPV4Host_0= ruleIPV4Host |this_IPV6Host_1= ruleIPV6Host |this_NamedHost_2= ruleNamedHost )";
		}
	}

	static final String DFA159_eotS =
		"\35\uffff";
	static final String DFA159_eofS =
		"\1\uffff\1\4\3\uffff\2\13\2\20\1\uffff\1\20\3\uffff\2\20\1\uffff\3\20"+
		"\1\13\1\uffff\1\20\3\uffff\2\20\1\13";
	static final String DFA159_minS =
		"\3\10\1\33\1\uffff\1\10\1\33\2\10\1\33\1\10\2\uffff\2\10\1\33\1\uffff"+
		"\2\10\1\21\1\10\1\uffff\1\10\1\uffff\1\10\1\uffff\1\10\1\21\1\10";
	static final String DFA159_maxS =
		"\1\34\1\51\2\34\1\uffff\4\51\1\34\1\51\2\uffff\1\11\2\51\1\uffff\4\51"+
		"\1\uffff\1\51\1\uffff\1\11\1\uffff\3\51";
	static final String DFA159_acceptS =
		"\4\uffff\1\1\6\uffff\1\2\1\5\3\uffff\1\3\4\uffff\1\7\1\uffff\1\4\1\uffff"+
		"\1\6\3\uffff";
	static final String DFA159_specialS =
		"\35\uffff}>";
	static final String[] DFA159_transitionS = {
			"\1\3\1\2\22\uffff\1\1",
			"\1\6\1\5\37\uffff\1\4",
			"\1\11\22\uffff\1\7\1\10",
			"\1\7\1\12",
			"",
			"\1\13\20\uffff\1\14\1\uffff\1\13\15\uffff\1\13",
			"\1\15\15\uffff\1\13",
			"\1\17\1\16\37\uffff\1\20",
			"\1\20\1\21\37\uffff\1\20",
			"\1\7\1\10",
			"\1\23\1\22\37\uffff\1\20",
			"",
			"",
			"\1\13\1\24",
			"\1\17\20\uffff\1\25\1\uffff\1\7\1\10\14\uffff\1\20",
			"\1\7\1\10\14\uffff\1\20",
			"",
			"\1\20\20\uffff\1\25\1\uffff\2\20\14\uffff\1\20",
			"\1\23\10\uffff\1\27\7\uffff\1\25\1\uffff\1\26\1\20\14\uffff\1\20",
			"\1\27\11\uffff\1\26\1\20\14\uffff\1\20",
			"\1\13\20\uffff\1\31\1\uffff\1\30\15\uffff\1\13",
			"",
			"\1\33\1\32\37\uffff\1\20",
			"",
			"\1\13\1\34",
			"",
			"\1\33\10\uffff\1\27\11\uffff\1\26\1\20\14\uffff\1\20",
			"\1\27\11\uffff\1\26\1\20\14\uffff\1\20",
			"\1\13\20\uffff\1\31\1\uffff\1\13\15\uffff\1\13"
	};

	static final short[] DFA159_eot = DFA.unpackEncodedString(DFA159_eotS);
	static final short[] DFA159_eof = DFA.unpackEncodedString(DFA159_eofS);
	static final char[] DFA159_min = DFA.unpackEncodedStringToUnsignedChars(DFA159_minS);
	static final char[] DFA159_max = DFA.unpackEncodedStringToUnsignedChars(DFA159_maxS);
	static final short[] DFA159_accept = DFA.unpackEncodedString(DFA159_acceptS);
	static final short[] DFA159_special = DFA.unpackEncodedString(DFA159_specialS);
	static final short[][] DFA159_transition;

	static {
		int numStates = DFA159_transitionS.length;
		DFA159_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA159_transition[i] = DFA.unpackEncodedString(DFA159_transitionS[i]);
		}
	}

	protected class DFA159 extends DFA {

		public DFA159(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 159;
			this.eot = DFA159_eot;
			this.eof = DFA159_eof;
			this.min = DFA159_min;
			this.max = DFA159_max;
			this.accept = DFA159_accept;
			this.special = DFA159_special;
			this.transition = DFA159_transition;
		}
		@Override
		public String getDescription() {
			return "5968:2: (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' |kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT |this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) )";
		}
	}

	static final String DFA158_eotS =
		"\10\uffff";
	static final String DFA158_eofS =
		"\10\uffff";
	static final String DFA158_minS =
		"\2\10\1\33\1\10\1\uffff\1\10\1\33\1\uffff";
	static final String DFA158_maxS =
		"\1\11\2\34\1\11\1\uffff\2\34\1\uffff";
	static final String DFA158_acceptS =
		"\4\uffff\1\1\2\uffff\1\2";
	static final String DFA158_specialS =
		"\10\uffff}>";
	static final String[] DFA158_transitionS = {
			"\1\2\1\1",
			"\1\2\22\uffff\1\3\1\4",
			"\1\3\1\4",
			"\1\6\1\5",
			"",
			"\1\6\20\uffff\1\7\1\uffff\1\3\1\4",
			"\1\3\1\4",
			""
	};

	static final short[] DFA158_eot = DFA.unpackEncodedString(DFA158_eotS);
	static final short[] DFA158_eof = DFA.unpackEncodedString(DFA158_eofS);
	static final char[] DFA158_min = DFA.unpackEncodedStringToUnsignedChars(DFA158_minS);
	static final char[] DFA158_max = DFA.unpackEncodedStringToUnsignedChars(DFA158_maxS);
	static final short[] DFA158_accept = DFA.unpackEncodedString(DFA158_acceptS);
	static final short[] DFA158_special = DFA.unpackEncodedString(DFA158_specialS);
	static final short[][] DFA158_transition;

	static {
		int numStates = DFA158_transitionS.length;
		DFA158_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA158_transition[i] = DFA.unpackEncodedString(DFA158_transitionS[i]);
		}
	}

	protected class DFA158 extends DFA {

		public DFA158(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 158;
			this.eot = DFA158_eot;
			this.eof = DFA158_eof;
			this.min = DFA158_min;
			this.max = DFA158_max;
			this.accept = DFA158_accept;
			this.special = DFA158_special;
			this.transition = DFA158_transition;
		}
		@Override
		public String getDescription() {
			return "6177:4: ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) )";
		}
	}

	static final String DFA163_eotS =
		"\6\uffff";
	static final String DFA163_eofS =
		"\1\uffff\3\4\2\uffff";
	static final String DFA163_minS =
		"\4\10\2\uffff";
	static final String DFA163_maxS =
		"\1\52\3\124\2\uffff";
	static final String DFA163_acceptS =
		"\4\uffff\1\2\1\1";
	static final String DFA163_specialS =
		"\6\uffff}>";
	static final String[] DFA163_transitionS = {
			"\1\1\20\uffff\1\2\1\4\15\uffff\1\4\1\uffff\1\3",
			"\1\1\15\uffff\1\4\2\uffff\1\2\1\4\2\uffff\1\5\12\uffff\2\4\1\3\51\uffff"+
			"\1\4",
			"\1\1\15\uffff\1\4\2\uffff\1\2\1\4\2\uffff\1\5\12\uffff\2\4\1\3\51\uffff"+
			"\1\4",
			"\1\1\15\uffff\1\4\2\uffff\1\2\1\4\2\uffff\1\5\12\uffff\2\4\1\3\51\uffff"+
			"\1\4",
			"",
			""
	};

	static final short[] DFA163_eot = DFA.unpackEncodedString(DFA163_eotS);
	static final short[] DFA163_eof = DFA.unpackEncodedString(DFA163_eofS);
	static final char[] DFA163_min = DFA.unpackEncodedStringToUnsignedChars(DFA163_minS);
	static final char[] DFA163_max = DFA.unpackEncodedStringToUnsignedChars(DFA163_maxS);
	static final short[] DFA163_accept = DFA.unpackEncodedString(DFA163_acceptS);
	static final short[] DFA163_special = DFA.unpackEncodedString(DFA163_specialS);
	static final short[][] DFA163_transition;

	static {
		int numStates = DFA163_transitionS.length;
		DFA163_transition = new short[numStates][];
		for (int i=0; i<numStates; i++) {
			DFA163_transition[i] = DFA.unpackEncodedString(DFA163_transitionS[i]);
		}
	}

	protected class DFA163 extends DFA {

		public DFA163(BaseRecognizer recognizer) {
			this.recognizer = recognizer;
			this.decisionNumber = 163;
			this.eot = DFA163_eot;
			this.eof = DFA163_eof;
			this.min = DFA163_min;
			this.max = DFA163_max;
			this.accept = DFA163_accept;
			this.special = DFA163_special;
			this.transition = DFA163_transition;
		}
		@Override
		public String getDescription() {
			return "6430:3: (this_FSName_0= ruleFSName kw= ':\\\\' )?";
		}
	}

	public static final BitSet FOLLOW_ruleModel_in_entryRuleModel66 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleModel72 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTargetDecl_in_ruleModel118 = new BitSet(new long[]{0x0424001800000000L,0x00000000000000DCL});
	public static final BitSet FOLLOW_ruleImport_in_ruleModel156 = new BitSet(new long[]{0x0424001800000000L,0x00000000000000DCL});
	public static final BitSet FOLLOW_rulePreamble_in_ruleModel195 = new BitSet(new long[]{0x0404001800000000L,0x00000000000000DCL});
	public static final BitSet FOLLOW_ruleReactor_in_ruleModel234 = new BitSet(new long[]{0x0404000800000002L,0x00000000000000C0L});
	public static final BitSet FOLLOW_ruleImport_in_entryRuleImport272 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleImport278 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_53_in_ruleImport307 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ruleImportedReactor_in_ruleImport334 = new BitSet(new long[]{0x0008000000400000L});
	public static final BitSet FOLLOW_22_in_ruleImport360 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ruleImportedReactor_in_ruleImport392 = new BitSet(new long[]{0x0008000000400000L});
	public static final BitSet FOLLOW_51_in_ruleImport421 = new BitSet(new long[]{0x0000000000004000L});
	public static final BitSet FOLLOW_RULE_STRING_in_ruleImport442 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleImport474 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleImportedReactor_in_entryRuleImportedReactor506 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleImportedReactor512 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleImportedReactor558 = new BitSet(new long[]{0x0000200000000002L});
	public static final BitSet FOLLOW_45_in_ruleImportedReactor584 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleImportedReactor609 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleReactor_in_entryRuleReactor661 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleReactor667 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleReactor726 = new BitSet(new long[]{0x0404000800000000L,0x00000000000000C0L});
	public static final BitSet FOLLOW_50_in_ruleReactor829 = new BitSet(new long[]{0x0404000000000000L,0x00000000000000C0L});
	public static final BitSet FOLLOW_58_in_ruleReactor923 = new BitSet(new long[]{0x0404000000000000L,0x00000000000000C0L});
	public static final BitSet FOLLOW_71_in_ruleReactor1045 = new BitSet(new long[]{0x0404000000000000L,0x00000000000000C0L});
	public static final BitSet FOLLOW_70_in_ruleReactor1141 = new BitSet(new long[]{0x0002400080040100L,0x0000000000040000L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleReactor1162 = new BitSet(new long[]{0x0002400080040000L,0x0000000000040000L});
	public static final BitSet FOLLOW_31_in_ruleReactor1195 = new BitSet(new long[]{0x0000000000000100L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleTypeParm_in_ruleReactor1227 = new BitSet(new long[]{0x0000000400400000L});
	public static final BitSet FOLLOW_22_in_ruleReactor1258 = new BitSet(new long[]{0x0000000000000100L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleTypeParm_in_ruleReactor1295 = new BitSet(new long[]{0x0000000400400000L});
	public static final BitSet FOLLOW_34_in_ruleReactor1329 = new BitSet(new long[]{0x0002400000040000L,0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleReactor1350 = new BitSet(new long[]{0x0000000800000100L});
	public static final BitSet FOLLOW_ruleParameter_in_ruleReactor1382 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleReactor1413 = new BitSet(new long[]{0x0000000800000100L});
	public static final BitSet FOLLOW_ruleParameter_in_ruleReactor1450 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleReactor1484 = new BitSet(new long[]{0x0002400000000000L,0x0000000000040000L});
	public static final BitSet FOLLOW_46_in_ruleReactor1505 = new BitSet(new long[]{0x0000004000000300L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleHost_in_ruleReactor1537 = new BitSet(new long[]{0x0002000000000000L,0x0000000000040000L});
	public static final BitSet FOLLOW_49_in_ruleReactor1571 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleReactor1612 = new BitSet(new long[]{0x0000000000400000L,0x0000000000040000L});
	public static final BitSet FOLLOW_22_in_ruleReactor1648 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleReactor1690 = new BitSet(new long[]{0x0000000000400000L,0x0000000000040000L});
	public static final BitSet FOLLOW_82_in_ruleReactor1737 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_rulePreamble_in_ruleReactor1772 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleStateVar_in_ruleReactor1826 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleMethod_in_ruleReactor1880 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleInput_in_ruleReactor1934 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleOutput_in_ruleReactor1988 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleTimer_in_ruleReactor2042 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleAction_in_ruleReactor2096 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleInstantiation_in_ruleReactor2150 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleConnection_in_ruleReactor2204 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleReaction_in_ruleReactor2258 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_ruleMode_in_ruleReactor2312 = new BitSet(new long[]{0x7BC0881800040100L,0x000000000010913FL});
	public static final BitSet FOLLOW_84_in_ruleReactor2341 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTypeParm_in_entryRuleTypeParm2367 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTypeParm2373 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTypeExpr_in_ruleTypeParm2419 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleCode_in_ruleTypeParm2465 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTypeExpr_in_entryRuleTypeExpr2502 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTypeExpr2508 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleTypeExpr2537 = new BitSet(new long[]{0x0000000000000102L});
	public static final BitSet FOLLOW_ruleTargetDecl_in_entryRuleTargetDecl2568 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTargetDecl2574 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_77_in_ruleTargetDecl2603 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleTargetDecl2624 = new BitSet(new long[]{0x0000000040000002L,0x0000000000040000L});
	public static final BitSet FOLLOW_ruleKeyValuePairs_in_ruleTargetDecl2668 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleTargetDecl2695 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleStateVar_in_entryRuleStateVar2727 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleStateVar2733 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleStateVar2779 = new BitSet(new long[]{0x0000000800000000L,0x0000000000001100L});
	public static final BitSet FOLLOW_72_in_ruleStateVar2812 = new BitSet(new long[]{0x0000000000000000L,0x0000000000001000L});
	public static final BitSet FOLLOW_76_in_ruleStateVar2840 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleStateVar2861 = new BitSet(new long[]{0x0000000048040002L,0x0000000000040000L});
	public static final BitSet FOLLOW_27_in_ruleStateVar2899 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleStateVar2936 = new BitSet(new long[]{0x0000000040040002L,0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleStateVar3000 = new BitSet(new long[]{0x000000000288D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleStateVar3079 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleStateVar3125 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleStateVar3177 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleStateVar3250 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_82_in_ruleStateVar3331 = new BitSet(new long[]{0x000000000280D360L,0x0000000000180000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleStateVar3410 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_22_in_ruleStateVar3456 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleStateVar3508 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_84_in_ruleStateVar3581 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleStateVar3641 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleMethod_in_entryRuleMethod3673 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleMethod3679 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_47_in_ruleMethod3719 = new BitSet(new long[]{0x0800000000000000L});
	public static final BitSet FOLLOW_59_in_ruleMethod3747 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleMethod3768 = new BitSet(new long[]{0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleMethod3795 = new BitSet(new long[]{0x0000000000080100L});
	public static final BitSet FOLLOW_ruleMethodArgument_in_ruleMethod3830 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleMethod3861 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ruleMethodArgument_in_ruleMethod3898 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleMethod3936 = new BitSet(new long[]{0x0000000008000000L,0x0000000000080000L});
	public static final BitSet FOLLOW_27_in_ruleMethod3951 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleMethod3983 = new BitSet(new long[]{0x0000000000000000L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleCode_in_ruleMethod4029 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleMethod4055 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleMethodArgument_in_entryRuleMethodArgument4087 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleMethodArgument4093 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleMethodArgument4133 = new BitSet(new long[]{0x0000000008000002L});
	public static final BitSet FOLLOW_27_in_ruleMethodArgument4165 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleMethodArgument4197 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleInput_in_entryRuleInput4242 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleInput4248 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleInput4294 = new BitSet(new long[]{0x2080000800000000L});
	public static final BitSet FOLLOW_61_in_ruleInput4327 = new BitSet(new long[]{0x0080000000000000L});
	public static final BitSet FOLLOW_55_in_ruleInput4355 = new BitSet(new long[]{0x0000004000000100L});
	public static final BitSet FOLLOW_ruleWidthSpec_in_ruleInput4382 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleInput4415 = new BitSet(new long[]{0x0000000048000002L});
	public static final BitSet FOLLOW_27_in_ruleInput4447 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleInput4479 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleInput4513 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleOutput_in_entryRuleOutput4545 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleOutput4551 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleOutput4597 = new BitSet(new long[]{0x0000000800000000L,0x0000000000000001L});
	public static final BitSet FOLLOW_64_in_ruleOutput4619 = new BitSet(new long[]{0x0000004000000100L});
	public static final BitSet FOLLOW_ruleWidthSpec_in_ruleOutput4646 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleOutput4679 = new BitSet(new long[]{0x0000000048000002L});
	public static final BitSet FOLLOW_27_in_ruleOutput4711 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleOutput4743 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleOutput4777 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTimer_in_entryRuleTimer4809 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTimer4815 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleTimer4861 = new BitSet(new long[]{0x0000000800000000L,0x0000000000008000L});
	public static final BitSet FOLLOW_79_in_ruleTimer4883 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleTimer4904 = new BitSet(new long[]{0x0000000040040002L});
	public static final BitSet FOLLOW_18_in_ruleTimer4936 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleTimer4968 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleTimer4999 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleTimer5036 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleTimer5070 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleTimer5091 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBoolean_in_entryRuleBoolean5123 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleBoolean5129 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_TRUE_in_ruleBoolean5158 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_FALSE_in_ruleBoolean5180 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleMode_in_entryRuleMode5210 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleMode5216 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_54_in_ruleMode5269 = new BitSet(new long[]{0x1000000000000000L});
	public static final BitSet FOLLOW_60_in_ruleMode5297 = new BitSet(new long[]{0x0000000000000100L,0x0000000000040000L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleMode5318 = new BitSet(new long[]{0x0000000000000000L,0x0000000000040000L});
	public static final BitSet FOLLOW_82_in_ruleMode5346 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_ruleStateVar_in_ruleMode5381 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_ruleTimer_in_ruleMode5435 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_ruleAction_in_ruleMode5489 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_ruleInstantiation_in_ruleMode5543 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_ruleConnection_in_ruleMode5597 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_ruleReaction_in_ruleMode5651 = new BitSet(new long[]{0x4300081800040100L,0x0000000000109122L});
	public static final BitSet FOLLOW_84_in_ruleMode5680 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAction_in_entryRuleAction5706 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleAction5712 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleAction5758 = new BitSet(new long[]{0x0200081800000000L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleActionOrigin_in_ruleAction5797 = new BitSet(new long[]{0x0000080000000000L});
	public static final BitSet FOLLOW_43_in_ruleAction5819 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleAction5840 = new BitSet(new long[]{0x0000000048040002L});
	public static final BitSet FOLLOW_18_in_ruleAction5872 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAction5904 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleAction5935 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAction5972 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleAction6008 = new BitSet(new long[]{0x0000000000004000L});
	public static final BitSet FOLLOW_RULE_STRING_in_ruleAction6041 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleAction6094 = new BitSet(new long[]{0x0000000048000002L});
	public static final BitSet FOLLOW_27_in_ruleAction6115 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleAction6147 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleAction6181 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleReaction_in_entryRuleReaction6213 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleReaction6219 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleReaction6265 = new BitSet(new long[]{0x4000000800000000L,0x0000000000000020L});
	public static final BitSet FOLLOW_69_in_ruleReaction6292 = new BitSet(new long[]{0x0100000001040100L,0x0000000000080000L});
	public static final BitSet FOLLOW_62_in_ruleReaction6326 = new BitSet(new long[]{0x0100000001040100L,0x0000000000080000L});
	public static final BitSet FOLLOW_18_in_ruleReaction6366 = new BitSet(new long[]{0x0100000000080100L,0x0000000000000D00L});
	public static final BitSet FOLLOW_ruleTriggerRef_in_ruleReaction6407 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleReaction6443 = new BitSet(new long[]{0x0100000000000100L,0x0000000000000D00L});
	public static final BitSet FOLLOW_ruleTriggerRef_in_ruleReaction6485 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleReaction6529 = new BitSet(new long[]{0x0100000001000100L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleReaction6570 = new BitSet(new long[]{0x0000000001400000L,0x0000000000080000L});
	public static final BitSet FOLLOW_22_in_ruleReaction6601 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleReaction6638 = new BitSet(new long[]{0x0000000001400000L,0x0000000000080000L});
	public static final BitSet FOLLOW_24_in_ruleReaction6681 = new BitSet(new long[]{0x0110000000000100L,0x0000000000000100L});
	public static final BitSet FOLLOW_ruleVarRefOrModeTransition_in_ruleReaction6713 = new BitSet(new long[]{0x0000000000400000L,0x0000000000080000L});
	public static final BitSet FOLLOW_22_in_ruleReaction6744 = new BitSet(new long[]{0x0110000000000100L,0x0000000000000100L});
	public static final BitSet FOLLOW_ruleVarRefOrModeTransition_in_ruleReaction6781 = new BitSet(new long[]{0x0000000000400000L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleCode_in_ruleReaction6836 = new BitSet(new long[]{0x0001002000000002L});
	public static final BitSet FOLLOW_ruleSTP_in_ruleReaction6874 = new BitSet(new long[]{0x0001000000000002L});
	public static final BitSet FOLLOW_ruleDeadline_in_ruleReaction6913 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTriggerRef_in_entryRuleTriggerRef6951 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTriggerRef6957 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBuiltinTriggerRef_in_ruleTriggerRef6990 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleTriggerRef7012 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBuiltinTriggerRef_in_entryRuleBuiltinTriggerRef7038 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleBuiltinTriggerRef7044 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBuiltinTrigger_in_ruleBuiltinTriggerRef7083 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleDeadline_in_entryRuleDeadline7114 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleDeadline7120 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_48_in_ruleDeadline7149 = new BitSet(new long[]{0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleDeadline7159 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleDeadline7186 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleDeadline7207 = new BitSet(new long[]{0x0000000000000000L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleCode_in_ruleDeadline7234 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSTP_in_entryRuleSTP7271 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleSTP7277 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_37_in_ruleSTP7306 = new BitSet(new long[]{0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleSTP7316 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleSTP7343 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleSTP7364 = new BitSet(new long[]{0x0000000000000000L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleCode_in_ruleSTP7391 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_rulePreamble_in_entryRulePreamble7428 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRulePreamble7434 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleVisibility_in_rulePreamble7480 = new BitSet(new long[]{0x0000000000000000L,0x0000000000000004L});
	public static final BitSet FOLLOW_66_in_rulePreamble7502 = new BitSet(new long[]{0x0000000000000000L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleCode_in_rulePreamble7529 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleInstantiation_in_entryRuleInstantiation7566 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleInstantiation7572 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleInstantiation7612 = new BitSet(new long[]{0x0000000100000000L});
	public static final BitSet FOLLOW_32_in_ruleInstantiation7639 = new BitSet(new long[]{0x8000000000000000L});
	public static final BitSet FOLLOW_63_in_ruleInstantiation7649 = new BitSet(new long[]{0x0000004000000100L});
	public static final BitSet FOLLOW_ruleWidthSpec_in_ruleInstantiation7676 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleInstantiation7715 = new BitSet(new long[]{0x0000000080040000L});
	public static final BitSet FOLLOW_31_in_ruleInstantiation7741 = new BitSet(new long[]{0x0000000000000100L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleTypeParm_in_ruleInstantiation7773 = new BitSet(new long[]{0x0000000400400000L});
	public static final BitSet FOLLOW_22_in_ruleInstantiation7804 = new BitSet(new long[]{0x0000000000000100L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleTypeParm_in_ruleInstantiation7841 = new BitSet(new long[]{0x0000000400400000L});
	public static final BitSet FOLLOW_34_in_ruleInstantiation7875 = new BitSet(new long[]{0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleInstantiation7891 = new BitSet(new long[]{0x0000000000080100L});
	public static final BitSet FOLLOW_ruleAssignment_in_ruleInstantiation7926 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleInstantiation7957 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ruleAssignment_in_ruleInstantiation7994 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleInstantiation8032 = new BitSet(new long[]{0x0000400040000002L});
	public static final BitSet FOLLOW_46_in_ruleInstantiation8053 = new BitSet(new long[]{0x0000004000000300L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleHost_in_ruleInstantiation8090 = new BitSet(new long[]{0x0000000040000000L});
	public static final BitSet FOLLOW_30_in_ruleInstantiation8119 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_30_in_ruleInstantiation8152 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleConnection_in_entryRuleConnection8190 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleConnection8196 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleConnection8259 = new BitSet(new long[]{0x0000000001400000L,0x0000000000200000L});
	public static final BitSet FOLLOW_22_in_ruleConnection8295 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleConnection8337 = new BitSet(new long[]{0x0000000001400000L,0x0000000000200000L});
	public static final BitSet FOLLOW_18_in_ruleConnection8395 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleConnection8432 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleConnection8468 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleConnection8510 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleConnection8549 = new BitSet(new long[]{0x0000000001200000L,0x0000000000200000L});
	public static final BitSet FOLLOW_21_in_ruleConnection8578 = new BitSet(new long[]{0x0000000001000000L,0x0000000000200000L});
	public static final BitSet FOLLOW_24_in_ruleConnection8628 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_85_in_ruleConnection8662 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleConnection8714 = new BitSet(new long[]{0x0000100040400002L,0x0000000000000200L});
	public static final BitSet FOLLOW_22_in_ruleConnection8740 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleConnection8772 = new BitSet(new long[]{0x0000100040400002L,0x0000000000000200L});
	public static final BitSet FOLLOW_44_in_ruleConnection8806 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleConnection8838 = new BitSet(new long[]{0x0000000040000002L,0x0000000000000200L});
	public static final BitSet FOLLOW_ruleSerializer_in_ruleConnection8884 = new BitSet(new long[]{0x0000000040000002L});
	public static final BitSet FOLLOW_30_in_ruleConnection8911 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSerializer_in_entryRuleSerializer8943 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleSerializer8949 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_73_in_ruleSerializer8978 = new BitSet(new long[]{0x0000000000004000L});
	public static final BitSet FOLLOW_RULE_STRING_in_ruleSerializer8999 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_entryRuleAttribute9042 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleAttribute9048 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_35_in_ruleAttribute9077 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleAttribute9098 = new BitSet(new long[]{0x0000000000040002L});
	public static final BitSet FOLLOW_18_in_ruleAttribute9130 = new BitSet(new long[]{0x000000000288D340L});
	public static final BitSet FOLLOW_ruleAttrParm_in_ruleAttribute9171 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleAttribute9207 = new BitSet(new long[]{0x000000000280D340L});
	public static final BitSet FOLLOW_ruleAttrParm_in_ruleAttribute9249 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleAttribute9295 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleAttribute9322 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttrParm_in_entryRuleAttrParm9354 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleAttrParm9360 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleAttrParm9407 = new BitSet(new long[]{0x0000000100000000L});
	public static final BitSet FOLLOW_32_in_ruleAttrParm9439 = new BitSet(new long[]{0x000000000280D240L});
	public static final BitSet FOLLOW_ruleAttrParmValue_in_ruleAttrParm9472 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttrParmValue_in_entryRuleAttrParmValue9509 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleAttrParmValue9515 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_STRING_in_ruleAttrParmValue9555 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSignedInt_in_ruleAttrParmValue9607 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBoolean_in_ruleAttrParmValue9653 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSignedFloat_in_ruleAttrParmValue9699 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKeyValuePairs_in_entryRuleKeyValuePairs9736 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleKeyValuePairs9742 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_82_in_ruleKeyValuePairs9784 = new BitSet(new long[]{0x0000000000000100L,0x0000000000100002L});
	public static final BitSet FOLLOW_ruleKeyValuePair_in_ruleKeyValuePairs9819 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_22_in_ruleKeyValuePairs9850 = new BitSet(new long[]{0x0000000000000100L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKeyValuePair_in_ruleKeyValuePairs9887 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_22_in_ruleKeyValuePairs9927 = new BitSet(new long[]{0x0000000000000000L,0x0000000000100000L});
	public static final BitSet FOLLOW_84_in_ruleKeyValuePairs9950 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKeyValuePair_in_entryRuleKeyValuePair9976 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleKeyValuePair9982 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_ruleKeyValuePair10028 = new BitSet(new long[]{0x0000000008000000L});
	public static final BitSet FOLLOW_27_in_ruleKeyValuePair10049 = new BitSet(new long[]{0x000005400680D360L,0x0000000000040000L});
	public static final BitSet FOLLOW_ruleElement_in_ruleKeyValuePair10076 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleArray_in_entryRuleArray10113 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleArray10119 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_38_in_ruleArray10148 = new BitSet(new long[]{0x000005400680D360L,0x0000000000040000L});
	public static final BitSet FOLLOW_ruleElement_in_ruleArray10175 = new BitSet(new long[]{0x0000020000400000L});
	public static final BitSet FOLLOW_22_in_ruleArray10201 = new BitSet(new long[]{0x000005400680D360L,0x0000000000040000L});
	public static final BitSet FOLLOW_ruleElement_in_ruleArray10233 = new BitSet(new long[]{0x0000020000400000L});
	public static final BitSet FOLLOW_22_in_ruleArray10267 = new BitSet(new long[]{0x0000020000000000L});
	public static final BitSet FOLLOW_41_in_ruleArray10283 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleElement_in_entryRuleElement10309 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleElement10315 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKeyValuePairs_in_ruleElement10361 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleArray_in_ruleElement10407 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleLiteral_in_ruleElement10453 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleElement10500 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ruleTimeUnit_in_ruleElement10552 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_rulePath_in_ruleElement10605 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTypedVariable_in_entryRuleTypedVariable10642 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTypedVariable10648 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_rulePort_in_ruleTypedVariable10681 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAction_in_ruleTypedVariable10703 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleVarRef_in_entryRuleVarRef10729 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleVarRef10735 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRef10781 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRef10835 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_ruleVarRef10860 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRef10892 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_56_in_ruleVarRef10946 = new BitSet(new long[]{0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleVarRef10978 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRef11019 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRef11091 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_ruleVarRef11124 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRef11166 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleVarRef11208 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleVarRefOrModeTransition_in_entryRuleVarRefOrModeTransition11239 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleVarRefOrModeTransition11245 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleVarRefOrModeTransition11278 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleModeTransition_in_ruleVarRefOrModeTransition11321 = new BitSet(new long[]{0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleVarRefOrModeTransition11346 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleVarRefOrModeTransition11378 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleVarRefOrModeTransition11403 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAssignment_in_entryRuleAssignment11434 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleAssignment11440 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleAssignment11486 = new BitSet(new long[]{0x0000000100040000L,0x0000000000040000L});
	public static final BitSet FOLLOW_32_in_ruleAssignment11533 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAssignment11593 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_32_in_ruleAssignment11656 = new BitSet(new long[]{0x0000000000040000L,0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleAssignment11728 = new BitSet(new long[]{0x000000000288D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAssignment11816 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleAssignment11867 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAssignment11924 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleAssignment12005 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_82_in_ruleAssignment12096 = new BitSet(new long[]{0x000000000280D360L,0x0000000000180000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAssignment12184 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_22_in_ruleAssignment12235 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleAssignment12292 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_84_in_ruleAssignment12373 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleParameter_in_entryRuleParameter12454 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleParameter12460 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleAttribute_in_ruleParameter12506 = new BitSet(new long[]{0x0000000800000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleParameter12539 = new BitSet(new long[]{0x0000000008040002L,0x0000000000040000L});
	public static final BitSet FOLLOW_27_in_ruleParameter12571 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleParameter12603 = new BitSet(new long[]{0x0000000000040002L,0x0000000000040000L});
	public static final BitSet FOLLOW_18_in_ruleParameter12658 = new BitSet(new long[]{0x000000000288D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleParameter12728 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_22_in_ruleParameter12769 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleParameter12816 = new BitSet(new long[]{0x0000000000480000L});
	public static final BitSet FOLLOW_19_in_ruleParameter12881 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_82_in_ruleParameter12952 = new BitSet(new long[]{0x000000000280D360L,0x0000000000180000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleParameter13022 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_22_in_ruleParameter13063 = new BitSet(new long[]{0x000000000280D360L,0x0000000000080000L});
	public static final BitSet FOLLOW_ruleExpression_in_ruleParameter13110 = new BitSet(new long[]{0x0000000000400000L,0x0000000000100000L});
	public static final BitSet FOLLOW_84_in_ruleParameter13175 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleExpression_in_entryRuleExpression13236 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleExpression13242 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleLiteral_in_ruleExpression13312 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTime_in_ruleExpression13352 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleParameterReference_in_ruleExpression13374 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleCode_in_ruleExpression13396 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleParameterReference_in_entryRuleParameterReference13422 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleParameterReference13428 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleParameterReference13467 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleTime_in_entryRuleTime13498 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTime13504 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleTime13544 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_ruleTimeUnit_in_ruleTime13588 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_rulePort_in_entryRulePort13625 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRulePort13631 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleInput_in_rulePort13664 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleOutput_in_rulePort13686 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleType_in_entryRuleType13712 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleType13718 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_78_in_ruleType13765 = new BitSet(new long[]{0x0000004000000002L});
	public static final BitSet FOLLOW_ruleArraySpec_in_ruleType13817 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleDottedName_in_ruleType13879 = new BitSet(new long[]{0x0000004080100002L});
	public static final BitSet FOLLOW_31_in_ruleType13910 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleType13947 = new BitSet(new long[]{0x0000000400400000L});
	public static final BitSet FOLLOW_22_in_ruleType13983 = new BitSet(new long[]{0x0000000000000100L,0x0000000000084000L});
	public static final BitSet FOLLOW_ruleType_in_ruleType14025 = new BitSet(new long[]{0x0000000400400000L});
	public static final BitSet FOLLOW_34_in_ruleType14064 = new BitSet(new long[]{0x0000004000100002L});
	public static final BitSet FOLLOW_20_in_ruleType14096 = new BitSet(new long[]{0x0000004000100002L});
	public static final BitSet FOLLOW_ruleArraySpec_in_ruleType14149 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleCode_in_ruleType14203 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleArraySpec_in_entryRuleArraySpec14240 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleArraySpec14246 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_38_in_ruleArraySpec14275 = new BitSet(new long[]{0x0000020000000200L});
	public static final BitSet FOLLOW_41_in_ruleArraySpec14303 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleArraySpec14365 = new BitSet(new long[]{0x0000020000000000L});
	public static final BitSet FOLLOW_41_in_ruleArraySpec14402 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleWidthSpec_in_entryRuleWidthSpec14439 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleWidthSpec14445 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_38_in_ruleWidthSpec14474 = new BitSet(new long[]{0x0000020000000300L,0x00000000000A0000L});
	public static final BitSet FOLLOW_41_in_ruleWidthSpec14502 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleWidthTerm_in_ruleWidthSpec14572 = new BitSet(new long[]{0x0000020000200000L});
	public static final BitSet FOLLOW_21_in_ruleWidthSpec14608 = new BitSet(new long[]{0x0000000000000300L,0x00000000000A0000L});
	public static final BitSet FOLLOW_ruleWidthTerm_in_ruleWidthSpec14650 = new BitSet(new long[]{0x0000020000200000L});
	public static final BitSet FOLLOW_41_in_ruleWidthSpec14689 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleWidthTerm_in_entryRuleWidthTerm14726 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleWidthTerm14732 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleWidthTerm14772 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleWidthTerm14824 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_81_in_ruleWidthTerm14858 = new BitSet(new long[]{0x0100000000000100L});
	public static final BitSet FOLLOW_ruleVarRef_in_ruleWidthTerm14890 = new BitSet(new long[]{0x0000000000080000L});
	public static final BitSet FOLLOW_19_in_ruleWidthTerm14915 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleCode_in_ruleWidthTerm14955 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV4Host_in_entryRuleIPV4Host14992 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleIPV4Host14998 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_ruleIPV4Host15052 = new BitSet(new long[]{0x0000000800000000L});
	public static final BitSet FOLLOW_35_in_ruleIPV4Host15077 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_ruleIPV4Addr_in_ruleIPV4Host15110 = new BitSet(new long[]{0x0000000008000002L});
	public static final BitSet FOLLOW_27_in_ruleIPV4Host15136 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV4Host15161 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV6Host_in_entryRuleIPV6Host15213 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleIPV6Host15219 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_38_in_ruleIPV6Host15248 = new BitSet(new long[]{0x0000000010000300L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_ruleIPV6Host15283 = new BitSet(new long[]{0x0000000800000000L});
	public static final BitSet FOLLOW_35_in_ruleIPV6Host15308 = new BitSet(new long[]{0x0000000010000300L});
	public static final BitSet FOLLOW_ruleIPV6Addr_in_ruleIPV6Host15341 = new BitSet(new long[]{0x0000020000000000L});
	public static final BitSet FOLLOW_41_in_ruleIPV6Host15362 = new BitSet(new long[]{0x0000000008000002L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Host15377 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV6Host15402 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleNamedHost_in_entryRuleNamedHost15454 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleNamedHost15460 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_ruleNamedHost15514 = new BitSet(new long[]{0x0000000800000000L});
	public static final BitSet FOLLOW_35_in_ruleNamedHost15539 = new BitSet(new long[]{0x0000000000000100L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleHostName_in_ruleNamedHost15572 = new BitSet(new long[]{0x0000000008000002L});
	public static final BitSet FOLLOW_27_in_ruleNamedHost15598 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleNamedHost15623 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleHost_in_entryRuleHost15675 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleHost15681 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV4Host_in_ruleHost15714 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV6Host_in_ruleHost15736 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleNamedHost_in_ruleHost15758 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleHostName_in_entryRuleHostName15784 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleHostName15790 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_ruleHostName15823 = new BitSet(new long[]{0x0000000002000002L});
	public static final BitSet FOLLOW_25_in_ruleHostName15842 = new BitSet(new long[]{0x0000000000000100L,0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_ruleHostName15859 = new BitSet(new long[]{0x0000000002000002L});
	public static final BitSet FOLLOW_ruleDottedName_in_entryRuleDottedName15896 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleDottedName15902 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleDottedName15931 = new BitSet(new long[]{0x0000000012000002L});
	public static final BitSet FOLLOW_25_in_ruleDottedName15956 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_28_in_ruleDottedName15980 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleDottedName15998 = new BitSet(new long[]{0x0000000012000002L});
	public static final BitSet FOLLOW_ruleSignedInt_in_entryRuleSignedInt16035 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleSignedInt16041 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleSignedInt16070 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_NEGINT_in_ruleSignedInt16092 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleLiteral_in_entryRuleLiteral16122 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleLiteral16128 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_STRING_in_ruleLiteral16157 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_CHAR_LIT_in_ruleLiteral16179 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSignedFloat_in_ruleLiteral16205 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSignedInt_in_ruleLiteral16231 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBoolean_in_ruleLiteral16257 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleKebab_in_entryRuleKebab16287 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleKebab16293 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleKebab16327 = new BitSet(new long[]{0x0000000000800002L});
	public static final BitSet FOLLOW_65_in_ruleKebab16353 = new BitSet(new long[]{0x0000000000800002L});
	public static final BitSet FOLLOW_23_in_ruleKebab16373 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleKebab16385 = new BitSet(new long[]{0x0000000000800002L});
	public static final BitSet FOLLOW_ruleIPV4Addr_in_entryRuleIPV4Addr16422 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleIPV4Addr16428 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV4Addr16457 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_ruleIPV4Addr16471 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV4Addr16481 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_ruleIPV4Addr16495 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV4Addr16505 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_ruleIPV4Addr16519 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV4Addr16529 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_entryRuleIPV6Seg16559 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleIPV6Seg16565 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV6Seg16594 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV6Seg16627 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleIPV6Seg16652 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV6Addr_in_entryRuleIPV6Addr16688 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleIPV6Addr16694 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr16723 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr16746 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16770 = new BitSet(new long[]{0x0000000008000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr16790 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16814 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16859 = new BitSet(new long[]{0x0000000018000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr16886 = new BitSet(new long[]{0x0000000000000302L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr16913 = new BitSet(new long[]{0x0000000000000302L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr16951 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleIPV6Addr16992 = new BitSet(new long[]{0x0000000010000000L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr17009 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17026 = new BitSet(new long[]{0x0000000008020000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr17049 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17069 = new BitSet(new long[]{0x0000000008020000L});
	public static final BitSet FOLLOW_17_in_ruleIPV6Addr17094 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV6Addr17112 = new BitSet(new long[]{0x0000000000000302L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleIPV6Addr17142 = new BitSet(new long[]{0x0000000000000302L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr17183 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_ruleIPV4Addr_in_ruleIPV6Addr17200 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr17233 = new BitSet(new long[]{0x0000000000000100L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleIPV6Addr17245 = new BitSet(new long[]{0x0000000008000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr17262 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleIPV6Addr17280 = new BitSet(new long[]{0x0000000008000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr17300 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_ruleIPV4Addr_in_ruleIPV6Addr17324 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17377 = new BitSet(new long[]{0x0000000018000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr17408 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17434 = new BitSet(new long[]{0x0000000018000000L});
	public static final BitSet FOLLOW_28_in_ruleIPV6Addr17467 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17521 = new BitSet(new long[]{0x0000000008000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr17556 = new BitSet(new long[]{0x0000000000000300L});
	public static final BitSet FOLLOW_ruleIPV6Seg_in_ruleIPV6Addr17585 = new BitSet(new long[]{0x0000000008000000L});
	public static final BitSet FOLLOW_27_in_ruleIPV6Addr17628 = new BitSet(new long[]{0x0000000000000200L});
	public static final BitSet FOLLOW_ruleIPV4Addr_in_ruleIPV6Addr17658 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSignedFloat_in_entryRuleSignedFloat17694 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleSignedFloat17700 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleSignedInt_in_ruleSignedFloat17739 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_23_in_ruleSignedFloat17765 = new BitSet(new long[]{0x0000000002000000L});
	public static final BitSet FOLLOW_25_in_ruleSignedFloat17781 = new BitSet(new long[]{0x0000000000000280L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleSignedFloat17796 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_FLOAT_EXP_SUFFIX_in_ruleSignedFloat17822 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleCode_in_entryRuleCode17858 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleCode17864 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_83_in_ruleCode17906 = new BitSet(new long[]{0xFFFDFFCFFFFFFFF0L,0x000000000015FDFFL});
	public static final BitSet FOLLOW_ruleBody_in_ruleCode17933 = new BitSet(new long[]{0x0000000200000000L});
	public static final BitSet FOLLOW_33_in_ruleCode17954 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleFSName_in_entryRuleFSName17980 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleFSName17986 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleFSName18015 = new BitSet(new long[]{0x0000040002000102L});
	public static final BitSet FOLLOW_25_in_ruleFSName18037 = new BitSet(new long[]{0x0000040002000102L});
	public static final BitSet FOLLOW_42_in_ruleFSName18055 = new BitSet(new long[]{0x0000040002000102L});
	public static final BitSet FOLLOW_rulePath_in_entryRulePath18082 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRulePath18088 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleFSName_in_rulePath18127 = new BitSet(new long[]{0x0000000020000000L});
	public static final BitSet FOLLOW_29_in_rulePath18144 = new BitSet(new long[]{0x0000050006000100L});
	public static final BitSet FOLLOW_40_in_rulePath18165 = new BitSet(new long[]{0x0000040002000100L});
	public static final BitSet FOLLOW_26_in_rulePath18186 = new BitSet(new long[]{0x0000040002000100L});
	public static final BitSet FOLLOW_ruleFSName_in_rulePath18206 = new BitSet(new long[]{0x0000010004000002L});
	public static final BitSet FOLLOW_40_in_rulePath18231 = new BitSet(new long[]{0x0000040002000100L});
	public static final BitSet FOLLOW_26_in_rulePath18255 = new BitSet(new long[]{0x0000040002000100L});
	public static final BitSet FOLLOW_ruleFSName_in_rulePath18278 = new BitSet(new long[]{0x0000010004000002L});
	public static final BitSet FOLLOW_ruleTimeUnit_in_entryRuleTimeUnit18315 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleTimeUnit18321 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleTimeUnit18346 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleBody_in_entryRuleBody18371 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleBody18377 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_ruleToken_in_ruleBody18410 = new BitSet(new long[]{0xFFFDFFCDFFFFFFF2L,0x000000000015FDFFL});
	public static final BitSet FOLLOW_ruleToken_in_entryRuleToken18441 = new BitSet(new long[]{0x0000000000000000L});
	public static final BitSet FOLLOW_EOF_in_entryRuleToken18447 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ID_in_ruleToken18476 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_INT_in_ruleToken18498 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_FLOAT_EXP_SUFFIX_in_ruleToken18520 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_LT_ANNOT_in_ruleToken18542 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_STRING_in_ruleToken18564 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_CHAR_LIT_in_ruleToken18586 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ML_COMMENT_in_ruleToken18608 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_SL_COMMENT_in_ruleToken18630 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_WS_in_ruleToken18652 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_ANY_OTHER_in_ruleToken18674 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_77_in_ruleToken18696 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_53_in_ruleToken18714 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_58_in_ruleToken18732 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_71_in_ruleToken18750 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_70_in_ruleToken18768 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_76_in_ruleToken18786 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_78_in_ruleToken18804 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_61_in_ruleToken18822 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_55_in_ruleToken18840 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_64_in_ruleToken18858 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_79_in_ruleToken18876 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_43_in_ruleToken18894 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_69_in_ruleToken18912 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_75_in_ruleToken18930 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_74_in_ruleToken18948 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_44_in_ruleToken18966 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_48_in_ruleToken18984 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_62_in_ruleToken19002 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_66_in_ruleToken19020 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_63_in_ruleToken19038 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_50_in_ruleToken19056 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_46_in_ruleToken19074 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_45_in_ruleToken19092 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_51_in_ruleToken19110 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_80_in_ruleToken19128 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_47_in_ruleToken19146 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_59_in_ruleToken19164 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_56_in_ruleToken19182 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_60_in_ruleToken19200 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_54_in_ruleToken19218 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_72_in_ruleToken19236 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_52_in_ruleToken19254 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_NEGINT_in_ruleToken19272 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_TRUE_in_ruleToken19294 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_RULE_FALSE_in_ruleToken19316 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_57_in_ruleToken19338 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_65_in_ruleToken19356 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_67_in_ruleToken19374 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_68_in_ruleToken19392 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_18_in_ruleToken19410 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_19_in_ruleToken19428 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_82_in_ruleToken19446 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_84_in_ruleToken19464 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_38_in_ruleToken19482 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_41_in_ruleToken19500 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_31_in_ruleToken19518 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_34_in_ruleToken19536 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_27_in_ruleToken19554 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_30_in_ruleToken19572 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_22_in_ruleToken19590 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_25_in_ruleToken19608 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_28_in_ruleToken19626 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_29_in_ruleToken19644 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_40_in_ruleToken19662 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_21_in_ruleToken19680 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_23_in_ruleToken19698 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_20_in_ruleToken19716 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_26_in_ruleToken19734 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_42_in_ruleToken19752 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_24_in_ruleToken19770 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_32_in_ruleToken19788 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_17_in_ruleToken19806 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_35_in_ruleToken19824 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_39_in_ruleToken19842 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_36_in_ruleActionOrigin19884 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_57_in_ruleActionOrigin19912 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_65_in_ruleActionOrigin19940 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_36_in_ruleVisibility19987 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_67_in_ruleVisibility20015 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_68_in_ruleVisibility20043 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_75_in_ruleBuiltinTrigger20090 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_74_in_ruleBuiltinTrigger20118 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_72_in_ruleBuiltinTrigger20146 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_72_in_ruleModeTransition20193 = new BitSet(new long[]{0x0000000000000002L});
	public static final BitSet FOLLOW_52_in_ruleModeTransition20221 = new BitSet(new long[]{0x0000000000000002L});
}
