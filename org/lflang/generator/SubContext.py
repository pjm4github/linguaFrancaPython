#!/usr/bin/env python
""" generated source for module SubContext """
# package: org.lflang.generator
# import java.util.Properties
# import org.eclipse.xtext.util.CancelIndicator

from org.lflang.ErrorReporter

from org.lflang.FileConfig

# 
#  * A {@code SubContext} is the context of a process within a build process. For example,
#  * compilation of generated code may optionally be given a {@code SubContext} because
#  * compilation is part of a complete build.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class SubContext(LFGeneratorContext):
    """ generated source for class SubContext """
    containingContext = None
    startPercentProgress = int()
    endPercentProgress = int()

    #      * Initializes the context within {@code containingContext} of the process that extends from
    #      * {@code startPercentProgress} to {@code endPercentProgress}.
    #      * @param containingContext The context of the containing build process.
    #      * @param startPercentProgress The percent progress of the containing build process when this
    #      *                             nested process starts.
    #      * @param endPercentProgress The percent progress of the containing build process when this
    #      *                           nested process ends.
    #      
    def __init__(self, containingContext, startPercentProgress, endPercentProgress):
        """ generated source for method __init__ """
        super().__init__()
        self.containingContext = containingContext
        self.startPercentProgress = startPercentProgress
        self.endPercentProgress = endPercentProgress

    def getCancelIndicator(self):
        """ generated source for method getCancelIndicator """
        return self.containingContext.getCancelIndicator()

    def getMode(self):
        """ generated source for method getMode """
        return self.containingContext.getMode()

    def getArgs(self):
        """ generated source for method getArgs """
        return self.containingContext.getArgs()

    def useHierarchicalBin(self):
        """ generated source for method useHierarchicalBin """
        return self.containingContext.useHierarchicalBin()

    def constructErrorReporter(self, fileConfig):
        """ generated source for method constructErrorReporter """
        raise TypeError("Nested contexts should use the error reporters constructed by their containing contexts.")

    def finish(self, result):
        """ generated source for method finish """
        #  Do nothing. A build process is not finished until the outermost containing context is finished.

    def getResult(self):
        """ generated source for method getResult """
        raise TypeError("Only the outermost context can have a final result.")

    def reportProgress(self, message, percentage):
        """ generated source for method reportProgress """
        self.containingContext.reportProgress(message, self.startPercentProgress * (100 - percentage) / 100 + self.endPercentProgress * percentage / 100)
