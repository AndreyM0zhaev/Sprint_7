import requests
import pytest
import allure
import json

from endpoints import Endpoint
from constants import Constants
from data_user import Order

class TestCreateOrder:

    @pytest.mark.parametrize('order_data', [{"color": ["GREY"]}, {"color": ["BLACK"]}, {"color": ["BLACK", "GREY"]}, {"color": [""]}])
    @allure.title('Успешное создание заказа')
    def test_create_order(self, order_data):
        Order.data_user_order.update(order_data)
        order_data = json.dumps(Order.data_user_order)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{Constants.BASE_URL}{Endpoint.CREATE_ORDER}', data=order_data, headers=headers)

        assert response.status_code == 201 and 'track' in response.text