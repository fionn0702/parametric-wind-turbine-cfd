"""
SECTION 1
Generate airfoil sections using Kármán-Trefftz Transformation (circle -> airfoil)
and Generate Blade shape. 
"""
import numpy as np

def generate_blade(points, height, N, base_height, trailing_edge_angle_deg, num_root_sections, radius_root, 
                         centre_x_end, centre_z_end, max_thickness_fraction, radius_airfoil_start, radius_thick, 
                         radius_tip, centre_x_start, centre_z_start, x_stretch, b, width, blade_rotate_deg, 
                         taper_z_start, taper_z_end, taper_z_rate, taper_x_start, taper_x_end, taper_x_rate):    
    
    #%% 
    """
    Constants
    """
    
    theta = np.linspace(0, 2 * np.pi, points)              # Theta values for circle
    y_coords = np.linspace(0, height, N) + base_height     # y-coordinates for each section (altitude)
    
    # Calculate n based on trailing edge angle
    trailing_edge_angle = np.deg2rad(trailing_edge_angle_deg)
    n = 1.8 #2 - (trailing_edge_angle / np.pi)                  # Parameter n default to 1.8
    
    #%%
    """
    Initialisation
    """
    
    # Initialise circle centre and radius of N sections
    radii = np.zeros(N)                   # Initialise radii array
    centres = np.zeros(N, dtype=complex)  # Initialise centres as complex numbers
    
    # Vertices is 3D array that stores every point on N sections
    vertices = np.zeros((points, 3, N))   # Initialise vertices 3-D matrix 
    
    #%%
    """
    Radii calculations
    """
    
    # Root sections have constant radius
    radii[:num_root_sections] = radius_root
    
    # Generate radii with taper effect: Above root, blade will enlargen until maximum thickness then taper off to small tip
    fraction_increasing = int(max_thickness_fraction * (N - num_root_sections))  # Fraction of sections exhibiting increasing radii
    fraction_decreasing = N - num_root_sections - fraction_increasing            # Fraction of sections exhibiting decreasing radii
    
    # Split the range: Faster from radius_root to radius_thick, slower from radius_thick to radius_tip
    radii_rise = np.linspace(radius_airfoil_start, radius_thick, fraction_increasing, endpoint=False)   # Fast rise
    radii_fall = np.linspace(radius_thick, radius_tip, fraction_decreasing)                             # Slow fall
    
    # Comcatenate the 3 radii sections
    radii[num_root_sections:] = np.concatenate((radii_rise, radii_fall))           # Assign to transformed sections
    
    #%%
    """
    Centre Calculations
    """

    # Root sections are centred on origin
    for j in range(num_root_sections):
        centres[j] = 0 + 0j             # Centered on the origin
        
    # Linear interpolation between specified centres for remaining centres
    centre_x = np.linspace(centre_x_start, centre_x_end, N - num_root_sections) 
    centre_z = np.linspace(centre_z_start, centre_z_end, N - num_root_sections)
    
    # Put x and z centres into complex 'centres' array
    for j in range(num_root_sections, N):
        centres[j] = complex(centre_x[j - num_root_sections], centre_z[j - num_root_sections])
    
    
    #%%
    """
    Generate circles then airfoils
    """
    
    
    for j in range(N):
        # Generate circles that will be transformed with K-T
        circle_points = centres[j] + radii[j] * np.exp(1j * theta)
        
        # 'airfoil_points' stores every section along the blade including root
        # Keep root as circle
        if j < num_root_sections:
            airfoil_points = circle_points
        else:
            # Apply Kármán-Trefftz transformation
            airfoil_points = (
                n * b * ((circle_points + b) ** n + (circle_points - b) ** n) /
                ((circle_points + b) ** n - (circle_points - b) ** n))
        
        # Re-center the airfoil back to (0,0) by subtracting the original center
        initial_center = centres[j]  # This is where the airfoil is originally centered before transformation
        airfoil_points -= initial_center  # Shift the airfoil back to the origin
        
        
        # Assign x and z coordinates to vertices
        vertices[:, 0, j] = np.real(airfoil_points)  # X-coordinates
        vertices[:, 2, j] = -np.imag(airfoil_points)  # Z-coordinates
        
    
    # Reverse Direction     
    vertices[:, 0, :] = -vertices[:, 0, :]   
    #%%
    """
    Tapering in x and z to get blade shape
    """
    # Number of sections involved in the transition
    taper_start = num_root_sections  # Start of transition
    taper_end = N # taper_start + int(0.1 * N)  # Define how long the transition lasts
    
    # Generate a smooth tapering effect
    #tapering_factor_z = np.linspace(1.2, 0.3, taper_end - taper_start)  # Linear
    
    # Exponential Decay for z-coords (Rapid Initial Drop)
    x = np.linspace(0, 1, taper_end - taper_start)                                                  # Normalised range
    tapering_factor_z = taper_z_end + (taper_z_start - taper_z_end) * np.exp(-taper_z_rate * x)     # exponential gives tapering effect

    tapering_factor_x = np.linspace(1.0, 0.4, taper_end - taper_start)                              # Linear (simpler)
    # tapering_factor_x = taper_x_end + (taper_x_start - taper_x_end) * np.exp(-taper_x_rate * x)   # Optional exponential for x

    # Apply stretching in z-direction to transition sections
    for j in range(taper_start, taper_end):
        
        vertices[:, 2, j] *= tapering_factor_z[j - taper_start]  # Scale z-coordinates
        vertices[:, 0, j] *= tapering_factor_x[j - taper_start]  # Scale x-coordinates

    #%%
    """
    Rotate blade on axis
    """
    # Optional: Enforce overall rotation angle (twist blade on its axis)
    optional_angle = 0
    blade_rotate_rad = np.radians(optional_angle)  # Convert degrees to radians
    
    # Rotation matrix about the y-axis
    R_y = np.array([
        [np.cos(blade_rotate_rad), 0, np.sin(blade_rotate_rad)],
        [0, 1, 0],
        [-np.sin(blade_rotate_rad), 0, np.cos(blade_rotate_rad)]
    ])
    
    # Apply the rotation to each point in the vertices array
    for j in range(N):                                        # Loop through each airfoil section
        vertices[:, :, j] = np.dot(vertices[:, :, j], R_y.T)  # Rotate each point
    
    
    # Twist and taper effect (this is specified in main script)
    for j in range(N):

        taper_factor = 1  - (j / (N - 1))

        tapered_rotate_deg = taper_factor * blade_rotate_deg  # Apply tapering effect
        tapered_rotate_rad = np.radians(tapered_rotate_deg)   # Convert to radians
        
        # Rotation matrix about the y-axis
        R_y = np.array([
            [np.cos(tapered_rotate_rad), 0, np.sin(tapered_rotate_rad)],
            [0, 1, 0],
            [-np.sin(tapered_rotate_rad), 0, np.cos(tapered_rotate_rad)]
        ])
        
        # Apply the rotation to each point in the vertices array
        vertices[:, :, j] = np.dot(vertices[:, :, j], R_y.T)  # Rotate each point
    
    
    # Calculate the y-coordinates after rotation (has to be done after due to curving)
    for j in range(N):
        # Calculate the radius of each section (constant width, changing y-coordinates)
        R = np.sqrt(width**2 + (y_coords[j])**2)
        
        # Assign y coordinates using a circle centered on origin
        vertices[:, 1, j] = np.sqrt(R**2 - vertices[:, 0, j]**2)   # Y-coordinates
        
    #%%
    """
    Centre blade on leading edge
    """
    # # Define target x-coordinate for alignment
    # target_leading_edge_x = radius_root  
     
    # # Compute shift required for all sections at once
    # shift_x = target_leading_edge_x - np.max(vertices[:, 0, :], axis=0) #axis=0 ensures that we find the maximum  x-coordinate for each section separately 
   
    # # Apply shift
    # vertices[:, 0, :] += shift_x
    #%%
    """
    First Blade vertices are now created
    """
    
    return vertices, y_coords, centre_x, centre_z, R, radii
