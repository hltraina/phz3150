def displacement(v0, t, a):
    """Calculates the total displacement of a body during a time of t, an initial speed v0, and constant acceleration a"""
    x = v0 * t + (0.5)* a * t**2
    """t is the total time the object moves, a is constant acceleration, and v0 is the initial speed of the body"""
    return x