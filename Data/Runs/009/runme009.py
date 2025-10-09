# BEFORE RUNNING PUT SETTINGS,MATERIALS, AND GEOMETRY XML IN FILE!!!

# Bailey Oteri 
# 09/12/25
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.11.0 with library OpenMC Data/LANL/ENDF vii.1
#
# ARO, Boron Concentration = 975 ppm 
# Settings seed = 140211718, temperature = 566.483 K
# Temeprature Settings: method = interpolation, default = temperature,range = 300-600 K, tollerance = 100 K 
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

# Set the path to the cross-sections data - LANL ENDF vii.1 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/media/bailey/DATA/nuclear/data/CrossSectionData/openmc-data/LANL-Based/ENDF71/mcnp_endfb71_Add_O18_C12_C13/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# ============================================================================
# Run OpenMC (save and display output)
# ============================================================================

# --- Change working directory to output_path ---
os.chdir(output_path)

# --- Run OpenMC from within the output directory ---
log_path = "openmc_output.log"
with open(log_path, "w") as log_file:
    process = subprocess.Popen(
        ["/home/bailey/miniconda3/envs/openmc11/bin/openmc"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

    for line in process.stdout:
        print(line, end='')
        log_file.write(line)

    process.wait()

    # Record and log end time
    finish_time = datetime.now()
    log_file.write("Cross-Section Library: OpenMC Data LANL ENDF/B vii.1, Rod Configuration: ARO, Boron Concentration = 975 ppm, Other Notes: None")
    log_file.write(f"=== OpenMC run started at: {start_time} ===\n")
    log_file.write(f"=== OpenMC run finished at: {finish_time} ===\n")    
    print(f"=== OpenMC run started at: {start_time} ===")
    print(f"=== OpenMC run finished at: {finish_time} ===")
