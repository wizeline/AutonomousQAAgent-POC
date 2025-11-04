import math
from typing import Union

def calculate_rectangle_area(length: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    """
    Calculates the area of a rectangle.

    The area is measured in square units corresponding to the input units
    (e.g., square meters if length/width are in meters).
    Acreage is typically a land measurement (1 acre = 43,560 sq ft), but this
    function returns the general geometric area (length * width).

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The calculated area of the rectangle.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    return length * width

def calculate_circle_perimeter(radius: Union[int, float]) -> Union[int, float]:
    """
    Calculates the perimeter (circumference) of a circle.

    The formula used is C = 2 * pi * r.

    Args:
        radius: The radius of the circle.

    Returns:
        The calculated perimeter (circumference) of the circle.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive value.")
    # math.pi provides a highly accurate value for pi
    return 2 * math.pi * radius
