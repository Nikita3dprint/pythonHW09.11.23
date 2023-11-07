for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (x == y) and (not y or not z) and (z or w):
                    print(x, y, z, w)
                    