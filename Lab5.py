# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    row = 0
    
    while row < n:
        if row == 0 or row == n - 1:
            result += "*" * n
        else:
            result += "*" + " " * (n - 2) + "*"
        
        if row < n - 1:
            result += "\n"
        
        row += 1
    
    return result

 
            

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    row = 1
    
    while row <= n:
        col = 1
        while col <= row:
            result += str(col)
            col += 1
        
        if row < n:
            result += "\n"
        
        row += 1
    
    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0

    while n > 0:
        total += n 
        n-= 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    row = 1
    
    while row <= n:
        spaces = n - row
        stars = 2 * row - 1
        
        result += " " * spaces + "*" * stars
        
        if row < n:
            result += "\n"
        
        row += 1
    
    return result
