list = [2,3,4,5,8,6,7,8,6,0]
sub_list = [8,2,1]

if (set(list) & set(sub_list) == set(sub_list) ):
    print("it is subset of list")
else:
    print("not subset of a list")
    