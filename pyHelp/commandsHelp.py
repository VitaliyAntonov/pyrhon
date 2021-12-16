


class ListHelp:
    """ Основные методы работы со списками"""

    def __init__(self):
        pass







if __name__ == '__main__':

    # Варианты записи цикла for
    # Поэлементный обход списка
    for i in [1, 2, 3]:
        print(i)

    print('')
    # Посимвольный обход строки
    for ch in "Hi!":
        print(ch)

    print('')
    # Указание количества итераций
    for num in range(5):
        print('Head First Rocks!')

    print('класс '+ListHelp.__name__ + ': ' + ListHelp.__doc__)





