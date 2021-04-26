def factorial(num):
  if (num<=0):
    print("Invalid Input")
  else:
    res=1
    for i in range (1,num+1):
      res=res*i
    return res
num=int(input("Enter a number greater than 0 to find factorial: "))
print(factorial(num))
