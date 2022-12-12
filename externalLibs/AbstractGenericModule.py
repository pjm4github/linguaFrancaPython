#!/usr/bin/env python
""" generated source for module AbstractGenericModule """
# 
#  * Copyright (c) 2008 itemis AG (http://www.itemis.eu) and others.
#  * This program and the accompanying materials are made available under the
#  * terms of the Eclipse Public License 2.0 which is available at
#  * http://www.eclipse.org/legal/epl-2.0.
#  *
#  * SPDX-License-Identifier: EPL-2.0
#  
# package: org.eclipse.xtext.service
# import java.io.IOException
#
# import java.io.InputStream
#
# import java.lang.reflect.Method
#
# import java.util.Properties
#
# import org.apache.log4j.Logger
#
# import com.google.inject.Binder
#
# import com.google.inject.Module
#
# import com.google.inject.name.Names

# 
#  * @author Heiko Behrens - Initial contribution and API
#  * @author Sven Efftinge
#  * @author Sebastian Zarnekow
#
from logging import Logger

from externalLibs.DefaultRuntimeModule import Names
from include.SpecialExceptions import IllegalStateException, RuntimeException
from lflang.cli.LFStandaloneModule import Module
from lflang.util.Properties import Properties


class CompoundModule:
    pass


class FreeModule:
    pass


class BindModule:
    pass


class ProviderModule:
    pass


class AbstractGenericModule(Module):
    """ generated source for class AbstractGenericModule """
    def configure(self, binder):
        """ generated source for method configure """
        compound = self.getBindings()
        compound.configure(binder)

    def getBindings(self):
        """ generated source for method getBindings """
        methods = self.__class__.getMethods()
        result = CompoundModule()
        for method_ in methods:
            try:
                if method_.__name__.startsWith("bind"):
                    result.add(BindModule(method_, self))
                elif method_.__name__.startsWith("provide"):
                    result.add(ProviderModule(method_, self))
                elif method_.__name__.startsWith("configure"):
                    if not method_.__name__ == "configure" and len(self.length) and method_.getParameterTypes()[0] == Binder.__class__:
                        result.add(FreeModule(method_, self))
            except Exception as e:
                self.LOGGER.warn("Trying to use method " + method_.toGenericString() + " for configuration failed", e)
        return result

    def bindProperties(self, binder, propertyFilePath):
        """ generated source for method bindProperties """
        try:
            in_ = self.getClass().getClassLoader().getResourceAsStream(propertyFilePath)
            if in_ != None:
                properties = Properties()
                properties.load(in_)
                Names.bindProperties(binder, properties)
            else:
                raise IllegalStateException("Couldn't find property file : " + propertyFilePath)
        except IOError as e:
            raise RuntimeException(e)

    def tryBindProperties(self, binder, propertyFilePath):
        """ generated source for method tryBindProperties """
        try:
            in_ = self.getClass().getClassLoader().getResourceAsStream(propertyFilePath)
            if in_ != None:
                properties = Properties()
                properties.load(in_)
                Names.bindProperties(binder, properties)
                return properties
            else:
                return None
        except IOError as e:
            return None

AbstractGenericModule.LOGGER = Logger.getLogger(AbstractGenericModule.__class__)
