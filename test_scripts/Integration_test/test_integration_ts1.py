from src.constants.APIconstants import url_update_delete_booking
from src.helpers.api_wrapper import patch_request
from src.helpers.payload_manager import payload_update_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import *
import pytest

class TestIntegration(object):

    # def test_setup(self):
    #     print("Before")

    def test_verify_creating_booking_by_updating_deleting(self):
        response = patch_request(url_update_delete_booking, headers = common_headers(), auth=None,
                                payload=payload_update_booking(), in_json=False)
        verify_http_code(response, 200)
        verify_key_for_not_null_greater_than_zero(response.json() ["bookingid"])

        #print(bookingid)