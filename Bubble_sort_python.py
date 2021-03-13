# Bubble sorting..

l=int(input("Enter the length: "))
lst=[]
z=0
for i in range(l):
	a=int(input("Enter the element: "))
	lst.append(a)
print("The list contain: ")	
print(lst)
for x in range(l):
	for y in range(l):
		if(lst[x]<lst[y]):
			z=lst[x]
			lst[x]=lst[y]
			lst[y]=z
print("The sorted list contain: ")			
print(lst)
