#!/usr/bin/env python
""" generated source for module LFUiModuleImpl """
# package: org.lflang.ui
# import com.google.common.base.Objects
# import com.google.inject.Provider
# import java.io.PrintStream
# import java.util.LinkedList
# import java.util.List
# import org.eclipse.jface.text.BadLocationException
# import org.eclipse.jface.text.DocumentCommand
# import org.eclipse.jface.text.IDocument
# import org.eclipse.jface.text.IRegion
# import org.eclipse.jface.text.TextUtilities
# import org.eclipse.ui.console.ConsolePlugin
# import org.eclipse.ui.console.IConsole
# import org.eclipse.ui.console.MessageConsole
# import org.eclipse.ui.console.MessageConsoleStream
# import org.eclipse.ui.plugin.AbstractUIPlugin
# import org.eclipse.xtext.resource.containers.IAllContainersState
# import org.eclipse.xtext.ui.editor.autoedit.AbstractEditStrategyProvider
# import org.eclipse.xtext.ui.editor.autoedit.AbstractTerminalsEditStrategy
# import org.eclipse.xtext.ui.editor.autoedit.CommandInfo
# import org.eclipse.xtext.ui.editor.autoedit.DefaultAutoEditStrategyProvider
# import org.eclipse.xtext.ui.editor.autoedit.MultiLineTerminalsEditStrategy
# import org.eclipse.xtext.ui.editor.autoedit.SingleLineTerminalsStrategy
# import org.eclipse.xtext.ui.shared.Access

# 
#  * Use this class to register components to be used within the Eclipse IDE.
#  *
#  * This subclass provides an astonishingly opaque and complex override of
#  * the default editor behavior to properly handle the code body delimiters
#  * {= ... =} of Lingua Franca.  It is disheartening how difficult this was
#  * to accomplish.  The design of xtext does not seem to lend itself to
#  * subclassing, and the code has no comments in it at all.
#  
class LFUiModuleImpl(AbstractLFUiModule):
    """ generated source for class LFUiModuleImpl """
    class LinguaFrancaAutoEdit(DefaultAutoEditStrategyProvider):
        """ generated source for class LinguaFrancaAutoEdit """
        class LFMultiLineTerminalsEditStrategy(MultiLineTerminalsEditStrategy):
            """ generated source for class LFMultiLineTerminalsEditStrategy """
            def __init__(self, leftTerminal, rightTerminal, nested):
                """ generated source for method __init__ """
                super(LFMultiLineTerminalsEditStrategy, self).__init__(nested)

            def handleCursorInFirstLine(self, document, command, startTerminal, stopTerminal):
                """ generated source for method handleCursorInFirstLine """
                #  Create a modified command.
                newC = CommandInfo()
                #  If this is handling delimiters { }, but the actual delimiters are {= =},
                #  then do nothing.
                if getLeftTerminal() == "{":
                    start = document.get(startTerminal.getOffset(), 2)
                    if start == "{=":
                        return newC
                newC.isChange = True
                newC.offset = command.offset
                #  Insert the Return character into the new command.
                newC.text += "\n"
                newC.text += command.text.trim()
                newC.cursorOffset = command.offset + len(length)
                if stopTerminal == None and atEndOfLineInput(document, command.offset):
                    newC.text += command.text + getRightTerminal()
                if stopTerminal != None and stopTerminal.getOffset() >= command.offset:
                    #  If the right delimiter is on the same line as the left,
                    #  collect the text between them and indent to the right place.
                    if util.isSameLine(document, stopTerminal.getOffset(), command.offset):
                        #  Get the code block between the delimiters, trimed of whitespace.
                        codeBlock = document.get(command.offset, stopTerminal.getOffset() - command.offset).trim()
                        indentation = indentationAt(document, command.offset)
                        #  Indent by at least 4 spaces.
                        numSpaces = 4 * ((indentation / 4) + 1)
                        newC.text += " ".repeat(numSpaces)
                        newC.cursorOffset += numSpaces
                        newC.text += codeBlock
                        newC.text += command.text.trim()
                        newC.text += "\n"
                        numNextLineSpaces = 4 * (indentation / 4)
                        newC.text += " ".repeat(numNextLineSpaces)
                        len(newC)
                    else:
                        #  Creating a new first line within a pre-existing block.
                        indentation = indentationAt(document, command.offset)
                        #  Indent by at least 4 spaces.
                        numSpaces = 4 * ((indentation / 4) + 1)
                        newC.text += " ".repeat(numSpaces)
                        newC.cursorOffset += numSpaces
                        #  The length field is, as usual for xtext, undocumented.
                        #  It is not the length of the new command, but seems to be
                        #  the number of characters of the original document that are
                        #  to be replaced.
                        len(newC)
                return newC

            #  Expose base class protected methods within this package.
            def findStopTerminal(self, document, offset):
                """ generated source for method findStopTerminal """
                return super(LFMultiLineTerminalsEditStrategy, self).findStopTerminal(document, offset)

            def findStartTerminal(self, document, offset):
                """ generated source for method findStartTerminal """
                return super(LFMultiLineTerminalsEditStrategy, self).findStartTerminal(document, offset)

            def internalCustomizeDocumentCommand(self, document, command):
                """ generated source for method internalCustomizeDocumentCommand """
                super(LFMultiLineTerminalsEditStrategy, self).internalCustomizeDocumentCommand(document, command)

            #          * Strategy for handling combinations of nested braces of different types.
        #          * This is based on CompoundMultiLineTerminalsEditStrategy by Sebastian Zarnekow,
        #          * but unfortunately, that class is not written in a way that can be overridden,
        #          * so this is a reimplementation.
        #          
        class CompoundLFMultiLineTerminalsEditStrategy(AbstractTerminalsEditStrategy):
            """ generated source for class CompoundLFMultiLineTerminalsEditStrategy """
            def __init__(self, leftTerminal, rightTerminal):
                """ generated source for method __init__ """
                super(CompoundLFMultiLineTerminalsEditStrategy, self).__init__(rightTerminal)

            def internalCustomizeDocumentCommand(self, document, command):
                """ generated source for method internalCustomizeDocumentCommand """
                if len(command):
                    return
                lineDelimiters = document.getLegalLineDelimiters()
                delimiterIndex = TextUtilities.startsWith(lineDelimiters, command.text)
                if delimiterIndex != -1:
                    bestStrategy = None
                    bestStart = None
                    for strategy in strategies:
                        candidate = strategy.findStartTerminal(document, command.offset)
                        if candidate != None:
                            if bestStart == None or bestStart.getOffset() < candidate.getOffset():
                                bestStrategy = strategy
                                bestStart = candidate
                    if bestStrategy != None:
                        bestStrategy.internalCustomizeDocumentCommand(document, command)

            #          * Strategies used to handle combinations of nested braces.
        #          
        strategies = list(LFMultiLineTerminalsEditStrategy("(", ")", True), LFMultiLineTerminalsEditStrategy("{", "}", True), LFMultiLineTerminalsEditStrategy("[", "]", True), LFMultiLineTerminalsEditStrategy("{=", "=}", True))

            #          * Handle combinations of nested braces.
        #          * The following from the base class completely messes up with codeblocks.
        #          * So we replace it below. Unfortunately, the base class CompoundMultiLineTerminalsEditStrategy
        #          * is not written in a way that can be overridden, so we have to completely
        #          * reimplement it.
        #          
        def configureCompoundBracesBlocks(self, acceptor):
            """ generated source for method configureCompoundBracesBlocks """
            acceptor.accept(self.CompoundLFMultiLineTerminalsEditStrategy("{=", "=}"), IDocument.DEFAULT_CONTENT_TYPE)

            #          * For the given document, return the indentation of the line at
        #          * the specified offset. If the indentation is accomplished with
        #          * tabs, count each tab as four spaces.
        #          * @param document The document.
        #          * @param offset The offset.
        #          
        @classmethod
        def indentationAt(cls, document, offset):
            """ generated source for method indentationAt """
            lineNumber = document.getLineOfOffset(offset)
            #  Line number.
            lineStart = document.getLineOffset(lineNumber)
            #  Offset of start of line.
            lineLength = document.getLineLength(lineNumber)
            #  Length of the line.
            line = document.get(lineStart, lineLength)
            #  Replace all tabs with four spaces.
            line = line.replaceAll("\t", "    ")
            return line.indexOf(line.trim())

            #          * When encountering {= append =}.
        #          
        def configureCodeBlock(self, acceptor):
            """ generated source for method configureCodeBlock """
            acceptor.accept(SingleLineTerminalsStrategy("{=", "=}", SingleLineTerminalsStrategy.DEFAULT), IDocument.DEFAULT_CONTENT_TYPE)

            #          * When hitting Return with a code block, move the =} to a newline properly indented.
        #          
        def configureMultilineCodeBlock(self, acceptor):
            """ generated source for method configureMultilineCodeBlock """
            for strategy in strategies:
                acceptor.accept(strategy, IDocument.DEFAULT_CONTENT_TYPE)

            #          * Ensure that all text printed via println() is shown in the Console of the LF IDE.
        #          
        def configureConsole(self):
            """ generated source for method configureConsole """
            if not consoleInitialized:
                console = MessageConsole("LF Output", None)
                ConsolePlugin.getDefault().getConsoleManager().addConsoles([None] * )
                ConsolePlugin.getDefault().getConsoleManager().showConsoleView(console)
                stream = console.newMessageStream()
                System.setOut(PrintStream(stream))
                System.setErr(PrintStream(stream))
                consoleInitialized = True
            return consoleInitialized

        def configure(self, acceptor):
            """ generated source for method configure """
            self.configureConsole()
            self.configureMultilineCodeBlock(acceptor)
            super(LinguaFrancaAutoEdit, self).configure(acceptor)
            self.configureCodeBlock(acceptor)

    consoleInitialized = False

    def provideIAllContainersState(self):
        """ generated source for method provideIAllContainersState """
        return Access.getJavaProjectsState()

    def bindAutoEditStrategy(self):
        """ generated source for method bindAutoEditStrategy """
        return self.LinguaFrancaAutoEdit.__class__

    def __init__(self, arg0):
        """ generated source for method __init__ """
        super(LFUiModuleImpl, self).__init__(arg0)
