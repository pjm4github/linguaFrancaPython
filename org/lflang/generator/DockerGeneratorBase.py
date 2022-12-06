#!/usr/bin/env python
""" generated source for module DockerGeneratorBase """
import sys
from abc import ABCMeta, abstractmethod

from include.SpecialExceptions import RuntimeException
from include.overloading import overloaded
# package: org.lflang.generator
# import java.io.IOException
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.List
from lflang.generator.CodeBuilder import CodeBuilder

from org.lflang.util.FileUtil import FileUtil

# 
#  * The base class for docker file related code generation.
#  *
#  * The design of abstractions is as follows:
#  *
#  * Docker-facing API
#  * - This ("DockerGeneratorBase") class defines a "DockerData" class
#  *   that specifies the information it needs to generate docker files and
#  *   docker compose files for any target. This is the docker-facing
#  *   API.
#  *
#  * Target Code Generator-facing API
#  * - Each target-specific docker generator implements this class and
#  *   defines in themselves a class that implements the "GeneratorData"
#  *   interface of this class. This is the target code generator-facing API.
#  *
#  * The purpose of this abstraction design is to contain all
#  * docker-specific information inside docker generator classes and
#  * prevent docker-related information from polluting target code generators.
#  *
#  * @author{Hou Seng Wong <housengw@berkeley.edu>}
#  
class DockerGeneratorBase(object):
    """ generated source for class DockerGeneratorBase """
    #      * The docker compose services representing each federate.
    #      * Ideally, this would be a list of Strings instead of a StringBuilder.
    #      
    composeServices = None

    #      * A docker file will be generated for each lingua franca module.
    #      * This maps the name of the LF module to the data related to the docker
    #      * file for that module.
    #      
    dockerDataList = None

    #      * Indicates whether or not the program is federated.
    #      
    isFederated = bool()

    #      * In federated execution, the host of the rti.
    #      
    host = None

    #      * Generates the docker file related code for the Python target.
    #      * The type specified in the following javadoc refers to the
    #      * type of the object stored in `moduleNameToData.get(lfModuleName)`
    #      
    class DockerData(object):
        """ generated source for class DockerData """
            #          * The absolute path to the docker file.
        #          
        filePath = None

            #          * The content of the docker file to be generated.
        #          
        fileContent = None

            #          * The name of the docker compose service for the LF module.
        #          
        composeServiceName = None

            #          * The build context of the docker container.
        #          
        buildContext = None

        def __init__(self, dockerFilePath, dockerFileContent, dockerBuildContext):
            """ generated source for method __init__ """
            if dockerFilePath == None or dockerFileContent == None or dockerBuildContext == None:
                raise RuntimeException("Missing fields in DockerData instance")
            if not dockerFilePath.toFile().isAbsolute():
                raise RuntimeException("Non-absolute docker file path in DockerData instance")
            if not dockerFilePath.__str__().endsWith(".Dockerfile"):
                raise RuntimeException("Docker file path does not end with \".Dockerfile\" in DockerData instance")
            self.filePath = dockerFilePath
            self.fileContent = dockerFileContent
            self.composeServiceName = self.filePath.getFileName().__str__().replace(".Dockerfile", "").lower()
            self.buildContext = dockerBuildContext

        def getFilePath(self):
            """ generated source for method getFilePath """
            return self.filePath

        def getFileContent(self):
            """ generated source for method getFileContent """
            return self.fileContent

        def getComposeServiceName(self):
            """ generated source for method getComposeServiceName """
            return self.composeServiceName

        def getBuildContext(self):
            """ generated source for method getBuildContext """
            return self.buildContext

    class GeneratorData(object):
        """ generated source for interface GeneratorData """
        __metaclass__ = ABCMeta

    def __init__(self, isFederated):
        """ generated source for method __init__ """
        self.dockerDataList = []
        self.composeServices = ""
        self.isFederated = isFederated

    def generateDockerData(self, generatorData):
        """ generated source for method generateDockerData """

    def addFile(self, generatorData):
        """ generated source for method addFile """
        dockerData = self.generateDockerData(generatorData)
        self.dockerDataList.append(dockerData)
        self.appendFederateToDockerComposeServices(dockerData)

    def writeDockerFiles(self, dockerComposeFilePath):
        """ generated source for method writeDockerFiles """
        if not dockerComposeFilePath.getFileName().__str__() == "docker-compose.yml":
            raise RuntimeException("Docker compose file must have the name \"docker-compose.yml\"")
        for dockerData in self.dockerDataList:
            self.writeDockerFile(dockerData)
            print(self.getDockerBuildCommandMsg(dockerComposeFilePath, dockerData))
        print(self.getDockerComposeUpMsg(dockerComposeFilePath))
        if self.isFederated and self.host != None:
            self.appendRtiToDockerComposeServices("lflang/rti:rti", self.host)
        self.writeFederatesDockerComposeFile(dockerComposeFilePath, "lf")

    def writeDockerFile(self, dockerData):
        """ generated source for method writeDockerFile """
        dockerFilePath = dockerData.getFilePath()
        if dockerFilePath.toFile().exists():
            dockerFilePath.toFile().delete()
        FileUtil.writeToFile(dockerData.getFileContent(), dockerFilePath)

    @classmethod
    def getDockerComposeCommand(cls):
        """ generated source for method getDockerComposeCommand """
        OS = sys.getProperty("os.name").lower()
        return "docker-compose" if (OS.indexOf("nux") >= 0) else "docker compose"

    def getDockerBuildCommandMsg(self, dockerComposeFilePath, dockerData):
        """ generated source for method getDockerBuildCommandMsg """
        return "\n".join([ "Dockerfile for " + dockerData.getComposeServiceName() + " written to " + dockerData.getFilePath(),
                           "#####################################",
                           "To build the docker image, go to " + dockerComposeFilePath.getParent() + " and run:",
                           "",
                           "    " + self.getDockerComposeCommand() + " build " + dockerData.getComposeServiceName(),
                           "",
                           "#####################################"])

    def getDockerComposeUpMsg(self, dockerComposeFilePath):
        """ generated source for method getDockerComposeUpMsg """
        return "\n".join([ "#####################################",
                           "To launch the docker container(s), go to " + dockerComposeFilePath.getParent() + " and run:",
                           "",
                           "    " + self.getDockerComposeCommand() + " up",
                           "",
                           "#####################################"])

    def writeFederatesDockerComposeFile(self, dockerComposeFilePath, networkName):
        """ generated source for method writeFederatesDockerComposeFile """
        contents = CodeBuilder()
        contents.pr("\n".join([ "version: \"3.9\"",
                                "services:",
                                self.composeServices.__str__(),
                                "networks:",
                                "    lingua-franca:",
                                "        name: " + networkName]))
        FileUtil.writeToFile(contents.__str__(), dockerComposeFilePath)

    def appendFederateToDockerComposeServices(self, dockerData):
        """ generated source for method appendFederateToDockerComposeServices """
        tab = " ".repeat(4)
        self.composeServices.append(tab + dockerData.getComposeServiceName() + ":\n")
        self.composeServices.append(tab + tab + "build:\n")
        self.composeServices.append(tab + tab + tab + "context: " + dockerData.getBuildContext() + "\n")
        self.composeServices.append(tab + tab + tab + "dockerfile: " + dockerData.getFilePath() + "\n")
        if self.isFederated:
            self.composeServices.append(tab + tab + "command: -i 1\n")

    def appendRtiToDockerComposeServices(self, rtiImageName, hostName):
        """ generated source for method appendRtiToDockerComposeServices """
        tab = " ".repeat(4)
        self.composeServices.append(tab + "rti:\n")
        self.composeServices.append(tab + tab + "image: " + rtiImageName + "\n")
        self.composeServices.append(tab + tab + "hostname: " + hostName + "\n")
        self.composeServices.append(tab + tab + "command: -i 1 -n " + len(self.dockerDataList) + "\n")

    @overloaded
    def setHost(self, host):
        """ generated source for method setHost """
        if host != None:
            self.setHost(host.__str__())

    @setHost.register(object, str)
    def setHost_0(self, host):
        """ generated source for method setHost_0 """
        self.host = host
