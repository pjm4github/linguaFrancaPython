#!/usr/bin/env python
""" generated source for module NamedInstanceUtil """
# 
# Copyright (c) 2020, Kiel University.
# *
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# *
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# *
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# *
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# package: org.lflang.diagram.synthesis.util
# import de.cau.cs.kieler.klighd.kgraph.KGraphElement
# import org.eclipse.elk.graph.properties.IPropertyHolder
# import org.eclipse.elk.graph.properties.Property

from org.lflang.generator import NamedInstance

# 
#  * Utility class to link KGraphElements to NamedInstances.
#  * 
#  * @author{Alexander Schulz-Rosengarten <als@informatik.uni-kiel.de>}
#
import configparser
config = configparser.RawConfigParser()

class NamedInstanceUtil(object):
    """ generated source for class NamedInstanceUtil """
    LINKED_INSTANCE = config.get("org.lflang.linguafranca.diagram.synthesis.graph.instance")

    #      * Establishes a link between KGraphElement and NamedInstance.
    #      
    @classmethod
    def linkInstance(cls, elem, instance):
        """ generated source for method linkInstance """
        return elem.setProperty(cls.LINKED_INSTANCE, instance)

    #      * Returns the linked NamedInstance for ther given KGraphElement.
    #      
    @classmethod
    def getLinkedInstance(cls, elem):
        """ generated source for method getLinkedInstance """
        instance = elem.getProperty(cls.LINKED_INSTANCE)
        if instance != None:
            return instance
        return None
