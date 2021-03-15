# Insertion sorting..

nlist=[]
len = int(input("Enter the length :"))
for i in range(len):
	a=input("Enter a element: ")
	nlist.append(a)
print("The list contain: ")
print(nlist)

for index in range(1,len):
  currentvalue = nlist[index]
  position = index
  
  while position>0 and nlist[position-1]>currentvalue:
      nlist[position]=nlist[position-1]
      position = position-1
  
  nlist[position]=currentvalue

print("The sorted list contain :")
print(nlist)
