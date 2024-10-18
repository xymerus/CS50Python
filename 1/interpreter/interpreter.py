# input
number = input("Expression: ")
# excute(one decimal place)
x, y, z = number.split(" ")
x = float(x)
z = float(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    if z != 0:
        result = x / z
    else :
        raise ValueError("Cannot divide by zero.") 

print(f"{result:.1f}")