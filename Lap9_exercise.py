def quicksort(arr):
    """Quick sort algorithm implementation."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def replace_elements(arr, target, replacement):
    """Replace all occurrences of target with replacement in the array."""
    return [replacement if x == target else x for x in arr]

def main():
    # Step 1: Prompt the user to input an array of integers
    user_input = input("Enter an array of integers, separated by spaces: ")
    
    # Step 2: Store the elements in an array in a Python list
    arr = list(map(int, user_input.split()))
    
    # Step 3: Implement the quick sort algorithm to sort the input array in ascending order
    sorted_arr = quicksort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # Step 4: Allow the user to specify a target element to search for in the sorted array
    target = int(input("Enter the target element to search for: "))
    
    # Step 5: If the target element is found, prompt the user to input a replacement element
    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))
        
        # Replace all occurrences of the target element with the replacement element in the array
        modified_arr = replace_elements(sorted_arr, target, replacement)
    else:
        modified_arr = sorted_arr
        print(f"Target element {target} not found in the array.")
    
    # Step 6: Display the modified array after replacing the elements
    print(f"Modified array: {modified_arr}")

if __name__ == "__main__":
    main()
    
