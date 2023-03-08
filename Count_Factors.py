A=int(input("Enter a number to find it's Factor count: "))
i=1
count=0
while i*i<=A:
    if A%i==0:
        if i==A/i:
            count+=1
        else:
            count+=2
    i+=1
print("Factor count :",count)

# output:
# Enter a number to find it's Factor count: 5
# Factor count :2