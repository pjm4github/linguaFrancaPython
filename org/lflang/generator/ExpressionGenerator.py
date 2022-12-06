#!/usr/bin/env python
""" generated source for module ExpressionGenerator """
from abc import ABCMeta, abstractmethod
from include.overloading import overloaded
# package: org.lflang.generator
# import java.util.List
# import java.util.ArrayList
# import java.util.stream.Collectors

from org.lflang.ASTUtils import ASTUtils

from org.lflang.TimeValue import TimeValue

from org.lflang.lf import Assignment

from org.lflang.lf import Expression

from org.lflang.lf import Instantiation

from org.lflang.lf import Parameter

from org.lflang.lf  import ParameterReference

from org.lflang.lf import StateVar

from org.lflang.lf import Time

from org.lflang import TimeUnit

# 
#  * Encapsulates logic for representing {@code Value}s in a
#  * target language.
#  
class ExpressionGenerator(object):
    """ generated source for class ExpressionGenerator """
    #      * A {@code TimeInTargetLanguage} is a
    #      * target-language-specific time representation
    #      * strategy.
    #      
    class TimeInTargetLanguage(object):
        """ generated source for interface TimeInTargetLanguage """
        __metaclass__ = ABCMeta
        @abstractmethod
        def apply(self, t):
            """ generated source for method apply """

    #      * A {@code GetTargetReference} instance is a
    #      * target-language-specific function. It provides the
    #      * target language code that refers to the given
    #      * parameter {@code param}.
    #      
    class GetTargetReference(object):
        """ generated source for interface GetTargetReference """
        __metaclass__ = ABCMeta
        @abstractmethod
        def apply(self, param):
            """ generated source for method apply """

    #      * Instantiates a target-language-specific
    #      * ExpressionGenerator parameterized by {@code f}.
    #      * @param f a time representation strategy
    #      
    def __init__(self, f, g):
        """ generated source for method __init__ """
        self.timeInTargetLanguage = f
        self.getTargetReference = g

    #      * Create a list of state initializers in target code.
    #      *
    #      * @param state The state variable to create initializers for
    #      * @return A list of initializers in target code
    #      
    @overloaded
    def getInitializerList(self, state):
        """ generated source for method getInitializerList """
        list = []
        #  FIXME: Previously, we returned null if it was not initialized, which would have caused an
        #   NPE in TSStateGenerator. Is this the desired behavior?
        if not ASTUtils.isInitialized(state):
            return list
        for expr in state.getInit():
            if isinstance(expr, (ParameterReference)):
                list.append(self.getTargetReference.apply((expr).getParameter()))
            else:
                list.append(self.getTargetValue(expr, ASTUtils.isOfTimeType(state)))
        return list

    @getInitializerList.register(object, Parameter)
    def getInitializerList_0(self, param):
        """
        Create a list of default parameter initializers in target code.

        :param param: The parameter to create initializers for
        :return: A list of initializers in target code
        """
        """ generated source for method getInitializerList_0 """
        list = []
        if param == None:
            return list
        for expr in param.getInit():
            list.append(self.getTargetValue(expr, ASTUtils.isOfTimeType(param)))
        return list

    @getInitializerList.register(object, Parameter, Instantiation)
    def getInitializerList_1(self, param, i):
        """
        Create a list of parameter initializers in target code in the context
        of an reactor instantiation.
        This respects the parameter assignments given in the reactor
        instantiation and falls back to the reactors default initializers
        if no value is assigned to it.

        :param param: The parameter to create initializers for
        :param i:
        :return: A list of initializers in target code
        """

        assignments = []
        for it in i.getParameters():
            if it.getLhs() == param:
                assignments.append(it)
        if len(assignments) == 0:
            #  Case 0: The parameter was not overwritten in the instantiation
            return self.getInitializerList(param)
        #  Case 1: The parameter was overwritten in the instantiation
        list = []
        if assignments.get(0) == None:
            return list
        for expr in assignments.get(0).getRhs():
            list.append(self.getTargetValue(expr, ASTUtils.isOfTimeType(param)))
        return list

    @overloaded
    def getTargetTime(self, t):
        """
        Return the time specified by {@code t}, expressed as
        code that is valid for some target languages.
        :param t:
        :return:
        """
        return self.timeInTargetLanguage.apply(t)

    @getTargetTime.register(object, Time)
    def getTargetTime_0(self, t):
        """
        Return the time specified by {@code t}, expressed as
        code that is valid for some target languages.

        :param t:
        :return:
        """
        return self.timeInTargetLanguage.apply(TimeValue(t.getInterval(), TimeUnit.fromName(t.getUnit())))

    @getTargetTime.register(object, Expression)
    def getTargetTime_1(self, expr):
        """
        Return the time specified by {@code v}, expressed as
        code that is valid for some target languages.
        :param expr:
        :return:
        """
        return self.getTargetValue(expr, True)

    @overloaded
    def getTargetValue(self, expr):
        """
        Get textual representation of an expression in the target language.
        If the value evaluates to 0, it is interpreted as a literal.

        :param expr: A time AST node
        :return: A time string in the target language
        """
        return ASTUtils.toText(expr)

    @getTargetValue.register(object, Expression, bool)
    def getTargetValue_0(self, expr, isTime):
        """
        Get textual representation of an expression in the target language.

        :param expr: A time AST node
        :param isTime: Whether {@code v} is expected to be a time
        :return: A time string in the target language
        """
        """ generated source for method getTargetValue_0 """
        if isinstance(expr, (Time)):
            return self.getTargetTime(expr)
        if isTime and ASTUtils.isZero(expr):
            return self.timeInTargetLanguage.apply(TimeValue.ZERO)
        return ASTUtils.toText(expr)
