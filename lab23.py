import os
import pickle

def cache_result(filename):
    def decorator(func):
        def wrapper(n):
            if os.path.exists(filename):
                with open(filename, 'rb') as file:
                    result = pickle.load(file)
                print("Wczytano dane z dysku.")
            else:
                # Jeśli plik nie istnieje, oblicz wynik funkcji
                result = func(n)
                # Zapisz wynik na dysku
                with open(filename, 'wb') as file:
                    pickle.dump(result, file)
                print("Zapisano dane na dysku.")
            return result
        return wrapper
    return decorator

@cache_result('cached_fibonacci.pkl')
def Fibonacci(steps):
    if steps <= 1:
        return steps
    else:
        return Fibonacci(steps - 1) + Fibonacci(steps - 2)

result = Fibonacci(30)
print("Wynik ciągu Fibonacciego dla n=30:", result)