def check_palindrome(s):
  plain_str=""
  for char in s:
      if char.isalnum():
          if char.isupper():
              char=char.lower()
          plain_str+=char
  reverse_str=""
  for char in reversed(plain_str):
      reverse_str+=char
  if plain_str==reverse_str:
      return True
  return False


s="A man, a plan, a canal: Panama"
result=check_palindrome(s)
print(result)

# output:True