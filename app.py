from math import log, ceil

# Вычисление длины кодовой комбинации
def code_combination(length, amount):
    return length * amount

# Вычисление средней длины кодовой комбинации
def find_average_length(entropy, countSigns):
    return entropy / log(countSigns, 2)

# Нахождение избыточности кода
def redundancy_of_code(entropy, length, countSigns):
    ncp = find_average_length(entropy, countSigns)
    return round((length - ncp) / length * 100, 3)

# Функция для поиска энтропии сообщения
def entropy_message(probabilityArray):
    result = 0
    for i in range(0, len(probabilityArray)):
        if probabilityArray[i] > 0:  # Проверка на случай log(0)
            result += probabilityArray[i] * log(probabilityArray[i], 2)
    if result != 0:
        result *= -1
    print('Entropy:', result)
    return result

# Ввод и валидация целого числа
def validation():
    while True:
        try:
            data = int(input('Введите целое число больше 0: '))
            if data > 0:
                return data
            print('Введенное значение не больше 0')
        except ValueError:
            print('Вы ввели не число')
        print('Попробуйте еще раз')

# Ввод списка дробей (вероятностей)
def input_probability():
    while True:
        print('Введите количество сообщений')
        count = validation()
        probabilityArray = []

        for _ in range(count):
            while True:
                prob = input('Введите вероятность появления сообщения в формате "1/2": ')
                try:
                    first = int(prob.split('/')[0])
                    second = int(prob.split('/')[1])
                    probabilityArray.append(first / second)
                    break  # Выход из внутреннего цикла, если ввод корректен
                except (ValueError, IndexError):
                    print('Данные введены не верно! Попробуйте еще раз.')

        if sum(probabilityArray) == 1:
            return probabilityArray
        print('Помните. Сумма вероятностей должна быть равна 1!')