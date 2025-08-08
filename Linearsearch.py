import time

def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()
            print(f"Search started at: {start_time}")
            print(f"Search ended at: {end_time}")
            print(f"Time taken: {end_time - start_time} seconds")
            return i
    end_time = time.time()
    print(f"Search started at: {start_time}")
    print(f"Search ended at: {end_time}")
    print(f"Time taken: {end_time - start_time} seconds")
    return -1


array = [5, 3, 8, 4, 2]
target_value = int(input("Enter the targetted no:"))

index = linear_search(array, target_value)
if index != -1:
    print(f"Element {target_value} found at index {index}.")
else:
    print(f"Element {target_value} not found in the array.")
