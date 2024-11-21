# SNMP MIB module (TSS-MIB1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1209TSS.mib
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

_Tss_ObjectIdentity = ObjectIdentity
tss = _Tss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4)
)
_TssSystemSetup_ObjectIdentity = ObjectIdentity
tssSystemSetup = _TssSystemSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1)
)


class _SensorSystemReset_Type(Integer32):
    """Custom type sensorSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("reinitialize", 2),
          ("shortDiagnostics", 3),
          ("fullDiagnostics", 4),
          ("commandComplete", 255))
    )


_SensorSystemReset_Type.__name__ = "Integer32"
_SensorSystemReset_Object = MibScalar
sensorSystemReset = _SensorSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 1),
    _SensorSystemReset_Type()
)
sensorSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorSystemReset.setStatus("mandatory")


class _SensorSystemStatus_Type(Integer32):
    """Custom type sensorSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oK", 1),
          ("initializing", 2),
          ("other", 3))
    )


_SensorSystemStatus_Type.__name__ = "Integer32"
_SensorSystemStatus_Object = MibScalar
sensorSystemStatus = _SensorSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 2),
    _SensorSystemStatus_Type()
)
sensorSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorSystemStatus.setStatus("mandatory")


class _SensorSystemDataType_Type(Integer32):
    """Custom type sensorSystemDataType based on Integer32"""
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
        *(("nonnormalizedOccupancy", 1),
          ("pointOccupancy", 2),
          ("normalizedSixFootLoopOccupancy", 3),
          ("normalizedTwoMeterLoopOccupancy", 4),
          ("normalizedOtherOccupancy", 5))
    )


_SensorSystemDataType_Type.__name__ = "Integer32"
_SensorSystemDataType_Object = MibScalar
sensorSystemDataType = _SensorSystemDataType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 3),
    _SensorSystemDataType_Type()
)
sensorSystemDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorSystemDataType.setStatus("optional")


class _MaxSensorZones_Type(Integer32):
    """Custom type maxSensorZones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxSensorZones_Type.__name__ = "Integer32"
_MaxSensorZones_Object = MibScalar
maxSensorZones = _MaxSensorZones_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 4),
    _MaxSensorZones_Type()
)
maxSensorZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSensorZones.setStatus("mandatory")
_SensorZoneTable_Object = MibTable
sensorZoneTable = _SensorZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    sensorZoneTable.setStatus("mandatory")
_SensorZoneEntry_Object = MibTableRow
sensorZoneEntry = _SensorZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 5, 1)
)
sensorZoneEntry.setIndexNames(
    (0, "TSS-MIB1", "sensorZoneNumber"),
    (0, "TSS-MIB1", "outputNumber"),
)
if mibBuilder.loadTexts:
    sensorZoneEntry.setStatus("mandatory")


class _SensorZoneNumber_Type(Integer32):
    """Custom type sensorZoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SensorZoneNumber_Type.__name__ = "Integer32"
_SensorZoneNumber_Object = MibTableColumn
sensorZoneNumber = _SensorZoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 5, 1, 1),
    _SensorZoneNumber_Type()
)
sensorZoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorZoneNumber.setStatus("mandatory")


class _SensorZoneOptions_Type(Integer32):
    """Custom type sensorZoneOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SensorZoneOptions_Type.__name__ = "Integer32"
_SensorZoneOptions_Object = MibTableColumn
sensorZoneOptions = _SensorZoneOptions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 5, 1, 2),
    _SensorZoneOptions_Type()
)
sensorZoneOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorZoneOptions.setStatus("mandatory")


class _SensorZoneSamplePeriod_Type(Integer32):
    """Custom type sensorZoneSamplePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SensorZoneSamplePeriod_Type.__name__ = "Integer32"
_SensorZoneSamplePeriod_Object = MibTableColumn
sensorZoneSamplePeriod = _SensorZoneSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 5, 1, 3),
    _SensorZoneSamplePeriod_Type()
)
sensorZoneSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorZoneSamplePeriod.setStatus("mandatory")


class _SensorZoneLabel_Type(OctetString):
    """Custom type sensorZoneLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SensorZoneLabel_Type.__name__ = "OctetString"
_SensorZoneLabel_Object = MibTableColumn
sensorZoneLabel = _SensorZoneLabel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 5, 1, 4),
    _SensorZoneLabel_Type()
)
sensorZoneLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensorZoneLabel.setStatus("optional")


class _ClockAvailable_Type(Integer32):
    """Custom type clockAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockYes", 1),
          ("clockNo", 2))
    )


_ClockAvailable_Type.__name__ = "Integer32"
_ClockAvailable_Object = MibScalar
clockAvailable = _ClockAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 1, 6),
    _ClockAvailable_Type()
)
clockAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockAvailable.setStatus("mandatory")
_TssControl_ObjectIdentity = ObjectIdentity
tssControl = _TssControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2)
)


class _MaxOutputNumber_Type(Integer32):
    """Custom type maxOutputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxOutputNumber_Type.__name__ = "Integer32"
_MaxOutputNumber_Object = MibScalar
maxOutputNumber = _MaxOutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 1),
    _MaxOutputNumber_Type()
)
maxOutputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxOutputNumber.setStatus("mandatory")
_OutputConfigurationTable_Object = MibTable
outputConfigurationTable = _OutputConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    outputConfigurationTable.setStatus("mandatory")
_OutputConfigurationEntry_Object = MibTableRow
outputConfigurationEntry = _OutputConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 2, 1)
)
outputConfigurationEntry.setIndexNames(
    (0, "TSS-MIB1", "sensorZoneNumber"),
    (0, "TSS-MIB1", "outputNumber"),
)
if mibBuilder.loadTexts:
    outputConfigurationEntry.setStatus("mandatory")


class _OutputNumber_Type(Integer32):
    """Custom type outputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OutputNumber_Type.__name__ = "Integer32"
_OutputNumber_Object = MibTableColumn
outputNumber = _OutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 2, 1, 1),
    _OutputNumber_Type()
)
outputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumber.setStatus("mandatory")


class _OutputConfiguration_Type(Integer32):
    """Custom type outputConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("failsafeModeOn", 1),
          ("failsafeModeOff", 2),
          ("overrideCommandOn", 3),
          ("overrideCommandOff", 4),
          ("commandComplete", 255))
    )


_OutputConfiguration_Type.__name__ = "Integer32"
_OutputConfiguration_Object = MibTableColumn
outputConfiguration = _OutputConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 2, 1, 2),
    _OutputConfiguration_Type()
)
outputConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputConfiguration.setStatus("mandatory")


class _OutputLabel_Type(OctetString):
    """Custom type outputLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OutputLabel_Type.__name__ = "OctetString"
_OutputLabel_Object = MibTableColumn
outputLabel = _OutputLabel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 2, 1, 3),
    _OutputLabel_Type()
)
outputLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputLabel.setStatus("optional")


class _MaxOutputGroups_Type(Integer32):
    """Custom type maxOutputGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MaxOutputGroups_Type.__name__ = "Integer32"
_MaxOutputGroups_Object = MibScalar
maxOutputGroups = _MaxOutputGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 3),
    _MaxOutputGroups_Type()
)
maxOutputGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxOutputGroups.setStatus("mandatory")
_OutputGroupTable_Object = MibTable
outputGroupTable = _OutputGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    outputGroupTable.setStatus("mandatory")
_OutputGroupEntry_Object = MibTableRow
outputGroupEntry = _OutputGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 4, 1)
)
outputGroupEntry.setIndexNames(
    (0, "TSS-MIB1", "outputGroupNumber"),
)
if mibBuilder.loadTexts:
    outputGroupEntry.setStatus("mandatory")


class _OutputGroupNumber_Type(Integer32):
    """Custom type outputGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_OutputGroupNumber_Type.__name__ = "Integer32"
_OutputGroupNumber_Object = MibTableColumn
outputGroupNumber = _OutputGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 4, 1, 1),
    _OutputGroupNumber_Type()
)
outputGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputGroupNumber.setStatus("mandatory")


class _OutputGroupOutputState_Type(OctetString):
    """Custom type outputGroupOutputState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OutputGroupOutputState_Type.__name__ = "OctetString"
_OutputGroupOutputState_Object = MibTableColumn
outputGroupOutputState = _OutputGroupOutputState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 4, 1, 2),
    _OutputGroupOutputState_Type()
)
outputGroupOutputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputGroupOutputState.setStatus("mandatory")


class _OutputGroupReadbackState_Type(OctetString):
    """Custom type outputGroupReadbackState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OutputGroupReadbackState_Type.__name__ = "OctetString"
_OutputGroupReadbackState_Object = MibTableColumn
outputGroupReadbackState = _OutputGroupReadbackState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 2, 4, 1, 3),
    _OutputGroupReadbackState_Type()
)
outputGroupReadbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputGroupReadbackState.setStatus("mandatory")
_TssDataCollection_ObjectIdentity = ObjectIdentity
tssDataCollection = _TssDataCollection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3)
)
_DataCollectionTable_Object = MibTable
dataCollectionTable = _DataCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dataCollectionTable.setStatus("mandatory")
_DataCollectionEntry_Object = MibTableRow
dataCollectionEntry = _DataCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1, 1)
)
dataCollectionEntry.setIndexNames(
    (0, "TSS-MIB1", "sensorZoneNumber"),
    (0, "TSS-MIB1", "outputNumber"),
)
if mibBuilder.loadTexts:
    dataCollectionEntry.setStatus("mandatory")


class _EndTime_Type(Integer32):
    """Custom type endTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EndTime_Type.__name__ = "Integer32"
_EndTime_Object = MibTableColumn
endTime = _EndTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1, 1, 1),
    _EndTime_Type()
)
endTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endTime.setStatus("mandatory")


class _VolumeData_Type(Integer32):
    """Custom type volumeData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VolumeData_Type.__name__ = "Integer32"
_VolumeData_Object = MibTableColumn
volumeData = _VolumeData_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1, 1, 2),
    _VolumeData_Type()
)
volumeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeData.setStatus("mandatory")


class _PercentOccupancy_Type(Integer32):
    """Custom type percentOccupancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PercentOccupancy_Type.__name__ = "Integer32"
_PercentOccupancy_Object = MibTableColumn
percentOccupancy = _PercentOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1, 1, 3),
    _PercentOccupancy_Type()
)
percentOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentOccupancy.setStatus("mandatory")


class _SpeedData_Type(Integer32):
    """Custom type speedData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_SpeedData_Type.__name__ = "Integer32"
_SpeedData_Object = MibTableColumn
speedData = _SpeedData_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1, 1, 4),
    _SpeedData_Type()
)
speedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedData.setStatus("mandatory")


class _ZoneStatus_Type(Integer32):
    """Custom type zoneStatus based on Integer32"""
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
        *(("oK", 1),
          ("initializing", 2),
          ("other", 3),
          ("noActivity", 4),
          ("maxPresence", 5),
          ("configurationError", 6),
          ("erraticCounts", 7),
          ("disabled", 8))
    )


_ZoneStatus_Type.__name__ = "Integer32"
_ZoneStatus_Object = MibTableColumn
zoneStatus = _ZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 1, 1, 5),
    _ZoneStatus_Type()
)
zoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneStatus.setStatus("mandatory")
_DataBufferTable_Object = MibTable
dataBufferTable = _DataBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    dataBufferTable.setStatus("mandatory")
_DataBufferEntry_Object = MibTableRow
dataBufferEntry = _DataBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2, 1)
)
dataBufferEntry.setIndexNames(
    (0, "TSS-MIB1", "sensorZoneNumber"),
    (0, "TSS-MIB1", "outputNumber"),
)
if mibBuilder.loadTexts:
    dataBufferEntry.setStatus("mandatory")


class _EndTimeBuffer_Type(Integer32):
    """Custom type endTimeBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EndTimeBuffer_Type.__name__ = "Integer32"
_EndTimeBuffer_Object = MibTableColumn
endTimeBuffer = _EndTimeBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2, 1, 1),
    _EndTimeBuffer_Type()
)
endTimeBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endTimeBuffer.setStatus("mandatory")


class _VolumeDataBuffer_Type(Integer32):
    """Custom type volumeDataBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VolumeDataBuffer_Type.__name__ = "Integer32"
_VolumeDataBuffer_Object = MibTableColumn
volumeDataBuffer = _VolumeDataBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2, 1, 2),
    _VolumeDataBuffer_Type()
)
volumeDataBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeDataBuffer.setStatus("mandatory")


class _PercentOccupancyBuffer_Type(Integer32):
    """Custom type percentOccupancyBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PercentOccupancyBuffer_Type.__name__ = "Integer32"
_PercentOccupancyBuffer_Object = MibTableColumn
percentOccupancyBuffer = _PercentOccupancyBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2, 1, 3),
    _PercentOccupancyBuffer_Type()
)
percentOccupancyBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentOccupancyBuffer.setStatus("mandatory")


class _SpeedDataBuffer_Type(Integer32):
    """Custom type speedDataBuffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2550),
    )


_SpeedDataBuffer_Type.__name__ = "Integer32"
_SpeedDataBuffer_Object = MibTableColumn
speedDataBuffer = _SpeedDataBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2, 1, 4),
    _SpeedDataBuffer_Type()
)
speedDataBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDataBuffer.setStatus("mandatory")


class _ZoneStatusBuffer_Type(Integer32):
    """Custom type zoneStatusBuffer based on Integer32"""
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
        *(("oK", 1),
          ("initializing", 2),
          ("other", 3),
          ("noActivity", 4),
          ("maxPresence", 5),
          ("configurationError", 6),
          ("erraticCounts", 7),
          ("disabled", 8))
    )


_ZoneStatusBuffer_Type.__name__ = "Integer32"
_ZoneStatusBuffer_Object = MibTableColumn
zoneStatusBuffer = _ZoneStatusBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 3, 2, 1, 5),
    _ZoneStatusBuffer_Type()
)
zoneStatusBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneStatusBuffer.setStatus("mandatory")
_TssEvent_ObjectIdentity = ObjectIdentity
tssEvent = _TssEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 4)
)


class _EventOccurrence_Type(Integer32):
    """Custom type eventOccurrence based on Integer32"""
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
        *(("eventNumber1", 1),
          ("eventNumber2", 2),
          ("eventNumber3", 3),
          ("eventNumber4", 4),
          ("eventNumber5", 5),
          ("eventNumber6", 6),
          ("eventNumber7", 7),
          ("eventNumber8", 8))
    )


_EventOccurrence_Type.__name__ = "Integer32"
_EventOccurrence_Object = MibScalar
eventOccurrence = _EventOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 4, 1),
    _EventOccurrence_Type()
)
eventOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventOccurrence.setStatus("mandatory")


class _EventOccurrenceBuffer_Type(Integer32):
    """Custom type eventOccurrenceBuffer based on Integer32"""
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
        *(("eventNumber1", 1),
          ("eventNumber2", 2),
          ("eventNumber3", 3),
          ("eventNumber4", 4),
          ("eventNumber5", 5),
          ("eventNumber6", 6),
          ("eventNumber7", 7),
          ("eventNumber8", 8))
    )


_EventOccurrenceBuffer_Type.__name__ = "Integer32"
_EventOccurrenceBuffer_Object = MibScalar
eventOccurrenceBuffer = _EventOccurrenceBuffer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 4, 4, 2),
    _EventOccurrenceBuffer_Type()
)
eventOccurrenceBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventOccurrenceBuffer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TSS-MIB1",
    **{"tss": tss,
       "tssSystemSetup": tssSystemSetup,
       "sensorSystemReset": sensorSystemReset,
       "sensorSystemStatus": sensorSystemStatus,
       "sensorSystemDataType": sensorSystemDataType,
       "maxSensorZones": maxSensorZones,
       "sensorZoneTable": sensorZoneTable,
       "sensorZoneEntry": sensorZoneEntry,
       "sensorZoneNumber": sensorZoneNumber,
       "sensorZoneOptions": sensorZoneOptions,
       "sensorZoneSamplePeriod": sensorZoneSamplePeriod,
       "sensorZoneLabel": sensorZoneLabel,
       "clockAvailable": clockAvailable,
       "tssControl": tssControl,
       "maxOutputNumber": maxOutputNumber,
       "outputConfigurationTable": outputConfigurationTable,
       "outputConfigurationEntry": outputConfigurationEntry,
       "outputNumber": outputNumber,
       "outputConfiguration": outputConfiguration,
       "outputLabel": outputLabel,
       "maxOutputGroups": maxOutputGroups,
       "outputGroupTable": outputGroupTable,
       "outputGroupEntry": outputGroupEntry,
       "outputGroupNumber": outputGroupNumber,
       "outputGroupOutputState": outputGroupOutputState,
       "outputGroupReadbackState": outputGroupReadbackState,
       "tssDataCollection": tssDataCollection,
       "dataCollectionTable": dataCollectionTable,
       "dataCollectionEntry": dataCollectionEntry,
       "endTime": endTime,
       "volumeData": volumeData,
       "percentOccupancy": percentOccupancy,
       "speedData": speedData,
       "zoneStatus": zoneStatus,
       "dataBufferTable": dataBufferTable,
       "dataBufferEntry": dataBufferEntry,
       "endTimeBuffer": endTimeBuffer,
       "volumeDataBuffer": volumeDataBuffer,
       "percentOccupancyBuffer": percentOccupancyBuffer,
       "speedDataBuffer": speedDataBuffer,
       "zoneStatusBuffer": zoneStatusBuffer,
       "tssEvent": tssEvent,
       "eventOccurrence": eventOccurrence,
       "eventOccurrenceBuffer": eventOccurrenceBuffer}
)
