A=input("Enter a string with uppercase and lowercase: ")
result=""
for val in A:
    if val.isupper():
        result+=val.lower()
    else:
        result+=val.upper()
print("The toggle result is: ",result)

# output:
# Enter a string with uppercase and lowercase: ThiS Is PyThOn
# The toggle result is:  tHIs iS pYtHoN