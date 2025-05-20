"""
Section 11S
Write splines
"""

def write_splines(f, N, num_blades, blade_offset, vertices_blade1, vertices_blade2, vertices_blade3, points, vertex0_idx, vertex1_idx, vertex2_idx, vertex3_idx, vertex4_idx, vertex5_idx, vertex6_idx, vertex7_idx, vertex8_idx, vertex9_idx, vertex10_idx, vertex11_idx, vertex12_idx, vertex13_idx, vertex14_idx, vertex15_idx, write_central):
    
    # Splines for all blades
    for blade in range(num_blades):
        blade_start = blade * blade_offset  # Calculate the offset for each blade
    
        # Select the appropriate vertices array for the current blade
        if blade == 0:
            current_vertices = vertices_blade1
        elif blade == 1:
            current_vertices = vertices_blade2
        elif blade == 2:
            current_vertices = vertices_blade3
        elif blade == 3:
            current_vertices = vertices_blade4
            
        # Write splines for each section of the blade
        for j in range(N):
            section_start = j * 56
            total_offset = blade_start + section_start
    
            # Airfoil vertices spline connects
            spline_vertex0 = total_offset  # vertex 0
            spline_vertex1 = total_offset + 1  # vertex 1
            spline_vertex2 = total_offset + 2  # vertex 2
            spline_vertex3 = total_offset + 3  # vertex 3
            spline_vertex4 = total_offset + 4  # vertex 4
            spline_vertex5 = total_offset + 5  # vertex 5
            spline_vertex6 = total_offset + 6  # vertex 6
            spline_vertex7 = total_offset + 7  # vertex 7
            spline_vertex8 = total_offset + 8   # vertex 8
            spline_vertex9 = total_offset + 9   # vertex 9
            spline_vertex10 = total_offset + 10 # vertex 10
            spline_vertex11 = total_offset + 11 # vertex 11
            spline_vertex12 = total_offset + 12 # vertex 12
            spline_vertex13 = total_offset + 13 # vertex 13
            spline_vertex14 = total_offset + 14 # vertex 14
            spline_vertex15 = total_offset + 15 # vertex 15

            # interpolation points
            spline_points = [
                current_vertices[vertex0_idx:vertex1_idx, :, j],
                current_vertices[vertex1_idx:vertex2_idx, :, j],
                current_vertices[vertex2_idx:vertex3_idx, :, j],
                current_vertices[vertex3_idx:vertex4_idx, :, j],
                current_vertices[vertex4_idx:vertex5_idx, :, j],
                current_vertices[vertex5_idx:vertex6_idx, :, j],
                current_vertices[vertex6_idx:vertex7_idx, :, j],
                current_vertices[vertex7_idx:vertex8_idx, :, j],
                current_vertices[vertex8_idx:vertex9_idx, :, j],
                current_vertices[vertex9_idx:vertex10_idx, :, j],
                current_vertices[vertex10_idx:vertex11_idx, :, j],
                current_vertices[vertex11_idx:vertex12_idx, :, j],
                current_vertices[vertex12_idx:vertex13_idx, :, j],
                current_vertices[vertex13_idx:vertex14_idx, :, j],
                current_vertices[vertex14_idx:vertex15_idx, :, j],
                current_vertices[vertex15_idx:points, :, j],
            ]

            
            # actual vertices to be splined together
            spline_vertices = [
                (spline_vertex0, spline_vertex1),
                (spline_vertex1, spline_vertex2),
                (spline_vertex2, spline_vertex3),
                (spline_vertex3, spline_vertex4),
                (spline_vertex4, spline_vertex5),
                (spline_vertex5, spline_vertex6),
                (spline_vertex6, spline_vertex7),
                (spline_vertex7, spline_vertex8),
                (spline_vertex8, spline_vertex9),
                (spline_vertex9, spline_vertex10),
                (spline_vertex10, spline_vertex11),
                (spline_vertex11, spline_vertex12),
                (spline_vertex12, spline_vertex13),
                (spline_vertex13, spline_vertex14),
                (spline_vertex14, spline_vertex15),
                (spline_vertex15, spline_vertex0),  
            ]

    
            #Write splines
            if write_central:
                for idx, (v_start, v_end) in enumerate(spline_vertices):
                    f.write(f"    spline {v_start} {v_end}\n    (\n")
                    for point in spline_points[idx]:
                        f.write(f"        ({point[0]} {point[1]} {point[2]})\n")
                    f.write("    )\n")

    
    f.write(");\n")