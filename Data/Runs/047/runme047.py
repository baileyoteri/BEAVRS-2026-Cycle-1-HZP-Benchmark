# Bailey Oteri 
# 08/19/25 
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.15.2 with library OpenMC Data/LANL/ENDF vii.1
#
# A, B, C, D, SE, SD in, Boron Concentration = 631.32953 ppm 
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

# Get time of run start to see how long run takes 
start_time = datetime.now().time()

sys.path.append("")
from beavrs.builder import BEAVRS
import beavrs.constants as c

# Set the path to the cross-sections data - LANL ENDF vii.1 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/u/af/ao/boteri/nuclear/data/Cross-Section-Lib/OpenMC-Data/LANL-Based/mcnp_endfb71_Add_O18_C12_C13/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# Add print statement to top of output terminal file of details of simulation
print("Cross-Section Library: OpenMC Data LANL ENDF/B vii.1, Rod Configuration: A, B, C, D, SE, SD in, Boron Concentration = 631.32953 ppm, Other Notes: HZP Bank Worths Calculation")
# ============================================================================
# Build BEAVRS
# ============================================================================
insertions = c.rcca_bank_steps_withdrawn_default

# Insert rod banks A, B, C, D, SE, SD in
insertions['A'] = 0
insertions['B'] = 0
insertions['C'] = 0
insertions['D'] = 0
insertions['SE'] = 0
insertions['SD'] = 0

b = BEAVRS(boron_ppm = 631.32953, rcca_z=insertions, output_path = output_path)

settings = b.get_openmc_settings_file()

# "BEAVRS" in the A0Z25 cipher gives "1 4 0 21 17 18"
settings.seed = 140211718

settings.export_to_xml(output_path)
b.write_openmc_geometry()
b.write_openmc_materials()
# ============================================================================
# Run OpenMC (save and display output)
# ============================================================================

openmc.run(cwd=output_path)

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
