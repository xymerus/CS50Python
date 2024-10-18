import sys
# get uses' time and answer waht to eat
def main():
    time = input("What time is it? ")
    value = round(convert(time), 1)
    if value >= 7.0 and value <= 8.0:
        print("breakfast time")
    elif value >= 12.0 and value <= 13.0:
        print("lunch time")
    elif value >= 18.0 and value <= 19.0:
        print("dinner time")
    else:
        sys.exit()


# convert ##:## to ##.#
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    value = hours + minutes
    return value


if __name__ == "__main__":
    main()