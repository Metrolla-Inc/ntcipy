# SNMP MIB module (CCTVSwitch-MIB1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1208SW.mib
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

_CctvSwitch_ObjectIdentity = ObjectIdentity
cctvSwitch = _CctvSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8)
)
_CctvSwitchInput_ObjectIdentity = ObjectIdentity
cctvSwitchInput = _CctvSwitchInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1)
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 3),
    _InputLatchClear_Type()
)
inputLatchClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputLatchClear.setStatus("mandatory")
_InputTable_Object = MibTable
inputTable = _InputTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    inputTable.setStatus("mandatory")
_InputTableEntry_Object = MibTableRow
inputTableEntry = _InputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 4, 1)
)
inputTableEntry.setIndexNames(
    (0, "CCTVSwitch-MIB1", "inputNumber"),
)
if mibBuilder.loadTexts:
    inputTableEntry.setStatus("mandatory")


class _InputNumber_Type(Integer32):
    """Custom type inputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InputNumber_Type.__name__ = "Integer32"
_InputNumber_Object = MibTableColumn
inputNumber = _InputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 4, 1, 1),
    _InputNumber_Type()
)
inputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputNumber.setStatus("mandatory")


class _InputMonitorPortNumber_Type(Integer32):
    """Custom type inputMonitorPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InputMonitorPortNumber_Type.__name__ = "Integer32"
_InputMonitorPortNumber_Object = MibTableColumn
inputMonitorPortNumber = _InputMonitorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 4, 1, 2),
    _InputMonitorPortNumber_Type()
)
inputMonitorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputMonitorPortNumber.setStatus("mandatory")


class _InputCameraPortNumber_Type(Integer32):
    """Custom type inputCameraPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InputCameraPortNumber_Type.__name__ = "Integer32"
_InputCameraPortNumber_Object = MibTableColumn
inputCameraPortNumber = _InputCameraPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 4, 1, 3),
    _InputCameraPortNumber_Type()
)
inputCameraPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCameraPortNumber.setStatus("mandatory")


class _InputLabelNumber_Type(Integer32):
    """Custom type inputLabelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InputLabelNumber_Type.__name__ = "Integer32"
_InputLabelNumber_Object = MibTableColumn
inputLabelNumber = _InputLabelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 1, 4, 1, 4),
    _InputLabelNumber_Type()
)
inputLabelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputLabelNumber.setStatus("mandatory")
_CctvSwitchOutput_ObjectIdentity = ObjectIdentity
cctvSwitchOutput = _CctvSwitchOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2)
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 2),
    _OutputControl_Type()
)
outputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputControl.setStatus("mandatory")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 3)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("mandatory")
_OutputTableEntry_Object = MibTableRow
outputTableEntry = _OutputTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 3, 1)
)
outputTableEntry.setIndexNames(
    (0, "CCTVSwitch-MIB1", "outputNumber"),
)
if mibBuilder.loadTexts:
    outputTableEntry.setStatus("mandatory")


class _OutputNumber_Type(Integer32):
    """Custom type outputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OutputNumber_Type.__name__ = "Integer32"
_OutputNumber_Object = MibTableColumn
outputNumber = _OutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 3, 1, 1),
    _OutputNumber_Type()
)
outputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputNumber.setStatus("mandatory")


class _OutputMonitorPortNumber_Type(Integer32):
    """Custom type outputMonitorPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutputMonitorPortNumber_Type.__name__ = "Integer32"
_OutputMonitorPortNumber_Object = MibTableColumn
outputMonitorPortNumber = _OutputMonitorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 3, 1, 2),
    _OutputMonitorPortNumber_Type()
)
outputMonitorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputMonitorPortNumber.setStatus("mandatory")


class _OutputCameraPortNumber_Type(Integer32):
    """Custom type outputCameraPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OutputCameraPortNumber_Type.__name__ = "Integer32"
_OutputCameraPortNumber_Object = MibTableColumn
outputCameraPortNumber = _OutputCameraPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 3, 1, 3),
    _OutputCameraPortNumber_Type()
)
outputCameraPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCameraPortNumber.setStatus("mandatory")


class _OutputLabelNumber_Type(Integer32):
    """Custom type outputLabelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OutputLabelNumber_Type.__name__ = "Integer32"
_OutputLabelNumber_Object = MibTableColumn
outputLabelNumber = _OutputLabelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 2, 3, 1, 4),
    _OutputLabelNumber_Type()
)
outputLabelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputLabelNumber.setStatus("mandatory")
_CctvSwitchLabel_ObjectIdentity = ObjectIdentity
cctvSwitchLabel = _CctvSwitchLabel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3)
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 1),
    _LabelMaximum_Type()
)
labelMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelMaximum.setStatus("mandatory")
_LabelSwitchTable_Object = MibTable
labelSwitchTable = _LabelSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    labelSwitchTable.setStatus("mandatory")
_LabelSwitchEntry_Object = MibTableRow
labelSwitchEntry = _LabelSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1)
)
labelSwitchEntry.setIndexNames(
    (0, "CCTVSwitch-MIB1", "labelNumber"),
)
if mibBuilder.loadTexts:
    labelSwitchEntry.setStatus("mandatory")


class _LabelNumber_Type(Integer32):
    """Custom type labelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LabelNumber_Type.__name__ = "Integer32"
_LabelNumber_Object = MibTableColumn
labelNumber = _LabelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 1),
    _LabelNumber_Type()
)
labelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    labelNumber.setStatus("mandatory")


class _LabelText_Type(OctetString):
    """Custom type labelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LabelText_Type.__name__ = "OctetString"
_LabelText_Object = MibTableColumn
labelText = _LabelText_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 7),
    _LabelStartColumn_Type()
)
labelStartColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelStartColumn.setStatus("mandatory")


class _LabelActive_Type(OctetString):
    """Custom type labelActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixedLength = 1


_LabelActive_Type.__name__ = "OctetString"
_LabelActive_Object = MibTableColumn
labelActive = _LabelActive_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 3, 2, 1, 8),
    _LabelActive_Type()
)
labelActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    labelActive.setStatus("mandatory")
_CctvSwitchAssignment_ObjectIdentity = ObjectIdentity
cctvSwitchAssignment = _CctvSwitchAssignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4)
)


class _CctvSwitchAssignmentMaximumCameraPorts_Type(Integer32):
    """Custom type cctvSwitchAssignmentMaximumCameraPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CctvSwitchAssignmentMaximumCameraPorts_Type.__name__ = "Integer32"
_CctvSwitchAssignmentMaximumCameraPorts_Object = MibScalar
cctvSwitchAssignmentMaximumCameraPorts = _CctvSwitchAssignmentMaximumCameraPorts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 1),
    _CctvSwitchAssignmentMaximumCameraPorts_Type()
)
cctvSwitchAssignmentMaximumCameraPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentMaximumCameraPorts.setStatus("mandatory")


class _CctvSwitchAssignmentMaximumMonitorPorts_Type(Integer32):
    """Custom type cctvSwitchAssignmentMaximumMonitorPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CctvSwitchAssignmentMaximumMonitorPorts_Type.__name__ = "Integer32"
_CctvSwitchAssignmentMaximumMonitorPorts_Object = MibScalar
cctvSwitchAssignmentMaximumMonitorPorts = _CctvSwitchAssignmentMaximumMonitorPorts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 2),
    _CctvSwitchAssignmentMaximumMonitorPorts_Type()
)
cctvSwitchAssignmentMaximumMonitorPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentMaximumMonitorPorts.setStatus("mandatory")
_CctvSwitchAssignmentTable_Object = MibTable
cctvSwitchAssignmentTable = _CctvSwitchAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3)
)
if mibBuilder.loadTexts:
    cctvSwitchAssignmentTable.setStatus("mandatory")
_CctvSwitchAssignmentTableEntry_Object = MibTableRow
cctvSwitchAssignmentTableEntry = _CctvSwitchAssignmentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1)
)
cctvSwitchAssignmentTableEntry.setIndexNames(
    (0, "CCTVSwitch-MIB1", "cctvSwitchAssignmentMonitorPortNumber"),
)
if mibBuilder.loadTexts:
    cctvSwitchAssignmentTableEntry.setStatus("mandatory")


class _CctvSwitchAssignmentMonitorPortNumber_Type(Integer32):
    """Custom type cctvSwitchAssignmentMonitorPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CctvSwitchAssignmentMonitorPortNumber_Type.__name__ = "Integer32"
_CctvSwitchAssignmentMonitorPortNumber_Object = MibTableColumn
cctvSwitchAssignmentMonitorPortNumber = _CctvSwitchAssignmentMonitorPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1, 1),
    _CctvSwitchAssignmentMonitorPortNumber_Type()
)
cctvSwitchAssignmentMonitorPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentMonitorPortNumber.setStatus("mandatory")


class _CctvSwitchAssignmentAssignments_Type(Integer32):
    """Custom type cctvSwitchAssignmentAssignments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CctvSwitchAssignmentAssignments_Type.__name__ = "Integer32"
_CctvSwitchAssignmentAssignments_Object = MibTableColumn
cctvSwitchAssignmentAssignments = _CctvSwitchAssignmentAssignments_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1, 2),
    _CctvSwitchAssignmentAssignments_Type()
)
cctvSwitchAssignmentAssignments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentAssignments.setStatus("mandatory")


class _CctvSwitchAssignmentLabelNumber_Type(Integer32):
    """Custom type cctvSwitchAssignmentLabelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CctvSwitchAssignmentLabelNumber_Type.__name__ = "Integer32"
_CctvSwitchAssignmentLabelNumber_Object = MibTableColumn
cctvSwitchAssignmentLabelNumber = _CctvSwitchAssignmentLabelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1, 3),
    _CctvSwitchAssignmentLabelNumber_Type()
)
cctvSwitchAssignmentLabelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentLabelNumber.setStatus("mandatory")


class _CctvSwitchAssignmentTimeMode_Type(Integer32):
    """Custom type cctvSwitchAssignmentTimeMode based on Integer32"""
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
        *(("timeNotDisplayed", 1),
          ("timeDisplayed", 2),
          ("dateDisplayed", 3),
          ("bothTimeDateDisplayed", 4))
    )


_CctvSwitchAssignmentTimeMode_Type.__name__ = "Integer32"
_CctvSwitchAssignmentTimeMode_Object = MibTableColumn
cctvSwitchAssignmentTimeMode = _CctvSwitchAssignmentTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1, 4),
    _CctvSwitchAssignmentTimeMode_Type()
)
cctvSwitchAssignmentTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentTimeMode.setStatus("mandatory")


class _CctvSwitchAssignmentSequence_Type(OctetString):
    """Custom type cctvSwitchAssignmentSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_CctvSwitchAssignmentSequence_Type.__name__ = "OctetString"
_CctvSwitchAssignmentSequence_Object = MibTableColumn
cctvSwitchAssignmentSequence = _CctvSwitchAssignmentSequence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1, 5),
    _CctvSwitchAssignmentSequence_Type()
)
cctvSwitchAssignmentSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentSequence.setStatus("mandatory")


class _CctvSwitchAssignmentSequenceMode_Type(Integer32):
    """Custom type cctvSwitchAssignmentSequenceMode based on Integer32"""
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
        *(("displaySequence", 1),
          ("holdSequence", 2),
          ("nextCamera", 3),
          ("previousCamera", 4),
          ("nullSequence", 5))
    )


_CctvSwitchAssignmentSequenceMode_Type.__name__ = "Integer32"
_CctvSwitchAssignmentSequenceMode_Object = MibTableColumn
cctvSwitchAssignmentSequenceMode = _CctvSwitchAssignmentSequenceMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 3, 1, 6),
    _CctvSwitchAssignmentSequenceMode_Type()
)
cctvSwitchAssignmentSequenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentSequenceMode.setStatus("mandatory")
_CctvSwitchAssignmentStatusTable_Object = MibTable
cctvSwitchAssignmentStatusTable = _CctvSwitchAssignmentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 4)
)
if mibBuilder.loadTexts:
    cctvSwitchAssignmentStatusTable.setStatus("mandatory")
_CctvSwitchAssignmentStatusTableEntry_Object = MibTableRow
cctvSwitchAssignmentStatusTableEntry = _CctvSwitchAssignmentStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 4, 1)
)
cctvSwitchAssignmentStatusTableEntry.setIndexNames(
    (0, "CCTVSwitch-MIB1", "cctvSwitchAssignmentMonitorPortNumber"),
)
if mibBuilder.loadTexts:
    cctvSwitchAssignmentStatusTableEntry.setStatus("mandatory")


class _CctvSwitchAssignmentStatus_Type(Integer32):
    """Custom type cctvSwitchAssignmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("assignmentAccepted", 1),
          ("assignmentRejected", 2),
          ("noAssignment", 255))
    )


_CctvSwitchAssignmentStatus_Type.__name__ = "Integer32"
_CctvSwitchAssignmentStatus_Object = MibTableColumn
cctvSwitchAssignmentStatus = _CctvSwitchAssignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 4, 1, 1),
    _CctvSwitchAssignmentStatus_Type()
)
cctvSwitchAssignmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentStatus.setStatus("mandatory")


class _CctvSwitchAssignmentStatusLabelNumber_Type(Integer32):
    """Custom type cctvSwitchAssignmentStatusLabelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CctvSwitchAssignmentStatusLabelNumber_Type.__name__ = "Integer32"
_CctvSwitchAssignmentStatusLabelNumber_Object = MibTableColumn
cctvSwitchAssignmentStatusLabelNumber = _CctvSwitchAssignmentStatusLabelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 4, 1, 2),
    _CctvSwitchAssignmentStatusLabelNumber_Type()
)
cctvSwitchAssignmentStatusLabelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentStatusLabelNumber.setStatus("mandatory")


class _CctvSwitchAssignmentTimeFormat_Type(Integer32):
    """Custom type cctvSwitchAssignmentTimeFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("timeType1", 1),
          ("timeType2", 2),
          ("noTime", 255))
    )


_CctvSwitchAssignmentTimeFormat_Type.__name__ = "Integer32"
_CctvSwitchAssignmentTimeFormat_Object = MibScalar
cctvSwitchAssignmentTimeFormat = _CctvSwitchAssignmentTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 5),
    _CctvSwitchAssignmentTimeFormat_Type()
)
cctvSwitchAssignmentTimeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentTimeFormat.setStatus("mandatory")


class _CctvSwitchAssignmentDateFormat_Type(Integer32):
    """Custom type cctvSwitchAssignmentDateFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dateType1", 1),
          ("dateType2", 2),
          ("dateType3", 3),
          ("dateType4", 4),
          ("dateType5", 5),
          ("dateType6", 6),
          ("noTime", 255))
    )


_CctvSwitchAssignmentDateFormat_Type.__name__ = "Integer32"
_CctvSwitchAssignmentDateFormat_Object = MibScalar
cctvSwitchAssignmentDateFormat = _CctvSwitchAssignmentDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 8, 4, 6),
    _CctvSwitchAssignmentDateFormat_Type()
)
cctvSwitchAssignmentDateFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctvSwitchAssignmentDateFormat.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CCTVSwitch-MIB1",
    **{"cctvSwitch": cctvSwitch,
       "cctvSwitchInput": cctvSwitchInput,
       "inputStatus": inputStatus,
       "inputLatchStatus": inputLatchStatus,
       "inputLatchClear": inputLatchClear,
       "inputTable": inputTable,
       "inputTableEntry": inputTableEntry,
       "inputNumber": inputNumber,
       "inputMonitorPortNumber": inputMonitorPortNumber,
       "inputCameraPortNumber": inputCameraPortNumber,
       "inputLabelNumber": inputLabelNumber,
       "cctvSwitchOutput": cctvSwitchOutput,
       "outputStatus": outputStatus,
       "outputControl": outputControl,
       "outputTable": outputTable,
       "outputTableEntry": outputTableEntry,
       "outputNumber": outputNumber,
       "outputMonitorPortNumber": outputMonitorPortNumber,
       "outputCameraPortNumber": outputCameraPortNumber,
       "outputLabelNumber": outputLabelNumber,
       "cctvSwitchLabel": cctvSwitchLabel,
       "labelMaximum": labelMaximum,
       "labelSwitchTable": labelSwitchTable,
       "labelSwitchEntry": labelSwitchEntry,
       "labelNumber": labelNumber,
       "labelText": labelText,
       "labelFontType": labelFontType,
       "labelHeight": labelHeight,
       "labelColor": labelColor,
       "labelStartRow": labelStartRow,
       "labelStartColumn": labelStartColumn,
       "labelActive": labelActive,
       "cctvSwitchAssignment": cctvSwitchAssignment,
       "cctvSwitchAssignmentMaximumCameraPorts": cctvSwitchAssignmentMaximumCameraPorts,
       "cctvSwitchAssignmentMaximumMonitorPorts": cctvSwitchAssignmentMaximumMonitorPorts,
       "cctvSwitchAssignmentTable": cctvSwitchAssignmentTable,
       "cctvSwitchAssignmentTableEntry": cctvSwitchAssignmentTableEntry,
       "cctvSwitchAssignmentMonitorPortNumber": cctvSwitchAssignmentMonitorPortNumber,
       "cctvSwitchAssignmentAssignments": cctvSwitchAssignmentAssignments,
       "cctvSwitchAssignmentLabelNumber": cctvSwitchAssignmentLabelNumber,
       "cctvSwitchAssignmentTimeMode": cctvSwitchAssignmentTimeMode,
       "cctvSwitchAssignmentSequence": cctvSwitchAssignmentSequence,
       "cctvSwitchAssignmentSequenceMode": cctvSwitchAssignmentSequenceMode,
       "cctvSwitchAssignmentStatusTable": cctvSwitchAssignmentStatusTable,
       "cctvSwitchAssignmentStatusTableEntry": cctvSwitchAssignmentStatusTableEntry,
       "cctvSwitchAssignmentStatus": cctvSwitchAssignmentStatus,
       "cctvSwitchAssignmentStatusLabelNumber": cctvSwitchAssignmentStatusLabelNumber,
       "cctvSwitchAssignmentTimeFormat": cctvSwitchAssignmentTimeFormat,
       "cctvSwitchAssignmentDateFormat": cctvSwitchAssignmentDateFormat}
)
