#!/usr/bin/env python
""" generated source for module RangeTests """
# package: org.lflang.tests.compiler
# import java.util.List
# import java.util.Set

class RangeTests:
    """ generated source for class RangeTests """
    reporter = DefaultErrorReporter()
    factory = LfFactory.eINSTANCE

    def createRange(self):
        """ generated source for method createRange """
        main = self.factory.createReactor()
        maini = ReactorInstance(main, self.reporter)
        a = self.factory.createReactor()
        a.setName("A")
        ai = ReactorInstance(a, maini, self.reporter)
        ai.setWidth(2)
        b = self.factory.createReactor()
        b.setName("B")
        bi = ReactorInstance(b, ai, self.reporter)
        bi.setWidth(2)
        p = self.factory.createPort()
        p.setName("P")
        pi = PortInstance(p, bi, self.reporter)
        pi.setWidth(2)
        Assertions.assertEquals(".A.B.P", pi.getFullName())
        range = RuntimeRange.Port(pi, 3, 4, None)
        Assertions.assertEquals(8, range.maxWidth)
        Assertions.assertEquals(".A.B.P(3,4)", range.__str__())
        #  The results expected below are derived from the class comment for RuntimeRange,
        #  which includes this example.
        instances = range.instances()
        Assertions.assertEquals(list(3, 4, 5, 6), instances)
        parents = range.parentInstances(1)
        Assertions.assertEquals(Set.of(1, 2, 3), parents)
        parents = range.parentInstances(2)
        Assertions.assertEquals(Set.of(0, 1), parents)
        #  Test startMR().getDigits.
        Assertions.assertEquals(list(1, 1, 0), range.startMR().getDigits())
        #  Create a SendRange sending from and to this range.
        sendRange = SendRange(pi, 3, 4, None, None)
        sendRange.destinations.append(range)
        #  Test getNumberOfDestinationReactors.
        Assertions.assertEquals(3, sendRange.getNumberOfDestinationReactors())
        #  Make first interleaved version.
        range = range.toggleInterleaved(bi)
        instances = range.instances()
        Assertions.assertEquals(list(3, 4, 6, 5), instances)
        #  Test startMR().getDigits.
        Assertions.assertEquals(list(1, 1, 0), range.startMR().getDigits())
        #  Make second interleaved version.
        range = range.toggleInterleaved(ai)
        instances = range.instances()
        Assertions.assertEquals(list(6, 1, 5, 3), instances)
        #  Test startMR().getDigits.
        Assertions.assertEquals(list(0, 1, 1), range.startMR().getDigits())
        #  Test instances of the parent.
        Assertions.assertEquals(Set.of(3, 0, 2, 1), range.parentInstances(1))
        #  Add this range to the sendRange destinations and verify
        #  that the number of destination reactors becomes 4.
        sendRange.addDestination(range)
        Assertions.assertEquals(4, sendRange.getNumberOfDestinationReactors())
        #  Make third interleaved version.
        range = range.toggleInterleaved(bi)
        instances = range.instances()
        Assertions.assertEquals(list(5, 2, 6, 3), instances)
        #  Test startMR().getDigits.
        Assertions.assertEquals(list(1, 0, 1), range.startMR().getDigits())
