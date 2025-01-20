import requests
import pytest
import allure
import json

from endpoints import Endpoint
from constants import Constants
from data_user import Order


class TestCreateOrder:
    @pytest.mark.parametrize('order_data', [
        {"color": ["GREY"]},
        {"color": ["BLACK"]},
        {"color": ["BLACK", "GREY"]},
        {"color": [""]}
    ])
    @allure.title('Успешное создание заказа')
    @allure.description('Проверка создания заказа с различными комбинациями цветов')
    def test_create_order(self, order_data):
        with allure.step('Подготовка данных для заказа'):
            Order.data_user_order.update(order_data)
            order_data_json = json.dumps(Order.data_user_order)
            headers = {'Content-Type': 'application/json'}
            allure.attach(f'Данные заказа: {order_data_json}', name='Request Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Отправка запроса на создание заказа'):
            response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_ORDER}', data=order_data_json, headers=headers)
            allure.attach(f'Ответ сервера: {response.text}', name='Response Body', attachment_type=allure.attachment_type.TEXT)

        with allure.step('Проверка кода ответа и наличия поля "track"'):
            assert response.status_code == 201
            assert 'track' in response.text