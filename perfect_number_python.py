def per_num(n):
    sum=0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    if (sum==n):
      per="Perfect Number"
    else:
      per="Not perfect Number"
    return per
    
a=int(input("Enter a number: "))
print(per_num(a))