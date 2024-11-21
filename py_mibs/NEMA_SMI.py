# SNMP MIB module (NEMA_SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/x-wing/PycharmProjects/NTCIPY/source_mibs_orig/SMIC MIBs/1101SMI.mib
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
 enterprises,
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
    "enterprises",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nema_ObjectIdentity = ObjectIdentity
nema = _Nema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206)
)
_NemaMgmt_ObjectIdentity = ObjectIdentity
nemaMgmt = _NemaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 1)
)
_NemaExperimental_ObjectIdentity = ObjectIdentity
nemaExperimental = _NemaExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 2)
)
_NemaPrivate_ObjectIdentity = ObjectIdentity
nemaPrivate = _NemaPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 3)
)
_Transportation_ObjectIdentity = ObjectIdentity
transportation = _Transportation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1206, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEMA_SMI",
    **{"nema": nema,
       "nemaMgmt": nemaMgmt,
       "nemaExperimental": nemaExperimental,
       "nemaPrivate": nemaPrivate,
       "transportation": transportation}
)
