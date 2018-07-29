# coding=utf-8  
' 蒋方正Python函数库 '  
__author__ = 'Sandeepin'  
  
import math  
import os  
from PIL import Image  
  
# 功能：博客图片生成缩略图，1280横屏压缩，1000竖屏压缩  
# 参数：图片名称  
# 返回：OK，保存同名文件在thumb目录下  
def JfzBlogImgThumb(ImgName, ImgName2):  
    im = Image.open(ImgName)  
    # print('格式',im.format, '，分辨率',im.size, '，色彩',im.mode)  
    # print len(im.split())
    if max(im.size[0], im.size[1]) > 1000:  
        if im.size[0] > im.size[1]:  
            im.thumbnail((1280, 1280))
        else:  
            im.thumbnail((1000, 1000))
        l = im.split()
        if len(l) == 4:
            #prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = l
            im = Image.merge("RGB", (r, g, b))
        im.save(ImgName2, 'JPEG', quality=90)
    return 'OK'  
  
def main():
    # JfzBlogImgThumb('1.jpg')  
    # JfzBlogImgThumb('2.jpg')  
    
    # 列出当前目录所有jpg文件  
    lst=os.listdir(os.getcwd())  
    imgname = [c for c in lst if os.path.isfile(c) and c.endswith('.jpg')]  
    print(imgname)  
    
    # 全处理  
    JfzBlogImgThumb(imgname[0],'thumb\\'+imgname[0])


if __name__ == '__main__':
    main()