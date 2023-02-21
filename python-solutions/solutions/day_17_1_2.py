"""
    ####

    .#.
    ###
    .#.

    ..#
    ..#
    ###

    #
    #
    #
    #

    ##
    ##
"""
rocks = {
    0: (4, 1),
    1: (3, 3),
    2: (3, 3),
    3: (1, 4),
    4: (2, 2)
}

movements = {
    "<": -1,
    ">": 1
}

with open("../../input/input_17_test.txt") as fp:
    JETS = list(fp.read())[:-1]
top_surface = set({(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)})


class Rock:
    __slots__ = ("t", "x", "y")

    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y


def heighest_top():
    return max([y for x, y in top_surface])


def get_next_horizontal_projectile(rock, movement):
    if rock.t == 0:
        return [(rock.x+movement+i, rock.y) for i in range(4)]
    elif rock.t == 1:
        if movement == -1:
            return [(rock.x-1, rock.y+1), (rock.x, rock.y), (rock.x, rock.y+2)]
        else:
            return [(rock.x+3, rock.y+1), (rock.x+2, rock.y), (rock.x+2, rock.y+2)]
    elif rock.t == 2:
        if movement == -1:
            return [(rock.x-1, rock.y), (rock.x+1, rock.y+1), (rock.x+1, rock.y+2)]
        else:
            return [(rock.x+3, rock.y), (rock.x+3, rock.y+1), (rock.x+3, rock.y+2)]
    elif rock.t == 3:
        return [(rock.x+movement, rock.y+i) for i in range(4)]
    elif rock.t == 4:
        if movement == -1:
            return [(rock.x-1, rock.y), (rock.x-1, rock.y+1)]
        else:
            return [(rock.x+2, rock.y), (rock.x+2, rock.y+1)]


def get_next_vertical_projectile(rock):
    if rock.t == 0:
        return [(rock.x+i, rock.y-1) for i in range(4)]
    elif rock.t == 1:
        return [(rock.x, rock.y), (rock.x+1, rock.y+1), (rock.x+2, rock.y)]
    elif rock.t == 2:
        return [(rock.x+i, rock.y-1) for i in range(3)]
    elif rock.t == 3:
        return [(rock.x, rock.y-1)]
    elif rock.t == 4:
        return [(rock.x, rock.y-1), (rock.x+1, rock.y-1)]


def can_move_horiozontally(rock, movement):
    if rock.x + movement >= 0 and rock.x + movement + rocks[rock.t][0] <= 6:
        for p in get_next_horizontal_projectile(rock, movement):
            if p in top_surface:
                return False
        return True
    return False


def get_vertical_collusion(rock):
    for p in get_next_vertical_projectile(rock):
        if p in top_surface:
            return (p.x, p.y+1)


def settle_rock_on_surface(rock, c):
    if rock.t == 0:
        for i in range(4):
            top_surface.add((rock.x+i, c[2]))
    # elif rock.t == 1:


def jet_generator():
    for j in JETS:
        yield j


jg = jet_generator()
generate_new_rock = False
r = Rock(0, 2, 4)
cnt = 1
while True:
    try:
        if (generate_new_rock):
            n = r.t + 1
            if n >= 5:
                n -= 5
            mx = heighest_top(top_surface)
            r = Rock(n, 2, mx + 4)
            cnt += 1
            if cnt == 3:
                break
            generate_new_rock = False
        else:
            j = next(jg)
            if can_move_horiozontally(r, movements[j]):
                r.x += movements[j]
            if (c := get_vertical_collusion(r)):
                settle_rock_on_surface(r, top_surface, c)
                print(top_surface)
                generate_new_rock = True
            else:
                r.y -= 1

    except StopIteration:
        jg = jet_generator()
        continue
