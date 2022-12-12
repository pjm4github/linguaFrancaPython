#!/usr/bin/env python
""" generated source for module PythonInfoGenerator """
# package: org.lflang.generator.python
# import java.io.File

from org.lflang import FileConfig

class PythonInfoGenerator:
    """ generated source for class PythonInfoGenerator """
    #      * Print information about necessary steps to install the supporting
    #      * Python C extension for the generated program.
    #      *
    #      * @note Only needed if no-compile is set to true
    #      
    @classmethod
    def generateSetupInfo(cls, fileConfig):
        """ generated source for method generateSetupInfo """
        return "\n".join([ "", "#####################################", "To compile and install the generated code, do:", "    ", "    cd " + fileConfig.getSrcGenPath() + File.separator, "    python3 -m pip install --force-reinstall .", ""])

    #      * Print information on how to execute the generated program.
    #      
    @classmethod
    def generateRunInfo(cls, fileConfig, lfModuleName):
        """ generated source for method generateRunInfo """
        return "\n".join([ "", "#####################################", "To run the generated program, use:", "    ", "    python3 " + fileConfig.getSrcGenPath() + File.separator + lfModuleName + ".py", "", "#####################################", ""])

    #      * Print information on how to execute the generated federation.
    #      
    @classmethod
    def generateFedRunInfo(cls, fileConfig):
        """ generated source for method generateFedRunInfo """
        return "\n".join([ "", "#####################################", "To run the generated program, run:", "    ", "    bash " + fileConfig.binPath + "/" + fileConfig.name, "", "#####################################", ""])
