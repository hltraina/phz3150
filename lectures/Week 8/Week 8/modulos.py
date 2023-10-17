def modulos_ten( input_list ):
    """Function that takes as input a list and returns a new list 
    with only the elements that are perfectly divisible by 10.
    Input: random list
    Output: list with elements of random list for which element%10 = 0 . """
    
    
    output_list = [ ]
    
    for num in input_list:
        if num % 10 == 0:
            output_list.append( num )
            
            
            
   ### or
   ## for n in range( len( input_list ) ):
   ##      if input_list[ n ] % 10 == 0:
   ##.         output_list.append( input_list[ n ] )
    
    return output_list 