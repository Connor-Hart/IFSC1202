FromValue = int(input("Enter From Value: "))
FromUnit = str(input("Enter From Unit (inch, ft, yd, mi): "))
ToUnit = str(input("Enter To Unit (inch, ft, yd, mi): "))
ToValue = 0
fromcorrect = bool(False)
tocorrect = bool(False)
if FromUnit == str("ft"):
    fromcorrect = bool(True)
if FromUnit == str("inch"):
    fromcorrect = bool(True)
if FromUnit == str("yd"):
    fromcorrect = bool(True)
if FromUnit == str("mi"):
    fromcorrect = bool(True)
if fromcorrect == bool(False):
    print("FromUnit is not valid")
    exit()
if ToUnit == str("ft"):
    tocorrect = bool(True)
if ToUnit == str("inch"):
    tocorrect = bool(True)
if ToUnit == str("yd"):
    tocorrect = bool(True)
if ToUnit == str("mi"):
    tocorrect = bool(True)
if tocorrect == bool(False):
    print("ToUnit is not valid")
    exit()
if FromUnit == ToUnit:
    ToValue = FromValue
if FromUnit == "inch" and ToUnit == "ft":
    ToValue = float(round(FromValue/12,7))
if FromUnit == "inch" and ToUnit == "yd":
    ToValue = float(round(FromValue/36,7))
if FromUnit == "inch" and ToUnit == "mi":
    ToValue = float(round(FromValue/63360,7))
if FromUnit == "ft" and ToUnit == "inch":
    ToValue = float(round(FromValue*12,7))
if FromUnit == "ft" and ToUnit == "yd":
    ToValue = float(round(FromValue/3,7))
if FromUnit == "ft" and ToUnit == "mi":
    ToValue = float(round(FromValue/5280,7))
if FromUnit == "yd" and ToUnit == "inch":
    ToValue == float(round(FromValue*36,7))
if FromUnit == "yd" and ToUnit == "ft":
    ToValue == float(round(FromValue*3,7))
if FromUnit == "yd" and ToUnit == "mi":
    ToValue == float(round(FromValue/1760,7))
if FromUnit == "mi" and ToUnit == "inch":
    ToValue == float(round(FromValue*63360,7))
if FromUnit == "mi" and ToUnit == "ft":
    ToValue == float(round(FromValue*5280,7))
if FromUnit == "mi" and ToUnit == "yd":
    ToValue += float(round(FromValue*1760,7))
print(ToValue)