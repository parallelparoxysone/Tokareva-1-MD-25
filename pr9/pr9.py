def z1():
    import os
    from PIL import Image
    fol1 = 'first'
    fol2 = 'second'
    for file_name in os.listdir(fol1):
            image_path = os.path.join(fol1, file_name)
            img = Image.open(image_path)
            img = img.rotate(90)
            destination_path = os.path.join(fol2, file_name)
            img.save(destination_path)
    print('Изображения обработаны и сохранены в папке:', fol2)

def z2():
    import os
    from PIL import Image
    fol1 = 'first'
    fol2 = 'second'
    for file_name in os.listdir(fol1):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            image_path = os.path.join(fol1, file_name)
            img = Image.open(image_path)
            img = img.rotate(90)
            destination_path = os.path.join(fol2, file_name)
            img.save(destination_path)
    print('Изображения обработаны и сохранены в папке:', fol2)
def z3():
    import csv
    def f(filename):
        total = 0
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print("Нужно купить:")
            for row in reader:
                pr, quantity, price = row
                cost = int(quantity) * int(price)
                total += cost
                print(f"{pr} - {quantity} шт. за {price} руб.")
            print(f"Итоговая сумма: {total} руб.")

    file_name = 'Книга1.csv'
    f(file_name)
z3()