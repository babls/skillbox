import re
#   1
def to_camel_case(text):
    return re.split('_|-', text)[0]+ ''.join(word.title() for word in re.split('_|-', text)[1::])
print(to_camel_case('Foo-Bar'))

#   Функция перевода в CamelCase, ВерблюжийРегистр
#   берем не 2 элемент, а 1 ( re.split('_|-', text)[0])
#   переменная text в ковычках, распознается как текст

#   2
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class SingletonClass(metaclass=SingletonMeta):
    pass

class RegularClass():
    pass

x = SingletonClass()
y = SingletonClass()
print(x == y)

x = RegularClass()
y = RegularClass()
print(x == y)

#   Синглтон  - это шаблон проектирования, который позволяет создать всего один экземпляр класса
#   Скажу честно, нашел статью на хабр))
#   https://habr.com/ru/company/otus/blog/527384/

#   3
count_bits = lambda n: bin(n).count('1')
print(count_bits(10))

#   Функция подсчета единицы в двоичном представлении чисел
#   Пример 10 -> 00001010
#                    1+1 = Ответ 2
#   не указан аргумент для лямбда-функции

#   4
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int, str(n))))
print(digital_root(156))
#   Как я понял это рекурсивная функция для вычисления Цифрового корня цисла
#   Пример 156 -> 3
#   сумма всех цисел 1 + 5 + 6 = 12, далее сумма  1 + 2 = 3, 
#   когда число меньше 10 выводим результат.

#   5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
print(even_or_odd(10))
print(even_or_odd(9))

#   Функция проверки, является ли число четным или нечетным
#   в лямбда-функции, в условии небыло указана переменная number
