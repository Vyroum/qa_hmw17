import requests
from jsonschema import validate

from schemas import get_user, post_user, update_user, register_user, error_register_user


def test_create_user():
    response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})

    assert response.status_code == 201
    body = response.json()
    validate(body, post_user)


def test_get_user_info_positive():
    response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200
    body = response.json()
    validate(body, get_user)


def test_get_user_info_negative():
    response = requests.get("https://reqres.in/api/users/23")

    assert response.status_code == 404


def test_update_user_info():
    response = requests.put("https://reqres.in/api/users/2", data={"name": "Trinity", "job": "bodyguard"})
    assert response.status_code == 200
    body = response.json()
    validate(body, update_user)


def test_successful_user_registration():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "pistol"})
    assert response.status_code == 200
    body = response.json()
    validate(body, register_user)


def test_unsuccessful_user_registration():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "sydney@fife"})
    assert response.status_code == 400
    body = response.json()
    validate(body, error_register_user)


def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")
    if response.text != "":
        raise AssertionError("Response not empty!")
    assert response.status_code == 204
