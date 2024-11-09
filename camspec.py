import re

def extract_integers(expression):
    # Use regex to find all integers in the string
    numbers = re.findall(r'\d+', expression)
    
    # Convert them to integers
    numbers = [int(num) for num in numbers]
    
    # Ensure there are exactly 5 integers, filling with 0 if needed
    while len(numbers) < 5:
        numbers.append(0)
    
    # If there are more than 5, we just take the first 5
    numbers = numbers[:5]
    
    # Unpack into 5 variables
    num1, num2, num3, num4, num5 = numbers
    
    return num1, num2, num3, num4, num5


