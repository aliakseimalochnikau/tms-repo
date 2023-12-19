from datetime import datetime
import pytest
import requests
from homework.lesson_26.data_generator import generated_data


class PetStore:
    HOST = "https://petstore.swagger.io/v2"
    USER = "/user"
    USER_USERNAME = "/user/{username}"


@pytest.fixture
def user_data():
    new_user = next(generated_data())
    data = {
        "id": int(datetime.now().timestamp()),
        "username": new_user.username,
        "firstName": new_user.first_name,
        "lastName": new_user.last_name,
        "email": new_user.email,
        "password": new_user.password,
        "phone": new_user.phone_number,
        "userStatus": 0
    }
    return data


# Actions
def create_user(user_data):
    url = f"{PetStore.HOST}{PetStore.USER}"
    response = requests.post(url, json=user_data)
    return response


def read_user(user_data):
    url = f"{PetStore.HOST}{PetStore.USER_USERNAME.format(username=user_data["username"])}"
    response = requests.get(url)
    return response


def update_user(user_data, json_data):
    url = f"{PetStore.HOST}{PetStore.USER_USERNAME.format(username=user_data["username"])}"
    response = requests.put(url, json=json_data)
    return response


def delete_user(user_data):
    url = f"{PetStore.HOST}{PetStore.USER_USERNAME.format(username=user_data["username"])}"
    response = requests.delete(url)
    return response


# Assertions
def response_is_ok(response):
    assert response.ok, f"{response.status_code =}"


def assert_username(response, expected_username):
    json_data = response.json()
    assert json_data["username"] == expected_username, f'{json_data["username"] =}'


def assert_full_name(response, expected_first_name, expected_last_name):
    json_data = response.json()
    assert json_data["firstName"] == expected_first_name, f'{json_data["firstName"] =}'
    assert json_data["lastName"] == expected_last_name, f'{json_data["firstName"] =}'


def assert_message(response, expected_message):
    json_data = response.json()
    assert json_data["message"] == str(expected_message), f'{json_data["message"] =}'


class TestUser:
    def test_create_user(self, user_data):
        # Create a new user
        create_response = create_user(user_data)
        response_is_ok(create_response)

        # Assert user is created
        assert_message(create_response, user_data["id"])

    def test_read_user(self, user_data):
        # Create a new user
        create_response = create_user(user_data)
        response_is_ok(create_response)
        assert_message(create_response, user_data["id"])

        # Get created user
        read_response = read_user(user_data)
        response_is_ok(read_response)

        # Assert
        assert_username(read_response, user_data["username"])

    def test_update_user(self, user_data):
        # Create a new user
        create_response = create_user(user_data)
        response_is_ok(create_response)
        assert_message(create_response, user_data["id"])

        # Get created user
        read_response = read_user(user_data)
        response_is_ok(read_response)
        assert_full_name(read_response, user_data["firstName"], user_data["lastName"])

        # Update created user
        json_data = read_response.json()
        new_first_name = "Adam"
        new_last_name = "Jensen"
        json_data["firstName"] = new_first_name
        json_data["lastName"] = new_last_name
        update_response = update_user(user_data, json_data=json_data)
        response_is_ok(update_response)

        # Assert via getting updated user
        read_response = read_user(user_data)
        response_is_ok(read_response)
        assert_full_name(read_response, new_first_name, new_last_name)

    def test_delete_user(self, user_data):
        # Create a new user
        create_response = create_user(user_data)
        response_is_ok(create_response)
        assert_message(create_response, user_data["id"])

        # Get created user
        read_response = read_user(user_data)
        response_is_ok(read_response)
        assert_username(read_response, user_data["username"])

        # Delete created user
        delete_response = delete_user(user_data)
        response_is_ok(delete_response)
        assert_message(delete_response, user_data["username"])

        # Assert via getting deleted user
        read_response = read_user(user_data)
        assert_message(read_response, "User not found")
