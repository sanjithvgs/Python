def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

my_string = "Hello, World!"
reversed_string = reverse_string(my_string)
print(reversed_string)

# output:
# !dlroW ,olleH