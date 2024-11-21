# SNMP MIB module (ASC_MIB1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1202ASC.mib
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

(devices,) = mibBuilder.importSymbols(
    "TMIB-II",
    "devices")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asc_ObjectIdentity = ObjectIdentity
asc = _Asc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1)
)
_Phase_ObjectIdentity = ObjectIdentity
phase = _Phase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1)
)


class _MaxPhases_Type(Integer32):
    """Custom type maxPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxPhases_Type.__name__ = "Integer32"
_MaxPhases_Object = MibScalar
maxPhases = _MaxPhases_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 1),
    _MaxPhases_Type()
)
maxPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPhases.setStatus("mandatory")
_PhaseTable_Object = MibTable
phaseTable = _PhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    phaseTable.setStatus("mandatory")
_PhaseEntry_Object = MibTableRow
phaseEntry = _PhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1)
)
phaseEntry.setIndexNames(
    (0, "ASC_MIB1", "phaseNumber"),
)
if mibBuilder.loadTexts:
    phaseEntry.setStatus("mandatory")


class _PhaseNumber_Type(Integer32):
    """Custom type phaseNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhaseNumber_Type.__name__ = "Integer32"
_PhaseNumber_Object = MibTableColumn
phaseNumber = _PhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 1),
    _PhaseNumber_Type()
)
phaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseNumber.setStatus("mandatory")


class _PhaseWalk_Type(Integer32):
    """Custom type phaseWalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseWalk_Type.__name__ = "Integer32"
_PhaseWalk_Object = MibTableColumn
phaseWalk = _PhaseWalk_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 2),
    _PhaseWalk_Type()
)
phaseWalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseWalk.setStatus("mandatory")


class _PhasePedestrianClear_Type(Integer32):
    """Custom type phasePedestrianClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhasePedestrianClear_Type.__name__ = "Integer32"
_PhasePedestrianClear_Object = MibTableColumn
phasePedestrianClear = _PhasePedestrianClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 3),
    _PhasePedestrianClear_Type()
)
phasePedestrianClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phasePedestrianClear.setStatus("mandatory")


class _PhaseMinimumGreen_Type(Integer32):
    """Custom type phaseMinimumGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseMinimumGreen_Type.__name__ = "Integer32"
_PhaseMinimumGreen_Object = MibTableColumn
phaseMinimumGreen = _PhaseMinimumGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 4),
    _PhaseMinimumGreen_Type()
)
phaseMinimumGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseMinimumGreen.setStatus("mandatory")


class _PhasePassage_Type(Integer32):
    """Custom type phasePassage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhasePassage_Type.__name__ = "Integer32"
_PhasePassage_Object = MibTableColumn
phasePassage = _PhasePassage_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 5),
    _PhasePassage_Type()
)
phasePassage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phasePassage.setStatus("mandatory")


class _PhaseMaximum1_Type(Integer32):
    """Custom type phaseMaximum1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseMaximum1_Type.__name__ = "Integer32"
_PhaseMaximum1_Object = MibTableColumn
phaseMaximum1 = _PhaseMaximum1_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 6),
    _PhaseMaximum1_Type()
)
phaseMaximum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseMaximum1.setStatus("mandatory")


class _PhaseMaximum2_Type(Integer32):
    """Custom type phaseMaximum2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseMaximum2_Type.__name__ = "Integer32"
_PhaseMaximum2_Object = MibTableColumn
phaseMaximum2 = _PhaseMaximum2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 7),
    _PhaseMaximum2_Type()
)
phaseMaximum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseMaximum2.setStatus("mandatory")


class _PhaseYellowChange_Type(Integer32):
    """Custom type phaseYellowChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseYellowChange_Type.__name__ = "Integer32"
_PhaseYellowChange_Object = MibTableColumn
phaseYellowChange = _PhaseYellowChange_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 8),
    _PhaseYellowChange_Type()
)
phaseYellowChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseYellowChange.setStatus("mandatory")


class _PhaseRedClear_Type(Integer32):
    """Custom type phaseRedClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseRedClear_Type.__name__ = "Integer32"
_PhaseRedClear_Object = MibTableColumn
phaseRedClear = _PhaseRedClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 9),
    _PhaseRedClear_Type()
)
phaseRedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseRedClear.setStatus("mandatory")


class _PhaseRedRevert_Type(Integer32):
    """Custom type phaseRedRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseRedRevert_Type.__name__ = "Integer32"
_PhaseRedRevert_Object = MibTableColumn
phaseRedRevert = _PhaseRedRevert_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 10),
    _PhaseRedRevert_Type()
)
phaseRedRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseRedRevert.setStatus("optional")


class _PhaseAddedInitial_Type(Integer32):
    """Custom type phaseAddedInitial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseAddedInitial_Type.__name__ = "Integer32"
_PhaseAddedInitial_Object = MibTableColumn
phaseAddedInitial = _PhaseAddedInitial_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 11),
    _PhaseAddedInitial_Type()
)
phaseAddedInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseAddedInitial.setStatus("mandatory")


class _PhaseMaximumInitial_Type(Integer32):
    """Custom type phaseMaximumInitial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseMaximumInitial_Type.__name__ = "Integer32"
_PhaseMaximumInitial_Object = MibTableColumn
phaseMaximumInitial = _PhaseMaximumInitial_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 12),
    _PhaseMaximumInitial_Type()
)
phaseMaximumInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseMaximumInitial.setStatus("mandatory")


class _PhaseTimeBeforeReduction_Type(Integer32):
    """Custom type phaseTimeBeforeReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseTimeBeforeReduction_Type.__name__ = "Integer32"
_PhaseTimeBeforeReduction_Object = MibTableColumn
phaseTimeBeforeReduction = _PhaseTimeBeforeReduction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 13),
    _PhaseTimeBeforeReduction_Type()
)
phaseTimeBeforeReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseTimeBeforeReduction.setStatus("mandatory")


class _PhaseCarsBeforeReduction_Type(Integer32):
    """Custom type phaseCarsBeforeReduction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseCarsBeforeReduction_Type.__name__ = "Integer32"
_PhaseCarsBeforeReduction_Object = MibTableColumn
phaseCarsBeforeReduction = _PhaseCarsBeforeReduction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 14),
    _PhaseCarsBeforeReduction_Type()
)
phaseCarsBeforeReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseCarsBeforeReduction.setStatus("optional")


class _PhaseTimeToReduce_Type(Integer32):
    """Custom type phaseTimeToReduce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseTimeToReduce_Type.__name__ = "Integer32"
_PhaseTimeToReduce_Object = MibTableColumn
phaseTimeToReduce = _PhaseTimeToReduce_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 15),
    _PhaseTimeToReduce_Type()
)
phaseTimeToReduce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseTimeToReduce.setStatus("mandatory")


class _PhaseReduceBy_Type(Integer32):
    """Custom type phaseReduceBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseReduceBy_Type.__name__ = "Integer32"
_PhaseReduceBy_Object = MibTableColumn
phaseReduceBy = _PhaseReduceBy_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 16),
    _PhaseReduceBy_Type()
)
phaseReduceBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseReduceBy.setStatus("optional")


class _PhaseMinimumGap_Type(Integer32):
    """Custom type phaseMinimumGap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseMinimumGap_Type.__name__ = "Integer32"
_PhaseMinimumGap_Object = MibTableColumn
phaseMinimumGap = _PhaseMinimumGap_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 17),
    _PhaseMinimumGap_Type()
)
phaseMinimumGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseMinimumGap.setStatus("mandatory")


class _PhaseDynamicMaxLimit_Type(Integer32):
    """Custom type phaseDynamicMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseDynamicMaxLimit_Type.__name__ = "Integer32"
_PhaseDynamicMaxLimit_Object = MibTableColumn
phaseDynamicMaxLimit = _PhaseDynamicMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 18),
    _PhaseDynamicMaxLimit_Type()
)
phaseDynamicMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseDynamicMaxLimit.setStatus("optional")


class _PhaseDynamicMaxStep_Type(Integer32):
    """Custom type phaseDynamicMaxStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseDynamicMaxStep_Type.__name__ = "Integer32"
_PhaseDynamicMaxStep_Object = MibTableColumn
phaseDynamicMaxStep = _PhaseDynamicMaxStep_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 19),
    _PhaseDynamicMaxStep_Type()
)
phaseDynamicMaxStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseDynamicMaxStep.setStatus("optional")


class _PhaseStartup_Type(Integer32):
    """Custom type phaseStartup based on Integer32"""
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
          ("phaseNotOn", 2),
          ("greenWalk", 3),
          ("greenNoWalk", 4),
          ("yellowChange", 5),
          ("redClear", 6))
    )


_PhaseStartup_Type.__name__ = "Integer32"
_PhaseStartup_Object = MibTableColumn
phaseStartup = _PhaseStartup_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 20),
    _PhaseStartup_Type()
)
phaseStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseStartup.setStatus("mandatory")


class _PhaseOptions_Type(Integer32):
    """Custom type phaseOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PhaseOptions_Type.__name__ = "Integer32"
_PhaseOptions_Object = MibTableColumn
phaseOptions = _PhaseOptions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 21),
    _PhaseOptions_Type()
)
phaseOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseOptions.setStatus("mandatory")


class _PhaseRing_Type(Integer32):
    """Custom type phaseRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseRing_Type.__name__ = "Integer32"
_PhaseRing_Object = MibTableColumn
phaseRing = _PhaseRing_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 22),
    _PhaseRing_Type()
)
phaseRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseRing.setStatus("mandatory")
_PhaseConcurrency_Type = OctetString
_PhaseConcurrency_Object = MibTableColumn
phaseConcurrency = _PhaseConcurrency_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 2, 1, 23),
    _PhaseConcurrency_Type()
)
phaseConcurrency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseConcurrency.setStatus("mandatory")


class _MaxPhaseGroups_Type(Integer32):
    """Custom type maxPhaseGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MaxPhaseGroups_Type.__name__ = "Integer32"
_MaxPhaseGroups_Object = MibScalar
maxPhaseGroups = _MaxPhaseGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 3),
    _MaxPhaseGroups_Type()
)
maxPhaseGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPhaseGroups.setStatus("mandatory")
_PhaseStatusGroupTable_Object = MibTable
phaseStatusGroupTable = _PhaseStatusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    phaseStatusGroupTable.setStatus("mandatory")
_PhaseStatusGroupEntry_Object = MibTableRow
phaseStatusGroupEntry = _PhaseStatusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1)
)
phaseStatusGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "phaseStatusGroupNumber"),
)
if mibBuilder.loadTexts:
    phaseStatusGroupEntry.setStatus("mandatory")


class _PhaseStatusGroupNumber_Type(Integer32):
    """Custom type phaseStatusGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhaseStatusGroupNumber_Type.__name__ = "Integer32"
_PhaseStatusGroupNumber_Object = MibTableColumn
phaseStatusGroupNumber = _PhaseStatusGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 1),
    _PhaseStatusGroupNumber_Type()
)
phaseStatusGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupNumber.setStatus("mandatory")


class _PhaseStatusGroupReds_Type(Integer32):
    """Custom type phaseStatusGroupReds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupReds_Type.__name__ = "Integer32"
_PhaseStatusGroupReds_Object = MibTableColumn
phaseStatusGroupReds = _PhaseStatusGroupReds_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 2),
    _PhaseStatusGroupReds_Type()
)
phaseStatusGroupReds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupReds.setStatus("mandatory")


class _PhaseStatusGroupYellows_Type(Integer32):
    """Custom type phaseStatusGroupYellows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupYellows_Type.__name__ = "Integer32"
_PhaseStatusGroupYellows_Object = MibTableColumn
phaseStatusGroupYellows = _PhaseStatusGroupYellows_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 3),
    _PhaseStatusGroupYellows_Type()
)
phaseStatusGroupYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupYellows.setStatus("mandatory")


class _PhaseStatusGroupGreens_Type(Integer32):
    """Custom type phaseStatusGroupGreens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupGreens_Type.__name__ = "Integer32"
_PhaseStatusGroupGreens_Object = MibTableColumn
phaseStatusGroupGreens = _PhaseStatusGroupGreens_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 4),
    _PhaseStatusGroupGreens_Type()
)
phaseStatusGroupGreens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupGreens.setStatus("mandatory")


class _PhaseStatusGroupDontWalks_Type(Integer32):
    """Custom type phaseStatusGroupDontWalks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupDontWalks_Type.__name__ = "Integer32"
_PhaseStatusGroupDontWalks_Object = MibTableColumn
phaseStatusGroupDontWalks = _PhaseStatusGroupDontWalks_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 5),
    _PhaseStatusGroupDontWalks_Type()
)
phaseStatusGroupDontWalks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupDontWalks.setStatus("mandatory")


class _PhaseStatusGroupPedClears_Type(Integer32):
    """Custom type phaseStatusGroupPedClears based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupPedClears_Type.__name__ = "Integer32"
_PhaseStatusGroupPedClears_Object = MibTableColumn
phaseStatusGroupPedClears = _PhaseStatusGroupPedClears_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 6),
    _PhaseStatusGroupPedClears_Type()
)
phaseStatusGroupPedClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupPedClears.setStatus("mandatory")


class _PhaseStatusGroupWalks_Type(Integer32):
    """Custom type phaseStatusGroupWalks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupWalks_Type.__name__ = "Integer32"
_PhaseStatusGroupWalks_Object = MibTableColumn
phaseStatusGroupWalks = _PhaseStatusGroupWalks_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 7),
    _PhaseStatusGroupWalks_Type()
)
phaseStatusGroupWalks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupWalks.setStatus("mandatory")


class _PhaseStatusGroupVehCalls_Type(Integer32):
    """Custom type phaseStatusGroupVehCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupVehCalls_Type.__name__ = "Integer32"
_PhaseStatusGroupVehCalls_Object = MibTableColumn
phaseStatusGroupVehCalls = _PhaseStatusGroupVehCalls_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 8),
    _PhaseStatusGroupVehCalls_Type()
)
phaseStatusGroupVehCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupVehCalls.setStatus("mandatory")


class _PhaseStatusGroupPedCalls_Type(Integer32):
    """Custom type phaseStatusGroupPedCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupPedCalls_Type.__name__ = "Integer32"
_PhaseStatusGroupPedCalls_Object = MibTableColumn
phaseStatusGroupPedCalls = _PhaseStatusGroupPedCalls_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 9),
    _PhaseStatusGroupPedCalls_Type()
)
phaseStatusGroupPedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupPedCalls.setStatus("mandatory")


class _PhaseStatusGroupPhaseOns_Type(Integer32):
    """Custom type phaseStatusGroupPhaseOns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupPhaseOns_Type.__name__ = "Integer32"
_PhaseStatusGroupPhaseOns_Object = MibTableColumn
phaseStatusGroupPhaseOns = _PhaseStatusGroupPhaseOns_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 10),
    _PhaseStatusGroupPhaseOns_Type()
)
phaseStatusGroupPhaseOns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupPhaseOns.setStatus("mandatory")


class _PhaseStatusGroupPhaseNexts_Type(Integer32):
    """Custom type phaseStatusGroupPhaseNexts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseStatusGroupPhaseNexts_Type.__name__ = "Integer32"
_PhaseStatusGroupPhaseNexts_Object = MibTableColumn
phaseStatusGroupPhaseNexts = _PhaseStatusGroupPhaseNexts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 4, 1, 11),
    _PhaseStatusGroupPhaseNexts_Type()
)
phaseStatusGroupPhaseNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseStatusGroupPhaseNexts.setStatus("mandatory")
_PhaseControlGroupTable_Object = MibTable
phaseControlGroupTable = _PhaseControlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    phaseControlGroupTable.setStatus("optional")
_PhaseControlGroupEntry_Object = MibTableRow
phaseControlGroupEntry = _PhaseControlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1)
)
phaseControlGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "phaseControlGroupNumber"),
)
if mibBuilder.loadTexts:
    phaseControlGroupEntry.setStatus("mandatory")


class _PhaseControlGroupNumber_Type(Integer32):
    """Custom type phaseControlGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PhaseControlGroupNumber_Type.__name__ = "Integer32"
_PhaseControlGroupNumber_Object = MibTableColumn
phaseControlGroupNumber = _PhaseControlGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 1),
    _PhaseControlGroupNumber_Type()
)
phaseControlGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phaseControlGroupNumber.setStatus("mandatory")


class _PhaseControlGroupPhaseOmit_Type(Integer32):
    """Custom type phaseControlGroupPhaseOmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseControlGroupPhaseOmit_Type.__name__ = "Integer32"
_PhaseControlGroupPhaseOmit_Object = MibTableColumn
phaseControlGroupPhaseOmit = _PhaseControlGroupPhaseOmit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 2),
    _PhaseControlGroupPhaseOmit_Type()
)
phaseControlGroupPhaseOmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseControlGroupPhaseOmit.setStatus("mandatory")


class _PhaseControlGroupPedOmit_Type(Integer32):
    """Custom type phaseControlGroupPedOmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseControlGroupPedOmit_Type.__name__ = "Integer32"
_PhaseControlGroupPedOmit_Object = MibTableColumn
phaseControlGroupPedOmit = _PhaseControlGroupPedOmit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 3),
    _PhaseControlGroupPedOmit_Type()
)
phaseControlGroupPedOmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseControlGroupPedOmit.setStatus("mandatory")


class _PhaseControlGroupHold_Type(Integer32):
    """Custom type phaseControlGroupHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseControlGroupHold_Type.__name__ = "Integer32"
_PhaseControlGroupHold_Object = MibTableColumn
phaseControlGroupHold = _PhaseControlGroupHold_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 4),
    _PhaseControlGroupHold_Type()
)
phaseControlGroupHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseControlGroupHold.setStatus("mandatory")


class _PhaseControlGroupForceOff_Type(Integer32):
    """Custom type phaseControlGroupForceOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseControlGroupForceOff_Type.__name__ = "Integer32"
_PhaseControlGroupForceOff_Object = MibTableColumn
phaseControlGroupForceOff = _PhaseControlGroupForceOff_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 5),
    _PhaseControlGroupForceOff_Type()
)
phaseControlGroupForceOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseControlGroupForceOff.setStatus("optional")


class _PhaseControlGroupVehCall_Type(Integer32):
    """Custom type phaseControlGroupVehCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseControlGroupVehCall_Type.__name__ = "Integer32"
_PhaseControlGroupVehCall_Object = MibTableColumn
phaseControlGroupVehCall = _PhaseControlGroupVehCall_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 6),
    _PhaseControlGroupVehCall_Type()
)
phaseControlGroupVehCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseControlGroupVehCall.setStatus("mandatory")


class _PhaseControlGroupPedCall_Type(Integer32):
    """Custom type phaseControlGroupPedCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PhaseControlGroupPedCall_Type.__name__ = "Integer32"
_PhaseControlGroupPedCall_Object = MibTableColumn
phaseControlGroupPedCall = _PhaseControlGroupPedCall_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 1, 5, 1, 7),
    _PhaseControlGroupPedCall_Type()
)
phaseControlGroupPedCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseControlGroupPedCall.setStatus("mandatory")
_Detector_ObjectIdentity = ObjectIdentity
detector = _Detector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2)
)


class _MaxVehicleDetectors_Type(Integer32):
    """Custom type maxVehicleDetectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxVehicleDetectors_Type.__name__ = "Integer32"
_MaxVehicleDetectors_Object = MibScalar
maxVehicleDetectors = _MaxVehicleDetectors_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 1),
    _MaxVehicleDetectors_Type()
)
maxVehicleDetectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxVehicleDetectors.setStatus("mandatory")
_VehicleDetectorTable_Object = MibTable
vehicleDetectorTable = _VehicleDetectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vehicleDetectorTable.setStatus("mandatory")
_VehicleDetectorEntry_Object = MibTableRow
vehicleDetectorEntry = _VehicleDetectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1)
)
vehicleDetectorEntry.setIndexNames(
    (0, "ASC_MIB1", "vehicleDetectorNumber"),
)
if mibBuilder.loadTexts:
    vehicleDetectorEntry.setStatus("mandatory")


class _VehicleDetectorNumber_Type(Integer32):
    """Custom type vehicleDetectorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VehicleDetectorNumber_Type.__name__ = "Integer32"
_VehicleDetectorNumber_Object = MibTableColumn
vehicleDetectorNumber = _VehicleDetectorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 1),
    _VehicleDetectorNumber_Type()
)
vehicleDetectorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vehicleDetectorNumber.setStatus("mandatory")


class _VehicleDetectorOptions_Type(Integer32):
    """Custom type vehicleDetectorOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorOptions_Type.__name__ = "Integer32"
_VehicleDetectorOptions_Object = MibTableColumn
vehicleDetectorOptions = _VehicleDetectorOptions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 2),
    _VehicleDetectorOptions_Type()
)
vehicleDetectorOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorOptions.setStatus("mandatory")


class _VehicleDetectorCallPhase_Type(Integer32):
    """Custom type vehicleDetectorCallPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorCallPhase_Type.__name__ = "Integer32"
_VehicleDetectorCallPhase_Object = MibTableColumn
vehicleDetectorCallPhase = _VehicleDetectorCallPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 4),
    _VehicleDetectorCallPhase_Type()
)
vehicleDetectorCallPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorCallPhase.setStatus("mandatory")


class _VehicleDetectorSwitchPhase_Type(Integer32):
    """Custom type vehicleDetectorSwitchPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorSwitchPhase_Type.__name__ = "Integer32"
_VehicleDetectorSwitchPhase_Object = MibTableColumn
vehicleDetectorSwitchPhase = _VehicleDetectorSwitchPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 5),
    _VehicleDetectorSwitchPhase_Type()
)
vehicleDetectorSwitchPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorSwitchPhase.setStatus("mandatory")


class _VehicleDetectorDelay_Type(Integer32):
    """Custom type vehicleDetectorDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VehicleDetectorDelay_Type.__name__ = "Integer32"
_VehicleDetectorDelay_Object = MibTableColumn
vehicleDetectorDelay = _VehicleDetectorDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 6),
    _VehicleDetectorDelay_Type()
)
vehicleDetectorDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorDelay.setStatus("mandatory")


class _VehicleDetectorExtend_Type(Integer32):
    """Custom type vehicleDetectorExtend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorExtend_Type.__name__ = "Integer32"
_VehicleDetectorExtend_Object = MibTableColumn
vehicleDetectorExtend = _VehicleDetectorExtend_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 7),
    _VehicleDetectorExtend_Type()
)
vehicleDetectorExtend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorExtend.setStatus("mandatory")


class _VehicleDetectorQueueLimit_Type(Integer32):
    """Custom type vehicleDetectorQueueLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorQueueLimit_Type.__name__ = "Integer32"
_VehicleDetectorQueueLimit_Object = MibTableColumn
vehicleDetectorQueueLimit = _VehicleDetectorQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 8),
    _VehicleDetectorQueueLimit_Type()
)
vehicleDetectorQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorQueueLimit.setStatus("optional")


class _VehicleDetectorNoActivity_Type(Integer32):
    """Custom type vehicleDetectorNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorNoActivity_Type.__name__ = "Integer32"
_VehicleDetectorNoActivity_Object = MibTableColumn
vehicleDetectorNoActivity = _VehicleDetectorNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 9),
    _VehicleDetectorNoActivity_Type()
)
vehicleDetectorNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorNoActivity.setStatus("mandatory")


class _VehicleDetectorMaxPresence_Type(Integer32):
    """Custom type vehicleDetectorMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorMaxPresence_Type.__name__ = "Integer32"
_VehicleDetectorMaxPresence_Object = MibTableColumn
vehicleDetectorMaxPresence = _VehicleDetectorMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 10),
    _VehicleDetectorMaxPresence_Type()
)
vehicleDetectorMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorMaxPresence.setStatus("mandatory")


class _VehicleDetectorErraticCounts_Type(Integer32):
    """Custom type vehicleDetectorErraticCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorErraticCounts_Type.__name__ = "Integer32"
_VehicleDetectorErraticCounts_Object = MibTableColumn
vehicleDetectorErraticCounts = _VehicleDetectorErraticCounts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 11),
    _VehicleDetectorErraticCounts_Type()
)
vehicleDetectorErraticCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorErraticCounts.setStatus("mandatory")


class _VehicleDetectorFailTime_Type(Integer32):
    """Custom type vehicleDetectorFailTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorFailTime_Type.__name__ = "Integer32"
_VehicleDetectorFailTime_Object = MibTableColumn
vehicleDetectorFailTime = _VehicleDetectorFailTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 12),
    _VehicleDetectorFailTime_Type()
)
vehicleDetectorFailTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorFailTime.setStatus("optional")


class _VehicleDetectorAlarms_Type(Integer32):
    """Custom type vehicleDetectorAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorAlarms_Type.__name__ = "Integer32"
_VehicleDetectorAlarms_Object = MibTableColumn
vehicleDetectorAlarms = _VehicleDetectorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 13),
    _VehicleDetectorAlarms_Type()
)
vehicleDetectorAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vehicleDetectorAlarms.setStatus("mandatory")


class _VehicleDetectorReportedAlarms_Type(Integer32):
    """Custom type vehicleDetectorReportedAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorReportedAlarms_Type.__name__ = "Integer32"
_VehicleDetectorReportedAlarms_Object = MibTableColumn
vehicleDetectorReportedAlarms = _VehicleDetectorReportedAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 14),
    _VehicleDetectorReportedAlarms_Type()
)
vehicleDetectorReportedAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vehicleDetectorReportedAlarms.setStatus("optional")


class _VehicleDetectorReset_Type(Integer32):
    """Custom type vehicleDetectorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VehicleDetectorReset_Type.__name__ = "Integer32"
_VehicleDetectorReset_Object = MibTableColumn
vehicleDetectorReset = _VehicleDetectorReset_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 2, 1, 15),
    _VehicleDetectorReset_Type()
)
vehicleDetectorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vehicleDetectorReset.setStatus("mandatory")


class _MaxVehicleDetectorStatusGroups_Type(Integer32):
    """Custom type maxVehicleDetectorStatusGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxVehicleDetectorStatusGroups_Type.__name__ = "Integer32"
_MaxVehicleDetectorStatusGroups_Object = MibScalar
maxVehicleDetectorStatusGroups = _MaxVehicleDetectorStatusGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 3),
    _MaxVehicleDetectorStatusGroups_Type()
)
maxVehicleDetectorStatusGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxVehicleDetectorStatusGroups.setStatus("mandatory")
_VehicleDetectorStatusGroupTable_Object = MibTable
vehicleDetectorStatusGroupTable = _VehicleDetectorStatusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    vehicleDetectorStatusGroupTable.setStatus("mandatory")
_VehicleDetectorStatusGroupEntry_Object = MibTableRow
vehicleDetectorStatusGroupEntry = _VehicleDetectorStatusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 4, 1)
)
vehicleDetectorStatusGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "vehicleDetectorStatusGroupNumber"),
)
if mibBuilder.loadTexts:
    vehicleDetectorStatusGroupEntry.setStatus("mandatory")


class _VehicleDetectorStatusGroupNumber_Type(Integer32):
    """Custom type vehicleDetectorStatusGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VehicleDetectorStatusGroupNumber_Type.__name__ = "Integer32"
_VehicleDetectorStatusGroupNumber_Object = MibTableColumn
vehicleDetectorStatusGroupNumber = _VehicleDetectorStatusGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 4, 1, 1),
    _VehicleDetectorStatusGroupNumber_Type()
)
vehicleDetectorStatusGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vehicleDetectorStatusGroupNumber.setStatus("mandatory")


class _VehicleDetectorStatusGroupActive_Type(Integer32):
    """Custom type vehicleDetectorStatusGroupActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorStatusGroupActive_Type.__name__ = "Integer32"
_VehicleDetectorStatusGroupActive_Object = MibTableColumn
vehicleDetectorStatusGroupActive = _VehicleDetectorStatusGroupActive_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 4, 1, 2),
    _VehicleDetectorStatusGroupActive_Type()
)
vehicleDetectorStatusGroupActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vehicleDetectorStatusGroupActive.setStatus("mandatory")


class _VehicleDetectorStatusGroupAlarms_Type(Integer32):
    """Custom type vehicleDetectorStatusGroupAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VehicleDetectorStatusGroupAlarms_Type.__name__ = "Integer32"
_VehicleDetectorStatusGroupAlarms_Object = MibTableColumn
vehicleDetectorStatusGroupAlarms = _VehicleDetectorStatusGroupAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 4, 1, 3),
    _VehicleDetectorStatusGroupAlarms_Type()
)
vehicleDetectorStatusGroupAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vehicleDetectorStatusGroupAlarms.setStatus("mandatory")
_VolumeOccupancyReport_ObjectIdentity = ObjectIdentity
volumeOccupancyReport = _VolumeOccupancyReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5)
)


class _VolumeOccupancySequence_Type(Integer32):
    """Custom type volumeOccupancySequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VolumeOccupancySequence_Type.__name__ = "Integer32"
_VolumeOccupancySequence_Object = MibScalar
volumeOccupancySequence = _VolumeOccupancySequence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 1),
    _VolumeOccupancySequence_Type()
)
volumeOccupancySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeOccupancySequence.setStatus("mandatory")


class _VolumeOccupancyPeriod_Type(Integer32):
    """Custom type volumeOccupancyPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VolumeOccupancyPeriod_Type.__name__ = "Integer32"
_VolumeOccupancyPeriod_Object = MibScalar
volumeOccupancyPeriod = _VolumeOccupancyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 2),
    _VolumeOccupancyPeriod_Type()
)
volumeOccupancyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    volumeOccupancyPeriod.setStatus("mandatory")


class _ActiveVolumeOccupancyDetectors_Type(Integer32):
    """Custom type activeVolumeOccupancyDetectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ActiveVolumeOccupancyDetectors_Type.__name__ = "Integer32"
_ActiveVolumeOccupancyDetectors_Object = MibScalar
activeVolumeOccupancyDetectors = _ActiveVolumeOccupancyDetectors_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 3),
    _ActiveVolumeOccupancyDetectors_Type()
)
activeVolumeOccupancyDetectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeVolumeOccupancyDetectors.setStatus("mandatory")
_VolumeOccupancyTable_Object = MibTable
volumeOccupancyTable = _VolumeOccupancyTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    volumeOccupancyTable.setStatus("mandatory")
_VolumeOccupancyEntry_Object = MibTableRow
volumeOccupancyEntry = _VolumeOccupancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 4, 1)
)
volumeOccupancyEntry.setIndexNames(
    (0, "ASC_MIB1", "vehicleDetectorNumber"),
)
if mibBuilder.loadTexts:
    volumeOccupancyEntry.setStatus("mandatory")


class _DetectorVolume_Type(Integer32):
    """Custom type detectorVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DetectorVolume_Type.__name__ = "Integer32"
_DetectorVolume_Object = MibTableColumn
detectorVolume = _DetectorVolume_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 4, 1, 1),
    _DetectorVolume_Type()
)
detectorVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detectorVolume.setStatus("mandatory")


class _DetectorOccupancy_Type(Integer32):
    """Custom type detectorOccupancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DetectorOccupancy_Type.__name__ = "Integer32"
_DetectorOccupancy_Object = MibTableColumn
detectorOccupancy = _DetectorOccupancy_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 5, 4, 1, 2),
    _DetectorOccupancy_Type()
)
detectorOccupancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detectorOccupancy.setStatus("mandatory")


class _MaxPedestrianDetectors_Type(Integer32):
    """Custom type maxPedestrianDetectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxPedestrianDetectors_Type.__name__ = "Integer32"
_MaxPedestrianDetectors_Object = MibScalar
maxPedestrianDetectors = _MaxPedestrianDetectors_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 6),
    _MaxPedestrianDetectors_Type()
)
maxPedestrianDetectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPedestrianDetectors.setStatus("mandatory")
_PedestrianDetectorTable_Object = MibTable
pedestrianDetectorTable = _PedestrianDetectorTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    pedestrianDetectorTable.setStatus("mandatory")
_PedestrianDetectorEntry_Object = MibTableRow
pedestrianDetectorEntry = _PedestrianDetectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1)
)
pedestrianDetectorEntry.setIndexNames(
    (0, "ASC_MIB1", "pedestrianDetectorNumber"),
)
if mibBuilder.loadTexts:
    pedestrianDetectorEntry.setStatus("mandatory")


class _PedestrianDetectorNumber_Type(Integer32):
    """Custom type pedestrianDetectorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PedestrianDetectorNumber_Type.__name__ = "Integer32"
_PedestrianDetectorNumber_Object = MibTableColumn
pedestrianDetectorNumber = _PedestrianDetectorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1, 1),
    _PedestrianDetectorNumber_Type()
)
pedestrianDetectorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pedestrianDetectorNumber.setStatus("mandatory")


class _PedestrianDetectorCallPhase_Type(Integer32):
    """Custom type pedestrianDetectorCallPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PedestrianDetectorCallPhase_Type.__name__ = "Integer32"
_PedestrianDetectorCallPhase_Object = MibTableColumn
pedestrianDetectorCallPhase = _PedestrianDetectorCallPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1, 2),
    _PedestrianDetectorCallPhase_Type()
)
pedestrianDetectorCallPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pedestrianDetectorCallPhase.setStatus("mandatory")


class _PedestrianDetectorNoActivity_Type(Integer32):
    """Custom type pedestrianDetectorNoActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PedestrianDetectorNoActivity_Type.__name__ = "Integer32"
_PedestrianDetectorNoActivity_Object = MibTableColumn
pedestrianDetectorNoActivity = _PedestrianDetectorNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1, 3),
    _PedestrianDetectorNoActivity_Type()
)
pedestrianDetectorNoActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pedestrianDetectorNoActivity.setStatus("mandatory")


class _PedestrianDetectorMaxPresence_Type(Integer32):
    """Custom type pedestrianDetectorMaxPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PedestrianDetectorMaxPresence_Type.__name__ = "Integer32"
_PedestrianDetectorMaxPresence_Object = MibTableColumn
pedestrianDetectorMaxPresence = _PedestrianDetectorMaxPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1, 4),
    _PedestrianDetectorMaxPresence_Type()
)
pedestrianDetectorMaxPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pedestrianDetectorMaxPresence.setStatus("mandatory")


class _PedestrianDetectorErraticCounts_Type(Integer32):
    """Custom type pedestrianDetectorErraticCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PedestrianDetectorErraticCounts_Type.__name__ = "Integer32"
_PedestrianDetectorErraticCounts_Object = MibTableColumn
pedestrianDetectorErraticCounts = _PedestrianDetectorErraticCounts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1, 5),
    _PedestrianDetectorErraticCounts_Type()
)
pedestrianDetectorErraticCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pedestrianDetectorErraticCounts.setStatus("mandatory")


class _PedestrianDetectorAlarms_Type(Integer32):
    """Custom type pedestrianDetectorAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PedestrianDetectorAlarms_Type.__name__ = "Integer32"
_PedestrianDetectorAlarms_Object = MibTableColumn
pedestrianDetectorAlarms = _PedestrianDetectorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 2, 7, 1, 6),
    _PedestrianDetectorAlarms_Type()
)
pedestrianDetectorAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pedestrianDetectorAlarms.setStatus("mandatory")
_Unit_ObjectIdentity = ObjectIdentity
unit = _Unit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3)
)


class _UnitStartUpFlash_Type(Integer32):
    """Custom type unitStartUpFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UnitStartUpFlash_Type.__name__ = "Integer32"
_UnitStartUpFlash_Object = MibScalar
unitStartUpFlash = _UnitStartUpFlash_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 1),
    _UnitStartUpFlash_Type()
)
unitStartUpFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitStartUpFlash.setStatus("mandatory")


class _UnitAutoPedestrianClear_Type(Integer32):
    """Custom type unitAutoPedestrianClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_UnitAutoPedestrianClear_Type.__name__ = "Integer32"
_UnitAutoPedestrianClear_Object = MibScalar
unitAutoPedestrianClear = _UnitAutoPedestrianClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 2),
    _UnitAutoPedestrianClear_Type()
)
unitAutoPedestrianClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitAutoPedestrianClear.setStatus("mandatory")


class _UnitBackupTime_Type(Integer32):
    """Custom type unitBackupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UnitBackupTime_Type.__name__ = "Integer32"
_UnitBackupTime_Object = MibScalar
unitBackupTime = _UnitBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 3),
    _UnitBackupTime_Type()
)
unitBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitBackupTime.setStatus("mandatory")


class _UnitRedRevert_Type(Integer32):
    """Custom type unitRedRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UnitRedRevert_Type.__name__ = "Integer32"
_UnitRedRevert_Object = MibScalar
unitRedRevert = _UnitRedRevert_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 4),
    _UnitRedRevert_Type()
)
unitRedRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRedRevert.setStatus("mandatory")


class _UnitControlStatus_Type(Integer32):
    """Custom type unitControlStatus based on Integer32"""
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
        *(("other", 1),
          ("systemControl", 2),
          ("systemStandby", 3),
          ("backupMode", 4),
          ("manual", 5),
          ("timebase", 6),
          ("interconnect", 7),
          ("interconnectBackup", 8))
    )


_UnitControlStatus_Type.__name__ = "Integer32"
_UnitControlStatus_Object = MibScalar
unitControlStatus = _UnitControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 5),
    _UnitControlStatus_Type()
)
unitControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitControlStatus.setStatus("mandatory")


class _UnitFlashStatus_Type(Integer32):
    """Custom type unitFlashStatus based on Integer32"""
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
        *(("other", 1),
          ("notFlash", 2),
          ("automatic", 3),
          ("localManual", 4),
          ("faultMonitor", 5),
          ("mmu", 6),
          ("startup", 7),
          ("preempt", 8))
    )


_UnitFlashStatus_Type.__name__ = "Integer32"
_UnitFlashStatus_Object = MibScalar
unitFlashStatus = _UnitFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 6),
    _UnitFlashStatus_Type()
)
unitFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFlashStatus.setStatus("mandatory")


class _UnitAlarmStatus2_Type(Integer32):
    """Custom type unitAlarmStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UnitAlarmStatus2_Type.__name__ = "Integer32"
_UnitAlarmStatus2_Object = MibScalar
unitAlarmStatus2 = _UnitAlarmStatus2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 7),
    _UnitAlarmStatus2_Type()
)
unitAlarmStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmStatus2.setStatus("mandatory")


class _UnitAlarmStatus1_Type(Integer32):
    """Custom type unitAlarmStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UnitAlarmStatus1_Type.__name__ = "Integer32"
_UnitAlarmStatus1_Object = MibScalar
unitAlarmStatus1 = _UnitAlarmStatus1_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 8),
    _UnitAlarmStatus1_Type()
)
unitAlarmStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitAlarmStatus1.setStatus("mandatory")


class _ShortAlarmStatus_Type(Integer32):
    """Custom type shortAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ShortAlarmStatus_Type.__name__ = "Integer32"
_ShortAlarmStatus_Object = MibScalar
shortAlarmStatus = _ShortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 9),
    _ShortAlarmStatus_Type()
)
shortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shortAlarmStatus.setStatus("mandatory")


class _UnitControl_Type(Integer32):
    """Custom type unitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UnitControl_Type.__name__ = "Integer32"
_UnitControl_Object = MibScalar
unitControl = _UnitControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 10),
    _UnitControl_Type()
)
unitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitControl.setStatus("mandatory")


class _MaxAlarmGroups_Type(Integer32):
    """Custom type maxAlarmGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxAlarmGroups_Type.__name__ = "Integer32"
_MaxAlarmGroups_Object = MibScalar
maxAlarmGroups = _MaxAlarmGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 11),
    _MaxAlarmGroups_Type()
)
maxAlarmGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAlarmGroups.setStatus("mandatory")
_AlarmGroupTable_Object = MibTable
alarmGroupTable = _AlarmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 12)
)
if mibBuilder.loadTexts:
    alarmGroupTable.setStatus("mandatory")
_AlarmGroupEntry_Object = MibTableRow
alarmGroupEntry = _AlarmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 12, 1)
)
alarmGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "alarmGroupNumber"),
)
if mibBuilder.loadTexts:
    alarmGroupEntry.setStatus("mandatory")


class _AlarmGroupNumber_Type(Integer32):
    """Custom type alarmGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlarmGroupNumber_Type.__name__ = "Integer32"
_AlarmGroupNumber_Object = MibTableColumn
alarmGroupNumber = _AlarmGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 12, 1, 1),
    _AlarmGroupNumber_Type()
)
alarmGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGroupNumber.setStatus("mandatory")


class _AlarmGroupState_Type(Integer32):
    """Custom type alarmGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlarmGroupState_Type.__name__ = "Integer32"
_AlarmGroupState_Object = MibTableColumn
alarmGroupState = _AlarmGroupState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 12, 1, 2),
    _AlarmGroupState_Type()
)
alarmGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGroupState.setStatus("mandatory")


class _MaxSpecialFunctionOutputs_Type(Integer32):
    """Custom type maxSpecialFunctionOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxSpecialFunctionOutputs_Type.__name__ = "Integer32"
_MaxSpecialFunctionOutputs_Object = MibScalar
maxSpecialFunctionOutputs = _MaxSpecialFunctionOutputs_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 13),
    _MaxSpecialFunctionOutputs_Type()
)
maxSpecialFunctionOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSpecialFunctionOutputs.setStatus("mandatory")
_SpecialFunctionOutputTable_Object = MibTable
specialFunctionOutputTable = _SpecialFunctionOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 14)
)
if mibBuilder.loadTexts:
    specialFunctionOutputTable.setStatus("mandatory")
_SpecialFunctionOutputEntry_Object = MibTableRow
specialFunctionOutputEntry = _SpecialFunctionOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 14, 1)
)
specialFunctionOutputEntry.setIndexNames(
    (0, "ASC_MIB1", "specialFunctionOutputNumber"),
)
if mibBuilder.loadTexts:
    specialFunctionOutputEntry.setStatus("mandatory")


class _SpecialFunctionOutputNumber_Type(Integer32):
    """Custom type specialFunctionOutputNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SpecialFunctionOutputNumber_Type.__name__ = "Integer32"
_SpecialFunctionOutputNumber_Object = MibTableColumn
specialFunctionOutputNumber = _SpecialFunctionOutputNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 14, 1, 1),
    _SpecialFunctionOutputNumber_Type()
)
specialFunctionOutputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specialFunctionOutputNumber.setStatus("mandatory")


class _SpecialFunctionOutputState_Type(Integer32):
    """Custom type specialFunctionOutputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SpecialFunctionOutputState_Type.__name__ = "Integer32"
_SpecialFunctionOutputState_Object = MibTableColumn
specialFunctionOutputState = _SpecialFunctionOutputState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 3, 14, 1, 2),
    _SpecialFunctionOutputState_Type()
)
specialFunctionOutputState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specialFunctionOutputState.setStatus("mandatory")
_Coord_ObjectIdentity = ObjectIdentity
coord = _Coord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4)
)


class _CoordOperationalMode_Type(Integer32):
    """Custom type coordOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CoordOperationalMode_Type.__name__ = "Integer32"
_CoordOperationalMode_Object = MibScalar
coordOperationalMode = _CoordOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 1),
    _CoordOperationalMode_Type()
)
coordOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coordOperationalMode.setStatus("mandatory")


class _CoordCorrectionMode_Type(Integer32):
    """Custom type coordCorrectionMode based on Integer32"""
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
          ("dwell", 2),
          ("shortway", 3),
          ("addOnly", 4))
    )


_CoordCorrectionMode_Type.__name__ = "Integer32"
_CoordCorrectionMode_Object = MibScalar
coordCorrectionMode = _CoordCorrectionMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 2),
    _CoordCorrectionMode_Type()
)
coordCorrectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coordCorrectionMode.setStatus("mandatory")


class _CoordMaximumMode_Type(Integer32):
    """Custom type coordMaximumMode based on Integer32"""
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
          ("maximum1", 2),
          ("maximum2", 3),
          ("maxInhibit", 4))
    )


_CoordMaximumMode_Type.__name__ = "Integer32"
_CoordMaximumMode_Object = MibScalar
coordMaximumMode = _CoordMaximumMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 3),
    _CoordMaximumMode_Type()
)
coordMaximumMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coordMaximumMode.setStatus("mandatory")


class _CoordForceMode_Type(Integer32):
    """Custom type coordForceMode based on Integer32"""
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
          ("floating", 2),
          ("fixed", 3))
    )


_CoordForceMode_Type.__name__ = "Integer32"
_CoordForceMode_Object = MibScalar
coordForceMode = _CoordForceMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 4),
    _CoordForceMode_Type()
)
coordForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coordForceMode.setStatus("mandatory")


class _MaxPatterns_Type(Integer32):
    """Custom type maxPatterns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_MaxPatterns_Type.__name__ = "Integer32"
_MaxPatterns_Object = MibScalar
maxPatterns = _MaxPatterns_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 5),
    _MaxPatterns_Type()
)
maxPatterns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPatterns.setStatus("mandatory")


class _PatternTableType_Type(Integer32):
    """Custom type patternTableType based on Integer32"""
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
          ("patterns", 2),
          ("offset3", 3),
          ("offset5", 4))
    )


_PatternTableType_Type.__name__ = "Integer32"
_PatternTableType_Object = MibScalar
patternTableType = _PatternTableType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 6),
    _PatternTableType_Type()
)
patternTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patternTableType.setStatus("mandatory")
_PatternTable_Object = MibTable
patternTable = _PatternTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    patternTable.setStatus("mandatory")
_PatternEntry_Object = MibTableRow
patternEntry = _PatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7, 1)
)
patternEntry.setIndexNames(
    (0, "ASC_MIB1", "patternNumber"),
)
if mibBuilder.loadTexts:
    patternEntry.setStatus("mandatory")


class _PatternNumber_Type(Integer32):
    """Custom type patternNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 253),
    )


_PatternNumber_Type.__name__ = "Integer32"
_PatternNumber_Object = MibTableColumn
patternNumber = _PatternNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7, 1, 1),
    _PatternNumber_Type()
)
patternNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patternNumber.setStatus("mandatory")


class _PatternCycleTime_Type(Integer32):
    """Custom type patternCycleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PatternCycleTime_Type.__name__ = "Integer32"
_PatternCycleTime_Object = MibTableColumn
patternCycleTime = _PatternCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7, 1, 2),
    _PatternCycleTime_Type()
)
patternCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternCycleTime.setStatus("mandatory")


class _PatternOffsetTime_Type(Integer32):
    """Custom type patternOffsetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PatternOffsetTime_Type.__name__ = "Integer32"
_PatternOffsetTime_Object = MibTableColumn
patternOffsetTime = _PatternOffsetTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7, 1, 3),
    _PatternOffsetTime_Type()
)
patternOffsetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternOffsetTime.setStatus("mandatory")


class _PatternSplitNumber_Type(Integer32):
    """Custom type patternSplitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PatternSplitNumber_Type.__name__ = "Integer32"
_PatternSplitNumber_Object = MibTableColumn
patternSplitNumber = _PatternSplitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7, 1, 4),
    _PatternSplitNumber_Type()
)
patternSplitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternSplitNumber.setStatus("mandatory")


class _PatternSequenceNumber_Type(Integer32):
    """Custom type patternSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PatternSequenceNumber_Type.__name__ = "Integer32"
_PatternSequenceNumber_Object = MibTableColumn
patternSequenceNumber = _PatternSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 7, 1, 5),
    _PatternSequenceNumber_Type()
)
patternSequenceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patternSequenceNumber.setStatus("mandatory")


class _MaxSplits_Type(Integer32):
    """Custom type maxSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxSplits_Type.__name__ = "Integer32"
_MaxSplits_Object = MibScalar
maxSplits = _MaxSplits_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 8),
    _MaxSplits_Type()
)
maxSplits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSplits.setStatus("mandatory")
_SplitTable_Object = MibTable
splitTable = _SplitTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    splitTable.setStatus("mandatory")
_SplitEntry_Object = MibTableRow
splitEntry = _SplitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9, 1)
)
splitEntry.setIndexNames(
    (0, "ASC_MIB1", "splitNumber"),
    (0, "ASC_MIB1", "splitPhase"),
)
if mibBuilder.loadTexts:
    splitEntry.setStatus("mandatory")


class _SplitNumber_Type(Integer32):
    """Custom type splitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SplitNumber_Type.__name__ = "Integer32"
_SplitNumber_Object = MibTableColumn
splitNumber = _SplitNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9, 1, 1),
    _SplitNumber_Type()
)
splitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    splitNumber.setStatus("mandatory")


class _SplitPhase_Type(Integer32):
    """Custom type splitPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SplitPhase_Type.__name__ = "Integer32"
_SplitPhase_Object = MibTableColumn
splitPhase = _SplitPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9, 1, 2),
    _SplitPhase_Type()
)
splitPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    splitPhase.setStatus("mandatory")


class _SplitTime_Type(Integer32):
    """Custom type splitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SplitTime_Type.__name__ = "Integer32"
_SplitTime_Object = MibTableColumn
splitTime = _SplitTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9, 1, 3),
    _SplitTime_Type()
)
splitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    splitTime.setStatus("mandatory")


class _SplitMode_Type(Integer32):
    """Custom type splitMode based on Integer32"""
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
          ("none", 2),
          ("minimumVehicleRecall", 3),
          ("maximumVehicleRecall", 4),
          ("pedestrianRecall", 5),
          ("maximumVehicleAndPedestrianRecall", 6),
          ("phaseOmitted", 7))
    )


_SplitMode_Type.__name__ = "Integer32"
_SplitMode_Object = MibTableColumn
splitMode = _SplitMode_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9, 1, 4),
    _SplitMode_Type()
)
splitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    splitMode.setStatus("mandatory")


class _SplitCoordPhase_Type(Integer32):
    """Custom type splitCoordPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SplitCoordPhase_Type.__name__ = "Integer32"
_SplitCoordPhase_Object = MibTableColumn
splitCoordPhase = _SplitCoordPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 9, 1, 5),
    _SplitCoordPhase_Type()
)
splitCoordPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    splitCoordPhase.setStatus("mandatory")


class _CoordPatternStatus_Type(Integer32):
    """Custom type coordPatternStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CoordPatternStatus_Type.__name__ = "Integer32"
_CoordPatternStatus_Object = MibScalar
coordPatternStatus = _CoordPatternStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 10),
    _CoordPatternStatus_Type()
)
coordPatternStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coordPatternStatus.setStatus("mandatory")


class _LocalFreeStatus_Type(Integer32):
    """Custom type localFreeStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("notFree", 2),
          ("commandFree", 3),
          ("transitionFree", 4),
          ("inputFree", 5),
          ("coordFree", 6),
          ("badPlan", 7),
          ("badCycleTime", 8),
          ("splitOverrun", 9),
          ("invalidOffset", 10),
          ("failed", 11))
    )


_LocalFreeStatus_Type.__name__ = "Integer32"
_LocalFreeStatus_Object = MibScalar
localFreeStatus = _LocalFreeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 11),
    _LocalFreeStatus_Type()
)
localFreeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localFreeStatus.setStatus("mandatory")


class _CoordCycleStatus_Type(Integer32):
    """Custom type coordCycleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CoordCycleStatus_Type.__name__ = "Integer32"
_CoordCycleStatus_Object = MibScalar
coordCycleStatus = _CoordCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 12),
    _CoordCycleStatus_Type()
)
coordCycleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coordCycleStatus.setStatus("mandatory")


class _CoordSyncStatus_Type(Integer32):
    """Custom type coordSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CoordSyncStatus_Type.__name__ = "Integer32"
_CoordSyncStatus_Object = MibScalar
coordSyncStatus = _CoordSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 13),
    _CoordSyncStatus_Type()
)
coordSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coordSyncStatus.setStatus("mandatory")


class _SystemPatternControl_Type(Integer32):
    """Custom type systemPatternControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemPatternControl_Type.__name__ = "Integer32"
_SystemPatternControl_Object = MibScalar
systemPatternControl = _SystemPatternControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 14),
    _SystemPatternControl_Type()
)
systemPatternControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPatternControl.setStatus("mandatory")


class _SystemSyncControl_Type(Integer32):
    """Custom type systemSyncControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SystemSyncControl_Type.__name__ = "Integer32"
_SystemSyncControl_Object = MibScalar
systemSyncControl = _SystemSyncControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 4, 15),
    _SystemSyncControl_Type()
)
systemSyncControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSyncControl.setStatus("mandatory")
_TimebaseAsc_ObjectIdentity = ObjectIdentity
timebaseAsc = _TimebaseAsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5)
)


class _TimebaseAscPatternSync_Type(Integer32):
    """Custom type timebaseAscPatternSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TimebaseAscPatternSync_Type.__name__ = "Integer32"
_TimebaseAscPatternSync_Object = MibScalar
timebaseAscPatternSync = _TimebaseAscPatternSync_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 1),
    _TimebaseAscPatternSync_Type()
)
timebaseAscPatternSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timebaseAscPatternSync.setStatus("mandatory")


class _MaxTimebaseAscActions_Type(Integer32):
    """Custom type maxTimebaseAscActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxTimebaseAscActions_Type.__name__ = "Integer32"
_MaxTimebaseAscActions_Object = MibScalar
maxTimebaseAscActions = _MaxTimebaseAscActions_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 2),
    _MaxTimebaseAscActions_Type()
)
maxTimebaseAscActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTimebaseAscActions.setStatus("mandatory")
_TimebaseAscActionTable_Object = MibTable
timebaseAscActionTable = _TimebaseAscActionTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    timebaseAscActionTable.setStatus("mandatory")
_TimebaseAscActionEntry_Object = MibTableRow
timebaseAscActionEntry = _TimebaseAscActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 3, 1)
)
timebaseAscActionEntry.setIndexNames(
    (0, "ASC_MIB1", "timebaseAscActionNumber"),
)
if mibBuilder.loadTexts:
    timebaseAscActionEntry.setStatus("mandatory")


class _TimebaseAscActionNumber_Type(Integer32):
    """Custom type timebaseAscActionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TimebaseAscActionNumber_Type.__name__ = "Integer32"
_TimebaseAscActionNumber_Object = MibTableColumn
timebaseAscActionNumber = _TimebaseAscActionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 3, 1, 1),
    _TimebaseAscActionNumber_Type()
)
timebaseAscActionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timebaseAscActionNumber.setStatus("mandatory")


class _TimebaseAscPattern_Type(Integer32):
    """Custom type timebaseAscPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TimebaseAscPattern_Type.__name__ = "Integer32"
_TimebaseAscPattern_Object = MibTableColumn
timebaseAscPattern = _TimebaseAscPattern_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 3, 1, 2),
    _TimebaseAscPattern_Type()
)
timebaseAscPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timebaseAscPattern.setStatus("mandatory")


class _TimebaseAscAuxillaryFunction_Type(Integer32):
    """Custom type timebaseAscAuxillaryFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TimebaseAscAuxillaryFunction_Type.__name__ = "Integer32"
_TimebaseAscAuxillaryFunction_Object = MibTableColumn
timebaseAscAuxillaryFunction = _TimebaseAscAuxillaryFunction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 3, 1, 3),
    _TimebaseAscAuxillaryFunction_Type()
)
timebaseAscAuxillaryFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timebaseAscAuxillaryFunction.setStatus("mandatory")


class _TimebaseAscSpecialFunction_Type(Integer32):
    """Custom type timebaseAscSpecialFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TimebaseAscSpecialFunction_Type.__name__ = "Integer32"
_TimebaseAscSpecialFunction_Object = MibTableColumn
timebaseAscSpecialFunction = _TimebaseAscSpecialFunction_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 3, 1, 4),
    _TimebaseAscSpecialFunction_Type()
)
timebaseAscSpecialFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timebaseAscSpecialFunction.setStatus("mandatory")


class _TimebaseAscActionStatus_Type(Integer32):
    """Custom type timebaseAscActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TimebaseAscActionStatus_Type.__name__ = "Integer32"
_TimebaseAscActionStatus_Object = MibScalar
timebaseAscActionStatus = _TimebaseAscActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 5, 4),
    _TimebaseAscActionStatus_Type()
)
timebaseAscActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timebaseAscActionStatus.setStatus("mandatory")
_Preempt_ObjectIdentity = ObjectIdentity
preempt = _Preempt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6)
)


class _MaxPreempts_Type(Integer32):
    """Custom type maxPreempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxPreempts_Type.__name__ = "Integer32"
_MaxPreempts_Object = MibScalar
maxPreempts = _MaxPreempts_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 1),
    _MaxPreempts_Type()
)
maxPreempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPreempts.setStatus("mandatory")
_PreemptTable_Object = MibTable
preemptTable = _PreemptTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    preemptTable.setStatus("mandatory")
_PreemptEntry_Object = MibTableRow
preemptEntry = _PreemptEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1)
)
preemptEntry.setIndexNames(
    (0, "ASC_MIB1", "preemptNumber"),
)
if mibBuilder.loadTexts:
    preemptEntry.setStatus("mandatory")


class _PreemptNumber_Type(Integer32):
    """Custom type preemptNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PreemptNumber_Type.__name__ = "Integer32"
_PreemptNumber_Object = MibTableColumn
preemptNumber = _PreemptNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 1),
    _PreemptNumber_Type()
)
preemptNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preemptNumber.setStatus("mandatory")


class _PreemptControl_Type(Integer32):
    """Custom type preemptControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptControl_Type.__name__ = "Integer32"
_PreemptControl_Object = MibTableColumn
preemptControl = _PreemptControl_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 2),
    _PreemptControl_Type()
)
preemptControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptControl.setStatus("mandatory")


class _PreemptLink_Type(Integer32):
    """Custom type preemptLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptLink_Type.__name__ = "Integer32"
_PreemptLink_Object = MibTableColumn
preemptLink = _PreemptLink_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 3),
    _PreemptLink_Type()
)
preemptLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptLink.setStatus("mandatory")


class _PreemptDelay_Type(Integer32):
    """Custom type preemptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PreemptDelay_Type.__name__ = "Integer32"
_PreemptDelay_Object = MibTableColumn
preemptDelay = _PreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 4),
    _PreemptDelay_Type()
)
preemptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptDelay.setStatus("mandatory")


class _PreemptMinimumDuration_Type(Integer32):
    """Custom type preemptMinimumDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PreemptMinimumDuration_Type.__name__ = "Integer32"
_PreemptMinimumDuration_Object = MibTableColumn
preemptMinimumDuration = _PreemptMinimumDuration_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 5),
    _PreemptMinimumDuration_Type()
)
preemptMinimumDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptMinimumDuration.setStatus("mandatory")


class _PreemptMinimumGreen_Type(Integer32):
    """Custom type preemptMinimumGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptMinimumGreen_Type.__name__ = "Integer32"
_PreemptMinimumGreen_Object = MibTableColumn
preemptMinimumGreen = _PreemptMinimumGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 6),
    _PreemptMinimumGreen_Type()
)
preemptMinimumGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptMinimumGreen.setStatus("optional")


class _PreemptMinimumWalk_Type(Integer32):
    """Custom type preemptMinimumWalk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptMinimumWalk_Type.__name__ = "Integer32"
_PreemptMinimumWalk_Object = MibTableColumn
preemptMinimumWalk = _PreemptMinimumWalk_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 7),
    _PreemptMinimumWalk_Type()
)
preemptMinimumWalk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptMinimumWalk.setStatus("optional")


class _PreemptEnterPedClear_Type(Integer32):
    """Custom type preemptEnterPedClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptEnterPedClear_Type.__name__ = "Integer32"
_PreemptEnterPedClear_Object = MibTableColumn
preemptEnterPedClear = _PreemptEnterPedClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 8),
    _PreemptEnterPedClear_Type()
)
preemptEnterPedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptEnterPedClear.setStatus("optional")


class _PreemptTrackGreen_Type(Integer32):
    """Custom type preemptTrackGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptTrackGreen_Type.__name__ = "Integer32"
_PreemptTrackGreen_Object = MibTableColumn
preemptTrackGreen = _PreemptTrackGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 9),
    _PreemptTrackGreen_Type()
)
preemptTrackGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptTrackGreen.setStatus("mandatory")


class _PreemptDwellGreen_Type(Integer32):
    """Custom type preemptDwellGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PreemptDwellGreen_Type.__name__ = "Integer32"
_PreemptDwellGreen_Object = MibTableColumn
preemptDwellGreen = _PreemptDwellGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 10),
    _PreemptDwellGreen_Type()
)
preemptDwellGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptDwellGreen.setStatus("mandatory")


class _PreemptMaximumPresence_Type(Integer32):
    """Custom type preemptMaximumPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PreemptMaximumPresence_Type.__name__ = "Integer32"
_PreemptMaximumPresence_Object = MibTableColumn
preemptMaximumPresence = _PreemptMaximumPresence_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 11),
    _PreemptMaximumPresence_Type()
)
preemptMaximumPresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptMaximumPresence.setStatus("mandatory")
_PreemptTrackPhase_Type = OctetString
_PreemptTrackPhase_Object = MibTableColumn
preemptTrackPhase = _PreemptTrackPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 12),
    _PreemptTrackPhase_Type()
)
preemptTrackPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptTrackPhase.setStatus("mandatory")
_PreemptDwellPhase_Type = OctetString
_PreemptDwellPhase_Object = MibTableColumn
preemptDwellPhase = _PreemptDwellPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 13),
    _PreemptDwellPhase_Type()
)
preemptDwellPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptDwellPhase.setStatus("mandatory")
_PreemptDwellPed_Type = OctetString
_PreemptDwellPed_Object = MibTableColumn
preemptDwellPed = _PreemptDwellPed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 14),
    _PreemptDwellPed_Type()
)
preemptDwellPed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptDwellPed.setStatus("optional")
_PreemptExitPhase_Type = OctetString
_PreemptExitPhase_Object = MibTableColumn
preemptExitPhase = _PreemptExitPhase_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 15),
    _PreemptExitPhase_Type()
)
preemptExitPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptExitPhase.setStatus("mandatory")


class _PreemptState_Type(Integer32):
    """Custom type preemptState based on Integer32"""
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
          ("notActive", 2),
          ("notActiveWithCall", 3),
          ("entryStarted", 4),
          ("trackService", 5),
          ("dwell", 6),
          ("linkActive", 7),
          ("exitStarted", 8),
          ("maxPresence", 9))
    )


_PreemptState_Type.__name__ = "Integer32"
_PreemptState_Object = MibTableColumn
preemptState = _PreemptState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 2, 1, 16),
    _PreemptState_Type()
)
preemptState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preemptState.setStatus("optional")
_PreemptControlTable_Object = MibTable
preemptControlTable = _PreemptControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    preemptControlTable.setStatus("optional")
_PreemptControlEntry_Object = MibTableRow
preemptControlEntry = _PreemptControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 3, 1)
)
preemptControlEntry.setIndexNames(
    (0, "ASC_MIB1", "preemptControlNumber"),
)
if mibBuilder.loadTexts:
    preemptControlEntry.setStatus("mandatory")


class _PreemptControlNumber_Type(Integer32):
    """Custom type preemptControlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PreemptControlNumber_Type.__name__ = "Integer32"
_PreemptControlNumber_Object = MibTableColumn
preemptControlNumber = _PreemptControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 3, 1, 1),
    _PreemptControlNumber_Type()
)
preemptControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    preemptControlNumber.setStatus("mandatory")


class _PreemptControlState_Type(Integer32):
    """Custom type preemptControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PreemptControlState_Type.__name__ = "Integer32"
_PreemptControlState_Object = MibTableColumn
preemptControlState = _PreemptControlState_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 6, 3, 1, 2),
    _PreemptControlState_Type()
)
preemptControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preemptControlState.setStatus("mandatory")
_Ring_ObjectIdentity = ObjectIdentity
ring = _Ring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7)
)


class _MaxRings_Type(Integer32):
    """Custom type maxRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxRings_Type.__name__ = "Integer32"
_MaxRings_Object = MibScalar
maxRings = _MaxRings_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 1),
    _MaxRings_Type()
)
maxRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRings.setStatus("mandatory")


class _MaxSequences_Type(Integer32):
    """Custom type maxSequences based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxSequences_Type.__name__ = "Integer32"
_MaxSequences_Object = MibScalar
maxSequences = _MaxSequences_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 2),
    _MaxSequences_Type()
)
maxSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSequences.setStatus("mandatory")
_SequenceTable_Object = MibTable
sequenceTable = _SequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    sequenceTable.setStatus("mandatory")
_SequenceEntry_Object = MibTableRow
sequenceEntry = _SequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 3, 1)
)
sequenceEntry.setIndexNames(
    (0, "ASC_MIB1", "sequenceNumber"),
    (0, "ASC_MIB1", "sequenceRingNumber"),
)
if mibBuilder.loadTexts:
    sequenceEntry.setStatus("mandatory")


class _SequenceNumber_Type(Integer32):
    """Custom type sequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SequenceNumber_Type.__name__ = "Integer32"
_SequenceNumber_Object = MibTableColumn
sequenceNumber = _SequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 3, 1, 1),
    _SequenceNumber_Type()
)
sequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceNumber.setStatus("mandatory")


class _SequenceRingNumber_Type(Integer32):
    """Custom type sequenceRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SequenceRingNumber_Type.__name__ = "Integer32"
_SequenceRingNumber_Object = MibTableColumn
sequenceRingNumber = _SequenceRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 3, 1, 2),
    _SequenceRingNumber_Type()
)
sequenceRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceRingNumber.setStatus("mandatory")
_SequenceData_Type = OctetString
_SequenceData_Object = MibTableColumn
sequenceData = _SequenceData_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 3, 1, 3),
    _SequenceData_Type()
)
sequenceData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sequenceData.setStatus("mandatory")


class _MaxRingControlGroups_Type(Integer32):
    """Custom type maxRingControlGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxRingControlGroups_Type.__name__ = "Integer32"
_MaxRingControlGroups_Object = MibScalar
maxRingControlGroups = _MaxRingControlGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 4),
    _MaxRingControlGroups_Type()
)
maxRingControlGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxRingControlGroups.setStatus("mandatory")
_RingControlGroupTable_Object = MibTable
ringControlGroupTable = _RingControlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    ringControlGroupTable.setStatus("mandatory")
_RingControlGroupEntry_Object = MibTableRow
ringControlGroupEntry = _RingControlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1)
)
ringControlGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "ringControlGroupNumber"),
)
if mibBuilder.loadTexts:
    ringControlGroupEntry.setStatus("mandatory")


class _RingControlGroupNumber_Type(Integer32):
    """Custom type ringControlGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RingControlGroupNumber_Type.__name__ = "Integer32"
_RingControlGroupNumber_Object = MibTableColumn
ringControlGroupNumber = _RingControlGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 1),
    _RingControlGroupNumber_Type()
)
ringControlGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringControlGroupNumber.setStatus("mandatory")


class _RingControlGroupStopTime_Type(Integer32):
    """Custom type ringControlGroupStopTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupStopTime_Type.__name__ = "Integer32"
_RingControlGroupStopTime_Object = MibTableColumn
ringControlGroupStopTime = _RingControlGroupStopTime_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 2),
    _RingControlGroupStopTime_Type()
)
ringControlGroupStopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupStopTime.setStatus("mandatory")


class _RingControlGroupForceOff_Type(Integer32):
    """Custom type ringControlGroupForceOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupForceOff_Type.__name__ = "Integer32"
_RingControlGroupForceOff_Object = MibTableColumn
ringControlGroupForceOff = _RingControlGroupForceOff_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 3),
    _RingControlGroupForceOff_Type()
)
ringControlGroupForceOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupForceOff.setStatus("mandatory")


class _RingControlGroupMax2_Type(Integer32):
    """Custom type ringControlGroupMax2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupMax2_Type.__name__ = "Integer32"
_RingControlGroupMax2_Object = MibTableColumn
ringControlGroupMax2 = _RingControlGroupMax2_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 4),
    _RingControlGroupMax2_Type()
)
ringControlGroupMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupMax2.setStatus("optional")


class _RingControlGroupMaxInhibit_Type(Integer32):
    """Custom type ringControlGroupMaxInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupMaxInhibit_Type.__name__ = "Integer32"
_RingControlGroupMaxInhibit_Object = MibTableColumn
ringControlGroupMaxInhibit = _RingControlGroupMaxInhibit_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 5),
    _RingControlGroupMaxInhibit_Type()
)
ringControlGroupMaxInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupMaxInhibit.setStatus("optional")


class _RingControlGroupPedRecycle_Type(Integer32):
    """Custom type ringControlGroupPedRecycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupPedRecycle_Type.__name__ = "Integer32"
_RingControlGroupPedRecycle_Object = MibTableColumn
ringControlGroupPedRecycle = _RingControlGroupPedRecycle_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 6),
    _RingControlGroupPedRecycle_Type()
)
ringControlGroupPedRecycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupPedRecycle.setStatus("mandatory")


class _RingControlGroupRedRest_Type(Integer32):
    """Custom type ringControlGroupRedRest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupRedRest_Type.__name__ = "Integer32"
_RingControlGroupRedRest_Object = MibTableColumn
ringControlGroupRedRest = _RingControlGroupRedRest_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 7),
    _RingControlGroupRedRest_Type()
)
ringControlGroupRedRest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupRedRest.setStatus("optional")


class _RingControlGroupOmitRedClear_Type(Integer32):
    """Custom type ringControlGroupOmitRedClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RingControlGroupOmitRedClear_Type.__name__ = "Integer32"
_RingControlGroupOmitRedClear_Object = MibTableColumn
ringControlGroupOmitRedClear = _RingControlGroupOmitRedClear_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 7, 5, 1, 8),
    _RingControlGroupOmitRedClear_Type()
)
ringControlGroupOmitRedClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringControlGroupOmitRedClear.setStatus("optional")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8)
)


class _MaxChannels_Type(Integer32):
    """Custom type maxChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxChannels_Type.__name__ = "Integer32"
_MaxChannels_Object = MibScalar
maxChannels = _MaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 1),
    _MaxChannels_Type()
)
maxChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxChannels.setStatus("mandatory")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("mandatory")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2, 1)
)
channelEntry.setIndexNames(
    (0, "ASC_MIB1", "channelNumber"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("mandatory")


class _ChannelNumber_Type(Integer32):
    """Custom type channelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChannelNumber_Type.__name__ = "Integer32"
_ChannelNumber_Object = MibTableColumn
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2, 1, 1),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumber.setStatus("mandatory")


class _ChannelControlSource_Type(Integer32):
    """Custom type channelControlSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelControlSource_Type.__name__ = "Integer32"
_ChannelControlSource_Object = MibTableColumn
channelControlSource = _ChannelControlSource_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2, 1, 2),
    _ChannelControlSource_Type()
)
channelControlSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelControlSource.setStatus("mandatory")


class _ChannelControlType_Type(Integer32):
    """Custom type channelControlType based on Integer32"""
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
          ("phaseVehicle", 2),
          ("phasePedestrian", 3),
          ("overlap", 4))
    )


_ChannelControlType_Type.__name__ = "Integer32"
_ChannelControlType_Object = MibTableColumn
channelControlType = _ChannelControlType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2, 1, 3),
    _ChannelControlType_Type()
)
channelControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelControlType.setStatus("mandatory")


class _ChannelFlash_Type(Integer32):
    """Custom type channelFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelFlash_Type.__name__ = "Integer32"
_ChannelFlash_Object = MibTableColumn
channelFlash = _ChannelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2, 1, 4),
    _ChannelFlash_Type()
)
channelFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelFlash.setStatus("mandatory")


class _ChannelDim_Type(Integer32):
    """Custom type channelDim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelDim_Type.__name__ = "Integer32"
_ChannelDim_Object = MibTableColumn
channelDim = _ChannelDim_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 2, 1, 5),
    _ChannelDim_Type()
)
channelDim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelDim.setStatus("mandatory")


class _MaxChannelStatusGroups_Type(Integer32):
    """Custom type maxChannelStatusGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxChannelStatusGroups_Type.__name__ = "Integer32"
_MaxChannelStatusGroups_Object = MibScalar
maxChannelStatusGroups = _MaxChannelStatusGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 3),
    _MaxChannelStatusGroups_Type()
)
maxChannelStatusGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxChannelStatusGroups.setStatus("mandatory")
_ChannelStatusGroupTable_Object = MibTable
channelStatusGroupTable = _ChannelStatusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    channelStatusGroupTable.setStatus("mandatory")
_ChannelStatusGroupEntry_Object = MibTableRow
channelStatusGroupEntry = _ChannelStatusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 4, 1)
)
channelStatusGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "channelStatusGroupNumber"),
)
if mibBuilder.loadTexts:
    channelStatusGroupEntry.setStatus("mandatory")


class _ChannelStatusGroupNumber_Type(Integer32):
    """Custom type channelStatusGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChannelStatusGroupNumber_Type.__name__ = "Integer32"
_ChannelStatusGroupNumber_Object = MibTableColumn
channelStatusGroupNumber = _ChannelStatusGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 4, 1, 1),
    _ChannelStatusGroupNumber_Type()
)
channelStatusGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatusGroupNumber.setStatus("mandatory")


class _ChannelStatusGroupReds_Type(Integer32):
    """Custom type channelStatusGroupReds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelStatusGroupReds_Type.__name__ = "Integer32"
_ChannelStatusGroupReds_Object = MibTableColumn
channelStatusGroupReds = _ChannelStatusGroupReds_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 4, 1, 2),
    _ChannelStatusGroupReds_Type()
)
channelStatusGroupReds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatusGroupReds.setStatus("mandatory")


class _ChannelStatusGroupYellows_Type(Integer32):
    """Custom type channelStatusGroupYellows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelStatusGroupYellows_Type.__name__ = "Integer32"
_ChannelStatusGroupYellows_Object = MibTableColumn
channelStatusGroupYellows = _ChannelStatusGroupYellows_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 4, 1, 3),
    _ChannelStatusGroupYellows_Type()
)
channelStatusGroupYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatusGroupYellows.setStatus("mandatory")


class _ChannelStatusGroupGreens_Type(Integer32):
    """Custom type channelStatusGroupGreens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChannelStatusGroupGreens_Type.__name__ = "Integer32"
_ChannelStatusGroupGreens_Object = MibTableColumn
channelStatusGroupGreens = _ChannelStatusGroupGreens_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 8, 4, 1, 4),
    _ChannelStatusGroupGreens_Type()
)
channelStatusGroupGreens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatusGroupGreens.setStatus("mandatory")
_Overlap_ObjectIdentity = ObjectIdentity
overlap = _Overlap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9)
)


class _MaxOverlaps_Type(Integer32):
    """Custom type maxOverlaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxOverlaps_Type.__name__ = "Integer32"
_MaxOverlaps_Object = MibScalar
maxOverlaps = _MaxOverlaps_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 1),
    _MaxOverlaps_Type()
)
maxOverlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxOverlaps.setStatus("mandatory")
_OverlapTable_Object = MibTable
overlapTable = _OverlapTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    overlapTable.setStatus("mandatory")
_OverlapEntry_Object = MibTableRow
overlapEntry = _OverlapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1)
)
overlapEntry.setIndexNames(
    (0, "ASC_MIB1", "overlapNumber"),
)
if mibBuilder.loadTexts:
    overlapEntry.setStatus("mandatory")


class _OverlapNumber_Type(Integer32):
    """Custom type overlapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OverlapNumber_Type.__name__ = "Integer32"
_OverlapNumber_Object = MibTableColumn
overlapNumber = _OverlapNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 1),
    _OverlapNumber_Type()
)
overlapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overlapNumber.setStatus("mandatory")


class _OverlapType_Type(Integer32):
    """Custom type overlapType based on Integer32"""
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
          ("normal", 2),
          ("minusGreenYellow", 3))
    )


_OverlapType_Type.__name__ = "Integer32"
_OverlapType_Object = MibTableColumn
overlapType = _OverlapType_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 2),
    _OverlapType_Type()
)
overlapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlapType.setStatus("mandatory")
_OverlapIncludedPhases_Type = OctetString
_OverlapIncludedPhases_Object = MibTableColumn
overlapIncludedPhases = _OverlapIncludedPhases_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 3),
    _OverlapIncludedPhases_Type()
)
overlapIncludedPhases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlapIncludedPhases.setStatus("mandatory")
_OverlapModifierPhases_Type = OctetString
_OverlapModifierPhases_Object = MibTableColumn
overlapModifierPhases = _OverlapModifierPhases_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 4),
    _OverlapModifierPhases_Type()
)
overlapModifierPhases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlapModifierPhases.setStatus("mandatory")


class _OverlapTrailGreen_Type(Integer32):
    """Custom type overlapTrailGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverlapTrailGreen_Type.__name__ = "Integer32"
_OverlapTrailGreen_Object = MibTableColumn
overlapTrailGreen = _OverlapTrailGreen_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 5),
    _OverlapTrailGreen_Type()
)
overlapTrailGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlapTrailGreen.setStatus("mandatory")


class _OverlapTrailYellow_Type(Integer32):
    """Custom type overlapTrailYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverlapTrailYellow_Type.__name__ = "Integer32"
_OverlapTrailYellow_Object = MibTableColumn
overlapTrailYellow = _OverlapTrailYellow_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 6),
    _OverlapTrailYellow_Type()
)
overlapTrailYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlapTrailYellow.setStatus("mandatory")


class _OverlapTrailRed_Type(Integer32):
    """Custom type overlapTrailRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverlapTrailRed_Type.__name__ = "Integer32"
_OverlapTrailRed_Object = MibTableColumn
overlapTrailRed = _OverlapTrailRed_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 2, 1, 7),
    _OverlapTrailRed_Type()
)
overlapTrailRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overlapTrailRed.setStatus("mandatory")


class _MaxOverlapStatusGroups_Type(Integer32):
    """Custom type maxOverlapStatusGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxOverlapStatusGroups_Type.__name__ = "Integer32"
_MaxOverlapStatusGroups_Object = MibScalar
maxOverlapStatusGroups = _MaxOverlapStatusGroups_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 3),
    _MaxOverlapStatusGroups_Type()
)
maxOverlapStatusGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxOverlapStatusGroups.setStatus("mandatory")
_OverlapStatusGroupTable_Object = MibTable
overlapStatusGroupTable = _OverlapStatusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    overlapStatusGroupTable.setStatus("mandatory")
_OverlapStatusGroupEntry_Object = MibTableRow
overlapStatusGroupEntry = _OverlapStatusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 4, 1)
)
overlapStatusGroupEntry.setIndexNames(
    (0, "ASC_MIB1", "overlapStatusGroupNumber"),
)
if mibBuilder.loadTexts:
    overlapStatusGroupEntry.setStatus("mandatory")


class _OverlapStatusGroupNumber_Type(Integer32):
    """Custom type overlapStatusGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OverlapStatusGroupNumber_Type.__name__ = "Integer32"
_OverlapStatusGroupNumber_Object = MibTableColumn
overlapStatusGroupNumber = _OverlapStatusGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 4, 1, 1),
    _OverlapStatusGroupNumber_Type()
)
overlapStatusGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overlapStatusGroupNumber.setStatus("mandatory")


class _OverlapStatusGroupReds_Type(Integer32):
    """Custom type overlapStatusGroupReds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverlapStatusGroupReds_Type.__name__ = "Integer32"
_OverlapStatusGroupReds_Object = MibTableColumn
overlapStatusGroupReds = _OverlapStatusGroupReds_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 4, 1, 2),
    _OverlapStatusGroupReds_Type()
)
overlapStatusGroupReds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overlapStatusGroupReds.setStatus("mandatory")


class _OverlapStatusGroupYellows_Type(Integer32):
    """Custom type overlapStatusGroupYellows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverlapStatusGroupYellows_Type.__name__ = "Integer32"
_OverlapStatusGroupYellows_Object = MibTableColumn
overlapStatusGroupYellows = _OverlapStatusGroupYellows_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 4, 1, 3),
    _OverlapStatusGroupYellows_Type()
)
overlapStatusGroupYellows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overlapStatusGroupYellows.setStatus("mandatory")


class _OverlapStatusGroupGreens_Type(Integer32):
    """Custom type overlapStatusGroupGreens based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OverlapStatusGroupGreens_Type.__name__ = "Integer32"
_OverlapStatusGroupGreens_Object = MibTableColumn
overlapStatusGroupGreens = _OverlapStatusGroupGreens_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 9, 4, 1, 4),
    _OverlapStatusGroupGreens_Type()
)
overlapStatusGroupGreens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overlapStatusGroupGreens.setStatus("mandatory")
_Ts2port1_ObjectIdentity = ObjectIdentity
ts2port1 = _Ts2port1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10)
)


class _MaxPort1Addresses_Type(Integer32):
    """Custom type maxPort1Addresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MaxPort1Addresses_Type.__name__ = "Integer32"
_MaxPort1Addresses_Object = MibScalar
maxPort1Addresses = _MaxPort1Addresses_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 1),
    _MaxPort1Addresses_Type()
)
maxPort1Addresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPort1Addresses.setStatus("mandatory")
_Port1Table_Object = MibTable
port1Table = _Port1Table_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    port1Table.setStatus("mandatory")
_Port1Entry_Object = MibTableRow
port1Entry = _Port1Entry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2, 1)
)
port1Entry.setIndexNames(
    (0, "ASC_MIB1", "port1Number"),
)
if mibBuilder.loadTexts:
    port1Entry.setStatus("mandatory")


class _Port1Number_Type(Integer32):
    """Custom type port1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Port1Number_Type.__name__ = "Integer32"
_Port1Number_Object = MibTableColumn
port1Number = _Port1Number_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2, 1, 1),
    _Port1Number_Type()
)
port1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port1Number.setStatus("mandatory")


class _Port1DevicePresent_Type(Integer32):
    """Custom type port1DevicePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port1DevicePresent_Type.__name__ = "Integer32"
_Port1DevicePresent_Object = MibTableColumn
port1DevicePresent = _Port1DevicePresent_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2, 1, 2),
    _Port1DevicePresent_Type()
)
port1DevicePresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1DevicePresent.setStatus("mandatory")


class _Port1Frame40Enable_Type(Integer32):
    """Custom type port1Frame40Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port1Frame40Enable_Type.__name__ = "Integer32"
_Port1Frame40Enable_Object = MibTableColumn
port1Frame40Enable = _Port1Frame40Enable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2, 1, 3),
    _Port1Frame40Enable_Type()
)
port1Frame40Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Frame40Enable.setStatus("mandatory")


class _Port1Status_Type(Integer32):
    """Custom type port1Status based on Integer32"""
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
          ("online", 2),
          ("responseFault", 3))
    )


_Port1Status_Type.__name__ = "Integer32"
_Port1Status_Object = MibTableColumn
port1Status = _Port1Status_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2, 1, 4),
    _Port1Status_Type()
)
port1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port1Status.setStatus("mandatory")


class _Port1FaultFrame_Type(Integer32):
    """Custom type port1FaultFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port1FaultFrame_Type.__name__ = "Integer32"
_Port1FaultFrame_Object = MibTableColumn
port1FaultFrame = _Port1FaultFrame_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 2, 1, 10, 2, 1, 5),
    _Port1FaultFrame_Type()
)
port1FaultFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port1FaultFrame.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASC_MIB1",
    **{"asc": asc,
       "phase": phase,
       "maxPhases": maxPhases,
       "phaseTable": phaseTable,
       "phaseEntry": phaseEntry,
       "phaseNumber": phaseNumber,
       "phaseWalk": phaseWalk,
       "phasePedestrianClear": phasePedestrianClear,
       "phaseMinimumGreen": phaseMinimumGreen,
       "phasePassage": phasePassage,
       "phaseMaximum1": phaseMaximum1,
       "phaseMaximum2": phaseMaximum2,
       "phaseYellowChange": phaseYellowChange,
       "phaseRedClear": phaseRedClear,
       "phaseRedRevert": phaseRedRevert,
       "phaseAddedInitial": phaseAddedInitial,
       "phaseMaximumInitial": phaseMaximumInitial,
       "phaseTimeBeforeReduction": phaseTimeBeforeReduction,
       "phaseCarsBeforeReduction": phaseCarsBeforeReduction,
       "phaseTimeToReduce": phaseTimeToReduce,
       "phaseReduceBy": phaseReduceBy,
       "phaseMinimumGap": phaseMinimumGap,
       "phaseDynamicMaxLimit": phaseDynamicMaxLimit,
       "phaseDynamicMaxStep": phaseDynamicMaxStep,
       "phaseStartup": phaseStartup,
       "phaseOptions": phaseOptions,
       "phaseRing": phaseRing,
       "phaseConcurrency": phaseConcurrency,
       "maxPhaseGroups": maxPhaseGroups,
       "phaseStatusGroupTable": phaseStatusGroupTable,
       "phaseStatusGroupEntry": phaseStatusGroupEntry,
       "phaseStatusGroupNumber": phaseStatusGroupNumber,
       "phaseStatusGroupReds": phaseStatusGroupReds,
       "phaseStatusGroupYellows": phaseStatusGroupYellows,
       "phaseStatusGroupGreens": phaseStatusGroupGreens,
       "phaseStatusGroupDontWalks": phaseStatusGroupDontWalks,
       "phaseStatusGroupPedClears": phaseStatusGroupPedClears,
       "phaseStatusGroupWalks": phaseStatusGroupWalks,
       "phaseStatusGroupVehCalls": phaseStatusGroupVehCalls,
       "phaseStatusGroupPedCalls": phaseStatusGroupPedCalls,
       "phaseStatusGroupPhaseOns": phaseStatusGroupPhaseOns,
       "phaseStatusGroupPhaseNexts": phaseStatusGroupPhaseNexts,
       "phaseControlGroupTable": phaseControlGroupTable,
       "phaseControlGroupEntry": phaseControlGroupEntry,
       "phaseControlGroupNumber": phaseControlGroupNumber,
       "phaseControlGroupPhaseOmit": phaseControlGroupPhaseOmit,
       "phaseControlGroupPedOmit": phaseControlGroupPedOmit,
       "phaseControlGroupHold": phaseControlGroupHold,
       "phaseControlGroupForceOff": phaseControlGroupForceOff,
       "phaseControlGroupVehCall": phaseControlGroupVehCall,
       "phaseControlGroupPedCall": phaseControlGroupPedCall,
       "detector": detector,
       "maxVehicleDetectors": maxVehicleDetectors,
       "vehicleDetectorTable": vehicleDetectorTable,
       "vehicleDetectorEntry": vehicleDetectorEntry,
       "vehicleDetectorNumber": vehicleDetectorNumber,
       "vehicleDetectorOptions": vehicleDetectorOptions,
       "vehicleDetectorCallPhase": vehicleDetectorCallPhase,
       "vehicleDetectorSwitchPhase": vehicleDetectorSwitchPhase,
       "vehicleDetectorDelay": vehicleDetectorDelay,
       "vehicleDetectorExtend": vehicleDetectorExtend,
       "vehicleDetectorQueueLimit": vehicleDetectorQueueLimit,
       "vehicleDetectorNoActivity": vehicleDetectorNoActivity,
       "vehicleDetectorMaxPresence": vehicleDetectorMaxPresence,
       "vehicleDetectorErraticCounts": vehicleDetectorErraticCounts,
       "vehicleDetectorFailTime": vehicleDetectorFailTime,
       "vehicleDetectorAlarms": vehicleDetectorAlarms,
       "vehicleDetectorReportedAlarms": vehicleDetectorReportedAlarms,
       "vehicleDetectorReset": vehicleDetectorReset,
       "maxVehicleDetectorStatusGroups": maxVehicleDetectorStatusGroups,
       "vehicleDetectorStatusGroupTable": vehicleDetectorStatusGroupTable,
       "vehicleDetectorStatusGroupEntry": vehicleDetectorStatusGroupEntry,
       "vehicleDetectorStatusGroupNumber": vehicleDetectorStatusGroupNumber,
       "vehicleDetectorStatusGroupActive": vehicleDetectorStatusGroupActive,
       "vehicleDetectorStatusGroupAlarms": vehicleDetectorStatusGroupAlarms,
       "volumeOccupancyReport": volumeOccupancyReport,
       "volumeOccupancySequence": volumeOccupancySequence,
       "volumeOccupancyPeriod": volumeOccupancyPeriod,
       "activeVolumeOccupancyDetectors": activeVolumeOccupancyDetectors,
       "volumeOccupancyTable": volumeOccupancyTable,
       "volumeOccupancyEntry": volumeOccupancyEntry,
       "detectorVolume": detectorVolume,
       "detectorOccupancy": detectorOccupancy,
       "maxPedestrianDetectors": maxPedestrianDetectors,
       "pedestrianDetectorTable": pedestrianDetectorTable,
       "pedestrianDetectorEntry": pedestrianDetectorEntry,
       "pedestrianDetectorNumber": pedestrianDetectorNumber,
       "pedestrianDetectorCallPhase": pedestrianDetectorCallPhase,
       "pedestrianDetectorNoActivity": pedestrianDetectorNoActivity,
       "pedestrianDetectorMaxPresence": pedestrianDetectorMaxPresence,
       "pedestrianDetectorErraticCounts": pedestrianDetectorErraticCounts,
       "pedestrianDetectorAlarms": pedestrianDetectorAlarms,
       "unit": unit,
       "unitStartUpFlash": unitStartUpFlash,
       "unitAutoPedestrianClear": unitAutoPedestrianClear,
       "unitBackupTime": unitBackupTime,
       "unitRedRevert": unitRedRevert,
       "unitControlStatus": unitControlStatus,
       "unitFlashStatus": unitFlashStatus,
       "unitAlarmStatus2": unitAlarmStatus2,
       "unitAlarmStatus1": unitAlarmStatus1,
       "shortAlarmStatus": shortAlarmStatus,
       "unitControl": unitControl,
       "maxAlarmGroups": maxAlarmGroups,
       "alarmGroupTable": alarmGroupTable,
       "alarmGroupEntry": alarmGroupEntry,
       "alarmGroupNumber": alarmGroupNumber,
       "alarmGroupState": alarmGroupState,
       "maxSpecialFunctionOutputs": maxSpecialFunctionOutputs,
       "specialFunctionOutputTable": specialFunctionOutputTable,
       "specialFunctionOutputEntry": specialFunctionOutputEntry,
       "specialFunctionOutputNumber": specialFunctionOutputNumber,
       "specialFunctionOutputState": specialFunctionOutputState,
       "coord": coord,
       "coordOperationalMode": coordOperationalMode,
       "coordCorrectionMode": coordCorrectionMode,
       "coordMaximumMode": coordMaximumMode,
       "coordForceMode": coordForceMode,
       "maxPatterns": maxPatterns,
       "patternTableType": patternTableType,
       "patternTable": patternTable,
       "patternEntry": patternEntry,
       "patternNumber": patternNumber,
       "patternCycleTime": patternCycleTime,
       "patternOffsetTime": patternOffsetTime,
       "patternSplitNumber": patternSplitNumber,
       "patternSequenceNumber": patternSequenceNumber,
       "maxSplits": maxSplits,
       "splitTable": splitTable,
       "splitEntry": splitEntry,
       "splitNumber": splitNumber,
       "splitPhase": splitPhase,
       "splitTime": splitTime,
       "splitMode": splitMode,
       "splitCoordPhase": splitCoordPhase,
       "coordPatternStatus": coordPatternStatus,
       "localFreeStatus": localFreeStatus,
       "coordCycleStatus": coordCycleStatus,
       "coordSyncStatus": coordSyncStatus,
       "systemPatternControl": systemPatternControl,
       "systemSyncControl": systemSyncControl,
       "timebaseAsc": timebaseAsc,
       "timebaseAscPatternSync": timebaseAscPatternSync,
       "maxTimebaseAscActions": maxTimebaseAscActions,
       "timebaseAscActionTable": timebaseAscActionTable,
       "timebaseAscActionEntry": timebaseAscActionEntry,
       "timebaseAscActionNumber": timebaseAscActionNumber,
       "timebaseAscPattern": timebaseAscPattern,
       "timebaseAscAuxillaryFunction": timebaseAscAuxillaryFunction,
       "timebaseAscSpecialFunction": timebaseAscSpecialFunction,
       "timebaseAscActionStatus": timebaseAscActionStatus,
       "preempt": preempt,
       "maxPreempts": maxPreempts,
       "preemptTable": preemptTable,
       "preemptEntry": preemptEntry,
       "preemptNumber": preemptNumber,
       "preemptControl": preemptControl,
       "preemptLink": preemptLink,
       "preemptDelay": preemptDelay,
       "preemptMinimumDuration": preemptMinimumDuration,
       "preemptMinimumGreen": preemptMinimumGreen,
       "preemptMinimumWalk": preemptMinimumWalk,
       "preemptEnterPedClear": preemptEnterPedClear,
       "preemptTrackGreen": preemptTrackGreen,
       "preemptDwellGreen": preemptDwellGreen,
       "preemptMaximumPresence": preemptMaximumPresence,
       "preemptTrackPhase": preemptTrackPhase,
       "preemptDwellPhase": preemptDwellPhase,
       "preemptDwellPed": preemptDwellPed,
       "preemptExitPhase": preemptExitPhase,
       "preemptState": preemptState,
       "preemptControlTable": preemptControlTable,
       "preemptControlEntry": preemptControlEntry,
       "preemptControlNumber": preemptControlNumber,
       "preemptControlState": preemptControlState,
       "ring": ring,
       "maxRings": maxRings,
       "maxSequences": maxSequences,
       "sequenceTable": sequenceTable,
       "sequenceEntry": sequenceEntry,
       "sequenceNumber": sequenceNumber,
       "sequenceRingNumber": sequenceRingNumber,
       "sequenceData": sequenceData,
       "maxRingControlGroups": maxRingControlGroups,
       "ringControlGroupTable": ringControlGroupTable,
       "ringControlGroupEntry": ringControlGroupEntry,
       "ringControlGroupNumber": ringControlGroupNumber,
       "ringControlGroupStopTime": ringControlGroupStopTime,
       "ringControlGroupForceOff": ringControlGroupForceOff,
       "ringControlGroupMax2": ringControlGroupMax2,
       "ringControlGroupMaxInhibit": ringControlGroupMaxInhibit,
       "ringControlGroupPedRecycle": ringControlGroupPedRecycle,
       "ringControlGroupRedRest": ringControlGroupRedRest,
       "ringControlGroupOmitRedClear": ringControlGroupOmitRedClear,
       "channel": channel,
       "maxChannels": maxChannels,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelNumber": channelNumber,
       "channelControlSource": channelControlSource,
       "channelControlType": channelControlType,
       "channelFlash": channelFlash,
       "channelDim": channelDim,
       "maxChannelStatusGroups": maxChannelStatusGroups,
       "channelStatusGroupTable": channelStatusGroupTable,
       "channelStatusGroupEntry": channelStatusGroupEntry,
       "channelStatusGroupNumber": channelStatusGroupNumber,
       "channelStatusGroupReds": channelStatusGroupReds,
       "channelStatusGroupYellows": channelStatusGroupYellows,
       "channelStatusGroupGreens": channelStatusGroupGreens,
       "overlap": overlap,
       "maxOverlaps": maxOverlaps,
       "overlapTable": overlapTable,
       "overlapEntry": overlapEntry,
       "overlapNumber": overlapNumber,
       "overlapType": overlapType,
       "overlapIncludedPhases": overlapIncludedPhases,
       "overlapModifierPhases": overlapModifierPhases,
       "overlapTrailGreen": overlapTrailGreen,
       "overlapTrailYellow": overlapTrailYellow,
       "overlapTrailRed": overlapTrailRed,
       "maxOverlapStatusGroups": maxOverlapStatusGroups,
       "overlapStatusGroupTable": overlapStatusGroupTable,
       "overlapStatusGroupEntry": overlapStatusGroupEntry,
       "overlapStatusGroupNumber": overlapStatusGroupNumber,
       "overlapStatusGroupReds": overlapStatusGroupReds,
       "overlapStatusGroupYellows": overlapStatusGroupYellows,
       "overlapStatusGroupGreens": overlapStatusGroupGreens,
       "ts2port1": ts2port1,
       "maxPort1Addresses": maxPort1Addresses,
       "port1Table": port1Table,
       "port1Entry": port1Entry,
       "port1Number": port1Number,
       "port1DevicePresent": port1DevicePresent,
       "port1Frame40Enable": port1Frame40Enable,
       "port1Status": port1Status,
       "port1FaultFrame": port1FaultFrame}
)
