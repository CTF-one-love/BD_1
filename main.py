import time
from colorama import init, Fore, Back, Style

#fdsd
def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("               **    **  ********  **        **            **      ")
    print("              **    **  ********  **        **         **     **   ")
    print("             ********  **        **        **         **      **  ")
    print("            ********  ********  **        **         **      **  ")
    print("           **    **  **        **        **         **      **  ")
    print("          **    **  ********  ********  ********    **    **   ")
    print("         **    **  ********  ********  ********       **      ")
console_picture()


def calculate_total_price(apples):
    total_price = 0
    for price in apples.values():
        total_price += int(price)
    return total_price

def draw_apple_outline():
    print("   ********^^*")
    print(" **          **")
    print("**           **")
    print("**           **")
    print("**           **")
    print("**           **")
    print(" **         **")
    print("   *********")

print("Введите количество яблок.")
apple_count= int(input())
print(f"У вас {apple_count} яблок.")
apples = dict()
print("Укажите, какого сорта яблоко по очереди:")
for i in range(0, int(apple_count)):
    type_apple = input()
    apples[type_apple] = None

print("Теперь укажите цену за каждое яблоко.")
for type_apple in apples:
    price = input()
    apples[type_apple] = price

print("Ваши яблоки и их цены:")
for type_apple, price in apples.items():
    print(f"{type_apple}: {price}")

total_price = calculate_total_price(apples)
print(f"Общая стоимость всех яблок: {total_price}")

print("Загрузка данных в базу данных...")
for i in range(1, 11):
    time.sleep(0.5)
    print(f"Загружено {i*10}% данных...")
print("Загрузка данных завершена.")

print("Напишите пароль содержащий цифры сумма которых даст 13:")
prol = 1
mam = 0
while prol != 13:
    stree = str(input())
    for i in range(0,len(stree)):
        mam += int(stree[i])
    prol = mam
    if prol == 13:
        print("Вы вошли в систему.")
    else:
        print("Попробуйте еще раз.")