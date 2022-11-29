import random


def check_access_by_age(age):
    if age < 18:
        return False
    return True


def test_if_age_is_14():
    if not check_access_by_age(14):
        print('OK')
    else:
        print('Not OK')


def test_if_age_less_than_18():
    for i in range(17):
        result = check_access_by_age(i)
        if result:
            print(f'Результат некорректен, возраст {i}')
        else:
            print('OK')


def test_if_age_than_18():
    result = check_access_by_age(18)
    if not result:
        print(f'Результат некорректен, возраст 18')



def sum_str(str1, str2):    #функция, склеивающая две строки
    gluestr = str1 + str2
    print(gluestr)
    return gluestr


def test_sum_str():         # Проверка на количество символов в сумме и тип
    for i in range(10):
        text = [random.choice('abc123') for _ in range(10)]
        text[5] = random.choice('ABC')
        str1 = ''.join(text)
        str2 = ''.join(text)
        sum_len = len(str1) + len(str2)
        res = sum_str(str1, str2)
        if len(res) == sum_len and isinstance(res, str):
            print('OK')
        else:
            print('NOT OK')


test_sum_str()
