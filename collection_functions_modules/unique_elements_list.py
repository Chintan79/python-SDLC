def unique_list(l):
    list = []
    for i in l:
        if i not in list:
            list.append(i)
    return list
print(unique_list([1,2,3,1,2,3,4,5,6,6,6,7,8,9,9]))
