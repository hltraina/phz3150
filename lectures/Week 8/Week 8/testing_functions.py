def student_grades( grades ):
    """important info here...
    Input: dictionary
    Output: print statements"""
    
    for key in grades:
        if grades[ key ] > 0.9:
            print( key, 'got an A' )
        elif grades[ key ] < 0.8:
            print( key, 'got a C' )
        else:
            print( key, 'got a B' )
            
            
def three_arrays( a,b,c):
    """informative docstring"""
    
#    mask = np.where( b > 0)
    d = a[ b > 0] + c[ b > 0]
    
    return d