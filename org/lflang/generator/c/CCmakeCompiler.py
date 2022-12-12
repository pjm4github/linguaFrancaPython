#!/usr/bin/env python
""" generated source for module CCmakeCompiler """
# 
#  * Copyright (c) 2019-2021, The University of California at Berkeley.
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.generator.c
# import java.io.File
# import java.io.IOException
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.ArrayList
# import java.util.List
import os

from include.overloading import overloaded
from lflang.generator.ReactionInstance import Runtime
from lflang.ErrorReporter import ErrorReporter
from lflang.FileConfig import FileConfig
from lflang.TargetConfig import TargetConfig
from lflang.generator.GeneratorBase import GeneratorBase
from lflang.generator.GeneratorUtils import GeneratorUtils
from lflang.generator.LFGeneratorContext import LFGeneratorContext
from lflang.util.FileUtil import FileUtil
from lflang.util.LFCommand import LFCommand
from lflang.TargetProperty import Platform

import CCompiler
# 
# Responsible for creating and executing the necessary CMake command to compile code that is generated
# by the CGenerator. This class uses CMake to compile.
#
# @author Soroush Bateni <soroush@utdallas.edu>

class CCmakeCompiler(CCompiler):
    """ generated source for class CCmakeCompiler """
    # @param targetConfig The current target configuration.
    # @param fileConfig The current file configuration.
    # @param errorReporter Used to report errors.
    # @param CppMode Indicate if the compilation should happen in C++ mode
    #      
    @overloaded
    def __init__(self, targetConfig, fileConfig, errorReporter, CppMode):
        """ generated source for method __init__ """
        super().__init__(CppMode)
        self.targetCongif = targetConfig
        self.fileConfig = fileConfig
        self.errorReporter = errorReporter

    # @param targetConfig The current target configuration.
    # @param fileConfig The current file configuration.
    # @param errorReporter Used to report errors.
    @__init__.register(object, TargetConfig, FileConfig, ErrorReporter)
    def __init___0(self, targetConfig, fileConfig, errorReporter):
        """ generated source for method __init___0 """
        super().__init__(errorReporter)
        self.targetCongif = targetConfig
        self.fileConfig = fileConfig

    # Run the C compiler by invoking cmake and make.
    # @param file The source file to compile without the .c extension.
    # @param noBinary If true, the compiler will create a .o output instead of a binary.
    #  If false, the compile command will produce a binary.
    # @param generator An instance of GenratorBase, only used to report error line numbers
    #  in the Eclipse IDE.
    #      *
    # @return true if compilation succeeds, false otherwise.
    #      
    def runCCompiler(self, file, noBinary, generator, context):
        """ generated source for method runCCompiler """
        #  Set the build directory to be "build"
        buildPath = self.fileConfig.getSrcGenPath().resolve("build")
        #  Remove the previous build directory if it exists to
        #  avoid any error residue that can occur in CMake from
        #  a previous build.
        #  FIXME:This is slow and only needed if an error
        #  has previously occurred. Deleting the build directory
        #  if no prior errors have occurred can prolong the compilation
        #  substantially.
        FileUtil.deleteDirectory(buildPath)
        #  Make sure the build directory exists
        os.mkdir(buildPath, exists=True)
        compile = self.compileCmakeCommand(file, noBinary)
        if compile == None:
            return False
        #  Use the user-specified compiler if any
        if self.targetConfig.compiler != None:
            if self.CppMode:
                #  Set the CXX environment variable to change the C++ compiler.
                compile.replaceEnvironmentVariable("CXX", self.targetConfig.compiler)
            else:
                #  Set the CC environment variable to change the C compiler.
                compile.replaceEnvironmentVariable("CC", self.targetConfig.compiler)
        cMakeReturnCode = compile.run(context.getCancelIndicator())
        if cMakeReturnCode != 0 and context.getMode() == LFGeneratorContext.Mode.STANDALONE and \
                not self.outputContainsKnownCMakeErrors(compile.getErrors()):
            self.errorReporter.reportError(self.targetConfig.compiler + " failed with error code " + cMakeReturnCode)
        #  For warnings (vs. errors), the return code is 0.
        #  But we still want to mark the IDE.
        if 0 > len(self.length) and context.getMode() != LFGeneratorContext.Mode.STANDALONE and not \
                self.outputContainsKnownCMakeErrors(compile.getErrors()):
            generator.reportCommandErrors(compile.getErrors())
        makeReturnCode = 0
        if cMakeReturnCode == 0:
            build = self.buildCmakeCommand(file, noBinary)
            makeReturnCode = build.run(context.getCancelIndicator())
            if makeReturnCode != 0 and context.getMode() == LFGeneratorContext.Mode.STANDALONE and not \
                    self.outputContainsKnownCMakeErrors(build.getErrors()):
                self.errorReporter.reportError(self.targetConfig.compiler + " failed with error code " + makeReturnCode)
            #  For warnings (vs. errors), the return code is 0.
            #  But we still want to mark the IDE.
            if 0 > len(self.length) and context.getMode() != LFGeneratorContext.Mode.STANDALONE and not \
                    self.outputContainsKnownCMakeErrors(build.getErrors()):
                generator.reportCommandErrors(build.getErrors())
            if makeReturnCode == 0 and (0 == len(self.length)):
                print("SUCCESS: Compiling generated code for " + self.fileConfig.name +
                      " finished with no errors.")
        return ((cMakeReturnCode == 0) and (makeReturnCode == 0))

    # Return a command to compile the specified C file using CMake.
    # This produces a C-specific compile command.
    #      *
    # @param fileToCompile The C filename without the .c extension.
    # @param noBinary If true, the compiler will create a .o output instead of a binary.
    #  If false, the compile command will produce a binary.
    def compileCmakeCommand(self, fileToCompile, noBinary):
        """ generated source for method compileCmakeCommand """
        #  Set the build directory to be "build"
        buildPath = self.fileConfig.getSrcGenPath().resolve("build")
        arguments = ["-DCMAKE_INSTALL_PREFIX=" + FileUtil.toUnixString(self.fileConfig.getOutPath()),
                     "-DCMAKE_INSTALL_BINDIR=" +
                     FileUtil.toUnixString(self.fileConfig.getOutPath().relativize(self.fileConfig.binPath)),
                     FileUtil.toUnixString(self.fileConfig.getSrcGenPath())]
        if self.targetConfig.platform == Platform.ARDUINO:
            arguments.insert(0, ["-DCMAKE_TOOLCHAIN_FILE=" +
                             FileUtil.globFilesEndsWith(self.fileConfig.srcPkgPath.getParent().getParent(),
                                                        "Arduino-toolchain.cmake").get(0)])
            arguments.insert(0, ["-DARDUINO_BOARD_OPTIONS_FILE=" +
                             FileUtil.globFilesEndsWith(self.fileConfig.getSrcGenPath(),
                                                        "BoardOptions.cmake").get(0)])
        if GeneratorUtils.isHostWindows():
            arguments.append(["-DCMAKE_SYSTEM_VERSION=\"10.0\""])
        command = self.commandFactory.createCommand("cmake", arguments, buildPath)
        if command is None:
            self.errorReporter.reportError("The C/CCpp target requires CMAKE >= 3.5 to compile the generated code. " +
                                           "Auto-compiling can be disabled using the \"no-compile: "
                                           "true\" target property.")
        return command

    def buildCmakeCommand(self, fileToCompile, noBinary):
        """
        Return a command to build the specified C file using CMake.
        This produces a C-specific build command.
        @note It appears that configuration and build cannot happen in one command.
        Therefore, this is separated into a compile and a build command.
        :param fileToCompile: The C filename without the .c extension.
        :param noBinary:  If true, the compiler will create a .o output instead of a binary.
                          If false, the compile command will produce a binary.
        :return:
        """
        #  Set the build directory to be "build"
        buildPath = self.fileConfig.getSrcGenPath().resolve("build")
        c = Runtime()
        cores = str(c.getRuntime().availableProcessors())
        command = self.commandFactory.createCommand(
            "cmake",
            ["--build",
             ".",
             "--target",
             "install",
             "--parallel",
             cores,
             "--config",
             self.targetConfig.cmakeBuildType if self.targetConfig.cmakeBuildType is not None else "Release",
             buildPath])
        if command is None:
            self.errorReporter.reportError("The C/CCpp target requires CMAKE >= 3.5 to "
                                           "compile the generated code. " +
                                           "Auto-compiling can be disabled using "
                                           "the \"no-compile: true\" target property.")
        return command

    def outputContainsKnownCMakeErrors(self, CMakeOutput):
        """
        Check if the output produced by CMake has any known and common errors.
        If a known error is detected, a specialized, more informative message
        is shown.
        Errors currently detected:
        - C++ compiler used to compile C files: This error shows up as
         '#error "The CMAKE_C_COMPILER is set to a C++ compiler"' in
         the 'CMakeOutput' string.
        :param CMakeOutput: The captured output from CMake.
        :return: true if the provided 'CMakeOutput' contains a known error.
         false otherwise.
        """
        #  Check if the error thrown is due to the wrong compiler
        if CMakeOutput.contains("The CMAKE_C_COMPILER is set to a C++ compiler"):
            #  If so, print an appropriate error message
            if self.targetConfig.compiler != None:
                self.errorReporter.reportError("A C++ compiler was requested in the compiler target property." + " Use the CCpp or the Cpp target instead.")
            else:
                self.errorReporter.reportError("\"A C++ compiler was detected." + " The C target works best with a C compiler." + " Use the CCpp or the Cpp target instead.\"")
            return True
        return False
