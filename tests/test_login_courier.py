import requests
import pytest
import allure

from endpoints import Endpoint
from constants import Constants
from data_user import User


class TestLoginCourier:

    @allure.title('Аутентификация с существующей парой логин-пароль')
    def test_login_current_user(self):
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}', data=User.current_user)

        assert response.status_code == 200 and 'id' in response.text


    @allure.title('Аутентификация с несуществующей парой логин-пароль')
    def test_not_reg_user(self):
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}', data=User.not_reg_user)

        assert response.status_code == 404 and 'Учетная запись не найдена' in response.text


    @pytest.mark.parametrize('auth_without_login_or_password', [User.auth_without_login, User.auth_without_password])
    @allure.title('Аутентификация без логина или пароля')
    def test_login_courier_with_incomplete_data(self, auth_without_login_or_password):
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}',data=auth_without_login_or_password)

        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.text
