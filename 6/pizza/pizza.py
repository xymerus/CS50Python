import sys
import tabulate
import csv

def main():
    pizza()

def pizza():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    
    file = sys.argv[1]
    
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            pizza_list = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate.tabulate(pizza_list[1:], headers=pizza_list[0], tablefmt="grid"))

if __name__ == "__main__":
    main()


