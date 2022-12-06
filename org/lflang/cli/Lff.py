#!/usr/bin/env python
""" generated source for module Lff """
#  Stand-alone version of the Lingua Franca formatter (lff). 
# package: org.lflang.cli
# import com.google.inject.Injector
# import java.io.IOException
# import java.nio.file.FileAlreadyExistsException
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.Arrays
# import java.util.List
# import java.util.stream.Collectors
# import org.apache.commons.cli.CommandLineParser
# import org.apache.commons.cli.DefaultParser
# import org.apache.commons.cli.HelpFormatter
# import org.apache.commons.cli.Option
# import org.apache.commons.cli.Options
# import org.apache.commons.cli.ParseException
# import org.eclipse.emf.ecore.resource.Resource
import sys
from argparse import HelpFormatter
from enum import Enum

from pyparsing import ParseException

from include.MiscClasses import Option, Options, DefaultParser, ReportingBackend, Io, Paths, Files
from include.SpecialExceptions import RuntimeException, IOException
from lflang.LFast.ToLf import Collectors
from lflang.cli.LFStandaloneModule import LFStandaloneModule
from org.lflang import LFRuntimeModule

from org.lflang import LFStandaloneSetup

from org.lflang import LocalStrings

from org.lflang.LFast import FormattingUtils
from org.lflang.util import FileUtil
import CliBase
# 
#  * Standalone version of the Lingua Franca formatter (lff). Based on lfc.
#  *
#  * @author {Marten Lohstroh <marten@berkeley.edu>}
#  * @author {Christian Menard <christian.menard@tu-dresden.de>}
#  * @author {Billy Bao <billybao@berkeley.edu>}
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
    DRY_RUN = "d", "dry-run",  False,  False, "Send the formatted file contents to stdout without writing to the file system."
    LINE_WRAP = "w", "wrap", True,  False, "Causes the formatter to line wrap the files to a specified length."
    NO_RECURSE = None, "no-recurse",  False,  False, "Do not format files in subdirectories of the specified paths."
    OUTPUT_PATH = "o", "output-path", True,  False, "If specified, outputs all formatted files into this directory instead of overwriting the original files. Subdirectory structure will be preserved."
    VERBOSE = "v", "verbose",  False,  False, "Print more details on files affected."
    HELP = "h", "help",  False,  False, "Display this information."
    VERSION = None, "version",  False,  False, "Print version information."

    def __init__(self, opt, longOpt, hasArg, isReq, description):
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
        :param description: The description used in the menu..
        """
        # The corresponding Apache CLI Option object.
        self.option = Option(opt, longOpt, hasArg, description)
        self.option.setRequired(isReq)

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


class FileAlreadyExistsException:
    pass


class Lff(CliBase):
    """ generated source for class Lff """
    #    * Supported CLI options.
    #    *
    #    * <p>Stores an Apache Commons CLI Option for each entry, sets it to be required if so specified,
    #    * and stores whether to pass the option to the code generator.
    #    *
    #    * @author Marten Lohstroh <marten@berkeley.edu>
    #    * @author {Billy Bao <billybao@berkeley.edu>}
    #    

    # /**
    #  * Main function of the stand-alone compiler.
    #  *
    #  * @param args CLI arguments

    def main(self, args):
        reporter = ReportingBackend(Io(), "lff: ")

        # // Injector used to obtain Main instance.
        injector =LFStandaloneSetup(LFRuntimeModule(), LFStandaloneModule(reporter)).createInjectorAndDoEMFRegistration()
        # // Main instance.
        main = injector.getInstance(self)
        # // Apache Commons Options object configured according to available CLI arguments.
        options = CLIOption.getOptions()
        # // CLI arguments parser.
        parser = DefaultParser()
        # // Helper object for printing "help" menu.
        formatter = HelpFormatter()

        try:
            main.cmd = parser.parse(options, args, True)

            # // If requested, print help and abort
            if (main.cmd.hasOption(CLIOption.HELP.option.getOpt())):
                formatter.printHelp("lff", options)
                sys.exit(0)

            # // If requested, print version and abort
            if (main.cmd.hasOption(CLIOption.VERSION.option.getLongOpt())):
                sys.stdout("lff " + LocalStrings.VERSION)
                sys.exit(0)

            files = main.cmd.getArgList()

            if (files.size() < 1):
                reporter.printFatalErrorAndExit("No input files.")
            try:
                paths = files.stream().map(Paths.get).collect(Collectors.toList())
                main.runFormatter(paths)
            except RuntimeException as e:
                reporter.printFatalErrorAndExit("An unexpected error occurred:" + e)
        except ParseException as e:
            reporter.printFatalError("Unable to parse commandline arguments. Reason: " + e.getMessage())
            formatter.printHelp("lff", options)
            sys.exit(1)

    # /**
    #  * Check all given input paths and the output path, then invokes the formatter on all files given.
    #  */
    def runFormatter(self, files):
        pathOption = CLIOption.OUTPUT_PATH.option.getOpt()
        outputRoot = None
        if self.cmd.hasOption(pathOption):
            outputRoot = Paths.get(self.cmd.getOptionValue(pathOption)).toAbsolutePath().normalize()
        if not Files.exists(outputRoot):
            self.reporter.printFatalErrorAndExit("Output location '" + outputRoot + "' does not exist.")

        if (not Files.isDirectory(outputRoot)):
            self.reporter.printFatalErrorAndExit("Output location '" + outputRoot + "' is not a directory.")

        for path in files:
            if (not Files.exists(path)):
                self.reporter.printFatalErrorAndExit(path + ": No such file or directory")

        lineLength = FormattingUtils.DEFAULT_LINE_LENGTH if not self.cmd.hasOption(CLIOption.LINE_WRAP.option.getOpt()) \
            else int(self.cmd.getOptionValue(CLIOption.LINE_WRAP.option.getOpt()))

        dryRun = self.cmd.hasOption(CLIOption.DRY_RUN.option.getOpt())

        for path in files:
            if self.verbose():
                self.reporter.printInfo("Formatting " + path + ":")
            path = path.toAbsolutePath()
            if Files.isDirectory(path) and not self.cmd.hasOption(CLIOption.NO_RECURSE.option.getLongOpt()):
                self.formatRecursive(Paths.get("."), path, outputRoot, lineLength, dryRun)
            else:
                if outputRoot == None:
                    self.formatSingleFile(path, path, lineLength, dryRun)
                else:
                    self.formatSingleFile(path, outputRoot.resolve(path.getFileName()), lineLength, dryRun)
        if not dryRun or self.verbose():
            self.reporter.printInfo("Done formatting.")

    # /**
    #  * Invoke the formatter on all files in a directory recursively.
    #  *
    #  * @param curPath Current relative path from inputRoot.
    #  * @param inputRoot Root directory of input files.
    #  * @param outputRoot Root output directory.
    #  * @param lineLength The preferred maximum number of columns per line.
    #  */
    def formatRecursive(self, curPath, inputRoot, outputRoot, lineLength, dryRun):
        curDir = inputRoot.resolve(curPath)
        try:
            dirStream = Files.newDirectoryStream(curDir)
            for path in dirStream:
                newPath = curPath.resolve(path.getFileName())
                if Files.isDirectory(path):
                    self.formatRecursive(newPath, inputRoot, outputRoot, lineLength, dryRun)
                else:
                    if outputRoot is None:
                        self.formatSingleFile(path, path, lineLength, dryRun)
                    else:
                        self.formatSingleFile(path, outputRoot.resolve(newPath), lineLength, dryRun)
        except IOException as e:
            self.reporter.printError("Error reading directory " + curDir + ": " + e.getMessage())

    # /** Load and validate a single file, then format it and output to the given outputPath. */
    def formatSingleFile(self, file, outputPath, lineLength, dryRun):
        file = file.normalize()
        outputPath = outputPath.normalize()
        resource = self.getResource(file)
        if resource == None:
            if self.verbose():
                self.reporter.printInfo("Skipped " + file + ": not an LF file")
            return # not an LF file, nothing to do here
        self.validateResource(resource)

        self.exitIfCollectedErrors()
        formattedFileContents =FormattingUtils.render(resource.getContents().get(0), lineLength)

        if (dryRun):
            sys.stdout(formattedFileContents)
        else:
            try:
                FileUtil.writeToFile(formattedFileContents, outputPath, True)
            except IOException as e:
                if isinstance(e, FileAlreadyExistsException):
                    #?         # // only happens if a subdirectory is named with ".lf" at the end
                    self.reporter.printFatalErrorAndExit(
                        "Error writing to "
                        + outputPath
                        + ": file already exists. Make sure that no file or directory"
                        + " within provided input paths have the same relative paths.")
                self.reporter.printFatalErrorAndExit("Error writing to " + outputPath + ": " + e.getMessage())

        self.exitIfCollectedErrors()
        for i in self.issueCollector.getAllIssues():
            self.reporter.printIssue(i)
        if self.verbose():
            msg = "Formatted " + file
            if file != outputPath:
                msg += " -> " + outputPath
                self.reporter.printInfo(msg)

    # /** Return whether the "verbose" flag has been set. */
    def verbose(self):
        return self.cmd.hasOption(CLIOption.VERBOSE.option.getOpt())
