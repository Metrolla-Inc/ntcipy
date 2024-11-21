# SNMP MIB module (CCTV-MIB1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1205CCTV.mib
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

(devices,
 profiles) = mibBuilder.importSymbols(
    "TMIB-II",
    "devices",
    "profiles")


# MODULE-IDENTITY


# Types definitions



class PositionReference(OctetString):
    """Custom type PositionReference based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cctv_ObjectIdentity = ObjectIdentity
cctv = _Cctv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7)
)
_CctvRange_ObjectIdentity = ObjectIdentity
cctvRange = _CctvRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1)
)


class _RangeMaximumPreset_Type(Integer32):
    """Custom type rangeMaximumPreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RangeMaximumPreset_Type.__name__ = "Integer32"
_RangeMaximumPreset_Object = MibScalar
rangeMaximumPreset = _RangeMaximumPreset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 1),
    _RangeMaximumPreset_Type()
)
rangeMaximumPreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeMaximumPreset.setStatus("mandatory")


class _RangePanLeftLimit_Type(Integer32):
    """Custom type rangePanLeftLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangePanLeftLimit_Type.__name__ = "Integer32"
_RangePanLeftLimit_Object = MibScalar
rangePanLeftLimit = _RangePanLeftLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 2),
    _RangePanLeftLimit_Type()
)
rangePanLeftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangePanLeftLimit.setStatus("mandatory")


class _RangePanRightLimit_Type(Integer32):
    """Custom type rangePanRightLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangePanRightLimit_Type.__name__ = "Integer32"
_RangePanRightLimit_Object = MibScalar
rangePanRightLimit = _RangePanRightLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 3),
    _RangePanRightLimit_Type()
)
rangePanRightLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangePanRightLimit.setStatus("mandatory")


class _RangePanHomePosition_Type(Integer32):
    """Custom type rangePanHomePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangePanHomePosition_Type.__name__ = "Integer32"
_RangePanHomePosition_Object = MibScalar
rangePanHomePosition = _RangePanHomePosition_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 4),
    _RangePanHomePosition_Type()
)
rangePanHomePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangePanHomePosition.setStatus("mandatory")


class _RangeTrueNorthOffset_Type(Integer32):
    """Custom type rangeTrueNorthOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangeTrueNorthOffset_Type.__name__ = "Integer32"
_RangeTrueNorthOffset_Object = MibScalar
rangeTrueNorthOffset = _RangeTrueNorthOffset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 5),
    _RangeTrueNorthOffset_Type()
)
rangeTrueNorthOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rangeTrueNorthOffset.setStatus("mandatory")


class _RangeTiltUpLimit_Type(Integer32):
    """Custom type rangeTiltUpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangeTiltUpLimit_Type.__name__ = "Integer32"
_RangeTiltUpLimit_Object = MibScalar
rangeTiltUpLimit = _RangeTiltUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 6),
    _RangeTiltUpLimit_Type()
)
rangeTiltUpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeTiltUpLimit.setStatus("mandatory")


class _RangeTiltDownLimit_Type(Integer32):
    """Custom type rangeTiltDownLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangeTiltDownLimit_Type.__name__ = "Integer32"
_RangeTiltDownLimit_Object = MibScalar
rangeTiltDownLimit = _RangeTiltDownLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 7),
    _RangeTiltDownLimit_Type()
)
rangeTiltDownLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeTiltDownLimit.setStatus("mandatory")


class _RangeZoomLimit_Type(Integer32):
    """Custom type rangeZoomLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RangeZoomLimit_Type.__name__ = "Integer32"
_RangeZoomLimit_Object = MibScalar
rangeZoomLimit = _RangeZoomLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 8),
    _RangeZoomLimit_Type()
)
rangeZoomLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeZoomLimit.setStatus("mandatory")


class _RangeFocusLimit_Type(Integer32):
    """Custom type rangeFocusLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RangeFocusLimit_Type.__name__ = "Integer32"
_RangeFocusLimit_Object = MibScalar
rangeFocusLimit = _RangeFocusLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 9),
    _RangeFocusLimit_Type()
)
rangeFocusLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeFocusLimit.setStatus("mandatory")


class _RangeIrisLimit_Type(Integer32):
    """Custom type rangeIrisLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RangeIrisLimit_Type.__name__ = "Integer32"
_RangeIrisLimit_Object = MibScalar
rangeIrisLimit = _RangeIrisLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 10),
    _RangeIrisLimit_Type()
)
rangeIrisLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeIrisLimit.setStatus("mandatory")


class _RangeMinimumPanStepAngle_Type(Integer32):
    """Custom type rangeMinimumPanStepAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangeMinimumPanStepAngle_Type.__name__ = "Integer32"
_RangeMinimumPanStepAngle_Object = MibScalar
rangeMinimumPanStepAngle = _RangeMinimumPanStepAngle_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 11),
    _RangeMinimumPanStepAngle_Type()
)
rangeMinimumPanStepAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeMinimumPanStepAngle.setStatus("mandatory")


class _RangeMinimumTiltStepAngle_Type(Integer32):
    """Custom type rangeMinimumTiltStepAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_RangeMinimumTiltStepAngle_Type.__name__ = "Integer32"
_RangeMinimumTiltStepAngle_Object = MibScalar
rangeMinimumTiltStepAngle = _RangeMinimumTiltStepAngle_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 1, 12),
    _RangeMinimumTiltStepAngle_Type()
)
rangeMinimumTiltStepAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rangeMinimumTiltStepAngle.setStatus("mandatory")
_CctvTimeout_ObjectIdentity = ObjectIdentity
cctvTimeout = _CctvTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 2)
)


class _TimeoutPan_Type(Integer32):
    """Custom type timeoutPan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimeoutPan_Type.__name__ = "Integer32"
_TimeoutPan_Object = MibScalar
timeoutPan = _TimeoutPan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 2, 1),
    _TimeoutPan_Type()
)
timeoutPan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeoutPan.setStatus("mandatory")


class _TimeoutTilt_Type(Integer32):
    """Custom type timeoutTilt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimeoutTilt_Type.__name__ = "Integer32"
_TimeoutTilt_Object = MibScalar
timeoutTilt = _TimeoutTilt_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 2, 2),
    _TimeoutTilt_Type()
)
timeoutTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeoutTilt.setStatus("mandatory")


class _TimeoutZoom_Type(Integer32):
    """Custom type timeoutZoom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimeoutZoom_Type.__name__ = "Integer32"
_TimeoutZoom_Object = MibScalar
timeoutZoom = _TimeoutZoom_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 2, 3),
    _TimeoutZoom_Type()
)
timeoutZoom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeoutZoom.setStatus("mandatory")


class _TimeoutFocus_Type(Integer32):
    """Custom type timeoutFocus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimeoutFocus_Type.__name__ = "Integer32"
_TimeoutFocus_Object = MibScalar
timeoutFocus = _TimeoutFocus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 2, 4),
    _TimeoutFocus_Type()
)
timeoutFocus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeoutFocus.setStatus("mandatory")


class _TimeoutIris_Type(Integer32):
    """Custom type timeoutIris based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimeoutIris_Type.__name__ = "Integer32"
_TimeoutIris_Object = MibScalar
timeoutIris = _TimeoutIris_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 2, 5),
    _TimeoutIris_Type()
)
timeoutIris.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeoutIris.setStatus("mandatory")
_CctvPreset_ObjectIdentity = ObjectIdentity
cctvPreset = _CctvPreset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 3)
)


class _PresetGotoPosition_Type(Integer32):
    """Custom type presetGotoPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PresetGotoPosition_Type.__name__ = "Integer32"
_PresetGotoPosition_Object = MibScalar
presetGotoPosition = _PresetGotoPosition_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 3, 1),
    _PresetGotoPosition_Type()
)
presetGotoPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presetGotoPosition.setStatus("mandatory")


class _PresetStorePosition_Type(Integer32):
    """Custom type presetStorePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PresetStorePosition_Type.__name__ = "Integer32"
_PresetStorePosition_Object = MibScalar
presetStorePosition = _PresetStorePosition_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 3, 2),
    _PresetStorePosition_Type()
)
presetStorePosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    presetStorePosition.setStatus("mandatory")
_CctvPosition_ObjectIdentity = ObjectIdentity
cctvPosition = _CctvPosition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 4)
)
_PositionPan_Type = PositionReference
_PositionPan_Object = MibScalar
positionPan = _PositionPan_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 4, 1),
    _PositionPan_Type()
)
positionPan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    positionPan.setStatus("mandatory")
_PositionTilt_Type = PositionReference
_PositionTilt_Object = MibScalar
positionTilt = _PositionTilt_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 4, 2),
    _PositionTilt_Type()
)
positionTilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    positionTilt.setStatus("mandatory")
_PositionZoomLens_Type = PositionReference
_PositionZoomLens_Object = MibScalar
positionZoomLens = _PositionZoomLens_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 4, 3),
    _PositionZoomLens_Type()
)
positionZoomLens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    positionZoomLens.setStatus("mandatory")
_PositionFocusLens_Type = PositionReference
_PositionFocusLens_Object = MibScalar
positionFocusLens = _PositionFocusLens_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 4, 4),
    _PositionFocusLens_Type()
)
positionFocusLens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    positionFocusLens.setStatus("mandatory")
_PositionIrisLens_Type = PositionReference
_PositionIrisLens_Object = MibScalar
positionIrisLens = _PositionIrisLens_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 4, 5),
    _PositionIrisLens_Type()
)
positionIrisLens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    positionIrisLens.setStatus("mandatory")
_CctvSystem_ObjectIdentity = ObjectIdentity
cctvSystem = _CctvSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5)
)


class _SystemCameraFeatureControl_Type(OctetString):
    """Custom type systemCameraFeatureControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_SystemCameraFeatureControl_Type.__name__ = "OctetString"
_SystemCameraFeatureControl_Object = MibScalar
systemCameraFeatureControl = _SystemCameraFeatureControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5, 1),
    _SystemCameraFeatureControl_Type()
)
systemCameraFeatureControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemCameraFeatureControl.setStatus("mandatory")


class _SystemCameraFeatureStatus_Type(OctetString):
    """Custom type systemCameraFeatureStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_SystemCameraFeatureStatus_Type.__name__ = "OctetString"
_SystemCameraFeatureStatus_Object = MibScalar
systemCameraFeatureStatus = _SystemCameraFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5, 2),
    _SystemCameraFeatureStatus_Type()
)
systemCameraFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCameraFeatureStatus.setStatus("mandatory")


class _SystemCameraEquipped_Type(OctetString):
    """Custom type systemCameraEquipped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_SystemCameraEquipped_Type.__name__ = "OctetString"
_SystemCameraEquipped_Object = MibScalar
systemCameraEquipped = _SystemCameraEquipped_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5, 3),
    _SystemCameraEquipped_Type()
)
systemCameraEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemCameraEquipped.setStatus("mandatory")


class _SystemLensFeatureControl_Type(OctetString):
    """Custom type systemLensFeatureControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_SystemLensFeatureControl_Type.__name__ = "OctetString"
_SystemLensFeatureControl_Object = MibScalar
systemLensFeatureControl = _SystemLensFeatureControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5, 4),
    _SystemLensFeatureControl_Type()
)
systemLensFeatureControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLensFeatureControl.setStatus("mandatory")


class _SystemLensFeatureStatus_Type(OctetString):
    """Custom type systemLensFeatureStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_SystemLensFeatureStatus_Type.__name__ = "OctetString"
_SystemLensFeatureStatus_Object = MibScalar
systemLensFeatureStatus = _SystemLensFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5, 5),
    _SystemLensFeatureStatus_Type()
)
systemLensFeatureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLensFeatureStatus.setStatus("mandatory")


class _SystemLensEquipped_Type(OctetString):
    """Custom type systemLensEquipped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_SystemLensEquipped_Type.__name__ = "OctetString"
_SystemLensEquipped_Object = MibScalar
systemLensEquipped = _SystemLensEquipped_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 5, 6),
    _SystemLensEquipped_Type()
)
systemLensEquipped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLensEquipped.setStatus("mandatory")
_CctvAlarm_ObjectIdentity = ObjectIdentity
cctvAlarm = _CctvAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6)
)


class _AlarmStatus_Type(OctetString):
    """Custom type alarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmStatus_Type.__name__ = "OctetString"
_AlarmStatus_Object = MibScalar
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 1),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")


class _AlarmLatchStatus_Type(OctetString):
    """Custom type alarmLatchStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmLatchStatus_Type.__name__ = "OctetString"
_AlarmLatchStatus_Object = MibScalar
alarmLatchStatus = _AlarmLatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 2),
    _AlarmLatchStatus_Type()
)
alarmLatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLatchStatus.setStatus("mandatory")


class _AlarmLatchClear_Type(OctetString):
    """Custom type alarmLatchClear based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmLatchClear_Type.__name__ = "OctetString"
_AlarmLatchClear_Object = MibScalar
alarmLatchClear = _AlarmLatchClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 3),
    _AlarmLatchClear_Type()
)
alarmLatchClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmLatchClear.setStatus("mandatory")


class _AlarmTemparatureHighLowThreshold_Type(OctetString):
    """Custom type alarmTemparatureHighLowThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_AlarmTemparatureHighLowThreshold_Type.__name__ = "OctetString"
_AlarmTemparatureHighLowThreshold_Object = MibScalar
alarmTemparatureHighLowThreshold = _AlarmTemparatureHighLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 4),
    _AlarmTemparatureHighLowThreshold_Type()
)
alarmTemparatureHighLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTemparatureHighLowThreshold.setStatus("mandatory")


class _AlarmTemparatureCurrentValue_Type(OctetString):
    """Custom type alarmTemparatureCurrentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmTemparatureCurrentValue_Type.__name__ = "OctetString"
_AlarmTemparatureCurrentValue_Object = MibScalar
alarmTemparatureCurrentValue = _AlarmTemparatureCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 5),
    _AlarmTemparatureCurrentValue_Type()
)
alarmTemparatureCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTemparatureCurrentValue.setStatus("mandatory")


class _AlarmPresureHighLowThreshold_Type(OctetString):
    """Custom type alarmPresureHighLowThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_AlarmPresureHighLowThreshold_Type.__name__ = "OctetString"
_AlarmPresureHighLowThreshold_Object = MibScalar
alarmPresureHighLowThreshold = _AlarmPresureHighLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 6),
    _AlarmPresureHighLowThreshold_Type()
)
alarmPresureHighLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPresureHighLowThreshold.setStatus("mandatory")


class _AlarmPresureCurrentValue_Type(OctetString):
    """Custom type alarmPresureCurrentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmPresureCurrentValue_Type.__name__ = "OctetString"
_AlarmPresureCurrentValue_Object = MibScalar
alarmPresureCurrentValue = _AlarmPresureCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 7),
    _AlarmPresureCurrentValue_Type()
)
alarmPresureCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmPresureCurrentValue.setStatus("mandatory")


class _AlarmWasherFluidHighLowThreshold_Type(OctetString):
    """Custom type alarmWasherFluidHighLowThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_AlarmWasherFluidHighLowThreshold_Type.__name__ = "OctetString"
_AlarmWasherFluidHighLowThreshold_Object = MibScalar
alarmWasherFluidHighLowThreshold = _AlarmWasherFluidHighLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 8),
    _AlarmWasherFluidHighLowThreshold_Type()
)
alarmWasherFluidHighLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmWasherFluidHighLowThreshold.setStatus("mandatory")


class _AlarmWasherFluidCurrentValue_Type(OctetString):
    """Custom type alarmWasherFluidCurrentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_AlarmWasherFluidCurrentValue_Type.__name__ = "OctetString"
_AlarmWasherFluidCurrentValue_Object = MibScalar
alarmWasherFluidCurrentValue = _AlarmWasherFluidCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 9),
    _AlarmWasherFluidCurrentValue_Type()
)
alarmWasherFluidCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmWasherFluidCurrentValue.setStatus("mandatory")


class _AlarmLabelIndex_Type(OctetString):
    """Custom type alarmLabelIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixedLength = 7


_AlarmLabelIndex_Type.__name__ = "OctetString"
_AlarmLabelIndex_Object = MibScalar
alarmLabelIndex = _AlarmLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 6, 10),
    _AlarmLabelIndex_Type()
)
alarmLabelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmLabelIndex.setStatus("mandatory")
_CctvInput_ObjectIdentity = ObjectIdentity
cctvInput = _CctvInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 7)
)


class _InputStatus_Type(OctetString):
    """Custom type inputStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_InputStatus_Type.__name__ = "OctetString"
_InputStatus_Object = MibScalar
inputStatus = _InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 7, 1),
    _InputStatus_Type()
)
inputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputStatus.setStatus("mandatory")


class _InputLatchStatus_Type(OctetString):
    """Custom type inputLatchStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_InputLatchStatus_Type.__name__ = "OctetString"
_InputLatchStatus_Object = MibScalar
inputLatchStatus = _InputLatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 7, 2),
    _InputLatchStatus_Type()
)
inputLatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLatchStatus.setStatus("mandatory")


class _InputLatchClear_Type(OctetString):
    """Custom type inputLatchClear based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_InputLatchClear_Type.__name__ = "OctetString"
_InputLatchClear_Object = MibScalar
inputLatchClear = _InputLatchClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 7, 3),
    _InputLatchClear_Type()
)
inputLatchClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputLatchClear.setStatus("mandatory")


class _InputLabelIndex_Type(OctetString):
    """Custom type inputLabelIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_InputLabelIndex_Type.__name__ = "OctetString"
_InputLabelIndex_Object = MibScalar
inputLabelIndex = _InputLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 7, 4),
    _InputLabelIndex_Type()
)
inputLabelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputLabelIndex.setStatus("mandatory")
_CctvOutput_ObjectIdentity = ObjectIdentity
cctvOutput = _CctvOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 8)
)


class _OutputStatus_Type(OctetString):
    """Custom type outputStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_OutputStatus_Type.__name__ = "OctetString"
_OutputStatus_Object = MibScalar
outputStatus = _OutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 8, 1),
    _OutputStatus_Type()
)
outputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputStatus.setStatus("mandatory")


class _OutputControl_Type(OctetString):
    """Custom type outputControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2


_OutputControl_Type.__name__ = "OctetString"
_OutputControl_Object = MibScalar
outputControl = _OutputControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 8, 2),
    _OutputControl_Type()
)
outputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputControl.setStatus("mandatory")


class _OutputLabelIndex_Type(OctetString):
    """Custom type outputLabelIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8


_OutputLabelIndex_Type.__name__ = "OctetString"
_OutputLabelIndex_Object = MibScalar
outputLabelIndex = _OutputLabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 8, 3),
    _OutputLabelIndex_Type()
)
outputLabelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputLabelIndex.setStatus("mandatory")
_CctvZone_ObjectIdentity = ObjectIdentity
cctvZone = _CctvZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9)
)


class _ZoneMaximum_Type(Integer32):
    """Custom type zoneMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZoneMaximum_Type.__name__ = "Integer32"
_ZoneMaximum_Object = MibScalar
zoneMaximum = _ZoneMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 1),
    _ZoneMaximum_Type()
)
zoneMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneMaximum.setStatus("mandatory")
_ZoneTable_Object = MibTable
zoneTable = _ZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2)
)
if mibBuilder.loadTexts:
    zoneTable.setStatus("mandatory")
_ZoneEntry_Object = MibTableRow
zoneEntry = _ZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1)
)
zoneEntry.setIndexNames(
    (0, "CCTV-MIB1", "zoneIndex"),
)
if mibBuilder.loadTexts:
    zoneEntry.setStatus("mandatory")


class _ZoneIndex_Type(Integer32):
    """Custom type zoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZoneIndex_Type.__name__ = "Integer32"
_ZoneIndex_Object = MibTableColumn
zoneIndex = _ZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1, 1),
    _ZoneIndex_Type()
)
zoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneIndex.setStatus("mandatory")


class _ZoneLabel_Type(Integer32):
    """Custom type zoneLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZoneLabel_Type.__name__ = "Integer32"
_ZoneLabel_Object = MibTableColumn
zoneLabel = _ZoneLabel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1, 2),
    _ZoneLabel_Type()
)
zoneLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zoneLabel.setStatus("mandatory")


class _ZonePanLeftLimit_Type(Integer32):
    """Custom type zonePanLeftLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_ZonePanLeftLimit_Type.__name__ = "Integer32"
_ZonePanLeftLimit_Object = MibTableColumn
zonePanLeftLimit = _ZonePanLeftLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1, 3),
    _ZonePanLeftLimit_Type()
)
zonePanLeftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonePanLeftLimit.setStatus("mandatory")


class _ZonePanRightLimit_Type(Integer32):
    """Custom type zonePanRightLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_ZonePanRightLimit_Type.__name__ = "Integer32"
_ZonePanRightLimit_Object = MibTableColumn
zonePanRightLimit = _ZonePanRightLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1, 4),
    _ZonePanRightLimit_Type()
)
zonePanRightLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonePanRightLimit.setStatus("mandatory")


class _ZoneTiltUpLimit_Type(Integer32):
    """Custom type zoneTiltUpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_ZoneTiltUpLimit_Type.__name__ = "Integer32"
_ZoneTiltUpLimit_Object = MibTableColumn
zoneTiltUpLimit = _ZoneTiltUpLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1, 5),
    _ZoneTiltUpLimit_Type()
)
zoneTiltUpLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTiltUpLimit.setStatus("mandatory")


class _ZoneTiltDownLimit_Type(Integer32):
    """Custom type zoneTiltDownLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35999),
    )


_ZoneTiltDownLimit_Type.__name__ = "Integer32"
_ZoneTiltDownLimit_Object = MibTableColumn
zoneTiltDownLimit = _ZoneTiltDownLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 9, 2, 1, 6),
    _ZoneTiltDownLimit_Type()
)
zoneTiltDownLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneTiltDownLimit.setStatus("mandatory")
_CctvLabel_ObjectIdentity = ObjectIdentity
cctvLabel = _CctvLabel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10)
)


class _LabelMaximum_Type(Integer32):
    """Custom type labelMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelMaximum_Type.__name__ = "Integer32"
_LabelMaximum_Object = MibScalar
labelMaximum = _LabelMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 1),
    _LabelMaximum_Type()
)
labelMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelMaximum.setStatus("mandatory")
_LabelTable_Object = MibTable
labelTable = _LabelTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2)
)
if mibBuilder.loadTexts:
    labelTable.setStatus("mandatory")
_LabelEntry_Object = MibTableRow
labelEntry = _LabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1)
)
labelEntry.setIndexNames(
    (0, "CCTV-MIB1", "labelIndex"),
)
if mibBuilder.loadTexts:
    labelEntry.setStatus("mandatory")


class _LabelIndex_Type(Integer32):
    """Custom type labelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelIndex_Type.__name__ = "Integer32"
_LabelIndex_Object = MibTableColumn
labelIndex = _LabelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 1),
    _LabelIndex_Type()
)
labelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelIndex.setStatus("mandatory")


class _LabelText_Type(OctetString):
    """Custom type labelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LabelText_Type.__name__ = "OctetString"
_LabelText_Object = MibTableColumn
labelText = _LabelText_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 2),
    _LabelText_Type()
)
labelText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelText.setStatus("mandatory")


class _LabelFontType_Type(Integer32):
    """Custom type labelFontType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelFontType_Type.__name__ = "Integer32"
_LabelFontType_Object = MibTableColumn
labelFontType = _LabelFontType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 3),
    _LabelFontType_Type()
)
labelFontType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelFontType.setStatus("mandatory")


class _LabelHeight_Type(Integer32):
    """Custom type labelHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelHeight_Type.__name__ = "Integer32"
_LabelHeight_Object = MibTableColumn
labelHeight = _LabelHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 4),
    _LabelHeight_Type()
)
labelHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelHeight.setStatus("mandatory")


class _LabelColor_Type(Integer32):
    """Custom type labelColor based on Integer32"""
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
        *(("blue", 1),
          ("green", 2),
          ("cyan", 3),
          ("red", 4),
          ("magenta", 5),
          ("brown", 6),
          ("white", 7),
          ("grey", 8),
          ("lightBlue", 9),
          ("lightGreen", 10),
          ("lightCyan", 11),
          ("lightRed", 12),
          ("lightMagenta", 13),
          ("yellow", 14),
          ("brightWhite", 15),
          ("black", 16))
    )


_LabelColor_Type.__name__ = "Integer32"
_LabelColor_Object = MibTableColumn
labelColor = _LabelColor_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 5),
    _LabelColor_Type()
)
labelColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelColor.setStatus("mandatory")


class _LabelStartRow_Type(Integer32):
    """Custom type labelStartRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelStartRow_Type.__name__ = "Integer32"
_LabelStartRow_Object = MibTableColumn
labelStartRow = _LabelStartRow_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 6),
    _LabelStartRow_Type()
)
labelStartRow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelStartRow.setStatus("mandatory")


class _LabelStartColumn_Type(Integer32):
    """Custom type labelStartColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelStartColumn_Type.__name__ = "Integer32"
_LabelStartColumn_Object = MibTableColumn
labelStartColumn = _LabelStartColumn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 7),
    _LabelStartColumn_Type()
)
labelStartColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelStartColumn.setStatus("mandatory")


class _LabelStatus_Type(OctetString):
    """Custom type labelStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_LabelStatus_Type.__name__ = "OctetString"
_LabelStatus_Object = MibTableColumn
labelStatus = _LabelStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 2, 1, 8),
    _LabelStatus_Type()
)
labelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelStatus.setStatus("mandatory")


class _LabelLocationLabel_Type(Integer32):
    """Custom type labelLocationLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LabelLocationLabel_Type.__name__ = "Integer32"
_LabelLocationLabel_Object = MibScalar
labelLocationLabel = _LabelLocationLabel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 3),
    _LabelLocationLabel_Type()
)
labelLocationLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelLocationLabel.setStatus("mandatory")


class _LabelEnableTextDisplay_Type(OctetString):
    """Custom type labelEnableTextDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_LabelEnableTextDisplay_Type.__name__ = "OctetString"
_LabelEnableTextDisplay_Object = MibScalar
labelEnableTextDisplay = _LabelEnableTextDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 10, 4),
    _LabelEnableTextDisplay_Type()
)
labelEnableTextDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelEnableTextDisplay.setStatus("mandatory")
_CctvMenu_ObjectIdentity = ObjectIdentity
cctvMenu = _CctvMenu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 11)
)


class _MenuActivate_Type(Integer32):
    """Custom type menuActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MenuActivate_Type.__name__ = "Integer32"
_MenuActivate_Object = MibScalar
menuActivate = _MenuActivate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 11, 1),
    _MenuActivate_Type()
)
menuActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuActivate.setStatus("mandatory")


class _MenuControl_Type(Integer32):
    """Custom type menuControl based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pageDown", 1),
          ("pageUp", 2),
          ("cursorUp", 3),
          ("cursorDown", 4),
          ("cursorRight", 5),
          ("cursorLeft", 6),
          ("incrementValue", 7),
          ("decrementValue", 8),
          ("enterValue", 9),
          ("noMenu", 255))
    )


_MenuControl_Type.__name__ = "Integer32"
_MenuControl_Object = MibScalar
menuControl = _MenuControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 7, 11, 2),
    _MenuControl_Type()
)
menuControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuControl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CCTV-MIB1",
    **{"PositionReference": PositionReference,
       "cctv": cctv,
       "cctvRange": cctvRange,
       "rangeMaximumPreset": rangeMaximumPreset,
       "rangePanLeftLimit": rangePanLeftLimit,
       "rangePanRightLimit": rangePanRightLimit,
       "rangePanHomePosition": rangePanHomePosition,
       "rangeTrueNorthOffset": rangeTrueNorthOffset,
       "rangeTiltUpLimit": rangeTiltUpLimit,
       "rangeTiltDownLimit": rangeTiltDownLimit,
       "rangeZoomLimit": rangeZoomLimit,
       "rangeFocusLimit": rangeFocusLimit,
       "rangeIrisLimit": rangeIrisLimit,
       "rangeMinimumPanStepAngle": rangeMinimumPanStepAngle,
       "rangeMinimumTiltStepAngle": rangeMinimumTiltStepAngle,
       "cctvTimeout": cctvTimeout,
       "timeoutPan": timeoutPan,
       "timeoutTilt": timeoutTilt,
       "timeoutZoom": timeoutZoom,
       "timeoutFocus": timeoutFocus,
       "timeoutIris": timeoutIris,
       "cctvPreset": cctvPreset,
       "presetGotoPosition": presetGotoPosition,
       "presetStorePosition": presetStorePosition,
       "cctvPosition": cctvPosition,
       "positionPan": positionPan,
       "positionTilt": positionTilt,
       "positionZoomLens": positionZoomLens,
       "positionFocusLens": positionFocusLens,
       "positionIrisLens": positionIrisLens,
       "cctvSystem": cctvSystem,
       "systemCameraFeatureControl": systemCameraFeatureControl,
       "systemCameraFeatureStatus": systemCameraFeatureStatus,
       "systemCameraEquipped": systemCameraEquipped,
       "systemLensFeatureControl": systemLensFeatureControl,
       "systemLensFeatureStatus": systemLensFeatureStatus,
       "systemLensEquipped": systemLensEquipped,
       "cctvAlarm": cctvAlarm,
       "alarmStatus": alarmStatus,
       "alarmLatchStatus": alarmLatchStatus,
       "alarmLatchClear": alarmLatchClear,
       "alarmTemparatureHighLowThreshold": alarmTemparatureHighLowThreshold,
       "alarmTemparatureCurrentValue": alarmTemparatureCurrentValue,
       "alarmPresureHighLowThreshold": alarmPresureHighLowThreshold,
       "alarmPresureCurrentValue": alarmPresureCurrentValue,
       "alarmWasherFluidHighLowThreshold": alarmWasherFluidHighLowThreshold,
       "alarmWasherFluidCurrentValue": alarmWasherFluidCurrentValue,
       "alarmLabelIndex": alarmLabelIndex,
       "cctvInput": cctvInput,
       "inputStatus": inputStatus,
       "inputLatchStatus": inputLatchStatus,
       "inputLatchClear": inputLatchClear,
       "inputLabelIndex": inputLabelIndex,
       "cctvOutput": cctvOutput,
       "outputStatus": outputStatus,
       "outputControl": outputControl,
       "outputLabelIndex": outputLabelIndex,
       "cctvZone": cctvZone,
       "zoneMaximum": zoneMaximum,
       "zoneTable": zoneTable,
       "zoneEntry": zoneEntry,
       "zoneIndex": zoneIndex,
       "zoneLabel": zoneLabel,
       "zonePanLeftLimit": zonePanLeftLimit,
       "zonePanRightLimit": zonePanRightLimit,
       "zoneTiltUpLimit": zoneTiltUpLimit,
       "zoneTiltDownLimit": zoneTiltDownLimit,
       "cctvLabel": cctvLabel,
       "labelMaximum": labelMaximum,
       "labelTable": labelTable,
       "labelEntry": labelEntry,
       "labelIndex": labelIndex,
       "labelText": labelText,
       "labelFontType": labelFontType,
       "labelHeight": labelHeight,
       "labelColor": labelColor,
       "labelStartRow": labelStartRow,
       "labelStartColumn": labelStartColumn,
       "labelStatus": labelStatus,
       "labelLocationLabel": labelLocationLabel,
       "labelEnableTextDisplay": labelEnableTextDisplay,
       "cctvMenu": cctvMenu,
       "menuActivate": menuActivate,
       "menuControl": menuControl}
)
