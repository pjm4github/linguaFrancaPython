#!/usr/bin/env python
""" generated source for module NamedInstance """
#  Base class for instances with names in Lingua Franca. 
# 
# Copyright (c) 2019, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
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
# package: org.lflang.generator
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.List
# import org.eclipse.emf.ecore.EObject

#  
#  * Base class for compile-time instances with names in Lingua Franca.
#  * An instance of concrete subclasses of this class represents one or
#  * more runtime instances of a reactor, port, reaction, etc. There
#  * will be more than one runtime instance if the object or any of its
#  * parents is a bank of reactors.
#  *  
#  * @author{Marten Lohstroh <marten@berkeley.edu>}
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#
import re

from include.overloading import overloaded
from lflang.generator.ReactorInstance import ReactorInstance


class NamedInstance:
    def __init__(self, definition, parent):
        """
        Construct a new instance with the specified definition
        and parent. E.g., for a reactor instance, the definition
        is Instantiation, and for a port instance, it is Port. These are
        nodes in the AST. This is protected because only subclasses
        should be constructed.

        :param definition: The definition in the AST for this instance.
        :param parent: The reactor instance that creates this instance.
        """

        # The full name of this instance.
        self._fullName = None

        #  A limit on the number of characters returned by uniqueID.
        self.identifierLengthLimit = 40

        # Map from a name of the form a_b_c to the number of
        # unique IDs with that prefix that have been already
        # assigned. If none have been assigned, then there is
        # no entry in this map. This map should be non-null only
        # for the main reactor (the top level).      
        self.uniqueIDCount = None

        # Unique ID for this instance. This is null until
        # uniqueID() is called.
        self._uniqueID = None

        # The width of this instance. This is 1 for everything
        # except a PortInstance representing a multiport and a
        # ReactorInstance representing a bank.
        self.width = 1

        #  The Instantiation AST object from which this was created.
        self.definition = definition

        #  The reactor instance that creates this instance.
        self.parent = parent
        # The depth in the hierarchy of this instance.
        # This is 0 for main or federated, 1 for the reactors immediately contained, etc.
        #  Calculate the depth.
        self.depth = 0
        p = self.parent
        while p is not None:
            p = p.parent
            self.depth += 1

    def getDefinition(self):
        """
        Return the definition, which is the AST node for this object.
        :return:
        """
        return self.definition

    def getDepth(self):
        """
        Get the depth of the reactor instance. This is 0 for the main reactor,
        1 for reactors immediately contained therein, etc.
        :return:
        """
        return self.depth

    def getFullName(self):
        """
        # Return the full name of this instance, which has the form
        # "a.b.c", where "c" is the name of this instance, "b" is the name
        # of its container, and "a" is the name of its container, stopping
        # at the container in main. If any reactor in the hierarchy is
        # in a bank of reactors then, it will appear as a[index].
        # Similarly, if c is a port in a multiport, it will appear as
        # c[index].
        :return: The full name of this instance.
        """
        return self.getFullNameWithJoiner(".")

    def getName(self):
        """
        # Return the name of this instance as given in its definition.
        # Note that this is unique only relative to other instances with
        # the same parent.
        :return: The name of this instance within its parent.
        """
        return self.getFullName()

    @overloaded
    def getParent(self):
        """
        Return the parent or null if this is a top-level reactor.
        :return:
        """
        return self.parent

    @getParent.register(object, int)
    def getParent_0(self, d):
        """
        Return the parent at the given depth or null if there is
        no parent at the given depth.
        :param d: The depth.
        :return:
        """
        if d >= self.depth or d < 0:
            return None
        p = self.parent
        while p is not None:
            if p.depth == d:
                return p
            p = p.parent
        return None

    def getWidth(self):
        """
        Return the width of this instance, which in this base class is 1.
        Subclasses PortInstance and ReactorInstance change this to the
        multiport and bank widths respectively.
        :return:
        """
        return self.width

    def hasParent(self, container):
        """
        Return true if this instance has the specified parent
        (possibly indirectly, anywhere up the hierarchy).
        :param container:
        :return:
        """
        p = self.parent
        while p is not None:
            if p == container:
                return True
            p = p.parent
        return False

    def parents(self):
        """
        Return a list of all the parents starting with the root().
        :return:
        """
        if isinstance(self, ReactorInstance) and self.parent is None:
            #  This is the top level, so it must be a reactor.
            self.result.append(self)
        container = self.parent
        while container is not None:
            self.result.append(container)
            container = container.parent
        return self.result

    def root(self):
        """
        Return the root reactor, which is the top-level parent.
        @return The top-level parent.
        :return:
        """
        if self.parent is not None:
            return self.parent.root()
        else:
            return self

    def setWidth(self, width):
        """
        Set the width. This method is here for testing only and should
        not be used for any other purpose.
        :param width: The new width.
        :return:
        """
        self.width = width

    def uniqueID(self):
        """
        Return an identifier for this instance, which has the form "a_b_c"
        or "a_b_c_n", where "c" is the name of this instance, "b" is the name
        of its container, and "a" is the name of its container, stopping
        at the container in main. All names are converted to lower case.
        The suffix _n is usually omitted, but it is possible to get name
        collisions using the above scheme, in which case _n will be an
        increasing integer until there is no collision.
        If the length of the root of the name as calculated above (the root
        is without the _n suffix) is longer than
        the static variable identifierLengthLimit, then the name will be
        truncated. The returned name will be the tail of the name calculated
        above with the prefix '_'.
        @return An identifier for this instance that is guaranteed to be
         unique within the top-level parent.
        :return:
        """
        if self._uniqueID is None:
            #  Construct the unique ID only if it has not been
            #  previously constructed.
            prefix = self.getFullNameWithJoiner("_").lower()
            #  Replace all non-alphanumeric (Latin) characters with underscore.
            prefix = re.sub(r'[^a-zA-Z\d]', '_', prefix)

            #  Truncate, if necessary.
            if self.identifierLengthLimit > len(prefix):
                prefix = '_' + prefix[:self.identifierLengthLimit - len(prefix) + 1]
            #  Ensure uniqueness.
            toplevel = self.root()
            if toplevel.uniqueIDCount is None:
                toplevel.uniqueIDCount = dict()
            count = toplevel.uniqueIDCount.get(prefix)
            if count is None:
                toplevel.uniqueIDCount.put(prefix, 1)
                self._uniqueID = prefix
            else:
                toplevel.uniqueIDCount.put(prefix, count + 1)
                #  NOTE: The length of this name could exceed
                #  identifierLengthLimit. Is this OK?
                self._uniqueID = prefix + '_' + (count + 1)
        return self._uniqueID

    def getMode(self, direct):
        """
        Returns the directly/indirectly enclosing mode.
        :param direct: flag whether to check only for direct enclosing mode
                       or also consider modes of parent reactor instances.
        :return: The mode, if any, null otherwise.
        """
        mode = None
        if self.parent is not None:
            if not self.parent.modes.isEmpty():
                mode = None
                for it in self.parent.modes:
                    if it.find(self) >= 0:
                        mode = it
                        break
            if mode is None and not direct:
                mode = self.parent.getMode(False)
        return mode

    def getFullNameWithJoiner(self, joiner: str):
        """
        Return a string of the form
        "a.b.c", where "." is replaced by the specified joiner,
        "c" is the name of this instance, "b" is the name
        of its container, and "a" is the name of its container, stopping
        at the container in main.
        :param joiner: a string joiner to concatenate the name parts
        :return: A string representing this instance.
        """
        #  This is not cached because _uniqueID is cached.
        if self.parent is None:
            return self.__name__
        elif self.getMode(True) is not None:
            s = joiner.join([self.parent.getFullNameWithJoiner(joiner),
                             self.getMode(True).__name__,
                             self.__name__])
            return s
        else:
            s = joiner.join([self.parent.getFullNameWithJoiner(joiner),
                             self.__name__])
            return s
