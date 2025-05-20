"""
SECTION 5
Generate vertices for bounding box mesh 
"""

# CHANGES 21/03/25
# removed -1 from every width 

import numpy as np

def generate_boundingbox_mesh(N, width, y_coords, circle_vertices_array_blade1):

    box_coords = np.zeros((24, 3, N)) # Initialise 16 vertices per airfoil section
    
    # Generate vertices, [x] represents vertex number on first airoil for demonstration
    for j in range(N):
        R = np.sqrt(width**2 + (y_coords[j])**2)
            
        box_coords[:, :, j] = [
        (-width, y_coords[j], circle_vertices_array_blade1[0, 2, 0]),   # [32]
        (-width, y_coords[j], circle_vertices_array_blade1[2, 2, 0]),   # [33]
        (-width, y_coords[j], circle_vertices_array_blade1[4, 2, 0]),                                  # [34]
        (-width, y_coords[j], - width),  # [35]
        (circle_vertices_array_blade1[4, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[4, 0, 0]**2), -width),  # [36]
        (circle_vertices_array_blade1[6, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[6, 0, 0]**2), -width),  # [37]
        (circle_vertices_array_blade1[8, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[8, 0, 0]**2), -width),                                   # [38]
        (circle_vertices_array_blade1[10, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[10, 0, 0]**2), -width),    # [39]
        (circle_vertices_array_blade1[12, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[12, 0, 0]**2), -width),    # [40]
        (width, y_coords[j], -width),   # [41]
        (width, y_coords[j], circle_vertices_array_blade1[12, 2, 0]),                                    # [42]
        (width, y_coords[j], circle_vertices_array_blade1[14, 2, 0]),   # [43]
        (width, y_coords[j], circle_vertices_array_blade1[16, 2, 0]),   # [44]
        (width, y_coords[j], circle_vertices_array_blade1[18, 2, 0]),   # [45]
        (width, y_coords[j], circle_vertices_array_blade1[20, 2, 0]),                                   # [46]
        (width, y_coords[j], width),  # [47]
        (circle_vertices_array_blade1[20, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[20, 0, 0]**2), width),  # [48]
        (circle_vertices_array_blade1[22, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[22, 0, 0]**2), width),  # [49]
        (circle_vertices_array_blade1[24, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[24, 0, 0]**2), width),  # [50]
        (circle_vertices_array_blade1[26, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[26, 0, 0]**2), width),  # [51]
        (circle_vertices_array_blade1[28, 0, 0], np.sqrt(R**2 - circle_vertices_array_blade1[28, 0, 0]**2), width),  # [52]
        (-width, y_coords[j], width),  # [53]
        (-width, y_coords[j], circle_vertices_array_blade1[28, 2, 0]),  # [54]
        (-width, y_coords[j], circle_vertices_array_blade1[30, 2, 0]),  # [55]

        
    ]

    return box_coords