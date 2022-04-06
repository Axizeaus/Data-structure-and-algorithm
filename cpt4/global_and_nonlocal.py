# def outer():
#     test = 1

#     def inner():
#         nonlocal test
#         test = 2
#         print('inner:', test)
#     inner()
#     print('outer:', test) # nonlocal affected this one 


# test = 0
# outer()
# print('global:', test)

def outer():
    test = 1

    def inner():
        global test
        test = 2
        print('inner:', test)
    inner()
    print('outer:', test) 


test = 0
print('before:', test)
outer()
print('global:', test) 
# outer => inner => global test changed

# nonlocal looks for the nearest var with the same name, excluding global

# def outer():
#     nonlocal test = 1 # this will end up as an error

#     def inner():
#         test = 2
#         print('inner:', test)
#     inner()
#     print('outer:', test) 


# test = 0
# print('before:', test)
# outer()
# print('global:', test) 