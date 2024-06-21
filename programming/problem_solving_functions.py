# Write a Python function to find the maximum of three numbers.
# Define a function that returns the maximum of two numbers
def max_of_two(x, y):
    # Check if x is greater than y
    if x > y:
        # If x is greater, return x
        return x
    # If y is greater or equal to x, return y
    return y

# Define a function that returns the maximum of three numbers
def max_of_three(x, y, z):
    # Call max_of_two function to find the maximum of y and z,
    # then compare it with x to find the overall maximum
    return max_of_two(x, max_of_two(y, z))

# Print the result of calling max_of_three function with arguments 3, 6, and -5
print(max_of_three(3, 6, -5)) 