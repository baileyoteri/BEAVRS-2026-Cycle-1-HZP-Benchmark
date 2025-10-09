# Bailey Oteri 
# 09/22/25 
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.15.2 with library OpenMC Data/LANL/ENDF viii.0, no thermal scattering data
#
# ARO, Boron Concentration = 975 ppm 
# Settings seed = 140211718, temperature = 566.483 K
# Temeprature Settings: method = interpolation, default = temperature,range = 300-600 K, tollerance = 100 K (from public BEAVRS commit bd42888)
# Particle Settings: 350 batches, 250 inactive, 4E6 particles
#
# ============================================================================
# Initialization 
# ============================================================================
import os  
import openmc  
import  sys
from datetime import datetime
import xml.etree.ElementTree as ET

# Get time of run start
start_time = datetime.now().time()

sys.path.append("")
from beavrs.builder import BEAVRS
import beavrs.constants as c 

# Set the path to the cross-sections data - LANL ENDF viii.0 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/u/af/ao/boteri/nuclear/data/Cross-Section-Lib/OpenMC-Data/LANL-Based/lib80x_hdf5/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

print("Cross-Section Library: LANL ENDF/B viii.0 with no thermal scattering data, Rod Configuration: ARO, Boron Concentration = 975 ppm, Other Notes: N/A")
# ============================================================================
# Build BEAVRS
# ============================================================================

# Change operating temperature for testing
c.operating_temperature = 566.483

model = BEAVRS(output_path = output_path)

settings = model.get_openmc_settings_file()

# "BEAVRS" in the A0Z25 cipher gives "1 4 0 21 17 18"
settings.seed = 140211718

settings.export_to_xml(output_path)
model.write_openmc_geometry()
model.write_openmc_materials()

# ============================================================================
# Remove thermal scattering from water materials 
# ============================================================================

# Parse the materials.xml file
tree = ET.parse(output_path + '/materials.xml')
root = tree.getroot()

# Iterate through each material in the XML file
for material in root.findall('material'):
    
    # Check if the material is "Borated Water"
    if material.get('id') == '15' and material.get('name') == 'Borated Water':
        # Find the <sab> element within this specific material
        sab_to_remove = None
        for sab in material.findall('sab'):
            if sab.get('name') == 'c_H_in_H2O':
                sab_to_remove = sab
                break
        
        # If the sab element is found, remove it
        if sab_to_remove is not None:
            material.remove(sab_to_remove)
            
    # Check if the material is "Water SPN"
    elif material.get('id') == '16' and material.get('name') == 'Water SPN':
        # Find the <sab> element within this specific material
        sab_to_remove = None
        for sab in material.findall('sab'):
            if sab.get('name') == 'c_H_in_H2O':
                sab_to_remove = sab
                break
        
        # If the sab element is found, remove it
        if sab_to_remove is not None:
            material.remove(sab_to_remove)
        
# Save the modified XML back to the file
tree.write(output_path + '/materials.xml')

# ============================================================================
# Run OpenMC
# ============================================================================

openmc.run(cwd=output_path)

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
