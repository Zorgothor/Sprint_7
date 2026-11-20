
import allure
import pytest
import requests

from helpers import BASE_URL, create_order_data

@pytest.mark.parametrize(
    "color",
    [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None,
    ],
)
@allure.feature("Заказы")
@allure.story("Создание заказа")
def test_create_order_with_different_colors_returns_track(color):
    order_data = create_order_data()

    if color is not None:
        order_data["color"] = color

    response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=order_data,
        timeout=30,
    )

    assert response.status_code == 201
    assert "track" in response.json()
    assert isinstance(response.json()["track"], int)