import requests
import allure

from endpoints import Endpoint
from constants import Constants

from data_user import registration_new_courier as new_reg
from data_user import registration_new_courier_without_login as new_reg_without_login
from data_user import registration_new_courier_without_password as new_reg_without_password



class TestCreateCourier:
    data = new_reg()
    courier_id = None


    @allure.title('Успешное создание учетной записи')
    @allure.description('Проверка, что курьер успешно создаётся при корректных данных')
    def test_create_courier(self):
        with allure.step('Создание курьера'):
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', TestCreateCourier.data)
            allure.attach(f'Запрос: {TestCreateCourier.data}', name='Request Body', attachment_type=allure.attachment_type.TEXT)
            allure.attach(f'Ответ: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и тела ответа'):
            assert response.status_code == 201
            assert response.json() == {"ok": True}

        TestCreateCourier.courier_id = self.get_courier_id(TestCreateCourier.data['login'], TestCreateCourier.data['password'])

    def get_courier_id(self, login, password):
        with allure.step('Получение ID курьера'):
            credentials = {
                "login": login,
                "password": password
            }
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.LOGIN_COURIER}', json=credentials)
            allure.attach(f'Запрос: {credentials}', name='Request Body', attachment_type=allure.attachment_type.TEXT)
            allure.attach(f'Ответ: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

            assert response.status_code == 200
            return response.json()['id']


    @allure.title('Запрос с повторяющимся логином')
    @allure.description('Проверка, что нельзя создать курьера с уже существующим логином')
    def test_create_courier_duplicate(self):
        with allure.step('Создание курьера с повторяющимся логином'):
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', TestCreateCourier.data)
            allure.attach(f'Запрос: {TestCreateCourier.data}', name='Request Body', attachment_type=allure.attachment_type.TEXT)
            allure.attach(f'Ответ: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert response.status_code == 409
            assert 'Этот логин уже используется' in response.text


    @allure.title('Запрос создания курьера без логина')
    @allure.description('Проверка, что нельзя создать курьера без указания логина')
    def test_create_courier_without_login(self):
        with allure.step('Создание курьера без логина'):
            data = new_reg_without_login()
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', data)
            allure.attach(f'Запрос: {data}', name='Request Body', attachment_type=allure.attachment_type.TEXT)
            allure.attach(f'Ответ: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert response.status_code == 400
            assert 'Недостаточно данных для создания учетной записи' in response.text


    @allure.title('Запрос создания курьера без пароля')
    @allure.description('Проверка, что нельзя создать курьера без указания пароля')
    def test_create_courier_without_password(self):
        with allure.step('Создание курьера без пароля'):
            data = new_reg_without_password()
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_COURIER}', data)
            allure.attach(f'Запрос: {data}', name='Request Body', attachment_type=allure.attachment_type.TEXT)
            allure.attach(f'Ответ: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и сообщения об ошибке'):
            assert response.status_code == 400
            assert 'Недостаточно данных для создания учетной записи' in response.text


    @allure.title('Удаление курьера')
    @allure.description('Проверка, что курьер успешно удаляется')
    def test_delete_courier(self):
        if TestCreateCourier.courier_id is not None:
            with allure.step('Удаление курьера'):
                response = requests.delete(f'{Constants.BASE_URL}{Endpoint.DELETE_COURIER}/{TestCreateCourier.courier_id}')
                allure.attach(f'Запрос: DELETE {Endpoint.DELETE_COURIER}/{TestCreateCourier.courier_id}', name='Request', attachment_type=allure.attachment_type.TEXT)
                allure.attach(f'Ответ: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

            with allure.step('Проверка кода ответа и тела ответа'):
                assert response.status_code == 200
                assert response.json() == {"ok": True}
        else:
            allure.attach('Курьер не был создан, удаление невозможно', name='Info', attachment_type=allure.attachment_type.TEXT)
            assert False, "Курьер не был создан, удаление невозможно"
