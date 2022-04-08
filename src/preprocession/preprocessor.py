import numpy as np
import os
import shutil
from PIL import Image
import imagePiler

# for i in range(0, 100):
#     index_list = np.random.randint(0, 144, [30])
#     os.makedirs('/home/quindex/Downloads/pile/' + str(i))
#     imagePiler.pile_image('/home/quindex/Downloads/slices/', '/home/quindex/Downloads/pile/' + str(i) + '/', index_list)
#
for i in range(0, 100):
    flag = np.random.randint(0, 7);
    shutil.copy('/home/quindex/Downloads/DPED-master/dped/iphone/training_data/iphone' + str(flag) + '/' + str(i) + '.png',
                '/home/quindex/Downloads/DPED-master/dped/iphone/training_data/iphone/' + str(i) + '.png')
    shutil.copy('/home/quindex/Downloads/DPED-master/dped/iphone/training_data/canon' + str(flag) + '/' + str(i) + '.png',
                '/home/quindex/Downloads/DPED-master/dped/iphone/training_data/canon/' + str(i) + '.png')

# for j in range(0, 7):
#     for i in range(0, 100):
#         shutil.copy('/home/quindex/Downloads/groundTruth/result_' + str(j) + '.png',
#                     '/home/quindex/Downloads/DPED-master/dped/iphone/training_data/canon' + str(j) + '/' + str(i) + '.png')

# for ind in range(0, 100):
#     index_list = np.random.randint(0, 144, [30])
#     R = [[0] * 64 for i in range(64)]
#     G = [[0] * 64 for i in range(64)]
#     B = [[0] * 64 for i in range(64)]
#     im = Image.new('RGB', (64, 64))
#     weight = len(index_list)
#     # print(index_list)
#     for index in index_list:
#         img = Image.open('/home/quindex/Downloads/slices/' + str(index).zfill(3) + '/7.png')
#         pix = img.convert("RGB")
#         x = 0
#         while x < 64:
#             y = 0
#             while y < 64:
#                 r, g, b = pix.getpixel((x, y))
#                 R[x][y] += r
#                 G[x][y] += g
#                 B[x][y] += b
#                 y += 1
#             x += 1
#     for i in range(0, 64):
#         for j in range(0, 64):
#             R[i][j] /= weight
#             G[i][j] /= weight
#             B[i][j] /= weight
#             im.putpixel((i, j), (int(R[i][j]), int(G[i][j]), int(B[i][j])))
#     im.save('/home/quindex/Downloads/DPED-master/dped/iphone/training_data/iphone7/' + str(ind) + '.png')