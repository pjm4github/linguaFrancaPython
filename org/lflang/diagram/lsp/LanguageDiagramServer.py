#!/usr/bin/env python
""" generated source for module LanguageDiagramServer """
# package: org.lflang.diagram.lsp
# import java.util.List
# import org.eclipse.xtext.ide.server.LanguageServerImpl
# import org.eclipse.xtext.ide.server.ILanguageServerExtension
# import org.eclipse.xtext.service.AbstractGenericModule
# import com.google.inject.Module
# import com.google.inject.util.Modules
# import de.cau.cs.kieler.klighd.lsp.KGraphLanguageClient
# import de.cau.cs.kieler.klighd.lsp.interactive.layered.LayeredInteractiveLanguageServerExtension
# import de.cau.cs.kieler.klighd.lsp.interactive.rectpacking.RectpackingInteractiveLanguageServerExtension
# import de.cau.cs.kieler.klighd.lsp.launch.AbstractLanguageServer
# import de.cau.cs.kieler.klighd.lsp.launch.AbstractLsCreator
# import de.cau.cs.kieler.klighd.lsp.launch.AbstractRegistrationLanguageServerExtension
# import de.cau.cs.kieler.klighd.lsp.launch.ILanguageRegistration
# import de.cau.cs.kieler.klighd.lsp.launch.Language

from org.lflang.ide import LFIdeSetup

from org.lflang.generator import LanguageServerErrorReporter

# 
#  * Language server with extended diagram communication.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#  
class AbstractLanguageServer:
    pass


class AbstractLsCreator:
    pass


class Modules:
    pass


class LFLsCreator:
    pass


class LayeredInteractiveLanguageServerExtension:
    pass


class RectpackingInteractiveLanguageServerExtension:
    pass


class LFLanguageServerExtension:
    pass


class LFRegistrationLanguageServerExtension:
    pass


class KGraphLanguageClient:
    pass


class ILanguageRegistration:
    pass


class AbstractGenericModule:
    pass


class AbstractRegistrationLanguageServerExtension:
    pass


class Language:
    pass


class LFLsCreator(AbstractLsCreator):
    """ generated source for class LFLsCreator """
    def createLSModules(self, socket):
        """ generated source for method createLSModules """
        return Modules.override(super().createLSModules(socket)).with_(AbstractGenericModule())

    constraints = None
    rectPack = None
    lfExtension = None

    def getLanguageServerExtensions(self):
        """ generated source for method getLanguageServerExtensions """
        self.constraints = self.injector.getInstance(LayeredInteractiveLanguageServerExtension.__class__)
        self.rectPack = self.injector.getInstance(RectpackingInteractiveLanguageServerExtension.__class__)
        self.lfExtension = self.injector.getInstance(LFLanguageServerExtension.__class__)
        return list(self.injector.getInstance(LFRegistrationLanguageServerExtension.__class__), self.constraints, self.rectPack, self.lfExtension)

    def getRemoteInterface(self):
        """ generated source for method getRemoteInterface """
        return KGraphLanguageClient.__class__

    def onConnect(self):
        """ generated source for method onConnect """
        super().onConnect()
        self.constraints.setClient(self.languageClient)
        self.rectPack.setClient(self.languageClient)
        LanguageServerErrorReporter.setClient(self.languageClient)
        self.lfExtension.setClient(self.languageClient)
        #  The following is needed because VS Code treats System.err like System.out and System.out like a shout
        #  into the void.
        sys.stdout = sys.stderr


class LFLanguageRegistration(ILanguageRegistration):
    """ generated source for class LFLanguageRegistration """
    def bindAndRegisterLanguages(self):
        """ generated source for method bindAndRegisterLanguages """
        LFIdeSetup.doSetup()


class LFRegistrationLanguageServerExtension(AbstractRegistrationLanguageServerExtension):
    """ generated source for class LFRegistrationLanguageServerExtension """
    def getLanguageExtensions(self):
        """ generated source for method getLanguageExtensions """
        return list(Language("lf", "Lingua Franca", []))


class LanguageDiagramServer(AbstractLanguageServer):
    """ generated source for class LanguageDiagramServer """

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        LanguageDiagramServer().start()

    def start(self):
        """ generated source for method start """
        self.configureAndRun(self.LFLanguageRegistration(), self.LFLsCreator())


if __name__ == '__main__':
    import sys
    LanguageDiagramServer.main(sys.argv)
