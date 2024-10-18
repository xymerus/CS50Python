def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    vowels = "aeiouAEIOU"
    output = ""
    for letter in word:
        if letter not in vowels:
            output += letter
    return output

if __name__ == "__main__":
    main()