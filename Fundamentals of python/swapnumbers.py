# usig temp variable
from re import X


a = int(input("enter number a: "))
b = int(input("enter number b: "))
temp = 0

temp = a
a = b
b = temp
print("a : ",a)
print("b : ",b)


#  without temp veriable
x = int(input("enter number x: "))
y = int(input("enter number y: "))

x , y = y , x

print("x : ",x)
print("y : ",y)
