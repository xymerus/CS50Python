from datetime import date
import inflect


def main():
    time = input("Date of Birth: ")
    print(convert_to_minutes(time))


def convert_to_minutes(time):
    birth_years, birth_months, birth_days = map(int, time.split('-'))
    today = date.today()

    

    minutes = (today - date(birth_years, birth_months, birth_days)).days * 24 * 60



    if minutes < 0:
        raise ValueError("Invalid date")


    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()