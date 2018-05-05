"""
Moon class, containing outline and body color
"""

import Util

class Moon:
    def __init__(self):
        # make seed-friendly
        self.color = (Util.r_int(0x0, 0xFF), Util.r_int(0x0, 0xFF), Util.r_int(0x00, 0xFF))
        self.radius = Util.r_int(5, 50)
