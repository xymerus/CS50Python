# get users' input
greet = input("Greeting: ")

# change the shape of users' input
G = greet.strip().upper()

# check "hello"$0 or "h(not hello)"$20 or others$100
if G[:5] == "HELLO":
    print("$0")
elif G[0] == "H":
    print("$20")
else :
    print("$100")
