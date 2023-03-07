str1=input("Enter the String: ")
dict_freq={}
for value in str1:
   if value not in dict_freq:
      dict_freq[value]=1
   else:
      dict_freq[value]+=1
print(dict_freq) 

# output:
# Enter the String: rraanddom
# {'r': 2, 'a': 2, 'n': 1, 'd': 2, 'o': 1, 'm': 1}