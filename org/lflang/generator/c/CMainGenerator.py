#!/usr/bin/env python
""" generated source for module CMainGenerator """
# package: org.lflang.generator import c
# import java.util.ArrayList
# import java.util.List

from org.lflang import TargetConfig

from org.lflang.generator import CodeBuilder

from org.lflang.util import StringUtil

from org.lflang.TargetProperty import Platform

class CMainGenerator(object):
    """ generated source for class CMainGenerator """
    targetConfig = None

    #  The command to run the generated code if specified in the target directive. 
    runCommand = None

    def __init__(self, targetConfig):
        """ generated source for method __init__ """
        self.targetConfig = targetConfig
        self.runCommand = []
        parseTargetParameters()

    #      * Generate the code that is the entry point
    #      * of the program.
    #      *
    #      * Ideally, this code would belong to its own `main.c`
    #      * file, but it currently lives in the same file
    #      * as all the code generated for reactors.
    #      
    def generateCode(self):
        """ generated source for method generateCode """
        code_ = CodeBuilder()
        code_.pr(generateMainFunction())
        code_.pr(generateSetDefaultCliOption())
        return code_.__str__()

    #      * Generate the `main` function.
    #      
    def generateMainFunction(self):
        """ generated source for method generateMainFunction """
        if self.targetConfig.platform == Platform.ARDUINO:
                    #                 By default, we must have a serial begin line prior to calling lf_reactor_c_main due to internal debugging messages requiring a print buffer.
            #                 For the future, we can check whether internal LF logging is enabled or not before removing this line.
            #                 - Logging
            #             
            return "\n".join([ "// Arduino setup() and loop() functions", "void setup() {", "Serial.begin(" + self.targetConfig.baudRate + ");", "lf_reactor_c_main(0, NULL);", "}", "void loop() {}"])
        return "\n".join([ "int main(int argc, const char* argv[]) {", "    return lf_reactor_c_main(argc, argv);", "}"])

    #      * Generate code that is used to override the
    #      * command line options to the `main` function
    #      
    def generateSetDefaultCliOption(self):
        """ generated source for method generateSetDefaultCliOption """
        #  Generate function to set default command-line options.
        #  A literal array needs to be given outside any function definition,
        #  so start with that.
        return "\n".join([ "const char* _lf_default_argv[] = { " + StringUtil.addDoubleQuotes(StringUtil.joinObjects(self.runCommand, StringUtil.addDoubleQuotes(", "))) + " };", "void _lf_set_default_command_line_options() {", "        default_argc = " + len(self.runCommand) + ";", "        default_argv = _lf_default_argv;", "}") if len(self.runCommand) > 0 else "void _lf_set_default_command_line_options(]) {}"

    #      * Parse the target parameters and set flags to the runCommand
    #      * accordingly.
    #      
    def parseTargetParameters(self):
        """ generated source for method parseTargetParameters """
        if self.targetConfig.fastMode:
            self.runCommand.append("-f")
            self.runCommand.append("true")
        if self.targetConfig.keepalive:
            self.runCommand.append("-k")
            self.runCommand.append("true")
        if self.targetConfig.timeout != None:
            self.runCommand.append("-o")
            self.runCommand.append(self.targetConfig.timeout.getMagnitude() + "")
            self.runCommand.append(self.targetConfig.timeout.unit.getCanonicalName())
        #  The runCommand has a first entry that is ignored but needed.
        if len(self.runCommand) > 0:
            self.runCommand.append(0, "dummy")
