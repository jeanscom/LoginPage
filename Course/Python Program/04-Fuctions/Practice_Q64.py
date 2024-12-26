#Implement any sorting algorithm using Recursion
def merge_sort(arr):
    # Base case: a list of length 1 is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point and divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    # Merge two sorted lists into one
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    
    # If there are any remaining elements in either list, add them
    sorted_list.extend(left)
    sorted_list.extend(right)
    
    return sorted_list

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)
