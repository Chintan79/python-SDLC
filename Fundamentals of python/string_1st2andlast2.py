str1 = input("enter string : ")
def new_string(str1):
    length = len(str1)
    if length < 2:
        return ''
    else:
        return str1[0:2] + str1[-2:]
        
print(new_string(str1))