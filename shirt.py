from PIL import Image, ImageOps
import os
import sys

def main():
    wear_shirt()

def wear_shirt():
    if len(sys.argv) < 3:
        sys.exit("Too few arguements")
    if len(sys.argv) > 3:
        sys.exit("Too much arguements")
    if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".jpeg") and not sys.argv[1].endswith(".png"):
        sys.exit("Invalid input")   
    if not sys.argv[2].endswith(".jpg") and not sys.argv[2].endswith(".jpeg") and not sys.argv[2].endswith(".png"):
        sys.exit("Invalid input")
    if not os.path.splitext(sys.argv[1])[1] == os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")

    
    try:
        shirt = Image.open("shirt.png")
        muppet = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    muppet = ImageOps.fit(muppet, shirt.size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

if __name__ == "__main__":
    main()