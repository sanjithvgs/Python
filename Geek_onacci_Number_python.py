'''Given four integers A, B, C, N.
   A, B, C represents the first three numbers of geek-onacci series.
   Find the Nth number of the series. 
   The nth number of geek-onacci series is a sum of the last three numbers (summation of N-1th, N-2th, and N-3th geek-onacci numbers)
'''
o=int(input("Enter the length: "))
l=0
lst2=[]
while l!=o:
    a,b,c,n=input().split(" ")
    lst=[]
    lst.append(int(a))
    lst.append(int(b))
    lst.append(int(c))
    n=int(n)
    k=0
    while len(lst)!=n:
      m=lst[k]+lst[k+1]+lst[k+2]
      lst.append(m)
      k+=1
    lst2.append(lst[-1])
    l+=1
for item in lst2:
  print("Result is: ",item)