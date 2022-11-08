str1 = input("enter string : ")
def notpoor(Str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    
    
    if spoor > snot and snot > 0 and spoor > 0:
        str2 = str1.replace(str1[snot:(spoor+4)],'good')
        return str2
    else:
        return str1
print(notpoor(str1))