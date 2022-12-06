#!/usr/bin/env python
""" generated source for module LFScopeProviderImpl """
# 
# Copyright (c) 2020, The University of California at Berkeley.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
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
# package: org.lflang.scoping
import 

import 
# import com.google.inject.Inject
# import java.util.ArrayList
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.EReference
# import org.eclipse.xtext.naming.SimpleNameProvider
# import org.eclipse.xtext.scoping.IScope
# import org.eclipse.xtext.scoping.Scopes
# import org.eclipse.xtext.scoping.impl.SelectableBasedScope

from org.lflang.lf


#  * This class enforces custom rules. In particular, it resolves references to
#  * parameters, ports, actions, and timers. Ports can be referenced across at
#  * most one level of hierarchy. Parameters, actions, and timers can be
#  * referenced locally, within the reactor.
#  *
#  * @author Marten Lohstroh
#  * @see <a href="https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#scoping"></a>
#  
class LFScopeProviderImpl(AbstractLFScopeProvider):
    """ generated source for class LFScopeProviderImpl """
    nameProvider = None
    scopeProvider = None

    #      * Enumerate of the kinds of references.
    #      
    class RefType:
        """ generated source for enum RefType """
        NULL = 'NULL'
        TRIGGER = 'TRIGGER'
        SOURCE = 'SOURCE'
        EFFECT = 'EFFECT'
        DEADLINE = 'DEADLINE'
        CLEFT = 'CLEFT'
        CRIGHT = 'CRIGHT'

    #      * Depending on the provided context, construct the appropriate scope
    #      * for the given reference.
    #      *
    #      * @param context   The AST node in which a to-be-resolved reference occurs.
    #      * @param reference The reference to resolve.
    #      
    def getScope(self, context, reference):
        """ generated source for method getScope """
        if isinstance(context, (VarRef)):
            return getScopeForVarRef(context, reference)
        elif isinstance(context, (Assignment)):
            return getScopeForAssignment(context, reference)
        elif isinstance(context, (Instantiation)):
            return getScopeForReactorDecl(context, reference)
        elif isinstance(context, (Reactor)):
            return getScopeForReactorDecl(context, reference)
        elif isinstance(context, (ImportedReactor)):
            return getScopeForImportedReactor(context, reference)
        return super(LFScopeProviderImpl, self).getScope(context, reference)

    #      * Filter out candidates that do not originate from the file listed in
    #      * this particular import statement.
    #      
    def getScopeForImportedReactor(self, context, reference):
        """ generated source for method getScopeForImportedReactor """
        importURI = (context.eContainer()).getImportURI()
        importedURI = self.scopeProvider.resolve("" if importURI == None else importURI, context.eResource())
        if importedURI != None:
            uniqueImportURIs = self.scopeProvider.getImportedUris(context.eResource())
            descriptions = self.scopeProvider.getResourceDescriptions(context.eResource(), uniqueImportURIs)
            description = descriptions.getResourceDescription(importedURI)
            return SelectableBasedScope.createScope(IScope.NULLSCOPE, description, None, reference.getEReferenceType(), False)
        return Scopes.scopeFor(emptyList())

    #      * @param obj       Instantiation or Reactor that has a ReactorDecl to resolve.
    #      * @param reference The reference to link to a ReactorDecl node.
    #      
    def getScopeForReactorDecl(self, obj, reference):
        """ generated source for method getScopeForReactorDecl """
        #  Find the local Model
        model = None
        container = obj
        while model == None and container != None:
            container = container.eContainer()
            if isinstance(container, (Model)):
                model = container
        if model == None:
            return Scopes.scopeFor(emptyList())
        #  Collect eligible candidates, all of which are local (i.e., not in other files).
        locals = ArrayList(model.getReactors())
        #  Either point to the import statement (if it is renamed)
        #  or directly to the reactor definition.
        for it in model.getImports():
            for ir in it.getReactorClasses():
                if ir.__name__ != None:
                    locals.append(ir)
                elif ir.getReactorClass() != None:
                    locals.append(ir.getReactorClass())
        return Scopes.scopeFor(locals)

    def getScopeForAssignment(self, assignment, reference):
        """ generated source for method getScopeForAssignment """
        if reference == LfPackage.Literals.ASSIGNMENT__LHS:
            defn = toDefinition((assignment.eContainer()).getReactorClass())
            if defn != None:
                return Scopes.scopeFor(allParameters(defn))
        if reference == LfPackage.Literals.ASSIGNMENT__RHS:
            return Scopes.scopeFor((assignment.eContainer().eContainer()).getParameters())
        return Scopes.scopeFor(emptyList())

    def getScopeForVarRef(self, variable, reference):
        """ generated source for method getScopeForVarRef """
        if reference == LfPackage.Literals.VAR_REF__VARIABLE:
            #  Resolve hierarchical reference
            reactor = None
            mode = None
            if isinstance(, (Reactor)):
                reactor = variable.eContainer().eContainer()
            elif isinstance(, (Mode)):
                mode = variable.eContainer().eContainer()
                reactor = variable.eContainer().eContainer().eContainer()
            else:
                return Scopes.scopeFor(emptyList())
            type = getRefType(variable)
            if variable.getContainer() != None:
                instanceName = self.nameProvider.getFullyQualifiedName(variable.getContainer())
                instances = ArrayList(reactor.getInstantiations())
                if mode != None:
                    instances.extend(mode.getInstantiations())
                if instanceName != None:
                    for instance in instances:
                        defn = toDefinition(instance.getReactorClass())
                        if defn != None and instance.__name__ == instanceName.__str__():
                            if type == TRIGGER:
                                pass
                            elif type == SOURCE:
                                pass
                            elif type == CLEFT:
                                return Scopes.scopeFor(allOutputs(defn))
                            elif type == EFFECT:
                                pass
                            elif type == DEADLINE:
                                pass
                            elif type == CRIGHT:
                                return Scopes.scopeFor(allInputs(defn))
                return Scopes.scopeFor(emptyList())
            else:
                if type == TRIGGER:
                    candidates = []
                    if mode != None:
                        candidates.extend(mode.getActions())
                        candidates.extend(mode.getTimers())
                    candidates.extend(allInputs(reactor))
                    candidates.extend(allActions(reactor))
                    candidates.extend(allTimers(reactor))
                    return Scopes.scopeFor(candidates)
                elif type == SOURCE:
                    return super(LFScopeProviderImpl, self).getScope(variable, reference)
                elif type == EFFECT:
                    candidates = []
                    if mode != None:
                        candidates.extend(mode.getActions())
                        candidates.extend(reactor.getModes())
                    candidates.extend(allOutputs(reactor))
                    candidates.extend(allActions(reactor))
                    return Scopes.scopeFor(candidates)
                elif type == DEADLINE:
                    pass
                elif type == CLEFT:
                    return Scopes.scopeFor(allInputs(reactor))
                elif type == CRIGHT:
                    return Scopes.scopeFor(allOutputs(reactor))
                else:
                    return Scopes.scopeFor(emptyList())
        else:
            return super(LFScopeProviderImpl, self).getScope(variable, reference)

    def getRefType(self, variable):
        """ generated source for method getRefType """
        if isinstance(, (Deadline)):
            return self.RefType.DEADLINE
        elif isinstance(, (Reaction)):
            reaction = variable.eContainer()
            if reaction.getTriggers().contains(variable):
                return self.RefType.TRIGGER
            elif reaction.getSources().contains(variable):
                return self.RefType.SOURCE
            elif reaction.getEffects().contains(variable):
                return self.RefType.EFFECT
        elif isinstance(, (Connection)):
            conn = variable.eContainer()
            if conn.getLeftPorts().contains(variable):
                return self.RefType.CLEFT
            elif conn.getRightPorts().contains(variable):
                return self.RefType.CRIGHT
        return self.RefType.NULL
