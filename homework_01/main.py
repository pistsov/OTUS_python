"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd(x):
    return x % 2 != 0


def is_even(x):
    return x % 2 == 0


def is_prime(x):
    if x != 1:
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return False
        return x


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(is_odd, numbers_list))
    if filter_type == EVEN:
        return list(filter(is_even, numbers_list))
    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))