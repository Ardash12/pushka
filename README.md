# Fastapi project

Установите и активируйте виртуальное окружение
```
python -v venv venv
venv\scripts\activate
```

Установите зависимости
```
pip install -r requirements.txt
```
Миграции (пропустить, тестовая бд)
```
alembic init alembic
alembic stamp head --purge
alembic revision --autogenerate -m "igrations"
alembic upgrade head
```
Запуск сервера
``` 
uvicorn app.main:application --reload
```
Струкиу проекта
```
app
├── core
│   ├── databese.py
│   └── models.py
│
├── categories
│   ├── model.py
│   ├── router.py
│   └── schemas.py
│
├──items
│   ├── model.py
│   ├── router.py
│   └── schemas.py
│
└──users
    ├── model.py
    ├── router.py
    └── schemas.py

```
