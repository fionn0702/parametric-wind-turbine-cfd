"""
Section 11P
Write Patches to blockmeshDict
"""

def write_patches(f, num_blades, N, disc_vertices_offset, write_up_down, write_central):
    
    f.write("boundary\n(\n")
    
    #%%
    """
    Blades
    """
    
    if write_central:
        # Loop through blades
        for blade in range(num_blades):  # Blade 1, 2, 3
            blade_name = f"blade{blade + 1}"  # Name of the patch
            blade_start = blade * N * 56  # Starting offset for the blade
            
            f.write(f"    {blade_name}\n")
            f.write("    {\n")
            f.write("        type wall;\n")
            f.write("        faces\n        (\n")
            
            # Loop through sections in this blade
            for j in range(N - 1):
                section_start = j * 56
                total_offset = blade_start + section_start
        
                # Write the faces that define the blade's surface
                f.write(f"            ({0+total_offset} {56+total_offset} {57+total_offset} {1+total_offset})\n")
                f.write(f"            ({1+total_offset} {57+total_offset} {58+total_offset} {2+total_offset})\n")
                f.write(f"            ({2+total_offset} {58+total_offset} {59+total_offset} {3+total_offset})\n")
                f.write(f"            ({3+total_offset} {59+total_offset} {60+total_offset} {4+total_offset})\n")
                f.write(f"            ({4+total_offset} {60+total_offset} {61+total_offset} {5+total_offset})\n")
                f.write(f"            ({5+total_offset} {61+total_offset} {62+total_offset} {6+total_offset})\n")
                f.write(f"            ({6+total_offset} {62+total_offset} {63+total_offset} {7+total_offset})\n")
                f.write(f"            ({7+total_offset} {63+total_offset} {64+total_offset} {8+total_offset})\n")
                f.write(f"            ({8+total_offset} {64+total_offset} {65+total_offset} {9+total_offset})\n")
                f.write(f"            ({9+total_offset} {65+total_offset} {66+total_offset} {10+total_offset})\n")
                f.write(f"            ({10+total_offset} {66+total_offset} {67+total_offset} {11+total_offset})\n")
                f.write(f"            ({11+total_offset} {67+total_offset} {68+total_offset} {12+total_offset})\n")
                f.write(f"            ({12+total_offset} {68+total_offset} {69+total_offset} {13+total_offset})\n")
                f.write(f"            ({13+total_offset} {69+total_offset} {70+total_offset} {14+total_offset})\n")
                f.write(f"            ({14+total_offset} {70+total_offset} {71+total_offset} {15+total_offset})\n")
                f.write(f"            ({15+total_offset} {71+total_offset} {56+total_offset} {0+total_offset})\n")
    
    
            f.write("        );\n")
            f.write("    }\n")
        
    
    #%%
    """
    ROTATINGAMI
    """
    
    if write_central:
        # ROTATINGAMI
        f.write("    rotatingAMI\n")
        f.write("    {\n")
        f.write("        type cyclicAMI;\n") # CHANGE BACK TO cyclicAMI
        f.write("        neighbourPatch fixedAMI;\n")
        f.write("        transform noOrdering;\n")
        f.write("        faces\n        (\n")
    
    
        # facing UP Blades
        for blade in range(num_blades):  # 0,1,2
            blade_start = blade * N * 56  # Starting offset for the blade
            
            
            for j in range(N-1):
                i_offset = j * 56  # Adjust vertices for each section
                inlet_offset = blade_start + i_offset
                
                f.write(f"            ({47+inlet_offset} {103+inlet_offset} {104+inlet_offset} {48+inlet_offset})\n")
                f.write(f"            ({48+inlet_offset} {104+inlet_offset} {105+inlet_offset} {49+inlet_offset})\n")
                f.write(f"            ({49+inlet_offset} {105+inlet_offset} {106+inlet_offset} {50+inlet_offset})\n")
                f.write(f"            ({50+inlet_offset} {106+inlet_offset} {107+inlet_offset} {51+inlet_offset})\n")
                f.write(f"            ({51+inlet_offset} {107+inlet_offset} {108+inlet_offset} {52+inlet_offset})\n")
                f.write(f"            ({52+inlet_offset} {108+inlet_offset} {109+inlet_offset} {53+inlet_offset})\n")
    
    
        # facing UP Gap
        for j in range(N-1):
            gap_inlet_offset = j * 56  # Adjust vertices for each section
            # Compute dynamic indices
            blade3_base = N * 56 * 2  # Start index for Blade 3
            blade2_base = N * 56  # Start index for Blade 2
            blade1_base = 0  # Blade 1 starts at index 0
    
            # top left
            f.write(f"            ({53+gap_inlet_offset} {109+gap_inlet_offset} {blade2_base+103+gap_inlet_offset} {blade2_base+47+gap_inlet_offset})\n")
            # top right
            f.write(f"            ({47+gap_inlet_offset} {blade3_base+53+gap_inlet_offset} {blade3_base+109+gap_inlet_offset} {103+gap_inlet_offset})\n")
            # bottom
            f.write(f"            ({blade3_base+47+gap_inlet_offset} {blade2_base+53+gap_inlet_offset} {blade2_base+109+gap_inlet_offset} {blade3_base+103+gap_inlet_offset})\n")
    
          
        
        # facing DOWN Blades
        for blade in range(num_blades):  # 0,1,2
            blade_start = blade * N * 56  # Starting offset for the blade
            
            
            for j in range(N-1):
                i_offset = j * 56  # Adjust vertices for each section
                inlet_offset = blade_start + i_offset
                
                f.write(f"            ({41+inlet_offset} {40+inlet_offset} {96+inlet_offset} {97+inlet_offset})\n")
                f.write(f"            ({40+inlet_offset} {39+inlet_offset} {95+inlet_offset} {96+inlet_offset})\n")
                f.write(f"            ({39+inlet_offset} {38+inlet_offset} {94+inlet_offset} {95+inlet_offset})\n")
                f.write(f"            ({38+inlet_offset} {37+inlet_offset} {93+inlet_offset} {94+inlet_offset})\n")
                f.write(f"            ({37+inlet_offset} {36+inlet_offset} {92+inlet_offset} {93+inlet_offset})\n")
                f.write(f"            ({36+inlet_offset} {35+inlet_offset} {91+inlet_offset} {92+inlet_offset})\n")
    
    
        
        # facing DOWN gap
        for j in range(N-1):
            gap_inlet_offset = j * 56  # Adjust vertices for each section
            # Compute dynamic indices
            blade3_base = N * 56 * 2  # Start index for Blade 3
            blade2_base = N * 56  # Start index for Blade 2
            blade1_base = 0  # Blade 1 starts at index 0
    
            # top left
            f.write(f"            ({35+gap_inlet_offset} {91+gap_inlet_offset} {blade2_base+97+gap_inlet_offset} {blade2_base+41+gap_inlet_offset})\n")
            # top right
            f.write(f"            ({41+gap_inlet_offset} {blade3_base+35+gap_inlet_offset} {blade3_base+91+gap_inlet_offset} {97+gap_inlet_offset})\n")
            # bottom
            f.write(f"            ({blade3_base+41+gap_inlet_offset} {blade2_base+35+gap_inlet_offset} {blade2_base+91+gap_inlet_offset} {blade3_base+97+gap_inlet_offset})\n")
    
        # blades top radial
        for j in range(1,num_blades+1):
            
            # go to top of blade
            b = (N)*56*j
            
            # inner
            f.write(f"            ({16 - 56 + b} {0 -56 + b} {1 - 56 + b} {17 -56 + b})\n") # have to -56 from each
            f.write(f"            ({17 - 56 + b} {1 -56 + b} {2 - 56 + b} {18 - 56 + b})\n") 
            f.write(f"            ({18 - 56 + b} {2 -56 + b} {3 - 56 + b} {19 - 56 + b})\n") 
            f.write(f"            ({19 - 56 + b} {3 -56 + b} {4 - 56 + b} {20 - 56 + b})\n") 
            f.write(f"            ({20 - 56 + b} {4 -56 + b} {5 - 56 + b} {21 - 56 + b})\n") 
            f.write(f"            ({21 - 56 + b} {5 -56 + b} {6 - 56 + b} {22 - 56 + b})\n") 
            f.write(f"            ({22 - 56 + b} {6 -56 + b} {7 - 56 + b} {23 - 56 + b})\n") 
            f.write(f"            ({23 - 56 + b} {7 -56 + b} {8 - 56 + b} {24 - 56 + b})\n") 
            f.write(f"            ({24 - 56 + b} {8 -56 + b} {9 - 56 + b} {25 - 56 + b})\n") 
            f.write(f"            ({25 - 56 + b} {9 -56 + b} {10 - 56 + b} {26 - 56 + b})\n") 
            f.write(f"            ({26 - 56 + b} {10 -56 + b} {11 - 56 + b} {27 - 56 + b})\n") 
            f.write(f"            ({27 - 56 + b} {11 -56 + b} {12 - 56 + b} {28 - 56 + b})\n") 
            f.write(f"            ({28 - 56 + b} {12 -56 + b} {13 - 56 + b} {29 - 56 + b})\n") 
            f.write(f"            ({29 - 56 + b} {13 -56 + b} {14 - 56 + b} {30 - 56 + b})\n") 
            f.write(f"            ({30 - 56 + b} {14 -56 + b} {15 - 56 + b} {31 - 56 + b})\n") 
            f.write(f"            ({31 - 56 + b} {15 -56 + b} {0 - 56 + b} {16- 56 + b})\n") 
    
            # outer
            f.write(f"            ({32 - 56 + b} {16 -56 + b} {17 - 56 + b} {33 - 56 + b})\n") 
            f.write(f"            ({33 - 56 + b} {17 -56 + b} {18 - 56 + b} {34 - 56 + b})\n") 
            f.write(f"            ({34 - 56 + b} {18 -56 + b} {36 - 56 + b} {35 - 56 + b})\n") 
            f.write(f"            ({36 - 56 + b} {18 - 56 + b} {19 - 56 + b} {37 - 56 + b})\n") 
            f.write(f"            ({37 - 56 + b} {19 -56 + b} {20 - 56 + b} {38 - 56 + b})\n") 
            f.write(f"            ({38 - 56 + b} {20 -56 + b} {21 - 56 + b} {39 - 56 + b})\n") 
            f.write(f"            ({39 - 56 + b} {21 -56 + b} {22 - 56 + b} {40 - 56 + b})\n") 
            f.write(f"            ({40 - 56 + b} {22 -56 + b} {42 - 56 + b} {41 - 56 + b})\n") 
            f.write(f"            ({22 - 56 + b} {23 -56 + b} {43 - 56 + b} {42 - 56 + b})\n") 
            f.write(f"            ({23 - 56 + b} {24 -56 + b} {44 - 56 + b} {43 - 56 + b})\n") 
            f.write(f"            ({24 - 56 + b} {25 -56 + b} {45 - 56 + b} {44 - 56 + b})\n") 
            f.write(f"            ({25 - 56 + b} {26 -56 + b} {46 - 56 + b} {45 - 56 + b})\n") 
            f.write(f"            ({26 - 56 + b} {48 -56 + b} {47 - 56 + b} {46 - 56 + b})\n") 
            f.write(f"            ({27 - 56 + b} {49 -56 + b} {48 - 56 + b} {26 - 56 + b})\n") 
            f.write(f"            ({28 - 56 + b} {50 -56 + b} {49 - 56 + b} {27 - 56 + b})\n") 
            f.write(f"            ({29 - 56 + b} {51 -56 + b} {50 - 56 + b} {28 - 56 + b})\n") 
            f.write(f"            ({30 - 56 + b} {52 -56 + b} {51 - 56 + b} {29 - 56 + b})\n") 
            f.write(f"            ({30 - 56 + b} {54 -56 + b} {53 - 56 + b} {52 - 56 + b})\n") 
            f.write(f"            ({31 - 56 + b} {55 -56 + b} {54 - 56 + b} {30 - 56 + b})\n") 
            f.write(f"            ({16 - 56 + b} {32 -56 + b} {55 - 56 + b} {31 - 56 + b})\n") 
    
       
        
        # gap facing radial
        b1 = N * 56
        b2 = N * 56 * 2
        b3 = N * 56 * 3
    
        # top left
        f.write(f"            ({35 - 56 + b1} {41 -56 + b2} {42 - 56 + b2} {34 -56 + b1})\n") # have to -56 from each
        f.write(f"            ({34 - 56 + b1} {42 -56 + b2} {43 - 56 + b2} {33 -56 + b1})\n")
        f.write(f"            ({33 - 56 + b1} {43 -56 + b2} {44 - 56 + b2} {32 -56 + b1})\n") 
        f.write(f"            ({32 - 56 + b1} {44 -56 + b2} {45 - 56 + b2} {55 -56 + b1})\n")
        f.write(f"            ({55 - 56 + b1} {45 -56 + b2} {46 - 56 + b2} {54 -56 + b1})\n")
        f.write(f"            ({54 - 56 + b1} {46 -56 + b2} {47 - 56 + b2} {53 -56 + b1})\n")
        
        # top right
        f.write(f"            ({35 - 56 + b3} {41 -56 + b1} {42 - 56 + b1} {34 -56 + b3})\n") # have to -56 from each
        f.write(f"            ({34 - 56 + b3} {42 -56 + b1} {43 - 56 + b1} {33 -56 + b3})\n")
        f.write(f"            ({33 - 56 + b3} {43 -56 + b1} {44 - 56 + b1} {32 -56 + b3})\n") 
        f.write(f"            ({32 - 56 + b3} {44 -56 + b1} {45 - 56 + b1} {55 -56 + b3})\n")
        f.write(f"            ({55 - 56 + b3} {45 -56 + b1} {46 - 56 + b1} {54 -56 + b3})\n")
        f.write(f"            ({54 - 56 + b3} {46 -56 + b1} {47 - 56 + b1} {53 -56 + b3})\n")
        
        # bottom
        f.write(f"            ({35 - 56 + b2} {41 -56 + b3} {42 - 56 + b3} {34 -56 + b2})\n") # have to -56 from each
        f.write(f"            ({34 - 56 + b2} {42 -56 + b3} {43 - 56 + b3} {33 -56 + b2})\n")
        f.write(f"            ({33 - 56 + b2} {43 -56 + b3} {44 - 56 + b3} {32 -56 + b2})\n") 
        f.write(f"            ({32 - 56 + b2} {44 -56 + b3} {45 - 56 + b3} {55 -56 + b2})\n")
        f.write(f"            ({55 - 56 + b2} {45 -56 + b3} {46 - 56 + b3} {54 -56 + b2})\n")
        f.write(f"            ({54 - 56 + b2} {46 -56 + b3} {47 - 56 + b3} {53 -56 + b2})\n")
        
       
        
        f.write("        );\n")
        f.write("    }\n")
    #%%
    """
    FIXEDAMI
    """
    
    if write_central:
        # FIXEDAMI
        f.write("    fixedAMI\n")
        f.write("    {\n")
        f.write("        type cyclicAMI;\n")
        f.write("        neighbourPatch rotatingAMI;\n")
        f.write("        transform noOrdering;\n")
        f.write("        faces\n        (\n")
        
        
        f.write(f"            ({10+disc_vertices_offset} {11+disc_vertices_offset} {15+disc_vertices_offset} {14+disc_vertices_offset})\n")
        f.write(f"            ({9+disc_vertices_offset} {10+disc_vertices_offset} {14+disc_vertices_offset} {13+disc_vertices_offset})\n")
        f.write(f"            ({8+disc_vertices_offset} {11+disc_vertices_offset} {15+disc_vertices_offset} {12+disc_vertices_offset})\n")
        f.write(f"            ({8+disc_vertices_offset} {9+disc_vertices_offset} {13+disc_vertices_offset} {12+disc_vertices_offset})\n")
    
        if write_up_down:
            # facing up
            f.write(f"            ({54+disc_vertices_offset} {55+disc_vertices_offset} {35+disc_vertices_offset} {34+disc_vertices_offset})\n")
            f.write(f"            ({53 + disc_vertices_offset} {54 + disc_vertices_offset} {34 + disc_vertices_offset} {33 + disc_vertices_offset})\n")
            f.write(f"            ({55 + disc_vertices_offset} {52 + disc_vertices_offset} {32 + disc_vertices_offset} {35 + disc_vertices_offset})\n")
            f.write(f"            ({52 + disc_vertices_offset} {53 + disc_vertices_offset} {33 + disc_vertices_offset} {32 + disc_vertices_offset})\n")
        
        
            # facing down
            f.write(f"            ({62 + disc_vertices_offset} {63 + disc_vertices_offset} {43 + disc_vertices_offset} {42 + disc_vertices_offset})\n")
            f.write(f"            ({61 + disc_vertices_offset} {62 + disc_vertices_offset} {42 + disc_vertices_offset} {41 + disc_vertices_offset})\n")
            f.write(f"            ({63 + disc_vertices_offset} {60 + disc_vertices_offset} {40 + disc_vertices_offset} {43 + disc_vertices_offset})\n")
            f.write(f"            ({60 + disc_vertices_offset} {61 + disc_vertices_offset} {41 + disc_vertices_offset} {40 + disc_vertices_offset})\n")
    
    
        f.write("        );\n")
        f.write("    }\n")
    
    #%%
    """
    HUB
    """
    if write_central:
        # HUB
        f.write("    hub\n")
        f.write("    {\n")
        f.write("        type wall;\n")
        f.write("        faces\n        (\n")
        
        for j in range(0,num_blades):
            hub_offset = N*56*j
            
            # inner
            f.write(f"            ({16 + hub_offset} {0 + hub_offset} {1 + hub_offset} {17 + hub_offset})\n") # have to -56 from each
            f.write(f"            ({17  + hub_offset} {1  + hub_offset} {2  + hub_offset} {18  + hub_offset})\n") 
            f.write(f"            ({18  + hub_offset} {2  + hub_offset} {3  + hub_offset} {19  + hub_offset})\n") 
            f.write(f"            ({19  + hub_offset} {3  + hub_offset} {4  + hub_offset} {20  + hub_offset})\n") 
            f.write(f"            ({20  + hub_offset} {4  + hub_offset} {5  + hub_offset} {21  + hub_offset})\n") 
            f.write(f"            ({21  + hub_offset} {5  + hub_offset} {6  + hub_offset} {22  + hub_offset})\n") 
            f.write(f"            ({22  + hub_offset} {6  + hub_offset} {7  + hub_offset} {23  + hub_offset})\n") 
            f.write(f"            ({23  + hub_offset} {7  + hub_offset} {8  + hub_offset} {24  + hub_offset})\n") 
            f.write(f"            ({24  + hub_offset} {8  + hub_offset} {9  + hub_offset} {25  + hub_offset})\n") 
            f.write(f"            ({25  + hub_offset} {9  + hub_offset} {10  + hub_offset} {26  + hub_offset})\n") 
            f.write(f"            ({26  + hub_offset} {10  + hub_offset} {11  + hub_offset} {27  + hub_offset})\n") 
            f.write(f"            ({27  + hub_offset} {11  + hub_offset} {12  + hub_offset} {28  + hub_offset})\n") 
            f.write(f"            ({28  + hub_offset} {12  + hub_offset} {13  + hub_offset} {29  + hub_offset})\n") 
            f.write(f"            ({29  + hub_offset} {13  + hub_offset} {14  + hub_offset} {30  + hub_offset})\n") 
            f.write(f"            ({30  + hub_offset} {14  + hub_offset} {15  + hub_offset} {31  + hub_offset})\n") 
            f.write(f"            ({31  + hub_offset} {15  + hub_offset} {0  + hub_offset} {16 + hub_offset})\n") 
    
            # outer
            f.write(f"            ({32  + hub_offset} {16  + hub_offset} {17  + hub_offset} {33  + hub_offset})\n") 
            f.write(f"            ({33  + hub_offset} {17  + hub_offset} {18  + hub_offset} {34  + hub_offset})\n") 
            f.write(f"            ({34  + hub_offset} {18  + hub_offset} {36  + hub_offset} {35  + hub_offset})\n") 
            f.write(f"            ({36  + hub_offset} {18  + hub_offset} {19  + hub_offset} {37  + hub_offset})\n") 
            f.write(f"            ({37  + hub_offset} {19  + hub_offset} {20  + hub_offset} {38  + hub_offset})\n") 
            f.write(f"            ({38  + hub_offset} {20  + hub_offset} {21  + hub_offset} {39  + hub_offset})\n") 
            f.write(f"            ({39  + hub_offset} {21  + hub_offset} {22  + hub_offset} {40  + hub_offset})\n") 
            f.write(f"            ({40  + hub_offset} {22  + hub_offset} {42  + hub_offset} {41  + hub_offset})\n") 
            f.write(f"            ({22  + hub_offset} {23  + hub_offset} {43  + hub_offset} {42  + hub_offset})\n") 
            f.write(f"            ({23  + hub_offset} {24  + hub_offset} {44  + hub_offset} {43  + hub_offset})\n") 
            f.write(f"            ({24  + hub_offset} {25  + hub_offset} {45  + hub_offset} {44  + hub_offset})\n") 
            f.write(f"            ({25  + hub_offset} {26  + hub_offset} {46  + hub_offset} {45  + hub_offset})\n") 
            f.write(f"            ({26  + hub_offset} {48  + hub_offset} {47  + hub_offset} {46  + hub_offset})\n") 
            f.write(f"            ({27  + hub_offset} {49  + hub_offset} {48  + hub_offset} {26  + hub_offset})\n") 
            f.write(f"            ({28  + hub_offset} {50  + hub_offset} {49  + hub_offset} {27  + hub_offset})\n") 
            f.write(f"            ({29  + hub_offset} {51  + hub_offset} {50  + hub_offset} {28  + hub_offset})\n") 
            f.write(f"            ({30  + hub_offset} {52  + hub_offset} {51  + hub_offset} {29  + hub_offset})\n") 
            f.write(f"            ({30  + hub_offset} {54  + hub_offset} {53  + hub_offset} {52  + hub_offset})\n") 
            f.write(f"            ({31  + hub_offset} {55  + hub_offset} {54  + hub_offset} {30  + hub_offset})\n") 
            f.write(f"            ({16  + hub_offset} {32  + hub_offset} {55  + hub_offset} {31  + hub_offset})\n")
            
    
        # connecting gap
        b1 = N * 56
        b2 = N * 56 * 2
        
        # top left
        f.write(f"            ({35} {41  + b1} {42  + b1} {34})\n") # have to  from each
        f.write(f"            ({34} {42  + b1} {43  + b1} {33})\n")
        f.write(f"            ({33} {43  + b1} {44  + b1} {32})\n") 
        f.write(f"            ({32} {44  + b1} {45  + b1} {55})\n")
        f.write(f"            ({55} {45  + b1} {46  + b1} {54})\n")
        f.write(f"            ({54} {46  + b1} {47  + b1} {53})\n")
    
        # top right
        f.write(f"            ({35  + b2} {41  } {42  } {34  + b2})\n") # have to  from each
        f.write(f"            ({34  + b2} {42  } {43  } {33  + b2})\n")
        f.write(f"            ({33  + b2} {43  } {44  } {32  + b2})\n") 
        f.write(f"            ({32  + b2} {44  } {45  } {55  + b2})\n")
        f.write(f"            ({55  + b2} {45  } {46  } {54  + b2})\n")
        f.write(f"            ({54  + b2} {46  } {47  } {53  + b2})\n")
        
        # bottom
        f.write(f"            ({35  + b1} {41  + b2} {42  + b2} {34  + b1})\n") # have to  from each
        f.write(f"            ({34  + b1} {42  + b2} {43  + b2} {33  + b1})\n")
        f.write(f"            ({33  + b1} {43  + b2} {44  + b2} {32  + b1})\n") 
        f.write(f"            ({32  + b1} {44  + b2} {45  + b2} {55  + b1})\n")
        f.write(f"            ({55  + b1} {45  + b2} {46  + b2} {54  + b1})\n")
        f.write(f"            ({54  + b1} {46  + b2} {47  + b2} {53  + b1})\n")
       
        f.write("        );\n")
        f.write("    }\n")
        
    
    #%%
    """
    INLET
    """
    
    if write_up_down:
        f.write("    inlet\n")
        f.write("    {\n")
        f.write("        type inlet;\n")
        f.write("        faces\n        (\n")
        
        # outer
        f.write(f"            ({16+disc_vertices_offset} {17+disc_vertices_offset} {23+disc_vertices_offset} {22+disc_vertices_offset})\n")
        f.write(f"            ({16 + disc_vertices_offset} {22 + disc_vertices_offset} {21 + disc_vertices_offset} {19 + disc_vertices_offset})\n")
        f.write(f"            ({23 + disc_vertices_offset} {17 + disc_vertices_offset} {18 + disc_vertices_offset} {20 + disc_vertices_offset})\n")
        f.write(f"            ({21 + disc_vertices_offset} {20 + disc_vertices_offset} {18 + disc_vertices_offset} {19 + disc_vertices_offset})\n")
    
        # inner
        f.write(f"            ({22 + disc_vertices_offset} {23 + disc_vertices_offset} {39 + disc_vertices_offset} {38 + disc_vertices_offset})\n")
        f.write(f"            ({21 + disc_vertices_offset} {22 + disc_vertices_offset} {38 + disc_vertices_offset} {37 + disc_vertices_offset})\n")
        f.write(f"            ({23 + disc_vertices_offset} {20 + disc_vertices_offset} {36 + disc_vertices_offset} {39 + disc_vertices_offset})\n")
        f.write(f"            ({20 + disc_vertices_offset} {21 + disc_vertices_offset} {37 + disc_vertices_offset} {36 + disc_vertices_offset})\n")
        
        # polo
        f.write(f"            ({70 + disc_vertices_offset} {86 + disc_vertices_offset} {87 + disc_vertices_offset} {71 + disc_vertices_offset})\n")
        f.write(f"            ({85 + disc_vertices_offset} {86 + disc_vertices_offset} {70 + disc_vertices_offset} {69 + disc_vertices_offset})\n")
        f.write(f"            ({84 + disc_vertices_offset} {68 + disc_vertices_offset} {71 + disc_vertices_offset} {87 + disc_vertices_offset})\n")
        f.write(f"            ({84 + disc_vertices_offset} {85 + disc_vertices_offset} {69 + disc_vertices_offset} {68 + disc_vertices_offset})\n")
        f.write(f"            ({68 + disc_vertices_offset} {69 + disc_vertices_offset} {70 + disc_vertices_offset} {71 + disc_vertices_offset})\n")
    
    
        f.write("        );\n")
        f.write("    }\n")
    
    #%%%
    """
    OUTLET
    """
    
    if write_up_down:
        f.write("    outlet\n")
        f.write("    {\n")
        f.write("        type outlet;\n")
        f.write("        faces\n        (\n")
        
        # outer
        f.write(f"            ({24 + disc_vertices_offset} {25 + disc_vertices_offset} {31 + disc_vertices_offset} {30 + disc_vertices_offset})\n")
        f.write(f"            ({24 + disc_vertices_offset} {30 + disc_vertices_offset} {29 + disc_vertices_offset} {27 + disc_vertices_offset})\n")
        f.write(f"            ({31 + disc_vertices_offset} {25 + disc_vertices_offset} {26 + disc_vertices_offset} {28 + disc_vertices_offset})\n")
        f.write(f"            ({29 + disc_vertices_offset} {28 + disc_vertices_offset} {26 + disc_vertices_offset} {27 + disc_vertices_offset})\n")
    
        # inner
        f.write(f"            ({30 + disc_vertices_offset} {31 + disc_vertices_offset} {47 + disc_vertices_offset} {46 + disc_vertices_offset})\n")
        f.write(f"            ({29 + disc_vertices_offset} {30 + disc_vertices_offset} {46 + disc_vertices_offset} {45 + disc_vertices_offset})\n")
        f.write(f"            ({31 + disc_vertices_offset} {28 + disc_vertices_offset} {44 + disc_vertices_offset} {47 + disc_vertices_offset})\n")
        f.write(f"            ({28 + disc_vertices_offset} {29 + disc_vertices_offset} {45 + disc_vertices_offset} {44 + disc_vertices_offset})\n")
    
        # polo
        f.write(f"            ({78 + disc_vertices_offset} {94 + disc_vertices_offset} {95 + disc_vertices_offset} {79 + disc_vertices_offset})\n")
        f.write(f"            ({93 + disc_vertices_offset} {94 + disc_vertices_offset} {78 + disc_vertices_offset} {77 + disc_vertices_offset})\n")
        f.write(f"            ({92 + disc_vertices_offset} {76 + disc_vertices_offset} {79 + disc_vertices_offset} {95 + disc_vertices_offset})\n")
        f.write(f"            ({92 + disc_vertices_offset} {93 + disc_vertices_offset} {77 + disc_vertices_offset} {76 + disc_vertices_offset})\n")
        f.write(f"            ({76 + disc_vertices_offset} {77 + disc_vertices_offset} {78 + disc_vertices_offset} {79 + disc_vertices_offset})\n")
    
        f.write("        );\n")
        f.write("    }\n")
    
    #%%
    """
    SURROUNDINGS
    """
    
    if write_up_down and write_central:
        f.write("    surroundingsSlip\n")
        f.write("    {\n")
        f.write("        type wall;\n")
        f.write("        faces\n        (\n")
        
        # central
        f.write(f"            ({7 + disc_vertices_offset} {4 + disc_vertices_offset} {0 + disc_vertices_offset} {3 + disc_vertices_offset})\n")
        f.write(f"            ({2 + disc_vertices_offset} {1 + disc_vertices_offset} {5 + disc_vertices_offset} {6 + disc_vertices_offset})\n")
        f.write(f"            ({7 + disc_vertices_offset} {3 + disc_vertices_offset} {2 + disc_vertices_offset} {6 + disc_vertices_offset})\n")
    
        # upstream
        f.write(f"            ({51 + disc_vertices_offset} {48 + disc_vertices_offset} {16 + disc_vertices_offset} {19 + disc_vertices_offset})\n")
        f.write(f"            ({18 + disc_vertices_offset} {17 + disc_vertices_offset} {49 + disc_vertices_offset} {50 + disc_vertices_offset})\n")
        f.write(f"            ({51 + disc_vertices_offset} {19 + disc_vertices_offset} {18 + disc_vertices_offset} {50 + disc_vertices_offset})\n")
    
        # downstream
        f.write(f"            ({27 + disc_vertices_offset} {24 + disc_vertices_offset} {56 + disc_vertices_offset} {59 + disc_vertices_offset})\n")
        f.write(f"            ({58 + disc_vertices_offset} {57 + disc_vertices_offset} {25 + disc_vertices_offset} {26 + disc_vertices_offset})\n")
        f.write(f"            ({27 + disc_vertices_offset} {59 + disc_vertices_offset} {58 + disc_vertices_offset} {26 + disc_vertices_offset})\n")
    
        
        f.write("        );\n")
        f.write("    }\n")
        
        
        f.write("    surroundingsNoSlip\n")
        f.write("    {\n")
        f.write("        type wall;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({0 + disc_vertices_offset} {4 + disc_vertices_offset} {5 + disc_vertices_offset} {1 + disc_vertices_offset})\n")
        f.write(f"            ({16 + disc_vertices_offset} {48 + disc_vertices_offset} {49 + disc_vertices_offset} {17 + disc_vertices_offset})\n")
        f.write(f"            ({56 + disc_vertices_offset} {24 + disc_vertices_offset} {25 + disc_vertices_offset} {57 + disc_vertices_offset})\n")
    
        
        f.write("        );\n")
        f.write("    }\n")

   
    
    #%%
    """
    MOVINGHUB
    """
    
    if write_up_down:
        f.write("    movingHub\n")
        f.write("    {\n")
        f.write("        type wall;\n")
        f.write("        faces\n        (\n")
        
        # polo up
        f.write(f"            ({66 + disc_vertices_offset} {82 + disc_vertices_offset} {83 + disc_vertices_offset} {67 + disc_vertices_offset})\n")
        f.write(f"            ({81 + disc_vertices_offset} {82 + disc_vertices_offset} {66 + disc_vertices_offset} {65 + disc_vertices_offset})\n")
        f.write(f"            ({80 + disc_vertices_offset} {64 + disc_vertices_offset} {67 + disc_vertices_offset} {83 + disc_vertices_offset})\n")
        f.write(f"            ({80 + disc_vertices_offset} {81 + disc_vertices_offset} {65 + disc_vertices_offset} {64 + disc_vertices_offset})\n")
        f.write(f"            ({64 + disc_vertices_offset} {65 + disc_vertices_offset} {66 + disc_vertices_offset} {67 + disc_vertices_offset})\n")
       
        # polo down (back of hub)
        f.write(f"            ({74 + disc_vertices_offset} {90 + disc_vertices_offset} {91 + disc_vertices_offset} {75 + disc_vertices_offset})\n")
        f.write(f"            ({89 + disc_vertices_offset} {90 + disc_vertices_offset} {74 + disc_vertices_offset} {73 + disc_vertices_offset})\n")
        f.write(f"            ({88 + disc_vertices_offset} {72 + disc_vertices_offset} {75 + disc_vertices_offset} {91 + disc_vertices_offset})\n")
        f.write(f"            ({88 + disc_vertices_offset} {89 + disc_vertices_offset} {73 + disc_vertices_offset} {72 + disc_vertices_offset})\n")
        f.write(f"            ({72 + disc_vertices_offset} {73 + disc_vertices_offset} {74 + disc_vertices_offset} {75 + disc_vertices_offset})\n")
        
    
        f.write("        );\n")
        f.write("    }\n")
    #%%
    """
    INTERFACES
    """
    
    if write_up_down and write_central:
        # Interface At Disc facing upstream (4 sections areound rotating disc)
        f.write("    interfaceDiscUp\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({0 + disc_vertices_offset} {1 + disc_vertices_offset} {11 + disc_vertices_offset} {10 + disc_vertices_offset})\n")
        f.write(f"            ({0 + disc_vertices_offset} {10 + disc_vertices_offset} {9 + disc_vertices_offset} {3 + disc_vertices_offset}) \n")
        f.write(f"            ({11 + disc_vertices_offset} {1 + disc_vertices_offset} {2 + disc_vertices_offset} {8 + disc_vertices_offset})\n")
        f.write(f"            ({9 + disc_vertices_offset} {8 + disc_vertices_offset} {2 + disc_vertices_offset} {3 + disc_vertices_offset})\n")
        
        f.write("        );\n")
        f.write("    }\n")
        
        # Interface At Start of Upstream Section (4 sections)
        f.write("    interfaceUp\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({48 + disc_vertices_offset} {49 + disc_vertices_offset} {55 + disc_vertices_offset} {54 + disc_vertices_offset})\n")
        f.write(f"            ({48 + disc_vertices_offset} {54 + disc_vertices_offset} {53 + disc_vertices_offset} {51 + disc_vertices_offset})\n")
        f.write(f"            ({55 + disc_vertices_offset} {49 + disc_vertices_offset} {50 + disc_vertices_offset} {52 + disc_vertices_offset})\n")
        f.write(f"            ({53 + disc_vertices_offset} {52 + disc_vertices_offset} {50 + disc_vertices_offset} {51 + disc_vertices_offset})\n")
        
        f.write("        );\n")
        f.write("    }\n")
        
        # Interface At Disc facing downstream (4 sections areound rotating disc)
        f.write("    interfaceDiscDown\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({4 + disc_vertices_offset} {5 + disc_vertices_offset} {15 + disc_vertices_offset} {14 + disc_vertices_offset})\n")
        f.write(f"            ({4 + disc_vertices_offset} {14 + disc_vertices_offset} {13 + disc_vertices_offset} {7 + disc_vertices_offset}) \n")
        f.write(f"            ({15 + disc_vertices_offset} {5 + disc_vertices_offset} {6 + disc_vertices_offset} {12 + disc_vertices_offset})\n")
        f.write(f"            ({13 + disc_vertices_offset} {12 + disc_vertices_offset} {6 + disc_vertices_offset} {7 + disc_vertices_offset})\n")
        
        f.write("        );\n")
        f.write("    }\n")
        
        
        # Interface At Start of Dpwnstream Section (4 sections)
        f.write("    interfaceDown\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({56 + disc_vertices_offset} {57 + disc_vertices_offset} {63 + disc_vertices_offset} {62 + disc_vertices_offset})\n")
        f.write(f"            ({56 + disc_vertices_offset} {62 + disc_vertices_offset} {61 + disc_vertices_offset} {59 + disc_vertices_offset})\n")
        f.write(f"            ({63 + disc_vertices_offset} {57 + disc_vertices_offset} {58 + disc_vertices_offset} {60 + disc_vertices_offset})\n")
        f.write(f"            ({61 + disc_vertices_offset} {60 + disc_vertices_offset} {58 + disc_vertices_offset} {59 + disc_vertices_offset})\n")
        
        f.write("        );\n")
        f.write("    }\n")
        
        # Polo mint interface UP [polo side] (between polo and surrounding cylinder)
        f.write("    interfacePoloSideUp\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({82 + disc_vertices_offset} {83 + disc_vertices_offset} {87 + disc_vertices_offset} {86 + disc_vertices_offset})\n")
        f.write(f"            ({81 + disc_vertices_offset} {82 + disc_vertices_offset} {86 + disc_vertices_offset} {85 + disc_vertices_offset})\n")
        f.write(f"            ({80 + disc_vertices_offset} {84 + disc_vertices_offset} {87 + disc_vertices_offset} {83 + disc_vertices_offset})\n")
        f.write(f"            ({81 + disc_vertices_offset} {85 + disc_vertices_offset} {84 + disc_vertices_offset} {80 + disc_vertices_offset})\n")
    
        f.write("        );\n")
        f.write("    }\n")
        
        # Polo mint interface UP [surrounding cylinder side] (between polo and surrounding cylinder)
        f.write("    interfacePoloCylUp\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({34 + disc_vertices_offset} {35 + disc_vertices_offset} {39 + disc_vertices_offset} {38 + disc_vertices_offset})\n")
        f.write(f"            ({33 + disc_vertices_offset} {34 + disc_vertices_offset} {38 + disc_vertices_offset} {37 + disc_vertices_offset})\n")
        f.write(f"            ({32 + disc_vertices_offset} {36 + disc_vertices_offset} {39 + disc_vertices_offset} {35 + disc_vertices_offset})\n")
        f.write(f"            ({33 + disc_vertices_offset} {37 + disc_vertices_offset} {36 + disc_vertices_offset} {32 + disc_vertices_offset})\n")
    
        f.write("        );\n")
        f.write("    }\n")
        
        # Polo mint interface DOWN [polo side] (between polo and surrounding cylinder)
        f.write("    interfacePoloSideDown\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({94 + disc_vertices_offset} {95 + disc_vertices_offset} {91 + disc_vertices_offset} {90 + disc_vertices_offset})\n")
        f.write(f"            ({93 + disc_vertices_offset} {94 + disc_vertices_offset} {90 + disc_vertices_offset} {89 + disc_vertices_offset})\n")
        f.write(f"            ({92 + disc_vertices_offset} {88 + disc_vertices_offset} {91 + disc_vertices_offset} {95 + disc_vertices_offset})\n")
        f.write(f"            ({93 + disc_vertices_offset} {89 + disc_vertices_offset} {88 + disc_vertices_offset} {92 + disc_vertices_offset})\n")
    
        f.write("        );\n")
        f.write("    }\n")
        
        # Polo mint interface DOWN [surrounding cylinder side] (between polo and surrounding cylinder)
        f.write("    interfacePoloCylDown\n")
        f.write("    {\n")
        f.write("        type patch;\n")
        f.write("        faces\n        (\n")
        
        f.write(f"            ({46 + disc_vertices_offset} {47 + disc_vertices_offset} {43 + disc_vertices_offset} {42 + disc_vertices_offset})\n")
        f.write(f"            ({45 + disc_vertices_offset} {46 + disc_vertices_offset} {42 + disc_vertices_offset} {41 + disc_vertices_offset})\n")
        f.write(f"            ({44 + disc_vertices_offset} {40 + disc_vertices_offset} {47 + disc_vertices_offset} {43 + disc_vertices_offset})\n")
        f.write(f"            ({45 + disc_vertices_offset} {41 + disc_vertices_offset} {40 + disc_vertices_offset} {44 + disc_vertices_offset})\n")
    
        f.write("        );\n")
        f.write("    }\n")
    
    #%%
    # DEFAUlt
    # f.write("    defaultFaces\n")
    # f.write("    {\n")
    # f.write("        type wall;\n")
    # f.write("        faces\n        (\n")
    # f.write("        );\n")
    # f.write("    }\n")
    
   
    
    
    
    f.write(");\n")
    