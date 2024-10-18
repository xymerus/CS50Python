import inflect

try:
    p = inflect.engine()
    names = []
    while True:
        name = input("Name: ")
        names.append(name)
    

except EOFError:
    print(f"Adieu, adieu, to {p.join(names, sep=', ')}")
    exit()