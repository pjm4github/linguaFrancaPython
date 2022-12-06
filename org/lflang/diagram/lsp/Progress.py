#!/usr/bin/env python
""" generated source for module Progress """
# package: org.lflang.diagram.lsp
# import java.util.HashMap
# import java.util.Map
# import org.eclipse.lsp4j.jsonrpc.messages.Either
# import org.eclipse.lsp4j.ProgressParams
# import org.eclipse.lsp4j.services.LanguageClient
# import org.eclipse.lsp4j.WorkDoneProgressCreateParams
# import org.eclipse.lsp4j.WorkDoneProgressBegin
# import org.eclipse.lsp4j.WorkDoneProgressEnd
# import org.eclipse.lsp4j.WorkDoneProgressNotification
# import org.eclipse.lsp4j.WorkDoneProgressReport
# import org.eclipse.xtext.util.CancelIndicator

# 
#  * A class for reporting the progress of an ongoing task.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#

class WorkDoneProgressCreateParams:
    pass


class WorkDoneProgressBegin:
    pass


class WorkDoneProgressReport:
    pass


class Either:
    pass


class WorkDoneProgressEnd:
    pass


class ProgressParams:
    pass


class Progress(object):
    """ generated source for class Progress """


    #      * Initialize the {@code Progress} of a task titled {@code title} that is
    #      * triggered via {@code client}.
    #      * @param client A language client through which a task was triggered.
    #      * @param title The title of the task.
    #      * @param cancellable Whether the task tracked by {@code this} can be
    #      * cancelled.
    #      
    def __init__(self, client, title, cancellable):
        """ generated source for method __init__ """
        self.client = client
        self.title = title
        self.nextToken = 0
        self.cancellations = dict()


        self.token = int()
        self.cancellable = bool()

        __nextToken_0 = self.nextToken
        self.nextToken += 1
        self.token = __nextToken_0
        self.cancellable = cancellable
        if cancellable:
            self.cancellations.put(self.token, False)
        client.createProgress(WorkDoneProgressCreateParams(Either.forRight(self.token)))

    #      * Cancel the task tracked by the {@code Progress} that has token
    #      * {@code token}.
    #      
    @classmethod
    def cancel(cls, token):
        """ generated source for method cancel """
        if cls.cancellations.containsKey(token):
            cls.cancellations.put(token, True)

    #      * Returns the cancel indicator for the task tracked by this
    #      * {@code Progress}.
    #      * @return the cancel indicator for the task tracked by this
    #      * {@code Progress}
    #      
    def getCancelIndicator(self):
        """ generated source for method getCancelIndicator """
        if self.cancellable:
            return self.cancellations.get(self.token)
        return False

    #      * Report that the task tracked by {@code this} is done.
    #      
    def begin(self):
        """ generated source for method begin """
        begin = WorkDoneProgressBegin()
        begin.setTitle(self.title)
        begin.setCancellable(self.cancellable)
        begin.setPercentage(0)
        self.notifyProgress(begin)

    #      * Report the progress of the task tracked by {@code this}.
    #      * @param message A message describing the progress of the task.
    #      
    def report(self, message, percentage):
        """ generated source for method report """
        report = WorkDoneProgressReport()
        report.setMessage(message)
        report.setCancellable(self.cancellable)
        report.setPercentage(percentage)
        self.notifyProgress(report)

    #      * Marks the task tracked by {@code this} as terminated.
    #      * @param message A message describing the outcome of the task.
    #      
    def end(self, message):
        """ generated source for method end """
        end = WorkDoneProgressEnd()
        end.setMessage(message)
        self.notifyProgress(end)

    #      * Send the given progress notification to the client.
    #      * @param notification
    #      
    def notifyProgress(self, notification):
        """ generated source for method notifyProgress """
        self.client.notifyProgress(ProgressParams(Either.forRight(self.token), Either.forLeft(notification)))
