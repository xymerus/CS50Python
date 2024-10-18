import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    
    if not os.path.splitext(sys.argv[1])[1] == ".py":
        sys.exit("Not a Python file")

    try:
        file_path = sys.argv[1]
        number_lines = get_lines(file_path)
        print(number_lines)
    except FileNotFoundError:
        print("File does not exist")
    


def get_lines(file_path):
    lines = 0
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                lines += 1
    return lines

if __name__ == "__main__":
    main()