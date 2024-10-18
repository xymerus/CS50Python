while True:
    Fraction = input("Fraction: ")
    
    # 尝试分割输入并转换为整数
    try:
        x, y = Fraction.split(sep="/")
        x = int(x)
        y = int(y)

        # 检查分母是否为 0，避免除以 0 的错误
        if y == 0:
            print("Denominator cannot be 0. Please try again.")
            continue

        # 如果输入有效，跳出循环
        break
    except ValueError:
        print("Invalid input. Please enter in the format 'numerator/denominator'.")

# 计算分数
tank = x / y
tank = round(tank, 2)

# 转换为百分比格式
tank = tank * 100
print(f"{tank}%")
