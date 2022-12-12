#!/usr/bin/env python
""" generated source for module CDockerGenerator """
# package: org.lflang.generator.c
# import org.eclipse.xtext.xbase.lib.IterableExtensions
from lflang.diagram.synthesis.LinguaFrancaSynthesis import IterableExtensions
from lflang.generator.DockerGeneratorBase import DockerData, GeneratorData
from org.lflang import FileConfig

from org.lflang import TargetConfig

from org.lflang.generator import DockerGeneratorBase


from org.lflang.util import StringUtil

# 
#  * Generate the docker file related code for the C and CCpp target.
#  *
#  * @author{Hou Seng Wong <housengw@berkeley.edu>}
#  

#      * The interface for data from the C code generator.
#

class CGeneratorData(GeneratorData):
    """ generated source for class CGeneratorData """

    # The name of the LF module in CGenerator.
    # Typically, this is "fileConfig.name + _ + federate.name"
    # in federated execution and "fileConfig.name" in non-federated
    # execution.
    def __init__(self, lfModuleName, federateName, fileConfig):
        """ generated source for method __init__ """
        super().__init__()
        self.lfModuleName = lfModuleName
        self.federateName = federateName
        self.fileConfig = fileConfig

    def getLfModuleName(self):
        """ generated source for method getLfModuleName """
        return self.lfModuleName

    def getFederateName(self):
        """ generated source for method getFederateName """
        return self.federateName

    def getFileConfig(self):
        """ generated source for method getFileConfig """
        return self.fileConfig


class CDockerGenerator(DockerGeneratorBase):
    """ generated source for class CDockerGenerator """
    defaultBaseImage = "alpine:latest"

    def __init__(self, isFederated, CCppMode, targetConfig):
        """ generated source for method __init__ """
        super().__init__(isFederated)
        self.CCppMode = CCppMode
        self.targetConfig = targetConfig

    # Translate data from the code generator to a map.
    #
    # @return data from the code generator put in a Map.
    def fromData(self, lfModuleName, federateName, fileConfig):
        """ generated source for method fromData """
        return self.CGeneratorData(lfModuleName, federateName, fileConfig)

    # Translate data from the code generator to docker data as
    # specified in the DockerData class.
    #
    # @param generatorData Data from the code generator.
    # @return docker data as specified in the DockerData class
    #      
    def generateDockerData(self, generatorData):
        """ generated source for method generateDockerData """
        cGeneratorData = generatorData
        lfModuleName = cGeneratorData.getLfModuleName()
        federateName = cGeneratorData.getFederateName()
        fileConfig = cGeneratorData.getFileConfig()
        dockerFilePath = fileConfig.getSrcGenPath().resolve(lfModuleName + ".Dockerfile")
        dockerFileContent = self.generateDockerFileContent(cGeneratorData)
        dockerBuildContext = federateName if self.isFederated else "."
        return DockerData(dockerFilePath, dockerFileContent, dockerBuildContext)

    # Generate the contents of the docker file.
    #
    # @param generatorData Data from the code generator.
    #      
    def generateDockerFileContent(self, generatorData):
        """ generated source for method generateDockerFileContent """
        lfModuleName = generatorData.getLfModuleName()
        compileCommand = self.generateDefaultCompileCommand() \
            if self.targetConfig.buildCommands is None else " ".join(self.targetConfig.buildCommands)
        compiler = "g++" if self.CCppMode else "gcc"
        baseImage = self.defaultBaseImage if self.targetConfig.dockerOptions.from_ is None else self.targetConfig.dockerOptions.from_
        return "\n".join(["# For instructions, see: https://www.lf-lang.org/docs/handbook/containerized-execution",
                          "FROM " + baseImage + " AS builder",
                          "WORKDIR /lingua-franca/" + lfModuleName,
                          "RUN set -ex && apk add --no-cache " + compiler + " musl-dev cmake make",
                          "COPY . src-gen",
                          compileCommand, "",
                          "FROM " + baseImage,
                          "WORKDIR /lingua-franca",
                          "RUN mkdir bin",
                          "COPY --from=builder /lingua-franca/" + lfModuleName + "/bin/" + lfModuleName + " ./bin/" + lfModuleName,
                          "",
                          "# Use ENTRYPOINT not CMD so that command-line arguments go through",
                          "ENTRYPOINT [\"./bin/" + lfModuleName + "\"]"])

    #      * Return the default compile command for the C docker container.
    #      
    def generateDefaultCompileCommand(self):
        """ generated source for method generateDefaultCompileCommand """
        return "\n".join(["RUN set -ex && \\",
                          "mkdir bin && \\",
                          "cmake -S src-gen -B bin && \\",
                          "cd bin && \\",
                          "make all"])
