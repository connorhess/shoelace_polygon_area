"""
Shoelace Polygon Area Calculator

This module provides functions to calculate the area of a polygon using the Shoelace formula
(also known as the surveyor's formula or Gauss's area formula).

The Shoelace formula is a mathematical algorithm to determine the area of a simple polygon
whose vertices are described by their Cartesian coordinates in the plane.

Example:
    >>> from shoelace_polygon_area import calculate_polygon_area
    >>> vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    >>> area = calculate_polygon_area(vertices)
    >>> print(area)
    12.0
"""

# Version of the shoelace_polygon_area package
__version__ = "1.0.0"

# Import main functions to make them available at package level
from .polygon_area import calculate_polygon_area, validate_polygon

# Define what should be imported with "from shoelace_polygon_area import *"
__all__ = ['calculate_polygon_area', 'validate_polygon', '__version__']
