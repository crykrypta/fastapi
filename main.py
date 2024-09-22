from fastapi import FastAPI

from models import User


app = FastAPI()


# Функция для проверки возраста
def is_adult(age: int) -> bool:
    return age >= 18


# GET - маршруты ------------------------------------------------------------

# Корневой маршрут
@app.get("/")
async def get_root():
    return {"message": "Hello World!"}


# Кастомный end-point
@app.get("/custom")
async def get_custom_endpoint():
    return {"message": "Custom endpoint!"}


# POST - маршруты ------------------------------------------------------------


# Создание пользователя с проверкой возраста
@app.post('user')
async def create_user(user: User):
    return {'name': user.name,
            'age': user.age,
            'is_adult': is_adult(user.age)}
