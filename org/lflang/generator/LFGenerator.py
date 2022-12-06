#!/usr/bin/env python
""" generated source for module LFGenerator """
# package: org.lflang.generator
# import java.io.IOException
# import java.lang.reflect.Constructor
# import java.lang.reflect.InvocationTargetException
# import java.nio.file.Path
# import java.util.Objects
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.generator.AbstractGenerator
# import org.eclipse.xtext.generator.IFileSystemAccess2
# import org.eclipse.xtext.generator.IGeneratorContext
# import org.eclipse.xtext.util.RuntimeIOException

from org.lflang import ASTUtils

from org.lflang import ErrorReporter

from org.lflang import FileConfig

from org.lflang import Target

from org.lflang.generator.c.CGenerator import CGenerator

from org.lflang.generator.python.PythonGenerator import PythonGenerator

from org.lflang.scoping  import LFGlobalScopeProvider
# import com.google.inject.Inject

# 
#  * Generates code from your model files on save.
#  *
#  * See
#  * https://www.eclipse.org/Xtext/documentation/303_runtime_concepts.html#code-generation
#  
class AbstractGenerator:
    pass


class LFGenerator(AbstractGenerator):
    """ generated source for class LFGenerator """
    scopeProvider = None

    #  Indicator of whether generator errors occurred.
    generatorErrorsOccurred = False

    #      * Create a target-specific FileConfig object in Kotlin
    #      * <p>
    #      * Since the CppFileConfig and TSFileConfig class are implemented in Kotlin, the classes are
    #      * not visible from all contexts. If the RCA is run from within Eclipse via
    #      * "Run as Eclipse Application", the Kotlin classes are unfortunately not
    #      * available at runtime due to bugs in the Eclipse Kotlin plugin. (See
    #      * https://stackoverflow.com/questions/68095816/is-ist-possible-to-build-mixed-kotlin-and-java-applications-with-a-recent-eclips)
    #      * <p>
    #      * If the FileConfig class is found, this method returns an instance.
    #      * Otherwise, it returns an Instance of FileConfig.
    #      *
    #      * @return A FileConfig object in Kotlin if the class can be found.
    #      * @throws IOException If the file config could not be created properly
    #      
    def createFileConfig(self, target, resource, fsa, context):
        """ generated source for method createFileConfig """
        srcGenBasePath = FileConfig.getSrcGenRoot(fsa)
        #  Since our Eclipse Plugin uses code injection via guice, we need to
        #  play a few tricks here so that FileConfig does not appear as an
        #  import. Instead we look the class up at runtime and instantiate it if
        #  found.
        if target == CPP:
            pass
        elif target == Rust:
            pass
        elif target == TS:
            className = "org.lflang.generator." + target.packageName + "." + target.classNamePrefix + "FileConfig"
            try:
                return Class.forName(className).getDeclaredConstructor(Resource.__class__, Path.__class__, .__class__).newInstance(resource, srcGenBasePath, context.useHierarchicalBin())
            except InvocationTargetException as e:
                raise RuntimeException("Exception instantiating " + className, e.getTargetException())
            except ReflectiveOperationException as e:
                return FileConfig(resource, srcGenBasePath, context.useHierarchicalBin())
        else:
            return FileConfig(resource, srcGenBasePath, context.useHierarchicalBin())

    def createGenerator(self, target, fileConfig, errorReporter):
        """ generated source for method createGenerator """
        if target == C:
            return CGenerator(fileConfig, errorReporter, False)
        elif target == CCPP:
            return CGenerator(fileConfig, errorReporter, True)
        elif target == Python:
            return PythonGenerator(fileConfig, errorReporter)
        elif target == CPP:
            pass
        elif target == TS:
            pass
        elif target == Rust:
            return createKotlinBaseGenerator(target, fileConfig, errorReporter)
        raise RuntimeException("Unexpected target!")

    def createKotlinBaseGenerator(self, target, fileConfig, errorReporter):
        """ generated source for method createKotlinBaseGenerator """
        classPrefix = "org.lflang.generator." + target.packageName + "." + target.classNamePrefix
        try:
            generatorClass = Class.forName(classPrefix + "Generator")
            fileConfigClass = Class.forName(classPrefix + "FileConfig")
            ctor = generatorClass.getDeclaredConstructor(fileConfigClass, ErrorReporter.__class__, LFGlobalScopeProvider.__class__)
            return ctor.newInstance(fileConfig, errorReporter, self.scopeProvider)
        except InvocationTargetException as e:
            raise RuntimeException("Exception instantiating " + classPrefix + "FileConfig", e.getTargetException())
        except ReflectiveOperationException as e:
            self.generatorErrorsOccurred = True
            errorReporter.reportError("The code generator for the " + target + " target could not be found. " + "This is likely because you built Epoch using " + "Eclipse. The " + target + " code generator is written in Kotlin " + "and, unfortunately, the plugin that Eclipse uses " + "for compiling Kotlin code is broken. " + "Please consider building Epoch using Maven.\n" + "For step-by-step instructions, see: " + "https://github.com/icyphy/lingua-franca/wiki/Running-Lingua-Franca-IDE-%28Epoch%29-with-Kotlin-based-Code-Generators-Enabled-%28without-Eclipse-Environment%29")
            return None

    def doGenerate(self, resource, fsa, context):
        """ generated source for method doGenerate """
        lfContext = LFGeneratorContext.lfGeneratorContextOf(context, resource)
        if lfContext.getMode() == LFGeneratorContext.Mode.LSP_FAST:
            return
        target = Target.fromDecl(ASTUtils.targetDecl(resource))
        assert target != None
        fileConfig = None
        try:
            fileConfig = Objects.requireNonNull(self.createFileConfig(target, resource, fsa, lfContext))
        except IOError as e:
            raise RuntimeIOException("Error during FileConfig instantiation", e)
        errorReporter = lfContext.constructErrorReporter(fileConfig)
        generator = self.createGenerator(target, fileConfig, errorReporter)
        if generator != None:
            generator.doGenerate(resource, lfContext)
            self.generatorErrorsOccurred = generator.errorsOccurred()
        if isinstance(errorReporter, (LanguageServerErrorReporter)):
            (errorReporter).publishDiagnostics()

    def errorsOccurred(self):
        """ generated source for method errorsOccurred """
        return self.generatorErrorsOccurred
