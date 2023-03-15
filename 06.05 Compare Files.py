linesread = 1
numdiff = 0
filea = open("06.05 CompareFileA.txt", "r")
fileb = open("06.05 CompareFileB.txt", "r")

x = filea.readline()
y = fileb.readline()
while x and y != "":
    if x == y:
        x = filea.readline()
        y = fileb.readline()
        linesread += 1
    else: 
        print("Line " + str(linesread) + " - FileA: " + str(x))
        print("Line " + str(linesread) + " - FileB: " + str(y))
        x = filea.readline()
        y = fileb.readline()
        linesread += 1
        numdiff += 1

print(str(numdiff) + " differences")
