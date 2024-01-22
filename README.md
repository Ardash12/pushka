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
Миграции
```
alembic init alembic
alembic revision --autogenerate -m "initial"
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
└──item
    ├── model.py
    ├── router.py
    └── schemas.py

```
