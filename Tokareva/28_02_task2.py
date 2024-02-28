a = " "
print("Введите слова: ")
while a[-5:] != "stop ":
    i = str(input())
    a += i
    a += " "
print(a[:-5])