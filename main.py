def move_zeros(lst):
    # Count the number of zeros in the array
    num_zeros = lst.count(0)
    
    # Remove all zeros from the array
    lst = [i for i in lst if i != 0]
    
    # Append the appropriate number of zeros to the end of the array
    lst += [0] * num_zeros
    
    return lst
