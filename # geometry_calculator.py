# geometry_calculator.py

import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def sphere_surface_area(radius):
    return 4 * math.pi * radius**2

def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2

# Example usage
print(sphere_volume(5)) # Output: 523.5987755982989
print(cylinder_surface_area(3, 10)) # Output: 188.4955592153876
