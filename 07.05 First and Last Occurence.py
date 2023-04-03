line = input(str("Enter a string: "))
firstf = line.find("f")
lastf = line.rfind("f")
if firstf == -1:
    print(0)
    exit()
if firstf != lastf:
    print(str(firstf) + " " + str(lastf))
if firstf == lastf:
    print(firstf)