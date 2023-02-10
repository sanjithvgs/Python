s=input("Enter the string: ")
count_digit = 0
count_alpha = 0
for char in s:
    if char.isalpha():
        count_alpha+=1
    if char.isnumeric():
        count_digit+=1
print(f"There are {count_alpha} alphabets found in given string!")
print(f"There are {count_digit} digits found in given string!")

# Enter the string: sanjith55@google.com
# There are 16 alphabets found in given string!
# There are 2 digits found in given string!