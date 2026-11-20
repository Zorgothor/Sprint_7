
import allure
import pytest
import requests

from helpers import BASE_URL

@allure.feature("Курьер")
@allure.story("Авторизация")
def test_login_success_returns_id(registered_courier):
    response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": registered_courier["login"],
            "password": registered_courier["password"],
        },
        timeout=30,
    )

    assert response.status_code == 200
    assert "id" in response.json()

@pytest.mark.parametrize(
    "missing_field",
    [
        "login",
        pytest.param(
            "password",
            marks=pytest.mark.xfail(
                raises=requests.exceptions.ReadTimeout,
                reason="API не отвечает при авторизации без пароля",
            ),
        ),
    ],
)
@allure.feature("Курьер")
@allure.story("Авторизация")
def test_login_without_required_field_returns_error(
    missing_field, registered_courier
):
    data = {
        "login": registered_courier["login"],
        "password": registered_courier["password"],
    }
    data.pop(missing_field)

    response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json=data,
        timeout=10,
    )

    assert response.status_code == 400

@allure.feature("Курьер")
@allure.story("Авторизация")
def test_login_with_wrong_password_returns_error(registered_courier):
    response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": registered_courier["login"],
            "password": "wrong_password_123",
        },
        timeout=30,
    )

    assert response.status_code == 404

@allure.feature("Курьер")
@allure.story("Авторизация")
def test_login_nonexistent_user_returns_error():
    response = requests.post(
        f"{BASE_URL}/api/v1/courier/login",
        json={
            "login": "unknown_login_123",
            "password": "unknown_password_123",
        },
        timeout=30,
    )

    assert response.status_code == 404