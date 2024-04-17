def f1():
    from PIL import Image
    image = Image.open('lemon.jpg')
    image.show()
    print(f"Размер: {image.size}")
    print(f"Размер: {image.format}")
    print(f"Размер: {image.mode}")

def f2():
    from PIL import Image
    image = Image.open('lemon.jpg')
    image.show()
    res_img2 = image.reduce(3)
    res_img2 = res_img2.transpose(Image.FLIP_LEFT_RIGHT)
    res_img2 = res_img2.transpose(Image.FLIP_TOP_BOTTOM)
    res_img2.save('coplemoon.jpg')

def f3():
    from PIL import Image, ImageFilter
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for img in images:
        image = Image.open(img)
        img_fil = image.filter(ImageFilter.EMBOSS)
        img_fil.save('filters' + str(img))
def f4():
    from PIL import Image
    def wm(im, outpath, wat, pos):
        base_image = Image.open(im)
        watermark = Image.open(wat)
        base_image.paste(watermark, pos)
        base_image.show()
        base_image.save(outpath)
    if __name__ == '__main__':
        wm('lemon.jpg', 'lemonwm.jpg', 'water.jpg', (0, 0))
f4()
