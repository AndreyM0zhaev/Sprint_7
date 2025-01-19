from faker import Faker

faker = Faker()

def registration_new_courier():
    login = faker.user_name()
    password = faker.password()
    firstName = faker.name()
    user_data = {"login": login, "password": password, "name": firstName}
    return user_data

def registration_new_courier_without_login():
    login = faker.user_name()
    firstName = faker.name()
    user_data = {"login": login, "name": firstName}
    return user_data

def registration_new_courier_without_password():
    password = faker.password()
    firstName = faker.name()
    user_data = {"password": password, "name": firstName}
    return user_data


class User:
    current_user = {
        "login": "Andre",
        "password": "1234"
    }
    not_reg_user = {
        "login": "зло не дремлет",
        "password": "666"
    }
    auth_without_login = {
        "login": "",
        "password": "1234"
    }
    auth_without_password = {
        "login": "Andre",
        "password": ""
    }

class Order:
    data_user_order = {
        "firstName": "Andre",
        "lastName": "Ali",
        "address": "Minsk, Lomonosov str.",
        "metroStation": 1,
        "phone": "+375 25 135 79 01",
        "rentTime": 3,
        "deliveryDate": "2025-01-27",
        "comment": "I need more ...",
        "color": [
            "BLACK"
        ]
    }
