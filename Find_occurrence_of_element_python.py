l=int(input("Enter the length of list: "))
lst=[]
cnt=0
for i in range(l):
  a=input("Enter a element: ")
  lst.append(a)
print(lst)
z=input("Enter a element to find number of occurance: ")
for i in range (l):
  if (lst[i]==z):
    cnt+=1
if (cnt==0):
  print("The element",z,"is not available in the list")
else:    
  print("The element",z,"occurs in",cnt,"times")