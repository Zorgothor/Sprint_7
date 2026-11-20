import allure
import pytest
import requests

from helpers import BASE_URL


@allure.feature("Курьер")
@allure.story("Авторизация")
class TestLoginCourier:

    @allure.title("Успешная авторизация возвращает id курьера")
    def test_login_success_returns_id(self, registered_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": registered_courier["login"],
                "password": registered_courier["password"],
            },
            timeout=30,
        )

        assert response.status_code == 200

        response_body = response.json()
        assert isinstance(response_body["id"], int)

    @allure.title("Авторизация без логина возвращает ошибку")
    def test_login_without_login_returns_error(self, registered_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={"password": registered_courier["password"]},
            timeout=30,
        )

        assert response.status_code == 400

        response_body = response.json()
        assert response_body["code"] == 400
        assert response_body["message"] == "Недостаточно данных для входа"

    @pytest.mark.xfail(
        raises=requests.exceptions.ReadTimeout,
        reason="API не отвечает на запрос авторизации без пароля",
    )
    @allure.title("Авторизация без пароля возвращает ошибку")
    def test_login_without_password_returns_error(self, registered_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={"login": registered_courier["login"]},
            timeout=10,
        )

        assert response.status_code == 400

        response_body = response.json()
        assert response_body["code"] == 400
        assert response_body["message"] == "Недостаточно данных для входа"

    @allure.title("Авторизация с неверным паролем возвращает ошибку")
    def test_login_with_wrong_password_returns_error(self, registered_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": registered_courier["login"],
                "password": "wrong_password_123",
            },
            timeout=30,
        )

        assert response.status_code == 404

        response_body = response.json()
        assert response_body["code"] == 404
        assert response_body["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация несуществующего курьера возвращает ошибку")
    def test_login_nonexistent_user_returns_error(self):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": "unknown_login_123",
                "password": "unknown_password_123",
            },
            timeout=30,
        )

        assert response.status_code == 404

        response_body = response.json()
        assert response_body["code"] == 404
        assert response_body["message"] == "Учетная запись не найдена"
