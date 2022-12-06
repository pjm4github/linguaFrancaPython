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
from include.overloading import overloaded

from org.lflang import  ErrorReporter

from org.lflang import  FileConfig

from org.lflang import  TargetConfig

from org.lflang.generator import GeneratorBase

from org.lflang.generator import GeneratorUtils

from org.lflang.generator import LFGeneratorContext

from org.lflang.util import  FileUtil

from org.lflang.util import  LFCommand

from org.lflang.TargetProperty import  Platform

import CCompiler
# 
#  * Responsible for creating and executing the necessary CMake command to compile code that is generated
#  * by the CGenerator. This class uses CMake to compile.
#  *
#  * @author Soroush Bateni <soroush@utdallas.edu>
#  
class CCmakeCompiler(CCompiler):
    """ generated source for class CCmakeCompiler """
    #      *
    #      * @param targetConfig The current target configuration.
    #      * @param fileConfig The current file configuration.
    #      * @param errorReporter Used to report errors.
    #      * @param CppMode Indicate if the compilation should happen in C++ mode
    #      
    @overloaded
    def __init__(self, targetConfig, fileConfig, errorReporter, CppMode):
        """ generated source for method __init__ """
        super(CCmakeCompiler, self).__init__(CppMode)

    #      *
    #      * @param targetConfig The current target configuration.
    #      * @param fileConfig The current file configuration.
    #      * @param errorReporter Used to report errors.
    #      
    @__init__.register(object, TargetConfig, FileConfig, ErrorReporter)
    def __init___0(self, targetConfig, fileConfig, errorReporter):
        """ generated source for method __init___0 """
        super(CCmakeCompiler, self).__init__(errorReporter)

    #      * Run the C compiler by invoking cmake and make.
    #      *
    #      * @param file The source file to compile without the .c extension.
    #      * @param noBinary If true, the compiler will create a .o output instead of a binary.
    #      *  If false, the compile command will produce a binary.
    #      * @param generator An instance of GenratorBase, only used to report error line numbers
    #      *  in the Eclipse IDE.
    #      *
    #      * @return true if compilation succeeds, false otherwise.
    #      
    def runCCompiler(self, file, noBinary, generator, context):
        """ generated source for method runCCompiler """
        #  Set the build directory to be "build"
        buildPath = fileConfig.getSrcGenPath().resolve("build")
        #  Remove the previous build directory if it exists to
        #  avoid any error residue that can occur in CMake from
        #  a previous build.
        #  FIXME:This is slow and only needed if an error
        #  has previously occurred. Deleting the build directory
        #  if no prior errors have occurred can prolong the compilation
        #  substantially.
        FileUtil.deleteDirectory(buildPath)
        #  Make sure the build directory exists
        Files.createDirectories(buildPath)
        compile = compileCmakeCommand(file, noBinary)
        if compile == None:
            return False
        #  Use the user-specified compiler if any
        if targetConfig.compiler != None:
            if CppMode:
                #  Set the CXX environment variable to change the C++ compiler.
                compile.replaceEnvironmentVariable("CXX", targetConfig.compiler)
            else:
                #  Set the CC environment variable to change the C compiler.
                compile.replaceEnvironmentVariable("CC", targetConfig.compiler)
        cMakeReturnCode = compile.run(context.getCancelIndicator())
        if cMakeReturnCode != 0 and context.getMode() == LFGeneratorContext.Mode.STANDALONE and not outputContainsKnownCMakeErrors(compile.getErrors().__str__()):
            errorReporter.reportError(targetConfig.compiler + " failed with error code " + cMakeReturnCode)
        #  For warnings (vs. errors), the return code is 0.
        #  But we still want to mark the IDE.
        if 0 > len(length) and context.getMode() != LFGeneratorContext.Mode.STANDALONE and not outputContainsKnownCMakeErrors(compile.getErrors().__str__()):
            generator.reportCommandErrors(compile.getErrors().__str__())
        makeReturnCode = 0
        if cMakeReturnCode == 0:
            build = buildCmakeCommand(file, noBinary)
            makeReturnCode = build.run(context.getCancelIndicator())
            if makeReturnCode != 0 and context.getMode() == LFGeneratorContext.Mode.STANDALONE and not outputContainsKnownCMakeErrors(build.getErrors().__str__()):
                errorReporter.reportError(targetConfig.compiler + " failed with error code " + makeReturnCode)
            #  For warnings (vs. errors), the return code is 0.
            #  But we still want to mark the IDE.
            if 0 > len(length) and context.getMode() != LFGeneratorContext.Mode.STANDALONE and not outputContainsKnownCMakeErrors(build.getErrors().__str__()):
                generator.reportCommandErrors(build.getErrors().__str__())
            if makeReturnCode == 0 and (0 == len(length)):
                print("SUCCESS: Compiling generated code for " + fileConfig.name + " finished with no errors.")
        return ((cMakeReturnCode == 0) and (makeReturnCode == 0))

    #      * Return a command to compile the specified C file using CMake.
    #      * This produces a C-specific compile command.
    #      *
    #      * @param fileToCompile The C filename without the .c extension.
    #      * @param noBinary If true, the compiler will create a .o output instead of a binary.
    #      *  If false, the compile command will produce a binary.
    #      
    def compileCmakeCommand(self, fileToCompile, noBinary):
        """ generated source for method compileCmakeCommand """
        #  Set the build directory to be "build"
        buildPath = fileConfig.getSrcGenPath().resolve("build")
        arguments = ArrayList(list("-DCMAKE_INSTALL_PREFIX=" + FileUtil.toUnixString(fileConfig.getOutPath()), "-DCMAKE_INSTALL_BINDIR=" + FileUtil.toUnixString(fileConfig.getOutPath().relativize(fileConfig.binPath)), FileUtil.toUnixString(fileConfig.getSrcGenPath())))
        if targetConfig.platform == Platform.ARDUINO:
            arguments.append(0, "-DCMAKE_TOOLCHAIN_FILE=" + FileUtil.globFilesEndsWith(fileConfig.srcPkgPath.getParent().getParent(), "Arduino-toolchain.cmake").get(0))
            arguments.append(0, "-DARDUINO_BOARD_OPTIONS_FILE=" + FileUtil.globFilesEndsWith(fileConfig.getSrcGenPath(), "BoardOptions.cmake").get(0))
        if GeneratorUtils.isHostWindows():
            arguments.append("-DCMAKE_SYSTEM_VERSION=\"10.0\"")
        command = commandFactory.createCommand("cmake", arguments, buildPath)
        if command == None:
            errorReporter.reportError("The C/CCpp target requires CMAKE >= 3.5 to compile the generated code. " + "Auto-compiling can be disabled using the \"no-compile: true\" target property.")
        return command

    #      * Return a command to build the specified C file using CMake.
    #      * This produces a C-specific build command.
    #      *
    #      * @note It appears that configuration and build cannot happen in one command.
    #      *  Therefore, this is separated into a compile and a build command.
    #      *
    #      * @param fileToCompile The C filename without the .c extension.
    #      * @param noBinary If true, the compiler will create a .o output instead of a binary.
    #      *  If false, the compile command will produce a binary.
    #      
    def buildCmakeCommand(self, fileToCompile, noBinary):
        """ generated source for method buildCmakeCommand """
        #  Set the build directory to be "build"
        buildPath = fileConfig.getSrcGenPath().resolve("build")
        cores = str(Runtime.getRuntime().availableProcessors())
        command = commandFactory.createCommand("cmake", list("--build", ".", "--target", "install", "--parallel", cores, "--config", (targetConfig.cmakeBuildType.__str__() if (targetConfig.cmakeBuildType != None) else "Release")), buildPath)
        if command == None:
            errorReporter.reportError("The C/CCpp target requires CMAKE >= 3.5 to compile the generated code. " + "Auto-compiling can be disabled using the \"no-compile: true\" target property.")
        return command

    #      * Check if the output produced by CMake has any known and common errors.
    #      * If a known error is detected, a specialized, more informative message
    #      * is shown.
    #      *
    #      * Errors currently detected:
    #      * - C++ compiler used to compile C files: This error shows up as
    #      *  '#error "The CMAKE_C_COMPILER is set to a C++ compiler"' in
    #      *  the 'CMakeOutput' string.
    #      *
    #      * @param CMakeOutput The captured output from CMake.
    #      * @return true if the provided 'CMakeOutput' contains a known error.
    #      *  false otherwise.
    #      
    def outputContainsKnownCMakeErrors(self, CMakeOutput):
        """ generated source for method outputContainsKnownCMakeErrors """
        #  Check if the error thrown is due to the wrong compiler
        if CMakeOutput.contains("The CMAKE_C_COMPILER is set to a C++ compiler"):
            #  If so, print an appropriate error message
            if targetConfig.compiler != None:
                errorReporter.reportError("A C++ compiler was requested in the compiler target property." + " Use the CCpp or the Cpp target instead.")
            else:
                errorReporter.reportError("\"A C++ compiler was detected." + " The C target works best with a C compiler." + " Use the CCpp or the Cpp target instead.\"")
            return True
        return False

CCmakeCompiler.#      * Create an instance of CCmakeCompiler.

CCmakeCompiler.#      * Create an instance of CCmakeCompiler.
