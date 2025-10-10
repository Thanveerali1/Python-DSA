import time

def fib_memo_simple(n, memo=None, start_time=None):
    if memo is None:
        memo = {}
    if start_time is None:
        start_time = time.time()  # start time only once
    
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    
    memo[n] = fib_memo_simple(n-1, memo, start_time) + fib_memo_simple(n-2, memo, start_time)
    
    # When we return from the original call (n), print times
    if n == max(memo.keys()):
        end_time = time.time()
        print(f"Start Time: {start_time}")
        print(f"End Time:   {end_time}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
    
    return memo[n]

# Example usage
n = int(input("Enter a number:"))
result = fib_memo_simple(n)
print(f"Fibonacci({n}) = {result}")
