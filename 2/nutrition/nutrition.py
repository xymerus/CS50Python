# creat a dictionary to store datas
FDA = {"apple":130, "banana":110, "grapefruit":60, "honeydewmelon":50, "lemon":15}

# get uses' fruits and output calaries
fruit = input("Item: ").lower()

if fruit in FDA:
    print(f"Calories: {FDA[fruit]}")
else:
    print("can not find such a fruit in our database")