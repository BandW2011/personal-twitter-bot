"""
Primary class for individual planetscape, each with its own seed
"""

import Atmosphere, Drawings, Util

from Moon import Moon
from PIL import Image, ImageDraw, ImageFilter

class World:
    def __init__(self):
        self.seed = Util.r_int(0x0, 0xFFFFFF)
        Util.seedGen(self.seed)
        self.star_type = Util.r_wchoice(["None", "Pale", "Colorful", "Uber Colorful"], [10, 10, 10, 1])
        self.star_intensity = int(Util.r_tri(0, 1500, 50))
        self.planet_color = (Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff))
        self.sun_color = (0xFF, Util.r_int(0x0, 0xFF), 0)
        self.moon_num = self.getMoonNum()
        self.sun_size = Util.r_int(5, 50)
        # temporary: will change to be based on a time variable, that affects the movement of the sun
        self.daylight = Util.r_bool()
        self.atmosphere = Atmosphere.Atmosphere(self.seed)
        self.day_sky = self.atmosphere.day_sky
        self.night_sky = self.atmosphere.night_sky

        self.moons = []
        for i in range(0, self.moon_num):
            m = Moon()
            print("Moons: " + str(len(self.moons)))
            self.moons.append(m)

        print("THERE ARE " + str(len(self.moons)) + " MOONS")

    def toString(self):
        string = "World " + str(self.seed)
        string += "\nAir density: " + str(int(self.atmosphere.air_density * 100)) + "%"
        string += "\nDaylight: " + str(self.daylight)
        string += "\nDay sky color: " + str(self.day_sky)
        string += "\nNight sky color: " + str(self.night_sky)
        string += "\nStar type: " + str(self.star_type)
        string += "\nStar intensity: " + str(self.star_intensity)
        string += "\nPlanet color: " + str(self.planet_color)
        string += "\nSun color: " + str(self.sun_color)
        string += "\nSun size: " + str(self.sun_size)
        string += "\nNumber of moons: " + str(self.moon_num)
        return string

    def createImage(self, WIDTH, HEIGHT):
        try:
            print(self.toString())

            im = Image.new("RGB", (WIDTH, HEIGHT))
            draw = ImageDraw.Draw(im)

            draw = Drawings.addSky(self, draw, WIDTH, HEIGHT)
            draw = Drawings.addStars(self, draw, WIDTH, HEIGHT)
            draw = Drawings.addSun(self, draw, WIDTH, HEIGHT)
            for moon in self.moons:
                draw = Drawings.addMoon(self, draw, WIDTH, HEIGHT, moon)
            draw = Drawings.addPlanet(self, draw, WIDTH, HEIGHT)
            draw = Drawings.addDebug(self, draw, WIDTH, HEIGHT) # pass as argument instead

            im = im.resize((WIDTH * 4, HEIGHT * 4))
            im.save(str(self.seed) + ".png", "PNG")
        except IOError:
            print("Cannot create image!")

    def getMoonNum(self):
        return Util.r_wchoice((0, 1, 2, 3, 4, 5, 6, 7, 8), (64, 32, 16, 8, 4, 2, 1, 1, 1))
