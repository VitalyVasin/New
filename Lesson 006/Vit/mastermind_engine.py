from random import random


import random

bulls = 0
cows = 0

def get_number():
    global num
    numbersi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num1 = random.choices(numbersi, k=1)
    numbersi.remove(num1[0])
    numbersi.append(0)
    num2 = random.choices(numbersi, k=1)
    numbersi.remove(num2[0])
    num3 = random.choices(numbersi, k=1)
    numbersi.remove(num3[0])
    num4 = random.choices(numbersi, k=1)
    numbersi.remove(num4[0])
    num1 = str(num1[0])
    num2 = str(num2[0])
    num3 = str(num3[0])
    num4 = str(num4[0])
    num = num1 + num2 + num3 + num4
    # print(num)
    return num


def try_number(numer, answer):
    global bulls
    global cows
    bulls = 0
    cows = 0
    for b in range(4):
        if numer[b] == answer[b]:
            bulls += 1

    for c in numer:
        for a in answer:
            if c == a:
                cows += 1
    cows -= bulls

    try_dict = {'bulls':0, 'cows':0}
    try_dict['bulls'] = bulls
    try_dict['cows'] = cows
    return bulls, cows, try_dict

def is_win():
    return bulls == 4

def enter_text(answer):
    input_text = answer
    is_process = False
    try:
        test_number = int(input_text)
        print('Вы ввели: ', test_number)
        if test_number > 1233 and test_number < 9877:
            try_num_test = 5
        else:
            print("Не корректный ввод!")
            try_num_test = -1
        if try_num_test != -1:

            answer = 0
            answer = str(input_text)
            is_process = True
    except ValueError:
        print("Не корректный ввод!")
    return is_process
