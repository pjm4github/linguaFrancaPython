#!/usr/bin/env python
""" generated source for module LFIdeSetup """
# 
#  * generated by Xtext 2.23.0
#  
# package: org.lflang.ide
from lflang.ide.LFIdeModule import LFIdeModule

from org.lflang.LFStandaloneSetup import LFStandaloneSetup

# 
#  * Initialization support for running Xtext languages as language servers.
#  
class LFIdeSetup(LFStandaloneSetup):
    """ generated source for class LFIdeSetup """
    def __init__(self):
        """ generated source for method __init__ """
        super(LFIdeSetup, self).__init__(LFIdeModule())

    @classmethod
    def doSetup(cls):
        """ generated source for method doSetup """
        LFIdeSetup().createInjectorAndDoEMFRegistration()
