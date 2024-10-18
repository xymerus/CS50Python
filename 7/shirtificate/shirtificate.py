import fpdf

def main():
    shirtificate()

def shirtificate():
    name = input("Name: ")
    shirt = fpdf.FPDF(orientation="P", unit="mm", format="A4")
    shirt.add_page()
    
    # 设置主标题
    shirt.set_font("helvetica", "B", 40)
    shirt.cell(0, 60, "CS50 Shirtificate", align="C")
    
    # 插入图像
    shirt.image("shirtificate.png", x=10, y=70, w=190)
    
    # 设置字体颜色为白色
    shirt.set_text_color(255, 255, 255)  # RGB颜色，255, 255, 255为白色
    
    # 设置Y坐标，使文本放置在胸口处
    shirt.set_y(140)  # 上移文本位置，可以根据需要调整
    
    # 设置字体变大
    shirt.set_font("helvetica", "B", 30)  # 字体大小为30
    
    # 插入文本
    shirt.cell(0, 10, f"{name} took CS50", align="C")
    
    # 输出PDF
    shirt.output("myshirtificate.pdf")

if __name__ == "__main__":
    main()
