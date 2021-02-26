row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))
lst=[]
for i in range (row):
  col1=[]
  print("Enter row value: ")
  for j in range (col):
    c=int(input())
    col1.append(c)
  lst.append(col1)
res = list(set(tuple(sorted(sub)) for sub in lst))
print(res)
