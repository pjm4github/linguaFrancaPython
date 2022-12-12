#!/usr/bin/env python
""" generated source for module LFCommand """
# 
#  Copyright (c) 2019-2021 TU Dresden
#  Copyright (c) 2019-2021 UC Berkeley
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
#  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
#  THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#  THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
# package: org.lflang.util
# import java.io.ByteArrayOutputStream
# import java.io.File
# import java.io.IOException
# import java.io.InputStream
# import java.io.OutputStream
# import java.io.PrintStream
# import java.nio.file.Path
# import java.nio.file.Paths
# import java.util.ArrayDeque
# import java.util.ArrayList
# import java.util.Arrays
# import java.util.List
# import java.util.Map
# import java.util.concurrent.Executors
# import java.util.concurrent.ScheduledExecutorService
# import java.util.concurrent.TimeUnit
# import java.util.stream.Collectors
# import org.eclipse.xtext.util.CancelIndicator

# 
#  * An abstraction for an external command
#  * <p>
#  * This is a wrapper around ProcessBuilder which allows for a more convenient usage in our code base.
#  
class LFCommand:
    """ generated source for class LFCommand """
    #      * The period with which the cancel indicator is
    #      * checked and the output and error streams are
    #      * forwarded.
    #      
    PERIOD_MILLISECONDS = 200

    #      * The maximum amount of time to wait for the
    #      * forwarding of output and error streams to finish.
    #      
    READ_TIMEOUT_MILLISECONDS = 1000
    processBuilder = None
    didRun = False
    output = ByteArrayOutputStream()
    errors = ByteArrayOutputStream()
    quiet = bool()

    #      * Construct an LFCommand that executes the command carried by {@code pb}.
    #      
    def __init__(self, pb, quiet):
        """ generated source for method __init__ """
        self.processBuilder = pb
        self.quiet = quiet

    #      * Get the output collected during command execution
    #      
    def getOutput(self):
        """ generated source for method getOutput """
        return self.output

    #      * Get the error output collected during command execution
    #      
    def getErrors(self):
        """ generated source for method getErrors """
        return self.errors

    #  Get this command's program and arguments. 
    def command(self):
        """ generated source for method command """
        return self.processBuilder.command()

    #  Get this command's working directory. 
    def directory(self):
        """ generated source for method directory """
        return self.processBuilder.directory()

    #      * Get a String representation of the stored command
    #      
    def __str__(self):
        """ generated source for method toString """
        return "\n".join([ self.processBuilder.command()])

    # Collect as much output as possible from {@code in} without blocking, print it to
    # {@code print} if not quiet, and store it in {@code store}.
    #       
    def collectOutput(self, in_, store, print):
        """ generated source for method collectOutput """
        buffer = [None] * 64
        len = int()
        while True:
            try:
                #  This depends on in.available() being
                #   greater than zero if data is available
                #   (so that all data is collected)
                #   and upper-bounded by maximum number of
                #   bytes that can be read without blocking.
                #   Only the latter of these two conditions
                #   is guaranteed by the spec.
                len = in_.read(buffer, 0, min(in_.available()))
                if len > 0:
                    store.write(buffer, 0, len)
                    if not self.quiet:
                        print.write(buffer, 0, len)
            except IOError as e:
                e.printStackTrace()
                break
            if not ((len > 0)):
                break
        #  Do not necessarily continue
        #  to EOF (len == -1) because a blocking read
        #  operation is hard to interrupt.

    # Handle user cancellation if necessary, and handle any output from {@code process}
    # otherwise.
    # @param process a {@code Process}
    # @param cancelIndicator a flag indicating whether a
    #                        cancellation of {@code process}
    #                        is requested
    # directly to stderr and stdout).
    #       
    def poll(self, process, cancelIndicator):
        """ generated source for method poll """
        if cancelIndicator != None and cancelIndicator.isCanceled():
            process.descendants().forEach(ProcessHandle.destroyForcibly)
            process.destroyForcibly()
        else:
            self.collectOutput(process.getInputStream(), self.output, System.out)
            self.collectOutput(process.getErrorStream(), self.errors, System.err)

    # Execute the command.
    # <p>
    # Executing a process directly with `processBuilder.start()` could
    # lead to a deadlock as the subprocess blocks when output or error
    # buffers are full. This method ensures that output and error messages
    # are continuously read and forwards them to the system output and
    # error streams as well as to the output and error streams hold in
    # this class.
    # </p>
    # <p>
    # If the current operation is cancelled (as indicated
    # by <code>cancelIndicator</code>), the subprocess
    # is destroyed. Output and error streams until that
    # point are still collected.
    # </p>
    #       *
    # @param cancelIndicator The indicator of whether the underlying process
    # should be terminated.
    # @return the process' return code
    # @author {Christian Menard <christian.menard@tu-dresden.de}
    #       
    @overloaded
    def run(self, cancelIndicator):
        """ generated source for method run """
        assert not self.didRun
        self.didRun = True
        print("--- Current working directory: " + self.processBuilder.directory().__str__())
        print("--- Executing command: " + "\n".join([ self.processBuilder.command())])
        process = startProcess()
        if process == None:
            return -1
        poller = Executors.newSingleThreadScheduledExecutor()
        poller.scheduleAtFixedRate(self.poll(process, cancelIndicator), 0, self.PERIOD_MILLISECONDS, TimeUnit.MILLISECONDS)
        try:
            returnCode = process.waitFor()
            poller.shutdown()
            poller.awaitTermination(self.READ_TIMEOUT_MILLISECONDS, TimeUnit.MILLISECONDS)
            #  Finish collecting any remaining data
            self.poll(process, cancelIndicator)
            return returnCode
        except InterruptedException as e:
            e.printStackTrace()
            return -2

    # Execute the command. Do not allow user cancellation.
    # @return the process' return code
    #       
    @run.register(object)
    def run_0(self):
        """ generated source for method run_0 """
        return self.run(None)

    # Add the given variables and their values to the command's environment.
    #       *
    # @param variables A map of variable names and their values
    #       
    def setEnvironmentVariables(self, variables):
        """ generated source for method setEnvironmentVariables """
        self.processBuilder.environment().putAll(variables)

    # Add the given variable and its value to the command's environment.
    #       *
    # @param variableName name of the variable to add
    # @param value        the variable's value
    #       
    def setEnvironmentVariable(self, variableName, value):
        """ generated source for method setEnvironmentVariable """
        self.processBuilder.environment().put(variableName, value)

    # Replace the given variable and its value in the command's environment.
    #       *
    # @param variableName name of the variable to add
    # @param value        the variable's value
    #       
    def replaceEnvironmentVariable(self, variableName, value):
        """ generated source for method replaceEnvironmentVariable """
        self.processBuilder.environment().remove(variableName)
        self.processBuilder.environment().put(variableName, value)

    # Require this to be quiet, overriding the verbosity specified at construction time.
    #       
    def setQuiet(self):
        """ generated source for method setQuiet """
        self.quiet = True

    # Create a LFCommand instance from a given command and argument list in the current working directory.
    #       *
    # @see #get(String, List, boolean, Path)
    #       
    @classmethod
    @overloaded
    def get(cls, cmd, args):
        """ generated source for method get """
        return cls.get(cmd, args, False, Paths.get(""))

    # Create a LFCommand instance from a given command and argument list in the current working directory.
    #       *
    # @see #get(String, List, boolean, Path)
    #       
    @classmethod
    @get.register(object, str, List, bool)
    def get_0(cls, cmd, args, quiet):
        """ generated source for method get_0 """
        return cls.get(cmd, args, quiet, Paths.get(""))

    # Create a LFCommand instance from a given command, an argument list and a directory.
    # <p>
    # This will check first if the command can actually be found and executed. If the command is not found, null is
    # returned. In order to find the command, different methods are applied in the following order:
    # <p>
    # 1. Check if the given command `cmd` is an executable file within `dir`.
    # 2. If the above fails 'which <cmd>' (or 'where <cmd>' on Windows) is executed to see if the command is available
    # on the PATH.
    # 3. If both points above fail, a third attempt is started using bash to indirectly execute the command (see below
    # for an explanation).
    # <p>
    # A bit more context:
    # If the command cannot be found directly, then a second attempt is made using a Bash shell with the --login
    # option, which sources the user's ~/.bash_profile, ~/.bash_login, or ~/.bashrc (whichever is first found) before
    # running the command. This helps to ensure that the user's PATH variable is set according to their usual
    # environment, assuming that they use a bash shell.
    # <p>
    # More information: Unfortunately, at least on a Mac if you are running within Eclipse, the PATH variable is
    # extremely limited; supposedly, it is given by the default provided in /etc/paths, but at least on my machine, it
    # does not even include directories in that file for some reason. One way to add a directory like /usr/local/bin
    # to
    # the path once-and-for-all is this:
    # <p>
    # sudo launchctl config user path /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
    # <p>
    # But asking users to do that is not ideal. Hence, we try a more hack-y approach of just trying to execute using a
    # bash shell. Also note that while ProcessBuilder can be configured to use custom environment variables, these
    # variables do not affect the command that is to be executed but merely the environment in which the command
    # executes.
    #       *
    # @param cmd  The command
    # @param args A list of arguments to pass to the command
    # @param quiet If true, the commands stdout and stderr will be suppressed
    # @param dir  The directory in which the command should be executed
    # @return Returns an LFCommand if the given command could be found or null otherwise.
    #       
    @classmethod
    @get.register(object, str, List, bool, Path)
    def get_1(cls, cmd, args, quiet, dir):
        """ generated source for method get_1 """
        assert cmd != None and args != None and dir != None
        dir = dir.toAbsolutePath()
        #  a list containing the command as first element and then all arguments
        cmdList = []
        cmdList.append(cmd)
        cmdList.extend(args)
        builder = None
        #  First, see if the command is a local executable file
        cmdFile = dir.resolve(cmd).toFile()
        if cmdFile.exists() and cmdFile.canExecute():
            builder = ProcessBuilder(cmdList)
        elif findCommand(cmd) != None:
            builder = ProcessBuilder(cmdList)
        elif checkIfCommandIsExecutableWithBash(cmd, dir):
            builder = ProcessBuilder("bash", "--login", "-c", "\"{:s}\"".format("\n".join([ cmdList))])
        if builder != None:
            builder.directory(dir.toFile())
            return LFCommand(builder, quiet)
        return None

    # Search for matches to the given command by following the PATH environment variable.
    # @param command A command for which to search.
    # @return The file locations of matches to the given command.
    #       
    @classmethod
    def findCommand(cls, command):
        """ generated source for method findCommand """
        whichCmd = "where" if System.getProperty("os.name").startsWith("Windows") else "which"
        whichBuilder = ProcessBuilder(list(whichCmd, command))
        try:
            p = whichBuilder.start()
            if p.waitFor() != 0:
                return None
            return List()
            #                Arrays.stream(new String(p.getInputStream().readAllBytes()).split("\n"))
            #                    .map(String.strip).map(File.new).filter(File.canExecute).collect(Collectors.toList());
        except InterruptedException as e:
            # | IOException e) {
            e.printStackTrace()
            return None

    # Attempt to start the execution of this command.
    #       *
    # First collect a list of paths where the executable might be found,
    # then select an executable that successfully executes from the
    # list of paths. Return the {@code Process} instance that is the
    # result of a successful execution, or {@code null} if no successful
    # execution happened.
    # @return The {@code Process} that is started by this command, or {@code null} in case of failure.
    #       
    def startProcess(self):
        """ generated source for method startProcess """
        commands = ArrayDeque()
        matchesOnPath = self.findCommand(self.processBuilder.command().get(0))
        if matchesOnPath != None:
            matchesOnPath.stream().map(File.toString).forEach(commands.addLast)
        while True:
            try:
                return self.processBuilder.start()
            except IOError as e:
                if commands.isEmpty():
                    e.printStackTrace()
                    return None
            self.processBuilder.command().set(0, commands.removeFirst())

    @classmethod
    def checkIfCommandIsExecutableWithBash(cls, command, dir):
        """ generated source for method checkIfCommandIsExecutableWithBash """
        if cls.findCommand("bash") == None:
            return False
        bashBuilder = ProcessBuilder(list("bash", "--login", "-c", "\"which {:s}\"".format(command)))
        bashBuilder.directory(dir.toFile())
        try:
            bashReturn = bashBuilder.start().waitFor()
            return bashReturn == 0
        except InterruptedException as e:
            e.printStackTrace()
            return False
