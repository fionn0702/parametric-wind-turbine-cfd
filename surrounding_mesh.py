""" 
SECTION 10
Generate vertices of mesh surrounding turbine disc mesh (for fixedAMI) as well
as up and downstream meshes to create box domain
"""

import numpy as np

def surrounding_mesh(height, width, R, y_coords, ordered_vertices):    

    #%%
    """
    Constants
    """
    
    # Define coords (sm = surrounding mesh)
    x_sm = 2.5 * height
    y_sm = 2.5 * height
    z_sm = width #- 1                # sm z 
    z_up = 5*z_sm #20*z_sm                  # upstream z coord
    z_down = -60*z_sm #-60*z_sm
    
    R0 = np.sqrt(width**2 + (y_coords[0])**2)    # Radius at root
    
    
    # Define angles for vertices in radians (45, 135, 225, 315 degrees)
    angles_sm = np.radians([45, 135, 225, 315])
    
    # Define angles for arc interpolations in radians (45, 135, 225, 315 degrees)
    arc_angles_sm = np.radians([0, 90, 180, 270])
    
 
    #%%
    """
    Around AMI
    """
    
    # Define box vertices (bottom to top, front to back)
    sm_vertices = np.array([
        [-x_sm, -y_sm, z_sm],  # 0 Bottom Left Front
        [ x_sm, -y_sm, z_sm],  # 1 Bottom Right Front
        [ x_sm,  y_sm, z_sm],  # 2 Top Right Front
        [-x_sm,  y_sm, z_sm],  # 3 Top Left Front
        
        [-x_sm, -y_sm,  -z_sm],  # 4 Bottom Left Back
        [ x_sm, -y_sm,  -z_sm],  # 5 Bottom Right Back
        [ x_sm,  y_sm,  -z_sm],  # 6 Top Right Back
        [-x_sm,  y_sm,  -z_sm],  # 7 Top Left Back
        
        [R * np.cos(angles_sm[0]), R * np.sin(angles_sm[0]), z_sm], # 8 Circle Top Right Front 
        [R * np.cos(angles_sm[1]), R * np.sin(angles_sm[1]), z_sm], # 9 Circle Top Left Left Front 
        [R * np.cos(angles_sm[2]), R * np.sin(angles_sm[2]), z_sm], # 10 Circle Bottom Left Front 
        [R * np.cos(angles_sm[3]), R * np.sin(angles_sm[3]), z_sm], # 11 Circle Bottom Right Front 
        
        [R * np.cos(angles_sm[0]), R * np.sin(angles_sm[0]), -z_sm], # 12 Circle Top Right Back 
        [R * np.cos(angles_sm[1]), R * np.sin(angles_sm[1]), -z_sm], # 13 Circle Top Left Back 
        [R * np.cos(angles_sm[2]), R * np.sin(angles_sm[2]), -z_sm], # 14 Circle Bottom Left Back 
        [R * np.cos(angles_sm[3]), R * np.sin(angles_sm[3]), -z_sm], # 15 Circle Bottom Right Back 
        
    ])
    
    
    sm_arc_interpolations = np.array([
        [R * np.cos(arc_angles_sm[0]), R * np.sin(arc_angles_sm[0]), z_sm], # interpolation point for sm_vertices 11, 8
        [R * np.cos(arc_angles_sm[1]), R * np.sin(arc_angles_sm[1]), z_sm], # 8, 9
        [R * np.cos(arc_angles_sm[2]), R * np.sin(arc_angles_sm[2]), z_sm], # 9, 10
        [R * np.cos(arc_angles_sm[3]), R * np.sin(arc_angles_sm[3]), z_sm], # 10,11

        [R * np.cos(arc_angles_sm[0]), R * np.sin(arc_angles_sm[0]), -z_sm], # 15, 12
        [R * np.cos(arc_angles_sm[1]), R * np.sin(arc_angles_sm[1]), -z_sm], # 12, 13
        [R * np.cos(arc_angles_sm[2]), R * np.sin(arc_angles_sm[2]), -z_sm], # 13, 14
        [R * np.cos(arc_angles_sm[3]), R * np.sin(arc_angles_sm[3]), -z_sm], # 14, 15
        
    ])
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, sm_vertices))
    
    #%%
    """
    Upstream
    """
    # Define box vertices (bottom to top, front to back)
    up_vertices = np.array([
        [-x_sm, -y_sm, z_up],  # 0 Bottom Left Front
        [ x_sm, -y_sm, z_up],  # 1 Bottom Right Front
        [ x_sm,  y_sm, z_up],  # 2 Top Right Front
        [-x_sm,  y_sm, z_up],  # 3 Top Left Front
        
        
        [R * np.cos(angles_sm[0]), R * np.sin(angles_sm[0]), z_up], # 8 Circle Top Right Front 
        [R * np.cos(angles_sm[1]), R * np.sin(angles_sm[1]), z_up], # 9 Circle Top Left Left Front 
        [R * np.cos(angles_sm[2]), R * np.sin(angles_sm[2]), z_up], # 10 Circle Bottom Left Front 
        [R * np.cos(angles_sm[3]), R * np.sin(angles_sm[3]), z_up], # 11 Circle Bottom Right Front 
        
        
    ])
    
    
    up_arc_interpolations = np.array([
        [R * np.cos(arc_angles_sm[0]), R * np.sin(arc_angles_sm[0]), z_up], # interpolation point for sm_vertices 11, 8
        [R * np.cos(arc_angles_sm[1]), R * np.sin(arc_angles_sm[1]), z_up], # 8, 9
        [R * np.cos(arc_angles_sm[2]), R * np.sin(arc_angles_sm[2]), z_up], # 9, 10
        [R * np.cos(arc_angles_sm[3]), R * np.sin(arc_angles_sm[3]), z_up], # 10,11

        
    ])
    
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, up_vertices))
    
    #%%
    """
    Downstream
    """
    # Define box vertices (bottom to top, front to back)
    down_vertices = np.array([
        [-x_sm, -y_sm, z_down],  # 0 Bottom Left Front
        [ x_sm, -y_sm, z_down],  # 1 Bottom Right Front
        [ x_sm,  y_sm, z_down],  # 2 Top Right Front
        [-x_sm,  y_sm, z_down],  # 3 Top Left Front
        
        
        [R * np.cos(angles_sm[0]), R * np.sin(angles_sm[0]), z_down], # 8 Circle Top Right Front 
        [R * np.cos(angles_sm[1]), R * np.sin(angles_sm[1]), z_down], # 9 Circle Top Left Left Front 
        [R * np.cos(angles_sm[2]), R * np.sin(angles_sm[2]), z_down], # 10 Circle Bottom Left Front 
        [R * np.cos(angles_sm[3]), R * np.sin(angles_sm[3]), z_down], # 11 Circle Bottom Right Front 
        
        
    ])
    
    
    down_arc_interpolations = np.array([
        [R * np.cos(arc_angles_sm[0]), R * np.sin(arc_angles_sm[0]), z_down], # interpolation point for sm_vertices 11, 8
        [R * np.cos(arc_angles_sm[1]), R * np.sin(arc_angles_sm[1]), z_down], # 8, 9
        [R * np.cos(arc_angles_sm[2]), R * np.sin(arc_angles_sm[2]), z_down], # 9, 10
        [R * np.cos(arc_angles_sm[3]), R * np.sin(arc_angles_sm[3]), z_down], # 10,11

        
    ])
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, down_vertices))
    
    #%%
    """
    Up and Downstream inner mesh
    """
    inner_vertices = np.array([

        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), z_sm], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), z_sm], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), z_sm], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), z_sm], #  
       
        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), z_up], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), z_up], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), z_up], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), z_up], #  
        
        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), -z_sm], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), -z_sm], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), -z_sm], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), -z_sm], #  
       
        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), z_down], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), z_down], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), z_down], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), z_down], #  
    ])
    
    
    inner_arc_interpolations = np.array([
        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), z_sm], # 0
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), z_sm], # 
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), z_sm], # 
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), z_sm], # 3

        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), z_up], # 4
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), z_up], # 
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), z_up], # 
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), z_up], # 7
        
        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), -z_sm], # 8
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), -z_sm], # 9
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), -z_sm], # 10
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), -z_sm], # 11

        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), z_down], # 12
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), z_down], # 13
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), z_down], # 14
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), z_down], # 270
        
    ])
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, inner_vertices))
    
    #%%
    """
    Up and Downstream additonal vertices for mergPatchPairs (differing densities between 3 regions)
    """
    interface_vertices = np.array([
        [-x_sm, -y_sm, z_sm],  # 0 Bottom Left Front
        [ x_sm, -y_sm, z_sm],  # 1 Bottom Right Front
        [ x_sm,  y_sm, z_sm],  # 2 Top Right Front
        [-x_sm,  y_sm, z_sm],  # 3 Top Left Front
        
        
        [R * np.cos(angles_sm[0]), R * np.sin(angles_sm[0]), z_sm], # 8 Circle Top Right Front 
        [R * np.cos(angles_sm[1]), R * np.sin(angles_sm[1]), z_sm], # 9 Circle Top Left Left Front 
        [R * np.cos(angles_sm[2]), R * np.sin(angles_sm[2]), z_sm], # 10 Circle Bottom Left Front 
        [R * np.cos(angles_sm[3]), R * np.sin(angles_sm[3]), z_sm], # 11 Circle Bottom Right Front 
        
        [-x_sm, -y_sm, -z_sm],  # 0 Bottom Left Front
        [ x_sm, -y_sm, -z_sm],  # 1 Bottom Right Front
        [ x_sm,  y_sm, -z_sm],  # 2 Top Right Front
        [-x_sm,  y_sm, -z_sm],  # 3 Top Left Front
        
        
        [R * np.cos(angles_sm[0]), R * np.sin(angles_sm[0]), -z_sm], # 8 Circle Top Right Front 
        [R * np.cos(angles_sm[1]), R * np.sin(angles_sm[1]), -z_sm], # 9 Circle Top Left Left Front 
        [R * np.cos(angles_sm[2]), R * np.sin(angles_sm[2]), -z_sm], # 10 Circle Bottom Left Front 
        [R * np.cos(angles_sm[3]), R * np.sin(angles_sm[3]), -z_sm], # 11 Circle Bottom Right Front 
        
    ])
    
    
    interface_arc_interpolations = np.array([
        [R * np.cos(arc_angles_sm[0]), R * np.sin(arc_angles_sm[0]), z_sm], # interpolation point for sm_vertices 11, 8
        [R * np.cos(arc_angles_sm[1]), R * np.sin(arc_angles_sm[1]), z_sm], # 8, 9
        [R * np.cos(arc_angles_sm[2]), R * np.sin(arc_angles_sm[2]), z_sm], # 9, 10
        [R * np.cos(arc_angles_sm[3]), R * np.sin(arc_angles_sm[3]), z_sm], # 10,11

        [R * np.cos(arc_angles_sm[0]), R * np.sin(arc_angles_sm[0]), -z_sm], # interpolation point for sm_vertices 11, 8
        [R * np.cos(arc_angles_sm[1]), R * np.sin(arc_angles_sm[1]), -z_sm], # 8, 9
        [R * np.cos(arc_angles_sm[2]), R * np.sin(arc_angles_sm[2]), -z_sm], # 9, 10
        [R * np.cos(arc_angles_sm[3]), R * np.sin(arc_angles_sm[3]), -z_sm], # 10,11
    ])
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, interface_vertices))
    
    #%%
    """
    Up and Downstream Central Cylinder (Polo mints)
    """
    
    centralcyl_vertices = np.array([

        # up 
        [R0/3 * np.cos(angles_sm[0]), R0/3 * np.sin(angles_sm[0]), z_sm+1], # square 
        [R0/3 * np.cos(angles_sm[1]), R0/3 * np.sin(angles_sm[1]), z_sm+1], #  
        [R0/3 * np.cos(angles_sm[2]), R0/3 * np.sin(angles_sm[2]), z_sm+1], #  
        [R0/3 * np.cos(angles_sm[3]), R0/3 * np.sin(angles_sm[3]), z_sm+1], #  
       
        [R0/3 * np.cos(angles_sm[0]), R0/3 * np.sin(angles_sm[0]), z_up], #  
        [R0/3 * np.cos(angles_sm[1]), R0/3 * np.sin(angles_sm[1]), z_up], #  
        [R0/3 * np.cos(angles_sm[2]), R0/3 * np.sin(angles_sm[2]), z_up], #  
        [R0/3 * np.cos(angles_sm[3]), R0/3 * np.sin(angles_sm[3]), z_up], #  
        
        
        
        # down
        [R0/3 * np.cos(angles_sm[0]), R0/3 * np.sin(angles_sm[0]), -z_sm], #  
        [R0/3 * np.cos(angles_sm[1]), R0/3 * np.sin(angles_sm[1]), -z_sm], #  
        [R0/3 * np.cos(angles_sm[2]), R0/3 * np.sin(angles_sm[2]), -z_sm], #  
        [R0/3 * np.cos(angles_sm[3]), R0/3 * np.sin(angles_sm[3]), -z_sm], #  
       
        [R0/3 * np.cos(angles_sm[0]), R0/3 * np.sin(angles_sm[0]), z_down], #  
        [R0/3 * np.cos(angles_sm[1]), R0/3 * np.sin(angles_sm[1]), z_down], #  
        [R0/3 * np.cos(angles_sm[2]), R0/3 * np.sin(angles_sm[2]), z_down], #  
        [R0/3 * np.cos(angles_sm[3]), R0/3 * np.sin(angles_sm[3]), z_down], #  
        
    ])
    
    polosquare_interface_arc_interpolations = np.array([
        [R0/3 * np.cos(arc_angles_sm[0]), R0/3 * np.sin(arc_angles_sm[0]), z_sm+1], # at turbine up side square 
        [R0/3 * np.cos(arc_angles_sm[1]), R0/3 * np.sin(arc_angles_sm[1]), z_sm+1], #  
        [R0/3 * np.cos(arc_angles_sm[2]), R0/3 * np.sin(arc_angles_sm[2]), z_sm+1], #  
        [R0/3 * np.cos(arc_angles_sm[3]), R0/3 * np.sin(arc_angles_sm[3]), z_sm+1], #
        
        [R0/3 * np.cos(arc_angles_sm[0]), R0/3 * np.sin(arc_angles_sm[0]), z_up], # upstream square 
        [R0/3 * np.cos(arc_angles_sm[1]), R0/3 * np.sin(arc_angles_sm[1]), z_up], #  
        [R0/3 * np.cos(arc_angles_sm[2]), R0/3 * np.sin(arc_angles_sm[2]), z_up], #  
        [R0/3 * np.cos(arc_angles_sm[3]), R0/3 * np.sin(arc_angles_sm[3]), z_up], #
        
    ])
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, centralcyl_vertices))
    
    #%%
    """
    Up and Downstream Central Cylinder additonal vertices for mergPatchPairs (need more vertives at R0)
    """
    
    cc_interface_vertices = np.array([

        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), z_sm], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), z_sm], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), z_sm], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), z_sm], #  
       
        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), z_up], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), z_up], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), z_up], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), z_up], #  
        
        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), -z_sm], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), -z_sm], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), -z_sm], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), -z_sm], #  
       
        [R0 * np.cos(angles_sm[0]), R0 * np.sin(angles_sm[0]), z_down], #  
        [R0 * np.cos(angles_sm[1]), R0 * np.sin(angles_sm[1]), z_down], #  
        [R0 * np.cos(angles_sm[2]), R0 * np.sin(angles_sm[2]), z_down], #  
        [R0 * np.cos(angles_sm[3]), R0 * np.sin(angles_sm[3]), z_down], #  
    ])
    
    
    cc_interface_arc_interpolations = np.array([
        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), z_sm], # 0
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), z_sm], # 
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), z_sm], # 
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), z_sm], # 3

        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), z_up], # 4
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), z_up], # 
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), z_up], # 
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), z_up], # 7
        
        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), -z_sm], # 8
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), -z_sm], # 9
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), -z_sm], # 10
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), -z_sm], # 11

        [R0 * np.cos(arc_angles_sm[0]), R0 * np.sin(arc_angles_sm[0]), z_down], # 12
        [R0 * np.cos(arc_angles_sm[1]), R0 * np.sin(arc_angles_sm[1]), z_down], # 13
        [R0 * np.cos(arc_angles_sm[2]), R0 * np.sin(arc_angles_sm[2]), z_down], # 14
        [R0 * np.cos(arc_angles_sm[3]), R0 * np.sin(arc_angles_sm[3]), z_down], # 270
        
    ])
    
    # Append to ordered_vertices
    ordered_vertices = np.vstack((ordered_vertices, cc_interface_vertices))
    #%%
    return ordered_vertices, sm_arc_interpolations, up_arc_interpolations, down_arc_interpolations, inner_arc_interpolations, interface_arc_interpolations, cc_interface_arc_interpolations, polosquare_interface_arc_interpolations
    
    
    
    
    