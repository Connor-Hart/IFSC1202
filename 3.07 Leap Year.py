x = int(input("Enter a four digit year: "))
if x%400 == 0:
    print("LEAP YEAR")
elif x%100!=0 and x%4==0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")
    