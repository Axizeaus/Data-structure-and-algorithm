class ExponentialA(object):
    base = 3
    @classmethod
    def exp(cls, x):
        return cls.base ** x
    
    @staticmethod
    def addition(x, y):
        return x + y
    
    
class ExponentialB(ExponentialA):
    base = 4 
    
a = ExponentialA()
b = a.exp(3)
print("3 ** 3 = ", b)
print('15+10 = ', ExponentialA.addition(15, 10))
print(ExponentialB.exp(3))

