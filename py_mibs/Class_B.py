# SNMP MIB module (Class_B) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/2001CLB.mib
# Produced by pysmi-1.5.9 at Wed Nov 20 01:53:45 2024
# On host Adams-MacBook-Air-10.local platform Darwin version 23.6.0 by user x-wing
# Using Python version 3.10.12 (main, Jun 20 2023, 19:43:52) [Clang 14.0.3 (clang-1403.0.22.14.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso,
 mgmt) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(DisplayString,) = mibBuilder.importSymbols(
    "TMIB-II",
    "DisplayString")


# MODULE-IDENTITY


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("mandatory")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("mandatory")
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("mandatory")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("mandatory")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")


class _SysServices_Type(Integer32):
    """Custom type sysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SysServices_Type.__name__ = "Integer32"
_SysServices_Object = MibScalar
sysServices = _SysServices_Object(
    (1, 3, 6, 1, 2, 1, 1, 7),
    _SysServices_Type()
)
sysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysServices.setStatus("mandatory")
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 3)
)
_AtTable_Object = MibTable
atTable = _AtTable_Object(
    (1, 3, 6, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atTable.setStatus("deprecated")
_AtEntry_Object = MibTableRow
atEntry = _AtEntry_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1)
)
atEntry.setIndexNames(
    (0, "Class_B", "atIfIndex"),
    (0, "Class_B", "atNetAddress"),
)
if mibBuilder.loadTexts:
    atEntry.setStatus("deprecated")


class _AtIfIndex_Type(Integer32):
    """Custom type atIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtIfIndex_Type.__name__ = "Integer32"
_AtIfIndex_Object = MibTableColumn
atIfIndex = _AtIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 1),
    _AtIfIndex_Type()
)
atIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atIfIndex.setStatus("deprecated")
_AtPhysAddress_Type = PhysAddress
_AtPhysAddress_Object = MibTableColumn
atPhysAddress = _AtPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 2),
    _AtPhysAddress_Type()
)
atPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atPhysAddress.setStatus("deprecated")
_AtNetAddress_Type = IpAddress
_AtNetAddress_Object = MibTableColumn
atNetAddress = _AtNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 3),
    _AtNetAddress_Type()
)
atNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetAddress.setStatus("deprecated")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)
_IpNetToMediaTable_Object = MibTable
ipNetToMediaTable = _IpNetToMediaTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 22)
)
if mibBuilder.loadTexts:
    ipNetToMediaTable.setStatus("mandatory")
_IpNetToMediaEntry_Object = MibTableRow
ipNetToMediaEntry = _IpNetToMediaEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1)
)
ipNetToMediaEntry.setIndexNames(
    (0, "Class_B", "ipNetToMediaIfIndex"),
    (0, "Class_B", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ipNetToMediaEntry.setStatus("mandatory")


class _IpNetToMediaIfIndex_Type(Integer32):
    """Custom type ipNetToMediaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpNetToMediaIfIndex_Type.__name__ = "Integer32"
_IpNetToMediaIfIndex_Object = MibTableColumn
ipNetToMediaIfIndex = _IpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 1),
    _IpNetToMediaIfIndex_Type()
)
ipNetToMediaIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaIfIndex.setStatus("mandatory")
_IpNetToMediaPhysAddress_Type = PhysAddress
_IpNetToMediaPhysAddress_Object = MibTableColumn
ipNetToMediaPhysAddress = _IpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 2),
    _IpNetToMediaPhysAddress_Type()
)
ipNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPhysAddress.setStatus("mandatory")
_IpNetToMediaNetAddress_Type = IpAddress
_IpNetToMediaNetAddress_Object = MibTableColumn
ipNetToMediaNetAddress = _IpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 3),
    _IpNetToMediaNetAddress_Type()
)
ipNetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaNetAddress.setStatus("mandatory")


class _IpNetToMediaType_Type(Integer32):
    """Custom type ipNetToMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4))
    )


_IpNetToMediaType_Type.__name__ = "Integer32"
_IpNetToMediaType_Object = MibTableColumn
ipNetToMediaType = _IpNetToMediaType_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 4),
    _IpNetToMediaType_Type()
)
ipNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaType.setStatus("mandatory")
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Lapb_ObjectIdentity = ObjectIdentity
lapb = _Lapb_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 16)
)
_LapbAdmnTable_Object = MibTable
lapbAdmnTable = _LapbAdmnTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1)
)
if mibBuilder.loadTexts:
    lapbAdmnTable.setStatus("mandatory")
_LapbAdmnEntry_Object = MibTableRow
lapbAdmnEntry = _LapbAdmnEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1)
)
lapbAdmnEntry.setIndexNames(
    (0, "Class_B", "lapbAdmnIndex"),
)
if mibBuilder.loadTexts:
    lapbAdmnEntry.setStatus("mandatory")
_LapbAdmnIndex_Type = IfIndexType
_LapbAdmnIndex_Object = MibTableColumn
lapbAdmnIndex = _LapbAdmnIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 1),
    _LapbAdmnIndex_Type()
)
lapbAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbAdmnIndex.setStatus("mandatory")


class _LapbAdmnT1AckTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT1AckTimer based on PositiveInteger"""
    defaultValue = 3000


_LapbAdmnT1AckTimer_Type.__name__ = "PositiveInteger"
_LapbAdmnT1AckTimer_Object = MibTableColumn
lapbAdmnT1AckTimer = _LapbAdmnT1AckTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 9),
    _LapbAdmnT1AckTimer_Type()
)
lapbAdmnT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT1AckTimer.setStatus("mandatory")


class _LapbAdmnT2AckDelayTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT2AckDelayTimer based on PositiveInteger"""
    defaultValue = 0


_LapbAdmnT2AckDelayTimer_Type.__name__ = "PositiveInteger"
_LapbAdmnT2AckDelayTimer_Object = MibTableColumn
lapbAdmnT2AckDelayTimer = _LapbAdmnT2AckDelayTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 10),
    _LapbAdmnT2AckDelayTimer_Type()
)
lapbAdmnT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT2AckDelayTimer.setStatus("mandatory")


class _LapbAdmnT3DisconnectTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT3DisconnectTimer based on PositiveInteger"""
    defaultValue = 60000


_LapbAdmnT3DisconnectTimer_Type.__name__ = "PositiveInteger"
_LapbAdmnT3DisconnectTimer_Object = MibTableColumn
lapbAdmnT3DisconnectTimer = _LapbAdmnT3DisconnectTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 11),
    _LapbAdmnT3DisconnectTimer_Type()
)
lapbAdmnT3DisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT3DisconnectTimer.setStatus("mandatory")


class _LapbAdmnT4IdleTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT4IdleTimer based on PositiveInteger"""
    defaultValue = 2147483647


_LapbAdmnT4IdleTimer_Type.__name__ = "PositiveInteger"
_LapbAdmnT4IdleTimer_Object = MibTableColumn
lapbAdmnT4IdleTimer = _LapbAdmnT4IdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 12),
    _LapbAdmnT4IdleTimer_Type()
)
lapbAdmnT4IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT4IdleTimer.setStatus("mandatory")
_LapbOperTable_Object = MibTable
lapbOperTable = _LapbOperTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2)
)
if mibBuilder.loadTexts:
    lapbOperTable.setStatus("mandatory")
_LapbOperEntry_Object = MibTableRow
lapbOperEntry = _LapbOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1)
)
lapbOperEntry.setIndexNames(
    (0, "Class_B", "lapbOperIndex"),
)
if mibBuilder.loadTexts:
    lapbOperEntry.setStatus("mandatory")
_LapbOperIndex_Type = IfIndexType
_LapbOperIndex_Object = MibTableColumn
lapbOperIndex = _LapbOperIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 1),
    _LapbOperIndex_Type()
)
lapbOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperIndex.setStatus("mandatory")
_LapbOperTransmitN1FrameSize_Type = PositiveInteger
_LapbOperTransmitN1FrameSize_Object = MibTableColumn
lapbOperTransmitN1FrameSize = _LapbOperTransmitN1FrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 4),
    _LapbOperTransmitN1FrameSize_Type()
)
lapbOperTransmitN1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperTransmitN1FrameSize.setStatus("mandatory")
_LapbOperReceiveN1FrameSize_Type = PositiveInteger
_LapbOperReceiveN1FrameSize_Object = MibTableColumn
lapbOperReceiveN1FrameSize = _LapbOperReceiveN1FrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 5),
    _LapbOperReceiveN1FrameSize_Type()
)
lapbOperReceiveN1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperReceiveN1FrameSize.setStatus("mandatory")
_LapbOperPortId_Type = ObjectIdentifier
_LapbOperPortId_Object = MibTableColumn
lapbOperPortId = _LapbOperPortId_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 13),
    _LapbOperPortId_Type()
)
lapbOperPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperPortId.setStatus("mandatory")
_Rs232_ObjectIdentity = ObjectIdentity
rs232 = _Rs232_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 33)
)
_Rs232Number_Type = Integer32
_Rs232Number_Object = MibScalar
rs232Number = _Rs232Number_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 1),
    _Rs232Number_Type()
)
rs232Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232Number.setStatus("mandatory")
_Rs232PortTable_Object = MibTable
rs232PortTable = _Rs232PortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2)
)
if mibBuilder.loadTexts:
    rs232PortTable.setStatus("mandatory")
_Rs232PortEntry_Object = MibTableRow
rs232PortEntry = _Rs232PortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1)
)
rs232PortEntry.setIndexNames(
    (0, "Class_B", "rs232PortIndex"),
)
if mibBuilder.loadTexts:
    rs232PortEntry.setStatus("mandatory")


class _Rs232PortIndex_Type(Integer32):
    """Custom type rs232PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Rs232PortIndex_Type.__name__ = "Integer32"
_Rs232PortIndex_Object = MibTableColumn
rs232PortIndex = _Rs232PortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 1),
    _Rs232PortIndex_Type()
)
rs232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortIndex.setStatus("mandatory")


class _Rs232PortType_Type(Integer32):
    """Custom type rs232PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs423", 4),
          ("v35", 5))
    )


_Rs232PortType_Type.__name__ = "Integer32"
_Rs232PortType_Object = MibTableColumn
rs232PortType = _Rs232PortType_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 2),
    _Rs232PortType_Type()
)
rs232PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortType.setStatus("mandatory")
_Rs232PortInSpeed_Type = Integer32
_Rs232PortInSpeed_Object = MibTableColumn
rs232PortInSpeed = _Rs232PortInSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 5),
    _Rs232PortInSpeed_Type()
)
rs232PortInSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortInSpeed.setStatus("mandatory")
_Rs232PortOutSpeed_Type = Integer32
_Rs232PortOutSpeed_Object = MibTableColumn
rs232PortOutSpeed = _Rs232PortOutSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 6),
    _Rs232PortOutSpeed_Type()
)
rs232PortOutSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortOutSpeed.setStatus("mandatory")
_Rs232AsyncPortTable_Object = MibTable
rs232AsyncPortTable = _Rs232AsyncPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3)
)
if mibBuilder.loadTexts:
    rs232AsyncPortTable.setStatus("mandatory")
_Rs232AsyncPortEntry_Object = MibTableRow
rs232AsyncPortEntry = _Rs232AsyncPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1)
)
rs232AsyncPortEntry.setIndexNames(
    (0, "Class_B", "rs232AsyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232AsyncPortEntry.setStatus("mandatory")


class _Rs232AsyncPortIndex_Type(Integer32):
    """Custom type rs232AsyncPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Rs232AsyncPortIndex_Type.__name__ = "Integer32"
_Rs232AsyncPortIndex_Object = MibTableColumn
rs232AsyncPortIndex = _Rs232AsyncPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 1),
    _Rs232AsyncPortIndex_Type()
)
rs232AsyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortIndex.setStatus("mandatory")
_Rs232AsyncPortFramingErrs_Type = Counter32
_Rs232AsyncPortFramingErrs_Object = MibTableColumn
rs232AsyncPortFramingErrs = _Rs232AsyncPortFramingErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 7),
    _Rs232AsyncPortFramingErrs_Type()
)
rs232AsyncPortFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortFramingErrs.setStatus("mandatory")
_Rs232AsyncPortOverrunErrs_Type = Counter32
_Rs232AsyncPortOverrunErrs_Object = MibTableColumn
rs232AsyncPortOverrunErrs = _Rs232AsyncPortOverrunErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 8),
    _Rs232AsyncPortOverrunErrs_Type()
)
rs232AsyncPortOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortOverrunErrs.setStatus("mandatory")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_SnmpInPkts_Type = Counter32
_SnmpInPkts_Object = MibScalar
snmpInPkts = _SnmpInPkts_Object(
    (1, 3, 6, 1, 2, 1, 11, 1),
    _SnmpInPkts_Type()
)
snmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInPkts.setStatus("mandatory")
_SnmpOutPkts_Type = Counter32
_SnmpOutPkts_Object = MibScalar
snmpOutPkts = _SnmpOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 11, 2),
    _SnmpOutPkts_Type()
)
snmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutPkts.setStatus("mandatory")
_SnmpInBadVersions_Type = Counter32
_SnmpInBadVersions_Object = MibScalar
snmpInBadVersions = _SnmpInBadVersions_Object(
    (1, 3, 6, 1, 2, 1, 11, 3),
    _SnmpInBadVersions_Type()
)
snmpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadVersions.setStatus("mandatory")
_SnmpInBadCommunityNames_Type = Counter32
_SnmpInBadCommunityNames_Object = MibScalar
snmpInBadCommunityNames = _SnmpInBadCommunityNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 4),
    _SnmpInBadCommunityNames_Type()
)
snmpInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadCommunityNames.setStatus("mandatory")
_SnmpInBadCommunityUses_Type = Counter32
_SnmpInBadCommunityUses_Object = MibScalar
snmpInBadCommunityUses = _SnmpInBadCommunityUses_Object(
    (1, 3, 6, 1, 2, 1, 11, 5),
    _SnmpInBadCommunityUses_Type()
)
snmpInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadCommunityUses.setStatus("mandatory")
_SnmpInASNParseErrs_Type = Counter32
_SnmpInASNParseErrs_Object = MibScalar
snmpInASNParseErrs = _SnmpInASNParseErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 6),
    _SnmpInASNParseErrs_Type()
)
snmpInASNParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInASNParseErrs.setStatus("mandatory")
_SnmpInTooBigs_Type = Counter32
_SnmpInTooBigs_Object = MibScalar
snmpInTooBigs = _SnmpInTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 11, 8),
    _SnmpInTooBigs_Type()
)
snmpInTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTooBigs.setStatus("mandatory")
_SnmpInNoSuchNames_Type = Counter32
_SnmpInNoSuchNames_Object = MibScalar
snmpInNoSuchNames = _SnmpInNoSuchNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 9),
    _SnmpInNoSuchNames_Type()
)
snmpInNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInNoSuchNames.setStatus("mandatory")
_SnmpInBadValues_Type = Counter32
_SnmpInBadValues_Object = MibScalar
snmpInBadValues = _SnmpInBadValues_Object(
    (1, 3, 6, 1, 2, 1, 11, 10),
    _SnmpInBadValues_Type()
)
snmpInBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadValues.setStatus("mandatory")
_SnmpInReadOnlys_Type = Counter32
_SnmpInReadOnlys_Object = MibScalar
snmpInReadOnlys = _SnmpInReadOnlys_Object(
    (1, 3, 6, 1, 2, 1, 11, 11),
    _SnmpInReadOnlys_Type()
)
snmpInReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInReadOnlys.setStatus("mandatory")
_SnmpInGenErrs_Type = Counter32
_SnmpInGenErrs_Object = MibScalar
snmpInGenErrs = _SnmpInGenErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 12),
    _SnmpInGenErrs_Type()
)
snmpInGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGenErrs.setStatus("mandatory")
_SnmpInGetRequests_Type = Counter32
_SnmpInGetRequests_Object = MibScalar
snmpInGetRequests = _SnmpInGetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 15),
    _SnmpInGetRequests_Type()
)
snmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetRequests.setStatus("mandatory")
_SnmpInGetNexts_Type = Counter32
_SnmpInGetNexts_Object = MibScalar
snmpInGetNexts = _SnmpInGetNexts_Object(
    (1, 3, 6, 1, 2, 1, 11, 16),
    _SnmpInGetNexts_Type()
)
snmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetNexts.setStatus("mandatory")
_SnmpInSetRequests_Type = Counter32
_SnmpInSetRequests_Object = MibScalar
snmpInSetRequests = _SnmpInSetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 17),
    _SnmpInSetRequests_Type()
)
snmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInSetRequests.setStatus("mandatory")
_SnmpInGetResponses_Type = Counter32
_SnmpInGetResponses_Object = MibScalar
snmpInGetResponses = _SnmpInGetResponses_Object(
    (1, 3, 6, 1, 2, 1, 11, 18),
    _SnmpInGetResponses_Type()
)
snmpInGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetResponses.setStatus("mandatory")
_SnmpInTraps_Type = Counter32
_SnmpInTraps_Object = MibScalar
snmpInTraps = _SnmpInTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 19),
    _SnmpInTraps_Type()
)
snmpInTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTraps.setStatus("mandatory")
_SnmpOutTooBigs_Type = Counter32
_SnmpOutTooBigs_Object = MibScalar
snmpOutTooBigs = _SnmpOutTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 11, 20),
    _SnmpOutTooBigs_Type()
)
snmpOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutTooBigs.setStatus("mandatory")
_SnmpOutNoSuchNames_Type = Counter32
_SnmpOutNoSuchNames_Object = MibScalar
snmpOutNoSuchNames = _SnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 21),
    _SnmpOutNoSuchNames_Type()
)
snmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutNoSuchNames.setStatus("mandatory")
_SnmpOutBadValues_Type = Counter32
_SnmpOutBadValues_Object = MibScalar
snmpOutBadValues = _SnmpOutBadValues_Object(
    (1, 3, 6, 1, 2, 1, 11, 22),
    _SnmpOutBadValues_Type()
)
snmpOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutBadValues.setStatus("mandatory")
_SnmpOutGenErrs_Type = Counter32
_SnmpOutGenErrs_Object = MibScalar
snmpOutGenErrs = _SnmpOutGenErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 24),
    _SnmpOutGenErrs_Type()
)
snmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGenErrs.setStatus("mandatory")
_SnmpOutGetRequests_Type = Counter32
_SnmpOutGetRequests_Object = MibScalar
snmpOutGetRequests = _SnmpOutGetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 25),
    _SnmpOutGetRequests_Type()
)
snmpOutGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetRequests.setStatus("mandatory")
_SnmpOutGetNexts_Type = Counter32
_SnmpOutGetNexts_Object = MibScalar
snmpOutGetNexts = _SnmpOutGetNexts_Object(
    (1, 3, 6, 1, 2, 1, 11, 26),
    _SnmpOutGetNexts_Type()
)
snmpOutGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetNexts.setStatus("mandatory")
_SnmpOutSetRequests_Type = Counter32
_SnmpOutSetRequests_Object = MibScalar
snmpOutSetRequests = _SnmpOutSetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 27),
    _SnmpOutSetRequests_Type()
)
snmpOutSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutSetRequests.setStatus("mandatory")
_SnmpOutGetResponses_Type = Counter32
_SnmpOutGetResponses_Object = MibScalar
snmpOutGetResponses = _SnmpOutGetResponses_Object(
    (1, 3, 6, 1, 2, 1, 11, 28),
    _SnmpOutGetResponses_Type()
)
snmpOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetResponses.setStatus("mandatory")
_SnmpOutTraps_Type = Counter32
_SnmpOutTraps_Object = MibScalar
snmpOutTraps = _SnmpOutTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 29),
    _SnmpOutTraps_Type()
)
snmpOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutTraps.setStatus("mandatory")


class _SnmpEnableAuthenTraps_Type(Integer32):
    """Custom type snmpEnableAuthenTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpEnableAuthenTraps_Type.__name__ = "Integer32"
_SnmpEnableAuthenTraps_Object = MibScalar
snmpEnableAuthenTraps = _SnmpEnableAuthenTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 30),
    _SnmpEnableAuthenTraps_Type()
)
snmpEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnableAuthenTraps.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Class_B",
    **{"PhysAddress": PhysAddress,
       "PositiveInteger": PositiveInteger,
       "IfIndexType": IfIndexType,
       "mib-2": mib_2,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysServices": sysServices,
       "at": at,
       "atTable": atTable,
       "atEntry": atEntry,
       "atIfIndex": atIfIndex,
       "atPhysAddress": atPhysAddress,
       "atNetAddress": atNetAddress,
       "ip": ip,
       "ipNetToMediaTable": ipNetToMediaTable,
       "ipNetToMediaEntry": ipNetToMediaEntry,
       "ipNetToMediaIfIndex": ipNetToMediaIfIndex,
       "ipNetToMediaPhysAddress": ipNetToMediaPhysAddress,
       "ipNetToMediaNetAddress": ipNetToMediaNetAddress,
       "ipNetToMediaType": ipNetToMediaType,
       "transmission": transmission,
       "lapb": lapb,
       "lapbAdmnTable": lapbAdmnTable,
       "lapbAdmnEntry": lapbAdmnEntry,
       "lapbAdmnIndex": lapbAdmnIndex,
       "lapbAdmnT1AckTimer": lapbAdmnT1AckTimer,
       "lapbAdmnT2AckDelayTimer": lapbAdmnT2AckDelayTimer,
       "lapbAdmnT3DisconnectTimer": lapbAdmnT3DisconnectTimer,
       "lapbAdmnT4IdleTimer": lapbAdmnT4IdleTimer,
       "lapbOperTable": lapbOperTable,
       "lapbOperEntry": lapbOperEntry,
       "lapbOperIndex": lapbOperIndex,
       "lapbOperTransmitN1FrameSize": lapbOperTransmitN1FrameSize,
       "lapbOperReceiveN1FrameSize": lapbOperReceiveN1FrameSize,
       "lapbOperPortId": lapbOperPortId,
       "rs232": rs232,
       "rs232Number": rs232Number,
       "rs232PortTable": rs232PortTable,
       "rs232PortEntry": rs232PortEntry,
       "rs232PortIndex": rs232PortIndex,
       "rs232PortType": rs232PortType,
       "rs232PortInSpeed": rs232PortInSpeed,
       "rs232PortOutSpeed": rs232PortOutSpeed,
       "rs232AsyncPortTable": rs232AsyncPortTable,
       "rs232AsyncPortEntry": rs232AsyncPortEntry,
       "rs232AsyncPortIndex": rs232AsyncPortIndex,
       "rs232AsyncPortFramingErrs": rs232AsyncPortFramingErrs,
       "rs232AsyncPortOverrunErrs": rs232AsyncPortOverrunErrs,
       "snmp": snmp,
       "snmpInPkts": snmpInPkts,
       "snmpOutPkts": snmpOutPkts,
       "snmpInBadVersions": snmpInBadVersions,
       "snmpInBadCommunityNames": snmpInBadCommunityNames,
       "snmpInBadCommunityUses": snmpInBadCommunityUses,
       "snmpInASNParseErrs": snmpInASNParseErrs,
       "snmpInTooBigs": snmpInTooBigs,
       "snmpInNoSuchNames": snmpInNoSuchNames,
       "snmpInBadValues": snmpInBadValues,
       "snmpInReadOnlys": snmpInReadOnlys,
       "snmpInGenErrs": snmpInGenErrs,
       "snmpInGetRequests": snmpInGetRequests,
       "snmpInGetNexts": snmpInGetNexts,
       "snmpInSetRequests": snmpInSetRequests,
       "snmpInGetResponses": snmpInGetResponses,
       "snmpInTraps": snmpInTraps,
       "snmpOutTooBigs": snmpOutTooBigs,
       "snmpOutNoSuchNames": snmpOutNoSuchNames,
       "snmpOutBadValues": snmpOutBadValues,
       "snmpOutGenErrs": snmpOutGenErrs,
       "snmpOutGetRequests": snmpOutGetRequests,
       "snmpOutGetNexts": snmpOutGetNexts,
       "snmpOutSetRequests": snmpOutSetRequests,
       "snmpOutGetResponses": snmpOutGetResponses,
       "snmpOutTraps": snmpOutTraps,
       "snmpEnableAuthenTraps": snmpEnableAuthenTraps}
)
