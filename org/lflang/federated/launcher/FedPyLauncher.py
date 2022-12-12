#!/usr/bin/env python
""" generated source for module FedPyLauncher """
# 
#  * Copyright (c) 2021, The University of California at Berkeley.
#  * Copyright (c) 2021, The University of Texas at Dallas.
#  * 
#  * Redistribution and use in source and binary forms, with or without
#  * modification, are permitted provided that the following conditions are met:
#  * 
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  * 
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
#  * 
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  * POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.federated.launcher
# from org.lflang import ErrorReporter
#
# from org.lflang import FileConfig
#
# from org.lflang import TargetConfig
#
# from org.lflang.federated import FederateInstance
import FedLauncher
# 
#  * Utility class that can be used to create a launcher for federated LF programs
#  * that are written in Python.
#  * 
#  * @author Soroush Bateni <soroush@utdallas.edu>
#  *


class FedPyLauncher(FedLauncher):
    """ generated source for class FedPyLauncher """
    #      *
    #      * @param targetConfig The current target configuration.
    #      * @param fileConfig The current file configuration.
    #      * @param errorReporter A error reporter for reporting any errors or warnings during the code generation
    #      
    def __init__(self, targetConfig, fileConfig, errorReporter):
        """ generated source for method __init__ """
        super().__init__(targetConfig, fileConfig, errorReporter)

    #      * Return the command that will execute a remote federate, assuming that the current
    #      * directory is the top-level project folder. This is used to create a launcher script
    #      * for federates.
    #      * 
    #      * @param federate The federate to execute.
    #      
    def executeCommandForRemoteFederate(self, federate):
        """ generated source for method executeCommandForRemoteFederate """
        return "python3 src-gen/" + self.fileConfig.name + "/" + federate.name + "/" + self.fileConfig.name + "_" + \
               federate.name + " -i '$FEDERATION_ID'"

    @staticmethod
    def executeCommandForLocalFederate(fileConfig, federate):
        """
        Return the command that will execute a local federate, assuming that the current
        directory is the top-level project folder. This is used to create a launcher script
        for federates.

        :param fileConfig:
        :param federate: The federate to execute
        :return:
        """
        """ generated source for method executeCommandForLocalFederate """
        return "python3 " + fileConfig.getSrcGenPath() + "/" + federate.name + "/" + \
               fileConfig.name + "_" + federate.name + ".py -i $FEDERATION_ID"
