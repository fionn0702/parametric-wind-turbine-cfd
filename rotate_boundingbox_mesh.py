import numpy as np

def rotate_boundingbox_mesh(box_coords, num_blades, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4):    


# Use the original box coordinates for the first blade
    box_coords_blade1 = box_coords.copy()
    
    if num_blades == 2:
        # For 2 blades: Apply 180° rotation to generate the second blade
        box_coords_blade2 = np.zeros_like(box_coords)
    
        for j in range(box_coords.shape[2]):  # Loop through sections
            box_coords_blade2[:, :, j] = np.dot(box_coords[:, :, j], rotation_matrices_2[0].T)  # 180°
    
    elif num_blades == 3:
        # For 3 blades: Apply 120° and 240° rotations to generate other blades
        box_coords_blade2 = np.zeros_like(box_coords)
        box_coords_blade3 = np.zeros_like(box_coords)
    
        for j in range(box_coords.shape[2]):  # Loop through sections
            box_coords_blade2[:, :, j] = np.dot(box_coords[:, :, j], rotation_matrices_3[0].T)  # 120°
            box_coords_blade3[:, :, j] = np.dot(box_coords[:, :, j], rotation_matrices_3[1].T)  # 240°
    
    elif num_blades == 4:
        # For 4 blades: Apply 90°, 180°, and 270° rotations to generate other blades
        box_coords_blade2 = np.zeros_like(box_coords)
        box_coords_blade3 = np.zeros_like(box_coords)
        box_coords_blade4 = np.zeros_like(box_coords)
    
        for j in range(box_coords.shape[2]):  # Loop through sections
            box_coords_blade2[:, :, j] = np.dot(box_coords[:, :, j], rotation_matrices_4[0].T)  # 90°
            box_coords_blade3[:, :, j] = np.dot(box_coords[:, :, j], rotation_matrices_4[1].T)  # 180°
            box_coords_blade4[:, :, j] = np.dot(box_coords[:, :, j], rotation_matrices_4[2].T)  # 270°

    return box_coords_blade1, box_coords_blade2, box_coords_blade3