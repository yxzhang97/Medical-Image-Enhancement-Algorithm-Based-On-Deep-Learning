# invert .img to .nii

import nibabel as nb


def invert(name_img, name_nii):
    img = nb.load(name_img)
    nb.save(img, name_img.replace(name_img, name_nii))
    # nb.save(img, fname.replace('.img', '.nii'))
