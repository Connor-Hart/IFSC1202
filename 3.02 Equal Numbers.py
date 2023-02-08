x = input("Enter the first number: ")
y = input("Enter the second number: ")
z = input("Enter the third number: ")

if x==y==z:
    print(3)
    if x!=y!=z:
        if x==y or x==z or y==z:
            print(2)
        else:
            print(0)
