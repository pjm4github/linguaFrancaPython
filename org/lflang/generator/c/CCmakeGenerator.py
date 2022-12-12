#!/usr/bin/env python
""" generated source for module CCmakeGenerator """
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
# import java.nio.file.Paths
# import java.util.ArrayList
# import java.util.List
from pathlib import Path

from org.lflang import ErrorReporter
from org.lflang import FileConfig
from org.lflang import TargetConfig
from org.lflang.TargetProperty import Platform
from org.lflang.generator import CodeBuilder
from org.lflang.util import FileUtil

# A helper class that generates a CMakefile that can be used to compile the generated C code.
#
# Adapted from @see org.lflang.generator.CppCmakeGenerator.kt
#
# @author Soroush Bateni <soroush@utdallas.edu>
#  
class CCmakeGenerator:
    """ generated source for class CCmakeGenerator """
    fileConfig = None
    targetConfig = None

    #       *
    # @param targetConfig The TargetConfig instance to use.
    # @param fileConfig The FileConfig instance to use.
    #       
    def __init__(self, targetConfig, fileConfig):
        """ generated source for method __init__ """
        self.fileConfig = fileConfig
        self.targetConfig = targetConfig

    # Generate the contents of a CMakeLists.txt that builds the provided LF C 'sources'. Any error will be
    # reported in the 'errorReporter'.
    #       *
    # @param sources A list of .c files to build.
    # @param executableName The name of the output executable.
    # @param errorReporter Used to report errors.
    # @param CppMode Indicate if the compilation should happen in C++ mode
    # @param hasMain Indicate if the .lf file has a main reactor or not. If not,
    #  a library target will be created instead of an executable.
    # @param cMakeExtras CMake-specific code that should be appended to the CMakeLists.txt.
    # @return The content of the CMakeLists.txt.
    #       
    def generateCMakeCode(self, sources, executableName, errorReporter, CppMode, hasMain, cMakeExtras):
        """ generated source for method generateCMakeCode """
        cMakeCode = CodeBuilder()
        additionalSources = []
        for file in self.targetConfig.compileAdditionalSources:
            relativePath = self.fileConfig.getSrcGenPath().relativize(self.fileConfig.getSrcGenPath().resolve(Path.resolve(file)))
            additionalSources.append(FileUtil.toUnixString(relativePath))
        cMakeCode.newLine()
        cMakeCode.pr("cmake_minimum_required(VERSION 3.13)")
        cMakeCode.pr("project(" + executableName + " LANGUAGES C)")
        cMakeCode.newLine()
        cMakeCode.pr("# Require C11")
        cMakeCode.pr("set(CMAKE_C_STANDARD 11)")
        cMakeCode.pr("set(CMAKE_C_STANDARD_REQUIRED ON)")
        cMakeCode.newLine()
        cMakeCode.pr("# Require C++17")
        cMakeCode.pr("set(CMAKE_CXX_STANDARD 17)")
        cMakeCode.pr("set(CMAKE_CXX_STANDARD_REQUIRED ON)")
        cMakeCode.newLine()
        #  Set the build type
        cMakeCode.pr("set(DEFAULT_BUILD_TYPE " + self.targetConfig.cmakeBuildType + ")\n")
        cMakeCode.pr("if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)\n")
        cMakeCode.pr("    set(CMAKE_BUILD_TYPE ${DEFAULT_BUILD_TYPE} CACHE STRING \"Choose the type of build.\" FORCE)\n")
        cMakeCode.pr("endif()\n")
        cMakeCode.newLine()
        cMakeCode.pr("set(CoreLib core)")
        cMakeCode.pr("set(PlatformLib platform)")
        cMakeCode.newLine()
        if CppMode:
            #  Suppress warnings about const char*.
            cMakeCode.pr("set(CMAKE_CXX_FLAGS \"${CMAKE_CXX_FLAGS} -Wno-write-strings\")")
            cMakeCode.newLine()
        if self.targetConfig.platform != Platform.AUTO:
            cMakeCode.pr("set(CMAKE_SYSTEM_NAME " + self.targetConfig.platform.getcMakeName() + ")")
        cMakeCode.pr("include(${CoreLib}/platform/Platform.cmake)")
        cMakeCode.newLine()
        cMakeCode.pr("include_directories(${CoreLib})")
        cMakeCode.pr("include_directories(${CoreLib}/platform)")
        cMakeCode.pr("include_directories(${CoreLib}/federated)")
        cMakeCode.newLine()
        cMakeCode.pr("set(LF_MAIN_TARGET " + executableName + ")")
        cMakeCode.newLine()
        if hasMain:
            cMakeCode.pr("# Declare a new executable target and list all its sources")
            cMakeCode.pr("add_executable(")
        else:
            cMakeCode.pr("# Declare a new library target and list all its sources")
            cMakeCode.pr("add_library(")
        cMakeCode.indent()
        cMakeCode.pr("${LF_MAIN_TARGET}")
        sources.forEach(cMakeCode.pr)
        cMakeCode.pr("${CoreLib}/platform/${LF_PLATFORM_FILE}")
        additionalSources.forEach(cMakeCode.pr)
        cMakeCode.unindent()
        cMakeCode.pr(")")
        cMakeCode.newLine()
        if self.targetConfig.threading or self.targetConfig.tracing != None:
            #  If threaded computation is requested, add the threads option.
            cMakeCode.pr("# Find threads and link to it")
            cMakeCode.pr("find_package(Threads REQUIRED)")
            cMakeCode.pr("target_link_libraries( ${LF_MAIN_TARGET} Threads::Threads)")
            cMakeCode.newLine()
            #  If the LF program itself is threaded or if tracing is enabled, we need to define
            #  NUMBER_OF_WORKERS so that platform-specific C files will contain the appropriate functions
            cMakeCode.pr("# Set the number of workers to enable threading")
            cMakeCode.pr("target_compile_definitions( ${LF_MAIN_TARGET} PUBLIC NUMBER_OF_WORKERS=" + self.targetConfig.workers + ")")
            cMakeCode.newLine()
        cMakeCode.pr("# Target definitions\n")
        #          targetConfig.compileDefinitions.forEach( (key, value) -> {
        #              cMakeCode.pr("target_compile_definitions( ${LF_MAIN_TARGET} PUBLIC "+key+"="+value+")\n");
        #          });
        cMakeCode.newLine()
        #  Check if CppMode is enabled
        if CppMode:
            #  First enable the CXX language
            cMakeCode.pr("enable_language(CXX)")
            #  FIXME: Instead of mixing a C compiler and a C++ compiler, we use a
            #  CMake flag to set the language of all .c files to C++.
            #  Also convert any additional sources. This is a deprecated functionality
            #  in clang, but intermingling C compiled code and C++ compiled code seems
            #  to require a substantial overhaul of the C target code structure. Instead,
            #  we force the usage of a C++ compiler on everything for now.
            for source in additionalSources:
                cMakeCode.pr("set_source_files_properties( " + source + " PROPERTIES LANGUAGE CXX)")
            cMakeCode.pr("set_source_files_properties(${CoreLib}/platform/${LF_PLATFORM_FILE} PROPERTIES LANGUAGE CXX)")
            cMakeCode.newLine()
        if self.targetConfig.compiler != None and not self.targetConfig.compiler.isBlank():
            if CppMode:
                #  Set the CXX compiler to what the user has requested.
                cMakeCode.pr("set(CMAKE_CXX_COMPILER " + self.targetConfig.compiler + ")")
            else:
                cMakeCode.pr("set(CMAKE_C_COMPILER " + self.targetConfig.compiler + ")")
            cMakeCode.newLine()
        #  Set the compiler flags
        #  We can detect a few common libraries and use the proper target_link_libraries to find them
        for compilerFlag in self.targetConfig.compilerFlags:
            if compilerFlag.trim() == "-lm":
                cMakeCode.pr("target_link_libraries( ${LF_MAIN_TARGET} m)")
            elif compilerFlag.trim() == "-lprotobuf-c":
                cMakeCode.pr("include(FindPackageHandleStandardArgs)")
                cMakeCode.pr("FIND_PATH( PROTOBUF_INCLUDE_DIR protobuf-c/protobuf-c.h)")
                #  cMakeCode.pr("\n find_library(PROTOBUF_LIBRARY\s\n NAMES libprotobuf-c.a libprotobuf-c.so libprotobuf-c.dylib protobuf-c.lib protobuf-c.dll\n)");
                cMakeCode.pr("find_package_handle_standard_args(libprotobuf-c DEFAULT_MSG PROTOBUF_INCLUDE_DIR PROTOBUF_LIBRARY)")
                cMakeCode.pr("target_include_directories( ${LF_MAIN_TARGET} PUBLIC ${PROTOBUF_INCLUDE_DIR} )")
                cMakeCode.pr("target_link_libraries( ${LF_MAIN_TARGET} ${PROTOBUF_LIBRARY})")
            elif compilerFlag.trim() == "-O2":
                if self.targetConfig.compiler == "gcc" or CppMode:
                    #  Workaround for the pre-added -O2 option in the CGenerator.
                    #  This flag is specific to gcc/g++ and the clang compiler
                    cMakeCode.pr("add_compile_options( -O2 )")
                    cMakeCode.pr("add_link_options( -O2 )")
            else:
                errorReporter.reportWarning("Using the flags target property with cmake is dangerous.\n" + " Use cmake-include instead.")
                cMakeCode.pr("add_compile_options( " + compilerFlag + " )")
                cMakeCode.pr("add_link_options( " + compilerFlag + ")")
        cMakeCode.newLine()
        #  Add the install option
        cMakeCode.pr("install(")
        cMakeCode.indent()
        cMakeCode.pr("TARGETS ${LF_MAIN_TARGET}")
        cMakeCode.pr("RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}")
        cMakeCode.unindent()
        cMakeCode.pr(")")
        cMakeCode.newLine()
        if self.targetConfig.platform == Platform.ARDUINO:
            cMakeCode.pr("target_link_arduino_libraries ( ${LF_MAIN_TARGET} PRIVATE core)")
            cMakeCode.pr("target_enable_arduino_upload(${LF_MAIN_TARGET})")
        #  Add the include file
        for includeFile in self.targetConfig.cmakeIncludesWithoutPath:
            cMakeCode.pr("include(\"" + includeFile + "\")")
        cMakeCode.newLine()
        cMakeCode.pr(cMakeExtras)
        cMakeCode.newLine()
        return cMakeCode
