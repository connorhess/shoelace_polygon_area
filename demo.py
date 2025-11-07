#!/usr/bin/env python3
"""
Demo script showcasing the shoelace_polygon_area module functionality.

This script demonstrates various use cases of the polygon area calculator.
"""

from shoelace_polygon_area import calculate_polygon_area, validate_polygon
from shoelace_polygon_area.polygon_area import calculate_polygon_area_with_info


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def demo_basic_shapes():
    """Demonstrate area calculations for basic shapes."""
    print_section("BASIC SHAPES")
    
    # Square
    print("1. Square (side length 5):")
    square = [(0, 0), (5, 0), (5, 5), (0, 5)]
    area = calculate_polygon_area(square)
    print(f"   Vertices: {square}")
    print(f"   Area: {area} square units\n")
    
    # Rectangle
    print("2. Rectangle (4 × 3):")
    rectangle = [(0, 0), (4, 0), (4, 3), (0, 3)]
    area = calculate_polygon_area(rectangle)
    print(f"   Vertices: {rectangle}")
    print(f"   Area: {area} square units\n")
    
    # Triangle
    print("3. Right Triangle (base 6, height 4):")
    triangle = [(0, 0), (6, 0), (0, 4)]
    area = calculate_polygon_area(triangle)
    print(f"   Vertices: {triangle}")
    print(f"   Area: {area} square units\n")


def demo_complex_shapes():
    """Demonstrate area calculations for complex polygons."""
    print_section("COMPLEX POLYGONS")
    
    # Pentagon
    print("1. Irregular Pentagon:")
    pentagon = [(0, 0), (3, 0), (4, 2), (2, 4), (-1, 2)]
    area = calculate_polygon_area(pentagon)
    print(f"   Vertices: {pentagon}")
    print(f"   Area: {area} square units\n")
    
    # Hexagon
    print("2. Hexagon:")
    hexagon = [(2, 0), (1, 1.732), (-1, 1.732), (-2, 0), (-1, -1.732), (1, -1.732)]
    area = calculate_polygon_area(hexagon)
    print(f"   Vertices: {hexagon}")
    print(f"   Area: {area:.2f} square units\n")


def demo_additional_info():
    """Demonstrate the calculate_polygon_area_with_info function."""
    print_section("ADDITIONAL INFORMATION")
    
    print("Rectangle with extra information:")
    vertices = [(0, 0), (6, 0), (6, 4), (0, 4)]
    info = calculate_polygon_area_with_info(vertices)
    
    print(f"   Vertices: {vertices}")
    print(f"   Area: {info['area']} square units")
    print(f"   Perimeter: {info['perimeter']:.2f} units")
    print(f"   Number of vertices: {info['vertices_count']}")
    print(f"   Centroid (center): {info['centroid']}\n")


def demo_vertex_ordering():
    """Demonstrate that vertex ordering doesn't affect the result."""
    print_section("VERTEX ORDERING INDEPENDENCE")
    
    print("Same square with different vertex orderings:\n")
    
    # Clockwise from bottom-left
    cw = [(0, 0), (3, 0), (3, 3), (0, 3)]
    area_cw = calculate_polygon_area(cw)
    print(f"1. Clockwise: {cw}")
    print(f"   Area: {area_cw} square units\n")
    
    # Counter-clockwise from bottom-left
    ccw = [(0, 0), (0, 3), (3, 3), (3, 0)]
    area_ccw = calculate_polygon_area(ccw)
    print(f"2. Counter-clockwise: {ccw}")
    print(f"   Area: {area_ccw} square units\n")
    
    # Starting from different vertex
    diff = [(3, 0), (3, 3), (0, 3), (0, 0)]
    area_diff = calculate_polygon_area(diff)
    print(f"3. Different starting point: {diff}")
    print(f"   Area: {area_diff} square units\n")
    
    print(f"   ✓ All areas are equal: {area_cw == area_ccw == area_diff}\n")


def demo_error_handling():
    """Demonstrate input validation and error handling."""
    print_section("INPUT VALIDATION")
    
    print("1. Valid polygon (passes validation):")
    valid = [(0, 0), (1, 0), (0.5, 1)]
    try:
        validate_polygon(valid)
        print(f"   {valid} ✓ Valid\n")
    except Exception as e:
        print(f"   Error: {e}\n")
    
    print("2. Too few vertices (should fail):")
    invalid = [(0, 0), (1, 1)]
    try:
        calculate_polygon_area(invalid)
        print(f"   {invalid} ✗ Should have failed!\n")
    except ValueError as e:
        print(f"   {invalid} ✓ Correctly rejected")
        print(f"   Error: {e}\n")
    
    print("3. Non-numeric coordinates (should fail):")
    invalid = [(0, 0), ("x", "y"), (1, 1)]
    try:
        calculate_polygon_area(invalid)
        print(f"   {invalid} ✗ Should have failed!\n")
    except TypeError as e:
        print(f"   {invalid} ✓ Correctly rejected")
        print(f"   Error: {e}\n")


def demo_real_world_example():
    """Demonstrate a real-world use case."""
    print_section("REAL-WORLD EXAMPLE: Plot of Land")
    
    print("Calculate the area of a plot of land with GPS coordinates:\n")
    
    # Simplified plot coordinates (in meters)
    plot = [
        (0, 0),      # Corner 1
        (50, 5),     # Corner 2
        (48, 40),    # Corner 3
        (10, 45),    # Corner 4
        (-5, 15)     # Corner 5
    ]
    
    info = calculate_polygon_area_with_info(plot)
    
    print(f"   Plot corners (in meters from reference point):")
    for i, corner in enumerate(plot, 1):
        print(f"   Corner {i}: {corner}")
    
    print(f"\n   Plot area: {info['area']:.2f} square meters")
    print(f"   Plot perimeter: {info['perimeter']:.2f} meters")
    print(f"   Plot center: {info['centroid']}\n")
    
    # Convert to other units
    area_hectares = info['area'] / 10000
    area_acres = info['area'] * 0.000247105
    
    print(f"   In other units:")
    print(f"   - {area_hectares:.4f} hectares")
    print(f"   - {area_acres:.4f} acres\n")


def main():
    """Run all demonstrations."""
    print("\n" + "="*70)
    print("  SHOELACE POLYGON AREA CALCULATOR - DEMONSTRATION")
    print("="*70)
    
    demo_basic_shapes()
    demo_complex_shapes()
    demo_additional_info()
    demo_vertex_ordering()
    demo_error_handling()
    demo_real_world_example()
    
    print("="*70)
    print("  Demo completed successfully!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
