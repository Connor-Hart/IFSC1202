line = input(str("Enter a string: "))
linelen = (len(line))
half = int(line.find(' ')+1)
newline = str(line[half:] + " " + line[:half])
print(newline)