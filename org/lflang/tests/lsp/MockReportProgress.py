#!/usr/bin/env python
""" generated source for module MockReportProgress """
# package: org.lflang.tests.lsp
from org.lflang.generator import IntegratedBuilder

# 
#  * Collect progress reports and check that they have the expected properties.
#  *
#  * @author Peter Donovan <peterdonovan@berkeley.edu>
#  
class MockReportProgress(IntegratedBuilder, ReportProgress):
    """ generated source for class MockReportProgress """
    previousPercentProgress = int()
    failed = bool()

    def __init__(self):
        """ generated source for method __init__ """
        super(MockReportProgress, self).__init__()
        self.previousPercentProgress = 0
        self.failed = False

    def apply(self, message, percentage):
        """ generated source for method apply """
        print(message)
        if percentage == None:
            return
        if percentage < self.previousPercentProgress or percentage < 0 or percentage > 100:
            self.failed = True
        self.previousPercentProgress = percentage

    #      * Returns whether an invalid sequence of progress reports was received.
    #      * @return whether an invalid sequence of progress reports was received
    #      
    def failed(self):
        """ generated source for method failed """
        return self.failed
