# Парсер данных кинопоиска
Работу веду в [колабе](https://colab.research.google.com/drive/1LpTNqnM9rLcBiJ5oD2b6acyMMb1lP5bB?usp=sharing) \
Репозиторий в [гите](https://github.com/Art9050/pet/blob/main/pars_kinopoisk/pars_kinopoisk.py) <не структурировал> \
Основа: [Провект по аналитеке данных](https://miptstats.github.io/courses/ad_fivt/data_parsing.html)  


- Разбираюсь как работает
- Вношу изменения где не работает
- Переношу на Другое API
- После формирования DF меняю логику - аналитика не интересна.
Новая логика: складыва инфу по фильмам в БД в системе СКД2. Проверяю неизменность инфы по фильмам.

---
## Требуется ТЗ
В моменте пришел к выводу что не знаю что я хочу. Фактически адекватная работа не возможно без записи целей и желаемых конечных результатов\
\
Подсказку для организации работы нашел в описании жизненного цикла ПО:

<div>
  <img src="https://hsto.org/r/w1560/webt/mw/bv/ee/mwbveegwbs-v5nez1ovzroceeqk.png" title="Схема процесса" alt="Google" width="300" height="300"/>&nbsp;
  <img src="https://beqa.pro/blog/wp-content/uploads/sdlc_idea.jpg" title="Схема процесса" alt="Google" width="400" height="400"/>
</div>

**SDLC:**

- **Анализ требований** отвечает на вопрос «Какие проблемы требуют решений?»\
_Недостаток опыта и знаний в парсинге информации в интернете. Наработка навыков построения баз данных_
- **Планирование** отвечает на вопрос «Что мы хотим сделать?»\
_Отработка скрапинга,парсинга на примере Кинопоиска и создание базы данных фильмов с положительным рейтингом (от 6 до 10 баллов)_
_Аналитическая справка по фильмам в базе данных <вопросы к анализу>_\
_**Вход:** Информация о фильмах\
**Выход:** База данных фильмов с историей изменений_
- **Проектирование и дизайн** отвечает на вопрос «Как мы добьемся наших целей?»\
_Идем по api на кинопоиск за .json с инфой о фильмах\
Грузим .json в DF\
Пишем DF в базу_

- **Разработка ПО** регулирует процесс создания продукта.

- **Тестирование** регулирует обеспечение качественной работы продукта.\
_<не понимаю как применить в текущем проекте>_

- **Развертывание** регулирует использование финального продукта.\
Постановка алгоритма на автоматическое выполенние в cron на домашнем сервере <может ну его  и просто арендовать сервак? За одно и VPN развернешь>

**Для понимания накидал блок схему процесса:** Сперва наполняем БД из топ250 кинопоиска, а после перебираем все фильмы по критерию и вносим в базу по алгоритму
<div>
  <img src="https://github.com/Art9050/pet/blob/main/pars_kinopoisk/image/image.png" title="Схема процесса" alt="Google" width="500" height="500"/>&nbsp;
</div>



