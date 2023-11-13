import dotenv
import os
from dotenv import load_dotenv
import requests
import pytest

@pytest.fixture
def test_post_create_booking():
    payload_create_booking = {
    "firstname" : "Dhonikkk",
    "lastname" : "Ram",
    "totalprice" : 350,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-01-01",
        "checkout" : "2023-02-02"
    },
    "additionalneeds" : "Breakfast"
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers, json=payload_create_booking)
    print(response.json())
    print(response.headers)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    assert response.status_code == 200
    return booking_id

@pytest.fixture
def test_put_req(test_post_create_booking):
    payload_create_booking = {
        "firstname": "Reema",
        "lastname": "Mahendra",
        "totalprice": 360,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-09-01",
            "checkout": "2023-10-02"
        },
        "additionalneeds": "Breakfast"
    }
    load_dotenv()
    temp_token = "token=" + os.getenv("token")
    print(temp_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie" : temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_booking)
    response = requests.put(url_put, headers=headers, json=payload_create_booking)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200
    #print("In Put Req", test_post_create_token, test_post_create_booking)

# def test_delete_req(test_post_create_token, test_post_create_booking):
#     temp_token = "token=" + test_post_create_token
#     print(temp_token)
#     headers = {
#         "Content-Type": "application/json",
#         "Cookie": temp_token
#     }
#     url_del = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_booking)
#     response = requests.delete(url_del, headers=headers)
#     print(response.text)
#     print(response.status_code)
#     assert response.status_code == 201