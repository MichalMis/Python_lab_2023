class FibonacciIterator:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0

    def __iter__(self): 
        self.a, self.b = 0, 1
        return self

    def __next__(self):
        if self.current_step >= self.steps:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current_step = self.current_step + 1
        return result

steps = 10 
fibonacci_iterator = FibonacciIterator(steps)
Myiterator = iter(fibonacci_iterator)

for iterations in Myiterator:
     print(iterations)