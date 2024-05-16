def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"В ресторане '{self.restaurant_name}'  {self.cuisine_type} кухня.")
        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")
    newRestaurant = Restaurant("Guisto", "итальянская")
    print(f"Название ресторана: {newRestaurant.restaurant_name}")
    print(f"Тип кухни: {newRestaurant.cuisine_type}")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"В ресторане '{self.restaurant_name}' {self.cuisine_type} кухня.")

        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")
    restaurant1 = Restaurant("Miu Miu", "французская")
    restaurant2 = Restaurant("Changi", "азиатская")
    restaurant3 = Restaurant("Rouge", "итальянская")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rat):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rat = rat
        def describe_restaurant(self):
            print(f"В ресторане  '{self.restaurant_name}' {self.cuisine_type} кухня. Рейтинг: {self.rat}")
        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")
        def update_rating(self, new_rat):
            self.rat = new_rat
            print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен: {self.rat}")

    restaurant1 = Restaurant("Miu Miu", "французская", 4.5)
    restaurant2 = Restaurant("Changi", "азиатская", 4.8)
    restaurant3 = Restaurant("Rouge", "итальянская", 4.9)
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    restaurant1.update_rating(4.7)
    restaurant1.describe_restaurant()
z3()