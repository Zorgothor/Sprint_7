
import allure
import pytest
import requests

from helpers import BASE_URL, create_courier_data

@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_courier_success():
    courier_data = create_courier_data()

    response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=courier_data,
        timeout=30,
    )

    assert response.status_code == 201
    assert response.json() == {"ok": True}

    login_response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": courier_data["login"],
            "password": courier_data["password"],
        },
        timeout=30,
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(
            f"{BASE_URL}/api/v1/courier/{courier_id}",
            timeout=30,
        )

@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_duplicate_courier_returns_error(registered_courier):
    response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=registered_courier,
        timeout=30,
    )

    assert response.status_code == 409

@pytest.mark.parametrize("missing_field", ["login", "password"])
@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_courier_without_required_field_returns_error(missing_field):
    courier_data = create_courier_data()
    courier_data.pop(missing_field)

    response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=courier_data,
        timeout=30,
    )

    assert response.status_code == 400