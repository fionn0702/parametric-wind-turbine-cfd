Parametric Wind Turbine Mesh Generator for OpenFOAM v2412
----------------------------------------------------------

This project is a modular Python-based tool for generating a structured CFD mesh of a horizontal-axis 
wind turbine (HAWT) using OpenFOAM v2412. The mesh is constructed with blockMesh and includes rotating 
mesh capability using cyclicAMI. Airfoil shapes are defined using the Kármán–Trefftz transformation, 
and all geometry and meshing steps are parameterised through a single main script.

Developed by Fionn McEvoy as part of a Master's thesis at University College Dublin.

A simple LAMINAR example case is included in this repository (HAWT_example_case).
This repo contains all the individual dictionary files and Python scripts used to generate a working OpenFOAM simulation. Users will need to manually recreate the standard OpenFOAM folder structure (0/, system/, constant/) and place the Python scripts inside system/Python/. Once set up, run main.py to generate the blockMeshDict, then run blockMesh followed by pimpleFoam to execute the simulation.

Key Features:
- Parametric 3-blade wind turbine mesh
- Airfoil sections generated using the Kármán–Trefftz transform
- Structured mesh generated entirely through blockMesh
- AMI interface used for rotating central region
- Upstream and downstream domains included
- Python modular structure allows for easy geometry and resolution changes
- main.py contains all mesh input parameters, edit this to create different blades 
- generate_blade.py should also be reviewed for more control

Limitations:
- The mesh generator models only the blades and an oversized hub (no tower or nacelle)
- Only three blades are supported in this version

Folder Setup:
Place all Python files inside:
  yourCase/system/python/

Make sure this folder includes:
	main.py
	generate_blade
	rotate_blade
	generate_circularmesh
	rotate_circularmesh
	generate_boundingbox_mesh
	rotate_boundingbox_mesh
	compile_allvertices
	generate_arc_points
	rotate_arc_points
	surrounding_mesh
	write_vertices
	write_blocks
	write_arcs
	write_splines
	write_patches

Also include example OpenFOAM dictionaries:
    system/dynamicMeshDict    # Required for cyclicAMI rotation: Here you specify rotation speed, axis etc.
    system/controlDict        # Set start/stop time, write interval, solver, etc.
    system/fvSchemes
    system/fvSolution
    0/U                       # Initial velocity field (e.g., inlet, outlet, rotating patches)
    0/p                       # Initial pressure field
    constant/transportProperties
    constant/polyMesh/        # Will be generated after running blockMesh

How to Use:
1. Run main.py using Python 3.x (NumPy required). This will write blockMeshDict to system/.
2. From the case root, run:
       blockMesh
3. To simulate, use:
       pimpleFoam


Dependencies:
- Python 3.x
- NumPy
- OpenFOAM v2412 (from openfoam.com)

Contact:
Fionn McEvoy
Email: fionn.mcevoy@ucdconnect.ie or mcevoyfionn@gmail.com

Institution:
University College Dublin
Project: Development of a Parametric Wind Turbine CFD Model (2025)
