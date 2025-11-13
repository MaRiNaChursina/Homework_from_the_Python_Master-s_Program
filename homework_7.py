'''Задание 1. Получение данных из публичного API

Выберите публичный API. Например, JSONPlaceholder.
Напишите скрипт, который:
· отправляет GET-запрос к /posts,
· извлекает и выводит заголовки и тела первых 5 постов.'''
import requests
from pprint import pprint

respons = requests.get('https://jsonplaceholder.typicode.com/posts')
if respons.status_code == 200:
    data = respons.json()
    # print(len(data))
    for i in range(5):
        print(f"\n Заголовок: {data[i]['title']}")
        print(f"\n Пост: {data[i]['body']}")
elif respons.status_code == 400:
    pprint(f'Ошибка сервера 400')
elif respons.status_code == 404:
    pprint(f'Ошибка сервера 404')
else:
    pprint(f'Ошибка: {respons.status_code}')

'''Задание 2. Работа с параметрами запроса

Используйте API OpenWeather для получения данных о погоде.
Напишите программу, которая:
· принимает название города от пользователя,
· отправляет GET-запрос к API и выводит текущую температуру и описание погоды.'''


'''Задание 3. Создание и обработка POST-запросов

Выберите API, который позволяет создавать ресурсы. Например, JSONPlaceholder.
Напишите программу, которая:
· отправляет POST-запрос для создания нового поста,
· выводит ID созданного поста и его содержимое.'''

# import requests
# from pprint import pprint

respon = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json={
        'userId': 10,
        'title': 'at nam consequatur ea labore ea harum',
        'body': 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut'
    }
)

if respon.status_code == 201:
    data = respon.json()
    pprint(data)
elif respon.status_code == 400:
    pprint(f'Ошибка сервера 400')
elif respon.status_code == 404:
    pprint(f'Ошибка сервера 404')
else:
    pprint(f'Ошибка: {respon.status_code}')

'''Задание 4. Обработка ошибок и работа с данными

Расширьте предыдущий код для обработки разных кодов состояния, например: 400, 404.
Добавьте вывод сообщения об ошибке в зависимости от полученного кода состояния.'''

