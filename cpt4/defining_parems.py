from turtle import pos


def func(a, b=4, c=99):
    print(a,b,c)
    
func(1)
func(b=10, a=0, c=102)
func(42, c=9)
func(23,24,35)

def minimum(*n): # takes 0 to infinite num of parems;
    if n: # n being a collection, if empty, false, else true;
        mn = n[0] # assigning minimum value as the first one
        for val in n[1:]: # start from second index, since first is assigned
            if val < mn: # if val smaller than min val, change min val to the smaller one
                mn = val
        print(mn)

# incoming n will be a tuple
minimum(2,3,5,6)
minimum()

def fun(**kwargs):
    print(kwargs)
    
fun(a = 1, b = 2)
fun()
fun(a=32, b=89, c=1000)

def pos_fun(a,b,/,c): # the first part is postional only, the second can be with kw
    print(a,b,c)
    
pos_fun(1,2,3)
pos_fun(1,2,c=3)
# pos_fun(a=20,b=0, 10) this is not gonna work

def pos_fun_play(a,b=10,/):
    print(a,b)
    
pos_fun_play(4,5)
pos_fun_play(3)

# emulating divmod()

def divmod(a,b,/):
    return (a//b, a%b)

# print(len(obj='hello'))
# obj = 'nice to meet you'
# print(len(obj))


# nice use case of / in parems

def nice(name,/,**kwargs):
    print(name)
    print(kwargs)
    
nice('positional only name', name="name in kwargs")