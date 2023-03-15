year = 1950
popdoc = open("08.11 USPopulation.txt", "r")
poparray = popdoc.read().split('\n')
popchangearray = ''.split('.')
poppercentarray = ''.split('.')
for i in range(0, len(poparray)):
    cur = int(poparray[i])
    if i != len(poparray):
        poparraychange = int((cur)*1000)
        poparray[i] = (str(poparraychange))
    if i != len(poparray) and i != 0:
        cur = int(poparray[i])
        prev = int(poparray[i-1])
        popchange = int(int(cur)-int(prev))
        popchangearray.append(str(popchange))
popchangearray.pop(0)
for i in range(0, len(poparray)):
    if i != len(popchangearray):
        cur = int(popchangearray[i])
        prev = int(poparray[i])  
        popchange = float("{:.2f}".format((cur/prev)*100))
        poppercentarray.append(popchange)
print("Year    Population    Change    Percent Change")
for i in range(0, len(poparray)):
    if i == 0:
        print(str(year) + "    " + str(poparray[i]) + "    N/A        N/A")
        year += 1
    if i != 0:
        print(str(year) + "    " + str(poparray[i]) + "    " + str(popchangearray[i-1]) + "    " + str(poppercentarray[i]))
        year += 1