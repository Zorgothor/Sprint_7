import allure
import requests

from helpers import BASE_URL


@allure.feature("Заказы")
@allure.story("Получение списка заказов")
class TestOrdersList:

    @allure.title(
        "Получение списка заказов возвращает заказы и информацию о странице"
    )
    def test_get_orders_returns_orders_list(self):
        response = requests.get(
            f"{BASE_URL}/api/v1/orders",
            timeout=30,
        )

        assert response.status_code == 200

        response_body = response.json()
        assert isinstance(response_body["orders"], list)
        assert isinstance(response_body["pageInfo"], dict)
        assert isinstance(response_body["availableStations"], list)
