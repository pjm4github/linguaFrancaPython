#!/usr/bin/env python
""" generated source for module LFResourceDescriptionStrategy """
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
# package: org.lflang
# import java.util.Map
# import java.util.stream.Collectors
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.xtext.naming.QualifiedName
# import org.eclipse.xtext.resource.EObjectDescription
# import org.eclipse.xtext.resource.IEObjectDescription
# import org.eclipse.xtext.resource.impl.DefaultResourceDescriptionStrategy
# import org.eclipse.xtext.scoping.impl.ImportUriResolver
# import org.eclipse.xtext.util.IAcceptor

from org.lflang.lf import Model
# import com.google.inject.Inject

# 
#  * Resource description strategy designed to limit global scope to only those
#  * files that were explicitly imported.
#  * <p>
#  * Adapted from example provided by Itemis.
#  *
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  * @see "https://blogs.itemis.com/en/in-five-minutes-to-transitive-imports-within-a-dsl-with-xtext"
#  
class LFResourceDescriptionStrategy(DefaultResourceDescriptionStrategy):
    """ generated source for class LFResourceDescriptionStrategy """
    #      * Key used in user data attached to description of a Model.
    #      
    INCLUDES = "includes"

    #      * Delimiter used in the values associated with INCLUDES keys in the
    #      * user-data descriptions of Models.
    #      
    DELIMITER = ","
    uriResolver = None

    def createEObjectDescriptions(self, eObject, acceptor):
        """ generated source for method createEObjectDescriptions """
        if isinstance(eObject, (Model)):
            self.createEObjectDescriptionForModel(eObject, acceptor)
            return True
        else:
            return super(LFResourceDescriptionStrategy, self).createEObjectDescriptions(eObject, acceptor)

    #      * Build an index containing the strings of the URIs imported resources.
    #      * <p>
    #      * All the URIs are added to comma-separated string and stored under the
    #      * key "includes" in the userData map of the object description.
    #      
    def createEObjectDescriptionForModel(self, model, acceptor):
        """ generated source for method createEObjectDescriptionForModel """
        uris = model.getImports().stream().map(self.uriResolver).collect(Collectors.joining(self.DELIMITER))
        userData = Map.of(self.INCLUDES, uris)
        qname = QualifiedName.create(model.eResource().getURI().__str__())
        acceptor.accept(EObjectDescription.create(qname, model, userData))
