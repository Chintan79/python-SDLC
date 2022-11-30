l1 = ['abc','aba','abcd','1221']

def compare(l1):
    a = 0
    for i in l1:
       if len(i)>1 and i[0] == i[-1]:
           a += 1
        
    return a

for i in l1:
    z = compare(l1)
print(z)
 