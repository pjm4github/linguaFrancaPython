#!/usr/bin/env python
""" generated source for module MainContext """
# package: org.lflang.generator
# import java.util.Properties
# import java.util.function_.Function
# import org.eclipse.xtext.util.CancelIndicator
from include.overloading import overloaded
from org.lflang import DefaultErrorReporter

from org.lflang import ErrorReporter

from org.lflang import FileConfig

from org.lflang.generator.IntegratedBuilder import ReportProgress
from org.lflang.generator.IntegratedBuilder import ReportProgress
# 
#  * A {@code MainContext} is an {@code LFGeneratorContext} that is
#  * not nested in any other generator context. There is one
#  * {@code MainContext} for every build process.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class MainContext(LFGeneratorContext):
    """ generated source for class MainContext """
    #      * The indicator that shows whether this build
    #      * process is canceled.
    #      
    cancelIndicator = None

    #  The {@code ReportProgress} function of {@code this}. 
    reportProgress = None

    #  Whether the requested build is required to be complete. 
    mode = None

    #  The result of the code generation process. 
    result = None
    args = None
    hierarchicalBin = bool()

    #  FIXME: The interface would be simpler if this were part of {@code args}, and in addition, a potentially useful feature would be exposed to the user.
    constructErrorReporter = None
    hasConstructedErrorReporter = bool()

    #      * Initialize the context of a build process whose cancellation is
    #      * indicated by {@code cancelIndicator}
    #      * @param mode The mode of this build process.
    #      * @param cancelIndicator The cancel indicator of the code generation
    #      *                        process to which this corresponds.
    #      
    @overloaded
    def __init__(self, mode, cancelIndicator):
        """ generated source for method __init__ """
        super().__init__()
        self.__init__(mode, cancelIndicator, None, Properties(), False, DefaultErrorReporter())

    #      * Initialize the context of a build process whose cancellation is
    #      * indicated by {@code cancelIndicator}
    #      * @param mode The mode of this build process.
    #      * @param cancelIndicator The cancel indicator of the code generation
    #      *                        process to which this corresponds.
    #      * @param reportProgress The {@code ReportProgress} function of
    #      *                       {@code this}.
    #      * @param args Any arguments that may be used to affect the product of the
    #      *             build.
    #      * @param hierarchicalBin Whether the bin directory should be structured
    #      *                        hierarchically.
    #      * @param constructErrorReporter A function that constructs the appropriate
    #      *                               error reporter for the given FileConfig.
    #      
    @__init__.register(object, Mode, CancelIndicator, ReportProgress, Properties, bool, Function)
    def __init___0(self, mode, cancelIndicator, reportProgress, args, hierarchicalBin, constructErrorReporter):
        """ generated source for method __init___0 """
        super().__init__()
        self.mode = mode
        self.cancelIndicator = False if cancelIndicator == None else cancelIndicator
        self.reportProgress = reportProgress
        self.args = args
        self.hierarchicalBin = hierarchicalBin
        self.constructErrorReporter = constructErrorReporter
        self.hasConstructedErrorReporter = False

    def getCancelIndicator(self):
        """ generated source for method getCancelIndicator """
        return self.cancelIndicator

    def getMode(self):
        """ generated source for method getMode """
        return self.mode

    def getArgs(self):
        """ generated source for method getArgs """
        return self.args

    def useHierarchicalBin(self):
        """ generated source for method useHierarchicalBin """
        return self.hierarchicalBin

    def constructErrorReporter(self, fileConfig):
        """ generated source for method constructErrorReporter """
        if self.hasConstructedErrorReporter:
            raise IllegalStateException("Only one error reporter should be constructed for a given context.")
        self.hasConstructedErrorReporter = True
        return self.constructErrorReporter.apply(fileConfig)

    def finish(self, result):
        """ generated source for method finish """
        if self.result != None:
            raise IllegalStateException("A code generation process can only have one result.")
        self.result = result
        self.reportProgress(result.getUserMessage(), 100)

    def getResult(self):
        """ generated source for method getResult """
        return self.result if self.result != None else GeneratorResult.NOTHING

    def reportProgress(self, message, percentage):
        """ generated source for method reportProgress """
        self.reportProgress.apply(message, percentage)
