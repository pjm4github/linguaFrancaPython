#!/usr/bin/env python
""" generated source for module FileConfig """
#  package org.lflang;
# 
#  # import java.io.File;
#  # import java.io.IOException;
#  # import java.nio.file.Path;
#  # import java.nio.file.Paths;
#  # import java.util.function.Consumer;
# 
#  # import org.eclipse.core.resources.IProject;
#  # import org.eclipse.core.resources.IResource;
#  # import org.eclipse.core.resources.ResourcesPlugin;
#  # import org.eclipse.emf.common.util.URI;
#  # import org.eclipse.emf.ecore.resource.Resource;
#  # import org.eclipse.xtext.generator.IFileSystemAccess2;
# 
#  from org.lflang.util.FileUtil;
# 
#  * Base class that governs the interactions between code generators and the file system.
#  *  
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  *
#
import os

from lflang.util import FileUtil


class FileConfig:
    """ generated source for class FileConfig """
    #  Public static fields.
    DEFAULT_SRC_DIR = "src"

    #      * Default name of the directory to store binaries in.
    #      
    DEFAULT_BIN_DIR = "bin"

    #      * Default name of the directory to store generated sources in.
    #      
    DEFAULT_SRC_GEN_DIR = "src-gen"

    #  Public fields.
    #      * The directory in which to put binaries, if the code generator produces any.
    #      
    binPath = None

    #      * The name of the main reactor, which has to match the file name (without
    #      * the '.lf' extension).
    #      
    name = None

    # The directory that is the root of the package in which the .lf source file resides.
    # This path is determined
    # differently depending on whether the compiler is invoked through the IDE or from the command line.
    # In the former
    # case, the package is the project root that the source resides in. In the latter case,
    # it is the parent directory
    # of the nearest `src` directory up the hierarchy, if there is one, or just the `outPath`
    # if there is none. It is
    # recommended to always keep the sources in a `src` directory regardless of the workflow,
    # in which case the
    # output behavior will be identical irrespective of the way the compiler is invoked.
    #      
    srcPkgPath = None

    # The file containing the main source code.
    # This is the Eclipse eCore view of the file, which is distinct
    # from the XText view of the file and the OS view of the file.
    #      
    resource = None

    # If running in an Eclipse IDE, the iResource refers to the
    # IFile representing the Lingua Franca program.
    # This is the XText view of the file, which is distinct
    # from the Eclipse eCore view of the file and the OS view of the file.
    #
    # This is null if running outside an Eclipse IDE.
    #      
    iResource = None

    # The full path to the file containing the .lf file including the
    # full filename with the .lf extension.
    #      
    srcFile = None

    # The directory in which the source .lf file was found.
    #      
    srcPath = None

    # Indicate whether the bin directory should be hierarchical.
    #      
    useHierarchicalBin = bool()

    #  Protected fields.
    #   Path representation of srcGenRoot, the root directory for generated
    #   sources.
    #      
    srcGenBasePath = None

    # The directory in which to put the generated sources.
    # This takes into account the location of the source file relative to the
    # package root. Specifically, if the source file is x/y/Z.lf relative
    # to the package root, then the generated sources will be put in x/y/Z
    # relative to srcGenBasePath.
    #      
    srcGenPath = None

    #  private fields
    #  The parent of the directory designated for placing generated sources into (`./src-gen` by default). Additional
    #  directories (such as `bin` or `build`) should be created as siblings of the directory for generated sources,
    #  which means that such directories should be created relative to the path assigned to this class variable.
    #
    #  The generated source directory is specified in the IDE (Project Properties->LF->Compiler->Output Folder). When
    #  invoking the standalone compiler, the output path is specified directly using the `-o` or `--output-path` option.
    #      
    outPath = None

    #      * The directory that denotes the root of the package to which the
    #      * generated sources belong. Even if the target language does not have a
    #      * notion of packages, this directory groups all files associated with a
    #      * single main reactor.
    #      * of packages.
    #      
    srcGenPkgPath = None

    def __init__(self, resource, srcGenBasePath, useHierarchicalBin):
        """ generated source for method __init__ """
        self.resource = resource
        self.useHierarchicalBin = useHierarchicalBin
        self.srcFile = FileUtil.toPath(self.resource)
        self.srcPath = self.srcFile.getParent()
        self.srcPkgPath = self.getPkgPath(resource)
        self.srcGenBasePath = srcGenBasePath
        self.name = FileUtil.nameWithoutExtension(self.srcFile)
        self.srcGenPath = srcGenBasePath.resolve(self.getSubPkgPath(self.srcPath)).resolve(self.name)
        self.srcGenPkgPath = self.srcGenPath
        self.outPath = srcGenBasePath.getParent()
        binRoot = self.outPath.resolve(self.DEFAULT_BIN_DIR)
        self.binPath = binRoot.resolve(self.getSubPkgPath(self.srcPath)) if useHierarchicalBin else binRoot
        self.iResource = FileUtil.getIResource(resource)

    #      * Get the directory a resource is located in relative to the root package
    #      
    def getDirectory(self, r):
        """ generated source for method getDirectory """
        return self.getSubPkgPath(FileUtil.toPath(r).getParent())

    # The parent of the directory designated for placing generated sources into (`./src-gen` by default). Additional
    # directories (such as `bin` or `build`) should be created as siblings of the directory for generated sources,
    # which means that such directories should be created relative to the path assigned to this class variable.
    #
    # The generated source directory is specified in the IDE (Project Properties->LF->Compiler->Output Folder). When
    # invoking the standalone compiler, the output path is specified directly using the `-o` or `--output-path` option.
    #      
    def getOutPath(self):
        """ generated source for method getOutPath """
        return self.outPath

    #  The directory in which to put the generated sources.
    #  This takes into account the location of the source file relative to the
    #  package root. Specifically, if the source file is x/y/Z.lf relative
    #  to the package root, then the generated sources will be put in x/y/Z
    #  relative to srcGenBasePath.
    #      
    def getSrcGenPath(self):
        """ generated source for method getSrcGenPath """
        return self.srcGenPath

    # Path representation of srcGenRoot, the root directory for generated
    # sources. This is the root, meaning that if the source file is x/y/Z.lf
    # relative to the package root, then the generated sources will be put in x/y/Z
    # relative to this URI.
    #      
    def getSrcGenBasePath(self):
        """ generated source for method getSrcGenBasePath """
        return self.srcGenBasePath

    # The directory that denotes the root of the package to which the
    # generated sources belong. Even if the target language does not have a
    # notion of packages, this directory groups all files associated with a
    # single main reactor.
    #      
    def getSrcGenPkgPath(self):
        """ generated source for method getSrcGenPkgPath """
        return self.srcGenPkgPath

    #  Returns the root directory for generated sources.
    #      
    @classmethod
    def getSrcGenRoot(cls, fsa):
        """ generated source for method getSrcGenRoot """
        srcGenURI = fsa.getURI("")
        if srcGenURI.hasTrailingPathSeparator():
            srcGenURI = srcGenURI.trimSegments(1)
        return FileUtil.toPath(srcGenURI)

    # Given a path that denotes the full path to a source file (not including the
    # file itself), return the relative path from the root of the 'src'
    # directory, or, if there is no 'src' directory, the relative path
    # from the root of the package.
    # @param srcPath The path to the source.
    # @return the relative path from the root of the 'src'
    # directory, or, if there is no 'src' directory, the relative path
    # from the root of the package
    #      
    def getSubPkgPath(self, srcPath):
        """ generated source for method getSubPkgPath """
        relSrcPath = self.srcPkgPath.relativize(srcPath)
        if relSrcPath.startsWith(self.DEFAULT_SRC_DIR):
            segments = relSrcPath.getNameCount()
            if segments == 1:
                return ""
            else:
                relSrcPath = relSrcPath.subpath(1, segments)
        return relSrcPath

    # Clean any artifacts produced by the code generator and target compilers.
    #
    # The base implementation deletes the bin and src-gen directories. If the
    # target code generator creates additional files or directories, the
    # corresponding generator should override this method.
    #
    # @throws IOException If an I/O error occurs.
    #      
    def doClean(self):
        """ generated source for method doClean """
        FileUtil.deleteDirectory(self.binPath)
        FileUtil.deleteDirectory(self.srcGenBasePath)

    @classmethod
    def getPkgPath(cls, resource):
        """ generated source for method getPkgPath """
        if resource.getURI().isPlatform():
            #  We are in the RCA.
            srcFile = FileUtil.toPath(resource).toFile()
            for r in os.getcwd():
                p = os.path.join(r, srcFile)
                f = cls.srcFile.getAbsolutePath()
                if f.startsWith(p):
                    return p
        return cls.findPackageRoot(FileUtil.toPath(resource), "s->{}")

    @classmethod
    def findPackageRoot(cls, input, printWarning):
        """ generated source for method findPackageRoot """
        p = input
        while True:
            p = p.getParent()
            if p == None:
                printWarning.accept("File '" + input.getFileName() + "' is not located in an 'src' directory.")
                printWarning.accept("Adopting the current working directory as the package root.")
                return os.path.join(".", p)
            if p == "src":
                break
        return p.getParent()
