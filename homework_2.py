# Домашние задание 2
# Задание 1. Копирование содержимого одного файла в другой
# Создайте программу, которая копирует содержимое файла source.txt в новый файл destination.txt.
def task_1(input_file, output_file):
    print("\nЗадание 1. Копирование содержимого одного файла в другой")
    try:
        with open(input_file, 'r', encoding='utf-8') as r:
            content = r.read()
        
        with open(output_file, 'w', encoding='utf-8') as w:
            w.write(content)
    except Exception:
        print('Возникла ошибка')
    else:
        print('Файл успешно скопирован в', output_file, '\n')

# Задание 2. Подсчёт стоимости заказа из файла
# Напишите программу, которая считывает файл prices.txt, содержащий информацию о товарах: название, количество и цену, и подсчитывает общую стоимость заказа.
def task_2(filename):
    print('Задание 2. Подсчёт стоимости заказа из файла')
    try:
        sum = 0
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 3:
                    name, quantity, price = parts
                    try:
                        sum += int(quantity) * float(price)
                    except ValueError:
                        print(" Ошибка в данных строки:", line.strip())
    except Exception:
        print("Возникла ошибка")
    else:
        print("Общая стоимость заказа:", sum ,"рублей\n")

# Задание 3. Подсчёт количества слов в файле
# Напишите программу, которая подсчитывает количество слов в текстовом файле text_file.txt и выводит результат на экран.
def task_3(filename):
    print('Задание 3. Подсчёт количества слов в файле')
    try:
        amount = 0
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            symbols = '.,!?:;—-()[]{}"\'«»…'
            for symbol in symbols:
                text = text.replace(symbol, ' ')
            text=len(text.split())
    except Exception:
        print("Возникла ошибка")
    else:
        print('В тексте',text,'слов\n')

# Задание 4. Копирование уникального содержимого одного файла в другой
# Создайте программу, которая считывает строки из файла input.txt, сохраняет только уникальные строки и записывает их в новый файл unique_output.txt.
def task_4(input_file, output_file):
    print('Задание 4. Копирование уникального содержимого одного файла в другой')
    try:
        unique_lines = set()
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    unique_lines.add(clean_line)

        with open(output_file, 'w', encoding='utf-8') as file:
            for line in unique_lines:
                file.write(line + '\n')
    except Exception:
        print("Возникла ошибка")
    else:
        print(" Уникальные строки из ", input_file," записаны в ",output_file)

if __name__ == "__main__":
    task_1('source.txt', 'destination.txt')
    task_2('prices.txt')
    task_3('text_file.txt')
    task_4('input.txt', 'unique_output.txt')