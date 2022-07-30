def count_args(*args):
    '''принимает произвольное количество аргументов и
    возвращает количество переданных в нее аргументов'''
    return len(args)


def test_count_args():
    if count_args() == 0:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    if count_args(10) == 1:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    if count_args('stepik', 'beegeek') == 2:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

    if count_args([], (''), 'a', 12, False) == 5:
        print("#test4 - ok")
    else:
        print("#test4 - fail")




def sq_sum(*args):
    '''принимает произвольное количество числовых
        аргументов и возвращает сумму их квадратов'''
    return sum(i ** 2 for i in args)


def test_sq_sum():
    if sq_sum() == 0:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    if sq_sum(2) == 4:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    if sq_sum(1.5, 2.5) == 8.5:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

    if sq_sum(1, 2, 3) == 14:
        print("#test4 - ok")
    else:
        print("#test4 - fail")

    if sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 385:
        print("#test5 - ok")
    else:
        print("#test5 - fail")




def mean(*args):
    '''принимает произвольное количество аргументов и
    возвращает среднее арифметическое переданных в нее
    числовых (int или float) аргументов'''
    res = [i for i in args if type(i) in (int, float)]
    if len(res) == 0:
        return 0.0
    return sum(res) / len(res)


def test_mean():
    if mean() == 0.0:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    if mean(7) == 7.0:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    if mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)) == 2.0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

    if mean(True, ['stepik'], 'beegeek', (1, 2)) == 0.0:
        print("#test4 - ok")
    else:
        print("#test4 - fail")

    if mean(-1, 2, 3, 10, ('5')) == 3.5:
        print("#test5 - ok")
    else:
        print("#test5 - fail")

    if mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 5.5:
        print("#test6 - ok")
    else:
        print("#test6 - fail")




def greet(name, *args):
    '''принимает произвольное количество аргументов
    строк имен (как минимум одно) и возвращает приветствие'''
    if len(args) == 0:
        return 'Hello, ' + name + '!'
    return 'Hello, ' + name + ' and ' + ' and '.join(args) + '!'


def test_greet():
    if greet('Timur') == 'Hello, Timur!':
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    if greet('Timur', 'Roman') == 'Hello, Timur and Roman!':
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    if greet('Timur', 'Roman', 'Ruslan') == 'Hello, Timur and Roman and Ruslan!':
        print("#test3 - ok")
    else:
        print("#test3 - fail")




def print_products(*args):
    '''принимает произвольное количество аргументов и выводит список
    продуктов по образцу: <номер продукта>) <название продукта>'''
    products = [i for i in args if type(i) == str and len(i) > 0]
    if len(products) == 0:
        print('Нет продуктов')
    else:
        for i, product in enumerate(products):
            print(f'{i + 1}) {product}')




def info_kwargs(**kwargs):
    '''принимает произвольное количество именованных аргументов и
    печатает именованные аргументы в соответствии с образцом:
    <имя аргумента>: <значение аргумента>,
    при этом имена аргументов следуют в алфавитном порядке (по возрастанию)'''
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')

