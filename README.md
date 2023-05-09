# shortener
## Запуск приложения
```
docker-compose up -d
```
## Настройка и использование дебагера в VSCode + Docker
1. В `launch.json` добавить конфигурацию
```json
{
    "name": "Python: Remote Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "0.0.0.0",
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/usr/src"
        }
    ]
}
```
2. Перейти в `Run And Debug` и запустить `Python: Remote Attach` при запущеном докер контейнере
## Описание ручек приложения
GET /{link_id} - Вызов укороченной ссылки, который редиректит на длиную ссылку
POST /links - Добавить длинную ссылку и получить укороченную в ответе
DELETE /{link_id} - Удалить укороченную ссылку

Спецификацию API можно посмотреть по ссылке `http://0.0.0.0:8080/docs`
