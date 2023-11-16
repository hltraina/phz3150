import numpy as np

def triathlon_time(sports,athletes_times):
    """Based on the data given from the array, this function will output which athlete will place in first and last place based on their times listed"""
    hours = athletes_times[:, 1:] / sports
    total_times = np.sum(hours, axis = 1)

    # Find the index of the participant who finishes first
    first_index = np.argmin(total_times)

    # Find the index of the participant who finishes last
    last_index = np.argmax(total_times)

    # Get the participant names and expected times
    winner = athletes_times[first_index, 0]
    winner_time = total_times[first_index] * 3600
    
    last_place = athletes_times[last_index, 0]
    last_place_time = total_times[last_index] * 3600
    
    print(f"The winner is Participant {winner} with an expected time of {winner_time:.2f} hours.")
    print(f"The last participant is Participant {last_place} with an expected time of {last_place_time:.2f} hours.")
    
def triathlon_time_dict(sports, athletes_times):
    """Uses dictionary to print the first and last finisher, with their names and average times"""
    
    sports_array = np.array(list(sports.values()))
    
    #for debugging:
   #print(sports_array)
    
    total_distances = {
        athlete: np.sum(np.array(speeds) / sports_array) for athlete, speeds in athletes_times.items()
    }
    #for debugging:
    #rint(total_distances)
   
    # Find the first and last participants
    fastest_athlete = min(total_distances, key=total_distances.get)
    slowest_athlete = max(total_distances, key=total_distances.get)

    # Calculate the time each participant will take
    fastest_time = total_distances[fastest_athlete] *3600  # Convert to hours
    slowest_time = total_distances[slowest_athlete] *3600  

    print(f"The winner is {fastest_athlete} with an expected time of {fastest_time:.2f} hours.")
    print(f"The last participant is {slowest_athlete} with an expected time of {slowest_time:.2f} hours.")

def my_circuit(configuration, num_resistors, resistances, value):
    """takes either a series or parallel configuration, the number of resistors, an array with individual resistances, and the volatage or amperage of the circuit. Uses the data to determine the total resistance and the total voltage/amperage"""
    
    if configuration.lower() == 'series':
        total_resistance = np.sum(resistances)
        total_value = value
    elif configuration.lower() == 'parallel':
        total_resistance = 1 / np.sum(1 / resistances)
        total_value = value
    else:
        print("Invalid input. Please indicate if a 'series' or 'parallel' configuration")

    return total_resistance, total_value

def piston(V, P0, V0, T0, gamma): 
    """Takes in the array of volumes, initial pressure, initial volume, initial temperature, and ratio of heat capacities (gamma) and returns the array of shape containing the Pressure, Volume and Temperature Values"""
    R = 8.314
    P = P0 * (V0/V)**(gamma-1)
    T = T0 * (V0/V)**(gamma-1)
    result = np.column_stack((P, V, T))
    return result