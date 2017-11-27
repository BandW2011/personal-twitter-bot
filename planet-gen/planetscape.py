#!/usr/bin/python3
import datetime, hashlib, noise, random
import Drawings, Util, World
from PIL import Image, ImageDraw, ImageFilter

WIDTH  = 720 // 4
HEIGHT = 1280 // 4

def createImage():
    try:
        world = World.World()

        print(world.toString())

        im = Image.new("RGB", (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(im)

        draw = Drawings.addSky(world, draw, WIDTH, HEIGHT)
        draw = Drawings.addStars(world, draw, WIDTH, HEIGHT)
        draw = Drawings.addPlanet(world, draw, WIDTH, HEIGHT)
        # draw = Drawings.addDebug(world, draw, WIDTH, HEIGHT)

        im = im.resize((WIDTH * 4, HEIGHT * 4))
        im.save(str(world.seed) + ".png", "PNG")
    except IOError:
        print("Cannot create image!")

createImage()
