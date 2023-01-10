# Завдання 1. Напишіть функцію, яка б приймала номер місяця,
# а вертала його назву. Реалізуйте у функції декілька обробок виключень.

print('--- Task 1 ---')

# Словник з номерами і назвами місяців.
month = {
    1: 'January', 2: 'February',
    3: 'March', 4: 'April', 5: 'May',
    6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November',
    12: 'December'
}


# Функція, яка повертає назву місяця за його номером.
def get_month():
    while True:
        try:
            mon = int(input('Enter a number to get the month [0 == break]: '))
            if mon == 1 or mon == 2 or mon == 3 or mon == 4 \
                    or mon == 5 or mon ==6 or mon == 7 \
                    or mon == 8 or mon == 9 or mon == 10 or mon == 11\
                    or mon == 12:
                print(month [mon])
                return get_month()
            elif mon > 12:
                raise
            elif mon == 0:
                print('Good bay!')
                break

        except ValueError as ex:
            print('Could not convert data to an integer:'.upper(), ex)
        except Exception:
            print('Please enter a valid input'.upper(),"[from 1 to 12]"'')

        #finally:


get_month()

# KeyError
# TypeError
# ValueError

