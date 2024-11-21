# SNMP MIB module (RMC-MIB1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1207RMC.mib
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

(devices,) = mibBuilder.importSymbols(
    "TMIB-II",
    "devices")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ramp_ObjectIdentity = ObjectIdentity
ramp = _Ramp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2)
)
_RmcCfg_ObjectIdentity = ObjectIdentity
rmcCfg = _RmcCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 1)
)


class _RmcCommRefreshThreshold_Type(Integer32):
    """Custom type rmcCommRefreshThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcCommRefreshThreshold_Type.__name__ = "Integer32"
_RmcCommRefreshThreshold_Object = MibScalar
rmcCommRefreshThreshold = _RmcCommRefreshThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 1, 1),
    _RmcCommRefreshThreshold_Type()
)
rmcCommRefreshThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCommRefreshThreshold.setStatus("mandatory")


class _RmcCalcInterval_Type(Integer32):
    """Custom type rmcCalcInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcCalcInterval_Type.__name__ = "Integer32"
_RmcCalcInterval_Object = MibScalar
rmcCalcInterval = _RmcCalcInterval_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 1, 2),
    _RmcCalcInterval_Type()
)
rmcCalcInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCalcInterval.setStatus("mandatory")
_RmcML_ObjectIdentity = ObjectIdentity
rmcML = _RmcML_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2)
)


class _RmcAveragingPeriods_Type(Integer32):
    """Custom type rmcAveragingPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcAveragingPeriods_Type.__name__ = "Integer32"
_RmcAveragingPeriods_Object = MibScalar
rmcAveragingPeriods = _RmcAveragingPeriods_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 1),
    _RmcAveragingPeriods_Type()
)
rmcAveragingPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcAveragingPeriods.setStatus("mandatory")


class _RmcMaxNumML_Type(Integer32):
    """Custom type rmcMaxNumML based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxNumML_Type.__name__ = "Integer32"
_RmcMaxNumML_Object = MibScalar
rmcMaxNumML = _RmcMaxNumML_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 2),
    _RmcMaxNumML_Type()
)
rmcMaxNumML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumML.setStatus("mandatory")


class _RmcNumML_Type(Integer32):
    """Custom type rmcNumML based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcNumML_Type.__name__ = "Integer32"
_RmcNumML_Object = MibScalar
rmcNumML = _RmcNumML_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 3),
    _RmcNumML_Type()
)
rmcNumML.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumML.setStatus("mandatory")
_RmcMLCtrlTable_Object = MibTable
rmcMLCtrlTable = _RmcMLCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    rmcMLCtrlTable.setStatus("mandatory")
_RmcMLCtrlEntry_Object = MibTableRow
rmcMLCtrlEntry = _RmcMLCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1)
)
rmcMLCtrlEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMLNumber"),
)
if mibBuilder.loadTexts:
    rmcMLCtrlEntry.setStatus("mandatory")


class _RmcMLNumber_Type(Integer32):
    """Custom type rmcMLNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLNumber_Type.__name__ = "Integer32"
_RmcMLNumber_Object = MibTableColumn
rmcMLNumber = _RmcMLNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 1),
    _RmcMLNumber_Type()
)
rmcMLNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMLNumber.setStatus("mandatory")


class _RmcMLMode_Type(Integer32):
    """Custom type rmcMLMode based on Integer32"""
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
        *(("disabled", 1),
          ("singleEnabledLead", 2),
          ("singleEnabledTrail", 3),
          ("dualEnabled", 4),
          ("preprocessedEnabled", 5))
    )


_RmcMLMode_Type.__name__ = "Integer32"
_RmcMLMode_Object = MibTableColumn
rmcMLMode = _RmcMLMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 2),
    _RmcMLMode_Type()
)
rmcMLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLMode.setStatus("mandatory")


class _RmcMLLeadZoneLength_Type(Integer32):
    """Custom type rmcMLLeadZoneLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLLeadZoneLength_Type.__name__ = "Integer32"
_RmcMLLeadZoneLength_Object = MibTableColumn
rmcMLLeadZoneLength = _RmcMLLeadZoneLength_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 3),
    _RmcMLLeadZoneLength_Type()
)
rmcMLLeadZoneLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLLeadZoneLength.setStatus("optional")


class _RmcMLTrailZoneLength_Type(Integer32):
    """Custom type rmcMLTrailZoneLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLTrailZoneLength_Type.__name__ = "Integer32"
_RmcMLTrailZoneLength_Object = MibTableColumn
rmcMLTrailZoneLength = _RmcMLTrailZoneLength_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 4),
    _RmcMLTrailZoneLength_Type()
)
rmcMLTrailZoneLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLTrailZoneLength.setStatus("optional")


class _RmcMLUsageMode_Type(Integer32):
    """Custom type rmcMLUsageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("schemeF", 2),
          ("schemeO", 3),
          ("schemeFO", 4),
          ("schemeS", 5),
          ("schemeFS", 6),
          ("schemeOS", 7),
          ("schemeFOS", 8),
          ("determinedByOther", 9))
    )


_RmcMLUsageMode_Type.__name__ = "Integer32"
_RmcMLUsageMode_Object = MibTableColumn
rmcMLUsageMode = _RmcMLUsageMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 5),
    _RmcMLUsageMode_Type()
)
rmcMLUsageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLUsageMode.setStatus("mandatory")


class _RmcMLSpeedTrapSpacing_Type(Integer32):
    """Custom type rmcMLSpeedTrapSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLSpeedTrapSpacing_Type.__name__ = "Integer32"
_RmcMLSpeedTrapSpacing_Object = MibTableColumn
rmcMLSpeedTrapSpacing = _RmcMLSpeedTrapSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 6),
    _RmcMLSpeedTrapSpacing_Type()
)
rmcMLSpeedTrapSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLSpeedTrapSpacing.setStatus("optional")


class _RmcMLErraticCount_Type(Integer32):
    """Custom type rmcMLErraticCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLErraticCount_Type.__name__ = "Integer32"
_RmcMLErraticCount_Object = MibTableColumn
rmcMLErraticCount = _RmcMLErraticCount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 7),
    _RmcMLErraticCount_Type()
)
rmcMLErraticCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLErraticCount.setStatus("optional")


class _RmcMLMaxPresence_Type(Integer32):
    """Custom type rmcMLMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcMLMaxPresence_Type.__name__ = "Integer32"
_RmcMLMaxPresence_Object = MibTableColumn
rmcMLMaxPresence = _RmcMLMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 8),
    _RmcMLMaxPresence_Type()
)
rmcMLMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLMaxPresence.setStatus("optional")


class _RmcMLNoActivity_Type(Integer32):
    """Custom type rmcMLNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcMLNoActivity_Type.__name__ = "Integer32"
_RmcMLNoActivity_Object = MibTableColumn
rmcMLNoActivity = _RmcMLNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 9),
    _RmcMLNoActivity_Type()
)
rmcMLNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLNoActivity.setStatus("optional")


class _RmcVehicleLength_Type(Integer32):
    """Custom type rmcVehicleLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcVehicleLength_Type.__name__ = "Integer32"
_RmcVehicleLength_Object = MibTableColumn
rmcVehicleLength = _RmcVehicleLength_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 4, 1, 10),
    _RmcVehicleLength_Type()
)
rmcVehicleLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcVehicleLength.setStatus("optional")


class _RmcAverageFlowRate_Type(Integer32):
    """Custom type rmcAverageFlowRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcAverageFlowRate_Type.__name__ = "Integer32"
_RmcAverageFlowRate_Object = MibScalar
rmcAverageFlowRate = _RmcAverageFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 5),
    _RmcAverageFlowRate_Type()
)
rmcAverageFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcAverageFlowRate.setStatus("mandatory")


class _RmcAverageOccupancy_Type(Integer32):
    """Custom type rmcAverageOccupancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcAverageOccupancy_Type.__name__ = "Integer32"
_RmcAverageOccupancy_Object = MibScalar
rmcAverageOccupancy = _RmcAverageOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 6),
    _RmcAverageOccupancy_Type()
)
rmcAverageOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcAverageOccupancy.setStatus("mandatory")


class _RmcAverageSpeed_Type(Integer32):
    """Custom type rmcAverageSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcAverageSpeed_Type.__name__ = "Integer32"
_RmcAverageSpeed_Object = MibScalar
rmcAverageSpeed = _RmcAverageSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 7),
    _RmcAverageSpeed_Type()
)
rmcAverageSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcAverageSpeed.setStatus("mandatory")
_RmcMLStatTable_Object = MibTable
rmcMLStatTable = _RmcMLStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 8)
)
if mibBuilder.loadTexts:
    rmcMLStatTable.setStatus("mandatory")
_RmcMLStatEntry_Object = MibTableRow
rmcMLStatEntry = _RmcMLStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 8, 1)
)
rmcMLStatEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMLNumber"),
)
if mibBuilder.loadTexts:
    rmcMLStatEntry.setStatus("mandatory")


class _RmcMLLeadStatus_Type(Integer32):
    """Custom type rmcMLLeadStatus based on Integer32"""
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
        *(("disabled", 1),
          ("working", 2),
          ("otherError", 3),
          ("erraticCount", 4),
          ("maxPresence", 5),
          ("noActivity", 6),
          ("errorAtSensor", 7))
    )


_RmcMLLeadStatus_Type.__name__ = "Integer32"
_RmcMLLeadStatus_Object = MibTableColumn
rmcMLLeadStatus = _RmcMLLeadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 8, 1, 1),
    _RmcMLLeadStatus_Type()
)
rmcMLLeadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMLLeadStatus.setStatus("optional")


class _RmcMLTrailStatus_Type(Integer32):
    """Custom type rmcMLTrailStatus based on Integer32"""
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
        *(("disabled", 1),
          ("working", 2),
          ("otherError", 3),
          ("erraticCount", 4),
          ("maxPresence", 5),
          ("noActivity", 6),
          ("errorAtSensor", 7))
    )


_RmcMLTrailStatus_Type.__name__ = "Integer32"
_RmcMLTrailStatus_Object = MibTableColumn
rmcMLTrailStatus = _RmcMLTrailStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 8, 1, 2),
    _RmcMLTrailStatus_Type()
)
rmcMLTrailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMLTrailStatus.setStatus("optional")


class _RmcMLStatus_Type(Integer32):
    """Custom type rmcMLStatus based on Integer32"""
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
        *(("working", 1),
          ("disabled", 2),
          ("partialFailure", 3),
          ("totalFailure", 4))
    )


_RmcMLStatus_Type.__name__ = "Integer32"
_RmcMLStatus_Object = MibTableColumn
rmcMLStatus = _RmcMLStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 8, 1, 3),
    _RmcMLStatus_Type()
)
rmcMLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMLStatus.setStatus("mandatory")


class _RmcMLUsageStatus_Type(Integer32):
    """Custom type rmcMLUsageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("schemeF", 2),
          ("schemeO", 3),
          ("schemeFO", 4),
          ("schemeS", 5),
          ("schemeFS", 6),
          ("schemeOS", 7),
          ("schemeFOS", 8))
    )


_RmcMLUsageStatus_Type.__name__ = "Integer32"
_RmcMLUsageStatus_Object = MibTableColumn
rmcMLUsageStatus = _RmcMLUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 2, 8, 1, 4),
    _RmcMLUsageStatus_Type()
)
rmcMLUsageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMLUsageStatus.setStatus("mandatory")
_RmcMeter_ObjectIdentity = ObjectIdentity
rmcMeter = _RmcMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3)
)
_RmcMeterMain_ObjectIdentity = ObjectIdentity
rmcMeterMain = _RmcMeterMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1)
)


class _RmcMaxNumMeteredLanes_Type(Integer32):
    """Custom type rmcMaxNumMeteredLanes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxNumMeteredLanes_Type.__name__ = "Integer32"
_RmcMaxNumMeteredLanes_Object = MibScalar
rmcMaxNumMeteredLanes = _RmcMaxNumMeteredLanes_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 1),
    _RmcMaxNumMeteredLanes_Type()
)
rmcMaxNumMeteredLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumMeteredLanes.setStatus("mandatory")


class _RmcNumMeteredLanes_Type(Integer32):
    """Custom type rmcNumMeteredLanes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcNumMeteredLanes_Type.__name__ = "Integer32"
_RmcNumMeteredLanes_Object = MibScalar
rmcNumMeteredLanes = _RmcNumMeteredLanes_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 2),
    _RmcNumMeteredLanes_Type()
)
rmcNumMeteredLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumMeteredLanes.setStatus("mandatory")
_RmcMeterCfgTable_Object = MibTable
rmcMeterCfgTable = _RmcMeterCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    rmcMeterCfgTable.setStatus("mandatory")
_RmcMeterCfgEntry_Object = MibTableRow
rmcMeterCfgEntry = _RmcMeterCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1)
)
rmcMeterCfgEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcMeterCfgEntry.setStatus("mandatory")


class _RmcMeterNumber_Type(Integer32):
    """Custom type rmcMeterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMeterNumber_Type.__name__ = "Integer32"
_RmcMeterNumber_Object = MibTableColumn
rmcMeterNumber = _RmcMeterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 1),
    _RmcMeterNumber_Type()
)
rmcMeterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMeterNumber.setStatus("mandatory")


class _RmcDependGroupNumber_Type(Integer32):
    """Custom type rmcDependGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcDependGroupNumber_Type.__name__ = "Integer32"
_RmcDependGroupNumber_Object = MibTableColumn
rmcDependGroupNumber = _RmcDependGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 2),
    _RmcDependGroupNumber_Type()
)
rmcDependGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDependGroupNumber.setStatus("mandatory")


class _RmcDependGroupSeqNumber_Type(Integer32):
    """Custom type rmcDependGroupSeqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcDependGroupSeqNumber_Type.__name__ = "Integer32"
_RmcDependGroupSeqNumber_Object = MibTableColumn
rmcDependGroupSeqNumber = _RmcDependGroupSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 3),
    _RmcDependGroupSeqNumber_Type()
)
rmcDependGroupSeqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDependGroupSeqNumber.setStatus("optional")


class _RmcCmdSourcePriorityOrder_Type(Integer32):
    """Custom type rmcCmdSourcePriorityOrder based on Integer32"""
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
        *(("schemeCIT", 1),
          ("schemeICT", 2),
          ("schemeTCI", 3),
          ("schemeTIC", 4),
          ("schemeCTI", 5),
          ("schemeITC", 6))
    )


_RmcCmdSourcePriorityOrder_Type.__name__ = "Integer32"
_RmcCmdSourcePriorityOrder_Object = MibTableColumn
rmcCmdSourcePriorityOrder = _RmcCmdSourcePriorityOrder_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 4),
    _RmcCmdSourcePriorityOrder_Type()
)
rmcCmdSourcePriorityOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCmdSourcePriorityOrder.setStatus("mandatory")


class _RmcDemandErraticCount_Type(Integer32):
    """Custom type rmcDemandErraticCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDemandErraticCount_Type.__name__ = "Integer32"
_RmcDemandErraticCount_Object = MibTableColumn
rmcDemandErraticCount = _RmcDemandErraticCount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 5),
    _RmcDemandErraticCount_Type()
)
rmcDemandErraticCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDemandErraticCount.setStatus("optional")


class _RmcDemandMaxPresence_Type(Integer32):
    """Custom type rmcDemandMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcDemandMaxPresence_Type.__name__ = "Integer32"
_RmcDemandMaxPresence_Object = MibTableColumn
rmcDemandMaxPresence = _RmcDemandMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 6),
    _RmcDemandMaxPresence_Type()
)
rmcDemandMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDemandMaxPresence.setStatus("optional")


class _RmcDemandNoActivity_Type(Integer32):
    """Custom type rmcDemandNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcDemandNoActivity_Type.__name__ = "Integer32"
_RmcDemandNoActivity_Object = MibTableColumn
rmcDemandNoActivity = _RmcDemandNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 7),
    _RmcDemandNoActivity_Type()
)
rmcDemandNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDemandNoActivity.setStatus("optional")


class _RmcMinMeterTime_Type(Integer32):
    """Custom type rmcMinMeterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMinMeterTime_Type.__name__ = "Integer32"
_RmcMinMeterTime_Object = MibTableColumn
rmcMinMeterTime = _RmcMinMeterTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 8),
    _RmcMinMeterTime_Type()
)
rmcMinMeterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMinMeterTime.setStatus("optional")


class _RmcMinNonMeterTime_Type(Integer32):
    """Custom type rmcMinNonMeterTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMinNonMeterTime_Type.__name__ = "Integer32"
_RmcMinNonMeterTime_Object = MibTableColumn
rmcMinNonMeterTime = _RmcMinNonMeterTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 9),
    _RmcMinNonMeterTime_Type()
)
rmcMinNonMeterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMinNonMeterTime.setStatus("optional")


class _RmcAbsoluteMinMeterRate_Type(Integer32):
    """Custom type rmcAbsoluteMinMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcAbsoluteMinMeterRate_Type.__name__ = "Integer32"
_RmcAbsoluteMinMeterRate_Object = MibTableColumn
rmcAbsoluteMinMeterRate = _RmcAbsoluteMinMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 10),
    _RmcAbsoluteMinMeterRate_Type()
)
rmcAbsoluteMinMeterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcAbsoluteMinMeterRate.setStatus("mandatory")


class _RmcAbsoluteMaxMeterRate_Type(Integer32):
    """Custom type rmcAbsoluteMaxMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcAbsoluteMaxMeterRate_Type.__name__ = "Integer32"
_RmcAbsoluteMaxMeterRate_Object = MibTableColumn
rmcAbsoluteMaxMeterRate = _RmcAbsoluteMaxMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 11),
    _RmcAbsoluteMaxMeterRate_Type()
)
rmcAbsoluteMaxMeterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcAbsoluteMaxMeterRate.setStatus("mandatory")


class _RmcSystemMinMeterRate_Type(Integer32):
    """Custom type rmcSystemMinMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcSystemMinMeterRate_Type.__name__ = "Integer32"
_RmcSystemMinMeterRate_Object = MibTableColumn
rmcSystemMinMeterRate = _RmcSystemMinMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 12),
    _RmcSystemMinMeterRate_Type()
)
rmcSystemMinMeterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcSystemMinMeterRate.setStatus("optional")


class _RmcSystemMaxMeterRate_Type(Integer32):
    """Custom type rmcSystemMaxMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcSystemMaxMeterRate_Type.__name__ = "Integer32"
_RmcSystemMaxMeterRate_Object = MibTableColumn
rmcSystemMaxMeterRate = _RmcSystemMaxMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 13),
    _RmcSystemMaxMeterRate_Type()
)
rmcSystemMaxMeterRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcSystemMaxMeterRate.setStatus("optional")


class _RmcStartAlert_Type(Integer32):
    """Custom type rmcStartAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcStartAlert_Type.__name__ = "Integer32"
_RmcStartAlert_Object = MibTableColumn
rmcStartAlert = _RmcStartAlert_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 14),
    _RmcStartAlert_Type()
)
rmcStartAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartAlert.setStatus("mandatory")


class _RmcStartWarning_Type(Integer32):
    """Custom type rmcStartWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcStartWarning_Type.__name__ = "Integer32"
_RmcStartWarning_Object = MibTableColumn
rmcStartWarning = _RmcStartWarning_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 15),
    _RmcStartWarning_Type()
)
rmcStartWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartWarning.setStatus("mandatory")


class _RmcStartGreen_Type(Integer32):
    """Custom type rmcStartGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcStartGreen_Type.__name__ = "Integer32"
_RmcStartGreen_Object = MibTableColumn
rmcStartGreen = _RmcStartGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 16),
    _RmcStartGreen_Type()
)
rmcStartGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartGreen.setStatus("mandatory")


class _RmcStartGapTime_Type(Integer32):
    """Custom type rmcStartGapTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcStartGapTime_Type.__name__ = "Integer32"
_RmcStartGapTime_Object = MibTableColumn
rmcStartGapTime = _RmcStartGapTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 17),
    _RmcStartGapTime_Type()
)
rmcStartGapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartGapTime.setStatus("optional")


class _RmcStartGapQueueDetectorNum_Type(Integer32):
    """Custom type rmcStartGapQueueDetectorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcStartGapQueueDetectorNum_Type.__name__ = "Integer32"
_RmcStartGapQueueDetectorNum_Object = MibTableColumn
rmcStartGapQueueDetectorNum = _RmcStartGapQueueDetectorNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 18),
    _RmcStartGapQueueDetectorNum_Type()
)
rmcStartGapQueueDetectorNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartGapQueueDetectorNum.setStatus("optional")


class _RmcStartYellow_Type(Integer32):
    """Custom type rmcStartYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcStartYellow_Type.__name__ = "Integer32"
_RmcStartYellow_Object = MibTableColumn
rmcStartYellow = _RmcStartYellow_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 19),
    _RmcStartYellow_Type()
)
rmcStartYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartYellow.setStatus("mandatory")


class _RmcStartRed_Type(Integer32):
    """Custom type rmcStartRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcStartRed_Type.__name__ = "Integer32"
_RmcStartRed_Object = MibTableColumn
rmcStartRed = _RmcStartRed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 20),
    _RmcStartRed_Type()
)
rmcStartRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcStartRed.setStatus("mandatory")


class _RmcMinRed_Type(Integer32):
    """Custom type rmcMinRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMinRed_Type.__name__ = "Integer32"
_RmcMinRed_Object = MibTableColumn
rmcMinRed = _RmcMinRed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 21),
    _RmcMinRed_Type()
)
rmcMinRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMinRed.setStatus("mandatory")


class _RmcRedViolationClearance_Type(Integer32):
    """Custom type rmcRedViolationClearance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcRedViolationClearance_Type.__name__ = "Integer32"
_RmcRedViolationClearance_Object = MibTableColumn
rmcRedViolationClearance = _RmcRedViolationClearance_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 22),
    _RmcRedViolationClearance_Type()
)
rmcRedViolationClearance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcRedViolationClearance.setStatus("optional")


class _RmcRedViolationAdjust_Type(Integer32):
    """Custom type rmcRedViolationAdjust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcRedViolationAdjust_Type.__name__ = "Integer32"
_RmcRedViolationAdjust_Object = MibTableColumn
rmcRedViolationAdjust = _RmcRedViolationAdjust_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 23),
    _RmcRedViolationAdjust_Type()
)
rmcRedViolationAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcRedViolationAdjust.setStatus("optional")


class _RmcMinGreen_Type(Integer32):
    """Custom type rmcMinGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMinGreen_Type.__name__ = "Integer32"
_RmcMinGreen_Object = MibTableColumn
rmcMinGreen = _RmcMinGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 24),
    _RmcMinGreen_Type()
)
rmcMinGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMinGreen.setStatus("mandatory")


class _RmcMaxGreen_Type(Integer32):
    """Custom type rmcMaxGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxGreen_Type.__name__ = "Integer32"
_RmcMaxGreen_Object = MibTableColumn
rmcMaxGreen = _RmcMaxGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 25),
    _RmcMaxGreen_Type()
)
rmcMaxGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMaxGreen.setStatus("mandatory")


class _RmcYellow_Type(Integer32):
    """Custom type rmcYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcYellow_Type.__name__ = "Integer32"
_RmcYellow_Object = MibTableColumn
rmcYellow = _RmcYellow_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 26),
    _RmcYellow_Type()
)
rmcYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcYellow.setStatus("mandatory")


class _RmcShortStopTime_Type(Integer32):
    """Custom type rmcShortStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcShortStopTime_Type.__name__ = "Integer32"
_RmcShortStopTime_Object = MibTableColumn
rmcShortStopTime = _RmcShortStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 27),
    _RmcShortStopTime_Type()
)
rmcShortStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShortStopTime.setStatus("optional")


class _RmcShortStopOccupancy_Type(Integer32):
    """Custom type rmcShortStopOccupancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcShortStopOccupancy_Type.__name__ = "Integer32"
_RmcShortStopOccupancy_Object = MibTableColumn
rmcShortStopOccupancy = _RmcShortStopOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 28),
    _RmcShortStopOccupancy_Type()
)
rmcShortStopOccupancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShortStopOccupancy.setStatus("optional")


class _RmcShortStopQueueDetectorNum_Type(Integer32):
    """Custom type rmcShortStopQueueDetectorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcShortStopQueueDetectorNum_Type.__name__ = "Integer32"
_RmcShortStopQueueDetectorNum_Object = MibTableColumn
rmcShortStopQueueDetectorNum = _RmcShortStopQueueDetectorNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 29),
    _RmcShortStopQueueDetectorNum_Type()
)
rmcShortStopQueueDetectorNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShortStopQueueDetectorNum.setStatus("optional")


class _RmcLongStopTime_Type(Integer32):
    """Custom type rmcLongStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcLongStopTime_Type.__name__ = "Integer32"
_RmcLongStopTime_Object = MibTableColumn
rmcLongStopTime = _RmcLongStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 30),
    _RmcLongStopTime_Type()
)
rmcLongStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcLongStopTime.setStatus("optional")


class _RmcDemandGap_Type(Integer32):
    """Custom type rmcDemandGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDemandGap_Type.__name__ = "Integer32"
_RmcDemandGap_Object = MibTableColumn
rmcDemandGap = _RmcDemandGap_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 31),
    _RmcDemandGap_Type()
)
rmcDemandGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDemandGap.setStatus("optional")


class _RmcDemandRed_Type(Integer32):
    """Custom type rmcDemandRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDemandRed_Type.__name__ = "Integer32"
_RmcDemandRed_Object = MibTableColumn
rmcDemandRed = _RmcDemandRed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 32),
    _RmcDemandRed_Type()
)
rmcDemandRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDemandRed.setStatus("optional")


class _RmcShutNormalRate_Type(Integer32):
    """Custom type rmcShutNormalRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcShutNormalRate_Type.__name__ = "Integer32"
_RmcShutNormalRate_Object = MibTableColumn
rmcShutNormalRate = _RmcShutNormalRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 33),
    _RmcShutNormalRate_Type()
)
rmcShutNormalRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShutNormalRate.setStatus("mandatory")


class _RmcShutWarning_Type(Integer32):
    """Custom type rmcShutWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcShutWarning_Type.__name__ = "Integer32"
_RmcShutWarning_Object = MibTableColumn
rmcShutWarning = _RmcShutWarning_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 34),
    _RmcShutWarning_Type()
)
rmcShutWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShutWarning.setStatus("mandatory")


class _RmcShutTime_Type(Integer32):
    """Custom type rmcShutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcShutTime_Type.__name__ = "Integer32"
_RmcShutTime_Object = MibTableColumn
rmcShutTime = _RmcShutTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 35),
    _RmcShutTime_Type()
)
rmcShutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShutTime.setStatus("mandatory")


class _RmcPostMeterGreen_Type(Integer32):
    """Custom type rmcPostMeterGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcPostMeterGreen_Type.__name__ = "Integer32"
_RmcPostMeterGreen_Object = MibTableColumn
rmcPostMeterGreen = _RmcPostMeterGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 36),
    _RmcPostMeterGreen_Type()
)
rmcPostMeterGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPostMeterGreen.setStatus("mandatory")


class _RmcQueueViolationFlag_Type(Integer32):
    """Custom type rmcQueueViolationFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcQueueViolationFlag_Type.__name__ = "Integer32"
_RmcQueueViolationFlag_Object = MibTableColumn
rmcQueueViolationFlag = _RmcQueueViolationFlag_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 37),
    _RmcQueueViolationFlag_Type()
)
rmcQueueViolationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueViolationFlag.setStatus("optional")


class _RmcQueueShutdownFlag_Type(Integer32):
    """Custom type rmcQueueShutdownFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcQueueShutdownFlag_Type.__name__ = "Integer32"
_RmcQueueShutdownFlag_Object = MibTableColumn
rmcQueueShutdownFlag = _RmcQueueShutdownFlag_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 38),
    _RmcQueueShutdownFlag_Type()
)
rmcQueueShutdownFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueShutdownFlag.setStatus("optional")


class _RmcQueueAdjustUsage_Type(Integer32):
    """Custom type rmcQueueAdjustUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("additive", 1),
          ("additiveXI", 2),
          ("priorityXI", 3))
    )


_RmcQueueAdjustUsage_Type.__name__ = "Integer32"
_RmcQueueAdjustUsage_Object = MibTableColumn
rmcQueueAdjustUsage = _RmcQueueAdjustUsage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 3, 1, 39),
    _RmcQueueAdjustUsage_Type()
)
rmcQueueAdjustUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustUsage.setStatus("mandatory")
_RmcMeterCtrlTable_Object = MibTable
rmcMeterCtrlTable = _RmcMeterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    rmcMeterCtrlTable.setStatus("mandatory")
_RmcMeterCtrlEntry_Object = MibTableRow
rmcMeterCtrlEntry = _RmcMeterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1)
)
rmcMeterCtrlEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcMeterCtrlEntry.setStatus("mandatory")


class _RmcMeterMode_Type(Integer32):
    """Custom type rmcMeterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcMeterMode_Type.__name__ = "Integer32"
_RmcMeterMode_Object = MibTableColumn
rmcMeterMode = _RmcMeterMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 1),
    _RmcMeterMode_Type()
)
rmcMeterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterMode.setStatus("mandatory")


class _RmcManualAction_Type(Integer32):
    """Custom type rmcManualAction based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("skip", 6))
    )


_RmcManualAction_Type.__name__ = "Integer32"
_RmcManualAction_Object = MibTableColumn
rmcManualAction = _RmcManualAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 2),
    _RmcManualAction_Type()
)
rmcManualAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcManualAction.setStatus("optional")


class _RmcManualPlan_Type(Integer32):
    """Custom type rmcManualPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcManualPlan_Type.__name__ = "Integer32"
_RmcManualPlan_Object = MibTableColumn
rmcManualPlan = _RmcManualPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 3),
    _RmcManualPlan_Type()
)
rmcManualPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcManualPlan.setStatus("optional")


class _RmcManualRate_Type(Integer32):
    """Custom type rmcManualRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcManualRate_Type.__name__ = "Integer32"
_RmcManualRate_Object = MibTableColumn
rmcManualRate = _RmcManualRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 4),
    _RmcManualRate_Type()
)
rmcManualRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcManualRate.setStatus("optional")


class _RmcManualVehiclesPerGrn_Type(Integer32):
    """Custom type rmcManualVehiclesPerGrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcManualVehiclesPerGrn_Type.__name__ = "Integer32"
_RmcManualVehiclesPerGrn_Object = MibTableColumn
rmcManualVehiclesPerGrn = _RmcManualVehiclesPerGrn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 5),
    _RmcManualVehiclesPerGrn_Type()
)
rmcManualVehiclesPerGrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcManualVehiclesPerGrn.setStatus("optional")


class _RmcIntercoAction_Type(Integer32):
    """Custom type rmcIntercoAction based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("skip", 6))
    )


_RmcIntercoAction_Type.__name__ = "Integer32"
_RmcIntercoAction_Object = MibTableColumn
rmcIntercoAction = _RmcIntercoAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 6),
    _RmcIntercoAction_Type()
)
rmcIntercoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcIntercoAction.setStatus("optional")


class _RmcIntercoPlan_Type(Integer32):
    """Custom type rmcIntercoPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcIntercoPlan_Type.__name__ = "Integer32"
_RmcIntercoPlan_Object = MibTableColumn
rmcIntercoPlan = _RmcIntercoPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 7),
    _RmcIntercoPlan_Type()
)
rmcIntercoPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcIntercoPlan.setStatus("optional")


class _RmcIntercoRate_Type(Integer32):
    """Custom type rmcIntercoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcIntercoRate_Type.__name__ = "Integer32"
_RmcIntercoRate_Object = MibTableColumn
rmcIntercoRate = _RmcIntercoRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 8),
    _RmcIntercoRate_Type()
)
rmcIntercoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcIntercoRate.setStatus("optional")


class _RmcIntercoVehiclesPerGrn_Type(Integer32):
    """Custom type rmcIntercoVehiclesPerGrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcIntercoVehiclesPerGrn_Type.__name__ = "Integer32"
_RmcIntercoVehiclesPerGrn_Object = MibTableColumn
rmcIntercoVehiclesPerGrn = _RmcIntercoVehiclesPerGrn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 9),
    _RmcIntercoVehiclesPerGrn_Type()
)
rmcIntercoVehiclesPerGrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcIntercoVehiclesPerGrn.setStatus("optional")


class _RmcCommActionStatus_Type(Integer32):
    """Custom type rmcCommActionStatus based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("skip", 6))
    )


_RmcCommActionStatus_Type.__name__ = "Integer32"
_RmcCommActionStatus_Object = MibTableColumn
rmcCommActionStatus = _RmcCommActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 10),
    _RmcCommActionStatus_Type()
)
rmcCommActionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCommActionStatus.setStatus("optional")


class _RmcCommPlan_Type(Integer32):
    """Custom type rmcCommPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcCommPlan_Type.__name__ = "Integer32"
_RmcCommPlan_Object = MibTableColumn
rmcCommPlan = _RmcCommPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 11),
    _RmcCommPlan_Type()
)
rmcCommPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCommPlan.setStatus("optional")


class _RmcCommRate_Type(Integer32):
    """Custom type rmcCommRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcCommRate_Type.__name__ = "Integer32"
_RmcCommRate_Object = MibTableColumn
rmcCommRate = _RmcCommRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 12),
    _RmcCommRate_Type()
)
rmcCommRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCommRate.setStatus("optional")


class _RmcCommVehiclesPerGrn_Type(Integer32):
    """Custom type rmcCommVehiclesPerGrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcCommVehiclesPerGrn_Type.__name__ = "Integer32"
_RmcCommVehiclesPerGrn_Object = MibTableColumn
rmcCommVehiclesPerGrn = _RmcCommVehiclesPerGrn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 13),
    _RmcCommVehiclesPerGrn_Type()
)
rmcCommVehiclesPerGrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcCommVehiclesPerGrn.setStatus("optional")


class _RmcDefaultAction_Type(Integer32):
    """Custom type rmcDefaultAction based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5))
    )


_RmcDefaultAction_Type.__name__ = "Integer32"
_RmcDefaultAction_Object = MibTableColumn
rmcDefaultAction = _RmcDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 14),
    _RmcDefaultAction_Type()
)
rmcDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDefaultAction.setStatus("mandatory")


class _RmcDefaultPlan_Type(Integer32):
    """Custom type rmcDefaultPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDefaultPlan_Type.__name__ = "Integer32"
_RmcDefaultPlan_Object = MibTableColumn
rmcDefaultPlan = _RmcDefaultPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 15),
    _RmcDefaultPlan_Type()
)
rmcDefaultPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDefaultPlan.setStatus("mandatory")


class _RmcDefaultRate_Type(Integer32):
    """Custom type rmcDefaultRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcDefaultRate_Type.__name__ = "Integer32"
_RmcDefaultRate_Object = MibTableColumn
rmcDefaultRate = _RmcDefaultRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 16),
    _RmcDefaultRate_Type()
)
rmcDefaultRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDefaultRate.setStatus("mandatory")


class _RmcDefaultVehiclesPerGrn_Type(Integer32):
    """Custom type rmcDefaultVehiclesPerGrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDefaultVehiclesPerGrn_Type.__name__ = "Integer32"
_RmcDefaultVehiclesPerGrn_Object = MibTableColumn
rmcDefaultVehiclesPerGrn = _RmcDefaultVehiclesPerGrn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 17),
    _RmcDefaultVehiclesPerGrn_Type()
)
rmcDefaultVehiclesPerGrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDefaultVehiclesPerGrn.setStatus("mandatory")


class _RmcDemandMode_Type(Integer32):
    """Custom type rmcDemandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("recalled", 1),
          ("enabledCall", 2),
          ("enabledStop", 3))
    )


_RmcDemandMode_Type.__name__ = "Integer32"
_RmcDemandMode_Object = MibTableColumn
rmcDemandMode = _RmcDemandMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 7, 1, 18),
    _RmcDemandMode_Type()
)
rmcDemandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDemandMode.setStatus("mandatory")
_RmcMeterStatTable_Object = MibTable
rmcMeterStatTable = _RmcMeterStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8)
)
if mibBuilder.loadTexts:
    rmcMeterStatTable.setStatus("mandatory")
_RmcMeterStatEntry_Object = MibTableRow
rmcMeterStatEntry = _RmcMeterStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1)
)
rmcMeterStatEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcMeterStatEntry.setStatus("mandatory")


class _RmcRequestCommandSource_Type(Integer32):
    """Custom type rmcRequestCommandSource based on Integer32"""
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
        *(("manual", 1),
          ("communications", 2),
          ("interconnect", 3),
          ("timebaseControl", 4),
          ("default", 5))
    )


_RmcRequestCommandSource_Type.__name__ = "Integer32"
_RmcRequestCommandSource_Object = MibTableColumn
rmcRequestCommandSource = _RmcRequestCommandSource_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 1),
    _RmcRequestCommandSource_Type()
)
rmcRequestCommandSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcRequestCommandSource.setStatus("mandatory")


class _RmcImplementCommandSource_Type(Integer32):
    """Custom type rmcImplementCommandSource based on Integer32"""
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
        *(("manual", 1),
          ("communications", 2),
          ("interconnect", 3),
          ("timebaseControl", 4),
          ("default", 5))
    )


_RmcImplementCommandSource_Type.__name__ = "Integer32"
_RmcImplementCommandSource_Object = MibTableColumn
rmcImplementCommandSource = _RmcImplementCommandSource_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 2),
    _RmcImplementCommandSource_Type()
)
rmcImplementCommandSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcImplementCommandSource.setStatus("mandatory")


class _RmcImplementAction_Type(Integer32):
    """Custom type rmcImplementAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("holdMeter", 6),
          ("holdNonMeter", 7),
          ("holdRestInGreen", 8))
    )


_RmcImplementAction_Type.__name__ = "Integer32"
_RmcImplementAction_Object = MibTableColumn
rmcImplementAction = _RmcImplementAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 3),
    _RmcImplementAction_Type()
)
rmcImplementAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcImplementAction.setStatus("mandatory")


class _RmcImplementPlan_Type(Integer32):
    """Custom type rmcImplementPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcImplementPlan_Type.__name__ = "Integer32"
_RmcImplementPlan_Object = MibTableColumn
rmcImplementPlan = _RmcImplementPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 4),
    _RmcImplementPlan_Type()
)
rmcImplementPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcImplementPlan.setStatus("mandatory")


class _RmcImplementRate_Type(Integer32):
    """Custom type rmcImplementRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcImplementRate_Type.__name__ = "Integer32"
_RmcImplementRate_Object = MibTableColumn
rmcImplementRate = _RmcImplementRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 5),
    _RmcImplementRate_Type()
)
rmcImplementRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcImplementRate.setStatus("mandatory")


class _RmcImplementVehiclesPerGrn_Type(Integer32):
    """Custom type rmcImplementVehiclesPerGrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcImplementVehiclesPerGrn_Type.__name__ = "Integer32"
_RmcImplementVehiclesPerGrn_Object = MibTableColumn
rmcImplementVehiclesPerGrn = _RmcImplementVehiclesPerGrn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 6),
    _RmcImplementVehiclesPerGrn_Type()
)
rmcImplementVehiclesPerGrn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcImplementVehiclesPerGrn.setStatus("mandatory")


class _RmcRequestAction_Type(Integer32):
    """Custom type rmcRequestAction based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5))
    )


_RmcRequestAction_Type.__name__ = "Integer32"
_RmcRequestAction_Object = MibTableColumn
rmcRequestAction = _RmcRequestAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 7),
    _RmcRequestAction_Type()
)
rmcRequestAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcRequestAction.setStatus("mandatory")


class _RmcRequestPlan_Type(Integer32):
    """Custom type rmcRequestPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcRequestPlan_Type.__name__ = "Integer32"
_RmcRequestPlan_Object = MibTableColumn
rmcRequestPlan = _RmcRequestPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 8),
    _RmcRequestPlan_Type()
)
rmcRequestPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcRequestPlan.setStatus("mandatory")


class _RmcRequestRate_Type(Integer32):
    """Custom type rmcRequestRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcRequestRate_Type.__name__ = "Integer32"
_RmcRequestRate_Object = MibTableColumn
rmcRequestRate = _RmcRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 9),
    _RmcRequestRate_Type()
)
rmcRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcRequestRate.setStatus("mandatory")


class _RmcRequestVehiclesPerGrn_Type(Integer32):
    """Custom type rmcRequestVehiclesPerGrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcRequestVehiclesPerGrn_Type.__name__ = "Integer32"
_RmcRequestVehiclesPerGrn_Object = MibTableColumn
rmcRequestVehiclesPerGrn = _RmcRequestVehiclesPerGrn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 10),
    _RmcRequestVehiclesPerGrn_Type()
)
rmcRequestVehiclesPerGrn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcRequestVehiclesPerGrn.setStatus("mandatory")


class _RmcCommAction_Type(Integer32):
    """Custom type rmcCommAction based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("skip", 6),
          ("noComm", 7))
    )


_RmcCommAction_Type.__name__ = "Integer32"
_RmcCommAction_Object = MibTableColumn
rmcCommAction = _RmcCommAction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 11),
    _RmcCommAction_Type()
)
rmcCommAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcCommAction.setStatus("optional")


class _RmcBaseMeterRate_Type(Integer32):
    """Custom type rmcBaseMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcBaseMeterRate_Type.__name__ = "Integer32"
_RmcBaseMeterRate_Object = MibTableColumn
rmcBaseMeterRate = _RmcBaseMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 12),
    _RmcBaseMeterRate_Type()
)
rmcBaseMeterRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcBaseMeterRate.setStatus("optional")


class _RmcActiveMeterRate_Type(Integer32):
    """Custom type rmcActiveMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcActiveMeterRate_Type.__name__ = "Integer32"
_RmcActiveMeterRate_Object = MibTableColumn
rmcActiveMeterRate = _RmcActiveMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 13),
    _RmcActiveMeterRate_Type()
)
rmcActiveMeterRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcActiveMeterRate.setStatus("mandatory")


class _RmcTBActionStatus_Type(Integer32):
    """Custom type rmcTBActionStatus based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("skip", 6))
    )


_RmcTBActionStatus_Type.__name__ = "Integer32"
_RmcTBActionStatus_Object = MibTableColumn
rmcTBActionStatus = _RmcTBActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 14),
    _RmcTBActionStatus_Type()
)
rmcTBActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcTBActionStatus.setStatus("optional")


class _RmcTBPlanStatus_Type(Integer32):
    """Custom type rmcTBPlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcTBPlanStatus_Type.__name__ = "Integer32"
_RmcTBPlanStatus_Object = MibTableColumn
rmcTBPlanStatus = _RmcTBPlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 15),
    _RmcTBPlanStatus_Type()
)
rmcTBPlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcTBPlanStatus.setStatus("optional")


class _RmcTBRateStatus_Type(Integer32):
    """Custom type rmcTBRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcTBRateStatus_Type.__name__ = "Integer32"
_RmcTBRateStatus_Object = MibTableColumn
rmcTBRateStatus = _RmcTBRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 16),
    _RmcTBRateStatus_Type()
)
rmcTBRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcTBRateStatus.setStatus("optional")


class _RmcTBVehiclesPerGrnStatus_Type(Integer32):
    """Custom type rmcTBVehiclesPerGrnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcTBVehiclesPerGrnStatus_Type.__name__ = "Integer32"
_RmcTBVehiclesPerGrnStatus_Object = MibTableColumn
rmcTBVehiclesPerGrnStatus = _RmcTBVehiclesPerGrnStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 17),
    _RmcTBVehiclesPerGrnStatus_Type()
)
rmcTBVehiclesPerGrnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcTBVehiclesPerGrnStatus.setStatus("optional")


class _RmcActiveInterval_Type(Integer32):
    """Custom type rmcActiveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("initialization", 1),
          ("preMeteringNonGreen", 2),
          ("preMeteringGreen", 3),
          ("startupAlert", 4),
          ("startupWarning", 5),
          ("startupGreen", 6),
          ("startupYellow", 7),
          ("startupRed", 8),
          ("red", 9),
          ("green", 10),
          ("yellow", 11),
          ("shutdownGreen", 12),
          ("shutdownYellow", 13),
          ("shutdownRed", 14),
          ("shutdownWarning", 15),
          ("postMeteringGreen", 16))
    )


_RmcActiveInterval_Type.__name__ = "Integer32"
_RmcActiveInterval_Object = MibTableColumn
rmcActiveInterval = _RmcActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 18),
    _RmcActiveInterval_Type()
)
rmcActiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcActiveInterval.setStatus("optional")


class _RmcTBCMinMeterRateStatus_Type(Integer32):
    """Custom type rmcTBCMinMeterRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcTBCMinMeterRateStatus_Type.__name__ = "Integer32"
_RmcTBCMinMeterRateStatus_Object = MibTableColumn
rmcTBCMinMeterRateStatus = _RmcTBCMinMeterRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 19),
    _RmcTBCMinMeterRateStatus_Type()
)
rmcTBCMinMeterRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcTBCMinMeterRateStatus.setStatus("optional")


class _RmcTBCMaxMeterRateStatus_Type(Integer32):
    """Custom type rmcTBCMaxMeterRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcTBCMaxMeterRateStatus_Type.__name__ = "Integer32"
_RmcTBCMaxMeterRateStatus_Object = MibTableColumn
rmcTBCMaxMeterRateStatus = _RmcTBCMaxMeterRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 20),
    _RmcTBCMaxMeterRateStatus_Type()
)
rmcTBCMaxMeterRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcTBCMaxMeterRateStatus.setStatus("optional")


class _RmcOperMinMeterRateStatus_Type(Integer32):
    """Custom type rmcOperMinMeterRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcOperMinMeterRateStatus_Type.__name__ = "Integer32"
_RmcOperMinMeterRateStatus_Object = MibTableColumn
rmcOperMinMeterRateStatus = _RmcOperMinMeterRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 21),
    _RmcOperMinMeterRateStatus_Type()
)
rmcOperMinMeterRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcOperMinMeterRateStatus.setStatus("optional")


class _RmcOperMaxMeterRateStatus_Type(Integer32):
    """Custom type rmcOperMaxMeterRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcOperMaxMeterRateStatus_Type.__name__ = "Integer32"
_RmcOperMaxMeterRateStatus_Object = MibTableColumn
rmcOperMaxMeterRateStatus = _RmcOperMaxMeterRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 22),
    _RmcOperMaxMeterRateStatus_Type()
)
rmcOperMaxMeterRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcOperMaxMeterRateStatus.setStatus("optional")


class _RmcDemandStatus_Type(Integer32):
    """Custom type rmcDemandStatus based on Integer32"""
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
        *(("recalled", 1),
          ("working", 2),
          ("otherError", 3),
          ("erraticCount", 4),
          ("maxPresence", 5),
          ("noActivity", 6),
          ("errorAtSensor", 7))
    )


_RmcDemandStatus_Type.__name__ = "Integer32"
_RmcDemandStatus_Object = MibTableColumn
rmcDemandStatus = _RmcDemandStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 1, 8, 1, 23),
    _RmcDemandStatus_Type()
)
rmcDemandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcDemandStatus.setStatus("mandatory")
_RmcDependGroup_ObjectIdentity = ObjectIdentity
rmcDependGroup = _RmcDependGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2)
)


class _RmcMaxNumDependGroup_Type(Integer32):
    """Custom type rmcMaxNumDependGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMaxNumDependGroup_Type.__name__ = "Integer32"
_RmcMaxNumDependGroup_Object = MibScalar
rmcMaxNumDependGroup = _RmcMaxNumDependGroup_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 1),
    _RmcMaxNumDependGroup_Type()
)
rmcMaxNumDependGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMaxNumDependGroup.setStatus("mandatory")


class _RmcNumDependGroup_Type(Integer32):
    """Custom type rmcNumDependGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcNumDependGroup_Type.__name__ = "Integer32"
_RmcNumDependGroup_Object = MibScalar
rmcNumDependGroup = _RmcNumDependGroup_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 2),
    _RmcNumDependGroup_Type()
)
rmcNumDependGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcNumDependGroup.setStatus("mandatory")
_RmcDependGroupCtrlTable_Object = MibTable
rmcDependGroupCtrlTable = _RmcDependGroupCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    rmcDependGroupCtrlTable.setStatus("mandatory")
_RmcDependGroupCtrlEntry_Object = MibTableRow
rmcDependGroupCtrlEntry = _RmcDependGroupCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1)
)
rmcDependGroupCtrlEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcDependGroupNumber"),
)
if mibBuilder.loadTexts:
    rmcDependGroupCtrlEntry.setStatus("mandatory")


class _RmcDependGroupMode_Type(Integer32):
    """Custom type rmcDependGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcDependGroupMode_Type.__name__ = "Integer32"
_RmcDependGroupMode_Object = MibTableColumn
rmcDependGroupMode = _RmcDependGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 1),
    _RmcDependGroupMode_Type()
)
rmcDependGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDependGroupMode.setStatus("mandatory")


class _RmcSignalServiceMode_Type(Integer32):
    """Custom type rmcSignalServiceMode based on Integer32"""
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
        *(("none", 1),
          ("mutex", 2),
          ("fixedOffset", 3),
          ("fractionalOffset", 4))
    )


_RmcSignalServiceMode_Type.__name__ = "Integer32"
_RmcSignalServiceMode_Object = MibTableColumn
rmcSignalServiceMode = _RmcSignalServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 2),
    _RmcSignalServiceMode_Type()
)
rmcSignalServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcSignalServiceMode.setStatus("mandatory")


class _RmcShutGapTime_Type(Integer32):
    """Custom type rmcShutGapTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcShutGapTime_Type.__name__ = "Integer32"
_RmcShutGapTime_Object = MibTableColumn
rmcShutGapTime = _RmcShutGapTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 3),
    _RmcShutGapTime_Type()
)
rmcShutGapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShutGapTime.setStatus("optional")


class _RmcShutGapReductTime_Type(Integer32):
    """Custom type rmcShutGapReductTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcShutGapReductTime_Type.__name__ = "Integer32"
_RmcShutGapReductTime_Object = MibTableColumn
rmcShutGapReductTime = _RmcShutGapReductTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 4),
    _RmcShutGapReductTime_Type()
)
rmcShutGapReductTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShutGapReductTime.setStatus("optional")


class _RmcShutGapReductValue_Type(Integer32):
    """Custom type rmcShutGapReductValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcShutGapReductValue_Type.__name__ = "Integer32"
_RmcShutGapReductValue_Object = MibTableColumn
rmcShutGapReductValue = _RmcShutGapReductValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 5),
    _RmcShutGapReductValue_Type()
)
rmcShutGapReductValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcShutGapReductValue.setStatus("optional")


class _RmcGreenOffset_Type(Integer32):
    """Custom type rmcGreenOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcGreenOffset_Type.__name__ = "Integer32"
_RmcGreenOffset_Object = MibTableColumn
rmcGreenOffset = _RmcGreenOffset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 6),
    _RmcGreenOffset_Type()
)
rmcGreenOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcGreenOffset.setStatus("optional")


class _RmcMinFractionalOffset_Type(Integer32):
    """Custom type rmcMinFractionalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMinFractionalOffset_Type.__name__ = "Integer32"
_RmcMinFractionalOffset_Object = MibTableColumn
rmcMinFractionalOffset = _RmcMinFractionalOffset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 7),
    _RmcMinFractionalOffset_Type()
)
rmcMinFractionalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMinFractionalOffset.setStatus("optional")


class _RmcPriorityLaneNum_Type(Integer32):
    """Custom type rmcPriorityLaneNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcPriorityLaneNum_Type.__name__ = "Integer32"
_RmcPriorityLaneNum_Object = MibTableColumn
rmcPriorityLaneNum = _RmcPriorityLaneNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 8),
    _RmcPriorityLaneNum_Type()
)
rmcPriorityLaneNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPriorityLaneNum.setStatus("optional")


class _RmcPriorityRedDelay_Type(Integer32):
    """Custom type rmcPriorityRedDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcPriorityRedDelay_Type.__name__ = "Integer32"
_RmcPriorityRedDelay_Object = MibTableColumn
rmcPriorityRedDelay = _RmcPriorityRedDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 9),
    _RmcPriorityRedDelay_Type()
)
rmcPriorityRedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPriorityRedDelay.setStatus("optional")


class _RmcMergeMode_Type(Integer32):
    """Custom type rmcMergeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcMergeMode_Type.__name__ = "Integer32"
_RmcMergeMode_Object = MibTableColumn
rmcMergeMode = _RmcMergeMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 10),
    _RmcMergeMode_Type()
)
rmcMergeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMergeMode.setStatus("optional")


class _RmcMergeGap_Type(Integer32):
    """Custom type rmcMergeGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMergeGap_Type.__name__ = "Integer32"
_RmcMergeGap_Object = MibTableColumn
rmcMergeGap = _RmcMergeGap_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 11),
    _RmcMergeGap_Type()
)
rmcMergeGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMergeGap.setStatus("optional")


class _RmcMergeDelay_Type(Integer32):
    """Custom type rmcMergeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMergeDelay_Type.__name__ = "Integer32"
_RmcMergeDelay_Object = MibTableColumn
rmcMergeDelay = _RmcMergeDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 12),
    _RmcMergeDelay_Type()
)
rmcMergeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMergeDelay.setStatus("optional")


class _RmcQueueMergeFlag_Type(Integer32):
    """Custom type rmcQueueMergeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcQueueMergeFlag_Type.__name__ = "Integer32"
_RmcQueueMergeFlag_Object = MibTableColumn
rmcQueueMergeFlag = _RmcQueueMergeFlag_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 13),
    _RmcQueueMergeFlag_Type()
)
rmcQueueMergeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueMergeFlag.setStatus("optional")


class _RmcMergeErraticCount_Type(Integer32):
    """Custom type rmcMergeErraticCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMergeErraticCount_Type.__name__ = "Integer32"
_RmcMergeErraticCount_Object = MibTableColumn
rmcMergeErraticCount = _RmcMergeErraticCount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 14),
    _RmcMergeErraticCount_Type()
)
rmcMergeErraticCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMergeErraticCount.setStatus("optional")


class _RmcMergeMaxPresence_Type(Integer32):
    """Custom type rmcMergeMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcMergeMaxPresence_Type.__name__ = "Integer32"
_RmcMergeMaxPresence_Object = MibTableColumn
rmcMergeMaxPresence = _RmcMergeMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 15),
    _RmcMergeMaxPresence_Type()
)
rmcMergeMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMergeMaxPresence.setStatus("optional")


class _RmcMergeNoActivity_Type(Integer32):
    """Custom type rmcMergeNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcMergeNoActivity_Type.__name__ = "Integer32"
_RmcMergeNoActivity_Object = MibTableColumn
rmcMergeNoActivity = _RmcMergeNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 3, 1, 16),
    _RmcMergeNoActivity_Type()
)
rmcMergeNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMergeNoActivity.setStatus("optional")
_RmcDependGroupStatTable_Object = MibTable
rmcDependGroupStatTable = _RmcDependGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 4)
)
if mibBuilder.loadTexts:
    rmcDependGroupStatTable.setStatus("mandatory")
_RmcDependGroupStatEntry_Object = MibTableRow
rmcDependGroupStatEntry = _RmcDependGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 4, 1)
)
rmcDependGroupStatEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcDependGroupNumber"),
)
if mibBuilder.loadTexts:
    rmcDependGroupStatEntry.setStatus("mandatory")


class _RmcMergeFlag_Type(Integer32):
    """Custom type rmcMergeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcMergeFlag_Type.__name__ = "Integer32"
_RmcMergeFlag_Object = MibTableColumn
rmcMergeFlag = _RmcMergeFlag_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 4, 1, 1),
    _RmcMergeFlag_Type()
)
rmcMergeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMergeFlag.setStatus("optional")


class _RmcMergeStatus_Type(Integer32):
    """Custom type rmcMergeStatus based on Integer32"""
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
        *(("disabled", 1),
          ("working", 2),
          ("otherError", 3),
          ("erraticCount", 4),
          ("maxPresence", 5),
          ("noActivity", 6),
          ("errorAtSensor", 7))
    )


_RmcMergeStatus_Type.__name__ = "Integer32"
_RmcMergeStatus_Object = MibTableColumn
rmcMergeStatus = _RmcMergeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 2, 4, 1, 2),
    _RmcMergeStatus_Type()
)
rmcMergeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMergeStatus.setStatus("optional")
_RmcQueue_ObjectIdentity = ObjectIdentity
rmcQueue = _RmcQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3)
)


class _RmcMaxNumQueueEntries_Type(Integer32):
    """Custom type rmcMaxNumQueueEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxNumQueueEntries_Type.__name__ = "Integer32"
_RmcMaxNumQueueEntries_Object = MibScalar
rmcMaxNumQueueEntries = _RmcMaxNumQueueEntries_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 1),
    _RmcMaxNumQueueEntries_Type()
)
rmcMaxNumQueueEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumQueueEntries.setStatus("mandatory")


class _RmcNumQueueEntries_Type(Integer32):
    """Custom type rmcNumQueueEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcNumQueueEntries_Type.__name__ = "Integer32"
_RmcNumQueueEntries_Object = MibScalar
rmcNumQueueEntries = _RmcNumQueueEntries_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 2),
    _RmcNumQueueEntries_Type()
)
rmcNumQueueEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumQueueEntries.setStatus("mandatory")
_RmcQueueCtrlTable_Object = MibTable
rmcQueueCtrlTable = _RmcQueueCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    rmcQueueCtrlTable.setStatus("mandatory")
_RmcQueueCtrlEntry_Object = MibTableRow
rmcQueueCtrlEntry = _RmcQueueCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1)
)
rmcQueueCtrlEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
    (0, "RMC-MIB1", "rmcQueueNum"),
)
if mibBuilder.loadTexts:
    rmcQueueCtrlEntry.setStatus("mandatory")


class _RmcQueueNum_Type(Integer32):
    """Custom type rmcQueueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcQueueNum_Type.__name__ = "Integer32"
_RmcQueueNum_Object = MibTableColumn
rmcQueueNum = _RmcQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 1),
    _RmcQueueNum_Type()
)
rmcQueueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcQueueNum.setStatus("mandatory")


class _RmcQueueType_Type(Integer32):
    """Custom type rmcQueueType based on Integer32"""
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
          ("intermediate", 2),
          ("excessive", 3))
    )


_RmcQueueType_Type.__name__ = "Integer32"
_RmcQueueType_Object = MibTableColumn
rmcQueueType = _RmcQueueType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 2),
    _RmcQueueType_Type()
)
rmcQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueType.setStatus("mandatory")


class _RmcQueueDetectMode_Type(Integer32):
    """Custom type rmcQueueDetectMode based on Integer32"""
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
        *(("disabled", 1),
          ("count", 2),
          ("occupancy", 3),
          ("quickOccupancy", 4))
    )


_RmcQueueDetectMode_Type.__name__ = "Integer32"
_RmcQueueDetectMode_Object = MibTableColumn
rmcQueueDetectMode = _RmcQueueDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 3),
    _RmcQueueDetectMode_Type()
)
rmcQueueDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueDetectMode.setStatus("mandatory")


class _RmcQueueLengthUpLimit_Type(Integer32):
    """Custom type rmcQueueLengthUpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueLengthUpLimit_Type.__name__ = "Integer32"
_RmcQueueLengthUpLimit_Object = MibTableColumn
rmcQueueLengthUpLimit = _RmcQueueLengthUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 4),
    _RmcQueueLengthUpLimit_Type()
)
rmcQueueLengthUpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueLengthUpLimit.setStatus("mandatory")


class _RmcQueueLengthLowLimit_Type(Integer32):
    """Custom type rmcQueueLengthLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueLengthLowLimit_Type.__name__ = "Integer32"
_RmcQueueLengthLowLimit_Object = MibTableColumn
rmcQueueLengthLowLimit = _RmcQueueLengthLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 5),
    _RmcQueueLengthLowLimit_Type()
)
rmcQueueLengthLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueLengthLowLimit.setStatus("mandatory")


class _RmcQueueOccUpLimit_Type(Integer32):
    """Custom type rmcQueueOccUpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueOccUpLimit_Type.__name__ = "Integer32"
_RmcQueueOccUpLimit_Object = MibTableColumn
rmcQueueOccUpLimit = _RmcQueueOccUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 6),
    _RmcQueueOccUpLimit_Type()
)
rmcQueueOccUpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueOccUpLimit.setStatus("mandatory")


class _RmcQueueOccUpDelay_Type(Integer32):
    """Custom type rmcQueueOccUpDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueOccUpDelay_Type.__name__ = "Integer32"
_RmcQueueOccUpDelay_Object = MibTableColumn
rmcQueueOccUpDelay = _RmcQueueOccUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 7),
    _RmcQueueOccUpDelay_Type()
)
rmcQueueOccUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueOccUpDelay.setStatus("mandatory")


class _RmcQueueOccLowLimit_Type(Integer32):
    """Custom type rmcQueueOccLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueOccLowLimit_Type.__name__ = "Integer32"
_RmcQueueOccLowLimit_Object = MibTableColumn
rmcQueueOccLowLimit = _RmcQueueOccLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 8),
    _RmcQueueOccLowLimit_Type()
)
rmcQueueOccLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueOccLowLimit.setStatus("mandatory")


class _RmcQueueOccLowDelay_Type(Integer32):
    """Custom type rmcQueueOccLowDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueOccLowDelay_Type.__name__ = "Integer32"
_RmcQueueOccLowDelay_Object = MibTableColumn
rmcQueueOccLowDelay = _RmcQueueOccLowDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 9),
    _RmcQueueOccLowDelay_Type()
)
rmcQueueOccLowDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueOccLowDelay.setStatus("mandatory")


class _RmcQueueQOccUpLimit_Type(Integer32):
    """Custom type rmcQueueQOccUpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueQOccUpLimit_Type.__name__ = "Integer32"
_RmcQueueQOccUpLimit_Object = MibTableColumn
rmcQueueQOccUpLimit = _RmcQueueQOccUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 10),
    _RmcQueueQOccUpLimit_Type()
)
rmcQueueQOccUpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueQOccUpLimit.setStatus("mandatory")


class _RmcQueueQOccUpDelay_Type(Integer32):
    """Custom type rmcQueueQOccUpDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueQOccUpDelay_Type.__name__ = "Integer32"
_RmcQueueQOccUpDelay_Object = MibTableColumn
rmcQueueQOccUpDelay = _RmcQueueQOccUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 11),
    _RmcQueueQOccUpDelay_Type()
)
rmcQueueQOccUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueQOccUpDelay.setStatus("mandatory")


class _RmcQueueQOccLowLimit_Type(Integer32):
    """Custom type rmcQueueQOccLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueQOccLowLimit_Type.__name__ = "Integer32"
_RmcQueueQOccLowLimit_Object = MibTableColumn
rmcQueueQOccLowLimit = _RmcQueueQOccLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 12),
    _RmcQueueQOccLowLimit_Type()
)
rmcQueueQOccLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueQOccLowLimit.setStatus("mandatory")


class _RmcQueueQOccLowDelay_Type(Integer32):
    """Custom type rmcQueueQOccLowDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueQOccLowDelay_Type.__name__ = "Integer32"
_RmcQueueQOccLowDelay_Object = MibTableColumn
rmcQueueQOccLowDelay = _RmcQueueQOccLowDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 13),
    _RmcQueueQOccLowDelay_Type()
)
rmcQueueQOccLowDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueQOccLowDelay.setStatus("mandatory")


class _RmcQueueAdjustMode_Type(Integer32):
    """Custom type rmcQueueAdjustMode based on Integer32"""
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
          ("rate", 2),
          ("level", 3),
          ("fixed", 4))
    )


_RmcQueueAdjustMode_Type.__name__ = "Integer32"
_RmcQueueAdjustMode_Object = MibTableColumn
rmcQueueAdjustMode = _RmcQueueAdjustMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 14),
    _RmcQueueAdjustMode_Type()
)
rmcQueueAdjustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustMode.setStatus("mandatory")


class _RmcQueueAdjustRate_Type(Integer32):
    """Custom type rmcQueueAdjustRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueAdjustRate_Type.__name__ = "Integer32"
_RmcQueueAdjustRate_Object = MibTableColumn
rmcQueueAdjustRate = _RmcQueueAdjustRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 15),
    _RmcQueueAdjustRate_Type()
)
rmcQueueAdjustRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustRate.setStatus("mandatory")


class _RmcQueueAdjustRateLimit_Type(Integer32):
    """Custom type rmcQueueAdjustRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueAdjustRateLimit_Type.__name__ = "Integer32"
_RmcQueueAdjustRateLimit_Object = MibTableColumn
rmcQueueAdjustRateLimit = _RmcQueueAdjustRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 16),
    _RmcQueueAdjustRateLimit_Type()
)
rmcQueueAdjustRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustRateLimit.setStatus("mandatory")


class _RmcQueueAdjustRateDelay_Type(Integer32):
    """Custom type rmcQueueAdjustRateDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueAdjustRateDelay_Type.__name__ = "Integer32"
_RmcQueueAdjustRateDelay_Object = MibTableColumn
rmcQueueAdjustRateDelay = _RmcQueueAdjustRateDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 17),
    _RmcQueueAdjustRateDelay_Type()
)
rmcQueueAdjustRateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustRateDelay.setStatus("mandatory")


class _RmcQueueAdjustRateIter_Type(Integer32):
    """Custom type rmcQueueAdjustRateIter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueAdjustRateIter_Type.__name__ = "Integer32"
_RmcQueueAdjustRateIter_Object = MibTableColumn
rmcQueueAdjustRateIter = _RmcQueueAdjustRateIter_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 18),
    _RmcQueueAdjustRateIter_Type()
)
rmcQueueAdjustRateIter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustRateIter.setStatus("mandatory")


class _RmcQueueAdjustLevel_Type(Integer32):
    """Custom type rmcQueueAdjustLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueAdjustLevel_Type.__name__ = "Integer32"
_RmcQueueAdjustLevel_Object = MibTableColumn
rmcQueueAdjustLevel = _RmcQueueAdjustLevel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 19),
    _RmcQueueAdjustLevel_Type()
)
rmcQueueAdjustLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustLevel.setStatus("mandatory")


class _RmcQueueAdjustLevelLimit_Type(Integer32):
    """Custom type rmcQueueAdjustLevelLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueAdjustLevelLimit_Type.__name__ = "Integer32"
_RmcQueueAdjustLevelLimit_Object = MibTableColumn
rmcQueueAdjustLevelLimit = _RmcQueueAdjustLevelLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 20),
    _RmcQueueAdjustLevelLimit_Type()
)
rmcQueueAdjustLevelLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustLevelLimit.setStatus("mandatory")


class _RmcQueueAdjustLevelDelay_Type(Integer32):
    """Custom type rmcQueueAdjustLevelDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueAdjustLevelDelay_Type.__name__ = "Integer32"
_RmcQueueAdjustLevelDelay_Object = MibTableColumn
rmcQueueAdjustLevelDelay = _RmcQueueAdjustLevelDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 21),
    _RmcQueueAdjustLevelDelay_Type()
)
rmcQueueAdjustLevelDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustLevelDelay.setStatus("mandatory")


class _RmcQueueAdjustLevelIter_Type(Integer32):
    """Custom type rmcQueueAdjustLevelIter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueAdjustLevelIter_Type.__name__ = "Integer32"
_RmcQueueAdjustLevelIter_Object = MibTableColumn
rmcQueueAdjustLevelIter = _RmcQueueAdjustLevelIter_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 22),
    _RmcQueueAdjustLevelIter_Type()
)
rmcQueueAdjustLevelIter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueAdjustLevelIter.setStatus("mandatory")


class _RmcQueueReplaceRate_Type(Integer32):
    """Custom type rmcQueueReplaceRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueReplaceRate_Type.__name__ = "Integer32"
_RmcQueueReplaceRate_Object = MibTableColumn
rmcQueueReplaceRate = _RmcQueueReplaceRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 23),
    _RmcQueueReplaceRate_Type()
)
rmcQueueReplaceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueReplaceRate.setStatus("mandatory")


class _RmcQueueErraticCount_Type(Integer32):
    """Custom type rmcQueueErraticCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcQueueErraticCount_Type.__name__ = "Integer32"
_RmcQueueErraticCount_Object = MibTableColumn
rmcQueueErraticCount = _RmcQueueErraticCount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 24),
    _RmcQueueErraticCount_Type()
)
rmcQueueErraticCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueErraticCount.setStatus("optional")


class _RmcQueueMaxPresence_Type(Integer32):
    """Custom type rmcQueueMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueMaxPresence_Type.__name__ = "Integer32"
_RmcQueueMaxPresence_Object = MibTableColumn
rmcQueueMaxPresence = _RmcQueueMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 25),
    _RmcQueueMaxPresence_Type()
)
rmcQueueMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueMaxPresence.setStatus("optional")


class _RmcQueueNoActivity_Type(Integer32):
    """Custom type rmcQueueNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcQueueNoActivity_Type.__name__ = "Integer32"
_RmcQueueNoActivity_Object = MibTableColumn
rmcQueueNoActivity = _RmcQueueNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 3, 1, 26),
    _RmcQueueNoActivity_Type()
)
rmcQueueNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcQueueNoActivity.setStatus("mandatory")
_RmcQueueStatTable_Object = MibTable
rmcQueueStatTable = _RmcQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    rmcQueueStatTable.setStatus("mandatory")
_RmcQueueStatEntry_Object = MibTableRow
rmcQueueStatEntry = _RmcQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 10, 1)
)
rmcQueueStatEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
    (0, "RMC-MIB1", "rmcQueueNum"),
)
if mibBuilder.loadTexts:
    rmcQueueStatEntry.setStatus("mandatory")


class _RmcQueueFlag_Type(Integer32):
    """Custom type rmcQueueFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcQueueFlag_Type.__name__ = "Integer32"
_RmcQueueFlag_Object = MibTableColumn
rmcQueueFlag = _RmcQueueFlag_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 10, 1, 1),
    _RmcQueueFlag_Type()
)
rmcQueueFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcQueueFlag.setStatus("mandatory")


class _RmcQueueStatus_Type(Integer32):
    """Custom type rmcQueueStatus based on Integer32"""
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
        *(("disabled", 1),
          ("working", 2),
          ("otherError", 3),
          ("erraticCount", 4),
          ("maxPresence", 5),
          ("noActitity", 6),
          ("errorAtSensor", 7))
    )


_RmcQueueStatus_Type.__name__ = "Integer32"
_RmcQueueStatus_Object = MibTableColumn
rmcQueueStatus = _RmcQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 3, 10, 1, 2),
    _RmcQueueStatus_Type()
)
rmcQueueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcQueueStatus.setStatus("mandatory")
_RmcPassage_ObjectIdentity = ObjectIdentity
rmcPassage = _RmcPassage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5)
)
_RmcPassageCtrlTable_Object = MibTable
rmcPassageCtrlTable = _RmcPassageCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    rmcPassageCtrlTable.setStatus("mandatory")
_RmcPassageCtrlEntry_Object = MibTableRow
rmcPassageCtrlEntry = _RmcPassageCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 1, 1)
)
rmcPassageCtrlEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcPassageCtrlEntry.setStatus("mandatory")


class _RmcPassageMode_Type(Integer32):
    """Custom type rmcPassageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("recalled", 1),
          ("enabledCall", 2),
          ("enabledNoCall", 3))
    )


_RmcPassageMode_Type.__name__ = "Integer32"
_RmcPassageMode_Object = MibTableColumn
rmcPassageMode = _RmcPassageMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 1, 1, 1),
    _RmcPassageMode_Type()
)
rmcPassageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPassageMode.setStatus("mandatory")


class _RmcPassageErraticCount_Type(Integer32):
    """Custom type rmcPassageErraticCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcPassageErraticCount_Type.__name__ = "Integer32"
_RmcPassageErraticCount_Object = MibTableColumn
rmcPassageErraticCount = _RmcPassageErraticCount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 1, 1, 2),
    _RmcPassageErraticCount_Type()
)
rmcPassageErraticCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPassageErraticCount.setStatus("optional")


class _RmcPassageMaxPresence_Type(Integer32):
    """Custom type rmcPassageMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcPassageMaxPresence_Type.__name__ = "Integer32"
_RmcPassageMaxPresence_Object = MibTableColumn
rmcPassageMaxPresence = _RmcPassageMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 1, 1, 3),
    _RmcPassageMaxPresence_Type()
)
rmcPassageMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPassageMaxPresence.setStatus("optional")


class _RmcPassageNoActivity_Type(Integer32):
    """Custom type rmcPassageNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcPassageNoActivity_Type.__name__ = "Integer32"
_RmcPassageNoActivity_Object = MibTableColumn
rmcPassageNoActivity = _RmcPassageNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 1, 1, 4),
    _RmcPassageNoActivity_Type()
)
rmcPassageNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcPassageNoActivity.setStatus("optional")
_RmcPassageStatTable_Object = MibTable
rmcPassageStatTable = _RmcPassageStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    rmcPassageStatTable.setStatus("mandatory")
_RmcPassageStatEntry_Object = MibTableRow
rmcPassageStatEntry = _RmcPassageStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 2, 1)
)
rmcPassageStatEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcPassageStatEntry.setStatus("mandatory")


class _RmcPassageStatus_Type(Integer32):
    """Custom type rmcPassageStatus based on Integer32"""
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
        *(("recalled", 1),
          ("working", 2),
          ("otherError", 3),
          ("erraticCount", 4),
          ("maxPresence", 5),
          ("noActitity", 6),
          ("errorAtSensor", 7))
    )


_RmcPassageStatus_Type.__name__ = "Integer32"
_RmcPassageStatus_Object = MibTableColumn
rmcPassageStatus = _RmcPassageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 3, 5, 2, 1, 1),
    _RmcPassageStatus_Type()
)
rmcPassageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcPassageStatus.setStatus("mandatory")
_MeteringPlan_ObjectIdentity = ObjectIdentity
meteringPlan = _MeteringPlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4)
)


class _RmcMaxNumMeteringPlans_Type(Integer32):
    """Custom type rmcMaxNumMeteringPlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMaxNumMeteringPlans_Type.__name__ = "Integer32"
_RmcMaxNumMeteringPlans_Object = MibScalar
rmcMaxNumMeteringPlans = _RmcMaxNumMeteringPlans_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 1),
    _RmcMaxNumMeteringPlans_Type()
)
rmcMaxNumMeteringPlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumMeteringPlans.setStatus("mandatory")


class _RmcNumMeteringPlans_Type(Integer32):
    """Custom type rmcNumMeteringPlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcNumMeteringPlans_Type.__name__ = "Integer32"
_RmcNumMeteringPlans_Object = MibScalar
rmcNumMeteringPlans = _RmcNumMeteringPlans_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 2),
    _RmcNumMeteringPlans_Type()
)
rmcNumMeteringPlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumMeteringPlans.setStatus("mandatory")


class _RmcMaxNumLevelsPerPlan_Type(Integer32):
    """Custom type rmcMaxNumLevelsPerPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMaxNumLevelsPerPlan_Type.__name__ = "Integer32"
_RmcMaxNumLevelsPerPlan_Object = MibScalar
rmcMaxNumLevelsPerPlan = _RmcMaxNumLevelsPerPlan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 3),
    _RmcMaxNumLevelsPerPlan_Type()
)
rmcMaxNumLevelsPerPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumLevelsPerPlan.setStatus("mandatory")


class _RmcNumMeteringLevels_Type(Integer32):
    """Custom type rmcNumMeteringLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcNumMeteringLevels_Type.__name__ = "Integer32"
_RmcNumMeteringLevels_Object = MibScalar
rmcNumMeteringLevels = _RmcNumMeteringLevels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 4),
    _RmcNumMeteringLevels_Type()
)
rmcNumMeteringLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumMeteringLevels.setStatus("mandatory")
_RmcMeteringPlanTable_Object = MibTable
rmcMeteringPlanTable = _RmcMeteringPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    rmcMeteringPlanTable.setStatus("mandatory")
_RmcMeteringPlanEntry_Object = MibTableRow
rmcMeteringPlanEntry = _RmcMeteringPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1)
)
rmcMeteringPlanEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeteringPlanNumber"),
    (0, "RMC-MIB1", "rmcMeteringLevel"),
)
if mibBuilder.loadTexts:
    rmcMeteringPlanEntry.setStatus("mandatory")


class _RmcMeteringPlanNumber_Type(Integer32):
    """Custom type rmcMeteringPlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMeteringPlanNumber_Type.__name__ = "Integer32"
_RmcMeteringPlanNumber_Object = MibTableColumn
rmcMeteringPlanNumber = _RmcMeteringPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1, 1),
    _RmcMeteringPlanNumber_Type()
)
rmcMeteringPlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMeteringPlanNumber.setStatus("mandatory")


class _RmcMeteringLevel_Type(Integer32):
    """Custom type rmcMeteringLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeteringLevel_Type.__name__ = "Integer32"
_RmcMeteringLevel_Object = MibTableColumn
rmcMeteringLevel = _RmcMeteringLevel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1, 2),
    _RmcMeteringLevel_Type()
)
rmcMeteringLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMeteringLevel.setStatus("mandatory")


class _RmcMeteringRate_Type(Integer32):
    """Custom type rmcMeteringRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcMeteringRate_Type.__name__ = "Integer32"
_RmcMeteringRate_Object = MibTableColumn
rmcMeteringRate = _RmcMeteringRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1, 3),
    _RmcMeteringRate_Type()
)
rmcMeteringRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeteringRate.setStatus("mandatory")


class _RmcFlowRateThreshold_Type(Integer32):
    """Custom type rmcFlowRateThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcFlowRateThreshold_Type.__name__ = "Integer32"
_RmcFlowRateThreshold_Object = MibTableColumn
rmcFlowRateThreshold = _RmcFlowRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1, 4),
    _RmcFlowRateThreshold_Type()
)
rmcFlowRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcFlowRateThreshold.setStatus("mandatory")


class _RmcOccupancyThreshold_Type(Integer32):
    """Custom type rmcOccupancyThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcOccupancyThreshold_Type.__name__ = "Integer32"
_RmcOccupancyThreshold_Object = MibTableColumn
rmcOccupancyThreshold = _RmcOccupancyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1, 5),
    _RmcOccupancyThreshold_Type()
)
rmcOccupancyThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcOccupancyThreshold.setStatus("mandatory")


class _RmcSpeedThreshold_Type(Integer32):
    """Custom type rmcSpeedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcSpeedThreshold_Type.__name__ = "Integer32"
_RmcSpeedThreshold_Object = MibTableColumn
rmcSpeedThreshold = _RmcSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 4, 5, 1, 6),
    _RmcSpeedThreshold_Type()
)
rmcSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcSpeedThreshold.setStatus("mandatory")
_RmcTimebase_ObjectIdentity = ObjectIdentity
rmcTimebase = _RmcTimebase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5)
)


class _RmcMaxNumTBCActions_Type(Integer32):
    """Custom type rmcMaxNumTBCActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxNumTBCActions_Type.__name__ = "Integer32"
_RmcMaxNumTBCActions_Object = MibScalar
rmcMaxNumTBCActions = _RmcMaxNumTBCActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 1),
    _RmcMaxNumTBCActions_Type()
)
rmcMaxNumTBCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumTBCActions.setStatus("mandatory")


class _RmcNumTBCActions_Type(Integer32):
    """Custom type rmcNumTBCActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcNumTBCActions_Type.__name__ = "Integer32"
_RmcNumTBCActions_Object = MibScalar
rmcNumTBCActions = _RmcNumTBCActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 2),
    _RmcNumTBCActions_Type()
)
rmcNumTBCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumTBCActions.setStatus("mandatory")
_RmcActionTable_Object = MibTable
rmcActionTable = _RmcActionTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    rmcActionTable.setStatus("mandatory")
_RmcActionEntry_Object = MibTableRow
rmcActionEntry = _RmcActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 3, 1)
)
rmcActionEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcActionNum"),
)
if mibBuilder.loadTexts:
    rmcActionEntry.setStatus("mandatory")


class _RmcActionNum_Type(Integer32):
    """Custom type rmcActionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcActionNum_Type.__name__ = "Integer32"
_RmcActionNum_Object = MibTableColumn
rmcActionNum = _RmcActionNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 3, 1, 1),
    _RmcActionNum_Type()
)
rmcActionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcActionNum.setStatus("mandatory")


class _RmcActionMode_Type(Integer32):
    """Custom type rmcActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcActionMode_Type.__name__ = "Integer32"
_RmcActionMode_Object = MibTableColumn
rmcActionMode = _RmcActionMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 3, 1, 2),
    _RmcActionMode_Type()
)
rmcActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcActionMode.setStatus("mandatory")


class _RmcMeterActionNum_Type(Integer32):
    """Custom type rmcMeterActionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterActionNum_Type.__name__ = "Integer32"
_RmcMeterActionNum_Object = MibTableColumn
rmcMeterActionNum = _RmcMeterActionNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 3, 1, 3),
    _RmcMeterActionNum_Type()
)
rmcMeterActionNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterActionNum.setStatus("mandatory")


class _RmcMLActionNum_Type(Integer32):
    """Custom type rmcMLActionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLActionNum_Type.__name__ = "Integer32"
_RmcMLActionNum_Object = MibTableColumn
rmcMLActionNum = _RmcMLActionNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 3, 1, 4),
    _RmcMLActionNum_Type()
)
rmcMLActionNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLActionNum.setStatus("optional")


class _RmcMaxNumMeterTBCActions_Type(Integer32):
    """Custom type rmcMaxNumMeterTBCActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxNumMeterTBCActions_Type.__name__ = "Integer32"
_RmcMaxNumMeterTBCActions_Object = MibScalar
rmcMaxNumMeterTBCActions = _RmcMaxNumMeterTBCActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 4),
    _RmcMaxNumMeterTBCActions_Type()
)
rmcMaxNumMeterTBCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumMeterTBCActions.setStatus("mandatory")


class _RmcNumMeterTBCActions_Type(Integer32):
    """Custom type rmcNumMeterTBCActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcNumMeterTBCActions_Type.__name__ = "Integer32"
_RmcNumMeterTBCActions_Object = MibScalar
rmcNumMeterTBCActions = _RmcNumMeterTBCActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 5),
    _RmcNumMeterTBCActions_Type()
)
rmcNumMeterTBCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumMeterTBCActions.setStatus("mandatory")
_RmcMeterActionTable_Object = MibTable
rmcMeterActionTable = _RmcMeterActionTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6)
)
if mibBuilder.loadTexts:
    rmcMeterActionTable.setStatus("mandatory")
_RmcMeterActionEntry_Object = MibTableRow
rmcMeterActionEntry = _RmcMeterActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1)
)
rmcMeterActionEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterActionIndex"),
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcMeterActionEntry.setStatus("mandatory")


class _RmcMeterActionIndex_Type(Integer32):
    """Custom type rmcMeterActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMeterActionIndex_Type.__name__ = "Integer32"
_RmcMeterActionIndex_Object = MibTableColumn
rmcMeterActionIndex = _RmcMeterActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 1),
    _RmcMeterActionIndex_Type()
)
rmcMeterActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMeterActionIndex.setStatus("mandatory")


class _RmcMeterActionMode_Type(Integer32):
    """Custom type rmcMeterActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcMeterActionMode_Type.__name__ = "Integer32"
_RmcMeterActionMode_Object = MibTableColumn
rmcMeterActionMode = _RmcMeterActionMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 2),
    _RmcMeterActionMode_Type()
)
rmcMeterActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterActionMode.setStatus("mandatory")


class _RmcTBActionCtrl_Type(Integer32):
    """Custom type rmcTBActionCtrl based on Integer32"""
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
        *(("dark", 1),
          ("restInGreen", 2),
          ("fixedRate", 3),
          ("trafficResponsive", 4),
          ("emergencyGreen", 5),
          ("skip", 6))
    )


_RmcTBActionCtrl_Type.__name__ = "Integer32"
_RmcTBActionCtrl_Object = MibTableColumn
rmcTBActionCtrl = _RmcTBActionCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 3),
    _RmcTBActionCtrl_Type()
)
rmcTBActionCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBActionCtrl.setStatus("mandatory")


class _RmcTBPlanCtrl_Type(Integer32):
    """Custom type rmcTBPlanCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcTBPlanCtrl_Type.__name__ = "Integer32"
_RmcTBPlanCtrl_Object = MibTableColumn
rmcTBPlanCtrl = _RmcTBPlanCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 4),
    _RmcTBPlanCtrl_Type()
)
rmcTBPlanCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBPlanCtrl.setStatus("mandatory")


class _RmcTBRateCtrl_Type(Integer32):
    """Custom type rmcTBRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcTBRateCtrl_Type.__name__ = "Integer32"
_RmcTBRateCtrl_Object = MibTableColumn
rmcTBRateCtrl = _RmcTBRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 5),
    _RmcTBRateCtrl_Type()
)
rmcTBRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBRateCtrl.setStatus("mandatory")


class _RmcTBVehiclesPerGrnCtrl_Type(Integer32):
    """Custom type rmcTBVehiclesPerGrnCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcTBVehiclesPerGrnCtrl_Type.__name__ = "Integer32"
_RmcTBVehiclesPerGrnCtrl_Object = MibTableColumn
rmcTBVehiclesPerGrnCtrl = _RmcTBVehiclesPerGrnCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 6),
    _RmcTBVehiclesPerGrnCtrl_Type()
)
rmcTBVehiclesPerGrnCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBVehiclesPerGrnCtrl.setStatus("mandatory")


class _RmcTBCMinMeterRateCtrl_Type(Integer32):
    """Custom type rmcTBCMinMeterRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcTBCMinMeterRateCtrl_Type.__name__ = "Integer32"
_RmcTBCMinMeterRateCtrl_Object = MibTableColumn
rmcTBCMinMeterRateCtrl = _RmcTBCMinMeterRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 7),
    _RmcTBCMinMeterRateCtrl_Type()
)
rmcTBCMinMeterRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBCMinMeterRateCtrl.setStatus("optional")


class _RmcTBCMaxMeterRateCtrl_Type(Integer32):
    """Custom type rmcTBCMaxMeterRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RmcTBCMaxMeterRateCtrl_Type.__name__ = "Integer32"
_RmcTBCMaxMeterRateCtrl_Object = MibTableColumn
rmcTBCMaxMeterRateCtrl = _RmcTBCMaxMeterRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 6, 1, 8),
    _RmcTBCMaxMeterRateCtrl_Type()
)
rmcTBCMaxMeterRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBCMaxMeterRateCtrl.setStatus("optional")


class _RmcMaxNumMLTBCActions_Type(Integer32):
    """Custom type rmcMaxNumMLTBCActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMaxNumMLTBCActions_Type.__name__ = "Integer32"
_RmcMaxNumMLTBCActions_Object = MibScalar
rmcMaxNumMLTBCActions = _RmcMaxNumMLTBCActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 7),
    _RmcMaxNumMLTBCActions_Type()
)
rmcMaxNumMLTBCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMaxNumMLTBCActions.setStatus("mandatory")


class _RmcNumMLTBCActions_Type(Integer32):
    """Custom type rmcNumMLTBCActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcNumMLTBCActions_Type.__name__ = "Integer32"
_RmcNumMLTBCActions_Object = MibScalar
rmcNumMLTBCActions = _RmcNumMLTBCActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 8),
    _RmcNumMLTBCActions_Type()
)
rmcNumMLTBCActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcNumMLTBCActions.setStatus("mandatory")
_RmcMLActionTable_Object = MibTable
rmcMLActionTable = _RmcMLActionTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 9)
)
if mibBuilder.loadTexts:
    rmcMLActionTable.setStatus("mandatory")
_RmcMLActionEntry_Object = MibTableRow
rmcMLActionEntry = _RmcMLActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 9, 1)
)
rmcMLActionEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMLActionIndex"),
    (0, "RMC-MIB1", "rmcMLNumber"),
)
if mibBuilder.loadTexts:
    rmcMLActionEntry.setStatus("mandatory")


class _RmcMLActionIndex_Type(Integer32):
    """Custom type rmcMLActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RmcMLActionIndex_Type.__name__ = "Integer32"
_RmcMLActionIndex_Object = MibTableColumn
rmcMLActionIndex = _RmcMLActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 9, 1, 1),
    _RmcMLActionIndex_Type()
)
rmcMLActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmcMLActionIndex.setStatus("mandatory")


class _RmcMLActionMode_Type(Integer32):
    """Custom type rmcMLActionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RmcMLActionMode_Type.__name__ = "Integer32"
_RmcMLActionMode_Object = MibTableColumn
rmcMLActionMode = _RmcMLActionMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 9, 1, 2),
    _RmcMLActionMode_Type()
)
rmcMLActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLActionMode.setStatus("mandatory")


class _RmcTBMLUsageMode_Type(Integer32):
    """Custom type rmcTBMLUsageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 1),
          ("schemeF", 2),
          ("schemeO", 3),
          ("schemeFO", 4),
          ("schemeS", 5),
          ("schemeFS", 6),
          ("schemeOS", 7),
          ("schemeFOS", 8))
    )


_RmcTBMLUsageMode_Type.__name__ = "Integer32"
_RmcTBMLUsageMode_Object = MibTableColumn
rmcTBMLUsageMode = _RmcTBMLUsageMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 5, 9, 1, 3),
    _RmcTBMLUsageMode_Type()
)
rmcTBMLUsageMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcTBMLUsageMode.setStatus("mandatory")
_RmcInOutput_ObjectIdentity = ObjectIdentity
rmcInOutput = _RmcInOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6)
)


class _RmcAdvSignOutNumber_Type(Integer32):
    """Custom type rmcAdvSignOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcAdvSignOutNumber_Type.__name__ = "Integer32"
_RmcAdvSignOutNumber_Object = MibScalar
rmcAdvSignOutNumber = _RmcAdvSignOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 1),
    _RmcAdvSignOutNumber_Type()
)
rmcAdvSignOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcAdvSignOutNumber.setStatus("optional")
_RmcMLInTable_Object = MibTable
rmcMLInTable = _RmcMLInTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    rmcMLInTable.setStatus("optional")
_RmcMLInEntry_Object = MibTableRow
rmcMLInEntry = _RmcMLInEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 2, 1)
)
rmcMLInEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMLNumber"),
)
if mibBuilder.loadTexts:
    rmcMLInEntry.setStatus("mandatory")


class _RmcMLLeadInNumber_Type(Integer32):
    """Custom type rmcMLLeadInNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLLeadInNumber_Type.__name__ = "Integer32"
_RmcMLLeadInNumber_Object = MibTableColumn
rmcMLLeadInNumber = _RmcMLLeadInNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 2, 1, 1),
    _RmcMLLeadInNumber_Type()
)
rmcMLLeadInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLLeadInNumber.setStatus("mandatory")


class _RmcMLTrailInNumber_Type(Integer32):
    """Custom type rmcMLTrailInNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMLTrailInNumber_Type.__name__ = "Integer32"
_RmcMLTrailInNumber_Object = MibTableColumn
rmcMLTrailInNumber = _RmcMLTrailInNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 2, 1, 2),
    _RmcMLTrailInNumber_Type()
)
rmcMLTrailInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMLTrailInNumber.setStatus("mandatory")
_RmcQueueInTable_Object = MibTable
rmcQueueInTable = _RmcQueueInTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    rmcQueueInTable.setStatus("optional")
_RmcQueueInEntry_Object = MibTableRow
rmcQueueInEntry = _RmcQueueInEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 3, 1)
)
rmcQueueInEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
    (0, "RMC-MIB1", "rmcQueueNum"),
)
if mibBuilder.loadTexts:
    rmcQueueInEntry.setStatus("mandatory")


class _RmcMetQueueInNumber_Type(Integer32):
    """Custom type rmcMetQueueInNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMetQueueInNumber_Type.__name__ = "Integer32"
_RmcMetQueueInNumber_Object = MibTableColumn
rmcMetQueueInNumber = _RmcMetQueueInNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 3, 1, 1),
    _RmcMetQueueInNumber_Type()
)
rmcMetQueueInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMetQueueInNumber.setStatus("mandatory")
_RmcMeterInOutTable_Object = MibTable
rmcMeterInOutTable = _RmcMeterInOutTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    rmcMeterInOutTable.setStatus("mandatory")
_RmcMeterInOutEntry_Object = MibTableRow
rmcMeterInOutEntry = _RmcMeterInOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1)
)
rmcMeterInOutEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcMeterNumber"),
)
if mibBuilder.loadTexts:
    rmcMeterInOutEntry.setStatus("mandatory")


class _RmcMeterDemandInNumber_Type(Integer32):
    """Custom type rmcMeterDemandInNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterDemandInNumber_Type.__name__ = "Integer32"
_RmcMeterDemandInNumber_Object = MibTableColumn
rmcMeterDemandInNumber = _RmcMeterDemandInNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1, 1),
    _RmcMeterDemandInNumber_Type()
)
rmcMeterDemandInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterDemandInNumber.setStatus("optional")


class _RmcMeterPassageInNumber_Type(Integer32):
    """Custom type rmcMeterPassageInNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterPassageInNumber_Type.__name__ = "Integer32"
_RmcMeterPassageInNumber_Object = MibTableColumn
rmcMeterPassageInNumber = _RmcMeterPassageInNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1, 2),
    _RmcMeterPassageInNumber_Type()
)
rmcMeterPassageInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterPassageInNumber.setStatus("optional")


class _RmcMeterRedOutNumber_Type(Integer32):
    """Custom type rmcMeterRedOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterRedOutNumber_Type.__name__ = "Integer32"
_RmcMeterRedOutNumber_Object = MibTableColumn
rmcMeterRedOutNumber = _RmcMeterRedOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1, 3),
    _RmcMeterRedOutNumber_Type()
)
rmcMeterRedOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterRedOutNumber.setStatus("mandatory")


class _RmcMeterYellowOutNumber_Type(Integer32):
    """Custom type rmcMeterYellowOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterYellowOutNumber_Type.__name__ = "Integer32"
_RmcMeterYellowOutNumber_Object = MibTableColumn
rmcMeterYellowOutNumber = _RmcMeterYellowOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1, 4),
    _RmcMeterYellowOutNumber_Type()
)
rmcMeterYellowOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterYellowOutNumber.setStatus("optional")


class _RmcMeterGreenOutNumber_Type(Integer32):
    """Custom type rmcMeterGreenOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterGreenOutNumber_Type.__name__ = "Integer32"
_RmcMeterGreenOutNumber_Object = MibTableColumn
rmcMeterGreenOutNumber = _RmcMeterGreenOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1, 5),
    _RmcMeterGreenOutNumber_Type()
)
rmcMeterGreenOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterGreenOutNumber.setStatus("mandatory")


class _RmcMeterAdvSignOutNumber_Type(Integer32):
    """Custom type rmcMeterAdvSignOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcMeterAdvSignOutNumber_Type.__name__ = "Integer32"
_RmcMeterAdvSignOutNumber_Object = MibTableColumn
rmcMeterAdvSignOutNumber = _RmcMeterAdvSignOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 4, 1, 6),
    _RmcMeterAdvSignOutNumber_Type()
)
rmcMeterAdvSignOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcMeterAdvSignOutNumber.setStatus("optional")
_RmcDependInOutTable_Object = MibTable
rmcDependInOutTable = _RmcDependInOutTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 5)
)
if mibBuilder.loadTexts:
    rmcDependInOutTable.setStatus("optional")
_RmcDependInOutEntry_Object = MibTableRow
rmcDependInOutEntry = _RmcDependInOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 5, 1)
)
rmcDependInOutEntry.setIndexNames(
    (0, "RMC-MIB1", "rmcDependGroupNumber"),
)
if mibBuilder.loadTexts:
    rmcDependInOutEntry.setStatus("mandatory")


class _RmcDependMergeInNumber_Type(Integer32):
    """Custom type rmcDependMergeInNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDependMergeInNumber_Type.__name__ = "Integer32"
_RmcDependMergeInNumber_Object = MibTableColumn
rmcDependMergeInNumber = _RmcDependMergeInNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 5, 1, 1),
    _RmcDependMergeInNumber_Type()
)
rmcDependMergeInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDependMergeInNumber.setStatus("optional")


class _RmcDependAdvSignOutNumber_Type(Integer32):
    """Custom type rmcDependAdvSignOutNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RmcDependAdvSignOutNumber_Type.__name__ = "Integer32"
_RmcDependAdvSignOutNumber_Object = MibTableColumn
rmcDependAdvSignOutNumber = _RmcDependAdvSignOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 2, 6, 5, 1, 2),
    _RmcDependAdvSignOutNumber_Type()
)
rmcDependAdvSignOutNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmcDependAdvSignOutNumber.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RMC-MIB1",
    **{"ramp": ramp,
       "rmcCfg": rmcCfg,
       "rmcCommRefreshThreshold": rmcCommRefreshThreshold,
       "rmcCalcInterval": rmcCalcInterval,
       "rmcML": rmcML,
       "rmcAveragingPeriods": rmcAveragingPeriods,
       "rmcMaxNumML": rmcMaxNumML,
       "rmcNumML": rmcNumML,
       "rmcMLCtrlTable": rmcMLCtrlTable,
       "rmcMLCtrlEntry": rmcMLCtrlEntry,
       "rmcMLNumber": rmcMLNumber,
       "rmcMLMode": rmcMLMode,
       "rmcMLLeadZoneLength": rmcMLLeadZoneLength,
       "rmcMLTrailZoneLength": rmcMLTrailZoneLength,
       "rmcMLUsageMode": rmcMLUsageMode,
       "rmcMLSpeedTrapSpacing": rmcMLSpeedTrapSpacing,
       "rmcMLErraticCount": rmcMLErraticCount,
       "rmcMLMaxPresence": rmcMLMaxPresence,
       "rmcMLNoActivity": rmcMLNoActivity,
       "rmcVehicleLength": rmcVehicleLength,
       "rmcAverageFlowRate": rmcAverageFlowRate,
       "rmcAverageOccupancy": rmcAverageOccupancy,
       "rmcAverageSpeed": rmcAverageSpeed,
       "rmcMLStatTable": rmcMLStatTable,
       "rmcMLStatEntry": rmcMLStatEntry,
       "rmcMLLeadStatus": rmcMLLeadStatus,
       "rmcMLTrailStatus": rmcMLTrailStatus,
       "rmcMLStatus": rmcMLStatus,
       "rmcMLUsageStatus": rmcMLUsageStatus,
       "rmcMeter": rmcMeter,
       "rmcMeterMain": rmcMeterMain,
       "rmcMaxNumMeteredLanes": rmcMaxNumMeteredLanes,
       "rmcNumMeteredLanes": rmcNumMeteredLanes,
       "rmcMeterCfgTable": rmcMeterCfgTable,
       "rmcMeterCfgEntry": rmcMeterCfgEntry,
       "rmcMeterNumber": rmcMeterNumber,
       "rmcDependGroupNumber": rmcDependGroupNumber,
       "rmcDependGroupSeqNumber": rmcDependGroupSeqNumber,
       "rmcCmdSourcePriorityOrder": rmcCmdSourcePriorityOrder,
       "rmcDemandErraticCount": rmcDemandErraticCount,
       "rmcDemandMaxPresence": rmcDemandMaxPresence,
       "rmcDemandNoActivity": rmcDemandNoActivity,
       "rmcMinMeterTime": rmcMinMeterTime,
       "rmcMinNonMeterTime": rmcMinNonMeterTime,
       "rmcAbsoluteMinMeterRate": rmcAbsoluteMinMeterRate,
       "rmcAbsoluteMaxMeterRate": rmcAbsoluteMaxMeterRate,
       "rmcSystemMinMeterRate": rmcSystemMinMeterRate,
       "rmcSystemMaxMeterRate": rmcSystemMaxMeterRate,
       "rmcStartAlert": rmcStartAlert,
       "rmcStartWarning": rmcStartWarning,
       "rmcStartGreen": rmcStartGreen,
       "rmcStartGapTime": rmcStartGapTime,
       "rmcStartGapQueueDetectorNum": rmcStartGapQueueDetectorNum,
       "rmcStartYellow": rmcStartYellow,
       "rmcStartRed": rmcStartRed,
       "rmcMinRed": rmcMinRed,
       "rmcRedViolationClearance": rmcRedViolationClearance,
       "rmcRedViolationAdjust": rmcRedViolationAdjust,
       "rmcMinGreen": rmcMinGreen,
       "rmcMaxGreen": rmcMaxGreen,
       "rmcYellow": rmcYellow,
       "rmcShortStopTime": rmcShortStopTime,
       "rmcShortStopOccupancy": rmcShortStopOccupancy,
       "rmcShortStopQueueDetectorNum": rmcShortStopQueueDetectorNum,
       "rmcLongStopTime": rmcLongStopTime,
       "rmcDemandGap": rmcDemandGap,
       "rmcDemandRed": rmcDemandRed,
       "rmcShutNormalRate": rmcShutNormalRate,
       "rmcShutWarning": rmcShutWarning,
       "rmcShutTime": rmcShutTime,
       "rmcPostMeterGreen": rmcPostMeterGreen,
       "rmcQueueViolationFlag": rmcQueueViolationFlag,
       "rmcQueueShutdownFlag": rmcQueueShutdownFlag,
       "rmcQueueAdjustUsage": rmcQueueAdjustUsage,
       "rmcMeterCtrlTable": rmcMeterCtrlTable,
       "rmcMeterCtrlEntry": rmcMeterCtrlEntry,
       "rmcMeterMode": rmcMeterMode,
       "rmcManualAction": rmcManualAction,
       "rmcManualPlan": rmcManualPlan,
       "rmcManualRate": rmcManualRate,
       "rmcManualVehiclesPerGrn": rmcManualVehiclesPerGrn,
       "rmcIntercoAction": rmcIntercoAction,
       "rmcIntercoPlan": rmcIntercoPlan,
       "rmcIntercoRate": rmcIntercoRate,
       "rmcIntercoVehiclesPerGrn": rmcIntercoVehiclesPerGrn,
       "rmcCommActionStatus": rmcCommActionStatus,
       "rmcCommPlan": rmcCommPlan,
       "rmcCommRate": rmcCommRate,
       "rmcCommVehiclesPerGrn": rmcCommVehiclesPerGrn,
       "rmcDefaultAction": rmcDefaultAction,
       "rmcDefaultPlan": rmcDefaultPlan,
       "rmcDefaultRate": rmcDefaultRate,
       "rmcDefaultVehiclesPerGrn": rmcDefaultVehiclesPerGrn,
       "rmcDemandMode": rmcDemandMode,
       "rmcMeterStatTable": rmcMeterStatTable,
       "rmcMeterStatEntry": rmcMeterStatEntry,
       "rmcRequestCommandSource": rmcRequestCommandSource,
       "rmcImplementCommandSource": rmcImplementCommandSource,
       "rmcImplementAction": rmcImplementAction,
       "rmcImplementPlan": rmcImplementPlan,
       "rmcImplementRate": rmcImplementRate,
       "rmcImplementVehiclesPerGrn": rmcImplementVehiclesPerGrn,
       "rmcRequestAction": rmcRequestAction,
       "rmcRequestPlan": rmcRequestPlan,
       "rmcRequestRate": rmcRequestRate,
       "rmcRequestVehiclesPerGrn": rmcRequestVehiclesPerGrn,
       "rmcCommAction": rmcCommAction,
       "rmcBaseMeterRate": rmcBaseMeterRate,
       "rmcActiveMeterRate": rmcActiveMeterRate,
       "rmcTBActionStatus": rmcTBActionStatus,
       "rmcTBPlanStatus": rmcTBPlanStatus,
       "rmcTBRateStatus": rmcTBRateStatus,
       "rmcTBVehiclesPerGrnStatus": rmcTBVehiclesPerGrnStatus,
       "rmcActiveInterval": rmcActiveInterval,
       "rmcTBCMinMeterRateStatus": rmcTBCMinMeterRateStatus,
       "rmcTBCMaxMeterRateStatus": rmcTBCMaxMeterRateStatus,
       "rmcOperMinMeterRateStatus": rmcOperMinMeterRateStatus,
       "rmcOperMaxMeterRateStatus": rmcOperMaxMeterRateStatus,
       "rmcDemandStatus": rmcDemandStatus,
       "rmcDependGroup": rmcDependGroup,
       "rmcMaxNumDependGroup": rmcMaxNumDependGroup,
       "rmcNumDependGroup": rmcNumDependGroup,
       "rmcDependGroupCtrlTable": rmcDependGroupCtrlTable,
       "rmcDependGroupCtrlEntry": rmcDependGroupCtrlEntry,
       "rmcDependGroupMode": rmcDependGroupMode,
       "rmcSignalServiceMode": rmcSignalServiceMode,
       "rmcShutGapTime": rmcShutGapTime,
       "rmcShutGapReductTime": rmcShutGapReductTime,
       "rmcShutGapReductValue": rmcShutGapReductValue,
       "rmcGreenOffset": rmcGreenOffset,
       "rmcMinFractionalOffset": rmcMinFractionalOffset,
       "rmcPriorityLaneNum": rmcPriorityLaneNum,
       "rmcPriorityRedDelay": rmcPriorityRedDelay,
       "rmcMergeMode": rmcMergeMode,
       "rmcMergeGap": rmcMergeGap,
       "rmcMergeDelay": rmcMergeDelay,
       "rmcQueueMergeFlag": rmcQueueMergeFlag,
       "rmcMergeErraticCount": rmcMergeErraticCount,
       "rmcMergeMaxPresence": rmcMergeMaxPresence,
       "rmcMergeNoActivity": rmcMergeNoActivity,
       "rmcDependGroupStatTable": rmcDependGroupStatTable,
       "rmcDependGroupStatEntry": rmcDependGroupStatEntry,
       "rmcMergeFlag": rmcMergeFlag,
       "rmcMergeStatus": rmcMergeStatus,
       "rmcQueue": rmcQueue,
       "rmcMaxNumQueueEntries": rmcMaxNumQueueEntries,
       "rmcNumQueueEntries": rmcNumQueueEntries,
       "rmcQueueCtrlTable": rmcQueueCtrlTable,
       "rmcQueueCtrlEntry": rmcQueueCtrlEntry,
       "rmcQueueNum": rmcQueueNum,
       "rmcQueueType": rmcQueueType,
       "rmcQueueDetectMode": rmcQueueDetectMode,
       "rmcQueueLengthUpLimit": rmcQueueLengthUpLimit,
       "rmcQueueLengthLowLimit": rmcQueueLengthLowLimit,
       "rmcQueueOccUpLimit": rmcQueueOccUpLimit,
       "rmcQueueOccUpDelay": rmcQueueOccUpDelay,
       "rmcQueueOccLowLimit": rmcQueueOccLowLimit,
       "rmcQueueOccLowDelay": rmcQueueOccLowDelay,
       "rmcQueueQOccUpLimit": rmcQueueQOccUpLimit,
       "rmcQueueQOccUpDelay": rmcQueueQOccUpDelay,
       "rmcQueueQOccLowLimit": rmcQueueQOccLowLimit,
       "rmcQueueQOccLowDelay": rmcQueueQOccLowDelay,
       "rmcQueueAdjustMode": rmcQueueAdjustMode,
       "rmcQueueAdjustRate": rmcQueueAdjustRate,
       "rmcQueueAdjustRateLimit": rmcQueueAdjustRateLimit,
       "rmcQueueAdjustRateDelay": rmcQueueAdjustRateDelay,
       "rmcQueueAdjustRateIter": rmcQueueAdjustRateIter,
       "rmcQueueAdjustLevel": rmcQueueAdjustLevel,
       "rmcQueueAdjustLevelLimit": rmcQueueAdjustLevelLimit,
       "rmcQueueAdjustLevelDelay": rmcQueueAdjustLevelDelay,
       "rmcQueueAdjustLevelIter": rmcQueueAdjustLevelIter,
       "rmcQueueReplaceRate": rmcQueueReplaceRate,
       "rmcQueueErraticCount": rmcQueueErraticCount,
       "rmcQueueMaxPresence": rmcQueueMaxPresence,
       "rmcQueueNoActivity": rmcQueueNoActivity,
       "rmcQueueStatTable": rmcQueueStatTable,
       "rmcQueueStatEntry": rmcQueueStatEntry,
       "rmcQueueFlag": rmcQueueFlag,
       "rmcQueueStatus": rmcQueueStatus,
       "rmcPassage": rmcPassage,
       "rmcPassageCtrlTable": rmcPassageCtrlTable,
       "rmcPassageCtrlEntry": rmcPassageCtrlEntry,
       "rmcPassageMode": rmcPassageMode,
       "rmcPassageErraticCount": rmcPassageErraticCount,
       "rmcPassageMaxPresence": rmcPassageMaxPresence,
       "rmcPassageNoActivity": rmcPassageNoActivity,
       "rmcPassageStatTable": rmcPassageStatTable,
       "rmcPassageStatEntry": rmcPassageStatEntry,
       "rmcPassageStatus": rmcPassageStatus,
       "meteringPlan": meteringPlan,
       "rmcMaxNumMeteringPlans": rmcMaxNumMeteringPlans,
       "rmcNumMeteringPlans": rmcNumMeteringPlans,
       "rmcMaxNumLevelsPerPlan": rmcMaxNumLevelsPerPlan,
       "rmcNumMeteringLevels": rmcNumMeteringLevels,
       "rmcMeteringPlanTable": rmcMeteringPlanTable,
       "rmcMeteringPlanEntry": rmcMeteringPlanEntry,
       "rmcMeteringPlanNumber": rmcMeteringPlanNumber,
       "rmcMeteringLevel": rmcMeteringLevel,
       "rmcMeteringRate": rmcMeteringRate,
       "rmcFlowRateThreshold": rmcFlowRateThreshold,
       "rmcOccupancyThreshold": rmcOccupancyThreshold,
       "rmcSpeedThreshold": rmcSpeedThreshold,
       "rmcTimebase": rmcTimebase,
       "rmcMaxNumTBCActions": rmcMaxNumTBCActions,
       "rmcNumTBCActions": rmcNumTBCActions,
       "rmcActionTable": rmcActionTable,
       "rmcActionEntry": rmcActionEntry,
       "rmcActionNum": rmcActionNum,
       "rmcActionMode": rmcActionMode,
       "rmcMeterActionNum": rmcMeterActionNum,
       "rmcMLActionNum": rmcMLActionNum,
       "rmcMaxNumMeterTBCActions": rmcMaxNumMeterTBCActions,
       "rmcNumMeterTBCActions": rmcNumMeterTBCActions,
       "rmcMeterActionTable": rmcMeterActionTable,
       "rmcMeterActionEntry": rmcMeterActionEntry,
       "rmcMeterActionIndex": rmcMeterActionIndex,
       "rmcMeterActionMode": rmcMeterActionMode,
       "rmcTBActionCtrl": rmcTBActionCtrl,
       "rmcTBPlanCtrl": rmcTBPlanCtrl,
       "rmcTBRateCtrl": rmcTBRateCtrl,
       "rmcTBVehiclesPerGrnCtrl": rmcTBVehiclesPerGrnCtrl,
       "rmcTBCMinMeterRateCtrl": rmcTBCMinMeterRateCtrl,
       "rmcTBCMaxMeterRateCtrl": rmcTBCMaxMeterRateCtrl,
       "rmcMaxNumMLTBCActions": rmcMaxNumMLTBCActions,
       "rmcNumMLTBCActions": rmcNumMLTBCActions,
       "rmcMLActionTable": rmcMLActionTable,
       "rmcMLActionEntry": rmcMLActionEntry,
       "rmcMLActionIndex": rmcMLActionIndex,
       "rmcMLActionMode": rmcMLActionMode,
       "rmcTBMLUsageMode": rmcTBMLUsageMode,
       "rmcInOutput": rmcInOutput,
       "rmcAdvSignOutNumber": rmcAdvSignOutNumber,
       "rmcMLInTable": rmcMLInTable,
       "rmcMLInEntry": rmcMLInEntry,
       "rmcMLLeadInNumber": rmcMLLeadInNumber,
       "rmcMLTrailInNumber": rmcMLTrailInNumber,
       "rmcQueueInTable": rmcQueueInTable,
       "rmcQueueInEntry": rmcQueueInEntry,
       "rmcMetQueueInNumber": rmcMetQueueInNumber,
       "rmcMeterInOutTable": rmcMeterInOutTable,
       "rmcMeterInOutEntry": rmcMeterInOutEntry,
       "rmcMeterDemandInNumber": rmcMeterDemandInNumber,
       "rmcMeterPassageInNumber": rmcMeterPassageInNumber,
       "rmcMeterRedOutNumber": rmcMeterRedOutNumber,
       "rmcMeterYellowOutNumber": rmcMeterYellowOutNumber,
       "rmcMeterGreenOutNumber": rmcMeterGreenOutNumber,
       "rmcMeterAdvSignOutNumber": rmcMeterAdvSignOutNumber,
       "rmcDependInOutTable": rmcDependInOutTable,
       "rmcDependInOutEntry": rmcDependInOutEntry,
       "rmcDependMergeInNumber": rmcDependMergeInNumber,
       "rmcDependAdvSignOutNumber": rmcDependAdvSignOutNumber}
)
