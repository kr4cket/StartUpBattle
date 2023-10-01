# StartUpBattle

Пока что нет докер-файлов для бота и воркера, поэтому сначала:
+ Запускаем dev-среду
+ Запускаем бота в директории /bot/main.py
+ Запускаем worker в директории /worker/main.py


##### Команда запуска dev-среды :
```
    docker-compose --project-name="test" up -d
    pip install -r requirements.txt
    yoyo apply --database postgresql://stbuser:stbuser@localhost:5436/data ./worker/migrations
```


##### Команда выключения dev-среды:
```
    docker-compose --project-name="test" down
```
