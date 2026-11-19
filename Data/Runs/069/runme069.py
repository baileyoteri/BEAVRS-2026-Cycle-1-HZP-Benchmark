# Bailey Oteri 
# 04/27/26

# NSE 2026 Paper - BEAVRS on OpenMC v0.15.2 with library OpenMC Official ENDF/B-VIII.1
#
# A, B, C, D, SE, SD, SC in, Boron Concentration = 508 ppm 
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
import beavrs.constants as c

library_path = "/OpenMC-Data/Offical-Libraries/endfb-viii.1-hdf5/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# ============================================================================
# Build BEAVRS
# ============================================================================
c.rcca_bank_steps_withdrawn_default = {
    'A':  0,
    'B':  0,
    'C':  0,
    'D':  0, # bite position is bank D at 213 steps withdrawn
    'SA': 228,
    'SB': 228,
    'SC': 0,
    'SD': 0,
    'SE': 0,
}
boron = 508
print(f"=== Control Rod Configuration: {c.rcca_bank_steps_withdrawn_default} ===")
print(f"=== Boron PPM: {boron} ===")

model = BEAVRS(boron_ppm =boron, rcca_z = c.rcca_bank_steps_withdrawn_default, output_path = output_path)

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

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
