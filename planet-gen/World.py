import Util

class World:
    seed = 0
    day_sky = 0x0
    night_sky = 0x0
    # temporary: will change to be based on a time variable, that affects the movement of the sun
    daylight = False
    star_intensity = 0
    star_type = 0
    planet_color = 0x0

    def __init__(self):
        self.seed = Util.r_int(0x0, 0xFFFFFF)
        Util.seedGen(self.seed)
        self.star_intensity = 100
        self.star_type = Util.r_int(0, 2)
        self.planet_color = (Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff), Util.r_int(0x0, 0xff))

        if Util.r_int(0, 1) == 1:
            self.daylight = True

        while True:
            temp_a = Util.r_int(0x0, 0xff)
            temp_b = Util.r_int(0x0, 0xff)
            temp_c = Util.r_int(0x0, 0xff)
            if not (temp_a > 0x60 and temp_b > 0x60 and temp_c > 0x60):
                self.day_sky = (temp_a, temp_b, temp_c)
                break
        while True:
            temp_a = Util.r_int(0x0, 0xff)
            temp_b = Util.r_int(0x0, 0xff)
            temp_c = Util.r_int(0x0, 0xff)
            if temp_a <= 0x50 and temp_b <= 0x50 and temp_c <= 0x50:
                self.night_sky = (temp_a, temp_b, temp_c)
                break
            
    def toString(self):
        string = "World " + str(self.seed)
        string += "\nDay sky color: " + str(self.day_sky)
        string += "\nNight sky color: " + str(self.night_sky)
        string += "\nStar type: " + str(self.star_type)
        string += "\nStar intensity: " + str(self.star_intensity)
        string += "\nPlanet color: " + str(self.planet_color)
        string += "\nDaylight: " + str(self.daylight)
        return string
