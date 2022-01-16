Minimal example testing vertex indexing
========================================

When opening .blend file in blender and inspecting the vertex indices, verts 0,2,4 and 6 form the top side (+Z).
The vertex shader assignes the colors red, green, blue and teal to these indices, respectively.a
Problem: The red, green and blue verts show up as expected, but a vertex on the bottom face is colored in teal, so index 6 lies somewhere other than expected.
