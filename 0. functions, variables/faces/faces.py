# def main function get input
def main():
    convert()
    
# def transform function
def convert():
    A = input()
    
    B = A.replace(":)", "🙂").replace(":(", "☹️")

    print(B)
# print

main()
