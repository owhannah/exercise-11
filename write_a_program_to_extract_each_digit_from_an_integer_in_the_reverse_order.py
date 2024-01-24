# Write a Program to extract each digit from an integer in the reverse order

number = 7536
print("Given number:", number)

# Iterate through each digit in reverse order
while number > 0:
    # Get the last digit
    last_digit = number % 10
    
    # Remove the last digit and repeat the loop
    number //= 10
    
    # Print the current digit
    print(last_digit, end=" ")