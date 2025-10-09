This folder contains the details of each simulation run for the 2026 BEAVRS benchmark, with the code used to run the simulation and the output XML files and a .txt file of the OpenMC output. 
Note: a few runs had to be redone due to missing files so openmc_output.log might have a slightly different keff than reported in the paper, but never more than the uncertainty.

| **Run number** | **BEAVRS version** | **OpenMC Version** | **Cross Section Library** | **Rod Configuration** | **Boron Concentration [ppm]** | **Temperature** | **Temperature Method** | **keff** | **Uncertainty** | **Tables where data used** | **Additional Notes** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **001** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99971 | 0.00004 | Table I, Table II, Table III,   Table IV |  |
| **002** | 3.0.1 | 0.12.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99973 | 0.00005 | Table I  |  |
| **003** | 3.0.0 | 0.10.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 1.00004 | 0.00004 | Table I  |  |
| **004** | 2.0.2 | 0.9.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 1.00046 | 0.00005 | Table I  |  |
| **005** | 3.0.2 (8/2025) | 0.15.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99971 | 0.00004 | Table II | Run using XML files from run001 |
| **006** | 3.0.2 (8/2025) | 0.14.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99971 | 0.00004 | Table II | Run using XML files from run001 |
| **007** | 3.0.2 (8/2025) | 0.13.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99972 | 0.00004 | Table II | Run using XML files from run001 |
| **008** | 3.0.2 (8/2025) | 0.12.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99968 | 0.00004 | Table II | Run using XML files from run001 |
| **009** | 3.0.2 (8/2025) | 0.11.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99977 | 0.00004 | Table II | Run using XML files from run001 |
| **010** | 3.0.2 (8/2025) | 0.10.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99989 | 0.00005 | Table II | Run using XML files from run001   - Cross section library manually built due to change in OpenMC's HDF5 library   format starting at v0.11.0 |
| **011** | 3.0.2 (8/2025) | 0.9.0 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 1.00001 | 0.00004 | Table II | Run using XML files from run001   - Cross section library manually built due to change in OpenMC's HDF5 library   format starting at v0.11.0 |
| **012** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.0 | ARO | 975 | 566 | Interpolation | 1.00008 | 0.00005 | Table III |  |
| **013** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B viii.0 | ARO | 975 | 566 | Interpolation | 1.00129 | 0.00005 | Table III |  |
| **014** | 3.0.2 (8/2025) | 0.15.2 | Offical ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 1.00015 | 0.00004 | Table III |  |
| **015** | 3.0.2 (8/2025) | 0.15.2 | Offical ENDF/B viii.0 | ARO | 975 | 566 | Interpolation | 1.00123 | 0.00004 | Table III |  |
| **016** | 3.0.2 (8/2025) | 0.15.2 | Offical JEFF 3.3 | ARO | 975 | 566 | Interpolation | 1.00405 | 0.00004 | Table III |  |
| **017** | 3.0.2 (8/2025) | 0.15.2 | Other JEFF 3.2 | ARO | 975 | 566 | Interpolation | 0.99927 | 0.00005 | Table III |  |
| **018** | 3.0.2 (8/2025) | 0.15.2 | Other Jeff 3.3  | ARO | 975 | 566 | Interpolation | 1.00362 | 0.00005 | Table III |  |
| **019** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.0 | ARO | 975 | 566 | Interpolation | 0.99981 | 0.00004 | Table III | Remove thermal scattering library (H2O) |
| **020** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99962 | 0.00005 | Table III | Remove thermal scattering library (H2O) |
| **021** | 3.0.2 (8/2025) | 0.15.2 | ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99947 | 0.00004 | Table III | Remove thermal scattering library (H2O) |
| **022** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B viii.0 | ARO | 975 | 566 | Interpolation | 1.00123 | 0.00005 | Table III | Remove thermal scattering library (H2O) |
| **023** | 3.0.2 (8/2025) | 0.15.2 | ENDF/B viii.0 | ARO | 975 | 566 | Interpolation | 1.00121 | 0.00004 | Table III | Remove thermal scattering library (H2O) |
| **024** | 3.0.2 (8/2025) | 0.15.2 | NEA JEFF 3.2 | ARO | 975 | 566 | Interpolation | 0.99848 | 0.00004 | Table III | Remove thermal scattering library (H2O) |
| **025** | 3.0.2 (8/2025) | 0.15.2 | NEA JEFF 3.3 | ARO | 975 | 566 | Interpolation | 1.00335 | 0.00004 | Table III | Remove thermal scattering library (H2O) |
| **026** | 3.0.2 (8/2025) | 0.15.2 | JEFF 3.3 | ARO | 975 | 566 | Interpolation | 1.00330 | 0.00005 | Table III | Remove thermal scattering library (H2O) |
| **027** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 300 | Interpolation | 1.01784 | 0.00004 | Figure 1 |  |
| **028** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 400 | Interpolation | 1.01111 | 0.00004 | Figure 1 |  |
| **029** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 500 | Interpolation | 1.00414 | 0.00005 | Figure 1 |  |
| **030** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 550 | Interpolation | 1.00080 | 0.00004 | Figure 1 |  |
| **031** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Interpolation | 0.99982 | 0.00005 | Figure 1 |  |
| **032** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 600 | Interpolation | 0.99758 | 0.00005 | Figure 1 |  |
| **033** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 300 | Nearest | 1.01834 | 0.00004 | Figure 1 |  |
| **034** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 500 | Nearest | 1.00084 | 0.00004 | Figure 1 |  |
| **035** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 550 | Nearest | 0.99911 | 0.00005 | Figure 1 |  |
| **036** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 566 | Nearest | 0.99911 | 0.00005 | Figure 1 |  |
| **037** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 600 | Nearest | 0.99764 | 0.00005 | Figure 1 |  |
| **038** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | D in | 902 | 566 | Interpolation | 1.00129 | 0.00004 | Table IV |  |
| **039** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | C, D in | 810 | 566 | Interpolation | 1.00045 | 0.00004 | Table IV |  |
| **040** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | A, B, C, D in | 686 | 566 | Interpolation | 0.99871 | 0.00004 | Table IV |  |
| **041** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | A, B, C, D, SE, SD, SC in | 508 | 566 | Interpolation | 0.99717 | 0.00005 | Table IV |  |
| **042** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | D in | 975 | 566 | Interpolation | 0.99200 | 0.00005 | Table IV |  |
| **043** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | C, D in | 902 | 566 | Interpolation | 0.98896 | 0.00004 | Table IV |  |
| **044** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | B, C, D in | 810 | 566 | Interpolation | 0.98844 | 0.00005 | Table IV |  |
| **045** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | A, B, C, D in | 768.09144 | 566 | Interpolation | 0.98840 | 0.00005 | Table IV |  |
| **046** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | A, B, C, D, SE in | 686 | 566 | Interpolation | 0.99388 | 0.00005 | Table IV |  |
| **047** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | A, B, C, D, SE, SD in | 631.32953 | 566 | Interpolation | 0.99272 | 0.00005 | Table IV |  |
| **048** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | A, B, C, D, SE, SD, SC in | 553.502 | 566 | Interpolation | 0.99143 | 0.00004 | Table IV |  |
| **049** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | B, C, D in | 768.09144 | 566 | Interpolation | 0.99382 | 0.00005 | Table IV |  |
| **050** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 300 | Interpolation | 1.01791 | 0.00004 |  | Run at 300 K with TSL for H2O   included - Test to see if at 300 K when TSL is introduced if keff goes up or   down to compare with resutls from run at 566 K and paper publication about   TSL |
| **051** | 3.0.2 (8/2025) | 0.15.2 | LANL ENDF/B vii.1 | ARO | 975 | 300 | Interpolation | 1.01881 | 0.00005 |  | Run at 300 K with TSL for H2O   removed - Test to see if at 300 K when TSL is introduced if keff goes up or   down to compare with resutls from run at 566 K and paper publication about   TSL |
