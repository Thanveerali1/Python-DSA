import time

def binary_search(arr, target):
    start_time = time.time()
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            end_time = time.time()
            print(f"Search started at: {start_time}")
            print(f"Search ended at: {end_time}")
            print(f"Time taken: {end_time - start_time} seconds")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    end_time = time.time()
    print(f"Search started at: {start_time}")
    print(f"Search ended at: {end_time}")
    print(f"Time taken: {end_time - start_time} seconds")
    return -1

sorted_array = [1, 3, 5, 7, 9, 11, 13]
target_value = int(input("Enter the targetted no:"))

index = binary_search(sorted_array, target_value)
if index != -1:
    print(f"Element {target_value} found at index {index}.")
else:
    print(f"Element {target_value} not found in the array.")
