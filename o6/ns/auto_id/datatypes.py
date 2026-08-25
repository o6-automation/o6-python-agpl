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


@o6.enumtype(nodeId="ns=auto_id;i=3003", browseName="DeviceStatusEnumeration")
class DeviceStatusEnumeration(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    ERROR = o6.enumfield(1, name="Error")
    SCANNING = o6.enumfield(2, name="Scanning")
    BUSY = o6.enumfield(3, name="Busy")


@o6.datatype(nodeId="ns=auto_id;i=3004", browseName="Position", defaultEncodingId="ns=auto_id;i=5007")
class Position(ns0.datatypes.Structure):
    positionX: o6.Int32
    positionY: o6.Int32
    sizeX: o6.Int32
    sizeY: o6.Int32
    rotation: o6.Int32


@o6.datatype(nodeId="ns=auto_id;i=3006", browseName="RfidSighting", defaultEncodingId="ns=auto_id;i=5009")
class RfidSighting(ns0.datatypes.Structure):
    antenna: o6.Int32
    strength: o6.Int32
    timestamp: o6.DateTime
    currentPowerLevel: o6.Int32


@o6.enumtype(nodeId="ns=auto_id;i=3009", browseName="LocationTypeEnumeration")
class LocationTypeEnumeration(ns0.datatypes.Enumeration):
    NMEA = o6.enumfield(0, name="NMEA")
    LOCAL = o6.enumfield(1, name="LOCAL")
    WGS84 = o6.enumfield(2, name="WGS84")
    NAME = o6.enumfield(3, name="NAME")


@o6.datatype(nodeId="ns=auto_id;i=3010", browseName="ScanSettings", defaultEncodingId="ns=auto_id;i=5015")
class ScanSettings(ns0.datatypes.Structure):
    duration: o6.Double
    cycles: o6.Int32
    dataAvailable: o6.Boolean
    locationType: LocationTypeEnumeration | None


@o6.datatype(nodeId="ns=auto_id;i=3011", browseName="AntennaNameIdPair", defaultEncodingId="ns=auto_id;i=5017")
class AntennaNameIdPair(ns0.datatypes.Structure):
    antennaId: o6.Int32
    antennaName: o6.String


@o6.datatype(nodeId="ns=auto_id;i=3012", browseName="NmeaCoordinateString", parent="i=12")
class NmeaCoordinateString:
    pass


@o6.enumtype(nodeId="ns=auto_id;i=3013", browseName="AutoIdOperationStatusEnumeration")
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


@o6.enumtype(nodeId="ns=auto_id;i=3014", browseName="RfidPasswordTypeEnumeration")
class RfidPasswordTypeEnumeration(ns0.datatypes.Enumeration):
    ACCESS = o6.enumfield(0, name="Access")
    KILL = o6.enumfield(1, name="Kill")
    READ = o6.enumfield(2, name="Read")
    WRITE = o6.enumfield(3, name="Write")


@o6.enumtype(nodeId="ns=auto_id;i=3015", browseName="RfidLockRegionEnumeration")
class RfidLockRegionEnumeration(ns0.datatypes.Enumeration):
    KILL = o6.enumfield(0, name="Kill")
    ACCESS = o6.enumfield(1, name="Access")
    EPC = o6.enumfield(2, name="EPC")
    TID = o6.enumfield(3, name="TID")
    USER = o6.enumfield(4, name="User")


@o6.enumtype(nodeId="ns=auto_id;i=3016", browseName="RfidLockOperationEnumeration")
class RfidLockOperationEnumeration(ns0.datatypes.Enumeration):
    LOCK = o6.enumfield(0, name="Lock")
    UNLOCK = o6.enumfield(1, name="Unlock")
    PERMANENT_LOCK = o6.enumfield(2, name="PermanentLock")
    PERMANENT_UNLOCK = o6.enumfield(3, name="PermanentUnlock")


@o6.datatype(nodeId="ns=auto_id;i=3019", browseName="LocalCoordinate", defaultEncodingId="ns=auto_id;i=5028")
class LocalCoordinate(ns0.datatypes.Structure):
    x: o6.Double
    y: o6.Double
    z: o6.Double
    timestamp: o6.DateTime
    dilutionOfPrecision: o6.Double
    usefulPrecision: o6.Int32


@o6.datatype(nodeId="ns=auto_id;i=3021", browseName="LocationName", parent="i=12")
class LocationName:
    pass


@o6.datatype(nodeId="ns=auto_id;i=3023", browseName="DhcpGeoConfCoordinate", defaultEncodingId="ns=auto_id;i=5034")
class DhcpGeoConfCoordinate(ns0.datatypes.Structure):
    laRes: o6.Byte
    latitudeInteger: o6.Int16
    latitudeFraction: o6.Int32
    loRes: o6.Byte
    longitudeInteger: o6.Int16
    longitudeFraction: o6.Int32
    aT: o6.Byte
    altRes: o6.Byte
    altitudeInteger: o6.Int32
    altitudeFraction: o6.Int16
    datum: o6.Byte


@o6.datatype(nodeId="ns=auto_id;i=3024", browseName="ScanDataEpc", defaultEncodingId="ns=auto_id;i=5036")
class ScanDataEpc(ns0.datatypes.Structure):
    pC: o6.UInt16
    uId: o6.ByteString
    xPC_W1: o6.UInt16
    xPC_W2: o6.UInt16


@o6.datatype(nodeId="ns=auto_id;i=3020", browseName="ScanData", defaultEncodingId="ns=auto_id;i=5030")
class ScanData(ns0.datatypes.Union):
    byteString: o6.ByteString
    string: o6.String
    epc: ScanDataEpc
    custom: Any


@o6.datatype(nodeId="ns=auto_id;i=3017", browseName="AccessResult", description="Result values of an AutoID Identifier access.", defaultEncodingId="ns=auto_id;i=5022")
class AccessResult(ns0.datatypes.Structure):
    codeType: o6.String | None
    identifier: ScanData | None
    timestamp: o6.DateTime | None


@o6.datatype(
    nodeId="ns=auto_id;i=3018", browseName="RfidAccessResult", description="Additional result values of an Rfid Transponder access.", defaultEncodingId="ns=auto_id;i=5024"
)
class RfidAccessResult(AccessResult):
    codeType: o6.String | None
    identifier: ScanData | None
    timestamp: o6.DateTime | None
    codeTypeRWData: o6.String | None
    rWData: ScanData | None
    antenna: o6.Int32 | None
    currentPowerLevel: o6.Int32 | None
    pC: o6.UInt16 | None
    polarization: o6.String | None
    strength: o6.Int32 | None


@o6.datatype(nodeId="ns=auto_id;i=3027", browseName="WGS84Coordinate", defaultEncodingId="ns=auto_id;i=5046")
class WGS84Coordinate(ns0.datatypes.Structure):
    n_S_Hemisphere: o6.String
    latitude: o6.Double
    e_W_Hemisphere: o6.String
    longitude: o6.Double
    altitude: o6.Double
    timestamp: o6.DateTime
    dilutionOfPrecision: o6.Double
    usefulPrecisionLatLon: o6.Int32
    usefulPrecisionAlt: o6.Int32


@o6.datatype(nodeId="ns=auto_id;i=3008", browseName="Location", defaultEncodingId="ns=auto_id;i=5013")
class Location(ns0.datatypes.Union):
    nMEA: o6.String
    local: LocalCoordinate
    wGS84: WGS84Coordinate
    name: o6.String


@o6.datatype(nodeId="ns=auto_id;i=3001", browseName="ScanResult", defaultEncodingId="ns=auto_id;i=5002", isAbstract=True)
class ScanResult(ns0.datatypes.Structure):
    codeType: o6.String
    scanData: ScanData
    timestamp: o6.DateTime
    location: Location | None


@o6.datatype(nodeId="ns=auto_id;i=3002", browseName="OcrScanResult", defaultEncodingId="ns=auto_id;i=5004")
class OcrScanResult(ScanResult):
    codeType: o6.String
    scanData: ScanData
    timestamp: o6.DateTime
    location: Location | None
    imageId: o6.NodeId
    quality: o6.Byte
    position: Position
    font: o6.String | None
    decodingTime: o6.DateTime | None


@o6.datatype(nodeId="ns=auto_id;i=3007", browseName="RfidScanResult", defaultEncodingId="ns=auto_id;i=5011")
class RfidScanResult(ScanResult):
    codeType: o6.String
    scanData: ScanData
    timestamp: o6.DateTime
    location: Location | None
    sighting: list[RfidSighting]


@o6.datatype(nodeId="ns=auto_id;i=3026", browseName="OpticalScanResult", defaultEncodingId="ns=auto_id;i=5040")
class OpticalScanResult(ScanResult):
    codeType: o6.String
    scanData: ScanData
    timestamp: o6.DateTime
    location: Location | None
    grade: o6.Float | None
    position: Position | None
    symbology: o6.String | None
    imageId: o6.NodeId | None


@o6.datatype(nodeId="ns=auto_id;i=3029", browseName="Rotation", defaultEncodingId="ns=auto_id;i=5050")
class Rotation(ns0.datatypes.Structure):
    yaw: o6.Double
    pitch: o6.Double
    roll: o6.Double


@o6.datatype(nodeId="ns=auto_id;i=3028", browseName="RtlsLocationResult", defaultEncodingId="ns=auto_id;i=5048")
class RtlsLocationResult(ScanResult):
    codeType: o6.String
    scanData: ScanData
    timestamp: o6.DateTime
    location: Location | None
    speed: o6.Double
    heading: o6.Double
    rotation: Rotation
    receiveTime: o6.DateTime


@o6.datatype(nodeId="ns=auto_id;i=3030", browseName="OpticalVerifierScanResult", defaultEncodingId="ns=auto_id;i=5052")
class OpticalVerifierScanResult(OpticalScanResult):
    codeType: o6.String
    scanData: ScanData
    timestamp: o6.DateTime
    location: Location | None
    grade: o6.Float | None
    position: Position | None
    symbology: o6.String | None
    imageId: o6.NodeId | None
    isoGrade: o6.String
    rMin: o6.Int16
    symbolContrast: o6.Int16
    eCMin: o6.Int16
    modulation: o6.Int16
    defects: o6.Int16
    decodability: o6.Int16
    decode: o6.Int16
    printGain: o6.Int16


@o6.datatype(nodeId="ns=auto_id;i=3031", browseName="CodeTypeDataType", parent="i=12")
class CodeTypeDataType:
    pass


del Any, TYPE_CHECKING, uuid, o6, di, ns0
