linesread = 0
lineswritten = 0

inputfile = open("06.04 Empty Lines Input.txt", "r")
outputfile = open("06.04 Empty Lines Output.txt", "w")

x = inputfile.readline()
while x != "":
    if x == "\n":
        linesread += 1
        x = inputfile.readline()
    else:
        outputfile.write("{}".format(str(x)))
        linesread += 1
        lineswritten += 1
        x = inputfile.readline()
print(str(linesread) + " records read")
print(str(lineswritten) + " records written")