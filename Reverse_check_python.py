def reverseCheck(number):
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False
num=int(input("Enter a number: "))
if reverseCheck(num):
  a="same"
else:
  a="Different"
print("The original number and reverse number are",a,"!")