#!/usr/bin/env python
""" generated source for module MainConflictChecker """
# package: org.lflang
import 
# import java.io.IOException
# import java.nio.file.FileVisitResult
# import java.nio.file.Files
# import java.nio.file.Path
# import java.nio.file.SimpleFileVisitor
# import java.nio.file.attribute.BasicFileAttributes
# import java.util.Iterator
# import java.util.LinkedList
# import java.util.List
# import org.eclipse.emf.common.util.URI
# import org.eclipse.emf.ecore.EObject
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.emf.ecore.resource.ResourceSet
# import org.eclipse.xtext.xbase.lib.IteratorExtensions

from org.lflang.lf

# import com.google.common.collect.Iterables

# 
#  * Class that (upon instantiation) determines whether there are any conflicting main reactors in the current package.
#  * Conflicts are reported in the instance's conflicts list.
#  * 
#  * @author Marten Lohstroh <marten@berkeley.edu>
#  *
#  
class MainConflictChecker(object):
    """ generated source for class MainConflictChecker """
    #      * List of conflict encountered while traversing the package.
    #      
    conflicts = LinkedList()

    #      * The current file configuration.
    #      
    fileConfig = None

    #      * Resource set used to obtain resources from.
    #      
    rs = LFStandaloneSetup().createInjectorAndDoEMFRegistration().getInstance(LFResourceProvider.__class__).getResourceSet()

    def __init__(self, fileConfig):
        """ generated source for method __init__ """
        self.fileConfig = fileConfig
        try:
            Files.walkFileTree(fileConfig.srcPkgPath, PackageVisitor())
        except IOError as e:
            System.err.println("Error while checking for name conflicts in package.")
            e.printStackTrace()

    class PackageVisitor(SimpleFileVisitor):
        """ generated source for class PackageVisitor """
        def visitFile(self, path, attr):
            """ generated source for method visitFile """
            path = path.normalize()
            if attr.isRegularFile() and path.__str__().endsWith(".lf"):
                r = self.rs.getResource(URI.createFileURI(path.toFile().getAbsolutePath()), True)
                if r.getErrors().isEmpty():
                    reactors = Iterables.filter(IteratorExtensions.toIterable(r.getAllContents()), Reactor.__class__).iterator()
            return CONTINUE
