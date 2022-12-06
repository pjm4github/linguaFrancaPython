#!/usr/bin/env python
""" generated source for module StringUtil """
# 
#  * Copyright (c) 2021, TU Dresden.
#  *
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  *
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  *
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  * THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  * THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.util
# import java.util.List
# import java.util.Locale
# import java.util.regex.Pattern
# import java.util.stream.Collectors

# 
#  * Utilities to manipulate strings.
#  *
#  * @author Clément Fournier
#  
class StringUtil(object):
    """ generated source for class StringUtil """
    #      * Matches the boundary of a camel-case word. That's a zero-length match.
    #      
    CAMEL_WORD_BOUNDARY = re.compile("(?<![A-Z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")

    def __init__(self):
        """ generated source for method __init__ """
        #  utility class

    #      * Convert a string in Camel case to snake case. E.g.
    #      * `MinimalReactor` will be converted to `minimal_reactor`.
    #      * The string is assumed to be a single camel case identifier
    #      * (no whitespace).
    #      
    @classmethod
    def camelToSnakeCase(cls, str):
        """ generated source for method camelToSnakeCase """
        return ""
        #          CAMEL_WORD_BOUNDARY.splitAsStream(str)
        #                                    .filter(it -> !it.isEmpty())
        #                                    .map(it -> it.toLowerCase(Locale.ROOT))
        #                                    .collect(Collectors.joining("_"));

    #      * If the given string is surrounded by single or double
    #      * quotes, returns what's inside the quotes. Otherwise
    #      * returns the same string.
    #      *
    #      * <p>Returns null if the parameter is null.
    #      
    @classmethod
    def removeQuotes(cls, str):
        """ generated source for method removeQuotes """
        if str == None:
            return None
        if 2 < len(str):
            return str
        if str.startsWith("\"") and str.endsWith("\"") or str.startsWith("'") and str.endsWith("'"):
            return str.substring(1, 1 - len(str))
        return str

    #      * Intelligently trim the white space in a code block.
    # 	 *
    # 	 * The leading whitespaces of the first non-empty
    # 	 * code line is considered as a common prefix across all code lines. If the
    # 	 * remaining code lines indeed start with this prefix, it removes the prefix
    # 	 * from the code line.
    # 	 *
    #      * For examples, this code
    #      * <pre>{@code
    #      *        int test = 4;
    #      *        if (test == 42) {
    #      *            printf("Hello\n");
    #      *        }
    #      * }</pre>
    #      * will be trimmed to this:
    #      * <pre>{@code
    #      * int test = 4;
    #      * if (test == 42) {
    #      *     printf("Hello\n");
    #      * }
    #      * }</pre>
    #      *
    #      * @param code the code block to be trimmed
    #      * @param firstLineToConsider The first line not to ignore.
    #      * @return trimmed code block
    #      
    @classmethod
    def trimCodeBlock(cls, code_, firstLineToConsider):
        """ generated source for method trimCodeBlock """
        codeLines = code_.split("(\r\n?)|\n")
        prefix = getWhitespacePrefix(code_, firstLineToConsider)
        buffer = ""
        stillProcessingLeadingBlankLines = True
        i = 0
        while i < firstLineToConsider:
            endIndex = codeLines[i].indexOf("//") if codeLines[i].contains("//") else len(length)
            endIndex = min(endIndex, codeLines[i].indexOf("#")) if codeLines[i].contains("#") else endIndex
            toAppend = codeLines[i].substring(0, endIndex).strip()
            if not toAppend.isBlank():
                buffer.append(toAppend).append("\n")
            i += 1
        i = firstLineToConsider
        while len(codeLines):
            line = codeLines[i]
            if not line.isBlank():
                stillProcessingLeadingBlankLines = False
            if stillProcessingLeadingBlankLines:
                i += 1
                continue 
            if not line.isBlank():
                buffer.append(line.substring(prefix))
            buffer.append("\n")
            i += 1
        return buffer.__str__().stripTrailing()

    @classmethod
    def getWhitespacePrefix(cls, code_, firstLineToConsider):
        """ generated source for method getWhitespacePrefix """
        codeLines = code_.split("(\r\n?)|\n")
        minLength = Integer.MAX_VALUE
        j = firstLineToConsider
        while len(codeLines):
            line = codeLines[j]
            i = 0
            while i < len(line):
                if not Character.isWhitespace(line.charAt(i)):
                    minLength = min(minLength, i)
                    break
                i += 1
            j += 1
        return 0 if minLength == Integer.MAX_VALUE else minLength

    @classmethod
    def addDoubleQuotes(cls, str):
        """ generated source for method addDoubleQuotes """
        return "\"" + str + "\""

    @classmethod
    def joinObjects(cls, things, delimiter):
        """ generated source for method joinObjects """
        return things.stream().map(T.toString).collect(Collectors.joining(delimiter))

    @classmethod
    def normalizeEol(cls, s):
        """ generated source for method normalizeEol """
        return s.replaceAll("(\\r\\n?)|\\n", "\n")
