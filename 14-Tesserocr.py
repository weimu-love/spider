# -*- coding: utf-8 -*-
"""
   File Name：     14-Tesserocr
   Description :    tesseract windows环境下安装常见问题及解决: https://blog.csdn.net/weixin_41982136/article/details/82747499
                    还得把tessdata拷贝到anaconda目录下： https://blog.csdn.net/u011192409/article/details/80415370
   date：          2020/2/12
"""
import tesserocr
from PIL import Image

# image = Image.open('image.png')
# # print(tesserocr.image_to_text(image))
# print(tesserocr.file_to_text('image.png'))

image = Image.open('code.jpg')
# 转为灰度图像
image = image.convert('L')
# 进行二值化处理
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# image.show()

result = tesserocr.image_to_text(image)
print(result)
