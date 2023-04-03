line = input(str("Enter a string: "))
firsth = line.find("h")
lasth = line.rfind("h")
print(line[:firsth] + line[lasth+1:])
