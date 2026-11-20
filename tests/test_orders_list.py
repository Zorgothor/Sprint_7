
import allure
import requests

from helpers import BASE_URL

@allure.feature("Заказы")
@allure.story("Получение списка заказов")
def test_get_orders_returns_orders_list():
    response = requests.get(
        f"{BASE_URL}/api/v1/orders",
        timeout=30,
    )

    assert response.status_code == 200

    response_body = response.json()

    assert "orders" in response_body
    assert isinstance(response_body["orders"], list)