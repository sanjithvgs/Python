from collections import Counter
print("Enter a sentence: ")
s = list(map(str, input().split()))
print("The original list contain: ")
print(s)
cnt = Counter(s)
print("\nMost common element in the list using collections: ")
print(cnt.most_common(1)[0][0])