# SNMP MIB module (GLOBAL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1201GLO.mib
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
 Opaque,
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
    "Opaque",
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

(DisplayString,
 devices,
 profiles,
 protocols) = mibBuilder.importSymbols(
    "TMIB-II",
    "DisplayString",
    "devices",
    "profiles",
    "protocols")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProfilesSTMP_ObjectIdentity = ObjectIdentity
profilesSTMP = _ProfilesSTMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 2)
)


class _DynamicObjectPersistence_Type(Integer32):
    """Custom type dynamicObjectPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DynamicObjectPersistence_Type.__name__ = "Integer32"
_DynamicObjectPersistence_Object = MibScalar
dynamicObjectPersistence = _DynamicObjectPersistence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 2, 1),
    _DynamicObjectPersistence_Type()
)
dynamicObjectPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicObjectPersistence.setStatus("mandatory")
_ProfilesPMPP_ObjectIdentity = ObjectIdentity
profilesPMPP = _ProfilesPMPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 3)
)


class _MaxGroupAddresses_Type(Integer32):
    """Custom type maxGroupAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxGroupAddresses_Type.__name__ = "Integer32"
_MaxGroupAddresses_Object = MibScalar
maxGroupAddresses = _MaxGroupAddresses_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 3, 1),
    _MaxGroupAddresses_Type()
)
maxGroupAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxGroupAddresses.setStatus("mandatory")
_HdlcGroupAddressTable_Object = MibTable
hdlcGroupAddressTable = _HdlcGroupAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hdlcGroupAddressTable.setStatus("mandatory")
_HdlcGroupAddressEntry_Object = MibTableRow
hdlcGroupAddressEntry = _HdlcGroupAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 3, 2, 1)
)
hdlcGroupAddressEntry.setIndexNames(
    (0, "GLOBAL", "hdlcGroupAddressIndex"),
)
if mibBuilder.loadTexts:
    hdlcGroupAddressEntry.setStatus("mandatory")


class _HdlcGroupAddressIndex_Type(Integer32):
    """Custom type hdlcGroupAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HdlcGroupAddressIndex_Type.__name__ = "Integer32"
_HdlcGroupAddressIndex_Object = MibTableColumn
hdlcGroupAddressIndex = _HdlcGroupAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 3, 2, 1, 1),
    _HdlcGroupAddressIndex_Type()
)
hdlcGroupAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcGroupAddressIndex.setStatus("mandatory")
_HdlcGroupAddress_Type = Integer32
_HdlcGroupAddress_Object = MibTableColumn
hdlcGroupAddress = _HdlcGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 2, 3, 2, 1, 2),
    _HdlcGroupAddress_Type()
)
hdlcGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcGroupAddress.setStatus("mandatory")
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6)
)
_GlobalConfiguration_ObjectIdentity = ObjectIdentity
globalConfiguration = _GlobalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1)
)


class _GlobalSetIDParameter_Type(Integer32):
    """Custom type globalSetIDParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GlobalSetIDParameter_Type.__name__ = "Integer32"
_GlobalSetIDParameter_Object = MibScalar
globalSetIDParameter = _GlobalSetIDParameter_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 1),
    _GlobalSetIDParameter_Type()
)
globalSetIDParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalSetIDParameter.setStatus("optional")


class _GlobalMaxModules_Type(Integer32):
    """Custom type globalMaxModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GlobalMaxModules_Type.__name__ = "Integer32"
_GlobalMaxModules_Object = MibScalar
globalMaxModules = _GlobalMaxModules_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 2),
    _GlobalMaxModules_Type()
)
globalMaxModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalMaxModules.setStatus("mandatory")
_GlobalModuleTable_Object = MibTable
globalModuleTable = _GlobalModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    globalModuleTable.setStatus("mandatory")
_ModuleTableEntry_Object = MibTableRow
moduleTableEntry = _ModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1)
)
moduleTableEntry.setIndexNames(
    (0, "GLOBAL", "moduleNumber"),
)
if mibBuilder.loadTexts:
    moduleTableEntry.setStatus("mandatory")


class _ModuleNumber_Type(Integer32):
    """Custom type moduleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ModuleNumber_Type.__name__ = "Integer32"
_ModuleNumber_Object = MibTableColumn
moduleNumber = _ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1, 1),
    _ModuleNumber_Type()
)
moduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumber.setStatus("mandatory")
_ModuleDeviceNode_Type = ObjectIdentifier
_ModuleDeviceNode_Object = MibTableColumn
moduleDeviceNode = _ModuleDeviceNode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1, 2),
    _ModuleDeviceNode_Type()
)
moduleDeviceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDeviceNode.setStatus("mandatory")
_ModuleMake_Type = OctetString
_ModuleMake_Object = MibTableColumn
moduleMake = _ModuleMake_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1, 3),
    _ModuleMake_Type()
)
moduleMake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMake.setStatus("mandatory")
_ModuleModel_Type = OctetString
_ModuleModel_Object = MibTableColumn
moduleModel = _ModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1, 4),
    _ModuleModel_Type()
)
moduleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleModel.setStatus("mandatory")
_ModuleVersion_Type = OctetString
_ModuleVersion_Object = MibTableColumn
moduleVersion = _ModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1, 5),
    _ModuleVersion_Type()
)
moduleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVersion.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("hardware", 2),
          ("software", 3))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 1, 3, 1, 6),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")
_GlobalDBManagement_ObjectIdentity = ObjectIdentity
globalDBManagement = _GlobalDBManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2)
)


class _DbCreateTransaction_Type(Integer32):
    """Custom type dbCreateTransaction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("transaction", 2),
          ("verifying", 3),
          ("done", 6))
    )


_DbCreateTransaction_Type.__name__ = "Integer32"
_DbCreateTransaction_Object = MibScalar
dbCreateTransaction = _DbCreateTransaction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 1),
    _DbCreateTransaction_Type()
)
dbCreateTransaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbCreateTransaction.setStatus("mandatory")


class _DbErrorType_Type(Integer32):
    """Custom type dbErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("tooBig", 1),
          ("noSuchName", 2),
          ("badValue", 3),
          ("readOnly", 4),
          ("genError", 5),
          ("updateError", 6),
          ("noError", 7))
    )


_DbErrorType_Type.__name__ = "Integer32"
_DbErrorType_Object = MibScalar
dbErrorType = _DbErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 2),
    _DbErrorType_Type()
)
dbErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbErrorType.setStatus("deprecated")
_DbErrorID_Type = ObjectIdentifier
_DbErrorID_Object = MibScalar
dbErrorID = _DbErrorID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 3),
    _DbErrorID_Type()
)
dbErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbErrorID.setStatus("deprecated")


class _DbTransactionID_Type(Integer32):
    """Custom type dbTransactionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DbTransactionID_Type.__name__ = "Integer32"
_DbTransactionID_Object = MibScalar
dbTransactionID = _DbTransactionID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 4),
    _DbTransactionID_Type()
)
dbTransactionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dbTransactionID.setStatus("deprecated")


class _DbMakeID_Type(Integer32):
    """Custom type dbMakeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DbMakeID_Type.__name__ = "Integer32"
_DbMakeID_Object = MibScalar
dbMakeID = _DbMakeID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 5),
    _DbMakeID_Type()
)
dbMakeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbMakeID.setStatus("deprecated")


class _DbVerifyStatus_Type(Integer32):
    """Custom type dbVerifyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDone", 0),
          ("doneWithError", 1),
          ("doneWithNoError", 2))
    )


_DbVerifyStatus_Type.__name__ = "Integer32"
_DbVerifyStatus_Object = MibScalar
dbVerifyStatus = _DbVerifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 6),
    _DbVerifyStatus_Type()
)
dbVerifyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbVerifyStatus.setStatus("mandatory")


class _DbVerifyError_Type(OctetString):
    """Custom type dbVerifyError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DbVerifyError_Type.__name__ = "OctetString"
_DbVerifyError_Object = MibScalar
dbVerifyError = _DbVerifyError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 2, 7),
    _DbVerifyError_Type()
)
dbVerifyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbVerifyError.setStatus("mandatory")
_GlobalTimeManagement_ObjectIdentity = ObjectIdentity
globalTimeManagement = _GlobalTimeManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3)
)
_GlobalTime_Type = Counter32
_GlobalTime_Object = MibScalar
globalTime = _GlobalTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 1),
    _GlobalTime_Type()
)
globalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalTime.setStatus("mandatory")


class _GlobalDaylightSaving_Type(Integer32):
    """Custom type globalDaylightSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disableDST", 2),
          ("enableUSDST", 3))
    )


_GlobalDaylightSaving_Type.__name__ = "Integer32"
_GlobalDaylightSaving_Object = MibScalar
globalDaylightSaving = _GlobalDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 2),
    _GlobalDaylightSaving_Type()
)
globalDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalDaylightSaving.setStatus("mandatory")
_Timebase_ObjectIdentity = ObjectIdentity
timebase = _Timebase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3)
)


class _MaxTimeBaseScheduleEntries_Type(Integer32):
    """Custom type maxTimeBaseScheduleEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaxTimeBaseScheduleEntries_Type.__name__ = "Integer32"
_MaxTimeBaseScheduleEntries_Object = MibScalar
maxTimeBaseScheduleEntries = _MaxTimeBaseScheduleEntries_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 1),
    _MaxTimeBaseScheduleEntries_Type()
)
maxTimeBaseScheduleEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTimeBaseScheduleEntries.setStatus("mandatory")
_TimeBaseScheduleTable_Object = MibTable
timeBaseScheduleTable = _TimeBaseScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2)
)
if mibBuilder.loadTexts:
    timeBaseScheduleTable.setStatus("mandatory")
_TimeBaseScheduleEntry_Object = MibTableRow
timeBaseScheduleEntry = _TimeBaseScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2, 1)
)
timeBaseScheduleEntry.setIndexNames(
    (0, "GLOBAL", "timeBaseScheduleNumber"),
)
if mibBuilder.loadTexts:
    timeBaseScheduleEntry.setStatus("mandatory")


class _TimeBaseScheduleNumber_Type(Integer32):
    """Custom type timeBaseScheduleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TimeBaseScheduleNumber_Type.__name__ = "Integer32"
_TimeBaseScheduleNumber_Object = MibTableColumn
timeBaseScheduleNumber = _TimeBaseScheduleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2, 1, 1),
    _TimeBaseScheduleNumber_Type()
)
timeBaseScheduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeBaseScheduleNumber.setStatus("mandatory")


class _TimeBaseScheduleMonth_Type(Integer32):
    """Custom type timeBaseScheduleMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimeBaseScheduleMonth_Type.__name__ = "Integer32"
_TimeBaseScheduleMonth_Object = MibTableColumn
timeBaseScheduleMonth = _TimeBaseScheduleMonth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2, 1, 2),
    _TimeBaseScheduleMonth_Type()
)
timeBaseScheduleMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeBaseScheduleMonth.setStatus("mandatory")


class _TimeBaseScheduleDay_Type(Integer32):
    """Custom type timeBaseScheduleDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TimeBaseScheduleDay_Type.__name__ = "Integer32"
_TimeBaseScheduleDay_Object = MibTableColumn
timeBaseScheduleDay = _TimeBaseScheduleDay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2, 1, 3),
    _TimeBaseScheduleDay_Type()
)
timeBaseScheduleDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeBaseScheduleDay.setStatus("mandatory")


class _TimeBaseScheduleDate_Type(Integer32):
    """Custom type timeBaseScheduleDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TimeBaseScheduleDate_Type.__name__ = "Integer32"
_TimeBaseScheduleDate_Object = MibTableColumn
timeBaseScheduleDate = _TimeBaseScheduleDate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2, 1, 4),
    _TimeBaseScheduleDate_Type()
)
timeBaseScheduleDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeBaseScheduleDate.setStatus("mandatory")


class _TimeBaseScheduleDayPlan_Type(Integer32):
    """Custom type timeBaseScheduleDayPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TimeBaseScheduleDayPlan_Type.__name__ = "Integer32"
_TimeBaseScheduleDayPlan_Object = MibTableColumn
timeBaseScheduleDayPlan = _TimeBaseScheduleDayPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 2, 1, 5),
    _TimeBaseScheduleDayPlan_Type()
)
timeBaseScheduleDayPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeBaseScheduleDayPlan.setStatus("mandatory")


class _MaxDayPlans_Type(Integer32):
    """Custom type maxDayPlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MaxDayPlans_Type.__name__ = "Integer32"
_MaxDayPlans_Object = MibScalar
maxDayPlans = _MaxDayPlans_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 3),
    _MaxDayPlans_Type()
)
maxDayPlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxDayPlans.setStatus("mandatory")


class _MaxDayPlanEvents_Type(Integer32):
    """Custom type maxDayPlanEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MaxDayPlanEvents_Type.__name__ = "Integer32"
_MaxDayPlanEvents_Object = MibScalar
maxDayPlanEvents = _MaxDayPlanEvents_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 4),
    _MaxDayPlanEvents_Type()
)
maxDayPlanEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxDayPlanEvents.setStatus("mandatory")
_TimeBaseDayPlanTable_Object = MibTable
timeBaseDayPlanTable = _TimeBaseDayPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5)
)
if mibBuilder.loadTexts:
    timeBaseDayPlanTable.setStatus("mandatory")
_TimeBaseDayPlanEntry_Object = MibTableRow
timeBaseDayPlanEntry = _TimeBaseDayPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5, 1)
)
timeBaseDayPlanEntry.setIndexNames(
    (0, "GLOBAL", "dayPlanNumber"),
    (0, "GLOBAL", "dayPlanEventNumber"),
)
if mibBuilder.loadTexts:
    timeBaseDayPlanEntry.setStatus("mandatory")


class _DayPlanNumber_Type(Integer32):
    """Custom type dayPlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DayPlanNumber_Type.__name__ = "Integer32"
_DayPlanNumber_Object = MibTableColumn
dayPlanNumber = _DayPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5, 1, 1),
    _DayPlanNumber_Type()
)
dayPlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dayPlanNumber.setStatus("mandatory")


class _DayPlanEventNumber_Type(Integer32):
    """Custom type dayPlanEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DayPlanEventNumber_Type.__name__ = "Integer32"
_DayPlanEventNumber_Object = MibTableColumn
dayPlanEventNumber = _DayPlanEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5, 1, 2),
    _DayPlanEventNumber_Type()
)
dayPlanEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dayPlanEventNumber.setStatus("mandatory")


class _DayPlanHour_Type(Integer32):
    """Custom type dayPlanHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DayPlanHour_Type.__name__ = "Integer32"
_DayPlanHour_Object = MibTableColumn
dayPlanHour = _DayPlanHour_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5, 1, 3),
    _DayPlanHour_Type()
)
dayPlanHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayPlanHour.setStatus("mandatory")


class _DayPlanMinute_Type(Integer32):
    """Custom type dayPlanMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DayPlanMinute_Type.__name__ = "Integer32"
_DayPlanMinute_Object = MibTableColumn
dayPlanMinute = _DayPlanMinute_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5, 1, 4),
    _DayPlanMinute_Type()
)
dayPlanMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayPlanMinute.setStatus("mandatory")
_DayPlanActionNumberOID_Type = ObjectIdentifier
_DayPlanActionNumberOID_Object = MibTableColumn
dayPlanActionNumberOID = _DayPlanActionNumberOID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 5, 1, 5),
    _DayPlanActionNumberOID_Type()
)
dayPlanActionNumberOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayPlanActionNumberOID.setStatus("mandatory")


class _DayPlanStatus_Type(Integer32):
    """Custom type dayPlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DayPlanStatus_Type.__name__ = "Integer32"
_DayPlanStatus_Object = MibScalar
dayPlanStatus = _DayPlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 3, 6),
    _DayPlanStatus_Type()
)
dayPlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dayPlanStatus.setStatus("mandatory")


class _GlobalLocalTimeDifferential_Type(Integer32):
    """Custom type globalLocalTimeDifferential based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43200, 43200),
    )


_GlobalLocalTimeDifferential_Type.__name__ = "Integer32"
_GlobalLocalTimeDifferential_Object = MibScalar
globalLocalTimeDifferential = _GlobalLocalTimeDifferential_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 3, 4),
    _GlobalLocalTimeDifferential_Type()
)
globalLocalTimeDifferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalLocalTimeDifferential.setStatus("mandatory")
_GlobalReport_ObjectIdentity = ObjectIdentity
globalReport = _GlobalReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4)
)


class _MaxEventLogConfigs_Type(Integer32):
    """Custom type maxEventLogConfigs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaxEventLogConfigs_Type.__name__ = "Integer32"
_MaxEventLogConfigs_Object = MibScalar
maxEventLogConfigs = _MaxEventLogConfigs_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 1),
    _MaxEventLogConfigs_Type()
)
maxEventLogConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxEventLogConfigs.setStatus("mandatory")
_EventLogConfigTable_Object = MibTable
eventLogConfigTable = _EventLogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2)
)
if mibBuilder.loadTexts:
    eventLogConfigTable.setStatus("mandatory")
_EventLogConfigEntry_Object = MibTableRow
eventLogConfigEntry = _EventLogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1)
)
eventLogConfigEntry.setIndexNames(
    (0, "GLOBAL", "eventConfigID"),
)
if mibBuilder.loadTexts:
    eventLogConfigEntry.setStatus("mandatory")


class _EventConfigID_Type(Integer32):
    """Custom type eventConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventConfigID_Type.__name__ = "Integer32"
_EventConfigID_Object = MibTableColumn
eventConfigID = _EventConfigID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 1),
    _EventConfigID_Type()
)
eventConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventConfigID.setStatus("mandatory")


class _EventConfigClass_Type(Integer32):
    """Custom type eventConfigClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EventConfigClass_Type.__name__ = "Integer32"
_EventConfigClass_Object = MibTableColumn
eventConfigClass = _EventConfigClass_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 2),
    _EventConfigClass_Type()
)
eventConfigClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigClass.setStatus("mandatory")


class _EventConfigMode_Type(Integer32):
    """Custom type eventConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("onChange", 2),
          ("greaterThanValue", 3),
          ("smallerThanValue", 4),
          ("hysteresisBound", 5),
          ("periodic", 6))
    )


_EventConfigMode_Type.__name__ = "Integer32"
_EventConfigMode_Object = MibTableColumn
eventConfigMode = _EventConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 3),
    _EventConfigMode_Type()
)
eventConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigMode.setStatus("mandatory")
_EventConfigCompareValue_Type = Integer32
_EventConfigCompareValue_Object = MibTableColumn
eventConfigCompareValue = _EventConfigCompareValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 4),
    _EventConfigCompareValue_Type()
)
eventConfigCompareValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigCompareValue.setStatus("mandatory")
_EventConfigCompareValue2_Type = Integer32
_EventConfigCompareValue2_Object = MibTableColumn
eventConfigCompareValue2 = _EventConfigCompareValue2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 5),
    _EventConfigCompareValue2_Type()
)
eventConfigCompareValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigCompareValue2.setStatus("mandatory")
_EventConfigCompareOID_Type = ObjectIdentifier
_EventConfigCompareOID_Object = MibTableColumn
eventConfigCompareOID = _EventConfigCompareOID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 6),
    _EventConfigCompareOID_Type()
)
eventConfigCompareOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigCompareOID.setStatus("mandatory")
_EventConfigLogOID_Type = ObjectIdentifier
_EventConfigLogOID_Object = MibTableColumn
eventConfigLogOID = _EventConfigLogOID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 7),
    _EventConfigLogOID_Type()
)
eventConfigLogOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigLogOID.setStatus("optional")


class _EventConfigAction_Type(Integer32):
    """Custom type eventConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("log", 3))
    )


_EventConfigAction_Type.__name__ = "Integer32"
_EventConfigAction_Object = MibTableColumn
eventConfigAction = _EventConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 2, 1, 8),
    _EventConfigAction_Type()
)
eventConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventConfigAction.setStatus("optional")


class _MaxEventLogSize_Type(Integer32):
    """Custom type maxEventLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MaxEventLogSize_Type.__name__ = "Integer32"
_MaxEventLogSize_Object = MibScalar
maxEventLogSize = _MaxEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 3),
    _MaxEventLogSize_Type()
)
maxEventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxEventLogSize.setStatus("mandatory")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4, 1)
)
eventLogEntry.setIndexNames(
    (0, "GLOBAL", "eventLogClass"),
    (0, "GLOBAL", "eventLogNumber"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("mandatory")


class _EventLogClass_Type(Integer32):
    """Custom type eventLogClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EventLogClass_Type.__name__ = "Integer32"
_EventLogClass_Object = MibTableColumn
eventLogClass = _EventLogClass_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4, 1, 1),
    _EventLogClass_Type()
)
eventLogClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogClass.setStatus("mandatory")


class _EventLogNumber_Type(Integer32):
    """Custom type eventLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EventLogNumber_Type.__name__ = "Integer32"
_EventLogNumber_Object = MibTableColumn
eventLogNumber = _EventLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4, 1, 2),
    _EventLogNumber_Type()
)
eventLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogNumber.setStatus("mandatory")


class _EventLogID_Type(Integer32):
    """Custom type eventLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EventLogID_Type.__name__ = "Integer32"
_EventLogID_Object = MibTableColumn
eventLogID = _EventLogID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4, 1, 3),
    _EventLogID_Type()
)
eventLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogID.setStatus("mandatory")
_EventLogTime_Type = Counter32
_EventLogTime_Object = MibTableColumn
eventLogTime = _EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4, 1, 4),
    _EventLogTime_Type()
)
eventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTime.setStatus("mandatory")
_EventLogValue_Type = Opaque
_EventLogValue_Object = MibTableColumn
eventLogValue = _EventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 4, 1, 5),
    _EventLogValue_Type()
)
eventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogValue.setStatus("mandatory")


class _MaxEventClasses_Type(Integer32):
    """Custom type maxEventClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxEventClasses_Type.__name__ = "Integer32"
_MaxEventClasses_Object = MibScalar
maxEventClasses = _MaxEventClasses_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 5),
    _MaxEventClasses_Type()
)
maxEventClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxEventClasses.setStatus("mandatory")
_EventClassTable_Object = MibTable
eventClassTable = _EventClassTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6)
)
if mibBuilder.loadTexts:
    eventClassTable.setStatus("mandatory")
_EventClassEntry_Object = MibTableRow
eventClassEntry = _EventClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6, 1)
)
eventClassEntry.setIndexNames(
    (0, "GLOBAL", "eventClassNumber"),
)
if mibBuilder.loadTexts:
    eventClassEntry.setStatus("mandatory")


class _EventClassNumber_Type(Integer32):
    """Custom type eventClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EventClassNumber_Type.__name__ = "Integer32"
_EventClassNumber_Object = MibTableColumn
eventClassNumber = _EventClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6, 1, 1),
    _EventClassNumber_Type()
)
eventClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventClassNumber.setStatus("mandatory")


class _EventClassLimit_Type(Integer32):
    """Custom type eventClassLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EventClassLimit_Type.__name__ = "Integer32"
_EventClassLimit_Object = MibTableColumn
eventClassLimit = _EventClassLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6, 1, 2),
    _EventClassLimit_Type()
)
eventClassLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventClassLimit.setStatus("mandatory")
_EventClassClearTime_Type = Counter32
_EventClassClearTime_Object = MibTableColumn
eventClassClearTime = _EventClassClearTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6, 1, 3),
    _EventClassClearTime_Type()
)
eventClassClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventClassClearTime.setStatus("mandatory")
_EventClassDescription_Type = OctetString
_EventClassDescription_Object = MibTableColumn
eventClassDescription = _EventClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6, 1, 4),
    _EventClassDescription_Type()
)
eventClassDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventClassDescription.setStatus("optional")


class _EventClassNumRowsInLog_Type(Integer32):
    """Custom type eventClassNumRowsInLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EventClassNumRowsInLog_Type.__name__ = "Integer32"
_EventClassNumRowsInLog_Object = MibTableColumn
eventClassNumRowsInLog = _EventClassNumRowsInLog_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 4, 6, 1, 5),
    _EventClassNumRowsInLog_Type()
)
eventClassNumRowsInLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventClassNumRowsInLog.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5)
)


class _CommunityNameAdmin_Type(OctetString):
    """Custom type communityNameAdmin based on OctetString"""
    defaultValue = OctetString("administrator")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 16),
    )


_CommunityNameAdmin_Type.__name__ = "OctetString"
_CommunityNameAdmin_Object = MibScalar
communityNameAdmin = _CommunityNameAdmin_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 1),
    _CommunityNameAdmin_Type()
)
communityNameAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityNameAdmin.setStatus("mandatory")


class _CommunityNamesMax_Type(Integer32):
    """Custom type communityNamesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CommunityNamesMax_Type.__name__ = "Integer32"
_CommunityNamesMax_Object = MibScalar
communityNamesMax = _CommunityNamesMax_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 2),
    _CommunityNamesMax_Type()
)
communityNamesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityNamesMax.setStatus("mandatory")
_CommunityNameTable_Object = MibTable
communityNameTable = _CommunityNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 3)
)
if mibBuilder.loadTexts:
    communityNameTable.setStatus("mandatory")
_CommunityNameTableEntry_Object = MibTableRow
communityNameTableEntry = _CommunityNameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 3, 1)
)
communityNameTableEntry.setIndexNames(
    (0, "GLOBAL", "communityNameIndex"),
)
if mibBuilder.loadTexts:
    communityNameTableEntry.setStatus("mandatory")


class _CommunityNameIndex_Type(Integer32):
    """Custom type communityNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CommunityNameIndex_Type.__name__ = "Integer32"
_CommunityNameIndex_Object = MibTableColumn
communityNameIndex = _CommunityNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 3, 1, 1),
    _CommunityNameIndex_Type()
)
communityNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityNameIndex.setStatus("mandatory")


class _CommunityNameUser_Type(OctetString):
    """Custom type communityNameUser based on OctetString"""
    defaultValue = OctetString("public")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 16),
    )


_CommunityNameUser_Type.__name__ = "OctetString"
_CommunityNameUser_Object = MibTableColumn
communityNameUser = _CommunityNameUser_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 3, 1, 2),
    _CommunityNameUser_Type()
)
communityNameUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityNameUser.setStatus("mandatory")


class _CommunityNameAccessMask_Type(Gauge32):
    """Custom type communityNameAccessMask based on Gauge32"""
    defaultValue = 4294967295


_CommunityNameAccessMask_Type.__name__ = "Gauge32"
_CommunityNameAccessMask_Object = MibTableColumn
communityNameAccessMask = _CommunityNameAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 6, 5, 3, 1, 3),
    _CommunityNameAccessMask_Type()
)
communityNameAccessMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityNameAccessMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GLOBAL",
    **{"profilesSTMP": profilesSTMP,
       "dynamicObjectPersistence": dynamicObjectPersistence,
       "profilesPMPP": profilesPMPP,
       "maxGroupAddresses": maxGroupAddresses,
       "hdlcGroupAddressTable": hdlcGroupAddressTable,
       "hdlcGroupAddressEntry": hdlcGroupAddressEntry,
       "hdlcGroupAddressIndex": hdlcGroupAddressIndex,
       "hdlcGroupAddress": hdlcGroupAddress,
       "global": _pysmi_global,
       "globalConfiguration": globalConfiguration,
       "globalSetIDParameter": globalSetIDParameter,
       "globalMaxModules": globalMaxModules,
       "globalModuleTable": globalModuleTable,
       "moduleTableEntry": moduleTableEntry,
       "moduleNumber": moduleNumber,
       "moduleDeviceNode": moduleDeviceNode,
       "moduleMake": moduleMake,
       "moduleModel": moduleModel,
       "moduleVersion": moduleVersion,
       "moduleType": moduleType,
       "globalDBManagement": globalDBManagement,
       "dbCreateTransaction": dbCreateTransaction,
       "dbErrorType": dbErrorType,
       "dbErrorID": dbErrorID,
       "dbTransactionID": dbTransactionID,
       "dbMakeID": dbMakeID,
       "dbVerifyStatus": dbVerifyStatus,
       "dbVerifyError": dbVerifyError,
       "globalTimeManagement": globalTimeManagement,
       "globalTime": globalTime,
       "globalDaylightSaving": globalDaylightSaving,
       "timebase": timebase,
       "maxTimeBaseScheduleEntries": maxTimeBaseScheduleEntries,
       "timeBaseScheduleTable": timeBaseScheduleTable,
       "timeBaseScheduleEntry": timeBaseScheduleEntry,
       "timeBaseScheduleNumber": timeBaseScheduleNumber,
       "timeBaseScheduleMonth": timeBaseScheduleMonth,
       "timeBaseScheduleDay": timeBaseScheduleDay,
       "timeBaseScheduleDate": timeBaseScheduleDate,
       "timeBaseScheduleDayPlan": timeBaseScheduleDayPlan,
       "maxDayPlans": maxDayPlans,
       "maxDayPlanEvents": maxDayPlanEvents,
       "timeBaseDayPlanTable": timeBaseDayPlanTable,
       "timeBaseDayPlanEntry": timeBaseDayPlanEntry,
       "dayPlanNumber": dayPlanNumber,
       "dayPlanEventNumber": dayPlanEventNumber,
       "dayPlanHour": dayPlanHour,
       "dayPlanMinute": dayPlanMinute,
       "dayPlanActionNumberOID": dayPlanActionNumberOID,
       "dayPlanStatus": dayPlanStatus,
       "globalLocalTimeDifferential": globalLocalTimeDifferential,
       "globalReport": globalReport,
       "maxEventLogConfigs": maxEventLogConfigs,
       "eventLogConfigTable": eventLogConfigTable,
       "eventLogConfigEntry": eventLogConfigEntry,
       "eventConfigID": eventConfigID,
       "eventConfigClass": eventConfigClass,
       "eventConfigMode": eventConfigMode,
       "eventConfigCompareValue": eventConfigCompareValue,
       "eventConfigCompareValue2": eventConfigCompareValue2,
       "eventConfigCompareOID": eventConfigCompareOID,
       "eventConfigLogOID": eventConfigLogOID,
       "eventConfigAction": eventConfigAction,
       "maxEventLogSize": maxEventLogSize,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogClass": eventLogClass,
       "eventLogNumber": eventLogNumber,
       "eventLogID": eventLogID,
       "eventLogTime": eventLogTime,
       "eventLogValue": eventLogValue,
       "maxEventClasses": maxEventClasses,
       "eventClassTable": eventClassTable,
       "eventClassEntry": eventClassEntry,
       "eventClassNumber": eventClassNumber,
       "eventClassLimit": eventClassLimit,
       "eventClassClearTime": eventClassClearTime,
       "eventClassDescription": eventClassDescription,
       "eventClassNumRowsInLog": eventClassNumRowsInLog,
       "security": security,
       "communityNameAdmin": communityNameAdmin,
       "communityNamesMax": communityNamesMax,
       "communityNameTable": communityNameTable,
       "communityNameTableEntry": communityNameTableEntry,
       "communityNameIndex": communityNameIndex,
       "communityNameUser": communityNameUser,
       "communityNameAccessMask": communityNameAccessMask}
)
