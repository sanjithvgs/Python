def reverse(string):
    if len(string)<1:
        return
    first_char=string[0]
    reverse(string[1:len(string)])
    print(first_char,end="")


string=input("Enter a string to reverse: ")
reverse(string)

# output:
# Enter a string to reverse: sanjithvgs
# sgvhtijnas