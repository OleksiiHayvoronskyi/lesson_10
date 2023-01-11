# Завдання 3. Напишіть користувацький клас виключення з функціоналом на свій
# вибір. Викличте його за допомогою інструкції raise.

import sys

print('--- Task 3 ---')


# Клас для підняття влосних виключень.
class MyException(Exception):
    pass


# Функція, яка перевіряє опереційну систему твого ПК.
def is_linux():
    #assert ('Linux' in sys.platform), 'Function can only run on Linux systems.'
    assert ('win32' in sys.platform), 'Function can only run on Linux systems'
    print('Your system is win32.')
    print('Keep coding...')

try:
    is_linux()
    x = float(input('Enter a number: '))
    if x < 0:
        # Якщо буде від’ємне число, то виникне raise.
        raise MyException('This is my exception:', 'enter only positive number'.upper())
    num = 5 / x
    print(num)

# Блок перехоплення виключень.
except AssertionError as error:
    print(error)
    print('Change your OS on win32.')
    print('Into exception block 1.')
except ZeroDivisionError as error:
    print('You can\'t', error)
    print('Into exception block 2')
except MyException as error:
    print(error)
    print('Into exception block 3')
