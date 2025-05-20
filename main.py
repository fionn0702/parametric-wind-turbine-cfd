import numpy as np

"""
==================================================================
Parametric HAWT Mesh Generator – main.py
==================================================================

Author   : Fionn McEvoy <mcevoyfionn@gmail.com> <fionn.mcevoy@ucdconnect.ie>
Created  : 31-03-2025
Version  : 0.12.0 

This is the main executable for generating a structured, three-bladed wind turbine mesh.

Place this script (main.py) along with all required modules in the /system/python/ directory.
The script writes to blockMeshDict in /system/, which is then used by OpenFOAM's 'blockMesh' utility
to build the mesh.

Purpose:
Generate a fully-structured **blockMeshDict** for a three-bladed
horizontal-axis wind-turbine (HAWT) in OpenFOAM.  The script
supports rigid-body rotation (AMI) and an expanded upstream /
downstream bounding box.

Workflow:
1. Generate and rotate airfoil blades (Kármán–Trefftz and other options 
   -> can be upgrdaed to simply accept NACA airfoil coordinates)
2. Add circular and bounding box mesh layers
3. Compile all vertices, define splines and arcs
4. Build outer mesh (incl. upstream/downstream)
5. Write blockMeshDict with all geometry and patch data

All inputs to the script are specified below, and of course one can still easily adjust 
parameters in any of the supporting modules. Only works with 3 blades, but can be built upon
to parameterise this.
"""


#%%
"""
SCRIPT INPUTS
"""
import generate_blade
import rotate_blade
import generate_circularmesh
import rotate_circularmesh
import generate_boundingbox_mesh
import rotate_boundingbox_mesh
import compile_allvertices
import generate_arc_points
import rotate_arc_points
import surrounding_mesh
import write_vertices
import write_blocks
import write_arcs
import write_splines
import write_patches

"""
Parameters for Kármán-Trefftz Transformation and Blade Generation
"""

# Constants
points = 129 #386 # multiple of 8 then + 1                                  # Number of points per section (airfoil resolution)
trailing_edge_angle_deg = 5                  # Trailing edge angle in degrees
b = 0.85                                     # Transformation constant, adjust for airfoil thickness

# Circle centre coords to generate N centre coords 
centre_x_start = 0.1                        # First circle centre in x
centre_x_end = 0.1 #-0.01                         # Final circle centre in x
centre_z_start = 0.15 # 0.05                        # First circle centre in z
centre_z_end = 0.15 # 0.12                          # Final circle centre in z

radius_scale_factor = 1.0                    # Easy size scaling
# Circle radii to linear interpolate between
radius_root = 2*radius_scale_factor                            # Circle at blade root radius
radius_airfoil_start = 1.3*radius_scale_factor
radius_thick = 1.3*radius_scale_factor                         # Circle at blade thickest point radius 
radius_tip = 1.3                          # Circle at blade tip radius 

# Parameters for blade size
N =  40                                      # Number of airfoil sections in each blade (blade resolution)
height = 45                                # LENGTH of blade 1
num_blades = 3                               # Number of blades
base_height = 4                              # Blade beginning height above origin (hub radius -> make bigger if more bladdes to overcome mesh clash)

# Blade root design
num_root_sections = int(0.07 * N)                    # Number of sections at the root where no transformation is applied 

# Parameters for blade shape. These values, in conjunction with the centre values, dictate the blade shape 
max_thickness_fraction = 0.2                 # Fraction of blade length at which maximum thickness occurs
blade_rotate_deg = 0                        # Rotation angle in degrees (twist blade on its axis)

# Z-direction taper (thickness)
taper_z_start = 2.0   # Multiplier at start of transition
taper_z_end   = 0.2   # Multiplier at tip
taper_z_rate  = 10.0   # How fast the exponential decays

# X-direction taper (width/stretch)
taper_x_start = 1.4
taper_x_end   = 0.1
taper_x_rate  = 2.0

"""
Parameters for Surrounding Cicrular (Ellipse) Mesh
"""
# Scaling factor for the x-direction (stretch factor)
x_stretch = 1 # Adjust this factor to control the degree of stretching (circle -> ellipse)
z_stretch = 1
"""
Parameters for Bounding Box
"""
width = 4.5  # +ve x coord for bounding box ie width of 16

"""
Rotation Matricies
"""
# Rotation angles for different configurations
angles_2_blades = np.radians([180])              # Angle for 2 blades
angles_3_blades = np.radians([120, 240])         # Angles for 3 blades
angles_4_blades = np.radians([90, 180, 270])     # Angles for 4 blades

# Generate rotation matrices
rotation_matrices_2 = [
    np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    for angle in angles_2_blades
]

rotation_matrices_3 = [
    np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    for angle in angles_3_blades
]

rotation_matrices_4 = [
    np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    for angle in angles_4_blades
]

"""
Mesh density
"""

# Inner Blade Mesh Density
ibm_res_x = 25
ibm_res_y = 35
ibm_res_z = 1

# Centre Sides Mesh Density
csm_res_x = ibm_res_x
csm_res_y = int(ibm_res_y/10)
csm_res_z = ibm_res_z

# Centre Front and Back Mesh Density
cfbm_res_x = int(ibm_res_y/10)
cfbm_res_y = ibm_res_x
cfbm_res_z = ibm_res_z

# Corner Mesh Density
cm_res_x = cfbm_res_x
cm_res_y = csm_res_y
cm_res_z = ibm_res_z

# Gap Front and Back Mesh Density
gfbm_res_x = cm_res_x
gfbm_res_y = 20
gfbm_res_z = ibm_res_z

# Gap Middle Mesh Density
gmm_res_x = csm_res_x
gmm_res_y = gfbm_res_y
gmm_res_z = ibm_res_z

# Surrounding Mesh Density (around disc)
# Define separate resolution for each axis (This is relative to how block is defined)
sm_res_x = ibm_res_x*1 #40 
sm_res_y = ibm_res_y*1 #25
sm_res_z = 50       

# Upstream Mesh Density
up_res_x = 1*sm_res_x
up_res_y = 1*sm_res_y
up_res_z = sm_res_z*1

# Downstream Mesh Density
down_res_x = 1*sm_res_x
down_res_y = 1*sm_res_y
down_res_z = 1*sm_res_z*6 

"""
Mesh Grading
"""
# Inner Blade Mesh Grading
ibm_grading = 0.005                   # Increase density toward origin (local +ve y-dir)

# Centre Sides Mesh Grading
csm_grading = 0.5                   # Increase density toward origin (local +ve y-dir)
csm_grading_inv = 1/csm_grading                   # Increase density toward origin (local +ve y-dir)

# Centre Front and Back Grading
cfbm_grading = 2                     # Increase density toward origin (local -ve x-dir)

# Corner Mesh Grading
cm_grading_x = cfbm_grading          # Increase density toward origin (local -ve x-dir)
cm_grading_y = csm_grading          # Increase density toward origin (local +ve y-dir)
cm_grading_y_inv = 1/cm_grading_y         # Increase density toward origin (local -ve y-dir)

# Gap Overall Multigrading to increase density toward blades
gm_multigrading = 2                         
gm_multigrading_inv = 1/gm_multigrading

# Gap Front and Back Mesh Grading
gfbm_grading_x = cm_grading_x           # Increase density toward origin (local -ve x-dir)
gfbm_grading_x_inv = 1/gfbm_grading_x     # Increase density toward origin (local +ve x-dir)

# Gap Middle Mesh Grading
gmm_grading = 1                         # No grading (same as csm in local x)

# Surrounding Mesh Grading
sm_grading = 32 #4                      # Increase density toward origin (local -ve dir)
sm_grading_inv = 1 / sm_grading     # Increase density toward origin (local +ve dir)

# Upstream Mesh Grading
up_grading = 10 

# Downstream Mesh Gradinbg
down_grading = 0.1
down_grading_rad = 10
down_grading_rad_inv = 1/down_grading_rad

# Define a flag to control whether to write the upstream and downstream meshes
write_up_down = True  

# Define a flag to control whether to write the central mesh
write_central = True

#%%
"""
SECTION 1
Generate airfoil sections using Kármán-Trefftz Transformation (circle -> airfoil)
and Generate Blade shape.
"""

vertices, y_coords, centre_x, centre_z, R, radii = generate_blade.generate_blade(points, height, N, base_height, trailing_edge_angle_deg, num_root_sections, 
                         radius_root, centre_x_end, centre_z_end, max_thickness_fraction, radius_airfoil_start, radius_thick, 
                         radius_tip, centre_x_start, centre_z_start, x_stretch, b, width, blade_rotate_deg, taper_z_start, taper_z_end, taper_z_rate, taper_x_start, taper_x_end, taper_x_rate)

#%%
"""
SECTION 2
Generate other turbine blades (airfoil vertices) by applying a rotation. (3 blades = 120 degrees)
"""

vertices_blade1, vertices_blade2, vertices_blade3 = rotate_blade.rotate_blade(vertices, num_blades, N, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4)


#%%
"""
SECTION 3
Generate vertices for circular mesh surrounding each arifoil
Uses centre of first aifoil section (root) to create a circle with an optional stretch factor for ellipse
"""

circle_vertices_array = generate_circularmesh.generate_circularmesh(vertices, N, x_stretch, width, y_coords, z_stretch, blade_rotate_deg)

#%%
""" 
SECTION 4
Apply rotations to generate vertices for circular mesh surrounding each airfoil in each blade
"""
circle_vertices_array_blade1, circle_vertices_array_blade2, circle_vertices_array_blade3 = rotate_circularmesh.rotate_circularmesh(circle_vertices_array, num_blades, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4)

#%%
"""
SECTION 5
Generate vertices for bounding box based on circle (elliptical) mesh 
"""

box_coords= generate_boundingbox_mesh.generate_boundingbox_mesh(N, width, y_coords, circle_vertices_array_blade1)

#%%
""" 
SECTION 6
Apply rotations to generate vertices for bounding box airfoil in each blade
Only 3 blades
"""

box_coords_blade1, box_coords_blade2, box_coords_blade3 = rotate_boundingbox_mesh.rotate_boundingbox_mesh(box_coords, num_blades, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4)

#%% 
""" 
SECTION 7
Compile and sort blade airfoil and mesh vertices. Puts all vertices into list
"""

ordered_vertices, x_coords, vertex0_idx, vertex1_idx, vertex2_idx, vertex3_idx, vertex4_idx, vertex5_idx, vertex6_idx, vertex7_idx, vertex8_idx, vertex9_idx, vertex10_idx, vertex11_idx, vertex12_idx, vertex13_idx, vertex14_idx, vertex15_idx  = compile_allvertices.compile_allvertices(num_blades, N, vertices, points, vertices_blade1, vertices_blade2, vertices_blade3, circle_vertices_array_blade1, circle_vertices_array_blade2, circle_vertices_array_blade3, box_coords_blade1, box_coords_blade2, box_coords_blade3)
#%%
"""
Section 8
Generate arc points to make blade curve in x-y plane
"""

arc_array = generate_arc_points.generate_arc_points(N, ordered_vertices, width, y_coords)

#%%
"""
SECTION 9
Rotate arc points for 3 blades
"""
arc_points_blade1, arc_points_blade2, arc_points_blade3 = rotate_arc_points.rotate_arc_points(arc_array, num_blades, N, rotation_matrices_2, rotation_matrices_3, rotation_matrices_4)


#%%
""" 
SECTION 10
Generate vertices of mesh surrounding turbine disc mesh (for fixedAMI) as well
as up and downstream meshes to create box domain
"""
ordered_vertices, sm_arc_interpolations, up_arc_interpolations, down_arc_interpolations, inner_arc_interpolations, interface_arc_interpolations, cc_interface_arc_interpolations, polosquare_interface_arc_interpolations = surrounding_mesh.surrounding_mesh(height, width, R, y_coords, ordered_vertices)

#%%
"""
Section 11
Write blockMeshDict
"""

# Write blockMeshDict        
with open("../blockMeshDict", "w") as f:
    f.write("FoamFile\n{\n")
    f.write("    version     2.0;\n")
    f.write("    format      ascii;\n") 
    f.write("    class       dictionary;\n")
    f.write("    location    \"system\";\n")
    f.write("    object      blockMeshDict;\n")
    f.write("}\n\n")
    
    disc_vertices_offset = N * 56 * num_blades # sm vertex numbering starts after blades
    blade_offset = N * 56  # Offset to jump from one blade to the next

    # arc data
    circle_vertices_arrays = [circle_vertices_array_blade1, circle_vertices_array_blade2, circle_vertices_array_blade3]  # Blade arcs. Store all blade circle vertices in a list for easy indexing
    arc_array_dict = [arc_points_blade1, arc_points_blade2, arc_points_blade3]                                           # Curvature arcs

    # Section11V: Write vertices to blockMeshDict
    write_vertices.write_vertices(f, ordered_vertices)
    
    # Section11B: Call functions to write blocks
    write_blocks.write_blocks(f, blade_offset, num_blades, N, ordered_vertices, disc_vertices_offset, ibm_res_x, ibm_res_y, ibm_res_z, ibm_grading, 
                                       csm_res_x, csm_res_y, csm_res_z, csm_grading, csm_grading_inv, cfbm_res_x, cfbm_res_y, cfbm_res_z, cfbm_grading, 
                                       cm_res_x, cm_res_y, cm_res_z, cm_grading_x, cm_grading_y, cm_grading_y_inv, gfbm_res_x, gfbm_res_y, gfbm_res_z, gfbm_grading_x, gfbm_grading_x_inv, 
                                       gmm_res_x, gmm_res_y, gmm_res_z, gmm_grading, sm_grading, sm_grading_inv, sm_res_x, sm_res_y, sm_res_z, gm_multigrading, gm_multigrading_inv,
                                       up_res_x, up_res_y, up_res_z, up_grading, down_res_x, down_res_y, down_res_z, down_grading, write_up_down, write_central, down_grading_rad, down_grading_rad_inv)
    
    
    # Section11A: Call functions to write arcs
    write_arcs.write_arcs(f, num_blades, num_root_sections, N, arc_array_dict, circle_vertices_arrays, ordered_vertices, y_coords, width, disc_vertices_offset, sm_arc_interpolations, up_arc_interpolations, down_arc_interpolations, inner_arc_interpolations, interface_arc_interpolations, cc_interface_arc_interpolations, polosquare_interface_arc_interpolations, write_up_down, write_central)
    
    # Section11S: Call function to write splines
    write_splines.write_splines(f, N, num_blades, blade_offset, vertices_blade1, vertices_blade2, vertices_blade3, points, vertex0_idx, vertex1_idx, vertex2_idx, vertex3_idx, vertex4_idx, vertex5_idx, vertex6_idx, vertex7_idx, vertex8_idx, vertex9_idx, vertex10_idx, vertex11_idx, vertex12_idx, vertex13_idx, vertex14_idx, vertex15_idx, write_central )
    
    # Section11P: Call funcion to write patches
    write_patches.write_patches(f, num_blades, N, disc_vertices_offset, write_up_down, write_central)
   
    # merpatchpairs to join upstream to central and downstream to central
    if write_up_down and write_central:
        f.write("mergePatchPairs\n")
        f.write("(\n")
        f.write("    (interfaceDiscUp interfaceUp) \n")
        f.write("    (interfaceDown interfaceDiscDown) \n")
        f.write("    (interfacePoloCylUp interfacePoloSideUp) \n")
        f.write("    (interfacePoloCylDown interfacePoloSideDown) \n")

        f.write(");\n")
    
    f.write("// End of blockMeshDict\n")
    
#%%
"""
Section 12
Optional export vertices to vtk for easy identification
"""
 
# def export_vertices_to_vtk(vertices, filename="vertices.vtk"):
#     with open(filename, "w") as f:
#         f.write("# vtk DataFile Version 3.0\n")
#         f.write("Airfoil Vertices\n")
#         f.write("ASCII\n")
#         f.write("DATASET POLYDATA\n")
#         f.write(f"POINTS {len(vertices)} float\n")
#         for v in vertices:
#             f.write(f"{v[0]} {v[1]} {v[2]}\n")
#         f.write(f"VERTICES {len(vertices)} {len(vertices) * 2}\n")
#         for i in range(len(vertices)):
#             f.write(f"1 {i}\n")

# export_vertices_to_vtk(ordered_vertices)

        
        
    


