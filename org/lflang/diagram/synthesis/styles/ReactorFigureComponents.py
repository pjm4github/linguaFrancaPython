#!/usr/bin/env python
""" generated source for module ReactorFigureComponents """
# 
#  * Copyright (c) 2020, Kiel University.
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
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
#  * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.diagram.synthesis.styles
# import de.cau.cs.kieler.klighd.krendering.KContainerRendering
# import de.cau.cs.kieler.klighd.krendering.KRendering
# import java.util.List
# import org.eclipse.xtext.xbase.lib.Pure
# import org.eclipse.xtext.xbase.lib.util.ToStringBuilder

class ToStringBuilder:

    def __init__(self, obj):
        self.obj = obj
        self.filters = {}
        self.fields = []


    def hideFieldNames(self):
        """
        Field names will not be included in the output.
        :return:
        """
        pass

    def singleLine(self):
        """
        Fields are printed on a single line, separated by commas instead of newlines
        :return:
        """
        pass

    def skipNulls(self):
        """
        Fields with null values will be excluded from the output
        :return:
        """
        pass

    def addDeclaredFields(self):
        """
        Adds all fields declared directly in the object's class to the output
        :return:
        """
        pass

    def addAllFields(self):
        """
        Adds all fields declared in the object's class and its superclasses to the output.
        :return:
        """
        pass

    def addField(self, fieldName):
        self.fields.append((fieldName, None))


    def add(self, a1, a2 = None):
        if not a2:
            field_name = ''
            value = a1
        else:
            field_name = a1
            value = a2
        self.fields.append((field_name, value))

    def makeFields(self):
        nv_pairs = []
        fields_array = []
        for name in self.fields:
            nv_pairs.append((name, getattr(self.obj, name), self.filters.get(name)))
        for name, value, predicate in nv_pairs:
            if predicate is None or predicate(value):
                fields_array.append(f'{name}={value}')
        return ', '.join(fields_array)

    def toString(self):
        name = type(self).__name__
        fields = self.makeFields()
        return f'<{name}({fields})>'

    def verbatimValues(self):
        """
        By default, Iterables, Arrays and multiline Strings are pretty-printed.
        :return:
        """
        pass


class ReactorFigureComponents(object):
    """ generated source for class ReactorFigureComponents """
    outer = None
    reactor = None
    figures = None

    def __init__(self, outer, reactor, figures):
        """ generated source for method __init__ """
        super(ReactorFigureComponents, self).__init__()
        self.outer = outer
        self.reactor = reactor
        self.figures = figures

    def hashCode(self):
        """ generated source for method hashCode """
        prime = 31
        result = 1
        result = prime * result + (0 if (self.outer == None) else self.outer.hashCode())
        result = prime * result + (0 if (self.reactor == None) else self.reactor.hashCode())
        return prime * result + (0 if (self.figures == None) else self.figures.hashCode())

    def equals(self, obj):
        """ generated source for method equals """
        if self == obj:
            return True
        if obj == None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.outer == None and other.outer != None:
            return False
        elif not self.outer == other.outer:
            return False
        if self.reactor == None and other.reactor != None:
            return False
        elif not self.reactor == other.reactor:
            return False
        if self.figures == None and other.figures != None:
            return False
        elif not self.figures == other.figures:
            return False
        return True

    def __str__(self):
        """ generated source for method toString """
        b = ToStringBuilder(self)
        b.append("outer", self.outer)
        b.append("reactor", self.reactor)
        b.append("figures", self.figures)
        return b.__str__()

    def getOuter(self):
        """ generated source for method getOuter """
        return self.outer

    def getReactor(self):
        """ generated source for method getReactor """
        return self.reactor

    def getFigures(self):
        """ generated source for method getFigures """
        return self.figures
