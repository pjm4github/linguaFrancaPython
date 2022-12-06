#!/usr/bin/env python
""" generated source for module LFSyntaxErrorMessageProvider """
# package: org.lflang
# import java.util.Set
# import java.util.stream.Collectors

import org.antlr.runtime.RecognitionException

import org.antlr.runtime.Token
# import org.eclipse.xtext.GrammarUtil
# import org.eclipse.xtext.IGrammarAccess
# import org.eclipse.xtext.nodemodel.SyntaxErrorMessage
# import org.eclipse.xtext.parser.antlr.SyntaxErrorMessageProvider
# import com.google.inject.Inject

# 
#  * Custom error message provider that intercepts syntax errors.
#  * 
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class LFSyntaxErrorMessageProvider(SyntaxErrorMessageProvider):
    """ generated source for class LFSyntaxErrorMessageProvider """
    #      * Issue code for syntax error due to misused keyword.
    #      
    USED_RESERVED_KEYWORD = "USED_RESERVED_KEYWORD"

    #      * Issue code for syntax error due to misused single quotes.
    #      
    SINGLY_QUOTED_STRING = "SINGLE_QUOTED_STRING"

    #      * Helper that provides access to the grammar.
    #      
    grammarAccess = None

    #      * Set of keywords that otherwise would be valid identifiers. 
    #      * For example, 'reaction' is part of this set, but '{=' is not.
    #      
    keywords = None

    #      * Customize intercepted error messages.
    #      * 
    #      * @Override
    #      
    def getSyntaxErrorMessage(self, context):
        """ generated source for method getSyntaxErrorMessage """
        if context != None:
            message = context.getDefaultMessage()
            #  Describe situation where an unexpected token was encountered where a closing single quote was expected.
            if message.contains("expecting '''"):
                return SyntaxErrorMessage("Single quotes can only be used around single characters, not strings. " + "Please use double quotes instead.", self.SINGLY_QUOTED_STRING)
            e = context.getRecognitionException()
            if e != None:
                token = e.token
                if token != None:
                    text = token.getText()
                    if text != None:
                        #  Update keywords if not yet set.
                        if self.keywords == None:
                            #  ('a'..'z'|'A'..'Z'|'_')('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
                            self.keywords = GrammarUtil.getAllKeywords(self.grammarAccess.getGrammar()).stream().filter(k.matches("^([a-z]|[A-Z]|_)+(\\w|_)*$")).collect(Collectors.toSet())
                        if self.keywords.contains(text):
                            return SyntaxErrorMessage("'" + text + "' is a reserved keyword " + "which cannot be used as an identifier.", self.USED_RESERVED_KEYWORD)
        return super(LFSyntaxErrorMessageProvider, self).getSyntaxErrorMessage(context)
