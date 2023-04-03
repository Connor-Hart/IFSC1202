from math import ceil
line = input(str("Enter a string: "))
linelen = (len(line))
half = int(ceil(linelen/2))
newline = str(line[half:] + line[:half])
print(newline)