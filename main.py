from math import log
from app import *

def main():
    countOfSignForEncoding = 2  # Количество знаков в кодировке (0 и 1)

    print('Вычисление качества используемого кода')

    # Ввод и валидация вероятностей
    array = input_probability()

    # Ввод и валидация длины сообщения
    length = validation()

    # Расчет энтропии сообщения
    entropy = entropy_message(array)

    # Расчет минимальной длины кодовой комбинации
    n_min = find_average_length(entropy, countOfSignForEncoding)

    # Расчет избыточности кода
    redundancy = redundancy_of_code(entropy, length, countOfSignForEncoding)

    # Расчет длины кодовой комбинации при заданной длине
    n_c = code_combination(length, len(array))

    print('Избыточность используемого кода:', redundancy, '%')
    print('Минимально необходимая длина кодовой комбинации равна:', n_min)
    print('Длина кодовой комбинации при заданной длине равна:', n_c)

    input("Нажмите Enter для завершения")

if __name__ == '__main__':
    main()