a = int(input("enter number a: "))
b = int(input("enter number b: "))
c = int(input("enter number c: "))

if a == b or b == c or a == c:
    print("your sum is : 0")
else:
    sum = a+b+c
    print("sum of three integers : ",sum)