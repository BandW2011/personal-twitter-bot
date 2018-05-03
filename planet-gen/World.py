import Atmosphere, Drawings, Util
from PIL import Image, ImageDraw, ImageFilter

class World:
    seed = 0
    atmosphere = 0
    # temporary: will change to be based on a time variable, that affects the movement of the sun
    daylight = False
    star_type = 0
    star_intensity = 0
    planet_color = 0x0
    sun_color = 0x0
    sun_size = 0
    moon_num = 0
    moons = []

    def __init__(self):
        self.seed = Util.r_int(0x0, 0xFFFFFF)
        Util.seedGen(self.seed)
        self.star_type = Util.r_int(0, 2)
        self.star_intensity = int(Util.r_tri(0, 1500, 50))
        self.planet_color = (Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff))
        self.sun_color = (0xFF, Util.r_int(0x0, 0xFF), 0)
        self.moon_num = self.getMoonNum()
        self.sun_size = Util.r_int(5, 50)
        self.daylight = Util.r_bool()
        self.atmosphere = Atmosphere.Atmosphere(self.seed)
        self.day_sky = self.atmosphere.day_sky
        self.night_sky = self.atmosphere.night_sky

        for i in range(0, self.moon_num):
            self.moons.append(((Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff)), Util.r_int(5, 50)))

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
            draw = Drawings.addDebug(self, draw, WIDTH, HEIGHT)

            im = im.resize((WIDTH * 4, HEIGHT * 4))
            im.save(str(self.seed) + ".png", "PNG")
        except IOError:
            print("Cannot create image!")

    def getMoonNum(self):
        # make more neat at some point
        F = Util.r_flo(0, 1)
        if F < 64 / 319:
            return 0
        elif F < 192 / 319:
            return 1
        elif F < 256 / 319:
            return 2
        elif F < 288 / 319:
            return 3
        elif F < 304 / 319:
            return 4
        elif F < 312 / 319:
            return 5
        elif F < 316 / 319:
            return 6
        elif F < 318 / 319:
            return 7
        else:
            return 8
