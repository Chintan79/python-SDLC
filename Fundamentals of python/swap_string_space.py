str1 = input("ebter first string : ")
str2 = input("enter second string : ")

x = str1[:2]

str1 = str1.replace(str1[0:2],str2[0:2])
str2 = str2.replace(str2[0:2],x)
print("your first string become : ",str1)
print("your econd string become : ",str2)