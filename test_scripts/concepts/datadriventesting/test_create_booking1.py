
from src.constants.APIconstants import url_create_token, url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utils import common_headers
from src.helpers.common_verification import *
import pytest
import allure

class TestIntegration(object):

    # def test_setup(self):
    #      print("Before")

    # def create_token_tc0(self):
    #     response = post_request(url_create_token(), headers=common_headers(), auth=None,
    #                             payload=payload_create_token(), in_json=False)
    #     verify_http_code(response, 200)
    #     verify_key_for_not_null_greater_than_zero(response.json()["token"])
    #     print(response.text)
    #     booking_id = response.json()["bookingid"]
    #     print(booking_id)

    @pytest.mark.some
    @allure.feature('TC#1 - verify Create Booking Feature')
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers = common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        verify_key_for_not_null_greater_than_zero(response.json() ["bookingid"])
        print(response.text)
        booking_id = response.json()["bookingid"]
        print(booking_id)

    @allure.feature('TC#2 - Verify Update Booking Feature')
    def test_create_booking_tc2(self):
        assert True

    @allure.feature('TC#3 - Verify Delete Booking Feature')
    def test_create_booking_tc3(self):
        assert True

    # @pytest.fixture(scope="module")
    # def tear_down(self):
    #     print("end")
