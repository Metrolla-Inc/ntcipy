import os
from pysnmp.hlapi import *
from pysnmp.smi import builder, view

MIB_PATH = str(os.path.join(os.path.dirname(__file__), 'py_mibs'))


class NTCIPInterface:
    def __init__(self, ip_address, community='public', port=161, mib_path=MIB_PATH, load_mibs_list=['ASC_MIB1']):
        self.ip_address = ip_address
        self.community = community
        self.port = port
        self.mib_builder = builder.MibBuilder()
        self.mib_view_controller = view.MibViewController(self.mib_builder)
        self.mib_sources = self.mib_builder.get_mib_sources() + (builder.DirMibSource(mib_path),)
        self.mib_builder.set_mib_sources(*self.mib_sources)
        self.load_mibs(load_mibs_list)

    def load_mibs(self, module_names):
        for module in module_names:
            print('Loading MIB module:', module)
            try:
                self.mib_builder.load_module(module)
                self.oid_library = self.extract_oids(module)
            except Exception as ex:
                print('Error loading module', module, ':', ex)

    def extract_oids(self, module_name):
        oid_dict = {}
        for name, symbol in self.mib_builder.mibSymbols.get(module_name).items():
            if hasattr(symbol, 'name'):
                oid_dict[name] = tuple(symbol.name)  # store oid as tuple
            else:
                print(name, dir(symbol), '\n\n')
        return oid_dict

    def get_oid(self, oid_name):
        oid = self.oid_library[oid_name]  # get OID from the library
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(self.community),
            UdpTransportTarget((self.ip_address, self.port)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
        error_indication, error_status, error_index, var_binds = next(iterator)
        if error_indication:
            print(f'Error: {error_indication}')
        elif error_status:
            print(f'Error: {error_status.prettyPrint()} at {error_index}')
        else:
            for var_bind in var_binds:
                return var_bind[1]

    def set_oid(self, oid_name, value, value_type):
        oid = self.oid_library[oid_name]  # get OID from the library
        iterator = setCmd(
            SnmpEngine(),
            CommunityData(self.community),
            UdpTransportTarget((self.ip_address, self.port)),
            ContextData(),
            ObjectType(ObjectIdentity(oid), value_type(value))
        )
        error_indication, error_status, error_index, var_binds = next(iterator)
        if error_indication:
            print(f'Error: {error_indication}')
        elif error_status:
            print(f'Error: {error_status.prettyPrint()} at {error_index}')
        else:
            print('Set operation successful')


ntcip = NTCIPInterface('192.168.1.100', 'public', 161, load_mibs_list=['ASC_MIB1', 'DMS-MIB'])
print(ntcip.get_oid('dmsMsgTableSource'))