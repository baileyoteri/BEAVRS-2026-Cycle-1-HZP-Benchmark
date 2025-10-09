# Bailey Oteri 
# 09/22/25 
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.15.2 with library OpenMC Data/LANL/ENDF vii.1
#
# ARO, Boron Concentration = 975 ppm 
# Settings seed = 140211718, temperature = 566 K
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

# Get time of run start
start_time = datetime.now().time()

sys.path.append("")
from beavrs.builder import BEAVRS
import beavrs.constants as c 

# Set the path to the cross-sections data - LANL ENDF vii.1 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/u/af/ao/boteri/nuclear/data/Cross-Section-Lib/OpenMC-Data/LANL-Based/mcnp_endfb71_Add_O18_C12_C13/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

print("Cross-Section Library: LANL ENDF/B vii.1, Rod Configuration: ARO, Boron Concentration = 975 ppm, Other Notes: temperature set to 566 K, temp method interpolation")
# ============================================================================
# Build BEAVRS
# ============================================================================

# Change operating temperature for testing
c.operating_temperature = 566

model = BEAVRS(output_path = output_path)

settings = model.get_openmc_settings_file()

# "BEAVRS" in the A0Z25 cipher gives "1 4 0 21 17 18"
settings.seed = 140211718

settings.export_to_xml(output_path)
model.write_openmc_geometry()
model.write_openmc_materials()

# ============================================================================
# Run OpenMC
# ============================================================================

openmc.run(cwd=output_path)

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
