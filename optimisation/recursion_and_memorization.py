# Fibonacci Sequence  with  recursion and memorization
from functools import lru_cache  # for method 2
# Method 1
fibonacci_cache = {}


def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Otherwise, compute the Nth term
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the value and return it
    fibonacci_cache[n] = value
    # return value
    return value


# Method 2 by using a  decorator

@lru_cache(maxsize=1000)
def fibonnaci_decorated(n):
    # chech the input is  a positive integer
    if type(n) != int:
        raise TypeError("n must be a  positive integer")
    if n < 1:
        raise ValueError("n must be a  positive integer")

    # Compute the Nth Term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonnaci_decorated(n-1)+fibonnaci_decorated(n-2)


if __name__ == "__main__":
    for n in range(1, 1001):
        print(n, ":", fibonnaci_decorated(n))
