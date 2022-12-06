#!/usr/bin/env python
""" generated source for module LFLanguageServerExtension """
# package: org.lflang.diagram.lsp
# import java.nio.file.Path
# import java.util.concurrent.CompletableFuture
# import java.util.function_.Function
# import java.util.ArrayList
# import org.eclipse.emf.common.util.URI
# import org.eclipse.lsp4j.jsonrpc.services.JsonNotification
# import org.eclipse.lsp4j.jsonrpc.services.JsonRequest
# import org.eclipse.lsp4j.jsonrpc.CancelChecker
# import org.eclipse.lsp4j.ProgressParams
# import org.eclipse.lsp4j.services.LanguageClient
# import org.eclipse.xtext.ide.server.ILanguageServerExtension
# import org.eclipse.xtext.ide.server.ILanguageServerAccess
# import org.eclipse.xtext.util.CancelIndicator
import sys

from lflang.diagram.lsp.Progress import Progress
from org.lflang.generator import IntegratedBuilder

from org.lflang.generator import GeneratorResult

from org.lflang import LFStandaloneSetup

from org.lflang import LFRuntimeModule

from org.lflang.util import LFCommand

# 
#  * Provide Lingua-Franca-specific extensions to the
#  * language server's behavior.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class CompletableFuture:
    pass


class ILanguageServerExtension:
    pass


class JsonRequest:
    pass


class JsonNotification:
    pass


class LFLanguageServerExtension(ILanguageServerExtension):
    """ generated source for class LFLanguageServerExtension """
    #  The IntegratedBuilder instance that handles all build requests for the current session. 
    builder = LFStandaloneSetup(LFRuntimeModule()).createInjectorAndDoEMFRegistration().getInstance(IntegratedBuilder.__class__)
    client = None

    def initialize(self, access):
        """ generated source for method initialize """

    def setClient(self, client):
        """ generated source for method setClient """
        self.client = client

    @JsonRequest("generator/build")
    def build(self, uri):
        """ generated source for method build """
        if self.client == None:
            return CompletableFuture.completedFuture("Please wait for the Lingua Franca language server to be fully initialized.")
        s = None
        try:
            s = self.buildWithProgress(self.client, uri, True).getUserMessage()
        except Exception as e:
            s = "An internal error occurred:\n" + e
        return CompletableFuture.supplyAsync()

    @JsonNotification("generator/partialBuild")
    def partialBuild(self, uri):
        """ generated source for method partialBuild """
        if self.client == None:
            return
        self.buildWithProgress(self.client, uri, False)

    @JsonNotification("generator/buildAndRun")
    def buildAndRun(self, uri):
        """ generated source for method buildAndRun """
        return CompletableFuture().completeAsync()

    def buildWithProgress(self, client, uri, mustComplete):
        """ generated source for method buildWithProgress """
        parsedUri = None
        try:
            parsedUri = uri.split('/')[-1]
        except Exception as e:
            sys.stderr(e)
            return GeneratorResult.NOTHING
        progress = Progress(client, "Build \"" + parsedUri + "\"", mustComplete)
        progress.begin()
        result = None
        try:
            result = self.builder.run(parsedUri, mustComplete, progress.report, progress.getCancelIndicator())
        finally:
            progress.end("An internal error occurred." if result == None else result.getUserMessage())
        return result
