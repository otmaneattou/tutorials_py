

def closest_to_zero(ints):
    if ints is None or len(ints) == 0:
        return 0
    closest = ints[0]
    for i in range(1, len(ints)):
        if abs(ints[i]) < abs(closest):
            closest = ints[i]
        if abs(ints[i]) == abs(closest) and ints[i] >= 0 or closest >= 0:
            closest = abs(closest)
    return closest


if __name__ == "__main__":
    ints = None
    print("Closest", closest_to_zero(ints))
