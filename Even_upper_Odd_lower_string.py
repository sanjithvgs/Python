word=input("Enter the string: ")
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
     if i % 2 == 0:
          converted_word += word2[i]
     else:
          converted_word += word1[i]
print(converted_word)

# output:

# Enter the string: this is python world
# tHiS Is pYtHoN WoRlD