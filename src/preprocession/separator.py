# separate a .nii file into a series of .png images

import nibabel as nib
import numpy as np
import imageio
import os

def read_niifile(niifile):  # 读取niifile文件
    img = nib.load(niifile)  # 下载niifile文件（其实是提取文件）
    img_fdata = img.get_fdata()  # 获取niifile数据
    return img_fdata


def save_fig(file):  # 保存为图片
    fdata = read_niifile(file)  # 调用上面的函数，获得数据
    print(fdata.shape)
    (x, y, z, p) = fdata.shape  # 获得数据shape信息：（长，宽，维度-切片数量）
    for k in range(z):
        silce = fdata[ :, :, k]  # 三个位置表示三个不同角度的切片
        # imageio.imwrite(os.path.join(savepicdir, '{}.png'.format(k)), silce)
        imageio.imwrite(os.path.join(savepicdir, '{}.jpg'.format(k)), silce)
        # 将切片信息保存为png格式


dir = '/home/quindex/Downloads/niis/000.nii'  # nii的路径
savepicdir = '/home/quindex/Downloads/temp'  # 保存png的路径
if(os.path.exists(savepicdir) == 0):
    os.mkdir(savepicdir)  # 创建文件夹
save_fig(dir)  # 运行程序，保存为图像

# index  = 0
# while index <= 143:
#     dir = '/home/quindex/Downloads/niis/' + str(index).zfill(3) + '.nii'  # nii的路径
#     savepicdir = '/home/quindex/Downloads/slices/' + str(index).zfill(3)  # 保存png的路径
#     if (os.path.exists(savepicdir) == 0):
#         os.mkdir(savepicdir)  # 创建文件夹
#     save_fig(dir)  # 运行程序，保存为图像
#     index += 1