a = int(input("Enter the size of first list: "))
a1= set(map(int, input("Enter the element: ").split()))
b = int(input("Enter the size of second list: "))
b1 = set(map(int, input("Enter the element: ").split()))
adiff = a1.difference(b1)
bdiff = b1.difference(a1)
output = sorted(list(adiff.union(bdiff)))
print("The combined sorted of two list without common value: ")
if output==0:
	print("0")
else:
	for i in output:
		print(i)