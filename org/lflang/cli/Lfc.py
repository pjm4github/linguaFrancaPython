#!/usr/bin/env python
""" generated source for module Lfc """
# 
#  * Stand-alone version of the Lingua Franca compiler (lfc).
#  
# package: org.lflang.cli
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.Arrays
# import java.util.List
# import java.util.Properties
# import java.util.stream.Collectors
# import org.apache.commons.cli.CommandLineParser
# import org.apache.commons.cli.DefaultParser
# import org.apache.commons.cli.HelpFormatter
# import org.apache.commons.cli.Option
# import org.apache.commons.cli.Options
# import org.apache.commons.cli.ParseException
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.generator.GeneratorDelegate
# import org.eclipse.xtext.generator.JavaIoFileSystemAccess
# import org.eclipse.xtext.util.CancelIndicator
import sys
from argparse import HelpFormatter
from enum import Enum

from pyparsing import ParseException

from include.MiscClasses import HashSet, ReportingBackend, DefaultParser, Paths, Files, Io, Option, Options
from include.Multimap import LinkedHashMap
from include.SpecialExceptions import RuntimeException
from include.overloading import overloaded
from lflang.LFast.ToLf import Collectors
from lflang.lf.ActionOrigin import Collections
from org.lflang import ASTUtils

from org.lflang import ErrorReporter

from org.lflang import FileConfig

from org.lflang import LFRuntimeModule

from org.lflang import LFStandaloneSetup

from org.lflang import LocalStrings

from org.lflang.generator import LFGeneratorContext

from org.lflang.generator import MainContext
import CliBase
import LFStandaloneModule
# import com.google.inject.Inject
# import com.google.inject.Injector
#   * Standalone version of the Lingua Franca compiler (lfc).
#  *
#  * @author {Marten Lohstroh <marten@berkeley.edu>}
#  * @author {Christian Menard <christian.menard@tu-dresden.de>}
#

class CLIOption(Enum):
    """
    Supported CLI options.
    <p>
    Stores an Apache Commons CLI Option for each entry, sets it to be
    if required if so specified, and stores whether or not to pass the
    option to the code generator.

    @author Marten Lohstroh <marten@berkeley.edu>
    """
    CLEAN = "c", "clean", False, False, "Clean before building.", True
    COMPILER = None, "target-compiler", True, False, "Target compiler to invoke.", True
    EXTERNAL_RUNTIME_PATH = None, "external-runtime-path", True, False, "Specify an external runtime library to be used by the compiled binary.", True
    FEDERATED = "f", "federated", False, False, "Treat main reactor as federated.", False
    HELP = "h", "help", False, False, "Display this information.", True
    LOGGING = None, "logging", True, False, "The logging level to use by the generated binary", True
    LINT = "l", "lint", False, False, "Enable or disable linting of generated code.", True
    NO_COMPILE = "n", "no-compile", False, False, "Do not invoke target compiler.", True
    OUTPUT_PATH = "o", "output-path", True, False, "Specify the root output directory.", False
    QUIET = "q", "quiet", False, False, "Suppress output of the target compiler and other commands", True
    RTI = "r", "rti", True, False, "Specify the location of the RTI.", True
    RUNTIME_VERSION = None, "runtime-version", True, False, "Specify the version of the runtime library used for compiling LF programs.", True
    SCHEDULER = "s", "scheduler", True, False, "Specify the runtime scheduler (if supported).", True
    THREADING = "t", "threading", True, False, "Specify whether the runtime should use multi-threading (True/False).", True
    VERSION = None, "version", False, False, "Print version information.", False
    WORKERS = "w", "workers", True, False, "Specify the default number of worker threads.", True

    def __init__(self, opt, longOpt, hasArg, isReq, description, passOn):
        """
        Construct a new CLIOption.
        :param opt:         The short option name. E.g.: "f" denotes a flag
                            "-f".
        :param longOpt:     The long option name. E.g.: "foo" denotes a flag
                            "--foo".
        :param hasArg:      Whether or not this option has an argument. E.g.:
                            "--foo bar" where "bar" is the argument value.
        :param isReq:       Whether or not this option is required. If it is
                            required but not specified a menu is shown.
        :param description: The description used in the menu.
        :param passOn:      Whether or not to pass this option as a property
                            to the code generator.
        """
        # The corresponding Apache CLI Option object.
        self.option = Option(opt, longOpt, hasArg, description)
        self.option.setRequired(isReq)
        # Whether to pass this option to the code generator.
        self.passOn = passOn

    def getOptions(self):
        """
        Create an Apache Commons CLI Options object and add all the options.
        :return: Options object that includes all the options in this enum.
        """
        opts = Options()
        for o in [CLIOption.values()]:
            opts.addOption(o.option)
        return opts


    def getPassedOptions(self):
        """
        Return a list of options that are to be passed on to the code
        generator.

        :return: List of options that must be passed on to the code gen stage.
        """
        r = []
        for opt in CLIOption.values():
            if opt.option == opt.passOn:
                r.append(opt)



class Lfc(CliBase):
    """ generated source for class Lfc """

    def __init__(self):
        # Injected code generator.
        self.generator = None
        # Injected file access object.
        self.fileAccess = None

    @classmethod
    def main(cls, args):
        """ generated source for method main """
        reporter = ReportingBackend(Io(), "lfc: ")
        #  Injector used to obtain Main instance.
        injector = LFStandaloneSetup(LFRuntimeModule(), LFStandaloneModule(reporter)).createInjectorAndDoEMFRegistration()
        #  Main instance.
        main = injector.getInstance(Lfc.__class__)
        #  Apache Commons Options object configured to according to available CLI arguments.
        options = CLIOption.getOptions()
        #  CLI arguments parser.
        parser = DefaultParser()
        #  Helper object for printing "help" menu.
        formatter = HelpFormatter()
        try:
            main.cmd = parser.parse(options, args, True)
            #  If requested, print help and abort
            if main.cmd.hasOption(CLIOption.HELP.option.getOpt()):
                formatter.printHelp("lfc", options)
                sys.exit(0)
            #  If requested, print version and abort
            if main.cmd.hasOption(CLIOption.VERSION.option.getLongOpt()):
                print("lfc " + LocalStrings.VERSION)
                sys.exit(0)
            files = main.cmd.getArgList()
            if len(files) < 1:
                reporter.printFatalErrorAndExit("No input files.")
            try:
                paths = files.stream().map(Paths.get).collect(Collectors.toList())
                main.runGenerator(paths, injector)
            except RuntimeException as e:
                reporter.printFatalErrorAndExit("An unexpected error occurred:", e)
        except ParseException as e:
            reporter.printFatalError("Unable to parse commandline arguments. Reason: " + e.getMessage())
            formatter.printHelp("lfc", options)
            sys.exit(1)

    def runGenerator(self, files, injector):
        """ generated source for method runGenerator """
        properties = self.filterProps(CLIOption.getPassedOptions())
        pathOption = CLIOption.OUTPUT_PATH.option.getOpt()
        root = None
        if self.cmd.hasOption(pathOption):
            root = Paths.get(self.cmd.getOptionValue(pathOption)).normalize()
            if not Files.exists(root):
                self.reporter.printFatalErrorAndExit("Output location '" + root + "' does not exist.")
            if not Files.isDirectory(root):
                self.reporter.printFatalErrorAndExit("Output location '" + root + "' is not a directory.")
        for path in files:
            if not Files.exists(path):
                self.reporter.printFatalErrorAndExit(path + ": No such file or directory")
        for path in files:
            path = path.toAbsolutePath()
            pkgRoot = FileConfig.findPackageRoot(path, self.reporter.printWarning)
            resolved = None
            if root != None:
                resolved = root.resolve("src-gen").__str__()
            else:
                resolved = pkgRoot.resolve("src-gen").__str__()
            self.fileAccess.setOutputPath(resolved)
            resource = self.getResource(path)
            if resource == None:
                self.reporter.printFatalErrorAndExit(path + " is not an LF file. Use the .lf file extension to denote LF files.")
            elif self.cmd != None and self.cmd.hasOption(CLIOption.FEDERATED.option.getOpt()):
                if not ASTUtils.makeFederated(resource):
                    self.reporter.printError("Unable to change main reactor to federated reactor.")
            self.validateResource(resource)
            self.exitIfCollectedErrors()
            context = MainContext()
            self.generator.generate(resource, self.fileAccess, context)
            self.exitIfCollectedErrors()
            self.issueCollector.getAllIssues().forEach(self.reporter.printIssue)
            print("Code generation finished.")


if __name__ == '__main__':
    import sys
    Lfc.main(sys.argv)
