import numpy as np
"""
Section 11A
Write arcs to blockMeshDict
"""

def write_arcs(f, num_blades, num_root_sections, N, arc_array_dict, circle_vertices_arrays, ordered_vertices, y_coords, width, disc_vertices_offset, sm_arc_interpolations, up_arc_interpolations, down_arc_interpolations, inner_arc_interpolations, interface_arc_interpolations, cc_interface_arc_interpolations, polosquare_interface_arc_interpolations, write_up_down, write_central):

    f.write("edges\n(\n")
    
    #%%
    """
    Blade arcs
    """
    
    if write_central:
        # Loop through blades
        for blade in range(num_blades):
            current_circle_vertices_array = circle_vertices_arrays[blade]  # Select vertices dynamically
            
            for j in range(N):
                arc_vertex_offset = blade * N * 56 + j * 56  # Offset for each section
                
                f.write(f"    arc {16+arc_vertex_offset} {17+arc_vertex_offset} ({current_circle_vertices_array[1, 0, j]} {current_circle_vertices_array[1, 1, j]} {current_circle_vertices_array[1, 2, j]})\n")
                f.write(f"    arc {17+arc_vertex_offset} {18+arc_vertex_offset} ({current_circle_vertices_array[3, 0, j]} {current_circle_vertices_array[3, 1, j]} {current_circle_vertices_array[3, 2, j]})\n")
                f.write(f"    arc {18+arc_vertex_offset} {19+arc_vertex_offset} ({current_circle_vertices_array[5, 0, j]} {current_circle_vertices_array[5, 1, j]} {current_circle_vertices_array[5, 2, j]})\n")
                f.write(f"    arc {19+arc_vertex_offset} {20+arc_vertex_offset} ({current_circle_vertices_array[7, 0, j]} {current_circle_vertices_array[7, 1, j]} {current_circle_vertices_array[7, 2, j]})\n")
                f.write(f"    arc {20+arc_vertex_offset} {21+arc_vertex_offset} ({current_circle_vertices_array[9, 0, j]} {current_circle_vertices_array[9, 1, j]} {current_circle_vertices_array[9, 2, j]})\n")
                f.write(f"    arc {21+arc_vertex_offset} {22+arc_vertex_offset} ({current_circle_vertices_array[11, 0, j]} {current_circle_vertices_array[11, 1, j]} {current_circle_vertices_array[11, 2, j]})\n")
                f.write(f"    arc {22+arc_vertex_offset} {23+arc_vertex_offset} ({current_circle_vertices_array[13, 0, j]} {current_circle_vertices_array[13, 1, j]} {current_circle_vertices_array[13, 2, j]})\n")
                f.write(f"    arc {23+arc_vertex_offset} {24+arc_vertex_offset} ({current_circle_vertices_array[15, 0, j]} {current_circle_vertices_array[15, 1, j]} {current_circle_vertices_array[15, 2, j]})\n")
                f.write(f"    arc {24+arc_vertex_offset} {25+arc_vertex_offset} ({current_circle_vertices_array[17, 0, j]} {current_circle_vertices_array[17, 1, j]} {current_circle_vertices_array[17, 2, j]})\n")
                f.write(f"    arc {25+arc_vertex_offset} {26+arc_vertex_offset} ({current_circle_vertices_array[19, 0, j]} {current_circle_vertices_array[19, 1, j]} {current_circle_vertices_array[19, 2, j]})\n")
                f.write(f"    arc {26+arc_vertex_offset} {27+arc_vertex_offset} ({current_circle_vertices_array[21, 0, j]} {current_circle_vertices_array[21, 1, j]} {current_circle_vertices_array[21, 2, j]})\n")
                f.write(f"    arc {27+arc_vertex_offset} {28+arc_vertex_offset} ({current_circle_vertices_array[23, 0, j]} {current_circle_vertices_array[23, 1, j]} {current_circle_vertices_array[23, 2, j]})\n")
                f.write(f"    arc {28+arc_vertex_offset} {29+arc_vertex_offset} ({current_circle_vertices_array[25, 0, j]} {current_circle_vertices_array[25, 1, j]} {current_circle_vertices_array[25, 2, j]})\n")
                f.write(f"    arc {29+arc_vertex_offset} {30+arc_vertex_offset} ({current_circle_vertices_array[27, 0, j]} {current_circle_vertices_array[27, 1, j]} {current_circle_vertices_array[27, 2, j]})\n")
                f.write(f"    arc {30+arc_vertex_offset} {31+arc_vertex_offset} ({current_circle_vertices_array[29, 0, j]} {current_circle_vertices_array[29, 1, j]} {current_circle_vertices_array[29, 2, j]})\n")
                f.write(f"    arc {31+arc_vertex_offset} {16+arc_vertex_offset} ({current_circle_vertices_array[31, 0, j]} {current_circle_vertices_array[31, 1, j]} {current_circle_vertices_array[31, 2, j]})\n")

    #%%
    """
    Curvature arcs
    """
   # arc_array
   
    if write_central:
        for blade in range(num_blades):
            current_arc_array = arc_array_dict[blade]  # Select vertices dynamically
            
            for j in range(N):
                arc_vertex_offset = blade * N * 56 + j * 56  # Offset for each section
                
                # inner
                f.write(f"    arc {16+arc_vertex_offset} {0+arc_vertex_offset} ({current_arc_array[0, 0, j]} {current_arc_array[0, 1, j]} {current_arc_array[0, 2, j]})\n")
                f.write(f"    arc {17+arc_vertex_offset} {1+arc_vertex_offset} ({current_arc_array[1, 0, j]} {current_arc_array[1, 1, j]} {current_arc_array[1, 2, j]})\n")
                f.write(f"    arc {18+arc_vertex_offset} {2+arc_vertex_offset} ({current_arc_array[2, 0, j]} {current_arc_array[2, 1, j]} {current_arc_array[2, 2, j]})\n")
                f.write(f"    arc {19+arc_vertex_offset} {3+arc_vertex_offset} ({current_arc_array[3, 0, j]} {current_arc_array[3, 1, j]} {current_arc_array[3, 2, j]})\n")
                # f.write(f"    arc {20+arc_vertex_offset} {4+arc_vertex_offset} ({current_arc_array[4, 0, j]} {current_arc_array[4, 1, j]} {current_arc_array[4, 2, j]})\n")
                f.write(f"    arc {21+arc_vertex_offset} {5+arc_vertex_offset} ({current_arc_array[5, 0, j]} {current_arc_array[5, 1, j]} {current_arc_array[5, 2, j]})\n")
                f.write(f"    arc {22+arc_vertex_offset} {6+arc_vertex_offset} ({current_arc_array[6, 0, j]} {current_arc_array[6, 1, j]} {current_arc_array[6, 2, j]})\n")
                f.write(f"    arc {23+arc_vertex_offset} {7+arc_vertex_offset} ({current_arc_array[7, 0, j]} {current_arc_array[7, 1, j]} {current_arc_array[7, 2, j]})\n")
                f.write(f"    arc {24+arc_vertex_offset} {8+arc_vertex_offset} ({current_arc_array[8, 0, j]} {current_arc_array[8, 1, j]} {current_arc_array[8, 2, j]})\n")
                f.write(f"    arc {25+arc_vertex_offset} {9+arc_vertex_offset} ({current_arc_array[9, 0, j]} {current_arc_array[9, 1, j]} {current_arc_array[9, 2, j]})\n")
                f.write(f"    arc {26+arc_vertex_offset} {10+arc_vertex_offset} ({current_arc_array[10, 0, j]} {current_arc_array[10, 1, j]} {current_arc_array[10, 2, j]})\n")
                f.write(f"    arc {27+arc_vertex_offset} {11+arc_vertex_offset} ({current_arc_array[11, 0, j]} {current_arc_array[11, 1, j]} {current_arc_array[11, 2, j]})\n")
                # f.write(f"    arc {28+arc_vertex_offset} {12+arc_vertex_offset} ({current_arc_array[12, 0, j]} {current_arc_array[12, 1, j]} {current_arc_array[12, 2, j]})\n")
                f.write(f"    arc {29+arc_vertex_offset} {13+arc_vertex_offset} ({current_arc_array[13, 0, j]} {current_arc_array[13, 1, j]} {current_arc_array[13, 2, j]})\n")
                f.write(f"    arc {30+arc_vertex_offset} {14+arc_vertex_offset} ({current_arc_array[14, 0, j]} {current_arc_array[14, 1, j]} {current_arc_array[14, 2, j]})\n")
                f.write(f"    arc {31+arc_vertex_offset} {15+arc_vertex_offset} ({current_arc_array[15, 0, j]} {current_arc_array[15, 1, j]} {current_arc_array[15, 2, j]})\n")
    
                # 32 to 34
                f.write(f"    arc {32+arc_vertex_offset} {16+arc_vertex_offset} ({current_arc_array[16, 0, j]} {current_arc_array[16, 1, j]} {current_arc_array[16, 2, j]})\n")
                f.write(f"    arc {33+arc_vertex_offset} {17+arc_vertex_offset} ({current_arc_array[17, 0, j]} {current_arc_array[17, 1, j]} {current_arc_array[17, 2, j]})\n")
                f.write(f"    arc {34+arc_vertex_offset} {18+arc_vertex_offset} ({current_arc_array[18, 0, j]} {current_arc_array[18, 1, j]} {current_arc_array[18, 2, j]})\n")
    
                # 42 to 46
                f.write(f"    arc {42+arc_vertex_offset} {22+arc_vertex_offset} ({current_arc_array[19, 0, j]} {current_arc_array[19, 1, j]} {current_arc_array[19, 2, j]})\n")
                f.write(f"    arc {43+arc_vertex_offset} {23+arc_vertex_offset} ({current_arc_array[20, 0, j]} {current_arc_array[20, 1, j]} {current_arc_array[20, 2, j]})\n")
                f.write(f"    arc {44+arc_vertex_offset} {24+arc_vertex_offset} ({current_arc_array[21, 0, j]} {current_arc_array[21, 1, j]} {current_arc_array[21, 2, j]})\n")
                f.write(f"    arc {45+arc_vertex_offset} {25+arc_vertex_offset} ({current_arc_array[22, 0, j]} {current_arc_array[22, 1, j]} {current_arc_array[22, 2, j]})\n")
                f.write(f"    arc {46+arc_vertex_offset} {26+arc_vertex_offset} ({current_arc_array[23, 0, j]} {current_arc_array[23, 1, j]} {current_arc_array[23, 2, j]})\n")
    
                # 54 to 55
                f.write(f"    arc {54+arc_vertex_offset} {30+arc_vertex_offset} ({current_arc_array[24, 0, j]} {current_arc_array[24, 1, j]} {current_arc_array[24, 2, j]})\n")
                f.write(f"    arc {55+arc_vertex_offset} {31+arc_vertex_offset} ({current_arc_array[25, 0, j]} {current_arc_array[25, 1, j]} {current_arc_array[25, 2, j]})\n")
    
                # 35 to 41
                f.write(f"    arc {35+arc_vertex_offset} {36+arc_vertex_offset} ({current_arc_array[26, 0, j]} {current_arc_array[26, 1, j]} {current_arc_array[26, 2, j]})\n")
                f.write(f"    arc {36+arc_vertex_offset} {37+arc_vertex_offset} ({current_arc_array[27, 0, j]} {current_arc_array[27, 1, j]} {current_arc_array[27, 2, j]})\n")
                f.write(f"    arc {37+arc_vertex_offset} {38+arc_vertex_offset} ({current_arc_array[28, 0, j]} {current_arc_array[28, 1, j]} {current_arc_array[28, 2, j]})\n")
                f.write(f"    arc {38+arc_vertex_offset} {39+arc_vertex_offset} ({current_arc_array[29, 0, j]} {current_arc_array[29, 1, j]} {current_arc_array[29, 2, j]})\n")
                f.write(f"    arc {39+arc_vertex_offset} {40+arc_vertex_offset} ({current_arc_array[30, 0, j]} {current_arc_array[30, 1, j]} {current_arc_array[30, 2, j]})\n")
                f.write(f"    arc {40+arc_vertex_offset} {41+arc_vertex_offset} ({current_arc_array[31, 0, j]} {current_arc_array[31, 1, j]} {current_arc_array[31, 2, j]})\n")
    
                # 47 to 53
                f.write(f"    arc {47+arc_vertex_offset} {48+arc_vertex_offset} ({current_arc_array[32, 0, j]} {current_arc_array[32, 1, j]} {current_arc_array[32, 2, j]})\n")
                f.write(f"    arc {48+arc_vertex_offset} {49+arc_vertex_offset} ({current_arc_array[33, 0, j]} {current_arc_array[33, 1, j]} {current_arc_array[33, 2, j]})\n")
                f.write(f"    arc {49+arc_vertex_offset} {50+arc_vertex_offset} ({current_arc_array[34, 0, j]} {current_arc_array[34, 1, j]} {current_arc_array[34, 2, j]})\n")
                f.write(f"    arc {50+arc_vertex_offset} {51+arc_vertex_offset} ({current_arc_array[35, 0, j]} {current_arc_array[35, 1, j]} {current_arc_array[35, 2, j]})\n")
                f.write(f"    arc {51+arc_vertex_offset} {52+arc_vertex_offset} ({current_arc_array[36, 0, j]} {current_arc_array[36, 1, j]} {current_arc_array[36, 2, j]})\n")
                f.write(f"    arc {52+arc_vertex_offset} {53+arc_vertex_offset} ({current_arc_array[37, 0, j]} {current_arc_array[37, 1, j]} {current_arc_array[37, 2, j]})\n")
    
                
                # # Only write these arcs if j > num_root_sections (straight line arc interpolation errors)
                # if j >= num_root_sections:
                    
                #     # f.write(f"    arc {20+arc_vertex_offset} {4+arc_vertex_offset} ({current_arc_array[4, 0, j]} {current_arc_array[4, 1, j]} {current_arc_array[4, 2, j]})\n")
                #     # f.write(f"    arc {28+arc_vertex_offset} {12+arc_vertex_offset} ({current_arc_array[12, 0, j]} {current_arc_array[12, 1, j]} {current_arc_array[12, 2, j]})\n")
       
        
                #     # IMPORTANT: For some N and height combinations it is necessary to add small offset to x values, maybe floating point errors!!!!
                #     # UNCOMMENT NEXT 3 LINES IF REQUIRED: 
                #     epsilon = 1e-6  # Small offset to avoid straight-line arcs
                #     f.write(f"    arc {20+arc_vertex_offset} {4+arc_vertex_offset} ({current_arc_array[4, 0, j] + epsilon} {current_arc_array[4, 1, j]} {current_arc_array[4, 2, j]})\n")
                #     f.write(f"    arc {28+arc_vertex_offset} {12+arc_vertex_offset} ({current_arc_array[12, 0, j] + epsilon} {current_arc_array[12, 1, j]} {current_arc_array[12, 2, j]})\n")

    #%%
    """
    Gap mesh arcs
    """
    
    if write_central:
        for j in range(N):
            offset = j * 56  # Adjust vertices for each section
            
            blade3_base = N * 56 * 2  # Start index for Blade 3
            blade2_base = N * 56  # Start index for Blade 2
        
            # gap 1
            f.write(f"    arc {47+offset} {blade3_base+53+offset} ({(ordered_vertices[47+offset][0] + ordered_vertices[blade3_base+53+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[47+offset][0] + ordered_vertices[blade3_base+53+offset][0])/2)**2)} {ordered_vertices[47+offset][2]})\n")
            f.write(f"    arc {46+offset} {blade3_base+54+offset} ({(ordered_vertices[46+offset][0] + ordered_vertices[blade3_base+54+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[46+offset][0] + ordered_vertices[blade3_base+54+offset][0])/2)**2)} {ordered_vertices[46+offset][2]})\n")
            f.write(f"    arc {45+offset} {blade3_base+55+offset} ({(ordered_vertices[45+offset][0] + ordered_vertices[blade3_base+55+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[45+offset][0] + ordered_vertices[blade3_base+55+offset][0])/2)**2)} {ordered_vertices[45+offset][2]})\n")
            f.write(f"    arc {44+offset} {blade3_base+32+offset} ({(ordered_vertices[44+offset][0] + ordered_vertices[blade3_base+32+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[44+offset][0] + ordered_vertices[blade3_base+32+offset][0])/2)**2)} {ordered_vertices[44+offset][2]})\n")
            f.write(f"    arc {43+offset} {blade3_base+33+offset} ({(ordered_vertices[43+offset][0] + ordered_vertices[blade3_base+33+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[43+offset][0] + ordered_vertices[blade3_base+33+offset][0])/2)**2)} {ordered_vertices[43+offset][2]})\n")
            f.write(f"    arc {42+offset} {blade3_base+34+offset} ({(ordered_vertices[42+offset][0] + ordered_vertices[blade3_base+34+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[42+offset][0] + ordered_vertices[blade3_base+34+offset][0])/2)**2)} {ordered_vertices[42+offset][2]})\n")
            f.write(f"    arc {41+offset} {blade3_base+35+offset} ({(ordered_vertices[41+offset][0] + ordered_vertices[blade3_base+35+offset][0])/2} {np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[41+offset][0] + ordered_vertices[blade3_base+35+offset][0])/2)**2)} {ordered_vertices[41+offset][2]})\n")
            
       
            # gap 2 bottom 
            f.write(f"    arc {blade2_base+53+offset} {blade3_base+47+offset} ({(ordered_vertices[blade2_base+53+offset][0] + ordered_vertices[blade3_base+47+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+53+offset][0] + ordered_vertices[blade3_base+47+offset][0])/2)**2)} {ordered_vertices[blade2_base+53+offset][2]})\n")
            f.write(f"    arc {blade2_base+54+offset} {blade3_base+46+offset} ({(ordered_vertices[blade2_base+54+offset][0] + ordered_vertices[blade3_base+46+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+54+offset][0] + ordered_vertices[blade3_base+46+offset][0])/2)**2)} {ordered_vertices[blade2_base+54+offset][2]})\n")
            f.write(f"    arc {blade2_base+55+offset} {blade3_base+45+offset} ({(ordered_vertices[blade2_base+55+offset][0] + ordered_vertices[blade3_base+45+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+55+offset][0] + ordered_vertices[blade3_base+45+offset][0])/2)**2)} {ordered_vertices[blade2_base+55+offset][2]})\n")
            f.write(f"    arc {blade2_base+32+offset} {blade3_base+44+offset} ({(ordered_vertices[blade2_base+32+offset][0] + ordered_vertices[blade3_base+44+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+32+offset][0] + ordered_vertices[blade3_base+44+offset][0])/2)**2)} {ordered_vertices[blade2_base+32+offset][2]})\n")
            f.write(f"    arc {blade2_base+33+offset} {blade3_base+43+offset} ({(ordered_vertices[blade2_base+33+offset][0] + ordered_vertices[blade3_base+43+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+33+offset][0] + ordered_vertices[blade3_base+43+offset][0])/2)**2)} {ordered_vertices[blade2_base+33+offset][2]})\n")
            f.write(f"    arc {blade2_base+34+offset} {blade3_base+42+offset} ({(ordered_vertices[blade2_base+34+offset][0] + ordered_vertices[blade3_base+42+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+34+offset][0] + ordered_vertices[blade3_base+42+offset][0])/2)**2)} {ordered_vertices[blade2_base+34+offset][2]})\n")
            f.write(f"    arc {blade2_base+35+offset} {blade3_base+41+offset} ({(ordered_vertices[blade2_base+35+offset][0] + ordered_vertices[blade3_base+41+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[blade2_base+35+offset][0] + ordered_vertices[blade3_base+41+offset][0])/2)**2)} {ordered_vertices[blade2_base+35+offset][2]})\n")
           
            # gap 3 top left
            f.write(f"    arc {53+offset} {blade2_base+47+offset} ({(ordered_vertices[53+offset][0] + ordered_vertices[blade2_base+47+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[53+offset][0] + ordered_vertices[blade2_base+47+offset][0])/2)**2)} {ordered_vertices[53+offset][2]})\n")
            f.write(f"    arc {54+offset} {blade2_base+46+offset} ({(ordered_vertices[54+offset][0] + ordered_vertices[blade2_base+46+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[54+offset][0] + ordered_vertices[blade2_base+46+offset][0])/2)**2)} {ordered_vertices[54+offset][2]})\n")
            f.write(f"    arc {55+offset} {blade2_base+45+offset} ({(ordered_vertices[55+offset][0] + ordered_vertices[blade2_base+45+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[55+offset][0] + ordered_vertices[blade2_base+45+offset][0])/2)**2)} {ordered_vertices[55+offset][2]})\n")
            f.write(f"    arc {32+offset} {blade2_base+44+offset} ({(ordered_vertices[32+offset][0] + ordered_vertices[blade2_base+44+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[32+offset][0] + ordered_vertices[blade2_base+44+offset][0])/2)**2)} {ordered_vertices[32+offset][2]})\n")
            f.write(f"    arc {33+offset} {blade2_base+43+offset} ({(ordered_vertices[33+offset][0] + ordered_vertices[blade2_base+43+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[33+offset][0] + ordered_vertices[blade2_base+43+offset][0])/2)**2)} {ordered_vertices[33+offset][2]})\n")
            f.write(f"    arc {34+offset} {blade2_base+42+offset} ({(ordered_vertices[34+offset][0] + ordered_vertices[blade2_base+42+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[34+offset][0] + ordered_vertices[blade2_base+42+offset][0])/2)**2)} {ordered_vertices[34+offset][2]})\n")
            f.write(f"    arc {35+offset} {blade2_base+41+offset} ({(ordered_vertices[35+offset][0] + ordered_vertices[blade2_base+41+offset][0])/2} {-np.sqrt((width**2 + (y_coords[j])**2) - ((ordered_vertices[35+offset][0] + ordered_vertices[blade2_base+41+offset][0])/2)**2)} {ordered_vertices[35+offset][2]})\n")

    #%%
    """
    Surrounding mesh (around disc for fixedami)
    """
    
    if write_central:
        f.write(f"    arc {10+disc_vertices_offset} {11+disc_vertices_offset} ({sm_arc_interpolations[3][0]} {sm_arc_interpolations[3][1]} {sm_arc_interpolations[3][2]})\n")
        f.write(f"    arc {14+disc_vertices_offset} {15+disc_vertices_offset} ({sm_arc_interpolations[7][0]} {sm_arc_interpolations[7][1]} {sm_arc_interpolations[7][2]})\n")
        
        f.write(f"    arc {9+disc_vertices_offset} {10+disc_vertices_offset} ({sm_arc_interpolations[2][0]} {sm_arc_interpolations[2][1]} {sm_arc_interpolations[2][2]})\n")
        f.write(f"    arc {13+disc_vertices_offset} {14+disc_vertices_offset} ({sm_arc_interpolations[6][0]} {sm_arc_interpolations[6][1]} {sm_arc_interpolations[6][2]})\n")
       
        f.write(f"    arc {11+disc_vertices_offset} {8+disc_vertices_offset} ({sm_arc_interpolations[0][0]} {sm_arc_interpolations[0][1]} {sm_arc_interpolations[0][2]})\n")
        f.write(f"    arc {15+disc_vertices_offset} {12+disc_vertices_offset} ({sm_arc_interpolations[4][0]} {sm_arc_interpolations[4][1]} {sm_arc_interpolations[4][2]})\n")
       
        f.write(f"    arc {8+disc_vertices_offset} {9+disc_vertices_offset} ({sm_arc_interpolations[1][0]} {sm_arc_interpolations[1][1]} {sm_arc_interpolations[1][2]})\n")
        f.write(f"    arc {12+disc_vertices_offset} {13+disc_vertices_offset} ({sm_arc_interpolations[5][0]} {sm_arc_interpolations[5][1]} {sm_arc_interpolations[5][2]})\n")

    #%%
    """
    Upstream
    """
    
    if write_up_down:
        f.write(f"    arc {22+disc_vertices_offset} {23+disc_vertices_offset} ({up_arc_interpolations[3][0]} {up_arc_interpolations[3][1]} {up_arc_interpolations[3][2]})\n")
        f.write(f"    arc {21+disc_vertices_offset} {22+disc_vertices_offset} ({up_arc_interpolations[2][0]} {up_arc_interpolations[2][1]} {up_arc_interpolations[2][2]})\n")
        f.write(f"    arc {23+disc_vertices_offset} {20+disc_vertices_offset} ({up_arc_interpolations[0][0]} {up_arc_interpolations[0][1]} {up_arc_interpolations[0][2]})\n")
        f.write(f"    arc {20+disc_vertices_offset} {21+disc_vertices_offset} ({up_arc_interpolations[1][0]} {up_arc_interpolations[1][1]} {up_arc_interpolations[1][2]})\n")
    
        f.write(f"    arc {54+disc_vertices_offset} {55+disc_vertices_offset} ({interface_arc_interpolations[3][0]} {interface_arc_interpolations[3][1]} {interface_arc_interpolations[3][2]})\n")
        f.write(f"    arc {53+disc_vertices_offset} {54+disc_vertices_offset} ({interface_arc_interpolations[2][0]} {interface_arc_interpolations[2][1]} {interface_arc_interpolations[2][2]})\n")
        f.write(f"    arc {55+disc_vertices_offset} {52+disc_vertices_offset} ({interface_arc_interpolations[0][0]} {interface_arc_interpolations[0][1]} {interface_arc_interpolations[0][2]})\n")
        f.write(f"    arc {52+disc_vertices_offset} {53+disc_vertices_offset} ({interface_arc_interpolations[1][0]} {interface_arc_interpolations[1][1]} {interface_arc_interpolations[1][2]})\n")
    
        f.write(f"    arc {34+disc_vertices_offset} {35+disc_vertices_offset} ({inner_arc_interpolations[3][0]} {inner_arc_interpolations[3][1]} {inner_arc_interpolations[3][2]})\n")
        f.write(f"    arc {38+disc_vertices_offset} {39+disc_vertices_offset} ({inner_arc_interpolations[7][0]} {inner_arc_interpolations[7][1]} {inner_arc_interpolations[7][2]})\n")
    
        f.write(f"    arc {33+disc_vertices_offset} {34+disc_vertices_offset} ({inner_arc_interpolations[2][0]} {inner_arc_interpolations[2][1]} {inner_arc_interpolations[2][2]})\n")
        f.write(f"    arc {37+disc_vertices_offset} {38+disc_vertices_offset} ({inner_arc_interpolations[6][0]} {inner_arc_interpolations[6][1]} {inner_arc_interpolations[6][2]})\n")
    
        f.write(f"    arc {35+disc_vertices_offset} {32+disc_vertices_offset} ({inner_arc_interpolations[0][0]} {inner_arc_interpolations[0][1]} {inner_arc_interpolations[0][2]})\n")
        f.write(f"    arc {39+disc_vertices_offset} {36+disc_vertices_offset} ({inner_arc_interpolations[4][0]} {inner_arc_interpolations[4][1]} {inner_arc_interpolations[4][2]})\n")
    
        f.write(f"    arc {32+disc_vertices_offset} {33+disc_vertices_offset} ({inner_arc_interpolations[1][0]} {inner_arc_interpolations[1][1]} {inner_arc_interpolations[1][2]})\n")
        f.write(f"    arc {36+disc_vertices_offset} {37+disc_vertices_offset} ({inner_arc_interpolations[5][0]} {inner_arc_interpolations[5][1]} {inner_arc_interpolations[5][2]})\n")
    
        # polo
        f.write(f"    arc {82+disc_vertices_offset} {83+disc_vertices_offset} ({cc_interface_arc_interpolations[3][0]} {cc_interface_arc_interpolations[3][1]} {cc_interface_arc_interpolations[3][2]})\n")
        f.write(f"    arc {86+disc_vertices_offset} {87+disc_vertices_offset} ({cc_interface_arc_interpolations[7][0]} {cc_interface_arc_interpolations[7][1]} {cc_interface_arc_interpolations[7][2]})\n")
        
        f.write(f"    arc {81+disc_vertices_offset} {82+disc_vertices_offset} ({cc_interface_arc_interpolations[2][0]} {cc_interface_arc_interpolations[2][1]} {cc_interface_arc_interpolations[2][2]})\n")
        f.write(f"    arc {85+disc_vertices_offset} {86+disc_vertices_offset} ({cc_interface_arc_interpolations[6][0]} {cc_interface_arc_interpolations[6][1]} {cc_interface_arc_interpolations[6][2]})\n")
    
        f.write(f"    arc {83+disc_vertices_offset} {80+disc_vertices_offset} ({cc_interface_arc_interpolations[0][0]} {cc_interface_arc_interpolations[0][1]} {cc_interface_arc_interpolations[0][2]})\n")
        f.write(f"    arc {87+disc_vertices_offset} {84+disc_vertices_offset} ({cc_interface_arc_interpolations[4][0]} {cc_interface_arc_interpolations[4][1]} {cc_interface_arc_interpolations[4][2]})\n")
    
        f.write(f"    arc {80+disc_vertices_offset} {81+disc_vertices_offset} ({cc_interface_arc_interpolations[1][0]} {cc_interface_arc_interpolations[1][1]} {cc_interface_arc_interpolations[1][2]})\n")
        f.write(f"    arc {84+disc_vertices_offset} {85+disc_vertices_offset} ({cc_interface_arc_interpolations[5][0]} {cc_interface_arc_interpolations[5][1]} {cc_interface_arc_interpolations[5][2]})\n")
        
        # square in polo at turbine
        f.write(f"    arc {66+disc_vertices_offset} {67+disc_vertices_offset} ({polosquare_interface_arc_interpolations[0][0]} {polosquare_interface_arc_interpolations[0][1]} {polosquare_interface_arc_interpolations[0][2]})\n")
        f.write(f"    arc {67+disc_vertices_offset} {64+disc_vertices_offset} ({polosquare_interface_arc_interpolations[1][0]} {polosquare_interface_arc_interpolations[1][1]} {polosquare_interface_arc_interpolations[1][2]})\n")
        
        f.write(f"    arc {64+disc_vertices_offset} {65+disc_vertices_offset} ({polosquare_interface_arc_interpolations[2][0]} {polosquare_interface_arc_interpolations[2][1]} {polosquare_interface_arc_interpolations[2][2]})\n")
        f.write(f"    arc {65+disc_vertices_offset} {66+disc_vertices_offset} ({polosquare_interface_arc_interpolations[3][0]} {polosquare_interface_arc_interpolations[3][1]} {polosquare_interface_arc_interpolations[3][2]})\n")
    
        # square in polo upstream. commented out as worsens non-orthog
        f.write(f"    arc {70+disc_vertices_offset} {71+disc_vertices_offset} ({polosquare_interface_arc_interpolations[4][0]} {polosquare_interface_arc_interpolations[4][1]} {polosquare_interface_arc_interpolations[4][2]})\n")
        f.write(f"    arc {71+disc_vertices_offset} {68+disc_vertices_offset} ({polosquare_interface_arc_interpolations[5][0]} {polosquare_interface_arc_interpolations[5][1]} {polosquare_interface_arc_interpolations[5][2]})\n")
    
        f.write(f"    arc {68+disc_vertices_offset} {69+disc_vertices_offset} ({polosquare_interface_arc_interpolations[6][0]} {polosquare_interface_arc_interpolations[6][1]} {polosquare_interface_arc_interpolations[6][2]})\n")
        f.write(f"    arc {69+disc_vertices_offset} {70+disc_vertices_offset} ({polosquare_interface_arc_interpolations[7][0]} {polosquare_interface_arc_interpolations[7][1]} {polosquare_interface_arc_interpolations[7][2]})\n")
    
       

    #%%
    """
    Downstream
    """
    
    if write_up_down:
        f.write(f"    arc {30+disc_vertices_offset} {31+disc_vertices_offset} ({down_arc_interpolations[3][0]} {down_arc_interpolations[3][1]} {down_arc_interpolations[3][2]})\n")
        f.write(f"    arc {29+disc_vertices_offset} {30+disc_vertices_offset} ({down_arc_interpolations[2][0]} {down_arc_interpolations[2][1]} {down_arc_interpolations[2][2]})\n")
        f.write(f"    arc {31+disc_vertices_offset} {28+disc_vertices_offset} ({down_arc_interpolations[0][0]} {down_arc_interpolations[0][1]} {down_arc_interpolations[0][2]})\n")
        f.write(f"    arc {28+disc_vertices_offset} {29+disc_vertices_offset} ({down_arc_interpolations[1][0]} {down_arc_interpolations[1][1]} {down_arc_interpolations[1][2]})\n")
    
        f.write(f"    arc {62+disc_vertices_offset} {63+disc_vertices_offset} ({interface_arc_interpolations[7][0]} {interface_arc_interpolations[7][1]} {interface_arc_interpolations[7][2]})\n")
        f.write(f"    arc {61+disc_vertices_offset} {62+disc_vertices_offset} ({interface_arc_interpolations[6][0]} {interface_arc_interpolations[6][1]} {interface_arc_interpolations[6][2]})\n")
        f.write(f"    arc {63+disc_vertices_offset} {60+disc_vertices_offset} ({interface_arc_interpolations[4][0]} {interface_arc_interpolations[4][1]} {interface_arc_interpolations[4][2]})\n")
        f.write(f"    arc {60+disc_vertices_offset} {61+disc_vertices_offset} ({interface_arc_interpolations[5][0]} {interface_arc_interpolations[5][1]} {interface_arc_interpolations[5][2]})\n")
    
        f.write(f"    arc {46+disc_vertices_offset} {47+disc_vertices_offset} ({inner_arc_interpolations[15][0]} {inner_arc_interpolations[15][1]} {inner_arc_interpolations[15][2]})\n")
        f.write(f"    arc {42+disc_vertices_offset} {43+disc_vertices_offset} ({inner_arc_interpolations[11][0]} {inner_arc_interpolations[11][1]} {inner_arc_interpolations[11][2]})\n")
    
        f.write(f"    arc {45+disc_vertices_offset} {46+disc_vertices_offset} ({inner_arc_interpolations[14][0]} {inner_arc_interpolations[14][1]} {inner_arc_interpolations[14][2]})\n")
        f.write(f"    arc {41+disc_vertices_offset} {42+disc_vertices_offset} ({inner_arc_interpolations[10][0]} {inner_arc_interpolations[10][1]} {inner_arc_interpolations[10][2]})\n")
    
        f.write(f"    arc {47+disc_vertices_offset} {44+disc_vertices_offset} ({inner_arc_interpolations[12][0]} {inner_arc_interpolations[12][1]} {inner_arc_interpolations[12][2]})\n")
        f.write(f"    arc {43+disc_vertices_offset} {40+disc_vertices_offset} ({inner_arc_interpolations[8][0]} {inner_arc_interpolations[8][1]} {inner_arc_interpolations[8][2]})\n")
    
        f.write(f"    arc {44+disc_vertices_offset} {45+disc_vertices_offset} ({inner_arc_interpolations[13][0]} {inner_arc_interpolations[13][1]} {inner_arc_interpolations[13][2]})\n")
        f.write(f"    arc {40+disc_vertices_offset} {41+disc_vertices_offset} ({inner_arc_interpolations[9][0]} {inner_arc_interpolations[9][1]} {inner_arc_interpolations[9][2]})\n")
    
        # polo
        f.write(f"    arc {94+disc_vertices_offset} {95+disc_vertices_offset} ({cc_interface_arc_interpolations[15][0]} {cc_interface_arc_interpolations[15][1]} {cc_interface_arc_interpolations[15][2]})\n")
        f.write(f"    arc {90+disc_vertices_offset} {91+disc_vertices_offset} ({cc_interface_arc_interpolations[11][0]} {cc_interface_arc_interpolations[11][1]} {cc_interface_arc_interpolations[11][2]})\n")
    
        f.write(f"    arc {93+disc_vertices_offset} {94+disc_vertices_offset} ({cc_interface_arc_interpolations[14][0]} {cc_interface_arc_interpolations[14][1]} {cc_interface_arc_interpolations[14][2]})\n")
        f.write(f"    arc {89+disc_vertices_offset} {90+disc_vertices_offset} ({cc_interface_arc_interpolations[10][0]} {cc_interface_arc_interpolations[10][1]} {cc_interface_arc_interpolations[10][2]})\n")
        
        f.write(f"    arc {95+disc_vertices_offset} {92+disc_vertices_offset} ({cc_interface_arc_interpolations[12][0]} {cc_interface_arc_interpolations[12][1]} {cc_interface_arc_interpolations[12][2]})\n")
        f.write(f"    arc {91+disc_vertices_offset} {88+disc_vertices_offset} ({cc_interface_arc_interpolations[8][0]} {cc_interface_arc_interpolations[8][1]} {cc_interface_arc_interpolations[8][2]})\n")
        
        f.write(f"    arc {92+disc_vertices_offset} {93+disc_vertices_offset} ({cc_interface_arc_interpolations[13][0]} {cc_interface_arc_interpolations[13][1]} {cc_interface_arc_interpolations[13][2]})\n")
        f.write(f"    arc {88+disc_vertices_offset} {89+disc_vertices_offset} ({cc_interface_arc_interpolations[9][0]} {cc_interface_arc_interpolations[9][1]} {cc_interface_arc_interpolations[9][2]})\n")
        
        