#!/usr/bin/env python
""" generated source for module LFGeneratorContext """
from abc import ABCMeta, abstractmethod
# package: org.lflang.generator
# import java.nio.file.Path
# import java.util.List
# import java.util.Map
# import java.util.Properties
# import org.eclipse.emf.ecore.resource.Resource
# import org.eclipse.xtext.generator.IGeneratorContext

from org.lflang.ErrorReporter

from org.lflang.FileConfig

from org.lflang.util.LFCommand

# 
#  * An {@code LFGeneratorContext} is the context of a Lingua Franca build process.
#  * It is the point of communication between a build process and the environment
#  * in which it is executed.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  

class Mode:
    """ generated source for enum Mode """
    STANDALONE = 'STANDALONE'
    EPOCH = 'EPOCH'
    LSP_FAST = 'LSP_FAST'
    LSP_MEDIUM = 'LSP_MEDIUM'
    LSP_SLOW = 'LSP_SLOW'
    UNDEFINED = 'UNDEFINED'


class LFGeneratorContext(IGeneratorContext):
    """ generated source for interface LFGeneratorContext """
    __metaclass__ = ABCMeta

    #      * Return the mode of operation, which indicates how the compiler has been invoked
    #      * (e.g., from within Epoch, from the command line, or via a Language Server).
    #      
    @abstractmethod
    def getMode(self):
        """ generated source for method getMode """

    #      * Return any arguments that will override target properties.
    #      
    @abstractmethod
    def getArgs(self):
        """ generated source for method getArgs """

    #      * Return whether the bin directory should be hierarchical.
    #      * @return whether the bin directory should be hierarchical
    #      
    @abstractmethod
    def useHierarchicalBin(self):
        """ generated source for method useHierarchicalBin """

    #      * Construct the appropriate error reporter for {@code fileConfig}.
    #      * @param fileConfig The {@code FileConfig} used by a build process.
    #      * @return the appropriate error reporter for {@code fileConfig}
    #      
    @abstractmethod
    def constructErrorReporter(self, fileConfig):
        """ generated source for method constructErrorReporter """

    #      * Mark the code generation process performed in this
    #      * context as finished with the result {@code result}.
    #      * @param result The result of the code generation
    #      *               process that was performed in this
    #      *               context.
    #      
    @abstractmethod
    def finish(self, result):
        """ generated source for method finish """

    #      * Return the result of the code generation process that was performed in
    #      * this context.
    #      * @return the result of the code generation process that was performed in
    #      * this context
    #      
    @abstractmethod
    def getResult(self):
        """ generated source for method getResult """

    #      * Report the progress of a build.
    #      * @param message A message for the LF programmer to read.
    #      * @param percentage The approximate percent completion of the build.
    #      
    @abstractmethod
    def reportProgress(self, message, percentage):
        """ generated source for method reportProgress """

    #      * Conclude this build and record the result if necessary.
    #      * @param status The status of the result.
    #      * @param execName The name of the executable produced by this code
    #      * generation process, or {@code null} if no executable was produced.
    #      * @param binPath The directory containing the executable (if applicable).
    #      * @param fileConfig The {@code FileConfig} instance used by the build.
    #      * @param codeMaps The generated files and their corresponding code maps.
    #      * @param interpreter The interpreter needed to run the executable, if
    #      *                    applicable.
    #      
    #        default void finish(
    #            GeneratorResult status,
    #            String execName,
    #            Path binPath,
    #            FileConfig fileConfig,
    #            Map codeMaps,
    #            String interpreter
    #        ) {
    #          final boolean isWindows = GeneratorUtils.isHostWindows();
    #          if (execName != null && binPath != null) {
    #               Path executable = binPath.resolve(execName + (isWindows && interpreter == null ? ".exe" : ""));
    #               String relativeExecutable = fileConfig.srcPkgPath.relativize(executable).__str__();
    #               LFCommand command = interpreter != null ?
    #                   LFCommand.get(interpreter, list(relativeExecutable), true, fileConfig.srcPkgPath) :
    #                   LFCommand.get(isWindows ? str(executable) : relativeExecutable, list(), true, fileConfig.srcPkgPath);
    #              finish(new GeneratorResult(status, executable, command, codeMaps));
    #          } else {
    #              finish(new GeneratorResult(status, null, null, codeMaps));
    #          }
    #      }
    #      /**
    # Conclude this build and record the result if necessary.
    # @param status The status of the result.
    # @param execName The name of the executable produced by this code
    # generation process, or {@code null} if no executable was produced.
    # @param fileConfig The directory containing the executable (if applicable)
    # @param codeMaps The generated files and their corresponding code maps.
    #       
    #      default void finish(
    #          GeneratorResult.Status status,
    #          String execName,
    #          FileConfig fileConfig,
    #          Map codeMaps
    #      ) {
    #          finish(status, execName, fileConfig.binPath, fileConfig, codeMaps, null);
    #      }
    #      /**
    # Conclude this build and record that it was unsuccessful.
    #       
    #      default void unsuccessfulFinish() {
    #          finish(
    #              getCancelIndicator() != null && getCancelIndicator().isCanceled() ?
    #              GeneratorResult.CANCELLED : GeneratorResult.FAILED
    #          );
    #      }
    #      /**
    # Return the {@code LFGeneratorContext} that best describes the given {@code context} when
    # building {@code Resource}.
    # @param context The context of a Lingua Franca build process.
    # @param resource The resource being built.
    # @return The {@code LFGeneratorContext} that best describes the given {@code context} when
    # building {@code Resource}.
    #       
    #      static LFGeneratorContext lfGeneratorContextOf(IGeneratorContext context, Resource resource) {
    #          if (context instanceof LFGeneratorContext) return (LFGeneratorContext) context;
    #          if (resource.getURI().isPlatform())
    #              return null;
    #  /*             new MainContext(
    #              Mode.EPOCH, context.getCancelIndicator(), (m, p) -> {}, new Properties(), false,
    #              EclipseErrorReporter::new
    #          ); 
    #          return new MainContext(Mode.LSP_FAST, context.getCancelIndicator());
    #      }
