n=1
count=0
A=int(input("Enter a number: "))
for i in range(2,A+1):
  flag=False
  for j in range(2,i):
    if i%j==0:
      flag=True
      break

  if not flag:
    count+=1
print(f"The count of prime number less than and equal to {A} is: ",count)

# output:
# Enter a number: 19
# The count of prime number less than and equal to 19 is:  8