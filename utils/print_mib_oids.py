import os
from pysnmp.smi import builder, error

# If you want more detailed log messages, uncomment the following line
# debug.setLogger(debug.Debug('compiler'))

# Initialize MIB Builder
mib_builder = builder.MibBuilder()

# Add directory containing the MIB files
MIB_PATH = str(os.path.join(os.path.dirname(__file__), '../py_mibs'))

mib_sources = mib_builder.get_mib_sources() + (builder.DirMibSource(MIB_PATH),)
mib_builder.set_mib_sources(*mib_sources)

oid_library = {}  # our oid library which we will populate


def extract_oids(module_name):
    oid_dict = {}
    for name, symbol in mib_builder.mibSymbols.get(module_name).items():
        if hasattr(symbol, 'name'):
            oid_dict[name] = tuple(symbol.name)  # store oid as tuple
    return oid_dict


def load_mibs(module_names):
    for module in module_names:
        print('Loading MIB module:', module)
        try:
            mib_builder.load_module(module)
            oid_library.update(extract_oids(module))
        except Exception as ex:
            print('Error loading module', module, ':', ex)


# Method call to load MIBs
load_mibs(['ASC_MIB1'])

# printing oid library
for k, v in oid_library.items():
    print(f'Name: {k}, OID: {v}')
