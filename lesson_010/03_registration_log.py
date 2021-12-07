# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код
class NotNameError(Exception):
    None
class NotEmailError(Exception):
    None


def registration(line):
    name, email, age = line.split(' ')
    if name and email and age:
        if name.isalpha():
            if "@" in email and "." in email:
                if int(age) >= 10 and int(age) <= 99:
                    # print('Основные проверки пройдены')
                    # print('добавить запись в файл registrations_good.log')
                    with open(r"registrations_good.log", "a") as file:
                        file.write(line + '\n')
                else:
                    # print('добавить запись в файл registrations_bad.log')
                    with open(r"registrations_bad.log", "a") as file:
                        file.write(line + '\n')
                    raise ValueError('Поле возраст НЕ является числом от 10 до 99')
            else:
                # print('добавить запись в файл registrations_bad.log')
                with open(r"registrations_bad.log", "a") as file:
                    file.write(line + '\n')
                raise NotEmailError('Поле емейл НЕ содержит @ и .(точку)')
        else:
            # print('добавить запись в файл registrations_bad.log')
            with open(r"registrations_bad.log", "a") as file:
                file.write(line + '\n')
            raise NotNameError('Поле имени содержит НЕ только буквы')
    else:
        # print('добавить запись в файл registrations_bad.log')
        with open(r"registrations_bad.log", "a") as file:
            file.write(line + '\n')
        raise ValueError('НЕ присутсвуют все три поля')


with open('registrations.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            registration(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'НЕ присутсвуют все три поля, {exc} в строке {line}')
            else:
                print(f'{exc} в строке {line}')
        except NotNameError as exc:
            print(f'{exc} в строке {line}')
        except NotEmailError as exc:
            print(f'{exc} в строке {line}')
