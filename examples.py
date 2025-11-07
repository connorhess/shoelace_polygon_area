#!/usr/bin/env python3
"""
Simple usage examples for the shoelace_polygon_area module.

Quick start examples to get you up and running.
"""

from shoelace_polygon_area import calculate_polygon_area

# Example 1: Calculate the area of a triangle
print("Example 1: Triangle")
triangle = [(0, 0), (4, 0), (2, 3)]
area = calculate_polygon_area(triangle)
print(f"Triangle vertices: {triangle}")
print(f"Area: {area} square units\n")

# Example 2: Calculate the area of a square
print("Example 2: Square")
square = [(0, 0), (5, 0), (5, 5), (0, 5)]
area = calculate_polygon_area(square)
print(f"Square vertices: {square}")
print(f"Area: {area} square units\n")

# Example 3: Calculate the area of an irregular polygon
print("Example 3: Irregular Pentagon")
pentagon = [(0, 0), (2, 0), (3, 1), (1, 3), (-1, 1)]
area = calculate_polygon_area(pentagon)
print(f"Pentagon vertices: {pentagon}")
print(f"Area: {area} square units\n")

# Example 4: Using floating-point coordinates
print("Example 4: Polygon with Float Coordinates")
float_polygon = [(0.5, 0.5), (3.5, 0.5), (3.5, 2.5), (0.5, 2.5)]
area = calculate_polygon_area(float_polygon)
print(f"Polygon vertices: {float_polygon}")
print(f"Area: {area} square units\n")

# Example 5: Get additional information
print("Example 5: Additional Information")
from shoelace_polygon_area.polygon_area import calculate_polygon_area_with_info

rectangle = [(0, 0), (6, 0), (6, 4), (0, 4)]
info = calculate_polygon_area_with_info(rectangle)
print(f"Rectangle vertices: {rectangle}")
print(f"Area: {info['area']} square units")
print(f"Perimeter: {info['perimeter']} units")
print(f"Centroid: {info['centroid']}")
