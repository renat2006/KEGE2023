print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (not (x or y) or (y and w)) == (not (not (y and z) or (w or x)))
                if f:
                    print(x, y, z, w)
