month_dict = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

time = input("Date: ").split("/")

while True:
    if len(time) == 3:
        month = int(time[0])
        day = int(time[1])
        year = int(time[2])
        print(f"{year}-{month:02}-{day:02}")
        break

    elif len(time) == 1:
        if not time[0].split(" ") == 3:
            time = input("Date: ").split(" ")
            continue
        time = time[0].split(" ")
        time[1] = time[1].replace(",","")
        month = int(month_dict[time[0]])
        day = int(time[1])
        year = int(time[2])
        print(f"{year}-{month:02}-{day:02}")
        break










