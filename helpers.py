
import random
import string
from datetime import date, timedelta

BASE_URL = "https://qa-scooter.praktikum-services.ru"

def generate_random_string(length=10):
    """Возвращает случайную строку из строчных латинских букв."""
    return "".join(
        random.choice(string.ascii_lowercase)
        for _ in range(length)
    )

def create_courier_data():
    """Готовит уникальные данные нового курьера."""
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }

def create_order_data():
    """Готовит данные нового заказа."""
    delivery_date = date.today() + timedelta(days=7)

    return {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, улица Пушкина, дом 10",
        "metroStation": 4,
        "phone": "+79990000000",
        "rentTime": 5,
        "deliveryDate": delivery_date.isoformat(),
        "comment": "Тестовый заказ",
    }