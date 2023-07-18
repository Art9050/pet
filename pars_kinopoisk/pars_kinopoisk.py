#!/usr/bin/python3

import json
import requests
import numpy as np
import pandas as pd

# Считываем токен авторизации если в файле dict
with open('token.txt', encoding='utf-8') as token_file:
    token = token_file.read()
# token(dict)
token = json.loads(token)
token = token["token"]

'''
##**Отрабатываем получения инфы на примере отдельного фильма**
Скачаем информацию про фильм "Три мушкетёра: Д’Артаньян". Для этого найдём его в поиске на сайте Кинопоиска. Страница с фильмом имеет вид https://www.kinopoisk.ru/film/4368100/, где 4368100 — это ID фильма.

Согласно документации, путь, на который нужно подать запрос, формируется таким образом: https://kinopoiskapiunofficial.tech/api/v2.2/films/{FILM_ID}
'''
# Отправляем запрос библиотекой requests, функцией get.

film_id = 4368100

url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/{}".format(film_id)
header = {'X-API-KEY': token}

# Отправляем запрос о фильме
req = requests.get(url, headers = header)

# # Получаем информацию в виде JSON
film_info = req.json()

# return <Response [200]>

