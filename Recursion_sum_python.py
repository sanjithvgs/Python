def sum_Digits(n):
  if n == 0:
    return 0
  else:
    z=n%10 + sum_Digits(int(n / 10))
    return z


a=int(input("Enter the integer value: "))
print(sum_Digits(a))