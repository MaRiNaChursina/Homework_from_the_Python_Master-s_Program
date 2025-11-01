'''
Задание 1.
Напишите программу, которая создаёт 2 потока для вычисления квадратов и кубов целых чисел от 1 до 10.
'''
import threading

def worker1():
    for i in range(1,11):
        print(i*i)

def worker2():
    for i in range(1,11):
        print(i*i*i)

print('Задание 1')
t1 = threading.Thread(target=worker1)
t1.start()
t2 = threading.Thread(target=worker2)
t2.start()

'''
Задание 2.
Напишите программу, которая создаёт несколько потоков для выполнения функции, которая выводит целые числа от 1 до 10 с задержкой в 1 секунду.
'''

import threading
import time

def worker():
    for i in range(0,10):
        print(i+1)
        time.sleep(1)

print('Задание 2')
t3 = threading.Thread(target=worker)
t3.start()
t4 = threading.Thread(target=worker)
t4.start()

