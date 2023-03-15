numrecords = 0
def FahrToCel(n):
    temp = (n-32)*(5/9)
    return(float(temp))

ftempfile = open("06.03 FTemps.txt", "r")
ctempfile = open("06.03 CTemps.txt", "w")
x = ftempfile.readline()

while x != "":
    FTemp = float(x)
    CTemp = float(FahrToCel(FTemp))
    ctempfile.write("{:>5.1f} {}".format(CTemp, "\n"))
    numrecords += 1
    x = ftempfile.readline()

print(str(numrecords) + " records written")