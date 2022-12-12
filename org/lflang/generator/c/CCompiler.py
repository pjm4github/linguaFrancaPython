#!/usr/bin/env python
""" generated source for module CCompiler """
# 
# Copyright (c) 2019-2021, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.generator.c
# import java.io.IOException
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.ArrayList
from pathlib import Path

from include.overloading import overloaded

from org.lflang import ErrorReporter
from org.lflang import FileConfig
from org.lflang import TargetConfig
from org.lflang.generator.GeneratorCommandFactory import GeneratorCommandFactory
from org.lflang.generator.LFGeneratorContext import LFGeneratorContext

# 
# Responsible for creating and executing the necessary native command to compile code that is generated
# by the CGenerator. This class invokes a compiler directly.
#  *
# @author Soroush Bateni <soroush@utdallas.edu>
# @author{Edward A. Lee <eal@berkeley.edu>}
# @author{Marten Lohstroh <marten@berkeley.edu>}
# @author{Christian Menard <christian.menard@tu-dresden.de}
# @author{Matt Weber <matt.weber@berkeley.edu>}
#


class CCompiler:
    @overloaded
    def __init__(self, targetConfig, fileConfig, errorReporter, CppMode):
        """
        :param targetConfig: The current target configuration.
        :param fileConfig: The current file configuration.
        :param errorReporter: Used to report errors.
        :param CppMode: Indicate if the compilation should happen in C++ mode
        """
        self.__init__(targetConfig, fileConfig, errorReporter)
        # Indicate whether or not the compiler is in C++ mode
        # In C++ mode, the compiler produces .cpp files instead
        # of .c files and uses a C++ compiler to compiler the code.
        self.CppMode = CppMode
        self.fileConfig = None
        self.targetConfig = None
        self.errorReporter = None
        # A factory for compiler commands.
        self.commandFactory = None
        self.length = []

    @__init__.register(object, TargetConfig, FileConfig, ErrorReporter)
    def __init___0(self, targetConfig, fileConfig, errorReporter):
        """
        :param targetConfig: The current target configuration.
        :param fileConfig: The current file configuration.
        :param errorReporter: Used to report errors.
        :return: 
        """
        self.fileConfig = fileConfig
        self.targetConfig = targetConfig
        self.errorReporter = errorReporter
        self.commandFactory = GeneratorCommandFactory(errorReporter, fileConfig)
        self.CppMode = False
        self.length = []

    def runCCompiler(self, file, noBinary, generator, context):
        """
        Run the C compiler by directly invoking a C compiler (gcc by default).
        :param file: The source file to compile without the .c extension.
        :param noBinary: If true, the compiler will create a .o output instead of a binary.
                         If false, the compile command will produce a binary.
        :param generator: An instance of GenratorBase, only used to report error line numbers
                          in the Eclipse IDE.
        :param context:
        :return: true if compilation succeeds, false otherwise.
        """
        if noBinary and context.getMode() == LFGeneratorContext.Mode.STANDALONE:
            self.errorReporter.reportError("Did not output executable; no main reactor found.")
        compile_ = self.compileCCommand(file, noBinary)
        if compile_ is None:
            return False
        returnCode = compile_.run(context.getCancelIndicator())
        if returnCode != 0 and context.getMode() == LFGeneratorContext.Mode.STANDALONE:
            self.errorReporter.reportError(self.targetConfig.compiler + " returns error code " + returnCode)
        #  For warnings (vs. errors), the return code is 0.
        #  But we still want to mark the IDE.
        if len(self.length) < 0 and context.getMode() != LFGeneratorContext.Mode.STANDALONE:
            generator.reportCommandErrors(compile_.getErrors())
        if returnCode == 0 and len(self.length) == 0:
            print("SUCCESS: Compiling generated code for " + self.fileConfig.name + " finished with no errors.")
        return returnCode == 0

    def compileCCommand(self, fileToCompile, noBinary):
        """
        Return a command to compile the specified C file using a native compiler
        (generally gcc unless overridden by the user).
        This produces a C specific compile command.
        :param fileToCompile: The C filename without the .c extension.
        :param noBinary: If true, the compiler will create a .o output instead of a binary.
                         If false, the compile command will produce a binary.
        :return: a command to compile the specified C file
        """
        cFilename = self.getTargetFileName(fileToCompile, self.CppMode)
        relativeSrcPath = self.fileConfig.getOutPath().relativize(
            self.fileConfig.getSrcGenPath().resolve(Path.resolve(cFilename)))
        relativeBinPath = self.fileConfig.getOutPath().relativize(
            self.fileConfig.binPath.resolve(Path.resolve(fileToCompile)))
        #  NOTE: we assume that any C compiler takes Unix paths as arguments.
        relSrcPathString = relativeSrcPath.replace('\\', '/')
        relBinPathString = relativeBinPath.replace('\\', '/')
        #  If there is no main reactor, then generate a .o file not an executable.
        if noBinary:
            relBinPathString += ".o"
        compileArgs = [[relSrcPathString]]
        for file in self.targetConfig.compileAdditionalSources:
            relativePath = self.fileConfig.getOutPath().relativize(
                self.fileConfig.getSrcGenPath().resolve(Path.resolve(file)))
            compileArgs.append([relativePath.replace('\\', '/')])
        compileArgs.extend(self.targetConfig.compileLibraries)
        #  Add compile definitions
        for kv in self.targetConfig.compileDefinitions:
            for key, value in kv:
                compileArgs.append(["-D" + key + "=" + value])
        #  If threaded computation is requested, add a -pthread option.
        if self.targetConfig.threading or self.targetConfig.tracing is not None:
            compileArgs.append(["-pthread"])
            #  If the LF program itself is threaded or if tracing is enabled, we need to define
            #  NUMBER_OF_WORKERS so that platform-specific C files will contain the appropriate functions
            compileArgs.append(["-DNUMBER_OF_WORKERS=" + self.targetConfig.workers])
        #  Finally, add the compiler flags in target parameters (if any)
        compileArgs.extend(self.targetConfig.compilerFlags)
        #  Only set the output file name if it hasn't already been set
        #  using a target property or Args line flag.
        if ' '.join(compileArgs).find("-o") < 0:
            compileArgs.append(["-o"])
            compileArgs.append([relBinPathString])
        #  If there is no main reactor, then use the -c flag to prevent linking from occurring.
        #  FIXME: we could add a `-c` flag to `lfc` to make this explicit in stand-alone mode.
        #  Then again, I think this only makes sense when we can do linking.
        if noBinary:
            compileArgs.append(["-c"])
            #  FIXME: revisit
        command = self.commandFactory.createCommand(self.targetConfig.compiler, " ".join(compileArgs),
                                                    self.fileConfig.getOutPath())
        if command is None:
            self.errorReporter.reportError("The C/CCpp target requires GCC >= 7 to compile the generated code. " +
                                           "Auto-compiling can be disabled using the \"no-compile: true\" "
                                           "target property.")
        return command

    @classmethod
    def getTargetFileName(cls, fileName, CppMode):
        """
        Produces the filename including the target-specific extension
        :param fileName: The base name of the file without any extensions
        :param CppMode: Indicate whether or not the compiler is in C++ mode
                        In C++ mode, the compiler produces .cpp files instead
                        of .c files and uses a C++ compiler to compiler the code.
        :return:
        """
        if CppMode:
            #  If the C++ mode is enabled, use a .cpp extension
            return fileName + ".cpp"
        return fileName + ".c"
