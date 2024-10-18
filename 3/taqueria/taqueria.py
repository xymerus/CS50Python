menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0


# input food, lowercase, 
try:
    while True:
        item = input("Item: ").title()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
        elif item == "":
            print(f"Total: ${total}")
            break
        else:
            print("We can not find that, please try again")

    



except EOFError:
    print(f"Total: ${total}")