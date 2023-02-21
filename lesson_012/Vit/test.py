import time
import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
other_simbols = string.printable

all_simbols = lowercase_letters + uppercase_letters + digits + other_simbols

try:
    length_password = int(input('Введите необходимую длину пароля:'))
    if length_password > 0 and length_password < 99:
        password_word = ''.join(random.sample(all_simbols, int(length_password)))
        print(f'Ваш пароль длинной {length_password} символов генерируется')
        time.sleep(2)
        print('Ваш безопасный пароль готов: ', password_word)
    else:
        print('Введено не корректное значение, проверьте ввод')
except ValueError:
    print('Введено не корректное значение, проверьте ввод')
