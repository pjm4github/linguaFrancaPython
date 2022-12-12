#!/usr/bin/env python
""" generated source for module DefaultRuntimeModule """
# 
#  * Copyright (c) 2008, 2020 itemis AG (http://www.itemis.eu) and others.
#  * This program and the accompanying materials are made available under the
#  * terms of the Eclipse Public License 2.0 which is available at
#  * http://www.eclipse.org/legal/epl-2.0.
#  *
#  * SPDX-License-Identifier: EPL-2.0
#  
# package: org.eclipse.xtext.service
# import org.eclipse.emf.ecore.EPackage
# import eclipse.emf.ecore.EValidator
# import eclipse.emf.ecore.resource.ResourceSet
# import eclipse.emf.ecore.util.Diagnostician
# import eclipse.xtext.common.services.DefaultTerminalConverters
# import eclipse.xtext.formatting.IFormatter
# import eclipse.xtext.formatting.INodeModelFormatter
# import eclipse.xtext.formatting.impl.DefaultNodeModelFormatter
# import eclipse.xtext.formatting.impl.OneWhitespaceFormatter
# import eclipse.xtext.linking.ILinkingService
# import eclipse.xtext.linking.LinkingScopeProviderBinding
# import eclipse.xtext.linking.impl.DefaultLinkingService
# import eclipse.xtext.linking.lazy.LazyLinker
# import eclipse.xtext.linking.lazy.LazyLinkingResource
# import eclipse.xtext.linking.lazy.LazyURIEncoder
# import eclipse.xtext.naming.IQualifiedNameProvider
# import eclipse.xtext.naming.SimpleNameProvider
# import eclipse.xtext.parser.EclipseProjectPropertiesEncodingProvider
# import eclipse.xtext.parser.IEncodingProvider
# import eclipse.xtext.parser.antlr.AntlrTokenToStringConverter
# import eclipse.xtext.parser.antlr.ITokenDefProvider
# import eclipse.xtext.parser.antlr.NullTokenDefProvider
# import eclipse.xtext.parser.impl.PartialParsingHelper
# import eclipse.xtext.parsetree.reconstr.ITransientValueService
# import eclipse.xtext.parsetree.reconstr.impl.DefaultTransientValueService
# import eclipse.xtext.resource.DefaultFragmentProvider
# import eclipse.xtext.resource.DefaultLocationInFileProvider
# import eclipse.xtext.resource.IContainer
# import eclipse.xtext.resource.IFragmentProvider
# import eclipse.xtext.resource.ILocationInFileProvider
# import eclipse.xtext.resource.IResourceDescriptions
# import eclipse.xtext.resource.IResourceFactory
# import eclipse.xtext.resource.IResourceServiceProvider
# import eclipse.xtext.resource.SynchronizedXtextResourceSet
# import eclipse.xtext.resource.XtextResource
# import eclipse.xtext.resource.XtextResourceFactory
# import eclipse.xtext.resource.XtextResourceSet
# import eclipse.xtext.resource.impl.IsAffectedExtension
# import eclipse.xtext.resource.impl.IsAffectedExtension.AllIsAffectedExtensions
# import eclipse.xtext.resource.impl.ResourceDescriptionsProvider
# import eclipse.xtext.resource.impl.ResourceSetBasedResourceDescriptions
# import eclipse.xtext.resource.impl.SimpleResourceDescriptionsBasedContainerManager
# import eclipse.xtext.scoping.IGlobalScopeProvider
# import eclipse.xtext.scoping.IScopeProvider
# import eclipse.xtext.scoping.impl.ImportUriGlobalScopeProvider
# import eclipse.xtext.scoping.impl.SimpleLocalScopeProvider
# import eclipse.xtext.serializer.ISerializer
# import eclipse.xtext.serializer.sequencer.BacktrackingSemanticSequencer
# import eclipse.xtext.serializer.sequencer.GenericSequencer
# import eclipse.xtext.serializer.sequencer.ISemanticSequencer
# import eclipse.xtext.serializer.tokens.SerializerScopeProviderBinding
# import eclipse.xtext.validation.CancelableDiagnostician
# import eclipse.xtext.validation.IConcreteSyntaxValidator
# import eclipse.xtext.validation.INamesAreUniqueValidationHelper
# import eclipse.xtext.validation.impl.ConcreteSyntaxValidator
# import com.google.common.collect.ImmutableList
# import com.google.inject.Binder
# import com.google.inject.Key
# import com.google.inject.Provider
# import com.google.inject.TypeLiteral
# import com.google.inject.name.Names

# 
#  * @author Heiko Behrens - Initial contribution and API
#  * @author Sven Efftinge
#  * @author Jan Koehnlein
#
from xmlrpc.client import Boolean

from externalLibs.AbstractGenericModule import AbstractGenericModule
from lflang.AbstractLFRuntimeModule import AntlrTokenToStringConverter
from lflang.cli.LFStandaloneModule import EValidator
from lflang.lf.Serializer import Serializer
from lflang.lf.impl.LfPackageImpl import EPackage


class DispatchingProvider:
    pass


class IEncodingProvider:
    pass


class IEncodingProviderDispatcher(DispatchingProvider, IEncodingProvider):
    def __init__(self, ):
        pass
        """ generated source for class IEncodingProviderDispatcher """


class IResourceServiceProvider:
    pass


class CancelableDiagnostician:
    pass


class DefaultFragmentProvider:
    pass


class DefaultTransientValueService:
    pass


class DefaultLocationInFileProvider:
    pass


class OneWhitespaceFormatter:
    pass


class DefaultNodeModelFormatter:
    pass


class SuppressWarnings:
    pass


class BacktrackingSemanticSequencer:
    pass


class ConcreteSyntaxValidator:
    pass


class XtextResourceFactory:
    pass


class DefaultLinkingService:
    pass


class SimpleLocalScopeProvider:
    pass


class IScopeProvider:
    pass


class SerializerScopeProviderBinding:
    pass


class LinkingScopeProviderBinding:
    pass


class ImportUriGlobalScopeProvider:
    pass


class IResourceDescriptions:
    pass


class ResourceSetBasedResourceDescriptions:
    pass


class SimpleNameProvider:
    pass


class LazyLinker:
    pass


class DefaultTerminalConverters:
    pass


class PartialParsingHelper:
    pass


class NullTokenDefProvider:
    pass


class DefaultEcoreElementFactory:
    pass


class LazyLinkingResource:
    pass


class XtextResourceSet:
    pass


class SynchronizedXtextResourceSet:
    pass


class SimpleResourceDescriptionsBasedContainerManager:
    pass


class EclipseProjectPropertiesEncodingProvider:
    pass


class Names:
    pass


class ResourceDescriptionsProvider:
    pass


class ISemanticSequencer:
    pass


class GenericSequencer:
    pass


class LazyURIEncoder:
    pass


class TypeLiteral:
    pass


class AllIsAffectedExtensions:
    pass


class IsAffectedExtension:
    pass


class Key:
    pass


class INamesAreUniqueValidationHelper:
    pass


class DefaultRuntimeModule(AbstractGenericModule):
    """ generated source for class DefaultRuntimeModule """
    def configure(self, binder):
        """ generated source for method configure """
        super(DefaultRuntimeModule, self).configure(binder)

    def bindEValidatorRegistry(self):
        """ generated source for method bindEValidatorRegistry """
        return EValidator.Registry.INSTANCE

    def bindEPackageRegistry(self):
        """ generated source for method bindEPackageRegistry """
        return EPackage.Registry.INSTANCE

    def bindIResourceServiceProvider_Registry(self):
        """ generated source for method bindIResourceServiceProvider$Registry """
        return IResourceServiceProvider.Registry.INSTANCE

    def bindDiagnostician(self):
        """ generated source for method bindDiagnostician """
        return CancelableDiagnostician.__class__

    def bindIFragmentProvider(self):
        """ generated source for method bindIFragmentProvider """
        return DefaultFragmentProvider.__class__

    def bindITransientValueService(self):
        """ generated source for method bindITransientValueService """
        return DefaultTransientValueService.__class__

    def bindILocationInFileProvider(self):
        """ generated source for method bindILocationInFileProvider """
        return DefaultLocationInFileProvider.__class__

    def bindIFormatter(self):
        """ generated source for method bindIFormatter """
        return OneWhitespaceFormatter.__class__

    def bindINodeModelFormatter(self):
        """ generated source for method bindINodeModelFormatter """
        return DefaultNodeModelFormatter.__class__

    @SuppressWarnings("deprecation")
    def bindISerializer(self):
        """ generated source for method bindISerializer """
        return Serializer.__class__

    # 
    # 	 * @since 2.0
    # 	 
    def bindISemanticSequencer(self):
        """ generated source for method bindISemanticSequencer """
        return BacktrackingSemanticSequencer.__class__

    def bindConcreteSyntaxValidator(self):
        """ generated source for method bindConcreteSyntaxValidator """
        return ConcreteSyntaxValidator.__class__

    def bindIResourceFactory(self):
        """ generated source for method bindIResourceFactory """
        return XtextResourceFactory.__class__

    def bindILinkingService(self):
        """ generated source for method bindILinkingService """
        return DefaultLinkingService.__class__

    def bindIScopeProvider(self):
        """ generated source for method bindIScopeProvider """
        return SimpleLocalScopeProvider.__class__

    # @since 2.4
    def configureSerializerIScopeProvider(self, binder):
        """ generated source for method configureSerializerIScopeProvider """
        binder.bind(IScopeProvider.__class__).annotatedWith(SerializerScopeProviderBinding.__class__).to(IScopeProvider.__class__)

    def configureLinkingIScopeProvider(self, binder):
        """ generated source for method configureLinkingIScopeProvider """
        binder.bind(IScopeProvider.__class__).annotatedWith(LinkingScopeProviderBinding.__class__).to(IScopeProvider.__class__)

    def bindIGlobalScopeProvider(self):
        """ generated source for method bindIGlobalScopeProvider """
        return ImportUriGlobalScopeProvider.__class__

    def configureIResourceDescriptions(self, binder):
        """ generated source for method configureIResourceDescriptions """
        binder.bind(IResourceDescriptions.__class__).to(ResourceSetBasedResourceDescriptions.__class__)

    def bindIQualifiedNameProvider(self):
        """ generated source for method bindIQualifiedNameProvider """
        return SimpleNameProvider.__class__

    def bindILinker(self):
        """ generated source for method bindILinker """
        return LazyLinker.__class__

    def bindIValueConverterService(self):
        """ generated source for method bindIValueConverterService """
        return DefaultTerminalConverters.__class__

    def bindITokenToStringConverter(self):
        """ generated source for method bindITokenToStringConverter """
        return AntlrTokenToStringConverter.__class__

    def bindIPartialParserHelper(self):
        """ generated source for method bindIPartialParserHelper """
        return PartialParsingHelper.__class__

    def bindITokenDefProvider(self):
        """ generated source for method bindITokenDefProvider """
        return NullTokenDefProvider.__class__

    def bindIAstFactory(self):
        """ generated source for method bindIAstFactory """
        return DefaultEcoreElementFactory.__class__

    def bindXtextResource(self):
        """ generated source for method bindXtextResource """
        return LazyLinkingResource.__class__

    def bindResourceSet(self):
        """ generated source for method bindResourceSet """
        return XtextResourceSet.__class__

    def bindXtextResourceSet(self):
        """ generated source for method bindXtextResourceSet """
        return SynchronizedXtextResourceSet.__class__

    def bindIContainer_Manager(self):
        """ generated source for method bindIContainer$Manager """
        return SimpleResourceDescriptionsBasedContainerManager.__class__

    def configureRuntimeEncodingProvider(self, binder):
        """ generated source for method configureRuntimeEncodingProvider """
        binder.bind(IEncodingProvider.__class__).annotatedWith(DispatchingProvider.Runtime.__class__).to(IEncodingProvider.Runtime.__class__)

    def bindRuntimeEncodingProvider(self):
        """ generated source for method bindRuntimeEncodingProvider """
        return EclipseProjectPropertiesEncodingProvider.__class__

    def provideIEncodingProvider(self):
        """ generated source for method provideIEncodingProvider """
        return IEncodingProviderDispatcher.__class__



    def configureIResourceDescriptionsBuilderScope(self, binder):
        """ generated source for method configureIResourceDescriptionsBuilderScope """
        binder.bind(IResourceDescriptions.__class__).annotatedWith(Names.named(ResourceDescriptionsProvider.NAMED_BUILDER_SCOPE)).to(ResourceSetBasedResourceDescriptions.__class__)

    def configureIResourceDescriptionsLiveScope(self, binder):
        """ generated source for method configureIResourceDescriptionsLiveScope """
        binder.bind(IResourceDescriptions.__class__).annotatedWith(Names.named(ResourceDescriptionsProvider.LIVE_SCOPE)).to(ResourceSetBasedResourceDescriptions.__class__)

    def configureGenericSemanticSequencer(self, binder):
        """ generated source for method configureGenericSemanticSequencer """
        binder.bind(ISemanticSequencer.__class__).annotatedWith(GenericSequencer.__class__).to(BacktrackingSemanticSequencer.__class__)

    def configureUseIndexFragmentsForLazyLinking(self, binder):
        """ generated source for method configureUseIndexFragmentsForLazyLinking """
        binder.bind(Boolean.TYPE).annotatedWith(Names.named(LazyURIEncoder.USE_INDEXED_FRAGMENTS_BINDING)).toInstance(Boolean.TRUE)

    def configureIsAffectedExtensions(self, binder):
        """ generated source for method configureIsAffectedExtensions """
        binder.bind(TypeLiteral()).toProvider(AllIsAffectedExtensions.__class__)
        binder.bind(Key.get(IsAffectedExtension.__class__, Names.named("IsAffectedExtension.UniqueNames"))).to(INamesAreUniqueValidationHelper.ContextProvider.__class__)
