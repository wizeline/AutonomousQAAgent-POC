
from typing import Union

from utils.geometric import calculate_circle_perimeter, calculate_rectangle_area


def calculate_cylinder_lateral_area(radius: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    """
    Calculates the outer lateral (side) surface area of a cylinder.

    This function determines the area of the curved surface, equivalent to the
    outer lateral area of the previous hollow cylinder function.
    It uses the formula: Area = Circumference * Height.
    The function uses 'calculate_circle_perimeter' and 'calculate_rectangle_area'.

    Args:
        radius: The radius of the cylinder's base.
        height: The height of the cylinder.

    Returns:
        The calculated lateral surface area (outer wall only).
    """
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive values.")

    # 1. Calculate the circumference (perimeter) using the existing function.
    perimeter = calculate_circle_perimeter(radius)

    # 2. Calculate the lateral area using the existing function (Perimeter * Height).
    # This uses calculate_rectangle_area as a general multiplication function.
    lateral_area = calculate_rectangle_area(perimeter, height)

    # 3. Return the outer lateral area.
    return lateral_area
