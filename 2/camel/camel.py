# get input
def main():
    camelcase = input("camelCase: ")
    snake_case = convert(camelcase)
    print(f"snake_case: {snake_case}")


# define convert function
def convert(camelcase):
# interate: if is capital, lower it and plus "_" behind this letter
    snake_case = ""
    for letter in camelcase:
        if letter.isupper():
            letter = "_" + letter.swapcase()
            snake_case += letter
        else:
            snake_case += letter
    return snake_case


main()