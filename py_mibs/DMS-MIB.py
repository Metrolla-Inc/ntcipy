# SNMP MIB module (DMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1203DMS.mib
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

(nemaExperimental,) = mibBuilder.importSymbols(
    "NEMA_SMI",
    "nemaExperimental")

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

(DisplayString,
 OwnerString,
 devices) = mibBuilder.importSymbols(
    "TMIB-II",
    "DisplayString",
    "OwnerString",
    "devices")


# MODULE-IDENTITY


# Types definitions



class MessageIDCode(OctetString):
    """Custom type MessageIDCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixedLength = 5





class MessageActivationCode(OctetString):
    """Custom type MessageActivationCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixedLength = 12




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Exp_global_ObjectIdentity = ObjectIdentity
exp_global = _Exp_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1)
)
_AuxiliaryIO_ObjectIdentity = ObjectIdentity
auxiliaryIO = _AuxiliaryIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1)
)


class _MaxAuxIODigital_Type(Integer32):
    """Custom type maxAuxIODigital based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxAuxIODigital_Type.__name__ = "Integer32"
_MaxAuxIODigital_Object = MibScalar
maxAuxIODigital = _MaxAuxIODigital_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 1),
    _MaxAuxIODigital_Type()
)
maxAuxIODigital.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAuxIODigital.setStatus("mandatory")


class _MaxAuxIOAnalog_Type(Integer32):
    """Custom type maxAuxIOAnalog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxAuxIOAnalog_Type.__name__ = "Integer32"
_MaxAuxIOAnalog_Object = MibScalar
maxAuxIOAnalog = _MaxAuxIOAnalog_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 2),
    _MaxAuxIOAnalog_Type()
)
maxAuxIOAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAuxIOAnalog.setStatus("mandatory")
_AuxIOTable_Object = MibTable
auxIOTable = _AuxIOTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    auxIOTable.setStatus("mandatory")
_AuxIOEntry_Object = MibTableRow
auxIOEntry = _AuxIOEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1)
)
auxIOEntry.setIndexNames(
    (0, "DMS-MIB", "auxIOPortType"),
    (0, "DMS-MIB", "auxIOPortNumber"),
)
if mibBuilder.loadTexts:
    auxIOEntry.setStatus("mandatory")


class _AuxIOPortType_Type(Integer32):
    """Custom type auxIOPortType based on Integer32"""
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
          ("analog", 2),
          ("digital", 3))
    )


_AuxIOPortType_Type.__name__ = "Integer32"
_AuxIOPortType_Object = MibTableColumn
auxIOPortType = _AuxIOPortType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1, 1),
    _AuxIOPortType_Type()
)
auxIOPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxIOPortType.setStatus("mandatory")


class _AuxIOPortNumber_Type(Integer32):
    """Custom type auxIOPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AuxIOPortNumber_Type.__name__ = "Integer32"
_AuxIOPortNumber_Object = MibTableColumn
auxIOPortNumber = _AuxIOPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1, 2),
    _AuxIOPortNumber_Type()
)
auxIOPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxIOPortNumber.setStatus("mandatory")


class _AuxIODescription_Type(DisplayString):
    """Custom type auxIODescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AuxIODescription_Type.__name__ = "DisplayString"
_AuxIODescription_Object = MibTableColumn
auxIODescription = _AuxIODescription_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1, 3),
    _AuxIODescription_Type()
)
auxIODescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxIODescription.setStatus("mandatory")


class _AuxIOResolution_Type(Integer32):
    """Custom type auxIOResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AuxIOResolution_Type.__name__ = "Integer32"
_AuxIOResolution_Object = MibTableColumn
auxIOResolution = _AuxIOResolution_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1, 4),
    _AuxIOResolution_Type()
)
auxIOResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxIOResolution.setStatus("mandatory")


class _AuxIOValue_Type(Integer32):
    """Custom type auxIOValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AuxIOValue_Type.__name__ = "Integer32"
_AuxIOValue_Object = MibTableColumn
auxIOValue = _AuxIOValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1, 5),
    _AuxIOValue_Type()
)
auxIOValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxIOValue.setStatus("mandatory")


class _AuxIOPortDirection_Type(Integer32):
    """Custom type auxIOPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("output", 1),
          ("input", 2),
          ("bidirectional", 3))
    )


_AuxIOPortDirection_Type.__name__ = "Integer32"
_AuxIOPortDirection_Object = MibTableColumn
auxIOPortDirection = _AuxIOPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 1206, 2, 1, 1, 3, 1, 6),
    _AuxIOPortDirection_Type()
)
auxIOPortDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxIOPortDirection.setStatus("mandatory")
_Dms_ObjectIdentity = ObjectIdentity
dms = _Dms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3)
)
_DmsSignCfg_ObjectIdentity = ObjectIdentity
dmsSignCfg = _DmsSignCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1)
)


class _DmsSignAccess_Type(Integer32):
    """Custom type dmsSignAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsSignAccess_Type.__name__ = "Integer32"
_DmsSignAccess_Object = MibScalar
dmsSignAccess = _DmsSignAccess_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 1),
    _DmsSignAccess_Type()
)
dmsSignAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsSignAccess.setStatus("mandatory")


class _DmsSignType_Type(Integer32):
    """Custom type dmsSignType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              129,
              130,
              131,
              132,
              133,
              134)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("bos", 2),
          ("cms", 3),
          ("vmsChar", 4),
          ("vmsLine", 5),
          ("vmsFull", 6),
          ("portableOther", 129),
          ("portableBOS", 130),
          ("portableCMS", 131),
          ("portableVMSChar", 132),
          ("portableVMSLine", 133),
          ("portableVMSFull", 134))
    )


_DmsSignType_Type.__name__ = "Integer32"
_DmsSignType_Object = MibScalar
dmsSignType = _DmsSignType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 2),
    _DmsSignType_Type()
)
dmsSignType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsSignType.setStatus("mandatory")


class _DmsSignHeight_Type(Integer32):
    """Custom type dmsSignHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsSignHeight_Type.__name__ = "Integer32"
_DmsSignHeight_Object = MibScalar
dmsSignHeight = _DmsSignHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 3),
    _DmsSignHeight_Type()
)
dmsSignHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsSignHeight.setStatus("mandatory")


class _DmsSignWidth_Type(Integer32):
    """Custom type dmsSignWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsSignWidth_Type.__name__ = "Integer32"
_DmsSignWidth_Object = MibScalar
dmsSignWidth = _DmsSignWidth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 4),
    _DmsSignWidth_Type()
)
dmsSignWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsSignWidth.setStatus("mandatory")


class _DmsHorizontalBorder_Type(Integer32):
    """Custom type dmsHorizontalBorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsHorizontalBorder_Type.__name__ = "Integer32"
_DmsHorizontalBorder_Object = MibScalar
dmsHorizontalBorder = _DmsHorizontalBorder_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 5),
    _DmsHorizontalBorder_Type()
)
dmsHorizontalBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsHorizontalBorder.setStatus("mandatory")


class _DmsVerticalBorder_Type(Integer32):
    """Custom type dmsVerticalBorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsVerticalBorder_Type.__name__ = "Integer32"
_DmsVerticalBorder_Object = MibScalar
dmsVerticalBorder = _DmsVerticalBorder_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 6),
    _DmsVerticalBorder_Type()
)
dmsVerticalBorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsVerticalBorder.setStatus("mandatory")


class _DmsLegend_Type(Integer32):
    """Custom type dmsLegend based on Integer32"""
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
          ("noLegend", 2),
          ("legendExists", 3))
    )


_DmsLegend_Type.__name__ = "Integer32"
_DmsLegend_Object = MibScalar
dmsLegend = _DmsLegend_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 7),
    _DmsLegend_Type()
)
dmsLegend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsLegend.setStatus("mandatory")


class _DmsBeaconType_Type(Integer32):
    """Custom type dmsBeaconType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("oneBeacon", 3),
          ("twoBeaconSyncFlash", 4),
          ("twoBeaconsOppFlash", 5),
          ("fourBeaconSyncFlash", 6),
          ("fourBeaconAltRowFlash", 7),
          ("fourBeaconAltColumnFlash", 8),
          ("fourBeaconAltDiagonalFlash", 9),
          ("fourBeaconNoSyncFlash", 10),
          ("oneBeaconStrobe", 11),
          ("twoBeaconStrobe", 12),
          ("fourBeaconStrobe", 13))
    )


_DmsBeaconType_Type.__name__ = "Integer32"
_DmsBeaconType_Object = MibScalar
dmsBeaconType = _DmsBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 8),
    _DmsBeaconType_Type()
)
dmsBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsBeaconType.setStatus("mandatory")


class _DmsSignTechnology_Type(Integer32):
    """Custom type dmsSignTechnology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsSignTechnology_Type.__name__ = "Integer32"
_DmsSignTechnology_Object = MibScalar
dmsSignTechnology = _DmsSignTechnology_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 1, 9),
    _DmsSignTechnology_Type()
)
dmsSignTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsSignTechnology.setStatus("mandatory")
_VmsCfg_ObjectIdentity = ObjectIdentity
vmsCfg = _VmsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2)
)


class _VmsCharacterHeightPixels_Type(Integer32):
    """Custom type vmsCharacterHeightPixels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmsCharacterHeightPixels_Type.__name__ = "Integer32"
_VmsCharacterHeightPixels_Object = MibScalar
vmsCharacterHeightPixels = _VmsCharacterHeightPixels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2, 1),
    _VmsCharacterHeightPixels_Type()
)
vmsCharacterHeightPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsCharacterHeightPixels.setStatus("mandatory")


class _VmsCharacterWidthPixels_Type(Integer32):
    """Custom type vmsCharacterWidthPixels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmsCharacterWidthPixels_Type.__name__ = "Integer32"
_VmsCharacterWidthPixels_Object = MibScalar
vmsCharacterWidthPixels = _VmsCharacterWidthPixels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2, 2),
    _VmsCharacterWidthPixels_Type()
)
vmsCharacterWidthPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsCharacterWidthPixels.setStatus("mandatory")


class _VmsSignHeightPixels_Type(Integer32):
    """Custom type vmsSignHeightPixels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmsSignHeightPixels_Type.__name__ = "Integer32"
_VmsSignHeightPixels_Object = MibScalar
vmsSignHeightPixels = _VmsSignHeightPixels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2, 3),
    _VmsSignHeightPixels_Type()
)
vmsSignHeightPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSignHeightPixels.setStatus("mandatory")


class _VmsSignWidthPixels_Type(Integer32):
    """Custom type vmsSignWidthPixels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmsSignWidthPixels_Type.__name__ = "Integer32"
_VmsSignWidthPixels_Object = MibScalar
vmsSignWidthPixels = _VmsSignWidthPixels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2, 4),
    _VmsSignWidthPixels_Type()
)
vmsSignWidthPixels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsSignWidthPixels.setStatus("mandatory")


class _VmsHorizontalPitch_Type(Integer32):
    """Custom type vmsHorizontalPitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmsHorizontalPitch_Type.__name__ = "Integer32"
_VmsHorizontalPitch_Object = MibScalar
vmsHorizontalPitch = _VmsHorizontalPitch_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2, 5),
    _VmsHorizontalPitch_Type()
)
vmsHorizontalPitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsHorizontalPitch.setStatus("mandatory")


class _VmsVerticalPitch_Type(Integer32):
    """Custom type vmsVerticalPitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmsVerticalPitch_Type.__name__ = "Integer32"
_VmsVerticalPitch_Object = MibScalar
vmsVerticalPitch = _VmsVerticalPitch_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 2, 6),
    _VmsVerticalPitch_Type()
)
vmsVerticalPitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmsVerticalPitch.setStatus("mandatory")
_FontDefinition_ObjectIdentity = ObjectIdentity
fontDefinition = _FontDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3)
)


class _NumFonts_Type(Integer32):
    """Custom type numFonts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumFonts_Type.__name__ = "Integer32"
_NumFonts_Object = MibScalar
numFonts = _NumFonts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 1),
    _NumFonts_Type()
)
numFonts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numFonts.setStatus("mandatory")
_FontTable_Object = MibTable
fontTable = _FontTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fontTable.setStatus("mandatory")
_FontEntry_Object = MibTableRow
fontEntry = _FontEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1)
)
fontEntry.setIndexNames(
    (0, "DMS-MIB", "fontIndex"),
)
if mibBuilder.loadTexts:
    fontEntry.setStatus("mandatory")


class _FontIndex_Type(Integer32):
    """Custom type fontIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FontIndex_Type.__name__ = "Integer32"
_FontIndex_Object = MibTableColumn
fontIndex = _FontIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 1),
    _FontIndex_Type()
)
fontIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fontIndex.setStatus("mandatory")


class _FontNumber_Type(Integer32):
    """Custom type fontNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FontNumber_Type.__name__ = "Integer32"
_FontNumber_Object = MibTableColumn
fontNumber = _FontNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 2),
    _FontNumber_Type()
)
fontNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fontNumber.setStatus("mandatory")


class _FontName_Type(DisplayString):
    """Custom type fontName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FontName_Type.__name__ = "DisplayString"
_FontName_Object = MibTableColumn
fontName = _FontName_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 3),
    _FontName_Type()
)
fontName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fontName.setStatus("mandatory")


class _FontHeight_Type(Integer32):
    """Custom type fontHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FontHeight_Type.__name__ = "Integer32"
_FontHeight_Object = MibTableColumn
fontHeight = _FontHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 4),
    _FontHeight_Type()
)
fontHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fontHeight.setStatus("mandatory")


class _FontCharSpacing_Type(Integer32):
    """Custom type fontCharSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FontCharSpacing_Type.__name__ = "Integer32"
_FontCharSpacing_Object = MibTableColumn
fontCharSpacing = _FontCharSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 5),
    _FontCharSpacing_Type()
)
fontCharSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fontCharSpacing.setStatus("mandatory")


class _FontLineSpacing_Type(Integer32):
    """Custom type fontLineSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FontLineSpacing_Type.__name__ = "Integer32"
_FontLineSpacing_Object = MibTableColumn
fontLineSpacing = _FontLineSpacing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 6),
    _FontLineSpacing_Type()
)
fontLineSpacing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fontLineSpacing.setStatus("mandatory")


class _FontVersionID_Type(Integer32):
    """Custom type fontVersionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FontVersionID_Type.__name__ = "Integer32"
_FontVersionID_Object = MibTableColumn
fontVersionID = _FontVersionID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 2, 1, 7),
    _FontVersionID_Type()
)
fontVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fontVersionID.setStatus("mandatory")


class _MaxFontCharacters_Type(Integer32):
    """Custom type maxFontCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MaxFontCharacters_Type.__name__ = "Integer32"
_MaxFontCharacters_Object = MibScalar
maxFontCharacters = _MaxFontCharacters_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 3),
    _MaxFontCharacters_Type()
)
maxFontCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFontCharacters.setStatus("mandatory")
_CharacterTable_Object = MibTable
characterTable = _CharacterTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    characterTable.setStatus("mandatory")
_CharacterEntry_Object = MibTableRow
characterEntry = _CharacterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 4, 1)
)
characterEntry.setIndexNames(
    (0, "DMS-MIB", "fontIndex"),
    (0, "DMS-MIB", "characterNumber"),
)
if mibBuilder.loadTexts:
    characterEntry.setStatus("mandatory")


class _CharacterNumber_Type(Integer32):
    """Custom type characterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CharacterNumber_Type.__name__ = "Integer32"
_CharacterNumber_Object = MibTableColumn
characterNumber = _CharacterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 4, 1, 1),
    _CharacterNumber_Type()
)
characterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    characterNumber.setStatus("mandatory")


class _CharacterWidth_Type(Integer32):
    """Custom type characterWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CharacterWidth_Type.__name__ = "Integer32"
_CharacterWidth_Object = MibTableColumn
characterWidth = _CharacterWidth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 4, 1, 2),
    _CharacterWidth_Type()
)
characterWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    characterWidth.setStatus("mandatory")
_CharacterBitmap_Type = OctetString
_CharacterBitmap_Object = MibTableColumn
characterBitmap = _CharacterBitmap_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 3, 4, 1, 3),
    _CharacterBitmap_Type()
)
characterBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    characterBitmap.setStatus("mandatory")
_MultiCfg_ObjectIdentity = ObjectIdentity
multiCfg = _MultiCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4)
)


class _DefaultBackgroundColor_Type(Integer32):
    """Custom type defaultBackgroundColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultBackgroundColor_Type.__name__ = "Integer32"
_DefaultBackgroundColor_Object = MibScalar
defaultBackgroundColor = _DefaultBackgroundColor_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 1),
    _DefaultBackgroundColor_Type()
)
defaultBackgroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultBackgroundColor.setStatus("mandatory")


class _DefaultForegroundColor_Type(Integer32):
    """Custom type defaultForegroundColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultForegroundColor_Type.__name__ = "Integer32"
_DefaultForegroundColor_Object = MibScalar
defaultForegroundColor = _DefaultForegroundColor_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 2),
    _DefaultForegroundColor_Type()
)
defaultForegroundColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForegroundColor.setStatus("mandatory")


class _DefaultFlashOn_Type(Integer32):
    """Custom type defaultFlashOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultFlashOn_Type.__name__ = "Integer32"
_DefaultFlashOn_Object = MibScalar
defaultFlashOn = _DefaultFlashOn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 3),
    _DefaultFlashOn_Type()
)
defaultFlashOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultFlashOn.setStatus("optional")


class _DefaultFlashOff_Type(Integer32):
    """Custom type defaultFlashOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultFlashOff_Type.__name__ = "Integer32"
_DefaultFlashOff_Object = MibScalar
defaultFlashOff = _DefaultFlashOff_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 4),
    _DefaultFlashOff_Type()
)
defaultFlashOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultFlashOff.setStatus("optional")


class _DefaultFont_Type(Integer32):
    """Custom type defaultFont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DefaultFont_Type.__name__ = "Integer32"
_DefaultFont_Object = MibScalar
defaultFont = _DefaultFont_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 5),
    _DefaultFont_Type()
)
defaultFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultFont.setStatus("mandatory")


class _DefaultJustificationLine_Type(Integer32):
    """Custom type defaultJustificationLine based on Integer32"""
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
          ("left", 2),
          ("center", 3),
          ("right", 4),
          ("full", 5))
    )


_DefaultJustificationLine_Type.__name__ = "Integer32"
_DefaultJustificationLine_Object = MibScalar
defaultJustificationLine = _DefaultJustificationLine_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 6),
    _DefaultJustificationLine_Type()
)
defaultJustificationLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultJustificationLine.setStatus("mandatory")


class _DefaultJustificationPage_Type(Integer32):
    """Custom type defaultJustificationPage based on Integer32"""
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
          ("top", 2),
          ("middle", 3),
          ("bottom", 4))
    )


_DefaultJustificationPage_Type.__name__ = "Integer32"
_DefaultJustificationPage_Object = MibScalar
defaultJustificationPage = _DefaultJustificationPage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 7),
    _DefaultJustificationPage_Type()
)
defaultJustificationPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultJustificationPage.setStatus("mandatory")


class _DefaultPageOnTime_Type(Integer32):
    """Custom type defaultPageOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DefaultPageOnTime_Type.__name__ = "Integer32"
_DefaultPageOnTime_Object = MibScalar
defaultPageOnTime = _DefaultPageOnTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 8),
    _DefaultPageOnTime_Type()
)
defaultPageOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultPageOnTime.setStatus("mandatory")


class _DefaultPageOffTime_Type(Integer32):
    """Custom type defaultPageOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DefaultPageOffTime_Type.__name__ = "Integer32"
_DefaultPageOffTime_Object = MibScalar
defaultPageOffTime = _DefaultPageOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 9),
    _DefaultPageOffTime_Type()
)
defaultPageOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultPageOffTime.setStatus("mandatory")


class _DefaultCharacterSet_Type(Integer32):
    """Custom type defaultCharacterSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("eightBit", 2))
    )


_DefaultCharacterSet_Type.__name__ = "Integer32"
_DefaultCharacterSet_Object = MibScalar
defaultCharacterSet = _DefaultCharacterSet_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 4, 10),
    _DefaultCharacterSet_Type()
)
defaultCharacterSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultCharacterSet.setStatus("mandatory")
_DmsMessage_ObjectIdentity = ObjectIdentity
dmsMessage = _DmsMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5)
)


class _DmsNumPermanentMsg_Type(Integer32):
    """Custom type dmsNumPermanentMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsNumPermanentMsg_Type.__name__ = "Integer32"
_DmsNumPermanentMsg_Object = MibScalar
dmsNumPermanentMsg = _DmsNumPermanentMsg_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 1),
    _DmsNumPermanentMsg_Type()
)
dmsNumPermanentMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsNumPermanentMsg.setStatus("mandatory")


class _DmsNumChangeableMsg_Type(Integer32):
    """Custom type dmsNumChangeableMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsNumChangeableMsg_Type.__name__ = "Integer32"
_DmsNumChangeableMsg_Object = MibScalar
dmsNumChangeableMsg = _DmsNumChangeableMsg_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 2),
    _DmsNumChangeableMsg_Type()
)
dmsNumChangeableMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsNumChangeableMsg.setStatus("mandatory")


class _DmsMaxChangeableMsg_Type(Integer32):
    """Custom type dmsMaxChangeableMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsMaxChangeableMsg_Type.__name__ = "Integer32"
_DmsMaxChangeableMsg_Object = MibScalar
dmsMaxChangeableMsg = _DmsMaxChangeableMsg_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 3),
    _DmsMaxChangeableMsg_Type()
)
dmsMaxChangeableMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMaxChangeableMsg.setStatus("mandatory")


class _DmsFreeChangeableMemory_Type(Integer32):
    """Custom type dmsFreeChangeableMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DmsFreeChangeableMemory_Type.__name__ = "Integer32"
_DmsFreeChangeableMemory_Object = MibScalar
dmsFreeChangeableMemory = _DmsFreeChangeableMemory_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 4),
    _DmsFreeChangeableMemory_Type()
)
dmsFreeChangeableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsFreeChangeableMemory.setStatus("mandatory")


class _DmsNumVolatileMsg_Type(Integer32):
    """Custom type dmsNumVolatileMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsNumVolatileMsg_Type.__name__ = "Integer32"
_DmsNumVolatileMsg_Object = MibScalar
dmsNumVolatileMsg = _DmsNumVolatileMsg_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 5),
    _DmsNumVolatileMsg_Type()
)
dmsNumVolatileMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsNumVolatileMsg.setStatus("mandatory")


class _DmsMaxVolatileMsg_Type(Integer32):
    """Custom type dmsMaxVolatileMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsMaxVolatileMsg_Type.__name__ = "Integer32"
_DmsMaxVolatileMsg_Object = MibScalar
dmsMaxVolatileMsg = _DmsMaxVolatileMsg_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 6),
    _DmsMaxVolatileMsg_Type()
)
dmsMaxVolatileMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMaxVolatileMsg.setStatus("mandatory")


class _DmsFreeVolatileMemory_Type(Integer32):
    """Custom type dmsFreeVolatileMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DmsFreeVolatileMemory_Type.__name__ = "Integer32"
_DmsFreeVolatileMemory_Object = MibScalar
dmsFreeVolatileMemory = _DmsFreeVolatileMemory_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 7),
    _DmsFreeVolatileMemory_Type()
)
dmsFreeVolatileMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsFreeVolatileMemory.setStatus("mandatory")
_DmsMessageTable_Object = MibTable
dmsMessageTable = _DmsMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8)
)
if mibBuilder.loadTexts:
    dmsMessageTable.setStatus("mandatory")
_DmsMessageEntry_Object = MibTableRow
dmsMessageEntry = _DmsMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1)
)
dmsMessageEntry.setIndexNames(
    (0, "DMS-MIB", "dmsMessageMemoryType"),
    (0, "DMS-MIB", "dmsMessageNumber"),
)
if mibBuilder.loadTexts:
    dmsMessageEntry.setStatus("mandatory")


class _DmsMessageMemoryType_Type(Integer32):
    """Custom type dmsMessageMemoryType based on Integer32"""
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
          ("permanent", 2),
          ("changeable", 3),
          ("volatile", 4),
          ("currentBuffer", 5),
          ("schedule", 6))
    )


_DmsMessageMemoryType_Type.__name__ = "Integer32"
_DmsMessageMemoryType_Object = MibTableColumn
dmsMessageMemoryType = _DmsMessageMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 1),
    _DmsMessageMemoryType_Type()
)
dmsMessageMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMessageMemoryType.setStatus("mandatory")


class _DmsMessageNumber_Type(Integer32):
    """Custom type dmsMessageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DmsMessageNumber_Type.__name__ = "Integer32"
_DmsMessageNumber_Object = MibTableColumn
dmsMessageNumber = _DmsMessageNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 2),
    _DmsMessageNumber_Type()
)
dmsMessageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMessageNumber.setStatus("mandatory")
_DmsMessageMultiString_Type = OctetString
_DmsMessageMultiString_Object = MibTableColumn
dmsMessageMultiString = _DmsMessageMultiString_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 3),
    _DmsMessageMultiString_Type()
)
dmsMessageMultiString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessageMultiString.setStatus("mandatory")
_DmsMessageOwner_Type = OwnerString
_DmsMessageOwner_Object = MibTableColumn
dmsMessageOwner = _DmsMessageOwner_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 4),
    _DmsMessageOwner_Type()
)
dmsMessageOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessageOwner.setStatus("mandatory")


class _DmsMessageCRC_Type(Integer32):
    """Custom type dmsMessageCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsMessageCRC_Type.__name__ = "Integer32"
_DmsMessageCRC_Object = MibTableColumn
dmsMessageCRC = _DmsMessageCRC_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 5),
    _DmsMessageCRC_Type()
)
dmsMessageCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMessageCRC.setStatus("mandatory")


class _DmsMessageBeacon_Type(Integer32):
    """Custom type dmsMessageBeacon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DmsMessageBeacon_Type.__name__ = "Integer32"
_DmsMessageBeacon_Object = MibTableColumn
dmsMessageBeacon = _DmsMessageBeacon_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 6),
    _DmsMessageBeacon_Type()
)
dmsMessageBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessageBeacon.setStatus("optional")


class _DmsMessagePixelService_Type(Integer32):
    """Custom type dmsMessagePixelService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DmsMessagePixelService_Type.__name__ = "Integer32"
_DmsMessagePixelService_Object = MibTableColumn
dmsMessagePixelService = _DmsMessagePixelService_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 7),
    _DmsMessagePixelService_Type()
)
dmsMessagePixelService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessagePixelService.setStatus("optional")


class _DmsMessageRunTimePriority_Type(Integer32):
    """Custom type dmsMessageRunTimePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DmsMessageRunTimePriority_Type.__name__ = "Integer32"
_DmsMessageRunTimePriority_Object = MibTableColumn
dmsMessageRunTimePriority = _DmsMessageRunTimePriority_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 8),
    _DmsMessageRunTimePriority_Type()
)
dmsMessageRunTimePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessageRunTimePriority.setStatus("mandatory")


class _DmsMessageStatus_Type(Integer32):
    """Custom type dmsMessageStatus based on Integer32"""
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
          ("modifying", 2),
          ("validating", 3),
          ("valid", 4),
          ("error", 5),
          ("modifyReq", 6),
          ("validateReq", 7),
          ("notUsedReq", 8))
    )


_DmsMessageStatus_Type.__name__ = "Integer32"
_DmsMessageStatus_Object = MibTableColumn
dmsMessageStatus = _DmsMessageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 8, 1, 9),
    _DmsMessageStatus_Type()
)
dmsMessageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessageStatus.setStatus("mandatory")


class _DmsValidateMessageError_Type(Integer32):
    """Custom type dmsValidateMessageError based on Integer32"""
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
          ("none", 2),
          ("beacons", 3),
          ("pixelService", 4),
          ("syntaxMULTI", 5))
    )


_DmsValidateMessageError_Type.__name__ = "Integer32"
_DmsValidateMessageError_Object = MibScalar
dmsValidateMessageError = _DmsValidateMessageError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 5, 9),
    _DmsValidateMessageError_Type()
)
dmsValidateMessageError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsValidateMessageError.setStatus("mandatory")
_SignControl_ObjectIdentity = ObjectIdentity
signControl = _SignControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6)
)


class _DmsControlMode_Type(Integer32):
    """Custom type dmsControlMode based on Integer32"""
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
          ("local", 2),
          ("external", 3),
          ("central", 4),
          ("centralOverride", 5),
          ("simulation", 6))
    )


_DmsControlMode_Type.__name__ = "Integer32"
_DmsControlMode_Object = MibScalar
dmsControlMode = _DmsControlMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 1),
    _DmsControlMode_Type()
)
dmsControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsControlMode.setStatus("mandatory")


class _DmsSWReset_Type(Integer32):
    """Custom type dmsSWReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DmsSWReset_Type.__name__ = "Integer32"
_DmsSWReset_Object = MibScalar
dmsSWReset = _DmsSWReset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 2),
    _DmsSWReset_Type()
)
dmsSWReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsSWReset.setStatus("optional")
_DmsActivateMessage_Type = MessageActivationCode
_DmsActivateMessage_Object = MibScalar
dmsActivateMessage = _DmsActivateMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 3),
    _DmsActivateMessage_Type()
)
dmsActivateMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsActivateMessage.setStatus("mandatory")


class _DmsMessageTimeRemaining_Type(Integer32):
    """Custom type dmsMessageTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsMessageTimeRemaining_Type.__name__ = "Integer32"
_DmsMessageTimeRemaining_Object = MibScalar
dmsMessageTimeRemaining = _DmsMessageTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 4),
    _DmsMessageTimeRemaining_Type()
)
dmsMessageTimeRemaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMessageTimeRemaining.setStatus("optional")
_DmsMsgTableSource_Type = MessageIDCode
_DmsMsgTableSource_Object = MibScalar
dmsMsgTableSource = _DmsMsgTableSource_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 5),
    _DmsMsgTableSource_Type()
)
dmsMsgTableSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMsgTableSource.setStatus("mandatory")
_DmsMsgRequesterID_Type = IpAddress
_DmsMsgRequesterID_Object = MibScalar
dmsMsgRequesterID = _DmsMsgRequesterID_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 6),
    _DmsMsgRequesterID_Type()
)
dmsMsgRequesterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMsgRequesterID.setStatus("mandatory")


class _DmsMsgSourceMode_Type(Integer32):
    """Custom type dmsMsgSourceMode based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("external", 3),
          ("otherCom1", 4),
          ("otherCom2", 5),
          ("otherCom3", 6),
          ("otherCom4", 7),
          ("central", 8),
          ("timebasedScheduler", 9),
          ("powerRecovery", 10),
          ("reset", 11),
          ("commLoss", 12),
          ("powerLoss", 13),
          ("endDuration", 14))
    )


_DmsMsgSourceMode_Type.__name__ = "Integer32"
_DmsMsgSourceMode_Object = MibScalar
dmsMsgSourceMode = _DmsMsgSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 7),
    _DmsMsgSourceMode_Type()
)
dmsMsgSourceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMsgSourceMode.setStatus("mandatory")
_DmsShortPowerRecoveryMessage_Type = MessageIDCode
_DmsShortPowerRecoveryMessage_Object = MibScalar
dmsShortPowerRecoveryMessage = _DmsShortPowerRecoveryMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 8),
    _DmsShortPowerRecoveryMessage_Type()
)
dmsShortPowerRecoveryMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsShortPowerRecoveryMessage.setStatus("optional")
_DmsLongPowerRecoveryMessage_Type = MessageIDCode
_DmsLongPowerRecoveryMessage_Object = MibScalar
dmsLongPowerRecoveryMessage = _DmsLongPowerRecoveryMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 9),
    _DmsLongPowerRecoveryMessage_Type()
)
dmsLongPowerRecoveryMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsLongPowerRecoveryMessage.setStatus("optional")


class _DmsShortPowerLossTime_Type(Integer32):
    """Custom type dmsShortPowerLossTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsShortPowerLossTime_Type.__name__ = "Integer32"
_DmsShortPowerLossTime_Object = MibScalar
dmsShortPowerLossTime = _DmsShortPowerLossTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 10),
    _DmsShortPowerLossTime_Type()
)
dmsShortPowerLossTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsShortPowerLossTime.setStatus("optional")
_DmsResetMessage_Type = MessageIDCode
_DmsResetMessage_Object = MibScalar
dmsResetMessage = _DmsResetMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 11),
    _DmsResetMessage_Type()
)
dmsResetMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsResetMessage.setStatus("optional")
_DmsCommunicationsLossMessage_Type = MessageIDCode
_DmsCommunicationsLossMessage_Object = MibScalar
dmsCommunicationsLossMessage = _DmsCommunicationsLossMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 12),
    _DmsCommunicationsLossMessage_Type()
)
dmsCommunicationsLossMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsCommunicationsLossMessage.setStatus("optional")


class _DmsTimeCommLoss_Type(Integer32):
    """Custom type dmsTimeCommLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsTimeCommLoss_Type.__name__ = "Integer32"
_DmsTimeCommLoss_Object = MibScalar
dmsTimeCommLoss = _DmsTimeCommLoss_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 13),
    _DmsTimeCommLoss_Type()
)
dmsTimeCommLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsTimeCommLoss.setStatus("optional")
_DmsPowerLossMessage_Type = MessageIDCode
_DmsPowerLossMessage_Object = MibScalar
dmsPowerLossMessage = _DmsPowerLossMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 14),
    _DmsPowerLossMessage_Type()
)
dmsPowerLossMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsPowerLossMessage.setStatus("optional")
_DmsEndDurationMessage_Type = MessageIDCode
_DmsEndDurationMessage_Object = MibScalar
dmsEndDurationMessage = _DmsEndDurationMessage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 15),
    _DmsEndDurationMessage_Type()
)
dmsEndDurationMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsEndDurationMessage.setStatus("optional")


class _DmsMemoryMgmt_Type(Integer32):
    """Custom type dmsMemoryMgmt based on Integer32"""
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
          ("normal", 2),
          ("clearChangeableMessages", 3),
          ("clearVolatileMessages", 4))
    )


_DmsMemoryMgmt_Type.__name__ = "Integer32"
_DmsMemoryMgmt_Object = MibScalar
dmsMemoryMgmt = _DmsMemoryMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 16),
    _DmsMemoryMgmt_Type()
)
dmsMemoryMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMemoryMgmt.setStatus("optional")


class _DmsActivateMsgError_Type(Integer32):
    """Custom type dmsActivateMsgError based on Integer32"""
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
        *(("other", 1),
          ("none", 2),
          ("priority", 3),
          ("underValidation", 4),
          ("memoryType", 5),
          ("messageNumber", 6),
          ("messageCRC", 7),
          ("syntaxMULTI", 8),
          ("localMode", 9))
    )


_DmsActivateMsgError_Type.__name__ = "Integer32"
_DmsActivateMsgError_Object = MibScalar
dmsActivateMsgError = _DmsActivateMsgError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 17),
    _DmsActivateMsgError_Type()
)
dmsActivateMsgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsActivateMsgError.setStatus("mandatory")


class _DmsMultiSyntaxError_Type(Integer32):
    """Custom type dmsMultiSyntaxError based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("unsupportedTag", 3),
          ("unsupportedTagValue", 4),
          ("textTooBig", 5),
          ("fontNotDefined", 6),
          ("characterNotDefined", 7),
          ("fieldDeviceNotExist", 8),
          ("fieldDeviceError", 9),
          ("flashRegionError", 10),
          ("tagConflict", 11),
          ("tooManyPages", 12))
    )


_DmsMultiSyntaxError_Type.__name__ = "Integer32"
_DmsMultiSyntaxError_Object = MibScalar
dmsMultiSyntaxError = _DmsMultiSyntaxError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 18),
    _DmsMultiSyntaxError_Type()
)
dmsMultiSyntaxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMultiSyntaxError.setStatus("mandatory")


class _DmsMultiSyntaxErrorPosition_Type(Integer32):
    """Custom type dmsMultiSyntaxErrorPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsMultiSyntaxErrorPosition_Type.__name__ = "Integer32"
_DmsMultiSyntaxErrorPosition_Object = MibScalar
dmsMultiSyntaxErrorPosition = _DmsMultiSyntaxErrorPosition_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 19),
    _DmsMultiSyntaxErrorPosition_Type()
)
dmsMultiSyntaxErrorPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsMultiSyntaxErrorPosition.setStatus("mandatory")


class _DmsMultiOtherErrorDescription_Type(DisplayString):
    """Custom type dmsMultiOtherErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DmsMultiOtherErrorDescription_Type.__name__ = "DisplayString"
_DmsMultiOtherErrorDescription_Object = MibScalar
dmsMultiOtherErrorDescription = _DmsMultiOtherErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 20),
    _DmsMultiOtherErrorDescription_Type()
)
dmsMultiOtherErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsMultiOtherErrorDescription.setStatus("optional")


class _VmsPixelServiceDuration_Type(Integer32):
    """Custom type vmsPixelServiceDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VmsPixelServiceDuration_Type.__name__ = "Integer32"
_VmsPixelServiceDuration_Object = MibScalar
vmsPixelServiceDuration = _VmsPixelServiceDuration_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 21),
    _VmsPixelServiceDuration_Type()
)
vmsPixelServiceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsPixelServiceDuration.setStatus("optional")


class _VmsPixelServiceFrequency_Type(Integer32):
    """Custom type vmsPixelServiceFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_VmsPixelServiceFrequency_Type.__name__ = "Integer32"
_VmsPixelServiceFrequency_Object = MibScalar
vmsPixelServiceFrequency = _VmsPixelServiceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 22),
    _VmsPixelServiceFrequency_Type()
)
vmsPixelServiceFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsPixelServiceFrequency.setStatus("optional")


class _VmsPixelServiceTime_Type(Integer32):
    """Custom type vmsPixelServiceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_VmsPixelServiceTime_Type.__name__ = "Integer32"
_VmsPixelServiceTime_Object = MibScalar
vmsPixelServiceTime = _VmsPixelServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 6, 23),
    _VmsPixelServiceTime_Type()
)
vmsPixelServiceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmsPixelServiceTime.setStatus("optional")
_Illum_ObjectIdentity = ObjectIdentity
illum = _Illum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7)
)


class _DmsIllumControl_Type(Integer32):
    """Custom type dmsIllumControl based on Integer32"""
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
          ("photocell", 2),
          ("timer", 3),
          ("manual", 4))
    )


_DmsIllumControl_Type.__name__ = "Integer32"
_DmsIllumControl_Object = MibScalar
dmsIllumControl = _DmsIllumControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 1),
    _DmsIllumControl_Type()
)
dmsIllumControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsIllumControl.setStatus("mandatory")


class _DmsIllumMaxPhotocellLevel_Type(Integer32):
    """Custom type dmsIllumMaxPhotocellLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsIllumMaxPhotocellLevel_Type.__name__ = "Integer32"
_DmsIllumMaxPhotocellLevel_Object = MibScalar
dmsIllumMaxPhotocellLevel = _DmsIllumMaxPhotocellLevel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 2),
    _DmsIllumMaxPhotocellLevel_Type()
)
dmsIllumMaxPhotocellLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsIllumMaxPhotocellLevel.setStatus("mandatory")


class _DmsIllumPhotocellLevelStatus_Type(Integer32):
    """Custom type dmsIllumPhotocellLevelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsIllumPhotocellLevelStatus_Type.__name__ = "Integer32"
_DmsIllumPhotocellLevelStatus_Object = MibScalar
dmsIllumPhotocellLevelStatus = _DmsIllumPhotocellLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 3),
    _DmsIllumPhotocellLevelStatus_Type()
)
dmsIllumPhotocellLevelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsIllumPhotocellLevelStatus.setStatus("mandatory")


class _DmsIllumNumBrightLevels_Type(Integer32):
    """Custom type dmsIllumNumBrightLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsIllumNumBrightLevels_Type.__name__ = "Integer32"
_DmsIllumNumBrightLevels_Object = MibScalar
dmsIllumNumBrightLevels = _DmsIllumNumBrightLevels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 4),
    _DmsIllumNumBrightLevels_Type()
)
dmsIllumNumBrightLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsIllumNumBrightLevels.setStatus("mandatory")


class _DmsIllumBrightLevelStatus_Type(Integer32):
    """Custom type dmsIllumBrightLevelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsIllumBrightLevelStatus_Type.__name__ = "Integer32"
_DmsIllumBrightLevelStatus_Object = MibScalar
dmsIllumBrightLevelStatus = _DmsIllumBrightLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 5),
    _DmsIllumBrightLevelStatus_Type()
)
dmsIllumBrightLevelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsIllumBrightLevelStatus.setStatus("mandatory")


class _DmsIllumManLevel_Type(Integer32):
    """Custom type dmsIllumManLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsIllumManLevel_Type.__name__ = "Integer32"
_DmsIllumManLevel_Object = MibScalar
dmsIllumManLevel = _DmsIllumManLevel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 6),
    _DmsIllumManLevel_Type()
)
dmsIllumManLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsIllumManLevel.setStatus("mandatory")
_DmsIllumBrightnessValues_Type = OctetString
_DmsIllumBrightnessValues_Object = MibScalar
dmsIllumBrightnessValues = _DmsIllumBrightnessValues_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 7),
    _DmsIllumBrightnessValues_Type()
)
dmsIllumBrightnessValues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsIllumBrightnessValues.setStatus("mandatory")


class _DmsIllumBrightnessValuesError_Type(Integer32):
    """Custom type dmsIllumBrightnessValuesError based on Integer32"""
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
          ("none", 2),
          ("photocellGap", 3),
          ("negativeSlope", 4),
          ("tooManyLevels", 5),
          ("invalidData", 6))
    )


_DmsIllumBrightnessValuesError_Type.__name__ = "Integer32"
_DmsIllumBrightnessValuesError_Object = MibScalar
dmsIllumBrightnessValuesError = _DmsIllumBrightnessValuesError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 8),
    _DmsIllumBrightnessValuesError_Type()
)
dmsIllumBrightnessValuesError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsIllumBrightnessValuesError.setStatus("mandatory")


class _DmsIllumLightOutputStatus_Type(Integer32):
    """Custom type dmsIllumLightOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmsIllumLightOutputStatus_Type.__name__ = "Integer32"
_DmsIllumLightOutputStatus_Object = MibScalar
dmsIllumLightOutputStatus = _DmsIllumLightOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 7, 9),
    _DmsIllumLightOutputStatus_Type()
)
dmsIllumLightOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsIllumLightOutputStatus.setStatus("optional")
_DmsSchedule_ObjectIdentity = ObjectIdentity
dmsSchedule = _DmsSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 8)
)


class _NumActionTableEntries_Type(Integer32):
    """Custom type numActionTableEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumActionTableEntries_Type.__name__ = "Integer32"
_NumActionTableEntries_Object = MibScalar
numActionTableEntries = _NumActionTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 8, 1),
    _NumActionTableEntries_Type()
)
numActionTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActionTableEntries.setStatus("mandatory")
_DmsActionTable_Object = MibTable
dmsActionTable = _DmsActionTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 8, 2)
)
if mibBuilder.loadTexts:
    dmsActionTable.setStatus("mandatory")
_DmsActionEntry_Object = MibTableRow
dmsActionEntry = _DmsActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 8, 2, 1)
)
dmsActionEntry.setIndexNames(
    (0, "DMS-MIB", "dmsActionIndex"),
)
if mibBuilder.loadTexts:
    dmsActionEntry.setStatus("mandatory")


class _DmsActionIndex_Type(Integer32):
    """Custom type dmsActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DmsActionIndex_Type.__name__ = "Integer32"
_DmsActionIndex_Object = MibTableColumn
dmsActionIndex = _DmsActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 8, 2, 1, 1),
    _DmsActionIndex_Type()
)
dmsActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsActionIndex.setStatus("mandatory")
_DmsActionMsgCode_Type = MessageIDCode
_DmsActionMsgCode_Object = MibTableColumn
dmsActionMsgCode = _DmsActionMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 8, 2, 1, 2),
    _DmsActionMsgCode_Type()
)
dmsActionMsgCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsActionMsgCode.setStatus("mandatory")
_DmsStatus_ObjectIdentity = ObjectIdentity
dmsStatus = _DmsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9)
)


class _StatMultiFieldRows_Type(Integer32):
    """Custom type statMultiFieldRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StatMultiFieldRows_Type.__name__ = "Integer32"
_StatMultiFieldRows_Object = MibScalar
statMultiFieldRows = _StatMultiFieldRows_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 1),
    _StatMultiFieldRows_Type()
)
statMultiFieldRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statMultiFieldRows.setStatus("mandatory")
_StatMultiFieldTable_Object = MibTable
statMultiFieldTable = _StatMultiFieldTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 2)
)
if mibBuilder.loadTexts:
    statMultiFieldTable.setStatus("mandatory")
_StatMultiFieldEntry_Object = MibTableRow
statMultiFieldEntry = _StatMultiFieldEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 2, 1)
)
statMultiFieldEntry.setIndexNames(
    (0, "DMS-MIB", "statMultiFieldIndex"),
)
if mibBuilder.loadTexts:
    statMultiFieldEntry.setStatus("mandatory")


class _StatMultiFieldIndex_Type(Integer32):
    """Custom type statMultiFieldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StatMultiFieldIndex_Type.__name__ = "Integer32"
_StatMultiFieldIndex_Object = MibTableColumn
statMultiFieldIndex = _StatMultiFieldIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 2, 1, 1),
    _StatMultiFieldIndex_Type()
)
statMultiFieldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statMultiFieldIndex.setStatus("mandatory")


class _StatMultiFieldCode_Type(Integer32):
    """Custom type statMultiFieldCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StatMultiFieldCode_Type.__name__ = "Integer32"
_StatMultiFieldCode_Object = MibTableColumn
statMultiFieldCode = _StatMultiFieldCode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 2, 1, 2),
    _StatMultiFieldCode_Type()
)
statMultiFieldCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statMultiFieldCode.setStatus("mandatory")


class _StatMultiCurrentFieldValue_Type(OctetString):
    """Custom type statMultiCurrentFieldValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_StatMultiCurrentFieldValue_Type.__name__ = "OctetString"
_StatMultiCurrentFieldValue_Object = MibTableColumn
statMultiCurrentFieldValue = _StatMultiCurrentFieldValue_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 2, 1, 3),
    _StatMultiCurrentFieldValue_Type()
)
statMultiCurrentFieldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statMultiCurrentFieldValue.setStatus("mandatory")


class _DmsCurrentSpeed_Type(Integer32):
    """Custom type dmsCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsCurrentSpeed_Type.__name__ = "Integer32"
_DmsCurrentSpeed_Object = MibScalar
dmsCurrentSpeed = _DmsCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 3),
    _DmsCurrentSpeed_Type()
)
dmsCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsCurrentSpeed.setStatus("optional")


class _DmsCurrentSpeedLimit_Type(Integer32):
    """Custom type dmsCurrentSpeedLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsCurrentSpeedLimit_Type.__name__ = "Integer32"
_DmsCurrentSpeedLimit_Object = MibScalar
dmsCurrentSpeedLimit = _DmsCurrentSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 4),
    _DmsCurrentSpeedLimit_Type()
)
dmsCurrentSpeedLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmsCurrentSpeedLimit.setStatus("optional")
_WatchdogFailureCount_Type = Counter32
_WatchdogFailureCount_Object = MibScalar
watchdogFailureCount = _WatchdogFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 5),
    _WatchdogFailureCount_Type()
)
watchdogFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogFailureCount.setStatus("optional")


class _DmsStatDoorOpen_Type(Integer32):
    """Custom type dmsStatDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmsStatDoorOpen_Type.__name__ = "Integer32"
_DmsStatDoorOpen_Object = MibScalar
dmsStatDoorOpen = _DmsStatDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 6),
    _DmsStatDoorOpen_Type()
)
dmsStatDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmsStatDoorOpen.setStatus("optional")
_StatError_ObjectIdentity = ObjectIdentity
statError = _StatError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7)
)


class _ShortErrorStatus_Type(Integer32):
    """Custom type shortErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ShortErrorStatus_Type.__name__ = "Integer32"
_ShortErrorStatus_Object = MibScalar
shortErrorStatus = _ShortErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 1),
    _ShortErrorStatus_Type()
)
shortErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shortErrorStatus.setStatus("mandatory")


class _PixelFailureTableNumRows_Type(Integer32):
    """Custom type pixelFailureTableNumRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PixelFailureTableNumRows_Type.__name__ = "Integer32"
_PixelFailureTableNumRows_Object = MibScalar
pixelFailureTableNumRows = _PixelFailureTableNumRows_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 2),
    _PixelFailureTableNumRows_Type()
)
pixelFailureTableNumRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pixelFailureTableNumRows.setStatus("mandatory")
_PixelFailureTable_Object = MibTable
pixelFailureTable = _PixelFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3)
)
if mibBuilder.loadTexts:
    pixelFailureTable.setStatus("mandatory")
_PixelFailureEntry_Object = MibTableRow
pixelFailureEntry = _PixelFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3, 1)
)
pixelFailureEntry.setIndexNames(
    (0, "DMS-MIB", "pixelFailureDetectionType"),
    (0, "DMS-MIB", "pixelFailureIndex"),
)
if mibBuilder.loadTexts:
    pixelFailureEntry.setStatus("mandatory")


class _PixelFailureDetectionType_Type(Integer32):
    """Custom type pixelFailureDetectionType based on Integer32"""
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
          ("pixelTest", 2),
          ("messageDisplay", 3))
    )


_PixelFailureDetectionType_Type.__name__ = "Integer32"
_PixelFailureDetectionType_Object = MibTableColumn
pixelFailureDetectionType = _PixelFailureDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3, 1, 1),
    _PixelFailureDetectionType_Type()
)
pixelFailureDetectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pixelFailureDetectionType.setStatus("mandatory")


class _PixelFailureIndex_Type(Integer32):
    """Custom type pixelFailureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PixelFailureIndex_Type.__name__ = "Integer32"
_PixelFailureIndex_Object = MibTableColumn
pixelFailureIndex = _PixelFailureIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3, 1, 2),
    _PixelFailureIndex_Type()
)
pixelFailureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pixelFailureIndex.setStatus("mandatory")


class _PixelFailureXLocation_Type(Integer32):
    """Custom type pixelFailureXLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PixelFailureXLocation_Type.__name__ = "Integer32"
_PixelFailureXLocation_Object = MibTableColumn
pixelFailureXLocation = _PixelFailureXLocation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3, 1, 3),
    _PixelFailureXLocation_Type()
)
pixelFailureXLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pixelFailureXLocation.setStatus("mandatory")


class _PixelFailureYLocation_Type(Integer32):
    """Custom type pixelFailureYLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PixelFailureYLocation_Type.__name__ = "Integer32"
_PixelFailureYLocation_Object = MibTableColumn
pixelFailureYLocation = _PixelFailureYLocation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3, 1, 4),
    _PixelFailureYLocation_Type()
)
pixelFailureYLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pixelFailureYLocation.setStatus("mandatory")


class _PixelFailureStatus_Type(Integer32):
    """Custom type pixelFailureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PixelFailureStatus_Type.__name__ = "Integer32"
_PixelFailureStatus_Object = MibTableColumn
pixelFailureStatus = _PixelFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 3, 1, 5),
    _PixelFailureStatus_Type()
)
pixelFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pixelFailureStatus.setStatus("mandatory")


class _PixelTestActivation_Type(Integer32):
    """Custom type pixelTestActivation based on Integer32"""
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
          ("noTest", 2),
          ("test", 3),
          ("clearTable", 4))
    )


_PixelTestActivation_Type.__name__ = "Integer32"
_PixelTestActivation_Object = MibScalar
pixelTestActivation = _PixelTestActivation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 4),
    _PixelTestActivation_Type()
)
pixelTestActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pixelTestActivation.setStatus("mandatory")


class _LampFailureStuckOn_Type(OctetString):
    """Custom type lampFailureStuckOn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LampFailureStuckOn_Type.__name__ = "OctetString"
_LampFailureStuckOn_Object = MibScalar
lampFailureStuckOn = _LampFailureStuckOn_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 5),
    _LampFailureStuckOn_Type()
)
lampFailureStuckOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lampFailureStuckOn.setStatus("mandatory")


class _LampFailureStuckOff_Type(OctetString):
    """Custom type lampFailureStuckOff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LampFailureStuckOff_Type.__name__ = "OctetString"
_LampFailureStuckOff_Object = MibScalar
lampFailureStuckOff = _LampFailureStuckOff_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 6),
    _LampFailureStuckOff_Type()
)
lampFailureStuckOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lampFailureStuckOff.setStatus("mandatory")


class _LampTestActivation_Type(Integer32):
    """Custom type lampTestActivation based on Integer32"""
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
          ("noTest", 2),
          ("test", 3))
    )


_LampTestActivation_Type.__name__ = "Integer32"
_LampTestActivation_Object = MibScalar
lampTestActivation = _LampTestActivation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 7),
    _LampTestActivation_Type()
)
lampTestActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lampTestActivation.setStatus("mandatory")


class _FanFailures_Type(OctetString):
    """Custom type fanFailures based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_FanFailures_Type.__name__ = "OctetString"
_FanFailures_Object = MibScalar
fanFailures = _FanFailures_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 8),
    _FanFailures_Type()
)
fanFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFailures.setStatus("optional")


class _FanTestActivation_Type(Integer32):
    """Custom type fanTestActivation based on Integer32"""
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
          ("noTest", 2),
          ("test", 3))
    )


_FanTestActivation_Type.__name__ = "Integer32"
_FanTestActivation_Object = MibScalar
fanTestActivation = _FanTestActivation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 9),
    _FanTestActivation_Type()
)
fanTestActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanTestActivation.setStatus("optional")


class _ControllerErrorStatus_Type(Integer32):
    """Custom type controllerErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ControllerErrorStatus_Type.__name__ = "Integer32"
_ControllerErrorStatus_Object = MibScalar
controllerErrorStatus = _ControllerErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 7, 10),
    _ControllerErrorStatus_Type()
)
controllerErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerErrorStatus.setStatus("mandatory")
_StatPower_ObjectIdentity = ObjectIdentity
statPower = _StatPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8)
)


class _SignVolts_Type(Integer32):
    """Custom type signVolts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SignVolts_Type.__name__ = "Integer32"
_SignVolts_Object = MibScalar
signVolts = _SignVolts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8, 1),
    _SignVolts_Type()
)
signVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signVolts.setStatus("optional")


class _LowFuelThreshold_Type(Integer32):
    """Custom type lowFuelThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LowFuelThreshold_Type.__name__ = "Integer32"
_LowFuelThreshold_Object = MibScalar
lowFuelThreshold = _LowFuelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8, 2),
    _LowFuelThreshold_Type()
)
lowFuelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowFuelThreshold.setStatus("optional")


class _FuelLevel_Type(Integer32):
    """Custom type fuelLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FuelLevel_Type.__name__ = "Integer32"
_FuelLevel_Object = MibScalar
fuelLevel = _FuelLevel_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8, 3),
    _FuelLevel_Type()
)
fuelLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelLevel.setStatus("optional")


class _EngineRPM_Type(Integer32):
    """Custom type engineRPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EngineRPM_Type.__name__ = "Integer32"
_EngineRPM_Object = MibScalar
engineRPM = _EngineRPM_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8, 4),
    _EngineRPM_Type()
)
engineRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engineRPM.setStatus("optional")


class _LineVolts_Type(Integer32):
    """Custom type lineVolts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LineVolts_Type.__name__ = "Integer32"
_LineVolts_Object = MibScalar
lineVolts = _LineVolts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8, 5),
    _LineVolts_Type()
)
lineVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineVolts.setStatus("optional")


class _PowerSource_Type(Integer32):
    """Custom type powerSource based on Integer32"""
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
        *(("other", 1),
          ("powerShutdown", 2),
          ("noSignPower", 3),
          ("acLine", 4),
          ("generator", 5),
          ("solar", 6),
          ("battery", 7))
    )


_PowerSource_Type.__name__ = "Integer32"
_PowerSource_Object = MibScalar
powerSource = _PowerSource_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 8, 6),
    _PowerSource_Type()
)
powerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSource.setStatus("mandatory")
_StatTemp_ObjectIdentity = ObjectIdentity
statTemp = _StatTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9)
)


class _TempMinCtrlCabinet_Type(Integer32):
    """Custom type tempMinCtrlCabinet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempMinCtrlCabinet_Type.__name__ = "Integer32"
_TempMinCtrlCabinet_Object = MibScalar
tempMinCtrlCabinet = _TempMinCtrlCabinet_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9, 1),
    _TempMinCtrlCabinet_Type()
)
tempMinCtrlCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinCtrlCabinet.setStatus("optional")


class _TempMaxCtrlCabinet_Type(Integer32):
    """Custom type tempMaxCtrlCabinet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempMaxCtrlCabinet_Type.__name__ = "Integer32"
_TempMaxCtrlCabinet_Object = MibScalar
tempMaxCtrlCabinet = _TempMaxCtrlCabinet_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9, 2),
    _TempMaxCtrlCabinet_Type()
)
tempMaxCtrlCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxCtrlCabinet.setStatus("optional")


class _TempMinAmbient_Type(Integer32):
    """Custom type tempMinAmbient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempMinAmbient_Type.__name__ = "Integer32"
_TempMinAmbient_Object = MibScalar
tempMinAmbient = _TempMinAmbient_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9, 3),
    _TempMinAmbient_Type()
)
tempMinAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinAmbient.setStatus("optional")


class _TempMaxAmbient_Type(Integer32):
    """Custom type tempMaxAmbient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempMaxAmbient_Type.__name__ = "Integer32"
_TempMaxAmbient_Object = MibScalar
tempMaxAmbient = _TempMaxAmbient_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9, 4),
    _TempMaxAmbient_Type()
)
tempMaxAmbient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxAmbient.setStatus("optional")


class _TempMinSignHousing_Type(Integer32):
    """Custom type tempMinSignHousing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_TempMinSignHousing_Type.__name__ = "Integer32"
_TempMinSignHousing_Object = MibScalar
tempMinSignHousing = _TempMinSignHousing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9, 5),
    _TempMinSignHousing_Type()
)
tempMinSignHousing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinSignHousing.setStatus("optional")


class _TempMaxSignHousing_Type(Integer32):
    """Custom type tempMaxSignHousing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TempMaxSignHousing_Type.__name__ = "Integer32"
_TempMaxSignHousing_Object = MibScalar
tempMaxSignHousing = _TempMaxSignHousing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 3, 9, 9, 6),
    _TempMaxSignHousing_Type()
)
tempMaxSignHousing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxSignHousing.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMS-MIB",
    **{"MessageIDCode": MessageIDCode,
       "MessageActivationCode": MessageActivationCode,
       "exp-global": exp_global,
       "auxiliaryIO": auxiliaryIO,
       "maxAuxIODigital": maxAuxIODigital,
       "maxAuxIOAnalog": maxAuxIOAnalog,
       "auxIOTable": auxIOTable,
       "auxIOEntry": auxIOEntry,
       "auxIOPortType": auxIOPortType,
       "auxIOPortNumber": auxIOPortNumber,
       "auxIODescription": auxIODescription,
       "auxIOResolution": auxIOResolution,
       "auxIOValue": auxIOValue,
       "auxIOPortDirection": auxIOPortDirection,
       "dms": dms,
       "dmsSignCfg": dmsSignCfg,
       "dmsSignAccess": dmsSignAccess,
       "dmsSignType": dmsSignType,
       "dmsSignHeight": dmsSignHeight,
       "dmsSignWidth": dmsSignWidth,
       "dmsHorizontalBorder": dmsHorizontalBorder,
       "dmsVerticalBorder": dmsVerticalBorder,
       "dmsLegend": dmsLegend,
       "dmsBeaconType": dmsBeaconType,
       "dmsSignTechnology": dmsSignTechnology,
       "vmsCfg": vmsCfg,
       "vmsCharacterHeightPixels": vmsCharacterHeightPixels,
       "vmsCharacterWidthPixels": vmsCharacterWidthPixels,
       "vmsSignHeightPixels": vmsSignHeightPixels,
       "vmsSignWidthPixels": vmsSignWidthPixels,
       "vmsHorizontalPitch": vmsHorizontalPitch,
       "vmsVerticalPitch": vmsVerticalPitch,
       "fontDefinition": fontDefinition,
       "numFonts": numFonts,
       "fontTable": fontTable,
       "fontEntry": fontEntry,
       "fontIndex": fontIndex,
       "fontNumber": fontNumber,
       "fontName": fontName,
       "fontHeight": fontHeight,
       "fontCharSpacing": fontCharSpacing,
       "fontLineSpacing": fontLineSpacing,
       "fontVersionID": fontVersionID,
       "maxFontCharacters": maxFontCharacters,
       "characterTable": characterTable,
       "characterEntry": characterEntry,
       "characterNumber": characterNumber,
       "characterWidth": characterWidth,
       "characterBitmap": characterBitmap,
       "multiCfg": multiCfg,
       "defaultBackgroundColor": defaultBackgroundColor,
       "defaultForegroundColor": defaultForegroundColor,
       "defaultFlashOn": defaultFlashOn,
       "defaultFlashOff": defaultFlashOff,
       "defaultFont": defaultFont,
       "defaultJustificationLine": defaultJustificationLine,
       "defaultJustificationPage": defaultJustificationPage,
       "defaultPageOnTime": defaultPageOnTime,
       "defaultPageOffTime": defaultPageOffTime,
       "defaultCharacterSet": defaultCharacterSet,
       "dmsMessage": dmsMessage,
       "dmsNumPermanentMsg": dmsNumPermanentMsg,
       "dmsNumChangeableMsg": dmsNumChangeableMsg,
       "dmsMaxChangeableMsg": dmsMaxChangeableMsg,
       "dmsFreeChangeableMemory": dmsFreeChangeableMemory,
       "dmsNumVolatileMsg": dmsNumVolatileMsg,
       "dmsMaxVolatileMsg": dmsMaxVolatileMsg,
       "dmsFreeVolatileMemory": dmsFreeVolatileMemory,
       "dmsMessageTable": dmsMessageTable,
       "dmsMessageEntry": dmsMessageEntry,
       "dmsMessageMemoryType": dmsMessageMemoryType,
       "dmsMessageNumber": dmsMessageNumber,
       "dmsMessageMultiString": dmsMessageMultiString,
       "dmsMessageOwner": dmsMessageOwner,
       "dmsMessageCRC": dmsMessageCRC,
       "dmsMessageBeacon": dmsMessageBeacon,
       "dmsMessagePixelService": dmsMessagePixelService,
       "dmsMessageRunTimePriority": dmsMessageRunTimePriority,
       "dmsMessageStatus": dmsMessageStatus,
       "dmsValidateMessageError": dmsValidateMessageError,
       "signControl": signControl,
       "dmsControlMode": dmsControlMode,
       "dmsSWReset": dmsSWReset,
       "dmsActivateMessage": dmsActivateMessage,
       "dmsMessageTimeRemaining": dmsMessageTimeRemaining,
       "dmsMsgTableSource": dmsMsgTableSource,
       "dmsMsgRequesterID": dmsMsgRequesterID,
       "dmsMsgSourceMode": dmsMsgSourceMode,
       "dmsShortPowerRecoveryMessage": dmsShortPowerRecoveryMessage,
       "dmsLongPowerRecoveryMessage": dmsLongPowerRecoveryMessage,
       "dmsShortPowerLossTime": dmsShortPowerLossTime,
       "dmsResetMessage": dmsResetMessage,
       "dmsCommunicationsLossMessage": dmsCommunicationsLossMessage,
       "dmsTimeCommLoss": dmsTimeCommLoss,
       "dmsPowerLossMessage": dmsPowerLossMessage,
       "dmsEndDurationMessage": dmsEndDurationMessage,
       "dmsMemoryMgmt": dmsMemoryMgmt,
       "dmsActivateMsgError": dmsActivateMsgError,
       "dmsMultiSyntaxError": dmsMultiSyntaxError,
       "dmsMultiSyntaxErrorPosition": dmsMultiSyntaxErrorPosition,
       "dmsMultiOtherErrorDescription": dmsMultiOtherErrorDescription,
       "vmsPixelServiceDuration": vmsPixelServiceDuration,
       "vmsPixelServiceFrequency": vmsPixelServiceFrequency,
       "vmsPixelServiceTime": vmsPixelServiceTime,
       "illum": illum,
       "dmsIllumControl": dmsIllumControl,
       "dmsIllumMaxPhotocellLevel": dmsIllumMaxPhotocellLevel,
       "dmsIllumPhotocellLevelStatus": dmsIllumPhotocellLevelStatus,
       "dmsIllumNumBrightLevels": dmsIllumNumBrightLevels,
       "dmsIllumBrightLevelStatus": dmsIllumBrightLevelStatus,
       "dmsIllumManLevel": dmsIllumManLevel,
       "dmsIllumBrightnessValues": dmsIllumBrightnessValues,
       "dmsIllumBrightnessValuesError": dmsIllumBrightnessValuesError,
       "dmsIllumLightOutputStatus": dmsIllumLightOutputStatus,
       "dmsSchedule": dmsSchedule,
       "numActionTableEntries": numActionTableEntries,
       "dmsActionTable": dmsActionTable,
       "dmsActionEntry": dmsActionEntry,
       "dmsActionIndex": dmsActionIndex,
       "dmsActionMsgCode": dmsActionMsgCode,
       "dmsStatus": dmsStatus,
       "statMultiFieldRows": statMultiFieldRows,
       "statMultiFieldTable": statMultiFieldTable,
       "statMultiFieldEntry": statMultiFieldEntry,
       "statMultiFieldIndex": statMultiFieldIndex,
       "statMultiFieldCode": statMultiFieldCode,
       "statMultiCurrentFieldValue": statMultiCurrentFieldValue,
       "dmsCurrentSpeed": dmsCurrentSpeed,
       "dmsCurrentSpeedLimit": dmsCurrentSpeedLimit,
       "watchdogFailureCount": watchdogFailureCount,
       "dmsStatDoorOpen": dmsStatDoorOpen,
       "statError": statError,
       "shortErrorStatus": shortErrorStatus,
       "pixelFailureTableNumRows": pixelFailureTableNumRows,
       "pixelFailureTable": pixelFailureTable,
       "pixelFailureEntry": pixelFailureEntry,
       "pixelFailureDetectionType": pixelFailureDetectionType,
       "pixelFailureIndex": pixelFailureIndex,
       "pixelFailureXLocation": pixelFailureXLocation,
       "pixelFailureYLocation": pixelFailureYLocation,
       "pixelFailureStatus": pixelFailureStatus,
       "pixelTestActivation": pixelTestActivation,
       "lampFailureStuckOn": lampFailureStuckOn,
       "lampFailureStuckOff": lampFailureStuckOff,
       "lampTestActivation": lampTestActivation,
       "fanFailures": fanFailures,
       "fanTestActivation": fanTestActivation,
       "controllerErrorStatus": controllerErrorStatus,
       "statPower": statPower,
       "signVolts": signVolts,
       "lowFuelThreshold": lowFuelThreshold,
       "fuelLevel": fuelLevel,
       "engineRPM": engineRPM,
       "lineVolts": lineVolts,
       "powerSource": powerSource,
       "statTemp": statTemp,
       "tempMinCtrlCabinet": tempMinCtrlCabinet,
       "tempMaxCtrlCabinet": tempMaxCtrlCabinet,
       "tempMinAmbient": tempMinAmbient,
       "tempMaxAmbient": tempMaxAmbient,
       "tempMinSignHousing": tempMinSignHousing,
       "tempMaxSignHousing": tempMaxSignHousing}
)
