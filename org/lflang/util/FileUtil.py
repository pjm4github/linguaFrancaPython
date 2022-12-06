#!/usr/bin/env python
""" generated source for module FileUtil """
# package: org.lflang.util
from include.overloading import overloaded

class FileUtil(object):
    """ generated source for class FileUtil """
    # Return the name of the file excluding its file extension.
    # @param file A Path object
    # @return The name of the file excluding its file extension.
    #       
    @classmethod
    @overloaded
    def nameWithoutExtension(cls, file):
        """ generated source for method nameWithoutExtension """
        name = file.getFileName().__str__()
        idx = name.lastIndexOf('.')
        return name if idx < 0 else name.substring(0, idx)

    # Return the name of the file associated with the given resource,
    # excluding its file extension.
    # @param r Any {@code Resource}.
    # @return The name of the file associated with the given resource,
    # excluding its file extension.
    # @throws IOException If the resource has an invalid URI.
    #       
    @classmethod
    @nameWithoutExtension.register(object, Resource)
    def nameWithoutExtension_0(cls, r):
        """ generated source for method nameWithoutExtension_0 """
        return cls.nameWithoutExtension(toPath(r))

    # Return a java.nio.Path object corresponding to the given URI.
    # @throws IOException If the given URI is invalid.
    #       
    @classmethod
    @overloaded
    def toPath(cls, uri):
        """ generated source for method toPath """
        return Paths.get(toIPath(uri).toFile().getAbsolutePath())

    @classmethod
    @toPath.register(object, Resource)
    def toPath_0(cls, resource):
        """ generated source for method toPath_0 """
        return cls.toPath(resource.getURI())

    @classmethod
    def toIPath(cls, uri):
        """ generated source for method toIPath """
        if uri.isPlatform():
            path = org.eclipse.core.runtime.Path(uri.toPlatformString(True))
            if path.segmentCount() == 1:
                return ResourcesPlugin.getWorkspace().getRoot().getProject(path.lastSegment()).getLocation()
            else:
                return ResourcesPlugin.getWorkspace().getRoot().getFile(path).getLocation()
        elif uri.isFile():
            return org.eclipse.core.runtime.Path(uri.toFileString())
        else:
            raise IOError("Unrecognized file protocol in URI " + uri)

    @classmethod
    def toUnixString(cls, path):
        """ generated source for method toUnixString """
        return path.__str__().replace('\\', '/')

    @classmethod
    def locateFile(cls, path, resource):
        """ generated source for method locateFile """
        try:
            uri = java.net.URI(path)
            if uri.getScheme() != None:
                return uri
        except Exception as e:
            pass
        file = File(path)
        if file.exists():
            try:
                return file.toURI()
            except Exception as e:
                pass
        if resource != None:
            eURI = resource.getURI()
            if eURI != None:
                sourceURI = None
                try:
                    if eURI.isFile():
                        sourceURI = java.net.URI(eURI.__str__())
                        sourceURI = java.net.URI(sourceURI.getScheme(), None, sourceURI.getPath().substring(0, sourceURI.getPath().lastIndexOf("/")), None)
                    elif eURI.isPlatformResource():
                        iFile = ResourcesPlugin.getWorkspace().getRoot().findMember(eURI.toPlatformString(True))
                        sourceURI = iFile.getRawLocation().toFile().getParentFile().toURI() if iFile != None else None
                    if sourceURI != None:
                        return sourceURI.resolve(path.__str__())
                except Exception as e:
                    pass
        return None

    @classmethod
    @overloaded
    def copyDirectory(cls, src, dest, skipIfUnchanged):
        """ generated source for method copyDirectory """

    @classmethod
    @copyDirectory.register(object, Path, Path)
    def copyDirectory_0(cls, src, dest):
        """ generated source for method copyDirectory_0 """
        cls.copyDirectory(src, dest, False)

    @classmethod
    @overloaded
    def copyFile(cls, source, destination, skipIfUnchanged):
        """ generated source for method copyFile """
        stream = BufferedInputStream(FileInputStream(source.toFile()))

    @classmethod
    @copyFile.register(object, Path, Path)
    def copyFile_0(cls, source, destination):
        """ generated source for method copyFile_0 """
        cls.copyFile(source, destination, False)

    @classmethod
    def copyInputStream(cls, source, destination, skipIfUnchanged):
        """ generated source for method copyInputStream """
        Files.createDirectories(destination.getParent())
        if skipIfUnchanged and Files.isRegularFile(destination):
            if Arrays == (source, Files.readAllBytes(destination)):
                return
        Files.copy(source, destination, StandardCopyOption.REPLACE_EXISTING)

    @classmethod
    @overloaded
    def copyFileFromClassPath(cls, source, destination, skipIfUnchanged):
        """ generated source for method copyFileFromClassPath """
        sourceStream = FileConfig.__class__.getResourceAsStream(source)
        if sourceStream == None:
            raise IOError("A required target resource could not be found: " + source + "\n" + "Perhaps a git submodule is missing or not up to date.\n" + "See https://github.com/icyphy/lingua-franca/wiki/downloading-and-building#clone-the-lingua-franca-repository.\n" + "Also try to refresh and clean the project explorer if working from eclipse.")
        else:
            cls.copyInputStream(sourceStream, destination, skipIfUnchanged)

    @classmethod
    @copyFileFromClassPath.register(object, str, Path)
    def copyFileFromClassPath_0(cls, source, destination):
        """ generated source for method copyFileFromClassPath_0 """
        cls.copyFileFromClassPath(source, destination, False)

    @classmethod
    def copyDirectoryFromClassPath(cls, source, destination, skipIfUnchanged):
        """ generated source for method copyDirectoryFromClassPath """
        resource = FileConfig.__class__.getResource(source)
        if resource == None:
            raise IOError("A required target resource could not be found: " + source + "\n" + "Perhaps a git submodule is missing or not up to date.\n" + "See https://github.com/icyphy/lingua-franca/wiki/downloading-and-building#clone-the-lingua-franca-repository.\n" + "Also try to refresh and clean the project explorer if working from eclipse.")
        connection = resource.openConnection()
        if isinstance(connection, (JarURLConnection)):
            copyDirectoryFromJar(connection, destination, skipIfUnchanged)
        else:
            try:
                dir = Paths.get(FileLocator.toFileURL(resource).toURI())
                cls.copyDirectory(dir, destination, skipIfUnchanged)
            except URISyntaxException as e:
                raise IOError("Unexpected error while resolving " + source + " on the classpath")

    @classmethod
    def copyDirectoryFromJar(cls, connection, destination, skipIfUnchanged):
        """ generated source for method copyDirectoryFromJar """
        jar = connection.getJarFile()
        connectionEntryName = connection.getEntryName()
        e = jar.entries()
        while e.hasMoreElements():
            entry = e.nextElement()
            entryName = entry.__name__
            if entryName.startsWith(connectionEntryName):
                filename = entry.__name__.substring(1 + len(connectionEntryName))
                currentFile = destination.resolve(filename)
                if entry.isDirectory():
                    Files.createDirectories(currentFile)
                else:
                    is_ = jar.getInputStream(entry)
                    cls.copyInputStream(is_, currentFile, skipIfUnchanged)


    @classmethod
    def copyFilesFromClassPath(cls, srcDir, dstDir, files):
        """ generated source for method copyFilesFromClassPath """
        for file in files:
            cls.copyFileFromClassPath(srcDir + '/' + file, dstDir.resolve(file))

    @classmethod
    def deleteDirectory(cls, dir):
        """ generated source for method deleteDirectory """
        if Files.isDirectory(dir):
            print("Cleaning " + dir)
            pathsToDelete = Files.walk(dir).sorted(Comparator.reverseOrder()).collect(Collectors.toList())
            for path in pathsToDelete:
                Files.deleteIfExists(path)

    @classmethod
    @overloaded
    def getIResource(cls, r):
        """ generated source for method getIResource """
        return cls.getIResource(FileUtil.toPath(r).toFile().toURI())

    @classmethod
    @getIResource.register(object, Path)
    def getIResource_0(cls, path):
        """ generated source for method getIResource_0 """
        ret = cls.getIResource(path.toUri())
        if ret != None:
            return ret
        try:
            return ResourcesPlugin.getWorkspace().getRoot().findMember(org.eclipse.core.runtime.Path.fromOSString(path.subpath(1, path.getNameCount()).__str__()))
        except IllegalStateException as e:
            pass
        return None

    @classmethod
    @getIResource.register(object, java.net.URI)
    def getIResource_1(cls, uri):
        """ generated source for method getIResource_1 """
        try:
            workspaceRoot = ResourcesPlugin.getWorkspace().getRoot()
            files = workspaceRoot.findFilesForLocationURI(uri)
            if files != None and len(files) and files[0] != None:
                return files[0]
        except IllegalStateException as e:
            pass
        return None

    @classmethod
    @overloaded
    def writeToFile(cls, text, path, skipIfUnchanged):
        """ generated source for method writeToFile """
        Files.createDirectories(path.getParent())
        bytes = text.getBytes()
        if skipIfUnchanged and Files.isRegularFile(path):
            if Arrays == (bytes, Files.readAllBytes(path)):
                return
        Files.write(path, text.getBytes())

    @classmethod
    @writeToFile.register(object, str, Path)
    def writeToFile_0(cls, text, path):
        """ generated source for method writeToFile_0 """
        cls.writeToFile(text, path, False)

    @classmethod
    @writeToFile.register(object, CharSequence, Path)
    def writeToFile_1(cls, text, path):
        """ generated source for method writeToFile_1 """
        cls.writeToFile(text.__str__(), path, False)

    @classmethod
    def globFilesEndsWith(cls, currentDir, str):
        """ generated source for method globFilesEndsWith """
        matches = []
        files = currentDir.toFile().listFiles()
        if files != None:
            for file in files:
                if file.isDirectory():
                    matches.extend(cls.globFilesEndsWith(file.toPath(), str))
                else:
                    if file.__name__.endsWith(str):
                        matches.append(file.getAbsoluteFile().toPath())
        return matches
