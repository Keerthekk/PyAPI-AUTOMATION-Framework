import pytest
import requests

#datadriven testing in excel
#create token


@pytest.fixtures
def test_post_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers,json=payload)
    print(response.text)
    assert response.status_code == 200
    print(response.json()["token"])
    return response.json()["token"]