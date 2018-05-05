"""
Primary class for individual planetscape, each with its own seed
"""

import Atmosphere, Drawings, io, json, os, Util

from Moon import Moon
from PIL import Image, ImageDraw, ImageFilter

class World:
    def __init__(self):
        if os.path.isfile("./default_config.json") and os.access("./default_config.json", os.R_OK):
            with io.open("./default_config.json", 'r') as json_file:
                json_data = json.load(json_file)
                print(json_data)

                if json_data["use_seed"] is True:
                    self.seed = json_data["seed"]
                else:
                    self.seed = Util.r_int(0x0, 0xFFFFFF)
                Util.seedGen(self.seed)

                self.star_type = Util.r_wchoice(["None", "Pale", "Colorful", "Uber Colorful"],
                        json_data["star_type_weights"])

                self.star_intensity = int(Util.r_tri(
                    json_data["minimum_star_intensity"],
                    json_data["maximum_star_intensity"],
                    json_data["median_star_intensity"]))

                self.planet_color = (
                    Util.r_int(json_data["planet_color"]["minimum_r"], json_data["planet_color"]["maximum_r"]),
                    Util.r_int(json_data["planet_color"]["minimum_g"], json_data["planet_color"]["maximum_g"]),
                    Util.r_int(json_data["planet_color"]["minimum_b"], json_data["planet_color"]["maximum_b"]))

                self.sun_color = (
                    Util.r_int(json_data["sun_color"]["minimum_r"], json_data["sun_color"]["maximum_r"]),
                    Util.r_int(json_data["sun_color"]["minimum_g"], json_data["sun_color"]["maximum_g"]),
                    Util.r_int(json_data["sun_color"]["minimum_b"], json_data["sun_color"]["maximum_b"]))

                self.moon_num = Util.r_wchoice(
                        json_data["moon_num_weights"]["moon_num"],
                        json_data["moon_num_weights"]["moon_probability"])

                self.sun_size = Util.r_int(
                        json_data["sun_size"]["minimum_size"],
                        json_data["sun_size"]["maximum_size"])

                # temporary: will change to be based on a time variable, that affects the movement of the sun
                if json_data["use_daylight"]:
                    self.daylight = json_data["daylight"]
                else:
                    self.daylight = Util.r_bool()
        """
        else:
            with io.open("./config.json", 'w') as json_file:
                json_file.write(json.dumps({}))
        """

        self.atmosphere = Atmosphere.Atmosphere(self.seed)
        self.day_sky = self.atmosphere.day_sky
        self.night_sky = self.atmosphere.night_sky

        self.moons = []
        for i in range(0, self.moon_num):
            m = Moon()
            self.moons.append(m)


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
