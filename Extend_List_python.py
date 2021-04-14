lst=[]
l=int(input("Enter the length: "))
for _ in range(l):
	a=input("Enter a element: ")
	lst.append(a)
print("Original list: "+str(lst))
lst.extend(lst)
print("Extended list: "+str(lst))
