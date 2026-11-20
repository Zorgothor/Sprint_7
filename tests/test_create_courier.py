import allure
import pytest
import requests

from helpers import BASE_URL, create_courier_data


@allure.feature("Курьер")
@allure.story("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
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

        assert login_response.status_code == 200

        delete_response = requests.delete(
            f"{BASE_URL}/api/v1/courier/{login_response.json()['id']}",
            timeout=30,
        )

        assert delete_response.status_code == 200

    @allure.title("Создание курьера с занятым логином возвращает ошибку")
    def test_create_duplicate_courier_returns_error(self, registered_courier):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=registered_courier,
            timeout=30,
        )

        assert response.status_code == 409

        response_body = response.json()
        assert response_body["code"] == 409
        assert response_body["message"] == (
            "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title("Создание курьера без поля {missing_field} возвращает ошибку")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_error(
        self, missing_field
    ):
        courier_data = create_courier_data()
        courier_data.pop(missing_field)

        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=courier_data,
            timeout=30,
        )

        assert response.status_code == 400

        response_body = response.json()
        assert response_body["code"] == 400
        assert response_body["message"] == (
            "Недостаточно данных для создания учетной записи"
        )
