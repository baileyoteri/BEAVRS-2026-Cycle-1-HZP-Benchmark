# Bailey Oteri 
# 10/05/25
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.15.2 with library OpenMC Data/LANL/ENDF vii.1
# Test to see if at 300 K the keff increases or decreases when TSL library is introduced
#
# ARO, Boron Concentration = 975 ppm 
# Settings seed = 140211718, temperature = 300 K
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

# Set the path to the cross-sections data - LANL ENDF vii.1 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/media/bailey/DATA/nuclear/data/CrossSectionData/openmc-data/LANL-Based/ENDF71/mcnp_endfb71_Add_O18_C12_C13/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# ============================================================================
# Build BEAVRS
# ============================================================================
# Change operating temperature for testing
c.operating_temperature = 300

model = BEAVRS(output_path = output_path)

settings = model.get_openmc_settings_file()

# "BEAVRS" in the A0Z25 cipher gives "1 4 0 21 17 18"
settings.seed = 140211718

settings.export_to_xml(output_path)
model.write_openmc_geometry()
# Keeping materials.xml as is written by source code (includes TSL)
model.write_openmc_materials()

# ============================================================================
# Run OpenMC (save and display output)
# ============================================================================

# --- Change working directory to output_path ---
os.chdir(output_path)

# --- Run OpenMC from within the output directory ---
log_path = "openmc_output.log"
with open(log_path, "w") as log_file:
    process = subprocess.Popen(
        ["/home/bailey/miniconda3/envs/openmc15_2/bin/openmc"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

    for line in process.stdout:
        print(line, end='')
        log_file.write(line)

    process.wait()
