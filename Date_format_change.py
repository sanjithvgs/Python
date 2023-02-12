#Date format changer
s=input("Enter the date in 'DD/MM/YYYY' format: ")
day=s[:2]
month=s[3:5]
year=s[6:]
sep="/"
print("MM/DD/YYYY: ",month+sep+day+sep+year)
print("YYYY/MM/DD: ",year+sep+month+sep+day)

# output:

# Enter the date in 'DD/MM/YYYY' format: 08/12/1998
# MM/DD/YYYY:  12/08/1998
# YYYY/MM/DD:  1998/12/08