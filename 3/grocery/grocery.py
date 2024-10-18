try:
    list = {}
    while True:
        item = input().upper()

        
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

       

except EOFError:

    list_sorted = sorted(list.items(), key = lambda x : x[0])

    for key, value in list_sorted:
        print(f"{value} {key.upper()}")

