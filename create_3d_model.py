from solid import *
from solid.utils import *

def create_model():
    # Create a base cylinder
    base = cylinder(r=30, h=10)
    
    # Create a sphere on top
    top_sphere = translate([0, 0, 10])(sphere(r=20))
    
    # Combine the shapes
    model = base + top_sphere
    
    return model

if __name__ == "__main__":
    model = create_model()
    
    # Save as OpenSCAD file
    scad_render_to_file(model, "output.scad")
    
    print("OpenSCAD file generated. Use OpenSCAD to export to STL for 3D printing.")