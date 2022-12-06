#!/usr/bin/env python
""" generated source for module RustTargetConfig """
# 
#  * Copyright (c) 2021, TU Dresden.
#  *
#  * Redistribution and use in source and binary forms, with or without modification,
#  * are permitted provided that the following conditions are met:
#  *
#  * 1. Redistributions of source code must retain the above copyright notice,
#  *    this list of conditions and the following disclaimer.
#  *
#  * 2. Redistributions in binary form must reproduce the above copyright notice,
#  *    this list of conditions and the following disclaimer in the documentation
#  *    and/or other materials provided with the distribution.
#  *
#  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  * THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  * THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.generator.rust
# import java.nio.file.Files
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.HashMap
# import java.util.List
# import java.util.Locale
# import java.util.Map
# import org.eclipse.emf.ecore.EObject

from org.lflang.ErrorReporter

from org.lflang.TargetProperty.BuildType

# 
#  * Rust-specific part of a {@link org.lflang.TargetConfig}.
#  *
#  * @author Clément Fournier - TU Dresden, INSA Rennes
#  
class RustTargetConfig(object):
    """ generated source for class RustTargetConfig """
    # List of Cargo features of the generated crate to enable.
    #       
    cargoFeatures = []

    # Map of Cargo dependency to dependency properties.
    #       
    cargoDependencies = dict()

    # List of top-level modules, those are absolute paths.
    #       
    rustTopLevelModules = []

    # Cargo profile, default is debug (corresponds to cargo dev profile).
    #       
    profile = BuildType.DEBUG

    def setCargoFeatures(self, cargoFeatures):
        """ generated source for method setCargoFeatures """
        self.cargoFeatures = cargoFeatures

    def setCargoDependencies(self, cargoDependencies):
        """ generated source for method setCargoDependencies """
        self.cargoDependencies = cargoDependencies

    def addAndCheckTopLevelModule(self, path, errorOwner, err):
        """ generated source for method addAndCheckTopLevelModule """
        fileName = path.getFileName().__str__()
        if not Files.exists(path):
            err.reportError(errorOwner, "File not found")
        elif Files.isRegularFile(path) and not fileName.endsWith(".rs"):
            err.reportError(errorOwner, "Not a rust file")
        elif fileName == "main.rs":
            err.reportError(errorOwner, "Cannot use 'main.rs' as a module name (reserved)")
        elif fileName == "reactors" or fileName == "reactors.rs":
            err.reportError(errorOwner, "Cannot use 'reactors' as a module name (reserved)")
        elif Files.isDirectory(path) and not Files.exists(path.resolve("mod.rs")):
            err.reportError(errorOwner, "Cannot find module descriptor in directory")
        self.rustTopLevelModules.append(path)

    def getCargoFeatures(self):
        """ generated source for method getCargoFeatures """
        return self.cargoFeatures

    # Returns a map of cargo dependencies.
    #       
    def getCargoDependencies(self):
        """ generated source for method getCargoDependencies """
        return self.cargoDependencies

    # Returns the list of top-level module files to include in main.rs.
    # Those files were checked to exists previously.
    #       
    def getRustTopLevelModules(self):
        """ generated source for method getRustTopLevelModules """
        return self.rustTopLevelModules

    # The build type to use. Corresponds to a Cargo profile.
    #       
    def getBuildType(self):
        """ generated source for method getBuildType """
        return self.profile

    # Set a build profile chosen based on a cmake profile.
    #       
    def setBuildType(self, profile):
        """ generated source for method setBuildType """
        self.profile = profile
