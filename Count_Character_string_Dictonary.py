str1=input("Enter string to count a character: ")
dict_freq={}
for value in str1:
   if value not in dict_freq:
      dict_freq[value]=1
   else:
      dict_freq[value]+=1
print(dict_freq)  

# output:

# Enter string to count a character: ABACAB
# {'A': 3, 'B': 2, 'C': 1}