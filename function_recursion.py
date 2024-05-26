def sum_of_digits(n):
    # Base case: if n is a single-digit number, return n
    if n < 10:
        return n
    else:
        # Recursive case: split the number into the last digit and the remaining digits
        last_digit = n % 10
        remaining_digits = n // 10
        # Return the sum of the last digit and the recursive call on the remaining digits
        return last_digit + sum_of_digits(remaining_digits)

# Example usage
print(sum_of_digits(123))  # Output: 6
print(sum_of_digits(9876)) # Output: 30
