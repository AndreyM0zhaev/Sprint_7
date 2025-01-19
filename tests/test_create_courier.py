import requests
import allure

from endpoints import Endpoint
from constants import Constants

from data_user import registration_new_courier as new
from data_user import registration_new_courier_without_login as new_without_login
from data_user import registration_new_courier_without_login as new_without_password


class TestCreateCourier:
    data = new()

    @allure.title('Создание курьера, запрос возвращает правильный код ответа, успешный запрос возвращает {"ok":true}')
    def test_create_courier(self):
        response_body = '{"ok":true}'
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', TestCreateCourier.data)

        assert response.status_code == 201 and response.text == response_body


    @allure.title('Запрос создания двух одинаковых курьеров, если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_courier_was_created(self):
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', TestCreateCourier.data)

        assert response.status_code == 409 and 'Этот логин уже используется' in response.text


    @allure.title('Запрос создания курьера без логина, если поля нет, запрос возвращает ошибку')
    def test_create_courier_without_login(self):
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', new_without_login())

        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text


    @allure.title('Запрос создания курьера без пароля, если поля нет, запрос возвращает ошибку')
    def test_create_courier_without_password(self):
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', new_without_password())

        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text
