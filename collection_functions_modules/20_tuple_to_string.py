tuple = ('i','a','m','c','h','i','n','t','a','n')
print(type(tuple))

def convert(tuple):
    
    string = ""
    for i in tuple:
        string = string+i
    return string
string = convert(tuple)
print(string)
print(type(string))