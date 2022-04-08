# compare tow .png images, result saved as a .png image, black pixel means the same pixel between two images, white pixel
# means different pixel between two images

from PIL import Image


def compare_image(img1, img2, save_dir):
    R = [[0] * 64 for i in range(64)]
    G = [[0] * 64 for i in range(64)]
    B = [[0] * 64 for i in range(64)]
    im = Image.new('RGB', (64, 64))
    pix1 = img1.convert("RGB")
    pix2 = img2.convert("RGB")
    x = 0
    while x < 64:
        y = 0
        while y < 64:
            r1, g1, b1 = pix1.getpixel((x, y))
            r2, g2, b2 = pix2.getpixel((x, y))
            R[x][y] += r1 - r2
            G[x][y] += g1 - g2
            B[x][y] += b1 - b2
            y += 1
        x += 1
    diffCount = 0
    for i in range(0, 64):
        for j in range(0, 64):
            if R[i][j] != 0 or G[i][j] != 0 or B[i][j] != 0:
                R[i][j] = 200
                G[i][j] = 200
                B[i][j] = 200
                diffCount += 1
            im.putpixel((i, j), (int(R[i][j]), int(G[i][j]), int(B[i][j])))
    im.save(save_dir)
    print(diffCount / 64 ** 2)
