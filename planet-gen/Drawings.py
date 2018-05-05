"""
Code responsible for rendering each planetscape
"""

import Util

from PIL import Image, ImageDraw, ImageFilter

def addSky(world, draw, WIDTH, HEIGHT):
    if world.daylight == False:
        draw.rectangle(((0, 0), (WIDTH, HEIGHT)), world.night_sky, None)
    else:
        draw.rectangle(((0, 0), (WIDTH, HEIGHT)), world.day_sky, None)
    return draw

def addStars(world, draw, WIDTH, HEIGHT):
    if world.star_type is "Pale":
        for x in range(0, world.star_intensity):
            draw.point((Util.r_int(0, WIDTH), Util.r_int(0, HEIGHT)), (
                Util.r_int(0xF0, 0xFF),
                Util.r_int(0xF0, 0xFF),
                Util.r_int(0xF0, 0xFF),
                Util.r_int(0x00, int(world.atmosphere.get_satellite_luminence() * 0xFF))))
    elif world.star_type is "Colorful":
        for x in range(0, world.star_intensity):
            draw.point((Util.r_int(0, WIDTH), Util.r_int(0, HEIGHT)), (
                Util.r_int(0xB0, 0xFF),
                Util.r_int(0xB0, 0xFF),
                Util.r_int(0xB0, 0xFF),
                Util.r_int(0x00, int(world.atmosphere.get_satellite_luminence() * 0xFF))))
    elif world.star_type is "Uber Colorful":
        for x in range(0, world.star_intensity):
            draw.point((Util.r_int(0, WIDTH), Util.r_int(0, HEIGHT)), (
                Util.r_int(0x7F, 0xFF),
                Util.r_int(0x7F, 0xFF),
                Util.r_int(0x7F, 0xFF),
                Util.r_int(0x00, int(world.atmosphere.get_satellite_luminence() * 0xFF))))
    return draw

def addSun(world, draw, WIDTH, HEIGHT):
    sky_color = 0x0
    pos = (Util.r_int(0, WIDTH), Util.r_int(0, HEIGHT))
    if world.daylight == False:
        return draw
    else:
        sky_color = world.day_sky
    outline = world.sun_color
    if Util.color_distance(world.sun_color, sky_color) < 10:
        outline = (outline[0] + 0xF, outline[1] + 0xF, outline[2] + 0xF)
    draw.ellipse(((pos[0], pos[1]), (pos[0] + world.sun_size, pos[1] + world.sun_size)), world.sun_color, outline)
    return draw

def addMoon(world, draw, WIDTH, HEIGHT, moon):
    sky_color = 0x0
    if world.daylight == False:
        sky_color = world.night_sky
    else:
        sky_color = world.day_sky
    pos = (Util.r_int(0, WIDTH), Util.r_int(0, HEIGHT))
    outline = moon.color
    if Util.color_distance(moon.color, sky_color) < 10:
        outline = (outline[0] + 0xF, outline[1] + 0xF, outline[2] + 0xF)
    draw.ellipse(((pos[0], pos[1]), (pos[0] + moon.radius, pos[1] + moon.radius)), moon.color, outline)
    return draw

def addPlanet(world, draw, WIDTH, HEIGHT):
    sky_color = 0x0
    outline = world.planet_color
    offset = Util.r_int(0, WIDTH * 2)
    if world.daylight == False:
        sky_color = world.night_sky
    else:
        sky_color = world.day_sky
    if Util.color_distance(world.planet_color, sky_color) < 10:
        outline = (outline[0] + 0xF, outline[1] + 0xF, outline[2] + 0xF)
    draw.ellipse(((-3 * WIDTH + offset, HEIGHT * 0.8), (3 * WIDTH, HEIGHT * 2)), world.planet_color, outline)
    return draw

def addDebug(world, draw, WIDTH, HEIGHT):
    draw.multiline_text((0, 0), world.toString(), 0xFFFFFF)
    return draw
