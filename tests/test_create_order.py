import allure
import pytest
import requests

from helpers import BASE_URL, create_order_data


@allure.feature("Заказы")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа возвращает трек")
    @pytest.mark.parametrize(
        "color_field",
        [
            {"color": ["BLACK"]},
            {"color": ["GREY"]},
            {"color": ["BLACK", "GREY"]},
            {},
        ],
        ids=["black", "grey", "black-and-grey", "no-color"],
    )
    def test_create_order_with_different_colors_returns_track(self, color_field):
        order_data = create_order_data()
        order_data.update(color_field)

        response = requests.post(
            f"{BASE_URL}/api/v1/orders",
            json=order_data,
            timeout=30,
        )

        assert response.status_code == 201

        response_body = response.json()
        assert isinstance(response_body["track"], int)
