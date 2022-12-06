"""An implementation of HashMultimap."""

# Based on https://raw.githubusercontent.com/loggi/python-multimapwithttl/main/multimapwithttl/multimapwithttl.py

from typing import Any, Iterable, Tuple, Generator
from collections import defaultdict


class HashMultimap():
    """
    An implementation of multimap.

    Based on: https://quickleft.com/blog/how-to-create-and-expire-list-items-in-redis/
    without the need for an extra job to delete old items.

    Values are internally stored on Redis using Sorted Sets :

        key1: { (score1, value1), (score2, value2), ... }
        key2: { (score3, value3), (score4, value4), ... }
        ...

    Where the `score` is the timestamp when the value was added.
    We use the timestamp to filter expired values and when an insertion happens,
    we opportunistically garbage collect expired values.
    The key itself is set to expire through redis ttl mechanism together with the newest value.
    These operations result in a simulated multimap with item expiration.

    You can use to keep track of values associated to keys,
    when the value has a notion of expiration.

        > s = HashMultimap('multimap')
        > s.add('a', 1, 2, 3)
        > sorted(s.get('a'))
        [1, 2, 3]
        > s.add_many([('b', (4, 5, 6)), ('c', (7, 8, 9)), ])
        > sorted(sorted(values) for values in s.get_many('a', 'b', 'c')))
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

    def __init__(self, key_prefix = '', *values: Iterable[Any]):
        """
        :param key_prefix:
        :param values:
        """
        self.key_prefix = key_prefix
        self._data = defaultdict(list)
        self._index = None
        if values:
            for k, v in values:
                if k in self._data.keys():
                    self._data[self._get_key(k)].append(v)
                else:
                    self._data[self._get_key(k)] = [v]

    def __str__(self):
        s = []
        for k in self._data:
            s.append(f"{k.split(':')[-1]}:  {self._data[k]}")
        return '\n'.join(s)

    def _get_key(self, name) -> str:
        """Return `name` namespaced with the key prefix, so all keys starts equal."""
        if type(name)==str:
            k = name
        else:
            try:
                k = str(hash(name))
            except TypeError as e:
                raise TypeError(f"HashMultimap must use a hashable key: {e}")
        return f"{self.key_prefix}:{k}"

    def add(self, name, *values) -> None:
        """
        Insert `*values` at the `name` key.

        Args:
            name (hashable object): The key name where `values` should be stored.
            *values: A list of values to be stored at `name`.

        Returns:
            None
        """
        self.add_many([(name, values)])

    def add_many(self, data: Iterable[Tuple[str, Iterable[Any]]]):
        """
        Bulk insert data.

        Args:
            data: An iterator of (key, values) pairs.

            Example:
                HashMultimap('expiringset').add_many([
                    ('a', (1, 2, 3)),
                    ('b', (4, 5, 6)),
                    ('c', (7, 8, 9)),
                ])

        Returns:
            None
        """
        for d in data:
            k, v = d
            key = self._get_key(k)
            if key in self._data.keys():
                self._data[key].append(v)
            else:
                self._data[key] = [v]

    def asMap(self, ):
        """ Returns a map view that associates each key with the corresponding values in the multimap."""
        # Not sure what this does
        return self

    def clear(self, ):
        """ Removes all key-value pairs from the multimap."""
        all_names = self.keys()
        self.delete(all_names)

    def containsEntry(self, key, value):
        """ Returns true if the multimap contains the specified key-value pair."""
        if key in self.keys():
            if self._data[self._get_key(key)] == value:
                return True
        return False

    def containsKey(self, key):
        """ Returns true if the multimap contains any values for the specified key."""
        if key in self.keys():
            return True
        return False

    def containsValue(self, value):
        """ Returns true if the multimap contains the specified value for any key."""
        for key in self.keys():
            if self._data[self._get_key(key)] == value:
                return True
        return False

    def create(self, a, expectedValuesPerKey):
        if expectedValuesPerKey is None:
            # Constructs a LinkedHashMultimap with the same mappings as the specified multimap.
            multimap = a
        else:
            # Constructs an empty LinkedHashMultimap with enough capacity to hold the specified numbers of keys and values without rehashing.

            expectedKeys = a
        pass

    def delete(self, *names) -> None:
        """Delete `*names` from the multimap."""
        for name in names:
            key = self._get_key(name)
            self._data.pop(key)

    def entries(self, ):
        """ Returns a collection of all key-value pairs."""
        return self._data

    def equals(self, other):
        """ Compares the specified  to this multimap for equality."""
        return self.__eq__(other)

    def get(self, *name):
        """
        Returns a collection view of all values associated with a key.
        :param name:
        :return: Returns a generator for the has of the given name list
        """
        # hashed_name = []
        # for n in name:
        #     hashed_name.append(str(hash(n)))
        #return x[0]
        return self.get_many(*name)

    def get_many(self, *names) -> [Any]:
        """
        Return a generator of generators of all values stored at `*names`.

        Args:
            *names: Name of the keys being queried.

        Returns:
            Generator[T]
        """
        for k in names:
            yield self._data[self._get_key(k)]

    def hashCode(self, ):
        """ Returns the hash code for this multimap."""
        return hash(self)

    def isEmpty(self, ):
        """ Returns true if the multimap contains no key-value pairs."""
        return True if len(self.keys())==0 else False

    def keys(self):
        """ Returns a collection, which may contain duplicates, of all keys."""
        r = []
        for k in self._data:
            r.append(f"{k.split(':')[-1]}")
        return r

    def keySet(self):
        """
        Returns the set of all keys, each appearing once in the returned set.
        :return: The string keyset of the hashmap (includes the hashed keys)
        """
        return set(self.keys())

    def remove(self, key, value):
        """ Removes a key-value pair from the multimap."""
        if key in self.keys():
            values = self._data.pop(key)
            new_value = []
            for v in values:
                if v == value:

                    # skip this
                    pass
                else:
                    new_value.append(v)
            self.put(key, new_value)

    def removeAll(self, key):
        """ Removes all values associated with a given key."""
        if key in self.keys():
            self._data.pop(key)
            new_value = []
            self.put(key, new_value)

    def replaceValues(self, key, values):
        """ Stores a collection of values with the same key, replacing any existing values for that key."""
        if key in self.keys():
            self._data.pop(key)
        self.put(key, values)

    def size(self, ):
        """ Returns the number of key-value pairs in the multimap."""
        return len(self.keys())

    def toString(self, ):
        """ Returns a string representation of the multimap, generated by calling toString on the map returned by Multimap.asMap(self, ):."""
        return self.__str__()

    def values(self, ):
        """
        Returns a collection of all values in the multimap.
        :return:
        """
        v = []
        for k in self.keys():
            v.append(self._data[k])
        return v

    def put(self, key, value):
        """
        Stores a key-value pair in the multimap.
        Creates a key of and object that has a hash
        :param a:
        :param b:
        :return:
        """
        self.add(key, value)

    def putAll(self, a, b=None):
        """
        Stores a collection of values with the same key or, if b is not None
        Copies all of another multimap's key-value pairsdef o this multimap
        :param a: multimap or
        :param b:
        :return:
        """
        if b is None:
            # Copies all of another multimap's key-value pairs from a into this multimap.
            multimap = a
        else:
            # Stores a collection of values with the same key.
            key = a
            values = b


class LinkedHashMap(dict):
    """ Works with python 3.7 which maintains the order of insertion"""
    def __init__(self,  seq=None, **kwargs):
        if seq is None:
            seq = {}
        super().__init__(seq, **kwargs)

    def values(self):
        """
        return all the values from the hashmap
        :return:
        """
        v = []
        for k in self.keys():
            v.append(self[k])
        return v

class LinkedHashMultimap(HashMultimap):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, *values: Iterable[Any]):
        """    Creates a new, empty LinkedHashMultimap with the default initial capacities."""
        super().__init__(*values)

    def containsValue(self, value):
        """    Returns true if the multimap contains the specified value for any key."""
        pass

    def create(self, a, expectedValuesPerKey):
        if expectedValuesPerKey is None:
            # Constructs a LinkedHashMultimap with the same mappings as the specified multimap.
            multimap = a
        else:
            # Constructs an empty LinkedHashMultimap with enough capacity to hold the specified numbers of keys and values without rehashing.

            expectedKeys = a
        pass


    def entries(self, ):
        """    Returns a set of all key-value pairs."""
        pass

    def equals(self, object):
        """    Compares the specified to this multimap for equality."""
        pass

    # def get(self, key):
    #     """    Returns a collection view of all values associated with a key."""
    #     pass

    def hashCode(self, ):
        """    Returns the hash code for this multimap."""
        pass

    def isEmpty(self, ):
        """    Returns true if the multimap contains no key-value pairs."""
        pass

    def keys(self, ):
        """    Returns a collection, which may contain duplicates, of all keys."""
        pass

    # def keySet(self, ):
    #     """    Returns the set of all keys, each appearing once in the returned set."""
    #     pass

    # def put(self, key, value):
    #     """    Stores a key-value pair in the multimap."""
    #     pass

    def putAll(self, key, values=None):
        if values is None:
            # Copies all of another multimap's key-value pairs into this multimap.
            multimap = key
        else:
            # Stores a collection of values with the same key."""
            pass
        pass

    def remove(self, key, value):
        """    Removes a key-value pair from the multimap."""
        pass

    def removeAll(self, key):
        """    Removes all values associated with a given key."""
        pass

    def replaceValues(self, key, values):
        """    Stores a collection of values with the same key, replacing any existing values for that key."""
        pass

    def size(self, ):
        """    Returns the number of key-value pairs in the multimap."""
        pass

    def toString(self, ):
        """    Returns a string representation of the multimap, generated by calling toString on the map returned by Multimap.asMap(self, ):."""
        pass

    def values(self, ):
        """    Returns a collection of all values in the multimap."""
        pass


class HashMap:
    # see https://stackoverflow.com/questions/8703496/hash-map-in-python
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        self.store = []

    def get(self, key):
        index = hash(key)
        if not self.store.index(index):
            return None
        n = self.store[index]
        while True:
            if n.key == key:
                return n.value
            else:
                if n.next:
                    n = n.next
                else:
                    return None

    def put(self, key, value):
        nd = self.Node(key, value)
        index = hash(key)
        n = self.store[index]
        if n is None:
            self.store[index] = nd
        else:
            if n.key == key:
                n.value = value
            else:
                while n.next:
                    if n.key == key:
                        n.value = value
                        return
                    else:
                        n = n.next
                n.next = nd

    def __del__(self, key):
        index = hash(key)
        if not self.store.index(index):
            return
        # Get the node structure
        nd = self.store[index]
        # Find and store the node that is pointed to in the to be removed data structure
        next_index = nd.next
        for ind in self.store:
            n = self.store[ind]
            if n.next == index:
                # This node needs to be linked to the removed nodes next data node.
                n.next = next_index
                break
        # Now remove the node
        self.store.pop(index)


if __name__ == "__main__":
    h = HashMultimap()

    h.add_many([
        ('a', (1, 2, 3)),
        ('b', (4, 5, 6)),
        ('c', (7, 8, 9)),
    ])
    print(h)
    x = list(h.get('a'))
    print(f'x={x[0]}')
    y = h.get_many('a','b')
    for x in y:
        print(f'item y: {x}')

    z = list(h.get('a','b'))
    print(f'z={z[0]}')
    print('deleting a')
    h.delete('a')
    print(h)
    print('adding b')
    h.add('b', 23, 27, 90)
    print(h)

    h.add('b', ('h', 'j', 'k'))
    print(h)

    h.add('b', 3, 'f', 's')
    print(h)

    h.add('b', {'key':0})
    print(h)
    v = (1,2,3)
    h.add(v, 'a')
    print(h)
    u = HashMultimap()
    h.add(u, 'my string')
    print(h)
    x = list(h.get(u))
    print(x[0])

    ks = h.keySet()
    print(ks)

    y = h.get_many('a','b')
    for x in y:
        print(f'item y: {x}')

    hm = LinkedHashMap({'a': 10})
    print(hm)
    print(hm.values())


    hm2 = LinkedHashMap()
    print(hm2)
