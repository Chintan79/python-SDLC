a = int(input("Enter your number : "))
fact = 1
if a < 0:
        print("factorial not vailable")
elif a == 0:
        print("factorial of 0 is 1")
else :
    for i in range(1,a+1):
        fact = fact * i
    print(fact)