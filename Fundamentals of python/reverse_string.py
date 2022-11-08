# string will be printed reverse if the length of string wil be multiple of 4

string = input("enter string : ")
x = len(string)
print(x)
if x % 4 == 0:
    print(string[::-1])
else:
    print(string)
    