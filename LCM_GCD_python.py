# Find GCD and LCM of given two numbers
 
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a<b:
  big=b
else:
  big=a
for i in range (1,big):
  if ( a%i == 0 and b%i == 0):
   z=i
lcm=(a*b)/z
print("The LCM of two numbers is: ",end="")
print(int(lcm))
print("The GCD of two numbers is: ",z)