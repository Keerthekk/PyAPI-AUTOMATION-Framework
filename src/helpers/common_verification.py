
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == int(expected_data), "Expected HTTP Status :" + expected_data

def verify_key_for_not_null_greater_than_zero(key):
        assert key != 0, "key is not Empty : " + key
        assert key > 0, "key should be greater than zero : " + key
