#!/usr/bin/env python
""" generated source for module CodeBuilder """
# package: org.lflang.generator
# import java.nio.file.Path
# import java.io.IOException
# import org.eclipse.emf.common.CommonPlugin
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.nodemodel.util.NodeModelUtils
from include.overloading import overloaded
from lflang.LFast.Nodemodels import NodeModelUtils
from lflang.generator import ReactorInstance, SendRange, RuntimeRange, CodeMap
from lflang.generator.c.CMixedRadixGenerator import CMixedRadixGenerator
from lflang.lf.LFCode import Code
from org.lflang.federated import FederateInstance

from org.lflang.generator.c import CUtil

from org.lflang.lf import LFCode

from org.lflang.util import FileUtil

# 
#  * Helper class for printing code with self.indentation.
#  * This class is backed by a StringBuilder and is used to accumulate
#  * code to be printed to a file. Its main function is to handle self.indentation.
#  * 
#  * @author Edward A. Lee
#  * @author Peter Donovan
class CommonPlugin:
    pass


class CodeBuilder:
    """ generated source for class CodeBuilder """
    # Construct a new empty code emitter.
    #      
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

        self.code_ = [""]
        self.indentation = ""

    # Construct a new code emitter with the text and indentation
    # of the specified code emitter.
    # @param model The model code emitter.
    #      
    @__init__.register(object, object)
    def __init___0(self, model):
        """ generated source for method __init___0 """
        self.indentation = model.self.indentation
        self.code_.append(model)

    # ///////////////////////////////////////////
    # /// Public methods.
    # Get the code produced so far.
    # @return The code produced so far as a String.
    #      
    def getCode(self):
        """ generated source for method getCode """
        return str(self.code_)

    # Increase the indentation of the output code produced.
    #      
    def indent(self):
        """ generated source for method indent """
        self.indentation += "    "

    # Insert the specified text at the specified position.
    # @param position The position.
    # @param text The text.
    #      
    def insert(self, position, text):
        """ generated source for method insert """
        self.code_.insert(position, text)

    # Return the length of the code in characters.
    #      
    def length(self):
        """ generated source for method length """
        return len(self.code_)

    # Add a new line.
    #      
    def newLine(self):
        """ generated source for method newLine """
        self.pr("")

    # Append the specified text plus a final newline.
    # @param format A format string to be used by {@code String.format} or
    #  the text to append if no further arguments are given.
    # @param args Additional arguments to pass to the formatter.
    #      
    @overloaded
    def pr(self, format, *args):
        """ generated source for method pr """
        self.pr(format.format(args) if (args != None and len(args)) else format)

    # Append the given text to the code buffer at the current self.indentation level.
    #      
    @pr.register(object, str)
    def pr_0(self, text):
        """ generated source for method pr_0 """
        for line in text.__str__().lines().iterator():
            self.code_.append(self.indentation).append(line).append("\n")

    @pr.register(object, object, object)
    def pr_1(self, eObject, text):
        """ generated source for method pr_1 """
        split = text.__str__().split("\n")
        for line in split:
            self.prSourceLineNumber(eObject)
            self.pr(line)

    def prSourceLineNumber(self, eObject):
        """ generated source for method prSourceLineNumber """
        node = NodeModelUtils.getNode(eObject)
        if node != None:
            offset = 0
            if isinstance(eObject, Code):
                offset += 1
            resolvedURI = CommonPlugin.resolve(eObject.eResource().getURI())
            self.pr("#line " + (node.getStartLine() + offset) + " \"" + resolvedURI + "\"")

    def prComment(self, comment):
        """ generated source for method prComment """
        self.pr("// " + comment)

    def removeLines(self, prefix):
        """ generated source for method removeLines """
        separator = "\n"
        lines = prefix.split(separator)
        builder = CodeBuilder()
        for line in lines:
            trimmedLine = line.trim()
            if not trimmedLine.startsWith(prefix):
                builder.pr(line)
        return builder

    @overloaded
    def startScopedBlock(self):
        """ generated source for method startScopedBlock """
        self.pr("{")
        self.indent()

    @startScopedBlock.register(object, ReactorInstance, FederateInstance, bool, bool)
    def startScopedBlock_0(self, reactor, federate, isFederated, restrict):
        """ generated source for method startScopedBlock_0 """
        if reactor != None and reactor.isBank():
            index = CUtil.bankIndexName(reactor)
            if reactor.depth == 1 and isFederated and restrict:
                self.startScopedBlock()
                self.pr("int " + index + " = " + federate.bankIndex + ";")
            else:
                self.pr("// Reactor is a bank. Iterate over bank members.")
                self.pr("for (int " + index + " = 0; " + index + " < " + reactor.width + "; " + index + "++) {")
                self.indent()
        else:
            self.startScopedBlock()

    def startChannelIteration(self, port):
        """ generated source for method startChannelIteration """
        if port.isMultiport:
            channel = CUtil.channelIndexName(port)
            self.pr("// Port " + port.getFullName() + " is a multiport. Iterate over its channels.")
            self.pr("for (int " + channel + " = 0; " + channel + " < " + port.width + "; " + channel + "++) {")
            self.indent()

    def startScopedBankChannelIteration(self, port, currentFederate, count, isFederated):
        """ generated source for method startScopedBankChannelIteration """
        if count != None:
            self.startScopedBlock()
            self.pr("int " + count + " = 0;")
        self.startScopedBlock(port.parent, currentFederate, isFederated, True)
        self.startChannelIteration(port)

    @overloaded
    def startScopedRangeBlock(self,
                              currentFederate,
                              range,
                              runtimeIndex,
                              bankIndex,
                              channelIndex,
                              nested,
                              isFederated,
                              restrict):
        """ generated source for method startScopedRangeBlock """
        self.pr("// Iterate over range " + range.__str__() + ".")
        ri = "runtime_index" if (runtimeIndex == None) else runtimeIndex
        ci = CUtil.channelIndexName(range.instance) if (channelIndex == None) else channelIndex
        bi = CUtil.bankIndexName(range.instance.parent) if (bankIndex == None) else bankIndex
        rangeMR = range.startMR()
        sizeMR = rangeMR.getDigits().size()
        nestedLevel = 2 if (nested) else 1
        self.startScopedBlock()
        if range.width > 1:
            self.pr("\n".join([ "int range_start[] =  { " + ", ".join(rangeMR.getDigits()) + " };",
                                "int range_radixes[] = { " + ", ".join(rangeMR.getRadixes()) + " };",
                                "int permutation[] = { " + ", ".join(range.permutation()) + " };",
                                "mixed_radix_int_t range_mr = {",
                                "    " + sizeMR + ",",
                                "    range_start,",
                                "    range_radixes,",
                                "    permutation",
                                "};",
                                "for (int range_count = " + range.start + "; range_count < " + range.start + " + " + range.width + "; range_count++) {"
                                ])
                    )
            self.indent()
            self.pr("\n".join([ "int " + ri + " = mixed_radix_parent(&range_mr, " + nestedLevel + "); // Runtime index.",
                                "SUPPRESS_UNUSED_WARNING(" + ri + ");",
                                "int " + ci + " = range_mr.digits[0]; // Channel index.",
                                "SUPPRESS_UNUSED_WARNING(" + ci + ");",
                                "int " + bi + " = " + ("0" if sizeMR <= 1 else "range_mr.digits[1]") + "; // Bank index.",
                                "SUPPRESS_UNUSED_WARNING(" + bi + ");"]))
            if isFederated:
                if restrict:
                    self.pr("if (range_mr.digits[range_mr.size - 1] == " + currentFederate.bankIndex + ") {")
                    self.indent()
                else:
                    self.startScopedBlock()
        else:
            ciValue = rangeMR.getDigits().get(0)
            riValue = rangeMR.get(nestedLevel)
            biValue = rangeMR.getDigits().get(1) if (sizeMR > 1) else 0
            if isFederated:
                if restrict:
                    self.pr("if (" + rangeMR.get(sizeMR - 1) + " == " + currentFederate.bankIndex + ") {")
                    self.indent()
                else:
                    self.startScopedBlock()
            self.pr("\n".join(["int " + ri + " = " + riValue + "; SUPPRESS_UNUSED_WARNING(" + ri + "); // Runtime index.",
                               "int " + ci + " = " + ciValue + "; SUPPRESS_UNUSED_WARNING(" + ci + "); // Channel index.",
                               "int " + bi + " = " + biValue + "; SUPPRESS_UNUSED_WARNING(" + bi + "); // Bank index.",
                               "int range_count = 0; SUPPRESS_UNUSED_WARNING(range_count);"]))

    @startScopedRangeBlock.register(object, FederateInstance, SendRange, RuntimeRange, bool)
    def startScopedRangeBlock_0(self,
                                currentFederate,
                                srcRange,
                                dstRange,
                                isFederated):
        """ generated source for method startScopedRangeBlock_0 """

        srcRangeMR = srcRange.startMR()
        srcSizeMR = srcRangeMR.getRadixes().size()
        srcNestedLevel = 2 if (srcRange.instance.isInput()) else 1
        dstNested = dstRange.instance.isOutput()
        self.pr("// Iterate over ranges " + srcRange + " and " + dstRange + ".")
        if isFederated and srcRange.width == 1:
            self.pr("if (" + srcRangeMR.get(srcRangeMR.numDigits() - 1) + " == " + currentFederate.bankIndex + ") {")
            self.indent()
        else:
            self.startScopedBlock()
        if srcRange.width > 1:
            self.pr("\n".join(["int src_start[] =  { " + ", ".join(srcRangeMR.getDigits())+ " };",
                               "int src_value[] =  { " + ", ".join(srcRangeMR.getDigits()) + " }; // Will be incremented.",
                               "int src_radixes[] = { " +", ".join(srcRangeMR.getRadixes()) + " };",
                               "int src_permutation[] = { " + ", ".join(srcRange.permutation()) + " };",
                               "mixed_radix_int_t src_range_mr = {", "    " + srcSizeMR + ",",
                               "    src_value,", "    src_radixes,", "    src_permutation", "};"]))
        else:
            ciValue = srcRangeMR.getDigits().get(0)
            biValue = srcRangeMR.getDigits().get(1) if (srcSizeMR > 1) else 0
            riValue = srcRangeMR.get(srcNestedLevel)
            self.pr("\n".join(["int " + CMixedRadixGenerator.sr + " = " + riValue + "; // Runtime index.",
                               "SUPPRESS_UNUSED_WARNING(" + CMixedRadixGenerator.sr + ");",
                               "int " + CMixedRadixGenerator.sc + " = " + ciValue + "; // Channel index.",
                               "SUPPRESS_UNUSED_WARNING(" + CMixedRadixGenerator.sc + ");",
                               "int " + CMixedRadixGenerator.sb + " = " + biValue + "; // Bank index.", "SUPPRESS_UNUSED_WARNING(" + CMixedRadixGenerator.sb + ");"]
                              ))
        self.startScopedRangeBlock(currentFederate, dstRange, CMixedRadixGenerator.dr, CMixedRadixGenerator.db, CMixedRadixGenerator.dc, dstNested, isFederated, True)
        if srcRange.width > 1:
            self.pr("\n".join(["int " + CMixedRadixGenerator.sr + " = mixed_radix_parent(&src_range_mr, " + srcNestedLevel + "); // Runtime index.",
                               "SUPPRESS_UNUSED_WARNING(" + CMixedRadixGenerator.sr + ");",
                               "int " + CMixedRadixGenerator.sc + " = src_range_mr.digits[0]; // Channel index.",
                               "SUPPRESS_UNUSED_WARNING(" + CMixedRadixGenerator.sc + ");",
                               "int " + CMixedRadixGenerator.sb + " = " + ("0" if srcSizeMR <= 1 else "src_range_mr.digits[1]") + "; // Bank index.",
                               "SUPPRESS_UNUSED_WARNING(" + CMixedRadixGenerator.sb + ");"]))
        if isFederated and srcRange.width > 1:
            self.pr("if (src_range_mr.digits[src_range_mr.size - 1] == " + currentFederate.bankIndex + ") {")
            self.indent()

    def endScopedBlock(self):
        """ generated source for method endScopedBlock """
        self.unindent()
        self.pr("}")

    def endChannelIteration(self, port):
        """ generated source for method endChannelIteration """
        if port.isMultiport:
            self.unindent()
            self.pr("}")

    def endScopedBankChannelIteration(self, port, count):
        """ generated source for method endScopedBankChannelIteration """
        if count != None:
            self.pr(count + "++;")
        self.endChannelIteration(port)
        self.endScopedBlock()
        if count != None:
            self.endScopedBlock()

    @overloaded
    def endScopedRangeBlock(self, range, isFederated):
        """ generated source for method endScopedRangeBlock """
        if isFederated:
            self.endScopedBlock()
        if range.width > 1:
            self.pr("mixed_radix_incr(&range_mr);")
            self.endScopedBlock()
        self.endScopedBlock()

    @endScopedRangeBlock.register(object, SendRange, RuntimeRange, bool)
    def endScopedRangeBlock_0(self, srcRange, dstRange, isFederated):
        """ generated source for method endScopedRangeBlock_0 """
        if isFederated:
            if srcRange.width > 1:
                self.endScopedBlock()
            self.endScopedBlock()
        if srcRange.width > 1:
            self.pr("\n".join(["mixed_radix_incr(&src_range_mr);",
                               "if (mixed_radix_to_int(&src_range_mr) >= " + srcRange.start + " + " + srcRange.width + ") {",
                               "    // Start over with the source.",
                               "    for (int i = 0; i < src_range_mr.size; i++) {",
                               "        src_range_mr.digits[i] = src_start[i];", "    }", "}"]))
        if dstRange.width > 1:
            self.pr("mixed_radix_incr(&range_mr);")
            self.endScopedBlock()
        self.endScopedBlock()
        self.endScopedBlock()

    def __str__(self):
        """ generated source for method toString """
        return self.code_.__str__()

    def unindent(self):
        """ generated source for method unindent """
        self.indentation = self.indentation[0:max(0, 4 - len(self.indentation))]

    def writeToFile(self, path):
        """ generated source for method writeToFile """
        ret = CodeMap.fromGeneratedCode(self.code_.__str__())
        FileUtil.writeToFile(ret.getGeneratedCode(), path, True)
        return ret


