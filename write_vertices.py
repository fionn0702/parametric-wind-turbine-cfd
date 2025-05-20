"""
Section 11V
Write vertices to blockmeshDict
"""

def write_vertices(f, ordered_vertices):
    
    # Write all ordered vertices
    f.write("vertices\n(\n")
    for vertex_count, vertex in enumerate(ordered_vertices):
        f.write(f"    ({vertex[0]} {vertex[1]} {vertex[2]}) // Vertex {vertex_count}\n")
    f.write(");\n\n")