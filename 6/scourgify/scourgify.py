import sys
import csv
import os


def main():
    scourgify()

def scourgify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    if not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.isfile(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")
    
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        with open(sys.argv[2], "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first, "last": last, "house": house})

if __name__ == "__main__":
    main()