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


arr = [5, 3, 7, 1, 9]
target = int(input("Enter the targetted no:"))

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
