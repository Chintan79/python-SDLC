a = {'a':1,'b':2,'c':3}
b = {'d':4,'e':5,'f':6}
c = {}
for i in (a,b):c.update(i)
print(c)
    
