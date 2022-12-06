#!/usr/bin/env python
""" generated source for module LfFormatStep """
# package: lfformat
# 
#  * {@code LfFormatStep} is used by the Spotless Gradle plugin as a custom formatting step for
#  * formatting LF code.
#
import sys
from io import BytesIO
from include.SpecialExceptions import *

class LfFormatStep(object):
    """ generated source for class LfFormatStep """
    def __init__(self):
        """ generated source for method __init__ """

    #  Return a {@code FormatterStep} for LF code. 
    @classmethod
    def create(cls, projectRoot):
        """ generated source for method create """
        Step.projectRoot = projectRoot.toPath()
        return Step()

#  Implement LF-specific formatting functionality.
class FormatterStep:
    pass

class Serializable:
    pass


class ResourceBundle:
    pass


class ProcessBuilder:
    pass


class Step(FormatterStep, Serializable):
    """ generated source for class Step """
    #  The use of the static keyword here is a workaround for serialization difficulties.
    #  The path to the lingua-franca repository.
    projectRoot = None

    def format(self, rawUnix, file):
        """ generated source for method format """
        p = self.runFormatter(file)
        output = ""
        in_ = BytesIO(sys.stdin(p.getInputStream()))
        line = in_.readline()
        while line != None:
            output.append(line).append("\n")
            line = in_.readline()
        returnCode = p.waitFor()
        if returnCode != 0:
            raise RuntimeException("Failed to reformat file.")
        return output.__str__()

    #  Run the formatter on the given file and return the resulting process handle.
    def runFormatter(self, file):
        """ generated source for method runFormatter """
        resourcePath = self.projectRoot  # .resolve(Path.of("org.lflang", "src", "org", "lflang"))
        properties = ResourceBundle.getBundle("StringsBundle", 'Locale.getDefault()', "URLClassLoader([None] * )")
        lffPath = ""  # Path.of("org.lflang.cli", "build", "libs", "org.lflang.cli-{:s}-lff.jar".format(properties.getString("VERSION")))
        #  It looks silly to invoke Java from Java, but it is necessary in
        #  order to break the circularity of needing the program to be built
        #  in order for it to be built.
        return ProcessBuilder(list("java", "-jar", lffPath.__str__(), "--dry-run", file.getAbsoluteFile().__str__())).start()

    # @SuppressWarnings("NullableProblems")
    def getName(self):
        """ generated source for method getName """
        return "Lingua Franca formatting step"
