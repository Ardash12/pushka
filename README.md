alembic init alembic
alembic revision --autogenerate -m "initial"
alembic upgrade head

uvicorn app.main:application --reload
