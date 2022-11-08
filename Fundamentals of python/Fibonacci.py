num = int(input("enter your number : "))

n1 = 0
n2 = 1
count = 0

if num == 0:
    print("please enter a positive number!")
elif num == 1 or num == 2:
    print("fibonacci :",n2)
else:
    print("your fibonacci series is : ")
    while count < num:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
        