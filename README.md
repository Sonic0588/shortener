# shortener

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
