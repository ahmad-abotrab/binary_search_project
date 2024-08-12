# src/binary_search.py

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore the right half
        else:
            right = mid - 1
    
    # Element is not present in array
    return -1