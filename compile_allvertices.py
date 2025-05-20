""" 
SECTION 7
Compile and sort blade airfoil and mesh vertices (not surrounding disc mesh)
"""

import numpy as np

def compile_allvertices(num_blades, N, vertices, points, vertices_blade1, vertices_blade2, vertices_blade3, circle_vertices_array_blade1, circle_vertices_array_blade2, circle_vertices_array_blade3, box_coords_blade1, box_coords_blade2, box_coords_blade3):

    # Define order_vertices matrix 
    ordered_vertices = []
    surrounding_circle_vertices = []
    surrounding_box_vertices = []
    
    # Dictionary to map blade numbers to their corresponding variables
    blade_data = {
        1: (vertices_blade1, circle_vertices_array_blade1, box_coords_blade1),
        2: (vertices_blade2, circle_vertices_array_blade2, box_coords_blade2),
        3: (vertices_blade3, circle_vertices_array_blade3, box_coords_blade3),
    }
    
    # Loop over the number of blades
    for blade_num in range(1, num_blades + 1):
        if blade_num not in blade_data:
            continue  # Skip if blade data doesn't exist (shouldn't happen)

        # Select the correct blade data
        current_blade_vertices, current_circle_vertices, current_box_vertices = blade_data[blade_num]

        for j in range(N):
            
            # Extract x and y coordinates
            x_coords = vertices[:, 0, j]
            
            # Identify the 8 key vertices index
            # Identify the 16 key vertices index
            vertex0_idx  = int(round(points *  0 / 16))
            vertex1_idx  = int(round(points *  1 / 16))
            vertex2_idx  = int(round(points *  2 / 16))
            vertex3_idx  = int(round(points *  3 / 16))
            vertex4_idx  = int(round(points *  4 / 16))
            vertex5_idx  = int(round(points *  5 / 16))
            vertex6_idx  = int(round(points *  6 / 16))
            vertex7_idx  = int(round(points *  7.25 / 16))
            vertex8_idx  = int(np.argmax(x_coords)) #round(points *  8.3 / 16))
            vertex9_idx  = int(round(points *  9.5 / 16))
            vertex10_idx = int(round(points * 10 / 16))
            vertex11_idx = int(round(points * 11 / 16))
            vertex12_idx = int(round(points * 12 / 16))
            vertex13_idx = int(round(points * 13 / 16))
            vertex14_idx = int(round(points * 14 / 16))
            vertex15_idx = int(round(points * 15 / 16))
            
            
            # # -180  degrees  
            # trail_idx = int(round(points * 5 / 8))                               # Trailing edge [0]
            # vertex1_idx = int(round(points * 6 / 8))    # 1/8th [1]
            # vertex2_idx = int(round(points * 7 / 8))   # 2/8th [2]
            # vertex3_idx = int(round(points * 0 / 8)) #np.argmax(x_coords) #int(round(points * 0 / 8))   # 3/8th [3]
            # lead_idx = int(round(points * 1 / 8)) #np.argmax(x_coords)             # Leading edge [4]
            # vertex5_idx = int(round(points * 2 / 8))  # 5/8th [5]
            # vertex6_idx = int(round(points * 3 / 8))  # 6/8th [6]
            # vertex7_idx = int(round(points * 4 / 8))   # 7/8th [7]



            # Ordered vertices for the current blade
            
            # Ordered vertices list for each airfoil. .extend is used to add multiple elements to a list called ordered_vertices
            # Ordered vertices list for each airfoil section (using 16 key points)
            ordered_vertices.extend([
                (current_blade_vertices[vertex0_idx, 0, j], current_blade_vertices[vertex0_idx, 1, j], current_blade_vertices[vertex0_idx, 2, j]),
                (current_blade_vertices[vertex1_idx, 0, j], current_blade_vertices[vertex1_idx, 1, j], current_blade_vertices[vertex1_idx, 2, j]),
                (current_blade_vertices[vertex2_idx, 0, j], current_blade_vertices[vertex2_idx, 1, j], current_blade_vertices[vertex2_idx, 2, j]),
                (current_blade_vertices[vertex3_idx, 0, j], current_blade_vertices[vertex3_idx, 1, j], current_blade_vertices[vertex3_idx, 2, j]),
                (current_blade_vertices[vertex4_idx, 0, j], current_blade_vertices[vertex4_idx, 1, j], current_blade_vertices[vertex4_idx, 2, j]),
                (current_blade_vertices[vertex5_idx, 0, j], current_blade_vertices[vertex5_idx, 1, j], current_blade_vertices[vertex5_idx, 2, j]),
                (current_blade_vertices[vertex6_idx, 0, j], current_blade_vertices[vertex6_idx, 1, j], current_blade_vertices[vertex6_idx, 2, j]),
                (current_blade_vertices[vertex7_idx, 0, j], current_blade_vertices[vertex7_idx, 1, j], current_blade_vertices[vertex7_idx, 2, j]),
                (current_blade_vertices[vertex8_idx, 0, j], current_blade_vertices[vertex8_idx, 1, j], current_blade_vertices[vertex8_idx, 2, j]),
                (current_blade_vertices[vertex9_idx, 0, j], current_blade_vertices[vertex9_idx, 1, j], current_blade_vertices[vertex9_idx, 2, j]),
                (current_blade_vertices[vertex10_idx, 0, j], current_blade_vertices[vertex10_idx, 1, j], current_blade_vertices[vertex10_idx, 2, j]),
                (current_blade_vertices[vertex11_idx, 0, j], current_blade_vertices[vertex11_idx, 1, j], current_blade_vertices[vertex11_idx, 2, j]),
                (current_blade_vertices[vertex12_idx, 0, j], current_blade_vertices[vertex12_idx, 1, j], current_blade_vertices[vertex12_idx, 2, j]),
                (current_blade_vertices[vertex13_idx, 0, j], current_blade_vertices[vertex13_idx, 1, j], current_blade_vertices[vertex13_idx, 2, j]),
                (current_blade_vertices[vertex14_idx, 0, j], current_blade_vertices[vertex14_idx, 1, j], current_blade_vertices[vertex14_idx, 2, j]),
                (current_blade_vertices[vertex15_idx, 0, j], current_blade_vertices[vertex15_idx, 1, j], current_blade_vertices[vertex15_idx, 2, j])
            ])

            
            # Define surrounding circle vertices for each section
            # Define every even-numbered surrounding circle vertex from 0 to 30 (16 total)
            surrounding_circle_vertices = [
                (current_circle_vertices[i, 0, j], current_circle_vertices[i, 1, j], current_circle_vertices[i, 2, j])
                for i in range(0, 31, 2)
            ]

            # Define surrounding circle vertices for each section
            # Define every even-numbered surrounding circle vertex from 0 to 30 (16 total)
            surrounding_box_vertices = [
                (current_box_vertices[i, 0, j], current_box_vertices[i, 1, j], current_box_vertices[i, 2, j])
                for i in range(0, 24, 1)
            ]
            
            # Construct the surrounding box vertices for Blade 1, using the 3D matrix `box_coords_blade1`
            # surrounding_box_vertices = [
            #     (current_box_vertices[0, 0, j], current_box_vertices[0, 1, j], current_box_vertices[0, 2, j]),  # [16]
            #     (current_box_vertices[1, 0, j], current_box_vertices[1, 1, j], current_box_vertices[1, 2, j]),  # [17]
            #     (current_box_vertices[2, 0, j], current_box_vertices[2, 1, j], current_box_vertices[2, 2, j]),  # [18]
            #     (current_box_vertices[3, 0, j], current_box_vertices[3, 1, j], current_box_vertices[3, 2, j]),  # [19]
            #     (current_box_vertices[4, 0, j], current_box_vertices[4, 1, j], current_box_vertices[4, 2, j]),  # [20]
            #     (current_box_vertices[5, 0, j], current_box_vertices[5, 1, j], current_box_vertices[5, 2, j]),  # [21]
            #     (current_box_vertices[6, 0, j], current_box_vertices[6, 1, j], current_box_vertices[6, 2, j]),  # [22]
            #     (current_box_vertices[7, 0, j], current_box_vertices[7, 1, j], current_box_vertices[7, 2, j]),  # [23]
            #     (current_box_vertices[8, 0, j], current_box_vertices[8, 1, j], current_box_vertices[8, 2, j]),  # [24]
            #     (current_box_vertices[9, 0, j], current_box_vertices[9, 1, j], current_box_vertices[9, 2, j]),  # [25]
            #     (current_box_vertices[10, 0, j],current_box_vertices[10, 1, j], current_box_vertices[10, 2, j]),  # [26]
            #     (current_box_vertices[11, 0, j], current_box_vertices[11, 1, j], current_box_vertices[11, 2, j]),  # [27]`
            #     (current_box_vertices[12, 0, j], current_box_vertices[12, 1, j], current_box_vertices[12, 2, j]),  # [28]
            #     (current_box_vertices[13, 0, j], current_box_vertices[13, 1, j], current_box_vertices[13, 2, j]),  # [29]
            #     (current_box_vertices[14, 0, j], current_box_vertices[14, 1, j], current_box_vertices[14, 2, j]),  # [30]
            #     (current_box_vertices[15, 0, j], current_box_vertices[15, 1, j], current_box_vertices[15, 2, j]),  # [31]
            # ]

            # Extend vertices lists
            ordered_vertices.extend(surrounding_circle_vertices)
            ordered_vertices.extend(surrounding_box_vertices)
            
    return ordered_vertices, x_coords, vertex0_idx, vertex1_idx, vertex2_idx, vertex3_idx, vertex4_idx, vertex5_idx, vertex6_idx, vertex7_idx, vertex8_idx, vertex9_idx, vertex10_idx, vertex11_idx, vertex12_idx, vertex13_idx, vertex14_idx, vertex15_idx 