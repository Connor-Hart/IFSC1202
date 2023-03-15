day = 0
price = 0
def percentage(n):
    value = ((curprice-price)/price)*100
    return(float(value))

stockfile = open("06.02 Stock.txt", "r")
x = stockfile.readline()
print("{:>10s} {:>10s}".format("Price", "Change"))
while x != "" and day == 0:
    price = float(x)
    print("{:>10.2f}".format(price))
    day += 1
    x = stockfile.readline()

while x != "" and day != 0:
    curprice = float(x)
    a = float(percentage(curprice))
    price = float(x)
    print("{:>10.2f} {:>10.2f}".format(price, a))
    x = stockfile.readline()