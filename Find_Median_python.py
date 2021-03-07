# sort a list and find Median of given set of numbers

cnt=int(input ("Enter the length less than 3: "))
if cnt<=2:
  print("Invalid Length")
else:
  lst=[]
  for i in range (cnt):
    a=int(input("Enter a value: "))
    lst.append(a)
  lst.sort()
  print("The sorted list :",lst)
  if (cnt%2 == 0):
    c=int(cnt/2)
    print("The Median of given set of number is: ",end="")
    print(lst[c-1],"and ",end="")
    print(lst[c])
  else:
    c=int((cnt)/2)
    print("The Median of given set of number is: ",end="")
    print(lst[c])
