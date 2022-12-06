#!/usr/bin/env python
""" generated source for module PythonPreambleGenerator """
# package: org.lflang.generator.python
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.List

from org.lflang import ASTUtils

from org.lflang import TargetConfig

from org.lflang.generator import CodeBuilder

from org.lflang.generator.c import CPreambleGenerator

from org.lflang.lf import Preamble

# 
#  * Generates user-defined preambles and #define and #include directives
#  * for the Python target.
#  *
#  * @author {Edward A. Lee <eal@berkeley.edu>}
#  * @author {Soroush Bateni <soroush@utdallas.edu>}
#  * @author {Hou Seng Wong <housengw@berkeley.edu>}
#  
class PythonPreambleGenerator(object):
    """ generated source for class PythonPreambleGenerator """
    #      * Generates preambles defined by user for a given reactor.
    #      * The preamble code is put inside the reactor class.
    #      
    @classmethod
    def generatePythonPreambles(cls, preambles):
        """ generated source for method generatePythonPreambles """
        preamblesCode = []
        for p in preambles:
            # preambles.forEach(p ->
            preamblesCode.append(ASTUtils.toText(p.getCode()))
            #              //);
        s = "\n".join[ preamblesCode]
        s1 = "\n".join([ "# From the preamble, verbatim:", s, "# End of preamble."])
        return s1 if len(preamblesCode) > 0 else ""

    @classmethod
    def generateCDefineDirectives(cls, targetConfig, numFederates, isFederated, srcGenPath, clockSyncIsOn, hasModalReactors):
        """ generated source for method generateCDefineDirectives """
        code_ = CodeBuilder()
        code_.pr(CPreambleGenerator.generateDefineDirectives(targetConfig, numFederates, isFederated, srcGenPath, clockSyncIsOn, hasModalReactors))
        code_.pr("#define _LF_GARBAGE_COLLECTED")
        return code_.__str__()

    @classmethod
    def generateCIncludeStatements(cls, targetConfig, isFederated, hasModalReactors):
        """ generated source for method generateCIncludeStatements """
        code_ = CodeBuilder()
        code_.pr(CPreambleGenerator.generateIncludeStatements(targetConfig, isFederated))
        code_.pr("#include \"pythontarget.c\"")
        if hasModalReactors:
            code_.pr("#include \"modal_models/definitions.h\"")
        return code_.__str__()
