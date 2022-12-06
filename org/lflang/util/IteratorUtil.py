#!/usr/bin/env python
""" generated source for module IteratorUtil """
# package: org.lflang.util
# import java.util.Iterator
# import java.util.stream.Stream
# import java.util.stream.StreamSupport
from include.overloading import overloaded

#  * A utility class for Iterator.
#  *
#  * @author Marten Lohstroh
#  * @author Hokeun Kim
#  
class StreamSupport:
    pass


class IteratorUtil(object):
    """ generated source for class IteratorUtil """
    def __init__(self):
        """ generated source for method __init__ """
        #  Don't let anyone instantiate this class.
        pass

    @classmethod
    @overloaded
    def asStream(cls, iterator):
        """
        #      * Turn an iterator into a sequential stream.
        #      *
        #      * @param iterator The iterator to create a sequential stream for.
        #      * @return A stream.
        #

        :param iterator:
        :return:
        """
        """ generated source for method asStream """
        return cls.asStream(iterator, False)

    @classmethod
    def asFilteredStream(cls, iterator, cls_type):
        """
        #      * Given an iterator of type T, turn it into a stream containing only the
        #      * instances of the given class of type S.
        #      *
        #      * @param <T>      The type of elements the iterator iterates over.
        #      * @param <S>      The type of class to filter out instance of.
        #      * @param iterator An iterator of type T.
        #      * @param cls      A given class of type S.
        #      * @return A filtered stream that only has in it instances of the given
        #      *         class.
        #

        :param iterator:
        :param cls:
        :return:
        """

        """ generated source for method asFilteredStream """
        return cls.asStream(iterator, False).filter(cls_type.isInstance).map(cls_type.cast)

    @classmethod
    @asStream.register(object, object, bool)
    def asStream_0(cls, iterator, parallel):
        """ generated source for method asStream_0 """
        iterable = iterator
        return StreamSupport.stream(iterable.spliterator(), parallel)

    @classmethod
    def asIterable(cls, iterator):
        """ generated source for method asIterable """
        return iterator
