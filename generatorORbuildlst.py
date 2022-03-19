import time

def odd_genrator(n, m):
    while n < m:
        yield n
        n += 2
    
def odd_list(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

t = time.time()
sum(odd_genrator(1, 100000))
print(f'time sum generator: {time.time() - t}')
sum(odd_list(1, 100000))
print(f'time sum list {time.time() - t}')

# also this one works 

ls = [i for i in range(10)]
print(ls)

gen = (i for i in range(10))
print(list(gen))