import requests
import pytest

url = 'https://reqres.in/api/users/2'


def test_getdata():
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200