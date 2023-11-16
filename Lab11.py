import sys

class complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self, number):
        return complex(self.real + number.real, self.imag + number.imag)
    
    def __sub__(self,number):
        return complex(self.real - number.real, self.imag - number.imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}j"
        else:
            return f"{self.real} {self.imag}j"
    
def main():
    a = complex(3,5)
    print(a)
    b = complex(5,10)
    print(b)
    c = a + b
    print(c)

if __name__ == "__main__":
    sys.exit(main())
