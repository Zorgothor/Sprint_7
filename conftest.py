
import pytest
import requests

from helpers import BASE_URL, create_courier_data

@pytest.fixture
def registered_courier():
    courier_data = create_courier_data()

    create_response = requests.post(
        f"{BASE_URL}/api/v1/courier",
        json=courier_data,
        timeout=30,
    )

    assert create_response.status_code == 201
    assert create_response.json() == {"ok": True}

    yield courier_data

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