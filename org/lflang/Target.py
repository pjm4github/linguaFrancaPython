#!/usr/bin/env python


#  Static information about targets. 
# 
# Copyright (c) 2019, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang
from enum import Enum
from include.SpecialExceptions import RuntimeException
from include.overloading import overloaded


class Target(Enum):
    """
    Enumeration of targets and their associated properties. These classes are
    written in Java, not Xtend, because the enum implementation in Xtend more
    primitive. It is safer to use enums rather than string values since it allows
    faulty references to be caught at compile time. Switch statements that take
    as input an enum but do not have cases for all members of the enum are also
    reported by Xtend with a warning message.

    @author Marten Lohstroh <marten@berkeley.edu>
    """
    #  List via: https://en.cppreference.com/w/c/keyword
    C = ("C",
         True,
         ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum",
          "extern", "float", "for", "goto", "if", "inline", "int", "long", "register", "restrict", "return", "short",
          "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while",
          "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn",
          "_Static_assert", "_Thread_local"])

    CCPP = ("CCpp", True, C[2])

    CPP = ("Cpp",
           True,
           "cpp",
           "Cpp",
           ["alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit",
            "atomic_noexcept", "auto(1)", "bitand", "bitor", "bool", "break", "case", "catch",
            "char", "char8_t", "char16_t", "char32_t", "class(1)", "compl", "concept",
            "const", "consteval", "constexpr", "constinit", "const_cast", "continue",
            "co_await", "co_return", "co_yield", "decltype", "default(1)", "delete(1)", "do",
            "double", "dynamic_cast", "else", "enum", "explicit", "export(1)(3)", "extern(1)",
            "false", "float", "for", "friend", "goto", "if", "inline(1)", "int", "long",
            "mutable(1)", "namespace", "new", "noexcept", "not", "not_eq", "nullptr",
            "operator", "or", "or_eq", "private", "protected", "public", "reflexpr",
            "register(2)", "reinterpret_cast", "requires", "return", "short", "signed",
            "sizeof(1)", "static", "static_assert", "static_cast", "struct(1)", "switch",
            "synchronized", "template", "this", "thread_local", "throw", "true", "try",
            "typedef", "typeid", "typename", "union", "unsigned", "using(1)", "virtual",
            "void", "volatile", "wchar_t", "while", "xor", "xor_eq"])

    # List via: https://github.com/Microsoft/TypeScript/issues/2536
    TS = ("TypeScript",
          False,
          "ts",
          "TS",
          ["break", "case", "catch", "class", "const", "continue", "debugger", "default",
           "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for",
           "function", "if", "import", "in", "instanceof", "new", "null", "return", "super",
           "switch", "this", "throw", "true", "try", "typeof", "var", "void", "while", "with",
           "as", "implements", "interface", "let", "package", "private", "protected",
           "public", "static", "yield", "any", "boolean", "constructor", "declare", "get",
           # Reactor-TS specific keywords (other classes, which are less user-facing, have double underscores)
           "module", "require", "number", "set", "string", "symbol", "type", "from", "of",
           "TimeUnit", "TimeValue", "Present", "Sched", "Read", "Write", "ReadWrite"])

    # List via: https://www.w3schools.com/python/python_ref_keywords.asp
    # and https://en.cppreference.com/w/c/keyword (due to reliance on the C lib).
    Python = ("Python",
              False,
              ["and", "as", "assert", "auto", "break", "case", "char", "class", "const",
               "continue", "def", "default", "del", "do", "double", "elif", "else", "enum",
               "except", "extern", "False", "finally", "float", "for", "from", "global",
               "goto", "if", "import", "inline", "int", "in", "is", "lambda", "long", "None",
               "nonlocal", "not", "or", "pass", "raise", "register", "restrict", "return",
               "short", "signed", "sizeof", "static", "struct", "switch", "True", "try",
               "typedef", "union", "unsigned", "void", "volatile", "while", "with", "yield",
               "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic",
               "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local"])

    # In our Rust implementation, the only reserved keywords
    # are those that are a valid expression. Others may be escaped
    # with the syntax r#keyword.
    Rust = ("Rust", True, "rust", "Rust", ["self", "true", "false"])

    @overloaded
    def __init__(self, displayName, requiresTypes, packageName, classNamePrefix, keywords):
        """
        :param displayName: String representation of this target.
        :param requiresTypes: Whether or not this target requires types.
        :param packageName: Name of package containing Kotlin classes for the target language.
        :param classNamePrefix: Prefix of names of Kotlin classes for the target language.
        :param keywords: Reserved words in the target language.
        """
        self.displayName = displayName
        self.requiresTypes = requiresTypes
        self.packageName = packageName
        self.classNamePrefix = classNamePrefix
        self.keywords = keywords

    @__init__.register(object, str, bool, list)
    def __init___0(self, displayName, requiresTypes, keywords):
        """
        Short form of private constructor for targets without
        packageName and classNamePrefix.
        :param displayName: String representation of this target.
        :param requiresTypes: Whether or not this target requires types.
        :param keywords: Reserved words in the target language.
        """
        self.__init__(displayName, requiresTypes, "N/A", "N/A", keywords)

    @classmethod
    def forName(cls, name):
        """
        Return the target whose {@linkplain #getDisplayName() display name}
        is the given string (modulo character case), or an empty
        optional if there is no such target.
        """
        for it in Target.values():
            if it.getDisplayName().lower() == name.lower():
                return it.getDisplayName()
        return None

    def getDisplayName(self):
        """
        Return the display name of the target, as it should be
        written in LF code. This is hence a single identifier.
        Eg for {@link #CPP} returns {@code "Cpp"}, for {@link #Python}
        returns {@code "Python"}. Avoid using either {@link #name()}
        or {@link #toString()}, which have unrelated contracts.
        """
        return self.displayName

    def getDirectoryName(self):
        """
        Returns the conventional directory name for this target.
        This is used to divide e.g. the {@code test} and {@code example}
        directories by target language. For instance, {@code test/Cpp}
        is the path of {@link #CPP}'s test directory, and this
        method returns {@code "Cpp"}.
        """
        return self.displayName

    def __str__(self):
        """
        Return the description. Avoid depending on this, toString
        is supposed to be debug information. Prefer {@link #getDisplayName()}.
        """
        return self.displayName

    def isReservedIdent(self, ident):
        """
        Returns whether the given identifier is invalid as the
        name of an LF construct. This usually means that the identifier
        is a keyword in the target language. In Rust, many
        keywords may be escaped with the syntax {@code r#keyword},
        and they are considered valid identifiers.
        """
        return self.keywords.contains(ident)

    def supportsMultiports(self):
        """
        Return true if the target supports multiports and banks
        of reactors.
        """
        if self == self.C:
            return True
        elif self == self.CCPP:
            return True
        elif self == self.CPP:
            return True
        elif self == self.Python:
            return True
        elif self == self.Rust:
            return True
        elif self == self.TS:
            return True
        return False

    def supportsParameterizedWidths(self):
        """
        Return true if the target supports widths of banks and
        multiports that depend on reactor parameters (not only
        on constants).
        """
        if self == self.C:
            return True
        elif self == self.CCPP:
            return True
        elif self == self.CPP:
            return True
        elif self == self.Python:
            return True
        elif self == self.Rust:
            return True
        elif self == self.TS:
            return True
        return False

    def setsKeepAliveOptionAutomatically(self):
        """
        Return true if the keepalive option is set automatically
        for this target if physical actions are detected in the
        program (and keepalive was not explicitly unset by the user).
        """
        return self != self.Rust

    @classmethod
    def match(cls, string, candidates):
        """
        Given a string and a list of candidate objects, return the first
        candidate that matches, or null if no candidate matches.

        TODO: move to CollectionUtil (introduced in #442)

        @param string     The string to match against candidates.
        @param candidates The candidates to match the string against.
        """

        #  kotlin: candidates.firstOrNull { it.__str__().lower() == string.lower() }
        for candidate in candidates:
            if str(candidate).lower() == string.lower():
                return candidate
        return None

    # @classmethod
    # @match.register(object, str, list)
    # def match_0(cls, string, candidates):
    #     """
    #     Given a string and a list of candidate objects, return the first
    #     candidate that matches, or null if no candidate matches.
    #     TODO: move to CollectionUtil (introduced in #442)
    #     @param string     The string to match against candidates.
    #     @param candidates The candidates to match the string against.
    #     """
    #     return cls.match(string, [candidates])

    @classmethod
    def fromDecl(cls, targetDecl):
        """
        Return the target constant corresponding to given target
        declaration among. Return a non-null result, will throw
        if invalid.
        @throws RuntimeException If no {@link TargetDecl} is present or if it is invalid.
        """
        name = targetDecl.__name__
        try:
            n = Target.forName(name)
        except RuntimeException as e:
            raise RuntimeException("Invalid target name '" + name + "'")
        return n

    @classmethod
    def ALL(cls):
        return Target.values()

    @classmethod
    def values(cls):
        return [e.value for e in cls]


if __name__ == "__main__":
    t = Target
    print(t)