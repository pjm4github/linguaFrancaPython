#!/usr/bin/env python
""" generated source for module AttributeSpec """
# 
#  * Copyright (c) 2019-2022, The University of California at Berkeley.
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
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
# package: org.lflang.validation
# import java.util.HashMap
# import java.util.HashSet
# import java.util.List
# import java.util.Map
# import java.util.Set
# import java.util.stream.Collectors

from org.lflang.lf import AttrParm

from org.lflang.lf import Attribute

from org.lflang.lf.LfPackage import Literals

# 
#  * Specification of the structure of an attribute annotation.
#  * 
#  * @author{Clément Fournier, TU Dresden, INSA Rennes}
#  * @author{Shaokai Lin <shaokai@berkeley.edu>}
#  
class AttributeSpec(object):
    """ generated source for class AttributeSpec """
    paramSpecByName = None
    VALUE_ATTR = "value"

    #  A map from a string to a supported AttributeSpec 
    ATTRIBUTE_SPECS_BY_NAME = dict()

    def __init__(self, params):
        """ generated source for method __init__ """
        if params != None:
            # paramSpecByName = params.stream().collect(Collectors.toMap(it -> it.name, it -> it));
            for it in params.stream():
                self.paramSpecByName.append((it.name, it))
        else:
            self.paramSpecByName = None

    #      * Check that the attribute conforms to this spec and whether
    #      * attr has the correct name.
    #      
    def check(self, validator, attr):
        """ generated source for method check """
        seen = None
        #  If there is just one parameter, it is required to be named "value".
        if attr.getAttrParms() != None and attr.getAttrParms().size() == 1 and attr.getAttrParms().get(0).__name__ == None:
            if self.paramSpecByName == None:
                validator.error("Attribute doesn't take a parameter.", Literals.ATTRIBUTE__ATTR_NAME)
                return
            valueSpec = self.paramSpecByName.get(self.VALUE_ATTR)
            if valueSpec == None:
                validator.error("Attribute doesn't have a 'value' parameter.", Literals.ATTR_PARM__NAME)
                return
            valueSpec.check(validator, attr.getAttrParms().get(0))
            seen = set(self.VALUE_ATTR)
        else:
            seen = self.processNamedAttrParms(validator, attr)
        if self.paramSpecByName != None:
            missingParams = dict(self.paramSpecByName)
            missingParams.keySet().removeAll(seen)
            for p in missingParams:
                name = p[0]
                paramSpec = p[1]
                if not paramSpec.isOptional():
                    validator.error("Missing required attribute parameter '" + name + "'.", Literals.ATTRIBUTE__ATTR_PARMS)

    def processNamedAttrParms(self, validator, attr):
        """ generated source for method processNamedAttrParms """
        seen = set()
        if attr.getAttrParms() != None:
            for parm in attr.getAttrParms():
                if self.paramSpecByName == None:
                    validator.error("Attribute does not take parameters.", Literals.ATTRIBUTE__ATTR_NAME)
                    break
                if parm.__name__ == None:
                    validator.error("Missing name for attribute parameter.", Literals.ATTRIBUTE__ATTR_NAME)
                    continue 
                parmSpec = self.paramSpecByName.get(parm.__name__)
                if parmSpec == None:
                    validator.error("\"" + parm.__name__ + "\"" + " is an unknown attribute parameter.", Literals.ATTRIBUTE__ATTR_NAME)
                    continue 
                parmSpec.check(validator, parm)
                seen.append(parm.__name__)
        return seen

    AttrParamSpec = None
