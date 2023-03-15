a = '1.3.5.7.9.10.5.3.7'.split('.')
for i in range(0, len(a)):
    if i%2 != 0:
        print(a[i])