#!/usr/bin/env python
""" generated source for module LfSwitch """
# 
#  * Copyright (c) 2020, RTE (http://www.rte-france.com)
#  * This Source Code Form is subject to the terms of the Mozilla Public
#  * License, v. 2.0. If a copy of the MPL was not distributed with this
#  * file, You can obtain one at http://mozilla.org/MPL/2.0/.
#  
# package: com.powsybl.openloadflow.network.impl
import com.powsybl.commons.PowsyblException

import com.powsybl.iidm.network.LimitType

import com.powsybl.iidm.network.Switch

import com.powsybl.openloadflow.network

import com.powsybl.openloadflow.util.Evaluable

import com.powsybl.security.results.BranchResult
# import java.util.Collections
# import java.util.List
# import java.util.Objects

import 

# 
#  * @author Geoffroy Jamgotchian <geoffroy.jamgotchian at rte-france.com>
#  
class LfSwitch(AbstractLfBranch):
    """ generated source for class LfSwitch """
    aSwitch = None

    def __init__(self, network, bus1, bus2, aSwitch):
        """ generated source for method __init__ """
        super(LfSwitch, self).__init__(SimplePiModel())
        self.aSwitch = Objects.requireNonNull(aSwitch)

    def getId(self):
        """ generated source for method getId """
        return self.aSwitch.getId()

    def getBranchType(self):
        """ generated source for method getBranchType """
        return BranchType.SWITCH

    def hasPhaseControlCapability(self):
        """ generated source for method hasPhaseControlCapability """
        return False

    def setP1(self, p1):
        """ generated source for method setP1 """
        #  nothing to do

    def getP1(self):
        """ generated source for method getP1 """
        return NAN

    def setP2(self, p2):
        """ generated source for method setP2 """
        #  nothing to do

    def getP2(self):
        """ generated source for method getP2 """
        return NAN

    def setQ1(self, q1):
        """ generated source for method setQ1 """
        #  nothing to do

    def getQ1(self):
        """ generated source for method getQ1 """
        return NAN

    def setQ2(self, q2):
        """ generated source for method setQ2 """
        #  nothing to do

    def getQ2(self):
        """ generated source for method getQ2 """
        return NAN

    def setI1(self, i1):
        """ generated source for method setI1 """
        #  nothing to do

    def getI1(self):
        """ generated source for method getI1 """
        return NAN

    def setI2(self, i2):
        """ generated source for method setI2 """
        #  nothing to do

    def getI2(self):
        """ generated source for method getI2 """
        return NAN

    def createBranchResult(self, preContingencyBranchP1, preContingencyBranchOfContingencyP1, createExtension):
        """ generated source for method createBranchResult """
        raise PowsyblException("Unsupported type of branch for branch result: " + self.aSwitch.getId())

    def getLimits1(self, type):
        """ generated source for method getLimits1 """
        return Collections.emptyList()

    def getLimits2(self, type):
        """ generated source for method getLimits2 """
        return Collections.emptyList()

    def updateState(self, phaseShifterRegulationOn, isTransformerVoltageControlOn, dc):
        """ generated source for method updateState """
        #  nothing to do

    def updateFlows(self, p1, q1, p2, q2):
        """ generated source for method updateFlows """
        #  nothing to do
