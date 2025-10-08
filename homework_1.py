# Домашние задание 1
# Задание 1. Обработка деления на ноль

def task_1():
    print("Задание 1. Обработка деления на ноль")
    try:
        number_1 = int(input('Введите первое число:'))
        number_2 = int(input('Введите второе число:'))
        rezult = number_1/number_2
    except ZeroDivisionError:
        print("Ошибка: Делить на ноль нельзя")
    else:
        print("Результат деления:", rezult)

# Задание 2. Обработка некорректного ввода
def task_2():
    print("Задание 2. Обработка некорректного ввода")
    try:
        number_1 = int(input('Введите первое число:'))
        number_2 = int(input('Введите второе число:'))
        rezult = number_1/number_2
    except ZeroDivisionError:
        print("Ошибка: Делить на ноль нельзя")
    except ValueError:
        print("Ошибка: Введено не число")
    else:
        print("Результат деления:", rezult)

# Задание 3. Создание собственных исключений
def task_3(list_sum):
    print("Задание 3. Создание собственных исключений")
    class EvenNumberError(Exception):
        # Ошибка, если найдено чётное число.
        pass

    class NegativeNumberError(Exception):
        # Ошибка, если найдено отрицательное число.
        pass

    def sum_of_list(numbers):
        try:
            for num in numbers:
                if num < 0:
                    raise NegativeNumberError(f"Найдено отрицательное число: {num}")
                if num % 2 == 0:
                    raise EvenNumberError(f"Найдено чётное число: {num}")
            total = sum(numbers)
        except NegativeNumberError as e:
            print("Ошибка:", e)
        except EvenNumberError as e:
            print("Ошибка:", e)
        else:
            print("Сумма списка:", total)

    sum_of_list(list_sum)
    list_sum.append(2)
    sum_of_list(list_sum)
    list_sum.insert(1,-2)
    sum_of_list(list_sum)

# Задание 4. Обработка ошибок индексации
def task_4():
    print("Задание 4. Обработка ошибок индексации")
    list_number = [1, 2, 3, 4, 5, 6, 7]
    try:
        index = int(input("Введите индекс списка:"))
        element = list_number[index]
    except IndexError:
        print("Ошибка: Индекс выходит за пределы списка")
    else:
        print('Элемент под ', index, 'индексом: ', element)

# Задание 5. Обработка ошибок преобразования типов
def task_5():
    print("Задание 5. Обработка ошибок преобразования типов")
    try:
        number = float(input('Введите число с плавающей точкой:'))
    except ValueError:
        print('Ошибка: Строку невозможно преобразовать в число с плавающей точкой')
    else:
        print('Ваше число:', number)

# Задание 6. Обработка ошибок импорта модулей
def task_6():
    print("Задание 6. Обработка ошибок импорта модулей")
    try:
        # import math 
        num = float(input("Введите число для вычисления квадратного корня: "))
        if num < 0:
            raise ValueError("Квадратный корень из отрицательного числа не вычисляется!")
        result = math.sqrt(num)
    except ImportError:
        print("Ошибка: модуль math не найден!")
    except ValueError as e:
        print("Ошибка:", e)
    except NameError:
        print("Ошибка: модуль math не определён!")
    else:
        print("Квадратный корень:", result)
    

if __name__ == "__main__":
    task_1()
    task_2()
    task_3([3,13,7])
    task_4()
    task_5()
    task_6()
