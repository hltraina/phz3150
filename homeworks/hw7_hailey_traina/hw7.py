import numpy as np
def circle(x,x0,y0,r):
    """ Takes in a radius, x final, x initial, and y initial and returns the y final value"""
    y = np.sqrt((r**2)-(x-x0)**2) + y0 
    return y

def order_array(input_array):
    """Takes an array and orders it from smallest to largest"""
    n = len(input_array) #n = length of input_array
    for i in range(n):
        for j in range(0, n-i-1):
            if input_array[j] > input_array[j+1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j] #scans the array and arranges so the smallest number appears before  a larger value (the j index plus 1)
    return input_array