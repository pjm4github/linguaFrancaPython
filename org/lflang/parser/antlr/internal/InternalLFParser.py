#!/usr/bin/env python
""" generated source for module InternalLFParser """
# package: org.lflang.parser.antlr.internal
# import org.eclipse.xtext
# import org.eclipse.xtext.parser
# import org.eclipse.xtext.parser.impl
# import org.eclipse.emf.ecore.util.EcoreUtil
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.common.util.Enumerator
# import org.eclipse.xtext.parser.antlr.AbstractInternalAntlrParser
# import org.eclipse.xtext.parser.antlr.XtextTokenStream
# import org.eclipse.xtext.parser.antlr.XtextTokenStream.HiddenTokens
# import org.eclipse.xtext.parser.antlr.AntlrDatatypeRuleToken
from include.overloading import overloaded
from org.lflang.services import LFGrammarAccess

# from org.antlr.runtime
# import java.util.Stack
# import java.util.List
# import java.util.ArrayList

@SuppressWarnings("all")
class InternalLFParser(AbstractInternalAntlrParser):
    """ generated source for class InternalLFParser """
    tokenNames = [None] * 
    T__50 = 50
    T__19 = 19
    RULE_LT_ANNOT = 12
    T__59 = 59
    T__17 = 17
    T__18 = 18
    T__55 = 55
    T__56 = 56
    T__57 = 57
    T__58 = 58
    T__51 = 51
    T__52 = 52
    T__53 = 53
    T__54 = 54
    RULE_NEGINT = 9
    T__60 = 60
    T__61 = 61
    RULE_ID = 5
    RULE_CHAR_LIT = 10
    T__26 = 26
    T__27 = 27
    T__28 = 28
    RULE_INT = 8
    T__29 = 29
    T__22 = 22
    T__66 = 66
    RULE_ML_COMMENT = 13
    T__23 = 23
    T__67 = 67
    RULE_FLOAT_EXP_SUFFIX = 11
    T__24 = 24
    T__68 = 68
    T__25 = 25
    T__69 = 69
    RULE_FALSE = 7
    T__62 = 62
    T__63 = 63
    T__20 = 20
    T__64 = 64
    T__21 = 21
    T__65 = 65
    T__70 = 70
    T__71 = 71
    T__72 = 72
    RULE_STRING = 4
    RULE_SL_COMMENT = 14
    T__37 = 37
    T__38 = 38
    T__39 = 39
    T__33 = 33
    T__77 = 77
    RULE_TRUE = 6
    T__34 = 34
    T__78 = 78
    T__35 = 35
    T__79 = 79
    T__36 = 36
    T__73 = 73
    EOF = -1
    T__30 = 30
    T__74 = 74
    T__31 = 31
    T__75 = 75
    T__32 = 32
    T__76 = 76
    T__80 = 80
    T__81 = 81
    T__82 = 82
    T__83 = 83
    RULE_WS = 15
    RULE_ANY_OTHER = 16
    T__48 = 48
    T__49 = 49
    T__44 = 44
    T__45 = 45
    T__46 = 46
    T__47 = 47
    T__40 = 40
    T__84 = 84
    T__41 = 41
    T__85 = 85
    T__42 = 42
    T__43 = 43

    #  delegates
    #  delegators
    @overloaded
    def __init__(self, input):
        """ generated source for method __init__ """
        super(InternalLFParser, self).__init__()
        self.__init__(input, RecognizerSharedState())

    @__init__.register(object, TokenStream, RecognizerSharedState)
    def __init___0(self, input, state):
        """ generated source for method __init___0 """
        super(InternalLFParser, self).__init__(state)

    def getTokenNames(self):
        """ generated source for method getTokenNames """
        return InternalLFParser.tokenNames

    def getGrammarFileName(self):
        """ generated source for method getGrammarFileName """
        return "InternalLF.g"

    grammarAccess = None

    @__init__.register(object, TokenStream, LFGrammarAccess)
    def __init___1(self, input, grammarAccess):
        """ generated source for method __init___1 """
        super(InternalLFParser, self).__init__()
        self.__init__(input)
        self.grammarAccess = grammarAccess
        registerRules(grammarAccess.getGrammar())

    def getFirstRuleName(self):
        """ generated source for method getFirstRuleName """
        return "Model"

    def getGrammarAccess(self):
        """ generated source for method getGrammarAccess """
        return self.grammarAccess

    #  $ANTLR start "entryRuleModel"
    #  InternalLF.g:65:1: entryRuleModel returns [EObject current=null] : iv_ruleModel= ruleModel EOF ;
    def entryRuleModel(self):
        """ generated source for method entryRuleModel """
        current = None
        iv_ruleModel = None
        try:
            #  InternalLF.g:65:46: (iv_ruleModel= ruleModel EOF )
            #  InternalLF.g:66:2: iv_ruleModel= ruleModel EOF
            newCompositeNode(self.grammarAccess.getModelRule())
            pushFollow(FOLLOW_1)
            iv_ruleModel = ruleModel()
            state._fsp -= 1
            current = iv_ruleModel
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleModel"
    #  $ANTLR start "ruleModel"
    #  InternalLF.g:72:1: ruleModel returns [EObject current=null] : ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ ) ;
    def ruleModel(self):
        """ generated source for method ruleModel """
        current = None
        lv_target_0_0 = None
        lv_imports_1_0 = None
        lv_preambles_2_0 = None
        lv_reactors_3_0 = None
        enterRule()
        try:
            #  InternalLF.g:78:2: ( ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ ) )
            #  InternalLF.g:79:2: ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ )
            #  InternalLF.g:79:2: ( ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+ )
            #  InternalLF.g:80:3: ( (lv_target_0_0= ruleTargetDecl ) ) ( (lv_imports_1_0= ruleImport ) )* ( (lv_preambles_2_0= rulePreamble ) )* ( (lv_reactors_3_0= ruleReactor ) )+
            #  InternalLF.g:80:3: ( (lv_target_0_0= ruleTargetDecl ) )
            #  InternalLF.g:81:4: (lv_target_0_0= ruleTargetDecl )
            #  InternalLF.g:81:4: (lv_target_0_0= ruleTargetDecl )
            #  InternalLF.g:82:5: lv_target_0_0= ruleTargetDecl
            newCompositeNode(self.grammarAccess.getModelAccess().getTargetTargetDeclParserRuleCall_0_0())
            pushFollow(FOLLOW_3)
            lv_target_0_0 = ruleTargetDecl()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getModelRule())
            set(current, "target", lv_target_0_0, "org.lflang.LF.TargetDecl")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:99:3: ( (lv_imports_1_0= ruleImport ) )*
            while True:
                alt1 = 2
                LA1_0 = input.LA(1)
                if (LA1_0 == 17):
                    alt1 = 1
                if alt1 == 1:
                    #  InternalLF.g:100:4: (lv_imports_1_0= ruleImport )
                    #  InternalLF.g:100:4: (lv_imports_1_0= ruleImport )
                    #  InternalLF.g:101:5: lv_imports_1_0= ruleImport
                    newCompositeNode(self.grammarAccess.getModelAccess().getImportsImportParserRuleCall_1_0())
                    pushFollow(FOLLOW_3)
                    lv_imports_1_0 = ruleImport()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModelRule())
                    add(current, "imports", lv_imports_1_0, "org.lflang.LF.Import")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:118:3: ( (lv_preambles_2_0= rulePreamble ) )*
            while True:
                alt2 = 2
                LA2_0 = input.LA(1)
                if (LA2_0 == 52 or (LA2_0 >= 82 and LA2_0 <= 83) or LA2_0 == 85):
                    alt2 = 1
                if alt2 == 1:
                    #  InternalLF.g:119:4: (lv_preambles_2_0= rulePreamble )
                    #  InternalLF.g:119:4: (lv_preambles_2_0= rulePreamble )
                    #  InternalLF.g:120:5: lv_preambles_2_0= rulePreamble
                    newCompositeNode(self.grammarAccess.getModelAccess().getPreamblesPreambleParserRuleCall_2_0())
                    pushFollow(FOLLOW_3)
                    lv_preambles_2_0 = rulePreamble()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModelRule())
                    add(current, "preambles", lv_preambles_2_0, "org.lflang.LF.Preamble")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:137:3: ( (lv_reactors_3_0= ruleReactor ) )+
            cnt3 = 0
            while True:
                alt3 = 2
                LA3_0 = input.LA(1)
                if ((LA3_0 >= 22 and LA3_0 <= 25) or LA3_0 == 59):
                    alt3 = 1
                if alt3 == 1:
                    #  InternalLF.g:138:4: (lv_reactors_3_0= ruleReactor )
                    #  InternalLF.g:138:4: (lv_reactors_3_0= ruleReactor )
                    #  InternalLF.g:139:5: lv_reactors_3_0= ruleReactor
                    newCompositeNode(self.grammarAccess.getModelAccess().getReactorsReactorParserRuleCall_3_0())
                    pushFollow(FOLLOW_4)
                    lv_reactors_3_0 = ruleReactor()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModelRule())
                    add(current, "reactors", lv_reactors_3_0, "org.lflang.LF.Reactor")
                    afterParserOrEnumRuleCall()
                else:
                    if cnt3 >= 1:
                    eee = EarlyExitException(3, input)
                    raise eee
                cnt3 += 1
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleModel"
    #  $ANTLR start "entryRuleImport"
    #  InternalLF.g:160:1: entryRuleImport returns [EObject current=null] : iv_ruleImport= ruleImport EOF ;
    def entryRuleImport(self):
        """ generated source for method entryRuleImport """
        current = None
        iv_ruleImport = None
        try:
            #  InternalLF.g:160:47: (iv_ruleImport= ruleImport EOF )
            #  InternalLF.g:161:2: iv_ruleImport= ruleImport EOF
            newCompositeNode(self.grammarAccess.getImportRule())
            pushFollow(FOLLOW_1)
            iv_ruleImport = ruleImport()
            state._fsp -= 1
            current = iv_ruleImport
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleImport"
    #  $ANTLR start "ruleImport"
    #  InternalLF.g:167:1: ruleImport returns [EObject current=null] : (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? ) ;
    def ruleImport(self):
        """ generated source for method ruleImport """
        current = None
        otherlv_0 = None
        otherlv_2 = None
        otherlv_4 = None
        lv_importURI_5_0 = None
        otherlv_6 = None
        lv_reactorClasses_1_0 = None
        lv_reactorClasses_3_0 = None
        enterRule()
        try:
            #  InternalLF.g:173:2: ( (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? ) )
            #  InternalLF.g:174:2: (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? )
            #  InternalLF.g:174:2: (otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )? )
            #  InternalLF.g:175:3: otherlv_0= 'import' ( (lv_reactorClasses_1_0= ruleImportedReactor ) ) (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )* otherlv_4= 'from' ( (lv_importURI_5_0= RULE_STRING ) ) (otherlv_6= ';' )?
            otherlv_0 = match(input, 17, FOLLOW_5)
            newLeafNode(otherlv_0, self.grammarAccess.getImportAccess().getImportKeyword_0())
            #  InternalLF.g:179:3: ( (lv_reactorClasses_1_0= ruleImportedReactor ) )
            #  InternalLF.g:180:4: (lv_reactorClasses_1_0= ruleImportedReactor )
            #  InternalLF.g:180:4: (lv_reactorClasses_1_0= ruleImportedReactor )
            #  InternalLF.g:181:5: lv_reactorClasses_1_0= ruleImportedReactor
            newCompositeNode(self.grammarAccess.getImportAccess().getReactorClassesImportedReactorParserRuleCall_1_0())
            pushFollow(FOLLOW_6)
            lv_reactorClasses_1_0 = ruleImportedReactor()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getImportRule())
            add(current, "reactorClasses", lv_reactorClasses_1_0, "org.lflang.LF.ImportedReactor")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:198:3: (otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) ) )*
            while True:
                alt4 = 2
                LA4_0 = input.LA(1)
                if (LA4_0 == 18):
                    alt4 = 1
                if alt4 == 1:
                    #  InternalLF.g:199:4: otherlv_2= ',' ( (lv_reactorClasses_3_0= ruleImportedReactor ) )
                    otherlv_2 = match(input, 18, FOLLOW_5)
                    newLeafNode(otherlv_2, self.grammarAccess.getImportAccess().getCommaKeyword_2_0())
                    #  InternalLF.g:203:4: ( (lv_reactorClasses_3_0= ruleImportedReactor ) )
                    #  InternalLF.g:204:5: (lv_reactorClasses_3_0= ruleImportedReactor )
                    #  InternalLF.g:204:5: (lv_reactorClasses_3_0= ruleImportedReactor )
                    #  InternalLF.g:205:6: lv_reactorClasses_3_0= ruleImportedReactor
                    newCompositeNode(self.grammarAccess.getImportAccess().getReactorClassesImportedReactorParserRuleCall_2_1_0())
                    pushFollow(FOLLOW_6)
                    lv_reactorClasses_3_0 = ruleImportedReactor()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getImportRule())
                    add(current, "reactorClasses", lv_reactorClasses_3_0, "org.lflang.LF.ImportedReactor")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            otherlv_4 = match(input, 19, FOLLOW_7)
            newLeafNode(otherlv_4, self.grammarAccess.getImportAccess().getFromKeyword_3())
            #  InternalLF.g:227:3: ( (lv_importURI_5_0= RULE_STRING ) )
            #  InternalLF.g:228:4: (lv_importURI_5_0= RULE_STRING )
            #  InternalLF.g:228:4: (lv_importURI_5_0= RULE_STRING )
            #  InternalLF.g:229:5: lv_importURI_5_0= RULE_STRING
            lv_importURI_5_0 = match(input, self.RULE_STRING, FOLLOW_8)
            newLeafNode(lv_importURI_5_0, self.grammarAccess.getImportAccess().getImportURISTRINGTerminalRuleCall_4_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getImportRule())
            setWithLastConsumed(current, "importURI", lv_importURI_5_0, "org.lflang.LF.STRING")
            #  InternalLF.g:245:3: (otherlv_6= ';' )?
            alt5 = 2
            LA5_0 = input.LA(1)
            if (LA5_0 == 20):
                alt5 = 1
            if alt5 == 1:
                #  InternalLF.g:246:4: otherlv_6= ';'
                otherlv_6 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_6, self.grammarAccess.getImportAccess().getSemicolonKeyword_5())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleImport"
    #  $ANTLR start "entryRuleImportedReactor"
    #  InternalLF.g:255:1: entryRuleImportedReactor returns [EObject current=null] : iv_ruleImportedReactor= ruleImportedReactor EOF ;
    def entryRuleImportedReactor(self):
        """ generated source for method entryRuleImportedReactor """
        current = None
        iv_ruleImportedReactor = None
        try:
            #  InternalLF.g:255:56: (iv_ruleImportedReactor= ruleImportedReactor EOF )
            #  InternalLF.g:256:2: iv_ruleImportedReactor= ruleImportedReactor EOF
            newCompositeNode(self.grammarAccess.getImportedReactorRule())
            pushFollow(FOLLOW_1)
            iv_ruleImportedReactor = ruleImportedReactor()
            state._fsp -= 1
            current = iv_ruleImportedReactor
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleImportedReactor"
    #  $ANTLR start "ruleImportedReactor"
    #  InternalLF.g:262:1: ruleImportedReactor returns [EObject current=null] : ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? ) ;
    def ruleImportedReactor(self):
        """ generated source for method ruleImportedReactor """
        current = None
        otherlv_0 = None
        otherlv_1 = None
        lv_name_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:268:2: ( ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? ) )
            #  InternalLF.g:269:2: ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? )
            #  InternalLF.g:269:2: ( ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )? )
            #  InternalLF.g:270:3: ( (otherlv_0= RULE_ID ) ) (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )?
            #  InternalLF.g:270:3: ( (otherlv_0= RULE_ID ) )
            #  InternalLF.g:271:4: (otherlv_0= RULE_ID )
            #  InternalLF.g:271:4: (otherlv_0= RULE_ID )
            #  InternalLF.g:272:5: otherlv_0= RULE_ID
            if current == None:
                current = createModelElement(self.grammarAccess.getImportedReactorRule())
            otherlv_0 = match(input, self.RULE_ID, FOLLOW_9)
            newLeafNode(otherlv_0, self.grammarAccess.getImportedReactorAccess().getReactorClassReactorCrossReference_0_0())
            #  InternalLF.g:283:3: (otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) ) )?
            alt6 = 2
            LA6_0 = input.LA(1)
            if (LA6_0 == 21):
                alt6 = 1
            if alt6 == 1:
                #  InternalLF.g:284:4: otherlv_1= 'as' ( (lv_name_2_0= RULE_ID ) )
                otherlv_1 = match(input, 21, FOLLOW_5)
                newLeafNode(otherlv_1, self.grammarAccess.getImportedReactorAccess().getAsKeyword_1_0())
                #  InternalLF.g:288:4: ( (lv_name_2_0= RULE_ID ) )
                #  InternalLF.g:289:5: (lv_name_2_0= RULE_ID )
                #  InternalLF.g:289:5: (lv_name_2_0= RULE_ID )
                #  InternalLF.g:290:6: lv_name_2_0= RULE_ID
                lv_name_2_0 = match(input, self.RULE_ID, FOLLOW_2)
                newLeafNode(lv_name_2_0, self.grammarAccess.getImportedReactorAccess().getNameIDTerminalRuleCall_1_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getImportedReactorRule())
                setWithLastConsumed(current, "name", lv_name_2_0, "org.lflang.LF.ID")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleImportedReactor"
    #  $ANTLR start "entryRuleReactor"
    #  InternalLF.g:311:1: entryRuleReactor returns [EObject current=null] : iv_ruleReactor= ruleReactor EOF ;
    def entryRuleReactor(self):
        """ generated source for method entryRuleReactor """
        current = None
        iv_ruleReactor = None
        try:
            #  InternalLF.g:311:48: (iv_ruleReactor= ruleReactor EOF )
            #  InternalLF.g:312:2: iv_ruleReactor= ruleReactor EOF
            newCompositeNode(self.grammarAccess.getReactorRule())
            pushFollow(FOLLOW_1)
            iv_ruleReactor = ruleReactor()
            state._fsp -= 1
            current = iv_ruleReactor
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleReactor"
    #  $ANTLR start "ruleReactor"
    #  InternalLF.g:318:1: ruleReactor returns [EObject current=null] : ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' ) ;
    def ruleReactor(self):
        """ generated source for method ruleReactor """
        current = None
        lv_federated_3_0 = None
        lv_main_4_0 = None
        lv_realtime_5_0 = None
        otherlv_6 = None
        lv_name_7_0 = None
        otherlv_8 = None
        otherlv_10 = None
        otherlv_12 = None
        otherlv_13 = None
        otherlv_15 = None
        otherlv_17 = None
        otherlv_18 = None
        otherlv_20 = None
        otherlv_21 = None
        otherlv_22 = None
        otherlv_23 = None
        otherlv_24 = None
        otherlv_36 = None
        lv_attributes_1_0 = None
        lv_typeParms_9_0 = None
        lv_typeParms_11_0 = None
        lv_parameters_14_0 = None
        lv_parameters_16_0 = None
        lv_host_19_0 = None
        lv_preambles_25_0 = None
        lv_stateVars_26_0 = None
        lv_methods_27_0 = None
        lv_inputs_28_0 = None
        lv_outputs_29_0 = None
        lv_timers_30_0 = None
        lv_actions_31_0 = None
        lv_instantiations_32_0 = None
        lv_connections_33_0 = None
        lv_reactions_34_0 = None
        lv_modes_35_0 = None
        enterRule()
        try:
            #  InternalLF.g:324:2: ( ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' ) )
            #  InternalLF.g:325:2: ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' )
            #  InternalLF.g:325:2: ( () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}' )
            #  InternalLF.g:326:3: () ( (lv_attributes_1_0= ruleAttribute ) )* ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) ) otherlv_6= 'reactor' ( (lv_name_7_0= RULE_ID ) )? (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )? (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )? (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )? (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )? otherlv_24= '{' ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )* otherlv_36= '}'
            #  InternalLF.g:326:3: ()
            #  InternalLF.g:327:4: 
            current = forceCreateModelElement(self.grammarAccess.getReactorAccess().getReactorAction_0(), current)
            #  InternalLF.g:333:3: ( (lv_attributes_1_0= ruleAttribute ) )*
            while True:
                alt7 = 2
                LA7_0 = input.LA(1)
                if (LA7_0 == 59):
                    alt7 = 1
                if alt7 == 1:
                    #  InternalLF.g:334:4: (lv_attributes_1_0= ruleAttribute )
                    #  InternalLF.g:334:4: (lv_attributes_1_0= ruleAttribute )
                    #  InternalLF.g:335:5: lv_attributes_1_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getReactorAccess().getAttributesAttributeParserRuleCall_1_0())
                    pushFollow(FOLLOW_10)
                    lv_attributes_1_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "attributes", lv_attributes_1_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:352:3: ( ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) ) )
            #  InternalLF.g:353:4: ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) )
            #  InternalLF.g:353:4: ( ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* ) )
            #  InternalLF.g:354:5: ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* )
            getUnorderedGroupHelper().enter(self.grammarAccess.getReactorAccess().getUnorderedGroup_2())
            #  InternalLF.g:357:5: ( ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )* )
            #  InternalLF.g:358:6: ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )*
            #  InternalLF.g:358:6: ( ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) ) | ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) ) )*
            while True:
                alt9 = 3
                LA9_0 = input.LA(1)
                if LA9_0 >= 22 and LA9_0 <= 23 and getUnorderedGroupHelper().canSelect(self.grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0):
                    alt9 = 1
                elif LA9_0 == 24 and getUnorderedGroupHelper().canSelect(self.grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1):
                    alt9 = 2
                if alt9 == 1:
                    #  InternalLF.g:359:4: ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) )
                    #  InternalLF.g:359:4: ({...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) ) )
                    #  InternalLF.g:360:5: {...}? => ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) )
                    if not getUnorderedGroupHelper().canSelect(self.grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0):
                        raise FailedPredicateException(input, "ruleReactor", "getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0)")
                    #  InternalLF.g:360:104: ( ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) ) )
                    #  InternalLF.g:361:6: ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) )
                    getUnorderedGroupHelper().select(self.grammarAccess.getReactorAccess().getUnorderedGroup_2(), 0)
                    #  InternalLF.g:364:9: ({...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) ) )
                    #  InternalLF.g:364:10: {...}? => ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) )
                    if not ((True)):
                        raise FailedPredicateException(input, "ruleReactor", "true")
                    #  InternalLF.g:364:19: ( ( (lv_federated_3_0= 'federated' ) ) | ( (lv_main_4_0= 'main' ) ) )
                    alt8 = 2
                    LA8_0 = input.LA(1)
                    if (LA8_0 == 22):
                        alt8 = 1
                    elif (LA8_0 == 23):
                        alt8 = 2
                    else:
                        nvae = NoViableAltException("", 8, 0, input)
                        raise nvae
                    if alt8 == 1:
                        #  InternalLF.g:364:20: ( (lv_federated_3_0= 'federated' ) )
                        #  InternalLF.g:364:20: ( (lv_federated_3_0= 'federated' ) )
                        #  InternalLF.g:365:10: (lv_federated_3_0= 'federated' )
                        #  InternalLF.g:365:10: (lv_federated_3_0= 'federated' )
                        #  InternalLF.g:366:11: lv_federated_3_0= 'federated'
                        lv_federated_3_0 = match(input, 22, FOLLOW_11)
                        newLeafNode(lv_federated_3_0, self.grammarAccess.getReactorAccess().getFederatedFederatedKeyword_2_0_0_0())
                        if current == None:
                            current = createModelElement(self.grammarAccess.getReactorRule())
                        setWithLastConsumed(current, "federated", lv_federated_3_0 != None, "federated")
                    elif alt8 == 2:
                        #  InternalLF.g:379:9: ( (lv_main_4_0= 'main' ) )
                        #  InternalLF.g:379:9: ( (lv_main_4_0= 'main' ) )
                        #  InternalLF.g:380:10: (lv_main_4_0= 'main' )
                        #  InternalLF.g:380:10: (lv_main_4_0= 'main' )
                        #  InternalLF.g:381:11: lv_main_4_0= 'main'
                        lv_main_4_0 = match(input, 23, FOLLOW_11)
                        newLeafNode(lv_main_4_0, self.grammarAccess.getReactorAccess().getMainMainKeyword_2_0_1_0())
                        if current == None:
                            current = createModelElement(self.grammarAccess.getReactorRule())
                        setWithLastConsumed(current, "main", lv_main_4_0 != None, "main")
                    getUnorderedGroupHelper().returnFromSelection(self.grammarAccess.getReactorAccess().getUnorderedGroup_2())
                elif alt9 == 2:
                    #  InternalLF.g:399:4: ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) )
                    #  InternalLF.g:399:4: ({...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) ) )
                    #  InternalLF.g:400:5: {...}? => ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) )
                    if not getUnorderedGroupHelper().canSelect(self.grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1):
                        raise FailedPredicateException(input, "ruleReactor", "getUnorderedGroupHelper().canSelect(grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1)")
                    #  InternalLF.g:400:104: ( ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) ) )
                    #  InternalLF.g:401:6: ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) )
                    getUnorderedGroupHelper().select(self.grammarAccess.getReactorAccess().getUnorderedGroup_2(), 1)
                    #  InternalLF.g:404:9: ({...}? => ( (lv_realtime_5_0= 'realtime' ) ) )
                    #  InternalLF.g:404:10: {...}? => ( (lv_realtime_5_0= 'realtime' ) )
                    if not ((True)):
                        raise FailedPredicateException(input, "ruleReactor", "true")
                    #  InternalLF.g:404:19: ( (lv_realtime_5_0= 'realtime' ) )
                    #  InternalLF.g:404:20: (lv_realtime_5_0= 'realtime' )
                    #  InternalLF.g:404:20: (lv_realtime_5_0= 'realtime' )
                    #  InternalLF.g:405:10: lv_realtime_5_0= 'realtime'
                    lv_realtime_5_0 = match(input, 24, FOLLOW_11)
                    newLeafNode(lv_realtime_5_0, self.grammarAccess.getReactorAccess().getRealtimeRealtimeKeyword_2_1_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getReactorRule())
                    setWithLastConsumed(current, "realtime", lv_realtime_5_0 != None, "realtime")
                    getUnorderedGroupHelper().returnFromSelection(self.grammarAccess.getReactorAccess().getUnorderedGroup_2())
                else:
                if not ((True)):
                    break
            getUnorderedGroupHelper().leave(self.grammarAccess.getReactorAccess().getUnorderedGroup_2())
            otherlv_6 = match(input, 25, FOLLOW_12)
            newLeafNode(otherlv_6, self.grammarAccess.getReactorAccess().getReactorKeyword_3())
            #  InternalLF.g:433:3: ( (lv_name_7_0= RULE_ID ) )?
            alt10 = 2
            LA10_0 = input.LA(1)
            if (LA10_0 == self.RULE_ID):
                alt10 = 1
            if alt10 == 1:
                #  InternalLF.g:434:4: (lv_name_7_0= RULE_ID )
                #  InternalLF.g:434:4: (lv_name_7_0= RULE_ID )
                #  InternalLF.g:435:5: lv_name_7_0= RULE_ID
                lv_name_7_0 = match(input, self.RULE_ID, FOLLOW_13)
                newLeafNode(lv_name_7_0, self.grammarAccess.getReactorAccess().getNameIDTerminalRuleCall_4_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getReactorRule())
                setWithLastConsumed(current, "name", lv_name_7_0, "org.lflang.LF.ID")
            #  InternalLF.g:451:3: (otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>' )?
            alt12 = 2
            LA12_0 = input.LA(1)
            if (LA12_0 == 26):
                alt12 = 1
            if alt12 == 1:
                #  InternalLF.g:452:4: otherlv_8= '<' ( (lv_typeParms_9_0= ruleTypeParm ) ) (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )* otherlv_12= '>'
                otherlv_8 = match(input, 26, FOLLOW_14)
                newLeafNode(otherlv_8, self.grammarAccess.getReactorAccess().getLessThanSignKeyword_5_0())
                #  InternalLF.g:456:4: ( (lv_typeParms_9_0= ruleTypeParm ) )
                #  InternalLF.g:457:5: (lv_typeParms_9_0= ruleTypeParm )
                #  InternalLF.g:457:5: (lv_typeParms_9_0= ruleTypeParm )
                #  InternalLF.g:458:6: lv_typeParms_9_0= ruleTypeParm
                newCompositeNode(self.grammarAccess.getReactorAccess().getTypeParmsTypeParmParserRuleCall_5_1_0())
                pushFollow(FOLLOW_15)
                lv_typeParms_9_0 = ruleTypeParm()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactorRule())
                add(current, "typeParms", lv_typeParms_9_0, "org.lflang.LF.TypeParm")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:475:4: (otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) ) )*
                while True:
                    alt11 = 2
                    LA11_0 = input.LA(1)
                    if (LA11_0 == 18):
                        alt11 = 1
                    if alt11 == 1:
                        #  InternalLF.g:476:5: otherlv_10= ',' ( (lv_typeParms_11_0= ruleTypeParm ) )
                        otherlv_10 = match(input, 18, FOLLOW_14)
                        newLeafNode(otherlv_10, self.grammarAccess.getReactorAccess().getCommaKeyword_5_2_0())
                        #  InternalLF.g:480:5: ( (lv_typeParms_11_0= ruleTypeParm ) )
                        #  InternalLF.g:481:6: (lv_typeParms_11_0= ruleTypeParm )
                        #  InternalLF.g:481:6: (lv_typeParms_11_0= ruleTypeParm )
                        #  InternalLF.g:482:7: lv_typeParms_11_0= ruleTypeParm
                        newCompositeNode(self.grammarAccess.getReactorAccess().getTypeParmsTypeParmParserRuleCall_5_2_1_0())
                        pushFollow(FOLLOW_15)
                        lv_typeParms_11_0 = ruleTypeParm()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getReactorRule())
                        add(current, "typeParms", lv_typeParms_11_0, "org.lflang.LF.TypeParm")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                otherlv_12 = match(input, 27, FOLLOW_16)
                newLeafNode(otherlv_12, self.grammarAccess.getReactorAccess().getGreaterThanSignKeyword_5_3())
            #  InternalLF.g:505:3: (otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')' )?
            alt14 = 2
            LA14_0 = input.LA(1)
            if (LA14_0 == 28):
                alt14 = 1
            if alt14 == 1:
                #  InternalLF.g:506:4: otherlv_13= '(' ( (lv_parameters_14_0= ruleParameter ) ) (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )* otherlv_17= ')'
                otherlv_13 = match(input, 28, FOLLOW_17)
                newLeafNode(otherlv_13, self.grammarAccess.getReactorAccess().getLeftParenthesisKeyword_6_0())
                #  InternalLF.g:510:4: ( (lv_parameters_14_0= ruleParameter ) )
                #  InternalLF.g:511:5: (lv_parameters_14_0= ruleParameter )
                #  InternalLF.g:511:5: (lv_parameters_14_0= ruleParameter )
                #  InternalLF.g:512:6: lv_parameters_14_0= ruleParameter
                newCompositeNode(self.grammarAccess.getReactorAccess().getParametersParameterParserRuleCall_6_1_0())
                pushFollow(FOLLOW_18)
                lv_parameters_14_0 = ruleParameter()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactorRule())
                add(current, "parameters", lv_parameters_14_0, "org.lflang.LF.Parameter")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:529:4: (otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) ) )*
                while True:
                    alt13 = 2
                    LA13_0 = input.LA(1)
                    if (LA13_0 == 18):
                        alt13 = 1
                    if alt13 == 1:
                        #  InternalLF.g:530:5: otherlv_15= ',' ( (lv_parameters_16_0= ruleParameter ) )
                        otherlv_15 = match(input, 18, FOLLOW_17)
                        newLeafNode(otherlv_15, self.grammarAccess.getReactorAccess().getCommaKeyword_6_2_0())
                        #  InternalLF.g:534:5: ( (lv_parameters_16_0= ruleParameter ) )
                        #  InternalLF.g:535:6: (lv_parameters_16_0= ruleParameter )
                        #  InternalLF.g:535:6: (lv_parameters_16_0= ruleParameter )
                        #  InternalLF.g:536:7: lv_parameters_16_0= ruleParameter
                        newCompositeNode(self.grammarAccess.getReactorAccess().getParametersParameterParserRuleCall_6_2_1_0())
                        pushFollow(FOLLOW_18)
                        lv_parameters_16_0 = ruleParameter()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getReactorRule())
                        add(current, "parameters", lv_parameters_16_0, "org.lflang.LF.Parameter")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                otherlv_17 = match(input, 29, FOLLOW_19)
                newLeafNode(otherlv_17, self.grammarAccess.getReactorAccess().getRightParenthesisKeyword_6_3())
            #  InternalLF.g:559:3: (otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) ) )?
            alt15 = 2
            LA15_0 = input.LA(1)
            if (LA15_0 == 30):
                alt15 = 1
            if alt15 == 1:
                #  InternalLF.g:560:4: otherlv_18= 'at' ( (lv_host_19_0= ruleHost ) )
                otherlv_18 = match(input, 30, FOLLOW_20)
                newLeafNode(otherlv_18, self.grammarAccess.getReactorAccess().getAtKeyword_7_0())
                #  InternalLF.g:564:4: ( (lv_host_19_0= ruleHost ) )
                #  InternalLF.g:565:5: (lv_host_19_0= ruleHost )
                #  InternalLF.g:565:5: (lv_host_19_0= ruleHost )
                #  InternalLF.g:566:6: lv_host_19_0= ruleHost
                newCompositeNode(self.grammarAccess.getReactorAccess().getHostHostParserRuleCall_7_1_0())
                pushFollow(FOLLOW_21)
                lv_host_19_0 = ruleHost()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactorRule())
                set(current, "host", lv_host_19_0, "org.lflang.LF.Host")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:584:3: (otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* ) )?
            alt17 = 2
            LA17_0 = input.LA(1)
            if (LA17_0 == 31):
                alt17 = 1
            if alt17 == 1:
                #  InternalLF.g:585:4: otherlv_20= 'extends' ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* )
                otherlv_20 = match(input, 31, FOLLOW_5)
                newLeafNode(otherlv_20, self.grammarAccess.getReactorAccess().getExtendsKeyword_8_0())
                #  InternalLF.g:589:4: ( ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )* )
                #  InternalLF.g:590:5: ( (otherlv_21= RULE_ID ) ) (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )*
                #  InternalLF.g:590:5: ( (otherlv_21= RULE_ID ) )
                #  InternalLF.g:591:6: (otherlv_21= RULE_ID )
                #  InternalLF.g:591:6: (otherlv_21= RULE_ID )
                #  InternalLF.g:592:7: otherlv_21= RULE_ID
                if current == None:
                    current = createModelElement(self.grammarAccess.getReactorRule())
                otherlv_21 = match(input, self.RULE_ID, FOLLOW_22)
                newLeafNode(otherlv_21, self.grammarAccess.getReactorAccess().getSuperClassesReactorDeclCrossReference_8_1_0_0())
                #  InternalLF.g:603:5: (otherlv_22= ',' ( (otherlv_23= RULE_ID ) ) )*
                while True:
                    alt16 = 2
                    LA16_0 = input.LA(1)
                    if (LA16_0 == 18):
                        alt16 = 1
                    if alt16 == 1:
                        #  InternalLF.g:604:6: otherlv_22= ',' ( (otherlv_23= RULE_ID ) )
                        otherlv_22 = match(input, 18, FOLLOW_5)
                        newLeafNode(otherlv_22, self.grammarAccess.getReactorAccess().getCommaKeyword_8_1_1_0())
                        #  InternalLF.g:608:6: ( (otherlv_23= RULE_ID ) )
                        #  InternalLF.g:609:7: (otherlv_23= RULE_ID )
                        #  InternalLF.g:609:7: (otherlv_23= RULE_ID )
                        #  InternalLF.g:610:8: otherlv_23= RULE_ID
                        if current == None:
                            current = createModelElement(self.grammarAccess.getReactorRule())
                        otherlv_23 = match(input, self.RULE_ID, FOLLOW_22)
                        newLeafNode(otherlv_23, self.grammarAccess.getReactorAccess().getSuperClassesReactorDeclCrossReference_8_1_1_1_0())
                    else:
                    if not ((True)):
                        break
            otherlv_24 = match(input, 32, FOLLOW_23)
            newLeafNode(otherlv_24, self.grammarAccess.getReactorAccess().getLeftCurlyBracketKeyword_9())
            #  InternalLF.g:628:3: ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )*
            while True:
                alt18 = 12
                alt18 = dfa18.predict(input)
                if alt18 == 1:
                    #  InternalLF.g:629:4: ( (lv_preambles_25_0= rulePreamble ) )
                    #  InternalLF.g:629:4: ( (lv_preambles_25_0= rulePreamble ) )
                    #  InternalLF.g:630:5: (lv_preambles_25_0= rulePreamble )
                    #  InternalLF.g:630:5: (lv_preambles_25_0= rulePreamble )
                    #  InternalLF.g:631:6: lv_preambles_25_0= rulePreamble
                    newCompositeNode(self.grammarAccess.getReactorAccess().getPreamblesPreambleParserRuleCall_10_0_0())
                    pushFollow(FOLLOW_23)
                    lv_preambles_25_0 = rulePreamble()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "preambles", lv_preambles_25_0, "org.lflang.LF.Preamble")
                    afterParserOrEnumRuleCall()
                elif alt18 == 2:
                    #  InternalLF.g:649:4: ( (lv_stateVars_26_0= ruleStateVar ) )
                    #  InternalLF.g:649:4: ( (lv_stateVars_26_0= ruleStateVar ) )
                    #  InternalLF.g:650:5: (lv_stateVars_26_0= ruleStateVar )
                    #  InternalLF.g:650:5: (lv_stateVars_26_0= ruleStateVar )
                    #  InternalLF.g:651:6: lv_stateVars_26_0= ruleStateVar
                    newCompositeNode(self.grammarAccess.getReactorAccess().getStateVarsStateVarParserRuleCall_10_1_0())
                    pushFollow(FOLLOW_23)
                    lv_stateVars_26_0 = ruleStateVar()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "stateVars", lv_stateVars_26_0, "org.lflang.LF.StateVar")
                    afterParserOrEnumRuleCall()
                elif alt18 == 3:
                    #  InternalLF.g:669:4: ( (lv_methods_27_0= ruleMethod ) )
                    #  InternalLF.g:669:4: ( (lv_methods_27_0= ruleMethod ) )
                    #  InternalLF.g:670:5: (lv_methods_27_0= ruleMethod )
                    #  InternalLF.g:670:5: (lv_methods_27_0= ruleMethod )
                    #  InternalLF.g:671:6: lv_methods_27_0= ruleMethod
                    newCompositeNode(self.grammarAccess.getReactorAccess().getMethodsMethodParserRuleCall_10_2_0())
                    pushFollow(FOLLOW_23)
                    lv_methods_27_0 = ruleMethod()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "methods", lv_methods_27_0, "org.lflang.LF.Method")
                    afterParserOrEnumRuleCall()
                elif alt18 == 4:
                    #  InternalLF.g:689:4: ( (lv_inputs_28_0= ruleInput ) )
                    #  InternalLF.g:689:4: ( (lv_inputs_28_0= ruleInput ) )
                    #  InternalLF.g:690:5: (lv_inputs_28_0= ruleInput )
                    #  InternalLF.g:690:5: (lv_inputs_28_0= ruleInput )
                    #  InternalLF.g:691:6: lv_inputs_28_0= ruleInput
                    newCompositeNode(self.grammarAccess.getReactorAccess().getInputsInputParserRuleCall_10_3_0())
                    pushFollow(FOLLOW_23)
                    lv_inputs_28_0 = ruleInput()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "inputs", lv_inputs_28_0, "org.lflang.LF.Input")
                    afterParserOrEnumRuleCall()
                elif alt18 == 5:
                    #  InternalLF.g:709:4: ( (lv_outputs_29_0= ruleOutput ) )
                    #  InternalLF.g:709:4: ( (lv_outputs_29_0= ruleOutput ) )
                    #  InternalLF.g:710:5: (lv_outputs_29_0= ruleOutput )
                    #  InternalLF.g:710:5: (lv_outputs_29_0= ruleOutput )
                    #  InternalLF.g:711:6: lv_outputs_29_0= ruleOutput
                    newCompositeNode(self.grammarAccess.getReactorAccess().getOutputsOutputParserRuleCall_10_4_0())
                    pushFollow(FOLLOW_23)
                    lv_outputs_29_0 = ruleOutput()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "outputs", lv_outputs_29_0, "org.lflang.LF.Output")
                    afterParserOrEnumRuleCall()
                elif alt18 == 6:
                    #  InternalLF.g:729:4: ( (lv_timers_30_0= ruleTimer ) )
                    #  InternalLF.g:729:4: ( (lv_timers_30_0= ruleTimer ) )
                    #  InternalLF.g:730:5: (lv_timers_30_0= ruleTimer )
                    #  InternalLF.g:730:5: (lv_timers_30_0= ruleTimer )
                    #  InternalLF.g:731:6: lv_timers_30_0= ruleTimer
                    newCompositeNode(self.grammarAccess.getReactorAccess().getTimersTimerParserRuleCall_10_5_0())
                    pushFollow(FOLLOW_23)
                    lv_timers_30_0 = ruleTimer()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "timers", lv_timers_30_0, "org.lflang.LF.Timer")
                    afterParserOrEnumRuleCall()
                elif alt18 == 7:
                    #  InternalLF.g:749:4: ( (lv_actions_31_0= ruleAction ) )
                    #  InternalLF.g:749:4: ( (lv_actions_31_0= ruleAction ) )
                    #  InternalLF.g:750:5: (lv_actions_31_0= ruleAction )
                    #  InternalLF.g:750:5: (lv_actions_31_0= ruleAction )
                    #  InternalLF.g:751:6: lv_actions_31_0= ruleAction
                    newCompositeNode(self.grammarAccess.getReactorAccess().getActionsActionParserRuleCall_10_6_0())
                    pushFollow(FOLLOW_23)
                    lv_actions_31_0 = ruleAction()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "actions", lv_actions_31_0, "org.lflang.LF.Action")
                    afterParserOrEnumRuleCall()
                elif alt18 == 8:
                    #  InternalLF.g:769:4: ( (lv_instantiations_32_0= ruleInstantiation ) )
                    #  InternalLF.g:769:4: ( (lv_instantiations_32_0= ruleInstantiation ) )
                    #  InternalLF.g:770:5: (lv_instantiations_32_0= ruleInstantiation )
                    #  InternalLF.g:770:5: (lv_instantiations_32_0= ruleInstantiation )
                    #  InternalLF.g:771:6: lv_instantiations_32_0= ruleInstantiation
                    newCompositeNode(self.grammarAccess.getReactorAccess().getInstantiationsInstantiationParserRuleCall_10_7_0())
                    pushFollow(FOLLOW_23)
                    lv_instantiations_32_0 = ruleInstantiation()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "instantiations", lv_instantiations_32_0, "org.lflang.LF.Instantiation")
                    afterParserOrEnumRuleCall()
                elif alt18 == 9:
                    #  InternalLF.g:789:4: ( (lv_connections_33_0= ruleConnection ) )
                    #  InternalLF.g:789:4: ( (lv_connections_33_0= ruleConnection ) )
                    #  InternalLF.g:790:5: (lv_connections_33_0= ruleConnection )
                    #  InternalLF.g:790:5: (lv_connections_33_0= ruleConnection )
                    #  InternalLF.g:791:6: lv_connections_33_0= ruleConnection
                    newCompositeNode(self.grammarAccess.getReactorAccess().getConnectionsConnectionParserRuleCall_10_8_0())
                    pushFollow(FOLLOW_23)
                    lv_connections_33_0 = ruleConnection()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "connections", lv_connections_33_0, "org.lflang.LF.Connection")
                    afterParserOrEnumRuleCall()
                elif alt18 == 10:
                    #  InternalLF.g:809:4: ( (lv_reactions_34_0= ruleReaction ) )
                    #  InternalLF.g:809:4: ( (lv_reactions_34_0= ruleReaction ) )
                    #  InternalLF.g:810:5: (lv_reactions_34_0= ruleReaction )
                    #  InternalLF.g:810:5: (lv_reactions_34_0= ruleReaction )
                    #  InternalLF.g:811:6: lv_reactions_34_0= ruleReaction
                    newCompositeNode(self.grammarAccess.getReactorAccess().getReactionsReactionParserRuleCall_10_9_0())
                    pushFollow(FOLLOW_23)
                    lv_reactions_34_0 = ruleReaction()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "reactions", lv_reactions_34_0, "org.lflang.LF.Reaction")
                    afterParserOrEnumRuleCall()
                elif alt18 == 11:
                    #  InternalLF.g:829:4: ( (lv_modes_35_0= ruleMode ) )
                    #  InternalLF.g:829:4: ( (lv_modes_35_0= ruleMode ) )
                    #  InternalLF.g:830:5: (lv_modes_35_0= ruleMode )
                    #  InternalLF.g:830:5: (lv_modes_35_0= ruleMode )
                    #  InternalLF.g:831:6: lv_modes_35_0= ruleMode
                    newCompositeNode(self.grammarAccess.getReactorAccess().getModesModeParserRuleCall_10_10_0())
                    pushFollow(FOLLOW_23)
                    lv_modes_35_0 = ruleMode()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactorRule())
                    add(current, "modes", lv_modes_35_0, "org.lflang.LF.Mode")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            otherlv_36 = match(input, 33, FOLLOW_2)
            newLeafNode(otherlv_36, self.grammarAccess.getReactorAccess().getRightCurlyBracketKeyword_11())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleReactor"
    #  $ANTLR start "entryRuleTypeParm"
    #  InternalLF.g:857:1: entryRuleTypeParm returns [EObject current=null] : iv_ruleTypeParm= ruleTypeParm EOF ;
    def entryRuleTypeParm(self):
        """ generated source for method entryRuleTypeParm """
        current = None
        iv_ruleTypeParm = None
        try:
            #  InternalLF.g:857:49: (iv_ruleTypeParm= ruleTypeParm EOF )
            #  InternalLF.g:858:2: iv_ruleTypeParm= ruleTypeParm EOF
            newCompositeNode(self.grammarAccess.getTypeParmRule())
            pushFollow(FOLLOW_1)
            iv_ruleTypeParm = ruleTypeParm()
            state._fsp -= 1
            current = iv_ruleTypeParm
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTypeParm"
    #  $ANTLR start "ruleTypeParm"
    #  InternalLF.g:864:1: ruleTypeParm returns [EObject current=null] : ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) ) ;
    def ruleTypeParm(self):
        """ generated source for method ruleTypeParm """
        current = None
        lv_literal_0_0 = None
        lv_code_1_0 = None
        enterRule()
        try:
            #  InternalLF.g:870:2: ( ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) ) )
            #  InternalLF.g:871:2: ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) )
            #  InternalLF.g:871:2: ( ( (lv_literal_0_0= ruleTypeExpr ) ) | ( (lv_code_1_0= ruleCode ) ) )
            alt19 = 2
            LA19_0 = input.LA(1)
            if (LA19_0 == self.RULE_ID):
                alt19 = 1
            elif (LA19_0 == 71):
                alt19 = 2
            else:
                nvae = NoViableAltException("", 19, 0, input)
                raise nvae
            if alt19 == 1:
                #  InternalLF.g:872:3: ( (lv_literal_0_0= ruleTypeExpr ) )
                #  InternalLF.g:872:3: ( (lv_literal_0_0= ruleTypeExpr ) )
                #  InternalLF.g:873:4: (lv_literal_0_0= ruleTypeExpr )
                #  InternalLF.g:873:4: (lv_literal_0_0= ruleTypeExpr )
                #  InternalLF.g:874:5: lv_literal_0_0= ruleTypeExpr
                newCompositeNode(self.grammarAccess.getTypeParmAccess().getLiteralTypeExprParserRuleCall_0_0())
                pushFollow(FOLLOW_2)
                lv_literal_0_0 = ruleTypeExpr()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getTypeParmRule())
                set(current, "literal", lv_literal_0_0, "org.lflang.LF.TypeExpr")
                afterParserOrEnumRuleCall()
            elif alt19 == 2:
                #  InternalLF.g:892:3: ( (lv_code_1_0= ruleCode ) )
                #  InternalLF.g:892:3: ( (lv_code_1_0= ruleCode ) )
                #  InternalLF.g:893:4: (lv_code_1_0= ruleCode )
                #  InternalLF.g:893:4: (lv_code_1_0= ruleCode )
                #  InternalLF.g:894:5: lv_code_1_0= ruleCode
                newCompositeNode(self.grammarAccess.getTypeParmAccess().getCodeCodeParserRuleCall_1_0())
                pushFollow(FOLLOW_2)
                lv_code_1_0 = ruleCode()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getTypeParmRule())
                set(current, "code", lv_code_1_0, "org.lflang.LF.Code")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTypeParm"
    #  $ANTLR start "entryRuleTypeExpr"
    #  InternalLF.g:915:1: entryRuleTypeExpr returns [String current=null] : iv_ruleTypeExpr= ruleTypeExpr EOF ;
    def entryRuleTypeExpr(self):
        """ generated source for method entryRuleTypeExpr """
        current = None
        iv_ruleTypeExpr = None
        try:
            #  InternalLF.g:915:48: (iv_ruleTypeExpr= ruleTypeExpr EOF )
            #  InternalLF.g:916:2: iv_ruleTypeExpr= ruleTypeExpr EOF
            newCompositeNode(self.grammarAccess.getTypeExprRule())
            pushFollow(FOLLOW_1)
            iv_ruleTypeExpr = ruleTypeExpr()
            state._fsp -= 1
            current = iv_ruleTypeExpr.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTypeExpr"
    #  $ANTLR start "ruleTypeExpr"
    #  InternalLF.g:922:1: ruleTypeExpr returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID )+ ;
    def ruleTypeExpr(self):
        """ generated source for method ruleTypeExpr """
        current = AntlrDatatypeRuleToken()
        this_ID_0 = None
        enterRule()
        try:
            #  InternalLF.g:928:2: ( (this_ID_0= RULE_ID )+ )
            #  InternalLF.g:929:2: (this_ID_0= RULE_ID )+
            #  InternalLF.g:929:2: (this_ID_0= RULE_ID )+
            cnt20 = 0
            while True:
                alt20 = 2
                LA20_0 = input.LA(1)
                if (LA20_0 == self.RULE_ID):
                    alt20 = 1
                if alt20 == 1:
                    #  InternalLF.g:930:3: this_ID_0= RULE_ID
                    this_ID_0 = match(input, self.RULE_ID, FOLLOW_24)
                    current.merge(this_ID_0)
                    newLeafNode(this_ID_0, self.grammarAccess.getTypeExprAccess().getIDTerminalRuleCall())
                else:
                    if cnt20 >= 1:
                    eee = EarlyExitException(20, input)
                    raise eee
                cnt20 += 1
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTypeExpr"
    #  $ANTLR start "entryRuleTargetDecl"
    #  InternalLF.g:941:1: entryRuleTargetDecl returns [EObject current=null] : iv_ruleTargetDecl= ruleTargetDecl EOF ;
    def entryRuleTargetDecl(self):
        """ generated source for method entryRuleTargetDecl """
        current = None
        iv_ruleTargetDecl = None
        try:
            #  InternalLF.g:941:51: (iv_ruleTargetDecl= ruleTargetDecl EOF )
            #  InternalLF.g:942:2: iv_ruleTargetDecl= ruleTargetDecl EOF
            newCompositeNode(self.grammarAccess.getTargetDeclRule())
            pushFollow(FOLLOW_1)
            iv_ruleTargetDecl = ruleTargetDecl()
            state._fsp -= 1
            current = iv_ruleTargetDecl
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTargetDecl"
    #  $ANTLR start "ruleTargetDecl"
    #  InternalLF.g:948:1: ruleTargetDecl returns [EObject current=null] : (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? ) ;
    def ruleTargetDecl(self):
        """ generated source for method ruleTargetDecl """
        current = None
        otherlv_0 = None
        lv_name_1_0 = None
        otherlv_3 = None
        lv_config_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:954:2: ( (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? ) )
            #  InternalLF.g:955:2: (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? )
            #  InternalLF.g:955:2: (otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )? )
            #  InternalLF.g:956:3: otherlv_0= 'target' ( (lv_name_1_0= RULE_ID ) ) ( (lv_config_2_0= ruleKeyValuePairs ) )? (otherlv_3= ';' )?
            otherlv_0 = match(input, 34, FOLLOW_5)
            newLeafNode(otherlv_0, self.grammarAccess.getTargetDeclAccess().getTargetKeyword_0())
            #  InternalLF.g:960:3: ( (lv_name_1_0= RULE_ID ) )
            #  InternalLF.g:961:4: (lv_name_1_0= RULE_ID )
            #  InternalLF.g:961:4: (lv_name_1_0= RULE_ID )
            #  InternalLF.g:962:5: lv_name_1_0= RULE_ID
            lv_name_1_0 = match(input, self.RULE_ID, FOLLOW_25)
            newLeafNode(lv_name_1_0, self.grammarAccess.getTargetDeclAccess().getNameIDTerminalRuleCall_1_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getTargetDeclRule())
            setWithLastConsumed(current, "name", lv_name_1_0, "org.lflang.LF.ID")
            #  InternalLF.g:978:3: ( (lv_config_2_0= ruleKeyValuePairs ) )?
            alt21 = 2
            LA21_0 = input.LA(1)
            if (LA21_0 == 32):
                alt21 = 1
            if alt21 == 1:
                #  InternalLF.g:979:4: (lv_config_2_0= ruleKeyValuePairs )
                #  InternalLF.g:979:4: (lv_config_2_0= ruleKeyValuePairs )
                #  InternalLF.g:980:5: lv_config_2_0= ruleKeyValuePairs
                newCompositeNode(self.grammarAccess.getTargetDeclAccess().getConfigKeyValuePairsParserRuleCall_2_0())
                pushFollow(FOLLOW_8)
                lv_config_2_0 = ruleKeyValuePairs()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getTargetDeclRule())
                set(current, "config", lv_config_2_0, "org.lflang.LF.KeyValuePairs")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:997:3: (otherlv_3= ';' )?
            alt22 = 2
            LA22_0 = input.LA(1)
            if (LA22_0 == 20):
                alt22 = 1
            if alt22 == 1:
                #  InternalLF.g:998:4: otherlv_3= ';'
                otherlv_3 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_3, self.grammarAccess.getTargetDeclAccess().getSemicolonKeyword_3())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTargetDecl"
    #  $ANTLR start "entryRuleStateVar"
    #  InternalLF.g:1007:1: entryRuleStateVar returns [EObject current=null] : iv_ruleStateVar= ruleStateVar EOF ;
    def entryRuleStateVar(self):
        """ generated source for method entryRuleStateVar """
        current = None
        iv_ruleStateVar = None
        try:
            #  InternalLF.g:1007:49: (iv_ruleStateVar= ruleStateVar EOF )
            #  InternalLF.g:1008:2: iv_ruleStateVar= ruleStateVar EOF
            newCompositeNode(self.grammarAccess.getStateVarRule())
            pushFollow(FOLLOW_1)
            iv_ruleStateVar = ruleStateVar()
            state._fsp -= 1
            current = iv_ruleStateVar
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleStateVar"
    #  $ANTLR start "ruleStateVar"
    #  InternalLF.g:1014:1: ruleStateVar returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? ) ;
    def ruleStateVar(self):
        """ generated source for method ruleStateVar """
        current = None
        lv_reset_1_0 = None
        otherlv_2 = None
        lv_name_3_0 = None
        otherlv_4 = None
        lv_parens_6_0 = None
        otherlv_8 = None
        lv_parens_10_0 = None
        lv_braces_11_0 = None
        otherlv_13 = None
        lv_braces_15_0 = None
        otherlv_16 = None
        lv_attributes_0_0 = None
        lv_type_5_0 = None
        lv_init_7_0 = None
        lv_init_9_0 = None
        lv_init_12_0 = None
        lv_init_14_0 = None
        enterRule()
        try:
            #  InternalLF.g:1020:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? ) )
            #  InternalLF.g:1021:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? )
            #  InternalLF.g:1021:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )? )
            #  InternalLF.g:1022:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_reset_1_0= 'reset' ) )? otherlv_2= 'state' ( (lv_name_3_0= RULE_ID ) ) ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? ) (otherlv_16= ';' )?
            #  InternalLF.g:1022:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt23 = 2
                LA23_0 = input.LA(1)
                if (LA23_0 == 59):
                    alt23 = 1
                if alt23 == 1:
                    #  InternalLF.g:1023:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1023:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1024:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getStateVarAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_26)
                    lv_attributes_0_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getStateVarRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:1041:3: ( (lv_reset_1_0= 'reset' ) )?
            alt24 = 2
            LA24_0 = input.LA(1)
            if (LA24_0 == 35):
                alt24 = 1
            if alt24 == 1:
                #  InternalLF.g:1042:4: (lv_reset_1_0= 'reset' )
                #  InternalLF.g:1042:4: (lv_reset_1_0= 'reset' )
                #  InternalLF.g:1043:5: lv_reset_1_0= 'reset'
                lv_reset_1_0 = match(input, 35, FOLLOW_27)
                newLeafNode(lv_reset_1_0, self.grammarAccess.getStateVarAccess().getResetResetKeyword_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getStateVarRule())
                setWithLastConsumed(current, "reset", lv_reset_1_0 != None, "reset")
            otherlv_2 = match(input, 36, FOLLOW_5)
            newLeafNode(otherlv_2, self.grammarAccess.getStateVarAccess().getStateKeyword_2())
            #  InternalLF.g:1059:3: ( (lv_name_3_0= RULE_ID ) )
            #  InternalLF.g:1060:4: (lv_name_3_0= RULE_ID )
            #  InternalLF.g:1060:4: (lv_name_3_0= RULE_ID )
            #  InternalLF.g:1061:5: lv_name_3_0= RULE_ID
            lv_name_3_0 = match(input, self.RULE_ID, FOLLOW_28)
            newLeafNode(lv_name_3_0, self.grammarAccess.getStateVarAccess().getNameIDTerminalRuleCall_3_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getStateVarRule())
            setWithLastConsumed(current, "name", lv_name_3_0, "org.lflang.LF.ID")
            #  InternalLF.g:1077:3: ( (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )? )
            #  InternalLF.g:1078:4: (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )?
            #  InternalLF.g:1078:4: (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )?
            alt25 = 2
            LA25_0 = input.LA(1)
            if (LA25_0 == 37):
                alt25 = 1
            if alt25 == 1:
                #  InternalLF.g:1079:5: otherlv_4= ':' ( (lv_type_5_0= ruleType ) )
                otherlv_4 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_4, self.grammarAccess.getStateVarAccess().getColonKeyword_4_0_0())
                #  InternalLF.g:1083:5: ( (lv_type_5_0= ruleType ) )
                #  InternalLF.g:1084:6: (lv_type_5_0= ruleType )
                #  InternalLF.g:1084:6: (lv_type_5_0= ruleType )
                #  InternalLF.g:1085:7: lv_type_5_0= ruleType
                newCompositeNode(self.grammarAccess.getStateVarAccess().getTypeTypeParserRuleCall_4_0_1_0())
                pushFollow(FOLLOW_30)
                lv_type_5_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getStateVarRule())
                set(current, "type", lv_type_5_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:1103:4: ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )?
            alt30 = 3
            alt30 = dfa30.predict(input)
            if alt30 == 1:
                #  InternalLF.g:1104:5: ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) )
                #  InternalLF.g:1104:5: ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) )
                #  InternalLF.g:1105:6: ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) )
                #  InternalLF.g:1105:6: ( (lv_parens_6_0= '(' ) )
                #  InternalLF.g:1106:7: (lv_parens_6_0= '(' )
                #  InternalLF.g:1106:7: (lv_parens_6_0= '(' )
                #  InternalLF.g:1107:8: lv_parens_6_0= '('
                lv_parens_6_0 = match(input, 28, FOLLOW_31)
                newLeafNode(lv_parens_6_0, self.grammarAccess.getStateVarAccess().getParensLeftParenthesisKeyword_4_1_0_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getStateVarRule())
                addWithLastConsumed(current, "parens", lv_parens_6_0, "(")
                #  InternalLF.g:1119:6: ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )?
                alt27 = 2
                LA27_0 = input.LA(1)
                if ((LA27_0 >= self.RULE_STRING and LA27_0 <= self.RULE_CHAR_LIT) or LA27_0 == 62 or LA27_0 == 69 or LA27_0 == 71):
                    alt27 = 1
                if alt27 == 1:
                    #  InternalLF.g:1120:7: ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )*
                    #  InternalLF.g:1120:7: ( (lv_init_7_0= ruleExpression ) )
                    #  InternalLF.g:1121:8: (lv_init_7_0= ruleExpression )
                    #  InternalLF.g:1121:8: (lv_init_7_0= ruleExpression )
                    #  InternalLF.g:1122:9: lv_init_7_0= ruleExpression
                    newCompositeNode(self.grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_0_1_0_0())
                    pushFollow(FOLLOW_18)
                    lv_init_7_0 = ruleExpression()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getStateVarRule())
                    add(current, "init", lv_init_7_0, "org.lflang.LF.Expression")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:1139:7: (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )*
                    while True:
                        alt26 = 2
                        LA26_0 = input.LA(1)
                        if (LA26_0 == 18):
                            alt26 = 1
                        if alt26 == 1:
                            #  InternalLF.g:1140:8: otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) )
                            otherlv_8 = match(input, 18, FOLLOW_32)
                            newLeafNode(otherlv_8, self.grammarAccess.getStateVarAccess().getCommaKeyword_4_1_0_1_1_0())
                            #  InternalLF.g:1144:8: ( (lv_init_9_0= ruleExpression ) )
                            #  InternalLF.g:1145:9: (lv_init_9_0= ruleExpression )
                            #  InternalLF.g:1145:9: (lv_init_9_0= ruleExpression )
                            #  InternalLF.g:1146:10: lv_init_9_0= ruleExpression
                            newCompositeNode(self.grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_0_1_1_1_0())
                            pushFollow(FOLLOW_18)
                            lv_init_9_0 = ruleExpression()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getStateVarRule())
                            add(current, "init", lv_init_9_0, "org.lflang.LF.Expression")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                #  InternalLF.g:1165:6: ( (lv_parens_10_0= ')' ) )
                #  InternalLF.g:1166:7: (lv_parens_10_0= ')' )
                #  InternalLF.g:1166:7: (lv_parens_10_0= ')' )
                #  InternalLF.g:1167:8: lv_parens_10_0= ')'
                lv_parens_10_0 = match(input, 29, FOLLOW_8)
                newLeafNode(lv_parens_10_0, self.grammarAccess.getStateVarAccess().getParensRightParenthesisKeyword_4_1_0_2_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getStateVarRule())
                addWithLastConsumed(current, "parens", lv_parens_10_0, ")")
            elif alt30 == 2:
                #  InternalLF.g:1181:5: ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) )
                #  InternalLF.g:1181:5: ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) )
                #  InternalLF.g:1182:6: ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) )
                #  InternalLF.g:1182:6: ( (lv_braces_11_0= '{' ) )
                #  InternalLF.g:1183:7: (lv_braces_11_0= '{' )
                #  InternalLF.g:1183:7: (lv_braces_11_0= '{' )
                #  InternalLF.g:1184:8: lv_braces_11_0= '{'
                lv_braces_11_0 = match(input, 32, FOLLOW_33)
                newLeafNode(lv_braces_11_0, self.grammarAccess.getStateVarAccess().getBracesLeftCurlyBracketKeyword_4_1_1_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getStateVarRule())
                addWithLastConsumed(current, "braces", lv_braces_11_0, "{")
                #  InternalLF.g:1196:6: ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )?
                alt29 = 2
                LA29_0 = input.LA(1)
                if ((LA29_0 >= self.RULE_STRING and LA29_0 <= self.RULE_CHAR_LIT) or LA29_0 == 62 or LA29_0 == 69 or LA29_0 == 71):
                    alt29 = 1
                if alt29 == 1:
                    #  InternalLF.g:1197:7: ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )*
                    #  InternalLF.g:1197:7: ( (lv_init_12_0= ruleExpression ) )
                    #  InternalLF.g:1198:8: (lv_init_12_0= ruleExpression )
                    #  InternalLF.g:1198:8: (lv_init_12_0= ruleExpression )
                    #  InternalLF.g:1199:9: lv_init_12_0= ruleExpression
                    newCompositeNode(self.grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_1_1_0_0())
                    pushFollow(FOLLOW_34)
                    lv_init_12_0 = ruleExpression()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getStateVarRule())
                    add(current, "init", lv_init_12_0, "org.lflang.LF.Expression")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:1216:7: (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )*
                    while True:
                        alt28 = 2
                        LA28_0 = input.LA(1)
                        if (LA28_0 == 18):
                            alt28 = 1
                        if alt28 == 1:
                            #  InternalLF.g:1217:8: otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) )
                            otherlv_13 = match(input, 18, FOLLOW_32)
                            newLeafNode(otherlv_13, self.grammarAccess.getStateVarAccess().getCommaKeyword_4_1_1_1_1_0())
                            #  InternalLF.g:1221:8: ( (lv_init_14_0= ruleExpression ) )
                            #  InternalLF.g:1222:9: (lv_init_14_0= ruleExpression )
                            #  InternalLF.g:1222:9: (lv_init_14_0= ruleExpression )
                            #  InternalLF.g:1223:10: lv_init_14_0= ruleExpression
                            newCompositeNode(self.grammarAccess.getStateVarAccess().getInitExpressionParserRuleCall_4_1_1_1_1_1_0())
                            pushFollow(FOLLOW_34)
                            lv_init_14_0 = ruleExpression()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getStateVarRule())
                            add(current, "init", lv_init_14_0, "org.lflang.LF.Expression")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                #  InternalLF.g:1242:6: ( (lv_braces_15_0= '}' ) )
                #  InternalLF.g:1243:7: (lv_braces_15_0= '}' )
                #  InternalLF.g:1243:7: (lv_braces_15_0= '}' )
                #  InternalLF.g:1244:8: lv_braces_15_0= '}'
                lv_braces_15_0 = match(input, 33, FOLLOW_8)
                newLeafNode(lv_braces_15_0, self.grammarAccess.getStateVarAccess().getBracesRightCurlyBracketKeyword_4_1_1_2_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getStateVarRule())
                addWithLastConsumed(current, "braces", lv_braces_15_0, "}")
            #  InternalLF.g:1259:3: (otherlv_16= ';' )?
            alt31 = 2
            LA31_0 = input.LA(1)
            if (LA31_0 == 20):
                alt31 = 1
            if alt31 == 1:
                #  InternalLF.g:1260:4: otherlv_16= ';'
                otherlv_16 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_16, self.grammarAccess.getStateVarAccess().getSemicolonKeyword_5())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleStateVar"
    #  $ANTLR start "entryRuleMethod"
    #  InternalLF.g:1269:1: entryRuleMethod returns [EObject current=null] : iv_ruleMethod= ruleMethod EOF ;
    def entryRuleMethod(self):
        """ generated source for method entryRuleMethod """
        current = None
        iv_ruleMethod = None
        try:
            #  InternalLF.g:1269:47: (iv_ruleMethod= ruleMethod EOF )
            #  InternalLF.g:1270:2: iv_ruleMethod= ruleMethod EOF
            newCompositeNode(self.grammarAccess.getMethodRule())
            pushFollow(FOLLOW_1)
            iv_ruleMethod = ruleMethod()
            state._fsp -= 1
            current = iv_ruleMethod
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleMethod"
    #  $ANTLR start "ruleMethod"
    #  InternalLF.g:1276:1: ruleMethod returns [EObject current=null] : ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? ) ;
    def ruleMethod(self):
        """ generated source for method ruleMethod """
        current = None
        lv_const_0_0 = None
        otherlv_1 = None
        lv_name_2_0 = None
        otherlv_3 = None
        otherlv_5 = None
        otherlv_7 = None
        otherlv_8 = None
        otherlv_11 = None
        lv_arguments_4_0 = None
        lv_arguments_6_0 = None
        lv_return_9_0 = None
        lv_code_10_0 = None
        enterRule()
        try:
            #  InternalLF.g:1282:2: ( ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? ) )
            #  InternalLF.g:1283:2: ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? )
            #  InternalLF.g:1283:2: ( ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )? )
            #  InternalLF.g:1284:3: ( (lv_const_0_0= 'const' ) )? otherlv_1= 'method' ( (lv_name_2_0= RULE_ID ) ) otherlv_3= '(' ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )? otherlv_7= ')' (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )? ( (lv_code_10_0= ruleCode ) ) (otherlv_11= ';' )?
            #  InternalLF.g:1284:3: ( (lv_const_0_0= 'const' ) )?
            alt32 = 2
            LA32_0 = input.LA(1)
            if (LA32_0 == 38):
                alt32 = 1
            if alt32 == 1:
                #  InternalLF.g:1285:4: (lv_const_0_0= 'const' )
                #  InternalLF.g:1285:4: (lv_const_0_0= 'const' )
                #  InternalLF.g:1286:5: lv_const_0_0= 'const'
                lv_const_0_0 = match(input, 38, FOLLOW_35)
                newLeafNode(lv_const_0_0, self.grammarAccess.getMethodAccess().getConstConstKeyword_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getMethodRule())
                setWithLastConsumed(current, "const", lv_const_0_0 != None, "const")
            otherlv_1 = match(input, 39, FOLLOW_5)
            newLeafNode(otherlv_1, self.grammarAccess.getMethodAccess().getMethodKeyword_1())
            #  InternalLF.g:1302:3: ( (lv_name_2_0= RULE_ID ) )
            #  InternalLF.g:1303:4: (lv_name_2_0= RULE_ID )
            #  InternalLF.g:1303:4: (lv_name_2_0= RULE_ID )
            #  InternalLF.g:1304:5: lv_name_2_0= RULE_ID
            lv_name_2_0 = match(input, self.RULE_ID, FOLLOW_36)
            newLeafNode(lv_name_2_0, self.grammarAccess.getMethodAccess().getNameIDTerminalRuleCall_2_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getMethodRule())
            setWithLastConsumed(current, "name", lv_name_2_0, "org.lflang.LF.ID")
            otherlv_3 = match(input, 28, FOLLOW_37)
            newLeafNode(otherlv_3, self.grammarAccess.getMethodAccess().getLeftParenthesisKeyword_3())
            #  InternalLF.g:1324:3: ( ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )* )?
            alt34 = 2
            LA34_0 = input.LA(1)
            if (LA34_0 == self.RULE_ID):
                alt34 = 1
            if alt34 == 1:
                #  InternalLF.g:1325:4: ( (lv_arguments_4_0= ruleMethodArgument ) ) (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )*
                #  InternalLF.g:1325:4: ( (lv_arguments_4_0= ruleMethodArgument ) )
                #  InternalLF.g:1326:5: (lv_arguments_4_0= ruleMethodArgument )
                #  InternalLF.g:1326:5: (lv_arguments_4_0= ruleMethodArgument )
                #  InternalLF.g:1327:6: lv_arguments_4_0= ruleMethodArgument
                newCompositeNode(self.grammarAccess.getMethodAccess().getArgumentsMethodArgumentParserRuleCall_4_0_0())
                pushFollow(FOLLOW_18)
                lv_arguments_4_0 = ruleMethodArgument()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getMethodRule())
                add(current, "arguments", lv_arguments_4_0, "org.lflang.LF.MethodArgument")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:1344:4: (otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) ) )*
                while True:
                    alt33 = 2
                    LA33_0 = input.LA(1)
                    if (LA33_0 == 18):
                        alt33 = 1
                    if alt33 == 1:
                        #  InternalLF.g:1345:5: otherlv_5= ',' ( (lv_arguments_6_0= ruleMethodArgument ) )
                        otherlv_5 = match(input, 18, FOLLOW_5)
                        newLeafNode(otherlv_5, self.grammarAccess.getMethodAccess().getCommaKeyword_4_1_0())
                        #  InternalLF.g:1349:5: ( (lv_arguments_6_0= ruleMethodArgument ) )
                        #  InternalLF.g:1350:6: (lv_arguments_6_0= ruleMethodArgument )
                        #  InternalLF.g:1350:6: (lv_arguments_6_0= ruleMethodArgument )
                        #  InternalLF.g:1351:7: lv_arguments_6_0= ruleMethodArgument
                        newCompositeNode(self.grammarAccess.getMethodAccess().getArgumentsMethodArgumentParserRuleCall_4_1_1_0())
                        pushFollow(FOLLOW_18)
                        lv_arguments_6_0 = ruleMethodArgument()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getMethodRule())
                        add(current, "arguments", lv_arguments_6_0, "org.lflang.LF.MethodArgument")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
            otherlv_7 = match(input, 29, FOLLOW_38)
            newLeafNode(otherlv_7, self.grammarAccess.getMethodAccess().getRightParenthesisKeyword_5())
            #  InternalLF.g:1374:3: (otherlv_8= ':' ( (lv_return_9_0= ruleType ) ) )?
            alt35 = 2
            LA35_0 = input.LA(1)
            if (LA35_0 == 37):
                alt35 = 1
            if alt35 == 1:
                #  InternalLF.g:1375:4: otherlv_8= ':' ( (lv_return_9_0= ruleType ) )
                otherlv_8 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_8, self.grammarAccess.getMethodAccess().getColonKeyword_6_0())
                #  InternalLF.g:1379:4: ( (lv_return_9_0= ruleType ) )
                #  InternalLF.g:1380:5: (lv_return_9_0= ruleType )
                #  InternalLF.g:1380:5: (lv_return_9_0= ruleType )
                #  InternalLF.g:1381:6: lv_return_9_0= ruleType
                newCompositeNode(self.grammarAccess.getMethodAccess().getReturnTypeParserRuleCall_6_1_0())
                pushFollow(FOLLOW_14)
                lv_return_9_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getMethodRule())
                set(current, "return", lv_return_9_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:1399:3: ( (lv_code_10_0= ruleCode ) )
            #  InternalLF.g:1400:4: (lv_code_10_0= ruleCode )
            #  InternalLF.g:1400:4: (lv_code_10_0= ruleCode )
            #  InternalLF.g:1401:5: lv_code_10_0= ruleCode
            newCompositeNode(self.grammarAccess.getMethodAccess().getCodeCodeParserRuleCall_7_0())
            pushFollow(FOLLOW_8)
            lv_code_10_0 = ruleCode()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getMethodRule())
            set(current, "code", lv_code_10_0, "org.lflang.LF.Code")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:1418:3: (otherlv_11= ';' )?
            alt36 = 2
            LA36_0 = input.LA(1)
            if (LA36_0 == 20):
                alt36 = 1
            if alt36 == 1:
                #  InternalLF.g:1419:4: otherlv_11= ';'
                otherlv_11 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_11, self.grammarAccess.getMethodAccess().getSemicolonKeyword_8())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleMethod"
    #  $ANTLR start "entryRuleMethodArgument"
    #  InternalLF.g:1428:1: entryRuleMethodArgument returns [EObject current=null] : iv_ruleMethodArgument= ruleMethodArgument EOF ;
    def entryRuleMethodArgument(self):
        """ generated source for method entryRuleMethodArgument """
        current = None
        iv_ruleMethodArgument = None
        try:
            #  InternalLF.g:1428:55: (iv_ruleMethodArgument= ruleMethodArgument EOF )
            #  InternalLF.g:1429:2: iv_ruleMethodArgument= ruleMethodArgument EOF
            newCompositeNode(self.grammarAccess.getMethodArgumentRule())
            pushFollow(FOLLOW_1)
            iv_ruleMethodArgument = ruleMethodArgument()
            state._fsp -= 1
            current = iv_ruleMethodArgument
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleMethodArgument"
    #  $ANTLR start "ruleMethodArgument"
    #  InternalLF.g:1435:1: ruleMethodArgument returns [EObject current=null] : ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? ) ;
    def ruleMethodArgument(self):
        """ generated source for method ruleMethodArgument """
        current = None
        lv_name_0_0 = None
        otherlv_1 = None
        lv_type_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:1441:2: ( ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? ) )
            #  InternalLF.g:1442:2: ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? )
            #  InternalLF.g:1442:2: ( ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )? )
            #  InternalLF.g:1443:3: ( (lv_name_0_0= RULE_ID ) ) (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )?
            #  InternalLF.g:1443:3: ( (lv_name_0_0= RULE_ID ) )
            #  InternalLF.g:1444:4: (lv_name_0_0= RULE_ID )
            #  InternalLF.g:1444:4: (lv_name_0_0= RULE_ID )
            #  InternalLF.g:1445:5: lv_name_0_0= RULE_ID
            lv_name_0_0 = match(input, self.RULE_ID, FOLLOW_39)
            newLeafNode(lv_name_0_0, self.grammarAccess.getMethodArgumentAccess().getNameIDTerminalRuleCall_0_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getMethodArgumentRule())
            setWithLastConsumed(current, "name", lv_name_0_0, "org.lflang.LF.ID")
            #  InternalLF.g:1461:3: (otherlv_1= ':' ( (lv_type_2_0= ruleType ) ) )?
            alt37 = 2
            LA37_0 = input.LA(1)
            if (LA37_0 == 37):
                alt37 = 1
            if alt37 == 1:
                #  InternalLF.g:1462:4: otherlv_1= ':' ( (lv_type_2_0= ruleType ) )
                otherlv_1 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_1, self.grammarAccess.getMethodArgumentAccess().getColonKeyword_1_0())
                #  InternalLF.g:1466:4: ( (lv_type_2_0= ruleType ) )
                #  InternalLF.g:1467:5: (lv_type_2_0= ruleType )
                #  InternalLF.g:1467:5: (lv_type_2_0= ruleType )
                #  InternalLF.g:1468:6: lv_type_2_0= ruleType
                newCompositeNode(self.grammarAccess.getMethodArgumentAccess().getTypeTypeParserRuleCall_1_1_0())
                pushFollow(FOLLOW_2)
                lv_type_2_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getMethodArgumentRule())
                set(current, "type", lv_type_2_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleMethodArgument"
    #  $ANTLR start "entryRuleInput"
    #  InternalLF.g:1490:1: entryRuleInput returns [EObject current=null] : iv_ruleInput= ruleInput EOF ;
    def entryRuleInput(self):
        """ generated source for method entryRuleInput """
        current = None
        iv_ruleInput = None
        try:
            #  InternalLF.g:1490:46: (iv_ruleInput= ruleInput EOF )
            #  InternalLF.g:1491:2: iv_ruleInput= ruleInput EOF
            newCompositeNode(self.grammarAccess.getInputRule())
            pushFollow(FOLLOW_1)
            iv_ruleInput = ruleInput()
            state._fsp -= 1
            current = iv_ruleInput
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleInput"
    #  $ANTLR start "ruleInput"
    #  InternalLF.g:1497:1: ruleInput returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? ) ;
    def ruleInput(self):
        """ generated source for method ruleInput """
        current = None
        lv_mutable_1_0 = None
        otherlv_2 = None
        lv_name_4_0 = None
        otherlv_5 = None
        otherlv_7 = None
        lv_attributes_0_0 = None
        lv_widthSpec_3_0 = None
        lv_type_6_0 = None
        enterRule()
        try:
            #  InternalLF.g:1503:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? ) )
            #  InternalLF.g:1504:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? )
            #  InternalLF.g:1504:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )? )
            #  InternalLF.g:1505:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_mutable_1_0= 'mutable' ) )? otherlv_2= 'input' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (lv_name_4_0= RULE_ID ) ) (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )? (otherlv_7= ';' )?
            #  InternalLF.g:1505:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt38 = 2
                LA38_0 = input.LA(1)
                if (LA38_0 == 59):
                    alt38 = 1
                if alt38 == 1:
                    #  InternalLF.g:1506:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1506:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1507:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getInputAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_40)
                    lv_attributes_0_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getInputRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:1524:3: ( (lv_mutable_1_0= 'mutable' ) )?
            alt39 = 2
            LA39_0 = input.LA(1)
            if (LA39_0 == 40):
                alt39 = 1
            if alt39 == 1:
                #  InternalLF.g:1525:4: (lv_mutable_1_0= 'mutable' )
                #  InternalLF.g:1525:4: (lv_mutable_1_0= 'mutable' )
                #  InternalLF.g:1526:5: lv_mutable_1_0= 'mutable'
                lv_mutable_1_0 = match(input, 40, FOLLOW_41)
                newLeafNode(lv_mutable_1_0, self.grammarAccess.getInputAccess().getMutableMutableKeyword_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getInputRule())
                setWithLastConsumed(current, "mutable", lv_mutable_1_0 != None, "mutable")
            otherlv_2 = match(input, 41, FOLLOW_42)
            newLeafNode(otherlv_2, self.grammarAccess.getInputAccess().getInputKeyword_2())
            #  InternalLF.g:1542:3: ( (lv_widthSpec_3_0= ruleWidthSpec ) )?
            alt40 = 2
            LA40_0 = input.LA(1)
            if (LA40_0 == 60):
                alt40 = 1
            if alt40 == 1:
                #  InternalLF.g:1543:4: (lv_widthSpec_3_0= ruleWidthSpec )
                #  InternalLF.g:1543:4: (lv_widthSpec_3_0= ruleWidthSpec )
                #  InternalLF.g:1544:5: lv_widthSpec_3_0= ruleWidthSpec
                newCompositeNode(self.grammarAccess.getInputAccess().getWidthSpecWidthSpecParserRuleCall_3_0())
                pushFollow(FOLLOW_5)
                lv_widthSpec_3_0 = ruleWidthSpec()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getInputRule())
                set(current, "widthSpec", lv_widthSpec_3_0, "org.lflang.LF.WidthSpec")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:1561:3: ( (lv_name_4_0= RULE_ID ) )
            #  InternalLF.g:1562:4: (lv_name_4_0= RULE_ID )
            #  InternalLF.g:1562:4: (lv_name_4_0= RULE_ID )
            #  InternalLF.g:1563:5: lv_name_4_0= RULE_ID
            lv_name_4_0 = match(input, self.RULE_ID, FOLLOW_43)
            newLeafNode(lv_name_4_0, self.grammarAccess.getInputAccess().getNameIDTerminalRuleCall_4_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getInputRule())
            setWithLastConsumed(current, "name", lv_name_4_0, "org.lflang.LF.ID")
            #  InternalLF.g:1579:3: (otherlv_5= ':' ( (lv_type_6_0= ruleType ) ) )?
            alt41 = 2
            LA41_0 = input.LA(1)
            if (LA41_0 == 37):
                alt41 = 1
            if alt41 == 1:
                #  InternalLF.g:1580:4: otherlv_5= ':' ( (lv_type_6_0= ruleType ) )
                otherlv_5 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_5, self.grammarAccess.getInputAccess().getColonKeyword_5_0())
                #  InternalLF.g:1584:4: ( (lv_type_6_0= ruleType ) )
                #  InternalLF.g:1585:5: (lv_type_6_0= ruleType )
                #  InternalLF.g:1585:5: (lv_type_6_0= ruleType )
                #  InternalLF.g:1586:6: lv_type_6_0= ruleType
                newCompositeNode(self.grammarAccess.getInputAccess().getTypeTypeParserRuleCall_5_1_0())
                pushFollow(FOLLOW_8)
                lv_type_6_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getInputRule())
                set(current, "type", lv_type_6_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:1604:3: (otherlv_7= ';' )?
            alt42 = 2
            LA42_0 = input.LA(1)
            if (LA42_0 == 20):
                alt42 = 1
            if alt42 == 1:
                #  InternalLF.g:1605:4: otherlv_7= ';'
                otherlv_7 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_7, self.grammarAccess.getInputAccess().getSemicolonKeyword_6())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleInput"
    #  $ANTLR start "entryRuleOutput"
    #  InternalLF.g:1614:1: entryRuleOutput returns [EObject current=null] : iv_ruleOutput= ruleOutput EOF ;
    def entryRuleOutput(self):
        """ generated source for method entryRuleOutput """
        current = None
        iv_ruleOutput = None
        try:
            #  InternalLF.g:1614:47: (iv_ruleOutput= ruleOutput EOF )
            #  InternalLF.g:1615:2: iv_ruleOutput= ruleOutput EOF
            newCompositeNode(self.grammarAccess.getOutputRule())
            pushFollow(FOLLOW_1)
            iv_ruleOutput = ruleOutput()
            state._fsp -= 1
            current = iv_ruleOutput
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleOutput"
    #  $ANTLR start "ruleOutput"
    #  InternalLF.g:1621:1: ruleOutput returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? ) ;
    def ruleOutput(self):
        """ generated source for method ruleOutput """
        current = None
        otherlv_1 = None
        lv_name_3_0 = None
        otherlv_4 = None
        otherlv_6 = None
        lv_attributes_0_0 = None
        lv_widthSpec_2_0 = None
        lv_type_5_0 = None
        enterRule()
        try:
            #  InternalLF.g:1627:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? ) )
            #  InternalLF.g:1628:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? )
            #  InternalLF.g:1628:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )? )
            #  InternalLF.g:1629:3: ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'output' ( (lv_widthSpec_2_0= ruleWidthSpec ) )? ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )? (otherlv_6= ';' )?
            #  InternalLF.g:1629:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt43 = 2
                LA43_0 = input.LA(1)
                if (LA43_0 == 59):
                    alt43 = 1
                if alt43 == 1:
                    #  InternalLF.g:1630:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1630:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1631:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getOutputAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_44)
                    lv_attributes_0_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getOutputRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            otherlv_1 = match(input, 42, FOLLOW_42)
            newLeafNode(otherlv_1, self.grammarAccess.getOutputAccess().getOutputKeyword_1())
            #  InternalLF.g:1652:3: ( (lv_widthSpec_2_0= ruleWidthSpec ) )?
            alt44 = 2
            LA44_0 = input.LA(1)
            if (LA44_0 == 60):
                alt44 = 1
            if alt44 == 1:
                #  InternalLF.g:1653:4: (lv_widthSpec_2_0= ruleWidthSpec )
                #  InternalLF.g:1653:4: (lv_widthSpec_2_0= ruleWidthSpec )
                #  InternalLF.g:1654:5: lv_widthSpec_2_0= ruleWidthSpec
                newCompositeNode(self.grammarAccess.getOutputAccess().getWidthSpecWidthSpecParserRuleCall_2_0())
                pushFollow(FOLLOW_5)
                lv_widthSpec_2_0 = ruleWidthSpec()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getOutputRule())
                set(current, "widthSpec", lv_widthSpec_2_0, "org.lflang.LF.WidthSpec")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:1671:3: ( (lv_name_3_0= RULE_ID ) )
            #  InternalLF.g:1672:4: (lv_name_3_0= RULE_ID )
            #  InternalLF.g:1672:4: (lv_name_3_0= RULE_ID )
            #  InternalLF.g:1673:5: lv_name_3_0= RULE_ID
            lv_name_3_0 = match(input, self.RULE_ID, FOLLOW_43)
            newLeafNode(lv_name_3_0, self.grammarAccess.getOutputAccess().getNameIDTerminalRuleCall_3_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getOutputRule())
            setWithLastConsumed(current, "name", lv_name_3_0, "org.lflang.LF.ID")
            #  InternalLF.g:1689:3: (otherlv_4= ':' ( (lv_type_5_0= ruleType ) ) )?
            alt45 = 2
            LA45_0 = input.LA(1)
            if (LA45_0 == 37):
                alt45 = 1
            if alt45 == 1:
                #  InternalLF.g:1690:4: otherlv_4= ':' ( (lv_type_5_0= ruleType ) )
                otherlv_4 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_4, self.grammarAccess.getOutputAccess().getColonKeyword_4_0())
                #  InternalLF.g:1694:4: ( (lv_type_5_0= ruleType ) )
                #  InternalLF.g:1695:5: (lv_type_5_0= ruleType )
                #  InternalLF.g:1695:5: (lv_type_5_0= ruleType )
                #  InternalLF.g:1696:6: lv_type_5_0= ruleType
                newCompositeNode(self.grammarAccess.getOutputAccess().getTypeTypeParserRuleCall_4_1_0())
                pushFollow(FOLLOW_8)
                lv_type_5_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getOutputRule())
                set(current, "type", lv_type_5_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:1714:3: (otherlv_6= ';' )?
            alt46 = 2
            LA46_0 = input.LA(1)
            if (LA46_0 == 20):
                alt46 = 1
            if alt46 == 1:
                #  InternalLF.g:1715:4: otherlv_6= ';'
                otherlv_6 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_6, self.grammarAccess.getOutputAccess().getSemicolonKeyword_5())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleOutput"
    #  $ANTLR start "entryRuleTimer"
    #  InternalLF.g:1724:1: entryRuleTimer returns [EObject current=null] : iv_ruleTimer= ruleTimer EOF ;
    def entryRuleTimer(self):
        """ generated source for method entryRuleTimer """
        current = None
        iv_ruleTimer = None
        try:
            #  InternalLF.g:1724:46: (iv_ruleTimer= ruleTimer EOF )
            #  InternalLF.g:1725:2: iv_ruleTimer= ruleTimer EOF
            newCompositeNode(self.grammarAccess.getTimerRule())
            pushFollow(FOLLOW_1)
            iv_ruleTimer = ruleTimer()
            state._fsp -= 1
            current = iv_ruleTimer
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTimer"
    #  $ANTLR start "ruleTimer"
    #  InternalLF.g:1731:1: ruleTimer returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? ) ;
    def ruleTimer(self):
        """ generated source for method ruleTimer """
        current = None
        otherlv_1 = None
        lv_name_2_0 = None
        otherlv_3 = None
        otherlv_5 = None
        otherlv_7 = None
        otherlv_8 = None
        lv_attributes_0_0 = None
        lv_offset_4_0 = None
        lv_period_6_0 = None
        enterRule()
        try:
            #  InternalLF.g:1737:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? ) )
            #  InternalLF.g:1738:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? )
            #  InternalLF.g:1738:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )? )
            #  InternalLF.g:1739:3: ( (lv_attributes_0_0= ruleAttribute ) )* otherlv_1= 'timer' ( (lv_name_2_0= RULE_ID ) ) (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )? (otherlv_8= ';' )?
            #  InternalLF.g:1739:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt47 = 2
                LA47_0 = input.LA(1)
                if (LA47_0 == 59):
                    alt47 = 1
                if alt47 == 1:
                    #  InternalLF.g:1740:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1740:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:1741:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getTimerAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_45)
                    lv_attributes_0_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getTimerRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            otherlv_1 = match(input, 43, FOLLOW_5)
            newLeafNode(otherlv_1, self.grammarAccess.getTimerAccess().getTimerKeyword_1())
            #  InternalLF.g:1762:3: ( (lv_name_2_0= RULE_ID ) )
            #  InternalLF.g:1763:4: (lv_name_2_0= RULE_ID )
            #  InternalLF.g:1763:4: (lv_name_2_0= RULE_ID )
            #  InternalLF.g:1764:5: lv_name_2_0= RULE_ID
            lv_name_2_0 = match(input, self.RULE_ID, FOLLOW_46)
            newLeafNode(lv_name_2_0, self.grammarAccess.getTimerAccess().getNameIDTerminalRuleCall_2_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getTimerRule())
            setWithLastConsumed(current, "name", lv_name_2_0, "org.lflang.LF.ID")
            #  InternalLF.g:1780:3: (otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')' )?
            alt49 = 2
            LA49_0 = input.LA(1)
            if (LA49_0 == 28):
                LA49_1 = input.LA(2)
                if (LA49_1 == self.RULE_ID):
                    LA49_3 = input.LA(3)
                    if (LA49_3 == 18):
                        LA49_5 = input.LA(4)
                        if (LA49_5 == self.RULE_ID):
                            LA49_7 = input.LA(5)
                            if (LA49_7 == 29):
                                LA49_6 = input.LA(6)
                                if (LA49_6 == self.EOF or LA49_6 == self.RULE_ID or LA49_6 == 20 or LA49_6 == 28 or LA49_6 == 33 or (LA49_6 >= 35 and LA49_6 <= 36) or (LA49_6 >= 38 and LA49_6 <= 48) or LA49_6 == 52 or LA49_6 == 59 or LA49_6 == 63 or LA49_6 == 68 or (LA49_6 >= 81 and LA49_6 <= 83) or LA49_6 == 85):
                                    alt49 = 1
                        elif (LA49_5 == self.RULE_STRING or (LA49_5 >= self.RULE_TRUE and LA49_5 <= self.RULE_CHAR_LIT) or LA49_5 == 62 or LA49_5 == 69 or LA49_5 == 71):
                            alt49 = 1
                    elif (LA49_3 == 29):
                        LA49_6 = input.LA(4)
                        if (LA49_6 == self.EOF or LA49_6 == self.RULE_ID or LA49_6 == 20 or LA49_6 == 28 or LA49_6 == 33 or (LA49_6 >= 35 and LA49_6 <= 36) or (LA49_6 >= 38 and LA49_6 <= 48) or LA49_6 == 52 or LA49_6 == 59 or LA49_6 == 63 or LA49_6 == 68 or (LA49_6 >= 81 and LA49_6 <= 83) or LA49_6 == 85):
                            alt49 = 1
                elif (LA49_1 == self.RULE_STRING or (LA49_1 >= self.RULE_TRUE and LA49_1 <= self.RULE_CHAR_LIT) or LA49_1 == 62 or LA49_1 == 69 or LA49_1 == 71):
                    alt49 = 1
            if alt49 == 1:
                #  InternalLF.g:1781:4: otherlv_3= '(' ( (lv_offset_4_0= ruleExpression ) ) (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )? otherlv_7= ')'
                otherlv_3 = match(input, 28, FOLLOW_32)
                newLeafNode(otherlv_3, self.grammarAccess.getTimerAccess().getLeftParenthesisKeyword_3_0())
                #  InternalLF.g:1785:4: ( (lv_offset_4_0= ruleExpression ) )
                #  InternalLF.g:1786:5: (lv_offset_4_0= ruleExpression )
                #  InternalLF.g:1786:5: (lv_offset_4_0= ruleExpression )
                #  InternalLF.g:1787:6: lv_offset_4_0= ruleExpression
                newCompositeNode(self.grammarAccess.getTimerAccess().getOffsetExpressionParserRuleCall_3_1_0())
                pushFollow(FOLLOW_18)
                lv_offset_4_0 = ruleExpression()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getTimerRule())
                set(current, "offset", lv_offset_4_0, "org.lflang.LF.Expression")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:1804:4: (otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) ) )?
                alt48 = 2
                LA48_0 = input.LA(1)
                if (LA48_0 == 18):
                    alt48 = 1
                if alt48 == 1:
                    #  InternalLF.g:1805:5: otherlv_5= ',' ( (lv_period_6_0= ruleExpression ) )
                    otherlv_5 = match(input, 18, FOLLOW_32)
                    newLeafNode(otherlv_5, self.grammarAccess.getTimerAccess().getCommaKeyword_3_2_0())
                    #  InternalLF.g:1809:5: ( (lv_period_6_0= ruleExpression ) )
                    #  InternalLF.g:1810:6: (lv_period_6_0= ruleExpression )
                    #  InternalLF.g:1810:6: (lv_period_6_0= ruleExpression )
                    #  InternalLF.g:1811:7: lv_period_6_0= ruleExpression
                    newCompositeNode(self.grammarAccess.getTimerAccess().getPeriodExpressionParserRuleCall_3_2_1_0())
                    pushFollow(FOLLOW_47)
                    lv_period_6_0 = ruleExpression()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getTimerRule())
                    set(current, "period", lv_period_6_0, "org.lflang.LF.Expression")
                    afterParserOrEnumRuleCall()
                otherlv_7 = match(input, 29, FOLLOW_8)
                newLeafNode(otherlv_7, self.grammarAccess.getTimerAccess().getRightParenthesisKeyword_3_3())
            #  InternalLF.g:1834:3: (otherlv_8= ';' )?
            alt50 = 2
            LA50_0 = input.LA(1)
            if (LA50_0 == 20):
                alt50 = 1
            if alt50 == 1:
                #  InternalLF.g:1835:4: otherlv_8= ';'
                otherlv_8 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_8, self.grammarAccess.getTimerAccess().getSemicolonKeyword_4())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTimer"
    #  $ANTLR start "entryRuleBoolean"
    #  InternalLF.g:1844:1: entryRuleBoolean returns [String current=null] : iv_ruleBoolean= ruleBoolean EOF ;
    def entryRuleBoolean(self):
        """ generated source for method entryRuleBoolean """
        current = None
        iv_ruleBoolean = None
        try:
            #  InternalLF.g:1844:47: (iv_ruleBoolean= ruleBoolean EOF )
            #  InternalLF.g:1845:2: iv_ruleBoolean= ruleBoolean EOF
            newCompositeNode(self.grammarAccess.getBooleanRule())
            pushFollow(FOLLOW_1)
            iv_ruleBoolean = ruleBoolean()
            state._fsp -= 1
            current = iv_ruleBoolean.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleBoolean"
    #  $ANTLR start "ruleBoolean"
    #  InternalLF.g:1851:1: ruleBoolean returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_TRUE_0= RULE_TRUE | this_FALSE_1= RULE_FALSE ) ;
    def ruleBoolean(self):
        """ generated source for method ruleBoolean """
        current = AntlrDatatypeRuleToken()
        this_TRUE_0 = None
        this_FALSE_1 = None
        enterRule()
        try:
            #  InternalLF.g:1857:2: ( (this_TRUE_0= RULE_TRUE | this_FALSE_1= RULE_FALSE ) )
            #  InternalLF.g:1858:2: (this_TRUE_0= RULE_TRUE | this_FALSE_1= RULE_FALSE )
            #  InternalLF.g:1858:2: (this_TRUE_0= RULE_TRUE | this_FALSE_1= RULE_FALSE )
            alt51 = 2
            LA51_0 = input.LA(1)
            if (LA51_0 == self.RULE_TRUE):
                alt51 = 1
            elif (LA51_0 == self.RULE_FALSE):
                alt51 = 2
            else:
                nvae = NoViableAltException("", 51, 0, input)
                raise nvae
            if alt51 == 1:
                #  InternalLF.g:1859:3: this_TRUE_0= RULE_TRUE
                this_TRUE_0 = match(input, self.RULE_TRUE, FOLLOW_2)
                current.merge(this_TRUE_0)
                newLeafNode(this_TRUE_0, self.grammarAccess.getBooleanAccess().getTRUETerminalRuleCall_0())
            elif alt51 == 2:
                #  InternalLF.g:1867:3: this_FALSE_1= RULE_FALSE
                this_FALSE_1 = match(input, self.RULE_FALSE, FOLLOW_2)
                current.merge(this_FALSE_1)
                newLeafNode(this_FALSE_1, self.grammarAccess.getBooleanAccess().getFALSETerminalRuleCall_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleBoolean"
    #  $ANTLR start "entryRuleMode"
    #  InternalLF.g:1878:1: entryRuleMode returns [EObject current=null] : iv_ruleMode= ruleMode EOF ;
    def entryRuleMode(self):
        """ generated source for method entryRuleMode """
        current = None
        iv_ruleMode = None
        try:
            #  InternalLF.g:1878:45: (iv_ruleMode= ruleMode EOF )
            #  InternalLF.g:1879:2: iv_ruleMode= ruleMode EOF
            newCompositeNode(self.grammarAccess.getModeRule())
            pushFollow(FOLLOW_1)
            iv_ruleMode = ruleMode()
            state._fsp -= 1
            current = iv_ruleMode
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleMode"
    #  $ANTLR start "ruleMode"
    #  InternalLF.g:1885:1: ruleMode returns [EObject current=null] : ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' ) ;
    def ruleMode(self):
        """ generated source for method ruleMode """
        current = None
        lv_initial_1_0 = None
        otherlv_2 = None
        lv_name_3_0 = None
        otherlv_4 = None
        otherlv_11 = None
        lv_stateVars_5_0 = None
        lv_timers_6_0 = None
        lv_actions_7_0 = None
        lv_instantiations_8_0 = None
        lv_connections_9_0 = None
        lv_reactions_10_0 = None
        enterRule()
        try:
            #  InternalLF.g:1891:2: ( ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' ) )
            #  InternalLF.g:1892:2: ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' )
            #  InternalLF.g:1892:2: ( () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}' )
            #  InternalLF.g:1893:3: () ( (lv_initial_1_0= 'initial' ) )? otherlv_2= 'mode' ( (lv_name_3_0= RULE_ID ) )? otherlv_4= '{' ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )* otherlv_11= '}'
            #  InternalLF.g:1893:3: ()
            #  InternalLF.g:1894:4: 
            current = forceCreateModelElement(self.grammarAccess.getModeAccess().getModeAction_0(), current)
            #  InternalLF.g:1900:3: ( (lv_initial_1_0= 'initial' ) )?
            alt52 = 2
            LA52_0 = input.LA(1)
            if (LA52_0 == 44):
                alt52 = 1
            if alt52 == 1:
                #  InternalLF.g:1901:4: (lv_initial_1_0= 'initial' )
                #  InternalLF.g:1901:4: (lv_initial_1_0= 'initial' )
                #  InternalLF.g:1902:5: lv_initial_1_0= 'initial'
                lv_initial_1_0 = match(input, 44, FOLLOW_48)
                newLeafNode(lv_initial_1_0, self.grammarAccess.getModeAccess().getInitialInitialKeyword_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getModeRule())
                setWithLastConsumed(current, "initial", lv_initial_1_0 != None, "initial")
            otherlv_2 = match(input, 45, FOLLOW_49)
            newLeafNode(otherlv_2, self.grammarAccess.getModeAccess().getModeKeyword_2())
            #  InternalLF.g:1918:3: ( (lv_name_3_0= RULE_ID ) )?
            alt53 = 2
            LA53_0 = input.LA(1)
            if (LA53_0 == self.RULE_ID):
                alt53 = 1
            if alt53 == 1:
                #  InternalLF.g:1919:4: (lv_name_3_0= RULE_ID )
                #  InternalLF.g:1919:4: (lv_name_3_0= RULE_ID )
                #  InternalLF.g:1920:5: lv_name_3_0= RULE_ID
                lv_name_3_0 = match(input, self.RULE_ID, FOLLOW_50)
                newLeafNode(lv_name_3_0, self.grammarAccess.getModeAccess().getNameIDTerminalRuleCall_3_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getModeRule())
                setWithLastConsumed(current, "name", lv_name_3_0, "org.lflang.LF.ID")
            otherlv_4 = match(input, 32, FOLLOW_51)
            newLeafNode(otherlv_4, self.grammarAccess.getModeAccess().getLeftCurlyBracketKeyword_4())
            #  InternalLF.g:1940:3: ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )*
            while True:
                alt54 = 7
                alt54 = dfa54.predict(input)
                if alt54 == 1:
                    #  InternalLF.g:1941:4: ( (lv_stateVars_5_0= ruleStateVar ) )
                    #  InternalLF.g:1941:4: ( (lv_stateVars_5_0= ruleStateVar ) )
                    #  InternalLF.g:1942:5: (lv_stateVars_5_0= ruleStateVar )
                    #  InternalLF.g:1942:5: (lv_stateVars_5_0= ruleStateVar )
                    #  InternalLF.g:1943:6: lv_stateVars_5_0= ruleStateVar
                    newCompositeNode(self.grammarAccess.getModeAccess().getStateVarsStateVarParserRuleCall_5_0_0())
                    pushFollow(FOLLOW_51)
                    lv_stateVars_5_0 = self.ruleStateVar()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModeRule())
                    add(current, "stateVars", lv_stateVars_5_0, "org.lflang.LF.StateVar")
                    afterParserOrEnumRuleCall()
                elif alt54 == 2:
                    #  InternalLF.g:1961:4: ( (lv_timers_6_0= ruleTimer ) )
                    #  InternalLF.g:1961:4: ( (lv_timers_6_0= ruleTimer ) )
                    #  InternalLF.g:1962:5: (lv_timers_6_0= ruleTimer )
                    #  InternalLF.g:1962:5: (lv_timers_6_0= ruleTimer )
                    #  InternalLF.g:1963:6: lv_timers_6_0= ruleTimer
                    newCompositeNode(self.grammarAccess.getModeAccess().getTimersTimerParserRuleCall_5_1_0())
                    pushFollow(FOLLOW_51)
                    lv_timers_6_0 = self.ruleTimer()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModeRule())
                    add(current, "timers", lv_timers_6_0, "org.lflang.LF.Timer")
                    afterParserOrEnumRuleCall()
                elif alt54 == 3:
                    #  InternalLF.g:1981:4: ( (lv_actions_7_0= ruleAction ) )
                    #  InternalLF.g:1981:4: ( (lv_actions_7_0= ruleAction ) )
                    #  InternalLF.g:1982:5: (lv_actions_7_0= ruleAction )
                    #  InternalLF.g:1982:5: (lv_actions_7_0= ruleAction )
                    #  InternalLF.g:1983:6: lv_actions_7_0= ruleAction
                    newCompositeNode(self.grammarAccess.getModeAccess().getActionsActionParserRuleCall_5_2_0())
                    pushFollow(FOLLOW_51)
                    lv_actions_7_0 = ruleAction()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModeRule())
                    add(current, "actions", lv_actions_7_0, "org.lflang.LF.Action")
                    afterParserOrEnumRuleCall()
                elif alt54 == 4:
                    #  InternalLF.g:2001:4: ( (lv_instantiations_8_0= ruleInstantiation ) )
                    #  InternalLF.g:2001:4: ( (lv_instantiations_8_0= ruleInstantiation ) )
                    #  InternalLF.g:2002:5: (lv_instantiations_8_0= ruleInstantiation )
                    #  InternalLF.g:2002:5: (lv_instantiations_8_0= ruleInstantiation )
                    #  InternalLF.g:2003:6: lv_instantiations_8_0= ruleInstantiation
                    newCompositeNode(self.grammarAccess.getModeAccess().getInstantiationsInstantiationParserRuleCall_5_3_0())
                    pushFollow(FOLLOW_51)
                    lv_instantiations_8_0 = ruleInstantiation()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModeRule())
                    add(current, "instantiations", lv_instantiations_8_0, "org.lflang.LF.Instantiation")
                    afterParserOrEnumRuleCall()
                elif alt54 == 5:
                    #  InternalLF.g:2021:4: ( (lv_connections_9_0= ruleConnection ) )
                    #  InternalLF.g:2021:4: ( (lv_connections_9_0= ruleConnection ) )
                    #  InternalLF.g:2022:5: (lv_connections_9_0= ruleConnection )
                    #  InternalLF.g:2022:5: (lv_connections_9_0= ruleConnection )
                    #  InternalLF.g:2023:6: lv_connections_9_0= ruleConnection
                    newCompositeNode(self.grammarAccess.getModeAccess().getConnectionsConnectionParserRuleCall_5_4_0())
                    pushFollow(FOLLOW_51)
                    lv_connections_9_0 = ruleConnection()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModeRule())
                    add(current, "connections", lv_connections_9_0, "org.lflang.LF.Connection")
                    afterParserOrEnumRuleCall()
                elif alt54 == 6:
                    #  InternalLF.g:2041:4: ( (lv_reactions_10_0= ruleReaction ) )
                    #  InternalLF.g:2041:4: ( (lv_reactions_10_0= ruleReaction ) )
                    #  InternalLF.g:2042:5: (lv_reactions_10_0= ruleReaction )
                    #  InternalLF.g:2042:5: (lv_reactions_10_0= ruleReaction )
                    #  InternalLF.g:2043:6: lv_reactions_10_0= ruleReaction
                    newCompositeNode(self.grammarAccess.getModeAccess().getReactionsReactionParserRuleCall_5_5_0())
                    pushFollow(FOLLOW_51)
                    lv_reactions_10_0 = ruleReaction()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getModeRule())
                    add(current, "reactions", lv_reactions_10_0, "org.lflang.LF.Reaction")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            otherlv_11 = match(input, 33, FOLLOW_2)
            newLeafNode(otherlv_11, self.grammarAccess.getModeAccess().getRightCurlyBracketKeyword_6())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleMode"
    #  $ANTLR start "entryRuleAction"
    #  InternalLF.g:2069:1: entryRuleAction returns [EObject current=null] : iv_ruleAction= ruleAction EOF ;
    def entryRuleAction(self):
        """ generated source for method entryRuleAction """
        current = None
        iv_ruleAction = None
        try:
            #  InternalLF.g:2069:47: (iv_ruleAction= ruleAction EOF )
            #  InternalLF.g:2070:2: iv_ruleAction= ruleAction EOF
            newCompositeNode(self.grammarAccess.getActionRule())
            pushFollow(FOLLOW_1)
            iv_ruleAction = ruleAction()
            state._fsp -= 1
            current = iv_ruleAction
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleAction"
    #  $ANTLR start "ruleAction"
    #  InternalLF.g:2076:1: ruleAction returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? ) ;
    def ruleAction(self):
        """ generated source for method ruleAction """
        current = None
        otherlv_2 = None
        lv_name_3_0 = None
        otherlv_4 = None
        otherlv_6 = None
        otherlv_8 = None
        lv_policy_9_0 = None
        otherlv_10 = None
        otherlv_11 = None
        otherlv_13 = None
        lv_attributes_0_0 = None
        lv_origin_1_0 = None
        lv_minDelay_5_0 = None
        lv_minSpacing_7_0 = None
        lv_type_12_0 = None
        enterRule()
        try:
            #  InternalLF.g:2082:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? ) )
            #  InternalLF.g:2083:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? )
            #  InternalLF.g:2083:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )? )
            #  InternalLF.g:2084:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_origin_1_0= ruleActionOrigin ) )? otherlv_2= 'action' ( (lv_name_3_0= RULE_ID ) ) (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )? (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )? (otherlv_13= ';' )?
            #  InternalLF.g:2084:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt55 = 2
                LA55_0 = input.LA(1)
                if (LA55_0 == 59):
                    alt55 = 1
                if alt55 == 1:
                    #  InternalLF.g:2085:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:2085:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:2086:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getActionAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_52)
                    lv_attributes_0_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getActionRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:2103:3: ( (lv_origin_1_0= ruleActionOrigin ) )?
            alt56 = 2
            LA56_0 = input.LA(1)
            if (LA56_0 == 68 or LA56_0 == 81 or LA56_0 == 85):
                alt56 = 1
            if alt56 == 1:
                #  InternalLF.g:2104:4: (lv_origin_1_0= ruleActionOrigin )
                #  InternalLF.g:2104:4: (lv_origin_1_0= ruleActionOrigin )
                #  InternalLF.g:2105:5: lv_origin_1_0= ruleActionOrigin
                newCompositeNode(self.grammarAccess.getActionAccess().getOriginActionOriginEnumRuleCall_1_0())
                pushFollow(FOLLOW_53)
                lv_origin_1_0 = ruleActionOrigin()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getActionRule())
                set(current, "origin", lv_origin_1_0, "org.lflang.LF.ActionOrigin")
                afterParserOrEnumRuleCall()
            otherlv_2 = match(input, 46, FOLLOW_5)
            newLeafNode(otherlv_2, self.grammarAccess.getActionAccess().getActionKeyword_2())
            #  InternalLF.g:2126:3: ( (lv_name_3_0= RULE_ID ) )
            #  InternalLF.g:2127:4: (lv_name_3_0= RULE_ID )
            #  InternalLF.g:2127:4: (lv_name_3_0= RULE_ID )
            #  InternalLF.g:2128:5: lv_name_3_0= RULE_ID
            lv_name_3_0 = match(input, self.RULE_ID, FOLLOW_54)
            newLeafNode(lv_name_3_0, self.grammarAccess.getActionAccess().getNameIDTerminalRuleCall_3_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getActionRule())
            setWithLastConsumed(current, "name", lv_name_3_0, "org.lflang.LF.ID")
            #  InternalLF.g:2144:3: (otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')' )?
            alt59 = 2
            LA59_0 = input.LA(1)
            if (LA59_0 == 28):
                LA59_1 = input.LA(2)
                if (LA59_1 == self.RULE_ID):
                    LA59_3 = input.LA(3)
                    if (LA59_3 == 18):
                        LA59_5 = input.LA(4)
                        if (LA59_5 == self.RULE_ID):
                            LA59_7 = input.LA(5)
                            if (LA59_7 == 29):
                                LA59_6 = input.LA(6)
                                if (LA59_6 == self.EOF or LA59_6 == self.RULE_ID or LA59_6 == 20 or LA59_6 == 28 or LA59_6 == 33 or (LA59_6 >= 35 and LA59_6 <= 48) or LA59_6 == 52 or LA59_6 == 59 or LA59_6 == 63 or LA59_6 == 68 or (LA59_6 >= 81 and LA59_6 <= 83) or LA59_6 == 85):
                                    alt59 = 1
                            elif (LA59_7 == 18):
                                LA59_8 = input.LA(6)
                                if (LA59_8 == self.RULE_STRING):
                                    alt59 = 1
                        elif (LA59_5 == self.RULE_STRING or (LA59_5 >= self.RULE_TRUE and LA59_5 <= self.RULE_CHAR_LIT) or LA59_5 == 62 or LA59_5 == 69 or LA59_5 == 71):
                            alt59 = 1
                    elif (LA59_3 == 29):
                        LA59_6 = input.LA(4)
                        if (LA59_6 == self.EOF or LA59_6 == self.RULE_ID or LA59_6 == 20 or LA59_6 == 28 or LA59_6 == 33 or (LA59_6 >= 35 and LA59_6 <= 48) or LA59_6 == 52 or LA59_6 == 59 or LA59_6 == 63 or LA59_6 == 68 or (LA59_6 >= 81 and LA59_6 <= 83) or LA59_6 == 85):
                            alt59 = 1
                elif (LA59_1 == self.RULE_STRING or (LA59_1 >= self.RULE_TRUE and LA59_1 <= self.RULE_CHAR_LIT) or LA59_1 == 62 or LA59_1 == 69 or LA59_1 == 71):
                    alt59 = 1
            if alt59 == 1:
                #  InternalLF.g:2145:4: otherlv_4= '(' ( (lv_minDelay_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )? otherlv_10= ')'
                otherlv_4 = match(input, 28, FOLLOW_32)
                newLeafNode(otherlv_4, self.grammarAccess.getActionAccess().getLeftParenthesisKeyword_4_0())
                #  InternalLF.g:2149:4: ( (lv_minDelay_5_0= ruleExpression ) )
                #  InternalLF.g:2150:5: (lv_minDelay_5_0= ruleExpression )
                #  InternalLF.g:2150:5: (lv_minDelay_5_0= ruleExpression )
                #  InternalLF.g:2151:6: lv_minDelay_5_0= ruleExpression
                newCompositeNode(self.grammarAccess.getActionAccess().getMinDelayExpressionParserRuleCall_4_1_0())
                pushFollow(FOLLOW_18)
                lv_minDelay_5_0 = ruleExpression()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getActionRule())
                set(current, "minDelay", lv_minDelay_5_0, "org.lflang.LF.Expression")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:2168:4: (otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )? )?
                alt58 = 2
                LA58_0 = input.LA(1)
                if (LA58_0 == 18):
                    alt58 = 1
                if alt58 == 1:
                    #  InternalLF.g:2169:5: otherlv_6= ',' ( (lv_minSpacing_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )?
                    otherlv_6 = match(input, 18, FOLLOW_32)
                    newLeafNode(otherlv_6, self.grammarAccess.getActionAccess().getCommaKeyword_4_2_0())
                    #  InternalLF.g:2173:5: ( (lv_minSpacing_7_0= ruleExpression ) )
                    #  InternalLF.g:2174:6: (lv_minSpacing_7_0= ruleExpression )
                    #  InternalLF.g:2174:6: (lv_minSpacing_7_0= ruleExpression )
                    #  InternalLF.g:2175:7: lv_minSpacing_7_0= ruleExpression
                    newCompositeNode(self.grammarAccess.getActionAccess().getMinSpacingExpressionParserRuleCall_4_2_1_0())
                    pushFollow(FOLLOW_18)
                    lv_minSpacing_7_0 = ruleExpression()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getActionRule())
                    set(current, "minSpacing", lv_minSpacing_7_0, "org.lflang.LF.Expression")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:2192:5: (otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) ) )?
                    alt57 = 2
                    LA57_0 = input.LA(1)
                    if (LA57_0 == 18):
                        alt57 = 1
                    if alt57 == 1:
                        #  InternalLF.g:2193:6: otherlv_8= ',' ( (lv_policy_9_0= RULE_STRING ) )
                        otherlv_8 = match(input, 18, FOLLOW_7)
                        newLeafNode(otherlv_8, self.grammarAccess.getActionAccess().getCommaKeyword_4_2_2_0())
                        #  InternalLF.g:2197:6: ( (lv_policy_9_0= RULE_STRING ) )
                        #  InternalLF.g:2198:7: (lv_policy_9_0= RULE_STRING )
                        #  InternalLF.g:2198:7: (lv_policy_9_0= RULE_STRING )
                        #  InternalLF.g:2199:8: lv_policy_9_0= RULE_STRING
                        lv_policy_9_0 = match(input, self.RULE_STRING, FOLLOW_47)
                        newLeafNode(lv_policy_9_0, self.grammarAccess.getActionAccess().getPolicySTRINGTerminalRuleCall_4_2_2_1_0())
                        if current == None:
                            current = createModelElement(self.grammarAccess.getActionRule())
                        setWithLastConsumed(current, "policy", lv_policy_9_0, "org.lflang.LF.STRING")
                otherlv_10 = match(input, 29, FOLLOW_43)
                newLeafNode(otherlv_10, self.grammarAccess.getActionAccess().getRightParenthesisKeyword_4_3())
            #  InternalLF.g:2222:3: (otherlv_11= ':' ( (lv_type_12_0= ruleType ) ) )?
            alt60 = 2
            LA60_0 = input.LA(1)
            if (LA60_0 == 37):
                alt60 = 1
            if alt60 == 1:
                #  InternalLF.g:2223:4: otherlv_11= ':' ( (lv_type_12_0= ruleType ) )
                otherlv_11 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_11, self.grammarAccess.getActionAccess().getColonKeyword_5_0())
                #  InternalLF.g:2227:4: ( (lv_type_12_0= ruleType ) )
                #  InternalLF.g:2228:5: (lv_type_12_0= ruleType )
                #  InternalLF.g:2228:5: (lv_type_12_0= ruleType )
                #  InternalLF.g:2229:6: lv_type_12_0= ruleType
                newCompositeNode(self.grammarAccess.getActionAccess().getTypeTypeParserRuleCall_5_1_0())
                pushFollow(FOLLOW_8)
                lv_type_12_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getActionRule())
                set(current, "type", lv_type_12_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:2247:3: (otherlv_13= ';' )?
            alt61 = 2
            LA61_0 = input.LA(1)
            if (LA61_0 == 20):
                alt61 = 1
            if alt61 == 1:
                #  InternalLF.g:2248:4: otherlv_13= ';'
                otherlv_13 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_13, self.grammarAccess.getActionAccess().getSemicolonKeyword_6())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleAction"
    #  $ANTLR start "entryRuleReaction"
    #  InternalLF.g:2257:1: entryRuleReaction returns [EObject current=null] : iv_ruleReaction= ruleReaction EOF ;
    def entryRuleReaction(self):
        """ generated source for method entryRuleReaction """
        current = None
        iv_ruleReaction = None
        try:
            #  InternalLF.g:2257:49: (iv_ruleReaction= ruleReaction EOF )
            #  InternalLF.g:2258:2: iv_ruleReaction= ruleReaction EOF
            newCompositeNode(self.grammarAccess.getReactionRule())
            pushFollow(FOLLOW_1)
            iv_ruleReaction = ruleReaction()
            state._fsp -= 1
            current = iv_ruleReaction
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleReaction"
    #  $ANTLR start "ruleReaction"
    #  InternalLF.g:2264:1: ruleReaction returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? ) ;
    def ruleReaction(self):
        """ generated source for method ruleReaction """
        current = None
        otherlv_1 = None
        lv_mutation_2_0 = None
        otherlv_3 = None
        otherlv_5 = None
        otherlv_7 = None
        otherlv_9 = None
        otherlv_11 = None
        otherlv_13 = None
        lv_attributes_0_0 = None
        lv_triggers_4_0 = None
        lv_triggers_6_0 = None
        lv_sources_8_0 = None
        lv_sources_10_0 = None
        lv_effects_12_0 = None
        lv_effects_14_0 = None
        lv_code_15_0 = None
        lv_stp_16_0 = None
        lv_deadline_17_0 = None
        enterRule()
        try:
            #  InternalLF.g:2270:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? ) )
            #  InternalLF.g:2271:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? )
            #  InternalLF.g:2271:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )? )
            #  InternalLF.g:2272:3: ( (lv_attributes_0_0= ruleAttribute ) )* (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) ) (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )? ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )? (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )? ( (lv_code_15_0= ruleCode ) ) ( (lv_stp_16_0= ruleSTP ) )? ( (lv_deadline_17_0= ruleDeadline ) )?
            #  InternalLF.g:2272:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt62 = 2
                LA62_0 = input.LA(1)
                if (LA62_0 == 59):
                    alt62 = 1
                if alt62 == 1:
                    #  InternalLF.g:2273:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:2273:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:2274:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getReactionAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_55)
                    lv_attributes_0_0 = ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactionRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:2291:3: (otherlv_1= 'reaction' | ( (lv_mutation_2_0= 'mutation' ) ) )
            alt63 = 2
            LA63_0 = input.LA(1)
            if (LA63_0 == 47):
                alt63 = 1
            elif (LA63_0 == 48):
                alt63 = 2
            else:
                nvae = NoViableAltException("", 63, 0, input)
                raise nvae
            if alt63 == 1:
                #  InternalLF.g:2292:4: otherlv_1= 'reaction'
                otherlv_1 = match(input, 47, FOLLOW_56)
                newLeafNode(otherlv_1, self.grammarAccess.getReactionAccess().getReactionKeyword_1_0())
            elif alt63 == 2:
                #  InternalLF.g:2297:4: ( (lv_mutation_2_0= 'mutation' ) )
                #  InternalLF.g:2297:4: ( (lv_mutation_2_0= 'mutation' ) )
                #  InternalLF.g:2298:5: (lv_mutation_2_0= 'mutation' )
                #  InternalLF.g:2298:5: (lv_mutation_2_0= 'mutation' )
                #  InternalLF.g:2299:6: lv_mutation_2_0= 'mutation'
                lv_mutation_2_0 = match(input, 48, FOLLOW_56)
                newLeafNode(lv_mutation_2_0, self.grammarAccess.getReactionAccess().getMutationMutationKeyword_1_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getReactionRule())
                setWithLastConsumed(current, "mutation", lv_mutation_2_0 != None, "mutation")
            #  InternalLF.g:2312:3: (otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')' )?
            alt66 = 2
            LA66_0 = input.LA(1)
            if (LA66_0 == 28):
                alt66 = 1
            if alt66 == 1:
                #  InternalLF.g:2313:4: otherlv_3= '(' ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )? otherlv_7= ')'
                otherlv_3 = match(input, 28, FOLLOW_57)
                newLeafNode(otherlv_3, self.grammarAccess.getReactionAccess().getLeftParenthesisKeyword_2_0())
                #  InternalLF.g:2317:4: ( ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )* )?
                alt65 = 2
                LA65_0 = input.LA(1)
                if (LA65_0 == self.RULE_ID or LA65_0 == 35 or LA65_0 == 63 or (LA65_0 >= 77 and LA65_0 <= 78)):
                    alt65 = 1
                if alt65 == 1:
                    #  InternalLF.g:2318:5: ( (lv_triggers_4_0= ruleTriggerRef ) ) (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )*
                    #  InternalLF.g:2318:5: ( (lv_triggers_4_0= ruleTriggerRef ) )
                    #  InternalLF.g:2319:6: (lv_triggers_4_0= ruleTriggerRef )
                    #  InternalLF.g:2319:6: (lv_triggers_4_0= ruleTriggerRef )
                    #  InternalLF.g:2320:7: lv_triggers_4_0= ruleTriggerRef
                    newCompositeNode(self.grammarAccess.getReactionAccess().getTriggersTriggerRefParserRuleCall_2_1_0_0())
                    pushFollow(FOLLOW_18)
                    lv_triggers_4_0 = ruleTriggerRef()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getReactionRule())
                    add(current, "triggers", lv_triggers_4_0, "org.lflang.LF.TriggerRef")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:2337:5: (otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) ) )*
                    while True:
                        alt64 = 2
                        LA64_0 = input.LA(1)
                        if (LA64_0 == 18):
                            alt64 = 1
                        if alt64 == 1:
                            #  InternalLF.g:2338:6: otherlv_5= ',' ( (lv_triggers_6_0= ruleTriggerRef ) )
                            otherlv_5 = match(input, 18, FOLLOW_58)
                            newLeafNode(otherlv_5, self.grammarAccess.getReactionAccess().getCommaKeyword_2_1_1_0())
                            #  InternalLF.g:2342:6: ( (lv_triggers_6_0= ruleTriggerRef ) )
                            #  InternalLF.g:2343:7: (lv_triggers_6_0= ruleTriggerRef )
                            #  InternalLF.g:2343:7: (lv_triggers_6_0= ruleTriggerRef )
                            #  InternalLF.g:2344:8: lv_triggers_6_0= ruleTriggerRef
                            newCompositeNode(self.grammarAccess.getReactionAccess().getTriggersTriggerRefParserRuleCall_2_1_1_1_0())
                            pushFollow(FOLLOW_18)
                            lv_triggers_6_0 = ruleTriggerRef()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getReactionRule())
                            add(current, "triggers", lv_triggers_6_0, "org.lflang.LF.TriggerRef")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                otherlv_7 = match(input, 29, FOLLOW_59)
                newLeafNode(otherlv_7, self.grammarAccess.getReactionAccess().getRightParenthesisKeyword_2_2())
            #  InternalLF.g:2368:3: ( ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )* )?
            alt68 = 2
            LA68_0 = input.LA(1)
            if (LA68_0 == self.RULE_ID or LA68_0 == 63):
                alt68 = 1
            if alt68 == 1:
                #  InternalLF.g:2369:4: ( (lv_sources_8_0= ruleVarRef ) ) (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )*
                #  InternalLF.g:2369:4: ( (lv_sources_8_0= ruleVarRef ) )
                #  InternalLF.g:2370:5: (lv_sources_8_0= ruleVarRef )
                #  InternalLF.g:2370:5: (lv_sources_8_0= ruleVarRef )
                #  InternalLF.g:2371:6: lv_sources_8_0= ruleVarRef
                newCompositeNode(self.grammarAccess.getReactionAccess().getSourcesVarRefParserRuleCall_3_0_0())
                pushFollow(FOLLOW_60)
                lv_sources_8_0 = ruleVarRef()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactionRule())
                add(current, "sources", lv_sources_8_0, "org.lflang.LF.VarRef")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:2388:4: (otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) ) )*
                while True:
                    alt67 = 2
                    LA67_0 = input.LA(1)
                    if (LA67_0 == 18):
                        alt67 = 1
                    if alt67 == 1:
                        #  InternalLF.g:2389:5: otherlv_9= ',' ( (lv_sources_10_0= ruleVarRef ) )
                        otherlv_9 = match(input, 18, FOLLOW_61)
                        newLeafNode(otherlv_9, self.grammarAccess.getReactionAccess().getCommaKeyword_3_1_0())
                        #  InternalLF.g:2393:5: ( (lv_sources_10_0= ruleVarRef ) )
                        #  InternalLF.g:2394:6: (lv_sources_10_0= ruleVarRef )
                        #  InternalLF.g:2394:6: (lv_sources_10_0= ruleVarRef )
                        #  InternalLF.g:2395:7: lv_sources_10_0= ruleVarRef
                        newCompositeNode(self.grammarAccess.getReactionAccess().getSourcesVarRefParserRuleCall_3_1_1_0())
                        pushFollow(FOLLOW_60)
                        lv_sources_10_0 = ruleVarRef()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getReactionRule())
                        add(current, "sources", lv_sources_10_0, "org.lflang.LF.VarRef")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
            #  InternalLF.g:2414:3: (otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )* )?
            alt70 = 2
            LA70_0 = input.LA(1)
            if (LA70_0 == 49):
                alt70 = 1
            if alt70 == 1:
                #  InternalLF.g:2415:4: otherlv_11= '->' ( (lv_effects_12_0= ruleVarRefOrModeTransition ) ) (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )*
                otherlv_11 = match(input, 49, FOLLOW_62)
                newLeafNode(otherlv_11, self.grammarAccess.getReactionAccess().getHyphenMinusGreaterThanSignKeyword_4_0())
                #  InternalLF.g:2419:4: ( (lv_effects_12_0= ruleVarRefOrModeTransition ) )
                #  InternalLF.g:2420:5: (lv_effects_12_0= ruleVarRefOrModeTransition )
                #  InternalLF.g:2420:5: (lv_effects_12_0= ruleVarRefOrModeTransition )
                #  InternalLF.g:2421:6: lv_effects_12_0= ruleVarRefOrModeTransition
                newCompositeNode(self.grammarAccess.getReactionAccess().getEffectsVarRefOrModeTransitionParserRuleCall_4_1_0())
                pushFollow(FOLLOW_63)
                lv_effects_12_0 = ruleVarRefOrModeTransition()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactionRule())
                add(current, "effects", lv_effects_12_0, "org.lflang.LF.VarRefOrModeTransition")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:2438:4: (otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) ) )*
                while True:
                    alt69 = 2
                    LA69_0 = input.LA(1)
                    if (LA69_0 == 18):
                        alt69 = 1
                    if alt69 == 1:
                        #  InternalLF.g:2439:5: otherlv_13= ',' ( (lv_effects_14_0= ruleVarRefOrModeTransition ) )
                        otherlv_13 = match(input, 18, FOLLOW_62)
                        newLeafNode(otherlv_13, self.grammarAccess.getReactionAccess().getCommaKeyword_4_2_0())
                        #  InternalLF.g:2443:5: ( (lv_effects_14_0= ruleVarRefOrModeTransition ) )
                        #  InternalLF.g:2444:6: (lv_effects_14_0= ruleVarRefOrModeTransition )
                        #  InternalLF.g:2444:6: (lv_effects_14_0= ruleVarRefOrModeTransition )
                        #  InternalLF.g:2445:7: lv_effects_14_0= ruleVarRefOrModeTransition
                        newCompositeNode(self.grammarAccess.getReactionAccess().getEffectsVarRefOrModeTransitionParserRuleCall_4_2_1_0())
                        pushFollow(FOLLOW_63)
                        lv_effects_14_0 = ruleVarRefOrModeTransition()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getReactionRule())
                        add(current, "effects", lv_effects_14_0, "org.lflang.LF.VarRefOrModeTransition")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
            #  InternalLF.g:2464:3: ( (lv_code_15_0= ruleCode ) )
            #  InternalLF.g:2465:4: (lv_code_15_0= ruleCode )
            #  InternalLF.g:2465:4: (lv_code_15_0= ruleCode )
            #  InternalLF.g:2466:5: lv_code_15_0= ruleCode
            newCompositeNode(self.grammarAccess.getReactionAccess().getCodeCodeParserRuleCall_5_0())
            pushFollow(FOLLOW_64)
            lv_code_15_0 = ruleCode()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getReactionRule())
            set(current, "code", lv_code_15_0, "org.lflang.LF.Code")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:2483:3: ( (lv_stp_16_0= ruleSTP ) )?
            alt71 = 2
            LA71_0 = input.LA(1)
            if (LA71_0 == 51):
                alt71 = 1
            if alt71 == 1:
                #  InternalLF.g:2484:4: (lv_stp_16_0= ruleSTP )
                #  InternalLF.g:2484:4: (lv_stp_16_0= ruleSTP )
                #  InternalLF.g:2485:5: lv_stp_16_0= ruleSTP
                newCompositeNode(self.grammarAccess.getReactionAccess().getStpSTPParserRuleCall_6_0())
                pushFollow(FOLLOW_65)
                lv_stp_16_0 = ruleSTP()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactionRule())
                set(current, "stp", lv_stp_16_0, "org.lflang.LF.STP")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:2502:3: ( (lv_deadline_17_0= ruleDeadline ) )?
            alt72 = 2
            LA72_0 = input.LA(1)
            if (LA72_0 == 50):
                alt72 = 1
            if alt72 == 1:
                #  InternalLF.g:2503:4: (lv_deadline_17_0= ruleDeadline )
                #  InternalLF.g:2503:4: (lv_deadline_17_0= ruleDeadline )
                #  InternalLF.g:2504:5: lv_deadline_17_0= ruleDeadline
                newCompositeNode(self.grammarAccess.getReactionAccess().getDeadlineDeadlineParserRuleCall_7_0())
                pushFollow(FOLLOW_2)
                lv_deadline_17_0 = ruleDeadline()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getReactionRule())
                set(current, "deadline", lv_deadline_17_0, "org.lflang.LF.Deadline")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleReaction"
    #  $ANTLR start "entryRuleTriggerRef"
    #  InternalLF.g:2525:1: entryRuleTriggerRef returns [EObject current=null] : iv_ruleTriggerRef= ruleTriggerRef EOF ;
    def entryRuleTriggerRef(self):
        """ generated source for method entryRuleTriggerRef """
        current = None
        iv_ruleTriggerRef = None
        try:
            #  InternalLF.g:2525:51: (iv_ruleTriggerRef= ruleTriggerRef EOF )
            #  InternalLF.g:2526:2: iv_ruleTriggerRef= ruleTriggerRef EOF
            newCompositeNode(self.grammarAccess.getTriggerRefRule())
            pushFollow(FOLLOW_1)
            iv_ruleTriggerRef = ruleTriggerRef()
            state._fsp -= 1
            current = iv_ruleTriggerRef
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTriggerRef"
    #  $ANTLR start "ruleTriggerRef"
    #  InternalLF.g:2532:1: ruleTriggerRef returns [EObject current=null] : (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef | this_VarRef_1= ruleVarRef ) ;
    def ruleTriggerRef(self):
        """ generated source for method ruleTriggerRef """
        current = None
        this_BuiltinTriggerRef_0 = None
        this_VarRef_1 = None
        enterRule()
        try:
            #  InternalLF.g:2538:2: ( (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef | this_VarRef_1= ruleVarRef ) )
            #  InternalLF.g:2539:2: (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef | this_VarRef_1= ruleVarRef )
            #  InternalLF.g:2539:2: (this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef | this_VarRef_1= ruleVarRef )
            alt73 = 2
            LA73_0 = input.LA(1)
            if (LA73_0 == 35 or (LA73_0 >= 77 and LA73_0 <= 78)):
                alt73 = 1
            elif (LA73_0 == self.RULE_ID or LA73_0 == 63):
                alt73 = 2
            else:
                nvae = NoViableAltException("", 73, 0, input)
                raise nvae
            if alt73 == 1:
                #  InternalLF.g:2540:3: this_BuiltinTriggerRef_0= ruleBuiltinTriggerRef
                newCompositeNode(self.grammarAccess.getTriggerRefAccess().getBuiltinTriggerRefParserRuleCall_0())
                pushFollow(FOLLOW_2)
                this_BuiltinTriggerRef_0 = ruleBuiltinTriggerRef()
                state._fsp -= 1
                current = this_BuiltinTriggerRef_0
                afterParserOrEnumRuleCall()
            elif alt73 == 2:
                #  InternalLF.g:2549:3: this_VarRef_1= ruleVarRef
                newCompositeNode(self.grammarAccess.getTriggerRefAccess().getVarRefParserRuleCall_1())
                pushFollow(FOLLOW_2)
                this_VarRef_1 = ruleVarRef()
                state._fsp -= 1
                current = this_VarRef_1
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTriggerRef"
    #  $ANTLR start "entryRuleBuiltinTriggerRef"
    #  InternalLF.g:2561:1: entryRuleBuiltinTriggerRef returns [EObject current=null] : iv_ruleBuiltinTriggerRef= ruleBuiltinTriggerRef EOF ;
    def entryRuleBuiltinTriggerRef(self):
        """ generated source for method entryRuleBuiltinTriggerRef """
        current = None
        iv_ruleBuiltinTriggerRef = None
        try:
            #  InternalLF.g:2561:58: (iv_ruleBuiltinTriggerRef= ruleBuiltinTriggerRef EOF )
            #  InternalLF.g:2562:2: iv_ruleBuiltinTriggerRef= ruleBuiltinTriggerRef EOF
            newCompositeNode(self.grammarAccess.getBuiltinTriggerRefRule())
            pushFollow(FOLLOW_1)
            iv_ruleBuiltinTriggerRef = ruleBuiltinTriggerRef()
            state._fsp -= 1
            current = iv_ruleBuiltinTriggerRef
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleBuiltinTriggerRef"
    #  $ANTLR start "ruleBuiltinTriggerRef"
    #  InternalLF.g:2568:1: ruleBuiltinTriggerRef returns [EObject current=null] : ( (lv_type_0_0= ruleBuiltinTrigger ) ) ;
    def ruleBuiltinTriggerRef(self):
        """ generated source for method ruleBuiltinTriggerRef """
        current = None
        lv_type_0_0 = None
        enterRule()
        try:
            #  InternalLF.g:2574:2: ( ( (lv_type_0_0= ruleBuiltinTrigger ) ) )
            #  InternalLF.g:2575:2: ( (lv_type_0_0= ruleBuiltinTrigger ) )
            #  InternalLF.g:2575:2: ( (lv_type_0_0= ruleBuiltinTrigger ) )
            #  InternalLF.g:2576:3: (lv_type_0_0= ruleBuiltinTrigger )
            #  InternalLF.g:2576:3: (lv_type_0_0= ruleBuiltinTrigger )
            #  InternalLF.g:2577:4: lv_type_0_0= ruleBuiltinTrigger
            newCompositeNode(self.grammarAccess.getBuiltinTriggerRefAccess().getTypeBuiltinTriggerEnumRuleCall_0())
            pushFollow(FOLLOW_2)
            lv_type_0_0 = ruleBuiltinTrigger()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getBuiltinTriggerRefRule())
            set(current, "type", lv_type_0_0, "org.lflang.LF.BuiltinTrigger")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleBuiltinTriggerRef"
    #  $ANTLR start "entryRuleDeadline"
    #  InternalLF.g:2597:1: entryRuleDeadline returns [EObject current=null] : iv_ruleDeadline= ruleDeadline EOF ;
    def entryRuleDeadline(self):
        """ generated source for method entryRuleDeadline """
        current = None
        iv_ruleDeadline = None
        try:
            #  InternalLF.g:2597:49: (iv_ruleDeadline= ruleDeadline EOF )
            #  InternalLF.g:2598:2: iv_ruleDeadline= ruleDeadline EOF
            newCompositeNode(self.grammarAccess.getDeadlineRule())
            pushFollow(FOLLOW_1)
            iv_ruleDeadline = ruleDeadline()
            state._fsp -= 1
            current = iv_ruleDeadline
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleDeadline"
    #  $ANTLR start "ruleDeadline"
    #  InternalLF.g:2604:1: ruleDeadline returns [EObject current=null] : (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) ;
    def ruleDeadline(self):
        """ generated source for method ruleDeadline """
        current = None
        otherlv_0 = None
        otherlv_1 = None
        otherlv_3 = None
        lv_delay_2_0 = None
        lv_code_4_0 = None
        enterRule()
        try:
            #  InternalLF.g:2610:2: ( (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) )
            #  InternalLF.g:2611:2: (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
            #  InternalLF.g:2611:2: (otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
            #  InternalLF.g:2612:3: otherlv_0= 'deadline' otherlv_1= '(' ( (lv_delay_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) )
            otherlv_0 = match(input, 50, FOLLOW_36)
            newLeafNode(otherlv_0, self.grammarAccess.getDeadlineAccess().getDeadlineKeyword_0())
            otherlv_1 = match(input, 28, FOLLOW_32)
            newLeafNode(otherlv_1, self.grammarAccess.getDeadlineAccess().getLeftParenthesisKeyword_1())
            #  InternalLF.g:2620:3: ( (lv_delay_2_0= ruleExpression ) )
            #  InternalLF.g:2621:4: (lv_delay_2_0= ruleExpression )
            #  InternalLF.g:2621:4: (lv_delay_2_0= ruleExpression )
            #  InternalLF.g:2622:5: lv_delay_2_0= ruleExpression
            newCompositeNode(self.grammarAccess.getDeadlineAccess().getDelayExpressionParserRuleCall_2_0())
            pushFollow(FOLLOW_47)
            lv_delay_2_0 = ruleExpression()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getDeadlineRule())
            set(current, "delay", lv_delay_2_0, "org.lflang.LF.Expression")
            afterParserOrEnumRuleCall()
            otherlv_3 = match(input, 29, FOLLOW_14)
            newLeafNode(otherlv_3, self.grammarAccess.getDeadlineAccess().getRightParenthesisKeyword_3())
            #  InternalLF.g:2643:3: ( (lv_code_4_0= ruleCode ) )
            #  InternalLF.g:2644:4: (lv_code_4_0= ruleCode )
            #  InternalLF.g:2644:4: (lv_code_4_0= ruleCode )
            #  InternalLF.g:2645:5: lv_code_4_0= ruleCode
            newCompositeNode(self.grammarAccess.getDeadlineAccess().getCodeCodeParserRuleCall_4_0())
            pushFollow(FOLLOW_2)
            lv_code_4_0 = ruleCode()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getDeadlineRule())
            set(current, "code", lv_code_4_0, "org.lflang.LF.Code")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleDeadline"
    #  $ANTLR start "entryRuleSTP"
    #  InternalLF.g:2666:1: entryRuleSTP returns [EObject current=null] : iv_ruleSTP= ruleSTP EOF ;
    def entryRuleSTP(self):
        """ generated source for method entryRuleSTP """
        current = None
        iv_ruleSTP = None
        try:
            #  InternalLF.g:2666:44: (iv_ruleSTP= ruleSTP EOF )
            #  InternalLF.g:2667:2: iv_ruleSTP= ruleSTP EOF
            newCompositeNode(self.grammarAccess.getSTPRule())
            pushFollow(FOLLOW_1)
            iv_ruleSTP = ruleSTP()
            state._fsp -= 1
            current = iv_ruleSTP
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleSTP"
    #  $ANTLR start "ruleSTP"
    #  InternalLF.g:2673:1: ruleSTP returns [EObject current=null] : (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) ;
    def ruleSTP(self):
        """ generated source for method ruleSTP """
        current = None
        otherlv_0 = None
        otherlv_1 = None
        otherlv_3 = None
        lv_value_2_0 = None
        lv_code_4_0 = None
        enterRule()
        try:
            #  InternalLF.g:2679:2: ( (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) ) )
            #  InternalLF.g:2680:2: (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
            #  InternalLF.g:2680:2: (otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) ) )
            #  InternalLF.g:2681:3: otherlv_0= 'STP' otherlv_1= '(' ( (lv_value_2_0= ruleExpression ) ) otherlv_3= ')' ( (lv_code_4_0= ruleCode ) )
            otherlv_0 = match(input, 51, FOLLOW_36)
            newLeafNode(otherlv_0, self.grammarAccess.getSTPAccess().getSTPKeyword_0())
            otherlv_1 = match(input, 28, FOLLOW_32)
            newLeafNode(otherlv_1, self.grammarAccess.getSTPAccess().getLeftParenthesisKeyword_1())
            #  InternalLF.g:2689:3: ( (lv_value_2_0= ruleExpression ) )
            #  InternalLF.g:2690:4: (lv_value_2_0= ruleExpression )
            #  InternalLF.g:2690:4: (lv_value_2_0= ruleExpression )
            #  InternalLF.g:2691:5: lv_value_2_0= ruleExpression
            newCompositeNode(self.grammarAccess.getSTPAccess().getValueExpressionParserRuleCall_2_0())
            pushFollow(FOLLOW_47)
            lv_value_2_0 = ruleExpression()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getSTPRule())
            set(current, "value", lv_value_2_0, "org.lflang.LF.Expression")
            afterParserOrEnumRuleCall()
            otherlv_3 = match(input, 29, FOLLOW_14)
            newLeafNode(otherlv_3, self.grammarAccess.getSTPAccess().getRightParenthesisKeyword_3())
            #  InternalLF.g:2712:3: ( (lv_code_4_0= ruleCode ) )
            #  InternalLF.g:2713:4: (lv_code_4_0= ruleCode )
            #  InternalLF.g:2713:4: (lv_code_4_0= ruleCode )
            #  InternalLF.g:2714:5: lv_code_4_0= ruleCode
            newCompositeNode(self.grammarAccess.getSTPAccess().getCodeCodeParserRuleCall_4_0())
            pushFollow(FOLLOW_2)
            lv_code_4_0 = ruleCode()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getSTPRule())
            set(current, "code", lv_code_4_0, "org.lflang.LF.Code")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleSTP"
    #  $ANTLR start "entryRulePreamble"
    #  InternalLF.g:2735:1: entryRulePreamble returns [EObject current=null] : iv_rulePreamble= rulePreamble EOF ;
    def entryRulePreamble(self):
        """ generated source for method entryRulePreamble """
        current = None
        iv_rulePreamble = None
        try:
            #  InternalLF.g:2735:49: (iv_rulePreamble= rulePreamble EOF )
            #  InternalLF.g:2736:2: iv_rulePreamble= rulePreamble EOF
            newCompositeNode(self.grammarAccess.getPreambleRule())
            pushFollow(FOLLOW_1)
            iv_rulePreamble = rulePreamble()
            state._fsp -= 1
            current = iv_rulePreamble
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRulePreamble"
    #  $ANTLR start "rulePreamble"
    #  InternalLF.g:2742:1: rulePreamble returns [EObject current=null] : ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) ) ;
    def rulePreamble(self):
        """ generated source for method rulePreamble """
        current = None
        otherlv_1 = None
        lv_visibility_0_0 = None
        lv_code_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:2748:2: ( ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) ) )
            #  InternalLF.g:2749:2: ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) )
            #  InternalLF.g:2749:2: ( ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) ) )
            #  InternalLF.g:2750:3: ( (lv_visibility_0_0= ruleVisibility ) )? otherlv_1= 'preamble' ( (lv_code_2_0= ruleCode ) )
            #  InternalLF.g:2750:3: ( (lv_visibility_0_0= ruleVisibility ) )?
            alt74 = 2
            LA74_0 = input.LA(1)
            if ((LA74_0 >= 82 and LA74_0 <= 83) or LA74_0 == 85):
                alt74 = 1
            if alt74 == 1:
                #  InternalLF.g:2751:4: (lv_visibility_0_0= ruleVisibility )
                #  InternalLF.g:2751:4: (lv_visibility_0_0= ruleVisibility )
                #  InternalLF.g:2752:5: lv_visibility_0_0= ruleVisibility
                newCompositeNode(self.grammarAccess.getPreambleAccess().getVisibilityVisibilityEnumRuleCall_0_0())
                pushFollow(FOLLOW_66)
                lv_visibility_0_0 = ruleVisibility()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getPreambleRule())
                set(current, "visibility", lv_visibility_0_0, "org.lflang.LF.Visibility")
                afterParserOrEnumRuleCall()
            otherlv_1 = match(input, 52, FOLLOW_14)
            newLeafNode(otherlv_1, self.grammarAccess.getPreambleAccess().getPreambleKeyword_1())
            #  InternalLF.g:2773:3: ( (lv_code_2_0= ruleCode ) )
            #  InternalLF.g:2774:4: (lv_code_2_0= ruleCode )
            #  InternalLF.g:2774:4: (lv_code_2_0= ruleCode )
            #  InternalLF.g:2775:5: lv_code_2_0= ruleCode
            newCompositeNode(self.grammarAccess.getPreambleAccess().getCodeCodeParserRuleCall_2_0())
            pushFollow(FOLLOW_2)
            lv_code_2_0 = ruleCode()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getPreambleRule())
            set(current, "code", lv_code_2_0, "org.lflang.LF.Code")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "rulePreamble"
    #  $ANTLR start "entryRuleInstantiation"
    #  InternalLF.g:2796:1: entryRuleInstantiation returns [EObject current=null] : iv_ruleInstantiation= ruleInstantiation EOF ;
    def entryRuleInstantiation(self):
        """ generated source for method entryRuleInstantiation """
        current = None
        iv_ruleInstantiation = None
        try:
            #  InternalLF.g:2796:54: (iv_ruleInstantiation= ruleInstantiation EOF )
            #  InternalLF.g:2797:2: iv_ruleInstantiation= ruleInstantiation EOF
            newCompositeNode(self.grammarAccess.getInstantiationRule())
            pushFollow(FOLLOW_1)
            iv_ruleInstantiation = ruleInstantiation()
            state._fsp -= 1
            current = iv_ruleInstantiation
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleInstantiation"
    #  $ANTLR start "ruleInstantiation"
    #  InternalLF.g:2803:1: ruleInstantiation returns [EObject current=null] : ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) ) ;
    def ruleInstantiation(self):
        """ generated source for method ruleInstantiation """
        current = None
        lv_name_0_0 = None
        otherlv_1 = None
        otherlv_2 = None
        otherlv_4 = None
        otherlv_5 = None
        otherlv_7 = None
        otherlv_9 = None
        otherlv_10 = None
        otherlv_12 = None
        otherlv_14 = None
        otherlv_15 = None
        otherlv_17 = None
        otherlv_18 = None
        lv_widthSpec_3_0 = None
        lv_typeParms_6_0 = None
        lv_typeParms_8_0 = None
        lv_parameters_11_0 = None
        lv_parameters_13_0 = None
        lv_host_16_0 = None
        enterRule()
        try:
            #  InternalLF.g:2809:2: ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) ) )
            #  InternalLF.g:2810:2: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) )
            #  InternalLF.g:2810:2: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? ) )
            #  InternalLF.g:2811:3: ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' otherlv_2= 'new' ( (lv_widthSpec_3_0= ruleWidthSpec ) )? ( (otherlv_4= RULE_ID ) ) (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )? otherlv_10= '(' ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )? otherlv_14= ')' ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? )
            #  InternalLF.g:2811:3: ( (lv_name_0_0= RULE_ID ) )
            #  InternalLF.g:2812:4: (lv_name_0_0= RULE_ID )
            #  InternalLF.g:2812:4: (lv_name_0_0= RULE_ID )
            #  InternalLF.g:2813:5: lv_name_0_0= RULE_ID
            lv_name_0_0 = match(input, self.RULE_ID, FOLLOW_67)
            newLeafNode(lv_name_0_0, self.grammarAccess.getInstantiationAccess().getNameIDTerminalRuleCall_0_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getInstantiationRule())
            setWithLastConsumed(current, "name", lv_name_0_0, "org.lflang.LF.ID")
            otherlv_1 = match(input, 53, FOLLOW_68)
            newLeafNode(otherlv_1, self.grammarAccess.getInstantiationAccess().getEqualsSignKeyword_1())
            otherlv_2 = match(input, 54, FOLLOW_42)
            newLeafNode(otherlv_2, self.grammarAccess.getInstantiationAccess().getNewKeyword_2())
            #  InternalLF.g:2837:3: ( (lv_widthSpec_3_0= ruleWidthSpec ) )?
            alt75 = 2
            LA75_0 = input.LA(1)
            if (LA75_0 == 60):
                alt75 = 1
            if alt75 == 1:
                #  InternalLF.g:2838:4: (lv_widthSpec_3_0= ruleWidthSpec )
                #  InternalLF.g:2838:4: (lv_widthSpec_3_0= ruleWidthSpec )
                #  InternalLF.g:2839:5: lv_widthSpec_3_0= ruleWidthSpec
                newCompositeNode(self.grammarAccess.getInstantiationAccess().getWidthSpecWidthSpecParserRuleCall_3_0())
                pushFollow(FOLLOW_5)
                lv_widthSpec_3_0 = ruleWidthSpec()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getInstantiationRule())
                set(current, "widthSpec", lv_widthSpec_3_0, "org.lflang.LF.WidthSpec")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:2856:3: ( (otherlv_4= RULE_ID ) )
            #  InternalLF.g:2857:4: (otherlv_4= RULE_ID )
            #  InternalLF.g:2857:4: (otherlv_4= RULE_ID )
            #  InternalLF.g:2858:5: otherlv_4= RULE_ID
            if current == None:
                current = createModelElement(self.grammarAccess.getInstantiationRule())
            otherlv_4 = match(input, self.RULE_ID, FOLLOW_69)
            newLeafNode(otherlv_4, self.grammarAccess.getInstantiationAccess().getReactorClassReactorDeclCrossReference_4_0())
            #  InternalLF.g:2869:3: (otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>' )?
            alt77 = 2
            LA77_0 = input.LA(1)
            if (LA77_0 == 26):
                alt77 = 1
            if alt77 == 1:
                #  InternalLF.g:2870:4: otherlv_5= '<' ( (lv_typeParms_6_0= ruleTypeParm ) ) (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )* otherlv_9= '>'
                otherlv_5 = match(input, 26, FOLLOW_14)
                newLeafNode(otherlv_5, self.grammarAccess.getInstantiationAccess().getLessThanSignKeyword_5_0())
                #  InternalLF.g:2874:4: ( (lv_typeParms_6_0= ruleTypeParm ) )
                #  InternalLF.g:2875:5: (lv_typeParms_6_0= ruleTypeParm )
                #  InternalLF.g:2875:5: (lv_typeParms_6_0= ruleTypeParm )
                #  InternalLF.g:2876:6: lv_typeParms_6_0= ruleTypeParm
                newCompositeNode(self.grammarAccess.getInstantiationAccess().getTypeParmsTypeParmParserRuleCall_5_1_0())
                pushFollow(FOLLOW_15)
                lv_typeParms_6_0 = self.ruleTypeParm()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getInstantiationRule())
                add(current, "typeParms", lv_typeParms_6_0, "org.lflang.LF.TypeParm")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:2893:4: (otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) ) )*
                while True:
                    alt76 = 2
                    LA76_0 = input.LA(1)
                    if (LA76_0 == 18):
                        alt76 = 1
                    if alt76 == 1:
                        #  InternalLF.g:2894:5: otherlv_7= ',' ( (lv_typeParms_8_0= ruleTypeParm ) )
                        otherlv_7 = match(input, 18, FOLLOW_14)
                        newLeafNode(otherlv_7, self.grammarAccess.getInstantiationAccess().getCommaKeyword_5_2_0())
                        #  InternalLF.g:2898:5: ( (lv_typeParms_8_0= ruleTypeParm ) )
                        #  InternalLF.g:2899:6: (lv_typeParms_8_0= ruleTypeParm )
                        #  InternalLF.g:2899:6: (lv_typeParms_8_0= ruleTypeParm )
                        #  InternalLF.g:2900:7: lv_typeParms_8_0= ruleTypeParm
                        newCompositeNode(self.grammarAccess.getInstantiationAccess().getTypeParmsTypeParmParserRuleCall_5_2_1_0())
                        pushFollow(FOLLOW_15)
                        lv_typeParms_8_0 = self.ruleTypeParm()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getInstantiationRule())
                        add(current, "typeParms", lv_typeParms_8_0, "org.lflang.LF.TypeParm")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                otherlv_9 = match(input, 27, FOLLOW_36)
                newLeafNode(otherlv_9, self.grammarAccess.getInstantiationAccess().getGreaterThanSignKeyword_5_3())
            otherlv_10 = match(input, 28, FOLLOW_37)
            newLeafNode(otherlv_10, self.grammarAccess.getInstantiationAccess().getLeftParenthesisKeyword_6())
            #  InternalLF.g:2927:3: ( ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )* )?
            alt79 = 2
            LA79_0 = input.LA(1)
            if (LA79_0 == self.RULE_ID):
                alt79 = 1
            if alt79 == 1:
                #  InternalLF.g:2928:4: ( (lv_parameters_11_0= ruleAssignment ) ) (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )*
                #  InternalLF.g:2928:4: ( (lv_parameters_11_0= ruleAssignment ) )
                #  InternalLF.g:2929:5: (lv_parameters_11_0= ruleAssignment )
                #  InternalLF.g:2929:5: (lv_parameters_11_0= ruleAssignment )
                #  InternalLF.g:2930:6: lv_parameters_11_0= ruleAssignment
                newCompositeNode(self.grammarAccess.getInstantiationAccess().getParametersAssignmentParserRuleCall_7_0_0())
                pushFollow(FOLLOW_18)
                lv_parameters_11_0 = ruleAssignment()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getInstantiationRule())
                add(current, "parameters", lv_parameters_11_0, "org.lflang.LF.Assignment")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:2947:4: (otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) ) )*
                while True:
                    alt78 = 2
                    LA78_0 = input.LA(1)
                    if (LA78_0 == 18):
                        alt78 = 1
                    if alt78 == 1:
                        #  InternalLF.g:2948:5: otherlv_12= ',' ( (lv_parameters_13_0= ruleAssignment ) )
                        otherlv_12 = match(input, 18, FOLLOW_5)
                        newLeafNode(otherlv_12, self.grammarAccess.getInstantiationAccess().getCommaKeyword_7_1_0())
                        #  InternalLF.g:2952:5: ( (lv_parameters_13_0= ruleAssignment ) )
                        #  InternalLF.g:2953:6: (lv_parameters_13_0= ruleAssignment )
                        #  InternalLF.g:2953:6: (lv_parameters_13_0= ruleAssignment )
                        #  InternalLF.g:2954:7: lv_parameters_13_0= ruleAssignment
                        newCompositeNode(self.grammarAccess.getInstantiationAccess().getParametersAssignmentParserRuleCall_7_1_1_0())
                        pushFollow(FOLLOW_18)
                        lv_parameters_13_0 = ruleAssignment()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getInstantiationRule())
                        add(current, "parameters", lv_parameters_13_0, "org.lflang.LF.Assignment")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
            otherlv_14 = match(input, 29, FOLLOW_70)
            newLeafNode(otherlv_14, self.grammarAccess.getInstantiationAccess().getRightParenthesisKeyword_8())
            #  InternalLF.g:2977:3: ( (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' ) | (otherlv_18= ';' )? )
            alt81 = 2
            LA81_0 = input.LA(1)
            if (LA81_0 == 30):
                alt81 = 1
            elif (LA81_0 == self.EOF or LA81_0 == self.RULE_ID or LA81_0 == 20 or LA81_0 == 28 or LA81_0 == 33 or (LA81_0 >= 35 and LA81_0 <= 36) or (LA81_0 >= 38 and LA81_0 <= 48) or LA81_0 == 52 or LA81_0 == 59 or LA81_0 == 63 or LA81_0 == 68 or (LA81_0 >= 81 and LA81_0 <= 83) or LA81_0 == 85):
                alt81 = 2
            else:
                nvae = NoViableAltException("", 81, 0, input)
                raise nvae
            if alt81 == 1:
                #  InternalLF.g:2978:4: (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' )
                #  InternalLF.g:2978:4: (otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';' )
                #  InternalLF.g:2979:5: otherlv_15= 'at' ( (lv_host_16_0= ruleHost ) ) otherlv_17= ';'
                otherlv_15 = match(input, 30, FOLLOW_20)
                newLeafNode(otherlv_15, self.grammarAccess.getInstantiationAccess().getAtKeyword_9_0_0())
                #  InternalLF.g:2983:5: ( (lv_host_16_0= ruleHost ) )
                #  InternalLF.g:2984:6: (lv_host_16_0= ruleHost )
                #  InternalLF.g:2984:6: (lv_host_16_0= ruleHost )
                #  InternalLF.g:2985:7: lv_host_16_0= ruleHost
                newCompositeNode(self.grammarAccess.getInstantiationAccess().getHostHostParserRuleCall_9_0_1_0())
                pushFollow(FOLLOW_71)
                lv_host_16_0 = ruleHost()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getInstantiationRule())
                set(current, "host", lv_host_16_0, "org.lflang.LF.Host")
                afterParserOrEnumRuleCall()
                otherlv_17 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_17, self.grammarAccess.getInstantiationAccess().getSemicolonKeyword_9_0_2())
            elif alt81 == 2:
                #  InternalLF.g:3008:4: (otherlv_18= ';' )?
                #  InternalLF.g:3008:4: (otherlv_18= ';' )?
                alt80 = 2
                LA80_0 = input.LA(1)
                if (LA80_0 == 20):
                    alt80 = 1
                if alt80 == 1:
                    #  InternalLF.g:3009:5: otherlv_18= ';'
                    otherlv_18 = match(input, 20, FOLLOW_2)
                    newLeafNode(otherlv_18, self.grammarAccess.getInstantiationAccess().getSemicolonKeyword_9_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleInstantiation"
    #  $ANTLR start "entryRuleConnection"
    #  InternalLF.g:3019:1: entryRuleConnection returns [EObject current=null] : iv_ruleConnection= ruleConnection EOF ;
    def entryRuleConnection(self):
        """ generated source for method entryRuleConnection """
        current = None
        iv_ruleConnection = None
        try:
            #  InternalLF.g:3019:51: (iv_ruleConnection= ruleConnection EOF )
            #  InternalLF.g:3020:2: iv_ruleConnection= ruleConnection EOF
            newCompositeNode(self.grammarAccess.getConnectionRule())
            pushFollow(FOLLOW_1)
            iv_ruleConnection = ruleConnection()
            state._fsp -= 1
            current = iv_ruleConnection
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleConnection"
    #  $ANTLR start "ruleConnection"
    #  InternalLF.g:3026:1: ruleConnection returns [EObject current=null] : ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? ) ;
    def ruleConnection(self):
        """ generated source for method ruleConnection """
        current = None
        otherlv_1 = None
        otherlv_3 = None
        otherlv_5 = None
        otherlv_7 = None
        lv_iterated_8_0 = None
        otherlv_9 = None
        lv_physical_10_0 = None
        otherlv_12 = None
        otherlv_14 = None
        otherlv_17 = None
        lv_leftPorts_0_0 = None
        lv_leftPorts_2_0 = None
        lv_leftPorts_4_0 = None
        lv_leftPorts_6_0 = None
        lv_rightPorts_11_0 = None
        lv_rightPorts_13_0 = None
        lv_delay_15_0 = None
        lv_serializer_16_0 = None
        enterRule()
        try:
            #  InternalLF.g:3032:2: ( ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? ) )
            #  InternalLF.g:3033:2: ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? )
            #  InternalLF.g:3033:2: ( ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )? )
            #  InternalLF.g:3034:3: ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) ) (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) ) ( (lv_rightPorts_11_0= ruleVarRef ) ) (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )* (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )? ( (lv_serializer_16_0= ruleSerializer ) )? (otherlv_17= ';' )?
            #  InternalLF.g:3034:3: ( ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* ) | (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? ) )
            alt85 = 2
            LA85_0 = input.LA(1)
            if (LA85_0 == self.RULE_ID or LA85_0 == 63):
                alt85 = 1
            elif (LA85_0 == 28):
                alt85 = 2
            else:
                nvae = NoViableAltException("", 85, 0, input)
                raise nvae
            if alt85 == 1:
                #  InternalLF.g:3035:4: ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* )
                #  InternalLF.g:3035:4: ( ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )* )
                #  InternalLF.g:3036:5: ( (lv_leftPorts_0_0= ruleVarRef ) ) (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )*
                #  InternalLF.g:3036:5: ( (lv_leftPorts_0_0= ruleVarRef ) )
                #  InternalLF.g:3037:6: (lv_leftPorts_0_0= ruleVarRef )
                #  InternalLF.g:3037:6: (lv_leftPorts_0_0= ruleVarRef )
                #  InternalLF.g:3038:7: lv_leftPorts_0_0= ruleVarRef
                newCompositeNode(self.grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_0_0_0())
                pushFollow(FOLLOW_72)
                lv_leftPorts_0_0 = ruleVarRef()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                add(current, "leftPorts", lv_leftPorts_0_0, "org.lflang.LF.VarRef")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:3055:5: (otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) ) )*
                while True:
                    alt82 = 2
                    LA82_0 = input.LA(1)
                    if (LA82_0 == 18):
                        alt82 = 1
                    if alt82 == 1:
                        #  InternalLF.g:3056:6: otherlv_1= ',' ( (lv_leftPorts_2_0= ruleVarRef ) )
                        otherlv_1 = match(input, 18, FOLLOW_61)
                        newLeafNode(otherlv_1, self.grammarAccess.getConnectionAccess().getCommaKeyword_0_0_1_0())
                        #  InternalLF.g:3060:6: ( (lv_leftPorts_2_0= ruleVarRef ) )
                        #  InternalLF.g:3061:7: (lv_leftPorts_2_0= ruleVarRef )
                        #  InternalLF.g:3061:7: (lv_leftPorts_2_0= ruleVarRef )
                        #  InternalLF.g:3062:8: lv_leftPorts_2_0= ruleVarRef
                        newCompositeNode(self.grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_0_1_1_0())
                        pushFollow(FOLLOW_72)
                        lv_leftPorts_2_0 = ruleVarRef()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                        add(current, "leftPorts", lv_leftPorts_2_0, "org.lflang.LF.VarRef")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
            elif alt85 == 2:
                #  InternalLF.g:3082:4: (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? )
                #  InternalLF.g:3082:4: (otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )? )
                #  InternalLF.g:3083:5: otherlv_3= '(' ( (lv_leftPorts_4_0= ruleVarRef ) ) (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )* otherlv_7= ')' ( (lv_iterated_8_0= '+' ) )?
                otherlv_3 = match(input, 28, FOLLOW_61)
                newLeafNode(otherlv_3, self.grammarAccess.getConnectionAccess().getLeftParenthesisKeyword_0_1_0())
                #  InternalLF.g:3087:5: ( (lv_leftPorts_4_0= ruleVarRef ) )
                #  InternalLF.g:3088:6: (lv_leftPorts_4_0= ruleVarRef )
                #  InternalLF.g:3088:6: (lv_leftPorts_4_0= ruleVarRef )
                #  InternalLF.g:3089:7: lv_leftPorts_4_0= ruleVarRef
                newCompositeNode(self.grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_1_1_0())
                pushFollow(FOLLOW_18)
                lv_leftPorts_4_0 = ruleVarRef()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                add(current, "leftPorts", lv_leftPorts_4_0, "org.lflang.LF.VarRef")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:3106:5: (otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) ) )*
                while True:
                    alt83 = 2
                    LA83_0 = input.LA(1)
                    if (LA83_0 == 18):
                        alt83 = 1
                    if alt83 == 1:
                        #  InternalLF.g:3107:6: otherlv_5= ',' ( (lv_leftPorts_6_0= ruleVarRef ) )
                        otherlv_5 = match(input, 18, FOLLOW_61)
                        newLeafNode(otherlv_5, self.grammarAccess.getConnectionAccess().getCommaKeyword_0_1_2_0())
                        #  InternalLF.g:3111:6: ( (lv_leftPorts_6_0= ruleVarRef ) )
                        #  InternalLF.g:3112:7: (lv_leftPorts_6_0= ruleVarRef )
                        #  InternalLF.g:3112:7: (lv_leftPorts_6_0= ruleVarRef )
                        #  InternalLF.g:3113:8: lv_leftPorts_6_0= ruleVarRef
                        newCompositeNode(self.grammarAccess.getConnectionAccess().getLeftPortsVarRefParserRuleCall_0_1_2_1_0())
                        pushFollow(FOLLOW_18)
                        lv_leftPorts_6_0 = ruleVarRef()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                        add(current, "leftPorts", lv_leftPorts_6_0, "org.lflang.LF.VarRef")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                otherlv_7 = match(input, 29, FOLLOW_73)
                newLeafNode(otherlv_7, self.grammarAccess.getConnectionAccess().getRightParenthesisKeyword_0_1_3())
                #  InternalLF.g:3135:5: ( (lv_iterated_8_0= '+' ) )?
                alt84 = 2
                LA84_0 = input.LA(1)
                if (LA84_0 == 55):
                    alt84 = 1
                if alt84 == 1:
                    #  InternalLF.g:3136:6: (lv_iterated_8_0= '+' )
                    #  InternalLF.g:3136:6: (lv_iterated_8_0= '+' )
                    #  InternalLF.g:3137:7: lv_iterated_8_0= '+'
                    lv_iterated_8_0 = match(input, 55, FOLLOW_74)
                    newLeafNode(lv_iterated_8_0, self.grammarAccess.getConnectionAccess().getIteratedPlusSignKeyword_0_1_4_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getConnectionRule())
                    setWithLastConsumed(current, "iterated", lv_iterated_8_0 != None, "+")
            #  InternalLF.g:3151:3: (otherlv_9= '->' | ( (lv_physical_10_0= '~>' ) ) )
            alt86 = 2
            LA86_0 = input.LA(1)
            if (LA86_0 == 49):
                alt86 = 1
            elif (LA86_0 == 56):
                alt86 = 2
            else:
                nvae = NoViableAltException("", 86, 0, input)
                raise nvae
            if alt86 == 1:
                #  InternalLF.g:3152:4: otherlv_9= '->'
                otherlv_9 = match(input, 49, FOLLOW_61)
                newLeafNode(otherlv_9, self.grammarAccess.getConnectionAccess().getHyphenMinusGreaterThanSignKeyword_1_0())
            elif alt86 == 2:
                #  InternalLF.g:3157:4: ( (lv_physical_10_0= '~>' ) )
                #  InternalLF.g:3157:4: ( (lv_physical_10_0= '~>' ) )
                #  InternalLF.g:3158:5: (lv_physical_10_0= '~>' )
                #  InternalLF.g:3158:5: (lv_physical_10_0= '~>' )
                #  InternalLF.g:3159:6: lv_physical_10_0= '~>'
                lv_physical_10_0 = match(input, 56, FOLLOW_61)
                newLeafNode(lv_physical_10_0, self.grammarAccess.getConnectionAccess().getPhysicalTildeGreaterThanSignKeyword_1_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getConnectionRule())
                setWithLastConsumed(current, "physical", lv_physical_10_0 != None, "~>")
            #  InternalLF.g:3172:3: ( (lv_rightPorts_11_0= ruleVarRef ) )
            #  InternalLF.g:3173:4: (lv_rightPorts_11_0= ruleVarRef )
            #  InternalLF.g:3173:4: (lv_rightPorts_11_0= ruleVarRef )
            #  InternalLF.g:3174:5: lv_rightPorts_11_0= ruleVarRef
            newCompositeNode(self.grammarAccess.getConnectionAccess().getRightPortsVarRefParserRuleCall_2_0())
            pushFollow(FOLLOW_75)
            lv_rightPorts_11_0 = ruleVarRef()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getConnectionRule())
            add(current, "rightPorts", lv_rightPorts_11_0, "org.lflang.LF.VarRef")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:3191:3: (otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) ) )*
            while True:
                alt87 = 2
                LA87_0 = input.LA(1)
                if (LA87_0 == 18):
                    alt87 = 1
                if alt87 == 1:
                    #  InternalLF.g:3192:4: otherlv_12= ',' ( (lv_rightPorts_13_0= ruleVarRef ) )
                    otherlv_12 = match(input, 18, FOLLOW_61)
                    newLeafNode(otherlv_12, self.grammarAccess.getConnectionAccess().getCommaKeyword_3_0())
                    #  InternalLF.g:3196:4: ( (lv_rightPorts_13_0= ruleVarRef ) )
                    #  InternalLF.g:3197:5: (lv_rightPorts_13_0= ruleVarRef )
                    #  InternalLF.g:3197:5: (lv_rightPorts_13_0= ruleVarRef )
                    #  InternalLF.g:3198:6: lv_rightPorts_13_0= ruleVarRef
                    newCompositeNode(self.grammarAccess.getConnectionAccess().getRightPortsVarRefParserRuleCall_3_1_0())
                    pushFollow(FOLLOW_75)
                    lv_rightPorts_13_0 = ruleVarRef()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                    add(current, "rightPorts", lv_rightPorts_13_0, "org.lflang.LF.VarRef")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:3216:3: (otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) ) )?
            alt88 = 2
            LA88_0 = input.LA(1)
            if (LA88_0 == 57):
                alt88 = 1
            if alt88 == 1:
                #  InternalLF.g:3217:4: otherlv_14= 'after' ( (lv_delay_15_0= ruleExpression ) )
                otherlv_14 = match(input, 57, FOLLOW_32)
                newLeafNode(otherlv_14, self.grammarAccess.getConnectionAccess().getAfterKeyword_4_0())
                #  InternalLF.g:3221:4: ( (lv_delay_15_0= ruleExpression ) )
                #  InternalLF.g:3222:5: (lv_delay_15_0= ruleExpression )
                #  InternalLF.g:3222:5: (lv_delay_15_0= ruleExpression )
                #  InternalLF.g:3223:6: lv_delay_15_0= ruleExpression
                newCompositeNode(self.grammarAccess.getConnectionAccess().getDelayExpressionParserRuleCall_4_1_0())
                pushFollow(FOLLOW_76)
                lv_delay_15_0 = ruleExpression()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                set(current, "delay", lv_delay_15_0, "org.lflang.LF.Expression")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:3241:3: ( (lv_serializer_16_0= ruleSerializer ) )?
            alt89 = 2
            LA89_0 = input.LA(1)
            if (LA89_0 == 58):
                alt89 = 1
            if alt89 == 1:
                #  InternalLF.g:3242:4: (lv_serializer_16_0= ruleSerializer )
                #  InternalLF.g:3242:4: (lv_serializer_16_0= ruleSerializer )
                #  InternalLF.g:3243:5: lv_serializer_16_0= ruleSerializer
                newCompositeNode(self.grammarAccess.getConnectionAccess().getSerializerSerializerParserRuleCall_5_0())
                pushFollow(FOLLOW_8)
                lv_serializer_16_0 = ruleSerializer()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getConnectionRule())
                set(current, "serializer", lv_serializer_16_0, "org.lflang.LF.Serializer")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:3260:3: (otherlv_17= ';' )?
            alt90 = 2
            LA90_0 = input.LA(1)
            if (LA90_0 == 20):
                alt90 = 1
            if alt90 == 1:
                #  InternalLF.g:3261:4: otherlv_17= ';'
                otherlv_17 = match(input, 20, FOLLOW_2)
                newLeafNode(otherlv_17, self.grammarAccess.getConnectionAccess().getSemicolonKeyword_6())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleConnection"
    #  $ANTLR start "entryRuleSerializer"
    #  InternalLF.g:3270:1: entryRuleSerializer returns [EObject current=null] : iv_ruleSerializer= ruleSerializer EOF ;
    def entryRuleSerializer(self):
        """ generated source for method entryRuleSerializer """
        current = None
        iv_ruleSerializer = None
        try:
            #  InternalLF.g:3270:51: (iv_ruleSerializer= ruleSerializer EOF )
            #  InternalLF.g:3271:2: iv_ruleSerializer= ruleSerializer EOF
            newCompositeNode(self.grammarAccess.getSerializerRule())
            pushFollow(FOLLOW_1)
            iv_ruleSerializer = ruleSerializer()
            state._fsp -= 1
            current = iv_ruleSerializer
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleSerializer"
    #  $ANTLR start "ruleSerializer"
    #  InternalLF.g:3277:1: ruleSerializer returns [EObject current=null] : (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) ) ;
    def ruleSerializer(self):
        """ generated source for method ruleSerializer """
        current = None
        otherlv_0 = None
        lv_type_1_0 = None
        enterRule()
        try:
            #  InternalLF.g:3283:2: ( (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) ) )
            #  InternalLF.g:3284:2: (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) )
            #  InternalLF.g:3284:2: (otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) ) )
            #  InternalLF.g:3285:3: otherlv_0= 'serializer' ( (lv_type_1_0= RULE_STRING ) )
            otherlv_0 = match(input, 58, FOLLOW_7)
            newLeafNode(otherlv_0, self.grammarAccess.getSerializerAccess().getSerializerKeyword_0())
            #  InternalLF.g:3289:3: ( (lv_type_1_0= RULE_STRING ) )
            #  InternalLF.g:3290:4: (lv_type_1_0= RULE_STRING )
            #  InternalLF.g:3290:4: (lv_type_1_0= RULE_STRING )
            #  InternalLF.g:3291:5: lv_type_1_0= RULE_STRING
            lv_type_1_0 = match(input, self.RULE_STRING, FOLLOW_2)
            newLeafNode(lv_type_1_0, self.grammarAccess.getSerializerAccess().getTypeSTRINGTerminalRuleCall_1_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getSerializerRule())
            setWithLastConsumed(current, "type", lv_type_1_0, "org.lflang.LF.STRING")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleSerializer"
    #  $ANTLR start "entryRuleAttribute"
    #  InternalLF.g:3311:1: entryRuleAttribute returns [EObject current=null] : iv_ruleAttribute= ruleAttribute EOF ;
    def entryRuleAttribute(self):
        """ generated source for method entryRuleAttribute """
        current = None
        iv_ruleAttribute = None
        try:
            #  InternalLF.g:3311:50: (iv_ruleAttribute= ruleAttribute EOF )
            #  InternalLF.g:3312:2: iv_ruleAttribute= ruleAttribute EOF
            newCompositeNode(self.grammarAccess.getAttributeRule())
            pushFollow(FOLLOW_1)
            iv_ruleAttribute = ruleAttribute()
            state._fsp -= 1
            current = iv_ruleAttribute
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleAttribute"
    #  $ANTLR start "ruleAttribute"
    #  InternalLF.g:3318:1: ruleAttribute returns [EObject current=null] : (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? ) ;
    def ruleAttribute(self):
        """ generated source for method ruleAttribute """
        current = None
        otherlv_0 = None
        lv_attrName_1_0 = None
        otherlv_2 = None
        otherlv_4 = None
        otherlv_6 = None
        otherlv_7 = None
        lv_attrParms_3_0 = None
        lv_attrParms_5_0 = None
        enterRule()
        try:
            #  InternalLF.g:3324:2: ( (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? ) )
            #  InternalLF.g:3325:2: (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? )
            #  InternalLF.g:3325:2: (otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )? )
            #  InternalLF.g:3326:3: otherlv_0= '@' ( (lv_attrName_1_0= RULE_ID ) ) (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )?
            otherlv_0 = match(input, 59, FOLLOW_5)
            newLeafNode(otherlv_0, self.grammarAccess.getAttributeAccess().getCommercialAtKeyword_0())
            #  InternalLF.g:3330:3: ( (lv_attrName_1_0= RULE_ID ) )
            #  InternalLF.g:3331:4: (lv_attrName_1_0= RULE_ID )
            #  InternalLF.g:3331:4: (lv_attrName_1_0= RULE_ID )
            #  InternalLF.g:3332:5: lv_attrName_1_0= RULE_ID
            lv_attrName_1_0 = match(input, self.RULE_ID, FOLLOW_77)
            newLeafNode(lv_attrName_1_0, self.grammarAccess.getAttributeAccess().getAttrNameIDTerminalRuleCall_1_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getAttributeRule())
            setWithLastConsumed(current, "attrName", lv_attrName_1_0, "org.lflang.LF.ID")
            #  InternalLF.g:3348:3: (otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')' )?
            alt94 = 2
            LA94_0 = input.LA(1)
            if (LA94_0 == 28):
                alt94 = 1
            if alt94 == 1:
                #  InternalLF.g:3349:4: otherlv_2= '(' ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )? otherlv_7= ')'
                otherlv_2 = match(input, 28, FOLLOW_78)
                newLeafNode(otherlv_2, self.grammarAccess.getAttributeAccess().getLeftParenthesisKeyword_2_0())
                #  InternalLF.g:3353:4: ( ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )? )?
                alt93 = 2
                LA93_0 = input.LA(1)
                if ((LA93_0 >= self.RULE_STRING and LA93_0 <= self.RULE_NEGINT) or LA93_0 == 62 or LA93_0 == 69):
                    alt93 = 1
                if alt93 == 1:
                    #  InternalLF.g:3354:5: ( (lv_attrParms_3_0= ruleAttrParm ) ) (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )* (otherlv_6= ',' )?
                    #  InternalLF.g:3354:5: ( (lv_attrParms_3_0= ruleAttrParm ) )
                    #  InternalLF.g:3355:6: (lv_attrParms_3_0= ruleAttrParm )
                    #  InternalLF.g:3355:6: (lv_attrParms_3_0= ruleAttrParm )
                    #  InternalLF.g:3356:7: lv_attrParms_3_0= ruleAttrParm
                    newCompositeNode(self.grammarAccess.getAttributeAccess().getAttrParmsAttrParmParserRuleCall_2_1_0_0())
                    pushFollow(FOLLOW_18)
                    lv_attrParms_3_0 = ruleAttrParm()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getAttributeRule())
                    add(current, "attrParms", lv_attrParms_3_0, "org.lflang.LF.AttrParm")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:3373:5: (otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) ) )*
                    while True:
                        alt91 = 2
                        LA91_0 = input.LA(1)
                        if (LA91_0 == 18):
                            LA91_1 = input.LA(2)
                            if ((LA91_1 >= self.RULE_STRING and LA91_1 <= self.RULE_NEGINT) or LA91_1 == 62 or LA91_1 == 69):
                                alt91 = 1
                        if alt91 == 1:
                            #  InternalLF.g:3374:6: otherlv_4= ',' ( (lv_attrParms_5_0= ruleAttrParm ) )
                            otherlv_4 = match(input, 18, FOLLOW_79)
                            newLeafNode(otherlv_4, self.grammarAccess.getAttributeAccess().getCommaKeyword_2_1_1_0())
                            #  InternalLF.g:3378:6: ( (lv_attrParms_5_0= ruleAttrParm ) )
                            #  InternalLF.g:3379:7: (lv_attrParms_5_0= ruleAttrParm )
                            #  InternalLF.g:3379:7: (lv_attrParms_5_0= ruleAttrParm )
                            #  InternalLF.g:3380:8: lv_attrParms_5_0= ruleAttrParm
                            newCompositeNode(self.grammarAccess.getAttributeAccess().getAttrParmsAttrParmParserRuleCall_2_1_1_1_0())
                            pushFollow(FOLLOW_18)
                            lv_attrParms_5_0 = ruleAttrParm()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getAttributeRule())
                            add(current, "attrParms", lv_attrParms_5_0, "org.lflang.LF.AttrParm")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                    #  InternalLF.g:3398:5: (otherlv_6= ',' )?
                    alt92 = 2
                    LA92_0 = input.LA(1)
                    if (LA92_0 == 18):
                        alt92 = 1
                    if alt92 == 1:
                        #  InternalLF.g:3399:6: otherlv_6= ','
                        otherlv_6 = match(input, 18, FOLLOW_47)
                        newLeafNode(otherlv_6, self.grammarAccess.getAttributeAccess().getCommaKeyword_2_1_2())
                otherlv_7 = match(input, 29, FOLLOW_2)
                newLeafNode(otherlv_7, self.grammarAccess.getAttributeAccess().getRightParenthesisKeyword_2_2())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleAttribute"
    #  $ANTLR start "entryRuleAttrParm"
    #  InternalLF.g:3414:1: entryRuleAttrParm returns [EObject current=null] : iv_ruleAttrParm= ruleAttrParm EOF ;
    def entryRuleAttrParm(self):
        """ generated source for method entryRuleAttrParm """
        current = None
        iv_ruleAttrParm = None
        try:
            #  InternalLF.g:3414:49: (iv_ruleAttrParm= ruleAttrParm EOF )
            #  InternalLF.g:3415:2: iv_ruleAttrParm= ruleAttrParm EOF
            newCompositeNode(self.grammarAccess.getAttrParmRule())
            pushFollow(FOLLOW_1)
            iv_ruleAttrParm = ruleAttrParm()
            state._fsp -= 1
            current = iv_ruleAttrParm
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleAttrParm"
    #  $ANTLR start "ruleAttrParm"
    #  InternalLF.g:3421:1: ruleAttrParm returns [EObject current=null] : ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) ) ;
    def ruleAttrParm(self):
        """ generated source for method ruleAttrParm """
        current = None
        lv_name_0_0 = None
        otherlv_1 = None
        lv_value_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:3427:2: ( ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) ) )
            #  InternalLF.g:3428:2: ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) )
            #  InternalLF.g:3428:2: ( ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) ) )
            #  InternalLF.g:3429:3: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )? ( (lv_value_2_0= ruleAttrParmValue ) )
            #  InternalLF.g:3429:3: ( ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '=' )?
            alt95 = 2
            LA95_0 = input.LA(1)
            if (LA95_0 == self.RULE_ID):
                alt95 = 1
            if alt95 == 1:
                #  InternalLF.g:3430:4: ( (lv_name_0_0= RULE_ID ) ) otherlv_1= '='
                #  InternalLF.g:3430:4: ( (lv_name_0_0= RULE_ID ) )
                #  InternalLF.g:3431:5: (lv_name_0_0= RULE_ID )
                #  InternalLF.g:3431:5: (lv_name_0_0= RULE_ID )
                #  InternalLF.g:3432:6: lv_name_0_0= RULE_ID
                lv_name_0_0 = match(input, self.RULE_ID, FOLLOW_67)
                newLeafNode(lv_name_0_0, self.grammarAccess.getAttrParmAccess().getNameIDTerminalRuleCall_0_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getAttrParmRule())
                setWithLastConsumed(current, "name", lv_name_0_0, "org.lflang.LF.ID")
                otherlv_1 = match(input, 53, FOLLOW_79)
                newLeafNode(otherlv_1, self.grammarAccess.getAttrParmAccess().getEqualsSignKeyword_0_1())
            #  InternalLF.g:3453:3: ( (lv_value_2_0= ruleAttrParmValue ) )
            #  InternalLF.g:3454:4: (lv_value_2_0= ruleAttrParmValue )
            #  InternalLF.g:3454:4: (lv_value_2_0= ruleAttrParmValue )
            #  InternalLF.g:3455:5: lv_value_2_0= ruleAttrParmValue
            newCompositeNode(self.grammarAccess.getAttrParmAccess().getValueAttrParmValueParserRuleCall_1_0())
            pushFollow(FOLLOW_2)
            lv_value_2_0 = ruleAttrParmValue()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getAttrParmRule())
            set(current, "value", lv_value_2_0, "org.lflang.LF.AttrParmValue")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleAttrParm"
    #  $ANTLR start "entryRuleAttrParmValue"
    #  InternalLF.g:3476:1: entryRuleAttrParmValue returns [EObject current=null] : iv_ruleAttrParmValue= ruleAttrParmValue EOF ;
    def entryRuleAttrParmValue(self):
        """ generated source for method entryRuleAttrParmValue """
        current = None
        iv_ruleAttrParmValue = None
        try:
            #  InternalLF.g:3476:54: (iv_ruleAttrParmValue= ruleAttrParmValue EOF )
            #  InternalLF.g:3477:2: iv_ruleAttrParmValue= ruleAttrParmValue EOF
            newCompositeNode(self.grammarAccess.getAttrParmValueRule())
            pushFollow(FOLLOW_1)
            iv_ruleAttrParmValue = ruleAttrParmValue()
            state._fsp -= 1
            current = iv_ruleAttrParmValue
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleAttrParmValue"
    #  $ANTLR start "ruleAttrParmValue"
    #  InternalLF.g:3483:1: ruleAttrParmValue returns [EObject current=null] : ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) ) ;
    def ruleAttrParmValue(self):
        """ generated source for method ruleAttrParmValue """
        current = None
        lv_str_0_0 = None
        lv_int_1_0 = None
        lv_bool_2_0 = None
        lv_float_3_0 = None
        enterRule()
        try:
            #  InternalLF.g:3489:2: ( ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) ) )
            #  InternalLF.g:3490:2: ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) )
            #  InternalLF.g:3490:2: ( ( (lv_str_0_0= RULE_STRING ) ) | ( (lv_int_1_0= ruleSignedInt ) ) | ( (lv_bool_2_0= ruleBoolean ) ) | ( (lv_float_3_0= ruleSignedFloat ) ) )
            alt96 = 4
            if input.LA(1) == self.RULE_STRING:
                alt96 = 1
            elif input.LA(1) == self.RULE_INT:
                LA96_2 = input.LA(2)
                if (LA96_2 == 62):
                    alt96 = 4
                elif (LA96_2 == self.EOF or LA96_2 == 18 or LA96_2 == 29):
                    alt96 = 2
                else:
                    nvae = NoViableAltException("", 96, 2, input)
                    raise nvae
            elif input.LA(1) == self.RULE_NEGINT:
                LA96_3 = input.LA(2)
                if (LA96_3 == self.EOF or LA96_3 == 18 or LA96_3 == 29):
                    alt96 = 2
                elif (LA96_3 == 62):
                    alt96 = 4
                else:
                    nvae = NoViableAltException("", 96, 3, input)
                    raise nvae
            elif input.LA(1) == self.RULE_TRUE:
                pass
            elif input.LA(1) == self.RULE_FALSE:
                alt96 = 3
            elif input.LA(1) == 62:
                pass
            elif input.LA(1) == 69:
                alt96 = 4
            else:
                nvae = NoViableAltException("", 96, 0, input)
                raise nvae
            if alt96 == 1:
                #  InternalLF.g:3491:3: ( (lv_str_0_0= RULE_STRING ) )
                #  InternalLF.g:3491:3: ( (lv_str_0_0= RULE_STRING ) )
                #  InternalLF.g:3492:4: (lv_str_0_0= RULE_STRING )
                #  InternalLF.g:3492:4: (lv_str_0_0= RULE_STRING )
                #  InternalLF.g:3493:5: lv_str_0_0= RULE_STRING
                lv_str_0_0 = match(input, self.RULE_STRING, FOLLOW_2)
                newLeafNode(lv_str_0_0, self.grammarAccess.getAttrParmValueAccess().getStrSTRINGTerminalRuleCall_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getAttrParmValueRule())
                setWithLastConsumed(current, "str", lv_str_0_0, "org.lflang.LF.STRING")
            elif alt96 == 2:
                #  InternalLF.g:3510:3: ( (lv_int_1_0= ruleSignedInt ) )
                #  InternalLF.g:3510:3: ( (lv_int_1_0= ruleSignedInt ) )
                #  InternalLF.g:3511:4: (lv_int_1_0= ruleSignedInt )
                #  InternalLF.g:3511:4: (lv_int_1_0= ruleSignedInt )
                #  InternalLF.g:3512:5: lv_int_1_0= ruleSignedInt
                newCompositeNode(self.grammarAccess.getAttrParmValueAccess().getIntSignedIntParserRuleCall_1_0())
                pushFollow(FOLLOW_2)
                lv_int_1_0 = ruleSignedInt()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getAttrParmValueRule())
                set(current, "int", lv_int_1_0, "org.lflang.LF.SignedInt")
                afterParserOrEnumRuleCall()
            elif alt96 == 3:
                #  InternalLF.g:3530:3: ( (lv_bool_2_0= ruleBoolean ) )
                #  InternalLF.g:3530:3: ( (lv_bool_2_0= ruleBoolean ) )
                #  InternalLF.g:3531:4: (lv_bool_2_0= ruleBoolean )
                #  InternalLF.g:3531:4: (lv_bool_2_0= ruleBoolean )
                #  InternalLF.g:3532:5: lv_bool_2_0= ruleBoolean
                newCompositeNode(self.grammarAccess.getAttrParmValueAccess().getBoolBooleanParserRuleCall_2_0())
                pushFollow(FOLLOW_2)
                lv_bool_2_0 = self.ruleBoolean()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getAttrParmValueRule())
                set(current, "bool", lv_bool_2_0, "org.lflang.LF.Boolean")
                afterParserOrEnumRuleCall()
            elif alt96 == 4:
                #  InternalLF.g:3550:3: ( (lv_float_3_0= ruleSignedFloat ) )
                #  InternalLF.g:3550:3: ( (lv_float_3_0= ruleSignedFloat ) )
                #  InternalLF.g:3551:4: (lv_float_3_0= ruleSignedFloat )
                #  InternalLF.g:3551:4: (lv_float_3_0= ruleSignedFloat )
                #  InternalLF.g:3552:5: lv_float_3_0= ruleSignedFloat
                newCompositeNode(self.grammarAccess.getAttrParmValueAccess().getFloatSignedFloatParserRuleCall_3_0())
                pushFollow(FOLLOW_2)
                lv_float_3_0 = ruleSignedFloat()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getAttrParmValueRule())
                set(current, "float", lv_float_3_0, "org.lflang.LF.SignedFloat")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleAttrParmValue"
    #  $ANTLR start "entryRuleKeyValuePairs"
    #  InternalLF.g:3573:1: entryRuleKeyValuePairs returns [EObject current=null] : iv_ruleKeyValuePairs= ruleKeyValuePairs EOF ;
    def entryRuleKeyValuePairs(self):
        """ generated source for method entryRuleKeyValuePairs """
        current = None
        iv_ruleKeyValuePairs = None
        try:
            #  InternalLF.g:3573:54: (iv_ruleKeyValuePairs= ruleKeyValuePairs EOF )
            #  InternalLF.g:3574:2: iv_ruleKeyValuePairs= ruleKeyValuePairs EOF
            newCompositeNode(self.grammarAccess.getKeyValuePairsRule())
            pushFollow(FOLLOW_1)
            iv_ruleKeyValuePairs = ruleKeyValuePairs()
            state._fsp -= 1
            current = iv_ruleKeyValuePairs
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleKeyValuePairs"
    #  $ANTLR start "ruleKeyValuePairs"
    #  InternalLF.g:3580:1: ruleKeyValuePairs returns [EObject current=null] : ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' ) ;
    def ruleKeyValuePairs(self):
        """ generated source for method ruleKeyValuePairs """
        current = None
        otherlv_1 = None
        otherlv_3 = None
        otherlv_5 = None
        otherlv_6 = None
        lv_pairs_2_0 = None
        lv_pairs_4_0 = None
        enterRule()
        try:
            #  InternalLF.g:3586:2: ( ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' ) )
            #  InternalLF.g:3587:2: ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' )
            #  InternalLF.g:3587:2: ( () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}' )
            #  InternalLF.g:3588:3: () otherlv_1= '{' ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )? otherlv_6= '}'
            #  InternalLF.g:3588:3: ()
            #  InternalLF.g:3589:4: 
            current = forceCreateModelElement(self.grammarAccess.getKeyValuePairsAccess().getKeyValuePairsAction_0(), current)
            otherlv_1 = match(input, 32, FOLLOW_80)
            newLeafNode(otherlv_1, self.grammarAccess.getKeyValuePairsAccess().getLeftCurlyBracketKeyword_1())
            #  InternalLF.g:3599:3: ( ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )? )?
            alt99 = 2
            LA99_0 = input.LA(1)
            if (LA99_0 == self.RULE_ID or LA99_0 == 68):
                alt99 = 1
            if alt99 == 1:
                #  InternalLF.g:3600:4: ( (lv_pairs_2_0= ruleKeyValuePair ) ) (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )* (otherlv_5= ',' )?
                #  InternalLF.g:3600:4: ( (lv_pairs_2_0= ruleKeyValuePair ) )
                #  InternalLF.g:3601:5: (lv_pairs_2_0= ruleKeyValuePair )
                #  InternalLF.g:3601:5: (lv_pairs_2_0= ruleKeyValuePair )
                #  InternalLF.g:3602:6: lv_pairs_2_0= ruleKeyValuePair
                newCompositeNode(self.grammarAccess.getKeyValuePairsAccess().getPairsKeyValuePairParserRuleCall_2_0_0())
                pushFollow(FOLLOW_34)
                lv_pairs_2_0 = ruleKeyValuePair()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getKeyValuePairsRule())
                add(current, "pairs", lv_pairs_2_0, "org.lflang.LF.KeyValuePair")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:3619:4: (otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) ) )*
                while True:
                    alt97 = 2
                    LA97_0 = input.LA(1)
                    if (LA97_0 == 18):
                        LA97_1 = input.LA(2)
                        if (LA97_1 == self.RULE_ID or LA97_1 == 68):
                            alt97 = 1
                    if alt97 == 1:
                        #  InternalLF.g:3620:5: otherlv_3= ',' ( (lv_pairs_4_0= ruleKeyValuePair ) )
                        otherlv_3 = match(input, 18, FOLLOW_81)
                        newLeafNode(otherlv_3, self.grammarAccess.getKeyValuePairsAccess().getCommaKeyword_2_1_0())
                        #  InternalLF.g:3624:5: ( (lv_pairs_4_0= ruleKeyValuePair ) )
                        #  InternalLF.g:3625:6: (lv_pairs_4_0= ruleKeyValuePair )
                        #  InternalLF.g:3625:6: (lv_pairs_4_0= ruleKeyValuePair )
                        #  InternalLF.g:3626:7: lv_pairs_4_0= ruleKeyValuePair
                        newCompositeNode(self.grammarAccess.getKeyValuePairsAccess().getPairsKeyValuePairParserRuleCall_2_1_1_0())
                        pushFollow(FOLLOW_34)
                        lv_pairs_4_0 = ruleKeyValuePair()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getKeyValuePairsRule())
                        add(current, "pairs", lv_pairs_4_0, "org.lflang.LF.KeyValuePair")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                #  InternalLF.g:3644:4: (otherlv_5= ',' )?
                alt98 = 2
                LA98_0 = input.LA(1)
                if (LA98_0 == 18):
                    alt98 = 1
                if alt98 == 1:
                    #  InternalLF.g:3645:5: otherlv_5= ','
                    otherlv_5 = match(input, 18, FOLLOW_82)
                    newLeafNode(otherlv_5, self.grammarAccess.getKeyValuePairsAccess().getCommaKeyword_2_2())
            otherlv_6 = match(input, 33, FOLLOW_2)
            newLeafNode(otherlv_6, self.grammarAccess.getKeyValuePairsAccess().getRightCurlyBracketKeyword_3())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleKeyValuePairs"
    #  $ANTLR start "entryRuleKeyValuePair"
    #  InternalLF.g:3659:1: entryRuleKeyValuePair returns [EObject current=null] : iv_ruleKeyValuePair= ruleKeyValuePair EOF ;
    def entryRuleKeyValuePair(self):
        """ generated source for method entryRuleKeyValuePair """
        current = None
        iv_ruleKeyValuePair = None
        try:
            #  InternalLF.g:3659:53: (iv_ruleKeyValuePair= ruleKeyValuePair EOF )
            #  InternalLF.g:3660:2: iv_ruleKeyValuePair= ruleKeyValuePair EOF
            newCompositeNode(self.grammarAccess.getKeyValuePairRule())
            pushFollow(FOLLOW_1)
            iv_ruleKeyValuePair = ruleKeyValuePair()
            state._fsp -= 1
            current = iv_ruleKeyValuePair
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleKeyValuePair"
    #  $ANTLR start "ruleKeyValuePair"
    #  InternalLF.g:3666:1: ruleKeyValuePair returns [EObject current=null] : ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) ) ;
    def ruleKeyValuePair(self):
        """ generated source for method ruleKeyValuePair """
        current = None
        otherlv_1 = None
        lv_name_0_0 = None
        lv_value_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:3672:2: ( ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) ) )
            #  InternalLF.g:3673:2: ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) )
            #  InternalLF.g:3673:2: ( ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) ) )
            #  InternalLF.g:3674:3: ( (lv_name_0_0= ruleKebab ) ) otherlv_1= ':' ( (lv_value_2_0= ruleElement ) )
            #  InternalLF.g:3674:3: ( (lv_name_0_0= ruleKebab ) )
            #  InternalLF.g:3675:4: (lv_name_0_0= ruleKebab )
            #  InternalLF.g:3675:4: (lv_name_0_0= ruleKebab )
            #  InternalLF.g:3676:5: lv_name_0_0= ruleKebab
            newCompositeNode(self.grammarAccess.getKeyValuePairAccess().getNameKebabParserRuleCall_0_0())
            pushFollow(FOLLOW_83)
            lv_name_0_0 = ruleKebab()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getKeyValuePairRule())
            set(current, "name", lv_name_0_0, "org.lflang.LF.Kebab")
            afterParserOrEnumRuleCall()
            otherlv_1 = match(input, 37, FOLLOW_84)
            newLeafNode(otherlv_1, self.grammarAccess.getKeyValuePairAccess().getColonKeyword_1())
            #  InternalLF.g:3697:3: ( (lv_value_2_0= ruleElement ) )
            #  InternalLF.g:3698:4: (lv_value_2_0= ruleElement )
            #  InternalLF.g:3698:4: (lv_value_2_0= ruleElement )
            #  InternalLF.g:3699:5: lv_value_2_0= ruleElement
            newCompositeNode(self.grammarAccess.getKeyValuePairAccess().getValueElementParserRuleCall_2_0())
            pushFollow(FOLLOW_2)
            lv_value_2_0 = ruleElement()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getKeyValuePairRule())
            set(current, "value", lv_value_2_0, "org.lflang.LF.Element")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleKeyValuePair"
    #  $ANTLR start "entryRuleArray"
    #  InternalLF.g:3720:1: entryRuleArray returns [EObject current=null] : iv_ruleArray= ruleArray EOF ;
    def entryRuleArray(self):
        """ generated source for method entryRuleArray """
        current = None
        iv_ruleArray = None
        try:
            #  InternalLF.g:3720:46: (iv_ruleArray= ruleArray EOF )
            #  InternalLF.g:3721:2: iv_ruleArray= ruleArray EOF
            newCompositeNode(self.grammarAccess.getArrayRule())
            pushFollow(FOLLOW_1)
            iv_ruleArray = ruleArray()
            state._fsp -= 1
            current = iv_ruleArray
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleArray"
    #  $ANTLR start "ruleArray"
    #  InternalLF.g:3727:1: ruleArray returns [EObject current=null] : (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' ) ;
    def ruleArray(self):
        """ generated source for method ruleArray """
        current = None
        otherlv_0 = None
        otherlv_2 = None
        otherlv_4 = None
        otherlv_5 = None
        lv_elements_1_0 = None
        lv_elements_3_0 = None
        enterRule()
        try:
            #  InternalLF.g:3733:2: ( (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' ) )
            #  InternalLF.g:3734:2: (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' )
            #  InternalLF.g:3734:2: (otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']' )
            #  InternalLF.g:3735:3: otherlv_0= '[' ( (lv_elements_1_0= ruleElement ) ) (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )* (otherlv_4= ',' )? otherlv_5= ']'
            otherlv_0 = match(input, 60, FOLLOW_84)
            newLeafNode(otherlv_0, self.grammarAccess.getArrayAccess().getLeftSquareBracketKeyword_0())
            #  InternalLF.g:3739:3: ( (lv_elements_1_0= ruleElement ) )
            #  InternalLF.g:3740:4: (lv_elements_1_0= ruleElement )
            #  InternalLF.g:3740:4: (lv_elements_1_0= ruleElement )
            #  InternalLF.g:3741:5: lv_elements_1_0= ruleElement
            newCompositeNode(self.grammarAccess.getArrayAccess().getElementsElementParserRuleCall_1_0())
            pushFollow(FOLLOW_85)
            lv_elements_1_0 = ruleElement()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getArrayRule())
            add(current, "elements", lv_elements_1_0, "org.lflang.LF.Element")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:3758:3: (otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) ) )*
            while True:
                alt100 = 2
                LA100_0 = input.LA(1)
                if (LA100_0 == 18):
                    LA100_1 = input.LA(2)
                    if ((LA100_1 >= self.RULE_STRING and LA100_1 <= self.RULE_CHAR_LIT) or LA100_1 == 32 or LA100_1 == 60 or LA100_1 == 62 or LA100_1 == 69 or LA100_1 == 73 or (LA100_1 >= 75 and LA100_1 <= 76)):
                        alt100 = 1
                if alt100 == 1:
                    #  InternalLF.g:3759:4: otherlv_2= ',' ( (lv_elements_3_0= ruleElement ) )
                    otherlv_2 = match(input, 18, FOLLOW_84)
                    newLeafNode(otherlv_2, self.grammarAccess.getArrayAccess().getCommaKeyword_2_0())
                    #  InternalLF.g:3763:4: ( (lv_elements_3_0= ruleElement ) )
                    #  InternalLF.g:3764:5: (lv_elements_3_0= ruleElement )
                    #  InternalLF.g:3764:5: (lv_elements_3_0= ruleElement )
                    #  InternalLF.g:3765:6: lv_elements_3_0= ruleElement
                    newCompositeNode(self.grammarAccess.getArrayAccess().getElementsElementParserRuleCall_2_1_0())
                    pushFollow(FOLLOW_85)
                    lv_elements_3_0 = ruleElement()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getArrayRule())
                    add(current, "elements", lv_elements_3_0, "org.lflang.LF.Element")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:3783:3: (otherlv_4= ',' )?
            alt101 = 2
            LA101_0 = input.LA(1)
            if (LA101_0 == 18):
                alt101 = 1
            if alt101 == 1:
                #  InternalLF.g:3784:4: otherlv_4= ','
                otherlv_4 = match(input, 18, FOLLOW_86)
                newLeafNode(otherlv_4, self.grammarAccess.getArrayAccess().getCommaKeyword_3())
            otherlv_5 = match(input, 61, FOLLOW_2)
            newLeafNode(otherlv_5, self.grammarAccess.getArrayAccess().getRightSquareBracketKeyword_4())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleArray"
    #  $ANTLR start "entryRuleElement"
    #  InternalLF.g:3797:1: entryRuleElement returns [EObject current=null] : iv_ruleElement= ruleElement EOF ;
    def entryRuleElement(self):
        """ generated source for method entryRuleElement """
        current = None
        iv_ruleElement = None
        try:
            #  InternalLF.g:3797:48: (iv_ruleElement= ruleElement EOF )
            #  InternalLF.g:3798:2: iv_ruleElement= ruleElement EOF
            newCompositeNode(self.grammarAccess.getElementRule())
            pushFollow(FOLLOW_1)
            iv_ruleElement = ruleElement()
            state._fsp -= 1
            current = iv_ruleElement
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleElement"
    #  $ANTLR start "ruleElement"
    #  InternalLF.g:3804:1: ruleElement returns [EObject current=null] : ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) ) ;
    def ruleElement(self):
        """ generated source for method ruleElement """
        current = None
        lv_time_3_0 = None
        lv_keyvalue_0_0 = None
        lv_array_1_0 = None
        lv_literal_2_0 = None
        lv_unit_4_0 = None
        lv_id_5_0 = None
        enterRule()
        try:
            #  InternalLF.g:3810:2: ( ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) ) )
            #  InternalLF.g:3811:2: ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) )
            #  InternalLF.g:3811:2: ( ( (lv_keyvalue_0_0= ruleKeyValuePairs ) ) | ( (lv_array_1_0= ruleArray ) ) | ( (lv_literal_2_0= ruleLiteral ) ) | ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) ) | ( (lv_id_5_0= rulePath ) ) )
            alt102 = 5
            if input.LA(1) == 32:
                alt102 = 1
            elif input.LA(1) == 60:
                alt102 = 2
            elif input.LA(1) == self.RULE_STRING:
                pass
            elif input.LA(1) == self.RULE_TRUE:
                pass
            elif input.LA(1) == self.RULE_FALSE:
                pass
            elif input.LA(1) == self.RULE_NEGINT:
                pass
            elif input.LA(1) == self.RULE_CHAR_LIT:
                pass
            elif input.LA(1) == 69:
                alt102 = 3
            elif input.LA(1) == self.RULE_INT:
                LA102_4 = input.LA(2)
                if (LA102_4 == self.EOF or LA102_4 == 18 or LA102_4 == 33 or (LA102_4 >= 61 and LA102_4 <= 62)):
                    alt102 = 3
                elif (LA102_4 == self.RULE_ID):
                    alt102 = 4
                else:
                    nvae = NoViableAltException("", 102, 4, input)
                    raise nvae
            elif input.LA(1) == 62:
                LA102_5 = input.LA(2)
                if (LA102_5 == self.EOF or LA102_5 == self.RULE_ID or LA102_5 == 18 or LA102_5 == 33 or (LA102_5 >= 61 and LA102_5 <= 62) or (LA102_5 >= 73 and LA102_5 <= 76)):
                    alt102 = 5
                elif (LA102_5 == self.RULE_INT or LA102_5 == self.RULE_FLOAT_EXP_SUFFIX):
                    alt102 = 3
                else:
                    nvae = NoViableAltException("", 102, 5, input)
                    raise nvae
            elif input.LA(1) == self.RULE_ID:
                pass
            elif input.LA(1) == 73:
                pass
            elif input.LA(1) == 75:
                pass
            elif input.LA(1) == 76:
                alt102 = 5
            else:
                nvae = NoViableAltException("", 102, 0, input)
                raise nvae
            if alt102 == 1:
                #  InternalLF.g:3812:3: ( (lv_keyvalue_0_0= ruleKeyValuePairs ) )
                #  InternalLF.g:3812:3: ( (lv_keyvalue_0_0= ruleKeyValuePairs ) )
                #  InternalLF.g:3813:4: (lv_keyvalue_0_0= ruleKeyValuePairs )
                #  InternalLF.g:3813:4: (lv_keyvalue_0_0= ruleKeyValuePairs )
                #  InternalLF.g:3814:5: lv_keyvalue_0_0= ruleKeyValuePairs
                newCompositeNode(self.grammarAccess.getElementAccess().getKeyvalueKeyValuePairsParserRuleCall_0_0())
                pushFollow(FOLLOW_2)
                lv_keyvalue_0_0 = self.ruleKeyValuePairs()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getElementRule())
                set(current, "keyvalue", lv_keyvalue_0_0, "org.lflang.LF.KeyValuePairs")
                afterParserOrEnumRuleCall()
            elif alt102 == 2:
                #  InternalLF.g:3832:3: ( (lv_array_1_0= ruleArray ) )
                #  InternalLF.g:3832:3: ( (lv_array_1_0= ruleArray ) )
                #  InternalLF.g:3833:4: (lv_array_1_0= ruleArray )
                #  InternalLF.g:3833:4: (lv_array_1_0= ruleArray )
                #  InternalLF.g:3834:5: lv_array_1_0= ruleArray
                newCompositeNode(self.grammarAccess.getElementAccess().getArrayArrayParserRuleCall_1_0())
                pushFollow(FOLLOW_2)
                lv_array_1_0 = self.ruleArray()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getElementRule())
                set(current, "array", lv_array_1_0, "org.lflang.LF.Array")
                afterParserOrEnumRuleCall()
            elif alt102 == 3:
                #  InternalLF.g:3852:3: ( (lv_literal_2_0= ruleLiteral ) )
                #  InternalLF.g:3852:3: ( (lv_literal_2_0= ruleLiteral ) )
                #  InternalLF.g:3853:4: (lv_literal_2_0= ruleLiteral )
                #  InternalLF.g:3853:4: (lv_literal_2_0= ruleLiteral )
                #  InternalLF.g:3854:5: lv_literal_2_0= ruleLiteral
                newCompositeNode(self.grammarAccess.getElementAccess().getLiteralLiteralParserRuleCall_2_0())
                pushFollow(FOLLOW_2)
                lv_literal_2_0 = ruleLiteral()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getElementRule())
                set(current, "literal", lv_literal_2_0, "org.lflang.LF.Literal")
                afterParserOrEnumRuleCall()
            elif alt102 == 4:
                #  InternalLF.g:3872:3: ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) )
                #  InternalLF.g:3872:3: ( ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) ) )
                #  InternalLF.g:3873:4: ( (lv_time_3_0= RULE_INT ) ) ( (lv_unit_4_0= ruleTimeUnit ) )
                #  InternalLF.g:3873:4: ( (lv_time_3_0= RULE_INT ) )
                #  InternalLF.g:3874:5: (lv_time_3_0= RULE_INT )
                #  InternalLF.g:3874:5: (lv_time_3_0= RULE_INT )
                #  InternalLF.g:3875:6: lv_time_3_0= RULE_INT
                lv_time_3_0 = match(input, self.RULE_INT, FOLLOW_5)
                newLeafNode(lv_time_3_0, self.grammarAccess.getElementAccess().getTimeINTTerminalRuleCall_3_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getElementRule())
                setWithLastConsumed(current, "time", lv_time_3_0, "org.lflang.LF.INT")
                #  InternalLF.g:3891:4: ( (lv_unit_4_0= ruleTimeUnit ) )
                #  InternalLF.g:3892:5: (lv_unit_4_0= ruleTimeUnit )
                #  InternalLF.g:3892:5: (lv_unit_4_0= ruleTimeUnit )
                #  InternalLF.g:3893:6: lv_unit_4_0= ruleTimeUnit
                newCompositeNode(self.grammarAccess.getElementAccess().getUnitTimeUnitParserRuleCall_3_1_0())
                pushFollow(FOLLOW_2)
                lv_unit_4_0 = ruleTimeUnit()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getElementRule())
                set(current, "unit", lv_unit_4_0, "org.lflang.LF.TimeUnit")
                afterParserOrEnumRuleCall()
            elif alt102 == 5:
                #  InternalLF.g:3912:3: ( (lv_id_5_0= rulePath ) )
                #  InternalLF.g:3912:3: ( (lv_id_5_0= rulePath ) )
                #  InternalLF.g:3913:4: (lv_id_5_0= rulePath )
                #  InternalLF.g:3913:4: (lv_id_5_0= rulePath )
                #  InternalLF.g:3914:5: lv_id_5_0= rulePath
                newCompositeNode(self.grammarAccess.getElementAccess().getIdPathParserRuleCall_4_0())
                pushFollow(FOLLOW_2)
                lv_id_5_0 = rulePath()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getElementRule())
                set(current, "id", lv_id_5_0, "org.lflang.LF.Path")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleElement"
    #  $ANTLR start "entryRuleTypedVariable"
    #  InternalLF.g:3935:1: entryRuleTypedVariable returns [EObject current=null] : iv_ruleTypedVariable= ruleTypedVariable EOF ;
    def entryRuleTypedVariable(self):
        """ generated source for method entryRuleTypedVariable """
        current = None
        iv_ruleTypedVariable = None
        try:
            #  InternalLF.g:3935:54: (iv_ruleTypedVariable= ruleTypedVariable EOF )
            #  InternalLF.g:3936:2: iv_ruleTypedVariable= ruleTypedVariable EOF
            newCompositeNode(self.grammarAccess.getTypedVariableRule())
            pushFollow(FOLLOW_1)
            iv_ruleTypedVariable = ruleTypedVariable()
            state._fsp -= 1
            current = iv_ruleTypedVariable
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTypedVariable"
    #  $ANTLR start "ruleTypedVariable"
    #  InternalLF.g:3942:1: ruleTypedVariable returns [EObject current=null] : (this_Port_0= rulePort | this_Action_1= ruleAction ) ;
    def ruleTypedVariable(self):
        """ generated source for method ruleTypedVariable """
        current = None
        this_Port_0 = None
        this_Action_1 = None
        enterRule()
        try:
            #  InternalLF.g:3948:2: ( (this_Port_0= rulePort | this_Action_1= ruleAction ) )
            #  InternalLF.g:3949:2: (this_Port_0= rulePort | this_Action_1= ruleAction )
            #  InternalLF.g:3949:2: (this_Port_0= rulePort | this_Action_1= ruleAction )
            alt103 = 2
            alt103 = dfa103.predict(input)
            if alt103 == 1:
                #  InternalLF.g:3950:3: this_Port_0= rulePort
                newCompositeNode(self.grammarAccess.getTypedVariableAccess().getPortParserRuleCall_0())
                pushFollow(FOLLOW_2)
                this_Port_0 = rulePort()
                state._fsp -= 1
                current = this_Port_0
                afterParserOrEnumRuleCall()
            elif alt103 == 2:
                #  InternalLF.g:3959:3: this_Action_1= ruleAction
                newCompositeNode(self.grammarAccess.getTypedVariableAccess().getActionParserRuleCall_1())
                pushFollow(FOLLOW_2)
                this_Action_1 = self.ruleAction()
                state._fsp -= 1
                current = this_Action_1
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTypedVariable"
    #  $ANTLR start "entryRuleVarRef"
    #  InternalLF.g:3971:1: entryRuleVarRef returns [EObject current=null] : iv_ruleVarRef= ruleVarRef EOF ;
    def entryRuleVarRef(self):
        """ generated source for method entryRuleVarRef """
        current = None
        iv_ruleVarRef = None
        try:
            #  InternalLF.g:3971:47: (iv_ruleVarRef= ruleVarRef EOF )
            #  InternalLF.g:3972:2: iv_ruleVarRef= ruleVarRef EOF
            newCompositeNode(self.grammarAccess.getVarRefRule())
            pushFollow(FOLLOW_1)
            iv_ruleVarRef = ruleVarRef()
            state._fsp -= 1
            current = iv_ruleVarRef
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleVarRef"
    #  $ANTLR start "ruleVarRef"
    #  InternalLF.g:3978:1: ruleVarRef returns [EObject current=null] : ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) ) ;
    def ruleVarRef(self):
        """ generated source for method ruleVarRef """
        current = None
        otherlv_0 = None
        otherlv_1 = None
        otherlv_2 = None
        otherlv_3 = None
        lv_interleaved_4_0 = None
        otherlv_5 = None
        otherlv_6 = None
        otherlv_7 = None
        otherlv_8 = None
        otherlv_9 = None
        otherlv_10 = None
        enterRule()
        try:
            #  InternalLF.g:3984:2: ( ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) ) )
            #  InternalLF.g:3985:2: ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) )
            #  InternalLF.g:3985:2: ( ( (otherlv_0= RULE_ID ) ) | ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) ) | ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' ) )
            alt105 = 3
            LA105_0 = input.LA(1)
            if (LA105_0 == self.RULE_ID):
                LA105_1 = input.LA(2)
                if (LA105_1 == self.EOF or LA105_1 == self.RULE_ID or LA105_1 == 18 or LA105_1 == 20 or (LA105_1 >= 28 and LA105_1 <= 29) or LA105_1 == 33 or (LA105_1 >= 35 and LA105_1 <= 36) or (LA105_1 >= 38 and LA105_1 <= 49) or LA105_1 == 52 or (LA105_1 >= 56 and LA105_1 <= 59) or LA105_1 == 63 or LA105_1 == 68 or LA105_1 == 71 or (LA105_1 >= 81 and LA105_1 <= 83) or LA105_1 == 85):
                    alt105 = 1
                elif (LA105_1 == 62):
                    alt105 = 2
                else:
                    nvae = NoViableAltException("", 105, 1, input)
                    raise nvae
            elif (LA105_0 == 63):
                alt105 = 3
            else:
                nvae = NoViableAltException("", 105, 0, input)
                raise nvae
            if alt105 == 1:
                #  InternalLF.g:3986:3: ( (otherlv_0= RULE_ID ) )
                #  InternalLF.g:3986:3: ( (otherlv_0= RULE_ID ) )
                #  InternalLF.g:3987:4: (otherlv_0= RULE_ID )
                #  InternalLF.g:3987:4: (otherlv_0= RULE_ID )
                #  InternalLF.g:3988:5: otherlv_0= RULE_ID
                if current == None:
                    current = createModelElement(self.grammarAccess.getVarRefRule())
                otherlv_0 = match(input, self.RULE_ID, FOLLOW_2)
                newLeafNode(otherlv_0, self.grammarAccess.getVarRefAccess().getVariableVariableCrossReference_0_0())
            elif alt105 == 2:
                #  InternalLF.g:4000:3: ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) )
                #  InternalLF.g:4000:3: ( ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) ) )
                #  InternalLF.g:4001:4: ( (otherlv_1= RULE_ID ) ) otherlv_2= '.' ( (otherlv_3= RULE_ID ) )
                #  InternalLF.g:4001:4: ( (otherlv_1= RULE_ID ) )
                #  InternalLF.g:4002:5: (otherlv_1= RULE_ID )
                #  InternalLF.g:4002:5: (otherlv_1= RULE_ID )
                #  InternalLF.g:4003:6: otherlv_1= RULE_ID
                if current == None:
                    current = createModelElement(self.grammarAccess.getVarRefRule())
                otherlv_1 = match(input, self.RULE_ID, FOLLOW_87)
                newLeafNode(otherlv_1, self.grammarAccess.getVarRefAccess().getContainerInstantiationCrossReference_1_0_0())
                otherlv_2 = match(input, 62, FOLLOW_5)
                newLeafNode(otherlv_2, self.grammarAccess.getVarRefAccess().getFullStopKeyword_1_1())
                #  InternalLF.g:4018:4: ( (otherlv_3= RULE_ID ) )
                #  InternalLF.g:4019:5: (otherlv_3= RULE_ID )
                #  InternalLF.g:4019:5: (otherlv_3= RULE_ID )
                #  InternalLF.g:4020:6: otherlv_3= RULE_ID
                if current == None:
                    current = createModelElement(self.grammarAccess.getVarRefRule())
                otherlv_3 = match(input, self.RULE_ID, FOLLOW_2)
                newLeafNode(otherlv_3, self.grammarAccess.getVarRefAccess().getVariableVariableCrossReference_1_2_0())
            elif alt105 == 3:
                #  InternalLF.g:4033:3: ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' )
                #  InternalLF.g:4033:3: ( ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')' )
                #  InternalLF.g:4034:4: ( (lv_interleaved_4_0= 'interleaved' ) ) otherlv_5= '(' ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) ) otherlv_10= ')'
                #  InternalLF.g:4034:4: ( (lv_interleaved_4_0= 'interleaved' ) )
                #  InternalLF.g:4035:5: (lv_interleaved_4_0= 'interleaved' )
                #  InternalLF.g:4035:5: (lv_interleaved_4_0= 'interleaved' )
                #  InternalLF.g:4036:6: lv_interleaved_4_0= 'interleaved'
                lv_interleaved_4_0 = match(input, 63, FOLLOW_36)
                newLeafNode(lv_interleaved_4_0, self.grammarAccess.getVarRefAccess().getInterleavedInterleavedKeyword_2_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getVarRefRule())
                setWithLastConsumed(current, "interleaved", lv_interleaved_4_0 != None, "interleaved")
                otherlv_5 = match(input, 28, FOLLOW_5)
                newLeafNode(otherlv_5, self.grammarAccess.getVarRefAccess().getLeftParenthesisKeyword_2_1())
                #  InternalLF.g:4052:4: ( ( (otherlv_6= RULE_ID ) ) | ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) ) )
                alt104 = 2
                LA104_0 = input.LA(1)
                if (LA104_0 == self.RULE_ID):
                    LA104_1 = input.LA(2)
                    if (LA104_1 == 62):
                        alt104 = 2
                    elif (LA104_1 == 29):
                        alt104 = 1
                    else:
                        nvae = NoViableAltException("", 104, 1, input)
                        raise nvae
                else:
                    nvae = NoViableAltException("", 104, 0, input)
                    raise nvae
                if alt104 == 1:
                    #  InternalLF.g:4053:5: ( (otherlv_6= RULE_ID ) )
                    #  InternalLF.g:4053:5: ( (otherlv_6= RULE_ID ) )
                    #  InternalLF.g:4054:6: (otherlv_6= RULE_ID )
                    #  InternalLF.g:4054:6: (otherlv_6= RULE_ID )
                    #  InternalLF.g:4055:7: otherlv_6= RULE_ID
                    if current == None:
                        current = createModelElement(self.grammarAccess.getVarRefRule())
                    otherlv_6 = match(input, self.RULE_ID, FOLLOW_47)
                    newLeafNode(otherlv_6, self.grammarAccess.getVarRefAccess().getVariableVariableCrossReference_2_2_0_0())
                elif alt104 == 2:
                    #  InternalLF.g:4067:5: ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) )
                    #  InternalLF.g:4067:5: ( ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) ) )
                    #  InternalLF.g:4068:6: ( (otherlv_7= RULE_ID ) ) otherlv_8= '.' ( (otherlv_9= RULE_ID ) )
                    #  InternalLF.g:4068:6: ( (otherlv_7= RULE_ID ) )
                    #  InternalLF.g:4069:7: (otherlv_7= RULE_ID )
                    #  InternalLF.g:4069:7: (otherlv_7= RULE_ID )
                    #  InternalLF.g:4070:8: otherlv_7= RULE_ID
                    if current == None:
                        current = createModelElement(self.grammarAccess.getVarRefRule())
                    otherlv_7 = match(input, self.RULE_ID, FOLLOW_87)
                    newLeafNode(otherlv_7, self.grammarAccess.getVarRefAccess().getContainerInstantiationCrossReference_2_2_1_0_0())
                    otherlv_8 = match(input, 62, FOLLOW_5)
                    newLeafNode(otherlv_8, self.grammarAccess.getVarRefAccess().getFullStopKeyword_2_2_1_1())
                    #  InternalLF.g:4085:6: ( (otherlv_9= RULE_ID ) )
                    #  InternalLF.g:4086:7: (otherlv_9= RULE_ID )
                    #  InternalLF.g:4086:7: (otherlv_9= RULE_ID )
                    #  InternalLF.g:4087:8: otherlv_9= RULE_ID
                    if current == None:
                        current = createModelElement(self.grammarAccess.getVarRefRule())
                    otherlv_9 = match(input, self.RULE_ID, FOLLOW_47)
                    newLeafNode(otherlv_9, self.grammarAccess.getVarRefAccess().getVariableVariableCrossReference_2_2_1_2_0())
                otherlv_10 = match(input, 29, FOLLOW_2)
                newLeafNode(otherlv_10, self.grammarAccess.getVarRefAccess().getRightParenthesisKeyword_2_3())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleVarRef"
    #  $ANTLR start "entryRuleVarRefOrModeTransition"
    #  InternalLF.g:4109:1: entryRuleVarRefOrModeTransition returns [EObject current=null] : iv_ruleVarRefOrModeTransition= ruleVarRefOrModeTransition EOF ;
    def entryRuleVarRefOrModeTransition(self):
        """ generated source for method entryRuleVarRefOrModeTransition """
        current = None
        iv_ruleVarRefOrModeTransition = None
        try:
            #  InternalLF.g:4109:63: (iv_ruleVarRefOrModeTransition= ruleVarRefOrModeTransition EOF )
            #  InternalLF.g:4110:2: iv_ruleVarRefOrModeTransition= ruleVarRefOrModeTransition EOF
            newCompositeNode(self.grammarAccess.getVarRefOrModeTransitionRule())
            pushFollow(FOLLOW_1)
            iv_ruleVarRefOrModeTransition = ruleVarRefOrModeTransition()
            state._fsp -= 1
            current = iv_ruleVarRefOrModeTransition
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleVarRefOrModeTransition"
    #  $ANTLR start "ruleVarRefOrModeTransition"
    #  InternalLF.g:4116:1: ruleVarRefOrModeTransition returns [EObject current=null] : (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) ) ;
    def ruleVarRefOrModeTransition(self):
        """ generated source for method ruleVarRefOrModeTransition """
        current = None
        otherlv_2 = None
        otherlv_3 = None
        otherlv_4 = None
        this_VarRef_0 = None
        lv_transition_1_0 = None
        enterRule()
        try:
            #  InternalLF.g:4122:2: ( (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) ) )
            #  InternalLF.g:4123:2: (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) )
            #  InternalLF.g:4123:2: (this_VarRef_0= ruleVarRef | ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' ) )
            alt106 = 2
            LA106_0 = input.LA(1)
            if (LA106_0 == self.RULE_ID or LA106_0 == 63):
                alt106 = 1
            elif (LA106_0 == 35 or LA106_0 == 80):
                alt106 = 2
            else:
                nvae = NoViableAltException("", 106, 0, input)
                raise nvae
            if alt106 == 1:
                #  InternalLF.g:4124:3: this_VarRef_0= ruleVarRef
                newCompositeNode(self.grammarAccess.getVarRefOrModeTransitionAccess().getVarRefParserRuleCall_0())
                pushFollow(FOLLOW_2)
                this_VarRef_0 = self.ruleVarRef()
                state._fsp -= 1
                current = this_VarRef_0
                afterParserOrEnumRuleCall()
            elif alt106 == 2:
                #  InternalLF.g:4133:3: ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' )
                #  InternalLF.g:4133:3: ( ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')' )
                #  InternalLF.g:4134:4: ( (lv_transition_1_0= ruleModeTransition ) ) otherlv_2= '(' ( (otherlv_3= RULE_ID ) ) otherlv_4= ')'
                #  InternalLF.g:4134:4: ( (lv_transition_1_0= ruleModeTransition ) )
                #  InternalLF.g:4135:5: (lv_transition_1_0= ruleModeTransition )
                #  InternalLF.g:4135:5: (lv_transition_1_0= ruleModeTransition )
                #  InternalLF.g:4136:6: lv_transition_1_0= ruleModeTransition
                newCompositeNode(self.grammarAccess.getVarRefOrModeTransitionAccess().getTransitionModeTransitionEnumRuleCall_1_0_0())
                pushFollow(FOLLOW_36)
                lv_transition_1_0 = ruleModeTransition()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getVarRefOrModeTransitionRule())
                set(current, "transition", lv_transition_1_0, "org.lflang.LF.ModeTransition")
                afterParserOrEnumRuleCall()
                otherlv_2 = match(input, 28, FOLLOW_5)
                newLeafNode(otherlv_2, self.grammarAccess.getVarRefOrModeTransitionAccess().getLeftParenthesisKeyword_1_1())
                #  InternalLF.g:4157:4: ( (otherlv_3= RULE_ID ) )
                #  InternalLF.g:4158:5: (otherlv_3= RULE_ID )
                #  InternalLF.g:4158:5: (otherlv_3= RULE_ID )
                #  InternalLF.g:4159:6: otherlv_3= RULE_ID
                if current == None:
                    current = createModelElement(self.grammarAccess.getVarRefOrModeTransitionRule())
                otherlv_3 = match(input, self.RULE_ID, FOLLOW_47)
                newLeafNode(otherlv_3, self.grammarAccess.getVarRefOrModeTransitionAccess().getVariableModeCrossReference_1_2_0())
                otherlv_4 = match(input, 29, FOLLOW_2)
                newLeafNode(otherlv_4, self.grammarAccess.getVarRefOrModeTransitionAccess().getRightParenthesisKeyword_1_3())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleVarRefOrModeTransition"
    #  $ANTLR start "entryRuleAssignment"
    #  InternalLF.g:4179:1: entryRuleAssignment returns [EObject current=null] : iv_ruleAssignment= ruleAssignment EOF ;
    def entryRuleAssignment(self):
        """ generated source for method entryRuleAssignment """
        current = None
        iv_ruleAssignment = None
        try:
            #  InternalLF.g:4179:51: (iv_ruleAssignment= ruleAssignment EOF )
            #  InternalLF.g:4180:2: iv_ruleAssignment= ruleAssignment EOF
            newCompositeNode(self.grammarAccess.getAssignmentRule())
            pushFollow(FOLLOW_1)
            iv_ruleAssignment = ruleAssignment()
            state._fsp -= 1
            current = iv_ruleAssignment
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleAssignment"
    #  $ANTLR start "ruleAssignment"
    #  InternalLF.g:4186:1: ruleAssignment returns [EObject current=null] : ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) ) ;
    def ruleAssignment(self):
        """ generated source for method ruleAssignment """
        current = None
        otherlv_0 = None
        lv_equals_1_0 = None
        lv_equals_3_0 = None
        lv_parens_4_0 = None
        otherlv_6 = None
        lv_parens_8_0 = None
        lv_braces_9_0 = None
        otherlv_11 = None
        lv_braces_13_0 = None
        lv_rhs_2_0 = None
        lv_rhs_5_0 = None
        lv_rhs_7_0 = None
        lv_rhs_10_0 = None
        lv_rhs_12_0 = None
        enterRule()
        try:
            #  InternalLF.g:4192:2: ( ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) ) )
            #  InternalLF.g:4193:2: ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) )
            #  InternalLF.g:4193:2: ( ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) ) )
            #  InternalLF.g:4194:3: ( (otherlv_0= RULE_ID ) ) ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) )
            #  InternalLF.g:4194:3: ( (otherlv_0= RULE_ID ) )
            #  InternalLF.g:4195:4: (otherlv_0= RULE_ID )
            #  InternalLF.g:4195:4: (otherlv_0= RULE_ID )
            #  InternalLF.g:4196:5: otherlv_0= RULE_ID
            if current == None:
                current = createModelElement(self.grammarAccess.getAssignmentRule())
            otherlv_0 = match(input, self.RULE_ID, FOLLOW_88)
            newLeafNode(otherlv_0, self.grammarAccess.getAssignmentAccess().getLhsParameterCrossReference_0_0())
            #  InternalLF.g:4207:3: ( ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) ) | ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) ) )
            alt113 = 2
            LA113_0 = input.LA(1)
            if (LA113_0 == 53):
                LA113_1 = input.LA(2)
                if ((LA113_1 >= self.RULE_STRING and LA113_1 <= self.RULE_CHAR_LIT) or LA113_1 == 62 or LA113_1 == 69 or LA113_1 == 71):
                    alt113 = 1
                elif (LA113_1 == 28 or LA113_1 == 32):
                    alt113 = 2
                else:
                    nvae = NoViableAltException("", 113, 1, input)
                    raise nvae
            elif (LA113_0 == 28 or LA113_0 == 32):
                alt113 = 2
            else:
                nvae = NoViableAltException("", 113, 0, input)
                raise nvae
            if alt113 == 1:
                #  InternalLF.g:4208:4: ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) )
                #  InternalLF.g:4208:4: ( ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) ) )
                #  InternalLF.g:4209:5: ( (lv_equals_1_0= '=' ) ) ( (lv_rhs_2_0= ruleExpression ) )
                #  InternalLF.g:4209:5: ( (lv_equals_1_0= '=' ) )
                #  InternalLF.g:4210:6: (lv_equals_1_0= '=' )
                #  InternalLF.g:4210:6: (lv_equals_1_0= '=' )
                #  InternalLF.g:4211:7: lv_equals_1_0= '='
                lv_equals_1_0 = match(input, 53, FOLLOW_32)
                newLeafNode(lv_equals_1_0, self.grammarAccess.getAssignmentAccess().getEqualsEqualsSignKeyword_1_0_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getAssignmentRule())
                setWithLastConsumed(current, "equals", lv_equals_1_0, "=")
                #  InternalLF.g:4223:5: ( (lv_rhs_2_0= ruleExpression ) )
                #  InternalLF.g:4224:6: (lv_rhs_2_0= ruleExpression )
                #  InternalLF.g:4224:6: (lv_rhs_2_0= ruleExpression )
                #  InternalLF.g:4225:7: lv_rhs_2_0= ruleExpression
                newCompositeNode(self.grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_0_1_0())
                pushFollow(FOLLOW_2)
                lv_rhs_2_0 = ruleExpression()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getAssignmentRule())
                add(current, "rhs", lv_rhs_2_0, "org.lflang.LF.Expression")
                afterParserOrEnumRuleCall()
            elif alt113 == 2:
                #  InternalLF.g:4244:4: ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) )
                #  InternalLF.g:4244:4: ( ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) ) )
                #  InternalLF.g:4245:5: ( (lv_equals_3_0= '=' ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )
                #  InternalLF.g:4245:5: ( (lv_equals_3_0= '=' ) )?
                alt107 = 2
                LA107_0 = input.LA(1)
                if (LA107_0 == 53):
                    alt107 = 1
                if alt107 == 1:
                    #  InternalLF.g:4246:6: (lv_equals_3_0= '=' )
                    #  InternalLF.g:4246:6: (lv_equals_3_0= '=' )
                    #  InternalLF.g:4247:7: lv_equals_3_0= '='
                    lv_equals_3_0 = match(input, 53, FOLLOW_89)
                    newLeafNode(lv_equals_3_0, self.grammarAccess.getAssignmentAccess().getEqualsEqualsSignKeyword_1_1_0_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getAssignmentRule())
                    setWithLastConsumed(current, "equals", lv_equals_3_0, "=")
                #  InternalLF.g:4259:5: ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )
                alt112 = 2
                LA112_0 = input.LA(1)
                if (LA112_0 == 28):
                    alt112 = 1
                elif (LA112_0 == 32):
                    alt112 = 2
                else:
                    nvae = NoViableAltException("", 112, 0, input)
                    raise nvae
                if alt112 == 1:
                    #  InternalLF.g:4260:6: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
                    #  InternalLF.g:4260:6: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
                    #  InternalLF.g:4261:7: ( (lv_parens_4_0= '(' ) ) ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) )
                    #  InternalLF.g:4261:7: ( (lv_parens_4_0= '(' ) )
                    #  InternalLF.g:4262:8: (lv_parens_4_0= '(' )
                    #  InternalLF.g:4262:8: (lv_parens_4_0= '(' )
                    #  InternalLF.g:4263:9: lv_parens_4_0= '('
                    lv_parens_4_0 = match(input, 28, FOLLOW_31)
                    newLeafNode(lv_parens_4_0, self.grammarAccess.getAssignmentAccess().getParensLeftParenthesisKeyword_1_1_1_0_0_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getAssignmentRule())
                    addWithLastConsumed(current, "parens", lv_parens_4_0, "(")
                    #  InternalLF.g:4275:7: ( ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )* )?
                    alt109 = 2
                    LA109_0 = input.LA(1)
                    if ((LA109_0 >= self.RULE_STRING and LA109_0 <= self.RULE_CHAR_LIT) or LA109_0 == 62 or LA109_0 == 69 or LA109_0 == 71):
                        alt109 = 1
                    if alt109 == 1:
                        #  InternalLF.g:4276:8: ( (lv_rhs_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )*
                        #  InternalLF.g:4276:8: ( (lv_rhs_5_0= ruleExpression ) )
                        #  InternalLF.g:4277:9: (lv_rhs_5_0= ruleExpression )
                        #  InternalLF.g:4277:9: (lv_rhs_5_0= ruleExpression )
                        #  InternalLF.g:4278:10: lv_rhs_5_0= ruleExpression
                        newCompositeNode(self.grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_0_1_0_0())
                        pushFollow(FOLLOW_18)
                        lv_rhs_5_0 = ruleExpression()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getAssignmentRule())
                        add(current, "rhs", lv_rhs_5_0, "org.lflang.LF.Expression")
                        afterParserOrEnumRuleCall()
                        #  InternalLF.g:4295:8: (otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) ) )*
                        while True:
                            alt108 = 2
                            LA108_0 = input.LA(1)
                            if (LA108_0 == 18):
                                alt108 = 1
                            if alt108 == 1:
                                #  InternalLF.g:4296:9: otherlv_6= ',' ( (lv_rhs_7_0= ruleExpression ) )
                                otherlv_6 = match(input, 18, FOLLOW_32)
                                newLeafNode(otherlv_6, self.grammarAccess.getAssignmentAccess().getCommaKeyword_1_1_1_0_1_1_0())
                                #  InternalLF.g:4300:9: ( (lv_rhs_7_0= ruleExpression ) )
                                #  InternalLF.g:4301:10: (lv_rhs_7_0= ruleExpression )
                                #  InternalLF.g:4301:10: (lv_rhs_7_0= ruleExpression )
                                #  InternalLF.g:4302:11: lv_rhs_7_0= ruleExpression
                                newCompositeNode(self.grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_0_1_1_1_0())
                                pushFollow(FOLLOW_18)
                                lv_rhs_7_0 = ruleExpression()
                                state._fsp -= 1
                                if current == None:
                                    current = createModelElementForParent(self.grammarAccess.getAssignmentRule())
                                add(current, "rhs", lv_rhs_7_0, "org.lflang.LF.Expression")
                                afterParserOrEnumRuleCall()
                            else:
                            if not ((True)):
                                break
                    #  InternalLF.g:4321:7: ( (lv_parens_8_0= ')' ) )
                    #  InternalLF.g:4322:8: (lv_parens_8_0= ')' )
                    #  InternalLF.g:4322:8: (lv_parens_8_0= ')' )
                    #  InternalLF.g:4323:9: lv_parens_8_0= ')'
                    lv_parens_8_0 = match(input, 29, FOLLOW_2)
                    newLeafNode(lv_parens_8_0, self.grammarAccess.getAssignmentAccess().getParensRightParenthesisKeyword_1_1_1_0_2_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getAssignmentRule())
                    addWithLastConsumed(current, "parens", lv_parens_8_0, ")")
                elif alt112 == 2:
                    #  InternalLF.g:4337:6: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
                    #  InternalLF.g:4337:6: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
                    #  InternalLF.g:4338:7: ( (lv_braces_9_0= '{' ) ) ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) )
                    #  InternalLF.g:4338:7: ( (lv_braces_9_0= '{' ) )
                    #  InternalLF.g:4339:8: (lv_braces_9_0= '{' )
                    #  InternalLF.g:4339:8: (lv_braces_9_0= '{' )
                    #  InternalLF.g:4340:9: lv_braces_9_0= '{'
                    lv_braces_9_0 = match(input, 32, FOLLOW_33)
                    newLeafNode(lv_braces_9_0, self.grammarAccess.getAssignmentAccess().getBracesLeftCurlyBracketKeyword_1_1_1_1_0_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getAssignmentRule())
                    addWithLastConsumed(current, "braces", lv_braces_9_0, "{")
                    #  InternalLF.g:4352:7: ( ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )* )?
                    alt111 = 2
                    LA111_0 = input.LA(1)
                    if ((LA111_0 >= self.RULE_STRING and LA111_0 <= self.RULE_CHAR_LIT) or LA111_0 == 62 or LA111_0 == 69 or LA111_0 == 71):
                        alt111 = 1
                    if alt111 == 1:
                        #  InternalLF.g:4353:8: ( (lv_rhs_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )*
                        #  InternalLF.g:4353:8: ( (lv_rhs_10_0= ruleExpression ) )
                        #  InternalLF.g:4354:9: (lv_rhs_10_0= ruleExpression )
                        #  InternalLF.g:4354:9: (lv_rhs_10_0= ruleExpression )
                        #  InternalLF.g:4355:10: lv_rhs_10_0= ruleExpression
                        newCompositeNode(self.grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_1_1_0_0())
                        pushFollow(FOLLOW_34)
                        lv_rhs_10_0 = ruleExpression()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getAssignmentRule())
                        add(current, "rhs", lv_rhs_10_0, "org.lflang.LF.Expression")
                        afterParserOrEnumRuleCall()
                        #  InternalLF.g:4372:8: (otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) ) )*
                        while True:
                            alt110 = 2
                            LA110_0 = input.LA(1)
                            if (LA110_0 == 18):
                                alt110 = 1
                            if alt110 == 1:
                                #  InternalLF.g:4373:9: otherlv_11= ',' ( (lv_rhs_12_0= ruleExpression ) )
                                otherlv_11 = match(input, 18, FOLLOW_32)
                                newLeafNode(otherlv_11, self.grammarAccess.getAssignmentAccess().getCommaKeyword_1_1_1_1_1_1_0())
                                #  InternalLF.g:4377:9: ( (lv_rhs_12_0= ruleExpression ) )
                                #  InternalLF.g:4378:10: (lv_rhs_12_0= ruleExpression )
                                #  InternalLF.g:4378:10: (lv_rhs_12_0= ruleExpression )
                                #  InternalLF.g:4379:11: lv_rhs_12_0= ruleExpression
                                newCompositeNode(self.grammarAccess.getAssignmentAccess().getRhsExpressionParserRuleCall_1_1_1_1_1_1_1_0())
                                pushFollow(FOLLOW_34)
                                lv_rhs_12_0 = ruleExpression()
                                state._fsp -= 1
                                if current == None:
                                    current = createModelElementForParent(self.grammarAccess.getAssignmentRule())
                                add(current, "rhs", lv_rhs_12_0, "org.lflang.LF.Expression")
                                afterParserOrEnumRuleCall()
                            else:
                            if not ((True)):
                                break
                    #  InternalLF.g:4398:7: ( (lv_braces_13_0= '}' ) )
                    #  InternalLF.g:4399:8: (lv_braces_13_0= '}' )
                    #  InternalLF.g:4399:8: (lv_braces_13_0= '}' )
                    #  InternalLF.g:4400:9: lv_braces_13_0= '}'
                    lv_braces_13_0 = match(input, 33, FOLLOW_2)
                    newLeafNode(lv_braces_13_0, self.grammarAccess.getAssignmentAccess().getBracesRightCurlyBracketKeyword_1_1_1_1_2_0())
                    if current == None:
                        current = createModelElement(self.grammarAccess.getAssignmentRule())
                    addWithLastConsumed(current, "braces", lv_braces_13_0, "}")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleAssignment"
    #  $ANTLR start "entryRuleParameter"
    #  InternalLF.g:4420:1: entryRuleParameter returns [EObject current=null] : iv_ruleParameter= ruleParameter EOF ;
    def entryRuleParameter(self):
        """ generated source for method entryRuleParameter """
        current = None
        iv_ruleParameter = None
        try:
            #  InternalLF.g:4420:50: (iv_ruleParameter= ruleParameter EOF )
            #  InternalLF.g:4421:2: iv_ruleParameter= ruleParameter EOF
            newCompositeNode(self.grammarAccess.getParameterRule())
            pushFollow(FOLLOW_1)
            iv_ruleParameter = ruleParameter()
            state._fsp -= 1
            current = iv_ruleParameter
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleParameter"
    #  $ANTLR start "ruleParameter"
    #  InternalLF.g:4427:1: ruleParameter returns [EObject current=null] : ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? ) ;
    def ruleParameter(self):
        """ generated source for method ruleParameter """
        current = None
        lv_name_1_0 = None
        otherlv_2 = None
        lv_parens_4_0 = None
        otherlv_6 = None
        lv_parens_8_0 = None
        lv_braces_9_0 = None
        otherlv_11 = None
        lv_braces_13_0 = None
        lv_attributes_0_0 = None
        lv_type_3_0 = None
        lv_init_5_0 = None
        lv_init_7_0 = None
        lv_init_10_0 = None
        lv_init_12_0 = None
        enterRule()
        try:
            #  InternalLF.g:4433:2: ( ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? ) )
            #  InternalLF.g:4434:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? )
            #  InternalLF.g:4434:2: ( ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )? )
            #  InternalLF.g:4435:3: ( (lv_attributes_0_0= ruleAttribute ) )* ( (lv_name_1_0= RULE_ID ) ) (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )? ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )?
            #  InternalLF.g:4435:3: ( (lv_attributes_0_0= ruleAttribute ) )*
            while True:
                alt114 = 2
                LA114_0 = input.LA(1)
                if (LA114_0 == 59):
                    alt114 = 1
                if alt114 == 1:
                    #  InternalLF.g:4436:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:4436:4: (lv_attributes_0_0= ruleAttribute )
                    #  InternalLF.g:4437:5: lv_attributes_0_0= ruleAttribute
                    newCompositeNode(self.grammarAccess.getParameterAccess().getAttributesAttributeParserRuleCall_0_0())
                    pushFollow(FOLLOW_17)
                    lv_attributes_0_0 = self.ruleAttribute()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getParameterRule())
                    add(current, "attributes", lv_attributes_0_0, "org.lflang.LF.Attribute")
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            #  InternalLF.g:4454:3: ( (lv_name_1_0= RULE_ID ) )
            #  InternalLF.g:4455:4: (lv_name_1_0= RULE_ID )
            #  InternalLF.g:4455:4: (lv_name_1_0= RULE_ID )
            #  InternalLF.g:4456:5: lv_name_1_0= RULE_ID
            lv_name_1_0 = match(input, self.RULE_ID, FOLLOW_90)
            newLeafNode(lv_name_1_0, self.grammarAccess.getParameterAccess().getNameIDTerminalRuleCall_1_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getParameterRule())
            setWithLastConsumed(current, "name", lv_name_1_0, "org.lflang.LF.ID")
            #  InternalLF.g:4472:3: (otherlv_2= ':' ( (lv_type_3_0= ruleType ) ) )?
            alt115 = 2
            LA115_0 = input.LA(1)
            if (LA115_0 == 37):
                alt115 = 1
            if alt115 == 1:
                #  InternalLF.g:4473:4: otherlv_2= ':' ( (lv_type_3_0= ruleType ) )
                otherlv_2 = match(input, 37, FOLLOW_29)
                newLeafNode(otherlv_2, self.grammarAccess.getParameterAccess().getColonKeyword_2_0())
                #  InternalLF.g:4477:4: ( (lv_type_3_0= ruleType ) )
                #  InternalLF.g:4478:5: (lv_type_3_0= ruleType )
                #  InternalLF.g:4478:5: (lv_type_3_0= ruleType )
                #  InternalLF.g:4479:6: lv_type_3_0= ruleType
                newCompositeNode(self.grammarAccess.getParameterAccess().getTypeTypeParserRuleCall_2_1_0())
                pushFollow(FOLLOW_91)
                lv_type_3_0 = ruleType()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getParameterRule())
                set(current, "type", lv_type_3_0, "org.lflang.LF.Type")
                afterParserOrEnumRuleCall()
            #  InternalLF.g:4497:3: ( ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) ) | ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) ) )?
            alt120 = 3
            LA120_0 = input.LA(1)
            if (LA120_0 == 28):
                alt120 = 1
            elif (LA120_0 == 32):
                alt120 = 2
            if alt120 == 1:
                #  InternalLF.g:4498:4: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
                #  InternalLF.g:4498:4: ( ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) ) )
                #  InternalLF.g:4499:5: ( (lv_parens_4_0= '(' ) ) ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )? ( (lv_parens_8_0= ')' ) )
                #  InternalLF.g:4499:5: ( (lv_parens_4_0= '(' ) )
                #  InternalLF.g:4500:6: (lv_parens_4_0= '(' )
                #  InternalLF.g:4500:6: (lv_parens_4_0= '(' )
                #  InternalLF.g:4501:7: lv_parens_4_0= '('
                lv_parens_4_0 = match(input, 28, FOLLOW_31)
                newLeafNode(lv_parens_4_0, self.grammarAccess.getParameterAccess().getParensLeftParenthesisKeyword_3_0_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getParameterRule())
                addWithLastConsumed(current, "parens", lv_parens_4_0, "(")
                #  InternalLF.g:4513:5: ( ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )* )?
                alt117 = 2
                LA117_0 = input.LA(1)
                if ((LA117_0 >= self.RULE_STRING and LA117_0 <= self.RULE_CHAR_LIT) or LA117_0 == 62 or LA117_0 == 69 or LA117_0 == 71):
                    alt117 = 1
                if alt117 == 1:
                    #  InternalLF.g:4514:6: ( (lv_init_5_0= ruleExpression ) ) (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )*
                    #  InternalLF.g:4514:6: ( (lv_init_5_0= ruleExpression ) )
                    #  InternalLF.g:4515:7: (lv_init_5_0= ruleExpression )
                    #  InternalLF.g:4515:7: (lv_init_5_0= ruleExpression )
                    #  InternalLF.g:4516:8: lv_init_5_0= ruleExpression
                    newCompositeNode(self.grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_0_1_0_0())
                    pushFollow(FOLLOW_18)
                    lv_init_5_0 = ruleExpression()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getParameterRule())
                    add(current, "init", lv_init_5_0, "org.lflang.LF.Expression")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:4533:6: (otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) ) )*
                    while True:
                        alt116 = 2
                        LA116_0 = input.LA(1)
                        if (LA116_0 == 18):
                            alt116 = 1
                        if alt116 == 1:
                            #  InternalLF.g:4534:7: otherlv_6= ',' ( (lv_init_7_0= ruleExpression ) )
                            otherlv_6 = match(input, 18, FOLLOW_32)
                            newLeafNode(otherlv_6, self.grammarAccess.getParameterAccess().getCommaKeyword_3_0_1_1_0())
                            #  InternalLF.g:4538:7: ( (lv_init_7_0= ruleExpression ) )
                            #  InternalLF.g:4539:8: (lv_init_7_0= ruleExpression )
                            #  InternalLF.g:4539:8: (lv_init_7_0= ruleExpression )
                            #  InternalLF.g:4540:9: lv_init_7_0= ruleExpression
                            newCompositeNode(self.grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_0_1_1_1_0())
                            pushFollow(FOLLOW_18)
                            lv_init_7_0 = ruleExpression()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getParameterRule())
                            add(current, "init", lv_init_7_0, "org.lflang.LF.Expression")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                #  InternalLF.g:4559:5: ( (lv_parens_8_0= ')' ) )
                #  InternalLF.g:4560:6: (lv_parens_8_0= ')' )
                #  InternalLF.g:4560:6: (lv_parens_8_0= ')' )
                #  InternalLF.g:4561:7: lv_parens_8_0= ')'
                lv_parens_8_0 = match(input, 29, FOLLOW_2)
                newLeafNode(lv_parens_8_0, self.grammarAccess.getParameterAccess().getParensRightParenthesisKeyword_3_0_2_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getParameterRule())
                addWithLastConsumed(current, "parens", lv_parens_8_0, ")")
            elif alt120 == 2:
                #  InternalLF.g:4575:4: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
                #  InternalLF.g:4575:4: ( ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) ) )
                #  InternalLF.g:4576:5: ( (lv_braces_9_0= '{' ) ) ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )? ( (lv_braces_13_0= '}' ) )
                #  InternalLF.g:4576:5: ( (lv_braces_9_0= '{' ) )
                #  InternalLF.g:4577:6: (lv_braces_9_0= '{' )
                #  InternalLF.g:4577:6: (lv_braces_9_0= '{' )
                #  InternalLF.g:4578:7: lv_braces_9_0= '{'
                lv_braces_9_0 = match(input, 32, FOLLOW_33)
                newLeafNode(lv_braces_9_0, self.grammarAccess.getParameterAccess().getBracesLeftCurlyBracketKeyword_3_1_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getParameterRule())
                addWithLastConsumed(current, "braces", lv_braces_9_0, "{")
                #  InternalLF.g:4590:5: ( ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )* )?
                alt119 = 2
                LA119_0 = input.LA(1)
                if ((LA119_0 >= self.RULE_STRING and LA119_0 <= self.RULE_CHAR_LIT) or LA119_0 == 62 or LA119_0 == 69 or LA119_0 == 71):
                    alt119 = 1
                if alt119 == 1:
                    #  InternalLF.g:4591:6: ( (lv_init_10_0= ruleExpression ) ) (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )*
                    #  InternalLF.g:4591:6: ( (lv_init_10_0= ruleExpression ) )
                    #  InternalLF.g:4592:7: (lv_init_10_0= ruleExpression )
                    #  InternalLF.g:4592:7: (lv_init_10_0= ruleExpression )
                    #  InternalLF.g:4593:8: lv_init_10_0= ruleExpression
                    newCompositeNode(self.grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_1_1_0_0())
                    pushFollow(FOLLOW_34)
                    lv_init_10_0 = ruleExpression()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getParameterRule())
                    add(current, "init", lv_init_10_0, "org.lflang.LF.Expression")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:4610:6: (otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) ) )*
                    while True:
                        alt118 = 2
                        LA118_0 = input.LA(1)
                        if (LA118_0 == 18):
                            alt118 = 1
                        if alt118 == 1:
                            #  InternalLF.g:4611:7: otherlv_11= ',' ( (lv_init_12_0= ruleExpression ) )
                            otherlv_11 = match(input, 18, FOLLOW_32)
                            newLeafNode(otherlv_11, self.grammarAccess.getParameterAccess().getCommaKeyword_3_1_1_1_0())
                            #  InternalLF.g:4615:7: ( (lv_init_12_0= ruleExpression ) )
                            #  InternalLF.g:4616:8: (lv_init_12_0= ruleExpression )
                            #  InternalLF.g:4616:8: (lv_init_12_0= ruleExpression )
                            #  InternalLF.g:4617:9: lv_init_12_0= ruleExpression
                            newCompositeNode(self.grammarAccess.getParameterAccess().getInitExpressionParserRuleCall_3_1_1_1_1_0())
                            pushFollow(FOLLOW_34)
                            lv_init_12_0 = ruleExpression()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getParameterRule())
                            add(current, "init", lv_init_12_0, "org.lflang.LF.Expression")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                #  InternalLF.g:4636:5: ( (lv_braces_13_0= '}' ) )
                #  InternalLF.g:4637:6: (lv_braces_13_0= '}' )
                #  InternalLF.g:4637:6: (lv_braces_13_0= '}' )
                #  InternalLF.g:4638:7: lv_braces_13_0= '}'
                lv_braces_13_0 = match(input, 33, FOLLOW_2)
                newLeafNode(lv_braces_13_0, self.grammarAccess.getParameterAccess().getBracesRightCurlyBracketKeyword_3_1_2_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getParameterRule())
                addWithLastConsumed(current, "braces", lv_braces_13_0, "}")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleParameter"
    #  $ANTLR start "entryRuleExpression"
    #  InternalLF.g:4656:1: entryRuleExpression returns [EObject current=null] : iv_ruleExpression= ruleExpression EOF ;
    def entryRuleExpression(self):
        """ generated source for method entryRuleExpression """
        current = None
        iv_ruleExpression = None
        try:
            #  InternalLF.g:4656:51: (iv_ruleExpression= ruleExpression EOF )
            #  InternalLF.g:4657:2: iv_ruleExpression= ruleExpression EOF
            newCompositeNode(self.grammarAccess.getExpressionRule())
            pushFollow(FOLLOW_1)
            iv_ruleExpression = ruleExpression()
            state._fsp -= 1
            current = iv_ruleExpression
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleExpression"
    #  $ANTLR start "ruleExpression"
    #  InternalLF.g:4663:1: ruleExpression returns [EObject current=null] : ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) | this_Time_2= ruleTime | this_ParameterReference_3= ruleParameterReference | this_Code_4= ruleCode ) ;
    def ruleExpression(self):
        """ generated source for method ruleExpression """
        current = None
        lv_literal_1_0 = None
        this_Time_2 = None
        this_ParameterReference_3 = None
        this_Code_4 = None
        enterRule()
        try:
            #  InternalLF.g:4669:2: ( ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) | this_Time_2= ruleTime | this_ParameterReference_3= ruleParameterReference | this_Code_4= ruleCode ) )
            #  InternalLF.g:4670:2: ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) | this_Time_2= ruleTime | this_ParameterReference_3= ruleParameterReference | this_Code_4= ruleCode )
            #  InternalLF.g:4670:2: ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) | this_Time_2= ruleTime | this_ParameterReference_3= ruleParameterReference | this_Code_4= ruleCode )
            alt121 = 4
            alt121 = dfa121.predict(input)
            if alt121 == 1:
                #  InternalLF.g:4671:3: ( () ( (lv_literal_1_0= ruleLiteral ) ) )
                #  InternalLF.g:4671:3: ( () ( (lv_literal_1_0= ruleLiteral ) ) )
                #  InternalLF.g:4672:4: () ( (lv_literal_1_0= ruleLiteral ) )
                #  InternalLF.g:4672:4: ()
                #  InternalLF.g:4673:5: 
                current = forceCreateModelElement(self.grammarAccess.getExpressionAccess().getLiteralAction_0_0(), current)
                #  InternalLF.g:4679:4: ( (lv_literal_1_0= ruleLiteral ) )
                #  InternalLF.g:4680:5: (lv_literal_1_0= ruleLiteral )
                #  InternalLF.g:4680:5: (lv_literal_1_0= ruleLiteral )
                #  InternalLF.g:4681:6: lv_literal_1_0= ruleLiteral
                newCompositeNode(self.grammarAccess.getExpressionAccess().getLiteralLiteralParserRuleCall_0_1_0())
                pushFollow(FOLLOW_2)
                lv_literal_1_0 = ruleLiteral()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getExpressionRule())
                set(current, "literal", lv_literal_1_0, "org.lflang.LF.Literal")
                afterParserOrEnumRuleCall()
            elif alt121 == 2:
                #  InternalLF.g:4700:3: this_Time_2= ruleTime
                newCompositeNode(self.grammarAccess.getExpressionAccess().getTimeParserRuleCall_1())
                pushFollow(FOLLOW_2)
                this_Time_2 = ruleTime()
                state._fsp -= 1
                current = this_Time_2
                afterParserOrEnumRuleCall()
            elif alt121 == 3:
                #  InternalLF.g:4709:3: this_ParameterReference_3= ruleParameterReference
                newCompositeNode(self.grammarAccess.getExpressionAccess().getParameterReferenceParserRuleCall_2())
                pushFollow(FOLLOW_2)
                this_ParameterReference_3 = ruleParameterReference()
                state._fsp -= 1
                current = this_ParameterReference_3
                afterParserOrEnumRuleCall()
            elif alt121 == 4:
                #  InternalLF.g:4718:3: this_Code_4= ruleCode
                newCompositeNode(self.grammarAccess.getExpressionAccess().getCodeParserRuleCall_3())
                pushFollow(FOLLOW_2)
                this_Code_4 = ruleCode()
                state._fsp -= 1
                current = this_Code_4
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleExpression"
    #  $ANTLR start "entryRuleParameterReference"
    #  InternalLF.g:4730:1: entryRuleParameterReference returns [EObject current=null] : iv_ruleParameterReference= ruleParameterReference EOF ;
    def entryRuleParameterReference(self):
        """ generated source for method entryRuleParameterReference """
        current = None
        iv_ruleParameterReference = None
        try:
            #  InternalLF.g:4730:59: (iv_ruleParameterReference= ruleParameterReference EOF )
            #  InternalLF.g:4731:2: iv_ruleParameterReference= ruleParameterReference EOF
            newCompositeNode(self.grammarAccess.getParameterReferenceRule())
            pushFollow(FOLLOW_1)
            iv_ruleParameterReference = ruleParameterReference()
            state._fsp -= 1
            current = iv_ruleParameterReference
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleParameterReference"
    #  $ANTLR start "ruleParameterReference"
    #  InternalLF.g:4737:1: ruleParameterReference returns [EObject current=null] : ( (otherlv_0= RULE_ID ) ) ;
    def ruleParameterReference(self):
        """ generated source for method ruleParameterReference """
        current = None
        otherlv_0 = None
        enterRule()
        try:
            #  InternalLF.g:4743:2: ( ( (otherlv_0= RULE_ID ) ) )
            #  InternalLF.g:4744:2: ( (otherlv_0= RULE_ID ) )
            #  InternalLF.g:4744:2: ( (otherlv_0= RULE_ID ) )
            #  InternalLF.g:4745:3: (otherlv_0= RULE_ID )
            #  InternalLF.g:4745:3: (otherlv_0= RULE_ID )
            #  InternalLF.g:4746:4: otherlv_0= RULE_ID
            if current == None:
                current = createModelElement(self.grammarAccess.getParameterReferenceRule())
            otherlv_0 = match(input, self.RULE_ID, FOLLOW_2)
            newLeafNode(otherlv_0, self.grammarAccess.getParameterReferenceAccess().getParameterParameterCrossReference_0())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleParameterReference"
    #  $ANTLR start "entryRuleTime"
    #  InternalLF.g:4760:1: entryRuleTime returns [EObject current=null] : iv_ruleTime= ruleTime EOF ;
    def entryRuleTime(self):
        """ generated source for method entryRuleTime """
        current = None
        iv_ruleTime = None
        try:
            #  InternalLF.g:4760:45: (iv_ruleTime= ruleTime EOF )
            #  InternalLF.g:4761:2: iv_ruleTime= ruleTime EOF
            newCompositeNode(self.grammarAccess.getTimeRule())
            pushFollow(FOLLOW_1)
            iv_ruleTime = ruleTime()
            state._fsp -= 1
            current = iv_ruleTime
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTime"
    #  $ANTLR start "ruleTime"
    #  InternalLF.g:4767:1: ruleTime returns [EObject current=null] : ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) ) ;
    def ruleTime(self):
        """ generated source for method ruleTime """
        current = None
        lv_interval_0_0 = None
        lv_unit_1_0 = None
        enterRule()
        try:
            #  InternalLF.g:4773:2: ( ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) ) )
            #  InternalLF.g:4774:2: ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) )
            #  InternalLF.g:4774:2: ( ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) ) )
            #  InternalLF.g:4775:3: ( (lv_interval_0_0= RULE_INT ) ) ( (lv_unit_1_0= ruleTimeUnit ) )
            #  InternalLF.g:4775:3: ( (lv_interval_0_0= RULE_INT ) )
            #  InternalLF.g:4776:4: (lv_interval_0_0= RULE_INT )
            #  InternalLF.g:4776:4: (lv_interval_0_0= RULE_INT )
            #  InternalLF.g:4777:5: lv_interval_0_0= RULE_INT
            lv_interval_0_0 = match(input, self.RULE_INT, FOLLOW_5)
            newLeafNode(lv_interval_0_0, self.grammarAccess.getTimeAccess().getIntervalINTTerminalRuleCall_0_0())
            if current == None:
                current = createModelElement(self.grammarAccess.getTimeRule())
            setWithLastConsumed(current, "interval", lv_interval_0_0, "org.lflang.LF.INT")
            #  InternalLF.g:4793:3: ( (lv_unit_1_0= ruleTimeUnit ) )
            #  InternalLF.g:4794:4: (lv_unit_1_0= ruleTimeUnit )
            #  InternalLF.g:4794:4: (lv_unit_1_0= ruleTimeUnit )
            #  InternalLF.g:4795:5: lv_unit_1_0= ruleTimeUnit
            newCompositeNode(self.grammarAccess.getTimeAccess().getUnitTimeUnitParserRuleCall_1_0())
            pushFollow(FOLLOW_2)
            lv_unit_1_0 = ruleTimeUnit()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getTimeRule())
            set(current, "unit", lv_unit_1_0, "org.lflang.LF.TimeUnit")
            afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTime"
    #  $ANTLR start "entryRulePort"
    #  InternalLF.g:4816:1: entryRulePort returns [EObject current=null] : iv_rulePort= rulePort EOF ;
    def entryRulePort(self):
        """ generated source for method entryRulePort """
        current = None
        iv_rulePort = None
        try:
            #  InternalLF.g:4816:45: (iv_rulePort= rulePort EOF )
            #  InternalLF.g:4817:2: iv_rulePort= rulePort EOF
            newCompositeNode(self.grammarAccess.getPortRule())
            pushFollow(FOLLOW_1)
            iv_rulePort = rulePort()
            state._fsp -= 1
            current = iv_rulePort
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRulePort"
    #  $ANTLR start "rulePort"
    #  InternalLF.g:4823:1: rulePort returns [EObject current=null] : (this_Input_0= ruleInput | this_Output_1= ruleOutput ) ;
    def rulePort(self):
        """ generated source for method rulePort """
        current = None
        this_Input_0 = None
        this_Output_1 = None
        enterRule()
        try:
            #  InternalLF.g:4829:2: ( (this_Input_0= ruleInput | this_Output_1= ruleOutput ) )
            #  InternalLF.g:4830:2: (this_Input_0= ruleInput | this_Output_1= ruleOutput )
            #  InternalLF.g:4830:2: (this_Input_0= ruleInput | this_Output_1= ruleOutput )
            alt122 = 2
            alt122 = dfa122.predict(input)
            if alt122 == 1:
                #  InternalLF.g:4831:3: this_Input_0= ruleInput
                newCompositeNode(self.grammarAccess.getPortAccess().getInputParserRuleCall_0())
                pushFollow(FOLLOW_2)
                this_Input_0 = self.ruleInput()
                state._fsp -= 1
                current = this_Input_0
                afterParserOrEnumRuleCall()
            elif alt122 == 2:
                #  InternalLF.g:4840:3: this_Output_1= ruleOutput
                newCompositeNode(self.grammarAccess.getPortAccess().getOutputParserRuleCall_1())
                pushFollow(FOLLOW_2)
                this_Output_1 = self.ruleOutput()
                state._fsp -= 1
                current = this_Output_1
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "rulePort"
    #  $ANTLR start "entryRuleType"
    #  InternalLF.g:4852:1: entryRuleType returns [EObject current=null] : iv_ruleType= ruleType EOF ;
    def entryRuleType(self):
        """ generated source for method entryRuleType """
        current = None
        iv_ruleType = None
        try:
            #  InternalLF.g:4852:45: (iv_ruleType= ruleType EOF )
            #  InternalLF.g:4853:2: iv_ruleType= ruleType EOF
            newCompositeNode(self.grammarAccess.getTypeRule())
            pushFollow(FOLLOW_1)
            iv_ruleType = ruleType()
            state._fsp -= 1
            current = iv_ruleType
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleType"
    #  $ANTLR start "ruleType"
    #  InternalLF.g:4859:1: ruleType returns [EObject current=null] : ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) ) ;
    def ruleType(self):
        """ generated source for method ruleType """
        current = None
        lv_time_0_0 = None
        otherlv_3 = None
        otherlv_5 = None
        otherlv_7 = None
        lv_stars_8_0 = None
        lv_arraySpec_1_0 = None
        lv_id_2_0 = None
        lv_typeParms_4_0 = None
        lv_typeParms_6_0 = None
        lv_arraySpec_9_0 = None
        lv_code_10_0 = None
        enterRule()
        try:
            #  InternalLF.g:4865:2: ( ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) ) )
            #  InternalLF.g:4866:2: ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) )
            #  InternalLF.g:4866:2: ( ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? ) | ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? ) | ( (lv_code_10_0= ruleCode ) ) )
            alt128 = 3
            if input.LA(1) == 64:
                alt128 = 1
            elif input.LA(1) == self.RULE_ID:
                alt128 = 2
            elif input.LA(1) == 71:
                alt128 = 3
            else:
                nvae = NoViableAltException("", 128, 0, input)
                raise nvae
            if alt128 == 1:
                #  InternalLF.g:4867:3: ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? )
                #  InternalLF.g:4867:3: ( ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )? )
                #  InternalLF.g:4868:4: ( (lv_time_0_0= 'time' ) ) ( (lv_arraySpec_1_0= ruleArraySpec ) )?
                #  InternalLF.g:4868:4: ( (lv_time_0_0= 'time' ) )
                #  InternalLF.g:4869:5: (lv_time_0_0= 'time' )
                #  InternalLF.g:4869:5: (lv_time_0_0= 'time' )
                #  InternalLF.g:4870:6: lv_time_0_0= 'time'
                lv_time_0_0 = match(input, 64, FOLLOW_92)
                newLeafNode(lv_time_0_0, self.grammarAccess.getTypeAccess().getTimeTimeKeyword_0_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getTypeRule())
                setWithLastConsumed(current, "time", lv_time_0_0 != None, "time")
                #  InternalLF.g:4882:4: ( (lv_arraySpec_1_0= ruleArraySpec ) )?
                alt123 = 2
                LA123_0 = input.LA(1)
                if (LA123_0 == 60):
                    alt123 = 1
                if alt123 == 1:
                    #  InternalLF.g:4883:5: (lv_arraySpec_1_0= ruleArraySpec )
                    #  InternalLF.g:4883:5: (lv_arraySpec_1_0= ruleArraySpec )
                    #  InternalLF.g:4884:6: lv_arraySpec_1_0= ruleArraySpec
                    newCompositeNode(self.grammarAccess.getTypeAccess().getArraySpecArraySpecParserRuleCall_0_1_0())
                    pushFollow(FOLLOW_2)
                    lv_arraySpec_1_0 = ruleArraySpec()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getTypeRule())
                    set(current, "arraySpec", lv_arraySpec_1_0, "org.lflang.LF.ArraySpec")
                    afterParserOrEnumRuleCall()
            elif alt128 == 2:
                #  InternalLF.g:4903:3: ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? )
                #  InternalLF.g:4903:3: ( ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )? )
                #  InternalLF.g:4904:4: ( (lv_id_2_0= ruleDottedName ) ) (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )? ( (lv_stars_8_0= '*' ) )* ( (lv_arraySpec_9_0= ruleArraySpec ) )?
                #  InternalLF.g:4904:4: ( (lv_id_2_0= ruleDottedName ) )
                #  InternalLF.g:4905:5: (lv_id_2_0= ruleDottedName )
                #  InternalLF.g:4905:5: (lv_id_2_0= ruleDottedName )
                #  InternalLF.g:4906:6: lv_id_2_0= ruleDottedName
                newCompositeNode(self.grammarAccess.getTypeAccess().getIdDottedNameParserRuleCall_1_0_0())
                pushFollow(FOLLOW_93)
                lv_id_2_0 = ruleDottedName()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getTypeRule())
                set(current, "id", lv_id_2_0, "org.lflang.LF.DottedName")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:4923:4: (otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>' )?
                alt125 = 2
                LA125_0 = input.LA(1)
                if (LA125_0 == 26):
                    alt125 = 1
                if alt125 == 1:
                    #  InternalLF.g:4924:5: otherlv_3= '<' ( (lv_typeParms_4_0= ruleType ) ) (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )* otherlv_7= '>'
                    otherlv_3 = match(input, 26, FOLLOW_29)
                    newLeafNode(otherlv_3, self.grammarAccess.getTypeAccess().getLessThanSignKeyword_1_1_0())
                    #  InternalLF.g:4928:5: ( (lv_typeParms_4_0= ruleType ) )
                    #  InternalLF.g:4929:6: (lv_typeParms_4_0= ruleType )
                    #  InternalLF.g:4929:6: (lv_typeParms_4_0= ruleType )
                    #  InternalLF.g:4930:7: lv_typeParms_4_0= ruleType
                    newCompositeNode(self.grammarAccess.getTypeAccess().getTypeParmsTypeParserRuleCall_1_1_1_0())
                    pushFollow(FOLLOW_15)
                    lv_typeParms_4_0 = self.ruleType()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getTypeRule())
                    add(current, "typeParms", lv_typeParms_4_0, "org.lflang.LF.Type")
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:4947:5: (otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) ) )*
                    while True:
                        alt124 = 2
                        LA124_0 = input.LA(1)
                        if (LA124_0 == 18):
                            alt124 = 1
                        if alt124 == 1:
                            #  InternalLF.g:4948:6: otherlv_5= ',' ( (lv_typeParms_6_0= ruleType ) )
                            otherlv_5 = match(input, 18, FOLLOW_29)
                            newLeafNode(otherlv_5, self.grammarAccess.getTypeAccess().getCommaKeyword_1_1_2_0())
                            #  InternalLF.g:4952:6: ( (lv_typeParms_6_0= ruleType ) )
                            #  InternalLF.g:4953:7: (lv_typeParms_6_0= ruleType )
                            #  InternalLF.g:4953:7: (lv_typeParms_6_0= ruleType )
                            #  InternalLF.g:4954:8: lv_typeParms_6_0= ruleType
                            newCompositeNode(self.grammarAccess.getTypeAccess().getTypeParmsTypeParserRuleCall_1_1_2_1_0())
                            pushFollow(FOLLOW_15)
                            lv_typeParms_6_0 = self.ruleType()
                            state._fsp -= 1
                            if current == None:
                                current = createModelElementForParent(self.grammarAccess.getTypeRule())
                            add(current, "typeParms", lv_typeParms_6_0, "org.lflang.LF.Type")
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                    otherlv_7 = match(input, 27, FOLLOW_94)
                    newLeafNode(otherlv_7, self.grammarAccess.getTypeAccess().getGreaterThanSignKeyword_1_1_3())
                #  InternalLF.g:4977:4: ( (lv_stars_8_0= '*' ) )*
                while True:
                    alt126 = 2
                    LA126_0 = input.LA(1)
                    if (LA126_0 == 65):
                        alt126 = 1
                    if alt126 == 1:
                        #  InternalLF.g:4978:5: (lv_stars_8_0= '*' )
                        #  InternalLF.g:4978:5: (lv_stars_8_0= '*' )
                        #  InternalLF.g:4979:6: lv_stars_8_0= '*'
                        lv_stars_8_0 = match(input, 65, FOLLOW_94)
                        newLeafNode(lv_stars_8_0, self.grammarAccess.getTypeAccess().getStarsAsteriskKeyword_1_2_0())
                        if current == None:
                            current = createModelElement(self.grammarAccess.getTypeRule())
                        addWithLastConsumed(current, "stars", lv_stars_8_0, "*")
                    else:
                    if not ((True)):
                        break
                #  InternalLF.g:4991:4: ( (lv_arraySpec_9_0= ruleArraySpec ) )?
                alt127 = 2
                LA127_0 = input.LA(1)
                if (LA127_0 == 60):
                    alt127 = 1
                if alt127 == 1:
                    #  InternalLF.g:4992:5: (lv_arraySpec_9_0= ruleArraySpec )
                    #  InternalLF.g:4992:5: (lv_arraySpec_9_0= ruleArraySpec )
                    #  InternalLF.g:4993:6: lv_arraySpec_9_0= ruleArraySpec
                    newCompositeNode(self.grammarAccess.getTypeAccess().getArraySpecArraySpecParserRuleCall_1_3_0())
                    pushFollow(FOLLOW_2)
                    lv_arraySpec_9_0 = ruleArraySpec()
                    state._fsp -= 1
                    if current == None:
                        current = createModelElementForParent(self.grammarAccess.getTypeRule())
                    set(current, "arraySpec", lv_arraySpec_9_0, "org.lflang.LF.ArraySpec")
                    afterParserOrEnumRuleCall()
            elif alt128 == 3:
                #  InternalLF.g:5012:3: ( (lv_code_10_0= ruleCode ) )
                #  InternalLF.g:5012:3: ( (lv_code_10_0= ruleCode ) )
                #  InternalLF.g:5013:4: (lv_code_10_0= ruleCode )
                #  InternalLF.g:5013:4: (lv_code_10_0= ruleCode )
                #  InternalLF.g:5014:5: lv_code_10_0= ruleCode
                newCompositeNode(self.grammarAccess.getTypeAccess().getCodeCodeParserRuleCall_2_0())
                pushFollow(FOLLOW_2)
                lv_code_10_0 = ruleCode()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getTypeRule())
                set(current, "code", lv_code_10_0, "org.lflang.LF.Code")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleType"
    #  $ANTLR start "entryRuleArraySpec"
    #  InternalLF.g:5035:1: entryRuleArraySpec returns [EObject current=null] : iv_ruleArraySpec= ruleArraySpec EOF ;
    def entryRuleArraySpec(self):
        """ generated source for method entryRuleArraySpec """
        current = None
        iv_ruleArraySpec = None
        try:
            #  InternalLF.g:5035:50: (iv_ruleArraySpec= ruleArraySpec EOF )
            #  InternalLF.g:5036:2: iv_ruleArraySpec= ruleArraySpec EOF
            newCompositeNode(self.grammarAccess.getArraySpecRule())
            pushFollow(FOLLOW_1)
            iv_ruleArraySpec = ruleArraySpec()
            state._fsp -= 1
            current = iv_ruleArraySpec
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleArraySpec"
    #  $ANTLR start "ruleArraySpec"
    #  InternalLF.g:5042:1: ruleArraySpec returns [EObject current=null] : (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) ) ;
    def ruleArraySpec(self):
        """ generated source for method ruleArraySpec """
        current = None
        otherlv_0 = None
        lv_ofVariableLength_1_0 = None
        lv_length_2_0 = None
        otherlv_3 = None
        enterRule()
        try:
            #  InternalLF.g:5048:2: ( (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) ) )
            #  InternalLF.g:5049:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) )
            #  InternalLF.g:5049:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) ) )
            #  InternalLF.g:5050:3: otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) )
            otherlv_0 = match(input, 60, FOLLOW_95)
            newLeafNode(otherlv_0, self.grammarAccess.getArraySpecAccess().getLeftSquareBracketKeyword_0())
            #  InternalLF.g:5054:3: ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' ) )
            alt129 = 2
            LA129_0 = input.LA(1)
            if (LA129_0 == 61):
                alt129 = 1
            elif (LA129_0 == self.RULE_INT):
                alt129 = 2
            else:
                nvae = NoViableAltException("", 129, 0, input)
                raise nvae
            if alt129 == 1:
                #  InternalLF.g:5055:4: ( (lv_ofVariableLength_1_0= ']' ) )
                #  InternalLF.g:5055:4: ( (lv_ofVariableLength_1_0= ']' ) )
                #  InternalLF.g:5056:5: (lv_ofVariableLength_1_0= ']' )
                #  InternalLF.g:5056:5: (lv_ofVariableLength_1_0= ']' )
                #  InternalLF.g:5057:6: lv_ofVariableLength_1_0= ']'
                lv_ofVariableLength_1_0 = match(input, 61, FOLLOW_2)
                newLeafNode(lv_ofVariableLength_1_0, self.grammarAccess.getArraySpecAccess().getOfVariableLengthRightSquareBracketKeyword_1_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getArraySpecRule())
                setWithLastConsumed(current, "ofVariableLength", lv_ofVariableLength_1_0 != None, "]")
            elif alt129 == 2:
                #  InternalLF.g:5070:4: ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' )
                #  InternalLF.g:5070:4: ( ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']' )
                #  InternalLF.g:5071:5: ( (lv_length_2_0= RULE_INT ) ) otherlv_3= ']'
                #  InternalLF.g:5071:5: ( (lv_length_2_0= RULE_INT ) )
                #  InternalLF.g:5072:6: (lv_length_2_0= RULE_INT )
                #  InternalLF.g:5072:6: (lv_length_2_0= RULE_INT )
                #  InternalLF.g:5073:7: lv_length_2_0= RULE_INT
                lv_length_2_0 = match(input, self.RULE_INT, FOLLOW_86)
                newLeafNode(lv_length_2_0, self.grammarAccess.getArraySpecAccess().getLengthINTTerminalRuleCall_1_1_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getArraySpecRule())
                setWithLastConsumed(current, "length", lv_length_2_0, "org.lflang.LF.INT")
                otherlv_3 = match(input, 61, FOLLOW_2)
                newLeafNode(otherlv_3, self.grammarAccess.getArraySpecAccess().getRightSquareBracketKeyword_1_1_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleArraySpec"
    #  $ANTLR start "entryRuleWidthSpec"
    #  InternalLF.g:5099:1: entryRuleWidthSpec returns [EObject current=null] : iv_ruleWidthSpec= ruleWidthSpec EOF ;
    def entryRuleWidthSpec(self):
        """ generated source for method entryRuleWidthSpec """
        current = None
        iv_ruleWidthSpec = None
        try:
            #  InternalLF.g:5099:50: (iv_ruleWidthSpec= ruleWidthSpec EOF )
            #  InternalLF.g:5100:2: iv_ruleWidthSpec= ruleWidthSpec EOF
            newCompositeNode(self.grammarAccess.getWidthSpecRule())
            pushFollow(FOLLOW_1)
            iv_ruleWidthSpec = ruleWidthSpec()
            state._fsp -= 1
            current = iv_ruleWidthSpec
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleWidthSpec"
    #  $ANTLR start "ruleWidthSpec"
    #  InternalLF.g:5106:1: ruleWidthSpec returns [EObject current=null] : (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) ) ;
    def ruleWidthSpec(self):
        """ generated source for method ruleWidthSpec """
        current = None
        otherlv_0 = None
        lv_ofVariableLength_1_0 = None
        otherlv_3 = None
        otherlv_5 = None
        lv_terms_2_0 = None
        lv_terms_4_0 = None
        enterRule()
        try:
            #  InternalLF.g:5112:2: ( (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) ) )
            #  InternalLF.g:5113:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) )
            #  InternalLF.g:5113:2: (otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) ) )
            #  InternalLF.g:5114:3: otherlv_0= '[' ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) )
            otherlv_0 = match(input, 60, FOLLOW_96)
            newLeafNode(otherlv_0, self.grammarAccess.getWidthSpecAccess().getLeftSquareBracketKeyword_0())
            #  InternalLF.g:5118:3: ( ( (lv_ofVariableLength_1_0= ']' ) ) | ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' ) )
            alt131 = 2
            LA131_0 = input.LA(1)
            if (LA131_0 == 61):
                alt131 = 1
            elif (LA131_0 == self.RULE_ID or LA131_0 == self.RULE_INT or LA131_0 == 66 or LA131_0 == 71):
                alt131 = 2
            else:
                nvae = NoViableAltException("", 131, 0, input)
                raise nvae
            if alt131 == 1:
                #  InternalLF.g:5119:4: ( (lv_ofVariableLength_1_0= ']' ) )
                #  InternalLF.g:5119:4: ( (lv_ofVariableLength_1_0= ']' ) )
                #  InternalLF.g:5120:5: (lv_ofVariableLength_1_0= ']' )
                #  InternalLF.g:5120:5: (lv_ofVariableLength_1_0= ']' )
                #  InternalLF.g:5121:6: lv_ofVariableLength_1_0= ']'
                lv_ofVariableLength_1_0 = match(input, 61, FOLLOW_2)
                newLeafNode(lv_ofVariableLength_1_0, self.grammarAccess.getWidthSpecAccess().getOfVariableLengthRightSquareBracketKeyword_1_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getWidthSpecRule())
                setWithLastConsumed(current, "ofVariableLength", lv_ofVariableLength_1_0 != None, "]")
            elif alt131 == 2:
                #  InternalLF.g:5134:4: ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' )
                #  InternalLF.g:5134:4: ( ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']' )
                #  InternalLF.g:5135:5: ( (lv_terms_2_0= ruleWidthTerm ) ) (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )* otherlv_5= ']'
                #  InternalLF.g:5135:5: ( (lv_terms_2_0= ruleWidthTerm ) )
                #  InternalLF.g:5136:6: (lv_terms_2_0= ruleWidthTerm )
                #  InternalLF.g:5136:6: (lv_terms_2_0= ruleWidthTerm )
                #  InternalLF.g:5137:7: lv_terms_2_0= ruleWidthTerm
                newCompositeNode(self.grammarAccess.getWidthSpecAccess().getTermsWidthTermParserRuleCall_1_1_0_0())
                pushFollow(FOLLOW_97)
                lv_terms_2_0 = ruleWidthTerm()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getWidthSpecRule())
                add(current, "terms", lv_terms_2_0, "org.lflang.LF.WidthTerm")
                afterParserOrEnumRuleCall()
                #  InternalLF.g:5154:5: (otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) ) )*
                while True:
                    alt130 = 2
                    LA130_0 = input.LA(1)
                    if (LA130_0 == 55):
                        alt130 = 1
                    if alt130 == 1:
                        #  InternalLF.g:5155:6: otherlv_3= '+' ( (lv_terms_4_0= ruleWidthTerm ) )
                        otherlv_3 = match(input, 55, FOLLOW_96)
                        newLeafNode(otherlv_3, self.grammarAccess.getWidthSpecAccess().getPlusSignKeyword_1_1_1_0())
                        #  InternalLF.g:5159:6: ( (lv_terms_4_0= ruleWidthTerm ) )
                        #  InternalLF.g:5160:7: (lv_terms_4_0= ruleWidthTerm )
                        #  InternalLF.g:5160:7: (lv_terms_4_0= ruleWidthTerm )
                        #  InternalLF.g:5161:8: lv_terms_4_0= ruleWidthTerm
                        newCompositeNode(self.grammarAccess.getWidthSpecAccess().getTermsWidthTermParserRuleCall_1_1_1_1_0())
                        pushFollow(FOLLOW_97)
                        lv_terms_4_0 = ruleWidthTerm()
                        state._fsp -= 1
                        if current == None:
                            current = createModelElementForParent(self.grammarAccess.getWidthSpecRule())
                        add(current, "terms", lv_terms_4_0, "org.lflang.LF.WidthTerm")
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                otherlv_5 = match(input, 61, FOLLOW_2)
                newLeafNode(otherlv_5, self.grammarAccess.getWidthSpecAccess().getRightSquareBracketKeyword_1_1_2())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleWidthSpec"
    #  $ANTLR start "entryRuleWidthTerm"
    #  InternalLF.g:5189:1: entryRuleWidthTerm returns [EObject current=null] : iv_ruleWidthTerm= ruleWidthTerm EOF ;
    def entryRuleWidthTerm(self):
        """ generated source for method entryRuleWidthTerm """
        current = None
        iv_ruleWidthTerm = None
        try:
            #  InternalLF.g:5189:50: (iv_ruleWidthTerm= ruleWidthTerm EOF )
            #  InternalLF.g:5190:2: iv_ruleWidthTerm= ruleWidthTerm EOF
            newCompositeNode(self.grammarAccess.getWidthTermRule())
            pushFollow(FOLLOW_1)
            iv_ruleWidthTerm = ruleWidthTerm()
            state._fsp -= 1
            current = iv_ruleWidthTerm
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleWidthTerm"
    #  $ANTLR start "ruleWidthTerm"
    #  InternalLF.g:5196:1: ruleWidthTerm returns [EObject current=null] : ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) ) ;
    def ruleWidthTerm(self):
        """ generated source for method ruleWidthTerm """
        current = None
        lv_width_0_0 = None
        otherlv_1 = None
        otherlv_2 = None
        otherlv_4 = None
        lv_port_3_0 = None
        lv_code_5_0 = None
        enterRule()
        try:
            #  InternalLF.g:5202:2: ( ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) ) )
            #  InternalLF.g:5203:2: ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) )
            #  InternalLF.g:5203:2: ( ( (lv_width_0_0= RULE_INT ) ) | ( (otherlv_1= RULE_ID ) ) | (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' ) | ( (lv_code_5_0= ruleCode ) ) )
            alt132 = 4
            if input.LA(1) == self.RULE_INT:
                alt132 = 1
            elif input.LA(1) == self.RULE_ID:
                alt132 = 2
            elif input.LA(1) == 66:
                alt132 = 3
            elif input.LA(1) == 71:
                alt132 = 4
            else:
                nvae = NoViableAltException("", 132, 0, input)
                raise nvae
            if alt132 == 1:
                #  InternalLF.g:5204:3: ( (lv_width_0_0= RULE_INT ) )
                #  InternalLF.g:5204:3: ( (lv_width_0_0= RULE_INT ) )
                #  InternalLF.g:5205:4: (lv_width_0_0= RULE_INT )
                #  InternalLF.g:5205:4: (lv_width_0_0= RULE_INT )
                #  InternalLF.g:5206:5: lv_width_0_0= RULE_INT
                lv_width_0_0 = match(input, self.RULE_INT, FOLLOW_2)
                newLeafNode(lv_width_0_0, self.grammarAccess.getWidthTermAccess().getWidthINTTerminalRuleCall_0_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getWidthTermRule())
                setWithLastConsumed(current, "width", lv_width_0_0, "org.lflang.LF.INT")
            elif alt132 == 2:
                #  InternalLF.g:5223:3: ( (otherlv_1= RULE_ID ) )
                #  InternalLF.g:5223:3: ( (otherlv_1= RULE_ID ) )
                #  InternalLF.g:5224:4: (otherlv_1= RULE_ID )
                #  InternalLF.g:5224:4: (otherlv_1= RULE_ID )
                #  InternalLF.g:5225:5: otherlv_1= RULE_ID
                if current == None:
                    current = createModelElement(self.grammarAccess.getWidthTermRule())
                otherlv_1 = match(input, self.RULE_ID, FOLLOW_2)
                newLeafNode(otherlv_1, self.grammarAccess.getWidthTermAccess().getParameterParameterCrossReference_1_0())
            elif alt132 == 3:
                #  InternalLF.g:5237:3: (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' )
                #  InternalLF.g:5237:3: (otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')' )
                #  InternalLF.g:5238:4: otherlv_2= 'widthof(' ( (lv_port_3_0= ruleVarRef ) ) otherlv_4= ')'
                otherlv_2 = match(input, 66, FOLLOW_61)
                newLeafNode(otherlv_2, self.grammarAccess.getWidthTermAccess().getWidthofKeyword_2_0())
                #  InternalLF.g:5242:4: ( (lv_port_3_0= ruleVarRef ) )
                #  InternalLF.g:5243:5: (lv_port_3_0= ruleVarRef )
                #  InternalLF.g:5243:5: (lv_port_3_0= ruleVarRef )
                #  InternalLF.g:5244:6: lv_port_3_0= ruleVarRef
                newCompositeNode(self.grammarAccess.getWidthTermAccess().getPortVarRefParserRuleCall_2_1_0())
                pushFollow(FOLLOW_47)
                lv_port_3_0 = self.ruleVarRef()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getWidthTermRule())
                set(current, "port", lv_port_3_0, "org.lflang.LF.VarRef")
                afterParserOrEnumRuleCall()
                otherlv_4 = match(input, 29, FOLLOW_2)
                newLeafNode(otherlv_4, self.grammarAccess.getWidthTermAccess().getRightParenthesisKeyword_2_2())
            elif alt132 == 4:
                #  InternalLF.g:5267:3: ( (lv_code_5_0= ruleCode ) )
                #  InternalLF.g:5267:3: ( (lv_code_5_0= ruleCode ) )
                #  InternalLF.g:5268:4: (lv_code_5_0= ruleCode )
                #  InternalLF.g:5268:4: (lv_code_5_0= ruleCode )
                #  InternalLF.g:5269:5: lv_code_5_0= ruleCode
                newCompositeNode(self.grammarAccess.getWidthTermAccess().getCodeCodeParserRuleCall_3_0())
                pushFollow(FOLLOW_2)
                lv_code_5_0 = ruleCode()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getWidthTermRule())
                set(current, "code", lv_code_5_0, "org.lflang.LF.Code")
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleWidthTerm"
    #  $ANTLR start "entryRuleIPV4Host"
    #  InternalLF.g:5290:1: entryRuleIPV4Host returns [EObject current=null] : iv_ruleIPV4Host= ruleIPV4Host EOF ;
    def entryRuleIPV4Host(self):
        """ generated source for method entryRuleIPV4Host """
        current = None
        iv_ruleIPV4Host = None
        try:
            #  InternalLF.g:5290:49: (iv_ruleIPV4Host= ruleIPV4Host EOF )
            #  InternalLF.g:5291:2: iv_ruleIPV4Host= ruleIPV4Host EOF
            newCompositeNode(self.grammarAccess.getIPV4HostRule())
            pushFollow(FOLLOW_1)
            iv_ruleIPV4Host = ruleIPV4Host()
            state._fsp -= 1
            current = iv_ruleIPV4Host
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleIPV4Host"
    #  $ANTLR start "ruleIPV4Host"
    #  InternalLF.g:5297:1: ruleIPV4Host returns [EObject current=null] : ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) ;
    def ruleIPV4Host(self):
        """ generated source for method ruleIPV4Host """
        current = None
        otherlv_1 = None
        otherlv_3 = None
        lv_port_4_0 = None
        lv_user_0_0 = None
        lv_addr_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:5303:2: ( ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) )
            #  InternalLF.g:5304:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
            #  InternalLF.g:5304:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
            #  InternalLF.g:5305:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleIPV4Addr ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
            #  InternalLF.g:5305:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )?
            alt133 = 2
            LA133_0 = input.LA(1)
            if (LA133_0 == self.RULE_ID or LA133_0 == 68):
                alt133 = 1
            if alt133 == 1:
                #  InternalLF.g:5306:4: ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@'
                #  InternalLF.g:5306:4: ( (lv_user_0_0= ruleKebab ) )
                #  InternalLF.g:5307:5: (lv_user_0_0= ruleKebab )
                #  InternalLF.g:5307:5: (lv_user_0_0= ruleKebab )
                #  InternalLF.g:5308:6: lv_user_0_0= ruleKebab
                newCompositeNode(self.grammarAccess.getIPV4HostAccess().getUserKebabParserRuleCall_0_0_0())
                pushFollow(FOLLOW_98)
                lv_user_0_0 = ruleKebab()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getIPV4HostRule())
                set(current, "user", lv_user_0_0, "org.lflang.LF.Kebab")
                afterParserOrEnumRuleCall()
                otherlv_1 = match(input, 59, FOLLOW_99)
                newLeafNode(otherlv_1, self.grammarAccess.getIPV4HostAccess().getCommercialAtKeyword_0_1())
            #  InternalLF.g:5330:3: ( (lv_addr_2_0= ruleIPV4Addr ) )
            #  InternalLF.g:5331:4: (lv_addr_2_0= ruleIPV4Addr )
            #  InternalLF.g:5331:4: (lv_addr_2_0= ruleIPV4Addr )
            #  InternalLF.g:5332:5: lv_addr_2_0= ruleIPV4Addr
            newCompositeNode(self.grammarAccess.getIPV4HostAccess().getAddrIPV4AddrParserRuleCall_1_0())
            pushFollow(FOLLOW_39)
            lv_addr_2_0 = ruleIPV4Addr()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getIPV4HostRule())
            set(current, "addr", lv_addr_2_0, "org.lflang.LF.IPV4Addr")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:5349:3: (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
            alt134 = 2
            LA134_0 = input.LA(1)
            if (LA134_0 == 37):
                alt134 = 1
            if alt134 == 1:
                #  InternalLF.g:5350:4: otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) )
                otherlv_3 = match(input, 37, FOLLOW_100)
                newLeafNode(otherlv_3, self.grammarAccess.getIPV4HostAccess().getColonKeyword_2_0())
                #  InternalLF.g:5354:4: ( (lv_port_4_0= RULE_INT ) )
                #  InternalLF.g:5355:5: (lv_port_4_0= RULE_INT )
                #  InternalLF.g:5355:5: (lv_port_4_0= RULE_INT )
                #  InternalLF.g:5356:6: lv_port_4_0= RULE_INT
                lv_port_4_0 = match(input, self.RULE_INT, FOLLOW_2)
                newLeafNode(lv_port_4_0, self.grammarAccess.getIPV4HostAccess().getPortINTTerminalRuleCall_2_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getIPV4HostRule())
                setWithLastConsumed(current, "port", lv_port_4_0, "org.lflang.LF.INT")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleIPV4Host"
    #  $ANTLR start "entryRuleIPV6Host"
    #  InternalLF.g:5377:1: entryRuleIPV6Host returns [EObject current=null] : iv_ruleIPV6Host= ruleIPV6Host EOF ;
    def entryRuleIPV6Host(self):
        """ generated source for method entryRuleIPV6Host """
        current = None
        iv_ruleIPV6Host = None
        try:
            #  InternalLF.g:5377:49: (iv_ruleIPV6Host= ruleIPV6Host EOF )
            #  InternalLF.g:5378:2: iv_ruleIPV6Host= ruleIPV6Host EOF
            newCompositeNode(self.grammarAccess.getIPV6HostRule())
            pushFollow(FOLLOW_1)
            iv_ruleIPV6Host = ruleIPV6Host()
            state._fsp -= 1
            current = iv_ruleIPV6Host
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleIPV6Host"
    #  $ANTLR start "ruleIPV6Host"
    #  InternalLF.g:5384:1: ruleIPV6Host returns [EObject current=null] : (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? ) ;
    def ruleIPV6Host(self):
        """ generated source for method ruleIPV6Host """
        current = None
        otherlv_0 = None
        otherlv_2 = None
        otherlv_4 = None
        otherlv_5 = None
        lv_port_6_0 = None
        lv_user_1_0 = None
        lv_addr_3_0 = None
        enterRule()
        try:
            #  InternalLF.g:5390:2: ( (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? ) )
            #  InternalLF.g:5391:2: (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? )
            #  InternalLF.g:5391:2: (otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )? )
            #  InternalLF.g:5392:3: otherlv_0= '[' ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )? ( (lv_addr_3_0= ruleIPV6Addr ) ) otherlv_4= ']' (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )?
            otherlv_0 = match(input, 60, FOLLOW_101)
            newLeafNode(otherlv_0, self.grammarAccess.getIPV6HostAccess().getLeftSquareBracketKeyword_0())
            #  InternalLF.g:5396:3: ( ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@' )?
            alt135 = 2
            LA135_0 = input.LA(1)
            if (LA135_0 == self.RULE_ID):
                LA135_1 = input.LA(2)
                if (LA135_1 == 59 or LA135_1 == 69):
                    alt135 = 1
            elif (LA135_0 == 68):
                alt135 = 1
            if alt135 == 1:
                #  InternalLF.g:5397:4: ( (lv_user_1_0= ruleKebab ) ) otherlv_2= '@'
                #  InternalLF.g:5397:4: ( (lv_user_1_0= ruleKebab ) )
                #  InternalLF.g:5398:5: (lv_user_1_0= ruleKebab )
                #  InternalLF.g:5398:5: (lv_user_1_0= ruleKebab )
                #  InternalLF.g:5399:6: lv_user_1_0= ruleKebab
                newCompositeNode(self.grammarAccess.getIPV6HostAccess().getUserKebabParserRuleCall_1_0_0())
                pushFollow(FOLLOW_98)
                lv_user_1_0 = ruleKebab()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getIPV6HostRule())
                set(current, "user", lv_user_1_0, "org.lflang.LF.Kebab")
                afterParserOrEnumRuleCall()
                otherlv_2 = match(input, 59, FOLLOW_101)
                newLeafNode(otherlv_2, self.grammarAccess.getIPV6HostAccess().getCommercialAtKeyword_1_1())
            #  InternalLF.g:5421:3: ( (lv_addr_3_0= ruleIPV6Addr ) )
            #  InternalLF.g:5422:4: (lv_addr_3_0= ruleIPV6Addr )
            #  InternalLF.g:5422:4: (lv_addr_3_0= ruleIPV6Addr )
            #  InternalLF.g:5423:5: lv_addr_3_0= ruleIPV6Addr
            newCompositeNode(self.grammarAccess.getIPV6HostAccess().getAddrIPV6AddrParserRuleCall_2_0())
            pushFollow(FOLLOW_86)
            lv_addr_3_0 = ruleIPV6Addr()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getIPV6HostRule())
            set(current, "addr", lv_addr_3_0, "org.lflang.LF.IPV6Addr")
            afterParserOrEnumRuleCall()
            otherlv_4 = match(input, 61, FOLLOW_39)
            newLeafNode(otherlv_4, self.grammarAccess.getIPV6HostAccess().getRightSquareBracketKeyword_3())
            #  InternalLF.g:5444:3: (otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) ) )?
            alt136 = 2
            LA136_0 = input.LA(1)
            if (LA136_0 == 37):
                alt136 = 1
            if alt136 == 1:
                #  InternalLF.g:5445:4: otherlv_5= ':' ( (lv_port_6_0= RULE_INT ) )
                otherlv_5 = match(input, 37, FOLLOW_100)
                newLeafNode(otherlv_5, self.grammarAccess.getIPV6HostAccess().getColonKeyword_4_0())
                #  InternalLF.g:5449:4: ( (lv_port_6_0= RULE_INT ) )
                #  InternalLF.g:5450:5: (lv_port_6_0= RULE_INT )
                #  InternalLF.g:5450:5: (lv_port_6_0= RULE_INT )
                #  InternalLF.g:5451:6: lv_port_6_0= RULE_INT
                lv_port_6_0 = match(input, self.RULE_INT, FOLLOW_2)
                newLeafNode(lv_port_6_0, self.grammarAccess.getIPV6HostAccess().getPortINTTerminalRuleCall_4_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getIPV6HostRule())
                setWithLastConsumed(current, "port", lv_port_6_0, "org.lflang.LF.INT")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleIPV6Host"
    #  $ANTLR start "entryRuleNamedHost"
    #  InternalLF.g:5472:1: entryRuleNamedHost returns [EObject current=null] : iv_ruleNamedHost= ruleNamedHost EOF ;
    def entryRuleNamedHost(self):
        """ generated source for method entryRuleNamedHost """
        current = None
        iv_ruleNamedHost = None
        try:
            #  InternalLF.g:5472:50: (iv_ruleNamedHost= ruleNamedHost EOF )
            #  InternalLF.g:5473:2: iv_ruleNamedHost= ruleNamedHost EOF
            newCompositeNode(self.grammarAccess.getNamedHostRule())
            pushFollow(FOLLOW_1)
            iv_ruleNamedHost = ruleNamedHost()
            state._fsp -= 1
            current = iv_ruleNamedHost
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleNamedHost"
    #  $ANTLR start "ruleNamedHost"
    #  InternalLF.g:5479:1: ruleNamedHost returns [EObject current=null] : ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) ;
    def ruleNamedHost(self):
        """ generated source for method ruleNamedHost """
        current = None
        otherlv_1 = None
        otherlv_3 = None
        lv_port_4_0 = None
        lv_user_0_0 = None
        lv_addr_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:5485:2: ( ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? ) )
            #  InternalLF.g:5486:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
            #  InternalLF.g:5486:2: ( ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )? )
            #  InternalLF.g:5487:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )? ( (lv_addr_2_0= ruleHostName ) ) (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
            #  InternalLF.g:5487:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )?
            alt137 = 2
            alt137 = dfa137.predict(input)
            if alt137 == 1:
                #  InternalLF.g:5488:4: ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@'
                #  InternalLF.g:5488:4: ( (lv_user_0_0= ruleKebab ) )
                #  InternalLF.g:5489:5: (lv_user_0_0= ruleKebab )
                #  InternalLF.g:5489:5: (lv_user_0_0= ruleKebab )
                #  InternalLF.g:5490:6: lv_user_0_0= ruleKebab
                newCompositeNode(self.grammarAccess.getNamedHostAccess().getUserKebabParserRuleCall_0_0_0())
                pushFollow(FOLLOW_98)
                lv_user_0_0 = ruleKebab()
                state._fsp -= 1
                if current == None:
                    current = createModelElementForParent(self.grammarAccess.getNamedHostRule())
                set(current, "user", lv_user_0_0, "org.lflang.LF.Kebab")
                afterParserOrEnumRuleCall()
                otherlv_1 = match(input, 59, FOLLOW_20)
                newLeafNode(otherlv_1, self.grammarAccess.getNamedHostAccess().getCommercialAtKeyword_0_1())
            #  InternalLF.g:5512:3: ( (lv_addr_2_0= ruleHostName ) )
            #  InternalLF.g:5513:4: (lv_addr_2_0= ruleHostName )
            #  InternalLF.g:5513:4: (lv_addr_2_0= ruleHostName )
            #  InternalLF.g:5514:5: lv_addr_2_0= ruleHostName
            newCompositeNode(self.grammarAccess.getNamedHostAccess().getAddrHostNameParserRuleCall_1_0())
            pushFollow(FOLLOW_39)
            lv_addr_2_0 = ruleHostName()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getNamedHostRule())
            set(current, "addr", lv_addr_2_0, "org.lflang.LF.HostName")
            afterParserOrEnumRuleCall()
            #  InternalLF.g:5531:3: (otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) ) )?
            alt138 = 2
            LA138_0 = input.LA(1)
            if (LA138_0 == 37):
                alt138 = 1
            if alt138 == 1:
                #  InternalLF.g:5532:4: otherlv_3= ':' ( (lv_port_4_0= RULE_INT ) )
                otherlv_3 = match(input, 37, FOLLOW_100)
                newLeafNode(otherlv_3, self.grammarAccess.getNamedHostAccess().getColonKeyword_2_0())
                #  InternalLF.g:5536:4: ( (lv_port_4_0= RULE_INT ) )
                #  InternalLF.g:5537:5: (lv_port_4_0= RULE_INT )
                #  InternalLF.g:5537:5: (lv_port_4_0= RULE_INT )
                #  InternalLF.g:5538:6: lv_port_4_0= RULE_INT
                lv_port_4_0 = match(input, self.RULE_INT, FOLLOW_2)
                newLeafNode(lv_port_4_0, self.grammarAccess.getNamedHostAccess().getPortINTTerminalRuleCall_2_1_0())
                if current == None:
                    current = createModelElement(self.grammarAccess.getNamedHostRule())
                setWithLastConsumed(current, "port", lv_port_4_0, "org.lflang.LF.INT")
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleNamedHost"
    #  $ANTLR start "entryRuleHost"
    #  InternalLF.g:5559:1: entryRuleHost returns [EObject current=null] : iv_ruleHost= ruleHost EOF ;
    def entryRuleHost(self):
        """ generated source for method entryRuleHost """
        current = None
        iv_ruleHost = None
        try:
            #  InternalLF.g:5559:45: (iv_ruleHost= ruleHost EOF )
            #  InternalLF.g:5560:2: iv_ruleHost= ruleHost EOF
            newCompositeNode(self.grammarAccess.getHostRule())
            pushFollow(FOLLOW_1)
            iv_ruleHost = ruleHost()
            state._fsp -= 1
            current = iv_ruleHost
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleHost"
    #  $ANTLR start "ruleHost"
    #  InternalLF.g:5566:1: ruleHost returns [EObject current=null] : (this_IPV4Host_0= ruleIPV4Host | this_IPV6Host_1= ruleIPV6Host | this_NamedHost_2= ruleNamedHost ) ;
    def ruleHost(self):
        """ generated source for method ruleHost """
        current = None
        this_IPV4Host_0 = None
        this_IPV6Host_1 = None
        this_NamedHost_2 = None
        enterRule()
        try:
            #  InternalLF.g:5572:2: ( (this_IPV4Host_0= ruleIPV4Host | this_IPV6Host_1= ruleIPV6Host | this_NamedHost_2= ruleNamedHost ) )
            #  InternalLF.g:5573:2: (this_IPV4Host_0= ruleIPV4Host | this_IPV6Host_1= ruleIPV6Host | this_NamedHost_2= ruleNamedHost )
            #  InternalLF.g:5573:2: (this_IPV4Host_0= ruleIPV4Host | this_IPV6Host_1= ruleIPV6Host | this_NamedHost_2= ruleNamedHost )
            alt139 = 3
            alt139 = dfa139.predict(input)
            if alt139 == 1:
                #  InternalLF.g:5574:3: this_IPV4Host_0= ruleIPV4Host
                newCompositeNode(self.grammarAccess.getHostAccess().getIPV4HostParserRuleCall_0())
                pushFollow(FOLLOW_2)
                this_IPV4Host_0 = self.ruleIPV4Host()
                state._fsp -= 1
                current = this_IPV4Host_0
                afterParserOrEnumRuleCall()
            elif alt139 == 2:
                #  InternalLF.g:5583:3: this_IPV6Host_1= ruleIPV6Host
                newCompositeNode(self.grammarAccess.getHostAccess().getIPV6HostParserRuleCall_1())
                pushFollow(FOLLOW_2)
                this_IPV6Host_1 = self.ruleIPV6Host()
                state._fsp -= 1
                current = this_IPV6Host_1
                afterParserOrEnumRuleCall()
            elif alt139 == 3:
                #  InternalLF.g:5592:3: this_NamedHost_2= ruleNamedHost
                newCompositeNode(self.grammarAccess.getHostAccess().getNamedHostParserRuleCall_2())
                pushFollow(FOLLOW_2)
                this_NamedHost_2 = self.ruleNamedHost()
                state._fsp -= 1
                current = this_NamedHost_2
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleHost"
    #  $ANTLR start "entryRuleHostName"
    #  InternalLF.g:5604:1: entryRuleHostName returns [String current=null] : iv_ruleHostName= ruleHostName EOF ;
    def entryRuleHostName(self):
        """ generated source for method entryRuleHostName """
        current = None
        iv_ruleHostName = None
        try:
            #  InternalLF.g:5604:48: (iv_ruleHostName= ruleHostName EOF )
            #  InternalLF.g:5605:2: iv_ruleHostName= ruleHostName EOF
            newCompositeNode(self.grammarAccess.getHostNameRule())
            pushFollow(FOLLOW_1)
            iv_ruleHostName = ruleHostName()
            state._fsp -= 1
            current = iv_ruleHostName.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleHostName"
    #  $ANTLR start "ruleHostName"
    #  InternalLF.g:5611:1: ruleHostName returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* ) ;
    def ruleHostName(self):
        """ generated source for method ruleHostName """
        current = AntlrDatatypeRuleToken()
        kw = None
        this_Kebab_0 = None
        this_Kebab_2 = None
        enterRule()
        try:
            #  InternalLF.g:5617:2: ( (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* ) )
            #  InternalLF.g:5618:2: (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* )
            #  InternalLF.g:5618:2: (this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )* )
            #  InternalLF.g:5619:3: this_Kebab_0= ruleKebab (kw= '.' this_Kebab_2= ruleKebab )*
            newCompositeNode(self.grammarAccess.getHostNameAccess().getKebabParserRuleCall_0())
            pushFollow(FOLLOW_102)
            this_Kebab_0 = ruleKebab()
            state._fsp -= 1
            current.merge(this_Kebab_0)
            afterParserOrEnumRuleCall()
            #  InternalLF.g:5629:3: (kw= '.' this_Kebab_2= ruleKebab )*
            while True:
                alt140 = 2
                LA140_0 = input.LA(1)
                if (LA140_0 == 62):
                    alt140 = 1
                if alt140 == 1:
                    #  InternalLF.g:5630:4: kw= '.' this_Kebab_2= ruleKebab
                    kw = match(input, 62, FOLLOW_81)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getHostNameAccess().getFullStopKeyword_1_0())
                    newCompositeNode(self.grammarAccess.getHostNameAccess().getKebabParserRuleCall_1_1())
                    pushFollow(FOLLOW_102)
                    this_Kebab_2 = ruleKebab()
                    state._fsp -= 1
                    current.merge(this_Kebab_2)
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleHostName"
    #  $ANTLR start "entryRuleDottedName"
    #  InternalLF.g:5650:1: entryRuleDottedName returns [String current=null] : iv_ruleDottedName= ruleDottedName EOF ;
    def entryRuleDottedName(self):
        """ generated source for method entryRuleDottedName """
        current = None
        iv_ruleDottedName = None
        try:
            #  InternalLF.g:5650:50: (iv_ruleDottedName= ruleDottedName EOF )
            #  InternalLF.g:5651:2: iv_ruleDottedName= ruleDottedName EOF
            newCompositeNode(self.grammarAccess.getDottedNameRule())
            pushFollow(FOLLOW_1)
            iv_ruleDottedName = ruleDottedName()
            state._fsp -= 1
            current = iv_ruleDottedName.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleDottedName"
    #  $ANTLR start "ruleDottedName"
    #  InternalLF.g:5657:1: ruleDottedName returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID ( (kw= '.' | kw= '::' ) this_ID_3= RULE_ID )* ) ;
    def ruleDottedName(self):
        """ generated source for method ruleDottedName """
        current = AntlrDatatypeRuleToken()
        this_ID_0 = None
        kw = None
        this_ID_3 = None
        enterRule()
        try:
            #  InternalLF.g:5663:2: ( (this_ID_0= RULE_ID ( (kw= '.' | kw= '::' ) this_ID_3= RULE_ID )* ) )
            #  InternalLF.g:5664:2: (this_ID_0= RULE_ID ( (kw= '.' | kw= '::' ) this_ID_3= RULE_ID )* )
            #  InternalLF.g:5664:2: (this_ID_0= RULE_ID ( (kw= '.' | kw= '::' ) this_ID_3= RULE_ID )* )
            #  InternalLF.g:5665:3: this_ID_0= RULE_ID ( (kw= '.' | kw= '::' ) this_ID_3= RULE_ID )*
            this_ID_0 = match(input, self.RULE_ID, FOLLOW_103)
            current.merge(this_ID_0)
            newLeafNode(this_ID_0, self.grammarAccess.getDottedNameAccess().getIDTerminalRuleCall_0())
            #  InternalLF.g:5672:3: ( (kw= '.' | kw= '::' ) this_ID_3= RULE_ID )*
            while True:
                alt142 = 2
                LA142_0 = input.LA(1)
                if (LA142_0 == 62 or LA142_0 == 67):
                    alt142 = 1
                if alt142 == 1:
                    #  InternalLF.g:5673:4: (kw= '.' | kw= '::' ) this_ID_3= RULE_ID
                    #  InternalLF.g:5673:4: (kw= '.' | kw= '::' )
                    alt141 = 2
                    LA141_0 = input.LA(1)
                    if (LA141_0 == 62):
                        alt141 = 1
                    elif (LA141_0 == 67):
                        alt141 = 2
                    else:
                        nvae = NoViableAltException("", 141, 0, input)
                        raise nvae
                    if alt141 == 1:
                        #  InternalLF.g:5674:5: kw= '.'
                        kw = match(input, 62, FOLLOW_5)
                        current.merge(kw)
                        newLeafNode(kw, self.grammarAccess.getDottedNameAccess().getFullStopKeyword_1_0_0())
                    elif alt141 == 2:
                        #  InternalLF.g:5680:5: kw= '::'
                        kw = match(input, 67, FOLLOW_5)
                        current.merge(kw)
                        newLeafNode(kw, self.grammarAccess.getDottedNameAccess().getColonColonKeyword_1_0_1())
                    this_ID_3 = match(input, self.RULE_ID, FOLLOW_103)
                    current.merge(this_ID_3)
                    newLeafNode(this_ID_3, self.grammarAccess.getDottedNameAccess().getIDTerminalRuleCall_1_1())
                else:
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleDottedName"
    #  $ANTLR start "entryRuleSignedInt"
    #  InternalLF.g:5698:1: entryRuleSignedInt returns [String current=null] : iv_ruleSignedInt= ruleSignedInt EOF ;
    def entryRuleSignedInt(self):
        """ generated source for method entryRuleSignedInt """
        current = None
        iv_ruleSignedInt = None
        try:
            #  InternalLF.g:5698:49: (iv_ruleSignedInt= ruleSignedInt EOF )
            #  InternalLF.g:5699:2: iv_ruleSignedInt= ruleSignedInt EOF
            newCompositeNode(self.grammarAccess.getSignedIntRule())
            pushFollow(FOLLOW_1)
            iv_ruleSignedInt = ruleSignedInt()
            state._fsp -= 1
            current = iv_ruleSignedInt.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleSignedInt"
    #  $ANTLR start "ruleSignedInt"
    #  InternalLF.g:5705:1: ruleSignedInt returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_INT_0= RULE_INT | this_NEGINT_1= RULE_NEGINT ) ;
    def ruleSignedInt(self):
        """ generated source for method ruleSignedInt """
        current = AntlrDatatypeRuleToken()
        this_INT_0 = None
        this_NEGINT_1 = None
        enterRule()
        try:
            #  InternalLF.g:5711:2: ( (this_INT_0= RULE_INT | this_NEGINT_1= RULE_NEGINT ) )
            #  InternalLF.g:5712:2: (this_INT_0= RULE_INT | this_NEGINT_1= RULE_NEGINT )
            #  InternalLF.g:5712:2: (this_INT_0= RULE_INT | this_NEGINT_1= RULE_NEGINT )
            alt143 = 2
            LA143_0 = input.LA(1)
            if (LA143_0 == self.RULE_INT):
                alt143 = 1
            elif (LA143_0 == self.RULE_NEGINT):
                alt143 = 2
            else:
                nvae = NoViableAltException("", 143, 0, input)
                raise nvae
            if alt143 == 1:
                #  InternalLF.g:5713:3: this_INT_0= RULE_INT
                this_INT_0 = match(input, self.RULE_INT, FOLLOW_2)
                current.merge(this_INT_0)
                newLeafNode(this_INT_0, self.grammarAccess.getSignedIntAccess().getINTTerminalRuleCall_0())
            elif alt143 == 2:
                #  InternalLF.g:5721:3: this_NEGINT_1= RULE_NEGINT
                this_NEGINT_1 = match(input, self.RULE_NEGINT, FOLLOW_2)
                current.merge(this_NEGINT_1)
                newLeafNode(this_NEGINT_1, self.grammarAccess.getSignedIntAccess().getNEGINTTerminalRuleCall_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleSignedInt"
    #  $ANTLR start "entryRuleLiteral"
    #  InternalLF.g:5732:1: entryRuleLiteral returns [String current=null] : iv_ruleLiteral= ruleLiteral EOF ;
    def entryRuleLiteral(self):
        """ generated source for method entryRuleLiteral """
        current = None
        iv_ruleLiteral = None
        try:
            #  InternalLF.g:5732:47: (iv_ruleLiteral= ruleLiteral EOF )
            #  InternalLF.g:5733:2: iv_ruleLiteral= ruleLiteral EOF
            newCompositeNode(self.grammarAccess.getLiteralRule())
            pushFollow(FOLLOW_1)
            iv_ruleLiteral = ruleLiteral()
            state._fsp -= 1
            current = iv_ruleLiteral.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleLiteral"
    #  $ANTLR start "ruleLiteral"
    #  InternalLF.g:5739:1: ruleLiteral returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_STRING_0= RULE_STRING | this_CHAR_LIT_1= RULE_CHAR_LIT | this_SignedFloat_2= ruleSignedFloat | this_SignedInt_3= ruleSignedInt | this_Boolean_4= ruleBoolean ) ;
    def ruleLiteral(self):
        """ generated source for method ruleLiteral """
        current = AntlrDatatypeRuleToken()
        this_STRING_0 = None
        this_CHAR_LIT_1 = None
        this_SignedFloat_2 = None
        this_SignedInt_3 = None
        this_Boolean_4 = None
        enterRule()
        try:
            #  InternalLF.g:5745:2: ( (this_STRING_0= RULE_STRING | this_CHAR_LIT_1= RULE_CHAR_LIT | this_SignedFloat_2= ruleSignedFloat | this_SignedInt_3= ruleSignedInt | this_Boolean_4= ruleBoolean ) )
            #  InternalLF.g:5746:2: (this_STRING_0= RULE_STRING | this_CHAR_LIT_1= RULE_CHAR_LIT | this_SignedFloat_2= ruleSignedFloat | this_SignedInt_3= ruleSignedInt | this_Boolean_4= ruleBoolean )
            #  InternalLF.g:5746:2: (this_STRING_0= RULE_STRING | this_CHAR_LIT_1= RULE_CHAR_LIT | this_SignedFloat_2= ruleSignedFloat | this_SignedInt_3= ruleSignedInt | this_Boolean_4= ruleBoolean )
            alt144 = 5
            if input.LA(1) == self.RULE_STRING:
                alt144 = 1
            elif input.LA(1) == self.RULE_CHAR_LIT:
                alt144 = 2
            elif input.LA(1) == self.RULE_INT:
                LA144_3 = input.LA(2)
                if (LA144_3 == self.EOF or LA144_3 == self.RULE_ID or LA144_3 == 18 or LA144_3 == 20 or (LA144_3 >= 28 and LA144_3 <= 29) or LA144_3 == 33 or (LA144_3 >= 35 and LA144_3 <= 36) or (LA144_3 >= 38 and LA144_3 <= 48) or LA144_3 == 52 or (LA144_3 >= 58 and LA144_3 <= 59) or LA144_3 == 61 or LA144_3 == 63 or LA144_3 == 68 or (LA144_3 >= 81 and LA144_3 <= 83) or LA144_3 == 85):
                    alt144 = 4
                elif (LA144_3 == 62):
                    alt144 = 3
                else:
                    nvae = NoViableAltException("", 144, 3, input)
                    raise nvae
            elif input.LA(1) == self.RULE_NEGINT:
                LA144_4 = input.LA(2)
                if (LA144_4 == 62):
                    alt144 = 3
                elif (LA144_4 == self.EOF or LA144_4 == self.RULE_ID or LA144_4 == 18 or LA144_4 == 20 or (LA144_4 >= 28 and LA144_4 <= 29) or LA144_4 == 33 or (LA144_4 >= 35 and LA144_4 <= 36) or (LA144_4 >= 38 and LA144_4 <= 48) or LA144_4 == 52 or (LA144_4 >= 58 and LA144_4 <= 59) or LA144_4 == 61 or LA144_4 == 63 or LA144_4 == 68 or (LA144_4 >= 81 and LA144_4 <= 83) or LA144_4 == 85):
                    alt144 = 4
                else:
                    nvae = NoViableAltException("", 144, 4, input)
                    raise nvae
            elif input.LA(1) == 62:
                pass
            elif input.LA(1) == 69:
                alt144 = 3
            elif input.LA(1) == self.RULE_TRUE:
                pass
            elif input.LA(1) == self.RULE_FALSE:
                alt144 = 5
            else:
                nvae = NoViableAltException("", 144, 0, input)
                raise nvae
            if alt144 == 1:
                #  InternalLF.g:5747:3: this_STRING_0= RULE_STRING
                this_STRING_0 = match(input, self.RULE_STRING, FOLLOW_2)
                current.merge(this_STRING_0)
                newLeafNode(this_STRING_0, self.grammarAccess.getLiteralAccess().getSTRINGTerminalRuleCall_0())
            elif alt144 == 2:
                #  InternalLF.g:5755:3: this_CHAR_LIT_1= RULE_CHAR_LIT
                this_CHAR_LIT_1 = match(input, self.RULE_CHAR_LIT, FOLLOW_2)
                current.merge(this_CHAR_LIT_1)
                newLeafNode(this_CHAR_LIT_1, self.grammarAccess.getLiteralAccess().getCHAR_LITTerminalRuleCall_1())
            elif alt144 == 3:
                #  InternalLF.g:5763:3: this_SignedFloat_2= ruleSignedFloat
                newCompositeNode(self.grammarAccess.getLiteralAccess().getSignedFloatParserRuleCall_2())
                pushFollow(FOLLOW_2)
                this_SignedFloat_2 = ruleSignedFloat()
                state._fsp -= 1
                current.merge(this_SignedFloat_2)
                afterParserOrEnumRuleCall()
            elif alt144 == 4:
                #  InternalLF.g:5774:3: this_SignedInt_3= ruleSignedInt
                newCompositeNode(self.grammarAccess.getLiteralAccess().getSignedIntParserRuleCall_3())
                pushFollow(FOLLOW_2)
                this_SignedInt_3 = self.ruleSignedInt()
                state._fsp -= 1
                current.merge(this_SignedInt_3)
                afterParserOrEnumRuleCall()
            elif alt144 == 5:
                #  InternalLF.g:5785:3: this_Boolean_4= ruleBoolean
                newCompositeNode(self.grammarAccess.getLiteralAccess().getBooleanParserRuleCall_4())
                pushFollow(FOLLOW_2)
                this_Boolean_4 = self.ruleBoolean()
                state._fsp -= 1
                current.merge(this_Boolean_4)
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleLiteral"
    #  $ANTLR start "entryRuleKebab"
    #  InternalLF.g:5799:1: entryRuleKebab returns [String current=null] : iv_ruleKebab= ruleKebab EOF ;
    def entryRuleKebab(self):
        """ generated source for method entryRuleKebab """
        current = None
        iv_ruleKebab = None
        try:
            #  InternalLF.g:5799:45: (iv_ruleKebab= ruleKebab EOF )
            #  InternalLF.g:5800:2: iv_ruleKebab= ruleKebab EOF
            newCompositeNode(self.grammarAccess.getKebabRule())
            pushFollow(FOLLOW_1)
            iv_ruleKebab = ruleKebab()
            state._fsp -= 1
            current = iv_ruleKebab.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleKebab"
    #  $ANTLR start "ruleKebab"
    #  InternalLF.g:5806:1: ruleKebab returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : ( (this_ID_0= RULE_ID | kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* ) ;
    def ruleKebab(self):
        """ generated source for method ruleKebab """
        current = AntlrDatatypeRuleToken()
        this_ID_0 = None
        kw = None
        this_ID_3 = None
        enterRule()
        try:
            #  InternalLF.g:5812:2: ( ( (this_ID_0= RULE_ID | kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* ) )
            #  InternalLF.g:5813:2: ( (this_ID_0= RULE_ID | kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* )
            #  InternalLF.g:5813:2: ( (this_ID_0= RULE_ID | kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )* )
            #  InternalLF.g:5814:3: (this_ID_0= RULE_ID | kw= 'physical' ) (kw= '-' this_ID_3= RULE_ID )*
            #  InternalLF.g:5814:3: (this_ID_0= RULE_ID | kw= 'physical' )
            alt145 = 2
            LA145_0 = input.LA(1)
            if (LA145_0 == self.RULE_ID):
                alt145 = 1
            elif (LA145_0 == 68):
                alt145 = 2
            else:
                nvae = NoViableAltException("", 145, 0, input)
                raise nvae
            if alt145 == 1:
                #  InternalLF.g:5815:4: this_ID_0= RULE_ID
                this_ID_0 = match(input, self.RULE_ID, FOLLOW_104)
                current.merge(this_ID_0)
                newLeafNode(this_ID_0, self.grammarAccess.getKebabAccess().getIDTerminalRuleCall_0_0())
            elif alt145 == 2:
                #  InternalLF.g:5823:4: kw= 'physical'
                kw = match(input, 68, FOLLOW_104)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getKebabAccess().getPhysicalKeyword_0_1())
            #  InternalLF.g:5829:3: (kw= '-' this_ID_3= RULE_ID )*
            while True:
                alt146 = 2
                LA146_0 = input.LA(1)
                if (LA146_0 == 69):
                    alt146 = 1
                if alt146 == 1:
                    #  InternalLF.g:5830:4: kw= '-' this_ID_3= RULE_ID
                    kw = match(input, 69, FOLLOW_5)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getKebabAccess().getHyphenMinusKeyword_1_0())
                    this_ID_3 = match(input, self.RULE_ID, FOLLOW_104)
                    current.merge(this_ID_3)
                    newLeafNode(this_ID_3, self.grammarAccess.getKebabAccess().getIDTerminalRuleCall_1_1())
                else:
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleKebab"
    #  $ANTLR start "entryRuleIPV4Addr"
    #  InternalLF.g:5847:1: entryRuleIPV4Addr returns [String current=null] : iv_ruleIPV4Addr= ruleIPV4Addr EOF ;
    def entryRuleIPV4Addr(self):
        """ generated source for method entryRuleIPV4Addr """
        current = None
        iv_ruleIPV4Addr = None
        try:
            #  InternalLF.g:5847:48: (iv_ruleIPV4Addr= ruleIPV4Addr EOF )
            #  InternalLF.g:5848:2: iv_ruleIPV4Addr= ruleIPV4Addr EOF
            newCompositeNode(self.grammarAccess.getIPV4AddrRule())
            pushFollow(FOLLOW_1)
            iv_ruleIPV4Addr = ruleIPV4Addr()
            state._fsp -= 1
            current = iv_ruleIPV4Addr.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleIPV4Addr"
    #  $ANTLR start "ruleIPV4Addr"
    #  InternalLF.g:5854:1: ruleIPV4Addr returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT ) ;
    def ruleIPV4Addr(self):
        """ generated source for method ruleIPV4Addr """
        current = AntlrDatatypeRuleToken()
        this_INT_0 = None
        kw = None
        this_INT_2 = None
        this_INT_4 = None
        this_INT_6 = None
        enterRule()
        try:
            #  InternalLF.g:5860:2: ( (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT ) )
            #  InternalLF.g:5861:2: (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT )
            #  InternalLF.g:5861:2: (this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT )
            #  InternalLF.g:5862:3: this_INT_0= RULE_INT kw= '.' this_INT_2= RULE_INT kw= '.' this_INT_4= RULE_INT kw= '.' this_INT_6= RULE_INT
            this_INT_0 = match(input, self.RULE_INT, FOLLOW_87)
            current.merge(this_INT_0)
            newLeafNode(this_INT_0, self.grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_0())
            kw = match(input, 62, FOLLOW_100)
            current.merge(kw)
            newLeafNode(kw, self.grammarAccess.getIPV4AddrAccess().getFullStopKeyword_1())
            this_INT_2 = match(input, self.RULE_INT, FOLLOW_87)
            current.merge(this_INT_2)
            newLeafNode(this_INT_2, self.grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_2())
            kw = match(input, 62, FOLLOW_100)
            current.merge(kw)
            newLeafNode(kw, self.grammarAccess.getIPV4AddrAccess().getFullStopKeyword_3())
            this_INT_4 = match(input, self.RULE_INT, FOLLOW_87)
            current.merge(this_INT_4)
            newLeafNode(this_INT_4, self.grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_4())
            kw = match(input, 62, FOLLOW_100)
            current.merge(kw)
            newLeafNode(kw, self.grammarAccess.getIPV4AddrAccess().getFullStopKeyword_5())
            this_INT_6 = match(input, self.RULE_INT, FOLLOW_2)
            current.merge(this_INT_6)
            newLeafNode(this_INT_6, self.grammarAccess.getIPV4AddrAccess().getINTTerminalRuleCall_6())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleIPV4Addr"
    #  $ANTLR start "entryRuleIPV6Seg"
    #  InternalLF.g:5909:1: entryRuleIPV6Seg returns [String current=null] : iv_ruleIPV6Seg= ruleIPV6Seg EOF ;
    def entryRuleIPV6Seg(self):
        """ generated source for method entryRuleIPV6Seg """
        current = None
        iv_ruleIPV6Seg = None
        try:
            #  InternalLF.g:5909:47: (iv_ruleIPV6Seg= ruleIPV6Seg EOF )
            #  InternalLF.g:5910:2: iv_ruleIPV6Seg= ruleIPV6Seg EOF
            newCompositeNode(self.grammarAccess.getIPV6SegRule())
            pushFollow(FOLLOW_1)
            iv_ruleIPV6Seg = ruleIPV6Seg()
            state._fsp -= 1
            current = iv_ruleIPV6Seg.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleIPV6Seg"
    #  $ANTLR start "ruleIPV6Seg"
    #  InternalLF.g:5916:1: ruleIPV6Seg returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) ) ;
    def ruleIPV6Seg(self):
        """ generated source for method ruleIPV6Seg """
        current = AntlrDatatypeRuleToken()
        this_INT_0 = None
        this_INT_1 = None
        this_ID_2 = None
        enterRule()
        try:
            #  InternalLF.g:5922:2: ( (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) ) )
            #  InternalLF.g:5923:2: (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) )
            #  InternalLF.g:5923:2: (this_INT_0= RULE_INT | ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID ) )
            alt148 = 2
            LA148_0 = input.LA(1)
            if (LA148_0 == self.RULE_INT):
                LA148_1 = input.LA(2)
                if (LA148_1 == self.RULE_ID):
                    alt148 = 2
                elif (LA148_1 == self.EOF or LA148_1 == 37 or LA148_1 == 61 or LA148_1 == 67 or LA148_1 == 70):
                    alt148 = 1
                else:
                    nvae = NoViableAltException("", 148, 1, input)
                    raise nvae
            elif (LA148_0 == self.RULE_ID):
                alt148 = 2
            else:
                nvae = NoViableAltException("", 148, 0, input)
                raise nvae
            if alt148 == 1:
                #  InternalLF.g:5924:3: this_INT_0= RULE_INT
                this_INT_0 = match(input, self.RULE_INT, FOLLOW_2)
                current.merge(this_INT_0)
                newLeafNode(this_INT_0, self.grammarAccess.getIPV6SegAccess().getINTTerminalRuleCall_0())
            elif alt148 == 2:
                #  InternalLF.g:5932:3: ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID )
                #  InternalLF.g:5932:3: ( (this_INT_1= RULE_INT )? this_ID_2= RULE_ID )
                #  InternalLF.g:5933:4: (this_INT_1= RULE_INT )? this_ID_2= RULE_ID
                #  InternalLF.g:5933:4: (this_INT_1= RULE_INT )?
                alt147 = 2
                LA147_0 = input.LA(1)
                if (LA147_0 == self.RULE_INT):
                    alt147 = 1
                if alt147 == 1:
                    #  InternalLF.g:5934:5: this_INT_1= RULE_INT
                    this_INT_1 = match(input, self.RULE_INT, FOLLOW_5)
                    current.merge(this_INT_1)
                    newLeafNode(this_INT_1, self.grammarAccess.getIPV6SegAccess().getINTTerminalRuleCall_1_0())
                this_ID_2 = match(input, self.RULE_ID, FOLLOW_2)
                current.merge(this_ID_2)
                newLeafNode(this_ID_2, self.grammarAccess.getIPV6SegAccess().getIDTerminalRuleCall_1_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleIPV6Seg"
    #  $ANTLR start "entryRuleIPV6Addr"
    #  InternalLF.g:5954:1: entryRuleIPV6Addr returns [String current=null] : iv_ruleIPV6Addr= ruleIPV6Addr EOF ;
    def entryRuleIPV6Addr(self):
        """ generated source for method entryRuleIPV6Addr """
        current = None
        iv_ruleIPV6Addr = None
        try:
            #  InternalLF.g:5954:48: (iv_ruleIPV6Addr= ruleIPV6Addr EOF )
            #  InternalLF.g:5955:2: iv_ruleIPV6Addr= ruleIPV6Addr EOF
            newCompositeNode(self.grammarAccess.getIPV6AddrRule())
            pushFollow(FOLLOW_1)
            iv_ruleIPV6Addr = ruleIPV6Addr()
            state._fsp -= 1
            current = iv_ruleIPV6Addr.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleIPV6Addr"
    #  $ANTLR start "ruleIPV6Addr"
    #  InternalLF.g:5961:1: ruleIPV6Addr returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) ) ;
    def ruleIPV6Addr(self):
        """ generated source for method ruleIPV6Addr """
        current = AntlrDatatypeRuleToken()
        kw = None
        this_ID_9 = None
        this_INT_15 = None
        this_ID_16 = None
        this_ID_20 = None
        this_INT_22 = None
        this_IPV6Seg_2 = None
        this_IPV6Seg_4 = None
        this_IPV6Seg_5 = None
        this_IPV6Seg_8 = None
        this_IPV6Seg_11 = None
        this_IPV6Seg_13 = None
        this_IPV4Addr_18 = None
        this_IPV4Addr_24 = None
        this_IPV6Seg_25 = None
        this_IPV6Seg_27 = None
        this_IPV6Seg_29 = None
        this_IPV6Seg_31 = None
        this_IPV4Addr_33 = None
        enterRule()
        try:
            #  InternalLF.g:5967:2: ( (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) ) )
            #  InternalLF.g:5968:2: (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) )
            #  InternalLF.g:5968:2: (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) )
            alt159 = 7
            alt159 = dfa159.predict(input)
            if alt159 == 1:
                #  InternalLF.g:5969:3: kw= '::'
                kw = match(input, 67, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_0())
            elif alt159 == 2:
                #  InternalLF.g:5975:3: (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg )
                #  InternalLF.g:5975:3: (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg )
                #  InternalLF.g:5976:4: kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg
                kw = match(input, 67, FOLLOW_105)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_1_0())
                #  InternalLF.g:5981:4: (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )*
                while True:
                    alt149 = 2
                    LA149_0 = input.LA(1)
                    if (LA149_0 == self.RULE_INT):
                        LA149_1 = input.LA(2)
                        if (LA149_1 == 37):
                            alt149 = 1
                        elif (LA149_1 == self.RULE_ID):
                            LA149_2 = input.LA(3)
                            if (LA149_2 == 37):
                                alt149 = 1
                    elif (LA149_0 == self.RULE_ID):
                        LA149_2 = input.LA(2)
                        if (LA149_2 == 37):
                            alt149 = 1
                    if alt149 == 1:
                        #  InternalLF.g:5982:5: this_IPV6Seg_2= ruleIPV6Seg kw= ':'
                        newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_1_1_0())
                        pushFollow(FOLLOW_83)
                        this_IPV6Seg_2 = self.ruleIPV6Seg()
                        state._fsp -= 1
                        current.merge(this_IPV6Seg_2)
                        afterParserOrEnumRuleCall()
                        kw = match(input, 37, FOLLOW_105)
                        current.merge(kw)
                        newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_1_1_1())
                    else:
                    if not ((True)):
                        break
                newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_1_2())
                pushFollow(FOLLOW_2)
                this_IPV6Seg_4 = self.ruleIPV6Seg()
                state._fsp -= 1
                current.merge(this_IPV6Seg_4)
                afterParserOrEnumRuleCall()
            elif alt159 == 3:
                #  InternalLF.g:6010:3: ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? )
                #  InternalLF.g:6010:3: ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? )
                #  InternalLF.g:6011:4: (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )?
                #  InternalLF.g:6011:4: (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+
                cnt151 = 0
                while True:
                    alt151 = 2
                    LA151_0 = input.LA(1)
                    if (LA151_0 == self.RULE_INT):
                        LA151_1 = input.LA(2)
                        if (LA151_1 == self.RULE_ID):
                            LA151_2 = input.LA(3)
                            if (LA151_2 == 37 or LA151_2 == 67):
                                alt151 = 1
                        elif (LA151_1 == 37 or LA151_1 == 67):
                            alt151 = 1
                    elif (LA151_0 == self.RULE_ID):
                        LA151_2 = input.LA(2)
                        if (LA151_2 == 37 or LA151_2 == 67):
                            alt151 = 1
                    if alt151 == 1:
                        #  InternalLF.g:6012:5: this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' )
                        newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_2_0_0())
                        pushFollow(FOLLOW_106)
                        this_IPV6Seg_5 = self.ruleIPV6Seg()
                        state._fsp -= 1
                        current.merge(this_IPV6Seg_5)
                        afterParserOrEnumRuleCall()
                        #  InternalLF.g:6022:5: (kw= ':' | kw= '::' )
                        alt150 = 2
                        LA150_0 = input.LA(1)
                        if (LA150_0 == 37):
                            alt150 = 1
                        elif (LA150_0 == 67):
                            alt150 = 2
                        else:
                            nvae = NoViableAltException("", 150, 0, input)
                            raise nvae
                        if alt150 == 1:
                            #  InternalLF.g:6023:6: kw= ':'
                            kw = match(input, 37, FOLLOW_107)
                            current.merge(kw)
                            newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_2_0_1_0())
                        elif alt150 == 2:
                            #  InternalLF.g:6029:6: kw= '::'
                            kw = match(input, 67, FOLLOW_107)
                            current.merge(kw)
                            newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_2_0_1_1())
                    else:
                        if cnt151 >= 1:
                        eee = EarlyExitException(151, input)
                        raise eee
                    cnt151 += 1
                    if not ((True)):
                        break
                #  InternalLF.g:6036:4: (this_IPV6Seg_8= ruleIPV6Seg )?
                alt152 = 2
                LA152_0 = input.LA(1)
                if (LA152_0 == self.RULE_ID or LA152_0 == self.RULE_INT):
                    alt152 = 1
                if alt152 == 1:
                    #  InternalLF.g:6037:5: this_IPV6Seg_8= ruleIPV6Seg
                    newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_2_1())
                    pushFollow(FOLLOW_2)
                    this_IPV6Seg_8 = self.ruleIPV6Seg()
                    state._fsp -= 1
                    current.merge(this_IPV6Seg_8)
                    afterParserOrEnumRuleCall()
            elif alt159 == 4:
                #  InternalLF.g:6050:3: (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ )
                #  InternalLF.g:6050:3: (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ )
                #  InternalLF.g:6051:4: this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+
                this_ID_9 = match(input, self.RULE_ID, FOLLOW_108)
                current.merge(this_ID_9)
                newLeafNode(this_ID_9, self.grammarAccess.getIPV6AddrAccess().getIDTerminalRuleCall_3_0())
                kw = match(input, 67, FOLLOW_105)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_3_1())
                newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_3_2())
                pushFollow(FOLLOW_109)
                this_IPV6Seg_11 = self.ruleIPV6Seg()
                state._fsp -= 1
                current.merge(this_IPV6Seg_11)
                afterParserOrEnumRuleCall()
                #  InternalLF.g:6073:4: (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )*
                while True:
                    alt153 = 2
                    LA153_0 = input.LA(1)
                    if (LA153_0 == 37):
                        alt153 = 1
                    if alt153 == 1:
                        #  InternalLF.g:6074:5: kw= ':' this_IPV6Seg_13= ruleIPV6Seg
                        kw = match(input, 37, FOLLOW_105)
                        current.merge(kw)
                        newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_3_3_0())
                        newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_3_3_1())
                        pushFollow(FOLLOW_109)
                        this_IPV6Seg_13 = self.ruleIPV6Seg()
                        state._fsp -= 1
                        current.merge(this_IPV6Seg_13)
                        afterParserOrEnumRuleCall()
                    else:
                    if not ((True)):
                        break
                kw = match(input, 70, FOLLOW_105)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getPercentSignKeyword_3_4())
                #  InternalLF.g:6095:4: (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+
                cnt154 = 0
                while True:
                    alt154 = 3
                    LA154_0 = input.LA(1)
                    if (LA154_0 == self.RULE_INT):
                        alt154 = 1
                    elif (LA154_0 == self.RULE_ID):
                        alt154 = 2
                    if alt154 == 1:
                        #  InternalLF.g:6096:5: this_INT_15= RULE_INT
                        this_INT_15 = match(input, self.RULE_INT, FOLLOW_107)
                        current.merge(this_INT_15)
                        newLeafNode(this_INT_15, self.grammarAccess.getIPV6AddrAccess().getINTTerminalRuleCall_3_5_0())
                    elif alt154 == 2:
                        #  InternalLF.g:6104:5: this_ID_16= RULE_ID
                        this_ID_16 = match(input, self.RULE_ID, FOLLOW_107)
                        current.merge(this_ID_16)
                        newLeafNode(this_ID_16, self.grammarAccess.getIPV6AddrAccess().getIDTerminalRuleCall_3_5_1())
                    else:
                        if cnt154 >= 1:
                        eee = EarlyExitException(154, input)
                        raise eee
                    cnt154 += 1
                    if not ((True)):
                        break
            elif alt159 == 5:
                #  InternalLF.g:6114:3: (kw= '::' this_IPV4Addr_18= ruleIPV4Addr )
                #  InternalLF.g:6114:3: (kw= '::' this_IPV4Addr_18= ruleIPV4Addr )
                #  InternalLF.g:6115:4: kw= '::' this_IPV4Addr_18= ruleIPV4Addr
                kw = match(input, 67, FOLLOW_99)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_4_0())
                newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV4AddrParserRuleCall_4_1())
                pushFollow(FOLLOW_2)
                this_IPV4Addr_18 = self.ruleIPV4Addr()
                state._fsp -= 1
                current.merge(this_IPV4Addr_18)
                afterParserOrEnumRuleCall()
            elif alt159 == 6:
                #  InternalLF.g:6132:3: (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr )
                #  InternalLF.g:6132:3: (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr )
                #  InternalLF.g:6133:4: kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr
                kw = match(input, 67, FOLLOW_5)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_5_0())
                this_ID_20 = match(input, self.RULE_ID, FOLLOW_83)
                current.merge(this_ID_20)
                newLeafNode(this_ID_20, self.grammarAccess.getIPV6AddrAccess().getIDTerminalRuleCall_5_1())
                kw = match(input, 37, FOLLOW_99)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_5_2())
                #  InternalLF.g:6150:4: (this_INT_22= RULE_INT kw= ':' )?
                alt155 = 2
                LA155_0 = input.LA(1)
                if (LA155_0 == self.RULE_INT):
                    LA155_1 = input.LA(2)
                    if (LA155_1 == 37):
                        alt155 = 1
                if alt155 == 1:
                    #  InternalLF.g:6151:5: this_INT_22= RULE_INT kw= ':'
                    this_INT_22 = match(input, self.RULE_INT, FOLLOW_83)
                    current.merge(this_INT_22)
                    newLeafNode(this_INT_22, self.grammarAccess.getIPV6AddrAccess().getINTTerminalRuleCall_5_3_0())
                    kw = match(input, 37, FOLLOW_99)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_5_3_1())
                newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV4AddrParserRuleCall_5_4())
                pushFollow(FOLLOW_2)
                this_IPV4Addr_24 = self.ruleIPV4Addr()
                state._fsp -= 1
                current.merge(this_IPV4Addr_24)
                afterParserOrEnumRuleCall()
            elif alt159 == 7:
                #  InternalLF.g:6176:3: ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr )
                #  InternalLF.g:6176:3: ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr )
                #  InternalLF.g:6177:4: ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr
                #  InternalLF.g:6177:4: ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) )
                alt158 = 2
                alt158 = dfa158.predict(input)
                if alt158 == 1:
                    #  InternalLF.g:6178:5: (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' )
                    #  InternalLF.g:6178:5: (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' )
                    #  InternalLF.g:6179:6: this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::'
                    newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_0_0())
                    pushFollow(FOLLOW_106)
                    this_IPV6Seg_25 = self.ruleIPV6Seg()
                    state._fsp -= 1
                    current.merge(this_IPV6Seg_25)
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:6189:6: (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )*
                    while True:
                        alt156 = 2
                        LA156_0 = input.LA(1)
                        if (LA156_0 == 37):
                            alt156 = 1
                        if alt156 == 1:
                            #  InternalLF.g:6190:7: kw= ':' this_IPV6Seg_27= ruleIPV6Seg
                            kw = match(input, 37, FOLLOW_105)
                            current.merge(kw)
                            newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_6_0_0_1_0())
                            newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_0_1_1())
                            pushFollow(FOLLOW_106)
                            this_IPV6Seg_27 = self.ruleIPV6Seg()
                            state._fsp -= 1
                            current.merge(this_IPV6Seg_27)
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                    kw = match(input, 67, FOLLOW_99)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonColonKeyword_6_0_0_2())
                elif alt158 == 2:
                    #  InternalLF.g:6213:5: ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' )
                    #  InternalLF.g:6213:5: ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' )
                    #  InternalLF.g:6214:6: (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':'
                    #  InternalLF.g:6214:6: (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* )
                    #  InternalLF.g:6215:7: this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )*
                    newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_1_0_0())
                    pushFollow(FOLLOW_83)
                    this_IPV6Seg_29 = self.ruleIPV6Seg()
                    state._fsp -= 1
                    current.merge(this_IPV6Seg_29)
                    afterParserOrEnumRuleCall()
                    #  InternalLF.g:6225:7: (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )*
                    while True:
                        alt157 = 2
                        LA157_0 = input.LA(1)
                        if (LA157_0 == 37):
                            LA157_1 = input.LA(2)
                            if (LA157_1 == self.RULE_INT):
                                LA157_2 = input.LA(3)
                                if (LA157_2 == self.RULE_ID or LA157_2 == 37):
                                    alt157 = 1
                            elif (LA157_1 == self.RULE_ID):
                                alt157 = 1
                        if alt157 == 1:
                            #  InternalLF.g:6226:8: kw= ':' this_IPV6Seg_31= ruleIPV6Seg
                            kw = match(input, 37, FOLLOW_105)
                            current.merge(kw)
                            newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_6_0_1_0_1_0())
                            newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV6SegParserRuleCall_6_0_1_0_1_1())
                            pushFollow(FOLLOW_83)
                            this_IPV6Seg_31 = self.ruleIPV6Seg()
                            state._fsp -= 1
                            current.merge(this_IPV6Seg_31)
                            afterParserOrEnumRuleCall()
                        else:
                        if not ((True)):
                            break
                    kw = match(input, 37, FOLLOW_99)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getIPV6AddrAccess().getColonKeyword_6_0_1_1())
                newCompositeNode(self.grammarAccess.getIPV6AddrAccess().getIPV4AddrParserRuleCall_6_1())
                pushFollow(FOLLOW_2)
                this_IPV4Addr_33 = self.ruleIPV4Addr()
                state._fsp -= 1
                current.merge(this_IPV4Addr_33)
                afterParserOrEnumRuleCall()
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleIPV6Addr"
    #  $ANTLR start "entryRuleSignedFloat"
    #  InternalLF.g:6265:1: entryRuleSignedFloat returns [String current=null] : iv_ruleSignedFloat= ruleSignedFloat EOF ;
    def entryRuleSignedFloat(self):
        """ generated source for method entryRuleSignedFloat """
        current = None
        iv_ruleSignedFloat = None
        try:
            #  InternalLF.g:6265:51: (iv_ruleSignedFloat= ruleSignedFloat EOF )
            #  InternalLF.g:6266:2: iv_ruleSignedFloat= ruleSignedFloat EOF
            newCompositeNode(self.grammarAccess.getSignedFloatRule())
            pushFollow(FOLLOW_1)
            iv_ruleSignedFloat = ruleSignedFloat()
            state._fsp -= 1
            current = iv_ruleSignedFloat.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleSignedFloat"
    #  $ANTLR start "ruleSignedFloat"
    #  InternalLF.g:6272:1: ruleSignedFloat returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : ( (this_SignedInt_0= ruleSignedInt | kw= '-' )? kw= '.' (this_INT_3= RULE_INT | this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) ) ;
    def ruleSignedFloat(self):
        """ generated source for method ruleSignedFloat """
        current = AntlrDatatypeRuleToken()
        kw = None
        this_INT_3 = None
        this_FLOAT_EXP_SUFFIX_4 = None
        this_SignedInt_0 = None
        enterRule()
        try:
            #  InternalLF.g:6278:2: ( ( (this_SignedInt_0= ruleSignedInt | kw= '-' )? kw= '.' (this_INT_3= RULE_INT | this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) ) )
            #  InternalLF.g:6279:2: ( (this_SignedInt_0= ruleSignedInt | kw= '-' )? kw= '.' (this_INT_3= RULE_INT | this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) )
            #  InternalLF.g:6279:2: ( (this_SignedInt_0= ruleSignedInt | kw= '-' )? kw= '.' (this_INT_3= RULE_INT | this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX ) )
            #  InternalLF.g:6280:3: (this_SignedInt_0= ruleSignedInt | kw= '-' )? kw= '.' (this_INT_3= RULE_INT | this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX )
            #  InternalLF.g:6280:3: (this_SignedInt_0= ruleSignedInt | kw= '-' )?
            alt160 = 3
            LA160_0 = input.LA(1)
            if ((LA160_0 >= self.RULE_INT and LA160_0 <= self.RULE_NEGINT)):
                alt160 = 1
            elif (LA160_0 == 69):
                alt160 = 2
            if alt160 == 1:
                #  InternalLF.g:6281:4: this_SignedInt_0= ruleSignedInt
                newCompositeNode(self.grammarAccess.getSignedFloatAccess().getSignedIntParserRuleCall_0_0())
                pushFollow(FOLLOW_87)
                this_SignedInt_0 = self.ruleSignedInt()
                state._fsp -= 1
                current.merge(this_SignedInt_0)
                afterParserOrEnumRuleCall()
            elif alt160 == 2:
                #  InternalLF.g:6292:4: kw= '-'
                kw = match(input, 69, FOLLOW_87)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getSignedFloatAccess().getHyphenMinusKeyword_0_1())
            kw = match(input, 62, FOLLOW_110)
            current.merge(kw)
            newLeafNode(kw, self.grammarAccess.getSignedFloatAccess().getFullStopKeyword_1())
            #  InternalLF.g:6303:3: (this_INT_3= RULE_INT | this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX )
            alt161 = 2
            LA161_0 = input.LA(1)
            if (LA161_0 == self.RULE_INT):
                alt161 = 1
            elif (LA161_0 == self.RULE_FLOAT_EXP_SUFFIX):
                alt161 = 2
            else:
                nvae = NoViableAltException("", 161, 0, input)
                raise nvae
            if alt161 == 1:
                #  InternalLF.g:6304:4: this_INT_3= RULE_INT
                this_INT_3 = match(input, self.RULE_INT, FOLLOW_2)
                current.merge(this_INT_3)
                newLeafNode(this_INT_3, self.grammarAccess.getSignedFloatAccess().getINTTerminalRuleCall_2_0())
            elif alt161 == 2:
                #  InternalLF.g:6312:4: this_FLOAT_EXP_SUFFIX_4= RULE_FLOAT_EXP_SUFFIX
                this_FLOAT_EXP_SUFFIX_4 = match(input, self.RULE_FLOAT_EXP_SUFFIX, FOLLOW_2)
                current.merge(this_FLOAT_EXP_SUFFIX_4)
                newLeafNode(this_FLOAT_EXP_SUFFIX_4, self.grammarAccess.getSignedFloatAccess().getFLOAT_EXP_SUFFIXTerminalRuleCall_2_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleSignedFloat"
    #  $ANTLR start "entryRuleCode"
    #  InternalLF.g:6324:1: entryRuleCode returns [EObject current=null] : iv_ruleCode= ruleCode EOF ;
    def entryRuleCode(self):
        """ generated source for method entryRuleCode """
        current = None
        iv_ruleCode = None
        try:
            #  InternalLF.g:6324:45: (iv_ruleCode= ruleCode EOF )
            #  InternalLF.g:6325:2: iv_ruleCode= ruleCode EOF
            newCompositeNode(self.grammarAccess.getCodeRule())
            pushFollow(FOLLOW_1)
            iv_ruleCode = ruleCode()
            state._fsp -= 1
            current = iv_ruleCode
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleCode"
    #  $ANTLR start "ruleCode"
    #  InternalLF.g:6331:1: ruleCode returns [EObject current=null] : ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' ) ;
    def ruleCode(self):
        """ generated source for method ruleCode """
        current = None
        otherlv_1 = None
        otherlv_3 = None
        lv_body_2_0 = None
        enterRule()
        try:
            #  InternalLF.g:6337:2: ( ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' ) )
            #  InternalLF.g:6338:2: ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' )
            #  InternalLF.g:6338:2: ( () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}' )
            #  InternalLF.g:6339:3: () otherlv_1= '{=' ( (lv_body_2_0= ruleBody ) ) otherlv_3= '=}'
            #  InternalLF.g:6339:3: ()
            #  InternalLF.g:6340:4: 
            current = forceCreateModelElement(self.grammarAccess.getCodeAccess().getCodeAction_0(), current)
            otherlv_1 = match(input, 71, FOLLOW_111)
            newLeafNode(otherlv_1, self.grammarAccess.getCodeAccess().getLeftCurlyBracketEqualsSignKeyword_1())
            #  InternalLF.g:6350:3: ( (lv_body_2_0= ruleBody ) )
            #  InternalLF.g:6351:4: (lv_body_2_0= ruleBody )
            #  InternalLF.g:6351:4: (lv_body_2_0= ruleBody )
            #  InternalLF.g:6352:5: lv_body_2_0= ruleBody
            newCompositeNode(self.grammarAccess.getCodeAccess().getBodyBodyParserRuleCall_2_0())
            pushFollow(FOLLOW_112)
            lv_body_2_0 = ruleBody()
            state._fsp -= 1
            if current == None:
                current = createModelElementForParent(self.grammarAccess.getCodeRule())
            set(current, "body", lv_body_2_0, "org.lflang.LF.Body")
            afterParserOrEnumRuleCall()
            otherlv_3 = match(input, 72, FOLLOW_2)
            newLeafNode(otherlv_3, self.grammarAccess.getCodeAccess().getEqualsSignRightCurlyBracketKeyword_3())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleCode"
    #  $ANTLR start "entryRuleFSName"
    #  InternalLF.g:6377:1: entryRuleFSName returns [String current=null] : iv_ruleFSName= ruleFSName EOF ;
    def entryRuleFSName(self):
        """ generated source for method entryRuleFSName """
        current = None
        iv_ruleFSName = None
        try:
            #  InternalLF.g:6377:46: (iv_ruleFSName= ruleFSName EOF )
            #  InternalLF.g:6378:2: iv_ruleFSName= ruleFSName EOF
            newCompositeNode(self.grammarAccess.getFSNameRule())
            pushFollow(FOLLOW_1)
            iv_ruleFSName = ruleFSName()
            state._fsp -= 1
            current = iv_ruleFSName.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleFSName"
    #  $ANTLR start "ruleFSName"
    #  InternalLF.g:6384:1: ruleFSName returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID | kw= '.' | kw= '_' )+ ;
    def ruleFSName(self):
        """ generated source for method ruleFSName """
        current = AntlrDatatypeRuleToken()
        this_ID_0 = None
        kw = None
        enterRule()
        try:
            #  InternalLF.g:6390:2: ( (this_ID_0= RULE_ID | kw= '.' | kw= '_' )+ )
            #  InternalLF.g:6391:2: (this_ID_0= RULE_ID | kw= '.' | kw= '_' )+
            #  InternalLF.g:6391:2: (this_ID_0= RULE_ID | kw= '.' | kw= '_' )+
            cnt162 = 0
            while True:
                alt162 = 4
                if input.LA(1) == self.RULE_ID:
                    alt162 = 1
                elif input.LA(1) == 62:
                    alt162 = 2
                elif input.LA(1) == 73:
                    alt162 = 3
                if alt162 == 1:
                    #  InternalLF.g:6392:3: this_ID_0= RULE_ID
                    this_ID_0 = match(input, self.RULE_ID, FOLLOW_113)
                    current.merge(this_ID_0)
                    newLeafNode(this_ID_0, self.grammarAccess.getFSNameAccess().getIDTerminalRuleCall_0())
                elif alt162 == 2:
                    #  InternalLF.g:6400:3: kw= '.'
                    kw = match(input, 62, FOLLOW_113)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getFSNameAccess().getFullStopKeyword_1())
                elif alt162 == 3:
                    #  InternalLF.g:6406:3: kw= '_'
                    kw = match(input, 73, FOLLOW_113)
                    current.merge(kw)
                    newLeafNode(kw, self.grammarAccess.getFSNameAccess().get_Keyword_2())
                else:
                    if cnt162 >= 1:
                    eee = EarlyExitException(162, input)
                    raise eee
                cnt162 += 1
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleFSName"
    #  $ANTLR start "entryRulePath"
    #  InternalLF.g:6415:1: entryRulePath returns [String current=null] : iv_rulePath= rulePath EOF ;
    def entryRulePath(self):
        """ generated source for method entryRulePath """
        current = None
        iv_rulePath = None
        try:
            #  InternalLF.g:6415:44: (iv_rulePath= rulePath EOF )
            #  InternalLF.g:6416:2: iv_rulePath= rulePath EOF
            newCompositeNode(self.grammarAccess.getPathRule())
            pushFollow(FOLLOW_1)
            iv_rulePath = rulePath()
            state._fsp -= 1
            current = iv_rulePath.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRulePath"
    #  $ANTLR start "rulePath"
    #  InternalLF.g:6422:1: rulePath returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' | kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName )* ) ;
    def rulePath(self):
        """ generated source for method rulePath """
        current = AntlrDatatypeRuleToken()
        kw = None
        this_FSName_0 = None
        this_FSName_4 = None
        this_FSName_7 = None
        enterRule()
        try:
            #  InternalLF.g:6428:2: ( ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' | kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName )* ) )
            #  InternalLF.g:6429:2: ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' | kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName )* )
            #  InternalLF.g:6429:2: ( (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' | kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName )* )
            #  InternalLF.g:6430:3: (this_FSName_0= ruleFSName kw= ':\\\\' )? (kw= '\\\\' | kw= '/' )? this_FSName_4= ruleFSName ( (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName )*
            #  InternalLF.g:6430:3: (this_FSName_0= ruleFSName kw= ':\\\\' )?
            alt163 = 2
            alt163 = dfa163.predict(input)
            if alt163 == 1:
                #  InternalLF.g:6431:4: this_FSName_0= ruleFSName kw= ':\\\\'
                newCompositeNode(self.grammarAccess.getPathAccess().getFSNameParserRuleCall_0_0())
                pushFollow(FOLLOW_114)
                this_FSName_0 = self.ruleFSName()
                state._fsp -= 1
                current.merge(this_FSName_0)
                afterParserOrEnumRuleCall()
                kw = match(input, 74, FOLLOW_115)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getPathAccess().getColonReverseSolidusKeyword_0_1())
            #  InternalLF.g:6447:3: (kw= '\\\\' | kw= '/' )?
            alt164 = 3
            LA164_0 = input.LA(1)
            if (LA164_0 == 75):
                alt164 = 1
            elif (LA164_0 == 76):
                alt164 = 2
            if alt164 == 1:
                #  InternalLF.g:6448:4: kw= '\\\\'
                kw = match(input, 75, FOLLOW_116)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getPathAccess().getBackslashKeyword_1_0())
            elif alt164 == 2:
                #  InternalLF.g:6454:4: kw= '/'
                kw = match(input, 76, FOLLOW_116)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getPathAccess().getSolidusKeyword_1_1())
            newCompositeNode(self.grammarAccess.getPathAccess().getFSNameParserRuleCall_2())
            pushFollow(FOLLOW_117)
            this_FSName_4 = self.ruleFSName()
            state._fsp -= 1
            current.merge(this_FSName_4)
            afterParserOrEnumRuleCall()
            #  InternalLF.g:6470:3: ( (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName )*
            while True:
                alt166 = 2
                LA166_0 = input.LA(1)
                if ((LA166_0 >= 75 and LA166_0 <= 76)):
                    alt166 = 1
                if alt166 == 1:
                    #  InternalLF.g:6471:4: (kw= '\\\\' | kw= '/' ) this_FSName_7= ruleFSName
                    #  InternalLF.g:6471:4: (kw= '\\\\' | kw= '/' )
                    alt165 = 2
                    LA165_0 = input.LA(1)
                    if (LA165_0 == 75):
                        alt165 = 1
                    elif (LA165_0 == 76):
                        alt165 = 2
                    else:
                        nvae = NoViableAltException("", 165, 0, input)
                        raise nvae
                    if alt165 == 1:
                        #  InternalLF.g:6472:5: kw= '\\\\'
                        kw = match(input, 75, FOLLOW_116)
                        current.merge(kw)
                        newLeafNode(kw, self.grammarAccess.getPathAccess().getBackslashKeyword_3_0_0())
                    elif alt165 == 2:
                        #  InternalLF.g:6478:5: kw= '/'
                        kw = match(input, 76, FOLLOW_116)
                        current.merge(kw)
                        newLeafNode(kw, self.grammarAccess.getPathAccess().getSolidusKeyword_3_0_1())
                    newCompositeNode(self.grammarAccess.getPathAccess().getFSNameParserRuleCall_3_1())
                    pushFollow(FOLLOW_117)
                    this_FSName_7 = self.ruleFSName()
                    state._fsp -= 1
                    current.merge(this_FSName_7)
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "rulePath"
    #  $ANTLR start "entryRuleTimeUnit"
    #  InternalLF.g:6499:1: entryRuleTimeUnit returns [String current=null] : iv_ruleTimeUnit= ruleTimeUnit EOF ;
    def entryRuleTimeUnit(self):
        """ generated source for method entryRuleTimeUnit """
        current = None
        iv_ruleTimeUnit = None
        try:
            #  InternalLF.g:6499:48: (iv_ruleTimeUnit= ruleTimeUnit EOF )
            #  InternalLF.g:6500:2: iv_ruleTimeUnit= ruleTimeUnit EOF
            newCompositeNode(self.grammarAccess.getTimeUnitRule())
            pushFollow(FOLLOW_1)
            iv_ruleTimeUnit = ruleTimeUnit()
            state._fsp -= 1
            current = iv_ruleTimeUnit.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleTimeUnit"
    #  $ANTLR start "ruleTimeUnit"
    #  InternalLF.g:6506:1: ruleTimeUnit returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : this_ID_0= RULE_ID ;
    def ruleTimeUnit(self):
        """ generated source for method ruleTimeUnit """
        current = AntlrDatatypeRuleToken()
        this_ID_0 = None
        enterRule()
        try:
            #  InternalLF.g:6512:2: (this_ID_0= RULE_ID )
            #  InternalLF.g:6513:2: this_ID_0= RULE_ID
            this_ID_0 = match(input, self.RULE_ID, FOLLOW_2)
            current.merge(this_ID_0)
            newLeafNode(this_ID_0, self.grammarAccess.getTimeUnitAccess().getIDTerminalRuleCall())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleTimeUnit"
    #  $ANTLR start "entryRuleBody"
    #  InternalLF.g:6523:1: entryRuleBody returns [String current=null] : iv_ruleBody= ruleBody EOF ;
    def entryRuleBody(self):
        """ generated source for method entryRuleBody """
        current = None
        iv_ruleBody = None
        try:
            #  InternalLF.g:6523:44: (iv_ruleBody= ruleBody EOF )
            #  InternalLF.g:6524:2: iv_ruleBody= ruleBody EOF
            newCompositeNode(self.grammarAccess.getBodyRule())
            pushFollow(FOLLOW_1)
            iv_ruleBody = ruleBody()
            state._fsp -= 1
            current = iv_ruleBody.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleBody"
    #  $ANTLR start "ruleBody"
    #  InternalLF.g:6530:1: ruleBody returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_Token_0= ruleToken )* ;
    def ruleBody(self):
        """ generated source for method ruleBody """
        current = AntlrDatatypeRuleToken()
        this_Token_0 = None
        enterRule()
        try:
            #  InternalLF.g:6536:2: ( (this_Token_0= ruleToken )* )
            #  InternalLF.g:6537:2: (this_Token_0= ruleToken )*
            #  InternalLF.g:6537:2: (this_Token_0= ruleToken )*
            while True:
                alt167 = 2
                LA167_0 = input.LA(1)
                if ((LA167_0 >= self.RULE_STRING and LA167_0 <= 30) or (LA167_0 >= 32 and LA167_0 <= 50) or (LA167_0 >= 52 and LA167_0 <= 55) or LA167_0 == 57 or (LA167_0 >= 59 and LA167_0 <= 65) or (LA167_0 >= 67 and LA167_0 <= 70) or (LA167_0 >= 73 and LA167_0 <= 84)):
                    alt167 = 1
                if alt167 == 1:
                    #  InternalLF.g:6538:3: this_Token_0= ruleToken
                    newCompositeNode(self.grammarAccess.getBodyAccess().getTokenParserRuleCall())
                    pushFollow(FOLLOW_118)
                    this_Token_0 = ruleToken()
                    state._fsp -= 1
                    current.merge(this_Token_0)
                    afterParserOrEnumRuleCall()
                else:
                if not ((True)):
                    break
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleBody"
    #  $ANTLR start "entryRuleToken"
    #  InternalLF.g:6552:1: entryRuleToken returns [String current=null] : iv_ruleToken= ruleToken EOF ;
    def entryRuleToken(self):
        """ generated source for method entryRuleToken """
        current = None
        iv_ruleToken = None
        try:
            #  InternalLF.g:6552:45: (iv_ruleToken= ruleToken EOF )
            #  InternalLF.g:6553:2: iv_ruleToken= ruleToken EOF
            newCompositeNode(self.grammarAccess.getTokenRule())
            pushFollow(FOLLOW_1)
            iv_ruleToken = ruleToken()
            state._fsp -= 1
            current = iv_ruleToken.getText()
            match(input, self.EOF, FOLLOW_2)
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "entryRuleToken"
    #  $ANTLR start "ruleToken"
    #  InternalLF.g:6559:1: ruleToken returns [AntlrDatatypeRuleToken current=new AntlrDatatypeRuleToken()] : (this_ID_0= RULE_ID | this_INT_1= RULE_INT | this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX | this_LT_ANNOT_3= RULE_LT_ANNOT | this_STRING_4= RULE_STRING | this_CHAR_LIT_5= RULE_CHAR_LIT | this_ML_COMMENT_6= RULE_ML_COMMENT | this_SL_COMMENT_7= RULE_SL_COMMENT | this_WS_8= RULE_WS | this_ANY_OTHER_9= RULE_ANY_OTHER | kw= 'target' | kw= 'import' | kw= 'main' | kw= 'realtime' | kw= 'reactor' | kw= 'state' | kw= 'time' | kw= 'mutable' | kw= 'input' | kw= 'output' | kw= 'timer' | kw= 'action' | kw= 'reaction' | kw= 'startup' | kw= 'shutdown' | kw= 'after' | kw= 'deadline' | kw= 'mutation' | kw= 'preamble' | kw= 'new' | kw= 'federated' | kw= 'at' | kw= 'as' | kw= 'from' | kw= 'widthof' | kw= 'const' | kw= 'method' | kw= 'interleaved' | kw= 'mode' | kw= 'initial' | kw= 'reset' | kw= 'history' | this_NEGINT_42= RULE_NEGINT | this_TRUE_43= RULE_TRUE | this_FALSE_44= RULE_FALSE | kw= 'logical' | kw= 'physical' | kw= 'private' | kw= 'public' | kw= '(' | kw= ')' | kw= '{' | kw= '}' | kw= '[' | kw= ']' | kw= '<' | kw= '>' | kw= ':' | kw= ';' | kw= ',' | kw= '.' | kw= '::' | kw= ':\\\\' | kw= '\\\\' | kw= '+' | kw= '-' | kw= '*' | kw= '/' | kw= '_' | kw= '->' | kw= '=' | kw= '%' | kw= '@' | kw= '\\'' ) ;
    def ruleToken(self):
        """ generated source for method ruleToken """
        current = AntlrDatatypeRuleToken()
        this_ID_0 = None
        this_INT_1 = None
        this_FLOAT_EXP_SUFFIX_2 = None
        this_LT_ANNOT_3 = None
        this_STRING_4 = None
        this_CHAR_LIT_5 = None
        this_ML_COMMENT_6 = None
        this_SL_COMMENT_7 = None
        this_WS_8 = None
        this_ANY_OTHER_9 = None
        kw = None
        this_NEGINT_42 = None
        this_TRUE_43 = None
        this_FALSE_44 = None
        enterRule()
        try:
            #  InternalLF.g:6565:2: ( (this_ID_0= RULE_ID | this_INT_1= RULE_INT | this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX | this_LT_ANNOT_3= RULE_LT_ANNOT | this_STRING_4= RULE_STRING | this_CHAR_LIT_5= RULE_CHAR_LIT | this_ML_COMMENT_6= RULE_ML_COMMENT | this_SL_COMMENT_7= RULE_SL_COMMENT | this_WS_8= RULE_WS | this_ANY_OTHER_9= RULE_ANY_OTHER | kw= 'target' | kw= 'import' | kw= 'main' | kw= 'realtime' | kw= 'reactor' | kw= 'state' | kw= 'time' | kw= 'mutable' | kw= 'input' | kw= 'output' | kw= 'timer' | kw= 'action' | kw= 'reaction' | kw= 'startup' | kw= 'shutdown' | kw= 'after' | kw= 'deadline' | kw= 'mutation' | kw= 'preamble' | kw= 'new' | kw= 'federated' | kw= 'at' | kw= 'as' | kw= 'from' | kw= 'widthof' | kw= 'const' | kw= 'method' | kw= 'interleaved' | kw= 'mode' | kw= 'initial' | kw= 'reset' | kw= 'history' | this_NEGINT_42= RULE_NEGINT | this_TRUE_43= RULE_TRUE | this_FALSE_44= RULE_FALSE | kw= 'logical' | kw= 'physical' | kw= 'private' | kw= 'public' | kw= '(' | kw= ')' | kw= '{' | kw= '}' | kw= '[' | kw= ']' | kw= '<' | kw= '>' | kw= ':' | kw= ';' | kw= ',' | kw= '.' | kw= '::' | kw= ':\\\\' | kw= '\\\\' | kw= '+' | kw= '-' | kw= '*' | kw= '/' | kw= '_' | kw= '->' | kw= '=' | kw= '%' | kw= '@' | kw= '\\'' ) )
            #  InternalLF.g:6566:2: (this_ID_0= RULE_ID | this_INT_1= RULE_INT | this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX | this_LT_ANNOT_3= RULE_LT_ANNOT | this_STRING_4= RULE_STRING | this_CHAR_LIT_5= RULE_CHAR_LIT | this_ML_COMMENT_6= RULE_ML_COMMENT | this_SL_COMMENT_7= RULE_SL_COMMENT | this_WS_8= RULE_WS | this_ANY_OTHER_9= RULE_ANY_OTHER | kw= 'target' | kw= 'import' | kw= 'main' | kw= 'realtime' | kw= 'reactor' | kw= 'state' | kw= 'time' | kw= 'mutable' | kw= 'input' | kw= 'output' | kw= 'timer' | kw= 'action' | kw= 'reaction' | kw= 'startup' | kw= 'shutdown' | kw= 'after' | kw= 'deadline' | kw= 'mutation' | kw= 'preamble' | kw= 'new' | kw= 'federated' | kw= 'at' | kw= 'as' | kw= 'from' | kw= 'widthof' | kw= 'const' | kw= 'method' | kw= 'interleaved' | kw= 'mode' | kw= 'initial' | kw= 'reset' | kw= 'history' | this_NEGINT_42= RULE_NEGINT | this_TRUE_43= RULE_TRUE | this_FALSE_44= RULE_FALSE | kw= 'logical' | kw= 'physical' | kw= 'private' | kw= 'public' | kw= '(' | kw= ')' | kw= '{' | kw= '}' | kw= '[' | kw= ']' | kw= '<' | kw= '>' | kw= ':' | kw= ';' | kw= ',' | kw= '.' | kw= '::' | kw= ':\\\\' | kw= '\\\\' | kw= '+' | kw= '-' | kw= '*' | kw= '/' | kw= '_' | kw= '->' | kw= '=' | kw= '%' | kw= '@' | kw= '\\'' )
            #  InternalLF.g:6566:2: (this_ID_0= RULE_ID | this_INT_1= RULE_INT | this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX | this_LT_ANNOT_3= RULE_LT_ANNOT | this_STRING_4= RULE_STRING | this_CHAR_LIT_5= RULE_CHAR_LIT | this_ML_COMMENT_6= RULE_ML_COMMENT | this_SL_COMMENT_7= RULE_SL_COMMENT | this_WS_8= RULE_WS | this_ANY_OTHER_9= RULE_ANY_OTHER | kw= 'target' | kw= 'import' | kw= 'main' | kw= 'realtime' | kw= 'reactor' | kw= 'state' | kw= 'time' | kw= 'mutable' | kw= 'input' | kw= 'output' | kw= 'timer' | kw= 'action' | kw= 'reaction' | kw= 'startup' | kw= 'shutdown' | kw= 'after' | kw= 'deadline' | kw= 'mutation' | kw= 'preamble' | kw= 'new' | kw= 'federated' | kw= 'at' | kw= 'as' | kw= 'from' | kw= 'widthof' | kw= 'const' | kw= 'method' | kw= 'interleaved' | kw= 'mode' | kw= 'initial' | kw= 'reset' | kw= 'history' | this_NEGINT_42= RULE_NEGINT | this_TRUE_43= RULE_TRUE | this_FALSE_44= RULE_FALSE | kw= 'logical' | kw= 'physical' | kw= 'private' | kw= 'public' | kw= '(' | kw= ')' | kw= '{' | kw= '}' | kw= '[' | kw= ']' | kw= '<' | kw= '>' | kw= ':' | kw= ';' | kw= ',' | kw= '.' | kw= '::' | kw= ':\\\\' | kw= '\\\\' | kw= '+' | kw= '-' | kw= '*' | kw= '/' | kw= '_' | kw= '->' | kw= '=' | kw= '%' | kw= '@' | kw= '\\'' )
            alt168 = 74
            if input.LA(1) == self.RULE_ID:
                alt168 = 1
            elif input.LA(1) == self.RULE_INT:
                alt168 = 2
            elif input.LA(1) == self.RULE_FLOAT_EXP_SUFFIX:
                alt168 = 3
            elif input.LA(1) == self.RULE_LT_ANNOT:
                alt168 = 4
            elif input.LA(1) == self.RULE_STRING:
                alt168 = 5
            elif input.LA(1) == self.RULE_CHAR_LIT:
                alt168 = 6
            elif input.LA(1) == self.RULE_ML_COMMENT:
                alt168 = 7
            elif input.LA(1) == self.RULE_SL_COMMENT:
                alt168 = 8
            elif input.LA(1) == self.RULE_WS:
                alt168 = 9
            elif input.LA(1) == self.RULE_ANY_OTHER:
                alt168 = 10
            elif input.LA(1) == 34:
                alt168 = 11
            elif input.LA(1) == 17:
                alt168 = 12
            elif input.LA(1) == 23:
                alt168 = 13
            elif input.LA(1) == 24:
                alt168 = 14
            elif input.LA(1) == 25:
                alt168 = 15
            elif input.LA(1) == 36:
                alt168 = 16
            elif input.LA(1) == 64:
                alt168 = 17
            elif input.LA(1) == 40:
                alt168 = 18
            elif input.LA(1) == 41:
                alt168 = 19
            elif input.LA(1) == 42:
                alt168 = 20
            elif input.LA(1) == 43:
                alt168 = 21
            elif input.LA(1) == 46:
                alt168 = 22
            elif input.LA(1) == 47:
                alt168 = 23
            elif input.LA(1) == 77:
                alt168 = 24
            elif input.LA(1) == 78:
                alt168 = 25
            elif input.LA(1) == 57:
                alt168 = 26
            elif input.LA(1) == 50:
                alt168 = 27
            elif input.LA(1) == 48:
                alt168 = 28
            elif input.LA(1) == 52:
                alt168 = 29
            elif input.LA(1) == 54:
                alt168 = 30
            elif input.LA(1) == 22:
                alt168 = 31
            elif input.LA(1) == 30:
                alt168 = 32
            elif input.LA(1) == 21:
                alt168 = 33
            elif input.LA(1) == 19:
                alt168 = 34
            elif input.LA(1) == 79:
                alt168 = 35
            elif input.LA(1) == 38:
                alt168 = 36
            elif input.LA(1) == 39:
                alt168 = 37
            elif input.LA(1) == 63:
                alt168 = 38
            elif input.LA(1) == 45:
                alt168 = 39
            elif input.LA(1) == 44:
                alt168 = 40
            elif input.LA(1) == 35:
                alt168 = 41
            elif input.LA(1) == 80:
                alt168 = 42
            elif input.LA(1) == self.RULE_NEGINT:
                alt168 = 43
            elif input.LA(1) == self.RULE_TRUE:
                alt168 = 44
            elif input.LA(1) == self.RULE_FALSE:
                alt168 = 45
            elif input.LA(1) == 81:
                alt168 = 46
            elif input.LA(1) == 68:
                alt168 = 47
            elif input.LA(1) == 82:
                alt168 = 48
            elif input.LA(1) == 83:
                alt168 = 49
            elif input.LA(1) == 28:
                alt168 = 50
            elif input.LA(1) == 29:
                alt168 = 51
            elif input.LA(1) == 32:
                alt168 = 52
            elif input.LA(1) == 33:
                alt168 = 53
            elif input.LA(1) == 60:
                alt168 = 54
            elif input.LA(1) == 61:
                alt168 = 55
            elif input.LA(1) == 26:
                alt168 = 56
            elif input.LA(1) == 27:
                alt168 = 57
            elif input.LA(1) == 37:
                alt168 = 58
            elif input.LA(1) == 20:
                alt168 = 59
            elif input.LA(1) == 18:
                alt168 = 60
            elif input.LA(1) == 62:
                alt168 = 61
            elif input.LA(1) == 67:
                alt168 = 62
            elif input.LA(1) == 74:
                alt168 = 63
            elif input.LA(1) == 75:
                alt168 = 64
            elif input.LA(1) == 55:
                alt168 = 65
            elif input.LA(1) == 69:
                alt168 = 66
            elif input.LA(1) == 65:
                alt168 = 67
            elif input.LA(1) == 76:
                alt168 = 68
            elif input.LA(1) == 73:
                alt168 = 69
            elif input.LA(1) == 49:
                alt168 = 70
            elif input.LA(1) == 53:
                alt168 = 71
            elif input.LA(1) == 70:
                alt168 = 72
            elif input.LA(1) == 59:
                alt168 = 73
            elif input.LA(1) == 84:
                alt168 = 74
            else:
                nvae = NoViableAltException("", 168, 0, input)
                raise nvae
            if alt168 == 1:
                #  InternalLF.g:6567:3: this_ID_0= RULE_ID
                this_ID_0 = match(input, self.RULE_ID, FOLLOW_2)
                current.merge(this_ID_0)
                newLeafNode(this_ID_0, self.grammarAccess.getTokenAccess().getIDTerminalRuleCall_0())
            elif alt168 == 2:
                #  InternalLF.g:6575:3: this_INT_1= RULE_INT
                this_INT_1 = match(input, self.RULE_INT, FOLLOW_2)
                current.merge(this_INT_1)
                newLeafNode(this_INT_1, self.grammarAccess.getTokenAccess().getINTTerminalRuleCall_1())
            elif alt168 == 3:
                #  InternalLF.g:6583:3: this_FLOAT_EXP_SUFFIX_2= RULE_FLOAT_EXP_SUFFIX
                this_FLOAT_EXP_SUFFIX_2 = match(input, self.RULE_FLOAT_EXP_SUFFIX, FOLLOW_2)
                current.merge(this_FLOAT_EXP_SUFFIX_2)
                newLeafNode(this_FLOAT_EXP_SUFFIX_2, self.grammarAccess.getTokenAccess().getFLOAT_EXP_SUFFIXTerminalRuleCall_2())
            elif alt168 == 4:
                #  InternalLF.g:6591:3: this_LT_ANNOT_3= RULE_LT_ANNOT
                this_LT_ANNOT_3 = match(input, self.RULE_LT_ANNOT, FOLLOW_2)
                current.merge(this_LT_ANNOT_3)
                newLeafNode(this_LT_ANNOT_3, self.grammarAccess.getTokenAccess().getLT_ANNOTTerminalRuleCall_3())
            elif alt168 == 5:
                #  InternalLF.g:6599:3: this_STRING_4= RULE_STRING
                this_STRING_4 = match(input, self.RULE_STRING, FOLLOW_2)
                current.merge(this_STRING_4)
                newLeafNode(this_STRING_4, self.grammarAccess.getTokenAccess().getSTRINGTerminalRuleCall_4())
            elif alt168 == 6:
                #  InternalLF.g:6607:3: this_CHAR_LIT_5= RULE_CHAR_LIT
                this_CHAR_LIT_5 = match(input, self.RULE_CHAR_LIT, FOLLOW_2)
                current.merge(this_CHAR_LIT_5)
                newLeafNode(this_CHAR_LIT_5, self.grammarAccess.getTokenAccess().getCHAR_LITTerminalRuleCall_5())
            elif alt168 == 7:
                #  InternalLF.g:6615:3: this_ML_COMMENT_6= RULE_ML_COMMENT
                this_ML_COMMENT_6 = match(input, self.RULE_ML_COMMENT, FOLLOW_2)
                current.merge(this_ML_COMMENT_6)
                newLeafNode(this_ML_COMMENT_6, self.grammarAccess.getTokenAccess().getML_COMMENTTerminalRuleCall_6())
            elif alt168 == 8:
                #  InternalLF.g:6623:3: this_SL_COMMENT_7= RULE_SL_COMMENT
                this_SL_COMMENT_7 = match(input, self.RULE_SL_COMMENT, FOLLOW_2)
                current.merge(this_SL_COMMENT_7)
                newLeafNode(this_SL_COMMENT_7, self.grammarAccess.getTokenAccess().getSL_COMMENTTerminalRuleCall_7())
            elif alt168 == 9:
                #  InternalLF.g:6631:3: this_WS_8= RULE_WS
                this_WS_8 = match(input, self.RULE_WS, FOLLOW_2)
                current.merge(this_WS_8)
                newLeafNode(this_WS_8, self.grammarAccess.getTokenAccess().getWSTerminalRuleCall_8())
            elif alt168 == 10:
                #  InternalLF.g:6639:3: this_ANY_OTHER_9= RULE_ANY_OTHER
                this_ANY_OTHER_9 = match(input, self.RULE_ANY_OTHER, FOLLOW_2)
                current.merge(this_ANY_OTHER_9)
                newLeafNode(this_ANY_OTHER_9, self.grammarAccess.getTokenAccess().getANY_OTHERTerminalRuleCall_9())
            elif alt168 == 11:
                #  InternalLF.g:6647:3: kw= 'target'
                kw = match(input, 34, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getTargetKeyword_10())
            elif alt168 == 12:
                #  InternalLF.g:6653:3: kw= 'import'
                kw = match(input, 17, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getImportKeyword_11())
            elif alt168 == 13:
                #  InternalLF.g:6659:3: kw= 'main'
                kw = match(input, 23, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getMainKeyword_12())
            elif alt168 == 14:
                #  InternalLF.g:6665:3: kw= 'realtime'
                kw = match(input, 24, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getRealtimeKeyword_13())
            elif alt168 == 15:
                #  InternalLF.g:6671:3: kw= 'reactor'
                kw = match(input, 25, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getReactorKeyword_14())
            elif alt168 == 16:
                #  InternalLF.g:6677:3: kw= 'state'
                kw = match(input, 36, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getStateKeyword_15())
            elif alt168 == 17:
                #  InternalLF.g:6683:3: kw= 'time'
                kw = match(input, 64, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getTimeKeyword_16())
            elif alt168 == 18:
                #  InternalLF.g:6689:3: kw= 'mutable'
                kw = match(input, 40, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getMutableKeyword_17())
            elif alt168 == 19:
                #  InternalLF.g:6695:3: kw= 'input'
                kw = match(input, 41, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getInputKeyword_18())
            elif alt168 == 20:
                #  InternalLF.g:6701:3: kw= 'output'
                kw = match(input, 42, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getOutputKeyword_19())
            elif alt168 == 21:
                #  InternalLF.g:6707:3: kw= 'timer'
                kw = match(input, 43, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getTimerKeyword_20())
            elif alt168 == 22:
                #  InternalLF.g:6713:3: kw= 'action'
                kw = match(input, 46, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getActionKeyword_21())
            elif alt168 == 23:
                #  InternalLF.g:6719:3: kw= 'reaction'
                kw = match(input, 47, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getReactionKeyword_22())
            elif alt168 == 24:
                #  InternalLF.g:6725:3: kw= 'startup'
                kw = match(input, 77, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getStartupKeyword_23())
            elif alt168 == 25:
                #  InternalLF.g:6731:3: kw= 'shutdown'
                kw = match(input, 78, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getShutdownKeyword_24())
            elif alt168 == 26:
                #  InternalLF.g:6737:3: kw= 'after'
                kw = match(input, 57, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getAfterKeyword_25())
            elif alt168 == 27:
                #  InternalLF.g:6743:3: kw= 'deadline'
                kw = match(input, 50, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getDeadlineKeyword_26())
            elif alt168 == 28:
                #  InternalLF.g:6749:3: kw= 'mutation'
                kw = match(input, 48, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getMutationKeyword_27())
            elif alt168 == 29:
                #  InternalLF.g:6755:3: kw= 'preamble'
                kw = match(input, 52, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getPreambleKeyword_28())
            elif alt168 == 30:
                #  InternalLF.g:6761:3: kw= 'new'
                kw = match(input, 54, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getNewKeyword_29())
            elif alt168 == 31:
                #  InternalLF.g:6767:3: kw= 'federated'
                kw = match(input, 22, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getFederatedKeyword_30())
            elif alt168 == 32:
                #  InternalLF.g:6773:3: kw= 'at'
                kw = match(input, 30, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getAtKeyword_31())
            elif alt168 == 33:
                #  InternalLF.g:6779:3: kw= 'as'
                kw = match(input, 21, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getAsKeyword_32())
            elif alt168 == 34:
                #  InternalLF.g:6785:3: kw= 'from'
                kw = match(input, 19, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getFromKeyword_33())
            elif alt168 == 35:
                #  InternalLF.g:6791:3: kw= 'widthof'
                kw = match(input, 79, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getWidthofKeyword_34())
            elif alt168 == 36:
                #  InternalLF.g:6797:3: kw= 'const'
                kw = match(input, 38, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getConstKeyword_35())
            elif alt168 == 37:
                #  InternalLF.g:6803:3: kw= 'method'
                kw = match(input, 39, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getMethodKeyword_36())
            elif alt168 == 38:
                #  InternalLF.g:6809:3: kw= 'interleaved'
                kw = match(input, 63, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getInterleavedKeyword_37())
            elif alt168 == 39:
                #  InternalLF.g:6815:3: kw= 'mode'
                kw = match(input, 45, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getModeKeyword_38())
            elif alt168 == 40:
                #  InternalLF.g:6821:3: kw= 'initial'
                kw = match(input, 44, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getInitialKeyword_39())
            elif alt168 == 41:
                #  InternalLF.g:6827:3: kw= 'reset'
                kw = match(input, 35, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getResetKeyword_40())
            elif alt168 == 42:
                #  InternalLF.g:6833:3: kw= 'history'
                kw = match(input, 80, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getHistoryKeyword_41())
            elif alt168 == 43:
                #  InternalLF.g:6839:3: this_NEGINT_42= RULE_NEGINT
                this_NEGINT_42 = match(input, self.RULE_NEGINT, FOLLOW_2)
                current.merge(this_NEGINT_42)
                newLeafNode(this_NEGINT_42, self.grammarAccess.getTokenAccess().getNEGINTTerminalRuleCall_42())
            elif alt168 == 44:
                #  InternalLF.g:6847:3: this_TRUE_43= RULE_TRUE
                this_TRUE_43 = match(input, self.RULE_TRUE, FOLLOW_2)
                current.merge(this_TRUE_43)
                newLeafNode(this_TRUE_43, self.grammarAccess.getTokenAccess().getTRUETerminalRuleCall_43())
            elif alt168 == 45:
                #  InternalLF.g:6855:3: this_FALSE_44= RULE_FALSE
                this_FALSE_44 = match(input, self.RULE_FALSE, FOLLOW_2)
                current.merge(this_FALSE_44)
                newLeafNode(this_FALSE_44, self.grammarAccess.getTokenAccess().getFALSETerminalRuleCall_44())
            elif alt168 == 46:
                #  InternalLF.g:6863:3: kw= 'logical'
                kw = match(input, 81, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getLogicalKeyword_45())
            elif alt168 == 47:
                #  InternalLF.g:6869:3: kw= 'physical'
                kw = match(input, 68, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getPhysicalKeyword_46())
            elif alt168 == 48:
                #  InternalLF.g:6875:3: kw= 'private'
                kw = match(input, 82, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getPrivateKeyword_47())
            elif alt168 == 49:
                #  InternalLF.g:6881:3: kw= 'public'
                kw = match(input, 83, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getPublicKeyword_48())
            elif alt168 == 50:
                #  InternalLF.g:6887:3: kw= '('
                kw = match(input, 28, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getLeftParenthesisKeyword_49())
            elif alt168 == 51:
                #  InternalLF.g:6893:3: kw= ')'
                kw = match(input, 29, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getRightParenthesisKeyword_50())
            elif alt168 == 52:
                #  InternalLF.g:6899:3: kw= '{'
                kw = match(input, 32, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getLeftCurlyBracketKeyword_51())
            elif alt168 == 53:
                #  InternalLF.g:6905:3: kw= '}'
                kw = match(input, 33, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getRightCurlyBracketKeyword_52())
            elif alt168 == 54:
                #  InternalLF.g:6911:3: kw= '['
                kw = match(input, 60, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getLeftSquareBracketKeyword_53())
            elif alt168 == 55:
                #  InternalLF.g:6917:3: kw= ']'
                kw = match(input, 61, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getRightSquareBracketKeyword_54())
            elif alt168 == 56:
                #  InternalLF.g:6923:3: kw= '<'
                kw = match(input, 26, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getLessThanSignKeyword_55())
            elif alt168 == 57:
                #  InternalLF.g:6929:3: kw= '>'
                kw = match(input, 27, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getGreaterThanSignKeyword_56())
            elif alt168 == 58:
                #  InternalLF.g:6935:3: kw= ':'
                kw = match(input, 37, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getColonKeyword_57())
            elif alt168 == 59:
                #  InternalLF.g:6941:3: kw= ';'
                kw = match(input, 20, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getSemicolonKeyword_58())
            elif alt168 == 60:
                #  InternalLF.g:6947:3: kw= ','
                kw = match(input, 18, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getCommaKeyword_59())
            elif alt168 == 61:
                #  InternalLF.g:6953:3: kw= '.'
                kw = match(input, 62, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getFullStopKeyword_60())
            elif alt168 == 62:
                #  InternalLF.g:6959:3: kw= '::'
                kw = match(input, 67, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getColonColonKeyword_61())
            elif alt168 == 63:
                #  InternalLF.g:6965:3: kw= ':\\\\'
                kw = match(input, 74, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getColonReverseSolidusKeyword_62())
            elif alt168 == 64:
                #  InternalLF.g:6971:3: kw= '\\\\'
                kw = match(input, 75, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getBackslashKeyword_63())
            elif alt168 == 65:
                #  InternalLF.g:6977:3: kw= '+'
                kw = match(input, 55, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getPlusSignKeyword_64())
            elif alt168 == 66:
                #  InternalLF.g:6983:3: kw= '-'
                kw = match(input, 69, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getHyphenMinusKeyword_65())
            elif alt168 == 67:
                #  InternalLF.g:6989:3: kw= '*'
                kw = match(input, 65, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getAsteriskKeyword_66())
            elif alt168 == 68:
                #  InternalLF.g:6995:3: kw= '/'
                kw = match(input, 76, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getSolidusKeyword_67())
            elif alt168 == 69:
                #  InternalLF.g:7001:3: kw= '_'
                kw = match(input, 73, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().get_Keyword_68())
            elif alt168 == 70:
                #  InternalLF.g:7007:3: kw= '->'
                kw = match(input, 49, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getHyphenMinusGreaterThanSignKeyword_69())
            elif alt168 == 71:
                #  InternalLF.g:7013:3: kw= '='
                kw = match(input, 53, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getEqualsSignKeyword_70())
            elif alt168 == 72:
                #  InternalLF.g:7019:3: kw= '%'
                kw = match(input, 70, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getPercentSignKeyword_71())
            elif alt168 == 73:
                #  InternalLF.g:7025:3: kw= '@'
                kw = match(input, 59, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getCommercialAtKeyword_72())
            elif alt168 == 74:
                #  InternalLF.g:7031:3: kw= '\\''
                kw = match(input, 84, FOLLOW_2)
                current.merge(kw)
                newLeafNode(kw, self.grammarAccess.getTokenAccess().getApostropheKeyword_73())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    #  $ANTLR end "ruleToken"
    #  $ANTLR start "ruleActionOrigin"
    #  InternalLF.g:7040:1: ruleActionOrigin returns [Enumerator current=null] : ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) ) ;
    def ruleActionOrigin(self):
        """ generated source for method ruleActionOrigin """
        current = None
        enumLiteral_0 = None
        enumLiteral_1 = None
        enumLiteral_2 = None
        enterRule()
        try:
            #  InternalLF.g:7046:2: ( ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) ) )
            #  InternalLF.g:7047:2: ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) )
            #  InternalLF.g:7047:2: ( (enumLiteral_0= 'NONE' ) | (enumLiteral_1= 'logical' ) | (enumLiteral_2= 'physical' ) )
            alt169 = 3
            if input.LA(1) == 85:
                alt169 = 1
            elif input.LA(1) == 81:
                alt169 = 2
            elif input.LA(1) == 68:
                alt169 = 3
            else:
                nvae = NoViableAltException("", 169, 0, input)
                raise nvae
            if alt169 == 1:
                #  InternalLF.g:7048:3: (enumLiteral_0= 'NONE' )
                #  InternalLF.g:7048:3: (enumLiteral_0= 'NONE' )
                #  InternalLF.g:7049:4: enumLiteral_0= 'NONE'
                enumLiteral_0 = match(input, 85, FOLLOW_2)
                current = self.grammarAccess.getActionOriginAccess().getNONEEnumLiteralDeclaration_0().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_0, self.grammarAccess.getActionOriginAccess().getNONEEnumLiteralDeclaration_0())
            elif alt169 == 2:
                enumLiteral_1 = match(input, 81, FOLLOW_2)
                current = self.grammarAccess.getActionOriginAccess().getLOGICALEnumLiteralDeclaration_1().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_1, self.grammarAccess.getActionOriginAccess().getLOGICALEnumLiteralDeclaration_1())
            elif alt169 == 3:
                enumLiteral_2 = match(input, 68, FOLLOW_2)
                current = self.grammarAccess.getActionOriginAccess().getPHYSICALEnumLiteralDeclaration_2().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_2, self.grammarAccess.getActionOriginAccess().getPHYSICALEnumLiteralDeclaration_2())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    def ruleVisibility(self):
        """ generated source for method ruleVisibility """
        current = None
        enumLiteral_0 = None
        enumLiteral_1 = None
        enumLiteral_2 = None
        enterRule()
        try:
            alt170 = 3
            if input.LA(1) == 85:
                alt170 = 1
            elif input.LA(1) == 82:
                alt170 = 2
            elif input.LA(1) == 83:
                alt170 = 3
            else:
                nvae = NoViableAltException("", 170, 0, input)
                raise nvae
            if alt170 == 1:
                enumLiteral_0 = match(input, 85, FOLLOW_2)
                current = self.grammarAccess.getVisibilityAccess().getNONEEnumLiteralDeclaration_0().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_0, self.grammarAccess.getVisibilityAccess().getNONEEnumLiteralDeclaration_0())
            elif alt170 == 2:
                enumLiteral_1 = match(input, 82, FOLLOW_2)
                current = self.grammarAccess.getVisibilityAccess().getPRIVATEEnumLiteralDeclaration_1().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_1, self.grammarAccess.getVisibilityAccess().getPRIVATEEnumLiteralDeclaration_1())
            elif alt170 == 3:
                enumLiteral_2 = match(input, 83, FOLLOW_2)
                current = self.grammarAccess.getVisibilityAccess().getPUBLICEnumLiteralDeclaration_2().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_2, self.grammarAccess.getVisibilityAccess().getPUBLICEnumLiteralDeclaration_2())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    def ruleBuiltinTrigger(self):
        """ generated source for method ruleBuiltinTrigger """
        current = None
        enumLiteral_0 = None
        enumLiteral_1 = None
        enumLiteral_2 = None
        enterRule()
        try:
            alt171 = 3
            if input.LA(1) == 77:
                alt171 = 1
            elif input.LA(1) == 78:
                alt171 = 2
            elif input.LA(1) == 35:
                alt171 = 3
            else:
                nvae = NoViableAltException("", 171, 0, input)
                raise nvae
            if alt171 == 1:
                enumLiteral_0 = match(input, 77, FOLLOW_2)
                current = self.grammarAccess.getBuiltinTriggerAccess().getSTARTUPEnumLiteralDeclaration_0().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_0, self.grammarAccess.getBuiltinTriggerAccess().getSTARTUPEnumLiteralDeclaration_0())
            elif alt171 == 2:
                enumLiteral_1 = match(input, 78, FOLLOW_2)
                current = self.grammarAccess.getBuiltinTriggerAccess().getSHUTDOWNEnumLiteralDeclaration_1().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_1, self.grammarAccess.getBuiltinTriggerAccess().getSHUTDOWNEnumLiteralDeclaration_1())
            elif alt171 == 3:
                enumLiteral_2 = match(input, 35, FOLLOW_2)
                current = self.grammarAccess.getBuiltinTriggerAccess().getRESETEnumLiteralDeclaration_2().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_2, self.grammarAccess.getBuiltinTriggerAccess().getRESETEnumLiteralDeclaration_2())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    def ruleModeTransition(self):
        """ generated source for method ruleModeTransition """
        current = None
        enumLiteral_0 = None
        enumLiteral_1 = None
        enterRule()
        try:
            alt172 = 2
            LA172_0 = input.LA(1)
            if (LA172_0 == 35):
                alt172 = 1
            elif (LA172_0 == 80):
                alt172 = 2
            else:
                nvae = NoViableAltException("", 172, 0, input)
                raise nvae
            if alt172 == 1:
                enumLiteral_0 = match(input, 35, FOLLOW_2)
                current = self.grammarAccess.getModeTransitionAccess().getRESETEnumLiteralDeclaration_0().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_0, self.grammarAccess.getModeTransitionAccess().getRESETEnumLiteralDeclaration_0())
            elif alt172 == 2:
                enumLiteral_1 = match(input, 80, FOLLOW_2)
                current = self.grammarAccess.getModeTransitionAccess().getHISTORYEnumLiteralDeclaration_1().getEnumLiteral().getInstance()
                newLeafNode(enumLiteral_1, self.grammarAccess.getModeTransitionAccess().getHISTORYEnumLiteralDeclaration_1())
            leaveRule()
        except RecognitionException as re:
            recover(input, re)
            appendSkippedTokens()
        finally:
        return current

    dfa18 = DFA18(self)
    dfa30 = DFA30(self)
    dfa54 = DFA54(self)
    dfa103 = DFA103(self)
    dfa121 = DFA121(self)
    dfa122 = DFA122(self)
    dfa137 = DFA137(self)
    dfa139 = DFA139(self)
    dfa159 = DFA159(self)
    dfa158 = DFA158(self)
    dfa163 = DFA163(self)
    dfa_1s = "\52\uffff"
    dfa_2s = "\1\5\1\uffff\1\56\1\uffff\1\5\6\uffff\1\22\3\uffff\1\34\1\uffff\1\4\1\65\5\22\1\76\1\10\1\43\2\4\2\22\1\65\5\22\1\76\1\10\1\4\2\22"
    dfa_3s = "\1\125\1\uffff\1\64\1\uffff\1\5\6\uffff\1\76\3\uffff\1\125\1\uffff\1\105\1\65\1\35\2\76\2\35\1\76\1\13\1\125\2\105\2\35\1\65\1\35\2\76\2\35\1\76\1\13\1\105\2\35"
    dfa_4s = "\1\uffff\1\14\1\uffff\1\1\1\uffff\1\2\1\3\1\4\1\5\1\6\1\7\1\uffff\1\11\1\12\1\13\1\uffff\1\10\31\uffff"
    dfa_5s = "\52\uffff}>"
    dfa_6s = ["\1\13\26\uffff\1\14\4\uffff\1\1\1\uffff\2\5\1\uffff\2\6\2\7\1\10\1\11\2\16\1\12\2\15\3\uffff\1\3\6\uffff\1\4\3\uffff\1\14\4\uffff\1\12\14\uffff\1\12\2\3\1\uffff\1\2", "", "\1\12\5\uffff\1\3", "", "\1\17", "", "", "", "", "", "", "\1\14\36\uffff\1\14\3\uffff\1\20\2\uffff\1\14\5\uffff\1\14", "", "", "", "\1\21\6\uffff\2\5\3\uffff\2\7\1\10\1\11\2\uffff\1\12\2\15\12\uffff\1\4\10\uffff\1\12\14\uffff\1\12\3\uffff\1\12", "", "\1\23\1\22\1\26\1\27\1\24\1\25\23\uffff\1\32\40\uffff\1\31\6\uffff\1\30", "\1\33", "\1\34\12\uffff\1\32", "\1\34\12\uffff\1\32\40\uffff\1\31", "\1\34\12\uffff\1\32\40\uffff\1\31", "\1\34\12\uffff\1\32", "\1\34\12\uffff\1\32", "\1\31", "\1\35\2\uffff\1\36", "\2\5\3\uffff\2\7\1\10\1\11\2\uffff\1\12\2\15\12\uffff\1\4\10\uffff\1\12\14\uffff\1\12\3\uffff\1\12", "\1\23\1\uffff\1\26\1\27\1\24\1\25\64\uffff\1\31\6\uffff\1\30", "\1\40\1\37\1\43\1\44\1\41\1\42\23\uffff\1\32\40\uffff\1\46\6\uffff\1\45", "\1\34\12\uffff\1\32", "\1\34\12\uffff\1\32", "\1\47", "\1\34\12\uffff\1\32", "\1\34\12\uffff\1\32\40\uffff\1\46", "\1\34\12\uffff\1\32\40\uffff\1\46", "\1\34\12\uffff\1\32", "\1\34\12\uffff\1\32", "\1\46", "\1\50\2\uffff\1\51", "\1\40\1\uffff\1\43\1\44\1\41\1\42\64\uffff\1\46\6\uffff\1\45", "\1\34\12\uffff\1\32", "\1\34\12\uffff\1\32"]
    dfa_1 = DFA.unpackEncodedString(dfa_1s)
    dfa_2 = DFA.unpackEncodedStringToUnsignedChars(dfa_2s)
    dfa_3 = DFA.unpackEncodedStringToUnsignedChars(dfa_3s)
    dfa_4 = DFA.unpackEncodedString(dfa_4s)
    dfa_5 = DFA.unpackEncodedString(dfa_5s)
    dfa_6 = unpackEncodedStringArray(dfa_6s)

    class DFA18(DFA):
        """ generated source for class DFA18 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA18, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 18
            self.eot = self.dfa_1
            self.eof = self.dfa_1
            self.min = self.dfa_2
            self.max = self.dfa_3
            self.accept = self.dfa_4
            self.special = self.dfa_5
            self.transition = self.dfa_6

        def getDescription(self):
            """ generated source for method getDescription """
            return "()* loopback of 628:3: ( ( (lv_preambles_25_0= rulePreamble ) ) | ( (lv_stateVars_26_0= ruleStateVar ) ) | ( (lv_methods_27_0= ruleMethod ) ) | ( (lv_inputs_28_0= ruleInput ) ) | ( (lv_outputs_29_0= ruleOutput ) ) | ( (lv_timers_30_0= ruleTimer ) ) | ( (lv_actions_31_0= ruleAction ) ) | ( (lv_instantiations_32_0= ruleInstantiation ) ) | ( (lv_connections_33_0= ruleConnection ) ) | ( (lv_reactions_34_0= ruleReaction ) ) | ( (lv_modes_35_0= ruleMode ) ) )*"

    dfa_7s = "\11\uffff"
    dfa_8s = "\1\3\6\uffff\1\5\1\uffff"
    dfa_9s = "\1\5\1\4\2\uffff\1\22\1\uffff\1\4\1\5\1\22"
    dfa_10s = "\1\125\1\107\2\uffff\1\76\1\uffff\1\107\1\125\1\76"
    dfa_11s = "\2\uffff\1\2\1\3\1\uffff\1\1\3\uffff"
    dfa_12s = "\11\uffff}>"
    dfa_13s = ["\1\3\16\uffff\1\3\7\uffff\1\1\3\uffff\1\2\1\3\1\uffff\2\3\1\uffff\13\3\3\uffff\1\3\6\uffff\1\3\3\uffff\1\3\4\uffff\1\3\14\uffff\3\3\1\uffff\1\3", "\1\5\1\4\5\5\22\uffff\1\5\40\uffff\1\5\1\3\5\uffff\1\5\1\uffff\1\5", "", "", "\1\6\12\uffff\1\7\40\uffff\1\3", "", "\1\5\1\10\5\5\63\uffff\1\5\1\3\5\uffff\1\5\1\uffff\1\5", "\1\5\16\uffff\1\5\7\uffff\1\5\4\uffff\1\5\1\uffff\2\5\1\uffff\13\5\1\3\2\uffff\1\5\2\uffff\2\3\2\uffff\1\5\3\uffff\1\5\4\uffff\1\5\14\uffff\3\5\1\uffff\1\5", "\1\6\12\uffff\1\7\40\uffff\1\3"]
    dfa_7 = DFA.unpackEncodedString(dfa_7s)
    dfa_8 = DFA.unpackEncodedString(dfa_8s)
    dfa_9 = DFA.unpackEncodedStringToUnsignedChars(dfa_9s)
    dfa_10 = DFA.unpackEncodedStringToUnsignedChars(dfa_10s)
    dfa_11 = DFA.unpackEncodedString(dfa_11s)
    dfa_12 = DFA.unpackEncodedString(dfa_12s)
    dfa_13 = unpackEncodedStringArray(dfa_13s)

    class DFA30(DFA):
        """ generated source for class DFA30 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA30, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 30
            self.eot = self.dfa_7
            self.eof = self.dfa_8
            self.min = self.dfa_9
            self.max = self.dfa_10
            self.accept = self.dfa_11
            self.special = self.dfa_12
            self.transition = self.dfa_13

        def getDescription(self):
            """ generated source for method getDescription """
            return "1103:4: ( ( ( (lv_parens_6_0= '(' ) ) ( ( (lv_init_7_0= ruleExpression ) ) (otherlv_8= ',' ( (lv_init_9_0= ruleExpression ) ) )* )? ( (lv_parens_10_0= ')' ) ) ) | ( ( (lv_braces_11_0= '{' ) ) ( ( (lv_init_12_0= ruleExpression ) ) (otherlv_13= ',' ( (lv_init_14_0= ruleExpression ) ) )* )? ( (lv_braces_15_0= '}' ) ) ) )?"

    dfa_14s = "\44\uffff"
    dfa_15s = "\1\5\1\uffff\1\5\3\uffff\1\22\2\uffff\1\34\1\uffff\1\4\1\65\5\22\1\76\1\10\1\43\2\4\2\22\1\65\5\22\1\76\1\10\1\4\2\22"
    dfa_16s = "\1\125\1\uffff\1\5\3\uffff\1\76\2\uffff\1\125\1\uffff\1\105\1\65\1\35\2\76\2\35\1\76\1\13\1\125\2\105\2\35\1\65\1\35\2\76\2\35\1\76\1\13\1\105\2\35"
    dfa_17s = "\1\uffff\1\7\1\uffff\1\1\1\2\1\3\1\uffff\1\5\1\6\1\uffff\1\4\31\uffff"
    dfa_18s = "\44\uffff}>"
    dfa_19s = ["\1\6\26\uffff\1\7\4\uffff\1\1\1\uffff\2\3\6\uffff\1\4\2\uffff\1\5\2\10\12\uffff\1\2\3\uffff\1\7\4\uffff\1\5\14\uffff\1\5\3\uffff\1\5", "", "\1\11", "", "", "", "\1\7\36\uffff\1\7\3\uffff\1\12\2\uffff\1\7\5\uffff\1\7", "", "", "\1\13\6\uffff\2\3\6\uffff\1\4\2\uffff\1\5\2\10\12\uffff\1\2\10\uffff\1\5\14\uffff\1\5\3\uffff\1\5", "", "\1\15\1\14\1\20\1\21\1\16\1\17\23\uffff\1\24\40\uffff\1\23\6\uffff\1\22", "\1\25", "\1\26\12\uffff\1\24", "\1\26\12\uffff\1\24\40\uffff\1\23", "\1\26\12\uffff\1\24\40\uffff\1\23", "\1\26\12\uffff\1\24", "\1\26\12\uffff\1\24", "\1\23", "\1\27\2\uffff\1\30", "\2\3\6\uffff\1\4\2\uffff\1\5\2\10\12\uffff\1\2\10\uffff\1\5\14\uffff\1\5\3\uffff\1\5", "\1\15\1\uffff\1\20\1\21\1\16\1\17\64\uffff\1\23\6\uffff\1\22", "\1\32\1\31\1\35\1\36\1\33\1\34\23\uffff\1\24\40\uffff\1\40\6\uffff\1\37", "\1\26\12\uffff\1\24", "\1\26\12\uffff\1\24", "\1\41", "\1\26\12\uffff\1\24", "\1\26\12\uffff\1\24\40\uffff\1\40", "\1\26\12\uffff\1\24\40\uffff\1\40", "\1\26\12\uffff\1\24", "\1\26\12\uffff\1\24", "\1\40", "\1\42\2\uffff\1\43", "\1\32\1\uffff\1\35\1\36\1\33\1\34\64\uffff\1\40\6\uffff\1\37", "\1\26\12\uffff\1\24", "\1\26\12\uffff\1\24"]
    dfa_14 = DFA.unpackEncodedString(dfa_14s)
    dfa_15 = DFA.unpackEncodedStringToUnsignedChars(dfa_15s)
    dfa_16 = DFA.unpackEncodedStringToUnsignedChars(dfa_16s)
    dfa_17 = DFA.unpackEncodedString(dfa_17s)
    dfa_18 = DFA.unpackEncodedString(dfa_18s)
    dfa_19 = unpackEncodedStringArray(dfa_19s)

    class DFA54(DFA):
        """ generated source for class DFA54 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA54, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 54
            self.eot = self.dfa_14
            self.eof = self.dfa_14
            self.min = self.dfa_15
            self.max = self.dfa_16
            self.accept = self.dfa_17
            self.special = self.dfa_18
            self.transition = self.dfa_19

        def getDescription(self):
            """ generated source for method getDescription """
            return "()* loopback of 1940:3: ( ( (lv_stateVars_5_0= ruleStateVar ) ) | ( (lv_timers_6_0= ruleTimer ) ) | ( (lv_actions_7_0= ruleAction ) ) | ( (lv_instantiations_8_0= ruleInstantiation ) ) | ( (lv_connections_9_0= ruleConnection ) ) | ( (lv_reactions_10_0= ruleReaction ) ) )*"

    dfa_20s = "\36\uffff"
    dfa_21s = "\1\50\1\5\2\uffff\1\34\1\4\1\65\5\22\1\76\1\10\1\50\2\4\2\22\1\65\5\22\1\76\1\10\1\4\2\22"
    dfa_22s = "\1\125\1\5\2\uffff\1\125\1\105\1\65\1\35\2\76\2\35\1\76\1\13\1\125\2\105\2\35\1\65\1\35\2\76\2\35\1\76\1\13\1\105\2\35"
    dfa_23s = "\2\uffff\1\1\1\2\32\uffff"
    dfa_24s = "\36\uffff}>"
    dfa_25s = ["\3\2\3\uffff\1\3\14\uffff\1\1\10\uffff\1\3\14\uffff\1\3\3\uffff\1\3", "\1\4", "", "", "\1\5\13\uffff\3\2\3\uffff\1\3\14\uffff\1\1\10\uffff\1\3\14\uffff\1\3\3\uffff\1\3", "\1\7\1\6\1\12\1\13\1\10\1\11\23\uffff\1\16\40\uffff\1\15\6\uffff\1\14", "\1\17", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16\40\uffff\1\15", "\1\20\12\uffff\1\16\40\uffff\1\15", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16", "\1\15", "\1\21\2\uffff\1\22", "\3\2\3\uffff\1\3\14\uffff\1\1\10\uffff\1\3\14\uffff\1\3\3\uffff\1\3", "\1\7\1\uffff\1\12\1\13\1\10\1\11\64\uffff\1\15\6\uffff\1\14", "\1\24\1\23\1\27\1\30\1\25\1\26\23\uffff\1\16\40\uffff\1\32\6\uffff\1\31", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16", "\1\33", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16\40\uffff\1\32", "\1\20\12\uffff\1\16\40\uffff\1\32", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16", "\1\32", "\1\34\2\uffff\1\35", "\1\24\1\uffff\1\27\1\30\1\25\1\26\64\uffff\1\32\6\uffff\1\31", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16"]
    dfa_20 = DFA.unpackEncodedString(dfa_20s)
    dfa_21 = DFA.unpackEncodedStringToUnsignedChars(dfa_21s)
    dfa_22 = DFA.unpackEncodedStringToUnsignedChars(dfa_22s)
    dfa_23 = DFA.unpackEncodedString(dfa_23s)
    dfa_24 = DFA.unpackEncodedString(dfa_24s)
    dfa_25 = unpackEncodedStringArray(dfa_25s)

    class DFA103(DFA):
        """ generated source for class DFA103 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA103, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 103
            self.eot = self.dfa_20
            self.eof = self.dfa_20
            self.min = self.dfa_21
            self.max = self.dfa_22
            self.accept = self.dfa_23
            self.special = self.dfa_24
            self.transition = self.dfa_25

        def getDescription(self):
            """ generated source for method getDescription """
            return "3949:2: (this_Port_0= rulePort | this_Action_1= ruleAction )"

    dfa_26s = "\14\uffff"
    dfa_27s = "\2\uffff\1\1\2\uffff\1\7\6\uffff"
    dfa_28s = "\1\4\1\uffff\1\5\2\uffff\1\5\1\4\1\uffff\1\22\1\4\1\22\1\4"
    dfa_29s = "\1\107\1\uffff\1\125\2\uffff\1\125\1\107\1\uffff\1\76\1\107\1\76\1\107"
    dfa_30s = "\1\uffff\1\1\1\uffff\1\3\1\4\2\uffff\1\2\4\uffff"
    dfa_31s = "\14\uffff}>"
    dfa_32s = ["\1\1\1\3\2\1\1\2\2\1\63\uffff\1\1\6\uffff\1\1\1\uffff\1\4", "", "\1\5\14\uffff\1\1\1\uffff\1\1\7\uffff\2\1\3\uffff\1\1\1\uffff\2\1\1\uffff\13\1\3\uffff\1\1\5\uffff\2\1\2\uffff\2\1\4\uffff\1\1\14\uffff\3\1\1\uffff\1\1", "", "", "\1\7\14\uffff\1\6\1\uffff\1\7\7\uffff\2\7\3\uffff\1\7\1\uffff\2\7\1\uffff\13\7\1\1\2\uffff\1\7\1\1\2\uffff\1\1\1\uffff\2\7\2\uffff\1\1\1\7\4\uffff\1\7\14\uffff\3\7\1\uffff\1\7", "\1\7\1\10\5\7\63\uffff\1\7\1\1\5\uffff\1\7\1\uffff\1\7", "", "\1\11\11\uffff\2\7\2\uffff\2\7\17\uffff\1\1\3\uffff\1\7\2\uffff\1\1\5\uffff\1\1", "\1\7\1\12\5\7\63\uffff\1\7\1\1\5\uffff\1\7\1\uffff\1\7", "\1\13\12\uffff\1\7\3\uffff\1\7\17\uffff\1\1\6\uffff\1\1\5\uffff\1\1", "\1\7\1\12\5\7\63\uffff\1\7\1\1\5\uffff\1\7\1\uffff\1\7"]
    dfa_26 = DFA.unpackEncodedString(dfa_26s)
    dfa_27 = DFA.unpackEncodedString(dfa_27s)
    dfa_28 = DFA.unpackEncodedStringToUnsignedChars(dfa_28s)
    dfa_29 = DFA.unpackEncodedStringToUnsignedChars(dfa_29s)
    dfa_30 = DFA.unpackEncodedString(dfa_30s)
    dfa_31 = DFA.unpackEncodedString(dfa_31s)
    dfa_32 = unpackEncodedStringArray(dfa_32s)

    class DFA121(DFA):
        """ generated source for class DFA121 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA121, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 121
            self.eot = self.dfa_26
            self.eof = self.dfa_27
            self.min = self.dfa_28
            self.max = self.dfa_29
            self.accept = self.dfa_30
            self.special = self.dfa_31
            self.transition = self.dfa_32

        def getDescription(self):
            """ generated source for method getDescription """
            return "4670:2: ( ( () ( (lv_literal_1_0= ruleLiteral ) ) ) | this_Time_2= ruleTime | this_ParameterReference_3= ruleParameterReference | this_Code_4= ruleCode )"

    dfa_33s = "\1\73\1\5\2\uffff\1\73\1\105\1\65\1\35\2\76\2\35\1\76\1\13\1\73\2\105\2\35\1\65\1\35\2\76\2\35\1\76\1\13\1\105\2\35"
    dfa_34s = ["\2\2\1\3\20\uffff\1\1", "\1\4", "", "", "\1\5\13\uffff\2\2\1\3\20\uffff\1\1", "\1\7\1\6\1\12\1\13\1\10\1\11\23\uffff\1\16\40\uffff\1\15\6\uffff\1\14", "\1\17", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16\40\uffff\1\15", "\1\20\12\uffff\1\16\40\uffff\1\15", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16", "\1\15", "\1\21\2\uffff\1\22", "\2\2\1\3\20\uffff\1\1", "\1\7\1\uffff\1\12\1\13\1\10\1\11\64\uffff\1\15\6\uffff\1\14", "\1\24\1\23\1\27\1\30\1\25\1\26\23\uffff\1\16\40\uffff\1\32\6\uffff\1\31", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16", "\1\33", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16\40\uffff\1\32", "\1\20\12\uffff\1\16\40\uffff\1\32", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16", "\1\32", "\1\34\2\uffff\1\35", "\1\24\1\uffff\1\27\1\30\1\25\1\26\64\uffff\1\32\6\uffff\1\31", "\1\20\12\uffff\1\16", "\1\20\12\uffff\1\16"]
    dfa_33 = DFA.unpackEncodedStringToUnsignedChars(dfa_33s)
    dfa_34 = unpackEncodedStringArray(dfa_34s)

    class DFA122(DFA):
        """ generated source for class DFA122 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA122, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 122
            self.eot = self.dfa_20
            self.eof = self.dfa_20
            self.min = self.dfa_21
            self.max = self.dfa_33
            self.accept = self.dfa_23
            self.special = self.dfa_24
            self.transition = self.dfa_34

        def getDescription(self):
            """ generated source for method getDescription """
            return "4830:2: (this_Input_0= ruleInput | this_Output_1= ruleOutput )"

    dfa_35s = "\7\uffff"
    dfa_36s = "\1\uffff\2\5\3\uffff\1\5"
    dfa_37s = "\1\5\2\24\1\5\2\uffff\1\24"
    dfa_38s = "\1\104\2\105\1\5\2\uffff\1\105"
    dfa_39s = "\4\uffff\1\1\1\2\1\uffff"
    dfa_40s = "\7\uffff}>"
    dfa_41s = ["\1\1\76\uffff\1\2", "\1\5\12\uffff\2\5\4\uffff\1\5\25\uffff\1\4\2\uffff\1\5\6\uffff\1\3", "\1\5\12\uffff\2\5\4\uffff\1\5\25\uffff\1\4\2\uffff\1\5\6\uffff\1\3", "\1\6", "", "", "\1\5\12\uffff\2\5\4\uffff\1\5\25\uffff\1\4\2\uffff\1\5\6\uffff\1\3"]
    dfa_35 = DFA.unpackEncodedString(dfa_35s)
    dfa_36 = DFA.unpackEncodedString(dfa_36s)
    dfa_37 = DFA.unpackEncodedStringToUnsignedChars(dfa_37s)
    dfa_38 = DFA.unpackEncodedStringToUnsignedChars(dfa_38s)
    dfa_39 = DFA.unpackEncodedString(dfa_39s)
    dfa_40 = DFA.unpackEncodedString(dfa_40s)
    dfa_41 = unpackEncodedStringArray(dfa_41s)

    class DFA137(DFA):
        """ generated source for class DFA137 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA137, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 137
            self.eot = self.dfa_35
            self.eof = self.dfa_36
            self.min = self.dfa_37
            self.max = self.dfa_38
            self.accept = self.dfa_39
            self.special = self.dfa_40
            self.transition = self.dfa_41

        def getDescription(self):
            """ generated source for method getDescription """
            return "5487:3: ( ( (lv_user_0_0= ruleKebab ) ) otherlv_1= '@' )?"

    dfa_42s = "\1\uffff\2\7\5\uffff\1\7"
    dfa_43s = "\1\5\2\24\2\uffff\2\5\1\uffff\1\24"
    dfa_44s = "\1\104\2\105\2\uffff\1\5\1\104\1\uffff\1\105"
    dfa_45s = "\3\uffff\1\1\1\2\2\uffff\1\3\1\uffff"
    dfa_46s = ["\1\1\2\uffff\1\3\63\uffff\1\4\7\uffff\1\2", "\1\7\12\uffff\2\7\4\uffff\1\7\25\uffff\1\6\2\uffff\1\7\6\uffff\1\5", "\1\7\12\uffff\2\7\4\uffff\1\7\25\uffff\1\6\2\uffff\1\7\6\uffff\1\5", "", "", "\1\10", "\1\7\2\uffff\1\3\73\uffff\1\7", "", "\1\7\12\uffff\2\7\4\uffff\1\7\25\uffff\1\6\2\uffff\1\7\6\uffff\1\5"]
    dfa_42 = DFA.unpackEncodedString(dfa_42s)
    dfa_43 = DFA.unpackEncodedStringToUnsignedChars(dfa_43s)
    dfa_44 = DFA.unpackEncodedStringToUnsignedChars(dfa_44s)
    dfa_45 = DFA.unpackEncodedString(dfa_45s)
    dfa_46 = unpackEncodedStringArray(dfa_46s)

    class DFA139(DFA):
        """ generated source for class DFA139 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA139, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 139
            self.eot = self.dfa_7
            self.eof = self.dfa_42
            self.min = self.dfa_43
            self.max = self.dfa_44
            self.accept = self.dfa_45
            self.special = self.dfa_12
            self.transition = self.dfa_46

        def getDescription(self):
            """ generated source for method getDescription """
            return "5573:2: (this_IPV4Host_0= ruleIPV4Host | this_IPV6Host_1= ruleIPV6Host | this_NamedHost_2= ruleNamedHost )"

    dfa_47s = "\35\uffff"
    dfa_48s = "\1\uffff\1\6\2\uffff\2\14\1\uffff\2\20\1\uffff\1\20\3\uffff\2\20\1\uffff\3\20\1\14\1\uffff\1\20\3\uffff\2\20\1\14"
    dfa_49s = "\3\5\2\45\1\5\1\uffff\2\5\1\45\2\5\2\uffff\1\5\1\45\1\uffff\2\5\1\45\1\5\1\uffff\1\5\1\uffff\1\5\1\uffff\1\5\1\45\1\5"
    dfa_50s = "\1\103\1\75\2\103\1\75\1\76\1\uffff\2\75\1\103\1\75\1\10\2\uffff\2\103\1\uffff\1\103\2\106\1\76\1\uffff\1\75\1\uffff\1\10\1\uffff\2\106\1\76"
    dfa_51s = "\6\uffff\1\1\5\uffff\1\2\1\5\2\uffff\1\3\4\uffff\1\7\1\uffff\1\4\1\uffff\1\6\3\uffff"
    dfa_52s = "\35\uffff}>"
    dfa_53s = ["\1\3\2\uffff\1\2\72\uffff\1\1", "\1\4\2\uffff\1\5\64\uffff\1\6", "\1\11\37\uffff\1\7\35\uffff\1\10", "\1\7\35\uffff\1\12", "\1\13\27\uffff\1\14", "\1\14\37\uffff\1\14\27\uffff\1\14\1\15", "", "\1\17\2\uffff\1\16\64\uffff\1\20", "\1\20\2\uffff\1\21\64\uffff\1\20", "\1\7\35\uffff\1\10", "\1\23\2\uffff\1\22\64\uffff\1\20", "\1\14\2\uffff\1\24", "", "", "\1\17\37\uffff\1\7\27\uffff\1\20\1\25\4\uffff\1\10", "\1\7\27\uffff\1\20\5\uffff\1\10", "", "\1\20\37\uffff\1\20\27\uffff\1\20\1\25\4\uffff\1\20", "\1\23\37\uffff\1\26\27\uffff\1\20\1\25\4\uffff\1\20\2\uffff\1\27", "\1\26\27\uffff\1\20\5\uffff\1\20\2\uffff\1\27", "\1\14\37\uffff\1\30\27\uffff\1\14\1\31", "", "\1\33\2\uffff\1\32\64\uffff\1\20", "", "\1\14\2\uffff\1\34", "", "\1\33\37\uffff\1\26\27\uffff\1\20\5\uffff\1\20\2\uffff\1\27", "\1\26\27\uffff\1\20\5\uffff\1\20\2\uffff\1\27", "\1\14\37\uffff\1\14\27\uffff\1\14\1\31"]
    dfa_47 = DFA.unpackEncodedString(dfa_47s)
    dfa_48 = DFA.unpackEncodedString(dfa_48s)
    dfa_49 = DFA.unpackEncodedStringToUnsignedChars(dfa_49s)
    dfa_50 = DFA.unpackEncodedStringToUnsignedChars(dfa_50s)
    dfa_51 = DFA.unpackEncodedString(dfa_51s)
    dfa_52 = DFA.unpackEncodedString(dfa_52s)
    dfa_53 = unpackEncodedStringArray(dfa_53s)

    class DFA159(DFA):
        """ generated source for class DFA159 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA159, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 159
            self.eot = self.dfa_47
            self.eof = self.dfa_48
            self.min = self.dfa_49
            self.max = self.dfa_50
            self.accept = self.dfa_51
            self.special = self.dfa_52
            self.transition = self.dfa_53

        def getDescription(self):
            """ generated source for method getDescription """
            return "5968:2: (kw= '::' | (kw= '::' (this_IPV6Seg_2= ruleIPV6Seg kw= ':' )* this_IPV6Seg_4= ruleIPV6Seg ) | ( (this_IPV6Seg_5= ruleIPV6Seg (kw= ':' | kw= '::' ) )+ (this_IPV6Seg_8= ruleIPV6Seg )? ) | (this_ID_9= RULE_ID kw= '::' this_IPV6Seg_11= ruleIPV6Seg (kw= ':' this_IPV6Seg_13= ruleIPV6Seg )* kw= '%' (this_INT_15= RULE_INT | this_ID_16= RULE_ID )+ ) | (kw= '::' this_IPV4Addr_18= ruleIPV4Addr ) | (kw= '::' this_ID_20= RULE_ID kw= ':' (this_INT_22= RULE_INT kw= ':' )? this_IPV4Addr_24= ruleIPV4Addr ) | ( ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) ) this_IPV4Addr_33= ruleIPV4Addr ) )"

    dfa_54s = "\10\uffff"
    dfa_55s = "\2\5\1\45\1\5\1\uffff\1\5\1\45\1\uffff"
    dfa_56s = "\1\10\2\103\1\10\1\uffff\2\103\1\uffff"
    dfa_57s = "\4\uffff\1\1\2\uffff\1\2"
    dfa_58s = "\10\uffff}>"
    dfa_59s = ["\1\2\2\uffff\1\1", "\1\2\37\uffff\1\3\35\uffff\1\4", "\1\3\35\uffff\1\4", "\1\6\2\uffff\1\5", "", "\1\6\37\uffff\1\3\30\uffff\1\7\4\uffff\1\4", "\1\3\35\uffff\1\4", ""]
    dfa_54 = DFA.unpackEncodedString(dfa_54s)
    dfa_55 = DFA.unpackEncodedStringToUnsignedChars(dfa_55s)
    dfa_56 = DFA.unpackEncodedStringToUnsignedChars(dfa_56s)
    dfa_57 = DFA.unpackEncodedString(dfa_57s)
    dfa_58 = DFA.unpackEncodedString(dfa_58s)
    dfa_59 = unpackEncodedStringArray(dfa_59s)

    class DFA158(DFA):
        """ generated source for class DFA158 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA158, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 158
            self.eot = self.dfa_54
            self.eof = self.dfa_54
            self.min = self.dfa_55
            self.max = self.dfa_56
            self.accept = self.dfa_57
            self.special = self.dfa_58
            self.transition = self.dfa_59

        def getDescription(self):
            """ generated source for method getDescription """
            return "6177:4: ( (this_IPV6Seg_25= ruleIPV6Seg (kw= ':' this_IPV6Seg_27= ruleIPV6Seg )* kw= '::' ) | ( (this_IPV6Seg_29= ruleIPV6Seg (kw= ':' this_IPV6Seg_31= ruleIPV6Seg )* ) kw= ':' ) )"

    dfa_60s = "\6\uffff"
    dfa_61s = "\1\uffff\3\4\2\uffff"
    dfa_62s = "\4\5\2\uffff"
    dfa_63s = "\4\114\2\uffff"
    dfa_64s = "\4\uffff\1\2\1\1"
    dfa_65s = "\6\uffff}>"
    dfa_66s = ["\1\1\70\uffff\1\2\12\uffff\1\3\1\uffff\2\4", "\1\1\14\uffff\1\4\16\uffff\1\4\33\uffff\1\4\1\2\12\uffff\1\3\1\5\2\4", "\1\1\14\uffff\1\4\16\uffff\1\4\33\uffff\1\4\1\2\12\uffff\1\3\1\5\2\4", "\1\1\14\uffff\1\4\16\uffff\1\4\33\uffff\1\4\1\2\12\uffff\1\3\1\5\2\4", "", ""]
    dfa_60 = DFA.unpackEncodedString(dfa_60s)
    dfa_61 = DFA.unpackEncodedString(dfa_61s)
    dfa_62 = DFA.unpackEncodedStringToUnsignedChars(dfa_62s)
    dfa_63 = DFA.unpackEncodedStringToUnsignedChars(dfa_63s)
    dfa_64 = DFA.unpackEncodedString(dfa_64s)
    dfa_65 = DFA.unpackEncodedString(dfa_65s)
    dfa_66 = unpackEncodedStringArray(dfa_66s)

    class DFA163(DFA):
        """ generated source for class DFA163 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA163, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 163
            self.eot = self.dfa_60
            self.eof = self.dfa_61
            self.min = self.dfa_62
            self.max = self.dfa_63
            self.accept = self.dfa_64
            self.special = self.dfa_65
            self.transition = self.dfa_66

        def getDescription(self):
            """ generated source for method getDescription """
            return "6430:3: (this_FSName_0= ruleFSName kw= ':\\\\' )?"

    FOLLOW_1 = BitSet([None] * )
    FOLLOW_2 = BitSet([None] * )
    FOLLOW_3 = BitSet([None] * )
    FOLLOW_4 = BitSet([None] * )
    FOLLOW_5 = BitSet([None] * )
    FOLLOW_6 = BitSet([None] * )
    FOLLOW_7 = BitSet([None] * )
    FOLLOW_8 = BitSet([None] * )
    FOLLOW_9 = BitSet([None] * )
    FOLLOW_10 = BitSet([None] * )
    FOLLOW_11 = BitSet([None] * )
    FOLLOW_12 = BitSet([None] * )
    FOLLOW_13 = BitSet([None] * )
    FOLLOW_14 = BitSet([None] * )
    FOLLOW_15 = BitSet([None] * )
    FOLLOW_16 = BitSet([None] * )
    FOLLOW_17 = BitSet([None] * )
    FOLLOW_18 = BitSet([None] * )
    FOLLOW_19 = BitSet([None] * )
    FOLLOW_20 = BitSet([None] * )
    FOLLOW_21 = BitSet([None] * )
    FOLLOW_22 = BitSet([None] * )
    FOLLOW_23 = BitSet([None] * )
    FOLLOW_24 = BitSet([None] * )
    FOLLOW_25 = BitSet([None] * )
    FOLLOW_26 = BitSet([None] * )
    FOLLOW_27 = BitSet([None] * )
    FOLLOW_28 = BitSet([None] * )
    FOLLOW_29 = BitSet([None] * )
    FOLLOW_30 = BitSet([None] * )
    FOLLOW_31 = BitSet([None] * )
    FOLLOW_32 = BitSet([None] * )
    FOLLOW_33 = BitSet([None] * )
    FOLLOW_34 = BitSet([None] * )
    FOLLOW_35 = BitSet([None] * )
    FOLLOW_36 = BitSet([None] * )
    FOLLOW_37 = BitSet([None] * )
    FOLLOW_38 = BitSet([None] * )
    FOLLOW_39 = BitSet([None] * )
    FOLLOW_40 = BitSet([None] * )
    FOLLOW_41 = BitSet([None] * )
    FOLLOW_42 = BitSet([None] * )
    FOLLOW_43 = BitSet([None] * )
    FOLLOW_44 = BitSet([None] * )
    FOLLOW_45 = BitSet([None] * )
    FOLLOW_46 = BitSet([None] * )
    FOLLOW_47 = BitSet([None] * )
    FOLLOW_48 = BitSet([None] * )
    FOLLOW_49 = BitSet([None] * )
    FOLLOW_50 = BitSet([None] * )
    FOLLOW_51 = BitSet([None] * )
    FOLLOW_52 = BitSet([None] * )
    FOLLOW_53 = BitSet([None] * )
    FOLLOW_54 = BitSet([None] * )
    FOLLOW_55 = BitSet([None] * )
    FOLLOW_56 = BitSet([None] * )
    FOLLOW_57 = BitSet([None] * )
    FOLLOW_58 = BitSet([None] * )
    FOLLOW_59 = BitSet([None] * )
    FOLLOW_60 = BitSet([None] * )
    FOLLOW_61 = BitSet([None] * )
    FOLLOW_62 = BitSet([None] * )
    FOLLOW_63 = BitSet([None] * )
    FOLLOW_64 = BitSet([None] * )
    FOLLOW_65 = BitSet([None] * )
    FOLLOW_66 = BitSet([None] * )
    FOLLOW_67 = BitSet([None] * )
    FOLLOW_68 = BitSet([None] * )
    FOLLOW_69 = BitSet([None] * )
    FOLLOW_70 = BitSet([None] * )
    FOLLOW_71 = BitSet([None] * )
    FOLLOW_72 = BitSet([None] * )
    FOLLOW_73 = BitSet([None] * )
    FOLLOW_74 = BitSet([None] * )
    FOLLOW_75 = BitSet([None] * )
    FOLLOW_76 = BitSet([None] * )
    FOLLOW_77 = BitSet([None] * )
    FOLLOW_78 = BitSet([None] * )
    FOLLOW_79 = BitSet([None] * )
    FOLLOW_80 = BitSet([None] * )
    FOLLOW_81 = BitSet([None] * )
    FOLLOW_82 = BitSet([None] * )
    FOLLOW_83 = BitSet([None] * )
    FOLLOW_84 = BitSet([None] * )
    FOLLOW_85 = BitSet([None] * )
    FOLLOW_86 = BitSet([None] * )
    FOLLOW_87 = BitSet([None] * )
    FOLLOW_88 = BitSet([None] * )
    FOLLOW_89 = BitSet([None] * )
    FOLLOW_90 = BitSet([None] * )
    FOLLOW_91 = BitSet([None] * )
    FOLLOW_92 = BitSet([None] * )
    FOLLOW_93 = BitSet([None] * )
    FOLLOW_94 = BitSet([None] * )
    FOLLOW_95 = BitSet([None] * )
    FOLLOW_96 = BitSet([None] * )
    FOLLOW_97 = BitSet([None] * )
    FOLLOW_98 = BitSet([None] * )
    FOLLOW_99 = BitSet([None] * )
    FOLLOW_100 = BitSet([None] * )
    FOLLOW_101 = BitSet([None] * )
    FOLLOW_102 = BitSet([None] * )
    FOLLOW_103 = BitSet([None] * )
    FOLLOW_104 = BitSet([None] * )
    FOLLOW_105 = BitSet([None] * )
    FOLLOW_106 = BitSet([None] * )
    FOLLOW_107 = BitSet([None] * )
    FOLLOW_108 = BitSet([None] * )
    FOLLOW_109 = BitSet([None] * )
    FOLLOW_110 = BitSet([None] * )
    FOLLOW_111 = BitSet([None] * )
    FOLLOW_112 = BitSet([None] * )
    FOLLOW_113 = BitSet([None] * )
    FOLLOW_114 = BitSet([None] * )
    FOLLOW_115 = BitSet([None] * )
    FOLLOW_116 = BitSet([None] * )
    FOLLOW_117 = BitSet([None] * )
    FOLLOW_118 = BitSet([None] * )
