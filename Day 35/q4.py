class calcuation:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def divide(self):
        return self.num1 / self.num2
    def multipy(self):
        return self.num1 * self.num2
    def sqrroot(self):
        return self.num1 ** 0.5

b = calcuation(10,320)
print(b.add())
print(b.sub())
print(b.divide())
print(b.multipy())
print(b.sqrroot())


    