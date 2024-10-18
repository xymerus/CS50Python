def main():
    greeting = input("Greeting: ")
    value(greeting)

def value(greeting):
    G = greeting.strip().upper()

    if G[:5] == "HELLO":
        z = "$0"
        print(z)
    elif G[0] == "H":
        z = "$20"
        print(z)
    else:
        z = "$100"
        print(z)
    return z

if __name__ == "__main__":
    main()