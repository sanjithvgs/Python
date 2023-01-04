num=int(input("Enter the number to check prime or not: "))
res="PRIME"
for i in range(2,num):
  if num%i==0:
    res="NON PRIME"
    break
print(res)