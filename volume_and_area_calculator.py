
from math import pi
print('calculate the area and volume of commen shape')
type_of_shapes = input(
 ' do you want to calculate 3D(volume) or 2D shapes(areas) : ').lower()

shapes = ['1_square', '2_circle', '3_rectangle', '4_triangle']

c_shapes = ['1_cube', '2_cuboid', '3_cylinder', '4_sphere ']


def calculate_cube_area():
    volume = side**3
    return volume


def calculate_cubiod_area():
    volume = length * base * height
    return volume


def calculate_cylinder_area():
    volume = pi*(raduis**2)*height
    return volume


def calculate_sphere_area():
    volume = (4*pi*raduis**3)/3
    return volume


def calculate_square_area():
    area = side**2
    return area


def calculate_rectangle_area():
    area = width * height
    return area


def calculate_triangle_area():
    area = (height * base)/2
    return area


def calculate_circle_area():
    area = pi*(raduis**2)
    return area


while type_of_shapes == '2d':
    print('if you want to change the type of shapes enter any number > 4')
    print(shapes)
    shape_type = int(
        input('the type of shape you want to calculate it area (1-4) : '))

    if shape_type == 4:
        height = int(input(' height : '))
        base = int(input(' base : '))
        result = calculate_triangle_area()
        print(' A  =', result)

    elif shape_type == 1:
        side = int(input(' side : '))
        result = calculate_square_area()
        print(' A  =', result)

    elif shape_type == 3:
        height = int(input(' height : '))
        width = int(input(' width : '))
        result = calculate_rectangle_area()
        print(' A  =', result)

    elif shape_type == 2:
        raduis = int(input(' raduis : '))
        result = calculate_circle_area()
        print(' A  =', result)
    else:
        ss = input('do you want to change the type of shape (y/n) : ')
        if ss == 'y' or ss == 'yes':
            break
while type_of_shapes == '3d':
    print(c_shapes)
    ch_shape = int(input(' enter a number 1-4  : '))

    if ch_shape == 1:
        side = int(input(' base : '))
        result = calculate_cube_area()
        print(' V : ', result)

    elif ch_shape == 2:
        base = int(input(' base : '))
        height = int(input(' height : '))
        length = int(input(' length : '))
        result = calculate_cubiod_area()
        print(' V : ', result)

    elif ch_shape == 3:
        raduis = int(input('reduis :  '))
        height = int(input(' height :  '))

        result = calculate_cylinder_area()
        print(' V : ', result)

    elif ch_shape == 4:
        raduis = int(input(' reduis :  '))
        result = calculate_sphere_area()
        print(' V : ', result)

    else:
        ss = input('do you want to change the type of shape (y/n) : ')
        if ss == 'y' or ss == 'yes':
            break
