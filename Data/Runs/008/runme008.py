# Bailey Oteri 
# 08/13/25 
# PHYSOR 2026 Paper - BEAVRS on OpenMC v0.12.0 with library OpenMC Data/LANL/ENDF vii.1
#
# model.xml read in from run01
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
from datetime import datetime

# Get time of run start
start_time = datetime.now().time()

XML_path =  ""

# Set the path to the cross-sections data - LANL ENDF vii.1 from OpenMC data website with O18, C12, and C13 libs 
# added from LANL ENDF viii.1 from OpenMC data website
library_path = "/u/af/ao/boteri/nuclear/data/Cross-Section-Lib/OpenMC-Data/LANL-Based/mcnp_endfb71_Add_O18_C12_C13/cross_sections.xml"
os.environ["OPENMC_CROSS_SECTIONS"] = library_path

output_path = ""

# Print details of simulation
print("Cross-Section Library: OpenMC Data LANL ENDF/B vii.1, Rod Configuration: ARO, Boron Concentration = 975 ppm, Other Notes: None")

# ============================================================================
# Load existing OpenMC model
# ============================================================================

# Load each file individually
materials = openmc.Materials.from_xml(os.path.join(XML_path, "materials.xml"))
geometry = openmc.Geometry.from_xml(os.path.join(XML_path, "geometry.xml"))
settings = openmc.Settings.from_xml(os.path.join(XML_path, "settings.xml"))

materials.export_to_xml(output_path)
geometry.export_to_xml(output_path)
settings.export_to_xml(output_path)

# ============================================================================
# Run OpenMC
# ============================================================================

openmc.run(cwd=output_path)

# Record and log end time
finish_time = datetime.now()
print(f"=== OpenMC run started at: {start_time} ===")
print(f"=== OpenMC run finished at: {finish_time} ===")
