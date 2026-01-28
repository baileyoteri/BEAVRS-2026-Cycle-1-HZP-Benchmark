# Bailey Oteri 
# 06/26/25
# For OpenMC 0.10.0 and before 
# Convert mcnp71 and ENDF71SaB (ENDFB/vii.1) from MCNP into HDF5 files for use in OpenMC
# Code from: https://github.com/openmc-dev/data/blob/1e26194e109ce42e7ad7f333c0d0a3aa9b924532/convert_mcnp71.py
# Code pushed to OpenMC Dev on Feb 8, 2019
#
# To Use: enter input and output paths for data, use conda enviorment with OpenMC 0.10.0 or earlier (unsure if nessisary)

import argparse
from collections import defaultdict
import glob
import os
import sys
import openmc.data

input_path = '/MCNP/MCNP_DATA'
output_path = '/ENDF/Openmc10_and_older/mcnp71'

description = """
Convert ENDF/B-VII.1 ACE data from the MCNP6 distribution into an HDF5 library
that can be used by OpenMC. This assumes that you have a directory containing
subdirectories 'endf71x' and 'ENDF71SaB'.

"""

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass

parser = argparse.ArgumentParser(
    description=description,
    formatter_class=CustomFormatter
)
parser.add_argument('-d', '--destination', default='mcnp_endfb71',
                    help='Directory to create new library in')
parser.add_argument('--libver', choices=['earliest', 'latest'],
                    default='earliest', help="Output HDF5 versioning. Use "
                    "'earliest' for backwards compatibility or 'latest' for "
                    "performance")
parser.add_argument('mcnpdata', help='Directory containing endf71x and ENDF71SaB')
sys.argv = ['convert_mcnp71_HDF5.py', input_path ,'-d',output_path]
args = parser.parse_args()
assert os.path.isdir(args.mcnpdata)

# Get a list of all ACE files
endf71x = glob.glob(os.path.join(args.mcnpdata, 'endf71x', '*', '*.71?nc'))
endf71sab = glob.glob(os.path.join(args.mcnpdata, 'ENDF71SaB' , '*.2?t'))

# There's a bug in H-Zr at 1200 K
# endf71sab.remove(os.path.join(args.mcnpdata, 'ENDF71SaB' , 'h-zr.27t'))

# Group together tables for the same nuclide
suffixes = defaultdict(list)
for filename in sorted(endf71x + endf71sab):
    dirname, basename = os.path.split(filename)
    zaid, xs = basename.split('.')
    suffixes[os.path.join(dirname, zaid)].append(xs)

# Create output directory if it doesn't exist
if not os.path.isdir(args.destination):
    os.mkdir(args.destination)

library = openmc.data.DataLibrary()

for basename, xs_list in sorted(suffixes.items()):
    # Convert first temperature for the table
    filename = '.'.join((basename, xs_list[0]))
    print('Converting: ' + filename)
    if filename.endswith('t'):
        data = openmc.data.ThermalScattering.from_ace(filename)
    else:
        data = openmc.data.IncidentNeutron.from_ace(filename, 'mcnp')

    # For each higher temperature, add cross sections to the existing table
    for xs in xs_list[1:]:
        filename = '.'.join((basename, xs))
        print('Adding: ' + filename)
        if filename.endswith('t'):
            data.add_temperature_from_ace(filename)
        else:
            data.add_temperature_from_ace(filename, 'mcnp')

    # Export HDF5 file
    h5_file = os.path.join(args.destination, data.name + '.h5')
    print('Writing {}...'.format(h5_file))
    data.export_to_hdf5(h5_file, 'w', libver=args.libver)

    # Register with library
    library.register_file(h5_file)

# Write cross_sections.xml
libpath = os.path.join(args.destination, 'cross_sections.xml')
library.export_to_xml(libpath)