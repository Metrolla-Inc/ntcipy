import os
import urllib.request

# retreived from https://www.simpleweb.org/ietf/mibs/
# find your missing mib modules here and list them here
missing_mibs = ['RFC-1212', 'RFC1155-SMI', 'SNMPv2-CONF', 'SNMPv2-SMI', 'SNMPv2-TC']
destination_directory = '/your-project-space/NTCIPY/source_mibs/default_mibs'  # Replace with your target directory


def get_default_mibs():
    for mib in missing_mibs:
        url = f'https://simpleweb.org/ietf/mibs/modules/IETF/txt/{mib}'
        destination_path = os.path.join(destination_directory, f'{mib}.mib')
        urllib.request.urlretrieve(url, destination_path)
        print(f'Downloaded {mib} to {destination_path}')


get_default_mibs()