# Copyright (c) 2026 o6 Automation GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Generated OPC UA powertrain namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.fx_ac as fx_ac
import o6.ns.fx_data as fx_data
import o6.ns.ia as ia
import o6.ns.irdi_v1_0_0 as irdi_v1_0_0
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import reftypes as powertrain_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object

ns0.objtypes.FolderType(nodeId="ns=powertrain;i=5004", browseName="ns=di;DeviceTypeImage")
o6.reference(o6.ns["ns=powertrain;i=5004"], "i=47", "ns=di;i=15056")
ns0.objtypes.FolderType(nodeId="ns=powertrain;i=5005", browseName="ns=di;Documentation")
o6.reference(o6.ns["ns=powertrain;i=5005"], "i=47", "ns=di;i=15058")
ns0.objtypes.FolderType(nodeId="ns=powertrain;i=5006", browseName="ns=di;ImageSet")
o6.reference(o6.ns["ns=powertrain;i=5006"], "i=47", "ns=di;i=15062")
ns0.objtypes.FolderType(nodeId="ns=powertrain;i=5007", browseName="ns=di;ProtocolSupport")
o6.reference(o6.ns["ns=powertrain;i=5007"], "i=47", "ns=di;i=15060")
ns0.objtypes.FolderType(nodeId="ns=powertrain;i=5039", browseName="ns=di;DocumentationFiles")
o6.reference(o6.ns["ns=powertrain;i=5039"], "i=47", "ns=di;i=28")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6145", browseName="ns=powertrain;ControlVoltageAC50HzRangeRated", dataType=ns0.datatypes.Range)
o6.reference(o6.ns["ns=powertrain;i=6145"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE602")
ns0.vartypes.PropertyType(
    nodeId="ns=powertrain;i=6393", browseName="ns=powertrain;OverloadCurrentSettingRange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
)
o6.reference(o6.ns["ns=powertrain;i=6393"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE741")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6397", browseName="ns=powertrain;OperationalCurrentAC3At400VRated", dataType=o6.Float, value=0.0)
o6.reference(o6.ns["ns=powertrain;i=6397"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE434")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6590", browseName="ns=powertrain;OperationalCurrentAC3At400VRated", dataType=o6.Float)
o6.reference(o6.ns["ns=powertrain;i=6590"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE434")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6596", browseName="ns=powertrain;NumberofMainContactsNO", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6596"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE404")
ns0.vartypes.PropertyType(
    nodeId="ns=powertrain;i=6597", browseName="ns=powertrain;ControlVoltageAC50HzRangeRated", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
)
o6.reference(o6.ns["ns=powertrain;i=6597"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE602")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6598", browseName="ns=powertrain;NumberofAuxiliaryContactsNO", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6598"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE511")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6599", browseName="ns=powertrain;NumberofAuxiliaryContactsNC", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6599"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE508")
ns0.vartypes.PropertyType(
    nodeId="ns=powertrain;i=6738", browseName="ns=powertrain;OverloadCurrentSettingRange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
)
o6.reference(o6.ns["ns=powertrain;i=6738"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE741")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6742", browseName="ns=powertrain;VoltageRated", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6742"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE457")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6743", browseName="ns=powertrain;NumberofAuxiliaryContactsNC", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6743"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE508")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6744", browseName="ns=powertrain;PhaseLossSensitiveSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6744"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE749")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6745", browseName="ns=powertrain;JamDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6745"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE222")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6746", browseName="ns=powertrain;StallDetectionSuported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6746"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE221")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6747", browseName="ns=powertrain;GroundEarthFaultDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6747"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE220")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6748", browseName="ns=powertrain;IntegratedByPassSupported", dataType=o6.Boolean)
o6.reference(o6.ns["ns=powertrain;i=6748"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE212")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6749", browseName="ns=powertrain;OperationalCurrent40CRated", dataType=o6.Float)
o6.reference(o6.ns["ns=powertrain;i=6749"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE430")
ns0.vartypes.PropertyType(
    nodeId="ns=powertrain;i=6750", browseName="ns=powertrain;OperationalVoltageRangeRated", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
)
o6.reference(o6.ns["ns=powertrain;i=6750"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE455")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6751", browseName="ns=powertrain;MotorOverloadProtectionIntegrated", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6751"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE211")
o6.reference(o6.ns["ns=powertrain;i=6751"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE430")
ns0.vartypes.PropertyType(
    nodeId="ns=powertrain;i=6752", browseName="ns=powertrain;OverloadCurrentSettingRange", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
)
o6.reference(o6.ns["ns=powertrain;i=6752"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE741")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6756", browseName="ns=powertrain;PhaseLossSensitiveSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6756"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE749")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6757", browseName="ns=powertrain;JamDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6757"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE222")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6758", browseName="ns=powertrain;StallDetectionSuported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6758"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE221")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6759", browseName="ns=powertrain;GroundEarthFaultDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6759"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE220")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6760", browseName="ns=powertrain;LoadSheddingSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6760"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE205")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6761", browseName="ns=powertrain;OverUnderCurrentDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6761"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE223")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6762", browseName="ns=powertrain;OverUnderVoltageDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6762"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE224")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6763", browseName="ns=powertrain;CurrentImbalanceDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6763"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE225")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6764", browseName="ns=powertrain;PhaseReversalDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6764"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE227")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6765", browseName="ns=powertrain;CosPhiVariationDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6765"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE302")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6766", browseName="ns=powertrain;VoltageMonitoringSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6766"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE301")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6767", browseName="ns=powertrain;UnderPowerDetectionSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6767"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE303")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6768", browseName="ns=powertrain;NumberOfPtcThermistorInputs", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6768"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE334")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6769", browseName="ns=powertrain;NumberOfAnalogInputs", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6769"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE331")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6770", browseName="ns=powertrain;NumberOfDigitalOutputs", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6770"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE333")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6771", browseName="ns=powertrain;NumberOfDigitalInputs", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=6771"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE332")
ns0.vartypes.PropertyType(
    nodeId="ns=powertrain;i=6772", browseName="ns=powertrain;ControlVoltageAC50HzRangeRated", dataType=ns0.datatypes.Range, value=ns0.datatypes.Range(low=0.0, high=0.0)
)
o6.reference(o6.ns["ns=powertrain;i=6772"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE602")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6773", browseName="ns=powertrain;HMIPortSupported", dataType=o6.Boolean, value=False)
o6.reference(o6.ns["ns=powertrain;i=6773"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE362")


o6.call(nodeId="ns=powertrain;i=7000", browseName="ns=fx_ac;VerifyAsset")
o6.reference(o6.ns["ns=powertrain;i=7000"], "i=46", "ns=fx_ac;i=1422")
o6.reference(o6.ns["ns=powertrain;i=7000"], "i=46", "ns=fx_ac;i=1423")


@o6.objecttype(
    nodeId="ns=powertrain;i=15898",
    browseName="ns=powertrain;IPtTagNameplateType",
    displayName="IPtTagNameplateType",
    description="Is a subtype of IMachineTagNameplateType defined in OPC 40001-1",
)
class IPtTagNameplateType(machinery.objtypes.IMachineTagNameplateType):
    comment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15905", browseName="ns=powertrain;Comment", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    contactInformation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15906", browseName="ns=powertrain;ContactInformation", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    function: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=15907", browseName="ns=powertrain;Function", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16337",
    browseName="ns=powertrain;PtAssetAttributesType",
    displayName="PtAssetAttributesType",
    description="Provides attributes to the respective asset in a modular manner",
    isAbstract=True,
)
class PtAssetAttributesType(ns0.objtypes.BaseObjectType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6020",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("powertrain:PtAssetAttribute_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=powertrain;i=1004", browseName="ns=powertrain;PtCapacitanceAttributesType", displayName="PtCapacitanceAttributesType")
class PtCapacitanceAttributesType(PtAssetAttributesType):
    capacitance: ns0.vartypes.AnalogUnitType
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6025",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtCapacitanceAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=powertrain;i=1006", browseName="ns=powertrain;PtReactorAttributesType", displayName="PtReactorAttributesType")
class PtReactorAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6432",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtReactorAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    inductance: ns0.vartypes.AnalogUnitType


@o6.objecttype(nodeId="ns=powertrain;i=1008", browseName="ns=powertrain;PtBleedAttributesType", displayName="PtBleedAttributesType")
class PtBleedAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6023",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtBleedAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleResistanceValueRangle: ns0.vartypes.AnalogUnitType | None
    powerRated: ns0.vartypes.AnalogUnitType


@o6.objecttype(nodeId="ns=powertrain;i=1010", browseName="ns=powertrain;PtPrechargeAttributesType", displayName="PtPrechargeAttributesType")
class PtPrechargeAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6420",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtPrechargeAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    preChargeCycleTimeLimit: ns0.vartypes.AnalogUnitType | None
    preChargeMaximumCapacitance: ns0.vartypes.AnalogUnitType | None
    preChargeTime: ns0.vartypes.AnalogUnitType | None
    preChargeTimeout: ns0.vartypes.AnalogUnitType | None
    preChargeType: ns0.vartypes.MultiStateValueDiscreteType
    prechargeThreshold: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=powertrain;i=1014", browseName="ns=powertrain;PtElectronicOverloadRelayAttributesType", displayName="PtElectronicOverloadRelayAttributesType")
class PtElectronicOverloadRelayAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6029",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtElectronicOverloadRelayAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    groundEarthFaultDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6747"])
    jamDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6745"])
    numberofAuxiliaryContactsNC: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6743"])
    overloadCurrentSettingRange: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6738"])
    phaseLossSensitiveSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6744"])
    stallDetectionSuported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6746"])
    tripClass: ns0.vartypes.MultiStateValueDiscreteType
    voltageRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6742"])


@o6.objecttype(nodeId="ns=powertrain;i=1019", browseName="ns=powertrain;PtSoftStarterAttributesType", displayName="PtSoftStarterAttributesType")
class PtSoftStarterAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6440",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtSoftStarterAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    integratedByPassSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6748"])
    motorOverloadProtectionIntegrated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6751"])
    operationalCurrent40CRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6749"])
    operationalVoltageRangeRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6750"])


@o6.objecttype(nodeId="ns=powertrain;i=1023", browseName="ns=powertrain;PtMotorManagementDeviceAttributesType", displayName="PtMotorManagementDeviceAttributesType")
class PtMotorManagementDeviceAttributesType(PtAssetAttributesType):
    controlVoltageAC50HzRangeRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6772"])
    cosPhiVariationDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6765"])
    currentImbalanceDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6763"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6045",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorManagementAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    groundEarthFaultDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6759"])
    hMIPortSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6773"])
    jamDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6757"])
    loadSheddingSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6760"])
    numberOfAnalogInputs: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6769"])
    numberOfDigitalInputs: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6771"])
    numberOfDigitalOutputs: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6770"])
    numberOfPtcThermistorInputs: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6768"])
    overUnderCurrentDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6761"])
    overUnderVoltageDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6762"])
    overloadCurrentSettingRange: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6752"])
    phaseLossSensitiveSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6756"])
    phaseReversalDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6764"])
    stallDetectionSuported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6758"])
    tripClass: ns0.vartypes.MultiStateValueDiscreteType
    underPowerDetectionSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6767"])
    voltageMonitoringSupported: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6766"])


@o6.objecttype(
    nodeId="ns=powertrain;i=16383",
    browseName="ns=powertrain;PtMotorAttributesType",
    displayName="PtMotorAttributesType",
    description="Provides operation mode rated attributes of a amotor",
)
class PtMotorAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6021",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    motorType: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(nodeId="ns=powertrain;i=1009", browseName="ns=powertrain;PtMotorRotaryAttributesType", displayName="PtMotorRotaryAttributesType")
class PtMotorRotaryAttributesType(PtMotorAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6022",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorRotaryAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    motorBackEMF: ns0.vartypes.AnalogUnitType | None
    motorInertia: ns0.vartypes.AnalogUnitType | None
    motorPolePairs: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6525", browseName="ns=powertrain;MotorPolePairs", dataType=o6.UInt16)
    )


@o6.objecttype(nodeId="ns=powertrain;i=1012", browseName="ns=powertrain;PtMotorLinearAttributesType", displayName="PtMotorLinearAttributesType")
class PtMotorLinearAttributesType(PtMotorAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6464",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorLinearAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    forcerWeight: ns0.vartypes.AnalogUnitType | None
    motorBackEMF: ns0.vartypes.AnalogUnitType | None
    motorPolePairPitch: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16399",
    browseName="ns=powertrain;PtMotorRatedAttributesType",
    displayName="PtMotorRatedAttributesType",
    description="Provides operation mode rated attributes of a amotor",
)
class PtMotorRatedAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6047",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorRatedAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    isCooled: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6328", browseName="ns=powertrain;IsCooled", dataType=o6.Boolean))
    motorCurrentContinuousStall: ns0.vartypes.AnalogUnitType | None
    motorEfficiencyClass: ns0.vartypes.MultiStateValueDiscreteType | None
    motorPowerFactor: ns0.vartypes.AnalogUnitType | None
    motorPowerRated: ns0.vartypes.AnalogUnitType | None
    motorWindingType: ns0.vartypes.MultiStateValueDiscreteType
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType
    ptMotorDutyAttributes: PtMotorDutyAttributesType | None


@o6.objecttype(nodeId="ns=powertrain;i=1015", browseName="ns=powertrain;PtMotorRotaryRatedAttributesType", displayName="PtMotorRotaryRatedAttributesType")
class PtMotorRotaryRatedAttributesType(PtMotorRatedAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6435",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorRotaryRatedAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    motorSpeedMax: ns0.vartypes.AnalogUnitType
    motorSpeedRated: ns0.vartypes.AnalogUnitType | None
    motorTorqueConstant: ns0.vartypes.AnalogUnitType | None
    motorTorqueContinuousStall: ns0.vartypes.AnalogUnitType | None
    motorTorqueMax: ns0.vartypes.AnalogUnitType
    motorTorqueRated: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=powertrain;i=1018", browseName="ns=powertrain;PtMotorLinearRatedAttributesType", displayName="PtMotorLinearRatedAttributesType")
class PtMotorLinearRatedAttributesType(PtMotorRatedAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6436",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorLinearRatedAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    motorForceConstant: ns0.vartypes.AnalogUnitType | None
    motorForceContinuousStall: ns0.vartypes.AnalogUnitType | None
    motorForceMax: ns0.vartypes.AnalogUnitType | None
    motorForceRated: ns0.vartypes.AnalogUnitType | None
    motorSpeedMax: ns0.vartypes.AnalogUnitType
    motorSpeedRated: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16499",
    browseName="ns=powertrain;PtMotorDutyAttributesType",
    displayName="PtMotorDutyAttributesType",
    description="Provides attributes for the encoder interface protocol",
)
class PtMotorDutyAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6044",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorDutyAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    dutyType: ns0.vartypes.MultiStateValueDiscreteType
    loadProfile: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16502", browseName="ns=powertrain;LoadProfile", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="ns=powertrain;i=16503", browseName="ns=powertrain;PtGearAttributesType", displayName="PtGearAttributesType", description="power train gear type")
class PtGearAttributesType(PtAssetAttributesType):
    axialForceMax: ns0.vartypes.AnalogUnitType | None
    backlash: ns0.vartypes.AnalogUnitType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6033",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtGearAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    gearInertia: ns0.vartypes.AnalogUnitType | None
    gearType: ns0.vartypes.MultiStateValueDiscreteType | None
    langleEfficiencyRangle: ns0.vartypes.AnalogUnitType | None
    langleGearRatioRangle: ns0.vartypes.AnalogUnitType | None
    lubricantInterval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16552", browseName="ns=powertrain;LubricantInterval", dataType=o6.Float)
    )
    lubricantType: ns0.vartypes.MultiStateValueDiscreteType | None
    speedRated: ns0.vartypes.AnalogUnitType | None
    torqueRated: ns0.vartypes.AnalogUnitType | None
    torsionalRigidity: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16553", browseName="ns=powertrain;PtEncoderAttributesType", displayName="PtEncoderAttributesType", description="Provides attributes for the encoder"
)
class PtEncoderAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6030",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtEncoderAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    encoderTechnology: ns0.vartypes.MultiStateValueDiscreteType | None
    encoderType: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(nodeId="ns=powertrain;i=1021", browseName="ns=powertrain;PtEncoderRotaryAttributesType", displayName="PtEncoderRotaryAttributesType")
class PtEncoderRotaryAttributesType(PtEncoderAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6466",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtEncoderRotaryAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    encoderFlangeSize: ns0.vartypes.AnalogUnitType | None
    encoderFlangeType: ns0.vartypes.MultiStateValueDiscreteType | None
    encoderRotarySpeedMax: ns0.vartypes.AnalogUnitType | None
    encoderShaftSize: ns0.vartypes.AnalogUnitType | None
    encoderShaftType: ns0.vartypes.MultiStateValueDiscreteType | None
    feedbackResolverExcitationFrequency: ns0.vartypes.AnalogUnitType | None
    feedbackResolverExcitationVoltage: ns0.vartypes.AnalogUnitType | None
    feedbackResolverPolePairNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6704", browseName="ns=powertrain;FeedbackResolverPolePairNumber", dataType=o6.UInt32)
    )
    feedbackResolverRatio: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6709", browseName="ns=powertrain;FeedbackResolverRatio", dataType=o6.Float)
    )
    resolutionMultiturnAbsolute: ns0.vartypes.AnalogUnitType | None
    resolutionRotaryIncremental: ns0.vartypes.AnalogUnitType | None
    resolutionSingleturnAbsolute: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=powertrain;i=1024", browseName="ns=powertrain;PtEncoderLinearAttributesType", displayName="PtEncoderLinearAttributesType")
class PtEncoderLinearAttributesType(PtEncoderAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6465",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtEncoderLinearAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    encoderMounting: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6733", browseName="ns=powertrain;EncoderMounting", dataType=o6.Float)
    )
    encoderReadingDistance: ns0.vartypes.AnalogUnitType | None
    encoderSpeedLinearMax: ns0.vartypes.AnalogUnitType | None
    rangeLinear: ns0.vartypes.AnalogUnitType | None
    resolutionLinearAbsolute: ns0.vartypes.AnalogUnitType | None
    resolutionLinearIncremental: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6728", browseName="ns=powertrain;ResolutionLinearIncremental", dataType=o6.UInt32)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16605",
    browseName="ns=powertrain;PtEncoderInterfaceProtocolAttributesType",
    displayName="PtEncoderInterfaceProtocolAttributesType",
    description="Provides attributes for the encoder interface protocol",
)
class PtEncoderInterfaceProtocolAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6032",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtEncoderInterfaceProtocolAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    encoderProtocol: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=1003",
    browseName="ns=powertrain;PtEncoderInterfaceAttributesType",
    displayName="PtEncoderInterfaceAttributesType",
    description="The PtEncoderInterfaceAttributesType provides the most common attributes of the encoder interface",
)
class PtEncoderInterfaceAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6031",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtEncoderInterfaceAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    encoderSignal: ns0.vartypes.MultiStateValueDiscreteType | None
    langlePtEncoderInterfaceProtocolAttributesRangle: PtEncoderInterfaceProtocolAttributesType | None = o6.reference(
        PtEncoderInterfaceProtocolAttributesType(
            nodeId="ns=powertrain;i=5069", browseName="ns=powertrain;<PtEncoderInterfaceProtocolAttributes>", modellingRule="OptionalPlaceholder"
        ),
        "ns=powertrain;i=4004",
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16708",
    browseName="ns=powertrain;PtTemperatureSensorAttributesType",
    displayName="PtTemperatureSensorAttributesType",
    description="Provides attributes for a temperature sensor",
)
class PtTemperatureSensorAttributesType(PtAssetAttributesType):
    accuracy: ns0.vartypes.AnalogUnitType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6460",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtTemperatureSensorAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    temperatureMax: ns0.vartypes.AnalogUnitType
    temperatureMin: ns0.vartypes.AnalogUnitType
    temperatureSensorTechnology: ns0.vartypes.MultiStateValueDiscreteType
    temperatureSensorType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16710", browseName="ns=powertrain;TemperatureSensorType", dataType=o6.String)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16747",
    browseName="ns=powertrain;PtVibrationSensorAttributesType",
    displayName="PtVibrationSensorAttributesType",
    description="Provides attributes for a vibration sensor",
)
class PtVibrationSensorAttributesType(PtAssetAttributesType):
    accuracy: ns0.vartypes.AnalogUnitType | None
    analogInputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    analogOutputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6463",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtVibrationSensorAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    digitalInputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    digitalOutputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    frequencyRange: ns0.vartypes.BaseDataVariableType
    linearity: ns0.vartypes.AnalogUnitType | None
    measuringRange: ns0.vartypes.BaseDataVariableType
    operatingVoltage: ns0.vartypes.AnalogUnitType | None
    outputFunction: ns0.vartypes.MultiStateValueDiscreteType | None
    resolution: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16798", browseName="ns=powertrain;PtDcBusAttributesType", displayName="PtDcBusAttributesType", description="Provides attributes for the DCBus"
)
class PtDcBusAttributesType(PtAssetAttributesType):
    dcBusVoltageRange: ns0.vartypes.BaseDataVariableType
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6028",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtDcBusAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleDcBusVoltageRatedRangle: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16806",
    browseName="ns=powertrain;PtInputConverterAttributesType",
    displayName="PtInputConverterAttributesType",
    description="Provides attributes for the input converter of a drive",
)
class PtInputConverterAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6034",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtInputConverterAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    efficiencyClass: ns0.vartypes.MultiStateValueDiscreteType | None
    inputConverterType: ns0.vartypes.MultiStateValueDiscreteType
    langlePwmSwitchingFrequencyRangle: ns0.vartypes.AnalogUnitType | None
    powerFactorCorrection: ns0.vartypes.AnalogUnitType | None
    regenerativeFeedbackSupported: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6222", browseName="ns=powertrain;RegenerativeFeedbackSupported", dataType=o6.Boolean)
    )
    regenerativePowerRated: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16818",
    browseName="ns=powertrain;PtOutputConverterAttributesType",
    displayName="PtOutputConverterAttributesType",
    description="Provides attributes for the output converter of a drive",
)
class PtOutputConverterAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6049",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtOutputConverterAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    efficiencyClass: ns0.vartypes.MultiStateValueDiscreteType | None
    langlePwmSwitchingFrequencyRangle: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=powertrain;i=16827",
    browseName="ns=powertrain;PtInputFilterAttributesType",
    displayName="PtInputFilterAttributesType",
    description="Provides attributes for line filter functionality",
)
class PtInputFilterAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6043",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtInputFilterAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    lineFilterEmcCategory: ns0.vartypes.MultiStateValueDiscreteType | None
    lineFilterEmcClass: ns0.vartypes.MultiStateValueDiscreteType | None
    lineFilterEmcGroup: ns0.vartypes.MultiStateValueDiscreteType | None
    lineFilterPowerLoss: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16838",
    browseName="ns=powertrain;PtOutputFilterAttributesType",
    displayName="PtOutputFilterAttributesType",
    description="Provides attributes for load-side filter functionality",
)
class PtOutputFilterAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6419",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtOutputFilterAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    outputFilterPowerLoss: ns0.vartypes.AnalogUnitType | None
    outputFilterType: ns0.vartypes.MultiStateValueDiscreteType


ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16850", browseName="ns=powertrain;NumberofMainContactsNO", dataType=o6.UInt16)
o6.reference(o6.ns["ns=powertrain;i=16850"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE404")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16852", browseName="ns=powertrain;NumberofAuxiliaryContactsNO", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=16852"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE511")
ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16853", browseName="ns=powertrain;NumberofAuxiliaryContactsNC", dataType=o6.UInt16, value=0)
o6.reference(o6.ns["ns=powertrain;i=16853"], "i=17597", "ns=irdi_v1_0_0;s=0112/2///62683#ACE508")


@o6.objecttype(
    nodeId="ns=powertrain;i=16847", browseName="ns=powertrain;PtContactorAttributesType", displayName="PtContactorAttributesType", description="power train contactor type"
)
class PtContactorAttributesType(PtAssetAttributesType):
    controlVoltageAC50HzRangeRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6145"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6027",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtContactorAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberofAuxiliaryContactsNC: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=16853"])
    numberofAuxiliaryContactsNO: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=16852"])
    numberofMainContactsNO: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=16850"])
    operationalCurrentAC3At400VRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6590"])


@o6.objecttype(
    nodeId="ns=powertrain;i=16854",
    browseName="ns=powertrain;PtMotorStarterAttributesType",
    displayName="PtMotorStarterAttributesType",
    description="Provides attributes of a motor starter",
)
class PtMotorStarterAttributesType(PtAssetAttributesType):
    controlVoltageAC50HzRangeRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6597"])
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6048",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMotorStarterAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberofAuxiliaryContactsNC: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6599"])
    numberofAuxiliaryContactsNO: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6598"])
    numberofMainContactsNO: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6596"])
    operationalCurrentAC3At400VRated: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6397"])
    overloadCurrentSettingRange: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=powertrain;i=6393"])
    tripClass: ns0.vartypes.MultiStateValueDiscreteType


@o6.objecttype(
    nodeId="ns=powertrain;i=16873",
    browseName="ns=powertrain;PtCommonAssetAttributesType",
    displayName="PtCommonAssetAttributesType",
    description="Provides attributes which apply to any or many of powertrain assets",
    isAbstract=True,
)
class PtCommonAssetAttributesType(PtAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6026",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtStandardAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16875",
    browseName="ns=powertrain;PtAmbientAttributesType",
    displayName="PtAmbientAttributesType",
    description="Provides ambient conditions in which the equipment is guaranteed to function",
)
class PtAmbientAttributesType(PtCommonAssetAttributesType):
    altitudeMax: ns0.vartypes.AnalogUnitType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6804",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAmbientAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    humidityMax: ns0.vartypes.AnalogUnitType | None
    humidityMin: ns0.vartypes.AnalogUnitType | None
    pressureMax: ns0.vartypes.AnalogUnitType | None
    pressureMin: ns0.vartypes.AnalogUnitType | None
    temperatureMax: ns0.vartypes.AnalogUnitType
    temperatureMin: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=powertrain;i=16907",
    browseName="ns=powertrain;PtAnalogInputElectricalAttributesType",
    displayName="PtAnalogInputElectricalAttributesType",
    description="Provides analog input properties",
)
class PtAnalogInputElectricalAttributesType(PtCommonAssetAttributesType):
    analogInputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6805",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAnalogInputElectricalAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    galvanicIsolationSupported: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16909", browseName="ns=powertrain;GalvanicIsolationSupported", dataType=o6.Boolean)
    )
    inputCurrentRange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=powertrain;i=6614", browseName="ns=powertrain;InputCurrentRange", dataType=ns0.datatypes.Range)
    )
    inputVoltageRange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=powertrain;i=6613", browseName="ns=powertrain;InputVoltageRange", dataType=ns0.datatypes.Range)
    )
    internalResistance: ns0.vartypes.AnalogUnitType | None
    numberOfChannels: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6615", browseName="ns=powertrain;NumberOfChannels", dataType=o6.UInt16)
    )
    resolution: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16911", browseName="ns=powertrain;Resolution", dataType=o6.Int32)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16913",
    browseName="ns=powertrain;PtAnalogOutputElectricalAttributesType",
    displayName="PtAnalogOutputElectricalAttributesType",
    description="Provides analog output properties",
)
class PtAnalogOutputElectricalAttributesType(PtCommonAssetAttributesType):
    analogOutputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6806",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAnalogOutputElectricalAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    frequencyRange: ns0.vartypes.BaseDataVariableType | None
    loadResistance: ns0.vartypes.AnalogUnitType | None
    numberOfChannels: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6618", browseName="ns=powertrain;NumberOfChannels", dataType=o6.UInt16)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16928",
    browseName="ns=powertrain;PtAuxiliarySupplyAttributesType",
    displayName="PtAuxiliarySupplyAttributesType",
    description="Provides attributes of the auxiliary supply of an inverter",
)
class PtAuxiliarySupplyAttributesType(PtCommonAssetAttributesType):
    currentMax: ns0.vartypes.AnalogUnitType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6807",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAuxiliarySupplyAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fuseProtectionCurrentMax: ns0.vartypes.AnalogUnitType | None
    powerConsumptionMax: ns0.vartypes.AnalogUnitType | None
    supplyVoltageAc: ns0.vartypes.AnalogUnitType | None
    supplyVoltageDc: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16960",
    browseName="ns=powertrain;PtCertificateAttributesType",
    displayName="PtCertificateAttributesType",
    description="Provides attributes of all supported certificates",
)
class PtCertificateAttributesType(PtCommonAssetAttributesType):
    certificates: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16962", browseName="ns=powertrain;Certificates", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6808",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtCertificateAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16963",
    browseName="ns=powertrain;PtCommunicationInterfaceAttributesType",
    displayName="PtCommunicationInterfaceAttributesType",
    description="Provides information about the communication attributes",
)
class PtCommunicationInterfaceAttributesType(PtCommonAssetAttributesType):
    communicationSpeed: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16968", browseName="ns=powertrain;CommunicationSpeed", dataType=o6.String)
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6809",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtCommunicationInterfaceAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    numberOfPorts: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16969", browseName="ns=powertrain;NumberOfPorts", dataType=o6.UInt16)
    )
    profileTypes: ns0.vartypes.MultiStateValueDiscreteType | None
    protocolTypes: ns0.vartypes.MultiStateValueDiscreteType
    safetyProtocolTypes: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=16970",
    browseName="ns=powertrain;PtCoolingAttributesType",
    displayName="PtCoolingAttributesType",
    description="Provides information about the cooling type",
)
class PtCoolingAttributesType(PtCommonAssetAttributesType):
    coolingMethod: ns0.vartypes.MultiStateValueDiscreteType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6811",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtCoolingAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=16973",
    browseName="ns=powertrain;PtHardwareAttributesType",
    displayName="PtHardwareAttributesType",
    description="Attributes describing the physical values and dimensions",
)
class PtHardwareAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6815",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtHardwareAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    frameSizeCoding: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6148", browseName="ns=powertrain;FrameSizeCoding", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    heatDissipationPower: ns0.vartypes.AnalogUnitType | None
    height: ns0.vartypes.AnalogUnitType | None
    length: ns0.vartypes.AnalogUnitType | None
    noiseLevel: ns0.vartypes.AnalogUnitType | None
    weight: ns0.vartypes.AnalogUnitType | None
    width: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=17000",
    browseName="ns=powertrain;PtDigitalInputElectricalAttributesType",
    displayName="PtDigitalInputElectricalAttributesType",
    description="Attributes describing the type of digital inputs",
)
class PtDigitalInputElectricalAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6810",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtDigitalInputElectricalAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    digitalInputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    numberOfChannels: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17008", browseName="ns=powertrain;NumberOfChannels", dataType=o6.UInt16)
    )
    safetyPropertySupported: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6421", browseName="ns=powertrain;SafetyPropertySupported", dataType=o6.Boolean)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=17009",
    browseName="ns=powertrain;PtDigitalOutputElectricalAttributesType",
    displayName="PtDigitalOutputElectricalAttributesType",
    description="Attributes describing the type of digital outputs",
)
class PtDigitalOutputElectricalAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6812",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtDigitalOutputElectricalAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    digitalOutputElectricalType: ns0.vartypes.MultiStateValueDiscreteType | None
    numberOfChannels: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17023", browseName="ns=powertrain;NumberOfChannels", dataType=o6.UInt16)
    )
    outputCurrentMax: ns0.vartypes.AnalogUnitType | None
    safetyPropertySupported: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6423", browseName="ns=powertrain;SafetyPropertySupported", dataType=o6.Boolean)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=17024", browseName="ns=powertrain;PtFuseAttributesType", displayName="PtFuseAttributesType", description="Provides the attributes describing a fuse"
)
class PtFuseAttributesType(PtCommonAssetAttributesType):
    breakingCapacity: ns0.vartypes.AnalogUnitType | None
    currentRated: ns0.vartypes.AnalogUnitType | None
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6814",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtFuseAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fuseElementSpeedMarking: ns0.vartypes.MultiStateValueDiscreteType | None
    fuseIdentificationType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6443", browseName="ns=powertrain;FuseIdentificationType", dataType=o6.String)
    )
    voltageRated: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=17046",
    browseName="ns=powertrain;PtInputInterfaceAttributesType",
    displayName="PtInputInterfaceAttributesType",
    description="Provides attributes describing the interface to the mains line",
)
class PtInputInterfaceAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6816",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtInputInterfaceAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    inputCurrentMax: ns0.vartypes.AnalogUnitType | None
    inputCurrentRated: ns0.vartypes.AnalogUnitType | None
    inputFrequencyMax: ns0.vartypes.AnalogUnitType | None
    inputFrequencyRangeRated: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=powertrain;i=6519", browseName="ns=powertrain;InputFrequencyRangeRated", dataType=ns0.datatypes.Range)
    )
    inputPowerMax: ns0.vartypes.AnalogUnitType | None
    inputPowerRated: ns0.vartypes.AnalogUnitType | None
    inputVoltageMax: ns0.vartypes.AnalogUnitType | None
    inputVoltageRange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=powertrain;i=6656", browseName="ns=powertrain;InputVoltageRange", dataType=ns0.datatypes.Range)
    )
    inputVoltageRated: ns0.vartypes.AnalogUnitType | None
    numberOfInputPhases: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17084", browseName="ns=powertrain;NumberOfInputPhases", dataType=o6.Byte)
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=17085", browseName="ns=powertrain;PtOutputInterfaceAttributesType", displayName="PtOutputInterfaceAttributesType", description="Provides ...."
)
class PtOutputInterfaceAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6818",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtOutputInterfaceAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    inputCurrentRated: ns0.vartypes.AnalogUnitType | None
    inputVoltageRated: ns0.vartypes.AnalogUnitType | None
    numberOfOutputPhases: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17135", browseName="ns=powertrain;NumberOfOutputPhases", dataType=o6.Byte)
    )
    outputCurrentMax: ns0.vartypes.AnalogUnitType | None
    outputCurrentRated: ns0.vartypes.AnalogUnitType | None
    outputFrequencyMax: ns0.vartypes.AnalogUnitType | None
    outputFrequencyRated: ns0.vartypes.AnalogUnitType | None
    outputPowerMax: ns0.vartypes.AnalogUnitType | None
    outputPowerRated: ns0.vartypes.AnalogUnitType | None
    outputVoltageMax: ns0.vartypes.AnalogUnitType | None
    outputVoltageRange: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=powertrain;i=6520", browseName="ns=powertrain;OutputVoltageRange", dataType=ns0.datatypes.Range)
    )
    outputVoltageRated: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=17136",
    browseName="ns=powertrain;PtMechanicalStrengthAttributesType",
    displayName="PtMechanicalStrengthAttributesType",
    description="Provides the attributes describing the mechanical strength.",
)
class PtMechanicalStrengthAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6817",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtMechanicalStrengthAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    shock: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17138", browseName="ns=powertrain;Shock", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    vibration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17139", browseName="ns=powertrain;Vibration", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=17140",
    browseName="ns=powertrain;PtProtectionClassAttributesType",
    displayName="PtProtectionClassAttributesType",
    description="Provides the attributes describing the protection class.",
)
class PtProtectionClassAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6819",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtProtectionClassAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    exClass: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6310", browseName="ns=powertrain;ExClass", dataType=o6.String))
    ipClass: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15912",
    browseName="ns=powertrain;PtAssetType",
    displayName="PtAssetType",
    description="Provides properties required for identifying assets of a powertrain",
    interfaces=[
        di.objtypes.IDeviceHealthType,
        di.objtypes.ISupportInfoType,
        fx_ac.objtypes.IAssetRevisionType,
        machinery.objtypes.IMachineryItemVendorNameplateType,
        IPtTagNameplateType,
    ],
)
class PtAssetType(ns0.objtypes.BaseObjectType):
    assetId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6243", browseName="ns=di;AssetId", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    buildAssetNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6471", browseName="ns=fx_ac;BuildAssetNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    comment: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6046", browseName="ns=powertrain;Comment", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    componentName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6236", browseName="ns=di;ComponentName", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    contactInformation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6257", browseName="ns=powertrain;ContactInformation", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6367",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("powertrain:PtAsset_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    deviceClass: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6059", browseName="ns=di;DeviceClass", dataType=o6.String))
    deviceHealth: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=powertrain;i=6058", browseName="ns=di;DeviceHealth", dataType=di.datatypes.DeviceHealthEnumeration)
    )
    deviceHealthAlarms: ns0.objtypes.FolderType | None = o6.hasComponent(ns0.objtypes.FolderType(nodeId="ns=powertrain;i=5000", browseName="ns=di;DeviceHealthAlarms"))
    deviceManual: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6062", browseName="ns=di;DeviceManual", dataType=o6.String))
    deviceRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6060", browseName="ns=di;DeviceRevision", dataType=o6.String)
    )
    deviceTypeImage: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=powertrain;i=5004"])
    documentation: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=powertrain;i=5005"])
    documentationFiles: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=powertrain;i=5039"])
    function: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6262", browseName="ns=powertrain;Function", dataType=o6.String, accessLevel=3, userAccessLevel=1)
    )
    hardwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6061", browseName="ns=di;HardwareRevision", dataType=o6.String)
    )
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    imageSet: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=powertrain;i=5006"])
    initialOperationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6231",
            browseName="ns=machinery;InitialOperationDate",
            description="The date, when the MachineryItem was switched on the first time after it has left the manufacturer plant.",
            dataType=o6.DateTime,
        )
    )
    langlePtAnalogInputElectricalAttributesRangle: PtAnalogInputElectricalAttributesType | None = o6.hasComponent(
        PtAnalogInputElectricalAttributesType(nodeId="ns=powertrain;i=5015", browseName="ns=powertrain;<PtAnalogInputElectricalAttributes>", modellingRule="OptionalPlaceholder")
    )
    langlePtAnalogOutputElectricalAttributesRangle: PtAnalogOutputElectricalAttributesType | None = o6.hasComponent(
        PtAnalogOutputElectricalAttributesType(nodeId="ns=powertrain;i=5017", browseName="ns=powertrain;<PtAnalogOutputElectricalAttributes>", modellingRule="OptionalPlaceholder")
    )
    langlePtDigitalInputElectricalAttributesRangle: PtDigitalInputElectricalAttributesType | None = o6.hasComponent(
        PtDigitalInputElectricalAttributesType(nodeId="ns=powertrain;i=5016", browseName="ns=powertrain;<PtDigitalInputElectricalAttributes>", modellingRule="OptionalPlaceholder")
    )
    langlePtDigitalOutputElectricalAttributesRangle: PtDigitalOutputElectricalAttributesType | None = o6.hasComponent(
        PtDigitalOutputElectricalAttributesType(
            nodeId="ns=powertrain;i=5018", browseName="ns=powertrain;<PtDigitalOutputElectricalAttributes>", modellingRule="OptionalPlaceholder"
        )
    )
    langlePtStandardAttributesRangle: PtStandardAttributesType | None
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6244",
            browseName="ns=machinery;Location",
            description="To be used by end users to store the location of the machine in a scheme specific to the end user Servers shall support at least 60 Unicode characters for the clients writing this value, this means clients can expect to be able to write strings with a length of 60 Unicode characters into that field.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    majorAssetVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6469", browseName="ns=fx_ac;MajorAssetVersion", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6051",
            browseName="ns=di;Manufacturer",
            description="A human-readable, localized name of the manufacturer of the MachineryItem.",
            dataType=o6.LocalizedText,
        )
    )
    manufacturerUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6063", browseName="ns=di;ManufacturerUri", dataType=o6.String)
    )
    minorAssetVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6056", browseName="ns=fx_ac;MinorAssetVersion", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    model: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6064", browseName="ns=di;Model", dataType=o6.LocalizedText))
    monthOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6230",
            browseName="ns=machinery;MonthOfConstruction",
            description="The month in which the manufacturing process of the MachineryItem has been completed. It shall be a number between 1 and 12, representing the month from January to December.",
            dataType=o6.Byte,
        )
    )
    patchIdentifiers: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6093", browseName="ns=di;PatchIdentifiers", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )
    productCode: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6212", browseName="ns=di;ProductCode", dataType=o6.String))
    productInstanceUri: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6203", browseName="ns=di;ProductInstanceUri", dataType=o6.String)
    )
    protocolSupport: ns0.objtypes.FolderType | None = o6.hasComponent(o6.ns["ns=powertrain;i=5007"])
    ptAmbientAttributes: PtAmbientAttributesType | None
    ptAuxiliarySupplyAttributes: PtAuxiliarySupplyAttributesType | None = o6.hasComponent(
        PtAuxiliarySupplyAttributesType(nodeId="ns=powertrain;i=5014", browseName="ns=powertrain;PtAuxiliarySupplyAttributes")
    )
    ptCertificateAttributes: PtCertificateAttributesType | None
    ptHardwareAttributes: PtHardwareAttributesType | None = o6.hasComponent(
        PtHardwareAttributesType(nodeId="ns=powertrain;i=5012", browseName="ns=powertrain;PtHardwareAttributes")
    )
    ptMechanicalStrengthAttributes: PtMechanicalStrengthAttributesType | None = o6.hasComponent(
        PtMechanicalStrengthAttributesType(nodeId="ns=powertrain;i=5011", browseName="ns=powertrain;PtMechanicalStrengthAttributes")
    )
    ptProtectionClassAttributes: PtProtectionClassAttributesType | None = o6.hasComponent(
        PtProtectionClassAttributesType(nodeId="ns=powertrain;i=5013", browseName="ns=powertrain;PtProtectionClassAttributes")
    )
    revisionCounter: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6213", browseName="ns=di;RevisionCounter", dataType=o6.Int32)
    )
    serialNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6000",
            browseName="ns=di;SerialNumber",
            description="A string containing a unique production number of the manufacturer of the MachineryItem. The global uniqueness of the serial number is only given in the context of the manufacturer, and potentially the model. The value shall not change during the life-cycle of the MachineryItem.",
            dataType=o6.String,
        )
    )
    softwareReleaseDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6229", browseName="ns=di;SoftwareReleaseDate", dataType=o6.DateTime)
    )
    softwareRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6217", browseName="ns=di;SoftwareRevision", dataType=o6.String)
    )
    subBuildAssetNumber: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6057", browseName="ns=fx_ac;SubBuildAssetNumber", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    verifyAsset: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=powertrain;i=7000"])
    yearOfConstruction: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6232",
            browseName="ns=machinery;YearOfConstruction",
            description="The year (Gregorian calendar) in which the manufacturing process of the MachineryItem has been completed. It shall be a four-digit number and never change during the life-cycle of a MachineryItem.",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(nodeId="ns=powertrain;i=1005", browseName="ns=powertrain;PtAssetDcBusModuleType", displayName="PtAssetDcBusModuleType")
class PtAssetDcBusModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6476",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetDcBusModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptCapacitanceAttributes: PtCapacitanceAttributesType | None
    ptDcBusAttributes: PtDcBusAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=1007", browseName="ns=powertrain;PtAssetReactorFilterType", displayName="PtAssetReactorFilterType")
class PtAssetReactorFilterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6589",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetReactorFilter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType | None
    ptReactorAttributes: PtReactorAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=1013", browseName="ns=powertrain;PtAssetBleedType", displayName="PtAssetBleedType")
class PtAssetBleedType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6467",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetBleed_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptBleedAttributes: PtBleedAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=1026", browseName="ns=powertrain;PtAssetElectricOverloadRelayType", displayName="PtAssetElectricOverloadRelayType")
class PtAssetElectricOverloadRelayType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6481",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetElectricOverloadRelay_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptCommunicationInterfaceAttributes: PtCommunicationInterfaceAttributesType | None
    ptElectronicOverloadRelayAttributes: PtElectronicOverloadRelayAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=1031", browseName="ns=powertrain;PtAssetPrechargeType", displayName="PtAssetPrechargeType")
class PtAssetPrechargeType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6588",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetPrecharge_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtFuseAttributesRangle: PtFuseAttributesType | None = o6.reference(
        PtFuseAttributesType(nodeId="ns=powertrain;i=5120", browseName="ns=powertrain;<PtFuseAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    ptCoolingAttributes: PtCoolingAttributesType | None = o6.reference(
        PtCoolingAttributesType(nodeId="ns=powertrain;i=5119", browseName="ns=powertrain;PtCoolingAttributes"), "ns=powertrain;i=4004"
    )
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType
    ptPrechargeAttributes: PtPrechargeAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=1034", browseName="ns=powertrain;PtAssetSoftStarterType", displayName="PtAssetSoftStarterType")
class PtAssetSoftStarterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6620",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetSoftStarter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptCommunicationInterfaceAttributes: PtCommunicationInterfaceAttributesType | None
    ptSoftStarterAttributes: PtSoftStarterAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=1040", browseName="ns=powertrain;PtAssetMotorManagementDeviceType", displayName="PtAssetMotorManagementDeviceType")
class PtAssetMotorManagementDeviceType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6580",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetMotorManagementDevice_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptCommunicationInterfaceAttributes: PtCommunicationInterfaceAttributesType | None
    ptMotorManagementDeviceAttributes: PtMotorManagementDeviceAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=15083", browseName="ns=powertrain;PtAssetMotorType", displayName="PtAssetMotorType", description="Describes a motor in a powertrain")
class PtAssetMotorType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6374",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetMotor_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptBrakeAttributes: PtBrakeAttributesType | None
    ptCoolingAttributes: PtCoolingAttributesType | None = o6.reference(
        PtCoolingAttributesType(nodeId="ns=powertrain;i=15094", browseName="ns=powertrain;PtCoolingAttributes"), "ns=powertrain;i=4004"
    )
    ptTemperatureSensorAttributes: PtTemperatureSensorAttributesType | None
    ptVibrationSensorAttributes: PtVibrationSensorAttributesType | None


@o6.objecttype(nodeId="ns=powertrain;i=1027", browseName="ns=powertrain;PtAssetMotorRotaryType", displayName="PtAssetMotorRotaryType")
class PtAssetMotorRotaryType(PtAssetMotorType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6822",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetMotorRotary_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderRotaryAttributesRangle: PtEncoderRotaryAttributesType | None = o6.reference(
        PtEncoderRotaryAttributesType(nodeId="ns=powertrain;i=5087", browseName="ns=powertrain;<PtEncoderRotaryAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )
    langlePtMotorRotaryRatedAttributesRangle: PtMotorRotaryRatedAttributesType
    ptMotorRotaryAttributes: PtMotorRotaryAttributesType = o6.reference(
        PtMotorRotaryAttributesType(nodeId="ns=powertrain;i=5084", browseName="ns=powertrain;PtMotorRotaryAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(nodeId="ns=powertrain;i=1025", browseName="ns=powertrain;PtAssetGearMotorRotaryType", displayName="PtAssetGearMotorRotaryType")
class PtAssetGearMotorRotaryType(PtAssetMotorRotaryType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6407",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetGearMotorRotary_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptGearAttributes: PtGearAttributesType = o6.reference(PtGearAttributesType(nodeId="ns=powertrain;i=5095", browseName="ns=powertrain;PtGearAttributes"), "ns=powertrain;i=4004")


@o6.objecttype(nodeId="ns=powertrain;i=1030", browseName="ns=powertrain;PtAssetMotorLinearType", displayName="PtAssetMotorLinearType")
class PtAssetMotorLinearType(PtAssetMotorType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6406",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetMotorLinear_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderLinearAttributesRangle: PtEncoderLinearAttributesType | None = o6.reference(
        PtEncoderLinearAttributesType(nodeId="ns=powertrain;i=5091", browseName="ns=powertrain;<PtEncoderLinearAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )
    langlePtMotorLinearRatedAttributesRangle: PtMotorLinearRatedAttributesType
    ptMotorLinearAttributes: PtMotorLinearAttributesType = o6.reference(
        PtMotorLinearAttributesType(nodeId="ns=powertrain;i=5088", browseName="ns=powertrain;PtMotorLinearAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(nodeId="ns=powertrain;i=1029", browseName="ns=powertrain;PtAssetGearMotorLinearType", displayName="PtAssetGearMotorLinearType")
class PtAssetGearMotorLinearType(PtAssetMotorLinearType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6417",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetGearMotorLinear_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptGearAttributes: PtGearAttributesType = o6.reference(PtGearAttributesType(nodeId="ns=powertrain;i=5096", browseName="ns=powertrain;PtGearAttributes"), "ns=powertrain;i=4004")


@o6.objecttype(nodeId="ns=powertrain;i=15116", browseName="ns=powertrain;PtAssetBrakeType", displayName="PtAssetBrakeType", description="Describes a brake used in a powertrain")
class PtAssetBrakeType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6468",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetBrake_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptBrakeAttributes: PtBrakeAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=15122", browseName="ns=powertrain;PtAssetGearType", displayName="PtAssetGearType", description="Describes a gear in a powertrain")
class PtAssetGearType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6484",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetGear_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptGearAttributes: PtGearAttributesType = o6.reference(PtGearAttributesType(nodeId="ns=powertrain;i=15127", browseName="ns=powertrain;PtGearAttributes"), "ns=powertrain;i=4004")
    ptTemperatureSensorAttributes: PtTemperatureSensorAttributesType | None
    ptVibrationSensorAttributes: PtVibrationSensorAttributesType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15130",
    browseName="ns=powertrain;PtAssetTemperatureSensorType",
    displayName="PtAssetTemperatureSensorType",
    description="Describes a temperature sensor used in a powertrain",
)
class PtAssetTemperatureSensorType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6621",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetTemperatureSensor_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptTemperatureSensorAttributes: PtTemperatureSensorAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=15136",
    browseName="ns=powertrain;PtAssetVibrationSensorType",
    displayName="PtAssetVibrationSensorType",
    description="Vibration sensor used in a powertrain",
)
class PtAssetVibrationSensorType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6622",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetVibrationSensor_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptVibrationSensorAttributes: PtVibrationSensorAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=15148",
    browseName="ns=powertrain;PtAssetElectricalBrakingModuleType",
    displayName="PtAssetElectricalBrakingModuleType",
    description="Brakeing module including brake resistor of an inverter",
)
class PtAssetElectricalBrakingModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6480",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetElectricalBrakingModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptBleedAttributes: PtBleedAttributesType
    ptCoolingAttributes: PtCoolingAttributesType | None = o6.reference(
        PtCoolingAttributesType(nodeId="ns=powertrain;i=15154", browseName="ns=powertrain;PtCoolingAttributes"), "ns=powertrain;i=4004"
    )
    ptDcBusAttributes: PtDcBusAttributesType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15196", browseName="ns=powertrain;PtAssetInputFilterType", displayName="PtAssetInputFilterType", description="Describes an input filter in an inverter"
)
class PtAssetInputFilterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6488",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetInputFilter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptInputFilterAttributes: PtInputFilterAttributesType
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType | None
    ptReactorAttributes: PtReactorAttributesType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15241",
    browseName="ns=powertrain;PtAssetInputReactorType",
    displayName="PtAssetInputReactorType",
    description="Describes an input filter realized by an input reactor",
)
class PtAssetInputReactorType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6522",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetInputReactor_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType | None
    ptReactorAttributes: PtReactorAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=15303",
    browseName="ns=powertrain;PtAssetOutputFilterType",
    displayName="PtAssetOutputFilterType",
    description="Describes an output filter in an inverter",
)
class PtAssetOutputFilterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6586",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetOutputFilter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptOutputFilterAttributes: PtOutputFilterAttributesType
    ptOutputInterfaceAttributes: PtOutputInterfaceAttributesType | None
    ptReactorAttributes: PtReactorAttributesType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15368",
    browseName="ns=powertrain;PtAssetOutputReactorType",
    displayName="PtAssetOutputReactorType",
    description="Describes an output reactor in an inverter",
)
class PtAssetOutputReactorType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6587",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetOutputReactor_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptOutputInterfaceAttributes: PtOutputInterfaceAttributesType | None
    ptReactorAttributes: PtReactorAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=15541", browseName="ns=powertrain;PtAssetCoolingType", displayName="PtAssetCoolingType", description="Describes the colling part of an inveter"
)
class PtAssetCoolingType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6803",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetCooling_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCoolingAttributesRangle: PtCoolingAttributesType


@o6.objecttype(nodeId="ns=powertrain;i=15549", browseName="ns=powertrain;PtAssetContactorType", displayName="PtAssetContactorType", description="powertrain asset contactor type")
class PtAssetContactorType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6472",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetContactor_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptContactorAttributes: PtContactorAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=15561", browseName="ns=powertrain;PtAssetMotorStarterType", displayName="PtAssetMotorStarterType", description="powertrain asset motor startet type"
)
class PtAssetMotorStarterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6584",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetMotorStarter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptCommunicationInterfaceAttributes: PtCommunicationInterfaceAttributesType | None
    ptMotorStarterAttributes: PtMotorStarterAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=17149",
    browseName="ns=powertrain;PtSafetyFunctionsAttributesType",
    displayName="PtSafetyFunctionsAttributesType",
    description="Provides the attributes describing the safety functions, standards, safety integrity level (SIL), safety perofmrance level and safety category.",
)
class PtSafetyFunctionsAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6820",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtSafetyFunctionsAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    functionalSafetyCategory: ns0.vartypes.MultiStateValueDiscreteType | None
    functionalSafetyPerformanceLevel: ns0.vartypes.MultiStateValueDiscreteType | None
    functionalSafetySilLevel: ns0.vartypes.MultiStateValueDiscreteType | None
    safetyFunctions: ns0.vartypes.MultiStateValueDiscreteType | None
    safetyStandards: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17152", browseName="ns=powertrain;SafetyStandards", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="ns=powertrain;i=1035", browseName="ns=powertrain;PtAssetDriveType", displayName="PtAssetDriveType")
class PtAssetDriveType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6477",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetDrive_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtOutputConverterAttributesRangle: PtOutputConverterAttributesType
    langlePtOutputFilterAttributesRangle: PtOutputFilterAttributesType | None
    langlePtOutputInterfaceAttributesRangle: PtOutputInterfaceAttributesType | None
    langlePtOutputReactorAttributesRangle: PtReactorAttributesType | None
    ptBleedAttributes: PtBleedAttributesType | None
    ptCommunicationInterfaceAttributes: PtCommunicationInterfaceAttributesType | None
    ptDcBusAttributes: PtDcBusAttributesType | None
    ptInputConverterAttributes: PtInputConverterAttributesType | None
    ptInputFilterAttributes: PtInputFilterAttributesType | None = o6.reference(
        PtInputFilterAttributesType(nodeId="ns=powertrain;i=5128", browseName="ns=powertrain;PtInputFilterAttributes"), "ns=powertrain;i=4004"
    )
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType | None
    ptInputReactorAttributes: PtReactorAttributesType | None
    ptSafetyFunctionsAttributes: PtSafetyFunctionsAttributesType | None = o6.reference(
        PtSafetyFunctionsAttributesType(nodeId="ns=powertrain;i=5132", browseName="ns=powertrain;PtSafetyFunctionsAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(nodeId="ns=powertrain;i=1016", browseName="ns=powertrain;PtAssetFrequencyConverterType", displayName="PtAssetFrequencyConverterType")
class PtAssetFrequencyConverterType(PtAssetDriveType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6638",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetFrequencyConverter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=powertrain;i=1020", browseName="ns=powertrain;PtAssetServoDriveType", displayName="PtAssetServoDriveType")
class PtAssetServoDriveType(PtAssetDriveType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6639",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetServoDrive_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType = o6.reference(
        PtEncoderInterfaceAttributesType(nodeId="ns=powertrain;i=5031", browseName="ns=powertrain;<PtEncoderInterfaceAttributes>", modellingRule="MandatoryPlaceholder"),
        "ns=powertrain;i=4004",
    )


@o6.objecttype(nodeId="ns=powertrain;i=1028", browseName="ns=powertrain;PtAssetVariableSpeedDriveType", displayName="PtAssetVariableSpeedDriveType")
class PtAssetVariableSpeedDriveType(PtAssetDriveType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6640",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("powertrain:PtAssetVariableSpeedDrive_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType | None = o6.reference(
        PtEncoderInterfaceAttributesType(nodeId="ns=powertrain;i=5032", browseName="ns=powertrain;<PtEncoderInterfaceAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=17144",
    browseName="ns=powertrain;PtFunctionalSafetyAttributesType",
    displayName="PtFunctionalSafetyAttributesType",
    description="Provides the attributes describing various safety functions, certifications and safety transport protocols.",
)
class PtFunctionalSafetyAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6813",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtFunctionalSafetyAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langleSafetyFunctionsAttributesRangle: PtSafetyFunctionsAttributesType | None = o6.reference(
        PtSafetyFunctionsAttributesType(nodeId="ns=powertrain;i=5064", browseName="ns=powertrain;<SafetyFunctionsAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )
    safetyAssessor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6433", browseName="ns=powertrain;SafetyAssessor", dataType=o6.String)
    )
    safetyTransportProtocols: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6434", browseName="ns=powertrain;SafetyTransportProtocols", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="ns=powertrain;i=1011", browseName="ns=powertrain;PtAssetDriveIntegratedMotorRotaryType", displayName="PtAssetDriveIntegratedMotorRotaryType")
class PtAssetDriveIntegratedMotorRotaryType(PtAssetMotorRotaryType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6797",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetDriveIntegratedMotorRotary_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtOutputConverterAttributesRangle: PtOutputConverterAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=5058", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )
    ptInputConverterAttributes: PtInputConverterAttributesType | None
    ptInputFilterAttributes: PtInputFilterAttributesType | None = o6.reference(
        PtInputFilterAttributesType(nodeId="ns=powertrain;i=5003", browseName="ns=powertrain;PtInputFilterAttributes"), "ns=powertrain;i=4004"
    )
    ptReactorAttributes: PtReactorAttributesType | None


@o6.objecttype(nodeId="ns=powertrain;i=1033", browseName="ns=powertrain;PtAssetDriveIntegratedGearMotorRotaryType", displayName="PtAssetDriveIntegratedGearMotorRotaryType")
class PtAssetDriveIntegratedGearMotorRotaryType(PtAssetDriveIntegratedMotorRotaryType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6800",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetDriveIntegratedGearMotorRotary_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptGearAttributes: PtGearAttributesType = o6.reference(PtGearAttributesType(nodeId="ns=powertrain;i=5097", browseName="ns=powertrain;PtGearAttributes"), "ns=powertrain;i=4004")


@o6.objecttype(nodeId="ns=powertrain;i=1017", browseName="ns=powertrain;PtAssetDriveIntegratedMotorLinearType", displayName="PtAssetDriveIntegratedMotorLinearType")
class PtAssetDriveIntegratedMotorLinearType(PtAssetMotorLinearType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6798",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetDriveIntegratedMotorLinear_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtOutputConverterAttributesRangle: PtOutputConverterAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=5092", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )
    ptInputConverterAttributes: PtInputConverterAttributesType | None
    ptInputFilterAttributes: PtInputFilterAttributesType | None = o6.reference(
        PtInputFilterAttributesType(nodeId="ns=powertrain;i=5062", browseName="ns=powertrain;PtInputFilterAttributes"), "ns=powertrain;i=4004"
    )
    ptReactorAttributes: PtReactorAttributesType | None


@o6.objecttype(nodeId="ns=powertrain;i=1036", browseName="ns=powertrain;PtAssetDriveIntegratedGearMotorLinearType", displayName="PtAssetDriveIntegratedGearMotorLinearType")
class PtAssetDriveIntegratedGearMotorLinearType(PtAssetDriveIntegratedMotorLinearType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6799",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetDriveIntegratedGearMotorLinear_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptGearAttributes: PtGearAttributesType = o6.reference(PtGearAttributesType(nodeId="ns=powertrain;i=5098", browseName="ns=powertrain;PtGearAttributes"), "ns=powertrain;i=4004")


@o6.objecttype(nodeId="ns=powertrain;i=1045", browseName="ns=powertrain;PtAssetEncoderInterfaceModuleType", displayName="PtAssetEncoderInterfaceModuleType")
class PtAssetEncoderInterfaceModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6482",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetEncoderInterfaceModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType = o6.reference(
        PtEncoderInterfaceAttributesType(nodeId="ns=powertrain;i=5101", browseName="ns=powertrain;<PtEncoderInterfaceAttributes>", modellingRule="MandatoryPlaceholder"),
        "ns=powertrain;i=4004",
    )
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=5102", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(nodeId="ns=powertrain;i=1022", browseName="ns=powertrain;PtAssetInputOutputConverterType", displayName="PtAssetInputOutputConverterType")
class PtAssetInputOutputConverterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6502",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetInputOutputConverter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtCoolingAttributesRangle: PtCoolingAttributesType | None = o6.reference(
        PtCoolingAttributesType(nodeId="ns=powertrain;i=5112", browseName="ns=powertrain;<PtCoolingAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType | None = o6.reference(
        PtEncoderInterfaceAttributesType(nodeId="ns=powertrain;i=5111", browseName="ns=powertrain;<PtEncoderInterfaceAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )
    langlePtFunctionalSafetyAttributesRangle: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=5115", browseName="ns=powertrain;<PtFunctionalSafetyAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )
    langlePtFuseAttributesRangle: PtFuseAttributesType | None = o6.reference(
        PtFuseAttributesType(nodeId="ns=powertrain;i=5114", browseName="ns=powertrain;<PtFuseAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    langlePtReactorAttributesRangle: PtReactorAttributesType | None
    ptDcBusAttributes: PtDcBusAttributesType | None
    ptInputConverterAttributes: PtInputConverterAttributesType
    ptInputFilterAttributes: PtInputFilterAttributesType | None = o6.reference(
        PtInputFilterAttributesType(nodeId="ns=powertrain;i=5109", browseName="ns=powertrain;PtInputFilterAttributes"), "ns=powertrain;i=4004"
    )
    ptInputInterfaceAttributes: PtInputInterfaceAttributesType
    ptOutputConverterAttributes: PtOutputConverterAttributesType
    ptOutputFilterAttributes: PtOutputFilterAttributesType | None
    ptOutputInterfaceAttributes: PtOutputInterfaceAttributesType


@o6.objecttype(
    nodeId="ns=powertrain;i=15108", browseName="ns=powertrain;PtAssetEncoderType", displayName="PtAssetEncoderType", description="Describes an encoder used in a powertrain"
)
class PtAssetEncoderType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6483",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetEncoder_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    ptEncoderInterfaceAttributes: PtEncoderInterfaceAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=5020", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(nodeId="ns=powertrain;i=1039", browseName="ns=powertrain;PtAssetEncoderRotaryType", displayName="PtAssetEncoderRotaryType")
class PtAssetEncoderRotaryType(PtAssetEncoderType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6801",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetEncoderRotary_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptEncoderRotaryAttributes: PtEncoderRotaryAttributesType | None = o6.reference(
        PtEncoderRotaryAttributesType(nodeId="ns=powertrain;i=5099", browseName="ns=powertrain;PtEncoderRotaryAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(nodeId="ns=powertrain;i=1042", browseName="ns=powertrain;PtAssetEncoderLinearType", displayName="PtAssetEncoderLinearType")
class PtAssetEncoderLinearType(PtAssetEncoderType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6802",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetEncoderLinear_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    ptEncoderLinearAttributes: PtEncoderLinearAttributesType | None = o6.reference(
        PtEncoderLinearAttributesType(nodeId="ns=powertrain;i=5100", browseName="ns=powertrain;PtEncoderLinearAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=15168",
    browseName="ns=powertrain;PtAssetInputConverterType",
    displayName="PtAssetInputConverterType",
    description="Describes an input converter in an inverter",
)
class PtAssetInputConverterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6486",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetInputConverter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtCoolingAttributesRangle: PtCoolingAttributesType | None = o6.reference(
        PtCoolingAttributesType(nodeId="ns=powertrain;i=15177", browseName="ns=powertrain;<PtCoolingAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    langlePtFuseAttributesRangle: PtFuseAttributesType | None = o6.reference(
        PtFuseAttributesType(nodeId="ns=powertrain;i=15179", browseName="ns=powertrain;<PtFuseAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    langlePtInputInterfaceAttributesRangle: PtInputInterfaceAttributesType
    ptBleedAttributes: PtBleedAttributesType | None
    ptCapacitanceAttributes: PtCapacitanceAttributesType | None
    ptDcBusAttributes: PtDcBusAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=15180", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )
    ptInputConverterAttributes: PtInputConverterAttributesType | None
    ptInputFilterAttributes: PtInputFilterAttributesType | None
    ptReactorAttributes: PtReactorAttributesType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15182",
    browseName="ns=powertrain;PtAssetOutputConverterType",
    displayName="PtAssetOutputConverterType",
    description="Describes an output converter in an inverter",
)
class PtAssetOutputConverterType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6585",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetOutputConverter_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtCoolingAttributesRangle: PtCoolingAttributesType | None = o6.reference(
        PtCoolingAttributesType(nodeId="ns=powertrain;i=15191", browseName="ns=powertrain;<PtCoolingAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType | None
    langlePtFunctionalSafetyAttributesRangle: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=15194", browseName="ns=powertrain;<PtFunctionalSafetyAttributes>", modellingRule="OptionalPlaceholder"),
        "ns=powertrain;i=4004",
    )
    langlePtFuseAttributesRangle: PtFuseAttributesType | None = o6.reference(
        PtFuseAttributesType(nodeId="ns=powertrain;i=15193", browseName="ns=powertrain;<PtFuseAttributes>", modellingRule="OptionalPlaceholder"), "ns=powertrain;i=4004"
    )
    langlePtOutputConverterAttributesRangle: PtOutputConverterAttributesType
    langlePtOutputFilterAttributesRangle: PtOutputFilterAttributesType | None
    ptCapacitanceAttributes: PtCapacitanceAttributesType | None
    ptDcBusAttributes: PtDcBusAttributesType | None
    ptOutputInterfaceAttributes: PtOutputInterfaceAttributesType
    ptReactorAttributes: PtReactorAttributesType | None


@o6.objecttype(
    nodeId="ns=powertrain;i=15430",
    browseName="ns=powertrain;PtAssetCommunicationModuleType",
    displayName="PtAssetCommunicationModuleType",
    description="Describes a communication module of an inverter",
)
class PtAssetCommunicationModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6470",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetCommunicationModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=15442", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=15447",
    browseName="ns=powertrain;PtAssetControlModuleType",
    displayName="PtAssetControlModuleType",
    description="Describes the control part of an inverter",
)
class PtAssetControlModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6475",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetControlModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtCommunicationInterfaceAttributesRangle: PtCommunicationInterfaceAttributesType | None
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=15459", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=15468", browseName="ns=powertrain;PtAssetIoModuleType", displayName="PtAssetIoModuleType", description="Describes the IO-Module part of an inveter"
)
class PtAssetIoModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6527",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetIoModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType | None = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=15477", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=15527",
    browseName="ns=powertrain;PtAssetSafetyModuleType",
    displayName="PtAssetSafetyModuleType",
    description="Describes the functional safety part of an inverter",
)
class PtAssetSafetyModuleType(PtAssetType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6619",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtAssetSafetyModule_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    langlePtEncoderInterfaceAttributesRangle: PtEncoderInterfaceAttributesType | None
    ptFunctionalSafetyAttributes: PtFunctionalSafetyAttributesType = o6.reference(
        PtFunctionalSafetyAttributesType(nodeId="ns=powertrain;i=15532", browseName="ns=powertrain;PtFunctionalSafetyAttributes"), "ns=powertrain;i=4004"
    )


@o6.objecttype(
    nodeId="ns=powertrain;i=17156",
    browseName="ns=powertrain;PtStandardAttributesType",
    displayName="PtStandardAttributesType",
    description="Standards provides all supported standards of an powertrain asset.",
)
class PtStandardAttributesType(PtCommonAssetAttributesType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6821",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtStandardAttributes"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    standards: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17158", browseName="ns=powertrain;Standards", dataType=o6.String, valueRank=1, arrayDimensions=[0])
    )


@o6.objecttype(nodeId="ns=powertrain;i=16609", browseName="ns=powertrain;PtBrakeAttributesType", displayName="PtBrakeAttributesType", description="Provides attributes of a brake")
class PtBrakeAttributesType(PtAssetAttributesType):
    b10dValue: ns0.vartypes.AnalogUnitType | None
    brakeAccelerationVoltage: ns0.vartypes.AnalogUnitType | None
    brakeCoolingMethod: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16707", browseName="ns=powertrain;BrakeCoolingMethod", dataType=o6.String)
    )
    brakeCurrentRated: ns0.vartypes.AnalogUnitType | None
    brakeDesignType: ns0.vartypes.MultiStateValueDiscreteType | None
    brakeDutyType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16706", browseName="ns=powertrain;BrakeDutyType", dataType=o6.String)
    )
    brakeEmergencySwitchOffCount: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=17160", browseName="ns=powertrain;BrakeEmergencySwitchOffCount", dataType=o6.Int16)
    )
    brakeHoldingVoltage: ns0.vartypes.AnalogUnitType | None
    brakeInertia: ns0.vartypes.AnalogUnitType | None
    brakeInsulationClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6092", browseName="ns=powertrain;BrakeInsulationClass", dataType=o6.String)
    )
    brakePowerRated: ns0.vartypes.AnalogUnitType | None
    brakeProtectionMechanicalImpact: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16705", browseName="ns=powertrain;BrakeProtectionMechanicalImpact", dataType=o6.String)
    )
    brakeRectifierType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=6378", browseName="ns=powertrain;BrakeRectifierType", dataType=o6.String)
    )
    brakeSurroundingAirTemperature: ns0.vartypes.AnalogUnitType | None
    brakeTorqueHolding: ns0.vartypes.AnalogUnitType | None
    brakeTorqueRated: ns0.vartypes.AnalogUnitType | None
    brakeTurnOffDelayAC: ns0.vartypes.AnalogUnitType | None
    brakeTurnOffDelayDC: ns0.vartypes.AnalogUnitType | None
    brakeTurnOffType: ns0.vartypes.MultiStateValueDiscreteType | None
    brakeTurnOnDelay: ns0.vartypes.AnalogUnitType | None
    brakeType: ns0.vartypes.MultiStateValueDiscreteType
    brakeVibrationClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16704", browseName="ns=powertrain;BrakeVibrationClass", dataType=o6.String)
    )
    brakeVoltageRated: ns0.vartypes.AnalogUnitType | None
    brakeVoltageType: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16673", browseName="ns=powertrain;BrakeVoltageType", dataType=o6.String)
    )
    brakeWearMaximum: ns0.vartypes.AnalogUnitType | None
    brakeWireTerminalCount: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16684", browseName="ns=powertrain;BrakeWireTerminalCount", dataType=o6.Int16)
    )
    brakingEnergySingleEngagementMax: ns0.vartypes.AnalogUnitType | None
    brakingFrequencyOperation: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16675", browseName="ns=powertrain;BrakingFrequencyOperation", dataType=o6.Int32)
    )
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=powertrain;i=6024",
            browseName="DefaultInstanceBrowseName",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("PtBrakeAttributes_01"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    safetyPropertySupported: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=powertrain;i=16612", browseName="ns=powertrain;SafetyPropertySupported", dataType=o6.Boolean)
    )


del Any, TYPE_CHECKING, uuid, o6, di, fx_ac, fx_data, ia, irdi_v1_0_0, machinery, ns0, powertrain_reftypes
