# SNMP MIB module (CHAP-MIB1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/2103CHAP.mib
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

(layers,) = mibBuilder.importSymbols(
    "TMIB-II",
    "layers")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chap_ObjectIdentity = ObjectIdentity
chap = _Chap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1, 1)
)


class _ChapMaxSecrets_Type(Integer32):
    """Custom type chapMaxSecrets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChapMaxSecrets_Type.__name__ = "Integer32"
_ChapMaxSecrets_Object = MibScalar
chapMaxSecrets = _ChapMaxSecrets_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1, 1, 1),
    _ChapMaxSecrets_Type()
)
chapMaxSecrets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chapMaxSecrets.setStatus("mandatory")
_ChapSecretTable_Object = MibTable
chapSecretTable = _ChapSecretTable_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chapSecretTable.setStatus("mandatory")
_ChapSecretEntry_Object = MibTableRow
chapSecretEntry = _ChapSecretEntry_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1, 1, 2, 1)
)
chapSecretEntry.setIndexNames(
    (0, "CHAP-MIB1", "chapName"),
)
if mibBuilder.loadTexts:
    chapSecretEntry.setStatus("mandatory")
_ChapName_Type = OctetString
_ChapName_Object = MibTableColumn
chapName = _ChapName_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1, 1, 2, 1, 1),
    _ChapName_Type()
)
chapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chapName.setStatus("mandatory")
_ChapSecret_Type = OctetString
_ChapSecret_Object = MibTableColumn
chapSecret = _ChapSecret_Object(
    (1, 3, 6, 1, 4, 1, 1206, 4, 1, 1, 1, 2, 1, 2),
    _ChapSecret_Type()
)
chapSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chapSecret.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHAP-MIB1",
    **{"chap": chap,
       "chapMaxSecrets": chapMaxSecrets,
       "chapSecretTable": chapSecretTable,
       "chapSecretEntry": chapSecretEntry,
       "chapName": chapName,
       "chapSecret": chapSecret}
)
