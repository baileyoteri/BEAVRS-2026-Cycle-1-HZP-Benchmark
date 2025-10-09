# Bailey Oteri 
# 08/14/25 
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.15.2 with library OpenMC Data/Offical Library/ENDF viii.0
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
import sys
from datetime import datetime

# Get time of run start to see how long run takes (using 40 CPU cores)
start_time = datetime.now().time()

sys.path.append("")
from beavrs.builder import BEAVRS

# Set the path to the cross-sections data - Offical Libraries ENDF viii.0 from OpenMC data website
library_path = "/u/af/ao/boteri/nuclear/data/Cross-Section-Lib/OpenMC-Data/Offical-Libraries/endfb-viii.0-hdf5/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# Add print statement to top of output terminal file of details of simulation
print("Cross-Section Library: OpenMC Data Offical Libraries ENDF/B viii.0, Rod Configuration: ARO, Boron Concentration = 975 ppm, Other Notes: None")
# ============================================================================
# Build BEAVRS
# ============================================================================

model = BEAVRS(output_path = output_path)

settings = model.get_openmc_settings_file()

# "BEAVRS" in the A0Z25 cipher gives "1 4 0 21 17 18"
settings.seed = 140211718

settings.export_to_xml(output_path)
model.write_openmc_geometry()
model.write_openmc_materials()
# ============================================================================
# Run OpenMC (save and display output)
# ============================================================================

openmc.run(cwd=output_path)

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
