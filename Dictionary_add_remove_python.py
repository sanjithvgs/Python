# Find a value in Dictionary ,if not available means add that value into the dictonary
# Delete a value in Dictionary using key

dic1={}
res="False"
num=int(input("Enter the length of dictionary: "))
for i in range(num):
  a=int(input("Enter a element: "))
  dic1[i]=a
print("Dictionary contain : ",dic1)
b=int(input("Enter a number to check in dictonary: "))
for i in range(num):
  if b == dic1[i]:
    res="True"
  else:
    abt=b
if(res=="False"):
  print("The element",abt,"is not founded so,it is added into dictonary")
  dic1.update({num:b})
else:
  print("The element",abt,"is founded..!")
print(dic1)
z=int(input("Enter a key to delete a value: "))
try:
  dic1.pop(z)
except:
  print("Invalid Key")
print(dic1)
