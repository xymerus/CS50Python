import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # 匹配时间格式
    if match := re.search(r"^([0-9]{1,2}):?([0-9]{0,2}) (AM|PM) to ([0-9]{1,2}):?([0-9]{0,2}) (AM|PM)$", s):
        match1 = int(match.group(1))
        match2 = int(match.group(2)) if match.group(2) else 0  # 默认分钟为 0
        match4 = int(match.group(4))
        match5 = int(match.group(5)) if match.group(5) else 0  # 默认分钟为 0

        # 检查小时和分钟是否合法
        if match1 > 12 or match4 > 12:
            return "Invalid"
        if match2 >= 60 or match5 >= 60:  # 检查分钟是否合法
            return "Invalid"

        # 处理 AM/PM 转换
        if match.group(3) == "PM" and match1 != 12:
            match1 += 12
        elif match.group(3) == "AM" and match1 == 12:
            match1 = 0

        if match.group(6) == "PM" and match4 != 12:
            match4 += 12
        elif match.group(6) == "AM" and match4 == 12:
            match4 = 0

        # 返回24小时制时间格式
        return f"{match1:02}:{match2:02} to {match4:02}:{match5:02}"

    else:
        return "Invalid"

if __name__ == "__main__":
    main()
