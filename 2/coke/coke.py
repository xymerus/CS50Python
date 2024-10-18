Insert_coin = int(input("Inser_coin: "))
Amount_Due = 50 - Insert_coin

while True:
    if Insert_coin < 50:
        print(f"Amount Due: {Amount_Due}")
        Insert_coin = Insert_coin + int(input("Inser_coin: "))
        Amount_Due = 50 - Insert_coin
    else:
        break

print(f"Change Owed: {Insert_coin - 50}")



