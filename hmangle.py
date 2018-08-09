def hmangle(h, m):
    mangle = m * 6
    hangle = (h + m/60) * 30
    if mangle < hangle:
        result = hangle - mangle
    else:
        result = mangle - hangle

    if result > 180:
        result = 360 - result

    return result

print (hmangle(3, 15))
