import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe(.)*></iframe>$", s):
        s = s.split('"')
        for i in s:
            if i := re.search(r"^https?://(www\.)?youtube\.com/embed/.+$", i):
                return i.group(0)
    else:
        return None



if __name__ == "__main__":
    main()