import time

def exponential_time(n):
    print(f"\nO(2^n) with n={n}")
    start = time.time()
    def helper(k):
        if k == 0:
            return
        helper(k - 1)
        helper(k - 1)
    helper(n)
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

exponential_time(10)