Fraction = input("Fraction: ")

# calculate
x, y = Fraction.split(sep="/")
while not (x.isdigit() and y.isdigit()):
    Fraction = input("Fraction: ")
    x, y = Fraction.split(sep="/")

while y == "0":
    Fraction = input("Fraction: ")
    x, y = Fraction.split(sep="/")    



x = int(x)
y = int(y)
tank = x / y
tank = round(tank, 2)

# turn into ##%
tank = tank * 100
print(f"{tank}%")