from PIL import Image

im = Image.open("35.jpg")
w, h = im.size
print('Original image size: %sx%s'%(w,h))
im.thumbnail((w/2,h/2))
im.save("thumbnail.jpeg","jpeg")


from PIL import Image,ImageFilter
im2 = Image.open("35.jpg")
im2.filter(ImageFilter.BLUR)
im2.save("blur.jpeg","jpeg")

im3 = Image.open("35.jpg")
im3.filter(ImageFilter.GaussianBlur)
im3.save("Gaussianblur.jpeg","jpeg")
