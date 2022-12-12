#!/usr/bin/env python
""" generated source for module MixedRadixIntTest """
# package: org.lflang.tests.compiler
# import java.util.Arrays
# import java.util.List

import org.junit.jupiter.api.Assertions

import org.junit.jupiter.api.Test

from org.lflang.generator import MixedRadixInt

class MixedRadixIntTest:
    """ generated source for class MixedRadixIntTest """
    #  Constants used many times below.
    radixes = Arrays.asList(2, 3, 4, 5)
    digits = Arrays.asList(1, 2, 3, 4)

    def create(self):
        """ generated source for method create """
        num = MixedRadixInt(self.digits, self.radixes, None)
        Assertions.assertEquals("1%2, 2%3, 3%4, 4%5", str(num))
        Assertions.assertEquals(1 + 2 * 2 + 3 * 6 + 4 * 24, num.get())
        altDigits = list(1, 2, 1)
        altNum = MixedRadixInt(altDigits, self.radixes, None)
        Assertions.assertEquals(11, altNum.get())

    def createWithInfinity(self):
        """ generated source for method createWithInfinity """
        radixes = list(2, 3, 4, 10000)
        num = MixedRadixInt(self.digits, radixes, None)
        Assertions.assertEquals(1 + 2 * 2 + 3 * 6 + 4 * 24, num.get())

    def createWithError(self):
        """ generated source for method createWithError """
        radixes = list(2, 3)
        try:
            MixedRadixInt(self.digits, radixes, None)
        except IllegalArgumentException as ex:
            Assertions.assertTrue(ex.getMessage().startsWith("Invalid"))
            return
        Assertions.assertTrue(False, "Expected exception did not occur.")

    def createWithNullAndSet(self):
        """ generated source for method createWithNullAndSet """
        num = MixedRadixInt(None, self.radixes, None)
        Assertions.assertEquals(0, num.get())
        Assertions.assertEquals("0%2", str(num))
        num.set(1 + 2 * 2 + 3 * 6 + 4 * 24)
        Assertions.assertEquals(1 + 2 * 2 + 3 * 6 + 4 * 24, num.get())
        mag = num.magnitude()
        Assertions.assertEquals(1 + 2 * 2 + 3 * 6 + 4 * 24, mag)
        num.increment()
        #  wrap to zero.
        Assertions.assertEquals(0, num.get())
        Assertions.assertEquals(0, num.magnitude())
        num = MixedRadixInt(None, self.radixes, None)
        num.setMagnitude(mag)
        Assertions.assertEquals(mag, num.magnitude())

    def testPermutation(self):
        """ generated source for method testPermutation """
        radixes = Arrays.asList(2, 5)
        digits = Arrays.asList(1, 2)
        permutation = Arrays.asList(1, 0)
        num = MixedRadixInt(digits, radixes, permutation)
        Assertions.assertEquals(5, num.get())
        Assertions.assertEquals(2, num.get(1))
        Assertions.assertEquals(7, num.magnitude())
        num.increment()
        Assertions.assertEquals(7, num.get())
        Assertions.assertEquals(8, num.magnitude())
        num = MixedRadixInt(None, radixes, permutation)
        num.setMagnitude(8)
        Assertions.assertEquals(8, num.magnitude())
        Assertions.assertEquals(7, num.get())
        #  Test radix infinity digit (effectively).
        digits = Arrays.asList(1, 2, 1)
        radixes = Arrays.asList(2, 5, 1000000)
        num = MixedRadixInt(digits, radixes, None)
        Assertions.assertEquals(15, num.get())
        Assertions.assertEquals(7, num.get(1))
        Assertions.assertEquals(15, num.magnitude())
        permutation = Arrays.asList(1, 0, 2)
        num = MixedRadixInt(digits, radixes, permutation)
        num.increment()
        Assertions.assertEquals(17, num.get())
        Assertions.assertEquals(18, num.magnitude())
        num = MixedRadixInt(None, radixes, permutation)
        num.setMagnitude(18)
        Assertions.assertEquals(18, num.magnitude())
        Assertions.assertEquals(17, num.get())

    def testIncrement(self):
        """ generated source for method testIncrement """
        radixes = Arrays.asList(2, 3)
        digits = Arrays.asList(0, 2)
        num = MixedRadixInt(digits, radixes, None)
        num.increment()
        Assertions.assertEquals(5, num.get())
        num.increment()
        #  Wrap around to zero.
        Assertions.assertEquals(0, num.get())
