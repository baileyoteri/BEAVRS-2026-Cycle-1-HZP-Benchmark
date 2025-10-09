# Bailey Oteri 
# 08/28/25 
# PHYSOR 2026 Paper - BEAVRS on OpenMC v.0.9.0 with library OpenMC Data/LANL/ENDF vii.1
# BEAVRS version 2.0.2
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

# Set the path to the cross-sections data - LANL ENDF vii.1 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/u/af/ao/boteri/nuclear/data/Cross-Section-Lib/OpenMC_10_And_Older/mcnp71_Add_O18_C12_C13/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

# Add print statement to top of output terminal file of details of simulation
print("BEAVRS Version: 2.0.2, Cross-Section Library: OpenMC Data LANL ENDF/B vii.1, Rod Configuration: ARO, Boron Concentration = 975 ppm, Other Notes: None")
# ============================================================================
# Build BEAVRS
# ============================================================================

model = BEAVRS()

model.write_openmc_settings()
model.write_openmc_geometry()
model.write_openmc_materials()
# ============================================================================
# Run OpenMC (save and display output)
# ============================================================================

openmc.run()

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
