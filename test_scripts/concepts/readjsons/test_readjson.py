import os
import json
from dotenv import load_dotenv
import pytest

@pytest.fixture
def load_test_data():
    load_dotenv()
    file_name = os.getenv("load_env")
    print(file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data

def test_make_req(load_test_data):
    print(load_test_data["url"])