#!/usr/bin/env python
""" generated source for module CUtil """
from abc import ABCMeta, abstractmethod
from include.overloading import overloaded
#  Utilities for C code generation. 
# 
# Copyright (c) 2019-2021, The University of California at Berkeley.
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
# package: org.lflang.generator.c
# import java.io.File
# import java.io.IOException
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.nio.file.StandardCopyOption
# import java.util.ArrayList
# import java.util.LinkedList
# import java.util.List
# import java.util.Objects
# import java.util.stream.Collectors

#  * A collection of utilities for C code generation.
#  * This class codifies the coding conventions for the C target code generator.
#  * I.e., it defines how variables are named and referenced.
#  * @author{Edward A. Lee <eal@berkeley.edu>}
#
from lflang.generator import PortInstance, ReactionInstance, ReactorInstance, \
    TriggerInstance, LFGeneratorContext
from lflang.lf import Port
from lflang.util import FileUtil


class CUtil:
    """ generated source for class CUtil """
    #      * Suffix that when appended to the name of a federated reactor yields
    #      * the name of its corresponding RTI executable.
    #      
    RTI_BIN_SUFFIX = "_RTI"

    #      * Suffix that when appended to the name of a federated reactor yields
    #      * the name of its corresponding distribution script.
    #      
    RTI_DISTRIBUTION_SCRIPT_SUFFIX = "_distribute.sh"

    # ////////////////////////////////////////////////////
    # // Public methods.
    #      * Return a default name of a variable to refer to the bank index of a reactor
    #      * in a bank. This is has the form uniqueID_i where uniqueID
    #      * is an identifier for the instance that is guaranteed to be different
    #      * from the ID of any other instance in the program.
    #      * If the instance is not a bank, return "0".
    #      * @param instance A reactor instance.
    #      
    @classmethod
    def bankIndex(cls, instance):
        """ generated source for method bankIndex """
        if not instance.isBank():
            return "0"
        return self.bankIndexName(instance)

    #      * Return a default name of a variable to refer to the bank index of a reactor
    #      * in a bank. This is has the form uniqueID_i where uniqueID
    #      * is an identifier for the instance that is guaranteed to be different
    #      * from the ID of any other instance in the program.
    #      * @param instance A reactor instance.
    #      
    @classmethod
    def bankIndexName(cls, instance):
        """ generated source for method bankIndexName """
        return instance.uniqueID() + "_i"

    #      * Return a default name of a variable to refer to the channel index of a port
    #      * in a bank. This has the form uniqueID_c where uniqueID
    #      * is an identifier for the instance that is guaranteed to be different
    #      * from the ID of any other instance in the program.
    #      * If the port is not a multiport, then return the string "0".
    #      
    @classmethod
    def channelIndex(cls, port):
        """ generated source for method channelIndex """
        if not port.isMultiport():
            return "0"
        return self.channelIndexName(port)

    #      * Return a default name of a variable to refer to the channel index of a port
    #      * in a bank. This is has the form uniqueID_c where uniqueID
    #      * is an identifier for the instance that is guaranteed to be different
    #      * from the ID of any other instance in the program.
    #      
    @classmethod
    def channelIndexName(cls, port):
        """ generated source for method channelIndexName """
        return port.uniqueID() + "_c"

    #      * Return a reference to the specified port.
    #      *
    #      * The returned string will have one of the following forms:
    #      *
    #      * * selfStructs[k]->_lf_portName
    #      * * selfStructs[k]->_lf_portName
    #      * * selfStructs[k]->_lf_portName[i]
    #      * * selfStructs[k]->_lf_parent.portName
    #      * * selfStructs[k]->_lf_parent.portName[i]
    #      * * selfStructs[k]->_lf_parent[j].portName
    #      * * selfStructs[k]->_lf_parent[j].portName[i]
    #      *
    #      * where k is the runtime index of either the port's parent
    #      * or the port's parent's parent, the latter when isNested is true.
    #      * The index j is present if the parent is a bank, and
    #      * the index i is present if the port is a multiport.
    #      *
    #      * The first two forms are used if isNested is false,
    #      * and the remaining four are used if isNested is true.
    #      * Set isNested to true when referencing a port belonging
    #      * to a contained reactor.
    #      *
    #      * @param port The port.
    #      * @param isNested True to return a reference relative to the parent's parent.
    #      * @param includeChannelIndex True to include the channel index at the end.
    #      * @param runtimeIndex A variable name to use to index the runtime instance or
    #      *  null to use the default, the string returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex A variable name to use to index the bank or null to use the
    #      *  default, the string returned by {@link CUtil#bankIndex(ReactorInstance)}.
    #      * @param channelIndex A variable name to use to index the channel or null to
    #      *  use the default, the string returned by {@link CUtil#channelIndex(PortInstance)}.
    #      
    @classmethod
    @overloaded
    def portRef(cls, port, isNested, includeChannelIndex, runtimeIndex, bankIndex, channelIndex):
        """ generated source for method portRef """
        channel = ""
        if channelIndex == None:
            channelIndex = channelIndex(port)
        if port.isMultiport() and includeChannelIndex:
            channel = "[" + channelIndex + "]"
        if isNested:
            return self.reactorRefNested(port.getParent(), runtimeIndex, bankIndex) + "." + port.__name__ + channel
        else:
            sourceStruct = CUtil.reactorRef(port.getParent(), runtimeIndex)
            return sourceStruct + "->_lf_" + port.__name__ + channel

    #      * Return a reference to the port on the self struct of the
    #      * port's parent.  This is used when an input port triggers a reaction
    #      * in the port's parent or when an output port is written to by
    #      * a reaction in the port's parent.
    #      * This is equivalent to calling `portRef(port, false, true, null, null)`.
    #      * @param port An instance of the port to be referenced.
    #      
    @classmethod
    @portRef.register(object, PortInstance)
    def portRef_0(cls, port):
        """ generated source for method portRef_0 """
        return cls.portRef(port, False, True, None, None, None)

    #      * Return a reference to the port on the self struct of the
    #      * port's parent using the specified index variables.
    #      * This is used when an input port triggers a reaction
    #      * in the port's parent or when an output port is written to by
    #      * a reaction in the port's parent.
    #      * This is equivalent to calling `portRef(port, false, true, bankIndex, channelIndex)`.
    #      * @param port An instance of the port to be referenced.
    #      * @param runtimeIndex A variable name to use to index the runtime instance or
    #      *  null to use the default, the string returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex A variable name to use to index the bank or null to use the
    #      *  default, the string returned by {@link CUtil#bankIndex(ReactorInstance)}.
    #      * @param channelIndex A variable name to use to index the channel or null to
    #      *  use the default, the string returned by {@link CUtil#channelIndex(PortInstance)}.
    #      
    @classmethod
    @portRef.register(object, PortInstance, str, str, str)
    def portRef_1(cls, port, runtimeIndex, bankIndex, channelIndex):
        """ generated source for method portRef_1 """
        return cls.portRef(port, False, True, runtimeIndex, bankIndex, channelIndex)

    #      * Return a reference to a port without any channel indexing.
    #      * This is useful for deriving a reference to the _width variable.
    #      * @param port An instance of the port to be referenced.
    #      
    @classmethod
    @overloaded
    def portRefName(cls, port):
        """ generated source for method portRefName """
        return cls.portRef(port, False, False, None, None, None)

    #      * Return the portRef without the channel indexing.
    #      * This is useful for deriving a reference to the _width variable.
    #      *
    #      * @param port An instance of the port to be referenced.
    #      * @param runtimeIndex A variable name to use to index the runtime instance or
    #      *  null to use the default, the string returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex A variable name to use to index the bank or null to use the
    #      *  default, the string returned by {@link CUtil#bankIndex(ReactorInstance)}.
    #      * @param channelIndex A variable name to use to index the channel or null to
    #      *  use the default, the string returned by {@link CUtil#channelIndex(PortInstance)}.
    #      
    @classmethod
    @portRefName.register(object, PortInstance, str, str, str)
    def portRefName_0(cls, port, runtimeIndex, bankIndex, channelIndex):
        """ generated source for method portRefName_0 """
        return cls.portRef(port, False, False, runtimeIndex, bankIndex, channelIndex)

    #      * Return a port reference to a port on the self struct of the
    #      * parent of the port's parent.  This is used when an input port
    #      * is written to by a reaction in the parent of the port's parent,
    #      * or when an output port triggers a reaction in the parent of the
    #      * port's parent. This is equivalent to calling
    #      * `portRef(port, true, true, null, null, null)`.
    #      *
    #      * @param port The port.
    #      
    @classmethod
    @overloaded
    def portRefNested(cls, port):
        """ generated source for method portRefNested """
        return cls.portRef(port, True, True, None, None, None)

    #      * Return a reference to the port on the self struct of the
    #      * parent of the port's parent.  This is used when an input port
    #      * is written to by a reaction in the parent of the port's parent,
    #      * or when an output port triggers a reaction in the parent of the
    #      * port's parent. This is equivalent to calling
    #      * `portRef(port, true, true, runtimeIndex, bankIndex, channelIndex)`.
    #      *
    #      * @param port The port.
    #      * @param runtimeIndex A variable name to use to index the runtime instance or
    #      *  null to use the default, the string returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex A variable name to use to index the bank or null to use the
    #      *  default, the string returned by {@link CUtil#bankIndex(ReactorInstance)}.
    #      * @param channelIndex A variable name to use to index the channel or null to
    #      *  use the default, the string returned by {@link CUtil#channelIndex(PortInstance)}.
    #      
    @classmethod
    @portRefNested.register(object, PortInstance, str, str, str)
    def portRefNested_0(cls, port, runtimeIndex, bankIndex, channelIndex):
        """ generated source for method portRefNested_0 """
        return cls.portRef(port, True, True, runtimeIndex, bankIndex, channelIndex)

    #      * Return a reference to the port on the self struct of the
    #      * parent of the port's parent, but without the channel indexing,
    #      * even if it is a multiport.  This is used when an input port
    #      * is written to by a reaction in the parent of the port's parent,
    #      * or when an output port triggers a reaction in the parent of the
    #      * port's parent.
    #      * This is equivalent to calling `portRef(port, true, false, null, null, null)`.
    #      *
    #      * @param port The port.
    #      
    @classmethod
    @overloaded
    def portRefNestedName(cls, port):
        """ generated source for method portRefNestedName """
        return cls.portRef(port, True, False, None, None, None)

    #      * Return a reference to the port on the self struct of the
    #      * parent of the port's parent, but without the channel indexing,
    #      * even if it is a multiport.  This is used when an input port
    #      * is written to by a reaction in the parent of the port's parent,
    #      * or when an output port triggers a reaction in the parent of the
    #      * port's parent. This is equivalent to calling
    #      * `portRefNested(port, true, false, runtimeIndex, bankIndex, channelIndex)`.
    #      *
    #      * @param port The port.
    #      * @param runtimeIndex A variable name to use to index the runtime instance or
    #      *  null to use the default, the string returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex A variable name to use to index the bank or null to use the
    #      *  default, the string returned by {@link CUtil#bankIndex(ReactorInstance)}.
    #      * @param channelIndex A variable name to use to index the channel or null to
    #      *  use the default, the string returned by {@link CUtil#channelIndex(PortInstance)}.
    #      
    @classmethod
    @portRefNestedName.register(object, PortInstance, str, str, str)
    def portRefNestedName_0(cls, port, runtimeIndex, bankIndex, channelIndex):
        """ generated source for method portRefNestedName_0 """
        return cls.portRef(port, True, False, runtimeIndex, bankIndex, channelIndex)

    #      * Return code for referencing a port within a reaction body possibly indexed by
    #      * a bank index and/or a multiport index. If the provided reference is
    #      * not a port, then this returns the string "ERROR: not a port."
    #      * @param reference The reference to the port.
    #      * @param bankIndex A bank index or null or negative if not in a bank.
    #      * @param multiportIndex A multiport index or null or negative if not in a multiport.
    #      
    @classmethod
    def portRefInReaction(cls, reference, bankIndex, multiportIndex):
        """ generated source for method portRefInReaction """
        if not reference.isinstance(Port):
            return "ERROR: not a port."
            #  FIXME: This is not the fail-fast approach, and it seems arbitrary.
        prefix = ""
        if reference.getContainer() != None:
            bank = ""
            if reference.getContainer().getWidthSpec() != None and bankIndex != None and bankIndex >= 0:
                bank = "[" + bankIndex + "]"
            prefix = reference.getContainer().__name__ + bank + "."
        multiport = ""
        if (reference.getVariable()).getWidthSpec() != None and multiportIndex != None and multiportIndex >= 0:
            multiport = "[" + multiportIndex + "]"
        return prefix + reference.getVariable().__name__ + multiport

    #      * Return a reference to the reaction entry on the self struct
    #      * of the parent of the specified reaction.
    #      * @param reaction The reaction.
    #      
    @classmethod
    @overloaded
    def reactionRef(cls, reaction):
        """ generated source for method reactionRef """
        return cls.reactionRef(reaction, None)

    #      * Return a reference to the reaction entry on the self struct
    #      * of the parent of the specified reaction.
    #      * @param reaction The reaction.
    #      * @param runtimeIndex An index into the array of self structs for the parent.
    #      
    @classmethod
    @reactionRef.register(object, ReactionInstance, str)
    def reactionRef_0(cls, reaction, runtimeIndex):
        """ generated source for method reactionRef_0 """
        return reactorRef(reaction.getParent(), runtimeIndex) + "->_lf__reaction_" + reaction.index

    #      * Return a reference to the "self" struct of the specified
    #      * reactor instance. The returned string has the form
    #      * self[j], where self is the name of the array of self structs
    #      * for this reactor instance and j is the expression returned
    #      * by {@link #runtimeIndex(ReactorInstance)} or 0 if there are no banks.
    #      * @param instance The reactor instance.
    #      
    @classmethod
    @overloaded
    def reactorRef(cls, instance):
        """ generated source for method reactorRef """
        return cls.reactorRef(instance, None)

    #      * Return the name of the array of "self" structs of the specified
    #      * reactor instance.  This is similar to {@link #reactorRef(ReactorInstance)}
    #      * except that it does not index into the array.
    #      * @param instance The reactor instance.
    #      
    @classmethod
    def reactorRefName(cls, instance):
        """ generated source for method reactorRefName """
        return instance.uniqueID() + "_self"

    #      * Return a reference to the "self" struct of the specified
    #      * reactor instance. The returned string has the form
    #      * self[runtimeIndex], where self is the name of the array of self structs
    #      * for this reactor instance. If runtimeIndex is null, then it is replaced by
    #      * the expression returned
    #      * by {@link #runtimeIndex(ReactorInstance)} or 0 if there are no banks.
    #      * @param instance The reactor instance.
    #      * @param runtimeIndex An optional expression to use to address bank members.
    #      *  If this is null, the expression used will be that returned  by
    #      *  {@link #runtimeIndex(ReactorInstance)}.
    #      
    @classmethod
    @reactorRef.register(object, ReactorInstance, str)
    def reactorRef_0(cls, instance, runtimeIndex):
        """ generated source for method reactorRef_0 """
        if runtimeIndex == None:
            runtimeIndex = runtimeIndex(instance)
        return cls.reactorRefName(instance) + "[" + runtimeIndex + "]"

    #      * For situations where a reaction reacts to or reads from an output
    #      * of a contained reactor or sends to an input of a contained reactor,
    #      * then the container's self struct will have a field
    #      * (or an array of fields if the contained reactor is a bank) that is
    #      * a struct with fields corresponding to those inputs and outputs.
    #      * This method returns a reference to that struct or array of structs.
    #      * Note that the returned reference is not to the self struct of the
    #      * contained reactor. Use {@link #reactorRef(ReactorInstance)} for that.
    #      *
    #      * @param reactor The contained reactor.
    #      
    @classmethod
    @overloaded
    def reactorRefNested(cls, reactor):
        """ generated source for method reactorRefNested """
        return cls.reactorRefNested(reactor, None, None)

    #      * For situations where a reaction reacts to or reads from an output
    #      * of a contained reactor or sends to an input of a contained reactor,
    #      * then the container's self struct will have a field
    #      * (or an array of fields if the contained reactor is a bank) that is
    #      * a struct with fields corresponding to those inputs and outputs.
    #      * This method returns a reference to that struct or array of structs.
    #      * Note that the returned reference is not to the self struct of the
    #      * contained reactor. Use {@link CUtil#reactorRef(ReactorInstance)} for that.
    #      *
    #      * @param reactor The contained reactor.
    #      * @param runtimeIndex A variable name to use to index the runtime instance or
    #      *  null to use the default, the string returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex A variable name to use to index the bank or null to use the
    #      *  default, the string returned by {@link CUtil#bankIndex(ReactorInstance)}.
    #      
    @classmethod
    @reactorRefNested.register(object, ReactorInstance, str, str)
    def reactorRefNested_0(cls, reactor, runtimeIndex, bankIndex):
        """ generated source for method reactorRefNested_0 """
        result = cls.reactorRef(reactor.getParent(), runtimeIndex) + "->_lf_" + reactor.__name__
        if reactor.isBank():
            #  Need the bank index not the runtimeIndex.
            if bankIndex == None:
                bankIndex = bankIndex(reactor)
            result += "[" + bankIndex + "]"
        return result

    #      * Return an expression that, when evaluated, gives the index of
    #      * a runtime instance of the specified ReactorInstance. If the reactor
    #      * is not within any banks, then this will return "0". Otherwise, it
    #      * will return an expression that evaluates a mixed-radix number
    #      * d0%w0, d1%w1, ... , dn%wn, where n is the depth minus one of the
    #      * reactor. The radixes, w0 to wn, are the widths of this reactor,
    #      * its parent reactor, on up to the top-level reactor. Since the top-level
    #      * reactor is never a bank, dn = 0 and wn = 1. The digits, di, are
    #      * either 0 (of the parent is not a bank) or the variable name returned
    #      * by {@link #bankIndexName(ReactorInstance)} if the parent is a bank.
    #      * The returned expression, when evaluated, will yield the following value:
    #      *
    #      *     d0 + w0 * (d1 + w1 * ( ... (dn-1 + wn-1 * dn) ... )
    #      *
    #      * @param reactor The reactor.
    #      
    @classmethod
    def runtimeIndex(cls, reactor):
        """ generated source for method runtimeIndex """
        result = ""
        width = 0
        parens = 0
        while reactor != None:
            if reactor.isBank() and reactor.getWidth() > 1:
                if width > 0:
                    result.append(" + " + width + " * (")
                    parens += 1
                result.append(cls.bankIndexName(reactor))
                width = reactor.getWidth()
            reactor = reactor.getParent()
        __parens_0 = parens
        parens -= 1
        while __parens_0 > 0:
            result.append(")")
        if 0 == len(result):
            return "0"
        return str(result)

    #      * Return a unique type for the "self" struct of the specified
    #      * reactor class from the reactor class.
    #      * @param reactor The reactor class.
    #      * @return The type of a self struct for the specified reactor class.
    #      
    @classmethod
    @overloaded
    def selfType(cls, reactor):
        """ generated source for method selfType """
        return reactor.__name__.lower() + "_self_t"

    #  Construct a unique type for the "self" struct of the class of the given reactor. 
    @classmethod
    @selfType.register(object, ReactorInstance)
    def selfType_0(cls, instance):
        """ generated source for method selfType_0 """
        return cls.selfType(instance.getDefinition().getReactorClass())

    #      * Return a reference to the trigger_t struct of the specified
    #      * trigger instance (input port or action). This trigger_t struct
    #      * is on the self struct.
    #      * @param instance The port or action instance.
    #      
    @classmethod
    @overloaded
    def triggerRef(cls, instance):
        """ generated source for method triggerRef """
        return cls.triggerRef(instance, None)

    #      * Return a reference to the trigger_t struct of the specified
    #      * trigger instance (input port or action). This trigger_t struct
    #      * is on the self struct.
    #      * @param instance The port or action instance.
    #      * @param runtimeIndex An optional index variable name to use to address runtime instances.
    #      
    @classmethod
    @triggerRef.register(object, TriggerInstance, str)
    def triggerRef_0(cls, instance, runtimeIndex):
        """ generated source for method triggerRef_0 """
        return cls.reactorRef(instance.getParent(), runtimeIndex) + "->_lf__" + instance.__name__

    #      * Return a reference to the trigger_t struct for the specified
    #      * port of a contained reactor.
    #      * @param port The output port of a contained reactor.
    #      
    @classmethod
    @overloaded
    def triggerRefNested(cls, port):
        """ generated source for method triggerRefNested """
        return cls.triggerRefNested(port, None, None)

    #      * Return a reference to the trigger_t struct for the specified
    #      * port of a contained reactor.
    #      * @param port The output port of a contained reactor.
    #      * @param runtimeIndex An optional index variable name to use to index
    #      *  the runtime instance of the port's parent's parent, or null to get the
    #      *  default returned by {@link CUtil#runtimeIndex(ReactorInstance)}.
    #      * @param bankIndex An optional index variable name to use to index
    #      *  the the bank of the port's parent, or null to get the default returned by
    #      *  {@link CUtil#bankIndex(ReactorInstance)}.
    #      
    @classmethod
    @triggerRefNested.register(object, PortInstance, str, str)
    def triggerRefNested_0(cls, port, runtimeIndex, bankIndex):
        """ generated source for method triggerRefNested_0 """
        return cls.reactorRefNested(port.getParent(), runtimeIndex, bankIndex) + "." + port.__name__ + "_trigger"

    #      * Copy the 'fileName' (which also could be a directory name) from the
    #      * 'srcDirectory' to the 'destinationDirectory'. This function has a
    #      * fallback search mechanism, where if `fileName` is not found in the
    #      * `srcDirectory`, it will try to find `fileName` via the following
    #      * procedure:
    #      *     1- Search in LF_CLASSPATH. @see findFile()
    #      *     2- Search in CLASSPATH. @see findFile()
    #      *     3- Search for 'fileName' as a resource. That means the `fileName`
    #      *        can be '/path/to/class/resource'. @see java.lang.Class.getResourceAsStream()
    #      *
    #      * @param fileName Name of the file or directory.
    #      * @param srcDir   Where the file or directory is currently located.
    #      * @param dstDir   Where the file or directory should be placed.
    #      * @return The name of the file or directory in destinationDirectory or an empty string on failure.
    #      
    @classmethod
    def copyFileOrResource(cls, fileName, srcDir, dstDir):
        """ generated source for method copyFileOrResource """
        #  Try to copy the file or directory from the file system.
        file = findFileOrDirectory(fileName, srcDir)
        if file != None:
            target = dstDir.resolve(file.getFileName())
            try:
                if Files.isDirectory(file):
                    FileUtil.copyDirectory(file, target)
                elif Files.isRegularFile(file):
                    Files.copy(file, target, StandardCopyOption.REPLACE_EXISTING)
                return file.getFileName().__str__()
            except IOError as e:
                pass
                #  Failed to copy the file or directory, most likely
                #  because it doesn't exist. Will try to find it as a
                #  resource before giving up.
        filenameWithoutPath = fileName
        lastSeparator = fileName.lastIndexOf(File.separator)
        if lastSeparator > 0:
            #  FIXME: Brittle. What if the file is in a subdirectory?
            filenameWithoutPath = fileName.substring(lastSeparator + 1)
        #  Try to copy the file or directory as a resource.
        try:
            FileUtil.copyFileFromClassPath(fileName, dstDir.resolve(filenameWithoutPath))
            return filenameWithoutPath
        except IOError as ex:
            pass
            #  Will try one more time as a directory
        try:
            FileUtil.copyDirectoryFromClassPath(fileName, dstDir.resolve(filenameWithoutPath), False)
            return filenameWithoutPath
        except IOError as ex:
            sys.stderr.write("WARNING: Failed to find file or directory " + fileName)
        return ""

# ////////////////////////////////////////////////////
# // FIXME: Not clear what the strategy is with the following inner interface.
#  The {@code ReportCommandErrors} interface allows the
#  method runBuildCommand to call a protected
#  method from the CGenerator if that method is passed
#  using a method reference. The method that is passed
#  is then interpreted as a ReportCommandErrors instance.
#  This is a convenient way to factor out part of the
#  internals of the CGenerator while maintaining
#  encapsulation, even though the internals of the CGenerator
#  might seem to be tightly coupled. FIXME: Delete this comment
#      * A {@code ReportCommandErrors} is a way to analyze command
#      * output and report any errors that it describes.
#      * FIXME: If the VSCode branch passes code review
#      *  without significant revision, this mechanism will probably be replaced.
#
class ReportCommandErrors:
    """ generated source for interface ReportCommandErrors """
    __metaclass__ = ABCMeta
    @abstractmethod
    def report(self, errors):
        """ generated source for method report """

    #      * Search for a given file or directory name in the given directory.
    #      * If not found, search in directories in LF_CLASSPATH.
    #      * If there is no LF_CLASSPATH environment variable, use CLASSPATH,
    #      * if it is defined. The first file or directory that is found will
    #      * be returned. Otherwise, null is returned.
    #      *
    #      * @param fileName The file or directory name or relative path + name
    #      * as a String.
    #      * @param directory String representation of the directory to search in.
    #      * @return A Java Path or null if not found.
    #      
    @classmethod
    def findFileOrDirectory(cls, fileName, directory):
        """ generated source for method findFileOrDirectory """
        foundFile = None
        #  Check in local directory
        foundFile = directory.resolve(fileName)
        if Files.exists(foundFile):
            return foundFile
        #  Check in LF_CLASSPATH
        #  Load all the resources in LF_CLASSPATH if it is set.
        classpathLF = System.getenv("LF_CLASSPATH")
        if classpathLF == None:
            classpathLF = System.getenv("CLASSPATH")
        if classpathLF != None:
            paths = classpathLF.split(System.getProperty("path.separator"))
            for path in paths:
                foundFile = Paths.get(path).resolve(fileName)
                if Files.exists(foundFile):
                    return foundFile
        #  Not found.
        return None

    #      * Run the custom build command specified with the "build" parameter.
    #      * This command is executed in the same directory as the source file.
    #      *
    #      * The following environment variables will be available to the command:
    #      *
    #      * * LF_CURRENT_WORKING_DIRECTORY: The directory in which the command is invoked.
    #      * * LF_SOURCE_DIRECTORY: The directory containing the .lf file being compiled.
    #      * * LF_SOURCE_GEN_DIRECTORY: The directory in which generated files are placed.
    #      * * LF_BIN_DIRECTORY: The directory into which to put binaries.
    #      *
    #      
    @classmethod
    def runBuildCommand(cls, fileConfig, targetConfig, commandFactory, errorReporter, reportCommandErrors, mode):
        """ generated source for method runBuildCommand """
        commands = getCommands(targetConfig.buildCommands, commandFactory, fileConfig.srcPath)
        #  If the build command could not be found, abort.
        #  An error has already been reported in createCommand.
        if commands.stream().anyMatch(Objects.isNull):
            return
        for cmd in commands:
            returnCode = cmd.run()
            if returnCode != 0 and mode != LFGeneratorContext.Mode.EPOCH:
                errorReporter.reportError("Build command \"{:s}\" failed with error code {:d}.".format(targetConfig.buildCommands, returnCode))
                return
            #  For warnings (vs. errors), the return code is 0.
            #  But we still want to mark the IDE.
            if not cmd.getErrors().__str__().isEmpty() and mode == LFGeneratorContext.Mode.EPOCH:
                reportCommandErrors.report(cmd.getErrors().__str__())
                return

    @classmethod
    def deleteBinFiles(cls, fileConfig):
        """ generated source for method deleteBinFiles """
        name = FileUtil.nameWithoutExtension(fileConfig.srcFile)
        files = fileConfig.binPath.toFile().list()
        federateNames = LinkedList()
        for f in files:
            if f == name or f == name + cls.RTI_BIN_SUFFIX or f == name + cls.RTI_DISTRIBUTION_SCRIPT_SUFFIX:
                fileConfig.binPath.resolve(f).toFile().delete()
            for federateName in federateNames:
                if f == name + "_" + federateName:
                    fileConfig.binPath.resolve(f).toFile().delete()

    @classmethod
    def multiportWidthExpression(cls, variable):
        """ generated source for method multiportWidthExpression """
        spec = multiportWidthTerms(variable)
        return None if spec == None else String.join(" + ", spec)

    @classmethod
    def getCommands(cls, commands, factory, dir):
        """ generated source for method getCommands """
        return None

    @classmethod
    def getTargetReference(cls, param):
        """ generated source for method getTargetReference """
        return param.__name__

    @classmethod
    def multiportWidthTerms(cls, variable):
        """ generated source for method multiportWidthTerms """
        result = None
        if isinstance(variable, (Port)):
            if (variable).getWidthSpec() != None:
                result = []
                if not (variable).getWidthSpec().isOfVariableLength():
                    for term in (variable).getWidthSpec().getTerms():
                        if term.getParameter() != None:
                            result.append(cls.getTargetReference(term.getParameter()))
                        else:
                            result.append("" + term.getWidth())
        return result

    @classmethod
    def isTokenType(cls, type, types):
        """ generated source for method isTokenType """
        if type.isUndefined():
            return False
        targetType = types.getVariableDeclaration(type, "", False)
        return type.isVariableSizeList or targetType.trim().endsWith("*")

    @classmethod
    def minThreadsToHandleInputPorts(cls, federates):
        """ generated source for method minThreadsToHandleInputPorts """
        nthreads = 1
        for federate in federates:
            nthreads = max(nthreads, len(federate.networkMessageActions) + 1)
        return nthreads

    @classmethod
    def generateWidthVariable(cls, var):
        """ generated source for method generateWidthVariable """
        return var + "_width"

    @classmethod
    def rootType(cls, type):
        """ generated source for method rootType """
        if type.endsWith("]"):
            return type.substring(0, type.indexOf("[")).trim()
        elif type.endsWith("*"):
            return type.substring(0, 1 - len(type)).trim()
        else:
            return type.trim()

    @classmethod
    def getShortenedName(cls, instance):
        """ generated source for method getShortenedName """
        description = instance.getFullName()
        period = description.indexOf(".")
        if period > 0:
            description = description.substring(period + 1)
        return description
