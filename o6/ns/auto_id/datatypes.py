# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Generated OPC UA auto_id namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=auto_id;i=3003", browseName="ns=auto_id;DeviceStatusEnumeration")
class DeviceStatusEnumeration(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    ERROR = o6.enumfield(1, name="Error")
    SCANNING = o6.enumfield(2, name="Scanning")
    BUSY = o6.enumfield(3, name="Busy")


@o6.datatype(nodeId="ns=auto_id;i=3004", browseName="ns=auto_id;Position", defaultEncodingId="ns=auto_id;i=5007")
class Position(ns0.datatypes.Structure):
    positionX: o6.Int32 = o6.field(name="PositionX")
    positionY: o6.Int32 = o6.field(name="PositionY")
    sizeX: o6.Int32 = o6.field(name="SizeX")
    sizeY: o6.Int32 = o6.field(name="SizeY")
    rotation: o6.Int32 = o6.field(name="Rotation")


@o6.datatype(nodeId="ns=auto_id;i=3006", browseName="ns=auto_id;RfidSighting", defaultEncodingId="ns=auto_id;i=5009")
class RfidSighting(ns0.datatypes.Structure):
    antenna: o6.Int32 = o6.field(name="Antenna")
    strength: o6.Int32 = o6.field(name="Strength")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    currentPowerLevel: o6.Int32 = o6.field(name="CurrentPowerLevel")


@o6.enumtype(nodeId="ns=auto_id;i=3009", browseName="ns=auto_id;LocationTypeEnumeration")
class LocationTypeEnumeration(ns0.datatypes.Enumeration):
    NMEA = o6.enumfield(0, name="NMEA")
    LOCAL = o6.enumfield(1, name="LOCAL")
    WGS84 = o6.enumfield(2, name="WGS84")
    NAME = o6.enumfield(3, name="NAME")


@o6.datatype(nodeId="ns=auto_id;i=3010", browseName="ns=auto_id;ScanSettings", defaultEncodingId="ns=auto_id;i=5015")
class ScanSettings(ns0.datatypes.Structure):
    duration: o6.Double = o6.field(name="Duration")
    cycles: o6.Int32 = o6.field(name="Cycles")
    dataAvailable: o6.Boolean = o6.field(name="DataAvailable")
    locationType: LocationTypeEnumeration | None = o6.field(name="LocationType")


@o6.datatype(nodeId="ns=auto_id;i=3011", browseName="ns=auto_id;AntennaNameIdPair", defaultEncodingId="ns=auto_id;i=5017")
class AntennaNameIdPair(ns0.datatypes.Structure):
    antennaId: o6.Int32 = o6.field(name="AntennaId")
    antennaName: o6.String = o6.field(name="AntennaName")


@o6.datatype(nodeId="ns=auto_id;i=3012", browseName="ns=auto_id;NmeaCoordinateString", parent="i=12")
class NmeaCoordinateString:
    pass


@o6.enumtype(nodeId="ns=auto_id;i=3013", browseName="ns=auto_id;AutoIdOperationStatusEnumeration")
class AutoIdOperationStatusEnumeration(ns0.datatypes.Enumeration):
    SUCCESS = o6.enumfield(0, name="SUCCESS")
    MISC_ERROR_TOTAL = o6.enumfield(1, name="MISC_ERROR_TOTAL")
    MISC_ERROR_PARTIAL = o6.enumfield(2, name="MISC_ERROR_PARTIAL")
    PERMISSON_ERROR = o6.enumfield(3, name="PERMISSON_ERROR")
    PASSWORD_ERROR = o6.enumfield(4, name="PASSWORD_ERROR")
    REGION_NOT_FOUND_ERROR = o6.enumfield(5, name="REGION_NOT_FOUND_ERROR")
    OP_NOT_POSSIBLE_ERROR = o6.enumfield(6, name="OP_NOT_POSSIBLE_ERROR")
    OUT_OF_RANGE_ERROR = o6.enumfield(7, name="OUT_OF_RANGE_ERROR")
    NO_IDENTIFIER = o6.enumfield(8, name="NO_IDENTIFIER")
    MULTIPLE_IDENTIFIERS = o6.enumfield(9, name="MULTIPLE_IDENTIFIERS")
    READ_ERROR = o6.enumfield(10, name="READ_ERROR")
    DECODING_ERROR = o6.enumfield(11, name="DECODING_ERROR")
    MATCH_ERROR = o6.enumfield(12, name="MATCH_ERROR")
    CODE_NOT_SUPPORTED = o6.enumfield(13, name="CODE_NOT_SUPPORTED")
    WRITE_ERROR = o6.enumfield(14, name="WRITE_ERROR")
    NOT_SUPPORTED_BY_DEVICE = o6.enumfield(15, name="NOT_SUPPORTED_BY_DEVICE")
    NOT_SUPPORTED_BY_TAG = o6.enumfield(16, name="NOT_SUPPORTED_BY_TAG")
    DEVICE_NOT_READY = o6.enumfield(17, name="DEVICE_NOT_READY")
    INVALID_CONFIGURATION = o6.enumfield(18, name="INVALID_CONFIGURATION")
    RF_COMMUNICATION_ERROR = o6.enumfield(19, name="RF_COMMUNICATION_ERROR")
    DEVICE_FAULT = o6.enumfield(20, name="DEVICE_FAULT")
    TAG_HAS_LOW_BATTERY = o6.enumfield(21, name="TAG_HAS_LOW_BATTERY")


@o6.enumtype(nodeId="ns=auto_id;i=3014", browseName="ns=auto_id;RfidPasswordTypeEnumeration")
class RfidPasswordTypeEnumeration(ns0.datatypes.Enumeration):
    ACCESS = o6.enumfield(0, name="Access")
    KILL = o6.enumfield(1, name="Kill")
    READ = o6.enumfield(2, name="Read")
    WRITE = o6.enumfield(3, name="Write")


@o6.enumtype(nodeId="ns=auto_id;i=3015", browseName="ns=auto_id;RfidLockRegionEnumeration")
class RfidLockRegionEnumeration(ns0.datatypes.Enumeration):
    KILL = o6.enumfield(0, name="Kill")
    ACCESS = o6.enumfield(1, name="Access")
    EPC = o6.enumfield(2, name="EPC")
    TID = o6.enumfield(3, name="TID")
    USER = o6.enumfield(4, name="User")


@o6.enumtype(nodeId="ns=auto_id;i=3016", browseName="ns=auto_id;RfidLockOperationEnumeration")
class RfidLockOperationEnumeration(ns0.datatypes.Enumeration):
    LOCK = o6.enumfield(0, name="Lock")
    UNLOCK = o6.enumfield(1, name="Unlock")
    PERMANENT_LOCK = o6.enumfield(2, name="PermanentLock")
    PERMANENT_UNLOCK = o6.enumfield(3, name="PermanentUnlock")


@o6.datatype(nodeId="ns=auto_id;i=3019", browseName="ns=auto_id;LocalCoordinate", defaultEncodingId="ns=auto_id;i=5028")
class LocalCoordinate(ns0.datatypes.Structure):
    x: o6.Double = o6.field(name="X")
    y: o6.Double = o6.field(name="Y")
    z: o6.Double = o6.field(name="Z")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    dilutionOfPrecision: o6.Double = o6.field(name="DilutionOfPrecision")
    usefulPrecision: o6.Int32 = o6.field(name="UsefulPrecision")


@o6.datatype(nodeId="ns=auto_id;i=3021", browseName="ns=auto_id;LocationName", parent="i=12")
class LocationName:
    pass


@o6.datatype(nodeId="ns=auto_id;i=3023", browseName="ns=auto_id;DhcpGeoConfCoordinate", defaultEncodingId="ns=auto_id;i=5034")
class DhcpGeoConfCoordinate(ns0.datatypes.Structure):
    laRes: o6.Byte = o6.field(name="LaRes")
    latitudeInteger: o6.Int16 = o6.field(name="LatitudeInteger")
    latitudeFraction: o6.Int32 = o6.field(name="LatitudeFraction")
    loRes: o6.Byte = o6.field(name="LoRes")
    longitudeInteger: o6.Int16 = o6.field(name="LongitudeInteger")
    longitudeFraction: o6.Int32 = o6.field(name="LongitudeFraction")
    aT: o6.Byte = o6.field(name="AT")
    altRes: o6.Byte = o6.field(name="AltRes")
    altitudeInteger: o6.Int32 = o6.field(name="AltitudeInteger")
    altitudeFraction: o6.Int16 = o6.field(name="AltitudeFraction")
    datum: o6.Byte = o6.field(name="Datum")


@o6.datatype(nodeId="ns=auto_id;i=3024", browseName="ns=auto_id;ScanDataEpc", defaultEncodingId="ns=auto_id;i=5036")
class ScanDataEpc(ns0.datatypes.Structure):
    pC: o6.UInt16 = o6.field(name="PC")
    uId: o6.ByteString = o6.field(name="UId")
    xPC_W1: o6.UInt16 = o6.field(name="XPC_W1")
    xPC_W2: o6.UInt16 = o6.field(name="XPC_W2")


@o6.datatype(nodeId="ns=auto_id;i=3020", browseName="ns=auto_id;ScanData", defaultEncodingId="ns=auto_id;i=5030")
class ScanData(ns0.datatypes.Union):
    byteString: o6.ByteString = o6.field(name="ByteString")
    string: o6.String = o6.field(name="String")
    epc: ScanDataEpc = o6.field(name="Epc")
    custom: Any = o6.field(name="Custom")


@o6.datatype(nodeId="ns=auto_id;i=3017", browseName="ns=auto_id;AccessResult", description="Result values of an AutoID Identifier access.", defaultEncodingId="ns=auto_id;i=5022")
class AccessResult(ns0.datatypes.Structure):
    codeType: o6.String | None = o6.field(name="CodeType")
    identifier: ScanData | None = o6.field(name="Identifier")
    timestamp: o6.DateTime | None = o6.field(name="Timestamp")


@o6.datatype(
    nodeId="ns=auto_id;i=3018",
    browseName="ns=auto_id;RfidAccessResult",
    description="Additional result values of an Rfid Transponder access.",
    defaultEncodingId="ns=auto_id;i=5024",
)
class RfidAccessResult(AccessResult):
    codeType: o6.String | None = o6.field(name="CodeType")
    identifier: ScanData | None = o6.field(name="Identifier")
    timestamp: o6.DateTime | None = o6.field(name="Timestamp")
    codeTypeRWData: o6.String | None = o6.field(name="CodeTypeRWData")
    rWData: ScanData | None = o6.field(name="RWData")
    antenna: o6.Int32 | None = o6.field(name="Antenna")
    currentPowerLevel: o6.Int32 | None = o6.field(name="CurrentPowerLevel")
    pC: o6.UInt16 | None = o6.field(name="PC")
    polarization: o6.String | None = o6.field(name="Polarization")
    strength: o6.Int32 | None = o6.field(name="Strength")


@o6.datatype(nodeId="ns=auto_id;i=3027", browseName="ns=auto_id;WGS84Coordinate", defaultEncodingId="ns=auto_id;i=5046")
class WGS84Coordinate(ns0.datatypes.Structure):
    n_S_Hemisphere: o6.String = o6.field(name="N/S Hemisphere")
    latitude: o6.Double = o6.field(name="Latitude")
    e_W_Hemisphere: o6.String = o6.field(name="E/W Hemisphere")
    longitude: o6.Double = o6.field(name="Longitude")
    altitude: o6.Double = o6.field(name="Altitude")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    dilutionOfPrecision: o6.Double = o6.field(name="DilutionOfPrecision")
    usefulPrecisionLatLon: o6.Int32 = o6.field(name="UsefulPrecisionLatLon")
    usefulPrecisionAlt: o6.Int32 = o6.field(name="UsefulPrecisionAlt")


@o6.datatype(nodeId="ns=auto_id;i=3008", browseName="ns=auto_id;Location", defaultEncodingId="ns=auto_id;i=5013")
class Location(ns0.datatypes.Union):
    nMEA: o6.String = o6.field(name="NMEA")
    local: LocalCoordinate = o6.field(name="Local")
    wGS84: WGS84Coordinate = o6.field(name="WGS84")
    name: o6.String = o6.field(name="Name")


@o6.datatype(nodeId="ns=auto_id;i=3001", browseName="ns=auto_id;ScanResult", defaultEncodingId="ns=auto_id;i=5002", isAbstract=True)
class ScanResult(ns0.datatypes.Structure):
    codeType: o6.String = o6.field(name="CodeType")
    scanData: ScanData = o6.field(name="ScanData")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    location: Location | None = o6.field(name="Location")


@o6.datatype(nodeId="ns=auto_id;i=3002", browseName="ns=auto_id;OcrScanResult", defaultEncodingId="ns=auto_id;i=5004")
class OcrScanResult(ScanResult):
    codeType: o6.String = o6.field(name="CodeType")
    scanData: ScanData = o6.field(name="ScanData")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    location: Location | None = o6.field(name="Location")
    imageId: o6.NodeId = o6.field(name="ImageId")
    quality: o6.Byte = o6.field(name="Quality")
    position: Position = o6.field(name="Position")
    font: o6.String | None = o6.field(name="Font")
    decodingTime: o6.DateTime | None = o6.field(name="DecodingTime")


@o6.datatype(nodeId="ns=auto_id;i=3007", browseName="ns=auto_id;RfidScanResult", defaultEncodingId="ns=auto_id;i=5011")
class RfidScanResult(ScanResult):
    codeType: o6.String = o6.field(name="CodeType")
    scanData: ScanData = o6.field(name="ScanData")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    location: Location | None = o6.field(name="Location")
    sighting: list[RfidSighting] = o6.field(name="Sighting", arrayDimensions=[0])


@o6.datatype(nodeId="ns=auto_id;i=3026", browseName="ns=auto_id;OpticalScanResult", defaultEncodingId="ns=auto_id;i=5040")
class OpticalScanResult(ScanResult):
    codeType: o6.String = o6.field(name="CodeType")
    scanData: ScanData = o6.field(name="ScanData")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    location: Location | None = o6.field(name="Location")
    grade: o6.Float | None = o6.field(name="Grade")
    position: Position | None = o6.field(name="Position")
    symbology: o6.String | None = o6.field(name="Symbology")
    imageId: o6.NodeId | None = o6.field(name="ImageId")


@o6.datatype(nodeId="ns=auto_id;i=3029", browseName="ns=auto_id;Rotation", defaultEncodingId="ns=auto_id;i=5050")
class Rotation(ns0.datatypes.Structure):
    yaw: o6.Double = o6.field(name="Yaw")
    pitch: o6.Double = o6.field(name="Pitch")
    roll: o6.Double = o6.field(name="Roll")


@o6.datatype(nodeId="ns=auto_id;i=3028", browseName="ns=auto_id;RtlsLocationResult", defaultEncodingId="ns=auto_id;i=5048")
class RtlsLocationResult(ScanResult):
    codeType: o6.String = o6.field(name="CodeType")
    scanData: ScanData = o6.field(name="ScanData")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    location: Location | None = o6.field(name="Location")
    speed: o6.Double = o6.field(name="Speed")
    heading: o6.Double = o6.field(name="Heading")
    rotation: Rotation = o6.field(name="Rotation")
    receiveTime: o6.DateTime = o6.field(name="ReceiveTime")


@o6.datatype(nodeId="ns=auto_id;i=3030", browseName="ns=auto_id;OpticalVerifierScanResult", defaultEncodingId="ns=auto_id;i=5052")
class OpticalVerifierScanResult(OpticalScanResult):
    codeType: o6.String = o6.field(name="CodeType")
    scanData: ScanData = o6.field(name="ScanData")
    timestamp: o6.DateTime = o6.field(name="Timestamp")
    location: Location | None = o6.field(name="Location")
    grade: o6.Float | None = o6.field(name="Grade")
    position: Position | None = o6.field(name="Position")
    symbology: o6.String | None = o6.field(name="Symbology")
    imageId: o6.NodeId | None = o6.field(name="ImageId")
    isoGrade: o6.String = o6.field(name="IsoGrade")
    rMin: o6.Int16 = o6.field(name="RMin")
    symbolContrast: o6.Int16 = o6.field(name="SymbolContrast")
    eCMin: o6.Int16 = o6.field(name="ECMin")
    modulation: o6.Int16 = o6.field(name="Modulation")
    defects: o6.Int16 = o6.field(name="Defects")
    decodability: o6.Int16 = o6.field(name="Decodability")
    decode: o6.Int16 = o6.field(name="Decode")
    printGain: o6.Int16 = o6.field(name="PrintGain")


@o6.datatype(nodeId="ns=auto_id;i=3031", browseName="ns=auto_id;CodeTypeDataType", parent="i=12")
class CodeTypeDataType:
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0
