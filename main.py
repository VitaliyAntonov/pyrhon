# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Репозиторий сообщества Python - библиотеки модулей :  https://pypi.org/

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

# Импорт модуля
from datetime import datetime
import time
import random

# Вывод 20-ти случайных чисел в диапазоне от 0 до 5
for ct in range(20):
    print(random.randint(0, 5))

# задержка на 5 секунд
time.sleep(5)

# Создание списка
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# Значение счётчика минут
right_this_minute = datetime.today().minute

seconds = datetime.second
microseconds = datetime.microsecond

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
