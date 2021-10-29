"""
    Author: Lori White
    Purpose: Showing how to use functions in python.
"""
# Functions with arguments and a return
def area_triangle(base, height):
    """
     Gets the area of a triangle based on the base and height.
    """
    return 0.5 * base * height

def area_rectangle(base, height):
    """
     Gets the area of a rectangle based on the base and height.
    """
    return base * height

def perimeter(sides):
    """
     Gets the perimeter of the shape based on the sides.
    """
    convert_list_of_strings_to_list_of_floats(sides)
    return sum(sides)

def generate_sides_ex(num_sides):
    """
     Gets an example of how the user should input the sides of their shape.
    """
    return ",".join([str(x) for x in range(1, num_sides + 1)])

# Functions with arguments and no return
def convert_list_of_strings_to_list_of_floats(the_list):
    """
     Converts a list of strings into a list of floats.
    """
    for i in range(0, len(the_list)):
        the_list[i] = float(the_list[i])

# Functions with no arguments and a return
def get_string_of_shape():
    """
     Gets a the user's chosen shape.
    """
    str_shape = ""
    if shape.upper() == "T":
        str_shape = "Triangle"
    else:
        str_shape = "Rectangle"
    return str_shape

# Functions with no arguments and no return
def prompt_area():
    """
     Prompts the user for the base and height of their shape and then calculates the area.
    """
    str_shape = get_string_of_shape()
    base = float(input(f"What is the base of your {str_shape}? "))
    height = float(input(f"What is the height of your {str_shape}? "))
    if shape.upper() == "T":
        area = area_triangle(base, height)
    else:
        area = area_rectangle(base, height)
    print(f"Your {str_shape} has a base of {base} {units}, height of {height} {units}, and an area of {area} {units}.")

def prompt_perimeter():
    """
     Prompts the user for the sides of their shape and then calculates the perimeter.
    """
    str_shape = get_string_of_shape()
    ex = ""
    if shape.upper() == "T":
        ex = generate_sides_ex(3)
    else:
        ex = generate_sides_ex(4)
    sides = input(f"What are the lengths of each side? (Separate ecah length with a ',' like {ex}) ").split(",")
    per = perimeter(sides)
    print(f"Your {str_shape}'s perimeter is {per} {units}.")

# Main program
units = input("What units will you be using? ")
option = input("Do you want to find the area or the perimeter of your shape? (Type A or P) ")
shape = input("What shape do you have? (Type T (Triangle) or R (Rectangle)) ")

if option.upper() == "A":
    prompt_area()
else:
    prompt_perimeter()