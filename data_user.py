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
