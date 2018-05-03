"""
Manages day and night sky color, air density (translucence), and luminence (brightness of cele. bodies)
"""

import Util

class Atmosphere:
    def __init__(self, seed):
        Util.seedGen(seed)
        self.air_density = Util.r_flo(0, 1)

        while True:
            temp_r = Util.r_int(0x0, 0xff)
            temp_g = Util.r_int(0x0, 0xff)
            temp_b = Util.r_int(0x0, 0xff)
            if not (temp_r > 0x60 and temp_g > 0x60 and temp_b > 0x60):
                self.day_sky = (
                    int(temp_r * self.air_density),
                    int(temp_g * self.air_density),
                    int(temp_b * self.air_density)
                )
                break

        while True:
            temp_r = Util.r_int(0x0, 0xff)
            temp_g = Util.r_int(0x0, 0xff)
            temp_b = Util.r_int(0x0, 0xff)
            if temp_r <= 0x50 and temp_g <= 0x50 and temp_b <= 0x50:
                self.night_sky = (
                    int(temp_r * self.air_density),
                    int(temp_g * self.air_density),
                    int(temp_b * self.air_density)
                )
                break

    def get_satellite_luminence(self):
        luminence = -2 * (self.air_density) + 1
        if luminence < 0: return 0
        else: return luminence

    def toString(self):
        string += "Day sky color: " + str(self.day_sky)
        string += "\nNight sky color: " + str(self.night_sky)
        string += "\nAir density: " + str(int(air_density * 100)) + "%"
        return string
