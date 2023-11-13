def payload_create_booking():
    payload = {
        "firstname": "DhoniMM",
        "lastname": "Brown",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-02-02"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_update_booking():
    payload = {
    "firstname" : "DhoniMM",
    "lastname" : "Brown",
    "totalprice" : 311,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2023-09-01",
        "checkout" : "2023-09-02"
    },
    "additionalneeds" : "Breakfast"
    }
    return payload