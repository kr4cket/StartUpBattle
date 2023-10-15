# StartUpBattle

Пока что нет докер-файлов для бота и воркера, поэтому сначала:
+ Запускаем dev-среду
+ Запускаем бота в директории /bot/main.py
+ Запускаем worker в директории /worker/main.py


##### Команды запуска dev-среды :
```
    docker-compose --project-name="test" up -d
    cd tgbot
    pem show
    pem migrate
```

Чтобы заполнить данные в БД, запустите скрипт core/filling_data/fill_tables

##### Команда выключения dev-среды:
```
    docker-compose --project-name="test" down
```

##### Стек технологий:

1. Ядро ИИ
    - Python
    - g4f
2. Telegram Bot
    - Python
    - Aiogram
3. Backend
    - Golang
    - Gin
4. Frontend:
    - VueJS
    - Vue Router
    - Vue i18n
    - Vuex
    - Stylus
5. Брокер сообщений:
    - RabbitMQ
6. База данных:
    - PostgreSQL