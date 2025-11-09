#!/usr/bin/env python3
"""
GPS Coordinate Examples for the shoelace_polygon_area module.

This script demonstrates how to use the GPS coordinate parsing
functionality to calculate polygon areas from GPS coordinate strings.
"""

from shoelace_polygon_area import (
    parse_gps_coordinates,
    calculate_polygon_area_from_gps,
    calculate_polygon_area
)


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def example_basic_gps():
    """Basic example with GPS coordinates in lat long alt accuracy format."""
    print_section("EXAMPLE 1: Basic GPS Coordinates")
    
    # GPS coordinates in the format: lat long alt accuracy
    gps_string = "1.323123 2.21312 0.0 0.0; 1.5 2.5 0.0 0.0; 2.0 3.0 0.0 0.0"
    
    print(f"GPS String:\n{gps_string}\n")
    
    # Parse the GPS coordinates
    coords = parse_gps_coordinates(gps_string)
    print(f"Parsed coordinates (longitude, latitude):")
    for i, coord in enumerate(coords, 1):
        print(f"  Point {i}: {coord}")
    
    # Calculate the area
    area = calculate_polygon_area_from_gps(gps_string)
    print(f"\nPolygon area: {area:.6f} square degrees")


def example_simplified_format():
    """Example with simplified lat/long format (no altitude/accuracy)."""
    print_section("EXAMPLE 2: Simplified Format (lat long only)")
    
    # GPS coordinates with only lat and long
    gps_string = "0.0 0.0; 0.0 4.0; 3.0 0.0"
    
    print(f"GPS String:\n{gps_string}\n")
    
    # Parse with lat_long format
    coords = parse_gps_coordinates(gps_string, coordinate_format="lat_long")
    print(f"Parsed coordinates (longitude, latitude):")
    for i, coord in enumerate(coords, 1):
        print(f"  Point {i}: {coord}")
    
    # Calculate the area
    area = calculate_polygon_area_from_gps(gps_string, coordinate_format="lat_long")
    print(f"\nPolygon area: {area:.6f} square degrees")


def example_real_world():
    """Example with realistic GPS coordinates of a plot of land."""
    print_section("EXAMPLE 3: Real-World Plot of Land")
    
    # Example: A small plot in New York (coordinates are simplified for demonstration)
    # Format: lat long alt accuracy
    gps_string = (
        "40.7128 -74.0060 10.5 0.5; "
        "40.7138 -74.0060 10.2 0.5; "
        "40.7138 -74.0050 10.8 0.5; "
        "40.7128 -74.0050 11.0 0.5"
    )
    
    print("GPS String (plot corners):")
    print(gps_string)
    print()
    
    # Parse coordinates
    coords = parse_gps_coordinates(gps_string)
    print("Parsed coordinates (longitude, latitude):")
    for i, coord in enumerate(coords, 1):
        print(f"  Corner {i}: longitude={coord[0]:.4f}°, latitude={coord[1]:.4f}°")
    
    # Calculate area in square degrees
    area_sq_degrees = calculate_polygon_area_from_gps(gps_string)
    print(f"\nArea: {area_sq_degrees:.10f} square degrees")
    
    # Convert to more practical units
    # Note: This is a rough approximation. For accurate conversions,
    # use proper geodetic calculations considering Earth's curvature
    
    # At latitude ~40°, 1 degree longitude ≈ 85.4 km
    # At latitude ~40°, 1 degree latitude ≈ 111.0 km
    km_per_deg_long = 85.4
    km_per_deg_lat = 111.0
    
    # Rough approximation (this assumes a rectangular plot)
    width_km = 0.001 * km_per_deg_long  # 0.001 degrees longitude
    height_km = 0.001 * km_per_deg_lat  # 0.001 degrees latitude
    area_sq_km = width_km * height_km
    area_sq_meters = area_sq_km * 1_000_000
    
    print(f"\nApproximate ground area:")
    print(f"  {area_sq_km:.6f} square kilometers")
    print(f"  {area_sq_meters:.2f} square meters")
    print(f"  {area_sq_meters * 10.764:.2f} square feet")
    
    print("\n⚠ Note: For accurate area calculations of GPS coordinates,")
    print("  consider using a proper coordinate projection system that")
    print("  accounts for Earth's curvature.")


def example_step_by_step():
    """Example showing step-by-step process."""
    print_section("EXAMPLE 4: Step-by-Step Process")
    
    gps_string = "1.0 2.0 0.0 0.0; 1.0 3.0 0.0 0.0; 2.0 3.0 0.0 0.0; 2.0 2.0 0.0 0.0"
    
    print("Step 1: Start with GPS coordinate string")
    print(f"  {gps_string}\n")
    
    print("Step 2: Parse GPS coordinates")
    coords = parse_gps_coordinates(gps_string)
    print(f"  Parsed to {len(coords)} vertices: {coords}\n")
    
    print("Step 3: Calculate polygon area")
    area = calculate_polygon_area(coords)
    print(f"  Area = {area} square degrees\n")
    
    print("Alternative: Use convenience function")
    area_direct = calculate_polygon_area_from_gps(gps_string)
    print(f"  calculate_polygon_area_from_gps() = {area_direct} square degrees\n")
    
    print(f"Both methods give the same result: {area == area_direct}")


def example_different_formats():
    """Example showing different coordinate formats."""
    print_section("EXAMPLE 5: Different Coordinate Formats")
    
    # Same polygon in different formats
    square_coords = [(0, 0), (0, 2), (2, 2), (2, 0)]
    
    print("Format 1: lat long alt accuracy")
    gps1 = "0.0 0.0 0.0 0.0; 0.0 2.0 0.0 0.0; 2.0 2.0 0.0 0.0; 2.0 0.0 0.0 0.0"
    area1 = calculate_polygon_area_from_gps(gps1)
    print(f"  GPS: {gps1}")
    print(f"  Area: {area1} square degrees\n")
    
    print("Format 2: lat long")
    gps2 = "0.0 0.0; 0.0 2.0; 2.0 2.0; 2.0 0.0"
    area2 = calculate_polygon_area_from_gps(gps2, coordinate_format="lat_long")
    print(f"  GPS: {gps2}")
    print(f"  Area: {area2} square degrees\n")
    
    print("Format 3: long lat (reversed)")
    gps3 = "0.0 0.0; 2.0 0.0; 2.0 2.0; 0.0 2.0"
    area3 = calculate_polygon_area_from_gps(gps3, coordinate_format="long_lat")
    print(f"  GPS: {gps3}")
    print(f"  Area: {area3} square degrees\n")
    
    print(f"All formats produce the same area: {area1 == area2 == area3}")


def main():
    """Run all examples."""
    print("\n" + "="*70)
    print("  GPS COORDINATE EXAMPLES - Shoelace Polygon Area Calculator")
    print("="*70)
    
    example_basic_gps()
    example_simplified_format()
    example_step_by_step()
    example_different_formats()
    example_real_world()
    
    print("\n" + "="*70)
    print("  Examples completed successfully!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
