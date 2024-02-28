import random
def f():
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  return num1, num2
def check(num1, num2, user):
    answer = num1 + num2
    if user == answer:
        print("Правильно!")
        return True
    else:
        print("Ответ Неверный")
        return False
corr = 0
mist = 0
while mist < 3:
    num1, num2 = f()
    user = int(input(f"{num1} + {num2} = "))
    if check(num1, num2, user):
        corr+= 1
    else:
        mist += 1
print("Игра окончена. Правильных ответов: ", corr)