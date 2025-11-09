"""
Comprehensive test suite for the shoelace_polygon_area module.

This module contains tests for:
1. Basic polygon area calculations (triangles, squares, rectangles)
2. Complex polygon shapes (pentagons, hexagons, irregular polygons)
3. Input validation and error handling
4. Edge cases (collinear points, very small/large coordinates)
5. Additional functionality (area with info function)
"""

import pytest
from shoelace_polygon_area import (
    calculate_polygon_area,
    validate_polygon,
    parse_gps_coordinates,
    calculate_polygon_area_from_gps
)
from shoelace_polygon_area.polygon_area import calculate_polygon_area_with_info


class TestBasicShapes:
    """Test area calculations for basic geometric shapes."""
    
    def test_unit_square(self):
        """Test area calculation for a unit square (1x1)."""
        # A square with vertices at (0,0), (1,0), (1,1), (0,1)
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        area = calculate_polygon_area(vertices)
        assert area == 1.0, f"Expected area 1.0, got {area}"
    
    def test_rectangle(self):
        """Test area calculation for a rectangle."""
        # Rectangle with width 4 and height 3
        vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
        area = calculate_polygon_area(vertices)
        assert area == 12.0, f"Expected area 12.0, got {area}"
    
    def test_right_triangle(self):
        """Test area calculation for a right triangle."""
        # Right triangle with base 4 and height 3
        # Area should be (1/2) * base * height = (1/2) * 4 * 3 = 6
        vertices = [(0, 0), (4, 0), (0, 3)]
        area = calculate_polygon_area(vertices)
        assert area == 6.0, f"Expected area 6.0, got {area}"
    
    def test_equilateral_triangle(self):
        """Test area calculation for an equilateral triangle."""
        # Equilateral triangle with side length 2
        # Vertices calculated to form an equilateral triangle
        vertices = [(0, 0), (2, 0), (1, 1.732050808)]
        area = calculate_polygon_area(vertices)
        # Area of equilateral triangle = (sqrt(3)/4) * side² ≈ 1.732
        assert abs(area - 1.732050808) < 0.001, f"Expected area ~1.732, got {area}"
    
    def test_square_large(self):
        """Test area calculation for a larger square."""
        # Square with side length 10
        vertices = [(0, 0), (10, 0), (10, 10), (0, 10)]
        area = calculate_polygon_area(vertices)
        assert area == 100.0, f"Expected area 100.0, got {area}"


class TestComplexShapes:
    """Test area calculations for more complex polygons."""
    
    def test_pentagon(self):
        """Test area calculation for an irregular pentagon."""
        vertices = [(0, 0), (2, 0), (3, 1), (1, 3), (-1, 1)]
        area = calculate_polygon_area(vertices)
        assert area == 7.0, f"Expected area 7.0, got {area}"
    
    def test_hexagon_regular(self):
        """Test area calculation for a regular hexagon."""
        # Regular hexagon with vertices calculated using trigonometry
        # Approximating a hexagon with radius 2 centered at origin
        vertices = [
            (2, 0),
            (1, 1.732),
            (-1, 1.732),
            (-2, 0),
            (-1, -1.732),
            (1, -1.732)
        ]
        area = calculate_polygon_area(vertices)
        # Expected area for regular hexagon with radius 2: 3*sqrt(3)*r² ≈ 10.39
        assert abs(area - 10.39) < 0.1, f"Expected area ~10.39, got {area}"
    
    def test_concave_polygon(self):
        """Test area calculation for a concave polygon (star-like shape)."""
        # A concave quadrilateral
        vertices = [(0, 0), (2, 0), (2, 2), (1, 1)]
        area = calculate_polygon_area(vertices)
        assert area == 2.0, f"Expected area 2.0, got {area}"
    
    def test_irregular_quadrilateral(self):
        """Test area calculation for an irregular quadrilateral."""
        vertices = [(0, 0), (3, 1), (4, 4), (1, 3)]
        area = calculate_polygon_area(vertices)
        assert area == 8.0, f"Expected area 8.0, got {area}"


class TestVertexOrdering:
    """Test that the formula works regardless of vertex ordering."""
    
    def test_clockwise_vertices(self):
        """Test with clockwise ordered vertices."""
        vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
        area = calculate_polygon_area(vertices)
        assert area == 12.0
    
    def test_counterclockwise_vertices(self):
        """Test with counter-clockwise ordered vertices."""
        # Same rectangle but vertices in reverse order
        vertices = [(0, 3), (4, 3), (4, 0), (0, 0)]
        area = calculate_polygon_area(vertices)
        assert area == 12.0
    
    def test_different_starting_point(self):
        """Test that starting from a different vertex gives same area."""
        # Square starting from different vertices
        vertices1 = [(0, 0), (1, 0), (1, 1), (0, 1)]
        vertices2 = [(1, 0), (1, 1), (0, 1), (0, 0)]
        vertices3 = [(1, 1), (0, 1), (0, 0), (1, 0)]
        
        area1 = calculate_polygon_area(vertices1)
        area2 = calculate_polygon_area(vertices2)
        area3 = calculate_polygon_area(vertices3)
        
        assert area1 == area2 == area3 == 1.0


class TestFloatingPointCoordinates:
    """Test calculations with floating-point coordinates."""
    
    def test_float_coordinates(self):
        """Test with floating-point coordinate values."""
        vertices = [(0.5, 0.5), (2.5, 0.5), (2.5, 2.5), (0.5, 2.5)]
        area = calculate_polygon_area(vertices)
        assert area == 4.0
    
    def test_negative_coordinates(self):
        """Test with negative coordinate values."""
        vertices = [(-2, -2), (2, -2), (2, 2), (-2, 2)]
        area = calculate_polygon_area(vertices)
        assert area == 16.0
    
    def test_mixed_coordinates(self):
        """Test with mixed positive and negative coordinates."""
        vertices = [(-1, -1), (1, -1), (2, 2), (-2, 2)]
        area = calculate_polygon_area(vertices)
        assert area == 9.0


class TestInputValidation:
    """Test input validation and error handling."""
    
    def test_empty_vertices_list(self):
        """Test that empty vertices list raises ValueError."""
        with pytest.raises(ValueError, match="Vertices list cannot be empty"):
            calculate_polygon_area([])
    
    def test_one_vertex(self):
        """Test that a single vertex raises ValueError."""
        with pytest.raises(ValueError, match="at least 3 vertices"):
            calculate_polygon_area([(0, 0)])
    
    def test_two_vertices(self):
        """Test that two vertices raise ValueError."""
        with pytest.raises(ValueError, match="at least 3 vertices"):
            calculate_polygon_area([(0, 0), (1, 1)])
    
    def test_non_list_input(self):
        """Test that non-list/tuple input raises TypeError."""
        with pytest.raises(TypeError, match="must be a list or tuple"):
            calculate_polygon_area("not a list")
    
    def test_invalid_vertex_format(self):
        """Test that invalid vertex format raises TypeError."""
        with pytest.raises(TypeError, match="must be a tuple or list"):
            calculate_polygon_area([(0, 0), "invalid", (1, 1)])
    
    def test_wrong_dimension_vertex(self):
        """Test that vertices with wrong dimensions raise ValueError."""
        with pytest.raises(ValueError, match="exactly 2 coordinates"):
            calculate_polygon_area([(0, 0, 0), (1, 1, 1), (2, 2, 2)])
    
    def test_non_numeric_coordinate(self):
        """Test that non-numeric coordinates raise TypeError."""
        with pytest.raises(TypeError, match="must be numeric"):
            calculate_polygon_area([(0, 0), ("x", "y"), (1, 1)])
    
    def test_single_non_numeric_coordinate(self):
        """Test that a single non-numeric coordinate raises TypeError."""
        with pytest.raises(TypeError, match="coordinate must be numeric"):
            calculate_polygon_area([(0, 0), (1, "y"), (2, 2)])


class TestValidatePolygon:
    """Test the validate_polygon function separately."""
    
    def test_valid_triangle(self):
        """Test that valid triangle passes validation."""
        vertices = [(0, 0), (1, 0), (0, 1)]
        # Should not raise any exception
        validate_polygon(vertices)
    
    def test_valid_square(self):
        """Test that valid square passes validation."""
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        # Should not raise any exception
        validate_polygon(vertices)
    
    def test_invalid_less_than_three(self):
        """Test that less than 3 vertices fails validation."""
        with pytest.raises(ValueError):
            validate_polygon([(0, 0), (1, 1)])


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_very_small_polygon(self):
        """Test with very small coordinate values."""
        vertices = [(0, 0), (0.001, 0), (0.001, 0.001), (0, 0.001)]
        area = calculate_polygon_area(vertices)
        assert abs(area - 0.000001) < 1e-9
    
    def test_very_large_polygon(self):
        """Test with very large coordinate values."""
        vertices = [(0, 0), (1000000, 0), (1000000, 1000000), (0, 1000000)]
        area = calculate_polygon_area(vertices)
        assert area == 1e12  # 1 trillion
    
    def test_collinear_points_triangle(self):
        """Test with collinear points forming a degenerate triangle."""
        # Three points on a line should give area 0
        vertices = [(0, 0), (1, 1), (2, 2)]
        area = calculate_polygon_area(vertices)
        assert area == 0.0


class TestCalculatePolygonAreaWithInfo:
    """Test the calculate_polygon_area_with_info function."""
    
    def test_basic_info_square(self):
        """Test that additional info is calculated correctly for a square."""
        vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
        info = calculate_polygon_area_with_info(vertices)
        
        assert info['area'] == 4.0
        assert info['vertices_count'] == 4
        assert info['perimeter'] == 8.0
        assert info['centroid'] == (1.0, 1.0)
    
    def test_basic_info_triangle(self):
        """Test additional info for a triangle."""
        vertices = [(0, 0), (4, 0), (2, 3)]
        info = calculate_polygon_area_with_info(vertices)
        
        assert info['area'] == 6.0
        assert info['vertices_count'] == 3
        # Perimeter: 4 + sqrt(13) + sqrt(13) ≈ 11.211
        assert abs(info['perimeter'] - 11.211) < 0.01
        # Centroid: ((0+4+2)/3, (0+0+3)/3) = (2, 1)
        assert info['centroid'] == (2.0, 1.0)
    
    def test_info_return_type(self):
        """Test that the function returns a dictionary."""
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        info = calculate_polygon_area_with_info(vertices)
        
        assert isinstance(info, dict)
        assert 'area' in info
        assert 'vertices_count' in info
        assert 'perimeter' in info
        assert 'centroid' in info


class TestIntegration:
    """Integration tests for the complete module."""
    
    def test_import_from_package(self):
        """Test that functions can be imported from the package."""
        from shoelace_polygon_area import calculate_polygon_area, validate_polygon
        
        vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        area = calculate_polygon_area(vertices)
        assert area == 1.0
    
    def test_module_has_version(self):
        """Test that the module has a version attribute."""
        import shoelace_polygon_area
        assert hasattr(shoelace_polygon_area, '__version__')
        assert isinstance(shoelace_polygon_area.__version__, str)
    
    def test_module_all_attribute(self):
        """Test that the module has __all__ defined."""
        import shoelace_polygon_area
        assert hasattr(shoelace_polygon_area, '__all__')
        assert 'calculate_polygon_area' in shoelace_polygon_area.__all__
        assert 'validate_polygon' in shoelace_polygon_area.__all__


class TestDocumentation:
    """Test that functions have proper documentation."""
    
    def test_calculate_polygon_area_has_docstring(self):
        """Test that main function has a docstring."""
        assert calculate_polygon_area.__doc__ is not None
        assert len(calculate_polygon_area.__doc__) > 50
    
    def test_validate_polygon_has_docstring(self):
        """Test that validation function has a docstring."""
        assert validate_polygon.__doc__ is not None
        assert len(validate_polygon.__doc__) > 50
    
    def test_module_has_docstring(self):
        """Test that the module has a docstring."""
        import shoelace_polygon_area
        assert shoelace_polygon_area.__doc__ is not None


class TestGPSCoordinateParsing:
    """Test GPS coordinate parsing functionality."""
    
    def test_parse_basic_gps_coordinates(self):
        """Test parsing GPS coordinates in lat long alt accuracy format."""
        gps_str = "1.0 2.0 0.0 0.0; 1.0 3.0 0.0 0.0; 2.0 3.0 0.0 0.0"
        coords = parse_gps_coordinates(gps_str)
        expected = [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
        assert coords == expected
    
    def test_parse_gps_with_decimals(self):
        """Test parsing GPS coordinates with decimal values."""
        gps_str = "1.323123 2.21312 0.0 0.0; 1.5 2.5 0.0 0.0; 2.0 3.0 0.0 0.0"
        coords = parse_gps_coordinates(gps_str)
        assert len(coords) == 3
        assert coords[0] == (2.21312, 1.323123)
        assert coords[1] == (2.5, 1.5)
        assert coords[2] == (3.0, 2.0)
    
    def test_parse_gps_lat_long_format(self):
        """Test parsing GPS coordinates in lat long format (no altitude/accuracy)."""
        gps_str = "1.0 2.0; 1.0 3.0; 2.0 3.0"
        coords = parse_gps_coordinates(gps_str, coordinate_format="lat_long")
        expected = [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
        assert coords == expected
    
    def test_parse_gps_long_lat_format(self):
        """Test parsing GPS coordinates in long lat format (reversed)."""
        gps_str = "2.0 1.0; 3.0 1.0; 3.0 2.0"
        coords = parse_gps_coordinates(gps_str, coordinate_format="long_lat")
        expected = [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
        assert coords == expected
    
    def test_parse_gps_with_extra_spaces(self):
        """Test that extra spaces are handled correctly."""
        gps_str = "  1.0   2.0   0.0   0.0  ;  1.0   3.0   0.0   0.0  ;  2.0   3.0   0.0   0.0  "
        coords = parse_gps_coordinates(gps_str)
        expected = [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
        assert coords == expected
    
    def test_parse_gps_with_trailing_semicolon(self):
        """Test that trailing semicolons are handled correctly."""
        gps_str = "1.0 2.0 0.0 0.0; 1.0 3.0 0.0 0.0; 2.0 3.0 0.0 0.0;"
        coords = parse_gps_coordinates(gps_str)
        expected = [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
        assert coords == expected
    
    def test_parse_gps_negative_coordinates(self):
        """Test parsing GPS coordinates with negative values."""
        gps_str = "-1.0 -2.0 0.0 0.0; -1.0 2.0 0.0 0.0; 2.0 2.0 0.0 0.0"
        coords = parse_gps_coordinates(gps_str)
        assert len(coords) == 3
        assert coords[0] == (-2.0, -1.0)
    
    def test_parse_gps_empty_string(self):
        """Test that empty GPS string raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            parse_gps_coordinates("")
    
    def test_parse_gps_whitespace_only(self):
        """Test that whitespace-only GPS string raises ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            parse_gps_coordinates("   ")
    
    def test_parse_gps_non_string_input(self):
        """Test that non-string input raises TypeError."""
        with pytest.raises(TypeError, match="must be a string"):
            parse_gps_coordinates(123)
    
    def test_parse_gps_too_few_vertices(self):
        """Test that fewer than 3 coordinates raises ValueError."""
        gps_str = "1.0 2.0 0.0 0.0; 1.0 3.0 0.0 0.0"
        with pytest.raises(ValueError, match="at least 3 vertices"):
            parse_gps_coordinates(gps_str)
    
    def test_parse_gps_invalid_coordinate_values(self):
        """Test that non-numeric coordinate values raise ValueError."""
        gps_str = "1.0 2.0 0.0 0.0; abc def 0.0 0.0; 2.0 3.0 0.0 0.0"
        with pytest.raises(ValueError, match="non-numeric values"):
            parse_gps_coordinates(gps_str)
    
    def test_parse_gps_insufficient_values_per_coordinate(self):
        """Test that insufficient values in a coordinate set raises ValueError."""
        gps_str = "1.0 2.0 0.0 0.0; 1.0; 2.0 3.0 0.0 0.0"
        with pytest.raises(ValueError, match="at least 2 values"):
            parse_gps_coordinates(gps_str)
    
    def test_parse_gps_unknown_format(self):
        """Test that unknown coordinate format raises ValueError."""
        gps_str = "1.0 2.0 0.0 0.0; 1.0 3.0 0.0 0.0; 2.0 3.0 0.0 0.0"
        with pytest.raises(ValueError, match="Unknown coordinate format"):
            parse_gps_coordinates(gps_str, coordinate_format="invalid_format")


class TestCalculatePolygonAreaFromGPS:
    """Test calculating polygon area directly from GPS coordinates."""
    
    def test_calculate_area_from_gps_basic(self):
        """Test calculating area from GPS coordinates."""
        # Triangle with known area
        gps_str = "0.0 0.0 0.0 0.0; 0.0 4.0 0.0 0.0; 3.0 0.0 0.0 0.0"
        area = calculate_polygon_area_from_gps(gps_str)
        assert area == 6.0
    
    def test_calculate_area_from_gps_square(self):
        """Test calculating area of a square from GPS coordinates."""
        gps_str = "0.0 0.0 0.0 0.0; 0.0 5.0 0.0 0.0; 5.0 5.0 0.0 0.0; 5.0 0.0 0.0 0.0"
        area = calculate_polygon_area_from_gps(gps_str)
        assert area == 25.0
    
    def test_calculate_area_from_gps_lat_long_format(self):
        """Test calculating area with lat long format."""
        gps_str = "0.0 0.0; 0.0 4.0; 3.0 0.0"
        area = calculate_polygon_area_from_gps(gps_str, coordinate_format="lat_long")
        assert area == 6.0
    
    def test_calculate_area_from_gps_real_coordinates(self):
        """Test with realistic GPS coordinate values."""
        # Small plot near equator (simplified for testing)
        # This creates a rectangle: 0.001 degrees lat x 0.001 degrees long
        gps_str = "40.7128 -74.0060 0.0 0.0; 40.7138 -74.0060 0.0 0.0; 40.7138 -74.0050 0.0 0.0; 40.7128 -74.0050 0.0 0.0"
        area = calculate_polygon_area_from_gps(gps_str)
        # Area in square degrees: approximately 0.001 * 0.001 = 0.000001 = 1e-6
        assert area == pytest.approx(1e-6, rel=1e-6)
    
    def test_calculate_area_from_gps_invalid_input(self):
        """Test that invalid GPS string raises appropriate error."""
        with pytest.raises(ValueError):
            calculate_polygon_area_from_gps("invalid")
    
    def test_calculate_area_from_gps_preserves_altitude_accuracy(self):
        """Test that altitude and accuracy values don't affect the area calculation."""
        # Same coordinates with different altitude and accuracy
        gps_str1 = "0.0 0.0 0.0 0.0; 0.0 4.0 0.0 0.0; 3.0 0.0 0.0 0.0"
        gps_str2 = "0.0 0.0 100.0 5.0; 0.0 4.0 200.0 10.0; 3.0 0.0 150.0 8.0"
        
        area1 = calculate_polygon_area_from_gps(gps_str1)
        area2 = calculate_polygon_area_from_gps(gps_str2)
        
        assert area1 == area2 == 6.0
