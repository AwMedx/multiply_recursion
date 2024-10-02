def multiply(x, y):
    if x == 0 or y == 0: # If any # is 0, you can't multiply by 0, also ends recursion
        return 0
    
    if x > 0 and y > 0: # If both are positive
        return x + multiply(x, y-1) # Normal Multiplication Summing for Pos. Numbers
        
    elif x > 0 and y > 0: # If both # are negative
        return -x + multiply(-x, y-1)
        
    else: # If only 1 # is negative
        return -x + multiply(x, y+1)
    
x = multiply(-2, -4)

print(x)
