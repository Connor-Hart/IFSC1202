x = int(input("Enter a month: "))
y = int(input("Enter a day: "))

if x == 1:
    y=y+1
elif y>31:
    y=1
    x=x+1
if x == 2:
   y=y+1
elif y>28:
    y=1
    x=x+1
if x == 3:
    y=y+1
elif y>31:
    y=1
    x=x+1
if x == 4:
    y=y+1
elif y>30:
    y=1
    x=x+1
if x == 5:
    y=y+1
elif y>31:
    y=1
    x=x+1
if x == 6:
    y=y+1
elif y>30:
    y=1
    x=x+1
if x == 7:
    y=y+1
elif y>31:
    y=1
    x=x+1
if x == 8:
    y=y+1
elif y>31:
    y=1
    x=x+1
if x == 9:
    y=y+1
elif y>30:
    y=1
    x=x+1
if x == 10:
    y=y+1
elif y>31:
    y=1
    x=x+1
if x == 11:
    y=y+1
elif y>30:
    y=1
    x=x+1
if x == 12:
    y=y+1
elif y>31:
    y=1
print(str(x) + "/" + str(y))