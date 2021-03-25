'''Get the length l
   print given string with increasing each character with l length
'''
def double_char(str,l):
  lst=""
  for i in range(len(str)):
    lst=lst+str[i]*l
  return lst

a=str(input("Enter the string: "))
l=int(input("Enter the number to increase the character: "))
print(double_char(str(a),l))