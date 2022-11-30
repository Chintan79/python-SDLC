l1 = []
n = int(input("enter n : "))

for i in range(0,n):
    ele = int(input())
    
    l1.append(ele)
    
print(l1)
l2 = []
for x in range(0,n):
    ele1 = int(input())
    
    l2.append(ele1)

def data(l1,l2):
    result = False
    for x in l1:
        for y in l2:
            if x == y:
                result = True
                return result
print(data(l1,l2))