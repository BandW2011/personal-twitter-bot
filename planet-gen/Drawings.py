import Rando
from PIL import Image, ImageDraw, ImageFilter

def addStars(world, draw, WIDTH, HEIGHT):
    # 1 is pale stars, 2 is colored stars
    if world.star_type is 1:
        for x in range(0, world.star_intensity):
            draw.point((Rando.r_int(0, WIDTH), Rando.r_int(0, HEIGHT)), (
                (Rando.r_int(0xF0, 0xFF)),
                (Rando.r_int(0xF0, 0xFF)),
                (Rando.r_int(0xF0, 0xFF))))
    elif world.star_type is 2:
        for x in range(0, world.star_intensity):
            draw.point((Rando.r_int(0, WIDTH), Rando.r_int(0, HEIGHT)), (
                (Rando.r_int(0xC0, 0xFF)),
                (Rando.r_int(0xC0, 0xFF)),
                (Rando.r_int(0xC0, 0xFF))))
    return draw
