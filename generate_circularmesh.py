"""
SECTION 3
Generate vertices for circular mesh surrounding each arifoil
Uses centre of first aifoil section (root) to create a circle with a optional stretch factor for ellipse
"""

import numpy as np

def generate_circularmesh(vertices, N, x_stretch, width, y_coords, z_stretch, blade_rotate_deg):
    
    # Centred on origin
    centre_mesh_circle_x = 0 
    centre_mesh_circle_z = 0
    
    
    #Radius equal to the root chord length
    #chord_length_root =  abs(np.max(vertices[:, 0, 0]) - np.min(vertices[:, 0, 0]))
    
    # Set radius equal to half of bounding box width
    radius = 3.5 #width/1.75 #width/2 #np.full(N, round(0.75 * chord_length_root) + 1) # Rounds to the nearest integer
    
    
    # Ellipse requires 8 points for vertices and 8 points for arc interpolation
    # Define angles for the 16 vertices, starting from the positive x-axis and going counterclockwise
    angles = np.linspace(0, 2 * np.pi, 33)[:-1]  # 16 points spaced evenly (it excludes the last point (2*pi))
    
    
    
    # Change specific indices to make trailing edge circular vertices closer. Indexing may change here on case by case basis!!
    angles[17]  = angles[17] - np.radians(10)  
    angles[18]  = angles[18] - np.radians(10)  


    
    # Define 10-degree rotation about Y-axis
    theta_rad = np.radians(0)
    
    R_y = np.array([
        [np.cos(theta_rad), 0, np.sin(theta_rad)],
        [0, 1, 0],
        [-np.sin(theta_rad), 0, np.cos(theta_rad)]
    ])
    
    # Initialize a 3D matrix to store the circle vertices
    circle_vertices_array = np.zeros((len(angles), 3, N))
    
    # Iterate over each section to assign x, y, and z coordinates
    for j in range(N):
        for i, angle in enumerate(angles):
            
            # ellipse is flat on x-z plane and curved in y
            x = centre_mesh_circle_x + x_stretch * radius * np.cos(angle)
            z = centre_mesh_circle_z + z_stretch * radius * np.sin(angle)
            
            # Apply rotation to (x, z)
            rotated_x, _, rotated_z = np.dot(R_y, np.array([x, 0, z]))
            
            # Compute y using rotated_x
            R = np.sqrt(width**2 + (y_coords[j])**2)  
            y = np.sqrt(R**2 - rotated_x**2)  

            # Assign rotated values
            circle_vertices_array[i, :, j] = [rotated_x, y, rotated_z]
    
    # Reverse to align correctly
    circle_vertices_array[:, 0, :] = -circle_vertices_array[:, 0, :]
    circle_vertices_array[:, 2, :] = -circle_vertices_array[:, 2, :]
    
    return circle_vertices_array