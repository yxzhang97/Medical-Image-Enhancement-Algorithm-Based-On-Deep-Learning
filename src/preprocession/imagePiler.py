# pile a series of .png images together, result saved as a .png image

from PIL import Image


def pile_image(img_dir, save_dir, index_list):
    seq = 0
    while seq <= 11:
        # num_list = [ [0] * 5 for i in range(2)]
        R = [[0] * 64 for i in range(64)]
        G = [[0] * 64 for i in range(64)]
        B = [[0] * 64 for i in range(64)]
        im = Image.new('RGB', (64, 64))
        weight = len(index_list)
        for index in index_list:
            img = Image.open(img_dir + str(index).zfill(3) + '/' + str(seq) + '.png')
            pix = img.convert("RGB")
            x = 0
            while x < 64:
                y = 0
                while y < 64:
                    r, g, b = pix.getpixel((x, y))
                    R[x][y] += r
                    G[x][y] += g
                    B[x][y] += b
                    y += 1
                x += 1
        for i in range(0, 64):
            for j in range(0, 64):
                R[i][j] /= weight
                G[i][j] /= weight
                B[i][j] /= weight
                im.putpixel((i, j), (int(R[i][j]), int(G[i][j]), int(B[i][j])))
        im.save(save_dir + str(seq) + ".png")
        seq += 1

    # im = Image.new("RGB", (x, y))   #创建图片
    # file = open('flag.txt')    #打开rbg值的文件
    # 通过每个rgb点生成图片
    # for i in range(0, x):
    #     for j in range(0, y):
    #         line = file.readline()  #获取一行的rgb值
    #         rgb = line.split(", ")  #分离rgb，文本中逗号后面有空格
    #         im.putpixel((i, j), (int(rgb[0]), int(rgb[1]), int(rgb[2])))    #将rgb转化为像素
    #
    # im.show()   #也可用im.save('flag.jpg')保存下来
