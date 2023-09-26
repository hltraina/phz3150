import numpy as np

def my_apprx_of_e(x):
    y = np.exp(x)
    y2 = 1 + x + x^2/2
    
    return [y, y2]
