total=int(input("Enter the limit of Fibonacci sequence: "))
a=0
b=1
res=0
for i in range(total):
  if res<i:
    print(res)
    a=b
    b=res
    res=a+b