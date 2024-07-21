from PIL import ImageDraw, Image, ImageFont


def replacecode(code):
    code = code.replace('\n', '')
    code = code.replace(' ', '')
    code = code.replace('9', '')
    code = code.replace('K', '13')
    code = code.replace('Q', '12')
    code = code.replace('J', '11')
    code = code.replace('A', '1')
    return code


def replacecode_0(code):
    code = replacecode(code)
    for i in range(len(code)):
        if code[i] != '1':
            code = code.replace(code[i], '0')
    return code


def decode(code):
    codelist = []

    while (len(code) >= 9):
        codelist.append(list(code[0:9]))
        code = code[9:]
    while (len(code) in range(1, 9)):
        code = code + 'x'
    if len(code) != 0:
        codelist.append(list(code))
    return codelist


def printimage(codelist):
    # 定义一个函数，根据列表生成九宫格图片
    def generate_sudoku_image(list):
        # 将列表转换为字符串
        code = ''.join(list)
        print(code)
        # 创建一个空白的正方形图片
        image = Image.new('RGB', (300, 300), (255, 255, 255))
        # 创建一个绘图对象
        draw = ImageDraw.Draw(image)
        # 设置字体和颜色
        font = ImageFont.truetype('arial.ttf', 100)
        color = (0, 0, 0)
        # 循环绘制数字
        for i in range(9):
            # 计算数字的位置
            x = (i % 3) * 100 + 25
            y = (i // 3) * 100 + 10
            # 绘制数字
            draw.text((x, y), code[i], font=font, fill=color)
        # 返回图片对象
        return image

    # 定义一个列表

    # 循环生成九宫格图片，并保存到本地
    for i in range(len(codelist)):
        # 调用函数，生成图片对象
        image = generate_sudoku_image(codelist[i])
        # print(codelist[i])
        # 保存图片到本地
        image.save('heiji' + str(i + 1) + '.png')
    return i


def main():
    code = '''A23A34J\n
            65K3Q3Q\n
            QJKA5AJ\n
            AJ39JKJ\n
            4A6AQ53\n
            AA2A4JA\n
            AAA52JA\n'''
    code = replacecode(code)
    # code = replacecode_0(code)
    codelist = decode(code)
    printimage(codelist)


if __name__ == "__main__":
    main()
