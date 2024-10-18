import random


def main():
    level = get_level()
    score = get_score(level)
    print("Score:", score)



def get_level():
    level = int(input("Level: "))
    while True:
        if level == 1:
            return 1
        elif level == 2:
            return 2
        elif level == 3:
            return 3
        else:
            level = int(input("Level: "))



def generate_integer(level):

    if level == 1:
        score = 0

        for k in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            z = x + y
            answer = int(input(f"{x} + {y} = "))
            while answer!= z:
                count = 0
                print("EEE")
                answer = int(input(f"{x} + {y} = "))
                count += 1
                if count == 2:
                    print(f"{x} + {y} = {z}")
            if answer == z:
                score += 1
        print("Score:", score)

    elif level == 2:
        score = 0
        for k in range(10):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            z = x + y
            answer = int(input(f"{x} + {y} = "))
            while answer!= z:
                count = 0
                print("EEE")
                answer = int(input(f"{x} + {y} = "))
                count += 1
                if count == 2:
                    print(f"{x} + {y} = {z}")
            if answer == z:
                score += 1
        print("Score:", score)

    elif level == 3:
        score = 0
        for k in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            z = x + y
            answer = int(input(f"{x} + {y} = "))
            while answer!= z:
                count = 0
                print("EEE")
                answer = int(input(f"{x} + {y} = "))
                count += 1
                if count == 2:
                    print(f"{x} + {y} = {z}")
            if answer == z:
                score += 1
        print("Score:", score)

def get_score(level):
    score = 0
    for k in range(10):
        count = 0
        x = random.randint(10**(level-1), 10**level-1)
        y = random.randint(10**(level-1), 10**level-1)
        z = x + y
        answer = int(input(f"{x} + {y} = "))
        while answer != z:
            print("EEE")
            answer = int(input(f"{x} + {y} = "))
            count += 1
            if count == 2:
                print(f"{x} + {y} = {z}")
                break

        if answer == z:
            score += 1
    return score


if __name__ == "__main__":
    main()




    