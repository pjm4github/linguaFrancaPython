#!/usr/bin/env python
""" generated source for module CCoreFilesUtils """
# package: org.lflang.generator.c
# import java.nio.file.Path
# import java.util.ArrayList
# import java.util.List
# import java.util.stream.Collectors
# import java.util.stream.Stream

from org.lflang.TargetProperty import SchedulerOption

# 
#  * Generates the list of files to be included in the
#  * core library for each reactor given conditions listed
#  * as arguments of each function.
#  *
#  * @author{Hou Seng Wong <housengw@berkeley.edu>}
#  
class CCoreFilesUtils(object):
    """ generated source for class CCoreFilesUtils """
    @classmethod
    def getCoreFiles(cls, isFederated, threading, scheduler):
        """ generated source for method getCoreFiles """
        coreFiles = []
        coreFiles.extend(getBaseCoreFiles())
        coreFiles.extend(getPlatformFiles())
        if isFederated:
            coreFiles.extend(getFederatedFiles())
        coreFiles.extend(getThreadSupportFiles(threading, scheduler))
        return coreFiles

    @classmethod
    def getCTargetSrc(cls):
        """ generated source for method getCTargetSrc """
        return list("lib/schedule.c", "lib/util.c", "lib/tag.c", "lib/time.c")

    @classmethod
    def getArduinoTargetHeaders(cls):
        """ generated source for method getArduinoTargetHeaders """
        return list("Arduino.h")

    @classmethod
    def getCTargetHeader(cls):
        """ generated source for method getCTargetHeader """
        return list("include/ctarget/ctarget.h")

    @classmethod
    def getCTargetSetHeader(cls):
        """ generated source for method getCTargetSetHeader """
        return "include/ctarget/set.h"

    @classmethod
    def getCTargetSetUndefHeader(cls):
        """ generated source for method getCTargetSetUndefHeader """
        return "include/ctarget/set_undef.h"

    @classmethod
    def getBaseCoreFiles(cls):
        """ generated source for method getBaseCoreFiles """
        return list("reactor_common.c", "reactor.h", "tag.h", "tag.c", "trace.h", "trace.c", "port.h", "port.c", "utils/pqueue.c", "utils/pqueue.h", "utils/pqueue_support.h", "utils/vector.c", "utils/vector.h", "utils/semaphore.h", "utils/semaphore.c", "utils/util.h", "utils/util.c", "platform.h", "platform/Platform.cmake", "mixed_radix.c", "mixed_radix.h", "modal_models/modes.h", "modal_models/modes.c")

    @classmethod
    def getPlatformFiles(cls):
        """ generated source for method getPlatformFiles """
        return list("platform/lf_tag_64_32.h", "platform/lf_POSIX_threads_support.c", "platform/lf_C11_threads_support.c", "platform/lf_C11_threads_support.h", "platform/lf_POSIX_threads_support.h", "platform/lf_POSIX_threads_support.c", "platform/lf_unix_clock_support.c", "platform/lf_unix_syscall_support.c", "platform/lf_macos_support.c", "platform/lf_macos_support.h", "platform/lf_windows_support.c", "platform/lf_windows_support.h", "platform/lf_arduino_support.c", "platform/lf_arduino_support.h", "platform/lf_linux_support.c", "platform/lf_linux_support.h")

    @classmethod
    def getFederatedFiles(cls):
        """ generated source for method getFederatedFiles """
        return list("federated/net_util.c", "federated/net_util.h", "federated/net_common.h", "federated/federate.c", "federated/federate.h", "federated/clock-sync.h", "federated/clock-sync.c")

    @classmethod
    def getThreadSupportFiles(cls, threading, scheduler):
        """ generated source for method getThreadSupportFiles """
        return Stream.concat(Stream.of("threaded/scheduler.h", "threaded/scheduler_instance.h", "threaded/scheduler_sync_tag_advance.c", "threaded/reactor_threaded.c"), None).collect(Collectors.toList()) if threading else list("reactor.c")
