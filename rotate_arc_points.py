"""
SECTION 9
Rotate arc points for 3 blades
"""

import numpy as np

def rotate_arc_points(arc_array, num_blades, N, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4):
    
    
    # Use the original arc_array as the first blade
    arc_points_blade1 = arc_array.copy()
    
    if num_blades == 2:
        
        # For 2 blades: Apply 180° rotation to generate the second blade
        arc_points_blade2 = np.zeros_like(arc_array)
    
        for j in range(N):  # Loop through airfoil sections
            arc_points_blade2[:, :, j] = np.dot(arc_array[:, :, j], rotation_matrices_2[0].T)  # 180°
            
    elif num_blades == 3:
        # For 3 blades: Apply 120° and 240° rotations to generate other blades
        arc_points_blade2 = np.zeros_like(arc_array)
        arc_points_blade3 = np.zeros_like(arc_array)
    
        for j in range(N):  # Loop through airfoil sections
            arc_points_blade2[:, :, j] = np.dot(arc_array[:, :, j], rotation_matrices_3[0].T)  # 120°
            arc_points_blade3[:, :, j] = np.dot(arc_array[:, :, j], rotation_matrices_3[1].T)  # 240°
    
    elif num_blades == 4:
        # For 4 blades: Apply 90°, 180°, and 270° rotations to generate other blades
        arc_points_blade2 = np.zeros_like(arc_array)
        arc_points_blade3 = np.zeros_like(arc_array)
        arc_points_blade4 = np.zeros_like(arc_array)
    
        for j in range(N):  # Loop through airfoil sections
            arc_points_blade2[:, :, j] = np.dot(arc_array[:, :, j], rotation_matrices_4[0].T)  # 90°
            arc_points_blade3[:, :, j] = np.dot(arc_array[:, :, j], rotation_matrices_4[1].T)  # 180°
            arc_points_blade4[:, :, j] = np.dot(arc_array[:, :, j], rotation_matrices_4[2].T)  # 270°
    
    return arc_points_blade1, arc_points_blade2, arc_points_blade3