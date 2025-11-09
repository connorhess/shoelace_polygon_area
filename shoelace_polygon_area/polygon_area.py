"""
Polygon Area Calculation Module

This module implements the Shoelace formula (also known as the surveyor's formula)
for calculating the area of a polygon given its vertices.

The Shoelace formula gets its name from the pattern of cross-multiplication that
resembles the crisscross pattern of shoelaces.

Mathematical Background:
    For a polygon with n vertices (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ), the area is:
    
    Area = 1/2 * |Σ(xᵢ * yᵢ₊₁ - xᵢ₊₁ * yᵢ)| for i = 1 to n
    
    where the indices wrap around (i.e., vertex n+1 is vertex 1).

References:
    - https://en.wikipedia.org/wiki/Shoelace_formula
"""

from typing import List, Tuple, Union, Optional


def validate_polygon(vertices: List[Tuple[Union[int, float], Union[int, float]]]) -> None:
    """
    Validate that the input represents a valid polygon.
    
    This function checks that:
    1. The vertices list is not empty
    2. The polygon has at least 3 vertices (minimum for a polygon)
    3. Each vertex is a tuple or list with exactly 2 coordinates
    4. All coordinates are numeric (int or float)
    
    Args:
        vertices: A list of tuples/lists representing (x, y) coordinates of polygon vertices
        
    Raises:
        ValueError: If the vertices don't form a valid polygon
        TypeError: If the input types are incorrect
        
    Example:
        >>> validate_polygon([(0, 0), (1, 0), (1, 1)])  # Valid - returns None
        >>> validate_polygon([(0, 0), (1, 0)])  # Raises ValueError - only 2 vertices
        Traceback (most recent call last):
        ...
        ValueError: A polygon must have at least 3 vertices. Got 2 vertices.
    """
    # Check if vertices is a list or tuple
    if not isinstance(vertices, (list, tuple)):
        raise TypeError(
            f"Vertices must be a list or tuple, got {type(vertices).__name__}"
        )
    
    # Check if vertices list is empty
    if not vertices:
        raise ValueError("Vertices list cannot be empty")
    
    # Check if polygon has at least 3 vertices
    # This is the minimum requirement for a polygon (triangle)
    if len(vertices) < 3:
        raise ValueError(
            f"A polygon must have at least 3 vertices. Got {len(vertices)} vertices."
        )
    
    # Validate each vertex
    for i, vertex in enumerate(vertices):
        # Check if vertex is a tuple or list
        if not isinstance(vertex, (tuple, list)):
            raise TypeError(
                f"Vertex {i} must be a tuple or list, got {type(vertex).__name__}"
            )
        
        # Check if vertex has exactly 2 coordinates (x and y)
        if len(vertex) != 2:
            raise ValueError(
                f"Vertex {i} must have exactly 2 coordinates (x, y), "
                f"got {len(vertex)} coordinates"
            )
        
        # Check if both coordinates are numeric (int or float)
        x, y = vertex
        if not isinstance(x, (int, float)):
            raise TypeError(
                f"Vertex {i} x-coordinate must be numeric, got {type(x).__name__}"
            )
        if not isinstance(y, (int, float)):
            raise TypeError(
                f"Vertex {i} y-coordinate must be numeric, got {type(y).__name__}"
            )


def calculate_polygon_area(
    vertices: List[Tuple[Union[int, float], Union[int, float]]]
) -> float:
    """
    Calculate the area of a polygon using the Shoelace formula.
    
    The Shoelace formula (also known as the surveyor's formula or Gauss's area formula)
    is a mathematical algorithm to determine the area of a simple polygon whose vertices
    are described by their Cartesian coordinates in the plane.
    
    The formula works by:
    1. Taking each pair of consecutive vertices
    2. Computing the cross product (x₁ * y₂ - x₂ * y₁)
    3. Summing all cross products
    4. Taking the absolute value and dividing by 2
    
    The algorithm automatically "closes" the polygon by connecting the last vertex
    back to the first vertex.
    
    Args:
        vertices: A list of tuples representing (x, y) coordinates of polygon vertices
                 in order (either clockwise or counter-clockwise). Each vertex should
                 be a tuple of two numbers (int or float).
                 
    Returns:
        float: The area of the polygon as a positive number. The result is always
               non-negative regardless of the vertex order (clockwise or counter-clockwise).
               
    Raises:
        ValueError: If the vertices don't form a valid polygon (less than 3 vertices)
        TypeError: If the input types are incorrect
        
    Examples:
        >>> # Square with side length 4
        >>> vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
        >>> calculate_polygon_area(vertices)
        16.0
        
        >>> # Triangle
        >>> vertices = [(0, 0), (4, 0), (2, 3)]
        >>> calculate_polygon_area(vertices)
        6.0
        
        >>> # Pentagon
        >>> vertices = [(0, 0), (2, 0), (3, 1), (1, 3), (-1, 1)]
        >>> calculate_polygon_area(vertices)
        7.0
        
    Note:
        - The vertices should be in order (either all clockwise or all counter-clockwise)
        - The polygon should be simple (non-self-intersecting) for accurate results
        - The formula works for both convex and concave polygons
        - Coordinates can be integers or floating-point numbers
    """
    # Step 1: Validate input to ensure we have a valid polygon
    # This will raise appropriate errors if validation fails
    validate_polygon(vertices)
    
    # Step 2: Initialize the area accumulator to zero
    # We'll add the cross products of consecutive vertices to this variable
    area = 0.0
    
    # Step 3: Get the number of vertices in the polygon
    # This will help us iterate through all vertices and wrap around to the first
    n = len(vertices)
    
    # Step 4: Apply the Shoelace formula
    # Iterate through each vertex and compute cross products with the next vertex
    # The formula: Area = 1/2 * |Σ(xᵢ * yᵢ₊₁ - xᵢ₊₁ * yᵢ)|
    for i in range(n):
        # Get the current vertex coordinates
        x1, y1 = vertices[i]
        
        # Get the next vertex coordinates
        # Use modulo (%) to wrap around: when i = n-1, (i+1) % n = 0
        # This connects the last vertex back to the first vertex
        x2, y2 = vertices[(i + 1) % n]
        
        # Compute the cross product for this pair of vertices
        # Cross product = (x1 * y2) - (x2 * y1)
        # This represents the signed area of the parallelogram formed by
        # the two vertices and the origin
        cross_product = (x1 * y2) - (x2 * y1)
        
        # Add the cross product to our running total
        # Note: Some cross products may be negative depending on vertex order
        area += cross_product
    
    # Step 5: Finalize the area calculation
    # Divide by 2 to get the actual area (formula requires this)
    # Take absolute value to ensure positive result regardless of vertex order
    # (clockwise gives positive, counter-clockwise gives negative, or vice versa)
    area = abs(area) / 2.0
    
    # Step 6: Return the calculated area
    return area


# Additional helper function for advanced use cases
def calculate_polygon_area_with_info(
    vertices: List[Tuple[Union[int, float], Union[int, float]]]
) -> dict:
    """
    Calculate polygon area and return additional information.
    
    This function provides the same area calculation as calculate_polygon_area()
    but also returns additional information about the polygon.
    
    Args:
        vertices: A list of tuples representing (x, y) coordinates of polygon vertices
        
    Returns:
        dict: A dictionary containing:
            - 'area': The calculated area of the polygon
            - 'vertices_count': The number of vertices
            - 'perimeter': The perimeter of the polygon
            - 'centroid': The centroid (center of mass) of the polygon
            
    Example:
        >>> vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
        >>> info = calculate_polygon_area_with_info(vertices)
        >>> info['area']
        12.0
        >>> info['vertices_count']
        4
    """
    # Calculate the area using our main function
    area = calculate_polygon_area(vertices)
    
    # Calculate the perimeter by summing the distances between consecutive vertices
    perimeter = 0.0
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        # Euclidean distance formula: sqrt((x2-x1)² + (y2-y1)²)
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        perimeter += distance
    
    # Calculate the centroid (geometric center) of the polygon
    # Centroid x-coordinate: sum of all x-coordinates divided by number of vertices
    # Centroid y-coordinate: sum of all y-coordinates divided by number of vertices
    centroid_x = sum(vertex[0] for vertex in vertices) / n
    centroid_y = sum(vertex[1] for vertex in vertices) / n
    
    # Return all the information as a dictionary
    return {
        'area': area,
        'vertices_count': n,
        'perimeter': perimeter,
        'centroid': (centroid_x, centroid_y)
    }


def parse_gps_coordinates(
    gps_string: str,
    coordinate_format: str = "lat_long_alt_accuracy"
) -> List[Tuple[float, float]]:
    """
    Parse GPS coordinates from a shapefile-like string format.
    
    This function parses GPS coordinate strings in various formats and extracts
    the latitude and longitude values to create a list of (x, y) tuples suitable
    for polygon area calculation.
    
    Args:
        gps_string: A string containing GPS coordinates separated by semicolons.
                   Each coordinate set should contain space-separated values.
                   Format: "lat long alt accuracy; lat long alt accuracy; ..."
                   Example: "1.323123 2.21312 0.0 0.0; 1.5 2.5 0.0 0.0"
        coordinate_format: The format of each coordinate set. Options:
                          - "lat_long_alt_accuracy": lat, long, altitude, accuracy (default)
                          - "lat_long": only latitude and longitude
                          - "long_lat": longitude, latitude (reversed)
                          
    Returns:
        List[Tuple[float, float]]: A list of (longitude, latitude) tuples that can be
                                   used with calculate_polygon_area(). Note that the
                                   return format is (longitude, latitude) which corresponds
                                   to (x, y) in standard Cartesian coordinates.
                                   
    Raises:
        ValueError: If the GPS string is empty, invalid, or coordinates cannot be parsed
        
    Examples:
        >>> # Standard format with altitude and accuracy
        >>> gps_str = "1.0 2.0 0.0 0.0; 1.0 3.0 0.0 0.0; 2.0 3.0 0.0 0.0"
        >>> coords = parse_gps_coordinates(gps_str)
        >>> coords
        [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
        
        >>> # Calculate area from GPS coordinates
        >>> area = calculate_polygon_area(coords)
        >>> area
        1.0
        
        >>> # Format with only lat/long
        >>> gps_str = "1.0 2.0; 1.0 3.0; 2.0 3.0"
        >>> coords = parse_gps_coordinates(gps_str, coordinate_format="lat_long")
        >>> coords
        [(2.0, 1.0), (3.0, 1.0), (3.0, 2.0)]
    
    Note:
        - GPS coordinates are typically given as (latitude, longitude), but for
          area calculations we treat longitude as x and latitude as y
        - Altitude and accuracy values are ignored for area calculations
        - Empty or whitespace-only coordinate sets are skipped
        - The function is flexible and handles various spacing and formatting
    """
    # Validate input
    if not isinstance(gps_string, str):
        raise TypeError(
            f"GPS string must be a string, got {type(gps_string).__name__}"
        )
    
    if not gps_string or not gps_string.strip():
        raise ValueError("GPS coordinate string cannot be empty")
    
    # Split by semicolons to get individual coordinate sets
    coordinate_sets = gps_string.split(';')
    
    # Parse each coordinate set
    vertices = []
    for i, coord_set in enumerate(coordinate_sets):
        # Skip empty or whitespace-only sets
        coord_set = coord_set.strip()
        if not coord_set:
            continue
        
        # Split by whitespace to get individual values
        values = coord_set.split()
        
        # Parse based on format
        try:
            if coordinate_format == "lat_long_alt_accuracy":
                if len(values) < 2:
                    raise ValueError(
                        f"Coordinate set {i} must have at least 2 values (lat, long), "
                        f"got {len(values)} values"
                    )
                # Extract lat and long (first two values)
                lat = float(values[0])
                long = float(values[1])
                # Note: For polygon area, we use (longitude, latitude) as (x, y)
                vertices.append((long, lat))
                
            elif coordinate_format == "lat_long":
                if len(values) != 2:
                    raise ValueError(
                        f"Coordinate set {i} must have exactly 2 values (lat, long), "
                        f"got {len(values)} values"
                    )
                lat = float(values[0])
                long = float(values[1])
                vertices.append((long, lat))
                
            elif coordinate_format == "long_lat":
                if len(values) != 2:
                    raise ValueError(
                        f"Coordinate set {i} must have exactly 2 values (long, lat), "
                        f"got {len(values)} values"
                    )
                long = float(values[0])
                lat = float(values[1])
                vertices.append((long, lat))
                
            else:
                raise ValueError(
                    f"Unknown coordinate format: {coordinate_format}. "
                    f"Supported formats: 'lat_long_alt_accuracy', 'lat_long', 'long_lat'"
                )
                
        except ValueError as e:
            if "could not convert" in str(e):
                raise ValueError(
                    f"Coordinate set {i} contains non-numeric values: '{coord_set}'"
                ) from e
            raise
    
    # Validate that we got at least 3 vertices for a polygon
    if len(vertices) < 3:
        raise ValueError(
            f"Parsed coordinates must form a polygon with at least 3 vertices. "
            f"Got {len(vertices)} vertices from GPS string."
        )
    
    return vertices


def calculate_polygon_area_from_gps(
    gps_string: str,
    coordinate_format: str = "lat_long_alt_accuracy"
) -> float:
    """
    Calculate the area of a polygon defined by GPS coordinates.
    
    This is a convenience function that combines parse_gps_coordinates() and
    calculate_polygon_area() to directly calculate the area from a GPS string.
    
    Args:
        gps_string: A string containing GPS coordinates separated by semicolons.
                   Format: "lat long alt accuracy; lat long alt accuracy; ..."
                   Example: "1.323123 2.21312 0.0 0.0; 1.5 2.5 0.0 0.0"
        coordinate_format: The format of each coordinate set. Options:
                          - "lat_long_alt_accuracy": lat, long, altitude, accuracy (default)
                          - "lat_long": only latitude and longitude
                          - "long_lat": longitude, latitude (reversed)
                          
    Returns:
        float: The area of the polygon defined by the GPS coordinates
        
    Raises:
        ValueError: If the GPS string is invalid or doesn't define a valid polygon
        
    Examples:
        >>> # Calculate area from GPS coordinates with altitude and accuracy
        >>> gps_str = "0.0 0.0 0.0 0.0; 0.0 4.0 0.0 0.0; 3.0 0.0 0.0 0.0"
        >>> area = calculate_polygon_area_from_gps(gps_str)
        >>> area
        6.0
        
        >>> # With only lat/long
        >>> gps_str = "1.323123 2.21312; 1.5 2.5; 2.0 3.0"
        >>> area = calculate_polygon_area_from_gps(gps_str, coordinate_format="lat_long")
        
    Note:
        - This function assumes GPS coordinates are in decimal degrees
        - For accurate area calculations in real-world applications, consider
          projecting GPS coordinates to a suitable coordinate system
        - The area returned is in square degrees, which may not represent
          actual ground area accurately (use appropriate conversions for that)
    """
    vertices = parse_gps_coordinates(gps_string, coordinate_format)
    return calculate_polygon_area(vertices)
