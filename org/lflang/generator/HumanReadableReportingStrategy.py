#!/usr/bin/env python
""" generated source for module HumanReadableReportingStrategy """
# package: org.lflang.generator
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.Iterator
# import java.util.Map
# import java.util.regex.Matcher
# import java.util.regex.Pattern
# import org.eclipse.lsp4j.DiagnosticSeverity
# import org.eclipse.xtext.xbase.lib.Procedures.Procedure0
# import org.eclipse.xtext.xbase.lib.Procedures.Procedure2
from pathlib import Path

from include.overloading import overloaded
from lflang.generator.DiagnosticReporting import DiagnosticReporting, Strategy
from lflang.generator.Position import Position
from org.lflang import ErrorReporter

# 
#  * An error reporting strategy that parses human-readable
#  * output.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#


class HumanReadableReportingStrategy(DiagnosticReporting, Strategy):
    """ generated source for class HumanReadableReportingStrategy """
    #  A pattern that matches lines that should be reported via this strategy. 
    diagnosticMessagePattern = None

    #  A pattern that matches labels that show the exact range to which the diagnostic pertains. 
    labelPattern = None

    #  The path against which any paths should be resolved. 
    relativeTo = None

    #  The next line to be processed, or {@code null}. 
    bufferedLine = None

    #      * Instantiate a reporting strategy for lines of
    #      * validator output that match {@code diagnosticMessagePattern}.
    #      * @param diagnosticMessagePattern A pattern that matches lines that should be
    #      *          reported via this strategy. This pattern
    #      *          must contain named capturing groups called
    #      *          "path", "line", "column", "message", and
    #      *          "severity".
    #      * @param labelPattern A pattern that matches lines that act as labels, showing
    #      *                     the location of the relevant piece of text. This pattern
    #      *                     must contain two groups, the first of which must match
    #      *                     characters that precede the location given by the "line"
    #      *                     and "column" groups.
    #      
    @overloaded
    def __init__(self, diagnosticMessagePattern, labelPattern):
        """ generated source for method __init__ """
        super().__init__()
        self.__init__(diagnosticMessagePattern, labelPattern, None)

    #      * Instantiate a reporting strategy for lines of
    #      * validator output that match {@code diagnosticMessagePattern}.
    #      * @param diagnosticMessagePattern a pattern that matches lines that should be
    #      *          reported via this strategy. This pattern
    #      *          must contain named capturing groups called
    #      *          "path", "line", "column", "message", and
    #      *          "severity".
    #      * @param labelPattern A pattern that matches lines that act as labels, showing
    #      *                     the location of the relevant piece of text. This pattern
    #      *                     must contain two groups, the first of which must match
    #      *                     characters that precede the location given by the "line"
    #      *                     and "column" groups.
    #      * @param relativeTo The path against which any paths should be resolved.
    #      
    @__init__.register(object, str, str, str)
    def __init___0(self, diagnosticMessagePattern, labelPattern, relativeTo):
        """ generated source for method __init___0 """
        super().__init__()
        for groupName in ["path", "line", "column", "message", "severity"]:
            assert diagnosticMessagePattern.pattern().contains(groupName)
        self.diagnosticMessagePattern = diagnosticMessagePattern
        self.labelPattern = labelPattern
        self.relativeTo = relativeTo
        self.bufferedLine = None

    def report(self, validationOutput, errorReporter, map):
        """ generated source for method report """
        it = validationOutput.lines().iterator()
        while it.hasNext() or self.bufferedLine != None:
            if self.bufferedLine != None:
                self.reportErrorLine(self.bufferedLine, it, errorReporter, map)
                self.bufferedLine = None
            else:
                self.reportErrorLine(it.next(), it, errorReporter, map)

    #      * Report the validation message contained in the given line of text.
    #      * @param line The current line.
    #      * @param it An iterator over the lines that follow the current line.
    #      * @param errorReporter An arbitrary ErrorReporter.
    #      * @param maps A mapping from generated file paths to
    #      *             CodeMaps.
    #      
    def reportErrorLine(self, line, it, errorReporter, maps):
        """ generated source for method reportErrorLine """
        matcher = self.diagnosticMessagePattern.matcher(self.stripEscaped(line))
        if matcher.matches():
            path = Path.resolve(matcher.group("path"))
            generatedFilePosition = Position.fromOneBased(
                int(matcher.group("line")),
                int(matcher.group("column") if matcher.group("column") is not None else "0"))
            message = DiagnosticReporting.messageOf(matcher.group("message"), path, generatedFilePosition)
            map = maps.get(self.relativeTo.resolve(path) if self.relativeTo != None else path)
            severity = DiagnosticReporting.severityOf(matcher.group("severity"))
            if map == None:
                errorReporter.report(None, severity, message)
                return
            for srcFile in map.lfSourcePaths():
                lfFilePosition = map.adjusted(srcFile, generatedFilePosition)
                if matcher.group("column") is not None:
                    (p0, p1) = errorReporter.report(srcFile, severity, message)
                    self.reportAppropriateRange((p0 ,p1), lfFilePosition, it)
                else:
                    errorReporter.report(srcFile, severity, message, lfFilePosition.getOneBasedLine())

    #      * Report the appropriate range to {@code report}.
    #      * @param report A reporting method whose first and
    #      *               second parameters are the (included)
    #      *               start and (excluded) end of the
    #      *               relevant range.
    #      * @param lfFilePosition The point about which the
    #      *                       relevant range is anchored.
    #      * @param it An iterator over the lines immediately
    #      *           following a diagnostic message.
    #      
    def reportAppropriateRange(self, report, lfFilePosition, it):
        """ generated source for method reportAppropriateRange """
        #          Procedure0 failGracefully = () -> report.apply(lfFilePosition, lfFilePosition.plus(" "));
        def failGracefully():
            report.apply(lfFilePosition, lfFilePosition.plus(" "))
        if not it.hasNext():
            failGracefully.apply()
            return
        line = it.next()
        labelMatcher = self.labelPattern.matcher(line)
        if labelMatcher.find():
            report.apply(Position.fromZeroBased(lfFilePosition.getZeroBasedLine(), lfFilePosition.getZeroBasedColumn()
                                                - len(self.length)), lfFilePosition.plus(labelMatcher.group(2)))
            return
        if self.diagnosticMessagePattern.matcher(line).find():
            failGracefully.apply()
            self.bufferedLine = line
            return
        self.reportAppropriateRange(report, lfFilePosition, it)

    #      * Strip the ANSI escape sequences from {@code s}.
    #      * @param s Any string.
    #      * @return {@code s}, with any escape sequences removed.
    #      
    @classmethod
    def stripEscaped(cls, s):
        """ generated source for method stripEscaped """
        return s.replaceAll("\u001B\\[[;\\d]*[ -/]*[@-~]", "")
