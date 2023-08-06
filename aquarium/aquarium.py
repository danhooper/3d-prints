#!/usr/bin/env python3
from solid2 import *

total_height = 150
top_piece_width = 3
light_width = 67
width = light_width + top_piece_width * 2 + 1
depth = 10

tank_overhang = 30

lip_total_height = 12

hole_offset_1 = width / 3
hole_offset_2 = width / 3 * 2

lip_width_1 = 18
lip_width_2 = 10
total_lip_width = lip_width_1 + lip_width_2

second_piece_offset_z = 30
second_piece_height = 15
# move bottom right piece up closer to the aquarium lip
second_piece_adjustment = 5
second_piece_adjustment_2 = 5

glass_thickness = 5
# not sure why but make the right piece's bottom a little less deep
second_piece_depth_adjustment = 6
cylinder_height_offset = 100

cylinder_base = cylinder(r=3.5, h=depth).rotateY(90)


def get_cyclinder_base(cylinder_depth):
    return cylinder(r=3.5, h=cylinder_depth).rotateY(90)


def left_piece():
    main_piece = cube([depth, width, total_height])

    light_side_right = cube([depth, top_piece_width, 10]).up(total_height)
    light_side_left = light_side_right.forward(width - top_piece_width)

    lip_piece = cube([total_lip_width, width, second_piece_height]).up(
        second_piece_offset_z).right(depth)

    first_cylinder = get_cyclinder_base(depth).forward(
        hole_offset_1).up(cylinder_height_offset)

    second_cylinder = get_cyclinder_base(depth).forward(
        hole_offset_2).up(cylinder_height_offset)

    return difference()(
        union()(
            main_piece, lip_piece, light_side_right, light_side_left
        ),
        first_cylinder,
        second_cylinder
    )


def right_piece():
    main_piece = cube(
        [depth, width, second_piece_offset_z + second_piece_height + depth - second_piece_adjustment - second_piece_adjustment_2]).up(second_piece_adjustment + second_piece_adjustment_2)

    bottom_piece = cube([total_lip_width - glass_thickness - second_piece_depth_adjustment, width,
                        second_piece_height - second_piece_adjustment]).right(depth).up(second_piece_adjustment + second_piece_adjustment_2)

    top_large_piece_height = total_height - \
        second_piece_offset_z - second_piece_height

    top_large_piece = cube([total_lip_width, width, top_large_piece_height])

    top_reducer_height = top_large_piece_height - depth

    top_reducer = cube(
        [total_lip_width, width, top_reducer_height]).left(10).up(10)
    # .up(
    #     second_piece_offset_z + second_piece_height + 10)

    first_cylinder = get_cyclinder_base(depth + total_lip_width).forward(
        hole_offset_1).up(cylinder_height_offset)

    second_cylinder = get_cyclinder_base(depth + total_lip_width).forward(
        hole_offset_2).up(cylinder_height_offset)

    return difference()(
        union()(
            main_piece, bottom_piece,
            difference()(
                top_large_piece,
                top_reducer
            ).up(
                second_piece_offset_z + second_piece_height).right(depth),
        ),
        first_cylinder,
        second_cylinder
    )


if __name__ == "__main__":
    (
        left_piece() +
        right_piece().rotateZ(180).forward(width).right(80)
    ).save_as_scad('debug.scad')

    left_piece().rotateY(-90).save_as_scad('left_piece.scad')
    right_piece().rotateY(90).save_as_scad('right_piece.scad')
    print("Created scad files")
