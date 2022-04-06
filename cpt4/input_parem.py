# x = 3

# def func(y):
#     print(y)
    
# func(x)

# x = 3
# def func(x):
#     x = 7
# func(x)
# print(x)

x = list('123')
def func(x):
    x[1] = 42
    x = 'new str'
    
func(x) # this only affects the original object, x is alright.
print(x) # mutable objects are affected 