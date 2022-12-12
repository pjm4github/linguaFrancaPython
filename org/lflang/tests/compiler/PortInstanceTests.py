#!/usr/bin/env python
""" generated source for module PortInstanceTests """
# package: org.lflang.tests.compiler
# import java.util.List
from include.overloading import overloaded

class PortInstanceTests:
    """ generated source for class PortInstanceTests """
    reporter = DefaultErrorReporter()
    factory = LfFactory.eINSTANCE

    def createRange(self):
        """ generated source for method createRange """
        main = self.factory.createReactor()
        maini = ReactorInstance(main, self.reporter)
        a = newReactor("A", maini)
        b = newReactor("B", maini)
        c = newReactor("C", maini)
        p = newOutputPort("p", a)
        q = newInputPort("q", b)
        r = newInputPort("r", c)
        Assertions.assertEquals(".A.p", p.getFullName())
        connect(p, q)
        connect(p, r)
        sr = p.eventualDestinations()
        #  Destinations should be empty because there are no reactions.
        Assertions.assertEquals("[]", str(sr))
        #  Clear caches to make a mutation.
        maini.clearCaches()
        newReaction(q)
        #  Re-retrieve destinations.
        sr = p.eventualDestinations()
        Assertions.assertEquals("[.A.p(0,1)->[.B.q(0,1)]]", str(sr))
        maini.clearCaches()
        newReaction(r)
        #  Re-retrieve destinations.
        sr = p.eventualDestinations()
        Assertions.assertEquals("[.A.p(0,1)->[.B.q(0,1), .C.r(0,1)]]", str(sr))
        #  Now test multiports.
        p.setWidth(3)
        r.setWidth(2)
        #  Have to redo the connections.
        clearConnections(maini)
        maini.clearCaches()
        connect(p, 0, 1, q, 0, 1)
        connect(p, 1, 2, r, 0, 2)
        #  Re-retrieve destinations.
        sr = p.eventualDestinations()
        Assertions.assertEquals("[.A.p(0,1)->[.B.q(0,1)], .A.p(1,2)->[.C.r(0,2)]]", str(sr))
        #  More complicated multiport connection.
        clearConnections(maini)
        maini.clearCaches()
        d = newReactor("D", maini)
        v = newOutputPort("v", d)
        v.setWidth(2)
        q.setWidth(3)
        connect(v, 0, 2, q, 0, 2)
        connect(p, 0, 1, q, 2, 1)
        connect(p, 1, 2, r, 0, 2)
        sr = p.eventualDestinations()
        Assertions.assertEquals("[.A.p(0,1)->[.B.q(2,1)], .A.p(1,2)->[.C.r(0,2)]]", str(sr))
        #  Additional multicast connection.
        maini.clearCaches()
        e = newReactor("E", maini)
        s = newPort("s", e)
        s.setWidth(3)
        newReaction(s)
        connect(p, s)
        sr = p.eventualDestinations()
        Assertions.assertEquals("[.A.p(0,1)->[.B.q(2,1), .E.s(0,1)], .A.p(1,2)->[.C.r(0,2), .E.s(1,2)]]", str(sr))
        #  Add hierarchical reactors that further split the ranges.
        maini.clearCaches()
        f = newReactor("F", e)
        t = newPort("t", f)
        newReaction(t)
        g = newReactor("G", e)
        u = newPort("u", g)
        u.setWidth(2)
        newReaction(u)
        connect(s, 0, 1, t, 0, 1)
        connect(s, 1, 2, u, 0, 2)
        sr = p.eventualDestinations()
        #  FIXME: Multicast destinations should be able to be reported in arbitrary order.
        Assertions.assertEquals("[.A.p(0,1)->[.E.F.t(0,1), .E.s(0,1), .B.q(2,1)], .A.p(1,2)->[.E.G.u(0,2), .E.s(1,2), .C.r(0,2)]]", str(sr))

    def multiportDestination(self):
        """ generated source for method multiportDestination """
        main = self.factory.createReactor()
        maini = ReactorInstance(main, self.reporter)
        a = newReactor("A", maini)
        b = newReactor("B", maini)
        b.setWidth(4)
        p = newOutputPort("p", a)
        q = newInputPort("q", b)
        connect(p, 0, 1, q, 0, 4)
        sr = p.eventualDestinations()
        #  Destination has no reactions, so empty list is right.
        Assertions.assertEquals("[]", str(sr))
        maini.clearCaches()
        newReaction(q)
        sr = p.eventualDestinations()
        Assertions.assertEquals("[.A.p(0,1)->[.B.q(0,4)]]", str(sr))

    #      * Clear connections. This recursively clears them for all contained reactors.
    #      
    def clearConnections(self, r):
        """ generated source for method clearConnections """
        for p in r.inputs:
            p.getDependentPorts().clear()
        for p in r.outputs:
            p.getDependentPorts().clear()
        for child in r.children:
            self.clearConnections(child)

    #      * Simple connection of two ports. This should be used only
    #      * for connections that would be allowed in the syntax (i.e., no
    #      * cross-hierarchy connections), but this is not checked. 
    #      * @param src The sending port.
    #      * @param dst The receiving port.
    #      
    @overloaded
    def connect(self, src, dst):
        """ generated source for method connect """
        srcRange = RuntimeRange.Port(src)
        dstRange = RuntimeRange.Port(dst)
        ReactorInstance.connectPortInstances(srcRange, dstRange, None)

    #      * Connection between multiports. This should be used only
    #      * for connections that would be allowed in the syntax (i.e., no
    #      * cross-hierarchy connections), but this is not checked. 
    #      * @param src The sending port.
    #      * @param dst The receiving port.
    #      
    @connect.register(object, PortInstance, int, int, PortInstance, int, int)
    def connect_0(self, src, srcStart, srcWidth, dst, dstStart, dstWidth):
        """ generated source for method connect_0 """
        srcRange = RuntimeRange.Port(src, srcStart, srcWidth, None)
        dstRange = RuntimeRange.Port(dst, dstStart, dstWidth, None)
        ReactorInstance.connectPortInstances(srcRange, dstRange, None)

    def newPort(self, name, container):
        """ generated source for method newPort """
        p = self.factory.createPort()
        p.setName(name)
        return PortInstance(p, container, self.reporter)

    def newInputPort(self, name, container):
        """ generated source for method newInputPort """
        pi = self.newPort(name, container)
        container.inputs.append(pi)
        return pi

    def newOutputPort(self, name, container):
        """ generated source for method newOutputPort """
        pi = self.newPort(name, container)
        container.outputs.append(pi)
        return pi

    #      * Return a new reaction triggered by the specified port.
    #      * @param trigger The triggering port.
    #      
    def newReaction(self, trigger):
        """ generated source for method newReaction """
        r = self.factory.createReaction()
        result = ReactionInstance(r, trigger.getParent(), False, trigger.getDependentReactions().size())
        trigger.getDependentReactions().append(result)
        trigger.getParent().reactions.append(result)
        return result

    def newReactor(self, name, container):
        """ generated source for method newReactor """
        r = self.factory.createReactor()
        r.setName(name)
        ri = ReactorInstance(r, container, self.reporter)
        container.children.append(ri)
        return ri
