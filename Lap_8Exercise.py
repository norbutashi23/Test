def find_first_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            print(f"First repeating character: {char}")
            print(f"Memory address of '{char}': {id(char)}")
            return char
        else:
            char_count[char] = 1
    
    return None

# Example usage
s = "geeksforgeeks"
result = find_first_repeating_character(s)
if result is None:
    print("No repeating character found.")
