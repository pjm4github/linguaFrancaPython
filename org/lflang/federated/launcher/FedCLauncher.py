#!/usr/bin/env python
""" generated source for module FedCLauncher """
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
# package: org.lflang.federated.launcher
# import java.io.File
# import java.io.IOException
import os

from org.lflang import ErrorReporter

from org.lflang import FileConfig

from org.lflang import TargetConfig

from org.lflang.federated import FedFileConfig

from org.lflang.federated import FederateInstance

from org.lflang.generator.c import CCompiler
import FedLauncher
# 
#  * Utility class that can be used to create a launcher for federated LF programs
#  * that are written in C.
#  * 
#  * @author Soroush Bateni <soroush@utdallas.edu>
#  
class FedCLauncher(FedLauncher):

    def __init__(self, targetConfig, fileConfig, errorReporter):
        """
        :param targetConfig: The current target configuration.
        :param fileConfig: The current file configuration.
        :param errorReporter: A error reporter for reporting any errors or warnings during the code generation
        """
        super().__init__(targetConfig, fileConfig, errorReporter)
        self.targetConfig: TargetConfig = None
        self.fileConfig: FileConfig = None
        self.errorReporter:ErrorReporter = None

    def compileCommandForFederate(self, federate):
        """
        Return the compile command for a federate.
        :param federate: The federate to compile.
        :throws IOException:
        """
        localTargetConfig = self.targetConfig
        try:
            fedFileConfig = FedFileConfig(self.fileConfig, federate.name)
        except IOError as e:
            self.errorReporter.reportError("Failed to create file config for federate " + federate.name)
            return ""
        #  FIXME: Hack to add platform support only for linux systems.
        #  We need to fix the CMake build command for remote federates.
        linuxPlatformSupport = "core" + os.sep + "platform" + os.sep + "lf_linux_support.c"
        if not localTargetConfig.compileAdditionalSources.contains(linuxPlatformSupport):
            localTargetConfig.compileAdditionalSources.append(linuxPlatformSupport)
        cCompiler = CCompiler(localTargetConfig, fedFileConfig, self.errorReporter)
        commandToReturn = "\n".join([str(cCompiler.compileCCommand(self.fileConfig.name + "_" + federate.name, False))])
        return commandToReturn


    def executeCommandForRemoteFederate(self, federate):
        """
        Return the command that will execute a remote federate, assuming that the current
        directory is the top-level project folder. This is used to create a launcher script
        for federates.
        :param federate: The federate to execute.
        """
        return "bin/" + self.fileConfig.name + "_" + federate.name + " -i '$FEDERATION_ID'"

    def executeCommandForLocalFederate(self, fileConfig, federate):
        """
        Return the command that will execute a local federate, assuming that the current
        directory is the top-level project folder. This is used to create a launcher script
        for federates.

        :param fileConfig:
        :param federate: The federate to execute.
        :return:
        """
        return fileConfig.binPath.resolve(fileConfig.name) + "_" + federate.name + " -i $FEDERATION_ID"

