# Bailey Oteri 
# 04/27/26

# NSE 2026 Paper - BEAVRS on OpenMC v0.15.2 with library LANL Based ENDF/B-VIII.1
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
import subprocess

# Get time of run start to see how long run takes (using 40 CPU cores)
start_time = datetime.now().time()

sys.path.append("")
from beavrs.builder import BEAVRS

library_path = "/LANL-Based/lib81x_hdf5/lib81x_hdf5/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# ============================================================================
# Build BEAVRS
# ============================================================================

model = BEAVRS(output_path = output_path)

settings = model.get_openmc_settings_file()

# "BEAVRS" in the A0Z25 cipher gives "1 4 0 21 17 18"
settings.seed = 140211718
settings.particles = 4000000

settings.export_to_xml(output_path)
model.write_openmc_geometry()
model.write_openmc_materials()
# ============================================================================
# Run OpenMC (save and display output)
# ============================================================================

openmc.run(cwd=output_path)
