''' A pangram is a unique sentence in which 
 every letter of the alphabet is used at least once 
  Example : The quick brown fox jumps over a lazy dog  '''


a=input("Enter a Sentence to check whether it is pangrams or not: \n")
a=a.lower()
lst=[]
lst2=[]
lst=a
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(lst)):
  if lst[i] in b:
    lst2.append(lst[i])

n="The given sentence is NOT PANGRAMS"
res = []
for i in lst2:
    if i not in res:
        res.append(i)
if len(res)==len(b):
  n="The given sentence is PANGRAMS"
print(n)