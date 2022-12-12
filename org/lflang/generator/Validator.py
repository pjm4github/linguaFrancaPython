#!/usr/bin/env python
""" generated source for module Validator """
# package: org.lflang.generator
# import org.eclipse.xtext.util.CancelIndicator
import sys

from lflang.diagram.lsp.LFLanguageServerExtension import CompletableFuture
from lflang.generator.LFGeneratorContext import LFGeneratorContext
from lflang.generator.ReactionInstance import Runtime
from lflang.generator.c.CGenerator import Executors
from lflang.ErrorReporter import ErrorReporter
from lflang.util.LFCommand import LFCommand

# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.Collection
# import java.util.Comparator
# import java.util.List
# import java.util.Map
# import java.util.concurrent.Callable
# import java.util.concurrent.CompletableFuture
# import java.util.concurrent.ExecutionException
# import java.util.concurrent.ExecutorService
# import java.util.concurrent.Executors
# import java.util.concurrent.Future
# import java.util.stream.Collectors
# import com.google.common.collect.ImmutableMap

# 
#  * Validate generated code.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  


class Pair:
    def __init__(self, first, second):
        """ generated source for method __init__ """
        self.first = first
        self.second = second


class Validator:
    """ generated source for class Validator """
    #      * Files older than {@code FILE_AGE_THRESHOLD_MILLIS} may be skipped in validation on the
    #      * grounds that they probably have not been updated since the last validator pass.
    #      
    #  This will cause silent validation failures if it takes too long to write all generated code to the file system.
    FILE_AGE_THRESHOLD_MILLIS = 10000

    def __init__(self, errorReporter, codeMaps):
        """
        Initialize a {@code Validator} that reports errors to {@code errorReporter} and adjusts
        document positions using {@code codeMaps}.
        :param errorReporter:
        :param codeMaps:
        """
        """ generated source for method __init__ """
        self.errorReporter = errorReporter
        self.codeMaps = dict(codeMaps)

    def doValidate(self, context):
        """
        Validate this Validator's group of generated files.
        :param context: The context of the current build.
        :return:
        """
        if not self.validationEnabled(context):
            return
        tasks = []
        for it in self.getValidationStrategies():
            tasks.append(it.second.run(context.getCancelIndicator()))

        for f in self.getFutures(tasks):
            f.get().first.getErrorReportingStrategy().report(str(f.get().second.getErrors()),
                                                             self.errorReporter, self.codeMaps)
            f.get().first.getOutputReportingStrategy().report(str(f.get().second.getOutput()),
                                                              self.errorReporter, self.codeMaps)

    def validationEnabled(self, context):
        """ generated source for method validationEnabled """
        return context.getArgs().containsKey("lint") or self.validationEnabledByDefault(context)

    def validationEnabledByDefault(self, context):
        """ generated source for method validationEnabledByDefault """
        return context.getMode() != LFGeneratorContext.Mode.STANDALONE

    @classmethod
    def getFutures(cls, tasks):
        """ generated source for method getFutures """
        futures = list()
        if len(tasks) == 0:
            pass
        elif len(tasks) == 1:
            try:
                futures = list(CompletableFuture.completedFuture(tasks.get(0).call()))
            except Exception as e:
                sys.stderr.write(e.getMessage())
        else:
            service = Executors.newFixedThreadPool(min(Runtime.getRuntime().availableProcessors(), len(tasks)))
            futures = service.invokeAll(tasks)
            service.shutdown()
        return futures

    def run(self, command, cancelIndicator):
        """ generated source for method run """
        returnCode = command.run(cancelIndicator)
        self.getBuildReportingStrategies().first.report(command.getErrors().__str__(), self.errorReporter, self.codeMaps)
        self.getBuildReportingStrategies().second.report(command.getOutput().__str__(), self.errorReporter, self.codeMaps)
        return returnCode

    def getValidationStrategies(self):
        """ generated source for method getValidationStrategies """
        commands = []
        mostRecentDateModified = 0.0
        for generatedFile in self.codeMaps.keySet():
            if generatedFile.toFile().lastModified() > mostRecentDateModified - self.FILE_AGE_THRESHOLD_MILLIS:
                p = self.getValidationStrategy(generatedFile)
                if p.first == None or p.second == None:
                    continue 
                commands.append(p)
                if p.first.isFullBatch():
                    break
        return commands

    def getValidationStrategy(self, generatedFile):
        """ generated source for method getValidationStrategy """
        sorted = []
        for strategy in sorted:
            validateCommand = strategy.getCommand(generatedFile)
            if validateCommand != None:
                return self.Pair(strategy, validateCommand)
        return self.Pair(None, None)

    def getPossibleStrategies(self):
        """ generated source for method getPossibleStrategies """

    def getBuildReportingStrategies(self):
        """ generated source for method getBuildReportingStrategies """
