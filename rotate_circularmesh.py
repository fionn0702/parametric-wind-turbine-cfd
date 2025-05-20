""" 
SECTION 4
Apply rotations to generate vertices for elliptical mesh surrounding each airfoil in each blade
"""
import numpy as np

def rotate_circularmesh(circle_vertices_array, num_blades, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4):
   
    # Use the original circle vertices array for the first blade
    circle_vertices_array_blade1 = circle_vertices_array.copy()
    
    if num_blades == 2:
        # For 2 blades: Apply 180° rotation to generate the second blade
        circle_vertices_array_blade2 = np.zeros_like(circle_vertices_array)
    
        for j in range(circle_vertices_array.shape[2]):  # Loop through sections
            circle_vertices_array_blade2[:, :, j] = np.dot(circle_vertices_array[:, :, j], rotation_matrices_2[0].T)  # 180°
    
    elif num_blades == 3:
        # For 3 blades: Apply 120° and 240° rotations to generate other blades
        circle_vertices_array_blade2 = np.zeros_like(circle_vertices_array)
        circle_vertices_array_blade3 = np.zeros_like(circle_vertices_array)
    
        for j in range(circle_vertices_array.shape[2]):  # Loop through sections
            circle_vertices_array_blade2[:, :, j] = np.dot(circle_vertices_array[:, :, j], rotation_matrices_3[0].T)  # 120°
            circle_vertices_array_blade3[:, :, j] = np.dot(circle_vertices_array[:, :, j], rotation_matrices_3[1].T)  # 240°
    
    elif num_blades == 4:
        # For 4 blades: Apply 90°, 180°, and 270° rotations to generate other blades
        circle_vertices_array_blade2 = np.zeros_like(circle_vertices_array)
        circle_vertices_array_blade3 = np.zeros_like(circle_vertices_array)
        circle_vertices_array_blade4 = np.zeros_like(circle_vertices_array)
    
        for j in range(circle_vertices_array.shape[2]):  # Loop through sections
            circle_vertices_array_blade2[:, :, j] = np.dot(circle_vertices_array[:, :, j], rotation_matrices_4[0].T)  # 90°
            circle_vertices_array_blade3[:, :, j] = np.dot(circle_vertices_array[:, :, j], rotation_matrices_4[1].T)  # 180°
            circle_vertices_array_blade4[:, :, j] = np.dot(circle_vertices_array[:, :, j], rotation_matrices_4[2].T)  # 270°
            
    return circle_vertices_array_blade1, circle_vertices_array_blade2, circle_vertices_array_blade3