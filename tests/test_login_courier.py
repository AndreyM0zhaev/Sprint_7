import requests
import pytest
import allure

from endpoints import Endpoint
from constants import Constants
from data_user import User


class TestLoginCourier:
    @allure.title('Аутентификация с существующей парой логин-пароль')
    @allure.description('Проверка успешной аутентификации с корректными данными')
    def test_login_current_user(self):
        with allure.step('Подготовка данных для аутентификации'):
            allure.attach(f'Данные для входа: {User.current_user}', name='Request Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Отправка запроса на аутентификацию'):
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}', data=User.current_user)
            allure.attach(f'Ответ сервера: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и наличия поля "id"'):
            assert response.status_code == 200
            assert 'id' in response.text

    @allure.title('Аутентификация с несуществующей парой логин-пароль')
    @allure.description('Проверка ошибки при аутентификации с некорректными данными')
    def test_not_reg_user(self):
        with allure.step('Подготовка данных для аутентификации'):
            allure.attach(f'Данные для входа: {User.not_reg_user}', name='Request Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Отправка запроса на аутентификацию'):
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}', data=User.not_reg_user)
            allure.attach(f'Ответ сервера: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert response.status_code == 404
            assert 'Учетная запись не найдена' in response.text

    @pytest.mark.parametrize('auth_without_login_or_password', [User.auth_without_login, User.auth_without_password])
    @allure.title('Аутентификация без логина или пароля')
    @allure.description('Проверка ошибки при аутентификации без логина или пароля')
    def test_login_courier_with_incomplete_data(self, auth_without_login_or_password):
        with allure.step('Подготовка данных для аутентификации'):
            allure.attach(f'Данные для входа: {auth_without_login_or_password}', name='Request Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Отправка запроса на аутентификацию'):
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}', data=auth_without_login_or_password)
            allure.attach(f'Ответ сервера: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert response.status_code == 400
            assert 'Недостаточно данных для входа' in response.text
