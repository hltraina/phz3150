def kepler_3rd(period): 
    """Calculates the orbital distance of a planet to Sun based on the orbital period using Kepler's third law. Takes in the oribital period of planet in years and returns the orbital distance."""
    #reference points!
    Earth_period = 365.25
    Earth_distance = 1.0
    distance = Earth_distance * (period**2/Earth_period**2) **(1/3)
    return distance
    