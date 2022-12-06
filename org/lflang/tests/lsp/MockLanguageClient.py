#!/usr/bin/env python
""" generated source for module MockLanguageClient """
# package: org.lflang.tests.lsp
# import java.util.ArrayList
# import java.util.Collections
# import java.util.List
# import java.util.concurrent.CompletableFuture
# import org.eclipse.lsp4j.Diagnostic
# import org.eclipse.lsp4j.DiagnosticSeverity
# import org.eclipse.lsp4j.MessageActionItem
# import org.eclipse.lsp4j.MessageParams
# import org.eclipse.lsp4j.PublishDiagnosticsParams
# import org.eclipse.lsp4j.ShowMessageRequestParams
# import org.eclipse.lsp4j.services.LanguageClient

# 
#  * A {@code MockLanguageClient} is a language client that should be used in language server tests.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class MockLanguageClient(LanguageClient):
    """ generated source for class MockLanguageClient """
    receivedDiagnostics = []

    def telemetryEvent(self, object):
        """ generated source for method telemetryEvent """
        #  Do nothing.

    def publishDiagnostics(self, diagnostics):
        """ generated source for method publishDiagnostics """
        self.receivedDiagnostics.extend(diagnostics.getDiagnostics())
        for d in diagnostics.getDiagnostics():
            (System.err if (d.getSeverity() == DiagnosticSeverity.Error or d.getSeverity() == DiagnosticSeverity.Warning) else System.out).println("Test client received diagnostic at line " + d.getRange().getStart().getLine() + ": " + d.getMessage())

    def showMessage(self, messageParams):
        """ generated source for method showMessage """
        print("Test client received message: " + messageParams.getMessage())

    def showMessageRequest(self, requestParams):
        """ generated source for method showMessageRequest """
        self.showMessage(requestParams)
        return None

    def logMessage(self, message):
        """ generated source for method logMessage """
        self.showMessage(message)

    def getReceivedDiagnostics(self):
        """ generated source for method getReceivedDiagnostics """
        return Collections.unmodifiableList(self.receivedDiagnostics)

    def clearDiagnostics(self):
        """ generated source for method clearDiagnostics """
        self.receivedDiagnostics.clear()
