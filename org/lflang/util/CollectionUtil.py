#!/usr/bin/env python
""" generated source for module CollectionUtil """
# package: org.lflang.util
# 
#  * Utilities to manipulate collections.
#  *
#  * <p>Most of these methods are using specialized collection
#  * implementations (possibly unmodifiable) for small collection
#  * sizes. No guarantee is made on the mutability of the collections
#  * returned from these functions, meaning, callers should always
#  * assume they are unmodifiable. Functions that take a collection
#  * parameter as input to produce a new one with a transformation
#  * require the input collection to have been obtained from one of
#  * the utility functions of this class in the first place.
#
from include.overloading import overloaded


class CollectionUtil(object):
    """ generated source for class CollectionUtil """
    #      * Returns a set which contains the elements of the given
    #      * set plus the given element. The returned set should be
    #      * considered unmodifiable.
    #      *
    #      * @param set initial set, nullable
    #      * @param t   new element
    #      * @param <T> Type of elements
    #      * @return A new set, or the same
    #      
    @classmethod
    @overloaded
    def plus(cls, set, t):
        """ generated source for method plus """
        if set == None or set.isEmpty():
            return Set.of(t)
        elif len(set) == 1:
            if set.contains(t):
                return set
            #  make mutable
            set = LinkedHashSet(set)
        #  else it's already mutable.
        set.append(t)
        return set

    @classmethod
    @plus.register(object, Map, K, V)
    def plus_0(cls, map, k, v):
        """ generated source for method plus_0 """
        if map == None or map.isEmpty():
            return Collections.singletonMap(k, v)
        elif len(map) == 1:
            e = map.entrySet().iterator().next()
            if e.getKey() == k:
                return Map.of(k, v)
            map = LinkedHashMap(map)
        map.put(k, v)
        return map

    @classmethod
    def removeFromValues(cls, map, valueToRemove):
        """ generated source for method removeFromValues """
        mapValuesInPlace(map, minus(set, valueToRemove))

    @classmethod
    def mapValuesInPlace(cls, map, mapper):
        """ generated source for method mapValuesInPlace """
        iterator = map.entrySet().iterator()
        while iterator.hasNext():
            e = iterator.next()
            existing = e.getValue()
            mapped = mapper.apply(existing)
            if mapped == None:
                iterator.remove()
            elif mapped != existing:
                e.setValue(mapped)

    @classmethod
    def minus(cls, set, eltToRemove):
        """ generated source for method minus """
        if isinstance(set, (LinkedHashSet)):
            set.remove(eltToRemove)
            return set
        if set == None or set.isEmpty():
            return Collections.emptySet()
        elif len(set) == 1:
            return Collections.emptySet() if set.contains(eltToRemove) else set
        raise AssertionError("should be unreachable")

    @classmethod
    def compute(cls, map, k, computation):
        """ generated source for method compute """
        if map == None or map.isEmpty():
            return Collections.singletonMap((k), computation.apply(k, None))
        elif len(map) == 1:
            e = map.entrySet().iterator().next()
            if e.getKey() == k:
                return Collections.singletonMap((k), computation.apply((k), e.getValue()))
            map = LinkedHashMap(map)
        map.compute(k, computation)
        return map

    @classmethod
    def copy(cls, set):
        """ generated source for method copy """
        if set == None or len(set) <= 1:
            return set
        else:
            return LinkedHashSet(set)

    @classmethod
    def immutableSetOf(cls, first, *rest):
        """ generated source for method immutableSetOf """
        if len(rest):
            return Set.of(first)
        result = {}
        result.append(first)
        result.extend(Arrays.asList(rest))
        return result
