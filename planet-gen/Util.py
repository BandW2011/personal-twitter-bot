"""
Holds general purpose math functions
"""

import random

def r_int(inc_begin, inc_end):
    return random.randint(inc_begin, inc_end)

def r_flo(inc_begin, inc_end):
    return random.uniform(inc_begin, inc_end)

def r_bool():
    return bool(random.getrandbits(1))

def r_tri(inc_begin, inc_end, median):
    return random.triangular(inc_begin, inc_end, median)

def seedGen(new_seed):
    random.seed(new_seed)

def color_distance(color_a, color_b):
    R = (color_b[0] - color_a[0]) * 2
    G = (color_b[1] - color_a[1]) * 2
    B = (color_b[2] - color_a[2]) * 2
    return ((R + G + B) ** 0.5).real
