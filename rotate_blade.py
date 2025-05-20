"""
SECTION 2
Generate other turbine blades (airfoil vertices) by applying a rotation. (3 blades = 120 degrees)
"""

import numpy as np

def rotate_blade(vertices, num_blades, N, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4):
    
    
    # Use the original vertices as the first blade
    vertices_blade1 = vertices.copy()
    
    if num_blades == 2:
        # For 2 blades: Apply 180° rotation to generate the second blade
        vertices_blade2 = np.zeros_like(vertices)
    
        for j in range(N):  # Loop through airfoil sections
            vertices_blade2[:, :, j] = np.dot(vertices[:, :, j], rotation_matrices_2[0].T)  # 180°
            
    elif num_blades == 3:
        # For 3 blades: Apply 120° and 240° rotations to generate other blades
        vertices_blade2 = np.zeros_like(vertices)
        vertices_blade3 = np.zeros_like(vertices)
    
        for j in range(N):  # Loop through airfoil sections
            vertices_blade2[:, :, j] = np.dot(vertices[:, :, j], rotation_matrices_3[0].T)  # 120°
            vertices_blade3[:, :, j] = np.dot(vertices[:, :, j], rotation_matrices_3[1].T)  # 240°
            
            
    
    elif num_blades == 4:
        # For 4 blades: Apply 90°, 180°, and 270° rotations to generate other blades
        vertices_blade2 = np.zeros_like(vertices)
        vertices_blade3 = np.zeros_like(vertices)
        vertices_blade4 = np.zeros_like(vertices)
    
        for j in range(N):  # Loop through airfoil sections
            vertices_blade2[:, :, j] = np.dot(vertices[:, :, j], rotation_matrices_4[0].T)  # 90°
            vertices_blade3[:, :, j] = np.dot(vertices[:, :, j], rotation_matrices_4[1].T)  # 180°
            vertices_blade4[:, :, j] = np.dot(vertices[:, :, j], rotation_matrices_4[2].T)  # 270°
    
    return vertices_blade1, vertices_blade2, vertices_blade3