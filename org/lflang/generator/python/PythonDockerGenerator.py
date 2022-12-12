#!/usr/bin/env python
""" generated source for module PythonDockerGenerator """
# package: org.lflang.generator.python
from org.lflang import TargetConfig

from org.lflang.generator.c import CDockerGenerator

# 
#  * Generates the docker file related code for the Python target.
#  *
#  * @author{Hou Seng Wong <housengw@berkeley.edu>}
#  
class PythonDockerGenerator(CDockerGenerator):
    """ generated source for class PythonDockerGenerator """
    targetConfig = None
    defaultBaseImage = "python:slim"

    def __init__(self, isFederated, targetConfig):
        """ generated source for method __init__ """
        super().__init__(targetConfig)

    #      * Generates the contents of the docker file.
    #      *
    #      * @param generatorData Data from the code generator.
    #      
    def generateDockerFileContent(self, generatorData):
        """ generated source for method generateDockerFileContent """
        baseImage = self.defaultBaseImage
        return "\n".join([ "# For instructions, see: https://github.com/icyphy/lingua-franca/wiki/Containerized-Execution", "FROM " + baseImage, "WORKDIR /lingua-franca/" + generatorData.getLfModuleName(), "RUN set -ex && apt-get update && apt-get install -y python3-pip", "COPY . src-gen", "RUN cd src-gen && python3 setup.py install && cd ..", "ENTRYPOINT [\"python3\", \"src-gen/" + generatorData.getLfModuleName() + ".py\"]"])
