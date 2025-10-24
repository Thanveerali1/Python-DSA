import time

def ConstantTime(n): 
    start = time.time()
    arr = [1,2,3]
    def inner(arr):
        return arr[0]
    end = time.time()
    print(f"Time taken for n = {n}: {end - start} seconds")

ConstantTime(1000)
ConstantTime(10000)
ConstantTime(100000)
