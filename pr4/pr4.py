def z1():
    def f(n):
        if n % 5 == 0:
            return "Число делится на 5"
        return "Число не делится на 5"

    a = int(input("Введите число: "))
    print(f(a))

def z2():
    def f():
        try:
            a = int(input("Введите число: "))
            if 300 % a == 0:
                print("Результат деления: ", 300 // a)
            else:
                print("300 не делится на число ", a)
        except ValueError:
            print("Ошибка. Вводить не число запрещено.")
        except ZeroDivisionError:
            print("Ошибка. Вводить ноль запрещено.")
    f()

def z3():
    def f(a, b, c):
        if a*b == int(c[-2:]):
           return True
        return False
    a = int(input("Введите день: "))
    b = int(input("Введите месяц: "))
    c = str(input("Введите год: "))
    print(f(a, b, c))

def z4():
    def g(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum
    def f(n):
        if len(n) % 2 != 0:
            return "Неверно введен номер билета. Попробуйте еще раз."
        half = len(n) // 2
        half1 = int(n[:half])
        half2 = int(n[half:])
        if g(half1) == g(half2):
            return "Поздравляю! У Вас счастливый билет!"
        return "К сожалению, у Вас не счастливый билет."
    a = str(input("Введите номер вашего билета: "))
    print(f(a))



