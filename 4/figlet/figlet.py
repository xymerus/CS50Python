from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
codes = ""

if len(sys.argv) == 1:
    codes = input("Input: ")
    f = figlet.getFonts()
    f = random.choice(f)
    figlet.setFont(font=f)
    print("Output:", figlet.renderText(codes))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    codes = input("Input: ")
    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        print("Output:", figlet.renderText(codes))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")