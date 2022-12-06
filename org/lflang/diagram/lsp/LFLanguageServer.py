#!/usr/bin/env python
""" generated source for module LFLanguageServer """
# package: org.lflang.diagram.lsp
# import org.eclipse.lsp4j.WorkDoneProgressCancelParams
# import de.cau.cs.kieler.klighd.lsp.KGraphLanguageServerExtension
# import org.eclipse.lsp4j.Hover
# import org.eclipse.lsp4j.HoverParams
# import org.eclipse.xtext.ide.server.hover.IHoverService
# import org.eclipse.xtext.util.CancelIndicator
import Progress
# 
#  * The Lingua Franca language and diagram server.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class KGraphLanguageServerExtension:
    pass


class IHoverService:
    pass


class LFLanguageServer(KGraphLanguageServerExtension):
    """ generated source for class LFLanguageServer """
    def cancelProgress(self, params):
        """ generated source for method cancelProgress """
        Progress.cancel(params.getToken().getRight().intValue())

    def hover(self, params, cancelIndicator):
        """ generated source for method hover """
        try:
            return super(LFLanguageServer, self).hover(params, cancelIndicator)
        except IndexError as e:
            return IHoverService.EMPTY_HOVER
