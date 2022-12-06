#!/usr/bin/env python
""" generated source for module RustTest """
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
# package: org.lflang.tests.runtime
# import java.util.Properties

from org.lflang.Target

from org.lflang.tests.RuntimeTest

# 
#  *
#  
class RustTest(RuntimeTest):
    """ generated source for class RustTest """
    def __init__(self):
        """ generated source for method __init__ """
        super(RustTest, self).__init__(Target.Rust)

    def addExtraLfcArgs(self, args):
        """ generated source for method addExtraLfcArgs """
        #  Set this environment variable if you develop the crate locally,
        #  it's more convenient. You'll have to delete test/Rust/src-gen/*
        #  to make a change (and checkout the Cargo.toml back).
        path = System.getenv("LOCAL_RUST_REACTOR_RT")
        if path != None:
            args.setProperty("external-runtime-path", path)

    def supportsGenericTypes(self):
        """ generated source for method supportsGenericTypes """
        return True
