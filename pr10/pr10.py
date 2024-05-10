def z1():
    import json
    with open('products.json') as file:
        data = json.load(file)
    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии")
        print()
def z2():
    import json

    def new():
        newp = {}
        newp['name'] = input("Введите название продукта: ")
        newp['price'] = int(input("Введите цену продукта: "))
        newp['weight'] = int(input("Введите вес продукта: "))
        newp['available'] = input("Продукт в наличии? (да/нет): ").lower() == 'да'

        with open('products.json', 'r') as file:
            data = json.load(file)
        data['products'].append(newp)
        with open('products.json', 'w') as file:
            json.dump(data, file, indent=4)
    new()

    with open('products.json') as file:
        data = json.load(file)

    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии")
        print()

def z3():
    dictt = {}
    with open('en-ru.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            en, ru_translations = line.strip().split(' - ')
            ru_words = [ru.strip() for ru in ru_translations.split(',')]
            for ru_word in ru_words:
                if ru_word in dictt:
                    dictt[ru_word].append(en)
                else:
                    dictt[ru_word] = [en]

    sorteddictt = dict(sorted(dictt.items()))

    with open('ru-en.txt', 'w') as file:
        for ru_word, en_words in sorteddictt.items():
            file.write(f"{ru_word} - {', '.join(en_words)}n")
z2()