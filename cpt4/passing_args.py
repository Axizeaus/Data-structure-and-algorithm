

def func(a, b, c):
    print(a, b, c)

# positional
func(1, 2, 3)

# keyword
func(a=10, c=35, b=100)

#  func(positional args then keyword ones)
func(10, b=20, c=99)

# iter unpacking
values = (1,4,-8)
func(*values) # mind the * before var name

# dict unpacking
values = {'b': 1, 'c': 2, 'a': 42}
func(*values) # this will only give keys 
func(**values) # this, only values

def func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)
func(1, *(2, 3), f=6, *(4, 5))
func(*(1, 2), e=5, *(3, 4), f=6)
func(1, **{'b': 2, 'c': 3}, d=4, **{'e': 5, 'f': 6})
func(c=3, *(1, 2), **{'d': 4}, e=5, **{'f': 6})

