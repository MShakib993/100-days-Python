def find_smallest(lst):
    # Base case: If the list contains only one element, return that element
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: Compare the first element with the smallest element in the rest of the list
    rest_smallest = find_smallest(lst[1:])
    
    # Return the smaller of the first element and the smallest from the rest of the list
    return lst[0] if lst[0] < rest_smallest else rest_smallest

# Example usage:
numbers = [5, 2, 9, 1, 6]
smallest = find_smallest(numbers)
print(f"The smallest number is: {smallest}")
