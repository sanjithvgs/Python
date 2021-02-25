lst=[]
lst2=[]
a=int(input("Enter the number of element in the list: "))
for i in range (a):
  b=int(input())
  lst.append(b)
print("The list contain ", lst)
res=int(input("Enter any option 1.Add element 2.Remove element 3.Exit: "))
while (res!= 3):
  if res == 1:
    add=input("Enter a element to add: ")
    lst.append(add)
    print(lst)
    break
  elif res == 2:
    d=int(input("Enter a element to remove from list: "))
    for i in range(0,a):
      if lst[i]== d:
        lst2.append(i)
    for j in range(0,len(lst2)):
        c=lst2[j]
        c=c-j
        del lst[c]
    print(lst)   
    break
  else:
    print("Invalid keyy..")
    break

