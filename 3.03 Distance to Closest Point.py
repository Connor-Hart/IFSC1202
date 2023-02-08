A = input("Enter point A: ")
B = input("Enter point B: ")
C = input("Enter point C: ")

x=0
Dist1 = int(A)-int(B)
Dist2 = int(A)-int(C)
if Dist1<Dist2:
    x=Dist1
if Dist2<Dist1:
    x=Dist2
print(abs(x))