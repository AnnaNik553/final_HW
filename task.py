
def get_array():
    answer = input('Хотите ввести элементы массива с клавиатуры? - y/n ').lower()
    while answer not in ('y', 'n'):
        answer = input('Пожалуйста, введите "y" или "n" на латинице ').lower()
    if answer == 'y':
        return input('введите элементы массива через пробел ').split()
    elif answer == 'n':
        return ['hello', '2', 'world', ':-)']


def get_filtered_array(arr):
    return f'Массив из строк длиной 3 и менее символа - {[x for x in arr if len(x) <= 3]}'


array = get_array()
print(get_filtered_array(array))
