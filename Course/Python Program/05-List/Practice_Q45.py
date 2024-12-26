# Write a Python Program to Find the Second Largest Number in a List Using Bubble Sort
# Function to perform bubble sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Perform bubble sort on the list
bubble_sort(numbers)

# Find the second largest number
# After sorting, the second largest will be at index -2
if len(numbers) >= 2:
    second_largest = numbers[-2]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not have a second largest number.")
