# Shoelace Polygon Area Calculator

A Python module to calculate the area of a polygon using the **Shoelace formula** (also known as the surveyor's formula or Gauss's area formula).

## Overview

The Shoelace formula is a mathematical algorithm to determine the area of a simple polygon whose vertices are described by their Cartesian coordinates in the plane. This implementation provides a clean, well-documented, and thoroughly tested Python module for calculating polygon areas.

## Features

- ✅ **Simple API**: Easy-to-use function for calculating polygon areas
- ✅ **GPS Coordinate Support**: Parse GPS coordinates in shapefile format
- ✅ **Well-documented**: Extensive comments and docstrings explaining each step
- ✅ **Robust validation**: Comprehensive input validation with clear error messages
- ✅ **Flexible input**: Works with any numeric coordinates (int or float)
- ✅ **Order-independent**: Handles both clockwise and counter-clockwise vertex ordering
- ✅ **Thoroughly tested**: Comprehensive test suite with 58+ test cases
- ✅ **Type hints**: Full type annotations for better IDE support
- ✅ **Additional features**: Extra function providing polygon perimeter and centroid

## Installation

### From source

```bash
git clone https://github.com/connorhess/shoelace_polygon_area.git
cd shoelace_polygon_area
pip install -e .
```

### For development

```bash
pip install -e ".[dev]"
```

Or using the requirements file:

```bash
pip install -r requirements-dev.txt
```

## Usage

### Basic Usage

```python
from shoelace_polygon_area import calculate_polygon_area

# Define polygon vertices as a list of (x, y) tuples
# Example: A square with side length 4
vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]

# Calculate the area
area = calculate_polygon_area(vertices)
print(f"Area: {area}")  # Output: Area: 16.0
```

### More Examples

```python
from shoelace_polygon_area import calculate_polygon_area

# Triangle
triangle = [(0, 0), (4, 0), (2, 3)]
area = calculate_polygon_area(triangle)
print(f"Triangle area: {area}")  # Output: 6.0

# Pentagon
pentagon = [(0, 0), (2, 0), (3, 1), (1, 3), (-1, 1)]
area = calculate_polygon_area(pentagon)
print(f"Pentagon area: {area}")  # Output: 7.0

# Works with floating-point coordinates
float_coords = [(0.5, 0.5), (2.5, 0.5), (2.5, 2.5), (0.5, 2.5)]
area = calculate_polygon_area(float_coords)
print(f"Float area: {area}")  # Output: 4.0

# Works with negative coordinates
negative = [(-2, -2), (2, -2), (2, 2), (-2, 2)]
area = calculate_polygon_area(negative)
print(f"Negative coords area: {area}")  # Output: 16.0
```

### Getting Additional Information

```python
from shoelace_polygon_area.polygon_area import calculate_polygon_area_with_info

vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
info = calculate_polygon_area_with_info(vertices)

print(f"Area: {info['area']}")              # Output: 12.0
print(f"Vertices: {info['vertices_count']}")  # Output: 4
print(f"Perimeter: {info['perimeter']}")    # Output: 14.0
print(f"Centroid: {info['centroid']}")      # Output: (2.0, 1.5)
```

### Working with GPS Coordinates

The module supports GPS coordinates in shapefile format, making it easy to calculate areas from GPS data:

```python
from shoelace_polygon_area import (
    parse_gps_coordinates,
    calculate_polygon_area_from_gps
)

# GPS coordinates in format: lat long alt accuracy
gps_string = "1.323123 2.21312 0.0 0.0; 1.5 2.5 0.0 0.0; 2.0 3.0 0.0 0.0"

# Method 1: Parse and then calculate
coords = parse_gps_coordinates(gps_string)
area = calculate_polygon_area(coords)

# Method 2: Calculate directly from GPS string
area = calculate_polygon_area_from_gps(gps_string)
print(f"Area: {area} square degrees")

# Simplified format (lat long only)
simple_gps = "0.0 0.0; 0.0 4.0; 3.0 0.0"
area = calculate_polygon_area_from_gps(simple_gps, coordinate_format="lat_long")
print(f"Area: {area} square degrees")

# Real-world example: Plot of land
plot_gps = (
    "40.7128 -74.0060 10.5 0.5; "
    "40.7138 -74.0060 10.2 0.5; "
    "40.7138 -74.0050 10.8 0.5; "
    "40.7128 -74.0050 11.0 0.5"
)
area = calculate_polygon_area_from_gps(plot_gps)
print(f"Plot area: {area} square degrees")
```

**Supported GPS Formats:**
- `"lat_long_alt_accuracy"`: Latitude, Longitude, Altitude, Accuracy (default)
- `"lat_long"`: Latitude, Longitude only
- `"long_lat"`: Longitude, Latitude (reversed)

**Note:** GPS coordinates are given in decimal degrees. For accurate ground area measurements, consider using appropriate coordinate projection systems that account for Earth's curvature. The area returned is in square degrees.

### Input Validation

The module includes robust input validation:

```python
from shoelace_polygon_area import calculate_polygon_area, validate_polygon

# Validate before calculating (optional - calculate_polygon_area does this automatically)
vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
validate_polygon(vertices)  # Raises exception if invalid

# Invalid inputs will raise appropriate errors:
try:
    calculate_polygon_area([(0, 0), (1, 1)])  # Only 2 vertices
except ValueError as e:
    print(e)  # "A polygon must have at least 3 vertices"

try:
    calculate_polygon_area([(0, 0), ("x", "y"), (1, 1)])  # Non-numeric
except TypeError as e:
    print(e)  # "Vertex 1 x-coordinate must be numeric"
```

## How It Works

The Shoelace formula calculates the area of a polygon using the coordinates of its vertices:

```
Area = 1/2 * |Σ(xᵢ × yᵢ₊₁ - xᵢ₊₁ × yᵢ)| for i = 1 to n
```

Where:
- `n` is the number of vertices
- `(xᵢ, yᵢ)` are the coordinates of vertex i
- The indices wrap around (vertex n+1 is vertex 1)

The algorithm:
1. Takes each pair of consecutive vertices
2. Computes the cross product: `x₁ × y₂ - x₂ × y₁`
3. Sums all cross products
4. Takes the absolute value and divides by 2

The name "Shoelace" comes from the pattern of cross-multiplication that resembles the crisscross pattern of shoelaces.

## API Reference

### `calculate_polygon_area(vertices)`

Calculate the area of a polygon using the Shoelace formula.

**Parameters:**
- `vertices` (List[Tuple[Union[int, float], Union[int, float]]]): A list of tuples representing (x, y) coordinates of polygon vertices in order

**Returns:**
- `float`: The area of the polygon (always non-negative)

**Raises:**
- `ValueError`: If the vertices don't form a valid polygon (less than 3 vertices)
- `TypeError`: If the input types are incorrect

### `validate_polygon(vertices)`

Validate that the input represents a valid polygon.

**Parameters:**
- `vertices` (List[Tuple[Union[int, float], Union[int, float]]]): A list of tuples representing (x, y) coordinates

**Raises:**
- `ValueError`: If the vertices don't form a valid polygon
- `TypeError`: If the input types are incorrect

### `calculate_polygon_area_with_info(vertices)`

Calculate polygon area and return additional information.

**Parameters:**
- `vertices` (List[Tuple[Union[int, float], Union[int, float]]]): A list of tuples representing (x, y) coordinates

**Returns:**
- `dict`: A dictionary containing:
  - `area`: The calculated area of the polygon
  - `vertices_count`: The number of vertices
  - `perimeter`: The perimeter of the polygon
  - `centroid`: The centroid (center of mass) as (x, y) tuple

### `parse_gps_coordinates(gps_string, coordinate_format="lat_long_alt_accuracy")`

Parse GPS coordinates from a shapefile-like string format.

**Parameters:**
- `gps_string` (str): A string containing GPS coordinates separated by semicolons. Format: `"lat long alt accuracy; lat long alt accuracy; ..."`
- `coordinate_format` (str): The format of each coordinate set. Options:
  - `"lat_long_alt_accuracy"`: Latitude, Longitude, Altitude, Accuracy (default)
  - `"lat_long"`: Latitude and Longitude only
  - `"long_lat"`: Longitude and Latitude (reversed order)

**Returns:**
- `List[Tuple[float, float]]`: A list of (longitude, latitude) tuples that can be used with `calculate_polygon_area()`

**Raises:**
- `ValueError`: If the GPS string is invalid or doesn't define a valid polygon
- `TypeError`: If the input types are incorrect

### `calculate_polygon_area_from_gps(gps_string, coordinate_format="lat_long_alt_accuracy")`

Calculate the area of a polygon directly from GPS coordinates.

**Parameters:**
- `gps_string` (str): A string containing GPS coordinates separated by semicolons
- `coordinate_format` (str): The format of each coordinate set (see `parse_gps_coordinates`)

**Returns:**
- `float`: The area of the polygon in square degrees

**Raises:**
- `ValueError`: If the GPS string is invalid or doesn't define a valid polygon

## Testing

The module includes a comprehensive test suite with 58+ test cases covering:

- Basic shapes (triangles, squares, rectangles)
- Complex polygons (pentagons, hexagons, irregular shapes)
- Vertex ordering (clockwise vs counter-clockwise)
- Floating-point coordinates
- Negative coordinates
- GPS coordinate parsing and validation
- Multiple GPS coordinate formats
- Input validation and error handling
- Edge cases (collinear points, very small/large coordinates)
- Integration tests
- Documentation tests

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=shoelace_polygon_area --cov-report=html

# Run specific test class
pytest tests/test_polygon_area.py::TestBasicShapes

# Run with verbose output
pytest -v
```

### Test Coverage

The test suite provides comprehensive coverage of all functions and edge cases.

## Project Structure

```
shoelace_polygon_area/
├── shoelace_polygon_area/      # Main package directory
│   ├── __init__.py             # Package initialization and exports
│   └── polygon_area.py         # Core implementation with Shoelace formula
├── tests/                      # Test suite
│   ├── __init__.py
│   └── test_polygon_area.py    # Comprehensive test cases
├── gps_example.py              # GPS coordinate usage examples
├── examples.py                 # Basic usage examples
├── demo.py                     # Demonstration script
├── pyproject.toml              # Modern Python project configuration
├── requirements-dev.txt        # Development dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore patterns
```

## Requirements

- Python 3.8 or higher
- No runtime dependencies (standard library only)
- Development dependencies: pytest, pytest-cov

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Mathematical Background

The Shoelace formula is also known as:
- **Surveyor's formula**: Used by surveyors to calculate land areas
- **Gauss's area formula**: Named after mathematician Carl Friedrich Gauss

### Properties

- Works for any simple polygon (non-self-intersecting)
- Handles both convex and concave polygons
- Result is independent of vertex ordering
- Efficient: O(n) time complexity where n is the number of vertices

### References

- [Shoelace Formula - Wikipedia](https://en.wikipedia.org/wiki/Shoelace_formula)
- [Surveyor's Formula - MathWorld](https://mathworld.wolfram.com/PolygonArea.html)

## Examples Gallery

### Triangle Area Calculation
```python
# Right triangle with base 4 and height 3
vertices = [(0, 0), (4, 0), (0, 3)]
area = calculate_polygon_area(vertices)  # 6.0
```

### Complex Polygon
```python
# Irregular hexagon
vertices = [(1, 0), (2, 1), (2, 3), (1, 4), (0, 3), (0, 1)]
area = calculate_polygon_area(vertices)  # 7.0
```

### Real-world Example: Plot of Land
```python
# GPS coordinates of a plot of land (simplified)
plot = [(0, 0), (50, 0), (60, 30), (40, 50), (0, 45)]
area_sq_meters = calculate_polygon_area(plot)
print(f"Land area: {area_sq_meters} square meters")
```

### GPS Coordinate Example
```python
from shoelace_polygon_area import calculate_polygon_area_from_gps

# Plot with GPS coordinates (lat long alt accuracy format)
gps_plot = (
    "40.7128 -74.0060 10.5 0.5; "
    "40.7138 -74.0060 10.2 0.5; "
    "40.7138 -74.0050 10.8 0.5; "
    "40.7128 -74.0050 11.0 0.5"
)
area = calculate_polygon_area_from_gps(gps_plot)
print(f"Plot area: {area} square degrees")
```

## Support

For issues, questions, or contributions, please visit:
- **GitHub Issues**: https://github.com/connorhess/shoelace_polygon_area/issues
- **Repository**: https://github.com/connorhess/shoelace_polygon_area

---

**Note**: This module is designed for educational and practical use. The implementation prioritizes clarity and correctness with extensive documentation to help users understand the Shoelace formula.