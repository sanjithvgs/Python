#Reverse the given number without using while loop
num=int(input("Enter the number: "))
res=0
final=0
while num!=0:
  res=num%10
  num=num//10
  final*=10
  final+=res
print("The reverss of give number is: ",final)