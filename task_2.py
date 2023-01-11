# Завдання 2. Напишіть програму, яка б приймала список з числами та перевіряла
# чи всі числа в ньому унікальні. Реалізуйте у функції декілька обробок
# виключень.

print('--- Task 2 ---')

# Список з цифрами.
list = [1, 1, 2, 2, 3, 5, 5, 6, 7, 8, 88, 9, 10, 10]

# Список, щоб перевірити роботу програми з унікальним списком цифр.
# list = [1, 2, 3, 5, 6, 7, 8, 88, 9, 10]

# Список унікальних цифр.
unique_elem = []
# Список повторюваних цифр.
duplicate_elem = []


# Функція для визначення унікальності цифр у списку.
def get_list():

    print('The current list is:', list)
    # Для перевірки роботи виключенння AssertionError.
    # assert len(list) < len(set(list)), 'This list is not unique'.upper()
    try:
        if len(list) == len(set(list)):
            print('This list is unique')
        else:
            print('Is the list unique? No, this is', False)
            for item in list:
                if item not in unique_elem:
                    unique_elem.append(item)
                elif item not in duplicate_elem:
                    duplicate_elem.append(item)
            print('\nDuplicated numbers:', duplicate_elem)
            print('Set of the unique numbers:', unique_elem)
            # Для перевірки виключення NameError.
            print('Set of the unique numbers:', unique_ele)
    # Блок опрацювання виключень.
    except NameError as err:
        print('\nSomething went wrong:'.upper(), err)

    # finally:
    #     print('Finally block:'.upper(), 'Process finished!')


get_list()
