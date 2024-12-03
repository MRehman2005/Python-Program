n = 5  # Number of elements
array = []
max_value = float('-inf')  # Initialize to a very small number
second_max = float('-inf')  # Initialize to a very small number

# Reading n inputs and storing them in the array
for i in range(n):
    array.append(int(input()))  # Assuming input values are integers
    
# Find the largest and second largest values
for num in array:
    if num > max_value:
        second_max = max_value  # Update second largest before max
        max_value = num  # Update max value
    elif num > second_max and num != max_value:
        second_max = num  # Update second largest value

# Output the second largest value
print("Second largest value:", second_max)
