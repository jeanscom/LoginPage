#Given a list of integers. Find a peak element i.e., an element that is not smaller than its neighbour's. Note: For corner elements, we need to consider only one neighbour

# Sample lists of integers
lists = [
    [5, 10, 20, 15],
    [10, 20, 15, 2, 23, 90, 67]
]

# Iterate through each list
for arr in lists:
    n = len(arr)
    peak_found = False  # Flag to indicate if a peak has been found

    # Check for corner elements
    if n == 1:
        peak = arr[0]  # Only one element is a peak
        peak_found = True
    elif arr[0] >= arr[1]:
        peak = arr[0]  # First element is a peak
        peak_found = True
    elif arr[n - 1] >= arr[n - 2]:
        peak = arr[n - 1]  # Last element is a peak
        peak_found = True

    # Check for peak elements in the middle
    if not peak_found:  # Only check middle elements if no peak found yet
        for i in range(1, n - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                peak = arr[i]  # Found a peak element
                peak_found = True
                break  # Exit the loop once a peak is found

    # Output the result
    if peak_found:
        print("Peak element found in list", arr, ":", peak)
    else:
        print("No peak element found in list", arr)