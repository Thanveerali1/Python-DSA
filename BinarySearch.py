import time

def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()
            print(f"Linear Search Start Time: {start_time}")
            print(f"Linear Search End Time:   {end_time}")
            print(f"Time taken: {end_time - start_time:.6f} seconds")
            return i
    end_time = time.time()
    print(f"Linear Search Start Time: {start_time}")
    print(f"Linear Search End Time:   {end_time}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    return -1

def binary_search(arr, target):
    start_time = time.time()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            end_time = time.time()
            print(f"Binary Search Start Time: {start_time}")
            print(f"Binary Search End Time:   {end_time}")
            print(f"Time taken: {end_time - start_time:.6f} seconds")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    end_time = time.time()
    print(f"Binary Search Start Time: {start_time}")
    print(f"Binary Search End Time:   {end_time}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    return -1

# Test data (sorted for binary search)
arr = [1, 3, 5, 7, 9, 11, 13]
target = int(input("Enter the targetted no:"))

print("Running Linear Search:")
lin_result = linear_search(arr, target)
if lin_result != -1:
    print(f"Linear Search: Element found at index {lin_result}")
else:
    print("Linear Search: Element not found")

print("\nRunning Binary Search:")
bin_result = binary_search(arr, target)
if bin_result != -1:
    print(f"Binary Search: Element found at index {bin_result}")
else:
    print("Binary Search: Element not found")
