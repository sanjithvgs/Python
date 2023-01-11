year=int(input("Enter the Year: "))
if year%400==0 or (year%4==0 and year%100!=0):
    print("You have entered leap year!")
else:
    print("You have entered an non leap year!")