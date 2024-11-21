# SNMP MIB module (TMIB-II) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1101TMIB.mib
# Produced by pysmi-1.5.9 at Wed Nov 20 01:53:44 2024
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

(transportation,) = mibBuilder.importSymbols(
    "NEMA_SMI",
    "transportation")

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
 iso) = mibBuilder.importSymbols(
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Byte(Integer32):
    """Custom type Byte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )





class UByte(Integer32):
    """Custom type UByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Short(Integer32):
    """Custom type Short based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )





class UShort(Integer32):
    """Custom type UShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class Long(Integer32):
    """Custom type Long based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )





class ULong(Integer32):
    """Custom type ULong based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class ConfigEntryStatus(Integer32):
    """Custom type ConfigEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("underCreation", 2),
          ("invalid", 3))
    )





class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("underCreation", 2),
          ("invalid", 3))
    )





class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1)
)
_Layers_ObjectIdentity = ObjectIdentity
layers = _Layers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1)
)
_Profiles_ObjectIdentity = ObjectIdentity
profiles = _Profiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2)
)
_DynObjMgmt_ObjectIdentity = ObjectIdentity
dynObjMgmt = _DynObjMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3)
)
_DynObjDef_Object = MibTable
dynObjDef = _DynObjDef_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dynObjDef.setStatus("mandatory")
_DynObjEntry_Object = MibTableRow
dynObjEntry = _DynObjEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1, 1)
)
dynObjEntry.setIndexNames(
    (0, "TMIB-II", "dynObjNumber"),
    (0, "TMIB-II", "dynObjIndex"),
)
if mibBuilder.loadTexts:
    dynObjEntry.setStatus("mandatory")


class _DynObjNumber_Type(Integer32):
    """Custom type dynObjNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_DynObjNumber_Type.__name__ = "Integer32"
_DynObjNumber_Object = MibTableColumn
dynObjNumber = _DynObjNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1, 1, 1),
    _DynObjNumber_Type()
)
dynObjNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynObjNumber.setStatus("mandatory")


class _DynObjIndex_Type(Integer32):
    """Custom type dynObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DynObjIndex_Type.__name__ = "Integer32"
_DynObjIndex_Object = MibTableColumn
dynObjIndex = _DynObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1, 1, 2),
    _DynObjIndex_Type()
)
dynObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynObjIndex.setStatus("mandatory")
_DynObjVariable_Type = ObjectIdentifier
_DynObjVariable_Object = MibTableColumn
dynObjVariable = _DynObjVariable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1, 1, 3),
    _DynObjVariable_Type()
)
dynObjVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObjVariable.setStatus("mandatory")
_DynObjOwner_Type = OwnerString
_DynObjOwner_Object = MibTableColumn
dynObjOwner = _DynObjOwner_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1, 1, 4),
    _DynObjOwner_Type()
)
dynObjOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObjOwner.setStatus("deprecated")
_DynObjStatus_Type = EntryStatus
_DynObjStatus_Object = MibTableColumn
dynObjStatus = _DynObjStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 1, 1, 5),
    _DynObjStatus_Type()
)
dynObjStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObjStatus.setStatus("deprecated")
_DynObjData_ObjectIdentity = ObjectIdentity
dynObjData = _DynObjData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2)
)
_DynObj1_Type = OctetString
_DynObj1_Object = MibScalar
dynObj1 = _DynObj1_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 1),
    _DynObj1_Type()
)
dynObj1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj1.setStatus("deprecated")
_DynObj2_Type = OctetString
_DynObj2_Object = MibScalar
dynObj2 = _DynObj2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 2),
    _DynObj2_Type()
)
dynObj2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj2.setStatus("deprecated")
_DynObj3_Type = OctetString
_DynObj3_Object = MibScalar
dynObj3 = _DynObj3_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 3),
    _DynObj3_Type()
)
dynObj3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj3.setStatus("deprecated")
_DynObj4_Type = OctetString
_DynObj4_Object = MibScalar
dynObj4 = _DynObj4_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 4),
    _DynObj4_Type()
)
dynObj4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj4.setStatus("deprecated")
_DynObj5_Type = OctetString
_DynObj5_Object = MibScalar
dynObj5 = _DynObj5_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 5),
    _DynObj5_Type()
)
dynObj5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj5.setStatus("deprecated")
_DynObj6_Type = OctetString
_DynObj6_Object = MibScalar
dynObj6 = _DynObj6_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 6),
    _DynObj6_Type()
)
dynObj6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj6.setStatus("deprecated")
_DynObj7_Type = OctetString
_DynObj7_Object = MibScalar
dynObj7 = _DynObj7_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 7),
    _DynObj7_Type()
)
dynObj7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj7.setStatus("deprecated")
_DynObj8_Type = OctetString
_DynObj8_Object = MibScalar
dynObj8 = _DynObj8_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 8),
    _DynObj8_Type()
)
dynObj8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj8.setStatus("deprecated")
_DynObj9_Type = OctetString
_DynObj9_Object = MibScalar
dynObj9 = _DynObj9_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 9),
    _DynObj9_Type()
)
dynObj9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj9.setStatus("deprecated")
_DynObj10_Type = OctetString
_DynObj10_Object = MibScalar
dynObj10 = _DynObj10_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 10),
    _DynObj10_Type()
)
dynObj10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj10.setStatus("deprecated")
_DynObj11_Type = OctetString
_DynObj11_Object = MibScalar
dynObj11 = _DynObj11_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 11),
    _DynObj11_Type()
)
dynObj11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj11.setStatus("deprecated")
_DynObj12_Type = OctetString
_DynObj12_Object = MibScalar
dynObj12 = _DynObj12_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 12),
    _DynObj12_Type()
)
dynObj12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj12.setStatus("deprecated")
_DynObj13_Type = OctetString
_DynObj13_Object = MibScalar
dynObj13 = _DynObj13_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 2, 13),
    _DynObj13_Type()
)
dynObj13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObj13.setStatus("deprecated")
_DynObjConfig_ObjectIdentity = ObjectIdentity
dynObjConfig = _DynObjConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 3)
)
_DynObjConfigTable_Object = MibTable
dynObjConfigTable = _DynObjConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dynObjConfigTable.setStatus("mandatory")
_DynObjConfigEntry_Object = MibTableRow
dynObjConfigEntry = _DynObjConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 3, 1, 1)
)
dynObjConfigEntry.setIndexNames(
    (0, "TMIB-II", "dynObjNumber"),
)
if mibBuilder.loadTexts:
    dynObjConfigEntry.setStatus("mandatory")
_DynObjConfigOwner_Type = OwnerString
_DynObjConfigOwner_Object = MibTableColumn
dynObjConfigOwner = _DynObjConfigOwner_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 3, 1, 1, 1),
    _DynObjConfigOwner_Type()
)
dynObjConfigOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObjConfigOwner.setStatus("mandatory")
_DynObjConfigStatus_Type = ConfigEntryStatus
_DynObjConfigStatus_Object = MibTableColumn
dynObjConfigStatus = _DynObjConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 3, 3, 1, 1, 2),
    _DynObjConfigStatus_Type()
)
dynObjConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynObjConfigStatus.setStatus("mandatory")
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TMIB-II",
    **{"DisplayString": DisplayString,
       "Byte": Byte,
       "UByte": UByte,
       "Short": Short,
       "UShort": UShort,
       "Long": Long,
       "ULong": ULong,
       "ConfigEntryStatus": ConfigEntryStatus,
       "EntryStatus": EntryStatus,
       "OwnerString": OwnerString,
       "protocols": protocols,
       "layers": layers,
       "profiles": profiles,
       "dynObjMgmt": dynObjMgmt,
       "dynObjDef": dynObjDef,
       "dynObjEntry": dynObjEntry,
       "dynObjNumber": dynObjNumber,
       "dynObjIndex": dynObjIndex,
       "dynObjVariable": dynObjVariable,
       "dynObjOwner": dynObjOwner,
       "dynObjStatus": dynObjStatus,
       "dynObjData": dynObjData,
       "dynObj1": dynObj1,
       "dynObj2": dynObj2,
       "dynObj3": dynObj3,
       "dynObj4": dynObj4,
       "dynObj5": dynObj5,
       "dynObj6": dynObj6,
       "dynObj7": dynObj7,
       "dynObj8": dynObj8,
       "dynObj9": dynObj9,
       "dynObj10": dynObj10,
       "dynObj11": dynObj11,
       "dynObj12": dynObj12,
       "dynObj13": dynObj13,
       "dynObjConfig": dynObjConfig,
       "dynObjConfigTable": dynObjConfigTable,
       "dynObjConfigEntry": dynObjConfigEntry,
       "dynObjConfigOwner": dynObjConfigOwner,
       "dynObjConfigStatus": dynObjConfigStatus,
       "devices": devices}
)
