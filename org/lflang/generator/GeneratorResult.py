#!/usr/bin/env python
""" generated source for module GeneratorResult """
from abc import ABCMeta, abstractmethod
# package: org.lflang.generator
# import java.nio.file.Path
# import java.util.Collections
# import java.util.List
# import java.util.Map
# import java.util.function_.Function
from enum import Enum

from include.overloading import overloaded
from lflang.lf.ActionOrigin import Collections
from org.lflang.util.LFCommand import LFCommand

# 
#  * A {@code GeneratorResult} is the outcome of a code generation task.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  

class GetUserMessage:
    """ generated source for interface GetUserMessage """
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply(self, result):
        self.COMPLETED = "Code generation completed." if result.executable is None else f'Code generation complete. The executable is at "{result.executable}".'

#  codeMaps);
#      * A {@code Status} is a level of completion of a code generation task.
#
class Status(Enum):
    """ generated source for enum Status
    * A {@code GetUserMessage} is a function that translates a
    * {@code GeneratorResult} into a human-readable report for the end user.
    """

    NOTHING = ""
    CANCELLED = "Code generation was cancelled."
    FAILED = ""
    GENERATED = GetUserMessage().COMPLETED
    COMPILED = GetUserMessage().COMPLETED
    status = None
    executable = None
    command = None
    codeMaps = None

    #  Initializes a {@code Status} whose {@code GetUserMessage} is {@code gum}.
    def __init__(self, gum):
        """ generated source for method __init__ """
        self.gum = gum


class GeneratorResult:
    """ generated source for class GeneratorResult """


    #      * @param status The level of completion of a code generation task.
    #      * @param executable The file that stores the final output of the code
    #      * generation task. Examples include a fully linked binary or a Python
    #      * file that can be passed to the Python interpreter.
    #      * @param command A command that runs the executable.
    #      * @param codeMaps A mapping from generated files to their CodeMaps.
    #
    @overloaded
    def __init__(self, status, executable, command, codeMaps):
        """ generated source for method __init__ """
        self.status = status if status is not None else self.Status.NOTHING
        self.executable = executable
        self.command = command
        self.codeMaps = codeMaps if codeMaps != None else Collections.emptyMap()
        self.NOTHING = self.incompleteGeneratorResult(Status.NOTHING)
        self.CANCELLED = self.incompleteGeneratorResult(Status.CANCELLED)
        self.FAILED = self.incompleteGeneratorResult(Status.FAILED)
        self.GENERATED_NO_EXECUTABLE = self.completeGeneratorResult(Status.GENERATED)


    #      * Return the result of an incomplete generation task that terminated
    #      * with status {@code status}.
    #      * @return the result of an incomplete generation task that terminated
    #      * with status {@code status}
    #      
    @classmethod
    def incompleteGeneratorResult(cls, status):
        """ generated source for method incompleteGeneratorResult """
        return GeneratorResult(status, None, None, Collections.emptyMap())

    @classmethod
    def completeGeneratorResult(cls, status):
        """ generated source for method incompleteGeneratorResult """
        return GeneratorResult(status, None, None, None)


    #  Return the status of {@code this}.
    def getStatus(self):
        """ generated source for method getStatus """
        return self.status

    #  Return the command needed to execute the executable, or {@code null} if none exists. 
    def getCommand(self):
        """ generated source for method getCommand """
        return self.command

    #  Return the exectuable produced by this build, or {@code null} if none exists. 
    def getExecutable(self):
        """ generated source for method getExecutable """
        return self.executable

    #      * Return a message that can be relayed to the end user about this
    #      * {@code GeneratorResult}.
    #      
    def getUserMessage(self):
        """ generated source for method getUserMessage """
        return self.status.gum.apply(self)

    #      * Return a map from generated sources to their code maps. The
    #      * completeness of this resulting map is given on a best-effort
    #      * basis, but those mappings that it does contain are guaranteed
    #      * to be correct.
    #      * @return An unmodifiable map from generated sources to their
    #      * code maps.
    #      
    def getCodeMaps(self):
        """ generated source for method getCodeMaps """
        return Collections.unmodifiableMap(self.codeMaps)

