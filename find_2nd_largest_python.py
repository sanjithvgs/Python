'''
 This program is used to find 2nd largest element in the list 
 Without using sort() Method
'''
lst=[]
big=0
sec_big=0
num=int(input("Enter more than 2 number of elements : "))
if(num<=2):
  print("Invalid Input")
else:
  for i in range(num):
    a=int(input())
    lst.append(a)
  for j in range(num):
   for k in range(num):
      if (lst[j]<lst[k] and lst[k]>big):
       big=lst[k]
  lst.remove(big)
  for j in range(num-1):
    for k in range(num-1):
      if (lst[j]<lst[k] and lst[k]>sec_big):
       sec_big=lst[k]
  print("The second largest number is : ",sec_big)
