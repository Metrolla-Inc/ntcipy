# SNMP MIB module (ESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1204ESS.mib
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
 devices) = mibBuilder.importSymbols(
    "TMIB-II",
    "DisplayString",
    "devices")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ess_ObjectIdentity = ObjectIdentity
ess = _Ess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5)
)
_EssBufr_ObjectIdentity = ObjectIdentity
essBufr = _EssBufr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1)
)
_EssBufrInstrumentation_ObjectIdentity = ObjectIdentity
essBufrInstrumentation = _EssBufrInstrumentation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 2)
)


class _EssTypeofStation_Type(Integer32):
    """Custom type essTypeofStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_EssTypeofStation_Type.__name__ = "Integer32"
_EssTypeofStation_Object = MibScalar
essTypeofStation = _EssTypeofStation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 2, 1),
    _EssTypeofStation_Type()
)
essTypeofStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essTypeofStation.setStatus("mandatory")
_EssBufrLocationVertical_ObjectIdentity = ObjectIdentity
essBufrLocationVertical = _EssBufrLocationVertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 7)
)


class _EssAtmosphericPressure_Type(Integer32):
    """Custom type essAtmosphericPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssAtmosphericPressure_Type.__name__ = "Integer32"
_EssAtmosphericPressure_Object = MibScalar
essAtmosphericPressure = _EssAtmosphericPressure_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 7, 4),
    _EssAtmosphericPressure_Type()
)
essAtmosphericPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essAtmosphericPressure.setStatus("mandatory")
_EssBufrWind_ObjectIdentity = ObjectIdentity
essBufrWind = _EssBufrWind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 11)
)


class _EssAvgWindDirection_Type(Integer32):
    """Custom type essAvgWindDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 361),
    )


_EssAvgWindDirection_Type.__name__ = "Integer32"
_EssAvgWindDirection_Object = MibScalar
essAvgWindDirection = _EssAvgWindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 11, 1),
    _EssAvgWindDirection_Type()
)
essAvgWindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essAvgWindDirection.setStatus("mandatory")


class _EssAvgWindSpeed_Type(Integer32):
    """Custom type essAvgWindSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssAvgWindSpeed_Type.__name__ = "Integer32"
_EssAvgWindSpeed_Object = MibScalar
essAvgWindSpeed = _EssAvgWindSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 11, 2),
    _EssAvgWindSpeed_Type()
)
essAvgWindSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essAvgWindSpeed.setStatus("mandatory")


class _EssMaxWindGustSpeed_Type(Integer32):
    """Custom type essMaxWindGustSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssMaxWindGustSpeed_Type.__name__ = "Integer32"
_EssMaxWindGustSpeed_Object = MibScalar
essMaxWindGustSpeed = _EssMaxWindGustSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 11, 41),
    _EssMaxWindGustSpeed_Type()
)
essMaxWindGustSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMaxWindGustSpeed.setStatus("mandatory")


class _EssMaxWindGustDir_Type(Integer32):
    """Custom type essMaxWindGustDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 361),
    )


_EssMaxWindGustDir_Type.__name__ = "Integer32"
_EssMaxWindGustDir_Object = MibScalar
essMaxWindGustDir = _EssMaxWindGustDir_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 11, 43),
    _EssMaxWindGustDir_Type()
)
essMaxWindGustDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMaxWindGustDir.setStatus("mandatory")
_EssBufrPrecip_ObjectIdentity = ObjectIdentity
essBufrPrecip = _EssBufrPrecip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13)
)


class _EssRelativeHumidity_Type(Integer32):
    """Custom type essRelativeHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EssRelativeHumidity_Type.__name__ = "Integer32"
_EssRelativeHumidity_Object = MibScalar
essRelativeHumidity = _EssRelativeHumidity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 3),
    _EssRelativeHumidity_Type()
)
essRelativeHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essRelativeHumidity.setStatus("mandatory")


class _EssPrecipRate_Type(Integer32):
    """Custom type essPrecipRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPrecipRate_Type.__name__ = "Integer32"
_EssPrecipRate_Object = MibScalar
essPrecipRate = _EssPrecipRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 14),
    _EssPrecipRate_Type()
)
essPrecipRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipRate.setStatus("mandatory")


class _EssSnowfallAccumRate_Type(Integer32):
    """Custom type essSnowfallAccumRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssSnowfallAccumRate_Type.__name__ = "Integer32"
_EssSnowfallAccumRate_Object = MibScalar
essSnowfallAccumRate = _EssSnowfallAccumRate_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 15),
    _EssSnowfallAccumRate_Type()
)
essSnowfallAccumRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSnowfallAccumRate.setStatus("mandatory")


class _EssPrecipitationOneHour_Type(Integer32):
    """Custom type essPrecipitationOneHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPrecipitationOneHour_Type.__name__ = "Integer32"
_EssPrecipitationOneHour_Object = MibScalar
essPrecipitationOneHour = _EssPrecipitationOneHour_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 19),
    _EssPrecipitationOneHour_Type()
)
essPrecipitationOneHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitationOneHour.setStatus("mandatory")


class _EssPrecipitationThreeHours_Type(Integer32):
    """Custom type essPrecipitationThreeHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPrecipitationThreeHours_Type.__name__ = "Integer32"
_EssPrecipitationThreeHours_Object = MibScalar
essPrecipitationThreeHours = _EssPrecipitationThreeHours_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 20),
    _EssPrecipitationThreeHours_Type()
)
essPrecipitationThreeHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitationThreeHours.setStatus("mandatory")


class _EssPrecipitationSixHours_Type(Integer32):
    """Custom type essPrecipitationSixHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPrecipitationSixHours_Type.__name__ = "Integer32"
_EssPrecipitationSixHours_Object = MibScalar
essPrecipitationSixHours = _EssPrecipitationSixHours_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 21),
    _EssPrecipitationSixHours_Type()
)
essPrecipitationSixHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitationSixHours.setStatus("mandatory")


class _EssPrecipitationTwelveHours_Type(Integer32):
    """Custom type essPrecipitationTwelveHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPrecipitationTwelveHours_Type.__name__ = "Integer32"
_EssPrecipitationTwelveHours_Object = MibScalar
essPrecipitationTwelveHours = _EssPrecipitationTwelveHours_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 22),
    _EssPrecipitationTwelveHours_Type()
)
essPrecipitationTwelveHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitationTwelveHours.setStatus("mandatory")


class _EssPrecipitation24Hours_Type(Integer32):
    """Custom type essPrecipitation24Hours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPrecipitation24Hours_Type.__name__ = "Integer32"
_EssPrecipitation24Hours_Object = MibScalar
essPrecipitation24Hours = _EssPrecipitation24Hours_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 13, 23),
    _EssPrecipitation24Hours_Type()
)
essPrecipitation24Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitation24Hours.setStatus("mandatory")
_EssBufrRadiation_ObjectIdentity = ObjectIdentity
essBufrRadiation = _EssBufrRadiation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 14)
)


class _EssSolarRadiation_Type(Integer32):
    """Custom type essSolarRadiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssSolarRadiation_Type.__name__ = "Integer32"
_EssSolarRadiation_Object = MibScalar
essSolarRadiation = _EssSolarRadiation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 14, 24),
    _EssSolarRadiation_Type()
)
essSolarRadiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSolarRadiation.setStatus("mandatory")


class _EssTotalSun_Type(Integer32):
    """Custom type essTotalSun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1441),
    )


_EssTotalSun_Type.__name__ = "Integer32"
_EssTotalSun_Object = MibScalar
essTotalSun = _EssTotalSun_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 1, 14, 31),
    _EssTotalSun_Type()
)
essTotalSun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essTotalSun.setStatus("mandatory")
_EssNtcip_ObjectIdentity = ObjectIdentity
essNtcip = _EssNtcip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2)
)
_EssNtcipIdentification_ObjectIdentity = ObjectIdentity
essNtcipIdentification = _EssNtcipIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 1)
)
_EssNtcipNum_Type = IpAddress
_EssNtcipNum_Object = MibScalar
essNtcipNum = _EssNtcipNum_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 1, 1),
    _EssNtcipNum_Type()
)
essNtcipNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essNtcipNum.setStatus("mandatory")


class _EssNtcipCategory_Type(Integer32):
    """Custom type essNtcipCategory based on Integer32"""
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
          ("permanent", 2),
          ("transportable", 3),
          ("mobile", 4))
    )


_EssNtcipCategory_Type.__name__ = "Integer32"
_EssNtcipCategory_Object = MibScalar
essNtcipCategory = _EssNtcipCategory_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 1, 2),
    _EssNtcipCategory_Type()
)
essNtcipCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essNtcipCategory.setStatus("mandatory")


class _EssNtcipSiteDescription_Type(DisplayString):
    """Custom type essNtcipSiteDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EssNtcipSiteDescription_Type.__name__ = "DisplayString"
_EssNtcipSiteDescription_Object = MibScalar
essNtcipSiteDescription = _EssNtcipSiteDescription_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 1, 3),
    _EssNtcipSiteDescription_Type()
)
essNtcipSiteDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essNtcipSiteDescription.setStatus("mandatory")
_EssNtcipHeight_ObjectIdentity = ObjectIdentity
essNtcipHeight = _EssNtcipHeight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 3)
)


class _EssReferenceHeight_Type(Integer32):
    """Custom type essReferenceHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 8001),
    )


_EssReferenceHeight_Type.__name__ = "Integer32"
_EssReferenceHeight_Object = MibScalar
essReferenceHeight = _EssReferenceHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 3, 1),
    _EssReferenceHeight_Type()
)
essReferenceHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essReferenceHeight.setStatus("mandatory")


class _EssPressureHeight_Type(Integer32):
    """Custom type essPressureHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssPressureHeight_Type.__name__ = "Integer32"
_EssPressureHeight_Object = MibScalar
essPressureHeight = _EssPressureHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 3, 2),
    _EssPressureHeight_Type()
)
essPressureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPressureHeight.setStatus("mandatory")


class _EssWindSensorHeight_Type(Integer32):
    """Custom type essWindSensorHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssWindSensorHeight_Type.__name__ = "Integer32"
_EssWindSensorHeight_Object = MibScalar
essWindSensorHeight = _EssWindSensorHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 3, 3),
    _EssWindSensorHeight_Type()
)
essWindSensorHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essWindSensorHeight.setStatus("mandatory")
_EssNtcipWind_ObjectIdentity = ObjectIdentity
essNtcipWind = _EssNtcipWind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 4)
)


class _EssSpotWindDirection_Type(Integer32):
    """Custom type essSpotWindDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 361),
    )


_EssSpotWindDirection_Type.__name__ = "Integer32"
_EssSpotWindDirection_Object = MibScalar
essSpotWindDirection = _EssSpotWindDirection_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 4, 1),
    _EssSpotWindDirection_Type()
)
essSpotWindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSpotWindDirection.setStatus("mandatory")


class _EssSpotWindSpeed_Type(Integer32):
    """Custom type essSpotWindSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssSpotWindSpeed_Type.__name__ = "Integer32"
_EssSpotWindSpeed_Object = MibScalar
essSpotWindSpeed = _EssSpotWindSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 4, 2),
    _EssSpotWindSpeed_Type()
)
essSpotWindSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSpotWindSpeed.setStatus("mandatory")


class _EssWindSituation_Type(Integer32):
    """Custom type essWindSituation based on Integer32"""
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
          ("unknown", 2),
          ("calm", 3),
          ("lightBreeze", 4),
          ("moderateBreeze", 5),
          ("strongBreeze", 6),
          ("gale", 7),
          ("moderateGale", 8),
          ("strongGale", 9),
          ("stormWinds", 10),
          ("hurricaneForceWinds", 11),
          ("gustyWinds", 12))
    )


_EssWindSituation_Type.__name__ = "Integer32"
_EssWindSituation_Object = MibScalar
essWindSituation = _EssWindSituation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 4, 3),
    _EssWindSituation_Type()
)
essWindSituation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essWindSituation.setStatus("mandatory")
_EssNtcipTemperature_ObjectIdentity = ObjectIdentity
essNtcipTemperature = _EssNtcipTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5)
)


class _EssNumTemperatureSensors_Type(Integer32):
    """Custom type essNumTemperatureSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssNumTemperatureSensors_Type.__name__ = "Integer32"
_EssNumTemperatureSensors_Object = MibScalar
essNumTemperatureSensors = _EssNumTemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 1),
    _EssNumTemperatureSensors_Type()
)
essNumTemperatureSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essNumTemperatureSensors.setStatus("mandatory")
_EssTemperatureSensorTable_Object = MibTable
essTemperatureSensorTable = _EssTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    essTemperatureSensorTable.setStatus("mandatory")
_EssTemperatureSensorEntry_Object = MibTableRow
essTemperatureSensorEntry = _EssTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 2, 1)
)
essTemperatureSensorEntry.setIndexNames(
    (0, "ESS-MIB", "essTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    essTemperatureSensorEntry.setStatus("mandatory")


class _EssTemperatureSensorIndex_Type(Integer32):
    """Custom type essTemperatureSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EssTemperatureSensorIndex_Type.__name__ = "Integer32"
_EssTemperatureSensorIndex_Object = MibTableColumn
essTemperatureSensorIndex = _EssTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 2, 1, 1),
    _EssTemperatureSensorIndex_Type()
)
essTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essTemperatureSensorIndex.setStatus("mandatory")


class _EssTemperatureSensorHeight_Type(Integer32):
    """Custom type essTemperatureSensorHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssTemperatureSensorHeight_Type.__name__ = "Integer32"
_EssTemperatureSensorHeight_Object = MibTableColumn
essTemperatureSensorHeight = _EssTemperatureSensorHeight_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 2, 1, 2),
    _EssTemperatureSensorHeight_Type()
)
essTemperatureSensorHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essTemperatureSensorHeight.setStatus("mandatory")


class _EssAirTemperature_Type(Integer32):
    """Custom type essAirTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssAirTemperature_Type.__name__ = "Integer32"
_EssAirTemperature_Object = MibTableColumn
essAirTemperature = _EssAirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 2, 1, 3),
    _EssAirTemperature_Type()
)
essAirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essAirTemperature.setStatus("mandatory")


class _EssWetbulbTemp_Type(Integer32):
    """Custom type essWetbulbTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssWetbulbTemp_Type.__name__ = "Integer32"
_EssWetbulbTemp_Object = MibScalar
essWetbulbTemp = _EssWetbulbTemp_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 3),
    _EssWetbulbTemp_Type()
)
essWetbulbTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essWetbulbTemp.setStatus("mandatory")


class _EssDewpointTemp_Type(Integer32):
    """Custom type essDewpointTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssDewpointTemp_Type.__name__ = "Integer32"
_EssDewpointTemp_Object = MibScalar
essDewpointTemp = _EssDewpointTemp_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 4),
    _EssDewpointTemp_Type()
)
essDewpointTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essDewpointTemp.setStatus("mandatory")


class _EssMaxTemp_Type(Integer32):
    """Custom type essMaxTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssMaxTemp_Type.__name__ = "Integer32"
_EssMaxTemp_Object = MibScalar
essMaxTemp = _EssMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 5),
    _EssMaxTemp_Type()
)
essMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMaxTemp.setStatus("mandatory")


class _EssMinTemp_Type(Integer32):
    """Custom type essMinTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssMinTemp_Type.__name__ = "Integer32"
_EssMinTemp_Object = MibScalar
essMinTemp = _EssMinTemp_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 5, 6),
    _EssMinTemp_Type()
)
essMinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMinTemp.setStatus("mandatory")
_EssNtcipPrecip_ObjectIdentity = ObjectIdentity
essNtcipPrecip = _EssNtcipPrecip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6)
)


class _EssWaterDepth_Type(Integer32):
    """Custom type essWaterDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssWaterDepth_Type.__name__ = "Integer32"
_EssWaterDepth_Object = MibScalar
essWaterDepth = _EssWaterDepth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 1),
    _EssWaterDepth_Type()
)
essWaterDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essWaterDepth.setStatus("mandatory")


class _EssAdjacentSnowDepth_Type(Integer32):
    """Custom type essAdjacentSnowDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3001),
    )


_EssAdjacentSnowDepth_Type.__name__ = "Integer32"
_EssAdjacentSnowDepth_Object = MibScalar
essAdjacentSnowDepth = _EssAdjacentSnowDepth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 2),
    _EssAdjacentSnowDepth_Type()
)
essAdjacentSnowDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essAdjacentSnowDepth.setStatus("mandatory")


class _EssRoadwaySnowDepth_Type(Integer32):
    """Custom type essRoadwaySnowDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3001),
    )


_EssRoadwaySnowDepth_Type.__name__ = "Integer32"
_EssRoadwaySnowDepth_Object = MibScalar
essRoadwaySnowDepth = _EssRoadwaySnowDepth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 3),
    _EssRoadwaySnowDepth_Type()
)
essRoadwaySnowDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essRoadwaySnowDepth.setStatus("mandatory")


class _EssRoadwaySnowPackDepth_Type(Integer32):
    """Custom type essRoadwaySnowPackDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3001),
    )


_EssRoadwaySnowPackDepth_Type.__name__ = "Integer32"
_EssRoadwaySnowPackDepth_Object = MibScalar
essRoadwaySnowPackDepth = _EssRoadwaySnowPackDepth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 4),
    _EssRoadwaySnowPackDepth_Type()
)
essRoadwaySnowPackDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essRoadwaySnowPackDepth.setStatus("mandatory")


class _EssPrecipYesNo_Type(Integer32):
    """Custom type essPrecipYesNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("precip", 1),
          ("noPrecip", 2),
          ("error", 3))
    )


_EssPrecipYesNo_Type.__name__ = "Integer32"
_EssPrecipYesNo_Object = MibScalar
essPrecipYesNo = _EssPrecipYesNo_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 5),
    _EssPrecipYesNo_Type()
)
essPrecipYesNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipYesNo.setStatus("mandatory")


class _EssPrecipSituation_Type(Integer32):
    """Custom type essPrecipSituation based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("noPrecipitation", 3),
          ("unidentifiedSlight", 4),
          ("unidentifiedModerate", 5),
          ("unidentifiedHeavy", 6),
          ("snowSlight", 7),
          ("snowModerate", 8),
          ("snowHeavy", 9),
          ("rainSlight", 10),
          ("rainModerate", 11),
          ("rainHeavy", 12),
          ("frozenPrecipitationSlight", 13),
          ("frozenPrecipitationModerate", 14),
          ("frozenPrecipitationHeavy", 15))
    )


_EssPrecipSituation_Type.__name__ = "Integer32"
_EssPrecipSituation_Object = MibScalar
essPrecipSituation = _EssPrecipSituation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 6),
    _EssPrecipSituation_Type()
)
essPrecipSituation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipSituation.setStatus("mandatory")


class _EssIceThickness_Type(Integer32):
    """Custom type essIceThickness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssIceThickness_Type.__name__ = "Integer32"
_EssIceThickness_Object = MibScalar
essIceThickness = _EssIceThickness_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 7),
    _EssIceThickness_Type()
)
essIceThickness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essIceThickness.setStatus("mandatory")


class _EssPrecipitationStartTime_Type(Integer32):
    """Custom type essPrecipitationStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EssPrecipitationStartTime_Type.__name__ = "Integer32"
_EssPrecipitationStartTime_Object = MibScalar
essPrecipitationStartTime = _EssPrecipitationStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 8),
    _EssPrecipitationStartTime_Type()
)
essPrecipitationStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitationStartTime.setStatus("mandatory")


class _EssPrecipitationEndTime_Type(Integer32):
    """Custom type essPrecipitationEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EssPrecipitationEndTime_Type.__name__ = "Integer32"
_EssPrecipitationEndTime_Object = MibScalar
essPrecipitationEndTime = _EssPrecipitationEndTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 6, 9),
    _EssPrecipitationEndTime_Type()
)
essPrecipitationEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPrecipitationEndTime.setStatus("mandatory")
_EssNtcipRadiation_ObjectIdentity = ObjectIdentity
essNtcipRadiation = _EssNtcipRadiation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 7)
)


class _EssCloudSituation_Type(Integer32):
    """Custom type essCloudSituation based on Integer32"""
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
        *(("overcast", 1),
          ("cloudy", 2),
          ("partlyCloudy", 3),
          ("mostlyClear", 4),
          ("clear", 5))
    )


_EssCloudSituation_Type.__name__ = "Integer32"
_EssCloudSituation_Object = MibScalar
essCloudSituation = _EssCloudSituation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 7, 1),
    _EssCloudSituation_Type()
)
essCloudSituation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essCloudSituation.setStatus("mandatory")
_EssNtcipVisibility_ObjectIdentity = ObjectIdentity
essNtcipVisibility = _EssNtcipVisibility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 8)
)


class _EssVisibility_Type(Integer32):
    """Custom type essVisibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000001),
    )


_EssVisibility_Type.__name__ = "Integer32"
_EssVisibility_Object = MibScalar
essVisibility = _EssVisibility_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 8, 1),
    _EssVisibility_Type()
)
essVisibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essVisibility.setStatus("mandatory")


class _EssVisibilitySituation_Type(Integer32):
    """Custom type essVisibilitySituation based on Integer32"""
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
          ("unknown", 2),
          ("clear", 3),
          ("fogNotPatchy", 4),
          ("patchyFog", 5),
          ("blowingSnow", 6),
          ("smoke", 7),
          ("seaSpray", 8),
          ("vehicleSpray", 9),
          ("blowingDustOrSand", 10),
          ("sunGlare", 11),
          ("swarmsOfInsects", 12))
    )


_EssVisibilitySituation_Type.__name__ = "Integer32"
_EssVisibilitySituation_Object = MibScalar
essVisibilitySituation = _EssVisibilitySituation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 8, 3),
    _EssVisibilitySituation_Type()
)
essVisibilitySituation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essVisibilitySituation.setStatus("mandatory")
_EssNtcipPavement_ObjectIdentity = ObjectIdentity
essNtcipPavement = _EssNtcipPavement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9)
)


class _NumEssPavementSensors_Type(Integer32):
    """Custom type numEssPavementSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumEssPavementSensors_Type.__name__ = "Integer32"
_NumEssPavementSensors_Object = MibScalar
numEssPavementSensors = _NumEssPavementSensors_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 1),
    _NumEssPavementSensors_Type()
)
numEssPavementSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEssPavementSensors.setStatus("mandatory")
_EssPavementSensorTable_Object = MibTable
essPavementSensorTable = _EssPavementSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2)
)
if mibBuilder.loadTexts:
    essPavementSensorTable.setStatus("mandatory")
_EssPavementSensorEntry_Object = MibTableRow
essPavementSensorEntry = _EssPavementSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1)
)
essPavementSensorEntry.setIndexNames(
    (0, "ESS-MIB", "essPavementSensorIndex"),
)
if mibBuilder.loadTexts:
    essPavementSensorEntry.setStatus("mandatory")


class _EssPavementSensorIndex_Type(Integer32):
    """Custom type essPavementSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EssPavementSensorIndex_Type.__name__ = "Integer32"
_EssPavementSensorIndex_Object = MibTableColumn
essPavementSensorIndex = _EssPavementSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 1),
    _EssPavementSensorIndex_Type()
)
essPavementSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPavementSensorIndex.setStatus("mandatory")


class _EssPavementSensorLocation_Type(DisplayString):
    """Custom type essPavementSensorLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EssPavementSensorLocation_Type.__name__ = "DisplayString"
_EssPavementSensorLocation_Object = MibTableColumn
essPavementSensorLocation = _EssPavementSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 2),
    _EssPavementSensorLocation_Type()
)
essPavementSensorLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essPavementSensorLocation.setStatus("mandatory")


class _EssPavementType_Type(Integer32):
    """Custom type essPavementType based on Integer32"""
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
          ("unknown", 2),
          ("asphalt", 3),
          ("openGradedAsphalt", 4),
          ("concrete", 5),
          ("steelBridge", 6),
          ("concreteBridge", 7),
          ("asphaltOverlayBridge", 8),
          ("timberBridge", 9))
    )


_EssPavementType_Type.__name__ = "Integer32"
_EssPavementType_Object = MibTableColumn
essPavementType = _EssPavementType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 3),
    _EssPavementType_Type()
)
essPavementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essPavementType.setStatus("mandatory")


class _EssPavementElevation_Type(Integer32):
    """Custom type essPavementElevation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssPavementElevation_Type.__name__ = "Integer32"
_EssPavementElevation_Object = MibTableColumn
essPavementElevation = _EssPavementElevation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 4),
    _EssPavementElevation_Type()
)
essPavementElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPavementElevation.setStatus("mandatory")


class _EssPavementExposure_Type(Integer32):
    """Custom type essPavementExposure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EssPavementExposure_Type.__name__ = "Integer32"
_EssPavementExposure_Object = MibTableColumn
essPavementExposure = _EssPavementExposure_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 5),
    _EssPavementExposure_Type()
)
essPavementExposure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essPavementExposure.setStatus("mandatory")


class _EssPavementSensorType_Type(Integer32):
    """Custom type essPavementSensorType based on Integer32"""
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
          ("contactPassive", 2),
          ("contactActive", 3),
          ("infrared", 4),
          ("radar", 5),
          ("vibrating", 6),
          ("microwave", 7))
    )


_EssPavementSensorType_Type.__name__ = "Integer32"
_EssPavementSensorType_Object = MibTableColumn
essPavementSensorType = _EssPavementSensorType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 6),
    _EssPavementSensorType_Type()
)
essPavementSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPavementSensorType.setStatus("mandatory")


class _EssSurfaceStatus_Type(Integer32):
    """Custom type essSurfaceStatus based on Integer32"""
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
          ("error", 2),
          ("dry", 3),
          ("traceMoisture", 4),
          ("wet", 5),
          ("chemicallyWet", 6),
          ("iceWarning", 7),
          ("iceWatch", 8),
          ("snowWarning", 9),
          ("snowWatch", 10),
          ("absorption", 11),
          ("dew", 12),
          ("frost", 13),
          ("absorptionAtDewpoint", 14))
    )


_EssSurfaceStatus_Type.__name__ = "Integer32"
_EssSurfaceStatus_Object = MibTableColumn
essSurfaceStatus = _EssSurfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 7),
    _EssSurfaceStatus_Type()
)
essSurfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceStatus.setStatus("mandatory")


class _EssSurfaceTemperature_Type(Integer32):
    """Custom type essSurfaceTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssSurfaceTemperature_Type.__name__ = "Integer32"
_EssSurfaceTemperature_Object = MibTableColumn
essSurfaceTemperature = _EssSurfaceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 8),
    _EssSurfaceTemperature_Type()
)
essSurfaceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceTemperature.setStatus("mandatory")


class _EssPavementTemperature_Type(Integer32):
    """Custom type essPavementTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssPavementTemperature_Type.__name__ = "Integer32"
_EssPavementTemperature_Object = MibTableColumn
essPavementTemperature = _EssPavementTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 9),
    _EssPavementTemperature_Type()
)
essPavementTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPavementTemperature.setStatus("mandatory")


class _EssSurfaceWaterDepth_Type(Integer32):
    """Custom type essSurfaceWaterDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssSurfaceWaterDepth_Type.__name__ = "Integer32"
_EssSurfaceWaterDepth_Object = MibTableColumn
essSurfaceWaterDepth = _EssSurfaceWaterDepth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 10),
    _EssSurfaceWaterDepth_Type()
)
essSurfaceWaterDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceWaterDepth.setStatus("mandatory")


class _EssSurfaceSalinity_Type(Integer32):
    """Custom type essSurfaceSalinity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssSurfaceSalinity_Type.__name__ = "Integer32"
_EssSurfaceSalinity_Object = MibTableColumn
essSurfaceSalinity = _EssSurfaceSalinity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 11),
    _EssSurfaceSalinity_Type()
)
essSurfaceSalinity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceSalinity.setStatus("optional")


class _EssSurfaceConductivity_Type(Integer32):
    """Custom type essSurfaceConductivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssSurfaceConductivity_Type.__name__ = "Integer32"
_EssSurfaceConductivity_Object = MibTableColumn
essSurfaceConductivity = _EssSurfaceConductivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 12),
    _EssSurfaceConductivity_Type()
)
essSurfaceConductivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceConductivity.setStatus("optional")


class _EssSurfaceFreezePoint_Type(Integer32):
    """Custom type essSurfaceFreezePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssSurfaceFreezePoint_Type.__name__ = "Integer32"
_EssSurfaceFreezePoint_Object = MibTableColumn
essSurfaceFreezePoint = _EssSurfaceFreezePoint_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 13),
    _EssSurfaceFreezePoint_Type()
)
essSurfaceFreezePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceFreezePoint.setStatus("mandatory")


class _EssSurfaceBlackIceSignal_Type(Integer32):
    """Custom type essSurfaceBlackIceSignal based on Integer32"""
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
          ("noIce", 2),
          ("blackIce", 3),
          ("detectorError", 4))
    )


_EssSurfaceBlackIceSignal_Type.__name__ = "Integer32"
_EssSurfaceBlackIceSignal_Object = MibTableColumn
essSurfaceBlackIceSignal = _EssSurfaceBlackIceSignal_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 14),
    _EssSurfaceBlackIceSignal_Type()
)
essSurfaceBlackIceSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSurfaceBlackIceSignal.setStatus("mandatory")


class _EssPavementSensorError_Type(Integer32):
    """Custom type essPavementSensorError based on Integer32"""
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
          ("noResponse", 3),
          ("cutCable", 4),
          ("shortCircuit", 5),
          ("dirtyLens", 6))
    )


_EssPavementSensorError_Type.__name__ = "Integer32"
_EssPavementSensorError_Object = MibTableColumn
essPavementSensorError = _EssPavementSensorError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 2, 1, 15),
    _EssPavementSensorError_Type()
)
essPavementSensorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPavementSensorError.setStatus("mandatory")


class _NumEssSubSurfaceSensors_Type(Integer32):
    """Custom type numEssSubSurfaceSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumEssSubSurfaceSensors_Type.__name__ = "Integer32"
_NumEssSubSurfaceSensors_Object = MibScalar
numEssSubSurfaceSensors = _NumEssSubSurfaceSensors_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 3),
    _NumEssSubSurfaceSensors_Type()
)
numEssSubSurfaceSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEssSubSurfaceSensors.setStatus("mandatory")
_EssSubSurfaceSensorTable_Object = MibTable
essSubSurfaceSensorTable = _EssSubSurfaceSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4)
)
if mibBuilder.loadTexts:
    essSubSurfaceSensorTable.setStatus("mandatory")
_EssSubSurfaceSensorEntry_Object = MibTableRow
essSubSurfaceSensorEntry = _EssSubSurfaceSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1)
)
essSubSurfaceSensorEntry.setIndexNames(
    (0, "ESS-MIB", "essSubSurfaceSensorIndex"),
)
if mibBuilder.loadTexts:
    essSubSurfaceSensorEntry.setStatus("mandatory")


class _EssSubSurfaceSensorIndex_Type(Integer32):
    """Custom type essSubSurfaceSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EssSubSurfaceSensorIndex_Type.__name__ = "Integer32"
_EssSubSurfaceSensorIndex_Object = MibTableColumn
essSubSurfaceSensorIndex = _EssSubSurfaceSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 1),
    _EssSubSurfaceSensorIndex_Type()
)
essSubSurfaceSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSubSurfaceSensorIndex.setStatus("mandatory")


class _EssSubSurfaceSensorLocation_Type(DisplayString):
    """Custom type essSubSurfaceSensorLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EssSubSurfaceSensorLocation_Type.__name__ = "DisplayString"
_EssSubSurfaceSensorLocation_Object = MibTableColumn
essSubSurfaceSensorLocation = _EssSubSurfaceSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 2),
    _EssSubSurfaceSensorLocation_Type()
)
essSubSurfaceSensorLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essSubSurfaceSensorLocation.setStatus("mandatory")


class _EssSubSurfaceType_Type(Integer32):
    """Custom type essSubSurfaceType based on Integer32"""
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
          ("unknown", 2),
          ("concrete", 3),
          ("asphalt", 4),
          ("openGradedAsphalt", 5),
          ("gravel", 6),
          ("clay", 7),
          ("loam", 8),
          ("sand", 9),
          ("permafrost", 10),
          ("variousAggregates", 11),
          ("air", 12))
    )


_EssSubSurfaceType_Type.__name__ = "Integer32"
_EssSubSurfaceType_Object = MibTableColumn
essSubSurfaceType = _EssSubSurfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 3),
    _EssSubSurfaceType_Type()
)
essSubSurfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essSubSurfaceType.setStatus("mandatory")


class _EssSubSurfaceSensorDepth_Type(Integer32):
    """Custom type essSubSurfaceSensorDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1001),
    )


_EssSubSurfaceSensorDepth_Type.__name__ = "Integer32"
_EssSubSurfaceSensorDepth_Object = MibTableColumn
essSubSurfaceSensorDepth = _EssSubSurfaceSensorDepth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 4),
    _EssSubSurfaceSensorDepth_Type()
)
essSubSurfaceSensorDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    essSubSurfaceSensorDepth.setStatus("mandatory")


class _EssSubSurfaceTemperature_Type(Integer32):
    """Custom type essSubSurfaceTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1001),
    )


_EssSubSurfaceTemperature_Type.__name__ = "Integer32"
_EssSubSurfaceTemperature_Object = MibTableColumn
essSubSurfaceTemperature = _EssSubSurfaceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 5),
    _EssSubSurfaceTemperature_Type()
)
essSubSurfaceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSubSurfaceTemperature.setStatus("mandatory")


class _EssSubSurfaceMoisture_Type(Integer32):
    """Custom type essSubSurfaceMoisture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EssSubSurfaceMoisture_Type.__name__ = "Integer32"
_EssSubSurfaceMoisture_Object = MibTableColumn
essSubSurfaceMoisture = _EssSubSurfaceMoisture_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 7),
    _EssSubSurfaceMoisture_Type()
)
essSubSurfaceMoisture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSubSurfaceMoisture.setStatus("mandatory")


class _EssSubSurfaceSensorError_Type(Integer32):
    """Custom type essSubSurfaceSensorError based on Integer32"""
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
          ("noResponse", 3),
          ("cutCable", 4),
          ("shortCircuit", 5))
    )


_EssSubSurfaceSensorError_Type.__name__ = "Integer32"
_EssSubSurfaceSensorError_Object = MibTableColumn
essSubSurfaceSensorError = _EssSubSurfaceSensorError_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 9, 4, 1, 8),
    _EssSubSurfaceSensorError_Type()
)
essSubSurfaceSensorError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSubSurfaceSensorError.setStatus("mandatory")
_EssNtcipMobile_ObjectIdentity = ObjectIdentity
essNtcipMobile = _EssNtcipMobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 10)
)


class _EssMobileFriction_Type(Integer32):
    """Custom type essMobileFriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_EssMobileFriction_Type.__name__ = "Integer32"
_EssMobileFriction_Object = MibScalar
essMobileFriction = _EssMobileFriction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 10, 1),
    _EssMobileFriction_Type()
)
essMobileFriction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMobileFriction.setStatus("mandatory")


class _EssMobileObservationGroundState_Type(Integer32):
    """Custom type essMobileObservationGroundState based on Integer32"""
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
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dry", 2),
          ("moist", 3),
          ("wet", 4),
          ("flooded", 5),
          ("frozen", 6),
          ("glaze", 7),
          ("dustySandy", 8),
          ("veryDry", 9),
          ("icy", 10),
          ("patchyWetSnow", 11),
          ("moderateWetSnowCover", 12),
          ("fullWetSnowCover", 13),
          ("patchyDrySnow", 14),
          ("moderateDrySnowCover", 15),
          ("fullDrySnowCover", 16),
          ("driftingSnow", 17),
          ("unknown", 18))
    )


_EssMobileObservationGroundState_Type.__name__ = "Integer32"
_EssMobileObservationGroundState_Object = MibScalar
essMobileObservationGroundState = _EssMobileObservationGroundState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 10, 2),
    _EssMobileObservationGroundState_Type()
)
essMobileObservationGroundState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMobileObservationGroundState.setStatus("mandatory")


class _EssMobileObservationPavement_Type(Integer32):
    """Custom type essMobileObservationPavement based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dry", 2),
          ("wet", 3),
          ("puddles", 4),
          ("shallowStandingWater", 5),
          ("shallowFlowingWater", 6),
          ("deepStandingWater", 7),
          ("deepFlowingWater", 8),
          ("dustingFreshSnow", 9),
          ("moderateFreshSnow", 10),
          ("deepFreshSnow", 11),
          ("plowedSnow", 12),
          ("slush", 13),
          ("packedSnowPatches", 14),
          ("packedSnow", 15),
          ("lightSnowDrifts", 16),
          ("moderateSnowDrifts", 17),
          ("heavySnowDrifts", 18),
          ("frost", 19),
          ("icePatches", 20),
          ("moderatelyIcy", 21),
          ("heavyIcing", 22),
          ("blackIce", 23),
          ("sheetIce", 24),
          ("frozenSlush", 25))
    )


_EssMobileObservationPavement_Type.__name__ = "Integer32"
_EssMobileObservationPavement_Object = MibScalar
essMobileObservationPavement = _EssMobileObservationPavement_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 10, 3),
    _EssMobileObservationPavement_Type()
)
essMobileObservationPavement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essMobileObservationPavement.setStatus("mandatory")
_EssNtcipTreatment_ObjectIdentity = ObjectIdentity
essNtcipTreatment = _EssNtcipTreatment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11)
)


class _NumEssTreatments_Type(Integer32):
    """Custom type numEssTreatments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumEssTreatments_Type.__name__ = "Integer32"
_NumEssTreatments_Object = MibScalar
numEssTreatments = _NumEssTreatments_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 1),
    _NumEssTreatments_Type()
)
numEssTreatments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEssTreatments.setStatus("mandatory")
_EssPavementTreatmentTable_Object = MibTable
essPavementTreatmentTable = _EssPavementTreatmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 2)
)
if mibBuilder.loadTexts:
    essPavementTreatmentTable.setStatus("mandatory")
_EssPavementTreatmentEntry_Object = MibTableRow
essPavementTreatmentEntry = _EssPavementTreatmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 2, 1)
)
essPavementTreatmentEntry.setIndexNames(
    (0, "ESS-MIB", "essPavementTreatmentIndex"),
)
if mibBuilder.loadTexts:
    essPavementTreatmentEntry.setStatus("mandatory")


class _EssPavementTreatmentIndex_Type(Integer32):
    """Custom type essPavementTreatmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EssPavementTreatmentIndex_Type.__name__ = "Integer32"
_EssPavementTreatmentIndex_Object = MibTableColumn
essPavementTreatmentIndex = _EssPavementTreatmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 2, 1, 1),
    _EssPavementTreatmentIndex_Type()
)
essPavementTreatmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPavementTreatmentIndex.setStatus("mandatory")


class _EssPaveTreatProductType_Type(Integer32):
    """Custom type essPaveTreatProductType based on Integer32"""
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
          ("sand", 2),
          ("dirt", 3),
          ("gravel", 4),
          ("cinders", 5),
          ("water", 6),
          ("enhancedSalts", 7),
          ("naCl", 8),
          ("caCl", 9),
          ("mgCl", 10),
          ("cMA", 11),
          ("kAC", 12),
          ("naFormate", 13),
          ("naA", 14))
    )


_EssPaveTreatProductType_Type.__name__ = "Integer32"
_EssPaveTreatProductType_Object = MibTableColumn
essPaveTreatProductType = _EssPaveTreatProductType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 2, 1, 2),
    _EssPaveTreatProductType_Type()
)
essPaveTreatProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPaveTreatProductType.setStatus("mandatory")


class _EssPaveTreatProductForm_Type(Integer32):
    """Custom type essPaveTreatProductForm based on Integer32"""
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
          ("dry", 2),
          ("prewet", 3),
          ("liquid", 4))
    )


_EssPaveTreatProductForm_Type.__name__ = "Integer32"
_EssPaveTreatProductForm_Object = MibTableColumn
essPaveTreatProductForm = _EssPaveTreatProductForm_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 2, 1, 3),
    _EssPaveTreatProductForm_Type()
)
essPaveTreatProductForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPaveTreatProductForm.setStatus("mandatory")


class _EssPercentProductMix_Type(Integer32):
    """Custom type essPercentProductMix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EssPercentProductMix_Type.__name__ = "Integer32"
_EssPercentProductMix_Object = MibTableColumn
essPercentProductMix = _EssPercentProductMix_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 2, 1, 4),
    _EssPercentProductMix_Type()
)
essPercentProductMix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPercentProductMix.setStatus("mandatory")


class _EssPaveTreatmentAmount_Type(Integer32):
    """Custom type essPaveTreatmentAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssPaveTreatmentAmount_Type.__name__ = "Integer32"
_EssPaveTreatmentAmount_Object = MibScalar
essPaveTreatmentAmount = _EssPaveTreatmentAmount_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 3),
    _EssPaveTreatmentAmount_Type()
)
essPaveTreatmentAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPaveTreatmentAmount.setStatus("mandatory")


class _EssPaveTreatmentWidth_Type(Integer32):
    """Custom type essPaveTreatmentWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssPaveTreatmentWidth_Type.__name__ = "Integer32"
_EssPaveTreatmentWidth_Object = MibScalar
essPaveTreatmentWidth = _EssPaveTreatmentWidth_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 11, 4),
    _EssPaveTreatmentWidth_Type()
)
essPaveTreatmentWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPaveTreatmentWidth.setStatus("mandatory")
_EssNtcipAirQuality_ObjectIdentity = ObjectIdentity
essNtcipAirQuality = _EssNtcipAirQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12)
)


class _EssCO_Type(Integer32):
    """Custom type essCO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssCO_Type.__name__ = "Integer32"
_EssCO_Object = MibScalar
essCO = _EssCO_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 1),
    _EssCO_Type()
)
essCO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essCO.setStatus("mandatory")


class _EssCO2_Type(Integer32):
    """Custom type essCO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssCO2_Type.__name__ = "Integer32"
_EssCO2_Object = MibScalar
essCO2 = _EssCO2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 2),
    _EssCO2_Type()
)
essCO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essCO2.setStatus("mandatory")


class _EssNO_Type(Integer32):
    """Custom type essNO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssNO_Type.__name__ = "Integer32"
_EssNO_Object = MibScalar
essNO = _EssNO_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 3),
    _EssNO_Type()
)
essNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essNO.setStatus("mandatory")


class _EssNO2_Type(Integer32):
    """Custom type essNO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssNO2_Type.__name__ = "Integer32"
_EssNO2_Object = MibScalar
essNO2 = _EssNO2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 4),
    _EssNO2_Type()
)
essNO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essNO2.setStatus("mandatory")


class _EssSO2_Type(Integer32):
    """Custom type essSO2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssSO2_Type.__name__ = "Integer32"
_EssSO2_Object = MibScalar
essSO2 = _EssSO2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 5),
    _EssSO2_Type()
)
essSO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essSO2.setStatus("mandatory")


class _EssO3_Type(Integer32):
    """Custom type essO3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssO3_Type.__name__ = "Integer32"
_EssO3_Object = MibScalar
essO3 = _EssO3_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 6),
    _EssO3_Type()
)
essO3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essO3.setStatus("mandatory")


class _EssPM10_Type(Integer32):
    """Custom type essPM10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EssPM10_Type.__name__ = "Integer32"
_EssPM10_Object = MibScalar
essPM10 = _EssPM10_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 12, 7),
    _EssPM10_Type()
)
essPM10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essPM10.setStatus("mandatory")
_EssNtcipWaterQuality_ObjectIdentity = ObjectIdentity
essNtcipWaterQuality = _EssNtcipWaterQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 2, 13)
)
_EssNtcipLocation_ObjectIdentity = ObjectIdentity
essNtcipLocation = _EssNtcipLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 3)
)


class _EssLatitude_Type(Integer32):
    """Custom type essLatitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000001),
    )


_EssLatitude_Type.__name__ = "Integer32"
_EssLatitude_Object = MibScalar
essLatitude = _EssLatitude_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 3, 1),
    _EssLatitude_Type()
)
essLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essLatitude.setStatus("mandatory")


class _EssLongitude_Type(Integer32):
    """Custom type essLongitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000001),
    )


_EssLongitude_Type.__name__ = "Integer32"
_EssLongitude_Object = MibScalar
essLongitude = _EssLongitude_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 3, 2),
    _EssLongitude_Type()
)
essLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essLongitude.setStatus("mandatory")


class _EssVehicleSpeed_Type(Integer32):
    """Custom type essVehicleSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EssVehicleSpeed_Type.__name__ = "Integer32"
_EssVehicleSpeed_Object = MibScalar
essVehicleSpeed = _EssVehicleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 3, 3),
    _EssVehicleSpeed_Type()
)
essVehicleSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essVehicleSpeed.setStatus("mandatory")


class _EssVehicleBearing_Type(Integer32):
    """Custom type essVehicleBearing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 361),
    )


_EssVehicleBearing_Type.__name__ = "Integer32"
_EssVehicleBearing_Object = MibScalar
essVehicleBearing = _EssVehicleBearing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 3, 4),
    _EssVehicleBearing_Type()
)
essVehicleBearing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essVehicleBearing.setStatus("mandatory")
_EssOdometer_Type = Counter32
_EssOdometer_Object = MibScalar
essOdometer = _EssOdometer_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 5, 3, 5),
    _EssOdometer_Type()
)
essOdometer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    essOdometer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESS-MIB",
    **{"ess": ess,
       "essBufr": essBufr,
       "essBufrInstrumentation": essBufrInstrumentation,
       "essTypeofStation": essTypeofStation,
       "essBufrLocationVertical": essBufrLocationVertical,
       "essAtmosphericPressure": essAtmosphericPressure,
       "essBufrWind": essBufrWind,
       "essAvgWindDirection": essAvgWindDirection,
       "essAvgWindSpeed": essAvgWindSpeed,
       "essMaxWindGustSpeed": essMaxWindGustSpeed,
       "essMaxWindGustDir": essMaxWindGustDir,
       "essBufrPrecip": essBufrPrecip,
       "essRelativeHumidity": essRelativeHumidity,
       "essPrecipRate": essPrecipRate,
       "essSnowfallAccumRate": essSnowfallAccumRate,
       "essPrecipitationOneHour": essPrecipitationOneHour,
       "essPrecipitationThreeHours": essPrecipitationThreeHours,
       "essPrecipitationSixHours": essPrecipitationSixHours,
       "essPrecipitationTwelveHours": essPrecipitationTwelveHours,
       "essPrecipitation24Hours": essPrecipitation24Hours,
       "essBufrRadiation": essBufrRadiation,
       "essSolarRadiation": essSolarRadiation,
       "essTotalSun": essTotalSun,
       "essNtcip": essNtcip,
       "essNtcipIdentification": essNtcipIdentification,
       "essNtcipNum": essNtcipNum,
       "essNtcipCategory": essNtcipCategory,
       "essNtcipSiteDescription": essNtcipSiteDescription,
       "essNtcipHeight": essNtcipHeight,
       "essReferenceHeight": essReferenceHeight,
       "essPressureHeight": essPressureHeight,
       "essWindSensorHeight": essWindSensorHeight,
       "essNtcipWind": essNtcipWind,
       "essSpotWindDirection": essSpotWindDirection,
       "essSpotWindSpeed": essSpotWindSpeed,
       "essWindSituation": essWindSituation,
       "essNtcipTemperature": essNtcipTemperature,
       "essNumTemperatureSensors": essNumTemperatureSensors,
       "essTemperatureSensorTable": essTemperatureSensorTable,
       "essTemperatureSensorEntry": essTemperatureSensorEntry,
       "essTemperatureSensorIndex": essTemperatureSensorIndex,
       "essTemperatureSensorHeight": essTemperatureSensorHeight,
       "essAirTemperature": essAirTemperature,
       "essWetbulbTemp": essWetbulbTemp,
       "essDewpointTemp": essDewpointTemp,
       "essMaxTemp": essMaxTemp,
       "essMinTemp": essMinTemp,
       "essNtcipPrecip": essNtcipPrecip,
       "essWaterDepth": essWaterDepth,
       "essAdjacentSnowDepth": essAdjacentSnowDepth,
       "essRoadwaySnowDepth": essRoadwaySnowDepth,
       "essRoadwaySnowPackDepth": essRoadwaySnowPackDepth,
       "essPrecipYesNo": essPrecipYesNo,
       "essPrecipSituation": essPrecipSituation,
       "essIceThickness": essIceThickness,
       "essPrecipitationStartTime": essPrecipitationStartTime,
       "essPrecipitationEndTime": essPrecipitationEndTime,
       "essNtcipRadiation": essNtcipRadiation,
       "essCloudSituation": essCloudSituation,
       "essNtcipVisibility": essNtcipVisibility,
       "essVisibility": essVisibility,
       "essVisibilitySituation": essVisibilitySituation,
       "essNtcipPavement": essNtcipPavement,
       "numEssPavementSensors": numEssPavementSensors,
       "essPavementSensorTable": essPavementSensorTable,
       "essPavementSensorEntry": essPavementSensorEntry,
       "essPavementSensorIndex": essPavementSensorIndex,
       "essPavementSensorLocation": essPavementSensorLocation,
       "essPavementType": essPavementType,
       "essPavementElevation": essPavementElevation,
       "essPavementExposure": essPavementExposure,
       "essPavementSensorType": essPavementSensorType,
       "essSurfaceStatus": essSurfaceStatus,
       "essSurfaceTemperature": essSurfaceTemperature,
       "essPavementTemperature": essPavementTemperature,
       "essSurfaceWaterDepth": essSurfaceWaterDepth,
       "essSurfaceSalinity": essSurfaceSalinity,
       "essSurfaceConductivity": essSurfaceConductivity,
       "essSurfaceFreezePoint": essSurfaceFreezePoint,
       "essSurfaceBlackIceSignal": essSurfaceBlackIceSignal,
       "essPavementSensorError": essPavementSensorError,
       "numEssSubSurfaceSensors": numEssSubSurfaceSensors,
       "essSubSurfaceSensorTable": essSubSurfaceSensorTable,
       "essSubSurfaceSensorEntry": essSubSurfaceSensorEntry,
       "essSubSurfaceSensorIndex": essSubSurfaceSensorIndex,
       "essSubSurfaceSensorLocation": essSubSurfaceSensorLocation,
       "essSubSurfaceType": essSubSurfaceType,
       "essSubSurfaceSensorDepth": essSubSurfaceSensorDepth,
       "essSubSurfaceTemperature": essSubSurfaceTemperature,
       "essSubSurfaceMoisture": essSubSurfaceMoisture,
       "essSubSurfaceSensorError": essSubSurfaceSensorError,
       "essNtcipMobile": essNtcipMobile,
       "essMobileFriction": essMobileFriction,
       "essMobileObservationGroundState": essMobileObservationGroundState,
       "essMobileObservationPavement": essMobileObservationPavement,
       "essNtcipTreatment": essNtcipTreatment,
       "numEssTreatments": numEssTreatments,
       "essPavementTreatmentTable": essPavementTreatmentTable,
       "essPavementTreatmentEntry": essPavementTreatmentEntry,
       "essPavementTreatmentIndex": essPavementTreatmentIndex,
       "essPaveTreatProductType": essPaveTreatProductType,
       "essPaveTreatProductForm": essPaveTreatProductForm,
       "essPercentProductMix": essPercentProductMix,
       "essPaveTreatmentAmount": essPaveTreatmentAmount,
       "essPaveTreatmentWidth": essPaveTreatmentWidth,
       "essNtcipAirQuality": essNtcipAirQuality,
       "essCO": essCO,
       "essCO2": essCO2,
       "essNO": essNO,
       "essNO2": essNO2,
       "essSO2": essSO2,
       "essO3": essO3,
       "essPM10": essPM10,
       "essNtcipWaterQuality": essNtcipWaterQuality,
       "essNtcipLocation": essNtcipLocation,
       "essLatitude": essLatitude,
       "essLongitude": essLongitude,
       "essVehicleSpeed": essVehicleSpeed,
       "essVehicleBearing": essVehicleBearing,
       "essOdometer": essOdometer}
)
