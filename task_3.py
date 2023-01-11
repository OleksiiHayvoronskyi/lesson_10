# Завдання 3. Напишіть користувацький клас виключення з функціоналом на свій
# вибір. Викличте його за допомогою інструкції raise.

print('--- Task 3 ---')


class MyException(Exception):
    pass


print('Code has been started')
x = int(input('Enter some number: '))
if x > 5 or x < 1:
    raise MyException
print('Code has been stopped ')
