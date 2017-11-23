import Rando

class World:
    seed = 0
    day_sky = 0x0
    night_sky = 0x0
    star_intensity = 0
    star_type = 0

    def __init__(self):
        self.seed = Rando.r_int(0, 9999999)
        Rando.seedGen(self.seed)
        self.star_intensity = 100
        self.star_type = Rando.r_int(0, 2)

        while True:
            temp_a = Rando.r_int(0x0, 0xff)
            temp_b = Rando.r_int(0x0, 0xff)
            temp_c = Rando.r_int(0x0, 0xff)
            if not (temp_a > 0x60 and temp_b > 0x60 and temp_c > 0x60):
                self.day_sky = (temp_a, temp_b, temp_c)
                break
        while True:
            temp_a = Rando.r_int(0x0, 0xff)
            temp_b = Rando.r_int(0x0, 0xff)
            temp_c = Rando.r_int(0x0, 0xff)
            if temp_a > 0x50 or temp_b > 0x50 or temp_c > 0x50:
                self.night_sky = (temp_a, temp_b, temp_c)
                break

    def toString(self):
        return "World " + str(self.seed) + "\nSky colors: " + str(self.day_sky) + ", " + str(self.night_sky) + "\nStar type: " + str(self.star_type) + ", Star intensity: " + str(self.star_intensity)


