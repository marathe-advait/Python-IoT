import random

def rand_coor():
    pat_coor = [];
    loc_coor = [];
    loc_coor.append(random.uniform(8.06667, 37.10000))
    loc_coor.append(random.uniform(68.11667, 97.41667))
    pat_coor.append(loc_coor[0] + random.uniform(-2.500, 2.500))
    pat_coor.append(loc_coor[1] + random.uniform(-2.500, 2.500))
    return tuple(loc_coor), tuple(pat_coor)
