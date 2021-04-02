
a=int(input("Enter the length of list: "))
lst1=[]
lst2=[]
lst3=[]
for i in range(a):
	z=int(input("Enter the element of First list: "))
	lst1.append(z)

for i in range(a):
	z=int(input("Enter the element of Second list: "))
	lst2.append(z)

for i in range(a):
	z=int(input("Enter the element of Third list: "))
	lst3.append(z)
x=map(lambda m,n,o : m+n+o,lst1,lst2,lst3)
z=map(lambda m,n,o : m*n*o,lst1,lst2,lst3)

print(lst1)
print(lst2)
print(lst3)
print("Multiplication: ",z)
print("Addition: ",x)