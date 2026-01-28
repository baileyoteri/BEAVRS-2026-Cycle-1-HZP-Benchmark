# Bailey Oteri 
# 06/26/25
# For OpenMC 0.10.0 and before 
# Convert lib80x and ENDF80SaB (ENDFB/viii.0) from MCNP into HDF5 files for use in OpenMC
# Code from: https://github.com/openmc-dev/data/blob/1e26194e109ce42e7ad7f333c0d0a3aa9b924532/convert_lib80x.py
# Code pushed to OpenMC Dev on Feb 8, 2019
#
# To Use: enter input and output paths for data, use conda enviorment with OpenMC 0.10.0 or earlier (unsure if nessisary)

import argparse
from collections import defaultdict
from pathlib import Path
import sys

import openmc.data

input_path = '/MCNP/MCNP_DATA'
output_path = '/Openmc10_and_older/mcnp80'


# Make sure Python version is sufficient
assert sys.version_info >= (3, 6), "Python 3.6+ is required"

description = """
Convert ENDF/B-VIII.0 ACE data from LANL into an HDF5 library
that can be used by OpenMC. This assumes that you have a directory containing
subdirectories 'Lib80x' and 'ENDF80SaB'.

"""

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass


parser = argparse.ArgumentParser(
    description=description,
    formatter_class=CustomFormatter
)
parser.add_argument('-d', '--destination', type=Path, default=Path('lib80x_hdf5'),
                    help='Directory to create new library in')
parser.add_argument('--libver', choices=['earliest', 'latest'],
                    default='earliest', help="Output HDF5 versioning. Use "
                    "'earliest' for backwards compatibility or 'latest' for "
                    "performance")
parser.add_argument('datadir', type=Path,
                    help='Directory containing Lib80x and ENDF80SaB')
sys.argv = ['convert_Lib80x_HDF5.py', input_path,'-d',output_path]

args = parser.parse_args()
assert args.datadir.is_dir()

# Get a list of all ACE files
lib80x = list(args.datadir.glob('Lib80x/**/*.80?nc'))
lib80sab = list(args.datadir.glob('ENDF80SaB/**/*.??t'))

# Find and fix B10 ACE files
b10files = list(args.datadir.glob('Lib80x/**/5010.80?nc'))
nxs1_position = 523
for filename in b10files:
    with open(filename, 'r+') as fh:
        # Read NXS(1)
        fh.seek(nxs1_position)
        nxs1 = int(fh.read(5))

        # Increase length to match actual length of XSS, but make sure this
        # isn't done twice by checking the current length
        if nxs1 < 86870:
            fh.seek(nxs1_position)
            fh.write(str(nxs1 + 53))

# Group together tables for the same nuclide
tables = defaultdict(list)
for p in sorted(lib80x + lib80sab):
    tables[p.stem].append(p)

# Create output directory if it doesn't exist
args.destination.mkdir(parents=True, exist_ok=True)

library = openmc.data.DataLibrary()

for name, paths in sorted(tables.items()):
    # Convert first temperature for the table
    p = paths[0]
    print(f'Converting: {p}')
    if p.name.endswith('t'):
        data = openmc.data.ThermalScattering.from_ace(p)
    else:
        data = openmc.data.IncidentNeutron.from_ace(p, 'mcnp')

    # For each higher temperature, add cross sections to the existing table
    for p in paths[1:]:
        print(f'Adding: {p}')
        if p.name.endswith('t'):
            data.add_temperature_from_ace(p)
        else:
            data.add_temperature_from_ace(p, 'mcnp')

    # Export HDF5 file
    h5_file = args.destination / f'{data.name}.h5'
    print(f'Writing {h5_file}...')
    data.export_to_hdf5(h5_file, 'w', libver=args.libver)

    # Register with library
    library.register_file(h5_file)

# Write cross_sections.xml
library.export_to_xml(args.destination / 'cross_sections.xml')