#!/usr/bin/env python
""" generated source for module LanguageServerErrorReporter """
# package: org.lflang.generator
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.List
# import java.util.Map
# import java.util.Optional
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.lsp4j.Diagnostic
# import org.eclipse.lsp4j.DiagnosticSeverity
# import org.eclipse.lsp4j.PublishDiagnosticsParams
# import org.eclipse.lsp4j.Range
# import org.eclipse.xtext.nodemodel.util.NodeModelUtils
# import org.eclipse.lsp4j.services.LanguageClient
from include.overloading import overloaded
from org.lflang import ErrorReporter

# 
#  * Report diagnostics to the language client.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class LanguageServerErrorReporter(ErrorReporter):
    """ generated source for class LanguageServerErrorReporter """
    #      * The language client to which errors should be
    #      * reported, if such a client is available.
    #      * FIXME: This is a de facto global, and it is a hack.
    #      
    client = None

    #  The document for which this is a diagnostic acceptor. 
    parseRoot = None

    #  The list of all diagnostics since the last reset. 
    diagnostics = None

    #  ------------------------  CONSTRUCTORS  -------------------------- 
    #      * Initialize a {@code DiagnosticAcceptor} for the
    #      * document whose parse tree root node is
    #      * {@code parseRoot}.
    #      * @param parseRoot the root of the AST of the document
    #      *                  for which this is an error reporter
    #      
    def __init__(self, parseRoot):
        """ generated source for method __init__ """
        super(LanguageServerErrorReporter, self).__init__()
        self.parseRoot = parseRoot
        self.diagnostics = dict()

    #  -----------------------  PUBLIC METHODS  ------------------------- 
    @overloaded
    def reportError(self, message):
        """ generated source for method reportError """
        return report(getMainFile(), DiagnosticSeverity.Error, message)

    @overloaded
    def reportWarning(self, message):
        """ generated source for method reportWarning """
        return report(getMainFile(), DiagnosticSeverity.Warning, message)

    @overloaded
    def reportInfo(self, message):
        """ generated source for method reportInfo """
        return report(getMainFile(), DiagnosticSeverity.Information, message)

    @reportError.register(object, EObject, str)
    def reportError_0(self, object, message):
        """ generated source for method reportError_0 """
        return self.reportError(message)

    @reportWarning.register(object, EObject, str)
    def reportWarning_0(self, object, message):
        """ generated source for method reportWarning_0 """
        return self.reportWarning(message)

    @reportInfo.register(object, EObject, str)
    def reportInfo_0(self, object, message):
        """ generated source for method reportInfo_0 """
        return self.reportInfo(message)

    @reportError.register(object, Path, int, str)
    def reportError_1(self, file, line, message):
        """ generated source for method reportError_1 """
        return report(file, DiagnosticSeverity.Error, message, line if line != None else 1)

    @reportWarning.register(object, Path, int, str)
    def reportWarning_1(self, file, line, message):
        """ generated source for method reportWarning_1 """
        return report(file, DiagnosticSeverity.Warning, message, line if line != None else 1)

    @reportInfo.register(object, Path, int, str)
    def reportInfo_1(self, file, line, message):
        """ generated source for method reportInfo_1 """
        return report(file, DiagnosticSeverity.Information, message, line if line != None else 1)

    def getErrorsOccurred(self):
        """ generated source for method getErrorsOccurred """
        return None
        #          diagnostics.values().stream().anyMatch(
        #              it -> it.stream().anyMatch(diagnostic -> diagnostic.getSeverity() == DiagnosticSeverity.Error)
        #          );

    @overloaded
    def report(self, file, severity, message):
        """ generated source for method report """
        return self.report(file, severity, message, 1)

    @report.register(object, Path, DiagnosticSeverity, str, int)
    def report_0(self, file, severity, message, line):
        """ generated source for method report_0 """
        text = getLine(line - 1)
        return self.report(file, severity, message, Position.fromOneBased(line, 1), Position.fromOneBased(line, 1 + (0 if text.isEmpty() else len(length))))

    @report.register(object, Path, DiagnosticSeverity, str, Position, Position)
    def report_1(self, file, severity, message, startPos, endPos):
        """ generated source for method report_1 """
        if file == None:
            file = getMainFile()
        self.diagnostics.putIfAbsent(file, [])
        self.diagnostics.get(file).append(Diagnostic(toRange(startPos, endPos), message, severity, "LF Language Server"))
        return "" + severity + ": " + message

    #      * Save a reference to the language client.
    #      * @param client the language client
    #      
    @classmethod
    def setClient(cls, client):
        """ generated source for method setClient """
        LanguageServerErrorReporter.client = client

    #      * Publish diagnostics by forwarding them to the
    #      * language client.
    #      
    def publishDiagnostics(self):
        """ generated source for method publishDiagnostics """
        if self.client == None:
            System.err.println("WARNING: Cannot publish diagnostics because the language client has not yet been found.")
            return
        for file in diagnostics.keySet():
            publishDiagnosticsParams = PublishDiagnosticsParams()
            publishDiagnosticsParams.setUri(URI.createFileURI(file.__str__()).toString())
            publishDiagnosticsParams.setDiagnostics(self.diagnostics.get(file))
            self.client.publishDiagnostics(publishDiagnosticsParams)

    #  -----------------------  PRIVATE METHODS  ------------------------ 
    #  Return the file on which the current validation process was triggered. 
    def getMainFile(self):
        """ generated source for method getMainFile """
        return Path.of(self.parseRoot.eResource().getURI().toFileString())

    def getText(self):
        """ generated source for method getText """
        return NodeModelUtils.getNode(self.parseRoot).getText()

    def getLine(self, line):
        """ generated source for method getLine """
        return self.getText().lines().skip(line).findFirst()

    def toRange(self, p0, p1):
        """ generated source for method toRange """
        return Range(org.eclipse.lsp4j.Position(p0.getZeroBasedLine(), p0.getZeroBasedColumn()), org.eclipse.lsp4j.Position(p1.getZeroBasedLine(), p1.getZeroBasedColumn()))
