#!/usr/bin/env python
""" generated source for module ValidationStrategy """
from abc import ABCMeta, abstractmethod
# package: org.lflang.generator
# import java.nio.file.Path

from org.lflang.util.LFCommand

# 
#  * A means of validating generated code.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class ValidationStrategy:
    """ generated source for interface ValidationStrategy """
    __metaclass__ = ABCMeta
    #      * Return the command that produces validation output in association
    #      * with {@code generatedFile}, or {@code null} if this strategy has no
    #      * command that will successfully produce validation output.
    #      
    @abstractmethod
    def getCommand(self, generatedFile):
        """ generated source for method getCommand """

    #      * Return a strategy for parsing the stderr of the validation command.
    #      * @return A strategy for parsing the stderr of the validation command.
    #      
    @abstractmethod
    def getErrorReportingStrategy(self):
        """ generated source for method getErrorReportingStrategy """

    #      * Return a strategy for parsing the stdout of the validation command.
    #      * @return A strategy for parsing the stdout of the validation command.
    #      
    @abstractmethod
    def getOutputReportingStrategy(self):
        """ generated source for method getOutputReportingStrategy """

    #      * Return whether this strategy validates all generated files, as
    #      * opposed to just the given one.
    #      * @return whether this strategy validates all generated files
    #      
    @abstractmethod
    def isFullBatch(self):
        """ generated source for method isFullBatch """

    #      * Return the priority of this. Strategies with higher
    #      * priorities are more likely to be used.
    #      * @return The priority of this.
    #      
    @abstractmethod
    def getPriority(self):
        """ generated source for method getPriority """
