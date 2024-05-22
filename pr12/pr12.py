def z1():
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
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, rat, flavors):
            super().__init__(restaurant_name, cuisine_type, rat)
            self.flavors = flavors
        def display_flavors(self):
            print("Вкусы мороженого: ")
            for flavor in self.flavors:
                print(flavor)

    restaurant1 = Restaurant("Miu Miu", "французская", 4.5)
    restaurant2 = Restaurant("Changi", "азиатская", 4.8)
    restaurant3 = Restaurant("Rouge", "итальянская", 4.9)
    ice_cream_stand = IceCreamStand("Mussy", "мороженое", 4.8, ["Ванильное", "Шоколадное", "Клубничное", "Мятное"])
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
    ice_cream_stand.describe_restaurant()
    restaurant1.update_rating(4.7)
    restaurant1.describe_restaurant()
    ice_cream_stand.display_flavors()

def z2():
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

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, rat, flavors, location, hours):
            super().__init__(restaurant_name, cuisine_type, rat)
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def describe_ice(self):
            print(f"В ресторане  '{self.restaurant_name}' {self.cuisine_type} кухня. Рейтинг: {self.rat}. Локация: {self.location}. Часы работы: {self.hours}")
        def display_flavors(self):
            print("Вкусы мороженого: ")
            for flavor in self.flavors:
                print(flavor)
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f"Добавлен новый вкус мороженого: {flavor}")
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"Удален вкус мороженого: {flavor}")
            else:
                print(f"Вкус мороженого '{flavor}' отсутствует")
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"Вкус мороженого '{flavor}' в наличие")
            else:
                print(f"Вкуса мороженого '{flavor}' нет в наличии")
        def popsicle_ice_cream(self):
            print("Мороженое на палочке")
        def soft_serve_ice_cream(self):
            print("Мягкое мороженое")

    restaurant1 = Restaurant("Miu Miu", "французская", 4.5)
    restaurant2 = Restaurant("Changi", "азиатская", 4.8)
    restaurant3 = Restaurant("Rouge", "итальянская", 4.9)
    ice_cream_stand = IceCreamStand("Mussy", "мороженое", 4.8, ["Ванильное", "Шоколадное", "Клубничное", "Мятное"], "Санкт-Петербург", "09:00-20:00")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
    ice_cream_stand.describe_ice()
    restaurant1.update_rating(4.7)
    restaurant1.describe_restaurant()
    ice_cream_stand.display_flavors()

def z3():
    import tkinter as tk
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
    class IceCreamGUI:
        def __init__(self, master, ice_cream_stand):
            self.master = master
            self.ice_cream_stand = ice_cream_stand

            self.master.title(f"{self.ice_cream_stand.name} Menu")

            self.label = tk.Label(self.master, text="Выберите вкус мороженого:")
            self.label.pack()

            self.selected_flavors = []
            for flavor in self.ice_cream_stand.flavors:
                flavor_var = tk.BooleanVar()
                flavor_checkbox = tk.Checkbutton(self.master, text=flavor, variable=flavor_var, onvalue=True,
                                                 offvalue=False)
                flavor_checkbox.pack()
                self.selected_flavors.append((flavor, flavor_var))

            self.confirm_button = tk.Button(self.master, text="Подтвердить", command=self.show_selected_flavors)
            self.confirm_button.pack()
        def show_selected_flavors(self):
            selected_flavors = [flavor[0] for flavor in self.selected_flavors if flavor[1].get()]
            message = f"Выбранные вкусы мороженого: {', '.join(selected_flavors)}"
            popup = tk.Toplevel()
            popup.title("Выбранные вкусы")
            popup_label = tk.Label(popup, text=message)
            popup_label.pack()

    def main():
        flavors_list = ["Ваниль", "Шоколад", "Клубника", "Мята"]
        ice_cream_stand = IceCreamStand("Mussy", flavors_list)

        root = tk.Tk()
        app = IceCreamGUI(root, ice_cream_stand)
        root.mainloop()

    if __name__ == "__main__":
        main()
z3()

