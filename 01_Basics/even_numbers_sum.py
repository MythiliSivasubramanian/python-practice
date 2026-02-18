# Sum only even numbers in a list

def sum_even_numbers(nums):
    # Totals the even numbers
    total = 0  
    
    for n in nums:
        # To check if the number is even 
        if n % 2 == 0:   
            total += n
    return total
    
# Test the function with input as a list [1,2,3,4,5,6]
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
