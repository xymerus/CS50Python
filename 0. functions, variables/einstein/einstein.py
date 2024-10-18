def main():
    E = Energe()
    print("E:", E)


# def calculate fuction
def Energe():
    m = int(input("m: "))
    c = 300000000
    E = m * c * c
    return E
    
main()


