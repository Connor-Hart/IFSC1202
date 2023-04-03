line = input(str("Enter a string: "))
firstf = line.find("f")
lastf = line.rfind("f")
if firstf == -1:
    print("Zero f")
    exit()
if firstf != lastf:
    print(lastf)
if firstf == lastf:
    print("One f")