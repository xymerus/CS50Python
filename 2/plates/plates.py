def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # 1. 长度在2到6之间
    if not (2 <= len(plate) <= 6):
        return False

    # 2. 至少以两个字母开头
    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    # 3. 车牌号中没有标点符号
    for char in plate:
        if not char.isalnum():  # 不是字母或数字
            return False

    # 4. 数字之后不能出现字母
    has_number_started = False  # 初始化，表示目前还没遇到数字

    for char in plate:  # 遍历车牌号中的每个字符
        if char.isdigit():  # 检查当前字符是否为数字
            has_number_started = True  # 如果遇到了数字，标记为 True
        elif has_number_started and char.isalpha():  # 如果数字已经出现且当前字符是字母
            return False  # 违反规则：数字后不能再出现字母，返回 False


    # 5. 如果车牌中有数字，数字不能以0开头
    number_found = False  # 标记是否找到了第一个数字
    for char in plate:
        if char.isdigit():
            if not number_found:  # 这是第一个出现的数字
                number_found = True
                if char == '0':  # 数字不能以0开头
                    return False
            # 继续检查其他数字
    
    return True

main()
