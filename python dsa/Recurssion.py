import time

def recursive_binary_search(arr, target, low, high, start_time=None):
    # Record the start time only once, on the very first call
    if start_time is None:
        start_time = time.time()
    
    if low > high:
        end_time = time.time()
        print(f"Recursive Binary Search Start Time: {start_time}")
        print(f"Recursive Binary Search End Time:   {end_time}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        end_time = time.time()
        print(f"Recursive Binary Search Start Time: {start_time}")
        print(f"Recursive Binary Search End Time:   {end_time}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high, start_time)
    else:
        return recursive_binary_search(arr, target, low, mid - 1, start_time)



arr = list(range(100000))
target = 99999
index = recursive_binary_search(arr, target, 0, len(arr) - 1)

print(f"Element found at index: {index}")
