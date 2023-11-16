import timeit
from functools import lru_cache
import sys


def Fibonacci(steps):
    if steps <= 1:
        return steps
    else:
        return Fibonacci(steps - 1) + Fibonacci(steps - 2)
     
@lru_cache(maxsize=None)
def Fibonacci_cached(n):
    if n <= 1:
        return n
    else:
        return Fibonacci_cached(n-1) + Fibonacci_cached(n-2)

def main():
    time = timeit.timeit("Fibonacci(30)", globals=globals(), number=1)
    print(f"Czas obliczania Fibonacciego rekurencyjnie: {time} sekundy")

    time_cached = timeit.timeit("Fibonacci_cached(30)", globals=globals(), number=1)
    print(f"Czas obliczania Fibonacciego z użyciem cache: {time_cached} sekundy")



if __name__ == "__main__":
    sys.exit(main())

