def z1():
    from PIL import Image
    def crop(image, xy, image2):
        img = Image.open(image)
        cropimg = img.crop(xy)
        cropimg.save(image2)
    crop("cake.jpg", (0, 80, 200, 400), "cake2.jpg")
def z2():
    from PIL import Image
    hol = {'День рождения': 'cake.jpg', '8 Марта': '8марта.jpg',
           'Новый Год': '2024.jpg', 'День Святого Валентина': '14fev.jpg'}
    a = str(input('К какому празднику нужна открытка? '))
    if a in hol:
        img4 = Image.open(hol[a])
        img4.show()
    else:
        print('Открытки для этого праздника, к сожалению, нет.')
def z3():
    from PIL import Image, ImageDraw, ImageFont
    a = str(input('Введите имя человека, которому хотите отправить открытку '))
    image = Image.open("cake.jpg")
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 18), a, font=font, fill='red')
    drawer.text((105, 18), ", поздравляю!", font=font, fill='red')
    image.save('new_img.jpg')
    image.show()

z3()