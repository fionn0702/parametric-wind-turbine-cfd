"""
Section 11B
Write blocks to blockmeshDict
"""

import numpy as np

# Define function to write blocks
def write_blocks(f, blade_offset, num_blades, N, ordered_vertices, disc_vertices_offset, ibm_res_x, ibm_res_y, ibm_res_z, ibm_grading, 
                     csm_res_x, csm_res_y, csm_res_z, csm_grading, csm_grading_inv, cfbm_res_x, cfbm_res_y, cfbm_res_z, cfbm_grading, 
                     cm_res_x, cm_res_y, cm_res_z, cm_grading_x, cm_grading_y, cm_grading_y_inv, gfbm_res_x, gfbm_res_y, gfbm_res_z, gfbm_grading_x, gfbm_grading_x_inv, 
                     gmm_res_x, gmm_res_y, gmm_res_z, gmm_grading, sm_grading, sm_grading_inv, sm_res_x, sm_res_y, sm_res_z, gm_multigrading, gm_multigrading_inv,
                     up_res_x, up_res_y, up_res_z, up_grading, down_res_x, down_res_y, down_res_z, down_grading, write_up_down, write_central, down_grading_rad, down_grading_rad_inv):
    f.write("blocks\n(\n")
        
    #%%
    """
    Blade blocks
    
    """
    
    ibm_cell_resolution = f"{ibm_res_x} {ibm_res_y} {ibm_res_z}" 
    ibm_grading_str = f"1 {ibm_grading} 1"
    test_grading_str = f"1 {ibm_grading} 1"
    
    csm_cell_resolution = f"{csm_res_x} {csm_res_y} {csm_res_z}" 
    csm_grading_str = f"1 {csm_grading} 1"
    testt_grading_str = f"1 {csm_grading} 1"
    csm_grading_str_inv = f"1 {csm_grading_inv} 1"

    
    cfbm_cell_resolution = f"{cfbm_res_x} {cfbm_res_y} {cfbm_res_z}" 
    cfbm_grading_str = f"{cfbm_grading} 1 1"
    
    cm_cell_resolution = f"{cm_res_x} {cm_res_y} {cm_res_z}" 
    cm_grading_str = f"{cm_grading_x} {cm_grading_y} 1"                    # note y-grading here, its same as csm#
    cm_grading_str_inv = f"{cm_grading_x} {cm_grading_y_inv} 1"            # note y-grading here, its same as csm#

    if write_central:
        # Loop through blades and sections
        for blade in range(num_blades):  # Loop over blades (0, 1, 2)
            blade_start = blade * blade_offset  # Calculate starting offset for the current blade
        
            for j in range(N - 1):  # Loop over sections within a single blade
                section_start = j * 56  # Offset for the current section within the blade
                total_offset = blade_start + section_start  # Combine blade and section offsets
                f.write(f"    hex ({17+total_offset} {16+total_offset} {0+total_offset} {1+total_offset} {73+total_offset} {72+total_offset} {56+total_offset} {57+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j}\n")
                f.write(f"    hex ({18+total_offset} {17+total_offset} {1+total_offset} {2+total_offset} {74+total_offset} {73+total_offset} {57+total_offset} {58+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+1}\n")
                f.write(f"    hex ({19+total_offset} {18+total_offset} {2+total_offset} {3+total_offset} {75+total_offset} {74+total_offset} {58+total_offset} {59+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+2}\n")
                f.write(f"    hex ({20+total_offset} {19+total_offset} {3+total_offset} {4+total_offset} {76+total_offset} {75+total_offset} {59+total_offset} {60+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+3}\n")
                f.write(f"    hex ({21+total_offset} {20+total_offset} {4+total_offset} {5+total_offset} {77+total_offset} {76+total_offset} {60+total_offset} {61+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+4}\n")
                f.write(f"    hex ({22+total_offset} {21+total_offset} {5+total_offset} {6+total_offset} {78+total_offset} {77+total_offset} {61+total_offset} {62+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+5}\n")
                f.write(f"    hex ({23+total_offset} {22+total_offset} {6+total_offset} {7+total_offset} {79+total_offset} {78+total_offset} {62+total_offset} {63+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({test_grading_str}) // block {8*j+6}\n")
                f.write(f"    hex ({24+total_offset} {23+total_offset} {7+total_offset} {8+total_offset} {80+total_offset} {79+total_offset} {63+total_offset} {64+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+7}\n")
                f.write(f"    hex ({25+total_offset} {24+total_offset} {8+total_offset} {9+total_offset} {81+total_offset} {80+total_offset} {64+total_offset} {65+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+8}\n")
                f.write(f"    hex ({26+total_offset} {25+total_offset} {9+total_offset} {10+total_offset} {82+total_offset} {81+total_offset} {65+total_offset} {66+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+9}\n")
                f.write(f"    hex ({27+total_offset} {26+total_offset} {10+total_offset} {11+total_offset} {83+total_offset} {82+total_offset} {66+total_offset} {67+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+10}\n")
                f.write(f"    hex ({28+total_offset} {27+total_offset} {11+total_offset} {12+total_offset} {84+total_offset} {83+total_offset} {67+total_offset} {68+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+11}\n")
                f.write(f"    hex ({29+total_offset} {28+total_offset} {12+total_offset} {13+total_offset} {85+total_offset} {84+total_offset} {68+total_offset} {69+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+12}\n")
                f.write(f"    hex ({30+total_offset} {29+total_offset} {13+total_offset} {14+total_offset} {86+total_offset} {85+total_offset} {69+total_offset} {70+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+13}\n")
                f.write(f"    hex ({31+total_offset} {30+total_offset} {14+total_offset} {15+total_offset} {87+total_offset} {86+total_offset} {70+total_offset} {71+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+14}\n")
                f.write(f"    hex ({16+total_offset} {31+total_offset} {15+total_offset} {0+total_offset} {72+total_offset} {87+total_offset} {71+total_offset} {56+total_offset}) rotatingZone ({ibm_cell_resolution}) simpleGrading ({ibm_grading_str}) // block {8*j+15}\n")
    
    
                f.write(f"    hex ({33+total_offset} {32+total_offset} {16+total_offset} {17+total_offset} {89+total_offset} {88+total_offset} {72+total_offset} {73+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")             
                f.write(f"    hex ({34+total_offset} {33+total_offset} {17+total_offset} {18+total_offset} {90+total_offset} {89+total_offset} {73+total_offset} {74+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({35+total_offset} {34+total_offset} {18+total_offset} {36+total_offset} {91+total_offset} {90+total_offset} {74+total_offset} {92+total_offset}) rotatingZone ({cm_cell_resolution}) simpleGrading ({cm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({36+total_offset} {18+total_offset} {19+total_offset} {37+total_offset} {92+total_offset} {74+total_offset} {75+total_offset} {93+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({37+total_offset} {19+total_offset} {20+total_offset} {38+total_offset} {93+total_offset} {75+total_offset} {76+total_offset} {94+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({38+total_offset} {20+total_offset} {21+total_offset} {39+total_offset} {94+total_offset} {76+total_offset} {77+total_offset} {95+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({39+total_offset} {21+total_offset} {22+total_offset} {40+total_offset} {95+total_offset} {77+total_offset} {78+total_offset} {96+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({40+total_offset} {22+total_offset} {42+total_offset} {41+total_offset} {96+total_offset} {78+total_offset} {98+total_offset} {97+total_offset}) rotatingZone ({cm_cell_resolution}) simpleGrading ({cm_grading_str}) // block {8*j+16}\n")
    
                f.write(f"    hex ({22+total_offset} {23+total_offset} {43+total_offset} {42+total_offset} {78+total_offset} {79+total_offset} {99+total_offset} {98+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({testt_grading_str}) // block {8*j+16}\n")             
                f.write(f"    hex ({23+total_offset} {24+total_offset} {44+total_offset} {43+total_offset} {79+total_offset} {80+total_offset} {100+total_offset} {99+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")             
                f.write(f"    hex ({24+total_offset} {25+total_offset} {45+total_offset} {44+total_offset} {80+total_offset} {81+total_offset} {101+total_offset} {100+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")             
                f.write(f"    hex ({25+total_offset} {26+total_offset} {46+total_offset} {45+total_offset} {81+total_offset} {82+total_offset} {102+total_offset} {101+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")             
    
                f.write(f"    hex ({26+total_offset} {48+total_offset} {47+total_offset} {46+total_offset} {82+total_offset} {104+total_offset} {103+total_offset} {102+total_offset}) rotatingZone ({cm_cell_resolution}) simpleGrading ({cm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({27+total_offset} {49+total_offset} {48+total_offset} {26+total_offset} {83+total_offset} {105+total_offset} {104+total_offset} {82+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({28+total_offset} {50+total_offset} {49+total_offset} {27+total_offset} {84+total_offset} {106+total_offset} {105+total_offset} {83+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({29+total_offset} {51+total_offset} {50+total_offset} {28+total_offset} {85+total_offset} {107+total_offset} {106+total_offset} {84+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({30+total_offset} {52+total_offset} {51+total_offset} {29+total_offset} {86+total_offset} {108+total_offset} {107+total_offset} {85+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({54+total_offset} {53+total_offset} {52+total_offset} {30+total_offset} {110+total_offset} {109+total_offset} {108+total_offset} {86+total_offset}) rotatingZone ({cm_cell_resolution}) simpleGrading ({cm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({55+total_offset} {54+total_offset} {30+total_offset} {31+total_offset} {111+total_offset} {110+total_offset} {86+total_offset} {87+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")
                f.write(f"    hex ({32+total_offset} {55+total_offset} {31+total_offset} {16+total_offset} {88+total_offset} {111+total_offset} {87+total_offset} {72+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str}) // block {8*j+16}\n")
    
                # f.write(f"    hex ({46+total_offset} {60+total_offset} {61+total_offset} {47+total_offset} {14+total_offset} {+total_offset} {29+total_offset} {15+total_offset}) rotatingZone ({cfbm_cell_resolution}) simpleGrading ({cfbm_grading_str}) // block {8*j+17}\n")
                # f.write(f"    hex ({47+total_offset} {61+total_offset} {62+total_offset} {63+total_offset} {15+total_offset} {29+total_offset} {30+total_offset} {31+total_offset}) rotatingZone ({cm_cell_resolution}) simpleGrading ({cm_grading_str_inv}) // block {8*j+18}\n")
                # f.write(f"    hex ({40+total_offset} {47+total_offset} {63+total_offset} {48+total_offset} {8+total_offset} {15+total_offset} {31+total_offset} {16+total_offset}) rotatingZone ({csm_cell_resolution}) simpleGrading ({csm_grading_str_inv}) // block {8*j+19}\n")
        f.write("\n")
  
    #%%
    """
    Gap blocks
    """
    
    
    gfbm_cell_resolution = f"{gfbm_res_x} {gfbm_res_y} {gfbm_res_z}" 
    gfbm_grading_str = f"{gfbm_grading_x} ({gm_multigrading} {gm_multigrading_inv}) 1"              # multigrading in local y (higher density toward blades)
    gfbm_grading_str_inv = f"{gfbm_grading_x_inv} ({gm_multigrading} {gm_multigrading_inv}) 1"

    gmm_cell_resolution = f"{gmm_res_x} {gmm_res_y} {gmm_res_z}"
    gmm_grading_str = f"{gmm_grading} ({gm_multigrading} {gm_multigrading_inv}) 1"
    
    if write_central:
        for j in range(N - 1):  
            offset = j * 56  # Offset for each section
        
            # Compute dynamic indices
            blade3_base = N * 56 * 2  # Start index for Blade 3
            blade2_base = N * 56  # Start index for Blade 2
            blade1_base = 0  # Blade 1 starts at index 0
        
            # gap 1 (top right)
            f.write(f"    hex ({46+offset} {47+offset} {blade3_base+53+offset} {blade3_base+54+offset} {102+offset} {103+offset} {blade3_base+109+offset} {blade3_base+110+offset}) rotatingZone ({gfbm_cell_resolution}) simpleGrading ({gfbm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({45+offset} {46+offset} {blade3_base+54+offset} {blade3_base+55+offset} {101+offset} {102+offset} {blade3_base+110+offset} {blade3_base+111+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({44+offset} {45+offset} {blade3_base+55+offset} {blade3_base+32+offset} {100+offset} {101+offset} {blade3_base+111+offset} {blade3_base+88+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({43+offset} {44+offset} {blade3_base+32+offset} {blade3_base+33+offset} {99+offset} {100+offset} {blade3_base+88+offset} {blade3_base+89+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({42+offset} {43+offset} {blade3_base+33+offset} {blade3_base+34+offset} {98+offset} {99+offset} {blade3_base+89+offset} {blade3_base+90+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({41+offset} {42+offset} {blade3_base+34+offset} {blade3_base+35+offset} {97+offset} {98+offset} {blade3_base+90+offset} {blade3_base+91+offset}) rotatingZone ({gfbm_cell_resolution}) simpleGrading ({gfbm_grading_str}) // block {8*j+12}\n")
    
           
            # gap 2 (bottom)
            f.write(f"    hex ({blade2_base+110+offset} {blade2_base+109+offset} {blade3_base+103+offset} {blade3_base+102+offset} {blade2_base+54+offset} {blade2_base+53+offset} {blade3_base+47+offset} {blade3_base+46+offset}) rotatingZone ({gfbm_cell_resolution}) simpleGrading ({gfbm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+111+offset} {blade2_base+110+offset} {blade3_base+102+offset} {blade3_base+101+offset} {blade2_base+55+offset} {blade2_base+54+offset} {blade3_base+46+offset} {blade3_base+45+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+88+offset} {blade2_base+111+offset} {blade3_base+101+offset} {blade3_base+100+offset} {blade2_base+32+offset} {blade2_base+55+offset} {blade3_base+45+offset} {blade3_base+44+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+89+offset} {blade2_base+88+offset} {blade3_base+100+offset} {blade3_base+99+offset} {blade2_base+33+offset} {blade2_base+32+offset} {blade3_base+44+offset} {blade3_base+43+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+90+offset} {blade2_base+89+offset} {blade3_base+99+offset} {blade3_base+98+offset} {blade2_base+34+offset} {blade2_base+33+offset} {blade3_base+43+offset} {blade3_base+42+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+91+offset} {blade2_base+90+offset} {blade3_base+98+offset} {blade3_base+97+offset} {blade2_base+35+offset} {blade2_base+34+offset} {blade3_base+42+offset} {blade3_base+41+offset}) rotatingZone ({gfbm_cell_resolution}) simpleGrading ({gfbm_grading_str}) // block {8*j+12}\n")
    
            
            # gap 3 (top left)
            f.write(f"    hex ({blade2_base+46+offset} {blade2_base+47+offset} {53+offset} {54+offset} {blade2_base+102+offset} {blade2_base+103+offset} {109+offset} {110+offset}) rotatingZone ({gfbm_cell_resolution}) simpleGrading ({gfbm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+45+offset} {blade2_base+46+offset} {54+offset} {55+offset} {blade2_base+101+offset} {blade2_base+102+offset} {110+offset} {111+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+44+offset} {blade2_base+45+offset} {55+offset} {32+offset} {blade2_base+100+offset} {blade2_base+101+offset} {111+offset} {88+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+43+offset} {blade2_base+44+offset} {32+offset} {33+offset} {blade2_base+99+offset} {blade2_base+100+offset} {88+offset} {89+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+42+offset} {blade2_base+43+offset} {33+offset} {34+offset} {blade2_base+98+offset} {blade2_base+99+offset} {89+offset} {90+offset}) rotatingZone ({gmm_cell_resolution}) simpleGrading ({gmm_grading_str}) // block {8*j+12}\n")
            f.write(f"    hex ({blade2_base+41+offset} {blade2_base+42+offset} {34+offset} {35+offset} {blade2_base+97+offset} {blade2_base+98+offset} {90+offset} {91+offset}) rotatingZone ({gfbm_cell_resolution}) simpleGrading ({gfbm_grading_str}) // block {8*j+12}\n")

    #%%
    """
    Surrounding mesh (around disc for fixedAMI)
    """
    
    # Cell resolution, x and y interchange due to block definition (relative x and y axis)
    sm_cell_resolution_TB = f"{sm_res_x} {sm_res_y} {sm_res_z}" # Top and Bottom
    sm_cell_resolution_LR = f"{sm_res_y} {sm_res_x} {sm_res_z}" # Left and Right
    
    # Define grading for different blocks as space-separated strings
    sm_grading_bottom = f"1 {sm_grading_inv} (0.25 4)"
    sm_grading_left   = f"{sm_grading_inv} 1 (0.25 4)"
    sm_grading_right  = f"{sm_grading} 1 (0.25 4)"
    sm_grading_top    = f"1 {sm_grading} (0.25 4)"
    
    if write_central:
        f.write(f"    hex ({4 + disc_vertices_offset} {5 + disc_vertices_offset} {15 + disc_vertices_offset} {14 + disc_vertices_offset} {0 + disc_vertices_offset} {1 + disc_vertices_offset} {11 + disc_vertices_offset} {10 + disc_vertices_offset} ) fixedZone ({sm_cell_resolution_TB}) simpleGrading ({sm_grading_bottom}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({4 + disc_vertices_offset} {14 + disc_vertices_offset} {13 + disc_vertices_offset} {7 + disc_vertices_offset} {0 + disc_vertices_offset} {10 + disc_vertices_offset} {9 + disc_vertices_offset} {3 + disc_vertices_offset} ) fixedZone ({sm_cell_resolution_LR}) simpleGrading ({sm_grading_left}) // block {8*j+12}\n")      # left
        f.write(f"    hex ({15 + disc_vertices_offset} {5 + disc_vertices_offset} {6 + disc_vertices_offset} {12 + disc_vertices_offset} {11 + disc_vertices_offset} {1 + disc_vertices_offset} {2 + disc_vertices_offset} {8 + disc_vertices_offset} ) fixedZone ({sm_cell_resolution_LR}) simpleGrading ({sm_grading_right}) // block {8*j+12}\n")     # right
        f.write(f"    hex ({13 + disc_vertices_offset} {12 + disc_vertices_offset} {6 + disc_vertices_offset} {7 + disc_vertices_offset} {9 + disc_vertices_offset} {8 + disc_vertices_offset} {2 + disc_vertices_offset} {3 + disc_vertices_offset} ) fixedZone ({sm_cell_resolution_TB}) simpleGrading ({sm_grading_top}) // block {8*j+12}\n")        # top
   
    #%%
    """
    Upstream
    """
    
    # Cell resolution, x and y interchange due to block definition (relative x and y axis)
    up_cell_resolution_TB = f"{np.ceil(up_res_x)} {np.ceil(up_res_y)} {np.ceil(up_res_z)}" # Top and Bottom
    up_cell_resolution_LR = f"{np.ceil(up_res_y)} {np.ceil(up_res_x)} {np.ceil(up_res_z)}" # Left and Right
    
    # Define grading for different blocks as space-separated strings
    up_grading_bottom = f"1 {sm_grading_inv} {up_grading}"
    up_grading_left   = f"{sm_grading_inv} 1 {up_grading}"
    up_grading_right  = f"{sm_grading} 1 {up_grading}"
    up_grading_top    = f"1 {sm_grading} {up_grading}"
    
    innerup_cell_resolution = f"{np.ceil(up_res_x)} {np.ceil(up_res_y)} {np.ceil(up_res_z)}"
    innerup_grading_all = f"1 1 {up_grading}"
    poloup_cell_resolution = f"{np.ceil(up_res_x/5)} {np.ceil(up_res_y/5)} {np.ceil(up_res_z)}" #f"5 1 {up_res_z}"
    poloupsquare_cell_resolution = f"{np.ceil(up_res_x/5)} {np.ceil(up_res_x/5)} {np.ceil(up_res_z)}" #f"5 5 {up_res_z}"
    j = 0
    if write_up_down:
        # outer
        f.write(f"    hex ({48 + disc_vertices_offset} {49 + disc_vertices_offset} {55 + disc_vertices_offset} {54 + disc_vertices_offset} {16 + disc_vertices_offset} {17 + disc_vertices_offset} {23 + disc_vertices_offset} {22 + disc_vertices_offset}) fixedZone ({up_cell_resolution_TB}) simpleGrading ({up_grading_bottom}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({48 + disc_vertices_offset} {54 + disc_vertices_offset} {53 + disc_vertices_offset} {51 + disc_vertices_offset} {16 + disc_vertices_offset} {22 + disc_vertices_offset} {21 + disc_vertices_offset} {19 + disc_vertices_offset}) fixedZone ({up_cell_resolution_LR}) simpleGrading ({up_grading_left}) // block {8*j+12}\n")      # left
        f.write(f"    hex ({55 + disc_vertices_offset} {49 + disc_vertices_offset} {50 + disc_vertices_offset} {52 + disc_vertices_offset} {23 + disc_vertices_offset} {17 + disc_vertices_offset} {18 + disc_vertices_offset} {20 + disc_vertices_offset}) fixedZone ({up_cell_resolution_LR}) simpleGrading ({up_grading_right}) // block {8*j+12}\n")     # right
        f.write(f"    hex ({53 + disc_vertices_offset} {52 + disc_vertices_offset} {50 + disc_vertices_offset} {51 + disc_vertices_offset} {21 + disc_vertices_offset} {20 + disc_vertices_offset} {18 + disc_vertices_offset} {19 + disc_vertices_offset}) fixedZone ({up_cell_resolution_TB}) simpleGrading ({up_grading_top}) // block {8*j+12}\n")        # top
        
        # inner
        f.write(f"    hex ({54 + disc_vertices_offset} {55 + disc_vertices_offset} {35 + disc_vertices_offset} {34 + disc_vertices_offset} {22 + disc_vertices_offset} {23 + disc_vertices_offset} {39 + disc_vertices_offset} {38 + disc_vertices_offset}) fixedZone ({innerup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({53 + disc_vertices_offset} {54 + disc_vertices_offset} {34 + disc_vertices_offset} {33 + disc_vertices_offset} {21 + disc_vertices_offset} {22 + disc_vertices_offset} {38 + disc_vertices_offset} {37 + disc_vertices_offset}) fixedZone ({innerup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({55 + disc_vertices_offset} {52 + disc_vertices_offset} {32 + disc_vertices_offset} {35 + disc_vertices_offset} {23 + disc_vertices_offset} {20 + disc_vertices_offset} {36 + disc_vertices_offset} {39 + disc_vertices_offset}) fixedZone ({innerup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({52 + disc_vertices_offset} {53 + disc_vertices_offset} {33 + disc_vertices_offset} {32 + disc_vertices_offset} {20 + disc_vertices_offset} {21 + disc_vertices_offset} {37 + disc_vertices_offset} {36 + disc_vertices_offset}) fixedZone ({innerup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
     
        # up central cylinder (polo mints)
        f.write(f"    hex ({82 + disc_vertices_offset} {83 + disc_vertices_offset} {67 + disc_vertices_offset} {66 + disc_vertices_offset} {86 + disc_vertices_offset} {87 + disc_vertices_offset} {71 + disc_vertices_offset} {70 + disc_vertices_offset}) fixedZone ({poloup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({81 + disc_vertices_offset} {82 + disc_vertices_offset} {66 + disc_vertices_offset} {65 + disc_vertices_offset} {85 + disc_vertices_offset} {86 + disc_vertices_offset} {70 + disc_vertices_offset} {69 + disc_vertices_offset}) fixedZone ({poloup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({83 + disc_vertices_offset} {80 + disc_vertices_offset} {64 + disc_vertices_offset} {67 + disc_vertices_offset} {87 + disc_vertices_offset} {84 + disc_vertices_offset} {68 + disc_vertices_offset} {71 + disc_vertices_offset}) fixedZone ({poloup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({80 + disc_vertices_offset} {81 + disc_vertices_offset} {65 + disc_vertices_offset} {64 + disc_vertices_offset} {84 + disc_vertices_offset} {85 + disc_vertices_offset} {69 + disc_vertices_offset} {68 + disc_vertices_offset}) fixedZone ({poloup_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({66 + disc_vertices_offset} {67 + disc_vertices_offset} {64 + disc_vertices_offset} {65 + disc_vertices_offset} {70 + disc_vertices_offset} {71 + disc_vertices_offset} {68 + disc_vertices_offset} {69 + disc_vertices_offset}) fixedZone ({poloupsquare_cell_resolution}) simpleGrading ({innerup_grading_all}) // block {8*j+12}\n")   # bottom

    #%%
    """
    Downstream
    """
    # Cell resolution, x and y interchange due to block definition (relative x and y axis)
    down_cell_resolution_TB = f"{np.ceil(down_res_x)} {np.ceil(down_res_y)} {np.ceil(down_res_z)}" # Top and Bottom
    down_cell_resolution_LR = f"{np.ceil(down_res_y)} {np.ceil(down_res_x)} {np.ceil(down_res_z)}" # Left and Right
    
    # Define grading for different blocks as space-separated strings
    down_grading_bottom = f"1 {down_grading_rad_inv} {down_grading}"
    down_grading_left   = f"{down_grading_rad_inv} 1 {down_grading}"
    down_grading_right  = f"{down_grading_rad} 1 {down_grading}"
    down_grading_top    = f"1 {down_grading_rad} {down_grading}"
    
    innerdown_cell_resolution = f"{np.ceil(down_res_x)} {np.ceil(down_res_y)} {np.ceil(down_res_z)}"
    innerdown_grading_all = f"1 1 {down_grading}"
    polodown_cell_resolution = f"{np.ceil(down_res_x/10)} {np.ceil(down_res_y/4)} {np.ceil(down_res_z)}" #f"5 1 {down_res_z}"
    polodownsquare_cell_resolution = f"{np.ceil(down_res_x/10)} {np.ceil(down_res_x/10)} {np.ceil(down_res_z)}" #f"5 5 {down_res_z}"
    
    if write_up_down:
        #inner
        f.write(f"    hex ({24 + disc_vertices_offset} {25 + disc_vertices_offset} {31 + disc_vertices_offset} {30 + disc_vertices_offset} {56 + disc_vertices_offset} {57 + disc_vertices_offset} {63 + disc_vertices_offset} {62 + disc_vertices_offset}) fixedZone ({down_cell_resolution_TB}) simpleGrading ({down_grading_bottom}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({24 + disc_vertices_offset} {30 + disc_vertices_offset} {29 + disc_vertices_offset} {27 + disc_vertices_offset} {56 + disc_vertices_offset} {62 + disc_vertices_offset} {61 + disc_vertices_offset} {59 + disc_vertices_offset}) fixedZone ({down_cell_resolution_LR}) simpleGrading ({down_grading_left}) // block {8*j+12}\n")      # left
        f.write(f"    hex ({31 + disc_vertices_offset} {25 + disc_vertices_offset} {26 + disc_vertices_offset} {28 + disc_vertices_offset} {63 + disc_vertices_offset} {57 + disc_vertices_offset} {58 + disc_vertices_offset} {60 + disc_vertices_offset} ) fixedZone ({down_cell_resolution_LR}) simpleGrading ({down_grading_right}) // block {8*j+12}\n")     # right
        f.write(f"    hex ({29 + disc_vertices_offset} {28 + disc_vertices_offset} {26 + disc_vertices_offset} {27 + disc_vertices_offset} {61 + disc_vertices_offset} {60 + disc_vertices_offset} {58 + disc_vertices_offset} {59 + disc_vertices_offset} ) fixedZone ({down_cell_resolution_TB}) simpleGrading ({down_grading_top}) // block {8*j+12}\n")        # top
        
        #outer
        f.write(f"    hex ({30 + disc_vertices_offset} {31 + disc_vertices_offset} {47 + disc_vertices_offset} {46 + disc_vertices_offset} {62 + disc_vertices_offset} {63 + disc_vertices_offset} {43 + disc_vertices_offset} {42 + disc_vertices_offset}) fixedZone ({innerdown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({29 + disc_vertices_offset} {30 + disc_vertices_offset} {46 + disc_vertices_offset} {45 + disc_vertices_offset} {61 + disc_vertices_offset} {62 + disc_vertices_offset} {42 + disc_vertices_offset} {41 + disc_vertices_offset}) fixedZone ({innerdown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({31 + disc_vertices_offset} {28 + disc_vertices_offset} {44 + disc_vertices_offset} {47 + disc_vertices_offset} {63 + disc_vertices_offset} {60 + disc_vertices_offset} {40 + disc_vertices_offset} {43 + disc_vertices_offset}) fixedZone ({innerdown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({28 + disc_vertices_offset} {29 + disc_vertices_offset} {45 + disc_vertices_offset} {44 + disc_vertices_offset} {60 + disc_vertices_offset} {61 + disc_vertices_offset} {41 + disc_vertices_offset} {40 + disc_vertices_offset}) fixedZone ({innerdown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
     
        # down central cylinder (polo mints)
        f.write(f"    hex ({94 + disc_vertices_offset} {95 + disc_vertices_offset} {79 + disc_vertices_offset} {78 + disc_vertices_offset} {90 + disc_vertices_offset} {91 + disc_vertices_offset} {75 + disc_vertices_offset} {74 + disc_vertices_offset}) fixedZone ({polodown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({93 + disc_vertices_offset} {94 + disc_vertices_offset} {78 + disc_vertices_offset} {77 + disc_vertices_offset} {89 + disc_vertices_offset} {90 + disc_vertices_offset} {74 + disc_vertices_offset} {73 + disc_vertices_offset}) fixedZone ({polodown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({95 + disc_vertices_offset} {92 + disc_vertices_offset} {76 + disc_vertices_offset} {79 + disc_vertices_offset} {91 + disc_vertices_offset} {88 + disc_vertices_offset} {72 + disc_vertices_offset} {75 + disc_vertices_offset}) fixedZone ({polodown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({92 + disc_vertices_offset} {93 + disc_vertices_offset} {77 + disc_vertices_offset} {76 + disc_vertices_offset} {88 + disc_vertices_offset} {89 + disc_vertices_offset} {73 + disc_vertices_offset} {72 + disc_vertices_offset}) fixedZone ({polodown_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom
        f.write(f"    hex ({78 + disc_vertices_offset} {79 + disc_vertices_offset} {76 + disc_vertices_offset} {77 + disc_vertices_offset} {74 + disc_vertices_offset} {75 + disc_vertices_offset} {72 + disc_vertices_offset} {73 + disc_vertices_offset}) fixedZone ({polodownsquare_cell_resolution}) simpleGrading ({innerdown_grading_all}) // block {8*j+12}\n")   # bottom

    
    #%%
    f.write(");\n\n")