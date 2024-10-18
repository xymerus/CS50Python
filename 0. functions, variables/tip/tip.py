def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
# remove $ and turn str into float with one float
    dollars = float(dollars.removeprefix("$").removesuffix("0"))
    return dollars

def percent_to_float(percent):
    percent = float(percent.removesuffix("%")) * 0.01
    return percent

main()