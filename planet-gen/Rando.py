import random

def r_int(inc_begin, inc_end):
    return random.randint(inc_begin, inc_end)

def seedGen(new_seed):
    random.seed(new_seed)
