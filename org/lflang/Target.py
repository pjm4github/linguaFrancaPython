#!/usr/bin/env python
""" generated source for module Target """
#  Static information about targets. 
# 
#  * Copyright (c) 2019, The University of California at Berkeley.
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  * 1. Redistributions of source code must retain the above copyright notice,
#  * this list of conditions and the following disclaimer.
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  * this list of conditions and the following disclaimer in the documentation
#  * and/or other materials provided with the distribution.
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
# package: org.lflang
# import java.util.Arrays
# import java.util.Collection
# import java.util.Collections
# import java.util.LinkedHashSet
# import java.util.List
# import java.util.Optional
# import java.util.Set
from org.lflang.lf import TargetDecl

#  
#  * Enumeration of targets and their associated properties. These classes are
#  * written in Java, not Xtend, because the enum implementation in Xtend more
#  * primitive. It is safer to use enums rather than string values since it allows
#  * faulty references to be caught at compile time. Switch statements that take
#  * as input an enum but do not have cases for all members of the enum are also
#  * reported by Xtend with a warning message.
#  * 
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  
class Target:
    """ generated source for enum Target """
    #      * String representation of this target.
    #      
    displayName = None

    #      * Name of package containing Kotlin classes for the target language.
    #      
    packageName = None

    #      * Prefix of names of Kotlin classes for the target language.
    #      
    classNamePrefix = None

    #      * Whether or not this target requires types.
    #      
    requiresTypes = bool()

    #      * Reserved words in the target language.
    #      
    keywords = None

    #      *An unmodifiable list of all known targets.
    #      
    ALL = list(Target.values())

    #      * Private constructor for targets.
    #      *
    #      * @param displayName     String representation of this target.
    #      * @param requiresTypes   Types Whether this target requires type annotations or not.
    #      * @param packageName     Name of package containing Kotlin classes for the target language.
    #      * @param classNamePrefix Prefix of names of Kotlin classes for the target language.
    #      * @param keywords        List of reserved strings in the target language.
    #      
    @overloaded
    def __init__(self, displayName, requiresTypes, packageName, classNamePrefix, keywords):
        """ generated source for method __init__ """
        self.displayName = displayName
        self.requiresTypes = requiresTypes
        self.keywords = Collections.unmodifiableSet(LinkedHashSet(keywords))
        self.packageName = packageName
        self.classNamePrefix = classNamePrefix

    #      * Private constructor for targets without pakcageName and classNamePrefix.
    #      
    @__init__.register(object, str, bool, Collection)
    def __init___0(self, displayName, requiresTypes, keywords):
        """ generated source for method __init___0 """
        self.__init__(displayName, requiresTypes, "N/A", "N/A", keywords)

    #      * Return the target whose {@linkplain #getDisplayName() display name}
    #      * is the given string (modulo character case), or an empty
    #      * optional if there is no such target.
    #      
    @classmethod
    def forName(cls, name):
        """ generated source for method forName """
        return True
        # Arrays.stream(Target.values())
        #       .filter(it -> it.getDisplayName().lower() == name.lower())
        #       .findFirst();

    #      * Return the display name of the target, as it should be
    #      * written in LF code. This is hence a single identifier.
    #      * Eg for {@link #CPP} returns {@code "Cpp"}, for {@link #Python}
    #      * returns {@code "Python"}. Avoid using either {@link #name()}
    #      * or {@link #toString()}, which have unrelated contracts.
    #      
    def getDisplayName(self):
        """ generated source for method getDisplayName """
        return self.displayName

    #      * Returns the conventional directory name for this target.
    #      * This is used to divide e.g. the {@code test} and {@code example}
    #      * directories by target language. For instance, {@code test/Cpp}
    #      * is the path of {@link #CPP}'s test directory, and this
    #      * method returns {@code "Cpp"}.
    #      
    def getDirectoryName(self):
        """ generated source for method getDirectoryName """
        return self.displayName

    #      * Return the description. Avoid depending on this, toString
    #      * is supposed to be debug information. Prefer {@link #getDisplayName()}.
    #      
    def __str__(self):
        """ generated source for method toString """
        return self.displayName

    #      * Returns whether the given identifier is invalid as the
    #      * name of an LF construct. This usually means that the identifier
    #      * is a keyword in the target language. In Rust, many
    #      * keywords may be escaped with the syntax {@code r#keyword},
    #      * and they are considered valid identifiers.
    #      
    def isReservedIdent(self, ident):
        """ generated source for method isReservedIdent """
        return self.keywords.contains(ident)

    #      * Return true if the target supports multiports and banks
    #      * of reactors.
    #      
    def supportsMultiports(self):
        """ generated source for method supportsMultiports """
        if self == C:
            pass
        elif self == CCPP:
            pass
        elif self == CPP:
            pass
        elif self == Python:
            pass
        elif self == Rust:
            pass
        elif self == TS:
            return True
        return False

    #      * Return true if the target supports widths of banks and
    #      * multiports that depend on reactor parameters (not only
    #      * on constants).
    #      
    def supportsParameterizedWidths(self):
        """ generated source for method supportsParameterizedWidths """
        if self == C:
            pass
        elif self == CCPP:
            pass
        elif self == CPP:
            pass
        elif self == Python:
            pass
        elif self == Rust:
            pass
        elif self == TS:
            return True
        return False

    #      * Return true if the keepalive option is set automatically
    #      * for this target if physical actions are detected in the
    #      * program (and keepalive was not explicitly unset by the user).
    #      
    def setsKeepAliveOptionAutomatically(self):
        """ generated source for method setsKeepAliveOptionAutomatically """
        return self != Rust

    #      * Given a string and a list of candidate objects, return the first
    #      * candidate that matches, or null if no candidate matches.
    #      *
    #      * todo move to CollectionUtil (introduced in #442)
    #      *
    #      * @param string     The string to match against candidates.
    #      * @param candidates The candidates to match the string against.
    #      
    @classmethod
    @overloaded
    def match(cls, string, candidates):
        """ generated source for method match """
        #  kotlin: candidates.firstOrNull { it.__str__().lower() == string.lower() }
        for candidate in candidates:
            if candidate.__str__().lower() == string.lower():
                return candidate
        return None

    #      * Given a string and a list of candidate objects, return the first
    #      * candidate that matches, or null if no candidate matches.
    #      *
    #      * todo move to CollectionUtil (introduced in #442)
    #      *
    #      * @param string     The string to match against candidates.
    #      * @param candidates The candidates to match the string against.
    #      
    @classmethod
    @match.register(object, str, T)
    def match_0(cls, string, candidates):
        """ generated source for method match_0 """
        return cls.match(string, Arrays.asList(candidates))

    #      * Return the target constant corresponding to given target
    #      * declaration among. Return a non-null result, will throw
    #      * if invalid.
    #      *
    #      * @throws RuntimeException If no {@link TargetDecl} is present or if it is invalid.
    #      
    @classmethod
    def fromDecl(cls, targetDecl):
        """ generated source for method fromDecl """
        name = targetDecl.__name__
        return Target.forName(name).orElseThrow(RuntimeException("Invalid target name '" + name + "'"))

Target.C = Target("C", True, Arrays.asList("auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long", "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local"), "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long", "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local")

Target.CCPP = Target("CCpp", True, Target.C.keywords)

Target.CPP = Target("Cpp", True, "cpp", "Cpp", Arrays.asList("alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit", "atomic_noexcept", "auto(1)", "bitand", "bitor", "bool", "break", "case", "catch", "char", "char8_t", "char16_t", "char32_t", "class(1)", "compl", "concept", "const", "consteval", "constexpr", "constinit", "const_cast", "continue", "co_await", "co_return", "co_yield", "decltype", "default(1)", "delete(1)", "do", "double", "dynamic_cast", "else", "enum", "explicit", "export(1)(3)", "extern(1)", "false", "float", "for", "friend", "goto", "if", "inline(1)", "int", "long", "mutable(1)", "namespace", "new", "noexcept", "not", "not_eq", "nullptr", "operator", "or", "or_eq", "private", "protected", "public", "reflexpr", "register(2)", "reinterpret_cast", "requires", "return", "short", "signed", "sizeof(1)", "static", "static_assert", "static_cast", "struct(1)", "switch", "synchronized", "template", "this", "thread_local", "throw", "true", "try", "typedef", "typeid", "typename", "union", "unsigned", "using(1)", "virtual", "void", "volatile", "wchar_t", "while", "xor", "xor_eq"), "alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit", "atomic_noexcept", "auto(1)", "bitand", "bitor", "bool", "break", "case", "catch", "char", "char8_t", "char16_t", "char32_t", "class(1)", "compl", "concept", "const", "consteval", "constexpr", "constinit", "const_cast", "continue", "co_await", "co_return", "co_yield", "decltype", "default(1)", "delete(1)", "do", "double", "dynamic_cast", "else", "enum", "explicit", "export(1)(3)", "extern(1)", "false", "float", "for", "friend", "goto", "if", "inline(1)", "int", "long", "mutable(1)", "namespace", "new", "noexcept", "not", "not_eq", "nullptr", "operator", "or", "or_eq", "private", "protected", "public", "reflexpr", "register(2)", "reinterpret_cast", "requires", "return", "short", "signed", "sizeof(1)", "static", "static_assert", "static_cast", "struct(1)", "switch", "synchronized", "template", "this", "thread_local", "throw", "true", "try", "typedef", "typeid", "typename", "union", "unsigned", "using(1)", "virtual", "void", "volatile", "wchar_t", "while", "xor", "xor_eq")

Target.TS = Target("TypeScript", False, "ts", "TS", Arrays.asList("break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function", "if", "import", "in", "instanceof", "new", "null", "return", "super", "switch", "this", "throw", "true", "try", "typeof", "var", "void", "while", "with", "as", "implements", "interface", "let", "package", "private", "protected", "public", "static", "yield", "any", "boolean", "constructor", "declare", "get", "module", "require", "number", "set", "string", "symbol", "type", "from", "of", "TimeUnit", "TimeValue", "Present", "Sched", "Read", "Write", "ReadWrite"), "break", "case", "catch", "class", "const", "continue", "debugger", "default", "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function", "if", "import", "in", "instanceof", "new", "null", "return", "super", "switch", "this", "throw", "true", "try", "typeof", "var", "void", "while", "with", "as", "implements", "interface", "let", "package", "private", "protected", "public", "static", "yield", "any", "boolean", "constructor", "declare", "get", "module", "require", "number", "set", "string", "symbol", "type", "from", "of", "TimeUnit", "TimeValue", "Present", "Sched", "Read", "Write", "ReadWrite")

Target.Python = Target("Python", False, Arrays.asList("and", "as", "assert", "auto", "break", "case", "char", "class", "const", "continue", "def", "default", "del", "do", "double", "elif", "else", "enum", "except", "extern", "False", "finally", "float", "for", "from", "global", "goto", "if", "import", "inline", "int", "in", "is", "lambda", "long", "None", "nonlocal", "not", "or", "pass", "raise", "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "True", "try", "typedef", "union", "unsigned", "void", "volatile", "while", "with", "yield", "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local"), "and", "as", "assert", "auto", "break", "case", "char", "class", "const", "continue", "def", "default", "del", "do", "double", "elif", "else", "enum", "except", "extern", "False", "finally", "float", "for", "from", "global", "goto", "if", "import", "inline", "int", "in", "is", "lambda", "long", "None", "nonlocal", "not", "or", "pass", "raise", "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "True", "try", "typedef", "union", "unsigned", "void", "volatile", "while", "with", "yield", "_Alignas", "_Alignof", "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local")

Target.Rust = Target("Rust", True, "rust", "Rust", Arrays.asList("self", "true", "false"), "self", "true", "false")
