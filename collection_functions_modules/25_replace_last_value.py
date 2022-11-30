tuple = (1,2,3,4,5,6,8)
print(tuple)

list = list(tuple)
list[-1] = 7

tuple = tuple(list)
print(tuple)