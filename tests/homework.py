import requests
from faker import Faker
from pytest_voluptuous import S

from schemas.reqres import single_user
from utils.sessions import reqres

faker = Faker()


def test_list_users():
    response = requests.get('https://reqres.in/api/users/2')
    assert response.status_code == 200
    assert S(single_user) == response.json()


def test_create_user():
    name = faker.first_name()
    job = faker.job()
    user_data = {'name': name, 'job': job}

    response = reqres().post('/users', data=user_data)

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_delete_user():
    response = requests.delete('https://reqres.in/api/users/2')
    assert response.status_code == 204


def test_update_user():
    name = faker.first_name()
    job = faker.job()
    user_data = {'name': name, 'job': job}

    response = requests.put('https://reqres.in/api/users/2', json=user_data)
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_login_unsuccessful():
    email = faker.email()
    user_data = {'email': email}

    response = requests.post('https://reqres.in/api/login', data=user_data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_register_unsuccessful():
    email = faker.email()
    user_data = {'email': email}

    response = reqres().post('/register', data=user_data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
