import requests
from pytest_voluptuous import S
from voluptuous import Schema, Any, ALLOW_EXTRA


def test_list_users():
    single_user = Schema(
        {
            'data': {
                'id': int,
                'email': str,
                'first_name': str,
                'last_name': str,
                'avatar': str
            },
            'support': {
                'url': str,
                'text': str
            }
        })

    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200
    assert S(single_user) == response.json()
