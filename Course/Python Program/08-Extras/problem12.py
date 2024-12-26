# You are given an array a
#  consisting of n
#  integer numbers.

# Let instability of the array be the following value: maxi=1nai−mini=1nai
# .

# You have to remove exactly one element from this array to minimize instability of the resulting (n−1)
# -elements array. Your task is to calculate the minimum possible instability.

def minimize_instability(arr):
    # Sort the array to easily find the min and max values
    arr.sort()
    
    # The original max and min
    original_max = arr[-1]
    original_min = arr[0]
    
    # Instability after removing the maximum element
    instability_remove_max = arr[-2] - original_min
    
    # Instability after removing the minimum element
    instability_remove_min = original_max - arr[1]
    
    # The minimum instability after removing one element
    min_instability = min(instability_remove_max, instability_remove_min)
    
    return min_instability

# Example usage
arr = [1, 3, 6, 4, 1, 2]
result = minimize_instability(arr)
print(result)  # Output the minimum possible instability